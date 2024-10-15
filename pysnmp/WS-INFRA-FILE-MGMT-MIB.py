# SNMP MIB module (WS-INFRA-FILE-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-INFRA-FILE-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:26 2024
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(wsInfra,) = mibBuilder.importSymbols(
    "WS-SMI",
    "wsInfra")

(DoActionNow,) = mibBuilder.importSymbols(
    "WS-TYPE-MIB",
    "DoActionNow")


# MODULE-IDENTITY

wsInfraFileMgmtModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1)
)
wsInfraFileMgmtModule.setRevisions(
        ("2006-10-06 11:14",
         "2006-07-06 11:49",
         "2006-06-26 18:57",
         "2006-05-26 14:52",
         "2006-05-24 10:44",
         "2005-11-14 15:48",
         "2005-11-03 10:14",
         "2005-10-18 16:12",
         "2005-10-12 14:10",
         "2005-10-12 13:55",
         "2005-10-12 11:03",
         "2005-10-11 17:33",
         "2005-08-04 10:18",
         "2005-07-06 11:49",
         "2005-06-28 11:58",
         "2005-06-27 14:34",
         "2005-06-24 12:07",
         "2005-06-23 13:17",
         "2005-06-22 10:34",
         "2005-06-20 11:05",
         "2005-06-09 15:24",
         "2005-06-07 18:43",
         "2005-05-04 16:13",
         "2005-05-04 10:58")
)


# Types definitions



class DoActionState(Integer32):
    """Custom type DoActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("inProgress", 3),
          ("success", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsInfraFileMgmt_ObjectIdentity = ObjectIdentity
wsInfraFileMgmt = _WsInfraFileMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2)
)
_WsInfraFileMgmtDir_ObjectIdentity = ObjectIdentity
wsInfraFileMgmtDir = _WsInfraFileMgmtDir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 1)
)
_WsInfraFileMgmtDirString_Type = DisplayString
_WsInfraFileMgmtDirString_Object = MibScalar
wsInfraFileMgmtDirString = _WsInfraFileMgmtDirString_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 1, 1),
    _WsInfraFileMgmtDirString_Type()
)
wsInfraFileMgmtDirString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraFileMgmtDirString.setStatus("current")
_WsInfraFIleMgmtDirError_Type = DisplayString
_WsInfraFIleMgmtDirError_Object = MibScalar
wsInfraFIleMgmtDirError = _WsInfraFIleMgmtDirError_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 1, 2),
    _WsInfraFIleMgmtDirError_Type()
)
wsInfraFIleMgmtDirError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFIleMgmtDirError.setStatus("current")
_WsInfraFileTable_Object = MibTable
wsInfraFileTable = _WsInfraFileTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    wsInfraFileTable.setStatus("current")
_WsInfraFileEntry_Object = MibTableRow
wsInfraFileEntry = _WsInfraFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1)
)
wsInfraFileEntry.setIndexNames(
    (0, "WS-INFRA-FILE-MGMT-MIB", "wsInfraFileIndex"),
)
if mibBuilder.loadTexts:
    wsInfraFileEntry.setStatus("current")


class _WsInfraFileIndex_Type(Integer32):
    """Custom type wsInfraFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WsInfraFileIndex_Type.__name__ = "Integer32"
_WsInfraFileIndex_Object = MibTableColumn
wsInfraFileIndex = _WsInfraFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 1),
    _WsInfraFileIndex_Type()
)
wsInfraFileIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsInfraFileIndex.setStatus("current")


class _WsInfraFileName_Type(DisplayString):
    """Custom type wsInfraFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WsInfraFileName_Type.__name__ = "DisplayString"
_WsInfraFileName_Object = MibTableColumn
wsInfraFileName = _WsInfraFileName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 2),
    _WsInfraFileName_Type()
)
wsInfraFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileName.setStatus("current")


class _WsInfraFileType_Type(Integer32):
    """Custom type wsInfraFileType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("binary", 1),
          ("certFile", 12),
          ("configFile", 10),
          ("coreFile", 13),
          ("directory", 4),
          ("dumpFile", 15),
          ("emptyFile", 6),
          ("historyFile", 9),
          ("licFile", 11),
          ("logFile", 8),
          ("panicFile", 14),
          ("pcapFile", 16),
          ("symlink", 5),
          ("text", 2),
          ("unReadableFile", 7),
          ("unknown", 3))
    )


