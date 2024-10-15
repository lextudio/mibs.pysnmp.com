# SNMP MIB module (CT-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-FLASH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:16 2024
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

(ctFlash,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctFlash")

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

_FlashStatus_ObjectIdentity = ObjectIdentity
flashStatus = _FlashStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1)
)
_FlashVolumeStatusTable_Object = MibTable
flashVolumeStatusTable = _FlashVolumeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1)
)
if mibBuilder.loadTexts:
    flashVolumeStatusTable.setStatus("mandatory")
_FlashVolumeStatusEntry_Object = MibTableRow
flashVolumeStatusEntry = _FlashVolumeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1, 1)
)
flashVolumeStatusEntry.setIndexNames(
    (0, "CT-FLASH-MIB", "flashVolume"),
)
if mibBuilder.loadTexts:
    flashVolumeStatusEntry.setStatus("mandatory")
_FlashVolume_Type = Integer32
_FlashVolume_Object = MibTableColumn
flashVolume = _FlashVolume_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1, 1, 1),
    _FlashVolume_Type()
)
flashVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashVolume.setStatus("mandatory")
_FlashVolFiles_Type = Integer32
_FlashVolFiles_Object = MibTableColumn
flashVolFiles = _FlashVolFiles_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1, 1, 2),
    _FlashVolFiles_Type()
)
flashVolFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashVolFiles.setStatus("mandatory")
_FlashVolSpace_Type = Integer32
_FlashVolSpace_Object = MibTableColumn
flashVolSpace = _FlashVolSpace_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1, 1, 3),
    _FlashVolSpace_Type()
)
flashVolSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashVolSpace.setStatus("mandatory")
_FlashFile_ObjectIdentity = ObjectIdentity
flashFile = _FlashFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2)
)
_FlashFileTable_Object = MibTable
flashFileTable = _FlashFileTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1)
)
if mibBuilder.loadTexts:
    flashFileTable.setStatus("mandatory")
_FlashFileEntry_Object = MibTableRow
flashFileEntry = _FlashFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1)
)
flashFileEntry.setIndexNames(
    (0, "CT-FLASH-MIB", "flashVolume"),
    (0, "CT-FLASH-MIB", "flashFileID"),
)
if mibBuilder.loadTexts:
    flashFileEntry.setStatus("mandatory")
_FlashFileID_Type = Integer32
_FlashFileID_Object = MibTableColumn
flashFileID = _FlashFileID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 1),
    _FlashFileID_Type()
)
flashFileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileID.setStatus("mandatory")


class _FlashFilename_Type(DisplayString):
    """Custom type flashFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FlashFilename_Type.__name__ = "DisplayString"
_FlashFilename_Object = MibTableColumn
flashFilename = _FlashFilename_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 2),
    _FlashFilename_Type()
)
flashFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFilename.setStatus("mandatory")


class _FlashFileVersion_Type(DisplayString):
    """Custom type flashFileVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FlashFileVersion_Type.__name__ = "DisplayString"
_FlashFileVersion_Object = MibTableColumn
flashFileVersion = _FlashFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 3),
    _FlashFileVersion_Type()
)
flashFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileVersion.setStatus("mandatory")


class _FlashFileType_Type(Integer32):
    """Custom type flashFileType based on Integer32"""
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
        *(("bOOT", 7),
          ("binary", 8),
          ("binaryCompressed", 9),
          ("dLL", 6),
          ("eLF", 4),
          ("iEEE695", 3),
          ("intelHex", 1),
          ("intelHexCompressed", 2),
          ("package", 11),
          ("table", 5),
          ("taggedData", 10))
    )


_FlashFileType_Type.__name__ = "Integer32"
_FlashFileType_Object = MibTableColumn
flashFileType = _FlashFileType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 4),
    _FlashFileType_Type()
)
flashFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileType.setStatus("mandatory")
_FlashFileSize_Type = Integer32
_FlashFileSize_Object = MibTableColumn
flashFileSize = _FlashFileSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 5),
    _FlashFileSize_Type()
)
flashFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileSize.setStatus("mandatory")
_FlashCmd_ObjectIdentity = ObjectIdentity
flashCmd = _FlashCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3)
)


class _FlashCmdPath_Type(DisplayString):
    """Custom type flashCmdPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FlashCmdPath_Type.__name__ = "DisplayString"
_FlashCmdPath_Object = MibScalar
flashCmdPath = _FlashCmdPath_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 1),
    _FlashCmdPath_Type()
)
flashCmdPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashCmdPath.setStatus("mandatory")
_FlashCmdNetAddress_Type = IpAddress
_FlashCmdNetAddress_Object = MibScalar
flashCmdNetAddress = _FlashCmdNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 2),
    _FlashCmdNetAddress_Type()
)
flashCmdNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashCmdNetAddress.setStatus("mandatory")
_FlashCmdVolume_Type = Integer32
_FlashCmdVolume_Object = MibScalar
flashCmdVolume = _FlashCmdVolume_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 3),
    _FlashCmdVolume_Type()
)
flashCmdVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashCmdVolume.setStatus("mandatory")


class _FlashCmdOperation_Type(Integer32):
    """Custom type flashCmdOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleanup", 4),
          ("delete", 5),
          ("download", 2),
          ("install", 1),
          ("none", 6),
          ("upload", 3))
    )


