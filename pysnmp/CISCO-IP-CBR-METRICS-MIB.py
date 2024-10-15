# SNMP MIB module (CISCO-IP-CBR-METRICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-CBR-METRICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:35 2024
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

ciscoIpCbrMetricsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697)
)
ciscoIpCbrMetricsMIB.setRevisions(
        ("2009-06-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIpCbrMetricsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpCbrMetricsMIBNotifs = _CiscoIpCbrMetricsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 0)
)
_CiscoIpCbrMetricsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpCbrMetricsMIBObjects = _CiscoIpCbrMetricsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1)
)
_CfmIpCbrMetrics_ObjectIdentity = ObjectIdentity
cfmIpCbrMetrics = _CfmIpCbrMetrics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1)
)
_CfmIpCbrMetricsTable_Object = MibTable
cfmIpCbrMetricsTable = _CfmIpCbrMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfmIpCbrMetricsTable.setStatus("current")
_CfmIpCbrMetricsEntry_Object = MibTableRow
cfmIpCbrMetricsEntry = _CfmIpCbrMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 1, 1)
)
cfmIpCbrMetricsEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
)
if mibBuilder.loadTexts:
    cfmIpCbrMetricsEntry.setStatus("current")
_CfmIpCbrMetricsCfgRateType_Type = FlowCfgRateType
_CfmIpCbrMetricsCfgRateType_Object = MibTableColumn
cfmIpCbrMetricsCfgRateType = _CfmIpCbrMetricsCfgRateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 1, 1, 1),
    _CfmIpCbrMetricsCfgRateType_Type()
)
cfmIpCbrMetricsCfgRateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsCfgRateType.setStatus("current")
_CfmIpCbrMetricsCfgBitRate_Type = FlowBitRateUnits
_CfmIpCbrMetricsCfgBitRate_Object = MibTableColumn
cfmIpCbrMetricsCfgBitRate = _CfmIpCbrMetricsCfgBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 1, 1, 2),
    _CfmIpCbrMetricsCfgBitRate_Type()
)
cfmIpCbrMetricsCfgBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsCfgBitRate.setStatus("current")


class _CfmIpCbrMetricsCfgRate_Type(Unsigned32):
    """Custom type cfmIpCbrMetricsCfgRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CfmIpCbrMetricsCfgRate_Type.__name__ = "Unsigned32"
_CfmIpCbrMetricsCfgRate_Object = MibTableColumn
cfmIpCbrMetricsCfgRate = _CfmIpCbrMetricsCfgRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 1, 1, 3),
    _CfmIpCbrMetricsCfgRate_Type()
)
cfmIpCbrMetricsCfgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsCfgRate.setStatus("current")


class _CfmIpCbrMetricsCfgMediaPktSize_Type(Unsigned32):
    """Custom type cfmIpCbrMetricsCfgMediaPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 65535),
    )


_CfmIpCbrMetricsCfgMediaPktSize_Type.__name__ = "Unsigned32"
_CfmIpCbrMetricsCfgMediaPktSize_Object = MibTableColumn
cfmIpCbrMetricsCfgMediaPktSize = _CfmIpCbrMetricsCfgMediaPktSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 1, 1, 4),
    _CfmIpCbrMetricsCfgMediaPktSize_Type()
)
cfmIpCbrMetricsCfgMediaPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsCfgMediaPktSize.setStatus("current")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsCfgMediaPktSize.setUnits("octets")


class _CfmIpCbrMetricsValid_Type(Bits):
    """Custom type cfmIpCbrMetricsValid based on Bits"""
    namedValues = NamedValues(
        *(("lostPkts", 0),
          ("mediaRateVariation", 1))
    )

