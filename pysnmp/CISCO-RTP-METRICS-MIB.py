# SNMP MIB module (CISCO-RTP-METRICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RTP-METRICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:45 2024
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

(FlowMetricPrecision,
 FlowMetricScale,
 FlowMetricValue) = mibBuilder.importSymbols(
    "CISCO-FLOW-MONITOR-TC-MIB",
    "FlowMetricPrecision",
    "FlowMetricScale",
    "FlowMetricValue")

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

ciscoRtpMetricsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703)
)
ciscoRtpMetricsMIB.setRevisions(
        ("2009-06-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoRtpMetricsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoRtpMetricsMIBNotifs = _CiscoRtpMetricsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 0)
)
_CiscoRtpMetricsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoRtpMetricsMIBObjects = _CiscoRtpMetricsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1)
)
_CfmRtpMetrics_ObjectIdentity = ObjectIdentity
cfmRtpMetrics = _CfmRtpMetrics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1)
)
_CfmRtpMetricsTable_Object = MibTable
cfmRtpMetricsTable = _CfmRtpMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfmRtpMetricsTable.setStatus("current")
_CfmRtpMetricsEntry_Object = MibTableRow
cfmRtpMetricsEntry = _CfmRtpMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1)
)
cfmRtpMetricsEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
)
if mibBuilder.loadTexts:
    cfmRtpMetricsEntry.setStatus("current")


class _CfmRtpMetricsValid_Type(Bits):
    """Custom type cfmRtpMetricsValid based on Bits"""
    namedValues = NamedValues(
        *(("avgLossDistance", 5),
          ("avgLossDuration", 4),
          ("expectedPkts", 0),
          ("jitter", 6),
          ("lossFraction", 2),
          ("lossIntervals", 3),
          ("lostPkts", 1))
    )

