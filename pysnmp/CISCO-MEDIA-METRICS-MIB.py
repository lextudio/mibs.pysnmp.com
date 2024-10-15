# SNMP MIB module (CISCO-MEDIA-METRICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MEDIA-METRICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:19 2024
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

(cfmFlowId,
 cfmFlowMetricsIntNumber,
 cfmFlowMonitorId) = mibBuilder.importSymbols(
    "CISCO-FLOW-MONITOR-MIB",
    "cfmFlowId",
    "cfmFlowMetricsIntNumber",
    "cfmFlowMonitorId")

(FlowBitRateUnits,) = mibBuilder.importSymbols(
    "CISCO-FLOW-MONITOR-TC-MIB",
    "FlowBitRateUnits")

(ReportIntervalCount,) = mibBuilder.importSymbols(
    "CISCO-REPORT-INTERVAL-TC-MIB",
    "ReportIntervalCount")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoMediaMetricsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 771)
)
ciscoMediaMetricsMIB.setRevisions(
        ("2011-03-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoMediaMetricsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMediaMetricsMIBNotifs = _CiscoMediaMetricsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 0)
)
_CiscoMediaMetricsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMediaMetricsMIBObjects = _CiscoMediaMetricsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1)
)
_CfmMediaMetrics_ObjectIdentity = ObjectIdentity
cfmMediaMetrics = _CfmMediaMetrics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1)
)
_CfmMediaMetricsTable_Object = MibTable
cfmMediaMetricsTable = _CfmMediaMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfmMediaMetricsTable.setStatus("current")
_CfmMediaMetricsEntry_Object = MibTableRow
cfmMediaMetricsEntry = _CfmMediaMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1)
)
cfmMediaMetricsEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
)
if mibBuilder.loadTexts:
    cfmMediaMetricsEntry.setStatus("current")


class _CfmMediaMetricsValid_Type(Bits):
    """Custom type cfmMediaMetricsValid based on Bits"""
    namedValues = NamedValues(
        *(("bitRate", 2),
          ("octets", 1),
          ("pktRate", 3),
          ("pkts", 0),
          ("streamBitRate", 4),
          ("streamBitRateMax", 5),
          ("streamBitRateMin", 6))
    )

_CfmMediaMetricsValid_Type.__name__ = "Bits"
_CfmMediaMetricsValid_Object = MibTableColumn
cfmMediaMetricsValid = _CfmMediaMetricsValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1, 1),
    _CfmMediaMetricsValid_Type()
)
cfmMediaMetricsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsValid.setStatus("current")
_CfmMediaMetricsPkts_Type = Counter64
_CfmMediaMetricsPkts_Object = MibTableColumn
cfmMediaMetricsPkts = _CfmMediaMetricsPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1, 2),
    _CfmMediaMetricsPkts_Type()
)
cfmMediaMetricsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfmMediaMetricsPkts.setUnits("packets")
_CfmMediaMetricsOctets_Type = Counter64
_CfmMediaMetricsOctets_Object = MibTableColumn
cfmMediaMetricsOctets = _CfmMediaMetricsOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1, 3),
    _CfmMediaMetricsOctets_Type()
)
cfmMediaMetricsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsOctets.setStatus("current")
if mibBuilder.loadTexts:
    cfmMediaMetricsOctets.setUnits("octets")