_CfmIpCbrMetricsValid_Type.__name__ = "Bits"
_CfmIpCbrMetricsValid_Object = MibTableColumn
cfmIpCbrMetricsValid = _CfmIpCbrMetricsValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 1, 1, 5),
    _CfmIpCbrMetricsValid_Type()
)
cfmIpCbrMetricsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsValid.setStatus("current")
_CfmIpCbrMetricsLostPkts_Type = Counter64
_CfmIpCbrMetricsLostPkts_Object = MibTableColumn
cfmIpCbrMetricsLostPkts = _CfmIpCbrMetricsLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 1, 1, 6),
    _CfmIpCbrMetricsLostPkts_Type()
)
cfmIpCbrMetricsLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsLostPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsLostPkts.setUnits("packets")
_CfmIpCbrMetricsMrvScale_Type = FlowMetricScale
_CfmIpCbrMetricsMrvScale_Object = MibTableColumn
cfmIpCbrMetricsMrvScale = _CfmIpCbrMetricsMrvScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 1, 1, 7),
    _CfmIpCbrMetricsMrvScale_Type()
)
cfmIpCbrMetricsMrvScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsMrvScale.setStatus("current")
_CfmIpCbrMetricsMrvPrecision_Type = FlowMetricPrecision
_CfmIpCbrMetricsMrvPrecision_Object = MibTableColumn
cfmIpCbrMetricsMrvPrecision = _CfmIpCbrMetricsMrvPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 1, 1, 8),
    _CfmIpCbrMetricsMrvPrecision_Type()
)
cfmIpCbrMetricsMrvPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsMrvPrecision.setStatus("current")
_CfmIpCbrMetricsMrv_Type = FlowMetricValue
_CfmIpCbrMetricsMrv_Object = MibTableColumn
cfmIpCbrMetricsMrv = _CfmIpCbrMetricsMrv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 1, 1, 9),
    _CfmIpCbrMetricsMrv_Type()
)
cfmIpCbrMetricsMrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsMrv.setStatus("current")
_CfmIpCbrMetricsTableChanged_Type = TimeStamp
_CfmIpCbrMetricsTableChanged_Object = MibScalar
cfmIpCbrMetricsTableChanged = _CfmIpCbrMetricsTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 2),
    _CfmIpCbrMetricsTableChanged_Type()
)
cfmIpCbrMetricsTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsTableChanged.setStatus("current")
_CfmIpCbrMetricsIntTable_Object = MibTable
cfmIpCbrMetricsIntTable = _CfmIpCbrMetricsIntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntTable.setStatus("current")
_CfmIpCbrMetricsIntEntry_Object = MibTableRow
cfmIpCbrMetricsIntEntry = _CfmIpCbrMetricsIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1)
)
cfmIpCbrMetricsIntEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntNumber"),
)
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntEntry.setStatus("current")


class _CfmIpCbrMetricsIntValid_Type(Bits):
    """Custom type cfmIpCbrMetricsIntValid based on Bits"""
    namedValues = NamedValues(
        *(("delayFactor", 4),
          ("lostPkts", 0),
          ("mediaRate", 3),
          ("mediaRateVariation", 5),
          ("vbMax", 2),
          ("vbMin", 1))
    )

