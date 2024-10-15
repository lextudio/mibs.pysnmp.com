# SNMP MIB module (CISCO-WIRELESS-P2MP-LINK-METRICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WIRELESS-P2MP-LINK-METRICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:38 2024
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

(CwrCwConsecutiveSevErrSecond,
 CwrCwDegradedSecond,
 CwrCwErrorFreeSecond,
 CwrCwErroredSecond,
 CwrCwSeverelyErroredSecond,
 CwrFixedPointPrecision,
 CwrFixedPointScale,
 CwrFixedPointValue,
 CwrPercentageValue,
 CwrUpdateTime,
 WirelessGauge64) = mibBuilder.importSymbols(
    "CISCO-WIRELESS-TC-MIB",
    "CwrCwConsecutiveSevErrSecond",
    "CwrCwDegradedSecond",
    "CwrCwErrorFreeSecond",
    "CwrCwErroredSecond",
    "CwrCwSeverelyErroredSecond",
    "CwrFixedPointPrecision",
    "CwrFixedPointScale",
    "CwrFixedPointValue",
    "CwrPercentageValue",
    "CwrUpdateTime",
    "WirelessGauge64")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

ciscoWirelessLinkMetricsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 181)
)
ciscoWirelessLinkMetricsMIB.setRevisions(
        ("2006-01-04 10:03",
         "2000-02-14 19:10")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_P2mpLinkMetricsGroup_ObjectIdentity = ObjectIdentity
p2mpLinkMetricsGroup = _P2mpLinkMetricsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1)
)
_P2mpMetricsPrecisionTable_Object = MibTable
p2mpMetricsPrecisionTable = _P2mpMetricsPrecisionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1, 1)
)
if mibBuilder.loadTexts:
    p2mpMetricsPrecisionTable.setStatus("current")
_P2mpMetricsPrecisionEntry_Object = MibTableRow
p2mpMetricsPrecisionEntry = _P2mpMetricsPrecisionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1, 1, 1)
)
p2mpMetricsPrecisionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    p2mpMetricsPrecisionEntry.setStatus("current")
_P2mpLinkMetricsScale_Type = CwrFixedPointScale
_P2mpLinkMetricsScale_Object = MibTableColumn
p2mpLinkMetricsScale = _P2mpLinkMetricsScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1, 1, 1, 1),
    _P2mpLinkMetricsScale_Type()
)
p2mpLinkMetricsScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpLinkMetricsScale.setStatus("current")
_P2mpLinkMetricsPrecision_Type = CwrFixedPointPrecision
_P2mpLinkMetricsPrecision_Object = MibTableColumn
p2mpLinkMetricsPrecision = _P2mpLinkMetricsPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1, 1, 1, 2),
    _P2mpLinkMetricsPrecision_Type()
)
p2mpLinkMetricsPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpLinkMetricsPrecision.setStatus("current")
_P2mpMetricsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
p2mpMetricsMIBNotificationPrefix = _P2mpMetricsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1, 2)
)
_P2mpMetricsMIBNotification_ObjectIdentity = ObjectIdentity
p2mpMetricsMIBNotification = _P2mpMetricsMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1, 2, 0)
)
_P2mpSuLinkMetricsGroup_ObjectIdentity = ObjectIdentity
p2mpSuLinkMetricsGroup = _P2mpSuLinkMetricsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2)
)
_P2mpSuLinkMetricsThreshTable_Object = MibTable
p2mpSuLinkMetricsThreshTable = _P2mpSuLinkMetricsThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 1)
)
if mibBuilder.loadTexts:
    p2mpSuLinkMetricsThreshTable.setStatus("current")
_P2mpSuLinkMetricsThreshEntry_Object = MibTableRow
p2mpSuLinkMetricsThreshEntry = _P2mpSuLinkMetricsThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 1, 1)
)
p2mpSuLinkMetricsThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    p2mpSuLinkMetricsThreshEntry.setStatus("current")
_P2mpSuLinkESThresh_Type = Unsigned32
_P2mpSuLinkESThresh_Object = MibTableColumn
p2mpSuLinkESThresh = _P2mpSuLinkESThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 1, 1, 1),
    _P2mpSuLinkESThresh_Type()
)
p2mpSuLinkESThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpSuLinkESThresh.setStatus("current")
_P2mpSuLinkDSThresh_Type = CwrPercentageValue
_P2mpSuLinkDSThresh_Object = MibTableColumn
p2mpSuLinkDSThresh = _P2mpSuLinkDSThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 1, 1, 2),
    _P2mpSuLinkDSThresh_Type()
)
p2mpSuLinkDSThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpSuLinkDSThresh.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSuLinkDSThresh.setUnits("0.00001 percent")
_P2mpSuLinkSESThresh_Type = CwrPercentageValue
_P2mpSuLinkSESThresh_Object = MibTableColumn
p2mpSuLinkSESThresh = _P2mpSuLinkSESThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 1, 1, 3),
    _P2mpSuLinkSESThresh_Type()
)
p2mpSuLinkSESThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpSuLinkSESThresh.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSuLinkSESThresh.setUnits("0.00001 percent")
_P2mpSuLinkCSESThresh_Type = Unsigned32
_P2mpSuLinkCSESThresh_Object = MibTableColumn
p2mpSuLinkCSESThresh = _P2mpSuLinkCSESThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 1, 1, 4),
    _P2mpSuLinkCSESThresh_Type()
)
p2mpSuLinkCSESThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpSuLinkCSESThresh.setStatus("current")
_P2mpSuLink1HrESAlarmThresh_Type = Unsigned32
_P2mpSuLink1HrESAlarmThresh_Object = MibTableColumn
p2mpSuLink1HrESAlarmThresh = _P2mpSuLink1HrESAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 1, 1, 5),
    _P2mpSuLink1HrESAlarmThresh_Type()
)
p2mpSuLink1HrESAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpSuLink1HrESAlarmThresh.setStatus("current")
_P2mpSuLink1HrSESAlarmThresh_Type = Unsigned32
_P2mpSuLink1HrSESAlarmThresh_Object = MibTableColumn
p2mpSuLink1HrSESAlarmThresh = _P2mpSuLink1HrSESAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 1, 1, 6),
    _P2mpSuLink1HrSESAlarmThresh_Type()
)
p2mpSuLink1HrSESAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpSuLink1HrSESAlarmThresh.setStatus("current")
_P2mpSuLink1HrCSESAlarmThresh_Type = Unsigned32
_P2mpSuLink1HrCSESAlarmThresh_Object = MibTableColumn
p2mpSuLink1HrCSESAlarmThresh = _P2mpSuLink1HrCSESAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 1, 1, 7),
    _P2mpSuLink1HrCSESAlarmThresh_Type()
)
p2mpSuLink1HrCSESAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpSuLink1HrCSESAlarmThresh.setStatus("current")
_P2mpSuLink1HrDCSAlarmThresh_Type = Unsigned32
_P2mpSuLink1HrDCSAlarmThresh_Object = MibTableColumn
p2mpSuLink1HrDCSAlarmThresh = _P2mpSuLink1HrDCSAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 1, 1, 8),
    _P2mpSuLink1HrDCSAlarmThresh_Type()
)
p2mpSuLink1HrDCSAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpSuLink1HrDCSAlarmThresh.setStatus("current")
_P2mpSu1SecMetricsTable_Object = MibTable
p2mpSu1SecMetricsTable = _P2mpSu1SecMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 2)
)
if mibBuilder.loadTexts:
    p2mpSu1SecMetricsTable.setStatus("current")
_P2mpSu1SecMetricsEntry_Object = MibTableRow
p2mpSu1SecMetricsEntry = _P2mpSu1SecMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 2, 1)
)
p2mpSu1SecMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1SecIndex"),
)
if mibBuilder.loadTexts:
    p2mpSu1SecMetricsEntry.setStatus("current")


class _P2mpSu1SecIndex_Type(Integer32):
    """Custom type p2mpSu1SecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_P2mpSu1SecIndex_Type.__name__ = "Integer32"
_P2mpSu1SecIndex_Object = MibTableColumn
p2mpSu1SecIndex = _P2mpSu1SecIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 2, 1, 1),
    _P2mpSu1SecIndex_Type()
)
p2mpSu1SecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpSu1SecIndex.setStatus("current")
_P2mpSu1SecUpdateTime_Type = CwrUpdateTime
_P2mpSu1SecUpdateTime_Object = MibTableColumn
p2mpSu1SecUpdateTime = _P2mpSu1SecUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 2, 1, 2),
    _P2mpSu1SecUpdateTime_Type()
)
p2mpSu1SecUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1SecUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1SecUpdateTime.setUnits("seconds")


class _P2mpSu1SecType_Type(Integer32):
    """Custom type p2mpSu1SecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("errorFree", 1),
          ("errored", 2),
          ("sevErrored", 4),
          ("syncLoss", 5),
          ("unknown", 0))
    )


