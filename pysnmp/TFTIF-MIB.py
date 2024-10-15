# SNMP MIB module (TFTIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TFTIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:29 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

(mcmSysAsciiTimeOfDay,) = mibBuilder.importSymbols(
    "MICOM-SYS-MIB",
    "mcmSysAsciiTimeOfDay")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MemAddress(OctetString):
    """Custom type MemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_McmTFTP_ObjectIdentity = ObjectIdentity
mcmTFTP = _McmTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3)
)
_McmTFTPParamGroup_ObjectIdentity = ObjectIdentity
mcmTFTPParamGroup = _McmTFTPParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 1)
)
_McmTFTPServerIpAddr_Type = IpAddress
_McmTFTPServerIpAddr_Object = MibScalar
mcmTFTPServerIpAddr = _McmTFTPServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 1, 1),
    _McmTFTPServerIpAddr_Type()
)
mcmTFTPServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmTFTPServerIpAddr.setStatus("mandatory")
_McmTFTPFileName_Type = DisplayString
_McmTFTPFileName_Object = MibScalar
mcmTFTPFileName = _McmTFTPFileName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 1, 2),
    _McmTFTPFileName_Type()
)
mcmTFTPFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmTFTPFileName.setStatus("mandatory")


class _McmTFTPTimeOut_Type(Integer32):
    """Custom type mcmTFTPTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_McmTFTPTimeOut_Type.__name__ = "Integer32"
_McmTFTPTimeOut_Object = MibScalar
mcmTFTPTimeOut = _McmTFTPTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 1, 3),
    _McmTFTPTimeOut_Type()
)
mcmTFTPTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmTFTPTimeOut.setStatus("mandatory")


class _McmTFTPRetransmissions_Type(Integer32):
    """Custom type mcmTFTPRetransmissions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_McmTFTPRetransmissions_Type.__name__ = "Integer32"
_McmTFTPRetransmissions_Object = MibScalar
mcmTFTPRetransmissions = _McmTFTPRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 1, 4),
    _McmTFTPRetransmissions_Type()
)
mcmTFTPRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmTFTPRetransmissions.setStatus("mandatory")


class _McmTFTPDownload_Type(Integer32):
    """Custom type mcmTFTPDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 5),
          ("dnldDefault", 3),
          ("dnldSpecific", 4),
          ("upldDefault", 1),
          ("upldSpecific", 2))
    )


_McmTFTPDownload_Type.__name__ = "Integer32"
_McmTFTPDownload_Object = MibScalar
mcmTFTPDownload = _McmTFTPDownload_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 1, 5),
    _McmTFTPDownload_Type()
)
mcmTFTPDownload.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmTFTPDownload.setStatus("deprecated")


class _McmTFTPStart_Type(Integer32):
    """Custom type mcmTFTPStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 5),
          ("dnldDefault", 3),
          ("dnldSpecific", 4),
          ("upldDefault", 1),
          ("upldSpecific", 2))
    )


_McmTFTPStart_Type.__name__ = "Integer32"
_McmTFTPStart_Object = MibScalar
mcmTFTPStart = _McmTFTPStart_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 1, 6),
    _McmTFTPStart_Type()
)
mcmTFTPStart.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmTFTPStart.setStatus("mandatory")


class _McmTFTPPortNumber_Type(Integer32):
    """Custom type mcmTFTPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_McmTFTPPortNumber_Type.__name__ = "Integer32"
_McmTFTPPortNumber_Object = MibScalar
mcmTFTPPortNumber = _McmTFTPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 1, 7),
    _McmTFTPPortNumber_Type()
)
mcmTFTPPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmTFTPPortNumber.setStatus("mandatory")


