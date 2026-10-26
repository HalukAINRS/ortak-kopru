#pragma once

/* Protocol 1: fixed-size, pointer-free, read-only kernel presence query.
 * This header is consumed after ntddk.h by the driver. All wire integers
 * are little endian; the 64-bit fields have the same layout on x64/ARM64.
 */
#define DEUS_DEVICE_TYPE 0x8000
#define DEUS_PROTOCOL_VERSION 1
#define DEUS_PROTOCOL_MAGIC 0x53554544 /* ASCII DEUS, little endian */
#define DEUS_CAP_QUERY 0x00000001
#define IOCTL_DEUS_QUERY CTL_CODE(DEUS_DEVICE_TYPE, 0x800, METHOD_BUFFERED, FILE_READ_DATA)

#pragma pack(push, 8)
typedef struct _DEUS_QUERY_REQUEST {
    ULONG Size;
    ULONG ProtocolVersion;
    ULONGLONG Nonce;
} DEUS_QUERY_REQUEST, *PDEUS_QUERY_REQUEST;

typedef struct _DEUS_QUERY_RESPONSE {
    ULONG Size;
    ULONG Magic;
    ULONG ProtocolVersion;
    ULONG Capabilities;
    ULONGLONG Nonce;
    ULONGLONG InterruptTime100ns;
} DEUS_QUERY_RESPONSE, *PDEUS_QUERY_RESPONSE;
#pragma pack(pop)
