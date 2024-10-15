# SNMP MIB module (CISCO-TCP-METRICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TCP-METRICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:33 2024
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

ciscoTcpMetricsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 770)
)
ciscoTcpMetricsMIB.setRevisions(
        ("2011-03-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoTcpMetricsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoTcpMetricsMIBNotifs = _CiscoTcpMetricsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 0)
)
_CiscoTcpMetricsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTcpMetricsMIBObjects = _CiscoTcpMetricsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1)
)
_CfmTcpMetrics_ObjectIdentity = ObjectIdentity
cfmTcpMetrics = _CfmTcpMetrics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1)
)
_CfmTcpMetricsTable_Object = MibTable
cfmTcpMetricsTable = _CfmTcpMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfmTcpMetricsTable.setStatus("current")
_CfmTcpMetricsEntry_Object = MibTableRow
cfmTcpMetricsEntry = _CfmTcpMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 1, 1)
)
cfmTcpMetricsEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
)
if mibBuilder.loadTexts:
    cfmTcpMetricsEntry.setStatus("current")


class _CfmTcpMetricsValid_Type(Bits):
    """Custom type cfmTcpMetricsValid based on Bits"""
    namedValues = NamedValues(
        ("roundTripTime", 0)
    )

_CfmTcpMetricsValid_Type.__name__ = "Bits"
_CfmTcpMetricsValid_Object = MibTableColumn
cfmTcpMetricsValid = _CfmTcpMetricsValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 1, 1, 1),
    _CfmTcpMetricsValid_Type()
)
cfmTcpMetricsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmTcpMetricsValid.setStatus("current")
_CfmTcpMetricsRoundTripTimeScale_Type = FlowMetricScale
_CfmTcpMetricsRoundTripTimeScale_Object = MibTableColumn
cfmTcpMetricsRoundTripTimeScale = _CfmTcpMetricsRoundTripTimeScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 1, 1, 2),
    _CfmTcpMetricsRoundTripTimeScale_Type()
)
cfmTcpMetricsRoundTripTimeScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmTcpMetricsRoundTripTimeScale.setStatus("current")
_CfmTcpMetricsRoundTripTimePrecision_Type = FlowMetricPrecision
_CfmTcpMetricsRoundTripTimePrecision_Object = MibTableColumn
cfmTcpMetricsRoundTripTimePrecision = _CfmTcpMetricsRoundTripTimePrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 1, 1, 3),
    _CfmTcpMetricsRoundTripTimePrecision_Type()
)
cfmTcpMetricsRoundTripTimePrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmTcpMetricsRoundTripTimePrecision.setStatus("current")
_CfmTcpMetricsRoundTripTime_Type = FlowMetricValue
_CfmTcpMetricsRoundTripTime_Object = MibTableColumn
cfmTcpMetricsRoundTripTime = _CfmTcpMetricsRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 1, 1, 4),
    _CfmTcpMetricsRoundTripTime_Type()
)
cfmTcpMetricsRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmTcpMetricsRoundTripTime.setStatus("current")
_CfmTcpMetricsTableChanged_Type = TimeStamp
_CfmTcpMetricsTableChanged_Object = MibScalar
cfmTcpMetricsTableChanged = _CfmTcpMetricsTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 2),
    _CfmTcpMetricsTableChanged_Type()
)
cfmTcpMetricsTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmTcpMetricsTableChanged.setStatus("current")
_CfmTcpMetricsIntTable_Object = MibTable
cfmTcpMetricsIntTable = _CfmTcpMetricsIntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfmTcpMetricsIntTable.setStatus("current")
_CfmTcpMetricsIntEntry_Object = MibTableRow
cfmTcpMetricsIntEntry = _CfmTcpMetricsIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 3, 1)
)
cfmTcpMetricsIntEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntNumber"),
)
if mibBuilder.loadTexts:
    cfmTcpMetricsIntEntry.setStatus("current")


class _CfmTcpMetricsIntValid_Type(Bits):
    """Custom type cfmTcpMetricsIntValid based on Bits"""
    namedValues = NamedValues(
        ("roundTripTime", 0)
    )

