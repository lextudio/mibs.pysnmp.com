# SNMP MIB module (CISCO-DATA-COLLECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DATA-COLLECTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:54 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(SnmpTagValue,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagValue")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

ciscoDataCollectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 312)
)
ciscoDataCollectionMIB.setRevisions(
        ("2002-10-30 05:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CdcCollectionSubtree(ObjectIdentifier, TextualConvention):
    status = "current"


class CdcCollectionList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class CdcRowInstanceId(ObjectIdentifier, TextualConvention):
    status = "current"


class CdcUrl(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CdcFileFormat(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cdcBulkASCII", 1),
          ("cdcBulkBinary", 2),
          ("cdcSchemaASCII", 3))
    )



class CdcFileXferStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("aborted", 3),
          ("authFailed", 9),
          ("badDomainName", 5),
          ("fileOpenFailRemote", 4),
          ("fileWriteFailed", 8),
          ("networkFailed", 7),
          ("notStarted", 1),
          ("success", 2),
          ("unreachableIpAddress", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDataCollMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDataCollMIBNotifs = _CiscoDataCollMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 0)
)
_CiscoDataCollMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDataCollMIBObjects = _CiscoDataCollMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1)
)
_CdcVFile_ObjectIdentity = ObjectIdentity
cdcVFile = _CdcVFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1)
)
_CdcVFilePersistentStorage_Type = TruthValue
_CdcVFilePersistentStorage_Object = MibScalar
cdcVFilePersistentStorage = _CdcVFilePersistentStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 1),
    _CdcVFilePersistentStorage_Type()
)
cdcVFilePersistentStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdcVFilePersistentStorage.setStatus("current")


class _CdcVFileMaxSizeHitsLimit_Type(Unsigned32):
    """Custom type cdcVFileMaxSizeHitsLimit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdcVFileMaxSizeHitsLimit_Type.__name__ = "Unsigned32"
_CdcVFileMaxSizeHitsLimit_Object = MibScalar
cdcVFileMaxSizeHitsLimit = _CdcVFileMaxSizeHitsLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 2),
    _CdcVFileMaxSizeHitsLimit_Type()
)
cdcVFileMaxSizeHitsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdcVFileMaxSizeHitsLimit.setStatus("current")
_CdcVFileTable_Object = MibTable
cdcVFileTable = _CdcVFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cdcVFileTable.setStatus("current")
_CdcVFileEntry_Object = MibTableRow
cdcVFileEntry = _CdcVFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1)
)
cdcVFileEntry.setIndexNames(
    (0, "CISCO-DATA-COLLECTION-MIB", "cdcVFileIndex"),
)
if mibBuilder.loadTexts:
    cdcVFileEntry.setStatus("current")


class _CdcVFileIndex_Type(Unsigned32):
    """Custom type cdcVFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdcVFileIndex_Type.__name__ = "Unsigned32"
_CdcVFileIndex_Object = MibTableColumn
cdcVFileIndex = _CdcVFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 1),
    _CdcVFileIndex_Type()
)
cdcVFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdcVFileIndex.setStatus("current")


class _CdcVFileName_Type(DisplayString):
    """Custom type cdcVFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CdcVFileName_Type.__name__ = "DisplayString"
_CdcVFileName_Object = MibTableColumn
cdcVFileName = _CdcVFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 2),
    _CdcVFileName_Type()
)
cdcVFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcVFileName.setStatus("current")


class _CdcVFileDescription_Type(SnmpAdminString):
    """Custom type cdcVFileDescription based on SnmpAdminString"""
    defaultHexValue = ""


_CdcVFileDescription_Object = MibTableColumn
cdcVFileDescription = _CdcVFileDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 3),
    _CdcVFileDescription_Type()
)
cdcVFileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcVFileDescription.setStatus("current")


class _CdcVFileCommand_Type(Integer32):
    """Custom type cdcVFileCommand based on Integer32"""
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
        *(("collectNow", 3),
          ("idle", 1),
          ("swapToNewFile", 2))
    )


_CdcVFileCommand_Type.__name__ = "Integer32"
_CdcVFileCommand_Object = MibTableColumn
cdcVFileCommand = _CdcVFileCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 4),
    _CdcVFileCommand_Type()
)
cdcVFileCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcVFileCommand.setStatus("current")


class _CdcVFileMaxSize_Type(Unsigned32):
    """Custom type cdcVFileMaxSize based on Unsigned32"""
    defaultValue = 50000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 4294967295),
    )


_CdcVFileMaxSize_Type.__name__ = "Unsigned32"
_CdcVFileMaxSize_Object = MibTableColumn
cdcVFileMaxSize = _CdcVFileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 5),
    _CdcVFileMaxSize_Type()
)
cdcVFileMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcVFileMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cdcVFileMaxSize.setUnits("bytes")


class _CdcVFileCurrentSize_Type(Unsigned32):
    """Custom type cdcVFileCurrentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdcVFileCurrentSize_Type.__name__ = "Unsigned32"
