# SNMP MIB module (ACC-FILESYS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-FILESYS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:14 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccFileSys_ObjectIdentity = ObjectIdentity
accFileSys = _AccFileSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41)
)
_AccFsDirectTable_Object = MibTable
accFsDirectTable = _AccFsDirectTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 1)
)
if mibBuilder.loadTexts:
    accFsDirectTable.setStatus("mandatory")
_AccFsDirectEntry_Object = MibTableRow
accFsDirectEntry = _AccFsDirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 1, 1)
)
accFsDirectEntry.setIndexNames(
    (0, "ACC-FILESYS", "accFsDirectFileSpec"),
)
if mibBuilder.loadTexts:
    accFsDirectEntry.setStatus("mandatory")
_AccFsDirectFileSpec_Type = DisplayString
_AccFsDirectFileSpec_Object = MibTableColumn
accFsDirectFileSpec = _AccFsDirectFileSpec_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 1, 1, 1),
    _AccFsDirectFileSpec_Type()
)
accFsDirectFileSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFsDirectFileSpec.setStatus("mandatory")
_AccFsDirectCreate_Type = Integer32
_AccFsDirectCreate_Object = MibTableColumn
accFsDirectCreate = _AccFsDirectCreate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 1, 1, 2),
    _AccFsDirectCreate_Type()
)
accFsDirectCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsDirectCreate.setStatus("mandatory")
_AccFsDirectBytSize_Type = Integer32
_AccFsDirectBytSize_Object = MibTableColumn
accFsDirectBytSize = _AccFsDirectBytSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 1, 1, 3),
    _AccFsDirectBytSize_Type()
)
accFsDirectBytSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsDirectBytSize.setStatus("mandatory")
_AccFsDirectBlkSize_Type = Integer32
_AccFsDirectBlkSize_Object = MibTableColumn
accFsDirectBlkSize = _AccFsDirectBlkSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 1, 1, 4),
    _AccFsDirectBlkSize_Type()
)
accFsDirectBlkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsDirectBlkSize.setStatus("mandatory")
_AccFsDirectAttribStr_Type = DisplayString
_AccFsDirectAttribStr_Object = MibTableColumn
accFsDirectAttribStr = _AccFsDirectAttribStr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 1, 1, 5),
    _AccFsDirectAttribStr_Type()
)
accFsDirectAttribStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsDirectAttribStr.setStatus("mandatory")
_AccFsDirectSwVers_Type = DisplayString
_AccFsDirectSwVers_Object = MibTableColumn
accFsDirectSwVers = _AccFsDirectSwVers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 1, 1, 6),
    _AccFsDirectSwVers_Type()
)
accFsDirectSwVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsDirectSwVers.setStatus("mandatory")
_AccFsDirectPlatform_Type = DisplayString
_AccFsDirectPlatform_Object = MibTableColumn
accFsDirectPlatform = _AccFsDirectPlatform_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 1, 1, 7),
    _AccFsDirectPlatform_Type()
)
accFsDirectPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsDirectPlatform.setStatus("mandatory")


