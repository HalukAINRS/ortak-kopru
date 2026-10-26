#include <ntddk.h>
#include <wdf.h>
#include "deus_protocol.h"

DRIVER_INITIALIZE DriverEntry;
EVT_WDF_DRIVER_UNLOAD DeusEvtDriverUnload;
EVT_WDF_IO_QUEUE_IO_DEVICE_CONTROL DeusEvtIoDeviceControl;

C_ASSERT(sizeof(DEUS_QUERY_REQUEST) == 16);
C_ASSERT(sizeof(DEUS_QUERY_RESPONSE) == 32);

/* A non-PnP control device is the NT-kernel endpoint. The first protocol
 * exposes only a bounded query: no pointers, process access, executable
 * content, filesystem writes, or model/credential payloads cross this ABI.
 */
NTSTATUS
DriverEntry(PDRIVER_OBJECT DriverObject, PUNICODE_STRING RegistryPath)
{
    NTSTATUS status;
    WDF_DRIVER_CONFIG config;
    WDFDRIVER driver;
    PWDFDEVICE_INIT deviceInit = NULL;
    WDFDEVICE device;
    WDF_OBJECT_ATTRIBUTES attributes;
    WDF_IO_QUEUE_CONFIG queueConfig;
    DECLARE_CONST_UNICODE_STRING(deviceName, L"\\Device\\DeusExMachina");
    DECLARE_CONST_UNICODE_STRING(symbolicLink, L"\\DosDevices\\Global\\DeusExMachina");
    DECLARE_CONST_UNICODE_STRING(sddl, L"D:P(A;;GA;;;SY)(A;;GA;;;BA)");

    WDF_DRIVER_CONFIG_INIT(&config, WDF_NO_EVENT_CALLBACK);
    config.DriverInitFlags |= WdfDriverInitNonPnpDriver;
    config.EvtDriverUnload = DeusEvtDriverUnload;
    status = WdfDriverCreate(DriverObject, RegistryPath,
                            WDF_NO_OBJECT_ATTRIBUTES, &config, &driver);
    if (!NT_SUCCESS(status)) {
        return status;
    }

    deviceInit = WdfControlDeviceInitAllocate(driver, &sddl);
    if (deviceInit == NULL) {
        return STATUS_INSUFFICIENT_RESOURCES;
    }
    WdfDeviceInitSetDeviceType(deviceInit, DEUS_DEVICE_TYPE);
    WdfDeviceInitSetCharacteristics(deviceInit, FILE_DEVICE_SECURE_OPEN, FALSE);
    WdfDeviceInitSetIoType(deviceInit, WdfDeviceIoBuffered);
    WdfDeviceInitSetExclusive(deviceInit, FALSE);
    status = WdfDeviceInitAssignName(deviceInit, &deviceName);
    if (!NT_SUCCESS(status)) {
        WdfDeviceInitFree(deviceInit);
        return status;
    }

    WDF_OBJECT_ATTRIBUTES_INIT(&attributes);
    attributes.ExecutionLevel = WdfExecutionLevelPassive;
    status = WdfDeviceCreate(&deviceInit, &attributes, &device);
    if (!NT_SUCCESS(status)) {
        if (deviceInit != NULL) {
            WdfDeviceInitFree(deviceInit);
        }
        return status;
    }
    status = WdfDeviceCreateSymbolicLink(device, &symbolicLink);
    if (!NT_SUCCESS(status)) {
        return status;
    }
    WDF_IO_QUEUE_CONFIG_INIT_DEFAULT_QUEUE(&queueConfig, WdfIoQueueDispatchParallel);
    queueConfig.PowerManaged = WdfFalse;
    queueConfig.EvtIoDeviceControl = DeusEvtIoDeviceControl;
    status = WdfIoQueueCreate(device, &queueConfig, WDF_NO_OBJECT_ATTRIBUTES,
                             WDF_NO_HANDLE);
    if (!NT_SUCCESS(status)) {
        return status;
    }
    WdfControlFinishInitializing(device);
    return STATUS_SUCCESS;
}

VOID
DeusEvtDriverUnload(WDFDRIVER Driver)
{
    /* WDF owns and releases the control device, queue and symbolic link. */
    UNREFERENCED_PARAMETER(Driver);
}

VOID
DeusEvtIoDeviceControl(WDFQUEUE Queue, WDFREQUEST Request,
                      size_t OutputBufferLength, size_t InputBufferLength,
                      ULONG IoControlCode)
{
    NTSTATUS status;
    PDEUS_QUERY_REQUEST input;
    PDEUS_QUERY_RESPONSE output;
    ULONGLONG nonce;

    UNREFERENCED_PARAMETER(Queue);
    if (IoControlCode != IOCTL_DEUS_QUERY) {
        WdfRequestComplete(Request, STATUS_INVALID_DEVICE_REQUEST);
        return;
    }
    if (InputBufferLength != sizeof(DEUS_QUERY_REQUEST) ||
        OutputBufferLength != sizeof(DEUS_QUERY_RESPONSE)) {
        WdfRequestComplete(Request, STATUS_INFO_LENGTH_MISMATCH);
        return;
    }
    status = WdfRequestRetrieveInputBuffer(Request, sizeof(DEUS_QUERY_REQUEST),
                                           (PVOID*)&input, NULL);
    if (!NT_SUCCESS(status)) {
        WdfRequestComplete(Request, status);
        return;
    }
    if (input->Size != sizeof(DEUS_QUERY_REQUEST) ||
        input->ProtocolVersion != DEUS_PROTOCOL_VERSION) {
        WdfRequestComplete(Request, STATUS_REVISION_MISMATCH);
        return;
    }
    /* METHOD_BUFFERED shares input/output storage. Copy input before writing. */
    nonce = input->Nonce;
    status = WdfRequestRetrieveOutputBuffer(Request, sizeof(DEUS_QUERY_RESPONSE),
                                            (PVOID*)&output, NULL);
    if (!NT_SUCCESS(status)) {
        WdfRequestComplete(Request, status);
        return;
    }
    RtlZeroMemory(output, sizeof(*output));
    output->Size = sizeof(*output);
    output->Magic = DEUS_PROTOCOL_MAGIC;
    output->ProtocolVersion = DEUS_PROTOCOL_VERSION;
    output->Capabilities = DEUS_CAP_QUERY;
    output->Nonce = nonce;
    output->InterruptTime100ns = KeQueryInterruptTime();
    WdfRequestCompleteWithInformation(Request, STATUS_SUCCESS, sizeof(*output));
}