_CfmRtpMetricsValid_Type.__name__ = "Bits"
_CfmRtpMetricsValid_Object = MibTableColumn
cfmRtpMetricsValid = _CfmRtpMetricsValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 1),
    _CfmRtpMetricsValid_Type()
)
cfmRtpMetricsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsValid.setStatus("current")
_CfmRtpMetricsExpectedPkts_Type = Counter64
_CfmRtpMetricsExpectedPkts_Object = MibTableColumn
cfmRtpMetricsExpectedPkts = _CfmRtpMetricsExpectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 2),
    _CfmRtpMetricsExpectedPkts_Type()
)
cfmRtpMetricsExpectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsExpectedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfmRtpMetricsExpectedPkts.setUnits("packets")
_CfmRtpMetricsLostPkts_Type = Counter64
_CfmRtpMetricsLostPkts_Object = MibTableColumn
cfmRtpMetricsLostPkts = _CfmRtpMetricsLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 3),
    _CfmRtpMetricsLostPkts_Type()
)
cfmRtpMetricsLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsLostPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfmRtpMetricsLostPkts.setUnits("packets")
_CfmRtpMetricsFracScale_Type = FlowMetricScale
_CfmRtpMetricsFracScale_Object = MibTableColumn
cfmRtpMetricsFracScale = _CfmRtpMetricsFracScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 4),
    _CfmRtpMetricsFracScale_Type()
)
cfmRtpMetricsFracScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsFracScale.setStatus("current")
_CfmRtpMetricsFracPrecision_Type = FlowMetricPrecision
_CfmRtpMetricsFracPrecision_Object = MibTableColumn
cfmRtpMetricsFracPrecision = _CfmRtpMetricsFracPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 5),
    _CfmRtpMetricsFracPrecision_Type()
)
cfmRtpMetricsFracPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsFracPrecision.setStatus("current")
_CfmRtpMetricsFrac_Type = FlowMetricValue
_CfmRtpMetricsFrac_Object = MibTableColumn
cfmRtpMetricsFrac = _CfmRtpMetricsFrac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 6),
    _CfmRtpMetricsFrac_Type()
)
cfmRtpMetricsFrac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsFrac.setStatus("current")
_CfmRtpMetricsLIs_Type = Counter64
_CfmRtpMetricsLIs_Object = MibTableColumn
cfmRtpMetricsLIs = _CfmRtpMetricsLIs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 7),
    _CfmRtpMetricsLIs_Type()
)
cfmRtpMetricsLIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsLIs.setStatus("current")
_CfmRtpMetricsAvgLDScale_Type = FlowMetricScale
_CfmRtpMetricsAvgLDScale_Object = MibTableColumn
cfmRtpMetricsAvgLDScale = _CfmRtpMetricsAvgLDScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 8),
    _CfmRtpMetricsAvgLDScale_Type()
)
cfmRtpMetricsAvgLDScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsAvgLDScale.setStatus("current")
_CfmRtpMetricsAvgLDPrecision_Type = FlowMetricPrecision
_CfmRtpMetricsAvgLDPrecision_Object = MibTableColumn
cfmRtpMetricsAvgLDPrecision = _CfmRtpMetricsAvgLDPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 9),
    _CfmRtpMetricsAvgLDPrecision_Type()
)
cfmRtpMetricsAvgLDPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsAvgLDPrecision.setStatus("current")
_CfmRtpMetricsAvgLD_Type = FlowMetricValue
_CfmRtpMetricsAvgLD_Object = MibTableColumn
cfmRtpMetricsAvgLD = _CfmRtpMetricsAvgLD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 10),
    _CfmRtpMetricsAvgLD_Type()
)
cfmRtpMetricsAvgLD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsAvgLD.setStatus("current")
_CfmRtpMetricsAvgLossDistance_Type = Gauge32
_CfmRtpMetricsAvgLossDistance_Object = MibTableColumn
cfmRtpMetricsAvgLossDistance = _CfmRtpMetricsAvgLossDistance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 11),
    _CfmRtpMetricsAvgLossDistance_Type()
)
cfmRtpMetricsAvgLossDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsAvgLossDistance.setStatus("current")
_CfmRtpMetricsJitterScale_Type = FlowMetricScale
_CfmRtpMetricsJitterScale_Object = MibTableColumn
cfmRtpMetricsJitterScale = _CfmRtpMetricsJitterScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 12),
    _CfmRtpMetricsJitterScale_Type()
)
cfmRtpMetricsJitterScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsJitterScale.setStatus("current")
_CfmRtpMetricsJitterPrecision_Type = FlowMetricPrecision
_CfmRtpMetricsJitterPrecision_Object = MibTableColumn
cfmRtpMetricsJitterPrecision = _CfmRtpMetricsJitterPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 13),
    _CfmRtpMetricsJitterPrecision_Type()
)
cfmRtpMetricsJitterPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsJitterPrecision.setStatus("current")
_CfmRtpMetricsJitter_Type = FlowMetricValue
_CfmRtpMetricsJitter_Object = MibTableColumn
cfmRtpMetricsJitter = _CfmRtpMetricsJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 1, 1, 14),
    _CfmRtpMetricsJitter_Type()
)
cfmRtpMetricsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsJitter.setStatus("current")
if mibBuilder.loadTexts:
    cfmRtpMetricsJitter.setUnits("seconds")
_CfmRtpMetricsTableChanged_Type = TimeStamp
_CfmRtpMetricsTableChanged_Object = MibScalar
cfmRtpMetricsTableChanged = _CfmRtpMetricsTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 2),
    _CfmRtpMetricsTableChanged_Type()
)
cfmRtpMetricsTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsTableChanged.setStatus("current")
_CfmRtpMetricsIntTable_Object = MibTable
cfmRtpMetricsIntTable = _CfmRtpMetricsIntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfmRtpMetricsIntTable.setStatus("current")
_CfmRtpMetricsIntEntry_Object = MibTableRow
cfmRtpMetricsIntEntry = _CfmRtpMetricsIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1)
)
cfmRtpMetricsIntEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntNumber"),
)
if mibBuilder.loadTexts:
    cfmRtpMetricsIntEntry.setStatus("current")


class _CfmRtpMetricsIntValid_Type(Bits):
    """Custom type cfmRtpMetricsIntValid based on Bits"""
    namedValues = NamedValues(
        *(("avgLossDistance", 5),
          ("avgLossIntervalDuration", 4),
          ("expectedPkts", 0),
          ("lossFraction", 2),
          ("lossIntervals", 3),
          ("lostPkts", 1),
          ("maxJitter", 6),
          ("maxMinTransit", 7))
    )