_WsInfraFileType_Type.__name__ = "Integer32"
_WsInfraFileType_Object = MibTableColumn
wsInfraFileType = _WsInfraFileType_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 3),
    _WsInfraFileType_Type()
)
wsInfraFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileType.setStatus("current")
_WsInfraFileSize_Type = Integer32
_WsInfraFileSize_Object = MibTableColumn
wsInfraFileSize = _WsInfraFileSize_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 4),
    _WsInfraFileSize_Type()
)
wsInfraFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileSize.setStatus("current")
if mibBuilder.loadTexts:
    wsInfraFileSize.setUnits("byte")


class _WsInfraFilePerm_Type(DisplayString):
    """Custom type wsInfraFilePerm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_WsInfraFilePerm_Type.__name__ = "DisplayString"
_WsInfraFilePerm_Object = MibTableColumn
wsInfraFilePerm = _WsInfraFilePerm_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 5),
    _WsInfraFilePerm_Type()
)
wsInfraFilePerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFilePerm.setStatus("current")
_WsInfraFileCreateDate_Type = DateAndTime
_WsInfraFileCreateDate_Object = MibTableColumn
wsInfraFileCreateDate = _WsInfraFileCreateDate_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 6),
    _WsInfraFileCreateDate_Type()
)
wsInfraFileCreateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileCreateDate.setStatus("current")
_WsInfraFileModDate_Type = DateAndTime
_WsInfraFileModDate_Object = MibTableColumn
wsInfraFileModDate = _WsInfraFileModDate_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 7),
    _WsInfraFileModDate_Type()
)
wsInfraFileModDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileModDate.setStatus("current")
_WsInfraFileMgmtImageTable_Object = MibTable
wsInfraFileMgmtImageTable = _WsInfraFileMgmtImageTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    wsInfraFileMgmtImageTable.setStatus("current")
_WsInfraFileMgmtImageEntry_Object = MibTableRow
wsInfraFileMgmtImageEntry = _WsInfraFileMgmtImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1)
)
wsInfraFileMgmtImageEntry.setIndexNames(
    (0, "WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageIndex"),
)
if mibBuilder.loadTexts:
    wsInfraFileMgmtImageEntry.setStatus("current")


class _WsInfraFileMgmtImageIndex_Type(Integer32):
    """Custom type wsInfraFileMgmtImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WsInfraFileMgmtImageIndex_Type.__name__ = "Integer32"