_CdcVFileCurrentSize_Object = MibTableColumn
cdcVFileCurrentSize = _CdcVFileCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 6),
    _CdcVFileCurrentSize_Type()
)
cdcVFileCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdcVFileCurrentSize.setStatus("current")
if mibBuilder.loadTexts:
    cdcVFileCurrentSize.setUnits("bytes")


class _CdcVFileFormat_Type(CdcFileFormat):
    """Custom type cdcVFileFormat based on CdcFileFormat"""


_CdcVFileFormat_Object = MibTableColumn
cdcVFileFormat = _CdcVFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 7),
    _CdcVFileFormat_Type()
)
cdcVFileFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcVFileFormat.setStatus("current")


class _CdcVFileCollectMode_Type(Integer32):
    """Custom type cdcVFileCollectMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_CdcVFileCollectMode_Type.__name__ = "Integer32"
_CdcVFileCollectMode_Object = MibTableColumn
cdcVFileCollectMode = _CdcVFileCollectMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 8),
    _CdcVFileCollectMode_Type()
)
cdcVFileCollectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcVFileCollectMode.setStatus("current")


class _CdcVFileCollectionPeriod_Type(Unsigned32):
    """Custom type cdcVFileCollectionPeriod based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 604800),
    )


_CdcVFileCollectionPeriod_Type.__name__ = "Unsigned32"
_CdcVFileCollectionPeriod_Object = MibTableColumn
cdcVFileCollectionPeriod = _CdcVFileCollectionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 9),
    _CdcVFileCollectionPeriod_Type()
)
cdcVFileCollectionPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcVFileCollectionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cdcVFileCollectionPeriod.setUnits("seconds")


class _CdcVFileRetentionPeriod_Type(Unsigned32):
    """Custom type cdcVFileRetentionPeriod based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CdcVFileRetentionPeriod_Type.__name__ = "Unsigned32"
_CdcVFileRetentionPeriod_Object = MibTableColumn
cdcVFileRetentionPeriod = _CdcVFileRetentionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 10),
    _CdcVFileRetentionPeriod_Type()
)
cdcVFileRetentionPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcVFileRetentionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cdcVFileRetentionPeriod.setUnits("seconds")


class _CdcVFileAdminStatus_Type(Integer32):
    """Custom type cdcVFileAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CdcVFileAdminStatus_Type.__name__ = "Integer32"
_CdcVFileAdminStatus_Object = MibTableColumn
cdcVFileAdminStatus = _CdcVFileAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 11),
    _CdcVFileAdminStatus_Type()
)
cdcVFileAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcVFileAdminStatus.setStatus("current")


class _CdcVFileOperStatus_Type(Integer32):
    """Custom type cdcVFileOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("error", 3))
    )


_CdcVFileOperStatus_Type.__name__ = "Integer32"
_CdcVFileOperStatus_Object = MibTableColumn
cdcVFileOperStatus = _CdcVFileOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 12),
    _CdcVFileOperStatus_Type()
)
cdcVFileOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdcVFileOperStatus.setStatus("current")


class _CdcVFileErrorCode_Type(Integer32):
    """Custom type cdcVFileErrorCode based on Integer32"""
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
        *(("noError", 1),
          ("noResource", 7),
          ("noSpace", 3),
          ("openError", 4),
          ("otherError", 2),
          ("tooManyMaxSizeHits", 6),
          ("tooSmallMaxSize", 5))
    )


_CdcVFileErrorCode_Type.__name__ = "Integer32"
_CdcVFileErrorCode_Object = MibTableColumn
cdcVFileErrorCode = _CdcVFileErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 13),
    _CdcVFileErrorCode_Type()
)
cdcVFileErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdcVFileErrorCode.setStatus("current")


class _CdcVFileCollectionErrorEnable_Type(TruthValue):
    """Custom type cdcVFileCollectionErrorEnable based on TruthValue"""


_CdcVFileCollectionErrorEnable_Object = MibTableColumn
cdcVFileCollectionErrorEnable = _CdcVFileCollectionErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 14),
    _CdcVFileCollectionErrorEnable_Type()
)
cdcVFileCollectionErrorEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcVFileCollectionErrorEnable.setStatus("current")
_CdcVFileRowStatus_Type = RowStatus
_CdcVFileRowStatus_Object = MibTableColumn
cdcVFileRowStatus = _CdcVFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 3, 1, 15),
    _CdcVFileRowStatus_Type()
)
cdcVFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcVFileRowStatus.setStatus("current")
_CdcVFileMgmtTable_Object = MibTable
cdcVFileMgmtTable = _CdcVFileMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cdcVFileMgmtTable.setStatus("current")
_CdcVFileMgmtEntry_Object = MibTableRow
cdcVFileMgmtEntry = _CdcVFileMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 4, 1)
)
cdcVFileMgmtEntry.setIndexNames(
    (0, "CISCO-DATA-COLLECTION-MIB", "cdcVFileIndex"),
    (0, "CISCO-DATA-COLLECTION-MIB", "cdcVFileMgmtIndex"),
)
if mibBuilder.loadTexts:
    cdcVFileMgmtEntry.setStatus("current")


class _CdcVFileMgmtIndex_Type(Unsigned32):
    """Custom type cdcVFileMgmtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdcVFileMgmtIndex_Type.__name__ = "Unsigned32"
