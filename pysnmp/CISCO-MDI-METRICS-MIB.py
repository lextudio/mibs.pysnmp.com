# SNMP MIB module (CISCO-MDI-METRICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MDI-METRICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:16 2024
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

(FlowBitRateUnits,
 FlowCfgRateType,
 FlowMetricPrecision,
 FlowMetricScale,
 FlowMetricValue) = mibBuilder.importSymbols(
    "CISCO-FLOW-MONITOR-TC-MIB",
    "FlowBitRateUnits",
    "FlowCfgRateType",
    "FlowMetricPrecision",
    "FlowMetricScale",
    "FlowMetricValue")

(ReportIntervalCount,) = mibBuilder.importSymbols(
    "CISCO-REPORT-INTERVAL-TC-MIB",
    "ReportIntervalCount")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(TimeIntervalMin,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "TimeIntervalMin")

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

ciscoMdiMetricsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699)
)
ciscoMdiMetricsMIB.setRevisions(
        ("2009-11-02 00:00",
         "2009-06-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoMdiMetricsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMdiMetricsMIBNotifs = _CiscoMdiMetricsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 0)
)
_CiscoMdiMetricsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMdiMetricsMIBObjects = _CiscoMdiMetricsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1)
)
_CfmMdiMetrics_ObjectIdentity = ObjectIdentity
cfmMdiMetrics = _CfmMdiMetrics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1)
)
_CfmMdiMetricsTable_Object = MibTable
cfmMdiMetricsTable = _CfmMdiMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfmMdiMetricsTable.setStatus("current")
_CfmMdiMetricsEntry_Object = MibTableRow
cfmMdiMetricsEntry = _CfmMdiMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 1, 1)
)
cfmMdiMetricsEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
)
if mibBuilder.loadTexts:
    cfmMdiMetricsEntry.setStatus("current")
_CfmMdiMetricsCfgRateType_Type = FlowCfgRateType
_CfmMdiMetricsCfgRateType_Object = MibTableColumn
cfmMdiMetricsCfgRateType = _CfmMdiMetricsCfgRateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 1, 1, 1),
    _CfmMdiMetricsCfgRateType_Type()
)
cfmMdiMetricsCfgRateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsCfgRateType.setStatus("current")
_CfmMdiMetricsCfgBitRate_Type = FlowBitRateUnits
_CfmMdiMetricsCfgBitRate_Object = MibTableColumn
cfmMdiMetricsCfgBitRate = _CfmMdiMetricsCfgBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 1, 1, 2),
    _CfmMdiMetricsCfgBitRate_Type()
)
cfmMdiMetricsCfgBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsCfgBitRate.setStatus("current")


class _CfmMdiMetricsCfgRate_Type(Unsigned32):
    """Custom type cfmMdiMetricsCfgRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CfmMdiMetricsCfgRate_Type.__name__ = "Unsigned32"
_CfmMdiMetricsCfgRate_Object = MibTableColumn
cfmMdiMetricsCfgRate = _CfmMdiMetricsCfgRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 1, 1, 3),
    _CfmMdiMetricsCfgRate_Type()
)
cfmMdiMetricsCfgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsCfgRate.setStatus("current")


class _CfmMdiMetricsCfgMediaPktSize_Type(Unsigned32):
    """Custom type cfmMdiMetricsCfgMediaPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 65535),
    )


_CfmMdiMetricsCfgMediaPktSize_Type.__name__ = "Unsigned32"
_CfmMdiMetricsCfgMediaPktSize_Object = MibTableColumn
cfmMdiMetricsCfgMediaPktSize = _CfmMdiMetricsCfgMediaPktSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 1, 1, 4),
    _CfmMdiMetricsCfgMediaPktSize_Type()
)
cfmMdiMetricsCfgMediaPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsCfgMediaPktSize.setStatus("current")
if mibBuilder.loadTexts:
    cfmMdiMetricsCfgMediaPktSize.setUnits("octets")


class _CfmMdiMetricsValid_Type(Bits):
    """Custom type cfmMdiMetricsValid based on Bits"""
    namedValues = NamedValues(
        *(("lostPkts", 0),
          ("mediaDiscontinuityCount", 2),
          ("mediaLossRate", 1))
    )