_CfmIpCbrMetricsIntValid_Type.__name__ = "Bits"
_CfmIpCbrMetricsIntValid_Object = MibTableColumn
cfmIpCbrMetricsIntValid = _CfmIpCbrMetricsIntValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1, 1),
    _CfmIpCbrMetricsIntValid_Type()
)
cfmIpCbrMetricsIntValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntValid.setStatus("current")
_CfmIpCbrMetricsIntLostPkts_Type = ReportIntervalCount
_CfmIpCbrMetricsIntLostPkts_Object = MibTableColumn
cfmIpCbrMetricsIntLostPkts = _CfmIpCbrMetricsIntLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1, 2),
    _CfmIpCbrMetricsIntLostPkts_Type()
)
cfmIpCbrMetricsIntLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntLostPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntLostPkts.setUnits("packets")
_CfmIpCbrMetricsIntVbMin_Type = ReportIntervalCount
_CfmIpCbrMetricsIntVbMin_Object = MibTableColumn
cfmIpCbrMetricsIntVbMin = _CfmIpCbrMetricsIntVbMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1, 3),
    _CfmIpCbrMetricsIntVbMin_Type()
)
cfmIpCbrMetricsIntVbMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntVbMin.setStatus("current")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntVbMin.setUnits("bytes")
_CfmIpCbrMetricsIntVbMax_Type = ReportIntervalCount
_CfmIpCbrMetricsIntVbMax_Object = MibTableColumn
cfmIpCbrMetricsIntVbMax = _CfmIpCbrMetricsIntVbMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1, 4),
    _CfmIpCbrMetricsIntVbMax_Type()
)
cfmIpCbrMetricsIntVbMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntVbMax.setStatus("current")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntVbMax.setUnits("bytes")
_CfmIpCbrMetricsIntMrUnits_Type = FlowBitRateUnits
_CfmIpCbrMetricsIntMrUnits_Object = MibTableColumn
cfmIpCbrMetricsIntMrUnits = _CfmIpCbrMetricsIntMrUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1, 5),
    _CfmIpCbrMetricsIntMrUnits_Type()
)
cfmIpCbrMetricsIntMrUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntMrUnits.setStatus("current")
_CfmIpCbrMetricsIntMr_Type = ReportIntervalCount
_CfmIpCbrMetricsIntMr_Object = MibTableColumn
cfmIpCbrMetricsIntMr = _CfmIpCbrMetricsIntMr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1, 6),
    _CfmIpCbrMetricsIntMr_Type()
)
cfmIpCbrMetricsIntMr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntMr.setStatus("current")
_CfmIpCbrMetricsIntDfScale_Type = FlowMetricScale
_CfmIpCbrMetricsIntDfScale_Object = MibTableColumn
cfmIpCbrMetricsIntDfScale = _CfmIpCbrMetricsIntDfScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1, 7),
    _CfmIpCbrMetricsIntDfScale_Type()
)
cfmIpCbrMetricsIntDfScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntDfScale.setStatus("current")
_CfmIpCbrMetricsIntDfPrecision_Type = FlowMetricPrecision
_CfmIpCbrMetricsIntDfPrecision_Object = MibTableColumn
cfmIpCbrMetricsIntDfPrecision = _CfmIpCbrMetricsIntDfPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1, 8),
    _CfmIpCbrMetricsIntDfPrecision_Type()
)
cfmIpCbrMetricsIntDfPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntDfPrecision.setStatus("current")
_CfmIpCbrMetricsIntDf_Type = FlowMetricValue
_CfmIpCbrMetricsIntDf_Object = MibTableColumn
cfmIpCbrMetricsIntDf = _CfmIpCbrMetricsIntDf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1, 9),
    _CfmIpCbrMetricsIntDf_Type()
)
cfmIpCbrMetricsIntDf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntDf.setStatus("current")
_CfmIpCbrMetricsIntMrvScale_Type = FlowMetricScale
_CfmIpCbrMetricsIntMrvScale_Object = MibTableColumn
cfmIpCbrMetricsIntMrvScale = _CfmIpCbrMetricsIntMrvScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1, 10),
    _CfmIpCbrMetricsIntMrvScale_Type()
)
cfmIpCbrMetricsIntMrvScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntMrvScale.setStatus("current")
_CfmIpCbrMetricsIntMrvPrecision_Type = FlowMetricPrecision
_CfmIpCbrMetricsIntMrvPrecision_Object = MibTableColumn
cfmIpCbrMetricsIntMrvPrecision = _CfmIpCbrMetricsIntMrvPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1, 11),
    _CfmIpCbrMetricsIntMrvPrecision_Type()
)
cfmIpCbrMetricsIntMrvPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntMrvPrecision.setStatus("current")
_CfmIpCbrMetricsIntMrv_Type = FlowMetricValue
_CfmIpCbrMetricsIntMrv_Object = MibTableColumn
cfmIpCbrMetricsIntMrv = _CfmIpCbrMetricsIntMrv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 1, 1, 3, 1, 12),
    _CfmIpCbrMetricsIntMrv_Type()
)
cfmIpCbrMetricsIntMrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmIpCbrMetricsIntMrv.setStatus("current")
_CiscoIpCbrMetricsMIBConform_ObjectIdentity = ObjectIdentity
ciscoIpCbrMetricsMIBConform = _CiscoIpCbrMetricsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 2)
)
_CiscoIpCbrMetricsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIpCbrMetricsMIBCompliances = _CiscoIpCbrMetricsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 2, 1)
)
_CiscoIpCbrMetricsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpCbrMetricsMIBGroups = _CiscoIpCbrMetricsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 2, 2)
)
_CiscoIpCbrMetricsMIBIds_ObjectIdentity = ObjectIdentity
ciscoIpCbrMetricsMIBIds = _CiscoIpCbrMetricsMIBIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 3)
)
_CfmIpCbrMonitoredElements_ObjectIdentity = ObjectIdentity
cfmIpCbrMonitoredElements = _CfmIpCbrMonitoredElements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 3, 1)
)
_CfmeIpCbrCumulativeLostPkts_ObjectIdentity = ObjectIdentity
cfmeIpCbrCumulativeLostPkts = _CfmeIpCbrCumulativeLostPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cfmeIpCbrCumulativeLostPkts.setStatus("current")
_CfmeIpCbrCumulativeMrv_ObjectIdentity = ObjectIdentity
cfmeIpCbrCumulativeMrv = _CfmeIpCbrCumulativeMrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cfmeIpCbrCumulativeMrv.setStatus("current")
_CfmeIpCbrLostPkts_ObjectIdentity = ObjectIdentity
cfmeIpCbrLostPkts = _CfmeIpCbrLostPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cfmeIpCbrLostPkts.setStatus("current")
_CfmeIpCbrDf_ObjectIdentity = ObjectIdentity
cfmeIpCbrDf = _CfmeIpCbrDf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cfmeIpCbrDf.setStatus("current")
_CfmeIpCbrMrv_ObjectIdentity = ObjectIdentity
cfmeIpCbrMrv = _CfmeIpCbrMrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cfmeIpCbrMrv.setStatus("current")

# Managed Objects groups

cfmIpCbrMetricsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 2, 2, 1)
)
cfmIpCbrMetricsGroup.setObjects(
      *(("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsCfgRateType"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsCfgBitRate"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsCfgRate"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsCfgMediaPktSize"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsValid"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsLostPkts"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsMrvScale"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsMrvPrecision"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsMrv"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsTableChanged"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsIntValid"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsIntLostPkts"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsIntVbMin"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsIntVbMax"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsIntMrUnits"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsIntMr"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsIntDfScale"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsIntDfPrecision"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsIntDf"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsIntMrvScale"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsIntMrvPrecision"),
        ("CISCO-IP-CBR-METRICS-MIB", "cfmIpCbrMetricsIntMrv"))
)
if mibBuilder.loadTexts:
    cfmIpCbrMetricsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIpCbrMetricsCompliance01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 697, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpCbrMetricsCompliance01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-CBR-METRICS-MIB",
    **{"ciscoIpCbrMetricsMIB": ciscoIpCbrMetricsMIB,
       "ciscoIpCbrMetricsMIBNotifs": ciscoIpCbrMetricsMIBNotifs,
       "ciscoIpCbrMetricsMIBObjects": ciscoIpCbrMetricsMIBObjects,
       "cfmIpCbrMetrics": cfmIpCbrMetrics,
       "cfmIpCbrMetricsTable": cfmIpCbrMetricsTable,
       "cfmIpCbrMetricsEntry": cfmIpCbrMetricsEntry,
       "cfmIpCbrMetricsCfgRateType": cfmIpCbrMetricsCfgRateType,
       "cfmIpCbrMetricsCfgBitRate": cfmIpCbrMetricsCfgBitRate,
       "cfmIpCbrMetricsCfgRate": cfmIpCbrMetricsCfgRate,
       "cfmIpCbrMetricsCfgMediaPktSize": cfmIpCbrMetricsCfgMediaPktSize,
       "cfmIpCbrMetricsValid": cfmIpCbrMetricsValid,
       "cfmIpCbrMetricsLostPkts": cfmIpCbrMetricsLostPkts,
       "cfmIpCbrMetricsMrvScale": cfmIpCbrMetricsMrvScale,
       "cfmIpCbrMetricsMrvPrecision": cfmIpCbrMetricsMrvPrecision,
       "cfmIpCbrMetricsMrv": cfmIpCbrMetricsMrv,
       "cfmIpCbrMetricsTableChanged": cfmIpCbrMetricsTableChanged,
       "cfmIpCbrMetricsIntTable": cfmIpCbrMetricsIntTable,
       "cfmIpCbrMetricsIntEntry": cfmIpCbrMetricsIntEntry,
       "cfmIpCbrMetricsIntValid": cfmIpCbrMetricsIntValid,
       "cfmIpCbrMetricsIntLostPkts": cfmIpCbrMetricsIntLostPkts,
       "cfmIpCbrMetricsIntVbMin": cfmIpCbrMetricsIntVbMin,
       "cfmIpCbrMetricsIntVbMax": cfmIpCbrMetricsIntVbMax,
       "cfmIpCbrMetricsIntMrUnits": cfmIpCbrMetricsIntMrUnits,
       "cfmIpCbrMetricsIntMr": cfmIpCbrMetricsIntMr,
       "cfmIpCbrMetricsIntDfScale": cfmIpCbrMetricsIntDfScale,
       "cfmIpCbrMetricsIntDfPrecision": cfmIpCbrMetricsIntDfPrecision,
       "cfmIpCbrMetricsIntDf": cfmIpCbrMetricsIntDf,
       "cfmIpCbrMetricsIntMrvScale": cfmIpCbrMetricsIntMrvScale,
       "cfmIpCbrMetricsIntMrvPrecision": cfmIpCbrMetricsIntMrvPrecision,
       "cfmIpCbrMetricsIntMrv": cfmIpCbrMetricsIntMrv,
       "ciscoIpCbrMetricsMIBConform": ciscoIpCbrMetricsMIBConform,
       "ciscoIpCbrMetricsMIBCompliances": ciscoIpCbrMetricsMIBCompliances,
       "ciscoIpCbrMetricsCompliance01": ciscoIpCbrMetricsCompliance01,
       "ciscoIpCbrMetricsMIBGroups": ciscoIpCbrMetricsMIBGroups,
       "cfmIpCbrMetricsGroup": cfmIpCbrMetricsGroup,
       "ciscoIpCbrMetricsMIBIds": ciscoIpCbrMetricsMIBIds,
       "cfmIpCbrMonitoredElements": cfmIpCbrMonitoredElements,
       "cfmeIpCbrCumulativeLostPkts": cfmeIpCbrCumulativeLostPkts,
       "cfmeIpCbrCumulativeMrv": cfmeIpCbrCumulativeMrv,
       "cfmeIpCbrLostPkts": cfmeIpCbrLostPkts,
       "cfmeIpCbrDf": cfmeIpCbrDf,
       "cfmeIpCbrMrv": cfmeIpCbrMrv}
)