_CdcVFileMgmtIndex_Object = MibTableColumn
cdcVFileMgmtIndex = _CdcVFileMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 4, 1, 1),
    _CdcVFileMgmtIndex_Type()
)
cdcVFileMgmtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdcVFileMgmtIndex.setStatus("current")
_CdcVFileMgmtName_Type = DisplayString
_CdcVFileMgmtName_Object = MibTableColumn
cdcVFileMgmtName = _CdcVFileMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 4, 1, 2),
    _CdcVFileMgmtName_Type()
)
cdcVFileMgmtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdcVFileMgmtName.setStatus("current")
_CdcVFileMgmtTimestamp_Type = DateAndTime
_CdcVFileMgmtTimestamp_Object = MibTableColumn
cdcVFileMgmtTimestamp = _CdcVFileMgmtTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 4, 1, 3),
    _CdcVFileMgmtTimestamp_Type()
)
cdcVFileMgmtTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdcVFileMgmtTimestamp.setStatus("current")


class _CdcVFileMgmtTimeToLive_Type(Unsigned32):
    """Custom type cdcVFileMgmtTimeToLive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CdcVFileMgmtTimeToLive_Type.__name__ = "Unsigned32"
_CdcVFileMgmtTimeToLive_Object = MibTableColumn
cdcVFileMgmtTimeToLive = _CdcVFileMgmtTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 4, 1, 4),
    _CdcVFileMgmtTimeToLive_Type()
)
cdcVFileMgmtTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdcVFileMgmtTimeToLive.setStatus("current")
if mibBuilder.loadTexts:
    cdcVFileMgmtTimeToLive.setUnits("seconds")


class _CdcVFileMgmtCommand_Type(Integer32):
    """Custom type cdcVFileMgmtCommand based on Integer32"""
    defaultValue = 1

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
        *(("abortTransfer", 4),
          ("delete", 2),
          ("idle", 1),
          ("transfer", 3))
    )


_CdcVFileMgmtCommand_Type.__name__ = "Integer32"
_CdcVFileMgmtCommand_Object = MibTableColumn
cdcVFileMgmtCommand = _CdcVFileMgmtCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 4, 1, 5),
    _CdcVFileMgmtCommand_Type()
)
cdcVFileMgmtCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdcVFileMgmtCommand.setStatus("current")
_CdcVFileMgmtXferURL_Type = CdcUrl
_CdcVFileMgmtXferURL_Object = MibTableColumn
cdcVFileMgmtXferURL = _CdcVFileMgmtXferURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 4, 1, 6),
    _CdcVFileMgmtXferURL_Type()
)
cdcVFileMgmtXferURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdcVFileMgmtXferURL.setStatus("current")
_CdcVFileMgmtLastXferStatus_Type = CdcFileXferStatus
_CdcVFileMgmtLastXferStatus_Object = MibTableColumn
cdcVFileMgmtLastXferStatus = _CdcVFileMgmtLastXferStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 4, 1, 7),
    _CdcVFileMgmtLastXferStatus_Type()
)
cdcVFileMgmtLastXferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdcVFileMgmtLastXferStatus.setStatus("current")
_CdcVFileMgmtLastXferURL_Type = CdcUrl
_CdcVFileMgmtLastXferURL_Object = MibTableColumn
cdcVFileMgmtLastXferURL = _CdcVFileMgmtLastXferURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 1, 4, 1, 8),
    _CdcVFileMgmtLastXferURL_Type()
)
cdcVFileMgmtLastXferURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdcVFileMgmtLastXferURL.setStatus("current")
_CdcDataGroup_ObjectIdentity = ObjectIdentity
cdcDataGroup = _CdcDataGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2)
)
_CdcDGTable_Object = MibTable
cdcDGTable = _CdcDGTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdcDGTable.setStatus("current")
_CdcDGEntry_Object = MibTableRow
cdcDGEntry = _CdcDGEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1, 1)
)
cdcDGEntry.setIndexNames(
    (0, "CISCO-DATA-COLLECTION-MIB", "cdcDGIndex"),
)
if mibBuilder.loadTexts:
    cdcDGEntry.setStatus("current")


class _CdcDGIndex_Type(Unsigned32):
    """Custom type cdcDGIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdcDGIndex_Type.__name__ = "Unsigned32"
_CdcDGIndex_Object = MibTableColumn
cdcDGIndex = _CdcDGIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1, 1, 1),
    _CdcDGIndex_Type()
)
cdcDGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdcDGIndex.setStatus("current")


class _CdcDGComment_Type(SnmpAdminString):
    """Custom type cdcDGComment based on SnmpAdminString"""
    defaultHexValue = ""