_P2mpSu1SecType_Type.__name__ = "Integer32"
_P2mpSu1SecType_Object = MibTableColumn
p2mpSu1SecType = _P2mpSu1SecType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 2, 1, 3),
    _P2mpSu1SecType_Type()
)
p2mpSu1SecType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1SecType.setStatus("current")
_P2mpSu1SecTotalCodewords_Type = WirelessGauge64
_P2mpSu1SecTotalCodewords_Object = MibTableColumn
p2mpSu1SecTotalCodewords = _P2mpSu1SecTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 2, 1, 4),
    _P2mpSu1SecTotalCodewords_Type()
)
p2mpSu1SecTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1SecTotalCodewords.setStatus("current")
_P2mpSu1SecTotalErrCodewords_Type = WirelessGauge64
_P2mpSu1SecTotalErrCodewords_Object = MibTableColumn
p2mpSu1SecTotalErrCodewords = _P2mpSu1SecTotalErrCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 2, 1, 5),
    _P2mpSu1SecTotalErrCodewords_Type()
)
p2mpSu1SecTotalErrCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1SecTotalErrCodewords.setStatus("current")
_P2mpSu1SecValidDataPkt_Type = Counter32
_P2mpSu1SecValidDataPkt_Object = MibTableColumn
p2mpSu1SecValidDataPkt = _P2mpSu1SecValidDataPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 2, 1, 6),
    _P2mpSu1SecValidDataPkt_Type()
)
p2mpSu1SecValidDataPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1SecValidDataPkt.setStatus("current")
_P2mpSu1MinMetricsTable_Object = MibTable
p2mpSu1MinMetricsTable = _P2mpSu1MinMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3)
)
if mibBuilder.loadTexts:
    p2mpSu1MinMetricsTable.setStatus("current")
_P2mpSu1MinMetricsEntry_Object = MibTableRow
p2mpSu1MinMetricsEntry = _P2mpSu1MinMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1)
)
p2mpSu1MinMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinIndex"),
)
if mibBuilder.loadTexts:
    p2mpSu1MinMetricsEntry.setStatus("current")


class _P2mpSu1MinIndex_Type(Integer32):
    """Custom type p2mpSu1MinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_P2mpSu1MinIndex_Type.__name__ = "Integer32"
_P2mpSu1MinIndex_Object = MibTableColumn
p2mpSu1MinIndex = _P2mpSu1MinIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 1),
    _P2mpSu1MinIndex_Type()
)
p2mpSu1MinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpSu1MinIndex.setStatus("current")
_P2mpSu1MinUpdateTime_Type = CwrUpdateTime
_P2mpSu1MinUpdateTime_Object = MibTableColumn
p2mpSu1MinUpdateTime = _P2mpSu1MinUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 2),
    _P2mpSu1MinUpdateTime_Type()
)
p2mpSu1MinUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1MinUpdateTime.setUnits("seconds")
_P2mpSu1MinTotalCodewords_Type = WirelessGauge64
_P2mpSu1MinTotalCodewords_Object = MibTableColumn
p2mpSu1MinTotalCodewords = _P2mpSu1MinTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 3),
    _P2mpSu1MinTotalCodewords_Type()
)
p2mpSu1MinTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinTotalCodewords.setStatus("current")
_P2mpSu1MinTotalErrCodewords_Type = WirelessGauge64
_P2mpSu1MinTotalErrCodewords_Object = MibTableColumn
p2mpSu1MinTotalErrCodewords = _P2mpSu1MinTotalErrCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 4),
    _P2mpSu1MinTotalErrCodewords_Type()
)
p2mpSu1MinTotalErrCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinTotalErrCodewords.setStatus("current")
_P2mpSu1MinValidDataPkt_Type = Counter32
_P2mpSu1MinValidDataPkt_Object = MibTableColumn
p2mpSu1MinValidDataPkt = _P2mpSu1MinValidDataPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 5),
    _P2mpSu1MinValidDataPkt_Type()
)
p2mpSu1MinValidDataPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinValidDataPkt.setStatus("current")
_P2mpSu1MinErrorFreeSeconds_Type = CwrCwErrorFreeSecond
_P2mpSu1MinErrorFreeSeconds_Object = MibTableColumn
p2mpSu1MinErrorFreeSeconds = _P2mpSu1MinErrorFreeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 6),
    _P2mpSu1MinErrorFreeSeconds_Type()
)
p2mpSu1MinErrorFreeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinErrorFreeSeconds.setStatus("current")
_P2mpSu1MinErroredSeconds_Type = CwrCwErroredSecond
_P2mpSu1MinErroredSeconds_Object = MibTableColumn
p2mpSu1MinErroredSeconds = _P2mpSu1MinErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 7),
    _P2mpSu1MinErroredSeconds_Type()
)
p2mpSu1MinErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinErroredSeconds.setStatus("current")
_P2mpSu1MinDegradedSeconds_Type = CwrCwDegradedSecond
_P2mpSu1MinDegradedSeconds_Object = MibTableColumn
p2mpSu1MinDegradedSeconds = _P2mpSu1MinDegradedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 8),
    _P2mpSu1MinDegradedSeconds_Type()
)
p2mpSu1MinDegradedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinDegradedSeconds.setStatus("current")
_P2mpSu1MinSevErroredSeconds_Type = CwrCwSeverelyErroredSecond
_P2mpSu1MinSevErroredSeconds_Object = MibTableColumn
p2mpSu1MinSevErroredSeconds = _P2mpSu1MinSevErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 9),
    _P2mpSu1MinSevErroredSeconds_Type()
)
p2mpSu1MinSevErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinSevErroredSeconds.setStatus("current")
_P2mpSu1MinConsecSevErrSeconds_Type = CwrCwConsecutiveSevErrSecond
_P2mpSu1MinConsecSevErrSeconds_Object = MibTableColumn
p2mpSu1MinConsecSevErrSeconds = _P2mpSu1MinConsecSevErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 10),
    _P2mpSu1MinConsecSevErrSeconds_Type()
)
p2mpSu1MinConsecSevErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinConsecSevErrSeconds.setStatus("current")
_P2mpSu1MinSyncLossSeconds_Type = Counter32
_P2mpSu1MinSyncLossSeconds_Object = MibTableColumn
p2mpSu1MinSyncLossSeconds = _P2mpSu1MinSyncLossSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 11),
    _P2mpSu1MinSyncLossSeconds_Type()
)
p2mpSu1MinSyncLossSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinSyncLossSeconds.setStatus("current")
_P2mpSu1MinTxPowerMax_Type = CwrFixedPointValue
_P2mpSu1MinTxPowerMax_Object = MibTableColumn
p2mpSu1MinTxPowerMax = _P2mpSu1MinTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 12),
    _P2mpSu1MinTxPowerMax_Type()
)
p2mpSu1MinTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinTxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1MinTxPowerMax.setUnits("dBm - decibel milliwatts")
_P2mpSu1MinTxPowerMin_Type = CwrFixedPointValue
_P2mpSu1MinTxPowerMin_Object = MibTableColumn
p2mpSu1MinTxPowerMin = _P2mpSu1MinTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 13),
    _P2mpSu1MinTxPowerMin_Type()
)
p2mpSu1MinTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinTxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1MinTxPowerMin.setUnits("dBm - decibel milliwatts")
_P2mpSu1MinTxPowerAvg_Type = CwrFixedPointValue
_P2mpSu1MinTxPowerAvg_Object = MibTableColumn
p2mpSu1MinTxPowerAvg = _P2mpSu1MinTxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 14),
    _P2mpSu1MinTxPowerAvg_Type()
)
p2mpSu1MinTxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinTxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1MinTxPowerAvg.setUnits("dBm - decibel milliwatts")
_P2mpSu1MinMainAntRxPowerMax_Type = CwrFixedPointValue
_P2mpSu1MinMainAntRxPowerMax_Object = MibTableColumn
p2mpSu1MinMainAntRxPowerMax = _P2mpSu1MinMainAntRxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 15),
    _P2mpSu1MinMainAntRxPowerMax_Type()
)
p2mpSu1MinMainAntRxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinMainAntRxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1MinMainAntRxPowerMax.setUnits("dBm - decibel milliwatts")
_P2mpSu1MinMainAntRxPowerMin_Type = CwrFixedPointValue
_P2mpSu1MinMainAntRxPowerMin_Object = MibTableColumn
p2mpSu1MinMainAntRxPowerMin = _P2mpSu1MinMainAntRxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 16),
    _P2mpSu1MinMainAntRxPowerMin_Type()
)
p2mpSu1MinMainAntRxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinMainAntRxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1MinMainAntRxPowerMin.setUnits("dBm - decibel milliwatts")
_P2mpSu1MinMainAntRxPowerAvg_Type = CwrFixedPointValue
_P2mpSu1MinMainAntRxPowerAvg_Object = MibTableColumn
p2mpSu1MinMainAntRxPowerAvg = _P2mpSu1MinMainAntRxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 17),
    _P2mpSu1MinMainAntRxPowerAvg_Type()
)
p2mpSu1MinMainAntRxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinMainAntRxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1MinMainAntRxPowerAvg.setUnits("dBm - decibel milliwatts")
_P2mpSu1MinDivAntRxPowerMax_Type = CwrFixedPointValue
_P2mpSu1MinDivAntRxPowerMax_Object = MibTableColumn
p2mpSu1MinDivAntRxPowerMax = _P2mpSu1MinDivAntRxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 18),
    _P2mpSu1MinDivAntRxPowerMax_Type()
)
p2mpSu1MinDivAntRxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinDivAntRxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1MinDivAntRxPowerMax.setUnits("dBm - decibel milliwatts")
_P2mpSu1MinDivAntRxPowerMin_Type = CwrFixedPointValue
_P2mpSu1MinDivAntRxPowerMin_Object = MibTableColumn
p2mpSu1MinDivAntRxPowerMin = _P2mpSu1MinDivAntRxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 19),
    _P2mpSu1MinDivAntRxPowerMin_Type()
)
p2mpSu1MinDivAntRxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinDivAntRxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1MinDivAntRxPowerMin.setUnits("dBm - decibel milliwatts")
_P2mpSu1MinDivAntRxPowerAvg_Type = CwrFixedPointValue
_P2mpSu1MinDivAntRxPowerAvg_Object = MibTableColumn
p2mpSu1MinDivAntRxPowerAvg = _P2mpSu1MinDivAntRxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 3, 1, 20),
    _P2mpSu1MinDivAntRxPowerAvg_Type()
)
p2mpSu1MinDivAntRxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1MinDivAntRxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1MinDivAntRxPowerAvg.setUnits("dBm - decibel milliwatts")
_P2mpSu1HrMetricsTable_Object = MibTable
p2mpSu1HrMetricsTable = _P2mpSu1HrMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4)
)
if mibBuilder.loadTexts:
    p2mpSu1HrMetricsTable.setStatus("current")
_P2mpSu1HrMetricsEntry_Object = MibTableRow
p2mpSu1HrMetricsEntry = _P2mpSu1HrMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1)
)
p2mpSu1HrMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrIndex"),
)
if mibBuilder.loadTexts:
    p2mpSu1HrMetricsEntry.setStatus("current")


class _P2mpSu1HrIndex_Type(Integer32):
    """Custom type p2mpSu1HrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_P2mpSu1HrIndex_Type.__name__ = "Integer32"