class _McmTFTPConfigUploadBank_Type(Integer32):
    """Custom type mcmTFTPConfigUploadBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bank3", 1),
          ("bank4", 2))
    )


_McmTFTPConfigUploadBank_Type.__name__ = "Integer32"
_McmTFTPConfigUploadBank_Object = MibScalar
mcmTFTPConfigUploadBank = _McmTFTPConfigUploadBank_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 1, 8),
    _McmTFTPConfigUploadBank_Type()
)
mcmTFTPConfigUploadBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmTFTPConfigUploadBank.setStatus("mandatory")
_NvmTFTPParamGroup_ObjectIdentity = ObjectIdentity
nvmTFTPParamGroup = _NvmTFTPParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 2)
)
_NvmTFTPServerIpAddr_Type = IpAddress
_NvmTFTPServerIpAddr_Object = MibScalar
nvmTFTPServerIpAddr = _NvmTFTPServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 2, 1),
    _NvmTFTPServerIpAddr_Type()
)
nvmTFTPServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmTFTPServerIpAddr.setStatus("mandatory")
_NvmTFTPFileName_Type = DisplayString
_NvmTFTPFileName_Object = MibScalar
nvmTFTPFileName = _NvmTFTPFileName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 2, 2),
    _NvmTFTPFileName_Type()
)
nvmTFTPFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmTFTPFileName.setStatus("mandatory")
_NvmTFTPTimeOut_Type = Integer32
_NvmTFTPTimeOut_Object = MibScalar
nvmTFTPTimeOut = _NvmTFTPTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 2, 3),
    _NvmTFTPTimeOut_Type()
)
nvmTFTPTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmTFTPTimeOut.setStatus("mandatory")
_NvmTFTPRetransmissions_Type = Integer32
_NvmTFTPRetransmissions_Object = MibScalar
nvmTFTPRetransmissions = _NvmTFTPRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 2, 4),
    _NvmTFTPRetransmissions_Type()
)
nvmTFTPRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmTFTPRetransmissions.setStatus("mandatory")


class _NvmTFTPPortNumber_Type(Integer32):
    """Custom type nvmTFTPPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NvmTFTPPortNumber_Type.__name__ = "Integer32"
_NvmTFTPPortNumber_Object = MibScalar
nvmTFTPPortNumber = _NvmTFTPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 2, 5),
    _NvmTFTPPortNumber_Type()
)
nvmTFTPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmTFTPPortNumber.setStatus("mandatory")


class _NvmTFTPConfigUploadBank_Type(Integer32):
    """Custom type nvmTFTPConfigUploadBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bank3", 1),
          ("bank4", 2))
    )


_NvmTFTPConfigUploadBank_Type.__name__ = "Integer32"
_NvmTFTPConfigUploadBank_Object = MibScalar
nvmTFTPConfigUploadBank = _NvmTFTPConfigUploadBank_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 2, 6),
    _NvmTFTPConfigUploadBank_Type()
)
nvmTFTPConfigUploadBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmTFTPConfigUploadBank.setStatus("mandatory")
_McmTFTPStatusGroup_ObjectIdentity = ObjectIdentity
mcmTFTPStatusGroup = _McmTFTPStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 3)
)


class _McmTFTPCurrentState_Type(Integer32):
    """Custom type mcmTFTPCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("retrieving-file", 2))
    )


_McmTFTPCurrentState_Type.__name__ = "Integer32"
_McmTFTPCurrentState_Object = MibScalar
mcmTFTPCurrentState = _McmTFTPCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 3, 1),
    _McmTFTPCurrentState_Type()
)
mcmTFTPCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTFTPCurrentState.setStatus("mandatory")
_McmTFTPErrorStatusGroup_ObjectIdentity = ObjectIdentity
mcmTFTPErrorStatusGroup = _McmTFTPErrorStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 4)
)


class _McmTFTPLastErrorStatus_Type(Integer32):
    """Custom type mcmTFTPLastErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              11,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("bad-file", 18),
          ("chksum-error", 11),
          ("connection-error", 17),
          ("download-failed", 6),
          ("download-success", 2),
          ("flash-error", 5),
          ("idle", 1),
          ("out-of-memory", 4),
          ("protocol-error", 14),
          ("server-error", 15),
          ("timeout", 16),
          ("transferring-file", 13),
          ("upload-failed", 7),
          ("upload-success", 8))
    )


_McmTFTPLastErrorStatus_Type.__name__ = "Integer32"
_McmTFTPLastErrorStatus_Object = MibScalar
mcmTFTPLastErrorStatus = _McmTFTPLastErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 4, 1),
    _McmTFTPLastErrorStatus_Type()
)
mcmTFTPLastErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTFTPLastErrorStatus.setStatus("mandatory")
_McmTFTPLastServerIpAddr_Type = IpAddress
_McmTFTPLastServerIpAddr_Object = MibScalar
mcmTFTPLastServerIpAddr = _McmTFTPLastServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 4, 2),
    _McmTFTPLastServerIpAddr_Type()
)
mcmTFTPLastServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTFTPLastServerIpAddr.setStatus("mandatory")
_McmTFTPLastFileName_Type = DisplayString
_McmTFTPLastFileName_Object = MibScalar
mcmTFTPLastFileName = _McmTFTPLastFileName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 4, 3),
    _McmTFTPLastFileName_Type()
)
mcmTFTPLastFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTFTPLastFileName.setStatus("mandatory")


class _McmTFTPTransferBank_Type(Integer32):
    """Custom type mcmTFTPTransferBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("fromBank3", 7),
          ("fromBank4", 8),
          ("fromDebug", 9),
          ("none", 1),
          ("toBank1", 3),
          ("toBank2", 4),
          ("toBank3", 5),
          ("toBank4", 6),
          ("toboot", 2))
    )