_CfmRtpMetricsIntValid_Type.__name__ = "Bits"
_CfmRtpMetricsIntValid_Object = MibTableColumn
cfmRtpMetricsIntValid = _CfmRtpMetricsIntValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 1),
    _CfmRtpMetricsIntValid_Type()
)
cfmRtpMetricsIntValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntValid.setStatus("current")
_CfmRtpMetricsIntExpectedPkts_Type = ReportIntervalCount
_CfmRtpMetricsIntExpectedPkts_Object = MibTableColumn
cfmRtpMetricsIntExpectedPkts = _CfmRtpMetricsIntExpectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 2),
    _CfmRtpMetricsIntExpectedPkts_Type()
)
cfmRtpMetricsIntExpectedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntExpectedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntExpectedPkts.setUnits("packets")
_CfmRtpMetricsIntLostPkts_Type = ReportIntervalCount
_CfmRtpMetricsIntLostPkts_Object = MibTableColumn
cfmRtpMetricsIntLostPkts = _CfmRtpMetricsIntLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 3),
    _CfmRtpMetricsIntLostPkts_Type()
)
cfmRtpMetricsIntLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntLostPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntLostPkts.setUnits("packets")
_CfmRtpMetricsIntFracScale_Type = FlowMetricScale
_CfmRtpMetricsIntFracScale_Object = MibTableColumn
cfmRtpMetricsIntFracScale = _CfmRtpMetricsIntFracScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 4),
    _CfmRtpMetricsIntFracScale_Type()
)
cfmRtpMetricsIntFracScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntFracScale.setStatus("current")
_CfmRtpMetricsIntFracPrecision_Type = FlowMetricPrecision
_CfmRtpMetricsIntFracPrecision_Object = MibTableColumn
cfmRtpMetricsIntFracPrecision = _CfmRtpMetricsIntFracPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 5),
    _CfmRtpMetricsIntFracPrecision_Type()
)
cfmRtpMetricsIntFracPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntFracPrecision.setStatus("current")
_CfmRtpMetricsIntFrac_Type = FlowMetricValue
_CfmRtpMetricsIntFrac_Object = MibTableColumn
cfmRtpMetricsIntFrac = _CfmRtpMetricsIntFrac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 6),
    _CfmRtpMetricsIntFrac_Type()
)
cfmRtpMetricsIntFrac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntFrac.setStatus("current")
_CfmRtpMetricsIntLIs_Type = ReportIntervalCount
_CfmRtpMetricsIntLIs_Object = MibTableColumn
cfmRtpMetricsIntLIs = _CfmRtpMetricsIntLIs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 7),
    _CfmRtpMetricsIntLIs_Type()
)
cfmRtpMetricsIntLIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntLIs.setStatus("current")
_CfmRtpMetricsIntAvgLDScale_Type = FlowMetricScale
_CfmRtpMetricsIntAvgLDScale_Object = MibTableColumn
cfmRtpMetricsIntAvgLDScale = _CfmRtpMetricsIntAvgLDScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 8),
    _CfmRtpMetricsIntAvgLDScale_Type()
)
cfmRtpMetricsIntAvgLDScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntAvgLDScale.setStatus("current")
_CfmRtpMetricsIntAvgLDPrecision_Type = FlowMetricPrecision
_CfmRtpMetricsIntAvgLDPrecision_Object = MibTableColumn
cfmRtpMetricsIntAvgLDPrecision = _CfmRtpMetricsIntAvgLDPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 9),
    _CfmRtpMetricsIntAvgLDPrecision_Type()
)
cfmRtpMetricsIntAvgLDPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntAvgLDPrecision.setStatus("current")
_CfmRtpMetricsIntAvgLD_Type = FlowMetricValue
_CfmRtpMetricsIntAvgLD_Object = MibTableColumn
cfmRtpMetricsIntAvgLD = _CfmRtpMetricsIntAvgLD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 10),
    _CfmRtpMetricsIntAvgLD_Type()
)
cfmRtpMetricsIntAvgLD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntAvgLD.setStatus("current")
_CfmRtpMetricsIntAvgLossDistance_Type = ReportIntervalCount
_CfmRtpMetricsIntAvgLossDistance_Object = MibTableColumn
cfmRtpMetricsIntAvgLossDistance = _CfmRtpMetricsIntAvgLossDistance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 11),
    _CfmRtpMetricsIntAvgLossDistance_Type()
)
cfmRtpMetricsIntAvgLossDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntAvgLossDistance.setStatus("current")
_CfmRtpMetricsIntJitterScale_Type = FlowMetricScale
_CfmRtpMetricsIntJitterScale_Object = MibTableColumn
cfmRtpMetricsIntJitterScale = _CfmRtpMetricsIntJitterScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 12),
    _CfmRtpMetricsIntJitterScale_Type()
)
cfmRtpMetricsIntJitterScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntJitterScale.setStatus("current")
_CfmRtpMetricsIntJitterPrecision_Type = FlowMetricPrecision
_CfmRtpMetricsIntJitterPrecision_Object = MibTableColumn
cfmRtpMetricsIntJitterPrecision = _CfmRtpMetricsIntJitterPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 13),
    _CfmRtpMetricsIntJitterPrecision_Type()
)
cfmRtpMetricsIntJitterPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntJitterPrecision.setStatus("current")
_CfmRtpMetricsIntJitter_Type = FlowMetricValue
_CfmRtpMetricsIntJitter_Object = MibTableColumn
cfmRtpMetricsIntJitter = _CfmRtpMetricsIntJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 14),
    _CfmRtpMetricsIntJitter_Type()
)
cfmRtpMetricsIntJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntJitter.setStatus("current")
_CfmRtpMetricsIntTransitScale_Type = FlowMetricScale
_CfmRtpMetricsIntTransitScale_Object = MibTableColumn
cfmRtpMetricsIntTransitScale = _CfmRtpMetricsIntTransitScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 15),
    _CfmRtpMetricsIntTransitScale_Type()
)
cfmRtpMetricsIntTransitScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntTransitScale.setStatus("current")
_CfmRtpMetricsIntTransitPrecision_Type = FlowMetricPrecision
_CfmRtpMetricsIntTransitPrecision_Object = MibTableColumn
cfmRtpMetricsIntTransitPrecision = _CfmRtpMetricsIntTransitPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 16),
    _CfmRtpMetricsIntTransitPrecision_Type()
)
cfmRtpMetricsIntTransitPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntTransitPrecision.setStatus("current")
_CfmRtpMetricsIntTransit_Type = FlowMetricValue
_CfmRtpMetricsIntTransit_Object = MibTableColumn
cfmRtpMetricsIntTransit = _CfmRtpMetricsIntTransit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 1, 1, 3, 1, 17),
    _CfmRtpMetricsIntTransit_Type()
)
cfmRtpMetricsIntTransit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmRtpMetricsIntTransit.setStatus("current")
_CiscoRtpMetricsMIBConform_ObjectIdentity = ObjectIdentity
ciscoRtpMetricsMIBConform = _CiscoRtpMetricsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 2)
)
_CiscoRtpMetricsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoRtpMetricsMIBCompliances = _CiscoRtpMetricsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 2, 1)
)
_CiscoRtpMetricsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoRtpMetricsMIBGroups = _CiscoRtpMetricsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 2, 2)
)
_CiscoRtpMetricsMIBIds_ObjectIdentity = ObjectIdentity
ciscoRtpMetricsMIBIds = _CiscoRtpMetricsMIBIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3)
)
_CfmRtpMonitoredElements_ObjectIdentity = ObjectIdentity
cfmRtpMonitoredElements = _CfmRtpMonitoredElements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1)
)
_CfmeRtpSsrcMismatch_ObjectIdentity = ObjectIdentity
cfmeRtpSsrcMismatch = _CfmeRtpSsrcMismatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cfmeRtpSsrcMismatch.setStatus("current")
_CfmeRtpCumulativeLostPkts_ObjectIdentity = ObjectIdentity
cfmeRtpCumulativeLostPkts = _CfmeRtpCumulativeLostPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cfmeRtpCumulativeLostPkts.setStatus("current")
_CfmeRtpCumulativeLossFraction_ObjectIdentity = ObjectIdentity
cfmeRtpCumulativeLossFraction = _CfmeRtpCumulativeLossFraction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cfmeRtpCumulativeLossFraction.setStatus("current")
_CfmeRtpCumulativeLossIntervals_ObjectIdentity = ObjectIdentity
cfmeRtpCumulativeLossIntervals = _CfmeRtpCumulativeLossIntervals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cfmeRtpCumulativeLossIntervals.setStatus("current")
_CfmeRtpCumulativeAvgLossDuration_ObjectIdentity = ObjectIdentity
cfmeRtpCumulativeAvgLossDuration = _CfmeRtpCumulativeAvgLossDuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cfmeRtpCumulativeAvgLossDuration.setStatus("current")
_CfmeRtpCumulativeAvgLossDistance_ObjectIdentity = ObjectIdentity
cfmeRtpCumulativeAvgLossDistance = _CfmeRtpCumulativeAvgLossDistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cfmeRtpCumulativeAvgLossDistance.setStatus("current")
_CfmeRtpCumulativeJitter_ObjectIdentity = ObjectIdentity
cfmeRtpCumulativeJitter = _CfmeRtpCumulativeJitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cfmeRtpCumulativeJitter.setStatus("current")
_CfmeRtpLostPkts_ObjectIdentity = ObjectIdentity
cfmeRtpLostPkts = _CfmeRtpLostPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 8)
)
if mibBuilder.loadTexts:
    cfmeRtpLostPkts.setStatus("current")