_CfmMdiMetricsValid_Type.__name__ = "Bits"
_CfmMdiMetricsValid_Object = MibTableColumn
cfmMdiMetricsValid = _CfmMdiMetricsValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 1, 1, 5),
    _CfmMdiMetricsValid_Type()
)
cfmMdiMetricsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsValid.setStatus("current")
_CfmMdiMetricsLostPkts_Type = Counter64
_CfmMdiMetricsLostPkts_Object = MibTableColumn
cfmMdiMetricsLostPkts = _CfmMdiMetricsLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 1, 1, 6),
    _CfmMdiMetricsLostPkts_Type()
)
cfmMdiMetricsLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsLostPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfmMdiMetricsLostPkts.setUnits("packets")
_CfmMdiMetricsMlrScale_Type = FlowMetricScale
_CfmMdiMetricsMlrScale_Object = MibTableColumn
cfmMdiMetricsMlrScale = _CfmMdiMetricsMlrScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 1, 1, 7),
    _CfmMdiMetricsMlrScale_Type()
)
cfmMdiMetricsMlrScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsMlrScale.setStatus("current")
_CfmMdiMetricsMlrPrecision_Type = FlowMetricPrecision
_CfmMdiMetricsMlrPrecision_Object = MibTableColumn
cfmMdiMetricsMlrPrecision = _CfmMdiMetricsMlrPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 1, 1, 8),
    _CfmMdiMetricsMlrPrecision_Type()
)
cfmMdiMetricsMlrPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsMlrPrecision.setStatus("current")
_CfmMdiMetricsMlr_Type = FlowMetricValue
_CfmMdiMetricsMlr_Object = MibTableColumn
cfmMdiMetricsMlr = _CfmMdiMetricsMlr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 1, 1, 9),
    _CfmMdiMetricsMlr_Type()
)
cfmMdiMetricsMlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsMlr.setStatus("current")
if mibBuilder.loadTexts:
    cfmMdiMetricsMlr.setUnits("packets per second")
_CfmMdiMetricsMdc_Type = Counter64
_CfmMdiMetricsMdc_Object = MibTableColumn
cfmMdiMetricsMdc = _CfmMdiMetricsMdc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 1, 1, 10),
    _CfmMdiMetricsMdc_Type()
)
cfmMdiMetricsMdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsMdc.setStatus("current")
if mibBuilder.loadTexts:
    cfmMdiMetricsMdc.setUnits("Events")
_CfmMdiMetricsTableChanged_Type = TimeStamp
_CfmMdiMetricsTableChanged_Object = MibScalar
cfmMdiMetricsTableChanged = _CfmMdiMetricsTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 2),
    _CfmMdiMetricsTableChanged_Type()
)
cfmMdiMetricsTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsTableChanged.setStatus("current")
_CfmMdiMetricsIntTable_Object = MibTable
cfmMdiMetricsIntTable = _CfmMdiMetricsIntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfmMdiMetricsIntTable.setStatus("current")
_CfmMdiMetricsIntEntry_Object = MibTableRow
cfmMdiMetricsIntEntry = _CfmMdiMetricsIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1)
)
cfmMdiMetricsIntEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntNumber"),
)
if mibBuilder.loadTexts:
    cfmMdiMetricsIntEntry.setStatus("current")


class _CfmMdiMetricsIntValid_Type(Bits):
    """Custom type cfmMdiMetricsIntValid based on Bits"""
    namedValues = NamedValues(
        *(("delayFactor", 4),
          ("lostPkts", 0),
          ("mediaDiscontinuityCount", 6),
          ("mediaLossRate", 5),
          ("mediaRate", 3),
          ("vbMax", 2),
          ("vbMin", 1))
    )

