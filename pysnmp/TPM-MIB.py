# SNMP MIB module (TPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:52 2024
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

(AppLocalIndex,
 DataSourceOrZero,
 RmonClientID,
 TransactionAggregationType,
 apmAppDirAppLocalIndex,
 apmAppDirResponsivenessType,
 apmExceptionGroup,
 apmExceptionIndex,
 apmReportGroup) = mibBuilder.importSymbols(
    "APM-MIB",
    "AppLocalIndex",
    "DataSourceOrZero",
    "RmonClientID",
    "TransactionAggregationType",
    "apmAppDirAppLocalIndex",
    "apmAppDirResponsivenessType",
    "apmExceptionGroup",
    "apmExceptionIndex",
    "apmReportGroup")

(ZeroBasedCounter64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "ZeroBasedCounter64")

(OwnerString,
 rmon) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
    "rmon")

(ZeroBasedCounter32,
 protocolDirLocalIndex) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32",
    "protocolDirLocalIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")

(SspmClockMaxSkew,
 SspmClockSource,
 SspmMicroSeconds) = mibBuilder.importSymbols(
    "SSPM-MIB",
    "SspmClockMaxSkew",
    "SspmClockSource",
    "SspmMicroSeconds")


# MODULE-IDENTITY

tpmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 30)
)
tpmMIB.setRevisions(
        ("2005-07-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TpmTransactionMetricIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TpmMetricDefID(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_TpmCapabilities_ObjectIdentity = ObjectIdentity
tpmCapabilities = _TpmCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 30, 1)
)
_TpmClockResolution_Type = SspmMicroSeconds
_TpmClockResolution_Object = MibScalar
tpmClockResolution = _TpmClockResolution_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 1),
    _TpmClockResolution_Type()
)
tpmClockResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmClockResolution.setStatus("current")
_TpmClockMaxSkew_Type = SspmClockMaxSkew
_TpmClockMaxSkew_Object = MibScalar
tpmClockMaxSkew = _TpmClockMaxSkew_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 2),
    _TpmClockMaxSkew_Type()
)
tpmClockMaxSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmClockMaxSkew.setStatus("current")
_TpmClockSource_Type = SspmClockSource
_TpmClockSource_Object = MibScalar
tpmClockSource = _TpmClockSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 3),
    _TpmClockSource_Type()
)
tpmClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmClockSource.setStatus("current")
_TpmTransMetricDirLastChange_Type = TimeStamp
_TpmTransMetricDirLastChange_Object = MibScalar
tpmTransMetricDirLastChange = _TpmTransMetricDirLastChange_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 4),
    _TpmTransMetricDirLastChange_Type()
)
tpmTransMetricDirLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmTransMetricDirLastChange.setStatus("current")
_TpmTransMetricDirTable_Object = MibTable
tpmTransMetricDirTable = _TpmTransMetricDirTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 5)
)
if mibBuilder.loadTexts:
    tpmTransMetricDirTable.setStatus("current")
_TpmTransMetricDirEntry_Object = MibTableRow
tpmTransMetricDirEntry = _TpmTransMetricDirEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 5, 1)
)
tpmTransMetricDirEntry.setIndexNames(
    (0, "TPM-MIB", "tpmTransMetricAppLocalIndex"),
    (0, "TPM-MIB", "tpmTransMetricIndex"),
)
if mibBuilder.loadTexts:
    tpmTransMetricDirEntry.setStatus("current")
_TpmTransMetricAppLocalIndex_Type = AppLocalIndex
_TpmTransMetricAppLocalIndex_Object = MibTableColumn
tpmTransMetricAppLocalIndex = _TpmTransMetricAppLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 5, 1, 1),
    _TpmTransMetricAppLocalIndex_Type()
)
tpmTransMetricAppLocalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmTransMetricAppLocalIndex.setStatus("current")
_TpmTransMetricIndex_Type = TpmTransactionMetricIndex
_TpmTransMetricIndex_Object = MibTableColumn
tpmTransMetricIndex = _TpmTransMetricIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 5, 1, 2),
    _TpmTransMetricIndex_Type()
)
tpmTransMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmTransMetricIndex.setStatus("current")


class _TpmTransMetricProtocolIndex_Type(Unsigned32):
    """Custom type tpmTransMetricProtocolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TpmTransMetricProtocolIndex_Type.__name__ = "Unsigned32"
_TpmTransMetricProtocolIndex_Object = MibTableColumn
tpmTransMetricProtocolIndex = _TpmTransMetricProtocolIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 5, 1, 3),
    _TpmTransMetricProtocolIndex_Type()
)
tpmTransMetricProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmTransMetricProtocolIndex.setStatus("current")


class _TpmTransMetricMetricIndex_Type(Unsigned32):
    """Custom type tpmTransMetricMetricIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TpmTransMetricMetricIndex_Type.__name__ = "Unsigned32"
_TpmTransMetricMetricIndex_Object = MibTableColumn
tpmTransMetricMetricIndex = _TpmTransMetricMetricIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 5, 1, 4),
    _TpmTransMetricMetricIndex_Type()
)
tpmTransMetricMetricIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmTransMetricMetricIndex.setStatus("current")


class _TpmTransMetricDirConfig_Type(Integer32):
    """Custom type tpmTransMetricDirConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supportedOff", 2),
          ("supportedOn", 3))
    )


_TpmTransMetricDirConfig_Type.__name__ = "Integer32"
_TpmTransMetricDirConfig_Object = MibTableColumn
tpmTransMetricDirConfig = _TpmTransMetricDirConfig_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 5, 1, 5),
    _TpmTransMetricDirConfig_Type()
)
tpmTransMetricDirConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpmTransMetricDirConfig.setStatus("current")
_TpmMetricDefTable_Object = MibTable
tpmMetricDefTable = _TpmMetricDefTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 6)
)
if mibBuilder.loadTexts:
    tpmMetricDefTable.setStatus("current")
_TpmMetricDefEntry_Object = MibTableRow
tpmMetricDefEntry = _TpmMetricDefEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1)
)
tpmMetricDefEntry.setIndexNames(
    (0, "TPM-MIB", "tpmMetricDefinitionID"),
)
if mibBuilder.loadTexts:
    tpmMetricDefEntry.setStatus("current")
_TpmMetricDefinitionID_Type = TpmMetricDefID
_TpmMetricDefinitionID_Object = MibTableColumn
tpmMetricDefinitionID = _TpmMetricDefinitionID_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1, 1),
    _TpmMetricDefinitionID_Type()
)
tpmMetricDefinitionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmMetricDefinitionID.setStatus("current")


class _TpmMetricDefType_Type(Integer32):
    """Custom type tpmMetricDefType based on Integer32"""
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
        *(("connectMetric", 2),
          ("delayMetric", 3),
          ("lossMetric", 4),
          ("other", 1))
    )


_TpmMetricDefType_Type.__name__ = "Integer32"
_TpmMetricDefType_Object = MibTableColumn
tpmMetricDefType = _TpmMetricDefType_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1, 2),
    _TpmMetricDefType_Type()
)
tpmMetricDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmMetricDefType.setStatus("current")


class _TpmMetricDefDirType_Type(Integer32):
    """Custom type tpmMetricDefDirType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiWay", 3),
          ("oneWay", 1),
          ("twoWay", 2))
    )