_WsInfraFileMgmtImageIndex_Object = MibTableColumn
wsInfraFileMgmtImageIndex = _WsInfraFileMgmtImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1, 1),
    _WsInfraFileMgmtImageIndex_Type()
)
wsInfraFileMgmtImageIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsInfraFileMgmtImageIndex.setStatus("current")
_WsInfraFileMgmtImageVersion_Type = DisplayString
_WsInfraFileMgmtImageVersion_Object = MibTableColumn
wsInfraFileMgmtImageVersion = _WsInfraFileMgmtImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1, 2),
    _WsInfraFileMgmtImageVersion_Type()
)
wsInfraFileMgmtImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileMgmtImageVersion.setStatus("current")
_WsInfraFileMgmtImageUseNow_Type = TruthValue
_WsInfraFileMgmtImageUseNow_Object = MibTableColumn
wsInfraFileMgmtImageUseNow = _WsInfraFileMgmtImageUseNow_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1, 3),
    _WsInfraFileMgmtImageUseNow_Type()
)
wsInfraFileMgmtImageUseNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileMgmtImageUseNow.setStatus("current")
_WsInfraFileMgmtImageUseOnBoot_Type = TruthValue
_WsInfraFileMgmtImageUseOnBoot_Object = MibTableColumn
wsInfraFileMgmtImageUseOnBoot = _WsInfraFileMgmtImageUseOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1, 4),
    _WsInfraFileMgmtImageUseOnBoot_Type()
)
wsInfraFileMgmtImageUseOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraFileMgmtImageUseOnBoot.setStatus("current")
_WsInfraFileMgmtImageBuildTime_Type = DateAndTime
_WsInfraFileMgmtImageBuildTime_Object = MibTableColumn
wsInfraFileMgmtImageBuildTime = _WsInfraFileMgmtImageBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1, 5),
    _WsInfraFileMgmtImageBuildTime_Type()
)
wsInfraFileMgmtImageBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileMgmtImageBuildTime.setStatus("current")
_WsInfraFileMgmtImageInstallTime_Type = DateAndTime
_WsInfraFileMgmtImageInstallTime_Object = MibTableColumn
wsInfraFileMgmtImageInstallTime = _WsInfraFileMgmtImageInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1, 6),
    _WsInfraFileMgmtImageInstallTime_Type()
)
wsInfraFileMgmtImageInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileMgmtImageInstallTime.setStatus("current")
_WsInfraImgUpd_ObjectIdentity = ObjectIdentity
wsInfraImgUpd = _WsInfraImgUpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 4)
)
_WsInfraImgUpdFile_Type = DisplayString
_WsInfraImgUpdFile_Object = MibScalar
wsInfraImgUpdFile = _WsInfraImgUpdFile_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 4, 1),
    _WsInfraImgUpdFile_Type()
)
wsInfraImgUpdFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraImgUpdFile.setStatus("current")


class _WsInfraImgUpdStart_Type(Integer32):
    """Custom type wsInfraImgUpdStart based on Integer32"""
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
        *(("abortUpdate", 2),
          ("idle", 3),
          ("imgUpdate", 1),
          ("removePatch", 4))
    )


_WsInfraImgUpdStart_Type.__name__ = "Integer32"
_WsInfraImgUpdStart_Object = MibScalar
wsInfraImgUpdStart = _WsInfraImgUpdStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 4, 2),
    _WsInfraImgUpdStart_Type()
)
wsInfraImgUpdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraImgUpdStart.setStatus("current")
_WsInfraImgUpdStatus_Type = DoActionState
_WsInfraImgUpdStatus_Object = MibScalar
wsInfraImgUpdStatus = _WsInfraImgUpdStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 4, 3),
    _WsInfraImgUpdStatus_Type()
)
wsInfraImgUpdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraImgUpdStatus.setStatus("current")
_WsInfraImgUpdLastFailedReason_Type = DisplayString
_WsInfraImgUpdLastFailedReason_Object = MibScalar
wsInfraImgUpdLastFailedReason = _WsInfraImgUpdLastFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 4, 4),
    _WsInfraImgUpdLastFailedReason_Type()
)
wsInfraImgUpdLastFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraImgUpdLastFailedReason.setStatus("current")
_WsInfraImgUpdCounter_Type = Counter32
_WsInfraImgUpdCounter_Object = MibScalar
wsInfraImgUpdCounter = _WsInfraImgUpdCounter_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 4, 5),
    _WsInfraImgUpdCounter_Type()
)
wsInfraImgUpdCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraImgUpdCounter.setStatus("current")
_WsInfraFileManage_ObjectIdentity = ObjectIdentity
wsInfraFileManage = _WsInfraFileManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5)
)
_WsInfraFileManageSrc_Type = DisplayString
_WsInfraFileManageSrc_Object = MibScalar
wsInfraFileManageSrc = _WsInfraFileManageSrc_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5, 1),
    _WsInfraFileManageSrc_Type()
)
wsInfraFileManageSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraFileManageSrc.setStatus("current")