_CfmMdiMetricsIntValid_Type.__name__ = "Bits"
_CfmMdiMetricsIntValid_Object = MibTableColumn
cfmMdiMetricsIntValid = _CfmMdiMetricsIntValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 1),
    _CfmMdiMetricsIntValid_Type()
)
cfmMdiMetricsIntValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntValid.setStatus("current")
_CfmMdiMetricsIntLostPkts_Type = ReportIntervalCount
_CfmMdiMetricsIntLostPkts_Object = MibTableColumn
cfmMdiMetricsIntLostPkts = _CfmMdiMetricsIntLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 2),
    _CfmMdiMetricsIntLostPkts_Type()
)
cfmMdiMetricsIntLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntLostPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntLostPkts.setUnits("packets")
_CfmMdiMetricsIntVbMin_Type = ReportIntervalCount
_CfmMdiMetricsIntVbMin_Object = MibTableColumn
cfmMdiMetricsIntVbMin = _CfmMdiMetricsIntVbMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 3),
    _CfmMdiMetricsIntVbMin_Type()
)
cfmMdiMetricsIntVbMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntVbMin.setStatus("current")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntVbMin.setUnits("bytes")
_CfmMdiMetricsIntVbMax_Type = ReportIntervalCount
_CfmMdiMetricsIntVbMax_Object = MibTableColumn
cfmMdiMetricsIntVbMax = _CfmMdiMetricsIntVbMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 4),
    _CfmMdiMetricsIntVbMax_Type()
)
cfmMdiMetricsIntVbMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntVbMax.setStatus("current")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntVbMax.setUnits("bytes")
_CfmMdiMetricsIntMrUnits_Type = FlowBitRateUnits
_CfmMdiMetricsIntMrUnits_Object = MibTableColumn
cfmMdiMetricsIntMrUnits = _CfmMdiMetricsIntMrUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 5),
    _CfmMdiMetricsIntMrUnits_Type()
)
cfmMdiMetricsIntMrUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntMrUnits.setStatus("current")
_CfmMdiMetricsIntMr_Type = ReportIntervalCount
_CfmMdiMetricsIntMr_Object = MibTableColumn
cfmMdiMetricsIntMr = _CfmMdiMetricsIntMr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 6),
    _CfmMdiMetricsIntMr_Type()
)
cfmMdiMetricsIntMr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntMr.setStatus("current")
_CfmMdiMetricsIntDfScale_Type = FlowMetricScale
_CfmMdiMetricsIntDfScale_Object = MibTableColumn
cfmMdiMetricsIntDfScale = _CfmMdiMetricsIntDfScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 7),
    _CfmMdiMetricsIntDfScale_Type()
)
cfmMdiMetricsIntDfScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntDfScale.setStatus("current")
_CfmMdiMetricsIntDfPrecision_Type = FlowMetricPrecision
_CfmMdiMetricsIntDfPrecision_Object = MibTableColumn
cfmMdiMetricsIntDfPrecision = _CfmMdiMetricsIntDfPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 8),
    _CfmMdiMetricsIntDfPrecision_Type()
)
cfmMdiMetricsIntDfPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntDfPrecision.setStatus("current")
_CfmMdiMetricsIntDf_Type = FlowMetricValue
_CfmMdiMetricsIntDf_Object = MibTableColumn
cfmMdiMetricsIntDf = _CfmMdiMetricsIntDf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 9),
    _CfmMdiMetricsIntDf_Type()
)
cfmMdiMetricsIntDf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntDf.setStatus("current")
_CfmMdiMetricsIntMlrScale_Type = FlowMetricScale
_CfmMdiMetricsIntMlrScale_Object = MibTableColumn
cfmMdiMetricsIntMlrScale = _CfmMdiMetricsIntMlrScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 10),
    _CfmMdiMetricsIntMlrScale_Type()
)
cfmMdiMetricsIntMlrScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntMlrScale.setStatus("current")
_CfmMdiMetricsIntMlrPrecision_Type = FlowMetricPrecision
_CfmMdiMetricsIntMlrPrecision_Object = MibTableColumn
cfmMdiMetricsIntMlrPrecision = _CfmMdiMetricsIntMlrPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 11),
    _CfmMdiMetricsIntMlrPrecision_Type()
)
cfmMdiMetricsIntMlrPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntMlrPrecision.setStatus("current")
_CfmMdiMetricsIntMlr_Type = FlowMetricValue
_CfmMdiMetricsIntMlr_Object = MibTableColumn
cfmMdiMetricsIntMlr = _CfmMdiMetricsIntMlr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 12),
    _CfmMdiMetricsIntMlr_Type()
)
cfmMdiMetricsIntMlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntMlr.setStatus("current")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntMlr.setUnits("packets per second")
_CfmMdiMetricsIntMdc_Type = ReportIntervalCount
_CfmMdiMetricsIntMdc_Object = MibTableColumn
cfmMdiMetricsIntMdc = _CfmMdiMetricsIntMdc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 1, 1, 3, 1, 13),
    _CfmMdiMetricsIntMdc_Type()
)
cfmMdiMetricsIntMdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntMdc.setStatus("current")
if mibBuilder.loadTexts:
    cfmMdiMetricsIntMdc.setUnits("Events")