_TpmMetricDefDirType_Type.__name__ = "Integer32"
_TpmMetricDefDirType_Object = MibTableColumn
tpmMetricDefDirType = _TpmMetricDefDirType_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1, 3),
    _TpmMetricDefDirType_Type()
)
tpmMetricDefDirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmMetricDefDirType.setStatus("current")
_TpmMetricDefName_Type = SnmpAdminString
_TpmMetricDefName_Object = MibTableColumn
tpmMetricDefName = _TpmMetricDefName_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1, 4),
    _TpmMetricDefName_Type()
)
tpmMetricDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmMetricDefName.setStatus("current")
_TpmMetricDefReference_Type = SnmpAdminString
_TpmMetricDefReference_Object = MibTableColumn
tpmMetricDefReference = _TpmMetricDefReference_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1, 5),
    _TpmMetricDefReference_Type()
)
tpmMetricDefReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmMetricDefReference.setStatus("current")
_TpmMetricDefGlobalID_Type = ObjectIdentifier
_TpmMetricDefGlobalID_Object = MibTableColumn
tpmMetricDefGlobalID = _TpmMetricDefGlobalID_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1, 6),
    _TpmMetricDefGlobalID_Type()
)
tpmMetricDefGlobalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmMetricDefGlobalID.setStatus("current")
_TpmReports_ObjectIdentity = ObjectIdentity
tpmReports = _TpmReports_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 30, 2)
)
_TpmAggrReportCntrlTable_Object = MibTable
tpmAggrReportCntrlTable = _TpmAggrReportCntrlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1)
)
if mibBuilder.loadTexts:
    tpmAggrReportCntrlTable.setStatus("current")
_TpmAggrReportCntrlEntry_Object = MibTableRow
tpmAggrReportCntrlEntry = _TpmAggrReportCntrlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1)
)
tpmAggrReportCntrlEntry.setIndexNames(
    (0, "TPM-MIB", "tpmAggrReportCntrlIndex"),
)
if mibBuilder.loadTexts:
    tpmAggrReportCntrlEntry.setStatus("current")


class _TpmAggrReportCntrlIndex_Type(Unsigned32):
    """Custom type tpmAggrReportCntrlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TpmAggrReportCntrlIndex_Type.__name__ = "Unsigned32"
_TpmAggrReportCntrlIndex_Object = MibTableColumn
tpmAggrReportCntrlIndex = _TpmAggrReportCntrlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 1),
    _TpmAggrReportCntrlIndex_Type()
)
tpmAggrReportCntrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlIndex.setStatus("current")


class _TpmAggrReportCntrlApmCntrlIndex_Type(Unsigned32):
    """Custom type tpmAggrReportCntrlApmCntrlIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TpmAggrReportCntrlApmCntrlIndex_Type.__name__ = "Unsigned32"
_TpmAggrReportCntrlApmCntrlIndex_Object = MibTableColumn
tpmAggrReportCntrlApmCntrlIndex = _TpmAggrReportCntrlApmCntrlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 2),
    _TpmAggrReportCntrlApmCntrlIndex_Type()
)
tpmAggrReportCntrlApmCntrlIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlApmCntrlIndex.setStatus("current")
_TpmAggrReportCntrlDataSource_Type = DataSourceOrZero
_TpmAggrReportCntrlDataSource_Object = MibTableColumn
tpmAggrReportCntrlDataSource = _TpmAggrReportCntrlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 3),
    _TpmAggrReportCntrlDataSource_Type()
)
tpmAggrReportCntrlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlDataSource.setStatus("current")
_TpmAggrReportCntrlAggrType_Type = TransactionAggregationType
_TpmAggrReportCntrlAggrType_Object = MibTableColumn
tpmAggrReportCntrlAggrType = _TpmAggrReportCntrlAggrType_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 4),
    _TpmAggrReportCntrlAggrType_Type()
)
tpmAggrReportCntrlAggrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlAggrType.setStatus("current")


class _TpmAggrReportCntrlInterval_Type(Unsigned32):
    """Custom type tpmAggrReportCntrlInterval based on Unsigned32"""
    defaultValue = 3600


_TpmAggrReportCntrlInterval_Object = MibTableColumn
tpmAggrReportCntrlInterval = _TpmAggrReportCntrlInterval_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 5),
    _TpmAggrReportCntrlInterval_Type()
)
tpmAggrReportCntrlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlInterval.setStatus("current")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlInterval.setUnits("Seconds")
_TpmAggrReportCntrlReqSize_Type = Unsigned32
_TpmAggrReportCntrlReqSize_Object = MibTableColumn
tpmAggrReportCntrlReqSize = _TpmAggrReportCntrlReqSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 6),
    _TpmAggrReportCntrlReqSize_Type()
)
tpmAggrReportCntrlReqSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlReqSize.setStatus("current")
_TpmAggrReportCntrlGrantedSize_Type = Unsigned32
_TpmAggrReportCntrlGrantedSize_Object = MibTableColumn
tpmAggrReportCntrlGrantedSize = _TpmAggrReportCntrlGrantedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 7),
    _TpmAggrReportCntrlGrantedSize_Type()
)
tpmAggrReportCntrlGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlGrantedSize.setStatus("current")


class _TpmAggrReportCntrlReqReports_Type(Unsigned32):
    """Custom type tpmAggrReportCntrlReqReports based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TpmAggrReportCntrlReqReports_Type.__name__ = "Unsigned32"
_TpmAggrReportCntrlReqReports_Object = MibTableColumn
tpmAggrReportCntrlReqReports = _TpmAggrReportCntrlReqReports_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 8),
    _TpmAggrReportCntrlReqReports_Type()
)
tpmAggrReportCntrlReqReports.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlReqReports.setStatus("current")


class _TpmAggrReportCntrlGrantedReports_Type(Unsigned32):
    """Custom type tpmAggrReportCntrlGrantedReports based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TpmAggrReportCntrlGrantedReports_Type.__name__ = "Unsigned32"
