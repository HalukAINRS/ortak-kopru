"""Read the real Deus KMDF control device, without installing or loading it.

Protocol presence is deliberately narrower than job execution or supervision.
There is no automatic software fallback and no arbitrary-device parameter.
"""
from __future__ import annotations

import ctypes
import datetime as dt
import secrets
import struct
import sys

DEVICE = r"\\.\DeusExMachina"
PROTOCOL_VERSION = 1
MAGIC = 0x53554544
CAP_QUERY = 0x00000001
# CTL_CODE(0x8000, 0x800, METHOD_BUFFERED, FILE_READ_DATA)
IOCTL_QUERY = 0x80006000
REQUEST = struct.Struct("<IIQ")
RESPONSE = struct.Struct("<IIIIQQ")


class KernelUnavailable(RuntimeError):
    """The required NT endpoint could not be verified."""

    def __init__(self, message: str, *, state: str = "unavailable", winerror: int | None = None):
        super().__init__(message)
        self.state = state
        self.winerror = winerror


def decode_response(payload: bytes, expected_nonce: int) -> dict:
    """Validate exact ABI/nonce/capabilities; no partial or guessed success."""
    if len(payload) != RESPONSE.size:
        raise KernelUnavailable("NT sürücü yanıtının boyutu protokolle uyuşmuyor.", state="protocol-error")
    size, magic, version, capabilities, nonce, interrupt_time = RESPONSE.unpack(payload)
    if size != RESPONSE.size or magic != MAGIC or version != PROTOCOL_VERSION:
        raise KernelUnavailable("NT sürücü protokolü bu istemciyle uyumlu değil.", state="protocol-error")
    if capabilities != CAP_QUERY:
        raise KernelUnavailable("NT sürücünün yetenek bildirimi desteklenmiyor.", state="protocol-error")
    if nonce != expected_nonce:
        raise KernelUnavailable("NT sürücü yanıtı bu sorguya ait değil.", state="protocol-error")
    return {
        "protocol_version": version,
        "capabilities": ["query"],
        "interrupt_time_100ns": interrupt_time,
        "verified_scope": "device-protocol",
        "task_execution": "user-mode",
        "supervision_available": False,
    }


def _exchange(request: bytes) -> bytes:
    if sys.platform != "win32":
        raise KernelUnavailable("NT Kernel aygıtı yalnız Windows üzerinde sorgulanabilir.", state="unsupported")

    # Fixed-width DWORDs keep the ABI explicit. HANDLE uses pointer width.
    dword = ctypes.c_uint32
    handle_type = ctypes.c_void_p
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.CreateFileW.argtypes = [ctypes.c_wchar_p, dword, dword, ctypes.c_void_p,
                                   dword, dword, handle_type]
    kernel32.CreateFileW.restype = handle_type
    kernel32.DeviceIoControl.argtypes = [handle_type, dword, ctypes.c_void_p, dword,
                                        ctypes.c_void_p, dword,
                                        ctypes.POINTER(dword), ctypes.c_void_p]
    kernel32.DeviceIoControl.restype = ctypes.c_int
    kernel32.CloseHandle.argtypes = [handle_type]
    kernel32.CloseHandle.restype = ctypes.c_int

    # Read access, shared probe handles, OPEN_EXISTING. No service mutation.
    handle = kernel32.CreateFileW(DEVICE, 0x80000000, 3, None, 3, 0, None)
    if handle is None or handle == ctypes.c_void_p(-1).value:
        code = ctypes.get_last_error()
        raise KernelUnavailable(f"NT aygıtı açılamadı (Windows hata {code}).", winerror=code)
    try:
        input_buffer = ctypes.create_string_buffer(request, len(request))
        output_buffer = ctypes.create_string_buffer(RESPONSE.size)
        returned = dword()
        success = kernel32.DeviceIoControl(
            handle, IOCTL_QUERY, input_buffer, len(request), output_buffer,
            RESPONSE.size, ctypes.byref(returned), None,
        )
        if not success:
            code = ctypes.get_last_error()
            raise KernelUnavailable(f"NT aygıtı sorgulanamadı (Windows hata {code}).", winerror=code)
        if returned.value > RESPONSE.size:
            raise KernelUnavailable("NT aygıtı geçersiz yanıt uzunluğu bildirdi.", state="protocol-error")
        return output_buffer.raw[:returned.value]
    finally:
        kernel32.CloseHandle(handle)


def query_status(*, strict: bool = False) -> dict:
    """Probe only. strict=True raises instead of returning any non-ready state."""
    result = {
        "backend": "nt-kernel", "ready": False, "state": "unavailable",
        "device": DEVICE, "probed_at": dt.datetime.now(dt.UTC).isoformat(),
    }
    try:
        nonce = secrets.randbits(64)
        response = _exchange(REQUEST.pack(REQUEST.size, PROTOCOL_VERSION, nonce))
        result.update(decode_response(response, nonce))
    except KernelUnavailable as exc:
        if strict:
            raise
        result.update(state=exc.state, error=str(exc))
        if exc.winerror is not None:
            result["winerror"] = exc.winerror
        return result
    except OSError as exc:
        error = KernelUnavailable("Windows aygıt bağlantısı kurulamadı.", winerror=getattr(exc, "winerror", None))
        if strict:
            raise error from exc
        result.update(error=str(error))
        if error.winerror is not None:
            result["winerror"] = error.winerror
        return result
    result.update(ready=True, state="verified")
    return result