_CiscoMdiMetricsMIBConform_ObjectIdentity = ObjectIdentity
ciscoMdiMetricsMIBConform = _CiscoMdiMetricsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 2)
)
_CiscoMdiMetricsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMdiMetricsMIBCompliances = _CiscoMdiMetricsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 2, 1)
)
_CiscoMdiMetricsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMdiMetricsMIBGroups = _CiscoMdiMetricsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 2, 2)
)
_CiscoMdiMetricsMIBIds_ObjectIdentity = ObjectIdentity
ciscoMdiMetricsMIBIds = _CiscoMdiMetricsMIBIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 3)
)
_CfmMdiMonitoredElements_ObjectIdentity = ObjectIdentity
cfmMdiMonitoredElements = _CfmMdiMonitoredElements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 3, 1)
)
_CfmeMdiCumulativeLostPkts_ObjectIdentity = ObjectIdentity
cfmeMdiCumulativeLostPkts = _CfmeMdiCumulativeLostPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cfmeMdiCumulativeLostPkts.setStatus("current")
_CfmeMdiCumulativeMlr_ObjectIdentity = ObjectIdentity
cfmeMdiCumulativeMlr = _CfmeMdiCumulativeMlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cfmeMdiCumulativeMlr.setStatus("current")
_CfmeMdiCumulativeMdc_ObjectIdentity = ObjectIdentity
cfmeMdiCumulativeMdc = _CfmeMdiCumulativeMdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cfmeMdiCumulativeMdc.setStatus("current")
_CfmeMdiLostPkts_ObjectIdentity = ObjectIdentity
cfmeMdiLostPkts = _CfmeMdiLostPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cfmeMdiLostPkts.setStatus("current")
_CfmeMdiDf_ObjectIdentity = ObjectIdentity
cfmeMdiDf = _CfmeMdiDf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cfmeMdiDf.setStatus("current")
_CfmeMdiMlr_ObjectIdentity = ObjectIdentity
cfmeMdiMlr = _CfmeMdiMlr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cfmeMdiMlr.setStatus("current")
_CfmeMdiMdc_ObjectIdentity = ObjectIdentity
cfmeMdiMdc = _CfmeMdiMdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cfmeMdiMdc.setStatus("current")

# Managed Objects groups

cfmMdiMetricsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 2, 2, 1)
)
cfmMdiMetricsGroup.setObjects(
      *(("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsCfgRateType"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsCfgBitRate"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsCfgRate"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsCfgMediaPktSize"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsValid"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsLostPkts"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsMlrScale"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsMlrPrecision"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsMlr"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsMdc"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsTableChanged"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntValid"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntLostPkts"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntVbMin"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntVbMax"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntMrUnits"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntMr"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntDfScale"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntDfPrecision"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntDf"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntMlrScale"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntMlrPrecision"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntMlr"),
        ("CISCO-MDI-METRICS-MIB", "cfmMdiMetricsIntMdc"))
)
if mibBuilder.loadTexts:
    cfmMdiMetricsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoMdiMetricsCompliance01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 699, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMdiMetricsCompliance01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MDI-METRICS-MIB",
    **{"ciscoMdiMetricsMIB": ciscoMdiMetricsMIB,
       "ciscoMdiMetricsMIBNotifs": ciscoMdiMetricsMIBNotifs,
       "ciscoMdiMetricsMIBObjects": ciscoMdiMetricsMIBObjects,
       "cfmMdiMetrics": cfmMdiMetrics,
       "cfmMdiMetricsTable": cfmMdiMetricsTable,
       "cfmMdiMetricsEntry": cfmMdiMetricsEntry,
       "cfmMdiMetricsCfgRateType": cfmMdiMetricsCfgRateType,
       "cfmMdiMetricsCfgBitRate": cfmMdiMetricsCfgBitRate,
       "cfmMdiMetricsCfgRate": cfmMdiMetricsCfgRate,
       "cfmMdiMetricsCfgMediaPktSize": cfmMdiMetricsCfgMediaPktSize,
       "cfmMdiMetricsValid": cfmMdiMetricsValid,
       "cfmMdiMetricsLostPkts": cfmMdiMetricsLostPkts,
       "cfmMdiMetricsMlrScale": cfmMdiMetricsMlrScale,
       "cfmMdiMetricsMlrPrecision": cfmMdiMetricsMlrPrecision,
       "cfmMdiMetricsMlr": cfmMdiMetricsMlr,
       "cfmMdiMetricsMdc": cfmMdiMetricsMdc,
       "cfmMdiMetricsTableChanged": cfmMdiMetricsTableChanged,
       "cfmMdiMetricsIntTable": cfmMdiMetricsIntTable,
       "cfmMdiMetricsIntEntry": cfmMdiMetricsIntEntry,
       "cfmMdiMetricsIntValid": cfmMdiMetricsIntValid,
       "cfmMdiMetricsIntLostPkts": cfmMdiMetricsIntLostPkts,
       "cfmMdiMetricsIntVbMin": cfmMdiMetricsIntVbMin,
       "cfmMdiMetricsIntVbMax": cfmMdiMetricsIntVbMax,
       "cfmMdiMetricsIntMrUnits": cfmMdiMetricsIntMrUnits,
       "cfmMdiMetricsIntMr": cfmMdiMetricsIntMr,
       "cfmMdiMetricsIntDfScale": cfmMdiMetricsIntDfScale,
       "cfmMdiMetricsIntDfPrecision": cfmMdiMetricsIntDfPrecision,
       "cfmMdiMetricsIntDf": cfmMdiMetricsIntDf,
       "cfmMdiMetricsIntMlrScale": cfmMdiMetricsIntMlrScale,
       "cfmMdiMetricsIntMlrPrecision": cfmMdiMetricsIntMlrPrecision,
       "cfmMdiMetricsIntMlr": cfmMdiMetricsIntMlr,
       "cfmMdiMetricsIntMdc": cfmMdiMetricsIntMdc,
       "ciscoMdiMetricsMIBConform": ciscoMdiMetricsMIBConform,
       "ciscoMdiMetricsMIBCompliances": ciscoMdiMetricsMIBCompliances,
       "ciscoMdiMetricsCompliance01": ciscoMdiMetricsCompliance01,
       "ciscoMdiMetricsMIBGroups": ciscoMdiMetricsMIBGroups,
       "cfmMdiMetricsGroup": cfmMdiMetricsGroup,
       "ciscoMdiMetricsMIBIds": ciscoMdiMetricsMIBIds,
       "cfmMdiMonitoredElements": cfmMdiMonitoredElements,
       "cfmeMdiCumulativeLostPkts": cfmeMdiCumulativeLostPkts,
       "cfmeMdiCumulativeMlr": cfmeMdiCumulativeMlr,
       "cfmeMdiCumulativeMdc": cfmeMdiCumulativeMdc,
       "cfmeMdiLostPkts": cfmeMdiLostPkts,
       "cfmeMdiDf": cfmeMdiDf,
       "cfmeMdiMlr": cfmeMdiMlr,
       "cfmeMdiMdc": cfmeMdiMdc}
)