_TpmAggrReportCntrlGrantedReports_Object = MibTableColumn
tpmAggrReportCntrlGrantedReports = _TpmAggrReportCntrlGrantedReports_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 9),
    _TpmAggrReportCntrlGrantedReports_Type()
)
tpmAggrReportCntrlGrantedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlGrantedReports.setStatus("current")
_TpmAggrReportCntrlStartTime_Type = TimeStamp
_TpmAggrReportCntrlStartTime_Object = MibTableColumn
tpmAggrReportCntrlStartTime = _TpmAggrReportCntrlStartTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 10),
    _TpmAggrReportCntrlStartTime_Type()
)
tpmAggrReportCntrlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlStartTime.setStatus("current")
_TpmAggrReportCntrlReportNumber_Type = Unsigned32
_TpmAggrReportCntrlReportNumber_Object = MibTableColumn
tpmAggrReportCntrlReportNumber = _TpmAggrReportCntrlReportNumber_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 11),
    _TpmAggrReportCntrlReportNumber_Type()
)
tpmAggrReportCntrlReportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlReportNumber.setStatus("current")
_TpmAggrReportCntrlInsertsDenied_Type = Counter32
_TpmAggrReportCntrlInsertsDenied_Object = MibTableColumn
tpmAggrReportCntrlInsertsDenied = _TpmAggrReportCntrlInsertsDenied_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 12),
    _TpmAggrReportCntrlInsertsDenied_Type()
)
tpmAggrReportCntrlInsertsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlInsertsDenied.setStatus("current")
_TpmAggrReportCntrlDroppedFrames_Type = Counter32
_TpmAggrReportCntrlDroppedFrames_Object = MibTableColumn
tpmAggrReportCntrlDroppedFrames = _TpmAggrReportCntrlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 13),
    _TpmAggrReportCntrlDroppedFrames_Type()
)
tpmAggrReportCntrlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlDroppedFrames.setStatus("current")
_TpmAggrReportCntrlOwner_Type = OwnerString
_TpmAggrReportCntrlOwner_Object = MibTableColumn
tpmAggrReportCntrlOwner = _TpmAggrReportCntrlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 14),
    _TpmAggrReportCntrlOwner_Type()
)
tpmAggrReportCntrlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlOwner.setStatus("current")
_TpmAggrReportCntrlStorageType_Type = StorageType
_TpmAggrReportCntrlStorageType_Object = MibTableColumn
tpmAggrReportCntrlStorageType = _TpmAggrReportCntrlStorageType_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 15),
    _TpmAggrReportCntrlStorageType_Type()
)
tpmAggrReportCntrlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlStorageType.setStatus("current")
_TpmAggrReportCntrlStatus_Type = RowStatus
_TpmAggrReportCntrlStatus_Object = MibTableColumn
tpmAggrReportCntrlStatus = _TpmAggrReportCntrlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 16),
    _TpmAggrReportCntrlStatus_Type()
)
tpmAggrReportCntrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpmAggrReportCntrlStatus.setStatus("current")
_TpmAggrReportTable_Object = MibTable
tpmAggrReportTable = _TpmAggrReportTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2)
)
if mibBuilder.loadTexts:
    tpmAggrReportTable.setStatus("current")
_TpmAggrReportEntry_Object = MibTableRow
tpmAggrReportEntry = _TpmAggrReportEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1)
)
tpmAggrReportEntry.setIndexNames(
    (0, "TPM-MIB", "tpmAggrReportCntrlIndex"),
    (0, "TPM-MIB", "tpmAggrReportIndex"),
    (0, "TPM-MIB", "tpmAggrReportAppLocalIndex"),
    (0, "TPM-MIB", "tpmAggrReportTransMetricIndex"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "TPM-MIB", "tpmAggrReportServerAddress"),
    (0, "TPM-MIB", "tpmAggrReportApmNameClientID"),
)
if mibBuilder.loadTexts:
    tpmAggrReportEntry.setStatus("current")


class _TpmAggrReportIndex_Type(Unsigned32):
    """Custom type tpmAggrReportIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TpmAggrReportIndex_Type.__name__ = "Unsigned32"
_TpmAggrReportIndex_Object = MibTableColumn
tpmAggrReportIndex = _TpmAggrReportIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 1),
    _TpmAggrReportIndex_Type()
)
tpmAggrReportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmAggrReportIndex.setStatus("current")
_TpmAggrReportAppLocalIndex_Type = AppLocalIndex
_TpmAggrReportAppLocalIndex_Object = MibTableColumn
tpmAggrReportAppLocalIndex = _TpmAggrReportAppLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 2),
    _TpmAggrReportAppLocalIndex_Type()
)
tpmAggrReportAppLocalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmAggrReportAppLocalIndex.setStatus("current")
_TpmAggrReportTransMetricIndex_Type = TpmTransactionMetricIndex
_TpmAggrReportTransMetricIndex_Object = MibTableColumn
tpmAggrReportTransMetricIndex = _TpmAggrReportTransMetricIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 3),
    _TpmAggrReportTransMetricIndex_Type()
)
tpmAggrReportTransMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmAggrReportTransMetricIndex.setStatus("current")


class _TpmAggrReportServerAddress_Type(OctetString):
    """Custom type tpmAggrReportServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_TpmAggrReportServerAddress_Type.__name__ = "OctetString"