_CfmTcpMetricsIntValid_Type.__name__ = "Bits"
_CfmTcpMetricsIntValid_Object = MibTableColumn
cfmTcpMetricsIntValid = _CfmTcpMetricsIntValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 3, 1, 1),
    _CfmTcpMetricsIntValid_Type()
)
cfmTcpMetricsIntValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmTcpMetricsIntValid.setStatus("current")
_CfmTcpMetricsIntRoundTripTimeScale_Type = FlowMetricScale
_CfmTcpMetricsIntRoundTripTimeScale_Object = MibTableColumn
cfmTcpMetricsIntRoundTripTimeScale = _CfmTcpMetricsIntRoundTripTimeScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 3, 1, 2),
    _CfmTcpMetricsIntRoundTripTimeScale_Type()
)
cfmTcpMetricsIntRoundTripTimeScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmTcpMetricsIntRoundTripTimeScale.setStatus("current")
_CfmTcpMetricsIntRoundTripTimePrecision_Type = FlowMetricPrecision
_CfmTcpMetricsIntRoundTripTimePrecision_Object = MibTableColumn
cfmTcpMetricsIntRoundTripTimePrecision = _CfmTcpMetricsIntRoundTripTimePrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 3, 1, 3),
    _CfmTcpMetricsIntRoundTripTimePrecision_Type()
)
cfmTcpMetricsIntRoundTripTimePrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmTcpMetricsIntRoundTripTimePrecision.setStatus("current")
_CfmTcpMetricsIntRoundTripTime_Type = FlowMetricValue
_CfmTcpMetricsIntRoundTripTime_Object = MibTableColumn
cfmTcpMetricsIntRoundTripTime = _CfmTcpMetricsIntRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 1, 1, 3, 1, 4),
    _CfmTcpMetricsIntRoundTripTime_Type()
)
cfmTcpMetricsIntRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmTcpMetricsIntRoundTripTime.setStatus("current")
_CiscoTcpMetricsMIBConform_ObjectIdentity = ObjectIdentity
ciscoTcpMetricsMIBConform = _CiscoTcpMetricsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 2)
)
_CiscoTcpMetricsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTcpMetricsMIBCompliances = _CiscoTcpMetricsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 2, 1)
)
_CiscoTcpMetricsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTcpMetricsMIBGroups = _CiscoTcpMetricsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 2, 2)
)
_CiscoTcpMetricsMIBIds_ObjectIdentity = ObjectIdentity
ciscoTcpMetricsMIBIds = _CiscoTcpMetricsMIBIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 3)
)

# Managed Objects groups

ciscoTcpMetricsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 2, 2, 1)
)
ciscoTcpMetricsGroup.setObjects(
      *(("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsValid"),
        ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsRoundTripTimeScale"),
        ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsRoundTripTimePrecision"),
        ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsRoundTripTime"),
        ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsTableChanged"),
        ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsIntValid"),
        ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsIntRoundTripTimeScale"),
        ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsIntRoundTripTimePrecision"),
        ("CISCO-TCP-METRICS-MIB", "cfmTcpMetricsIntRoundTripTime"))
)
if mibBuilder.loadTexts:
    ciscoTcpMetricsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoTcpMetricsMIBCompliance01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 770, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTcpMetricsMIBCompliance01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TCP-METRICS-MIB",
    **{"ciscoTcpMetricsMIB": ciscoTcpMetricsMIB,
       "ciscoTcpMetricsMIBNotifs": ciscoTcpMetricsMIBNotifs,
       "ciscoTcpMetricsMIBObjects": ciscoTcpMetricsMIBObjects,
       "cfmTcpMetrics": cfmTcpMetrics,
       "cfmTcpMetricsTable": cfmTcpMetricsTable,
       "cfmTcpMetricsEntry": cfmTcpMetricsEntry,
       "cfmTcpMetricsValid": cfmTcpMetricsValid,
       "cfmTcpMetricsRoundTripTimeScale": cfmTcpMetricsRoundTripTimeScale,
       "cfmTcpMetricsRoundTripTimePrecision": cfmTcpMetricsRoundTripTimePrecision,
       "cfmTcpMetricsRoundTripTime": cfmTcpMetricsRoundTripTime,
       "cfmTcpMetricsTableChanged": cfmTcpMetricsTableChanged,
       "cfmTcpMetricsIntTable": cfmTcpMetricsIntTable,
       "cfmTcpMetricsIntEntry": cfmTcpMetricsIntEntry,
       "cfmTcpMetricsIntValid": cfmTcpMetricsIntValid,
       "cfmTcpMetricsIntRoundTripTimeScale": cfmTcpMetricsIntRoundTripTimeScale,
       "cfmTcpMetricsIntRoundTripTimePrecision": cfmTcpMetricsIntRoundTripTimePrecision,
       "cfmTcpMetricsIntRoundTripTime": cfmTcpMetricsIntRoundTripTime,
       "ciscoTcpMetricsMIBConform": ciscoTcpMetricsMIBConform,
       "ciscoTcpMetricsMIBCompliances": ciscoTcpMetricsMIBCompliances,
       "ciscoTcpMetricsMIBCompliance01": ciscoTcpMetricsMIBCompliance01,
       "ciscoTcpMetricsMIBGroups": ciscoTcpMetricsMIBGroups,
       "ciscoTcpMetricsGroup": ciscoTcpMetricsGroup,
       "ciscoTcpMetricsMIBIds": ciscoTcpMetricsMIBIds}
)