_CdcDGComment_Object = MibTableColumn
cdcDGComment = _CdcDGComment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1, 1, 2),
    _CdcDGComment_Type()
)
cdcDGComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGComment.setStatus("current")


class _CdcDGType_Type(Integer32):
    """Custom type cdcDGType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("object", 1),
          ("table", 2))
    )


_CdcDGType_Type.__name__ = "Integer32"
_CdcDGType_Object = MibTableColumn
cdcDGType = _CdcDGType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1, 1, 3),
    _CdcDGType_Type()
)
cdcDGType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGType.setStatus("current")


class _CdcDGVFileIndex_Type(Unsigned32):
    """Custom type cdcDGVFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdcDGVFileIndex_Type.__name__ = "Unsigned32"
_CdcDGVFileIndex_Object = MibTableColumn
cdcDGVFileIndex = _CdcDGVFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1, 1, 4),
    _CdcDGVFileIndex_Type()
)
cdcDGVFileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGVFileIndex.setStatus("current")


class _CdcDGTargetTag_Type(SnmpTagValue):
    """Custom type cdcDGTargetTag based on SnmpTagValue"""
    defaultHexValue = ""


_CdcDGTargetTag_Object = MibTableColumn
cdcDGTargetTag = _CdcDGTargetTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1, 1, 5),
    _CdcDGTargetTag_Type()
)
cdcDGTargetTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGTargetTag.setStatus("current")


class _CdcDGContextName_Type(SnmpAdminString):
    """Custom type cdcDGContextName based on SnmpAdminString"""
    defaultHexValue = ""


_CdcDGContextName_Object = MibTableColumn
cdcDGContextName = _CdcDGContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1, 1, 6),
    _CdcDGContextName_Type()
)
cdcDGContextName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGContextName.setStatus("current")


class _CdcDGObject_Type(VariablePointer):
    """Custom type cdcDGObject based on VariablePointer"""
    defaultValue = (0, 0)


_CdcDGObject_Object = MibTableColumn
cdcDGObject = _CdcDGObject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1, 1, 7),
    _CdcDGObject_Type()
)
cdcDGObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGObject.setStatus("current")


class _CdcDGObjectGrpIndex_Type(Unsigned32):
    """Custom type cdcDGObjectGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdcDGObjectGrpIndex_Type.__name__ = "Unsigned32"
_CdcDGObjectGrpIndex_Object = MibTableColumn
cdcDGObjectGrpIndex = _CdcDGObjectGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1, 1, 8),
    _CdcDGObjectGrpIndex_Type()
)
cdcDGObjectGrpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGObjectGrpIndex.setStatus("current")


class _CdcDGInstGrpIndex_Type(Unsigned32):
    """Custom type cdcDGInstGrpIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdcDGInstGrpIndex_Type.__name__ = "Unsigned32"
_CdcDGInstGrpIndex_Object = MibTableColumn
cdcDGInstGrpIndex = _CdcDGInstGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1, 1, 9),
    _CdcDGInstGrpIndex_Type()
)
cdcDGInstGrpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGInstGrpIndex.setStatus("current")


class _CdcDGPollPeriod_Type(Unsigned32):
    """Custom type cdcDGPollPeriod based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CdcDGPollPeriod_Type.__name__ = "Unsigned32"
_CdcDGPollPeriod_Object = MibTableColumn
cdcDGPollPeriod = _CdcDGPollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1, 1, 10),
    _CdcDGPollPeriod_Type()
)
cdcDGPollPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGPollPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cdcDGPollPeriod.setUnits("seconds")
_CdcDGRowStatus_Type = RowStatus
_CdcDGRowStatus_Object = MibTableColumn
cdcDGRowStatus = _CdcDGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 1, 1, 11),
    _CdcDGRowStatus_Type()
)
cdcDGRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGRowStatus.setStatus("current")
_CdcDGBaseObjectTable_Object = MibTable
cdcDGBaseObjectTable = _CdcDGBaseObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cdcDGBaseObjectTable.setStatus("current")
_CdcDGBaseObjectEntry_Object = MibTableRow
cdcDGBaseObjectEntry = _CdcDGBaseObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 2, 1)
)
cdcDGBaseObjectEntry.setIndexNames(
    (0, "CISCO-DATA-COLLECTION-MIB", "cdcDGBaseObjectGrpIndex"),
    (0, "CISCO-DATA-COLLECTION-MIB", "cdcDGBaseObjectIndex"),
)
if mibBuilder.loadTexts:
    cdcDGBaseObjectEntry.setStatus("current")


class _CdcDGBaseObjectGrpIndex_Type(Unsigned32):
    """Custom type cdcDGBaseObjectGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdcDGBaseObjectGrpIndex_Type.__name__ = "Unsigned32"
_CdcDGBaseObjectGrpIndex_Object = MibTableColumn
cdcDGBaseObjectGrpIndex = _CdcDGBaseObjectGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 2, 1, 1),
    _CdcDGBaseObjectGrpIndex_Type()
)
cdcDGBaseObjectGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdcDGBaseObjectGrpIndex.setStatus("current")


