# SNMP MIB module (CISCO-ENTITY-PERFORMANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-PERFORMANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:38 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoEntityPerformanceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 756)
)
ciscoEntityPerformanceMIB.setRevisions(
        ("2014-06-18 00:00",
         "2010-09-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoEntPerfMeasurement(Counter64, TextualConvention):
    status = "current"


class CiscoEntPerfRange(Integer32, TextualConvention):
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
        *(("rangeInt32", 2),
          ("rangeInt64", 3),
          ("rangePercentage", 1))
    )



class CiscoEntPerfType(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("bitDropRate", 4),
          ("bitInputRate", 2),
          ("bitOutputRate", 3),
          ("packetDropRate", 7),
          ("packetInputRate", 5),
          ("packetOutputRate", 6),
          ("utilization", 1))
    )



class CiscoEntPerfInterval(Integer32, TextualConvention):
    status = "current"
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
        *(("current", 1),
          ("fifteenMinutes", 4),
          ("fiveMinutes", 3),
          ("oneMinute", 2))
    )



class CiscoEntPerfHistInterval(Integer32, TextualConvention):
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
        *(("fifteenMinutes", 3),
          ("fiveMinutes", 2),
          ("oneMinute", 1))
    )



class CiscoEntPerfIntervalAlgo(Integer32, TextualConvention):
    status = "current"
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
        *(("algoSMA", 4),
          ("current", 3),
          ("other", 2),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEntityPerformanceMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEntityPerformanceMIBNotifs = _CiscoEntityPerformanceMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 0)
)
_CiscoEntityPerformanceMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEntityPerformanceMIBObjects = _CiscoEntityPerformanceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1)
)
_CepEntityTable_Object = MibTable
cepEntityTable = _CepEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 1)
)
if mibBuilder.loadTexts:
    cepEntityTable.setStatus("current")
_CepEntityEntry_Object = MibTableRow
cepEntityEntry = _CepEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 1, 1)
)
cepEntityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cepEntityEntry.setStatus("current")
_CepEntityNumReloads_Type = Counter32
_CepEntityNumReloads_Object = MibTableColumn
cepEntityNumReloads = _CepEntityNumReloads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 1, 1, 1),
    _CepEntityNumReloads_Type()
)
cepEntityNumReloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepEntityNumReloads.setStatus("current")
if mibBuilder.loadTexts:
    cepEntityNumReloads.setUnits("reloads")
_CepEntityLastReloadTime_Type = DateAndTime
_CepEntityLastReloadTime_Object = MibTableColumn
cepEntityLastReloadTime = _CepEntityLastReloadTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 1, 1, 2),
    _CepEntityLastReloadTime_Type()
)
cepEntityLastReloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepEntityLastReloadTime.setStatus("current")
_CepConfigTable_Object = MibTable
cepConfigTable = _CepConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2)
)
if mibBuilder.loadTexts:
    cepConfigTable.setStatus("current")
_CepConfigEntry_Object = MibTableRow
cepConfigEntry = _CepConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1)
)
cepConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigInterval"),
    (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfType"),
)
if mibBuilder.loadTexts:
    cepConfigEntry.setStatus("current")
_CepConfigInterval_Type = CiscoEntPerfInterval
_CepConfigInterval_Object = MibTableColumn
cepConfigInterval = _CepConfigInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 1),
    _CepConfigInterval_Type()
)
cepConfigInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cepConfigInterval.setStatus("current")
_CepConfigPerfType_Type = CiscoEntPerfType
_CepConfigPerfType_Object = MibTableColumn
cepConfigPerfType = _CepConfigPerfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 2),
    _CepConfigPerfType_Type()
)
cepConfigPerfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cepConfigPerfType.setStatus("current")
_CepConfigPerfRange_Type = CiscoEntPerfRange
_CepConfigPerfRange_Object = MibTableColumn
cepConfigPerfRange = _CepConfigPerfRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 3),
    _CepConfigPerfRange_Type()
)
cepConfigPerfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepConfigPerfRange.setStatus("current")
_CepConfigRisingThreshold_Type = CiscoEntPerfMeasurement
_CepConfigRisingThreshold_Object = MibTableColumn
cepConfigRisingThreshold = _CepConfigRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 4),
    _CepConfigRisingThreshold_Type()
)
cepConfigRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cepConfigRisingThreshold.setStatus("current")
_CepConfigFallingThreshold_Type = CiscoEntPerfMeasurement
_CepConfigFallingThreshold_Object = MibTableColumn
cepConfigFallingThreshold = _CepConfigFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 5),
    _CepConfigFallingThreshold_Type()
)
cepConfigFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cepConfigFallingThreshold.setStatus("current")