_CfmMediaMetricsBitRateUnits_Type = FlowBitRateUnits
_CfmMediaMetricsBitRateUnits_Object = MibTableColumn
cfmMediaMetricsBitRateUnits = _CfmMediaMetricsBitRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1, 4),
    _CfmMediaMetricsBitRateUnits_Type()
)
cfmMediaMetricsBitRateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsBitRateUnits.setStatus("current")
_CfmMediaMetricsBitRate_Type = Gauge32
_CfmMediaMetricsBitRate_Object = MibTableColumn
cfmMediaMetricsBitRate = _CfmMediaMetricsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1, 5),
    _CfmMediaMetricsBitRate_Type()
)
cfmMediaMetricsBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsBitRate.setStatus("current")
_CfmMediaMetricsPktRate_Type = Gauge32
_CfmMediaMetricsPktRate_Object = MibTableColumn
cfmMediaMetricsPktRate = _CfmMediaMetricsPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1, 6),
    _CfmMediaMetricsPktRate_Type()
)
cfmMediaMetricsPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cfmMediaMetricsPktRate.setUnits("packets per second")
_CfmMediaMetricsStreamBitRateUnits_Type = FlowBitRateUnits
_CfmMediaMetricsStreamBitRateUnits_Object = MibTableColumn
cfmMediaMetricsStreamBitRateUnits = _CfmMediaMetricsStreamBitRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1, 7),
    _CfmMediaMetricsStreamBitRateUnits_Type()
)
cfmMediaMetricsStreamBitRateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsStreamBitRateUnits.setStatus("current")
_CfmMediaMetricsStreamBitRate_Type = Gauge32
_CfmMediaMetricsStreamBitRate_Object = MibTableColumn
cfmMediaMetricsStreamBitRate = _CfmMediaMetricsStreamBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1, 8),
    _CfmMediaMetricsStreamBitRate_Type()
)
cfmMediaMetricsStreamBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsStreamBitRate.setStatus("current")
_CfmMediaMetricsStreamBitRateMaxUnits_Type = FlowBitRateUnits
_CfmMediaMetricsStreamBitRateMaxUnits_Object = MibTableColumn
cfmMediaMetricsStreamBitRateMaxUnits = _CfmMediaMetricsStreamBitRateMaxUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1, 9),
    _CfmMediaMetricsStreamBitRateMaxUnits_Type()
)
cfmMediaMetricsStreamBitRateMaxUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsStreamBitRateMaxUnits.setStatus("current")
_CfmMediaMetricsStreamBitRateMax_Type = Gauge32
_CfmMediaMetricsStreamBitRateMax_Object = MibTableColumn
cfmMediaMetricsStreamBitRateMax = _CfmMediaMetricsStreamBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1, 10),
    _CfmMediaMetricsStreamBitRateMax_Type()
)
cfmMediaMetricsStreamBitRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsStreamBitRateMax.setStatus("current")
_CfmMediaMetricsStreamBitRateMinUnits_Type = FlowBitRateUnits
_CfmMediaMetricsStreamBitRateMinUnits_Object = MibTableColumn
cfmMediaMetricsStreamBitRateMinUnits = _CfmMediaMetricsStreamBitRateMinUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1, 11),
    _CfmMediaMetricsStreamBitRateMinUnits_Type()
)
cfmMediaMetricsStreamBitRateMinUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsStreamBitRateMinUnits.setStatus("current")
_CfmMediaMetricsStreamBitRateMin_Type = Gauge32
_CfmMediaMetricsStreamBitRateMin_Object = MibTableColumn
cfmMediaMetricsStreamBitRateMin = _CfmMediaMetricsStreamBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 1, 1, 12),
    _CfmMediaMetricsStreamBitRateMin_Type()
)
cfmMediaMetricsStreamBitRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsStreamBitRateMin.setStatus("current")
_CfmMediaMetricsTableChanged_Type = TimeStamp
_CfmMediaMetricsTableChanged_Object = MibScalar
cfmMediaMetricsTableChanged = _CfmMediaMetricsTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 2),
    _CfmMediaMetricsTableChanged_Type()
)
cfmMediaMetricsTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsTableChanged.setStatus("current")
_CfmMediaMetricsIntTable_Object = MibTable
cfmMediaMetricsIntTable = _CfmMediaMetricsIntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfmMediaMetricsIntTable.setStatus("current")
_CfmMediaMetricsIntEntry_Object = MibTableRow
cfmMediaMetricsIntEntry = _CfmMediaMetricsIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1)
)
cfmMediaMetricsIntEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntNumber"),
)
if mibBuilder.loadTexts:
    cfmMediaMetricsIntEntry.setStatus("current")


class _CfmMediaMetricsIntValid_Type(Bits):
    """Custom type cfmMediaMetricsIntValid based on Bits"""
    namedValues = NamedValues(
        *(("bitRate", 2),
          ("octets", 1),
          ("pktRate", 3),
          ("pkts", 0),
          ("streamBitRate", 4),
          ("streamBitRateMax", 5),
          ("streamBitRateMin", 6))
    )