_TpmAggrReportServerAddress_Object = MibTableColumn
tpmAggrReportServerAddress = _TpmAggrReportServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 4),
    _TpmAggrReportServerAddress_Type()
)
tpmAggrReportServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmAggrReportServerAddress.setStatus("current")
_TpmAggrReportApmNameClientID_Type = RmonClientID
_TpmAggrReportApmNameClientID_Object = MibTableColumn
tpmAggrReportApmNameClientID = _TpmAggrReportApmNameClientID_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 5),
    _TpmAggrReportApmNameClientID_Type()
)
tpmAggrReportApmNameClientID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmAggrReportApmNameClientID.setStatus("current")
_TpmAggrReportStatN_Type = ZeroBasedCounter32
_TpmAggrReportStatN_Object = MibTableColumn
tpmAggrReportStatN = _TpmAggrReportStatN_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 6),
    _TpmAggrReportStatN_Type()
)
tpmAggrReportStatN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportStatN.setStatus("current")
_TpmAggrReportOverflowStatN_Type = ZeroBasedCounter32
_TpmAggrReportOverflowStatN_Object = MibTableColumn
tpmAggrReportOverflowStatN = _TpmAggrReportOverflowStatN_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 7),
    _TpmAggrReportOverflowStatN_Type()
)
tpmAggrReportOverflowStatN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportOverflowStatN.setStatus("current")
_TpmAggrReportHCStatN_Type = ZeroBasedCounter64
_TpmAggrReportHCStatN_Object = MibTableColumn
tpmAggrReportHCStatN = _TpmAggrReportHCStatN_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 8),
    _TpmAggrReportHCStatN_Type()
)
tpmAggrReportHCStatN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportHCStatN.setStatus("current")
_TpmAggrReportStatSumX_Type = ZeroBasedCounter32
_TpmAggrReportStatSumX_Object = MibTableColumn
tpmAggrReportStatSumX = _TpmAggrReportStatSumX_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 9),
    _TpmAggrReportStatSumX_Type()
)
tpmAggrReportStatSumX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportStatSumX.setStatus("current")
_TpmAggrReportOverflowStatSumX_Type = ZeroBasedCounter32
_TpmAggrReportOverflowStatSumX_Object = MibTableColumn
tpmAggrReportOverflowStatSumX = _TpmAggrReportOverflowStatSumX_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 10),
    _TpmAggrReportOverflowStatSumX_Type()
)
tpmAggrReportOverflowStatSumX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportOverflowStatSumX.setStatus("current")
_TpmAggrReportHCStatSumX_Type = ZeroBasedCounter64
_TpmAggrReportHCStatSumX_Object = MibTableColumn
tpmAggrReportHCStatSumX = _TpmAggrReportHCStatSumX_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 11),
    _TpmAggrReportHCStatSumX_Type()
)
tpmAggrReportHCStatSumX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportHCStatSumX.setStatus("current")
_TpmAggrReportStatMaximum_Type = ZeroBasedCounter32
_TpmAggrReportStatMaximum_Object = MibTableColumn
tpmAggrReportStatMaximum = _TpmAggrReportStatMaximum_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 12),
    _TpmAggrReportStatMaximum_Type()
)
tpmAggrReportStatMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportStatMaximum.setStatus("current")
_TpmAggrReportStatMinimum_Type = ZeroBasedCounter32
_TpmAggrReportStatMinimum_Object = MibTableColumn
tpmAggrReportStatMinimum = _TpmAggrReportStatMinimum_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 13),
    _TpmAggrReportStatMinimum_Type()
)
tpmAggrReportStatMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportStatMinimum.setStatus("current")
_TpmAggrReportStatSumSq_Type = ZeroBasedCounter32
_TpmAggrReportStatSumSq_Object = MibTableColumn
tpmAggrReportStatSumSq = _TpmAggrReportStatSumSq_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 14),
    _TpmAggrReportStatSumSq_Type()
)
tpmAggrReportStatSumSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportStatSumSq.setStatus("current")
_TpmAggrReportOverflowStatSumSq_Type = ZeroBasedCounter32
_TpmAggrReportOverflowStatSumSq_Object = MibTableColumn
tpmAggrReportOverflowStatSumSq = _TpmAggrReportOverflowStatSumSq_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 15),
    _TpmAggrReportOverflowStatSumSq_Type()
)
tpmAggrReportOverflowStatSumSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportOverflowStatSumSq.setStatus("current")
_TpmAggrReportHCStatSumSq_Type = ZeroBasedCounter64
_TpmAggrReportHCStatSumSq_Object = MibTableColumn
tpmAggrReportHCStatSumSq = _TpmAggrReportHCStatSumSq_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 16),
    _TpmAggrReportHCStatSumSq_Type()
)
tpmAggrReportHCStatSumSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportHCStatSumSq.setStatus("current")
_TpmAggrReportStatSumIX_Type = ZeroBasedCounter32
_TpmAggrReportStatSumIX_Object = MibTableColumn
tpmAggrReportStatSumIX = _TpmAggrReportStatSumIX_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 17),
    _TpmAggrReportStatSumIX_Type()
)
tpmAggrReportStatSumIX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportStatSumIX.setStatus("current")
_TpmAggrReportOverflowStatSumIX_Type = ZeroBasedCounter32
_TpmAggrReportOverflowStatSumIX_Object = MibTableColumn
tpmAggrReportOverflowStatSumIX = _TpmAggrReportOverflowStatSumIX_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 18),
    _TpmAggrReportOverflowStatSumIX_Type()
)
tpmAggrReportOverflowStatSumIX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportOverflowStatSumIX.setStatus("current")
_TpmAggrReportHCStatSumIX_Type = ZeroBasedCounter64
_TpmAggrReportHCStatSumIX_Object = MibTableColumn
tpmAggrReportHCStatSumIX = _TpmAggrReportHCStatSumIX_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 19),
    _TpmAggrReportHCStatSumIX_Type()
)
tpmAggrReportHCStatSumIX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportHCStatSumIX.setStatus("current")
_TpmAggrReportStatSumIXSq_Type = ZeroBasedCounter32
_TpmAggrReportStatSumIXSq_Object = MibTableColumn
tpmAggrReportStatSumIXSq = _TpmAggrReportStatSumIXSq_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 20),
    _TpmAggrReportStatSumIXSq_Type()
)
tpmAggrReportStatSumIXSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportStatSumIXSq.setStatus("current")
_TpmAggrReportOverflowStatSumIXSq_Type = ZeroBasedCounter32
_TpmAggrReportOverflowStatSumIXSq_Object = MibTableColumn
tpmAggrReportOverflowStatSumIXSq = _TpmAggrReportOverflowStatSumIXSq_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 21),
    _TpmAggrReportOverflowStatSumIXSq_Type()
)
tpmAggrReportOverflowStatSumIXSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportOverflowStatSumIXSq.setStatus("current")
_TpmAggrReportHCStatSumIXSq_Type = ZeroBasedCounter64
_TpmAggrReportHCStatSumIXSq_Object = MibTableColumn
tpmAggrReportHCStatSumIXSq = _TpmAggrReportHCStatSumIXSq_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 22),
    _TpmAggrReportHCStatSumIXSq_Type()
)
tpmAggrReportHCStatSumIXSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmAggrReportHCStatSumIXSq.setStatus("current")
_TpmCurReportTable_Object = MibTable
tpmCurReportTable = _TpmCurReportTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 3)
)
if mibBuilder.loadTexts:
    tpmCurReportTable.setStatus("current")