class _AccFsDirectStatus_Type(Integer32):
    """Custom type accFsDirectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccFsDirectStatus_Type.__name__ = "Integer32"
_AccFsDirectStatus_Object = MibTableColumn
accFsDirectStatus = _AccFsDirectStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 1, 1, 8),
    _AccFsDirectStatus_Type()
)
accFsDirectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFsDirectStatus.setStatus("mandatory")


class _AccFsDirectAction_Type(Integer32):
    """Custom type accFsDirectAction based on Integer32"""
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
        *(("backup", 3),
          ("copy", 4),
          ("delete", 2),
          ("primary", 1),
          ("rename", 5))
    )


_AccFsDirectAction_Type.__name__ = "Integer32"
_AccFsDirectAction_Object = MibTableColumn
accFsDirectAction = _AccFsDirectAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 1, 1, 9),
    _AccFsDirectAction_Type()
)
accFsDirectAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFsDirectAction.setStatus("mandatory")
_AccFsVolumeTable_Object = MibTable
accFsVolumeTable = _AccFsVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 2)
)
if mibBuilder.loadTexts:
    accFsVolumeTable.setStatus("mandatory")
_AccFsVolumeEntry_Object = MibTableRow
accFsVolumeEntry = _AccFsVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 2, 1)
)
accFsVolumeEntry.setIndexNames(
    (0, "ACC-FILESYS", "accFsVolumeName"),
)
if mibBuilder.loadTexts:
    accFsVolumeEntry.setStatus("mandatory")
_AccFsVolumeName_Type = DisplayString
_AccFsVolumeName_Object = MibTableColumn
accFsVolumeName = _AccFsVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 2, 1, 1),
    _AccFsVolumeName_Type()
)
accFsVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsVolumeName.setStatus("mandatory")
_AccFsVolumeSize_Type = Integer32
_AccFsVolumeSize_Object = MibTableColumn
accFsVolumeSize = _AccFsVolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 2, 1, 2),
    _AccFsVolumeSize_Type()
)
accFsVolumeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsVolumeSize.setStatus("mandatory")
_AccFsVolumeBlockSize_Type = Integer32
_AccFsVolumeBlockSize_Object = MibTableColumn
accFsVolumeBlockSize = _AccFsVolumeBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 2, 1, 3),
    _AccFsVolumeBlockSize_Type()
)
accFsVolumeBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsVolumeBlockSize.setStatus("mandatory")
_AccFsVolumeFileNum_Type = Integer32
_AccFsVolumeFileNum_Object = MibTableColumn
accFsVolumeFileNum = _AccFsVolumeFileNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 2, 1, 4),
    _AccFsVolumeFileNum_Type()
)
accFsVolumeFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsVolumeFileNum.setStatus("mandatory")
_AccFsVolumeUsedBytes_Type = Integer32
_AccFsVolumeUsedBytes_Object = MibTableColumn
accFsVolumeUsedBytes = _AccFsVolumeUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 2, 1, 5),
    _AccFsVolumeUsedBytes_Type()
)
accFsVolumeUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsVolumeUsedBytes.setStatus("mandatory")
_AccFsVolumeFreeBlocks_Type = Integer32
_AccFsVolumeFreeBlocks_Object = MibTableColumn
accFsVolumeFreeBlocks = _AccFsVolumeFreeBlocks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 2, 1, 6),
    _AccFsVolumeFreeBlocks_Type()
)
accFsVolumeFreeBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsVolumeFreeBlocks.setStatus("mandatory")
_AccFsVolumeFreeBytes_Type = Integer32
_AccFsVolumeFreeBytes_Object = MibTableColumn
accFsVolumeFreeBytes = _AccFsVolumeFreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 2, 1, 7),
    _AccFsVolumeFreeBytes_Type()
)
accFsVolumeFreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsVolumeFreeBytes.setStatus("mandatory")
_AccFsVolumeResBlocks_Type = Integer32
_AccFsVolumeResBlocks_Object = MibTableColumn
accFsVolumeResBlocks = _AccFsVolumeResBlocks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 2, 1, 8),
    _AccFsVolumeResBlocks_Type()
)
accFsVolumeResBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsVolumeResBlocks.setStatus("mandatory")


class _AccFsVolumeAction_Type(Integer32):
    """Custom type accFsVolumeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("copy", 4)
    )