class _WsInfraFileManageDest_Type(DisplayString):
    """Custom type wsInfraFileManageDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WsInfraFileManageDest_Type.__name__ = "DisplayString"
_WsInfraFileManageDest_Object = MibScalar
wsInfraFileManageDest = _WsInfraFileManageDest_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5, 2),
    _WsInfraFileManageDest_Type()
)
wsInfraFileManageDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraFileManageDest.setStatus("current")


class _WsInfraFileManageStart_Type(Integer32):
    """Custom type wsInfraFileManageStart based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("abort", 17),
          ("cgiImport", 19),
          ("computeRunningCfgChkSum", 16),
          ("computeSavedCfgChkSum", 15),
          ("copy", 1),
          ("delete", 2),
          ("expand", 18),
          ("exportCert", 11),
          ("exportKey", 10),
          ("exportReq", 12),
          ("exportTrustPoint", 13),
          ("idle", 14),
          ("importCACert", 7),
          ("importKey", 6),
          ("importServerCert", 8),
          ("importTrustPoint", 9),
          ("mkDir", 5),
          ("rename", 3),
          ("rmDir", 4))
    )


_WsInfraFileManageStart_Type.__name__ = "Integer32"
_WsInfraFileManageStart_Object = MibScalar
wsInfraFileManageStart = _WsInfraFileManageStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5, 3),
    _WsInfraFileManageStart_Type()
)
wsInfraFileManageStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraFileManageStart.setStatus("current")
_WsInfraFileManageStatus_Type = DoActionState
_WsInfraFileManageStatus_Object = MibScalar
wsInfraFileManageStatus = _WsInfraFileManageStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5, 4),
    _WsInfraFileManageStatus_Type()
)
wsInfraFileManageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileManageStatus.setStatus("current")
_WsInfraFileManageLastFailedReason_Type = DisplayString
_WsInfraFileManageLastFailedReason_Object = MibScalar
wsInfraFileManageLastFailedReason = _WsInfraFileManageLastFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5, 5),
    _WsInfraFileManageLastFailedReason_Type()
)
wsInfraFileManageLastFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileManageLastFailedReason.setStatus("current")
_WsInfraFileManageCounter_Type = Counter32
_WsInfraFileManageCounter_Object = MibScalar
wsInfraFileManageCounter = _WsInfraFileManageCounter_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5, 6),
    _WsInfraFileManageCounter_Type()
)
wsInfraFileManageCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileManageCounter.setStatus("current")
_WsInfraFileImgUpdFailOver_Type = TruthValue
_WsInfraFileImgUpdFailOver_Object = MibScalar
wsInfraFileImgUpdFailOver = _WsInfraFileImgUpdFailOver_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 6),
    _WsInfraFileImgUpdFailOver_Type()
)
wsInfraFileImgUpdFailOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraFileImgUpdFailOver.setStatus("current")
_WsInfraCfgManage_ObjectIdentity = ObjectIdentity
wsInfraCfgManage = _WsInfraCfgManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 7)
)
_WsInfraCfgManageRunningCfgChangedFlag_Type = TruthValue
_WsInfraCfgManageRunningCfgChangedFlag_Object = MibScalar
wsInfraCfgManageRunningCfgChangedFlag = _WsInfraCfgManageRunningCfgChangedFlag_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 7, 1),
    _WsInfraCfgManageRunningCfgChangedFlag_Type()
)
wsInfraCfgManageRunningCfgChangedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraCfgManageRunningCfgChangedFlag.setStatus("current")
_WsInfraCfgManageSavedCfgChecksum_Type = OctetString
_WsInfraCfgManageSavedCfgChecksum_Object = MibScalar
wsInfraCfgManageSavedCfgChecksum = _WsInfraCfgManageSavedCfgChecksum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 7, 2),
    _WsInfraCfgManageSavedCfgChecksum_Type()
)
wsInfraCfgManageSavedCfgChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraCfgManageSavedCfgChecksum.setStatus("current")
_WsInfraCfgManageRunningCfgChecksum_Type = OctetString
_WsInfraCfgManageRunningCfgChecksum_Object = MibScalar
wsInfraCfgManageRunningCfgChecksum = _WsInfraCfgManageRunningCfgChecksum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 7, 3),
    _WsInfraCfgManageRunningCfgChecksum_Type()
)
wsInfraCfgManageRunningCfgChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraCfgManageRunningCfgChecksum.setStatus("current")
_WsInfraCfgManageResultantChecksum_Type = OctetString
_WsInfraCfgManageResultantChecksum_Object = MibScalar
wsInfraCfgManageResultantChecksum = _WsInfraCfgManageResultantChecksum_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 7, 4),
    _WsInfraCfgManageResultantChecksum_Type()
)
wsInfraCfgManageResultantChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraCfgManageResultantChecksum.setStatus("current")
_WsInfraFileMgmtPatchTable_Object = MibTable
wsInfraFileMgmtPatchTable = _WsInfraFileMgmtPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    wsInfraFileMgmtPatchTable.setStatus("current")
_WsInfraFileMgmtPatchEntry_Object = MibTableRow
wsInfraFileMgmtPatchEntry = _WsInfraFileMgmtPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 8, 1)
)
wsInfraFileMgmtPatchEntry.setIndexNames(
    (0, "WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtPatchIndex"),
)
if mibBuilder.loadTexts:
    wsInfraFileMgmtPatchEntry.setStatus("current")