class _CdcDGBaseObjectIndex_Type(Unsigned32):
    """Custom type cdcDGBaseObjectIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdcDGBaseObjectIndex_Type.__name__ = "Unsigned32"
_CdcDGBaseObjectIndex_Object = MibTableColumn
cdcDGBaseObjectIndex = _CdcDGBaseObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 2, 1, 2),
    _CdcDGBaseObjectIndex_Type()
)
cdcDGBaseObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdcDGBaseObjectIndex.setStatus("current")
_CdcDGBaseObjectSubtree_Type = CdcCollectionSubtree
_CdcDGBaseObjectSubtree_Object = MibTableColumn
cdcDGBaseObjectSubtree = _CdcDGBaseObjectSubtree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 2, 1, 3),
    _CdcDGBaseObjectSubtree_Type()
)
cdcDGBaseObjectSubtree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGBaseObjectSubtree.setStatus("current")
_CdcDGBaseObjectList_Type = CdcCollectionList
_CdcDGBaseObjectList_Object = MibTableColumn
cdcDGBaseObjectList = _CdcDGBaseObjectList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 2, 1, 4),
    _CdcDGBaseObjectList_Type()
)
cdcDGBaseObjectList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGBaseObjectList.setStatus("current")
_CdcDGBaseObjectRowStatus_Type = RowStatus
_CdcDGBaseObjectRowStatus_Object = MibTableColumn
cdcDGBaseObjectRowStatus = _CdcDGBaseObjectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 2, 1, 5),
    _CdcDGBaseObjectRowStatus_Type()
)
cdcDGBaseObjectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGBaseObjectRowStatus.setStatus("current")
_CdcDGInstanceTable_Object = MibTable
cdcDGInstanceTable = _CdcDGInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cdcDGInstanceTable.setStatus("current")
_CdcDGInstanceEntry_Object = MibTableRow
cdcDGInstanceEntry = _CdcDGInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 3, 1)
)
cdcDGInstanceEntry.setIndexNames(
    (0, "CISCO-DATA-COLLECTION-MIB", "cdcDGInstanceGrpIndex"),
    (0, "CISCO-DATA-COLLECTION-MIB", "cdcDGInstanceIndex"),
)
if mibBuilder.loadTexts:
    cdcDGInstanceEntry.setStatus("current")


class _CdcDGInstanceGrpIndex_Type(Unsigned32):
    """Custom type cdcDGInstanceGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdcDGInstanceGrpIndex_Type.__name__ = "Unsigned32"
_CdcDGInstanceGrpIndex_Object = MibTableColumn
cdcDGInstanceGrpIndex = _CdcDGInstanceGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 3, 1, 1),
    _CdcDGInstanceGrpIndex_Type()
)
cdcDGInstanceGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdcDGInstanceGrpIndex.setStatus("current")