_TpmCurReportEntry_Object = MibTableRow
tpmCurReportEntry = _TpmCurReportEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1)
)
tpmCurReportEntry.setIndexNames(
    (0, "TPM-MIB", "tpmAggrReportCntrlIndex"),
    (0, "TPM-MIB", "tpmCurReportAppLocalIndex"),
    (0, "TPM-MIB", "tpmCurReportTransMetricIndex"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "TPM-MIB", "tpmCurReportServerAddress"),
    (0, "TPM-MIB", "tpmCurReportApmNameClientID"),
    (0, "TPM-MIB", "tpmCurReportApmTransactionID"),
)
if mibBuilder.loadTexts:
    tpmCurReportEntry.setStatus("current")
_TpmCurReportAppLocalIndex_Type = AppLocalIndex
_TpmCurReportAppLocalIndex_Object = MibTableColumn
tpmCurReportAppLocalIndex = _TpmCurReportAppLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 1),
    _TpmCurReportAppLocalIndex_Type()
)
tpmCurReportAppLocalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmCurReportAppLocalIndex.setStatus("current")
_TpmCurReportTransMetricIndex_Type = TpmTransactionMetricIndex
_TpmCurReportTransMetricIndex_Object = MibTableColumn
tpmCurReportTransMetricIndex = _TpmCurReportTransMetricIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 2),
    _TpmCurReportTransMetricIndex_Type()
)
tpmCurReportTransMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmCurReportTransMetricIndex.setStatus("current")


class _TpmCurReportServerAddress_Type(OctetString):
    """Custom type tpmCurReportServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_TpmCurReportServerAddress_Type.__name__ = "OctetString"
_TpmCurReportServerAddress_Object = MibTableColumn
tpmCurReportServerAddress = _TpmCurReportServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 3),
    _TpmCurReportServerAddress_Type()
)
tpmCurReportServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmCurReportServerAddress.setStatus("current")
_TpmCurReportApmNameClientID_Type = RmonClientID
_TpmCurReportApmNameClientID_Object = MibTableColumn
tpmCurReportApmNameClientID = _TpmCurReportApmNameClientID_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 4),
    _TpmCurReportApmNameClientID_Type()
)
tpmCurReportApmNameClientID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmCurReportApmNameClientID.setStatus("current")


class _TpmCurReportApmTransactionID_Type(Unsigned32):
    """Custom type tpmCurReportApmTransactionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TpmCurReportApmTransactionID_Type.__name__ = "Unsigned32"
_TpmCurReportApmTransactionID_Object = MibTableColumn
tpmCurReportApmTransactionID = _TpmCurReportApmTransactionID_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 5),
    _TpmCurReportApmTransactionID_Type()
)
tpmCurReportApmTransactionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmCurReportApmTransactionID.setStatus("current")
_TpmCurReportMetricValue_Type = ZeroBasedCounter32
_TpmCurReportMetricValue_Object = MibTableColumn
tpmCurReportMetricValue = _TpmCurReportMetricValue_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 6),
    _TpmCurReportMetricValue_Type()
)
tpmCurReportMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmCurReportMetricValue.setStatus("current")