class _WsInfraFileMgmtPatchIndex_Type(DisplayString):
    """Custom type wsInfraFileMgmtPatchIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsInfraFileMgmtPatchIndex_Type.__name__ = "DisplayString"
_WsInfraFileMgmtPatchIndex_Object = MibTableColumn
wsInfraFileMgmtPatchIndex = _WsInfraFileMgmtPatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 8, 1, 1),
    _WsInfraFileMgmtPatchIndex_Type()
)
wsInfraFileMgmtPatchIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsInfraFileMgmtPatchIndex.setStatus("current")


class _WsInfraFileMgmtPatchName_Type(DisplayString):
    """Custom type wsInfraFileMgmtPatchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WsInfraFileMgmtPatchName_Type.__name__ = "DisplayString"
_WsInfraFileMgmtPatchName_Object = MibTableColumn
wsInfraFileMgmtPatchName = _WsInfraFileMgmtPatchName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 8, 1, 2),
    _WsInfraFileMgmtPatchName_Type()
)
wsInfraFileMgmtPatchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraFileMgmtPatchName.setStatus("current")
_WsInfraFileMgmtPatchVersion_Type = DisplayString
_WsInfraFileMgmtPatchVersion_Object = MibTableColumn
wsInfraFileMgmtPatchVersion = _WsInfraFileMgmtPatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 8, 1, 3),
    _WsInfraFileMgmtPatchVersion_Type()
)
wsInfraFileMgmtPatchVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraFileMgmtPatchVersion.setStatus("current")
_WsInfraFSTable_Object = MibTable
wsInfraFSTable = _WsInfraFSTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    wsInfraFSTable.setStatus("current")
_WsInfraFSEntry_Object = MibTableRow
wsInfraFSEntry = _WsInfraFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9, 1)
)
wsInfraFSEntry.setIndexNames(
    (0, "WS-INFRA-FILE-MGMT-MIB", "wsInfraFSIndex"),
)
if mibBuilder.loadTexts:
    wsInfraFSEntry.setStatus("current")