class _CepConfigThresholdNotifEnabled_Type(TruthValue):
    """Custom type cepConfigThresholdNotifEnabled based on TruthValue"""


_CepConfigThresholdNotifEnabled_Object = MibTableColumn
cepConfigThresholdNotifEnabled = _CepConfigThresholdNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 2, 1, 6),
    _CepConfigThresholdNotifEnabled_Type()
)
cepConfigThresholdNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cepConfigThresholdNotifEnabled.setStatus("current")
_CepStatsTable_Object = MibTable
cepStatsTable = _CepStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 3)
)
if mibBuilder.loadTexts:
    cepStatsTable.setStatus("current")
_CepStatsEntry_Object = MibTableRow
cepStatsEntry = _CepStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 3, 1)
)
cepStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigInterval"),
    (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfType"),
)
if mibBuilder.loadTexts:
    cepStatsEntry.setStatus("current")
_CepStatsAlgorithm_Type = CiscoEntPerfIntervalAlgo
_CepStatsAlgorithm_Object = MibTableColumn
cepStatsAlgorithm = _CepStatsAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 3, 1, 1),
    _CepStatsAlgorithm_Type()
)
cepStatsAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepStatsAlgorithm.setStatus("current")
_CepStatsMeasurement_Type = CiscoEntPerfMeasurement
_CepStatsMeasurement_Object = MibTableColumn
cepStatsMeasurement = _CepStatsMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 3, 1, 2),
    _CepStatsMeasurement_Type()
)
cepStatsMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepStatsMeasurement.setStatus("current")
_CepEntityIntervalTable_Object = MibTable
cepEntityIntervalTable = _CepEntityIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4)
)
if mibBuilder.loadTexts:
    cepEntityIntervalTable.setStatus("current")
_CepEntityIntervalEntry_Object = MibTableRow
cepEntityIntervalEntry = _CepEntityIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4, 1)
)
cepEntityIntervalEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepHistInterval"),
)
if mibBuilder.loadTexts:
    cepEntityIntervalEntry.setStatus("current")
_CepHistInterval_Type = CiscoEntPerfHistInterval
_CepHistInterval_Object = MibTableColumn
cepHistInterval = _CepHistInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4, 1, 1),
    _CepHistInterval_Type()
)
cepHistInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cepHistInterval.setStatus("current")


class _CepIntervalTimeElapsed_Type(Unsigned32):
    """Custom type cepIntervalTimeElapsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_CepIntervalTimeElapsed_Type.__name__ = "Unsigned32"
_CepIntervalTimeElapsed_Object = MibTableColumn
cepIntervalTimeElapsed = _CepIntervalTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4, 1, 2),
    _CepIntervalTimeElapsed_Type()
)
cepIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepIntervalTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    cepIntervalTimeElapsed.setUnits("seconds")


class _CepValidIntervalCount_Type(Unsigned32):
    """Custom type cepValidIntervalCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CepValidIntervalCount_Type.__name__ = "Unsigned32"
_CepValidIntervalCount_Object = MibTableColumn
cepValidIntervalCount = _CepValidIntervalCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 4, 1, 3),
    _CepValidIntervalCount_Type()
)
cepValidIntervalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepValidIntervalCount.setStatus("current")
_CepIntervalStatsTable_Object = MibTable
cepIntervalStatsTable = _CepIntervalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5)
)
if mibBuilder.loadTexts:
    cepIntervalStatsTable.setStatus("current")
_CepIntervalStatsEntry_Object = MibTableRow
cepIntervalStatsEntry = _CepIntervalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1)
)
cepIntervalStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepHistInterval"),
    (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfType"),
    (0, "CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalNumber"),
)
if mibBuilder.loadTexts:
    cepIntervalStatsEntry.setStatus("current")