_FlashCmdOperation_Type.__name__ = "Integer32"
_FlashCmdOperation_Object = MibScalar
flashCmdOperation = _FlashCmdOperation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 4),
    _FlashCmdOperation_Type()
)
flashCmdOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashCmdOperation.setStatus("mandatory")


class _FlashCmdStatus_Type(Integer32):
    """Custom type flashCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("completeError", 7),
          ("downLoadActive", 5),
          ("flashCleanup", 4),
          ("flashVerifyServer", 3),
          ("idle", 1),
          ("other", 2),
          ("upLoadActive", 6))
    )


_FlashCmdStatus_Type.__name__ = "Integer32"
_FlashCmdStatus_Object = MibScalar
flashCmdStatus = _FlashCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 5),
    _FlashCmdStatus_Type()
)
flashCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCmdStatus.setStatus("mandatory")


class _FlashCmdError_Type(Integer32):
    """Custom type flashCmdError based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("blockSequence", 23),
          ("bufferError", 24),
          ("corruptFile", 5),
          ("deleteFailed", 2),
          ("dupFlashName", 6),
          ("dupNetFile", 16),
          ("fileSystem", 3),
          ("flashAlloc", 8),
          ("invalidCmd", 19),
          ("invalidModId", 20),
          ("invalidName", 10),
          ("invalidType", 18),
          ("maxFiles", 9),
          ("netDiskFull", 15),
          ("noFlashFile", 7),
          ("noNetAccess", 14),
          ("noNetFile", 13),
          ("noServerIP", 21),
          ("oK", 1),
          ("parseError", 17),
          ("protocolErr", 11),
          ("serverLost", 12),
          ("socketError", 22),
          ("tFTPerror", 4))
    )


_FlashCmdError_Type.__name__ = "Integer32"
_FlashCmdError_Object = MibScalar
flashCmdError = _FlashCmdError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 6),
    _FlashCmdError_Type()
)
flashCmdError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCmdError.setStatus("mandatory")


class _FlashCmdFile_Type(DisplayString):
    """Custom type flashCmdFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FlashCmdFile_Type.__name__ = "DisplayString"
_FlashCmdFile_Object = MibScalar
flashCmdFile = _FlashCmdFile_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 7),
    _FlashCmdFile_Type()
)
flashCmdFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashCmdFile.setStatus("mandatory")


class _FlashCmdVersion_Type(DisplayString):
    """Custom type flashCmdVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FlashCmdVersion_Type.__name__ = "DisplayString"
_FlashCmdVersion_Object = MibScalar
flashCmdVersion = _FlashCmdVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 8),
    _FlashCmdVersion_Type()
)
flashCmdVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashCmdVersion.setStatus("mandatory")


class _FlashCmdType_Type(Integer32):
    """Custom type flashCmdType based on Integer32"""
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
        *(("bOOT", 7),
          ("binary", 8),
          ("binaryCompressed", 9),
          ("dLL", 6),
          ("eLF", 4),
          ("iEEE695", 3),
          ("intelHex", 1),
          ("intelHexCompressed", 2),
          ("package", 11),
          ("table", 5),
          ("taggedData", 10))
    )


_FlashCmdType_Type.__name__ = "Integer32"
_FlashCmdType_Object = MibScalar
flashCmdType = _FlashCmdType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 9),
    _FlashCmdType_Type()
)
flashCmdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashCmdType.setStatus("mandatory")
_FlashCmdSize_Type = Integer32
_FlashCmdSize_Object = MibScalar
flashCmdSize = _FlashCmdSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 10),
    _FlashCmdSize_Type()
)
flashCmdSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashCmdSize.setStatus("mandatory")
_FlashBlockCount_Type = Integer32
_FlashBlockCount_Object = MibScalar
flashBlockCount = _FlashBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 11),
    _FlashBlockCount_Type()
)
flashBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashBlockCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-FLASH-MIB",
    **{"flashStatus": flashStatus,
       "flashVolumeStatusTable": flashVolumeStatusTable,
       "flashVolumeStatusEntry": flashVolumeStatusEntry,
       "flashVolume": flashVolume,
       "flashVolFiles": flashVolFiles,
       "flashVolSpace": flashVolSpace,
       "flashFile": flashFile,
       "flashFileTable": flashFileTable,
       "flashFileEntry": flashFileEntry,
       "flashFileID": flashFileID,
       "flashFilename": flashFilename,
       "flashFileVersion": flashFileVersion,
       "flashFileType": flashFileType,
       "flashFileSize": flashFileSize,
       "flashCmd": flashCmd,
       "flashCmdPath": flashCmdPath,
       "flashCmdNetAddress": flashCmdNetAddress,
       "flashCmdVolume": flashCmdVolume,
       "flashCmdOperation": flashCmdOperation,
       "flashCmdStatus": flashCmdStatus,
       "flashCmdError": flashCmdError,
       "flashCmdFile": flashCmdFile,
       "flashCmdVersion": flashCmdVersion,
       "flashCmdType": flashCmdType,
       "flashCmdSize": flashCmdSize,
       "flashBlockCount": flashBlockCount}
)