class _WsInfraFSIndex_Type(Integer32):
    """Custom type wsInfraFSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WsInfraFSIndex_Type.__name__ = "Integer32"
_WsInfraFSIndex_Object = MibTableColumn
wsInfraFSIndex = _WsInfraFSIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9, 1, 1),
    _WsInfraFSIndex_Type()
)
wsInfraFSIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsInfraFSIndex.setStatus("current")
_WsInfraFSName_Type = DisplayString
_WsInfraFSName_Object = MibTableColumn
wsInfraFSName = _WsInfraFSName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9, 1, 2),
    _WsInfraFSName_Type()
)
wsInfraFSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFSName.setStatus("current")
_WsInfraFSAvailable_Type = TruthValue
_WsInfraFSAvailable_Object = MibTableColumn
wsInfraFSAvailable = _WsInfraFSAvailable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9, 1, 3),
    _WsInfraFSAvailable_Type()
)
wsInfraFSAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFSAvailable.setStatus("current")
_WsInfraFSFormatted_Type = TruthValue
_WsInfraFSFormatted_Object = MibTableColumn
wsInfraFSFormatted = _WsInfraFSFormatted_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9, 1, 4),
    _WsInfraFSFormatted_Type()
)
wsInfraFSFormatted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFSFormatted.setStatus("current")
_WsInfraFSFormat_Type = DoActionNow
_WsInfraFSFormat_Object = MibTableColumn
wsInfraFSFormat = _WsInfraFSFormat_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9, 1, 5),
    _WsInfraFSFormat_Type()
)
wsInfraFSFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsInfraFSFormat.setStatus("current")


class _WsInfraFileMgmtImportStatus_Type(Integer32):
    """Custom type wsInfraFileMgmtImportStatus based on Integer32"""
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
        *(("failure", 4),
          ("inProgress", 2),
          ("notDone", 1),
          ("success", 3))
    )


_WsInfraFileMgmtImportStatus_Type.__name__ = "Integer32"
_WsInfraFileMgmtImportStatus_Object = MibScalar
wsInfraFileMgmtImportStatus = _WsInfraFileMgmtImportStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 10),
    _WsInfraFileMgmtImportStatus_Type()
)
wsInfraFileMgmtImportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsInfraFileMgmtImportStatus.setStatus("current")
_WsInfraFileMgmtMIBConformance_ObjectIdentity = ObjectIdentity
wsInfraFileMgmtMIBConformance = _WsInfraFileMgmtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 100)
)
_WsInfraFileMgmtMIBGroups_ObjectIdentity = ObjectIdentity
wsInfraFileMgmtMIBGroups = _WsInfraFileMgmtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 100, 1)
)
_WsInfraFileMgmtMIBCompliances_ObjectIdentity = ObjectIdentity
wsInfraFileMgmtMIBCompliances = _WsInfraFileMgmtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 100, 2)
)

# Managed Objects groups

wsInfraFileMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 100, 1, 1)
)
wsInfraFileMgmtGroup.setObjects(
      *(("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileName"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileType"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileSize"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileCreateDate"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileModDate"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileManageSrc"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileManageDest"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileManageStatus"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileManageLastFailedReason"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileManageCounter"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileIndex"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileImgUpdFailOver"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileManageStart"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFilePerm"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtDirString"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFIleMgmtDirError"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageIndex"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageVersion"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageUseNow"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageUseOnBoot"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraCfgManageRunningCfgChecksum"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraCfgManageSavedCfgChecksum"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraCfgManageRunningCfgChangedFlag"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtPatchVersion"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtPatchName"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtPatchIndex"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFSIndex"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFSName"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFSAvailable"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFSFormatted"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFSFormat"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageInstallTime"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageBuildTime"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraImgUpdFile"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraImgUpdStart"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraImgUpdStatus"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraImgUpdLastFailedReason"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraImgUpdCounter"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraCfgManageResultantChecksum"),
        ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImportStatus"))
)
if mibBuilder.loadTexts:
    wsInfraFileMgmtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wsInfraFileMgmtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 100, 2, 1)
)
if mibBuilder.loadTexts:
    wsInfraFileMgmtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-INFRA-FILE-MGMT-MIB",
    **{"DoActionState": DoActionState,
       "wsInfraFileMgmt": wsInfraFileMgmt,
       "wsInfraFileMgmtModule": wsInfraFileMgmtModule,
       "wsInfraFileMgmtDir": wsInfraFileMgmtDir,
       "wsInfraFileMgmtDirString": wsInfraFileMgmtDirString,
       "wsInfraFIleMgmtDirError": wsInfraFIleMgmtDirError,
       "wsInfraFileTable": wsInfraFileTable,
       "wsInfraFileEntry": wsInfraFileEntry,
       "wsInfraFileIndex": wsInfraFileIndex,
       "wsInfraFileName": wsInfraFileName,
       "wsInfraFileType": wsInfraFileType,
       "wsInfraFileSize": wsInfraFileSize,
       "wsInfraFilePerm": wsInfraFilePerm,
       "wsInfraFileCreateDate": wsInfraFileCreateDate,
       "wsInfraFileModDate": wsInfraFileModDate,
       "wsInfraFileMgmtImageTable": wsInfraFileMgmtImageTable,
       "wsInfraFileMgmtImageEntry": wsInfraFileMgmtImageEntry,
       "wsInfraFileMgmtImageIndex": wsInfraFileMgmtImageIndex,
       "wsInfraFileMgmtImageVersion": wsInfraFileMgmtImageVersion,
       "wsInfraFileMgmtImageUseNow": wsInfraFileMgmtImageUseNow,
       "wsInfraFileMgmtImageUseOnBoot": wsInfraFileMgmtImageUseOnBoot,
       "wsInfraFileMgmtImageBuildTime": wsInfraFileMgmtImageBuildTime,
       "wsInfraFileMgmtImageInstallTime": wsInfraFileMgmtImageInstallTime,
       "wsInfraImgUpd": wsInfraImgUpd,
       "wsInfraImgUpdFile": wsInfraImgUpdFile,
       "wsInfraImgUpdStart": wsInfraImgUpdStart,
       "wsInfraImgUpdStatus": wsInfraImgUpdStatus,
       "wsInfraImgUpdLastFailedReason": wsInfraImgUpdLastFailedReason,
       "wsInfraImgUpdCounter": wsInfraImgUpdCounter,
       "wsInfraFileManage": wsInfraFileManage,
       "wsInfraFileManageSrc": wsInfraFileManageSrc,
       "wsInfraFileManageDest": wsInfraFileManageDest,
       "wsInfraFileManageStart": wsInfraFileManageStart,
       "wsInfraFileManageStatus": wsInfraFileManageStatus,
       "wsInfraFileManageLastFailedReason": wsInfraFileManageLastFailedReason,
       "wsInfraFileManageCounter": wsInfraFileManageCounter,
       "wsInfraFileImgUpdFailOver": wsInfraFileImgUpdFailOver,
       "wsInfraCfgManage": wsInfraCfgManage,
       "wsInfraCfgManageRunningCfgChangedFlag": wsInfraCfgManageRunningCfgChangedFlag,
       "wsInfraCfgManageSavedCfgChecksum": wsInfraCfgManageSavedCfgChecksum,
       "wsInfraCfgManageRunningCfgChecksum": wsInfraCfgManageRunningCfgChecksum,
       "wsInfraCfgManageResultantChecksum": wsInfraCfgManageResultantChecksum,
       "wsInfraFileMgmtPatchTable": wsInfraFileMgmtPatchTable,
       "wsInfraFileMgmtPatchEntry": wsInfraFileMgmtPatchEntry,
       "wsInfraFileMgmtPatchIndex": wsInfraFileMgmtPatchIndex,
       "wsInfraFileMgmtPatchName": wsInfraFileMgmtPatchName,
       "wsInfraFileMgmtPatchVersion": wsInfraFileMgmtPatchVersion,
       "wsInfraFSTable": wsInfraFSTable,
       "wsInfraFSEntry": wsInfraFSEntry,
       "wsInfraFSIndex": wsInfraFSIndex,
       "wsInfraFSName": wsInfraFSName,
       "wsInfraFSAvailable": wsInfraFSAvailable,
       "wsInfraFSFormatted": wsInfraFSFormatted,
       "wsInfraFSFormat": wsInfraFSFormat,
       "wsInfraFileMgmtImportStatus": wsInfraFileMgmtImportStatus,
       "wsInfraFileMgmtMIBConformance": wsInfraFileMgmtMIBConformance,
       "wsInfraFileMgmtMIBGroups": wsInfraFileMgmtMIBGroups,
       "wsInfraFileMgmtGroup": wsInfraFileMgmtGroup,
       "wsInfraFileMgmtMIBCompliances": wsInfraFileMgmtMIBCompliances,
       "wsInfraFileMgmtMIBCompliance": wsInfraFileMgmtMIBCompliance}
)