_P2mpSu1HrIndex_Object = MibTableColumn
p2mpSu1HrIndex = _P2mpSu1HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 1),
    _P2mpSu1HrIndex_Type()
)
p2mpSu1HrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpSu1HrIndex.setStatus("current")
_P2mpSu1HrUpdateTime_Type = CwrUpdateTime
_P2mpSu1HrUpdateTime_Object = MibTableColumn
p2mpSu1HrUpdateTime = _P2mpSu1HrUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 2),
    _P2mpSu1HrUpdateTime_Type()
)
p2mpSu1HrUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1HrUpdateTime.setUnits("seconds")
_P2mpSu1HrTotalCodewords_Type = WirelessGauge64
_P2mpSu1HrTotalCodewords_Object = MibTableColumn
p2mpSu1HrTotalCodewords = _P2mpSu1HrTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 3),
    _P2mpSu1HrTotalCodewords_Type()
)
p2mpSu1HrTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrTotalCodewords.setStatus("current")
_P2mpSu1HrTotalErrCodewords_Type = WirelessGauge64
_P2mpSu1HrTotalErrCodewords_Object = MibTableColumn
p2mpSu1HrTotalErrCodewords = _P2mpSu1HrTotalErrCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 4),
    _P2mpSu1HrTotalErrCodewords_Type()
)
p2mpSu1HrTotalErrCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrTotalErrCodewords.setStatus("current")
_P2mpSu1HrValidDataPkt_Type = Counter32
_P2mpSu1HrValidDataPkt_Object = MibTableColumn
p2mpSu1HrValidDataPkt = _P2mpSu1HrValidDataPkt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 5),
    _P2mpSu1HrValidDataPkt_Type()
)
p2mpSu1HrValidDataPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrValidDataPkt.setStatus("current")
_P2mpSu1HrErrorFreeSeconds_Type = CwrCwErrorFreeSecond
_P2mpSu1HrErrorFreeSeconds_Object = MibTableColumn
p2mpSu1HrErrorFreeSeconds = _P2mpSu1HrErrorFreeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 6),
    _P2mpSu1HrErrorFreeSeconds_Type()
)
p2mpSu1HrErrorFreeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrErrorFreeSeconds.setStatus("current")
_P2mpSu1HrErroredSeconds_Type = CwrCwErroredSecond
_P2mpSu1HrErroredSeconds_Object = MibTableColumn
p2mpSu1HrErroredSeconds = _P2mpSu1HrErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 7),
    _P2mpSu1HrErroredSeconds_Type()
)
p2mpSu1HrErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrErroredSeconds.setStatus("current")
_P2mpSu1HrSevErroredSeconds_Type = CwrCwSeverelyErroredSecond
_P2mpSu1HrSevErroredSeconds_Object = MibTableColumn
p2mpSu1HrSevErroredSeconds = _P2mpSu1HrSevErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 8),
    _P2mpSu1HrSevErroredSeconds_Type()
)
p2mpSu1HrSevErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrSevErroredSeconds.setStatus("current")
_P2mpSu1HrConsecSvErrSeconds_Type = CwrCwConsecutiveSevErrSecond
_P2mpSu1HrConsecSvErrSeconds_Object = MibTableColumn
p2mpSu1HrConsecSvErrSeconds = _P2mpSu1HrConsecSvErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 9),
    _P2mpSu1HrConsecSvErrSeconds_Type()
)
p2mpSu1HrConsecSvErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrConsecSvErrSeconds.setStatus("current")
_P2mpSu1HrSyncLossSeconds_Type = Counter32
_P2mpSu1HrSyncLossSeconds_Object = MibTableColumn
p2mpSu1HrSyncLossSeconds = _P2mpSu1HrSyncLossSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 10),
    _P2mpSu1HrSyncLossSeconds_Type()
)
p2mpSu1HrSyncLossSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrSyncLossSeconds.setStatus("current")
_P2mpSu1HrDegradedSeconds_Type = CwrCwDegradedSecond
_P2mpSu1HrDegradedSeconds_Object = MibTableColumn
p2mpSu1HrDegradedSeconds = _P2mpSu1HrDegradedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 11),
    _P2mpSu1HrDegradedSeconds_Type()
)
p2mpSu1HrDegradedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrDegradedSeconds.setStatus("current")
_P2mpSu1HrTxPowerMax_Type = CwrFixedPointValue
_P2mpSu1HrTxPowerMax_Object = MibTableColumn
p2mpSu1HrTxPowerMax = _P2mpSu1HrTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 12),
    _P2mpSu1HrTxPowerMax_Type()
)
p2mpSu1HrTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrTxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1HrTxPowerMax.setUnits("dBm - decibel milliwatts")
_P2mpSu1HrTxPowerMin_Type = CwrFixedPointValue
_P2mpSu1HrTxPowerMin_Object = MibTableColumn
p2mpSu1HrTxPowerMin = _P2mpSu1HrTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 13),
    _P2mpSu1HrTxPowerMin_Type()
)
p2mpSu1HrTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrTxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1HrTxPowerMin.setUnits("dBm - decibel milliwatts")
_P2mpSu1HrTxPowerAvg_Type = CwrFixedPointValue
_P2mpSu1HrTxPowerAvg_Object = MibTableColumn
p2mpSu1HrTxPowerAvg = _P2mpSu1HrTxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 14),
    _P2mpSu1HrTxPowerAvg_Type()
)
p2mpSu1HrTxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrTxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1HrTxPowerAvg.setUnits("dBm - decibel milliwatts")
_P2mpSu1HrMainAntRxPowerMax_Type = CwrFixedPointValue
_P2mpSu1HrMainAntRxPowerMax_Object = MibTableColumn
p2mpSu1HrMainAntRxPowerMax = _P2mpSu1HrMainAntRxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 15),
    _P2mpSu1HrMainAntRxPowerMax_Type()
)
p2mpSu1HrMainAntRxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrMainAntRxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1HrMainAntRxPowerMax.setUnits("dBm - decibel milliwatts")
_P2mpSu1HrMainAntRxPowerMin_Type = CwrFixedPointValue
_P2mpSu1HrMainAntRxPowerMin_Object = MibTableColumn
p2mpSu1HrMainAntRxPowerMin = _P2mpSu1HrMainAntRxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 16),
    _P2mpSu1HrMainAntRxPowerMin_Type()
)
p2mpSu1HrMainAntRxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrMainAntRxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1HrMainAntRxPowerMin.setUnits("dBm - decibel milliwatts")
_P2mpSu1HrMainAntRxPowerAvg_Type = CwrFixedPointValue
_P2mpSu1HrMainAntRxPowerAvg_Object = MibTableColumn
p2mpSu1HrMainAntRxPowerAvg = _P2mpSu1HrMainAntRxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 17),
    _P2mpSu1HrMainAntRxPowerAvg_Type()
)
p2mpSu1HrMainAntRxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrMainAntRxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1HrMainAntRxPowerAvg.setUnits("dBm - decibel milliwatts")
_P2mpSu1HrDivAntRxPowerMax_Type = CwrFixedPointValue
_P2mpSu1HrDivAntRxPowerMax_Object = MibTableColumn
p2mpSu1HrDivAntRxPowerMax = _P2mpSu1HrDivAntRxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 18),
    _P2mpSu1HrDivAntRxPowerMax_Type()
)
p2mpSu1HrDivAntRxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrDivAntRxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1HrDivAntRxPowerMax.setUnits("dBm - decibel milliwatts")
_P2mpSu1HrDivAntRxPowerMin_Type = CwrFixedPointValue
_P2mpSu1HrDivAntRxPowerMin_Object = MibTableColumn
p2mpSu1HrDivAntRxPowerMin = _P2mpSu1HrDivAntRxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 19),
    _P2mpSu1HrDivAntRxPowerMin_Type()
)
p2mpSu1HrDivAntRxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrDivAntRxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1HrDivAntRxPowerMin.setUnits("dBm - decibel milliwatts")
_P2mpSu1HrDivAntRxPowerAvg_Type = CwrFixedPointValue
_P2mpSu1HrDivAntRxPowerAvg_Object = MibTableColumn
p2mpSu1HrDivAntRxPowerAvg = _P2mpSu1HrDivAntRxPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 4, 1, 20),
    _P2mpSu1HrDivAntRxPowerAvg_Type()
)
p2mpSu1HrDivAntRxPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSu1HrDivAntRxPowerAvg.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSu1HrDivAntRxPowerAvg.setUnits("dBm - decibel milliwatts")
_P2mpSuCumulativeLinkMetricsTable_Object = MibTable
p2mpSuCumulativeLinkMetricsTable = _P2mpSuCumulativeLinkMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6)
)
if mibBuilder.loadTexts:
    p2mpSuCumulativeLinkMetricsTable.setStatus("current")