class _TpmCurReportCompletion_Type(Integer32):
    """Custom type tpmCurReportCompletion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("completed", 2),
          ("current", 1))
    )


_TpmCurReportCompletion_Type.__name__ = "Integer32"
_TpmCurReportCompletion_Object = MibTableColumn
tpmCurReportCompletion = _TpmCurReportCompletion_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 7),
    _TpmCurReportCompletion_Type()
)
tpmCurReportCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmCurReportCompletion.setStatus("current")
_TpmCurReportSize_Type = Unsigned32
_TpmCurReportSize_Object = MibScalar
tpmCurReportSize = _TpmCurReportSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 4),
    _TpmCurReportSize_Type()
)
tpmCurReportSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpmCurReportSize.setStatus("current")
_TpmExcpReportTable_Object = MibTable
tpmExcpReportTable = _TpmExcpReportTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5)
)
if mibBuilder.loadTexts:
    tpmExcpReportTable.setStatus("current")
_TpmExcpReportEntry_Object = MibTableRow
tpmExcpReportEntry = _TpmExcpReportEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1)
)
tpmExcpReportEntry.setIndexNames(
    (0, "APM-MIB", "apmAppDirAppLocalIndex"),
    (0, "APM-MIB", "apmAppDirResponsivenessType"),
    (0, "APM-MIB", "apmExceptionIndex"),
    (0, "TPM-MIB", "tpmExcpReportTransMetricIndex"),
)
if mibBuilder.loadTexts:
    tpmExcpReportEntry.setStatus("current")
_TpmExcpReportTransMetricIndex_Type = TpmTransactionMetricIndex
_TpmExcpReportTransMetricIndex_Object = MibTableColumn
tpmExcpReportTransMetricIndex = _TpmExcpReportTransMetricIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 1),
    _TpmExcpReportTransMetricIndex_Type()
)
tpmExcpReportTransMetricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpmExcpReportTransMetricIndex.setStatus("current")
_TpmExcpReportStatN_Type = ZeroBasedCounter32
_TpmExcpReportStatN_Object = MibTableColumn
tpmExcpReportStatN = _TpmExcpReportStatN_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 2),
    _TpmExcpReportStatN_Type()
)
tpmExcpReportStatN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportStatN.setStatus("current")
_TpmExcpReportOverflowStatN_Type = ZeroBasedCounter32
_TpmExcpReportOverflowStatN_Object = MibTableColumn
tpmExcpReportOverflowStatN = _TpmExcpReportOverflowStatN_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 3),
    _TpmExcpReportOverflowStatN_Type()
)
tpmExcpReportOverflowStatN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportOverflowStatN.setStatus("current")
_TpmExcpReportHCStatN_Type = ZeroBasedCounter64
_TpmExcpReportHCStatN_Object = MibTableColumn
tpmExcpReportHCStatN = _TpmExcpReportHCStatN_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 4),
    _TpmExcpReportHCStatN_Type()
)
tpmExcpReportHCStatN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportHCStatN.setStatus("current")
_TpmExcpReportStatSumX_Type = ZeroBasedCounter32
_TpmExcpReportStatSumX_Object = MibTableColumn
tpmExcpReportStatSumX = _TpmExcpReportStatSumX_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 5),
    _TpmExcpReportStatSumX_Type()
)
tpmExcpReportStatSumX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportStatSumX.setStatus("current")
_TpmExcpReportOverflowStatSumX_Type = ZeroBasedCounter32
_TpmExcpReportOverflowStatSumX_Object = MibTableColumn
tpmExcpReportOverflowStatSumX = _TpmExcpReportOverflowStatSumX_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 6),
    _TpmExcpReportOverflowStatSumX_Type()
)
tpmExcpReportOverflowStatSumX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportOverflowStatSumX.setStatus("current")
_TpmExcpReportHCStatSumX_Type = ZeroBasedCounter64
_TpmExcpReportHCStatSumX_Object = MibTableColumn
tpmExcpReportHCStatSumX = _TpmExcpReportHCStatSumX_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 7),
    _TpmExcpReportHCStatSumX_Type()
)
tpmExcpReportHCStatSumX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportHCStatSumX.setStatus("current")
_TpmExcpReportStatMaximum_Type = ZeroBasedCounter32
_TpmExcpReportStatMaximum_Object = MibTableColumn
tpmExcpReportStatMaximum = _TpmExcpReportStatMaximum_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 8),
    _TpmExcpReportStatMaximum_Type()
)
tpmExcpReportStatMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportStatMaximum.setStatus("current")
_TpmExcpReportStatMinimum_Type = ZeroBasedCounter32
_TpmExcpReportStatMinimum_Object = MibTableColumn
tpmExcpReportStatMinimum = _TpmExcpReportStatMinimum_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 9),
    _TpmExcpReportStatMinimum_Type()
)
tpmExcpReportStatMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportStatMinimum.setStatus("current")
_TpmExcpReportStatSumSq_Type = ZeroBasedCounter32
_TpmExcpReportStatSumSq_Object = MibTableColumn
tpmExcpReportStatSumSq = _TpmExcpReportStatSumSq_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 10),
    _TpmExcpReportStatSumSq_Type()
)
tpmExcpReportStatSumSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportStatSumSq.setStatus("current")
_TpmExcpReportOverflowStatSumSq_Type = ZeroBasedCounter32
_TpmExcpReportOverflowStatSumSq_Object = MibTableColumn
tpmExcpReportOverflowStatSumSq = _TpmExcpReportOverflowStatSumSq_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 11),
    _TpmExcpReportOverflowStatSumSq_Type()
)
tpmExcpReportOverflowStatSumSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportOverflowStatSumSq.setStatus("current")
_TpmExcpReportHCStatSumSq_Type = ZeroBasedCounter64
_TpmExcpReportHCStatSumSq_Object = MibTableColumn
tpmExcpReportHCStatSumSq = _TpmExcpReportHCStatSumSq_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 12),
    _TpmExcpReportHCStatSumSq_Type()
)
tpmExcpReportHCStatSumSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportHCStatSumSq.setStatus("current")
_TpmExcpReportStatSumIX_Type = ZeroBasedCounter32
_TpmExcpReportStatSumIX_Object = MibTableColumn
tpmExcpReportStatSumIX = _TpmExcpReportStatSumIX_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 13),
    _TpmExcpReportStatSumIX_Type()
)
tpmExcpReportStatSumIX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportStatSumIX.setStatus("current")
_TpmExcpReportOverflowStatSumIX_Type = ZeroBasedCounter32
_TpmExcpReportOverflowStatSumIX_Object = MibTableColumn
tpmExcpReportOverflowStatSumIX = _TpmExcpReportOverflowStatSumIX_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 14),
    _TpmExcpReportOverflowStatSumIX_Type()
)
tpmExcpReportOverflowStatSumIX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportOverflowStatSumIX.setStatus("current")
_TpmExcpReportHCStatSumIX_Type = ZeroBasedCounter64
_TpmExcpReportHCStatSumIX_Object = MibTableColumn
tpmExcpReportHCStatSumIX = _TpmExcpReportHCStatSumIX_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 15),
    _TpmExcpReportHCStatSumIX_Type()
)
tpmExcpReportHCStatSumIX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportHCStatSumIX.setStatus("current")
_TpmExcpReportStatSumIXSq_Type = ZeroBasedCounter32
_TpmExcpReportStatSumIXSq_Object = MibTableColumn
tpmExcpReportStatSumIXSq = _TpmExcpReportStatSumIXSq_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 16),
    _TpmExcpReportStatSumIXSq_Type()
)
tpmExcpReportStatSumIXSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportStatSumIXSq.setStatus("current")
_TpmExcpReportOverflowStatSumIXSq_Type = ZeroBasedCounter32
_TpmExcpReportOverflowStatSumIXSq_Object = MibTableColumn
tpmExcpReportOverflowStatSumIXSq = _TpmExcpReportOverflowStatSumIXSq_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 17),
    _TpmExcpReportOverflowStatSumIXSq_Type()
)
tpmExcpReportOverflowStatSumIXSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportOverflowStatSumIXSq.setStatus("current")
_TpmExcpReportHCStatSumIXSq_Type = ZeroBasedCounter64
_TpmExcpReportHCStatSumIXSq_Object = MibTableColumn
tpmExcpReportHCStatSumIXSq = _TpmExcpReportHCStatSumIXSq_Object(
    (1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 18),
    _TpmExcpReportHCStatSumIXSq_Type()
)
tpmExcpReportHCStatSumIXSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpmExcpReportHCStatSumIXSq.setStatus("current")
_TpmConformance_ObjectIdentity = ObjectIdentity
tpmConformance = _TpmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 30, 3)
)
_TpmMIBCompliances_ObjectIdentity = ObjectIdentity
tpmMIBCompliances = _TpmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 30, 3, 1)
)
_TpmGroups_ObjectIdentity = ObjectIdentity
tpmGroups = _TpmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 30, 3, 2)
)

# Managed Objects groups

tpmCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 30, 3, 2, 1)
)
tpmCapabilitiesGroup.setObjects(
      *(("TPM-MIB", "tpmClockResolution"),
        ("TPM-MIB", "tpmClockMaxSkew"),
        ("TPM-MIB", "tpmClockSource"),
        ("TPM-MIB", "tpmTransMetricDirLastChange"),
        ("TPM-MIB", "tpmTransMetricProtocolIndex"),
        ("TPM-MIB", "tpmTransMetricMetricIndex"),
        ("TPM-MIB", "tpmTransMetricDirConfig"),
        ("TPM-MIB", "tpmMetricDefType"),
        ("TPM-MIB", "tpmMetricDefDirType"),
        ("TPM-MIB", "tpmMetricDefName"),
        ("TPM-MIB", "tpmMetricDefReference"),
        ("TPM-MIB", "tpmMetricDefGlobalID"))
)
if mibBuilder.loadTexts:
    tpmCapabilitiesGroup.setStatus("current")

tpmAggregateReportsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 30, 3, 2, 2)
)
tpmAggregateReportsGroup.setObjects(
      *(("TPM-MIB", "tpmAggrReportCntrlApmCntrlIndex"),
        ("TPM-MIB", "tpmAggrReportCntrlDataSource"),
        ("TPM-MIB", "tpmAggrReportCntrlAggrType"),
        ("TPM-MIB", "tpmAggrReportCntrlInterval"),
        ("TPM-MIB", "tpmAggrReportCntrlReqSize"),
        ("TPM-MIB", "tpmAggrReportCntrlGrantedSize"),
        ("TPM-MIB", "tpmAggrReportCntrlReqReports"),
        ("TPM-MIB", "tpmAggrReportCntrlGrantedReports"),
        ("TPM-MIB", "tpmAggrReportCntrlStartTime"),
        ("TPM-MIB", "tpmAggrReportCntrlReportNumber"),
        ("TPM-MIB", "tpmAggrReportCntrlInsertsDenied"),
        ("TPM-MIB", "tpmAggrReportCntrlDroppedFrames"),
        ("TPM-MIB", "tpmAggrReportCntrlOwner"),
        ("TPM-MIB", "tpmAggrReportCntrlStorageType"),
        ("TPM-MIB", "tpmAggrReportCntrlStatus"),
        ("TPM-MIB", "tpmAggrReportStatN"),
        ("TPM-MIB", "tpmAggrReportOverflowStatN"),
        ("TPM-MIB", "tpmAggrReportHCStatN"),
        ("TPM-MIB", "tpmAggrReportStatSumX"),
        ("TPM-MIB", "tpmAggrReportOverflowStatSumX"),
        ("TPM-MIB", "tpmAggrReportHCStatSumX"),
        ("TPM-MIB", "tpmAggrReportStatMaximum"),
        ("TPM-MIB", "tpmAggrReportStatMinimum"),
        ("TPM-MIB", "tpmAggrReportStatSumSq"),
        ("TPM-MIB", "tpmAggrReportOverflowStatSumSq"),
        ("TPM-MIB", "tpmAggrReportHCStatSumSq"),
        ("TPM-MIB", "tpmAggrReportStatSumIX"),
        ("TPM-MIB", "tpmAggrReportOverflowStatSumIX"),
        ("TPM-MIB", "tpmAggrReportHCStatSumIX"),
        ("TPM-MIB", "tpmAggrReportStatSumIXSq"),
        ("TPM-MIB", "tpmAggrReportOverflowStatSumIXSq"),
        ("TPM-MIB", "tpmAggrReportHCStatSumIXSq"))
)
if mibBuilder.loadTexts:
    tpmAggregateReportsGroup.setStatus("current")

tpmCurrentReportsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 30, 3, 2, 3)
)
tpmCurrentReportsGroup.setObjects(
      *(("TPM-MIB", "tpmCurReportMetricValue"),
        ("TPM-MIB", "tpmCurReportCompletion"),
        ("TPM-MIB", "tpmCurReportSize"))
)
if mibBuilder.loadTexts:
    tpmCurrentReportsGroup.setStatus("current")

tpmExceptionReportsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 30, 3, 2, 4)
)
tpmExceptionReportsGroup.setObjects(
      *(("TPM-MIB", "tpmExcpReportStatN"),
        ("TPM-MIB", "tpmExcpReportOverflowStatN"),
        ("TPM-MIB", "tpmExcpReportHCStatN"),
        ("TPM-MIB", "tpmExcpReportStatSumX"),
        ("TPM-MIB", "tpmExcpReportOverflowStatSumX"),
        ("TPM-MIB", "tpmExcpReportHCStatSumX"),
        ("TPM-MIB", "tpmExcpReportStatMaximum"),
        ("TPM-MIB", "tpmExcpReportStatMinimum"),
        ("TPM-MIB", "tpmExcpReportStatSumSq"),
        ("TPM-MIB", "tpmExcpReportOverflowStatSumSq"),
        ("TPM-MIB", "tpmExcpReportHCStatSumSq"),
        ("TPM-MIB", "tpmExcpReportStatSumIX"),
        ("TPM-MIB", "tpmExcpReportOverflowStatSumIX"),
        ("TPM-MIB", "tpmExcpReportHCStatSumIX"),
        ("TPM-MIB", "tpmExcpReportStatSumIXSq"),
        ("TPM-MIB", "tpmExcpReportOverflowStatSumIXSq"),
        ("TPM-MIB", "tpmExcpReportHCStatSumIXSq"))
)
if mibBuilder.loadTexts:
    tpmExceptionReportsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tpmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 30, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tpmMIBCompliance.setStatus(
        "current"
    )

tpmCurrentReportsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 30, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tpmCurrentReportsCompliance.setStatus(
        "current"
    )

tpmExceptionReportsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 30, 3, 1, 3)
)
if mibBuilder.loadTexts:
    tpmExceptionReportsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPM-MIB",
    **{"TpmTransactionMetricIndex": TpmTransactionMetricIndex,
       "TpmMetricDefID": TpmMetricDefID,
       "tpmMIB": tpmMIB,
       "tpmCapabilities": tpmCapabilities,
       "tpmClockResolution": tpmClockResolution,
       "tpmClockMaxSkew": tpmClockMaxSkew,
       "tpmClockSource": tpmClockSource,
       "tpmTransMetricDirLastChange": tpmTransMetricDirLastChange,
       "tpmTransMetricDirTable": tpmTransMetricDirTable,
       "tpmTransMetricDirEntry": tpmTransMetricDirEntry,
       "tpmTransMetricAppLocalIndex": tpmTransMetricAppLocalIndex,
       "tpmTransMetricIndex": tpmTransMetricIndex,
       "tpmTransMetricProtocolIndex": tpmTransMetricProtocolIndex,
       "tpmTransMetricMetricIndex": tpmTransMetricMetricIndex,
       "tpmTransMetricDirConfig": tpmTransMetricDirConfig,
       "tpmMetricDefTable": tpmMetricDefTable,
       "tpmMetricDefEntry": tpmMetricDefEntry,
       "tpmMetricDefinitionID": tpmMetricDefinitionID,
       "tpmMetricDefType": tpmMetricDefType,
       "tpmMetricDefDirType": tpmMetricDefDirType,
       "tpmMetricDefName": tpmMetricDefName,
       "tpmMetricDefReference": tpmMetricDefReference,
       "tpmMetricDefGlobalID": tpmMetricDefGlobalID,
       "tpmReports": tpmReports,
       "tpmAggrReportCntrlTable": tpmAggrReportCntrlTable,
       "tpmAggrReportCntrlEntry": tpmAggrReportCntrlEntry,
       "tpmAggrReportCntrlIndex": tpmAggrReportCntrlIndex,
       "tpmAggrReportCntrlApmCntrlIndex": tpmAggrReportCntrlApmCntrlIndex,
       "tpmAggrReportCntrlDataSource": tpmAggrReportCntrlDataSource,
       "tpmAggrReportCntrlAggrType": tpmAggrReportCntrlAggrType,
       "tpmAggrReportCntrlInterval": tpmAggrReportCntrlInterval,
       "tpmAggrReportCntrlReqSize": tpmAggrReportCntrlReqSize,
       "tpmAggrReportCntrlGrantedSize": tpmAggrReportCntrlGrantedSize,
       "tpmAggrReportCntrlReqReports": tpmAggrReportCntrlReqReports,
       "tpmAggrReportCntrlGrantedReports": tpmAggrReportCntrlGrantedReports,
       "tpmAggrReportCntrlStartTime": tpmAggrReportCntrlStartTime,
       "tpmAggrReportCntrlReportNumber": tpmAggrReportCntrlReportNumber,
       "tpmAggrReportCntrlInsertsDenied": tpmAggrReportCntrlInsertsDenied,
       "tpmAggrReportCntrlDroppedFrames": tpmAggrReportCntrlDroppedFrames,
       "tpmAggrReportCntrlOwner": tpmAggrReportCntrlOwner,
       "tpmAggrReportCntrlStorageType": tpmAggrReportCntrlStorageType,
       "tpmAggrReportCntrlStatus": tpmAggrReportCntrlStatus,
       "tpmAggrReportTable": tpmAggrReportTable,
       "tpmAggrReportEntry": tpmAggrReportEntry,
       "tpmAggrReportIndex": tpmAggrReportIndex,
       "tpmAggrReportAppLocalIndex": tpmAggrReportAppLocalIndex,
       "tpmAggrReportTransMetricIndex": tpmAggrReportTransMetricIndex,
       "tpmAggrReportServerAddress": tpmAggrReportServerAddress,
       "tpmAggrReportApmNameClientID": tpmAggrReportApmNameClientID,
       "tpmAggrReportStatN": tpmAggrReportStatN,
       "tpmAggrReportOverflowStatN": tpmAggrReportOverflowStatN,
       "tpmAggrReportHCStatN": tpmAggrReportHCStatN,
       "tpmAggrReportStatSumX": tpmAggrReportStatSumX,
       "tpmAggrReportOverflowStatSumX": tpmAggrReportOverflowStatSumX,
       "tpmAggrReportHCStatSumX": tpmAggrReportHCStatSumX,
       "tpmAggrReportStatMaximum": tpmAggrReportStatMaximum,
       "tpmAggrReportStatMinimum": tpmAggrReportStatMinimum,
       "tpmAggrReportStatSumSq": tpmAggrReportStatSumSq,
       "tpmAggrReportOverflowStatSumSq": tpmAggrReportOverflowStatSumSq,
       "tpmAggrReportHCStatSumSq": tpmAggrReportHCStatSumSq,
       "tpmAggrReportStatSumIX": tpmAggrReportStatSumIX,
       "tpmAggrReportOverflowStatSumIX": tpmAggrReportOverflowStatSumIX,
       "tpmAggrReportHCStatSumIX": tpmAggrReportHCStatSumIX,
       "tpmAggrReportStatSumIXSq": tpmAggrReportStatSumIXSq,
       "tpmAggrReportOverflowStatSumIXSq": tpmAggrReportOverflowStatSumIXSq,
       "tpmAggrReportHCStatSumIXSq": tpmAggrReportHCStatSumIXSq,
       "tpmCurReportTable": tpmCurReportTable,
       "tpmCurReportEntry": tpmCurReportEntry,
       "tpmCurReportAppLocalIndex": tpmCurReportAppLocalIndex,
       "tpmCurReportTransMetricIndex": tpmCurReportTransMetricIndex,
       "tpmCurReportServerAddress": tpmCurReportServerAddress,
       "tpmCurReportApmNameClientID": tpmCurReportApmNameClientID,
       "tpmCurReportApmTransactionID": tpmCurReportApmTransactionID,
       "tpmCurReportMetricValue": tpmCurReportMetricValue,
       "tpmCurReportCompletion": tpmCurReportCompletion,
       "tpmCurReportSize": tpmCurReportSize,
       "tpmExcpReportTable": tpmExcpReportTable,
       "tpmExcpReportEntry": tpmExcpReportEntry,
       "tpmExcpReportTransMetricIndex": tpmExcpReportTransMetricIndex,
       "tpmExcpReportStatN": tpmExcpReportStatN,
       "tpmExcpReportOverflowStatN": tpmExcpReportOverflowStatN,
       "tpmExcpReportHCStatN": tpmExcpReportHCStatN,
       "tpmExcpReportStatSumX": tpmExcpReportStatSumX,
       "tpmExcpReportOverflowStatSumX": tpmExcpReportOverflowStatSumX,
       "tpmExcpReportHCStatSumX": tpmExcpReportHCStatSumX,
       "tpmExcpReportStatMaximum": tpmExcpReportStatMaximum,
       "tpmExcpReportStatMinimum": tpmExcpReportStatMinimum,
       "tpmExcpReportStatSumSq": tpmExcpReportStatSumSq,
       "tpmExcpReportOverflowStatSumSq": tpmExcpReportOverflowStatSumSq,
       "tpmExcpReportHCStatSumSq": tpmExcpReportHCStatSumSq,
       "tpmExcpReportStatSumIX": tpmExcpReportStatSumIX,
       "tpmExcpReportOverflowStatSumIX": tpmExcpReportOverflowStatSumIX,
       "tpmExcpReportHCStatSumIX": tpmExcpReportHCStatSumIX,
       "tpmExcpReportStatSumIXSq": tpmExcpReportStatSumIXSq,
       "tpmExcpReportOverflowStatSumIXSq": tpmExcpReportOverflowStatSumIXSq,
       "tpmExcpReportHCStatSumIXSq": tpmExcpReportHCStatSumIXSq,
       "tpmConformance": tpmConformance,
       "tpmMIBCompliances": tpmMIBCompliances,
       "tpmMIBCompliance": tpmMIBCompliance,
       "tpmCurrentReportsCompliance": tpmCurrentReportsCompliance,
       "tpmExceptionReportsCompliance": tpmExceptionReportsCompliance,
       "tpmGroups": tpmGroups,
       "tpmCapabilitiesGroup": tpmCapabilitiesGroup,
       "tpmAggregateReportsGroup": tpmAggregateReportsGroup,
       "tpmCurrentReportsGroup": tpmCurrentReportsGroup,
       "tpmExceptionReportsGroup": tpmExceptionReportsGroup}
)