_McmTFTPTransferBank_Type.__name__ = "Integer32"
_McmTFTPTransferBank_Object = MibScalar
mcmTFTPTransferBank = _McmTFTPTransferBank_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 4, 4),
    _McmTFTPTransferBank_Type()
)
mcmTFTPTransferBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTFTPTransferBank.setStatus("mandatory")


class _McmTFTPLastPortNumber_Type(Integer32):
    """Custom type mcmTFTPLastPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_McmTFTPLastPortNumber_Type.__name__ = "Integer32"
_McmTFTPLastPortNumber_Object = MibScalar
mcmTFTPLastPortNumber = _McmTFTPLastPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 4, 5),
    _McmTFTPLastPortNumber_Type()
)
mcmTFTPLastPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTFTPLastPortNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcmTFTPDownloadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 0, 1)
)
mcmTFTPDownloadFail.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("TFTIF-MIB", "mcmTFTPServerIpAddr"),
        ("TFTIF-MIB", "mcmTFTPFileName"))
)
if mibBuilder.loadTexts:
    mcmTFTPDownloadFail.setStatus(
        ""
    )

mcmTFTPUploadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 0, 2)
)
mcmTFTPUploadFail.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("TFTIF-MIB", "mcmTFTPServerIpAddr"),
        ("TFTIF-MIB", "mcmTFTPFileName"))
)
if mibBuilder.loadTexts:
    mcmTFTPUploadFail.setStatus(
        ""
    )

mcmTFTPDownloadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 0, 3)
)
mcmTFTPDownloadSuccess.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("TFTIF-MIB", "mcmTFTPServerIpAddr"),
        ("TFTIF-MIB", "mcmTFTPFileName"))
)
if mibBuilder.loadTexts:
    mcmTFTPDownloadSuccess.setStatus(
        ""
    )

mcmTFTPUploadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 3, 0, 4)
)
mcmTFTPUploadSuccess.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("TFTIF-MIB", "mcmTFTPServerIpAddr"),
        ("TFTIF-MIB", "mcmTFTPFileName"))
)
if mibBuilder.loadTexts:
    mcmTFTPUploadSuccess.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TFTIF-MIB",
    **{"MemAddress": MemAddress,
       "mcmTFTP": mcmTFTP,
       "mcmTFTPDownloadFail": mcmTFTPDownloadFail,
       "mcmTFTPUploadFail": mcmTFTPUploadFail,
       "mcmTFTPDownloadSuccess": mcmTFTPDownloadSuccess,
       "mcmTFTPUploadSuccess": mcmTFTPUploadSuccess,
       "mcmTFTPParamGroup": mcmTFTPParamGroup,
       "mcmTFTPServerIpAddr": mcmTFTPServerIpAddr,
       "mcmTFTPFileName": mcmTFTPFileName,
       "mcmTFTPTimeOut": mcmTFTPTimeOut,
       "mcmTFTPRetransmissions": mcmTFTPRetransmissions,
       "mcmTFTPDownload": mcmTFTPDownload,
       "mcmTFTPStart": mcmTFTPStart,
       "mcmTFTPPortNumber": mcmTFTPPortNumber,
       "mcmTFTPConfigUploadBank": mcmTFTPConfigUploadBank,
       "nvmTFTPParamGroup": nvmTFTPParamGroup,
       "nvmTFTPServerIpAddr": nvmTFTPServerIpAddr,
       "nvmTFTPFileName": nvmTFTPFileName,
       "nvmTFTPTimeOut": nvmTFTPTimeOut,
       "nvmTFTPRetransmissions": nvmTFTPRetransmissions,
       "nvmTFTPPortNumber": nvmTFTPPortNumber,
       "nvmTFTPConfigUploadBank": nvmTFTPConfigUploadBank,
       "mcmTFTPStatusGroup": mcmTFTPStatusGroup,
       "mcmTFTPCurrentState": mcmTFTPCurrentState,
       "mcmTFTPErrorStatusGroup": mcmTFTPErrorStatusGroup,
       "mcmTFTPLastErrorStatus": mcmTFTPLastErrorStatus,
       "mcmTFTPLastServerIpAddr": mcmTFTPLastServerIpAddr,
       "mcmTFTPLastFileName": mcmTFTPLastFileName,
       "mcmTFTPTransferBank": mcmTFTPTransferBank,
       "mcmTFTPLastPortNumber": mcmTFTPLastPortNumber}
)