_P2mpSuCumulativeLinkMetricsEntry_Object = MibTableRow
p2mpSuCumulativeLinkMetricsEntry = _P2mpSuCumulativeLinkMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1)
)
p2mpSuCumulativeLinkMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    p2mpSuCumulativeLinkMetricsEntry.setStatus("current")
_P2mpSuAvailableSeconds_Type = Counter32
_P2mpSuAvailableSeconds_Object = MibTableColumn
p2mpSuAvailableSeconds = _P2mpSuAvailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 1),
    _P2mpSuAvailableSeconds_Type()
)
p2mpSuAvailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuAvailableSeconds.setStatus("current")
_P2mpSuUnAvailableSeconds_Type = Counter32
_P2mpSuUnAvailableSeconds_Object = MibTableColumn
p2mpSuUnAvailableSeconds = _P2mpSuUnAvailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 2),
    _P2mpSuUnAvailableSeconds_Type()
)
p2mpSuUnAvailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuUnAvailableSeconds.setStatus("current")
_P2mpSuPctAvailSeconds_Type = CwrPercentageValue
_P2mpSuPctAvailSeconds_Object = MibTableColumn
p2mpSuPctAvailSeconds = _P2mpSuPctAvailSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 3),
    _P2mpSuPctAvailSeconds_Type()
)
p2mpSuPctAvailSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuPctAvailSeconds.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSuPctAvailSeconds.setUnits("0.00001 percent")
_P2mpSuSyncLossSeconds_Type = Counter32
_P2mpSuSyncLossSeconds_Object = MibTableColumn
p2mpSuSyncLossSeconds = _P2mpSuSyncLossSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 4),
    _P2mpSuSyncLossSeconds_Type()
)
p2mpSuSyncLossSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuSyncLossSeconds.setStatus("current")
_P2mpSuPctErrorFreeSeconds_Type = CwrPercentageValue
_P2mpSuPctErrorFreeSeconds_Object = MibTableColumn
p2mpSuPctErrorFreeSeconds = _P2mpSuPctErrorFreeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 5),
    _P2mpSuPctErrorFreeSeconds_Type()
)
p2mpSuPctErrorFreeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuPctErrorFreeSeconds.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSuPctErrorFreeSeconds.setUnits("0.00001 percent")
_P2mpSuPctErroredSeconds_Type = CwrPercentageValue
_P2mpSuPctErroredSeconds_Object = MibTableColumn
p2mpSuPctErroredSeconds = _P2mpSuPctErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 6),
    _P2mpSuPctErroredSeconds_Type()
)
p2mpSuPctErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuPctErroredSeconds.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSuPctErroredSeconds.setUnits("0.00001 percent")
_P2mpSuPctSevErroredSeconds_Type = CwrPercentageValue
_P2mpSuPctSevErroredSeconds_Object = MibTableColumn
p2mpSuPctSevErroredSeconds = _P2mpSuPctSevErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 7),
    _P2mpSuPctSevErroredSeconds_Type()
)
p2mpSuPctSevErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuPctSevErroredSeconds.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSuPctSevErroredSeconds.setUnits("0.00001 percent")
_P2mpSuPctDegradedSeconds_Type = CwrPercentageValue
_P2mpSuPctDegradedSeconds_Object = MibTableColumn
p2mpSuPctDegradedSeconds = _P2mpSuPctDegradedSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 8),
    _P2mpSuPctDegradedSeconds_Type()
)
p2mpSuPctDegradedSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuPctDegradedSeconds.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSuPctDegradedSeconds.setUnits("0.00001 percent")
_P2mpSuInitialSyncSeconds_Type = Counter32
_P2mpSuInitialSyncSeconds_Object = MibTableColumn
p2mpSuInitialSyncSeconds = _P2mpSuInitialSyncSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 9),
    _P2mpSuInitialSyncSeconds_Type()
)
p2mpSuInitialSyncSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuInitialSyncSeconds.setStatus("current")
_P2mpSuSyncSuccessCount_Type = Counter32
_P2mpSuSyncSuccessCount_Object = MibTableColumn
p2mpSuSyncSuccessCount = _P2mpSuSyncSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 10),
    _P2mpSuSyncSuccessCount_Type()
)
p2mpSuSyncSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuSyncSuccessCount.setStatus("current")
_P2mpSuLastSyncSuccessTime_Type = TimeInterval
_P2mpSuLastSyncSuccessTime_Object = MibTableColumn
p2mpSuLastSyncSuccessTime = _P2mpSuLastSyncSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 11),
    _P2mpSuLastSyncSuccessTime_Type()
)
p2mpSuLastSyncSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuLastSyncSuccessTime.setStatus("current")
_P2mpSuSyncFailureCount_Type = Counter32
_P2mpSuSyncFailureCount_Object = MibTableColumn
p2mpSuSyncFailureCount = _P2mpSuSyncFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 12),
    _P2mpSuSyncFailureCount_Type()
)
p2mpSuSyncFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuSyncFailureCount.setStatus("current")
_P2mpSuLastSyncFailTime_Type = TimeInterval
_P2mpSuLastSyncFailTime_Object = MibTableColumn
p2mpSuLastSyncFailTime = _P2mpSuLastSyncFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 13),
    _P2mpSuLastSyncFailTime_Type()
)
p2mpSuLastSyncFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuLastSyncFailTime.setStatus("current")
_P2mpSuSyncMedEffort_Type = Counter32
_P2mpSuSyncMedEffort_Object = MibTableColumn
p2mpSuSyncMedEffort = _P2mpSuSyncMedEffort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 14),
    _P2mpSuSyncMedEffort_Type()
)
p2mpSuSyncMedEffort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuSyncMedEffort.setStatus("current")
_P2mpSuSyncHighEffort_Type = Counter32
_P2mpSuSyncHighEffort_Object = MibTableColumn
p2mpSuSyncHighEffort = _P2mpSuSyncHighEffort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 15),
    _P2mpSuSyncHighEffort_Type()
)
p2mpSuSyncHighEffort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuSyncHighEffort.setStatus("current")
_P2mpSuEffectiveDataRate_Type = Gauge32
_P2mpSuEffectiveDataRate_Object = MibTableColumn
p2mpSuEffectiveDataRate = _P2mpSuEffectiveDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 16),
    _P2mpSuEffectiveDataRate_Type()
)
p2mpSuEffectiveDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuEffectiveDataRate.setStatus("current")
_P2mpSuPercentEfficiency_Type = CwrPercentageValue
_P2mpSuPercentEfficiency_Object = MibTableColumn
p2mpSuPercentEfficiency = _P2mpSuPercentEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 2, 6, 1, 17),
    _P2mpSuPercentEfficiency_Type()
)
p2mpSuPercentEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSuPercentEfficiency.setStatus("current")
if mibBuilder.loadTexts:
    p2mpSuPercentEfficiency.setUnits("0.00001 percent")