_AccFsVolumeAction_Type.__name__ = "Integer32"
_AccFsVolumeAction_Object = MibTableColumn
accFsVolumeAction = _AccFsVolumeAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 2, 1, 9),
    _AccFsVolumeAction_Type()
)
accFsVolumeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFsVolumeAction.setStatus("mandatory")
_AccFsVolumeDst_Type = DisplayString
_AccFsVolumeDst_Object = MibTableColumn
accFsVolumeDst = _AccFsVolumeDst_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 2, 1, 10),
    _AccFsVolumeDst_Type()
)
accFsVolumeDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFsVolumeDst.setStatus("mandatory")
_AccFsLoadedFiles_ObjectIdentity = ObjectIdentity
accFsLoadedFiles = _AccFsLoadedFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 3)
)
_AccFsLoadFtkFile_Type = DisplayString
_AccFsLoadFtkFile_Object = MibScalar
accFsLoadFtkFile = _AccFsLoadFtkFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 3, 1),
    _AccFsLoadFtkFile_Type()
)
accFsLoadFtkFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsLoadFtkFile.setStatus("mandatory")
_AccFsLoadAplFile_Type = DisplayString
_AccFsLoadAplFile_Object = MibScalar
accFsLoadAplFile = _AccFsLoadAplFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 3, 2),
    _AccFsLoadAplFile_Type()
)
accFsLoadAplFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsLoadAplFile.setStatus("mandatory")
_AccFsLoadDiaFile_Type = DisplayString
_AccFsLoadDiaFile_Object = MibScalar
accFsLoadDiaFile = _AccFsLoadDiaFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 3, 3),
    _AccFsLoadDiaFile_Type()
)
accFsLoadDiaFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsLoadDiaFile.setStatus("mandatory")
_AccFsLoadConFile_Type = DisplayString
_AccFsLoadConFile_Object = MibScalar
accFsLoadConFile = _AccFsLoadConFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 3, 4),
    _AccFsLoadConFile_Type()
)
accFsLoadConFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsLoadConFile.setStatus("mandatory")
_AccFsLoadScrFile_Type = DisplayString
_AccFsLoadScrFile_Object = MibScalar
accFsLoadScrFile = _AccFsLoadScrFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 3, 5),
    _AccFsLoadScrFile_Type()
)
accFsLoadScrFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsLoadScrFile.setStatus("mandatory")
_AccFsLoadFrmFile_Type = DisplayString
_AccFsLoadFrmFile_Object = MibScalar
accFsLoadFrmFile = _AccFsLoadFrmFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 3, 6),
    _AccFsLoadFrmFile_Type()
)
accFsLoadFrmFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFsLoadFrmFile.setStatus("mandatory")
_AccReloadFileList_Type = DisplayString
_AccReloadFileList_Object = MibScalar
accReloadFileList = _AccReloadFileList_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 41, 4),
    _AccReloadFileList_Type()
)
accReloadFileList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accReloadFileList.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-FILESYS",
    **{"accFileSys": accFileSys,
       "accFsDirectTable": accFsDirectTable,
       "accFsDirectEntry": accFsDirectEntry,
       "accFsDirectFileSpec": accFsDirectFileSpec,
       "accFsDirectCreate": accFsDirectCreate,
       "accFsDirectBytSize": accFsDirectBytSize,
       "accFsDirectBlkSize": accFsDirectBlkSize,
       "accFsDirectAttribStr": accFsDirectAttribStr,
       "accFsDirectSwVers": accFsDirectSwVers,
       "accFsDirectPlatform": accFsDirectPlatform,
       "accFsDirectStatus": accFsDirectStatus,
       "accFsDirectAction": accFsDirectAction,
       "accFsVolumeTable": accFsVolumeTable,
       "accFsVolumeEntry": accFsVolumeEntry,
       "accFsVolumeName": accFsVolumeName,
       "accFsVolumeSize": accFsVolumeSize,
       "accFsVolumeBlockSize": accFsVolumeBlockSize,
       "accFsVolumeFileNum": accFsVolumeFileNum,
       "accFsVolumeUsedBytes": accFsVolumeUsedBytes,
       "accFsVolumeFreeBlocks": accFsVolumeFreeBlocks,
       "accFsVolumeFreeBytes": accFsVolumeFreeBytes,
       "accFsVolumeResBlocks": accFsVolumeResBlocks,
       "accFsVolumeAction": accFsVolumeAction,
       "accFsVolumeDst": accFsVolumeDst,
       "accFsLoadedFiles": accFsLoadedFiles,
       "accFsLoadFtkFile": accFsLoadFtkFile,
       "accFsLoadAplFile": accFsLoadAplFile,
       "accFsLoadDiaFile": accFsLoadDiaFile,
       "accFsLoadConFile": accFsLoadConFile,
       "accFsLoadScrFile": accFsLoadScrFile,
       "accFsLoadFrmFile": accFsLoadFrmFile,
       "accReloadFileList": accReloadFileList}
)