class _CdcDGInstanceIndex_Type(Unsigned32):
    """Custom type cdcDGInstanceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdcDGInstanceIndex_Type.__name__ = "Unsigned32"
_CdcDGInstanceIndex_Object = MibTableColumn
cdcDGInstanceIndex = _CdcDGInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 3, 1, 2),
    _CdcDGInstanceIndex_Type()
)
cdcDGInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdcDGInstanceIndex.setStatus("current")


class _CdcDGInstanceType_Type(Integer32):
    """Custom type cdcDGInstanceType based on Integer32"""
    defaultValue = 4

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
        *(("individual", 1),
          ("other", 5),
          ("range", 2),
          ("repititions", 3),
          ("subTree", 4))
    )


_CdcDGInstanceType_Type.__name__ = "Integer32"
_CdcDGInstanceType_Object = MibTableColumn
cdcDGInstanceType = _CdcDGInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 3, 1, 3),
    _CdcDGInstanceType_Type()
)
cdcDGInstanceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGInstanceType.setStatus("current")


class _CdcDGInstanceOid_Type(CdcRowInstanceId):
    """Custom type cdcDGInstanceOid based on CdcRowInstanceId"""
    defaultValue = (0, 0)


_CdcDGInstanceOid_Object = MibTableColumn
cdcDGInstanceOid = _CdcDGInstanceOid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 3, 1, 4),
    _CdcDGInstanceOid_Type()
)
cdcDGInstanceOid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGInstanceOid.setStatus("current")


class _CdcDGInstanceOidEnd_Type(CdcRowInstanceId):
    """Custom type cdcDGInstanceOidEnd based on CdcRowInstanceId"""
    defaultValue = (0, 0)


_CdcDGInstanceOidEnd_Object = MibTableColumn
cdcDGInstanceOidEnd = _CdcDGInstanceOidEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 3, 1, 5),
    _CdcDGInstanceOidEnd_Type()
)
cdcDGInstanceOidEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGInstanceOidEnd.setStatus("current")


class _CdcDGInstanceNumRepititions_Type(Unsigned32):
    """Custom type cdcDGInstanceNumRepititions based on Unsigned32"""
    defaultValue = 1


_CdcDGInstanceNumRepititions_Object = MibTableColumn
cdcDGInstanceNumRepititions = _CdcDGInstanceNumRepititions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 3, 1, 6),
    _CdcDGInstanceNumRepititions_Type()
)
cdcDGInstanceNumRepititions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGInstanceNumRepititions.setStatus("current")


class _CdcDGInstanceOtherPtr_Type(RowPointer):
    """Custom type cdcDGInstanceOtherPtr based on RowPointer"""
    defaultValue = (0, 0)


_CdcDGInstanceOtherPtr_Object = MibTableColumn
cdcDGInstanceOtherPtr = _CdcDGInstanceOtherPtr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 3, 1, 7),
    _CdcDGInstanceOtherPtr_Type()
)
cdcDGInstanceOtherPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGInstanceOtherPtr.setStatus("current")
_CdcDGInstanceRowStatus_Type = RowStatus
_CdcDGInstanceRowStatus_Object = MibTableColumn
cdcDGInstanceRowStatus = _CdcDGInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 2, 3, 1, 8),
    _CdcDGInstanceRowStatus_Type()
)
cdcDGInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcDGInstanceRowStatus.setStatus("current")
_CdcFileXfer_ObjectIdentity = ObjectIdentity
cdcFileXfer = _CdcFileXfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 3)
)
_CdcFileXferConfTable_Object = MibTable
cdcFileXferConfTable = _CdcFileXferConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdcFileXferConfTable.setStatus("current")
_CdcFileXferConfEntry_Object = MibTableRow
cdcFileXferConfEntry = _CdcFileXferConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 3, 1, 1)
)
cdcFileXferConfEntry.setIndexNames(
    (0, "CISCO-DATA-COLLECTION-MIB", "cdcVFileIndex"),
)
if mibBuilder.loadTexts:
    cdcFileXferConfEntry.setStatus("current")
_CdcFileXferConfPriUrl_Type = CdcUrl
_CdcFileXferConfPriUrl_Object = MibTableColumn
cdcFileXferConfPriUrl = _CdcFileXferConfPriUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 3, 1, 1, 1),
    _CdcFileXferConfPriUrl_Type()
)
cdcFileXferConfPriUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcFileXferConfPriUrl.setStatus("current")
_CdcFileXferConfSecUrl_Type = CdcUrl
_CdcFileXferConfSecUrl_Object = MibTableColumn
cdcFileXferConfSecUrl = _CdcFileXferConfSecUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 3, 1, 1, 2),
    _CdcFileXferConfSecUrl_Type()
)
cdcFileXferConfSecUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcFileXferConfSecUrl.setStatus("current")


class _CdcFileXferConfRetryPeriod_Type(Unsigned32):
    """Custom type cdcFileXferConfRetryPeriod based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CdcFileXferConfRetryPeriod_Type.__name__ = "Unsigned32"
_CdcFileXferConfRetryPeriod_Object = MibTableColumn
cdcFileXferConfRetryPeriod = _CdcFileXferConfRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 3, 1, 1, 3),
    _CdcFileXferConfRetryPeriod_Type()
)
cdcFileXferConfRetryPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcFileXferConfRetryPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cdcFileXferConfRetryPeriod.setUnits("seconds")