_P2mpHeLinkMetricsGroup_ObjectIdentity = ObjectIdentity
p2mpHeLinkMetricsGroup = _P2mpHeLinkMetricsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3)
)
_P2mpHeLinkMetricsThreshTable_Object = MibTable
p2mpHeLinkMetricsThreshTable = _P2mpHeLinkMetricsThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 1)
)
if mibBuilder.loadTexts:
    p2mpHeLinkMetricsThreshTable.setStatus("current")
_P2mpHeLinkMetricsThreshEntry_Object = MibTableRow
p2mpHeLinkMetricsThreshEntry = _P2mpHeLinkMetricsThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 1, 1)
)
p2mpHeLinkMetricsThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    p2mpHeLinkMetricsThreshEntry.setStatus("current")
_P2mpHe1HrMinTotalCWThresh_Type = Unsigned32
_P2mpHe1HrMinTotalCWThresh_Object = MibTableColumn
p2mpHe1HrMinTotalCWThresh = _P2mpHe1HrMinTotalCWThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 1, 1, 1),
    _P2mpHe1HrMinTotalCWThresh_Type()
)
p2mpHe1HrMinTotalCWThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpHe1HrMinTotalCWThresh.setStatus("current")
_P2mpHe1HrPctErrCWThresh_Type = CwrPercentageValue
_P2mpHe1HrPctErrCWThresh_Object = MibTableColumn
p2mpHe1HrPctErrCWThresh = _P2mpHe1HrPctErrCWThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 1, 1, 2),
    _P2mpHe1HrPctErrCWThresh_Type()
)
p2mpHe1HrPctErrCWThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p2mpHe1HrPctErrCWThresh.setStatus("current")
if mibBuilder.loadTexts:
    p2mpHe1HrPctErrCWThresh.setUnits("0.00001 percent")
_P2mpHeBadSuTable_Object = MibTable
p2mpHeBadSuTable = _P2mpHeBadSuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 2)
)
if mibBuilder.loadTexts:
    p2mpHeBadSuTable.setStatus("current")
_P2mpHeBadSuEntry_Object = MibTableRow
p2mpHeBadSuEntry = _P2mpHeBadSuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 2, 1)
)
p2mpHeBadSuEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpBadSuIndex"),
)
if mibBuilder.loadTexts:
    p2mpHeBadSuEntry.setStatus("current")


class _P2mpBadSuIndex_Type(Integer32):
    """Custom type p2mpBadSuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_P2mpBadSuIndex_Type.__name__ = "Integer32"
_P2mpBadSuIndex_Object = MibTableColumn
p2mpBadSuIndex = _P2mpBadSuIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 2, 1, 1),
    _P2mpBadSuIndex_Type()
)
p2mpBadSuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpBadSuIndex.setStatus("current")
_P2mpBadSuUpdateTime_Type = CwrUpdateTime
_P2mpBadSuUpdateTime_Object = MibTableColumn
p2mpBadSuUpdateTime = _P2mpBadSuUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 2, 1, 2),
    _P2mpBadSuUpdateTime_Type()
)
p2mpBadSuUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpBadSuUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    p2mpBadSuUpdateTime.setUnits("seconds")
_P2mpBadSuMacAddress_Type = MacAddress
_P2mpBadSuMacAddress_Object = MibTableColumn
p2mpBadSuMacAddress = _P2mpBadSuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 2, 1, 3),
    _P2mpBadSuMacAddress_Type()
)
p2mpBadSuMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpBadSuMacAddress.setStatus("current")
_P2mpTotalErroredCodewords_Type = Unsigned32
_P2mpTotalErroredCodewords_Object = MibTableColumn
p2mpTotalErroredCodewords = _P2mpTotalErroredCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 2, 1, 4),
    _P2mpTotalErroredCodewords_Type()
)
p2mpTotalErroredCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpTotalErroredCodewords.setStatus("current")
_P2mpPctErroredCodewords_Type = Unsigned32
_P2mpPctErroredCodewords_Object = MibTableColumn
p2mpPctErroredCodewords = _P2mpPctErroredCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 2, 1, 5),
    _P2mpPctErroredCodewords_Type()
)
p2mpPctErroredCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpPctErroredCodewords.setStatus("current")
_P2mpHeCodewordErrorTable_Object = MibTable
p2mpHeCodewordErrorTable = _P2mpHeCodewordErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 3)
)
if mibBuilder.loadTexts:
    p2mpHeCodewordErrorTable.setStatus("current")
_P2mpHeCodewordErrorEntry_Object = MibTableRow
p2mpHeCodewordErrorEntry = _P2mpHeCodewordErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 3, 1)
)
p2mpHeCodewordErrorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuMacAddress"),
    (0, "CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHeCWErrorIndex"),
)
if mibBuilder.loadTexts:
    p2mpHeCodewordErrorEntry.setStatus("current")
_P2mpSuMacAddress_Type = MacAddress
_P2mpSuMacAddress_Object = MibTableColumn
p2mpSuMacAddress = _P2mpSuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 3, 1, 1),
    _P2mpSuMacAddress_Type()
)
p2mpSuMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpSuMacAddress.setStatus("current")


class _P2mpHeCWErrorIndex_Type(Integer32):
    """Custom type p2mpHeCWErrorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_P2mpHeCWErrorIndex_Type.__name__ = "Integer32"
_P2mpHeCWErrorIndex_Object = MibTableColumn
p2mpHeCWErrorIndex = _P2mpHeCWErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 3, 1, 2),
    _P2mpHeCWErrorIndex_Type()
)
p2mpHeCWErrorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpHeCWErrorIndex.setStatus("current")
_P2mpHeCWErrorUpdateTime_Type = CwrUpdateTime
_P2mpHeCWErrorUpdateTime_Object = MibTableColumn
p2mpHeCWErrorUpdateTime = _P2mpHeCWErrorUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 3, 1, 3),
    _P2mpHeCWErrorUpdateTime_Type()
)
p2mpHeCWErrorUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHeCWErrorUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    p2mpHeCWErrorUpdateTime.setUnits("seconds")
_P2mpTotalCodewords_Type = WirelessGauge64
_P2mpTotalCodewords_Object = MibTableColumn
p2mpTotalCodewords = _P2mpTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 3, 1, 4),
    _P2mpTotalCodewords_Type()
)
p2mpTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpTotalCodewords.setStatus("current")
_P2mpErroredCodewords_Type = WirelessGauge64
_P2mpErroredCodewords_Object = MibTableColumn
p2mpErroredCodewords = _P2mpErroredCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 3, 1, 5),
    _P2mpErroredCodewords_Type()
)
p2mpErroredCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpErroredCodewords.setStatus("current")
_P2mpSINR_Type = CwrFixedPointValue
_P2mpSINR_Object = MibTableColumn
p2mpSINR = _P2mpSINR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 3, 1, 6),
    _P2mpSINR_Type()
)
p2mpSINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSINR.setStatus("current")
_P2mpHe1SecMetricsTable_Object = MibTable
p2mpHe1SecMetricsTable = _P2mpHe1SecMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 4)
)
if mibBuilder.loadTexts:
    p2mpHe1SecMetricsTable.setStatus("current")