class _CepIntervalNumber_Type(Unsigned32):
    """Custom type cepIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CepIntervalNumber_Type.__name__ = "Unsigned32"
_CepIntervalNumber_Object = MibTableColumn
cepIntervalNumber = _CepIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 1),
    _CepIntervalNumber_Type()
)
cepIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cepIntervalNumber.setStatus("current")
_CepIntervalStatsValidData_Type = TruthValue
_CepIntervalStatsValidData_Object = MibTableColumn
cepIntervalStatsValidData = _CepIntervalStatsValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 2),
    _CepIntervalStatsValidData_Type()
)
cepIntervalStatsValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepIntervalStatsValidData.setStatus("current")
_CepIntervalStatsRange_Type = CiscoEntPerfRange
_CepIntervalStatsRange_Object = MibTableColumn
cepIntervalStatsRange = _CepIntervalStatsRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 3),
    _CepIntervalStatsRange_Type()
)
cepIntervalStatsRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepIntervalStatsRange.setStatus("current")
_CepIntervalStatsMeasurement_Type = CiscoEntPerfMeasurement
_CepIntervalStatsMeasurement_Object = MibTableColumn
cepIntervalStatsMeasurement = _CepIntervalStatsMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 4),
    _CepIntervalStatsMeasurement_Type()
)
cepIntervalStatsMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepIntervalStatsMeasurement.setStatus("current")
_CepIntervalStatsCreateTime_Type = TimeStamp
_CepIntervalStatsCreateTime_Object = MibTableColumn
cepIntervalStatsCreateTime = _CepIntervalStatsCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 5, 1, 5),
    _CepIntervalStatsCreateTime_Type()
)
cepIntervalStatsCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepIntervalStatsCreateTime.setStatus("current")
_CiscoEntityPerformanceMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoEntityPerformanceMIBNotifObjects = _CiscoEntityPerformanceMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 6)
)


class _CepThresholdNotifEnabled_Type(TruthValue):
    """Custom type cepThresholdNotifEnabled based on TruthValue"""


_CepThresholdNotifEnabled_Object = MibScalar
cepThresholdNotifEnabled = _CepThresholdNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 6, 1),
    _CepThresholdNotifEnabled_Type()
)
cepThresholdNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cepThresholdNotifEnabled.setStatus("current")


class _CepThroughputNotifEnabled_Type(TruthValue):
    """Custom type cepThroughputNotifEnabled based on TruthValue"""


_CepThroughputNotifEnabled_Object = MibScalar
cepThroughputNotifEnabled = _CepThroughputNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 6, 2),
    _CepThroughputNotifEnabled_Type()
)
cepThroughputNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cepThroughputNotifEnabled.setStatus("current")
_CepThroughputTable_Object = MibTable
cepThroughputTable = _CepThroughputTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7)
)
if mibBuilder.loadTexts:
    cepThroughputTable.setStatus("current")
_CepThroughputEntry_Object = MibTableRow
cepThroughputEntry = _CepThroughputEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1)
)
cepThroughputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cepThroughputEntry.setStatus("current")
_CepThroughputLicensedBW_Type = Counter64
_CepThroughputLicensedBW_Object = MibTableColumn
cepThroughputLicensedBW = _CepThroughputLicensedBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 1),
    _CepThroughputLicensedBW_Type()
)
cepThroughputLicensedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepThroughputLicensedBW.setStatus("current")
if mibBuilder.loadTexts:
    cepThroughputLicensedBW.setUnits("bits per second")


class _CepThroughputLevel_Type(Integer32):
    """Custom type cepThroughputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exceed", 3),
          ("normal", 1),
          ("warning", 2))
    )


_CepThroughputLevel_Type.__name__ = "Integer32"
_CepThroughputLevel_Object = MibTableColumn
cepThroughputLevel = _CepThroughputLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 2),
    _CepThroughputLevel_Type()
)
cepThroughputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepThroughputLevel.setStatus("current")


class _CepThroughputInterval_Type(Integer32):
    """Custom type cepThroughputInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_CepThroughputInterval_Type.__name__ = "Integer32"
_CepThroughputInterval_Object = MibTableColumn
cepThroughputInterval = _CepThroughputInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 3),
    _CepThroughputInterval_Type()
)
cepThroughputInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cepThroughputInterval.setStatus("current")
if mibBuilder.loadTexts:
    cepThroughputInterval.setUnits("seconds")


class _CepThroughputThreshold_Type(Integer32):
    """Custom type cepThroughputThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 95),
    )


_CepThroughputThreshold_Type.__name__ = "Integer32"
_CepThroughputThreshold_Object = MibTableColumn
cepThroughputThreshold = _CepThroughputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 4),
    _CepThroughputThreshold_Type()
)
cepThroughputThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cepThroughputThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cepThroughputThreshold.setUnits("percent")
_CepThroughputAvgRate_Type = Counter64
_CepThroughputAvgRate_Object = MibTableColumn
cepThroughputAvgRate = _CepThroughputAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 1, 7, 1, 5),
    _CepThroughputAvgRate_Type()
)
cepThroughputAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cepThroughputAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    cepThroughputAvgRate.setUnits("bits per second")
_CiscoEntityPerformanceMIBConform_ObjectIdentity = ObjectIdentity
ciscoEntityPerformanceMIBConform = _CiscoEntityPerformanceMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 2)
)
_CiscoEntityPerformanceMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEntityPerformanceMIBCompliances = _CiscoEntityPerformanceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 1)
)
_CiscoEntityPerformanceMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEntityPerformanceMIBGroups = _CiscoEntityPerformanceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2)
)