class _CdcFileXferConfRetryCount_Type(Unsigned32):
    """Custom type cdcFileXferConfRetryCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CdcFileXferConfRetryCount_Type.__name__ = "Unsigned32"
_CdcFileXferConfRetryCount_Object = MibTableColumn
cdcFileXferConfRetryCount = _CdcFileXferConfRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 3, 1, 1, 4),
    _CdcFileXferConfRetryCount_Type()
)
cdcFileXferConfRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcFileXferConfRetryCount.setStatus("current")
if mibBuilder.loadTexts:
    cdcFileXferConfRetryCount.setUnits("seconds")


class _CdcFileXferConfSuccessEnable_Type(TruthValue):
    """Custom type cdcFileXferConfSuccessEnable based on TruthValue"""


_CdcFileXferConfSuccessEnable_Object = MibTableColumn
cdcFileXferConfSuccessEnable = _CdcFileXferConfSuccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 3, 1, 1, 5),
    _CdcFileXferConfSuccessEnable_Type()
)
cdcFileXferConfSuccessEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcFileXferConfSuccessEnable.setStatus("current")


class _CdcFileXferConfFailureEnable_Type(TruthValue):
    """Custom type cdcFileXferConfFailureEnable based on TruthValue"""


_CdcFileXferConfFailureEnable_Object = MibTableColumn
cdcFileXferConfFailureEnable = _CdcFileXferConfFailureEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 1, 3, 1, 1, 6),
    _CdcFileXferConfFailureEnable_Type()
)
cdcFileXferConfFailureEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdcFileXferConfFailureEnable.setStatus("current")
_CiscoDataCollMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDataCollMIBConformance = _CiscoDataCollMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 2)
)
_CiscoDataCollMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDataCollMIBCompliances = _CiscoDataCollMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 2, 1)
)
_CiscoDataCollMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDataCollMIBGroups = _CiscoDataCollMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 2, 2)
)

# Managed Objects groups

cdcVFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 2, 2, 1)
)
cdcVFileGroup.setObjects(
      *(("CISCO-DATA-COLLECTION-MIB", "cdcVFilePersistentStorage"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileMaxSizeHitsLimit"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileName"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileDescription"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileCommand"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileMaxSize"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileCurrentSize"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileFormat"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileCollectMode"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileCollectionPeriod"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileRetentionPeriod"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileAdminStatus"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileOperStatus"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileErrorCode"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileRowStatus"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileMgmtName"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileMgmtTimestamp"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileMgmtTimeToLive"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileMgmtCommand"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileMgmtXferURL"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileMgmtLastXferStatus"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileMgmtLastXferURL"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileCollectionErrorEnable"))
)
if mibBuilder.loadTexts:
    cdcVFileGroup.setStatus("current")

cdcDataSelectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 2, 2, 2)
)
cdcDataSelectionGroup.setObjects(
      *(("CISCO-DATA-COLLECTION-MIB", "cdcDGComment"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGType"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGVFileIndex"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGTargetTag"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGContextName"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGObject"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGObjectGrpIndex"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGInstGrpIndex"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGPollPeriod"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGRowStatus"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGBaseObjectSubtree"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGBaseObjectList"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGBaseObjectRowStatus"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGInstanceType"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGInstanceOid"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGInstanceOidEnd"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGInstanceNumRepititions"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGInstanceOtherPtr"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcDGInstanceRowStatus"))
)
if mibBuilder.loadTexts:
    cdcDataSelectionGroup.setStatus("current")

cdcFileXferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 2, 2, 3)
)
cdcFileXferGroup.setObjects(
      *(("CISCO-DATA-COLLECTION-MIB", "cdcFileXferConfPriUrl"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcFileXferConfSecUrl"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcFileXferConfRetryPeriod"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcFileXferConfRetryCount"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcFileXferConfSuccessEnable"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcFileXferConfFailureEnable"))
)
if mibBuilder.loadTexts:
    cdcFileXferGroup.setStatus("current")


# Notification objects

cdcVFileCollectionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 0, 1)
)
cdcVFileCollectionError.setObjects(
      *(("CISCO-DATA-COLLECTION-MIB", "cdcVFileName"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileErrorCode"))
)
if mibBuilder.loadTexts:
    cdcVFileCollectionError.setStatus(
        "current"
    )

cdcFileXferComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 0, 2)
)
cdcFileXferComplete.setObjects(
      *(("CISCO-DATA-COLLECTION-MIB", "cdcVFileMgmtLastXferStatus"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcVFileMgmtLastXferURL"))
)
if mibBuilder.loadTexts:
    cdcFileXferComplete.setStatus(
        "current"
    )


# Notifications groups

cdcNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 2, 2, 4)
)
cdcNotificationGroup.setObjects(
      *(("CISCO-DATA-COLLECTION-MIB", "cdcVFileCollectionError"),
        ("CISCO-DATA-COLLECTION-MIB", "cdcFileXferComplete"))
)
if mibBuilder.loadTexts:
    cdcNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDataCollMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 312, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDataCollMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DATA-COLLECTION-MIB",
    **{"CdcCollectionSubtree": CdcCollectionSubtree,
       "CdcCollectionList": CdcCollectionList,
       "CdcRowInstanceId": CdcRowInstanceId,
       "CdcUrl": CdcUrl,
       "CdcFileFormat": CdcFileFormat,
       "CdcFileXferStatus": CdcFileXferStatus,
       "ciscoDataCollectionMIB": ciscoDataCollectionMIB,
       "ciscoDataCollMIBNotifs": ciscoDataCollMIBNotifs,
       "cdcVFileCollectionError": cdcVFileCollectionError,
       "cdcFileXferComplete": cdcFileXferComplete,
       "ciscoDataCollMIBObjects": ciscoDataCollMIBObjects,
       "cdcVFile": cdcVFile,
       "cdcVFilePersistentStorage": cdcVFilePersistentStorage,
       "cdcVFileMaxSizeHitsLimit": cdcVFileMaxSizeHitsLimit,
       "cdcVFileTable": cdcVFileTable,
       "cdcVFileEntry": cdcVFileEntry,
       "cdcVFileIndex": cdcVFileIndex,
       "cdcVFileName": cdcVFileName,
       "cdcVFileDescription": cdcVFileDescription,
       "cdcVFileCommand": cdcVFileCommand,
       "cdcVFileMaxSize": cdcVFileMaxSize,
       "cdcVFileCurrentSize": cdcVFileCurrentSize,
       "cdcVFileFormat": cdcVFileFormat,
       "cdcVFileCollectMode": cdcVFileCollectMode,
       "cdcVFileCollectionPeriod": cdcVFileCollectionPeriod,
       "cdcVFileRetentionPeriod": cdcVFileRetentionPeriod,
       "cdcVFileAdminStatus": cdcVFileAdminStatus,
       "cdcVFileOperStatus": cdcVFileOperStatus,
       "cdcVFileErrorCode": cdcVFileErrorCode,
       "cdcVFileCollectionErrorEnable": cdcVFileCollectionErrorEnable,
       "cdcVFileRowStatus": cdcVFileRowStatus,
       "cdcVFileMgmtTable": cdcVFileMgmtTable,
       "cdcVFileMgmtEntry": cdcVFileMgmtEntry,
       "cdcVFileMgmtIndex": cdcVFileMgmtIndex,
       "cdcVFileMgmtName": cdcVFileMgmtName,
       "cdcVFileMgmtTimestamp": cdcVFileMgmtTimestamp,
       "cdcVFileMgmtTimeToLive": cdcVFileMgmtTimeToLive,
       "cdcVFileMgmtCommand": cdcVFileMgmtCommand,
       "cdcVFileMgmtXferURL": cdcVFileMgmtXferURL,
       "cdcVFileMgmtLastXferStatus": cdcVFileMgmtLastXferStatus,
       "cdcVFileMgmtLastXferURL": cdcVFileMgmtLastXferURL,
       "cdcDataGroup": cdcDataGroup,
       "cdcDGTable": cdcDGTable,
       "cdcDGEntry": cdcDGEntry,
       "cdcDGIndex": cdcDGIndex,
       "cdcDGComment": cdcDGComment,
       "cdcDGType": cdcDGType,
       "cdcDGVFileIndex": cdcDGVFileIndex,
       "cdcDGTargetTag": cdcDGTargetTag,
       "cdcDGContextName": cdcDGContextName,
       "cdcDGObject": cdcDGObject,
       "cdcDGObjectGrpIndex": cdcDGObjectGrpIndex,
       "cdcDGInstGrpIndex": cdcDGInstGrpIndex,
       "cdcDGPollPeriod": cdcDGPollPeriod,
       "cdcDGRowStatus": cdcDGRowStatus,
       "cdcDGBaseObjectTable": cdcDGBaseObjectTable,
       "cdcDGBaseObjectEntry": cdcDGBaseObjectEntry,
       "cdcDGBaseObjectGrpIndex": cdcDGBaseObjectGrpIndex,
       "cdcDGBaseObjectIndex": cdcDGBaseObjectIndex,
       "cdcDGBaseObjectSubtree": cdcDGBaseObjectSubtree,
       "cdcDGBaseObjectList": cdcDGBaseObjectList,
       "cdcDGBaseObjectRowStatus": cdcDGBaseObjectRowStatus,
       "cdcDGInstanceTable": cdcDGInstanceTable,
       "cdcDGInstanceEntry": cdcDGInstanceEntry,
       "cdcDGInstanceGrpIndex": cdcDGInstanceGrpIndex,
       "cdcDGInstanceIndex": cdcDGInstanceIndex,
       "cdcDGInstanceType": cdcDGInstanceType,
       "cdcDGInstanceOid": cdcDGInstanceOid,
       "cdcDGInstanceOidEnd": cdcDGInstanceOidEnd,
       "cdcDGInstanceNumRepititions": cdcDGInstanceNumRepititions,
       "cdcDGInstanceOtherPtr": cdcDGInstanceOtherPtr,
       "cdcDGInstanceRowStatus": cdcDGInstanceRowStatus,
       "cdcFileXfer": cdcFileXfer,
       "cdcFileXferConfTable": cdcFileXferConfTable,
       "cdcFileXferConfEntry": cdcFileXferConfEntry,
       "cdcFileXferConfPriUrl": cdcFileXferConfPriUrl,
       "cdcFileXferConfSecUrl": cdcFileXferConfSecUrl,
       "cdcFileXferConfRetryPeriod": cdcFileXferConfRetryPeriod,
       "cdcFileXferConfRetryCount": cdcFileXferConfRetryCount,
       "cdcFileXferConfSuccessEnable": cdcFileXferConfSuccessEnable,
       "cdcFileXferConfFailureEnable": cdcFileXferConfFailureEnable,
       "ciscoDataCollMIBConformance": ciscoDataCollMIBConformance,
       "ciscoDataCollMIBCompliances": ciscoDataCollMIBCompliances,
       "ciscoDataCollMIBCompliance": ciscoDataCollMIBCompliance,
       "ciscoDataCollMIBGroups": ciscoDataCollMIBGroups,
       "cdcVFileGroup": cdcVFileGroup,
       "cdcDataSelectionGroup": cdcDataSelectionGroup,
       "cdcFileXferGroup": cdcFileXferGroup,
       "cdcNotificationGroup": cdcNotificationGroup}
)