_CfmeRtpLossFraction_ObjectIdentity = ObjectIdentity
cfmeRtpLossFraction = _CfmeRtpLossFraction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 9)
)
if mibBuilder.loadTexts:
    cfmeRtpLossFraction.setStatus("current")
_CfmeRtpLossIntervals_ObjectIdentity = ObjectIdentity
cfmeRtpLossIntervals = _CfmeRtpLossIntervals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 10)
)
if mibBuilder.loadTexts:
    cfmeRtpLossIntervals.setStatus("current")
_CfmeRtpAvgLossDuration_ObjectIdentity = ObjectIdentity
cfmeRtpAvgLossDuration = _CfmeRtpAvgLossDuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 11)
)
if mibBuilder.loadTexts:
    cfmeRtpAvgLossDuration.setStatus("current")
_CfmeRtpAvgLossDistance_ObjectIdentity = ObjectIdentity
cfmeRtpAvgLossDistance = _CfmeRtpAvgLossDistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 12)
)
if mibBuilder.loadTexts:
    cfmeRtpAvgLossDistance.setStatus("current")
_CfmeRtpMaxJitter_ObjectIdentity = ObjectIdentity
cfmeRtpMaxJitter = _CfmeRtpMaxJitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 13)
)
if mibBuilder.loadTexts:
    cfmeRtpMaxJitter.setStatus("current")