_CfmMediaMetricsIntValid_Type.__name__ = "Bits"
_CfmMediaMetricsIntValid_Object = MibTableColumn
cfmMediaMetricsIntValid = _CfmMediaMetricsIntValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1, 1),
    _CfmMediaMetricsIntValid_Type()
)
cfmMediaMetricsIntValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntValid.setStatus("current")
_CfmMediaMetricsIntPkts_Type = ReportIntervalCount
_CfmMediaMetricsIntPkts_Object = MibTableColumn
cfmMediaMetricsIntPkts = _CfmMediaMetricsIntPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1, 2),
    _CfmMediaMetricsIntPkts_Type()
)
cfmMediaMetricsIntPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntPkts.setUnits("packets")
_CfmMediaMetricsIntOctets_Type = ReportIntervalCount
_CfmMediaMetricsIntOctets_Object = MibTableColumn
cfmMediaMetricsIntOctets = _CfmMediaMetricsIntOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1, 3),
    _CfmMediaMetricsIntOctets_Type()
)
cfmMediaMetricsIntOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntOctets.setStatus("current")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntOctets.setUnits("octets")
_CfmMediaMetricsIntBitRateUnits_Type = FlowBitRateUnits
_CfmMediaMetricsIntBitRateUnits_Object = MibTableColumn
cfmMediaMetricsIntBitRateUnits = _CfmMediaMetricsIntBitRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1, 4),
    _CfmMediaMetricsIntBitRateUnits_Type()
)
cfmMediaMetricsIntBitRateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntBitRateUnits.setStatus("current")
_CfmMediaMetricsIntBitRate_Type = ReportIntervalCount
_CfmMediaMetricsIntBitRate_Object = MibTableColumn
cfmMediaMetricsIntBitRate = _CfmMediaMetricsIntBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1, 5),
    _CfmMediaMetricsIntBitRate_Type()
)
cfmMediaMetricsIntBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntBitRate.setStatus("current")
_CfmMediaMetricsIntPktRate_Type = ReportIntervalCount
_CfmMediaMetricsIntPktRate_Object = MibTableColumn
cfmMediaMetricsIntPktRate = _CfmMediaMetricsIntPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1, 6),
    _CfmMediaMetricsIntPktRate_Type()
)
cfmMediaMetricsIntPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntPktRate.setUnits("packets per second")
_CfmMediaMetricsIntStreamBitRateUnits_Type = FlowBitRateUnits
_CfmMediaMetricsIntStreamBitRateUnits_Object = MibTableColumn
cfmMediaMetricsIntStreamBitRateUnits = _CfmMediaMetricsIntStreamBitRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1, 7),
    _CfmMediaMetricsIntStreamBitRateUnits_Type()
)
cfmMediaMetricsIntStreamBitRateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntStreamBitRateUnits.setStatus("current")
_CfmMediaMetricsIntStreamBitRate_Type = ReportIntervalCount
_CfmMediaMetricsIntStreamBitRate_Object = MibTableColumn
cfmMediaMetricsIntStreamBitRate = _CfmMediaMetricsIntStreamBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1, 8),
    _CfmMediaMetricsIntStreamBitRate_Type()
)
cfmMediaMetricsIntStreamBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntStreamBitRate.setStatus("current")
_CfmMediaMetricsIntStreamBitRateMaxUnits_Type = FlowBitRateUnits
_CfmMediaMetricsIntStreamBitRateMaxUnits_Object = MibTableColumn
cfmMediaMetricsIntStreamBitRateMaxUnits = _CfmMediaMetricsIntStreamBitRateMaxUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1, 9),
    _CfmMediaMetricsIntStreamBitRateMaxUnits_Type()
)
cfmMediaMetricsIntStreamBitRateMaxUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntStreamBitRateMaxUnits.setStatus("current")
_CfmMediaMetricsIntStreamBitRateMax_Type = Gauge32
_CfmMediaMetricsIntStreamBitRateMax_Object = MibTableColumn
cfmMediaMetricsIntStreamBitRateMax = _CfmMediaMetricsIntStreamBitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1, 10),
    _CfmMediaMetricsIntStreamBitRateMax_Type()
)
cfmMediaMetricsIntStreamBitRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntStreamBitRateMax.setStatus("current")
_CfmMediaMetricsIntStreamBitRateMinUnits_Type = FlowBitRateUnits
_CfmMediaMetricsIntStreamBitRateMinUnits_Object = MibTableColumn
cfmMediaMetricsIntStreamBitRateMinUnits = _CfmMediaMetricsIntStreamBitRateMinUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1, 11),
    _CfmMediaMetricsIntStreamBitRateMinUnits_Type()
)
cfmMediaMetricsIntStreamBitRateMinUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntStreamBitRateMinUnits.setStatus("current")
_CfmMediaMetricsIntStreamBitRateMin_Type = Gauge32
_CfmMediaMetricsIntStreamBitRateMin_Object = MibTableColumn
cfmMediaMetricsIntStreamBitRateMin = _CfmMediaMetricsIntStreamBitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 1, 1, 3, 1, 12),
    _CfmMediaMetricsIntStreamBitRateMin_Type()
)
cfmMediaMetricsIntStreamBitRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMediaMetricsIntStreamBitRateMin.setStatus("current")
_CiscoMediaMetricsMIBConform_ObjectIdentity = ObjectIdentity
ciscoMediaMetricsMIBConform = _CiscoMediaMetricsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 2)
)
_CiscoMediaMetricsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMediaMetricsMIBCompliances = _CiscoMediaMetricsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 2, 1)
)
_CiscoMediaMetricsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMediaMetricsMIBGroups = _CiscoMediaMetricsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 2, 2)
)
_CiscoMediaMetricsMIBIds_ObjectIdentity = ObjectIdentity
ciscoMediaMetricsMIBIds = _CiscoMediaMetricsMIBIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 3)
)

# Managed Objects groups

ciscoMediaMetricsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 2, 2, 1)
)
ciscoMediaMetricsGroup.setObjects(
      *(("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsValid"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsPkts"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsOctets"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsBitRateUnits"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsBitRate"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsPktRate"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsStreamBitRateUnits"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsStreamBitRate"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsStreamBitRateMaxUnits"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsStreamBitRateMax"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsStreamBitRateMinUnits"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsStreamBitRateMin"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsTableChanged"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsIntValid"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsIntPkts"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsIntOctets"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsIntBitRateUnits"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsIntBitRate"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsIntPktRate"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsIntStreamBitRateUnits"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsIntStreamBitRate"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsIntStreamBitRateMaxUnits"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsIntStreamBitRateMax"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsIntStreamBitRateMinUnits"),
        ("CISCO-MEDIA-METRICS-MIB", "cfmMediaMetricsIntStreamBitRateMin"))
)
if mibBuilder.loadTexts:
    ciscoMediaMetricsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoMediaMetricsMIBCompliance01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 771, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMediaMetricsMIBCompliance01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MEDIA-METRICS-MIB",
    **{"ciscoMediaMetricsMIB": ciscoMediaMetricsMIB,
       "ciscoMediaMetricsMIBNotifs": ciscoMediaMetricsMIBNotifs,
       "ciscoMediaMetricsMIBObjects": ciscoMediaMetricsMIBObjects,
       "cfmMediaMetrics": cfmMediaMetrics,
       "cfmMediaMetricsTable": cfmMediaMetricsTable,
       "cfmMediaMetricsEntry": cfmMediaMetricsEntry,
       "cfmMediaMetricsValid": cfmMediaMetricsValid,
       "cfmMediaMetricsPkts": cfmMediaMetricsPkts,
       "cfmMediaMetricsOctets": cfmMediaMetricsOctets,
       "cfmMediaMetricsBitRateUnits": cfmMediaMetricsBitRateUnits,
       "cfmMediaMetricsBitRate": cfmMediaMetricsBitRate,
       "cfmMediaMetricsPktRate": cfmMediaMetricsPktRate,
       "cfmMediaMetricsStreamBitRateUnits": cfmMediaMetricsStreamBitRateUnits,
       "cfmMediaMetricsStreamBitRate": cfmMediaMetricsStreamBitRate,
       "cfmMediaMetricsStreamBitRateMaxUnits": cfmMediaMetricsStreamBitRateMaxUnits,
       "cfmMediaMetricsStreamBitRateMax": cfmMediaMetricsStreamBitRateMax,
       "cfmMediaMetricsStreamBitRateMinUnits": cfmMediaMetricsStreamBitRateMinUnits,
       "cfmMediaMetricsStreamBitRateMin": cfmMediaMetricsStreamBitRateMin,
       "cfmMediaMetricsTableChanged": cfmMediaMetricsTableChanged,
       "cfmMediaMetricsIntTable": cfmMediaMetricsIntTable,
       "cfmMediaMetricsIntEntry": cfmMediaMetricsIntEntry,
       "cfmMediaMetricsIntValid": cfmMediaMetricsIntValid,
       "cfmMediaMetricsIntPkts": cfmMediaMetricsIntPkts,
       "cfmMediaMetricsIntOctets": cfmMediaMetricsIntOctets,
       "cfmMediaMetricsIntBitRateUnits": cfmMediaMetricsIntBitRateUnits,
       "cfmMediaMetricsIntBitRate": cfmMediaMetricsIntBitRate,
       "cfmMediaMetricsIntPktRate": cfmMediaMetricsIntPktRate,
       "cfmMediaMetricsIntStreamBitRateUnits": cfmMediaMetricsIntStreamBitRateUnits,
       "cfmMediaMetricsIntStreamBitRate": cfmMediaMetricsIntStreamBitRate,
       "cfmMediaMetricsIntStreamBitRateMaxUnits": cfmMediaMetricsIntStreamBitRateMaxUnits,
       "cfmMediaMetricsIntStreamBitRateMax": cfmMediaMetricsIntStreamBitRateMax,
       "cfmMediaMetricsIntStreamBitRateMinUnits": cfmMediaMetricsIntStreamBitRateMinUnits,
       "cfmMediaMetricsIntStreamBitRateMin": cfmMediaMetricsIntStreamBitRateMin,
       "ciscoMediaMetricsMIBConform": ciscoMediaMetricsMIBConform,
       "ciscoMediaMetricsMIBCompliances": ciscoMediaMetricsMIBCompliances,
       "ciscoMediaMetricsMIBCompliance01": ciscoMediaMetricsMIBCompliance01,
       "ciscoMediaMetricsMIBGroups": ciscoMediaMetricsMIBGroups,
       "ciscoMediaMetricsGroup": ciscoMediaMetricsGroup,
       "ciscoMediaMetricsMIBIds": ciscoMediaMetricsMIBIds}
)