_P2mpHe1SecMetricsEntry_Object = MibTableRow
p2mpHe1SecMetricsEntry = _P2mpHe1SecMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 4, 1)
)
p2mpHe1SecMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1SecIndex"),
)
if mibBuilder.loadTexts:
    p2mpHe1SecMetricsEntry.setStatus("current")


class _P2mpHe1SecIndex_Type(Integer32):
    """Custom type p2mpHe1SecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_P2mpHe1SecIndex_Type.__name__ = "Integer32"
_P2mpHe1SecIndex_Object = MibTableColumn
p2mpHe1SecIndex = _P2mpHe1SecIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 4, 1, 1),
    _P2mpHe1SecIndex_Type()
)
p2mpHe1SecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpHe1SecIndex.setStatus("current")
_P2mpHe1SecUpdateTime_Type = CwrUpdateTime
_P2mpHe1SecUpdateTime_Object = MibTableColumn
p2mpHe1SecUpdateTime = _P2mpHe1SecUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 4, 1, 2),
    _P2mpHe1SecUpdateTime_Type()
)
p2mpHe1SecUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHe1SecUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    p2mpHe1SecUpdateTime.setUnits("seconds")
_P2mpHe1SecTotalCodewords_Type = WirelessGauge64
_P2mpHe1SecTotalCodewords_Object = MibTableColumn
p2mpHe1SecTotalCodewords = _P2mpHe1SecTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 4, 1, 3),
    _P2mpHe1SecTotalCodewords_Type()
)
p2mpHe1SecTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHe1SecTotalCodewords.setStatus("current")
_P2mpHe1SecErroredCodewords_Type = WirelessGauge64
_P2mpHe1SecErroredCodewords_Object = MibTableColumn
p2mpHe1SecErroredCodewords = _P2mpHe1SecErroredCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 4, 1, 4),
    _P2mpHe1SecErroredCodewords_Type()
)
p2mpHe1SecErroredCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHe1SecErroredCodewords.setStatus("current")
_P2mpHe1MinMetricsTable_Object = MibTable
p2mpHe1MinMetricsTable = _P2mpHe1MinMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 5)
)
if mibBuilder.loadTexts:
    p2mpHe1MinMetricsTable.setStatus("current")
_P2mpHe1MinMetricsEntry_Object = MibTableRow
p2mpHe1MinMetricsEntry = _P2mpHe1MinMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 5, 1)
)
p2mpHe1MinMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1MinIndex"),
)
if mibBuilder.loadTexts:
    p2mpHe1MinMetricsEntry.setStatus("current")


class _P2mpHe1MinIndex_Type(Integer32):
    """Custom type p2mpHe1MinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_P2mpHe1MinIndex_Type.__name__ = "Integer32"
_P2mpHe1MinIndex_Object = MibTableColumn
p2mpHe1MinIndex = _P2mpHe1MinIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 5, 1, 1),
    _P2mpHe1MinIndex_Type()
)
p2mpHe1MinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpHe1MinIndex.setStatus("current")
_P2mpHe1MinUpdateTime_Type = CwrUpdateTime
_P2mpHe1MinUpdateTime_Object = MibTableColumn
p2mpHe1MinUpdateTime = _P2mpHe1MinUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 5, 1, 2),
    _P2mpHe1MinUpdateTime_Type()
)
p2mpHe1MinUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHe1MinUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    p2mpHe1MinUpdateTime.setUnits("seconds")
_P2mpHe1MinTotalCodewords_Type = WirelessGauge64
_P2mpHe1MinTotalCodewords_Object = MibTableColumn
p2mpHe1MinTotalCodewords = _P2mpHe1MinTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 5, 1, 3),
    _P2mpHe1MinTotalCodewords_Type()
)
p2mpHe1MinTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHe1MinTotalCodewords.setStatus("current")
_P2mpHe1MinErroredCodewords_Type = WirelessGauge64
_P2mpHe1MinErroredCodewords_Object = MibTableColumn
p2mpHe1MinErroredCodewords = _P2mpHe1MinErroredCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 5, 1, 4),
    _P2mpHe1MinErroredCodewords_Type()
)
p2mpHe1MinErroredCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHe1MinErroredCodewords.setStatus("current")
_P2mpHe1HrMetricsTable_Object = MibTable
p2mpHe1HrMetricsTable = _P2mpHe1HrMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 6)
)
if mibBuilder.loadTexts:
    p2mpHe1HrMetricsTable.setStatus("current")
_P2mpHe1HrMetricsEntry_Object = MibTableRow
p2mpHe1HrMetricsEntry = _P2mpHe1HrMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 6, 1)
)
p2mpHe1HrMetricsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1HrIndex"),
)
if mibBuilder.loadTexts:
    p2mpHe1HrMetricsEntry.setStatus("current")


