"""Protocol tests use a fake transport; they never load or install a driver."""
from pathlib import Path
import struct
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ortak_kopru.adapters import windows_nt as nt


class NtProtocolTests(unittest.TestCase):
    def test_known_wire_response_is_accepted_with_narrow_claim(self):
        # Independently specified protocol-1 packet, including echoed nonce.
        packet = bytes.fromhex(
            "20000000 44455553 01000000 01000000 "
            "0807060504030201 6400000000000000"
        )
        decoded = nt.decode_response(packet, 0x0102030405060708)
        self.assertEqual(decoded["interrupt_time_100ns"], 100)
        self.assertEqual(decoded["verified_scope"], "device-protocol")
        self.assertEqual(decoded["task_execution"], "user-mode")
        self.assertFalse(decoded["supervision_available"])

    def test_malformed_foreign_or_extended_responses_are_rejected(self):
        valid = [32, 0x53554544, 1, 1, 123, 100]
        variants = [b"", b"x" * 31, b"x" * 33]
        for position, value in ((0, 0), (1, 0), (2, 2), (3, 0), (3, 3), (4, 456)):
            fields = valid.copy()
            fields[position] = value
            variants.append(struct.pack("<IIIIQQ", *fields))
        for payload in variants:
            with self.subTest(payload=payload.hex()):
                with self.assertRaises(nt.KernelUnavailable) as error:
                    nt.decode_response(payload, 123)
                self.assertEqual(error.exception.state, "protocol-error")

    def test_probe_requires_this_request_nonce(self):
        seen = []
        def transport(payload):
            size, version, nonce = struct.unpack("<IIQ", payload)
            seen.append((size, version, nonce))
            return struct.pack("<IIIIQQ", 32, 0x53554544, 1, 1, nonce, 700)
        with patch.object(nt, "_exchange", side_effect=transport), patch.object(nt.secrets, "randbits", return_value=42):
            state = nt.query_status(strict=True)
        self.assertEqual(seen, [(16, 1, 42)])
        self.assertTrue(state["ready"])
        self.assertEqual(state["state"], "verified")
        self.assertEqual(state["backend"], "nt-kernel")

    def test_non_windows_never_uses_driver_or_reports_ready(self):
        with patch.object(nt.sys, "platform", "linux"):
            state = nt.query_status()
            with self.assertRaises(nt.KernelUnavailable):
                nt.query_status(strict=True)
        self.assertFalse(state["ready"])
        self.assertEqual(state["state"], "unsupported")
        self.assertNotIn("protocol_version", state)

    def test_missing_driver_does_not_fall_back_to_portable(self):
        error = nt.KernelUnavailable("NT aygıtı açılamadı (Windows hata 2).", winerror=2)
        with patch.object(nt, "_exchange", side_effect=error):
            state = nt.query_status()
            with self.assertRaises(nt.KernelUnavailable):
                nt.query_status(strict=True)
        self.assertEqual(state["backend"], "nt-kernel")
        self.assertEqual(state["state"], "unavailable")
        self.assertEqual(state["winerror"], 2)
        self.assertFalse(state["ready"])

    def test_protocol_mismatch_is_not_a_successful_kernel_probe(self):
        with patch.object(nt, "_exchange", return_value=b"not the expected driver"):
            state = nt.query_status()
        self.assertEqual(state["state"], "protocol-error")
        self.assertFalse(state["ready"])


if __name__ == "__main__":
    unittest.main()