_CfmeRtpMaxMinTransit_ObjectIdentity = ObjectIdentity
cfmeRtpMaxMinTransit = _CfmeRtpMaxMinTransit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 3, 1, 14)
)
if mibBuilder.loadTexts:
    cfmeRtpMaxMinTransit.setStatus("current")

# Managed Objects groups

cfmRtpMetricsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 2, 2, 1)
)
cfmRtpMetricsGroup.setObjects(
      *(("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsValid"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsExpectedPkts"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsLostPkts"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsFracScale"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsFracPrecision"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsFrac"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsLIs"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsAvgLDScale"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsAvgLDPrecision"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsAvgLD"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsAvgLossDistance"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsJitterScale"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsJitterPrecision"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsJitter"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsTableChanged"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntValid"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntExpectedPkts"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntLostPkts"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntFracScale"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntFracPrecision"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntFrac"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntLIs"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntAvgLDScale"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntAvgLDPrecision"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntAvgLD"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntAvgLossDistance"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntJitterScale"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntJitterPrecision"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntJitter"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntTransitScale"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntTransitPrecision"),
        ("CISCO-RTP-METRICS-MIB", "cfmRtpMetricsIntTransit"))
)
if mibBuilder.loadTexts:
    cfmRtpMetricsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoRtpMetricsCompliance01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 703, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoRtpMetricsCompliance01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RTP-METRICS-MIB",
    **{"ciscoRtpMetricsMIB": ciscoRtpMetricsMIB,
       "ciscoRtpMetricsMIBNotifs": ciscoRtpMetricsMIBNotifs,
       "ciscoRtpMetricsMIBObjects": ciscoRtpMetricsMIBObjects,
       "cfmRtpMetrics": cfmRtpMetrics,
       "cfmRtpMetricsTable": cfmRtpMetricsTable,
       "cfmRtpMetricsEntry": cfmRtpMetricsEntry,
       "cfmRtpMetricsValid": cfmRtpMetricsValid,
       "cfmRtpMetricsExpectedPkts": cfmRtpMetricsExpectedPkts,
       "cfmRtpMetricsLostPkts": cfmRtpMetricsLostPkts,
       "cfmRtpMetricsFracScale": cfmRtpMetricsFracScale,
       "cfmRtpMetricsFracPrecision": cfmRtpMetricsFracPrecision,
       "cfmRtpMetricsFrac": cfmRtpMetricsFrac,
       "cfmRtpMetricsLIs": cfmRtpMetricsLIs,
       "cfmRtpMetricsAvgLDScale": cfmRtpMetricsAvgLDScale,
       "cfmRtpMetricsAvgLDPrecision": cfmRtpMetricsAvgLDPrecision,
       "cfmRtpMetricsAvgLD": cfmRtpMetricsAvgLD,
       "cfmRtpMetricsAvgLossDistance": cfmRtpMetricsAvgLossDistance,
       "cfmRtpMetricsJitterScale": cfmRtpMetricsJitterScale,
       "cfmRtpMetricsJitterPrecision": cfmRtpMetricsJitterPrecision,
       "cfmRtpMetricsJitter": cfmRtpMetricsJitter,
       "cfmRtpMetricsTableChanged": cfmRtpMetricsTableChanged,
       "cfmRtpMetricsIntTable": cfmRtpMetricsIntTable,
       "cfmRtpMetricsIntEntry": cfmRtpMetricsIntEntry,
       "cfmRtpMetricsIntValid": cfmRtpMetricsIntValid,
       "cfmRtpMetricsIntExpectedPkts": cfmRtpMetricsIntExpectedPkts,
       "cfmRtpMetricsIntLostPkts": cfmRtpMetricsIntLostPkts,
       "cfmRtpMetricsIntFracScale": cfmRtpMetricsIntFracScale,
       "cfmRtpMetricsIntFracPrecision": cfmRtpMetricsIntFracPrecision,
       "cfmRtpMetricsIntFrac": cfmRtpMetricsIntFrac,
       "cfmRtpMetricsIntLIs": cfmRtpMetricsIntLIs,
       "cfmRtpMetricsIntAvgLDScale": cfmRtpMetricsIntAvgLDScale,
       "cfmRtpMetricsIntAvgLDPrecision": cfmRtpMetricsIntAvgLDPrecision,
       "cfmRtpMetricsIntAvgLD": cfmRtpMetricsIntAvgLD,
       "cfmRtpMetricsIntAvgLossDistance": cfmRtpMetricsIntAvgLossDistance,
       "cfmRtpMetricsIntJitterScale": cfmRtpMetricsIntJitterScale,
       "cfmRtpMetricsIntJitterPrecision": cfmRtpMetricsIntJitterPrecision,
       "cfmRtpMetricsIntJitter": cfmRtpMetricsIntJitter,
       "cfmRtpMetricsIntTransitScale": cfmRtpMetricsIntTransitScale,
       "cfmRtpMetricsIntTransitPrecision": cfmRtpMetricsIntTransitPrecision,
       "cfmRtpMetricsIntTransit": cfmRtpMetricsIntTransit,
       "ciscoRtpMetricsMIBConform": ciscoRtpMetricsMIBConform,
       "ciscoRtpMetricsMIBCompliances": ciscoRtpMetricsMIBCompliances,
       "ciscoRtpMetricsCompliance01": ciscoRtpMetricsCompliance01,
       "ciscoRtpMetricsMIBGroups": ciscoRtpMetricsMIBGroups,
       "cfmRtpMetricsGroup": cfmRtpMetricsGroup,
       "ciscoRtpMetricsMIBIds": ciscoRtpMetricsMIBIds,
       "cfmRtpMonitoredElements": cfmRtpMonitoredElements,
       "cfmeRtpSsrcMismatch": cfmeRtpSsrcMismatch,
       "cfmeRtpCumulativeLostPkts": cfmeRtpCumulativeLostPkts,
       "cfmeRtpCumulativeLossFraction": cfmeRtpCumulativeLossFraction,
       "cfmeRtpCumulativeLossIntervals": cfmeRtpCumulativeLossIntervals,
       "cfmeRtpCumulativeAvgLossDuration": cfmeRtpCumulativeAvgLossDuration,
       "cfmeRtpCumulativeAvgLossDistance": cfmeRtpCumulativeAvgLossDistance,
       "cfmeRtpCumulativeJitter": cfmeRtpCumulativeJitter,
       "cfmeRtpLostPkts": cfmeRtpLostPkts,
       "cfmeRtpLossFraction": cfmeRtpLossFraction,
       "cfmeRtpLossIntervals": cfmeRtpLossIntervals,
       "cfmeRtpAvgLossDuration": cfmeRtpAvgLossDuration,
       "cfmeRtpAvgLossDistance": cfmeRtpAvgLossDistance,
       "cfmeRtpMaxJitter": cfmeRtpMaxJitter,
       "cfmeRtpMaxMinTransit": cfmeRtpMaxMinTransit}
)
