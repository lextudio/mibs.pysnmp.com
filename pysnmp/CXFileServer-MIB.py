# SNMP MIB module (CXFileServer-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXFileServer-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:25 2024
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

(cxFileServer,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxFileServer")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _CxFsTftpTransfer_Type(Integer32):
    """Custom type cxFsTftpTransfer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CxFsTftpTransfer_Type.__name__ = "Integer32"
_CxFsTftpTransfer_Object = MibScalar
cxFsTftpTransfer = _CxFsTftpTransfer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 1),
    _CxFsTftpTransfer_Type()
)
cxFsTftpTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFsTftpTransfer.setStatus("mandatory")


class _CxFsTftpTargetSlot_Type(Integer32):
    """Custom type cxFsTftpTargetSlot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CxFsTftpTargetSlot_Type.__name__ = "Integer32"
_CxFsTftpTargetSlot_Object = MibScalar
cxFsTftpTargetSlot = _CxFsTftpTargetSlot_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 2),
    _CxFsTftpTargetSlot_Type()
)
cxFsTftpTargetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFsTftpTargetSlot.setStatus("mandatory")


class _CxFsTftpRemxt_Type(Integer32):
    """Custom type cxFsTftpRemxt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CxFsTftpRemxt_Type.__name__ = "Integer32"
_CxFsTftpRemxt_Object = MibScalar
cxFsTftpRemxt = _CxFsTftpRemxt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 3),
    _CxFsTftpRemxt_Type()
)
cxFsTftpRemxt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFsTftpRemxt.setStatus("mandatory")


class _CxFsIsBusy_Type(Integer32):
    """Custom type cxFsIsBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxFsIsBusy_Type.__name__ = "Integer32"
_CxFsIsBusy_Object = MibScalar
cxFsIsBusy = _CxFsIsBusy_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 4),
    _CxFsIsBusy_Type()
)
cxFsIsBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFsIsBusy.setStatus("mandatory")


class _CxFsBackGroundCleanup_Type(Integer32):
    """Custom type cxFsBackGroundCleanup based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CxFsBackGroundCleanup_Type.__name__ = "Integer32"
_CxFsBackGroundCleanup_Object = MibScalar
cxFsBackGroundCleanup = _CxFsBackGroundCleanup_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 5),
    _CxFsBackGroundCleanup_Type()
)
cxFsBackGroundCleanup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFsBackGroundCleanup.setStatus("mandatory")


class _CxFsCleanupOnce_Type(Integer32):
    """Custom type cxFsCleanupOnce based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CxFsCleanupOnce_Type.__name__ = "Integer32"
_CxFsCleanupOnce_Object = MibScalar
cxFsCleanupOnce = _CxFsCleanupOnce_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 6),
    _CxFsCleanupOnce_Type()
)
cxFsCleanupOnce.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cxFsCleanupOnce.setStatus("mandatory")
_CxFsFreeBytes_Type = Integer32
_CxFsFreeBytes_Object = MibScalar
cxFsFreeBytes = _CxFsFreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 7),
    _CxFsFreeBytes_Type()
)
cxFsFreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFsFreeBytes.setStatus("mandatory")
_CxFsDeleteFile_Type = DisplayString
_CxFsDeleteFile_Object = MibScalar
cxFsDeleteFile = _CxFsDeleteFile_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 8),
    _CxFsDeleteFile_Type()
)
cxFsDeleteFile.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cxFsDeleteFile.setStatus("mandatory")
_CxFsFileList_Type = DisplayString
_CxFsFileList_Object = MibScalar
cxFsFileList = _CxFsFileList_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 9),
    _CxFsFileList_Type()
)
cxFsFileList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFsFileList.setStatus("mandatory")


class _CxFsTransferDestSlot_Type(Integer32):
    """Custom type cxFsTransferDestSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CxFsTransferDestSlot_Type.__name__ = "Integer32"
_CxFsTransferDestSlot_Object = MibScalar
cxFsTransferDestSlot = _CxFsTransferDestSlot_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 10),
    _CxFsTransferDestSlot_Type()
)
cxFsTransferDestSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFsTransferDestSlot.setStatus("mandatory")


class _CxFsTransferFileName_Type(DisplayString):
    """Custom type cxFsTransferFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 15),
    )


_CxFsTransferFileName_Type.__name__ = "DisplayString"
_CxFsTransferFileName_Object = MibScalar
cxFsTransferFileName = _CxFsTransferFileName_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 11),
    _CxFsTransferFileName_Type()
)
cxFsTransferFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFsTransferFileName.setStatus("mandatory")


class _CxFsTransferAction_Type(Integer32):
    """Custom type cxFsTransferAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("get", 2),
          ("no-action", 1),
          ("put", 3))
    )


_CxFsTransferAction_Type.__name__ = "Integer32"
_CxFsTransferAction_Object = MibScalar
cxFsTransferAction = _CxFsTransferAction_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 12),
    _CxFsTransferAction_Type()
)
cxFsTransferAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFsTransferAction.setStatus("mandatory")


class _CxFsTransferStatus_Type(Integer32):
    """Custom type cxFsTransferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("idle", 1),
          ("processing", 2),
          ("succeeded", 3))
    )


_CxFsTransferStatus_Type.__name__ = "Integer32"
_CxFsTransferStatus_Object = MibScalar
cxFsTransferStatus = _CxFsTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 13),
    _CxFsTransferStatus_Type()
)
cxFsTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFsTransferStatus.setStatus("mandatory")


class _CxFsTransferErrorCode_Type(Integer32):
    """Custom type cxFsTransferErrorCode based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("local-close-error", 9),
          ("local-open-error", 3),
          ("local-reading-error", 5),
          ("local-writing-error", 7),
          ("nfs-close-error", 10),
          ("nfs-open-error", 4),
          ("nfs-reading-error", 6),
          ("nfs-writing-error", 8),
          ("not-applicable", 1),
          ("ok", 2),
          ("other-error", 11))
    )


_CxFsTransferErrorCode_Type.__name__ = "Integer32"
_CxFsTransferErrorCode_Object = MibScalar
cxFsTransferErrorCode = _CxFsTransferErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 3, 14),
    _CxFsTransferErrorCode_Type()
)
cxFsTransferErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFsTransferErrorCode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXFileServer-MIB",
    **{"cxFsTftpTransfer": cxFsTftpTransfer,
       "cxFsTftpTargetSlot": cxFsTftpTargetSlot,
       "cxFsTftpRemxt": cxFsTftpRemxt,
       "cxFsIsBusy": cxFsIsBusy,
       "cxFsBackGroundCleanup": cxFsBackGroundCleanup,
       "cxFsCleanupOnce": cxFsCleanupOnce,
       "cxFsFreeBytes": cxFsFreeBytes,
       "cxFsDeleteFile": cxFsDeleteFile,
       "cxFsFileList": cxFsFileList,
       "cxFsTransferDestSlot": cxFsTransferDestSlot,
       "cxFsTransferFileName": cxFsTransferFileName,
       "cxFsTransferAction": cxFsTransferAction,
       "cxFsTransferStatus": cxFsTransferStatus,
       "cxFsTransferErrorCode": cxFsTransferErrorCode}
)