# Managed Objects groups

ciscoEntityPerformanceMIBEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 1)
)
ciscoEntityPerformanceMIBEntityGroup.setObjects(
      *(("CISCO-ENTITY-PERFORMANCE-MIB", "cepEntityNumReloads"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepEntityLastReloadTime"))
)
if mibBuilder.loadTexts:
    ciscoEntityPerformanceMIBEntityGroup.setStatus("current")

ciscoEntityPerformanceMIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 2)
)
ciscoEntityPerformanceMIBConfigGroup.setObjects(
      *(("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigRisingThreshold"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigFallingThreshold"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfRange"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigThresholdNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoEntityPerformanceMIBConfigGroup.setStatus("current")

ciscoEntityPerformanceMIBPerfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 3)
)
ciscoEntityPerformanceMIBPerfStatsGroup.setObjects(
      *(("CISCO-ENTITY-PERFORMANCE-MIB", "cepStatsAlgorithm"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepStatsMeasurement"))
)
if mibBuilder.loadTexts:
    ciscoEntityPerformanceMIBPerfStatsGroup.setStatus("current")

ciscoEntityPerformanceMIBEntityIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 4)
)
ciscoEntityPerformanceMIBEntityIntervalGroup.setObjects(
      *(("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalTimeElapsed"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepValidIntervalCount"))
)
if mibBuilder.loadTexts:
    ciscoEntityPerformanceMIBEntityIntervalGroup.setStatus("current")

ciscoEntityPerformanceMIBIntervalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 5)
)
ciscoEntityPerformanceMIBIntervalStatsGroup.setObjects(
      *(("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalStatsValidData"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalStatsMeasurement"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalStatsCreateTime"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepIntervalStatsRange"))
)
if mibBuilder.loadTexts:
    ciscoEntityPerformanceMIBIntervalStatsGroup.setStatus("current")

ciscoEntityPerformanceMIBNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 6)
)
ciscoEntityPerformanceMIBNotifControlGroup.setObjects(
      *(("CISCO-ENTITY-PERFORMANCE-MIB", "cepThresholdNotifEnabled"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoEntityPerformanceMIBNotifControlGroup.setStatus("current")

ciscoEntityPerformanceMIBThroughputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 8)
)
ciscoEntityPerformanceMIBThroughputGroup.setObjects(
      *(("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputLicensedBW"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputLevel"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputInterval"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputThreshold"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputAvgRate"))
)
if mibBuilder.loadTexts:
    ciscoEntityPerformanceMIBThroughputGroup.setStatus("current")


# Notification objects

cepPerfThreshRisingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 0, 1)
)
cepPerfThreshRisingEvent.setObjects(
      *(("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfRange"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigRisingThreshold"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepStatsMeasurement"))
)
if mibBuilder.loadTexts:
    cepPerfThreshRisingEvent.setStatus(
        "current"
    )

cepPerfThreshFallingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 0, 2)
)
cepPerfThreshFallingEvent.setObjects(
      *(("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigPerfRange"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepConfigFallingThreshold"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepStatsMeasurement"))
)
if mibBuilder.loadTexts:
    cepPerfThreshFallingEvent.setStatus(
        "current"
    )

cepThroughputNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 0, 3)
)
cepThroughputNotif.setObjects(
      *(("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputLicensedBW"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputLevel"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputAvgRate"))
)
if mibBuilder.loadTexts:
    cepThroughputNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoEntityPerformanceMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 2, 7)
)
ciscoEntityPerformanceMIBNotificationGroup.setObjects(
      *(("CISCO-ENTITY-PERFORMANCE-MIB", "cepPerfThreshRisingEvent"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepPerfThreshFallingEvent"),
        ("CISCO-ENTITY-PERFORMANCE-MIB", "cepThroughputNotif"))
)
if mibBuilder.loadTexts:
    ciscoEntityPerformanceMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEntityPerformanceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 756, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEntityPerformanceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-PERFORMANCE-MIB",
    **{"CiscoEntPerfMeasurement": CiscoEntPerfMeasurement,
       "CiscoEntPerfRange": CiscoEntPerfRange,
       "CiscoEntPerfType": CiscoEntPerfType,
       "CiscoEntPerfInterval": CiscoEntPerfInterval,
       "CiscoEntPerfHistInterval": CiscoEntPerfHistInterval,
       "CiscoEntPerfIntervalAlgo": CiscoEntPerfIntervalAlgo,
       "ciscoEntityPerformanceMIB": ciscoEntityPerformanceMIB,
       "ciscoEntityPerformanceMIBNotifs": ciscoEntityPerformanceMIBNotifs,
       "cepPerfThreshRisingEvent": cepPerfThreshRisingEvent,
       "cepPerfThreshFallingEvent": cepPerfThreshFallingEvent,
       "cepThroughputNotif": cepThroughputNotif,
       "ciscoEntityPerformanceMIBObjects": ciscoEntityPerformanceMIBObjects,
       "cepEntityTable": cepEntityTable,
       "cepEntityEntry": cepEntityEntry,
       "cepEntityNumReloads": cepEntityNumReloads,
       "cepEntityLastReloadTime": cepEntityLastReloadTime,
       "cepConfigTable": cepConfigTable,
       "cepConfigEntry": cepConfigEntry,
       "cepConfigInterval": cepConfigInterval,
       "cepConfigPerfType": cepConfigPerfType,
       "cepConfigPerfRange": cepConfigPerfRange,
       "cepConfigRisingThreshold": cepConfigRisingThreshold,
       "cepConfigFallingThreshold": cepConfigFallingThreshold,
       "cepConfigThresholdNotifEnabled": cepConfigThresholdNotifEnabled,
       "cepStatsTable": cepStatsTable,
       "cepStatsEntry": cepStatsEntry,
       "cepStatsAlgorithm": cepStatsAlgorithm,
       "cepStatsMeasurement": cepStatsMeasurement,
       "cepEntityIntervalTable": cepEntityIntervalTable,
       "cepEntityIntervalEntry": cepEntityIntervalEntry,
       "cepHistInterval": cepHistInterval,
       "cepIntervalTimeElapsed": cepIntervalTimeElapsed,
       "cepValidIntervalCount": cepValidIntervalCount,
       "cepIntervalStatsTable": cepIntervalStatsTable,
       "cepIntervalStatsEntry": cepIntervalStatsEntry,
       "cepIntervalNumber": cepIntervalNumber,
       "cepIntervalStatsValidData": cepIntervalStatsValidData,
       "cepIntervalStatsRange": cepIntervalStatsRange,
       "cepIntervalStatsMeasurement": cepIntervalStatsMeasurement,
       "cepIntervalStatsCreateTime": cepIntervalStatsCreateTime,
       "ciscoEntityPerformanceMIBNotifObjects": ciscoEntityPerformanceMIBNotifObjects,
       "cepThresholdNotifEnabled": cepThresholdNotifEnabled,
       "cepThroughputNotifEnabled": cepThroughputNotifEnabled,
       "cepThroughputTable": cepThroughputTable,
       "cepThroughputEntry": cepThroughputEntry,
       "cepThroughputLicensedBW": cepThroughputLicensedBW,
       "cepThroughputLevel": cepThroughputLevel,
       "cepThroughputInterval": cepThroughputInterval,
       "cepThroughputThreshold": cepThroughputThreshold,
       "cepThroughputAvgRate": cepThroughputAvgRate,
       "ciscoEntityPerformanceMIBConform": ciscoEntityPerformanceMIBConform,
       "ciscoEntityPerformanceMIBCompliances": ciscoEntityPerformanceMIBCompliances,
       "ciscoEntityPerformanceMIBCompliance": ciscoEntityPerformanceMIBCompliance,
       "ciscoEntityPerformanceMIBGroups": ciscoEntityPerformanceMIBGroups,
       "ciscoEntityPerformanceMIBEntityGroup": ciscoEntityPerformanceMIBEntityGroup,
       "ciscoEntityPerformanceMIBConfigGroup": ciscoEntityPerformanceMIBConfigGroup,
       "ciscoEntityPerformanceMIBPerfStatsGroup": ciscoEntityPerformanceMIBPerfStatsGroup,
       "ciscoEntityPerformanceMIBEntityIntervalGroup": ciscoEntityPerformanceMIBEntityIntervalGroup,
       "ciscoEntityPerformanceMIBIntervalStatsGroup": ciscoEntityPerformanceMIBIntervalStatsGroup,
       "ciscoEntityPerformanceMIBNotifControlGroup": ciscoEntityPerformanceMIBNotifControlGroup,
       "ciscoEntityPerformanceMIBNotificationGroup": ciscoEntityPerformanceMIBNotificationGroup,
       "ciscoEntityPerformanceMIBThroughputGroup": ciscoEntityPerformanceMIBThroughputGroup}
)