class _P2mpHe1HrIndex_Type(Integer32):
    """Custom type p2mpHe1HrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_P2mpHe1HrIndex_Type.__name__ = "Integer32"
_P2mpHe1HrIndex_Object = MibTableColumn
p2mpHe1HrIndex = _P2mpHe1HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 6, 1, 1),
    _P2mpHe1HrIndex_Type()
)
p2mpHe1HrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpHe1HrIndex.setStatus("current")
_P2mpHe1HrUpdateTime_Type = CwrUpdateTime
_P2mpHe1HrUpdateTime_Object = MibTableColumn
p2mpHe1HrUpdateTime = _P2mpHe1HrUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 6, 1, 2),
    _P2mpHe1HrUpdateTime_Type()
)
p2mpHe1HrUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHe1HrUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    p2mpHe1HrUpdateTime.setUnits("seconds")
_P2mpHe1HrTotalCodewords_Type = WirelessGauge64
_P2mpHe1HrTotalCodewords_Object = MibTableColumn
p2mpHe1HrTotalCodewords = _P2mpHe1HrTotalCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 6, 1, 3),
    _P2mpHe1HrTotalCodewords_Type()
)
p2mpHe1HrTotalCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHe1HrTotalCodewords.setStatus("current")
_P2mpHe1HrErroredCodewords_Type = WirelessGauge64
_P2mpHe1HrErroredCodewords_Object = MibTableColumn
p2mpHe1HrErroredCodewords = _P2mpHe1HrErroredCodewords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 3, 6, 1, 4),
    _P2mpHe1HrErroredCodewords_Type()
)
p2mpHe1HrErroredCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHe1HrErroredCodewords.setStatus("current")
_P2mpRadioLinkConformance_ObjectIdentity = ObjectIdentity
p2mpRadioLinkConformance = _P2mpRadioLinkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 4)
)
_P2mpRadioLinkCompliances_ObjectIdentity = ObjectIdentity
p2mpRadioLinkCompliances = _P2mpRadioLinkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 4, 1)
)
_P2mpRadioLinkGroups_ObjectIdentity = ObjectIdentity
p2mpRadioLinkGroups = _P2mpRadioLinkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 4, 2)
)

# Managed Objects groups

p2mpComplianceLinkMetricsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 4, 2, 1)
)
p2mpComplianceLinkMetricsGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpLinkMetricsScale"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpLinkMetricsPrecision"))
)
if mibBuilder.loadTexts:
    p2mpComplianceLinkMetricsGroup.setStatus("current")

p2mpComplianceSuMetricsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 4, 2, 2)
)
p2mpComplianceSuMetricsGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLinkESThresh"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLinkDSThresh"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLinkSESThresh"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLinkCSESThresh"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLink1HrESAlarmThresh"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLink1HrSESAlarmThresh"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLink1HrCSESAlarmThresh"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLink1HrDCSAlarmThresh"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1SecUpdateTime"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1SecType"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1SecTotalCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1SecTotalErrCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1SecValidDataPkt"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinUpdateTime"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinTotalCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinTotalErrCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinValidDataPkt"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinErrorFreeSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinErroredSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinSevErroredSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinConsecSevErrSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinSyncLossSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinDegradedSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinTxPowerMax"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinTxPowerMin"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinTxPowerAvg"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinMainAntRxPowerMax"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinMainAntRxPowerMin"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinMainAntRxPowerAvg"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinDivAntRxPowerMax"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinDivAntRxPowerMin"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1MinDivAntRxPowerAvg"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrUpdateTime"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrTotalCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrTotalErrCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrValidDataPkt"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrErrorFreeSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrErroredSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrSevErroredSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrConsecSvErrSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrSyncLossSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrDegradedSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrTxPowerMax"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrTxPowerMin"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrTxPowerAvg"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrMainAntRxPowerMax"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrMainAntRxPowerMin"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrMainAntRxPowerAvg"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrDivAntRxPowerMax"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrDivAntRxPowerMin"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSu1HrDivAntRxPowerAvg"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuAvailableSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuUnAvailableSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuPctAvailSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuSyncLossSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuPctErrorFreeSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuPctErroredSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuPctSevErroredSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuPctDegradedSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuInitialSyncSeconds"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuSyncSuccessCount"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLastSyncSuccessTime"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuSyncMedEffort"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuSyncHighEffort"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuSyncFailureCount"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLastSyncFailTime"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuEffectiveDataRate"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuPercentEfficiency"))
)
if mibBuilder.loadTexts:
    p2mpComplianceSuMetricsGroup.setStatus("current")

p2mpComplianceHeMetricsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 4, 2, 3)
)
p2mpComplianceHeMetricsGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1HrMinTotalCWThresh"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1HrPctErrCWThresh"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpBadSuUpdateTime"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpBadSuMacAddress"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpTotalErroredCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpPctErroredCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHeCWErrorUpdateTime"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpTotalCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpErroredCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSINR"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1SecUpdateTime"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1SecTotalCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1SecErroredCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1MinUpdateTime"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1MinTotalCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1MinErroredCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1HrUpdateTime"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1HrTotalCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1HrErroredCodewords"))
)
if mibBuilder.loadTexts:
    p2mpComplianceHeMetricsGroup.setStatus("current")


# Notification objects

p2mpHeChPctErrCWThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1, 2, 0, 1)
)
p2mpHeChPctErrCWThreshTrap.setObjects(
    ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHe1HrPctErrCWThresh")
)
if mibBuilder.loadTexts:
    p2mpHeChPctErrCWThreshTrap.setStatus(
        "current"
    )

p2mpHeMacPctErrCWThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1, 2, 0, 2)
)
p2mpHeMacPctErrCWThreshTrap.setObjects(
      *(("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpBadSuMacAddress"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpTotalErroredCodewords"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpPctErroredCodewords"))
)
if mibBuilder.loadTexts:
    p2mpHeMacPctErrCWThreshTrap.setStatus(
        "current"
    )

p2mpSuErrSecAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1, 2, 0, 3)
)
p2mpSuErrSecAlarmTrap.setObjects(
    ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLink1HrESAlarmThresh")
)
if mibBuilder.loadTexts:
    p2mpSuErrSecAlarmTrap.setStatus(
        "current"
    )

p2mpSuSevErrSecAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1, 2, 0, 4)
)
p2mpSuSevErrSecAlarmTrap.setObjects(
    ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLink1HrSESAlarmThresh")
)
if mibBuilder.loadTexts:
    p2mpSuSevErrSecAlarmTrap.setStatus(
        "current"
    )

p2mpSuConsecSevErrSecAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1, 2, 0, 5)
)
p2mpSuConsecSevErrSecAlarmTrap.setObjects(
    ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLink1HrCSESAlarmThresh")
)
if mibBuilder.loadTexts:
    p2mpSuConsecSevErrSecAlarmTrap.setStatus(
        "current"
    )

p2mpSuDegradedSecAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 1, 2, 0, 6)
)
p2mpSuDegradedSecAlarmTrap.setObjects(
    ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuLink1HrDCSAlarmThresh")
)
if mibBuilder.loadTexts:
    p2mpSuDegradedSecAlarmTrap.setStatus(
        "current"
    )


# Notifications groups

p2mpComplianceNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 4, 2, 4)
)
p2mpComplianceNotifGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHeChPctErrCWThreshTrap"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpHeMacPctErrCWThreshTrap"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuErrSecAlarmTrap"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuSevErrSecAlarmTrap"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuConsecSevErrSecAlarmTrap"),
        ("CISCO-WIRELESS-P2MP-LINK-METRICS-MIB", "p2mpSuDegradedSecAlarmTrap"))
)
if mibBuilder.loadTexts:
    p2mpComplianceNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

p2mpRadioLinkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 181, 4, 1, 1)
)
if mibBuilder.loadTexts:
    p2mpRadioLinkCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WIRELESS-P2MP-LINK-METRICS-MIB",
    **{"ciscoWirelessLinkMetricsMIB": ciscoWirelessLinkMetricsMIB,
       "p2mpLinkMetricsGroup": p2mpLinkMetricsGroup,
       "p2mpMetricsPrecisionTable": p2mpMetricsPrecisionTable,
       "p2mpMetricsPrecisionEntry": p2mpMetricsPrecisionEntry,
       "p2mpLinkMetricsScale": p2mpLinkMetricsScale,
       "p2mpLinkMetricsPrecision": p2mpLinkMetricsPrecision,
       "p2mpMetricsMIBNotificationPrefix": p2mpMetricsMIBNotificationPrefix,
       "p2mpMetricsMIBNotification": p2mpMetricsMIBNotification,
       "p2mpHeChPctErrCWThreshTrap": p2mpHeChPctErrCWThreshTrap,
       "p2mpHeMacPctErrCWThreshTrap": p2mpHeMacPctErrCWThreshTrap,
       "p2mpSuErrSecAlarmTrap": p2mpSuErrSecAlarmTrap,
       "p2mpSuSevErrSecAlarmTrap": p2mpSuSevErrSecAlarmTrap,
       "p2mpSuConsecSevErrSecAlarmTrap": p2mpSuConsecSevErrSecAlarmTrap,
       "p2mpSuDegradedSecAlarmTrap": p2mpSuDegradedSecAlarmTrap,
       "p2mpSuLinkMetricsGroup": p2mpSuLinkMetricsGroup,
       "p2mpSuLinkMetricsThreshTable": p2mpSuLinkMetricsThreshTable,
       "p2mpSuLinkMetricsThreshEntry": p2mpSuLinkMetricsThreshEntry,
       "p2mpSuLinkESThresh": p2mpSuLinkESThresh,
       "p2mpSuLinkDSThresh": p2mpSuLinkDSThresh,
       "p2mpSuLinkSESThresh": p2mpSuLinkSESThresh,
       "p2mpSuLinkCSESThresh": p2mpSuLinkCSESThresh,
       "p2mpSuLink1HrESAlarmThresh": p2mpSuLink1HrESAlarmThresh,
       "p2mpSuLink1HrSESAlarmThresh": p2mpSuLink1HrSESAlarmThresh,
       "p2mpSuLink1HrCSESAlarmThresh": p2mpSuLink1HrCSESAlarmThresh,
       "p2mpSuLink1HrDCSAlarmThresh": p2mpSuLink1HrDCSAlarmThresh,
       "p2mpSu1SecMetricsTable": p2mpSu1SecMetricsTable,
       "p2mpSu1SecMetricsEntry": p2mpSu1SecMetricsEntry,
       "p2mpSu1SecIndex": p2mpSu1SecIndex,
       "p2mpSu1SecUpdateTime": p2mpSu1SecUpdateTime,
       "p2mpSu1SecType": p2mpSu1SecType,
       "p2mpSu1SecTotalCodewords": p2mpSu1SecTotalCodewords,
       "p2mpSu1SecTotalErrCodewords": p2mpSu1SecTotalErrCodewords,
       "p2mpSu1SecValidDataPkt": p2mpSu1SecValidDataPkt,
       "p2mpSu1MinMetricsTable": p2mpSu1MinMetricsTable,
       "p2mpSu1MinMetricsEntry": p2mpSu1MinMetricsEntry,
       "p2mpSu1MinIndex": p2mpSu1MinIndex,
       "p2mpSu1MinUpdateTime": p2mpSu1MinUpdateTime,
       "p2mpSu1MinTotalCodewords": p2mpSu1MinTotalCodewords,
       "p2mpSu1MinTotalErrCodewords": p2mpSu1MinTotalErrCodewords,
       "p2mpSu1MinValidDataPkt": p2mpSu1MinValidDataPkt,
       "p2mpSu1MinErrorFreeSeconds": p2mpSu1MinErrorFreeSeconds,
       "p2mpSu1MinErroredSeconds": p2mpSu1MinErroredSeconds,
       "p2mpSu1MinDegradedSeconds": p2mpSu1MinDegradedSeconds,
       "p2mpSu1MinSevErroredSeconds": p2mpSu1MinSevErroredSeconds,
       "p2mpSu1MinConsecSevErrSeconds": p2mpSu1MinConsecSevErrSeconds,
       "p2mpSu1MinSyncLossSeconds": p2mpSu1MinSyncLossSeconds,
       "p2mpSu1MinTxPowerMax": p2mpSu1MinTxPowerMax,
       "p2mpSu1MinTxPowerMin": p2mpSu1MinTxPowerMin,
       "p2mpSu1MinTxPowerAvg": p2mpSu1MinTxPowerAvg,
       "p2mpSu1MinMainAntRxPowerMax": p2mpSu1MinMainAntRxPowerMax,
       "p2mpSu1MinMainAntRxPowerMin": p2mpSu1MinMainAntRxPowerMin,
       "p2mpSu1MinMainAntRxPowerAvg": p2mpSu1MinMainAntRxPowerAvg,
       "p2mpSu1MinDivAntRxPowerMax": p2mpSu1MinDivAntRxPowerMax,
       "p2mpSu1MinDivAntRxPowerMin": p2mpSu1MinDivAntRxPowerMin,
       "p2mpSu1MinDivAntRxPowerAvg": p2mpSu1MinDivAntRxPowerAvg,
       "p2mpSu1HrMetricsTable": p2mpSu1HrMetricsTable,
       "p2mpSu1HrMetricsEntry": p2mpSu1HrMetricsEntry,
       "p2mpSu1HrIndex": p2mpSu1HrIndex,
       "p2mpSu1HrUpdateTime": p2mpSu1HrUpdateTime,
       "p2mpSu1HrTotalCodewords": p2mpSu1HrTotalCodewords,
       "p2mpSu1HrTotalErrCodewords": p2mpSu1HrTotalErrCodewords,
       "p2mpSu1HrValidDataPkt": p2mpSu1HrValidDataPkt,
       "p2mpSu1HrErrorFreeSeconds": p2mpSu1HrErrorFreeSeconds,
       "p2mpSu1HrErroredSeconds": p2mpSu1HrErroredSeconds,
       "p2mpSu1HrSevErroredSeconds": p2mpSu1HrSevErroredSeconds,
       "p2mpSu1HrConsecSvErrSeconds": p2mpSu1HrConsecSvErrSeconds,
       "p2mpSu1HrSyncLossSeconds": p2mpSu1HrSyncLossSeconds,
       "p2mpSu1HrDegradedSeconds": p2mpSu1HrDegradedSeconds,
       "p2mpSu1HrTxPowerMax": p2mpSu1HrTxPowerMax,
       "p2mpSu1HrTxPowerMin": p2mpSu1HrTxPowerMin,
       "p2mpSu1HrTxPowerAvg": p2mpSu1HrTxPowerAvg,
       "p2mpSu1HrMainAntRxPowerMax": p2mpSu1HrMainAntRxPowerMax,
       "p2mpSu1HrMainAntRxPowerMin": p2mpSu1HrMainAntRxPowerMin,
       "p2mpSu1HrMainAntRxPowerAvg": p2mpSu1HrMainAntRxPowerAvg,
       "p2mpSu1HrDivAntRxPowerMax": p2mpSu1HrDivAntRxPowerMax,
       "p2mpSu1HrDivAntRxPowerMin": p2mpSu1HrDivAntRxPowerMin,
       "p2mpSu1HrDivAntRxPowerAvg": p2mpSu1HrDivAntRxPowerAvg,
       "p2mpSuCumulativeLinkMetricsTable": p2mpSuCumulativeLinkMetricsTable,
       "p2mpSuCumulativeLinkMetricsEntry": p2mpSuCumulativeLinkMetricsEntry,
       "p2mpSuAvailableSeconds": p2mpSuAvailableSeconds,
       "p2mpSuUnAvailableSeconds": p2mpSuUnAvailableSeconds,
       "p2mpSuPctAvailSeconds": p2mpSuPctAvailSeconds,
       "p2mpSuSyncLossSeconds": p2mpSuSyncLossSeconds,
       "p2mpSuPctErrorFreeSeconds": p2mpSuPctErrorFreeSeconds,
       "p2mpSuPctErroredSeconds": p2mpSuPctErroredSeconds,
       "p2mpSuPctSevErroredSeconds": p2mpSuPctSevErroredSeconds,
       "p2mpSuPctDegradedSeconds": p2mpSuPctDegradedSeconds,
       "p2mpSuInitialSyncSeconds": p2mpSuInitialSyncSeconds,
       "p2mpSuSyncSuccessCount": p2mpSuSyncSuccessCount,
       "p2mpSuLastSyncSuccessTime": p2mpSuLastSyncSuccessTime,
       "p2mpSuSyncFailureCount": p2mpSuSyncFailureCount,
       "p2mpSuLastSyncFailTime": p2mpSuLastSyncFailTime,
       "p2mpSuSyncMedEffort": p2mpSuSyncMedEffort,
       "p2mpSuSyncHighEffort": p2mpSuSyncHighEffort,
       "p2mpSuEffectiveDataRate": p2mpSuEffectiveDataRate,
       "p2mpSuPercentEfficiency": p2mpSuPercentEfficiency,
       "p2mpHeLinkMetricsGroup": p2mpHeLinkMetricsGroup,
       "p2mpHeLinkMetricsThreshTable": p2mpHeLinkMetricsThreshTable,
       "p2mpHeLinkMetricsThreshEntry": p2mpHeLinkMetricsThreshEntry,
       "p2mpHe1HrMinTotalCWThresh": p2mpHe1HrMinTotalCWThresh,
       "p2mpHe1HrPctErrCWThresh": p2mpHe1HrPctErrCWThresh,
       "p2mpHeBadSuTable": p2mpHeBadSuTable,
       "p2mpHeBadSuEntry": p2mpHeBadSuEntry,
       "p2mpBadSuIndex": p2mpBadSuIndex,
       "p2mpBadSuUpdateTime": p2mpBadSuUpdateTime,
       "p2mpBadSuMacAddress": p2mpBadSuMacAddress,
       "p2mpTotalErroredCodewords": p2mpTotalErroredCodewords,
       "p2mpPctErroredCodewords": p2mpPctErroredCodewords,
       "p2mpHeCodewordErrorTable": p2mpHeCodewordErrorTable,
       "p2mpHeCodewordErrorEntry": p2mpHeCodewordErrorEntry,
       "p2mpSuMacAddress": p2mpSuMacAddress,
       "p2mpHeCWErrorIndex": p2mpHeCWErrorIndex,
       "p2mpHeCWErrorUpdateTime": p2mpHeCWErrorUpdateTime,
       "p2mpTotalCodewords": p2mpTotalCodewords,
       "p2mpErroredCodewords": p2mpErroredCodewords,
       "p2mpSINR": p2mpSINR,
       "p2mpHe1SecMetricsTable": p2mpHe1SecMetricsTable,
       "p2mpHe1SecMetricsEntry": p2mpHe1SecMetricsEntry,
       "p2mpHe1SecIndex": p2mpHe1SecIndex,
       "p2mpHe1SecUpdateTime": p2mpHe1SecUpdateTime,
       "p2mpHe1SecTotalCodewords": p2mpHe1SecTotalCodewords,
       "p2mpHe1SecErroredCodewords": p2mpHe1SecErroredCodewords,
       "p2mpHe1MinMetricsTable": p2mpHe1MinMetricsTable,
       "p2mpHe1MinMetricsEntry": p2mpHe1MinMetricsEntry,
       "p2mpHe1MinIndex": p2mpHe1MinIndex,
       "p2mpHe1MinUpdateTime": p2mpHe1MinUpdateTime,
       "p2mpHe1MinTotalCodewords": p2mpHe1MinTotalCodewords,
       "p2mpHe1MinErroredCodewords": p2mpHe1MinErroredCodewords,
       "p2mpHe1HrMetricsTable": p2mpHe1HrMetricsTable,
       "p2mpHe1HrMetricsEntry": p2mpHe1HrMetricsEntry,
       "p2mpHe1HrIndex": p2mpHe1HrIndex,
       "p2mpHe1HrUpdateTime": p2mpHe1HrUpdateTime,
       "p2mpHe1HrTotalCodewords": p2mpHe1HrTotalCodewords,
       "p2mpHe1HrErroredCodewords": p2mpHe1HrErroredCodewords,
       "p2mpRadioLinkConformance": p2mpRadioLinkConformance,
       "p2mpRadioLinkCompliances": p2mpRadioLinkCompliances,
       "p2mpRadioLinkCompliance": p2mpRadioLinkCompliance,
       "p2mpRadioLinkGroups": p2mpRadioLinkGroups,
       "p2mpComplianceLinkMetricsGroup": p2mpComplianceLinkMetricsGroup,
       "p2mpComplianceSuMetricsGroup": p2mpComplianceSuMetricsGroup,
       "p2mpComplianceHeMetricsGroup": p2mpComplianceHeMetricsGroup,
       "p2mpComplianceNotifGroup": p2mpComplianceNotifGroup}
)
