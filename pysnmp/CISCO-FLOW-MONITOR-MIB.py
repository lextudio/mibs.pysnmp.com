# SNMP MIB module (CISCO-FLOW-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FLOW-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:41 2024
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

(FlowBitRateUnits,
 FlowIdentifier,
 FlowMetricPrecision,
 FlowMetricScale,
 FlowMetricValue,
 FlowMetrics,
 FlowMonitorAlarmGroupIdentifier,
 FlowMonitorConditionIdentifier,
 FlowMonitorConditions,
 FlowMonitorConditionsProfile,
 FlowMonitorConditionsProfileOrZero,
 FlowMonitorIdentifier,
 FlowPointIdentifier,
 FlowPointType,
 FlowSetIdentifier) = mibBuilder.importSymbols(
    "CISCO-FLOW-MONITOR-TC-MIB",
    "FlowBitRateUnits",
    "FlowIdentifier",
    "FlowMetricPrecision",
    "FlowMetricScale",
    "FlowMetricValue",
    "FlowMetrics",
    "FlowMonitorAlarmGroupIdentifier",
    "FlowMonitorConditionIdentifier",
    "FlowMonitorConditions",
    "FlowMonitorConditionsProfile",
    "FlowMonitorConditionsProfileOrZero",
    "FlowMonitorIdentifier",
    "FlowPointIdentifier",
    "FlowPointType",
    "FlowSetIdentifier")

(ReportIntervalCount,) = mibBuilder.importSymbols(
    "CISCO-REPORT-INTERVAL-TC-MIB",
    "ReportIntervalCount")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 Layer2Cos) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "Layer2Cos")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

(AutonomousType,
 DisplayString,
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoFlowMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692)
)
ciscoFlowMonitorMIB.setRevisions(
        ("2009-04-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFlowMonitorMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFlowMonitorMIBNotifs = _CiscoFlowMonitorMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 0)
)
_CiscoFlowMonitorMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFlowMonitorMIBObjects = _CiscoFlowMonitorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1)
)
_CfmFlowMonitors_ObjectIdentity = ObjectIdentity
cfmFlowMonitors = _CfmFlowMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1)
)
_CfmFlowMonitorTable_Object = MibTable
cfmFlowMonitorTable = _CfmFlowMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfmFlowMonitorTable.setStatus("current")
_CfmFlowMonitorEntry_Object = MibTableRow
cfmFlowMonitorEntry = _CfmFlowMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1)
)
cfmFlowMonitorEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
)
if mibBuilder.loadTexts:
    cfmFlowMonitorEntry.setStatus("current")
_CfmFlowMonitorId_Type = FlowMonitorIdentifier
_CfmFlowMonitorId_Object = MibTableColumn
cfmFlowMonitorId = _CfmFlowMonitorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 1),
    _CfmFlowMonitorId_Type()
)
cfmFlowMonitorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmFlowMonitorId.setStatus("current")
_CfmFlowMonitorDescr_Type = SnmpAdminString
_CfmFlowMonitorDescr_Object = MibTableColumn
cfmFlowMonitorDescr = _CfmFlowMonitorDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 2),
    _CfmFlowMonitorDescr_Type()
)
cfmFlowMonitorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorDescr.setStatus("current")
_CfmFlowMonitorCaps_Type = FlowMetrics
_CfmFlowMonitorCaps_Object = MibTableColumn
cfmFlowMonitorCaps = _CfmFlowMonitorCaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 3),
    _CfmFlowMonitorCaps_Type()
)
cfmFlowMonitorCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorCaps.setStatus("current")
_CfmFlowMonitorFlowCount_Type = Gauge32
_CfmFlowMonitorFlowCount_Object = MibTableColumn
cfmFlowMonitorFlowCount = _CfmFlowMonitorFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 4),
    _CfmFlowMonitorFlowCount_Type()
)
cfmFlowMonitorFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorFlowCount.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMonitorFlowCount.setUnits("traffic flows")
_CfmFlowMonitorConditionsProfile_Type = FlowMonitorConditionsProfileOrZero
_CfmFlowMonitorConditionsProfile_Object = MibTableColumn
cfmFlowMonitorConditionsProfile = _CfmFlowMonitorConditionsProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 5),
    _CfmFlowMonitorConditionsProfile_Type()
)
cfmFlowMonitorConditionsProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorConditionsProfile.setStatus("current")
_CfmFlowMonitorConditions_Type = FlowMonitorConditions
_CfmFlowMonitorConditions_Object = MibTableColumn
cfmFlowMonitorConditions = _CfmFlowMonitorConditions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 6),
    _CfmFlowMonitorConditions_Type()
)
cfmFlowMonitorConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorConditions.setStatus("current")
_CfmFlowMonitorAlarms_Type = FlowMonitorConditions
_CfmFlowMonitorAlarms_Object = MibTableColumn
cfmFlowMonitorAlarms = _CfmFlowMonitorAlarms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 7),
    _CfmFlowMonitorAlarms_Type()
)
cfmFlowMonitorAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorAlarms.setStatus("current")
_CfmFlowMonitorAlarmSeverity_Type = CiscoAlarmSeverity
_CfmFlowMonitorAlarmSeverity_Object = MibTableColumn
cfmFlowMonitorAlarmSeverity = _CfmFlowMonitorAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 8),
    _CfmFlowMonitorAlarmSeverity_Type()
)
cfmFlowMonitorAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorAlarmSeverity.setStatus("current")
_CfmFlowMonitorAlarmCriticalCount_Type = Gauge32
_CfmFlowMonitorAlarmCriticalCount_Object = MibTableColumn
cfmFlowMonitorAlarmCriticalCount = _CfmFlowMonitorAlarmCriticalCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 9),
    _CfmFlowMonitorAlarmCriticalCount_Type()
)
cfmFlowMonitorAlarmCriticalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorAlarmCriticalCount.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMonitorAlarmCriticalCount.setUnits("alarms")
_CfmFlowMonitorAlarmMajorCount_Type = Gauge32
_CfmFlowMonitorAlarmMajorCount_Object = MibTableColumn
cfmFlowMonitorAlarmMajorCount = _CfmFlowMonitorAlarmMajorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 10),
    _CfmFlowMonitorAlarmMajorCount_Type()
)
cfmFlowMonitorAlarmMajorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorAlarmMajorCount.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMonitorAlarmMajorCount.setUnits("alarms")
_CfmFlowMonitorAlarmMinorCount_Type = Gauge32
_CfmFlowMonitorAlarmMinorCount_Object = MibTableColumn
cfmFlowMonitorAlarmMinorCount = _CfmFlowMonitorAlarmMinorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 11),
    _CfmFlowMonitorAlarmMinorCount_Type()
)
cfmFlowMonitorAlarmMinorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorAlarmMinorCount.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMonitorAlarmMinorCount.setUnits("alarms")
_CfmFlowMonitorAlarmWarningCount_Type = Gauge32
_CfmFlowMonitorAlarmWarningCount_Object = MibTableColumn
cfmFlowMonitorAlarmWarningCount = _CfmFlowMonitorAlarmWarningCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 12),
    _CfmFlowMonitorAlarmWarningCount_Type()
)
cfmFlowMonitorAlarmWarningCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorAlarmWarningCount.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMonitorAlarmWarningCount.setUnits("alarms")
_CfmFlowMonitorAlarmInfoCount_Type = Gauge32
_CfmFlowMonitorAlarmInfoCount_Object = MibTableColumn
cfmFlowMonitorAlarmInfoCount = _CfmFlowMonitorAlarmInfoCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 1, 1, 13),
    _CfmFlowMonitorAlarmInfoCount_Type()
)
cfmFlowMonitorAlarmInfoCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorAlarmInfoCount.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMonitorAlarmInfoCount.setUnits("alarms")
_CfmFlowMonitorTableChanged_Type = TimeStamp
_CfmFlowMonitorTableChanged_Object = MibScalar
cfmFlowMonitorTableChanged = _CfmFlowMonitorTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 1, 2),
    _CfmFlowMonitorTableChanged_Type()
)
cfmFlowMonitorTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMonitorTableChanged.setStatus("current")
_CfmFlows_ObjectIdentity = ObjectIdentity
cfmFlows = _CfmFlows_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2)
)
_CfmFlowTable_Object = MibTable
cfmFlowTable = _CfmFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfmFlowTable.setStatus("current")
_CfmFlowEntry_Object = MibTableRow
cfmFlowEntry = _CfmFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1)
)
cfmFlowEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
)
if mibBuilder.loadTexts:
    cfmFlowEntry.setStatus("current")
_CfmFlowId_Type = FlowIdentifier
_CfmFlowId_Object = MibTableColumn
cfmFlowId = _CfmFlowId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 1),
    _CfmFlowId_Type()
)
cfmFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmFlowId.setStatus("current")
_CfmFlowDescr_Type = SnmpAdminString
_CfmFlowDescr_Object = MibTableColumn
cfmFlowDescr = _CfmFlowDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 2),
    _CfmFlowDescr_Type()
)
cfmFlowDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowDescr.setStatus("current")
_CfmFlowNext_Type = RowPointer
_CfmFlowNext_Object = MibTableColumn
cfmFlowNext = _CfmFlowNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 3),
    _CfmFlowNext_Type()
)
cfmFlowNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowNext.setStatus("current")
_CfmFlowCreateTime_Type = TimeStamp
_CfmFlowCreateTime_Object = MibTableColumn
cfmFlowCreateTime = _CfmFlowCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 4),
    _CfmFlowCreateTime_Type()
)
cfmFlowCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowCreateTime.setStatus("current")
_CfmFlowDiscontinuityTime_Type = TimeStamp
_CfmFlowDiscontinuityTime_Object = MibTableColumn
cfmFlowDiscontinuityTime = _CfmFlowDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 5),
    _CfmFlowDiscontinuityTime_Type()
)
cfmFlowDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowDiscontinuityTime.setStatus("current")


class _CfmFlowExpirationTime_Type(Unsigned32):
    """Custom type cfmFlowExpirationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CfmFlowExpirationTime_Type.__name__ = "Unsigned32"
_CfmFlowExpirationTime_Object = MibTableColumn
cfmFlowExpirationTime = _CfmFlowExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 6),
    _CfmFlowExpirationTime_Type()
)
cfmFlowExpirationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowExpirationTime.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowExpirationTime.setUnits("seconds")


class _CfmFlowDirection_Type(Integer32):
    """Custom type cfmFlowDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egress", 3),
          ("ingress", 2),
          ("unknown", 1))
    )


_CfmFlowDirection_Type.__name__ = "Integer32"
_CfmFlowDirection_Object = MibTableColumn
cfmFlowDirection = _CfmFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 7),
    _CfmFlowDirection_Type()
)
cfmFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowDirection.setStatus("current")


class _CfmFlowAdminStatus_Type(Integer32):
    """Custom type cfmFlowAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("expire", 3))
    )


_CfmFlowAdminStatus_Type.__name__ = "Integer32"
_CfmFlowAdminStatus_Object = MibTableColumn
cfmFlowAdminStatus = _CfmFlowAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 8),
    _CfmFlowAdminStatus_Type()
)
cfmFlowAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmFlowAdminStatus.setStatus("current")


class _CfmFlowOperStatus_Type(Integer32):
    """Custom type cfmFlowOperStatus based on Integer32"""
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


_CfmFlowOperStatus_Type.__name__ = "Integer32"
_CfmFlowOperStatus_Object = MibTableColumn
cfmFlowOperStatus = _CfmFlowOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 9),
    _CfmFlowOperStatus_Type()
)
cfmFlowOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowOperStatus.setStatus("current")
_CfmFlowIngressType_Type = FlowPointType
_CfmFlowIngressType_Object = MibTableColumn
cfmFlowIngressType = _CfmFlowIngressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 10),
    _CfmFlowIngressType_Type()
)
cfmFlowIngressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowIngressType.setStatus("current")
_CfmFlowIngress_Type = FlowPointIdentifier
_CfmFlowIngress_Object = MibTableColumn
cfmFlowIngress = _CfmFlowIngress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 11),
    _CfmFlowIngress_Type()
)
cfmFlowIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowIngress.setStatus("current")
_CfmFlowEgressType_Type = FlowPointType
_CfmFlowEgressType_Object = MibTableColumn
cfmFlowEgressType = _CfmFlowEgressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 12),
    _CfmFlowEgressType_Type()
)
cfmFlowEgressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowEgressType.setStatus("current")
_CfmFlowEgress_Type = FlowPointIdentifier
_CfmFlowEgress_Object = MibTableColumn
cfmFlowEgress = _CfmFlowEgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 1, 1, 13),
    _CfmFlowEgress_Type()
)
cfmFlowEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowEgress.setStatus("current")
_CfmFlowTableChanged_Type = TimeStamp
_CfmFlowTableChanged_Object = MibScalar
cfmFlowTableChanged = _CfmFlowTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 2),
    _CfmFlowTableChanged_Type()
)
cfmFlowTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowTableChanged.setStatus("current")
_CfmFlowL2VlanTable_Object = MibTable
cfmFlowL2VlanTable = _CfmFlowL2VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cfmFlowL2VlanTable.setStatus("current")
_CfmFlowL2VlanEntry_Object = MibTableRow
cfmFlowL2VlanEntry = _CfmFlowL2VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 3, 1)
)
cfmFlowL2VlanEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
)
if mibBuilder.loadTexts:
    cfmFlowL2VlanEntry.setStatus("current")
_CfmFlowL2VlanNext_Type = RowPointer
_CfmFlowL2VlanNext_Object = MibTableColumn
cfmFlowL2VlanNext = _CfmFlowL2VlanNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 3, 1, 1),
    _CfmFlowL2VlanNext_Type()
)
cfmFlowL2VlanNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowL2VlanNext.setStatus("current")
_CfmFlowL2VlanId_Type = VlanId
_CfmFlowL2VlanId_Object = MibTableColumn
cfmFlowL2VlanId = _CfmFlowL2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 3, 1, 2),
    _CfmFlowL2VlanId_Type()
)
cfmFlowL2VlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowL2VlanId.setStatus("current")
_CfmFlowL2VlanCos_Type = Layer2Cos
_CfmFlowL2VlanCos_Object = MibTableColumn
cfmFlowL2VlanCos = _CfmFlowL2VlanCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 3, 1, 3),
    _CfmFlowL2VlanCos_Type()
)
cfmFlowL2VlanCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowL2VlanCos.setStatus("current")
_CfmFlowL2VlanTableChanged_Type = TimeStamp
_CfmFlowL2VlanTableChanged_Object = MibScalar
cfmFlowL2VlanTableChanged = _CfmFlowL2VlanTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 4),
    _CfmFlowL2VlanTableChanged_Type()
)
cfmFlowL2VlanTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowL2VlanTableChanged.setStatus("current")
_CfmFlowIpTable_Object = MibTable
cfmFlowIpTable = _CfmFlowIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cfmFlowIpTable.setStatus("current")
_CfmFlowIpEntry_Object = MibTableRow
cfmFlowIpEntry = _CfmFlowIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 5, 1)
)
cfmFlowIpEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
)
if mibBuilder.loadTexts:
    cfmFlowIpEntry.setStatus("current")
_CfmFlowIpNext_Type = RowPointer
_CfmFlowIpNext_Object = MibTableColumn
cfmFlowIpNext = _CfmFlowIpNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 5, 1, 1),
    _CfmFlowIpNext_Type()
)
cfmFlowIpNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowIpNext.setStatus("current")
_CfmFlowIpAddrType_Type = InetAddressType
_CfmFlowIpAddrType_Object = MibTableColumn
cfmFlowIpAddrType = _CfmFlowIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 5, 1, 2),
    _CfmFlowIpAddrType_Type()
)
cfmFlowIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowIpAddrType.setStatus("current")
_CfmFlowIpAddrSrc_Type = InetAddress
_CfmFlowIpAddrSrc_Object = MibTableColumn
cfmFlowIpAddrSrc = _CfmFlowIpAddrSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 5, 1, 3),
    _CfmFlowIpAddrSrc_Type()
)
cfmFlowIpAddrSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowIpAddrSrc.setStatus("current")
_CfmFlowIpAddrDst_Type = InetAddress
_CfmFlowIpAddrDst_Object = MibTableColumn
cfmFlowIpAddrDst = _CfmFlowIpAddrDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 5, 1, 4),
    _CfmFlowIpAddrDst_Type()
)
cfmFlowIpAddrDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowIpAddrDst.setStatus("current")


class _CfmFlowIpValid_Type(Bits):
    """Custom type cfmFlowIpValid based on Bits"""
    namedValues = NamedValues(
        *(("hopLimit", 1),
          ("trafficClass", 0))
    )

_CfmFlowIpValid_Type.__name__ = "Bits"
_CfmFlowIpValid_Object = MibTableColumn
cfmFlowIpValid = _CfmFlowIpValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 5, 1, 5),
    _CfmFlowIpValid_Type()
)
cfmFlowIpValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowIpValid.setStatus("current")


class _CfmFlowIpTrafficClass_Type(Unsigned32):
    """Custom type cfmFlowIpTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfmFlowIpTrafficClass_Type.__name__ = "Unsigned32"
_CfmFlowIpTrafficClass_Object = MibTableColumn
cfmFlowIpTrafficClass = _CfmFlowIpTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 5, 1, 6),
    _CfmFlowIpTrafficClass_Type()
)
cfmFlowIpTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowIpTrafficClass.setStatus("current")


class _CfmFlowIpHopLimit_Type(Unsigned32):
    """Custom type cfmFlowIpHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfmFlowIpHopLimit_Type.__name__ = "Unsigned32"
_CfmFlowIpHopLimit_Object = MibTableColumn
cfmFlowIpHopLimit = _CfmFlowIpHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 5, 1, 7),
    _CfmFlowIpHopLimit_Type()
)
cfmFlowIpHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowIpHopLimit.setStatus("current")
_CfmFlowIpTableChanged_Type = TimeStamp
_CfmFlowIpTableChanged_Object = MibScalar
cfmFlowIpTableChanged = _CfmFlowIpTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 6),
    _CfmFlowIpTableChanged_Type()
)
cfmFlowIpTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowIpTableChanged.setStatus("current")
_CfmFlowUdpTable_Object = MibTable
cfmFlowUdpTable = _CfmFlowUdpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cfmFlowUdpTable.setStatus("current")
_CfmFlowUdpEntry_Object = MibTableRow
cfmFlowUdpEntry = _CfmFlowUdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 7, 1)
)
cfmFlowUdpEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
)
if mibBuilder.loadTexts:
    cfmFlowUdpEntry.setStatus("current")
_CfmFlowUdpNext_Type = RowPointer
_CfmFlowUdpNext_Object = MibTableColumn
cfmFlowUdpNext = _CfmFlowUdpNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 7, 1, 1),
    _CfmFlowUdpNext_Type()
)
cfmFlowUdpNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowUdpNext.setStatus("current")
_CfmFlowUdpPortSrc_Type = InetPortNumber
_CfmFlowUdpPortSrc_Object = MibTableColumn
cfmFlowUdpPortSrc = _CfmFlowUdpPortSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 7, 1, 2),
    _CfmFlowUdpPortSrc_Type()
)
cfmFlowUdpPortSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowUdpPortSrc.setStatus("current")
_CfmFlowUdpPortDst_Type = InetPortNumber
_CfmFlowUdpPortDst_Object = MibTableColumn
cfmFlowUdpPortDst = _CfmFlowUdpPortDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 7, 1, 3),
    _CfmFlowUdpPortDst_Type()
)
cfmFlowUdpPortDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowUdpPortDst.setStatus("current")
_CfmFlowUdpTableChanged_Type = TimeStamp
_CfmFlowUdpTableChanged_Object = MibScalar
cfmFlowUdpTableChanged = _CfmFlowUdpTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 8),
    _CfmFlowUdpTableChanged_Type()
)
cfmFlowUdpTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowUdpTableChanged.setStatus("current")
_CfmFlowTcpTable_Object = MibTable
cfmFlowTcpTable = _CfmFlowTcpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cfmFlowTcpTable.setStatus("current")
_CfmFlowTcpEntry_Object = MibTableRow
cfmFlowTcpEntry = _CfmFlowTcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 9, 1)
)
cfmFlowTcpEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
)
if mibBuilder.loadTexts:
    cfmFlowTcpEntry.setStatus("current")
_CfmFlowTcpNext_Type = RowPointer
_CfmFlowTcpNext_Object = MibTableColumn
cfmFlowTcpNext = _CfmFlowTcpNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 9, 1, 1),
    _CfmFlowTcpNext_Type()
)
cfmFlowTcpNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowTcpNext.setStatus("current")
_CfmFlowTcpPortSrc_Type = InetPortNumber
_CfmFlowTcpPortSrc_Object = MibTableColumn
cfmFlowTcpPortSrc = _CfmFlowTcpPortSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 9, 1, 2),
    _CfmFlowTcpPortSrc_Type()
)
cfmFlowTcpPortSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowTcpPortSrc.setStatus("current")
_CfmFlowTcpPortDst_Type = InetPortNumber
_CfmFlowTcpPortDst_Object = MibTableColumn
cfmFlowTcpPortDst = _CfmFlowTcpPortDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 9, 1, 3),
    _CfmFlowTcpPortDst_Type()
)
cfmFlowTcpPortDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowTcpPortDst.setStatus("current")
_CfmFlowTcpTableChanged_Type = TimeStamp
_CfmFlowTcpTableChanged_Object = MibScalar
cfmFlowTcpTableChanged = _CfmFlowTcpTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 10),
    _CfmFlowTcpTableChanged_Type()
)
cfmFlowTcpTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowTcpTableChanged.setStatus("current")
_CfmFlowRtpTable_Object = MibTable
cfmFlowRtpTable = _CfmFlowRtpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cfmFlowRtpTable.setStatus("current")
_CfmFlowRtpEntry_Object = MibTableRow
cfmFlowRtpEntry = _CfmFlowRtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 11, 1)
)
cfmFlowRtpEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
)
if mibBuilder.loadTexts:
    cfmFlowRtpEntry.setStatus("current")
_CfmFlowRtpNext_Type = RowPointer
_CfmFlowRtpNext_Object = MibTableColumn
cfmFlowRtpNext = _CfmFlowRtpNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 11, 1, 1),
    _CfmFlowRtpNext_Type()
)
cfmFlowRtpNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowRtpNext.setStatus("current")


class _CfmFlowRtpVersion_Type(Unsigned32):
    """Custom type cfmFlowRtpVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CfmFlowRtpVersion_Type.__name__ = "Unsigned32"
_CfmFlowRtpVersion_Object = MibTableColumn
cfmFlowRtpVersion = _CfmFlowRtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 11, 1, 2),
    _CfmFlowRtpVersion_Type()
)
cfmFlowRtpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowRtpVersion.setStatus("current")


class _CfmFlowRtpSsrc_Type(Unsigned32):
    """Custom type cfmFlowRtpSsrc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CfmFlowRtpSsrc_Type.__name__ = "Unsigned32"
_CfmFlowRtpSsrc_Object = MibTableColumn
cfmFlowRtpSsrc = _CfmFlowRtpSsrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 11, 1, 3),
    _CfmFlowRtpSsrc_Type()
)
cfmFlowRtpSsrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowRtpSsrc.setStatus("current")


class _CfmFlowRtpPayloadType_Type(Unsigned32):
    """Custom type cfmFlowRtpPayloadType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CfmFlowRtpPayloadType_Type.__name__ = "Unsigned32"
_CfmFlowRtpPayloadType_Object = MibTableColumn
cfmFlowRtpPayloadType = _CfmFlowRtpPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 11, 1, 4),
    _CfmFlowRtpPayloadType_Type()
)
cfmFlowRtpPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowRtpPayloadType.setStatus("current")
_CfmFlowRtpTableChanged_Type = TimeStamp
_CfmFlowRtpTableChanged_Object = MibScalar
cfmFlowRtpTableChanged = _CfmFlowRtpTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 2, 12),
    _CfmFlowRtpTableChanged_Type()
)
cfmFlowRtpTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowRtpTableChanged.setStatus("current")
_CfmFlowMetrics_ObjectIdentity = ObjectIdentity
cfmFlowMetrics = _CfmFlowMetrics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3)
)
_CfmFlowMetricsTable_Object = MibTable
cfmFlowMetricsTable = _CfmFlowMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cfmFlowMetricsTable.setStatus("current")
_CfmFlowMetricsEntry_Object = MibTableRow
cfmFlowMetricsEntry = _CfmFlowMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1)
)
cfmFlowMetricsEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
)
if mibBuilder.loadTexts:
    cfmFlowMetricsEntry.setStatus("current")
_CfmFlowMetricsCollected_Type = FlowMetrics
_CfmFlowMetricsCollected_Object = MibTableColumn
cfmFlowMetricsCollected = _CfmFlowMetricsCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 1),
    _CfmFlowMetricsCollected_Type()
)
cfmFlowMetricsCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsCollected.setStatus("current")


class _CfmFlowMetricsIntervalTime_Type(Unsigned32):
    """Custom type cfmFlowMetricsIntervalTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CfmFlowMetricsIntervalTime_Type.__name__ = "Unsigned32"
_CfmFlowMetricsIntervalTime_Object = MibTableColumn
cfmFlowMetricsIntervalTime = _CfmFlowMetricsIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 2),
    _CfmFlowMetricsIntervalTime_Type()
)
cfmFlowMetricsIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntervalTime.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntervalTime.setUnits("seconds")


class _CfmFlowMetricsMaxIntervals_Type(Unsigned32):
    """Custom type cfmFlowMetricsMaxIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CfmFlowMetricsMaxIntervals_Type.__name__ = "Unsigned32"
_CfmFlowMetricsMaxIntervals_Object = MibTableColumn
cfmFlowMetricsMaxIntervals = _CfmFlowMetricsMaxIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 3),
    _CfmFlowMetricsMaxIntervals_Type()
)
cfmFlowMetricsMaxIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsMaxIntervals.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMetricsMaxIntervals.setUnits("intervals")
_CfmFlowMetricsElapsedTime_Type = Gauge32
_CfmFlowMetricsElapsedTime_Object = MibTableColumn
cfmFlowMetricsElapsedTime = _CfmFlowMetricsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 4),
    _CfmFlowMetricsElapsedTime_Type()
)
cfmFlowMetricsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMetricsElapsedTime.setUnits("seconds")
_CfmFlowMetricsIntervals_Type = Gauge32
_CfmFlowMetricsIntervals_Object = MibTableColumn
cfmFlowMetricsIntervals = _CfmFlowMetricsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 5),
    _CfmFlowMetricsIntervals_Type()
)
cfmFlowMetricsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntervals.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntervals.setUnits("intervals")
_CfmFlowMetricsInvalidIntervals_Type = Gauge32
_CfmFlowMetricsInvalidIntervals_Object = MibTableColumn
cfmFlowMetricsInvalidIntervals = _CfmFlowMetricsInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 6),
    _CfmFlowMetricsInvalidIntervals_Type()
)
cfmFlowMetricsInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsInvalidIntervals.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMetricsInvalidIntervals.setUnits("intervals")
_CfmFlowMetricsConditionsProfile_Type = FlowMonitorConditionsProfileOrZero
_CfmFlowMetricsConditionsProfile_Object = MibTableColumn
cfmFlowMetricsConditionsProfile = _CfmFlowMetricsConditionsProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 7),
    _CfmFlowMetricsConditionsProfile_Type()
)
cfmFlowMetricsConditionsProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsConditionsProfile.setStatus("current")
_CfmFlowMetricsConditions_Type = FlowMonitorConditions
_CfmFlowMetricsConditions_Object = MibTableColumn
cfmFlowMetricsConditions = _CfmFlowMetricsConditions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 8),
    _CfmFlowMetricsConditions_Type()
)
cfmFlowMetricsConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsConditions.setStatus("current")
_CfmFlowMetricsAlarms_Type = FlowMonitorConditions
_CfmFlowMetricsAlarms_Object = MibTableColumn
cfmFlowMetricsAlarms = _CfmFlowMetricsAlarms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 9),
    _CfmFlowMetricsAlarms_Type()
)
cfmFlowMetricsAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsAlarms.setStatus("current")
_CfmFlowMetricsAlarmSeverity_Type = CiscoAlarmSeverity
_CfmFlowMetricsAlarmSeverity_Object = MibTableColumn
cfmFlowMetricsAlarmSeverity = _CfmFlowMetricsAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 10),
    _CfmFlowMetricsAlarmSeverity_Type()
)
cfmFlowMetricsAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsAlarmSeverity.setStatus("current")
_CfmFlowMetricsPkts_Type = Counter64
_CfmFlowMetricsPkts_Object = MibTableColumn
cfmFlowMetricsPkts = _CfmFlowMetricsPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 11),
    _CfmFlowMetricsPkts_Type()
)
cfmFlowMetricsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMetricsPkts.setUnits("packets")
_CfmFlowMetricsOctets_Type = Counter64
_CfmFlowMetricsOctets_Object = MibTableColumn
cfmFlowMetricsOctets = _CfmFlowMetricsOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 12),
    _CfmFlowMetricsOctets_Type()
)
cfmFlowMetricsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsOctets.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMetricsOctets.setUnits("octets")
_CfmFlowMetricsBitRateUnits_Type = FlowBitRateUnits
_CfmFlowMetricsBitRateUnits_Object = MibTableColumn
cfmFlowMetricsBitRateUnits = _CfmFlowMetricsBitRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 13),
    _CfmFlowMetricsBitRateUnits_Type()
)
cfmFlowMetricsBitRateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsBitRateUnits.setStatus("current")
_CfmFlowMetricsBitRate_Type = Gauge32
_CfmFlowMetricsBitRate_Object = MibTableColumn
cfmFlowMetricsBitRate = _CfmFlowMetricsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 14),
    _CfmFlowMetricsBitRate_Type()
)
cfmFlowMetricsBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsBitRate.setStatus("current")
_CfmFlowMetricsPktRate_Type = Gauge32
_CfmFlowMetricsPktRate_Object = MibTableColumn
cfmFlowMetricsPktRate = _CfmFlowMetricsPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 1, 1, 15),
    _CfmFlowMetricsPktRate_Type()
)
cfmFlowMetricsPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMetricsPktRate.setUnits("packets per second")
_CfmFlowMetricsTableChanged_Type = TimeStamp
_CfmFlowMetricsTableChanged_Object = MibScalar
cfmFlowMetricsTableChanged = _CfmFlowMetricsTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 2),
    _CfmFlowMetricsTableChanged_Type()
)
cfmFlowMetricsTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsTableChanged.setStatus("current")
_CfmFlowMetricsIntTable_Object = MibTable
cfmFlowMetricsIntTable = _CfmFlowMetricsIntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cfmFlowMetricsIntTable.setStatus("current")
_CfmFlowMetricsIntEntry_Object = MibTableRow
cfmFlowMetricsIntEntry = _CfmFlowMetricsIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3, 1)
)
cfmFlowMetricsIntEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntNumber"),
)
if mibBuilder.loadTexts:
    cfmFlowMetricsIntEntry.setStatus("current")


class _CfmFlowMetricsIntNumber_Type(Unsigned32):
    """Custom type cfmFlowMetricsIntNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CfmFlowMetricsIntNumber_Type.__name__ = "Unsigned32"
_CfmFlowMetricsIntNumber_Object = MibTableColumn
cfmFlowMetricsIntNumber = _CfmFlowMetricsIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3, 1, 1),
    _CfmFlowMetricsIntNumber_Type()
)
cfmFlowMetricsIntNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntNumber.setStatus("current")
_CfmFlowMetricsIntValid_Type = TruthValue
_CfmFlowMetricsIntValid_Object = MibTableColumn
cfmFlowMetricsIntValid = _CfmFlowMetricsIntValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3, 1, 2),
    _CfmFlowMetricsIntValid_Type()
)
cfmFlowMetricsIntValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntValid.setStatus("current")
_CfmFlowMetricsIntTime_Type = TimeStamp
_CfmFlowMetricsIntTime_Object = MibTableColumn
cfmFlowMetricsIntTime = _CfmFlowMetricsIntTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3, 1, 3),
    _CfmFlowMetricsIntTime_Type()
)
cfmFlowMetricsIntTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntTime.setStatus("current")
_CfmFlowMetricsIntConditions_Type = FlowMonitorConditions
_CfmFlowMetricsIntConditions_Object = MibTableColumn
cfmFlowMetricsIntConditions = _CfmFlowMetricsIntConditions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3, 1, 4),
    _CfmFlowMetricsIntConditions_Type()
)
cfmFlowMetricsIntConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntConditions.setStatus("current")
_CfmFlowMetricsIntAlarms_Type = FlowMonitorConditions
_CfmFlowMetricsIntAlarms_Object = MibTableColumn
cfmFlowMetricsIntAlarms = _CfmFlowMetricsIntAlarms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3, 1, 5),
    _CfmFlowMetricsIntAlarms_Type()
)
cfmFlowMetricsIntAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntAlarms.setStatus("current")
_CfmFlowMetricsIntAlarmSeverity_Type = CiscoAlarmSeverity
_CfmFlowMetricsIntAlarmSeverity_Object = MibTableColumn
cfmFlowMetricsIntAlarmSeverity = _CfmFlowMetricsIntAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3, 1, 6),
    _CfmFlowMetricsIntAlarmSeverity_Type()
)
cfmFlowMetricsIntAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntAlarmSeverity.setStatus("current")
_CfmFlowMetricsIntPkts_Type = ReportIntervalCount
_CfmFlowMetricsIntPkts_Object = MibTableColumn
cfmFlowMetricsIntPkts = _CfmFlowMetricsIntPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3, 1, 7),
    _CfmFlowMetricsIntPkts_Type()
)
cfmFlowMetricsIntPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntPkts.setUnits("packets")
_CfmFlowMetricsIntOctets_Type = ReportIntervalCount
_CfmFlowMetricsIntOctets_Object = MibTableColumn
cfmFlowMetricsIntOctets = _CfmFlowMetricsIntOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3, 1, 8),
    _CfmFlowMetricsIntOctets_Type()
)
cfmFlowMetricsIntOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntOctets.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntOctets.setUnits("octets")
_CfmFlowMetricsIntBitRateUnits_Type = FlowBitRateUnits
_CfmFlowMetricsIntBitRateUnits_Object = MibTableColumn
cfmFlowMetricsIntBitRateUnits = _CfmFlowMetricsIntBitRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3, 1, 9),
    _CfmFlowMetricsIntBitRateUnits_Type()
)
cfmFlowMetricsIntBitRateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntBitRateUnits.setStatus("current")
_CfmFlowMetricsIntBitRate_Type = ReportIntervalCount
_CfmFlowMetricsIntBitRate_Object = MibTableColumn
cfmFlowMetricsIntBitRate = _CfmFlowMetricsIntBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3, 1, 10),
    _CfmFlowMetricsIntBitRate_Type()
)
cfmFlowMetricsIntBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntBitRate.setStatus("current")
_CfmFlowMetricsIntPktRate_Type = ReportIntervalCount
_CfmFlowMetricsIntPktRate_Object = MibTableColumn
cfmFlowMetricsIntPktRate = _CfmFlowMetricsIntPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 3, 3, 1, 11),
    _CfmFlowMetricsIntPktRate_Type()
)
cfmFlowMetricsIntPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cfmFlowMetricsIntPktRate.setUnits("packets per second")
_CfmConditions_ObjectIdentity = ObjectIdentity
cfmConditions = _CfmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4)
)
_CfmConditionTable_Object = MibTable
cfmConditionTable = _CfmConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cfmConditionTable.setStatus("current")
_CfmConditionEntry_Object = MibTableRow
cfmConditionEntry = _CfmConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1)
)
cfmConditionEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmConditionProfile"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmConditionId"),
)
if mibBuilder.loadTexts:
    cfmConditionEntry.setStatus("current")
_CfmConditionProfile_Type = FlowMonitorConditionsProfile
_CfmConditionProfile_Object = MibTableColumn
cfmConditionProfile = _CfmConditionProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 1),
    _CfmConditionProfile_Type()
)
cfmConditionProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmConditionProfile.setStatus("current")
_CfmConditionId_Type = FlowMonitorConditionIdentifier
_CfmConditionId_Object = MibTableColumn
cfmConditionId = _CfmConditionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 2),
    _CfmConditionId_Type()
)
cfmConditionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmConditionId.setStatus("current")
_CfmConditionDescr_Type = SnmpAdminString
_CfmConditionDescr_Object = MibTableColumn
cfmConditionDescr = _CfmConditionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 3),
    _CfmConditionDescr_Type()
)
cfmConditionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionDescr.setStatus("current")
_CfmConditionMonitoredElement_Type = AutonomousType
_CfmConditionMonitoredElement_Object = MibTableColumn
cfmConditionMonitoredElement = _CfmConditionMonitoredElement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 4),
    _CfmConditionMonitoredElement_Type()
)
cfmConditionMonitoredElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionMonitoredElement.setStatus("current")


class _CfmConditionType_Type(Integer32):
    """Custom type cfmConditionType based on Integer32"""
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
        *(("boolean", 2),
          ("fallingThreshold", 4),
          ("other", 1),
          ("risingAndFallingThreshold", 5),
          ("risingThreshold", 3))
    )


_CfmConditionType_Type.__name__ = "Integer32"
_CfmConditionType_Object = MibTableColumn
cfmConditionType = _CfmConditionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 5),
    _CfmConditionType_Type()
)
cfmConditionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionType.setStatus("current")
_CfmConditionThreshRiseScale_Type = FlowMetricScale
_CfmConditionThreshRiseScale_Object = MibTableColumn
cfmConditionThreshRiseScale = _CfmConditionThreshRiseScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 6),
    _CfmConditionThreshRiseScale_Type()
)
cfmConditionThreshRiseScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionThreshRiseScale.setStatus("current")
_CfmConditionThreshRisePrecision_Type = FlowMetricPrecision
_CfmConditionThreshRisePrecision_Object = MibTableColumn
cfmConditionThreshRisePrecision = _CfmConditionThreshRisePrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 7),
    _CfmConditionThreshRisePrecision_Type()
)
cfmConditionThreshRisePrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionThreshRisePrecision.setStatus("current")
_CfmConditionThreshRise_Type = FlowMetricValue
_CfmConditionThreshRise_Object = MibTableColumn
cfmConditionThreshRise = _CfmConditionThreshRise_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 8),
    _CfmConditionThreshRise_Type()
)
cfmConditionThreshRise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionThreshRise.setStatus("current")
_CfmConditionThreshFallScale_Type = FlowMetricScale
_CfmConditionThreshFallScale_Object = MibTableColumn
cfmConditionThreshFallScale = _CfmConditionThreshFallScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 9),
    _CfmConditionThreshFallScale_Type()
)
cfmConditionThreshFallScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionThreshFallScale.setStatus("current")
_CfmConditionThreshFallPrecision_Type = FlowMetricPrecision
_CfmConditionThreshFallPrecision_Object = MibTableColumn
cfmConditionThreshFallPrecision = _CfmConditionThreshFallPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 10),
    _CfmConditionThreshFallPrecision_Type()
)
cfmConditionThreshFallPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionThreshFallPrecision.setStatus("current")
_CfmConditionThreshFall_Type = FlowMetricValue
_CfmConditionThreshFall_Object = MibTableColumn
cfmConditionThreshFall = _CfmConditionThreshFall_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 11),
    _CfmConditionThreshFall_Type()
)
cfmConditionThreshFall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionThreshFall.setStatus("current")


class _CfmConditionSampleType_Type(Integer32):
    """Custom type cfmConditionSampleType based on Integer32"""
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
        *(("expDecayingAvg", 4),
          ("other", 1),
          ("raw", 2),
          ("slidingWindowAvg", 3))
    )


_CfmConditionSampleType_Type.__name__ = "Integer32"
_CfmConditionSampleType_Object = MibTableColumn
cfmConditionSampleType = _CfmConditionSampleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 13),
    _CfmConditionSampleType_Type()
)
cfmConditionSampleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionSampleType.setStatus("current")


class _CfmConditionSampleWindow_Type(Unsigned32):
    """Custom type cfmConditionSampleWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CfmConditionSampleWindow_Type.__name__ = "Unsigned32"
_CfmConditionSampleWindow_Object = MibTableColumn
cfmConditionSampleWindow = _CfmConditionSampleWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 14),
    _CfmConditionSampleWindow_Type()
)
cfmConditionSampleWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionSampleWindow.setStatus("current")


class _CfmConditionAlarm_Type(Integer32):
    """Custom type cfmConditionAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discrete", 2),
          ("grouped", 3),
          ("none", 1))
    )


_CfmConditionAlarm_Type.__name__ = "Integer32"
_CfmConditionAlarm_Object = MibTableColumn
cfmConditionAlarm = _CfmConditionAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 15),
    _CfmConditionAlarm_Type()
)
cfmConditionAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionAlarm.setStatus("current")


class _CfmConditionAlarmActions_Type(Bits):
    """Custom type cfmConditionAlarmActions based on Bits"""
    namedValues = NamedValues(
        *(("snmp", 1),
          ("syslog", 0))
    )

_CfmConditionAlarmActions_Type.__name__ = "Bits"
_CfmConditionAlarmActions_Object = MibTableColumn
cfmConditionAlarmActions = _CfmConditionAlarmActions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 16),
    _CfmConditionAlarmActions_Type()
)
cfmConditionAlarmActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionAlarmActions.setStatus("current")
_CfmConditionAlarmSeverity_Type = CiscoAlarmSeverity
_CfmConditionAlarmSeverity_Object = MibTableColumn
cfmConditionAlarmSeverity = _CfmConditionAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 17),
    _CfmConditionAlarmSeverity_Type()
)
cfmConditionAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionAlarmSeverity.setStatus("current")
_CfmConditionAlarmGroup_Type = FlowMonitorAlarmGroupIdentifier
_CfmConditionAlarmGroup_Object = MibTableColumn
cfmConditionAlarmGroup = _CfmConditionAlarmGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 1, 1, 18),
    _CfmConditionAlarmGroup_Type()
)
cfmConditionAlarmGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionAlarmGroup.setStatus("current")
_CfmConditionTableChanged_Type = TimeStamp
_CfmConditionTableChanged_Object = MibScalar
cfmConditionTableChanged = _CfmConditionTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 4, 2),
    _CfmConditionTableChanged_Type()
)
cfmConditionTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmConditionTableChanged.setStatus("current")
_CfmAlarmGroups_ObjectIdentity = ObjectIdentity
cfmAlarmGroups = _CfmAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5)
)
_CfmAlarmGroupTable_Object = MibTable
cfmAlarmGroupTable = _CfmAlarmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cfmAlarmGroupTable.setStatus("current")
_CfmAlarmGroupEntry_Object = MibTableRow
cfmAlarmGroupEntry = _CfmAlarmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 1, 1)
)
cfmAlarmGroupEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupId"),
)
if mibBuilder.loadTexts:
    cfmAlarmGroupEntry.setStatus("current")
_CfmAlarmGroupId_Type = FlowMonitorAlarmGroupIdentifier
_CfmAlarmGroupId_Object = MibTableColumn
cfmAlarmGroupId = _CfmAlarmGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 1, 1, 1),
    _CfmAlarmGroupId_Type()
)
cfmAlarmGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmAlarmGroupId.setStatus("current")
_CfmAlarmGroupDescr_Type = SnmpAdminString
_CfmAlarmGroupDescr_Object = MibTableColumn
cfmAlarmGroupDescr = _CfmAlarmGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 1, 1, 2),
    _CfmAlarmGroupDescr_Type()
)
cfmAlarmGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmGroupDescr.setStatus("current")
_CfmAlarmGroupConditionsProfile_Type = FlowMonitorConditionsProfile
_CfmAlarmGroupConditionsProfile_Object = MibTableColumn
cfmAlarmGroupConditionsProfile = _CfmAlarmGroupConditionsProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 1, 1, 3),
    _CfmAlarmGroupConditionsProfile_Type()
)
cfmAlarmGroupConditionsProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmGroupConditionsProfile.setStatus("current")
_CfmAlarmGroupConditionId_Type = FlowMonitorConditionIdentifier
_CfmAlarmGroupConditionId_Object = MibTableColumn
cfmAlarmGroupConditionId = _CfmAlarmGroupConditionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 1, 1, 4),
    _CfmAlarmGroupConditionId_Type()
)
cfmAlarmGroupConditionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmGroupConditionId.setStatus("current")
_CfmAlarmGroupFlowSet_Type = FlowSetIdentifier
_CfmAlarmGroupFlowSet_Object = MibTableColumn
cfmAlarmGroupFlowSet = _CfmAlarmGroupFlowSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 1, 1, 5),
    _CfmAlarmGroupFlowSet_Type()
)
cfmAlarmGroupFlowSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmGroupFlowSet.setStatus("current")
_CfmAlarmGroupFlowCount_Type = Gauge32
_CfmAlarmGroupFlowCount_Object = MibTableColumn
cfmAlarmGroupFlowCount = _CfmAlarmGroupFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 1, 1, 6),
    _CfmAlarmGroupFlowCount_Type()
)
cfmAlarmGroupFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmGroupFlowCount.setStatus("current")
if mibBuilder.loadTexts:
    cfmAlarmGroupFlowCount.setUnits("traffic flows")


class _CfmAlarmGroupThresholdUnits_Type(Integer32):
    """Custom type cfmAlarmGroupThresholdUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flows", 2),
          ("other", 1),
          ("percent", 3))
    )


_CfmAlarmGroupThresholdUnits_Type.__name__ = "Integer32"
_CfmAlarmGroupThresholdUnits_Object = MibTableColumn
cfmAlarmGroupThresholdUnits = _CfmAlarmGroupThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 1, 1, 7),
    _CfmAlarmGroupThresholdUnits_Type()
)
cfmAlarmGroupThresholdUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmGroupThresholdUnits.setStatus("current")


class _CfmAlarmGroupThreshold_Type(Unsigned32):
    """Custom type cfmAlarmGroupThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CfmAlarmGroupThreshold_Type.__name__ = "Unsigned32"
_CfmAlarmGroupThreshold_Object = MibTableColumn
cfmAlarmGroupThreshold = _CfmAlarmGroupThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 1, 1, 8),
    _CfmAlarmGroupThreshold_Type()
)
cfmAlarmGroupThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmGroupThreshold.setStatus("current")
_CfmAlarmGroupRaised_Type = TruthValue
_CfmAlarmGroupRaised_Object = MibTableColumn
cfmAlarmGroupRaised = _CfmAlarmGroupRaised_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 1, 1, 9),
    _CfmAlarmGroupRaised_Type()
)
cfmAlarmGroupRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmGroupRaised.setStatus("current")
_CfmAlarmGroupCurrentCount_Type = Gauge32
_CfmAlarmGroupCurrentCount_Object = MibTableColumn
cfmAlarmGroupCurrentCount = _CfmAlarmGroupCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 1, 1, 10),
    _CfmAlarmGroupCurrentCount_Type()
)
cfmAlarmGroupCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmGroupCurrentCount.setStatus("current")
if mibBuilder.loadTexts:
    cfmAlarmGroupCurrentCount.setUnits("traffic flows")
_CfmAlarmGroupTableChanged_Type = TimeStamp
_CfmAlarmGroupTableChanged_Object = MibScalar
cfmAlarmGroupTableChanged = _CfmAlarmGroupTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 2),
    _CfmAlarmGroupTableChanged_Type()
)
cfmAlarmGroupTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmGroupTableChanged.setStatus("current")
_CfmAlarmGroupFlowTable_Object = MibTable
cfmAlarmGroupFlowTable = _CfmAlarmGroupFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cfmAlarmGroupFlowTable.setStatus("current")
_CfmAlarmGroupFlowEntry_Object = MibTableRow
cfmAlarmGroupFlowEntry = _CfmAlarmGroupFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 3, 1)
)
cfmAlarmGroupFlowEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupFlowSetId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupFlowMonitorId"),
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupFlowId"),
)
if mibBuilder.loadTexts:
    cfmAlarmGroupFlowEntry.setStatus("current")
_CfmAlarmGroupFlowSetId_Type = FlowSetIdentifier
_CfmAlarmGroupFlowSetId_Object = MibTableColumn
cfmAlarmGroupFlowSetId = _CfmAlarmGroupFlowSetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 3, 1, 1),
    _CfmAlarmGroupFlowSetId_Type()
)
cfmAlarmGroupFlowSetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmAlarmGroupFlowSetId.setStatus("current")
_CfmAlarmGroupFlowMonitorId_Type = FlowMonitorIdentifier
_CfmAlarmGroupFlowMonitorId_Object = MibTableColumn
cfmAlarmGroupFlowMonitorId = _CfmAlarmGroupFlowMonitorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 3, 1, 2),
    _CfmAlarmGroupFlowMonitorId_Type()
)
cfmAlarmGroupFlowMonitorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmAlarmGroupFlowMonitorId.setStatus("current")
_CfmAlarmGroupFlowId_Type = FlowIdentifier
_CfmAlarmGroupFlowId_Object = MibTableColumn
cfmAlarmGroupFlowId = _CfmAlarmGroupFlowId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 3, 1, 3),
    _CfmAlarmGroupFlowId_Type()
)
cfmAlarmGroupFlowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmGroupFlowId.setStatus("current")
_CfmAlarmGroupFlowTableChanged_Type = TimeStamp
_CfmAlarmGroupFlowTableChanged_Object = MibScalar
cfmAlarmGroupFlowTableChanged = _CfmAlarmGroupFlowTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 5, 4),
    _CfmAlarmGroupFlowTableChanged_Type()
)
cfmAlarmGroupFlowTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmGroupFlowTableChanged.setStatus("current")
_CfmAlarmHistory_ObjectIdentity = ObjectIdentity
cfmAlarmHistory = _CfmAlarmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 6)
)


class _CfmAlarmHistorySize_Type(Unsigned32):
    """Custom type cfmAlarmHistorySize based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CfmAlarmHistorySize_Type.__name__ = "Unsigned32"
_CfmAlarmHistorySize_Object = MibScalar
cfmAlarmHistorySize = _CfmAlarmHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 6, 1),
    _CfmAlarmHistorySize_Type()
)
cfmAlarmHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmAlarmHistorySize.setStatus("current")


class _CfmAlarmHistoryLastId_Type(Unsigned32):
    """Custom type cfmAlarmHistoryLastId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CfmAlarmHistoryLastId_Type.__name__ = "Unsigned32"
_CfmAlarmHistoryLastId_Object = MibScalar
cfmAlarmHistoryLastId = _CfmAlarmHistoryLastId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 6, 2),
    _CfmAlarmHistoryLastId_Type()
)
cfmAlarmHistoryLastId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmHistoryLastId.setStatus("current")
_CfmAlarmHistoryTable_Object = MibTable
cfmAlarmHistoryTable = _CfmAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cfmAlarmHistoryTable.setStatus("current")
_CfmAlarmHistoryEntry_Object = MibTableRow
cfmAlarmHistoryEntry = _CfmAlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 6, 3, 1)
)
cfmAlarmHistoryEntry.setIndexNames(
    (0, "CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistoryId"),
)
if mibBuilder.loadTexts:
    cfmAlarmHistoryEntry.setStatus("current")


class _CfmAlarmHistoryId_Type(Unsigned32):
    """Custom type cfmAlarmHistoryId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CfmAlarmHistoryId_Type.__name__ = "Unsigned32"
_CfmAlarmHistoryId_Object = MibTableColumn
cfmAlarmHistoryId = _CfmAlarmHistoryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 6, 3, 1, 1),
    _CfmAlarmHistoryId_Type()
)
cfmAlarmHistoryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmAlarmHistoryId.setStatus("current")


class _CfmAlarmHistoryType_Type(Integer32):
    """Custom type cfmAlarmHistoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("raised", 2))
    )


_CfmAlarmHistoryType_Type.__name__ = "Integer32"
_CfmAlarmHistoryType_Object = MibTableColumn
cfmAlarmHistoryType = _CfmAlarmHistoryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 6, 3, 1, 2),
    _CfmAlarmHistoryType_Type()
)
cfmAlarmHistoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmHistoryType.setStatus("current")
_CfmAlarmHistoryEntity_Type = RowPointer
_CfmAlarmHistoryEntity_Object = MibTableColumn
cfmAlarmHistoryEntity = _CfmAlarmHistoryEntity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 6, 3, 1, 3),
    _CfmAlarmHistoryEntity_Type()
)
cfmAlarmHistoryEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmHistoryEntity.setStatus("current")
_CfmAlarmHistoryConditionsProfile_Type = FlowMonitorConditionsProfile
_CfmAlarmHistoryConditionsProfile_Object = MibTableColumn
cfmAlarmHistoryConditionsProfile = _CfmAlarmHistoryConditionsProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 6, 3, 1, 4),
    _CfmAlarmHistoryConditionsProfile_Type()
)
cfmAlarmHistoryConditionsProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmHistoryConditionsProfile.setStatus("current")
_CfmAlarmHistoryConditionId_Type = FlowMonitorConditionIdentifier
_CfmAlarmHistoryConditionId_Object = MibTableColumn
cfmAlarmHistoryConditionId = _CfmAlarmHistoryConditionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 6, 3, 1, 5),
    _CfmAlarmHistoryConditionId_Type()
)
cfmAlarmHistoryConditionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmHistoryConditionId.setStatus("current")
_CfmAlarmHistorySeverity_Type = CiscoAlarmSeverity
_CfmAlarmHistorySeverity_Object = MibTableColumn
cfmAlarmHistorySeverity = _CfmAlarmHistorySeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 6, 3, 1, 6),
    _CfmAlarmHistorySeverity_Type()
)
cfmAlarmHistorySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmHistorySeverity.setStatus("current")
_CfmAlarmHistoryTime_Type = TimeStamp
_CfmAlarmHistoryTime_Object = MibTableColumn
cfmAlarmHistoryTime = _CfmAlarmHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 6, 3, 1, 7),
    _CfmAlarmHistoryTime_Type()
)
cfmAlarmHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmAlarmHistoryTime.setStatus("current")
_CfmNotify_ObjectIdentity = ObjectIdentity
cfmNotify = _CfmNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 7)
)
_CfmNotifyEnable_Type = TruthValue
_CfmNotifyEnable_Object = MibScalar
cfmNotifyEnable = _CfmNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 1, 7, 1),
    _CfmNotifyEnable_Type()
)
cfmNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmNotifyEnable.setStatus("current")
_CiscoFlowMonitorMIBConform_ObjectIdentity = ObjectIdentity
ciscoFlowMonitorMIBConform = _CiscoFlowMonitorMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 2)
)
_CiscoFlowMonitorMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFlowMonitorMIBCompliances = _CiscoFlowMonitorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 2, 1)
)
_CiscoFlowMonitorMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFlowMonitorMIBGroups = _CiscoFlowMonitorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 2, 2)
)
_CiscoFlowMonitorMIBIds_ObjectIdentity = ObjectIdentity
ciscoFlowMonitorMIBIds = _CiscoFlowMonitorMIBIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 3)
)
_CfmMonitoredElements_ObjectIdentity = ObjectIdentity
cfmMonitoredElements = _CfmMonitoredElements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 3, 1)
)
_CfmeOther_ObjectIdentity = ObjectIdentity
cfmeOther = _CfmeOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cfmeOther.setStatus("current")
_CfmeFlowCount_ObjectIdentity = ObjectIdentity
cfmeFlowCount = _CfmeFlowCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cfmeFlowCount.setStatus("current")
_CfmeFlowTimeouts_ObjectIdentity = ObjectIdentity
cfmeFlowTimeouts = _CfmeFlowTimeouts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cfmeFlowTimeouts.setStatus("current")
_CfmeFlowStop_ObjectIdentity = ObjectIdentity
cfmeFlowStop = _CfmeFlowStop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cfmeFlowStop.setStatus("current")
_CfmeFlowCumulativeBitRate_ObjectIdentity = ObjectIdentity
cfmeFlowCumulativeBitRate = _CfmeFlowCumulativeBitRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cfmeFlowCumulativeBitRate.setStatus("current")
_CfmeFlowCumulativePktRate_ObjectIdentity = ObjectIdentity
cfmeFlowCumulativePktRate = _CfmeFlowCumulativePktRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cfmeFlowCumulativePktRate.setStatus("current")
_CfmeFlowBitRate_ObjectIdentity = ObjectIdentity
cfmeFlowBitRate = _CfmeFlowBitRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cfmeFlowBitRate.setStatus("current")
_CfmeFlowPktRate_ObjectIdentity = ObjectIdentity
cfmeFlowPktRate = _CfmeFlowPktRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 3, 1, 8)
)
if mibBuilder.loadTexts:
    cfmeFlowPktRate.setStatus("current")

# Managed Objects groups

cfmFlowMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 2, 2, 1)
)
cfmFlowMonitorGroup.setObjects(
      *(("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorDescr"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorCaps"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorFlowCount"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorConditionsProfile"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorConditions"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorAlarms"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorAlarmSeverity"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorAlarmCriticalCount"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorAlarmMajorCount"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorAlarmMinorCount"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorAlarmWarningCount"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorAlarmInfoCount"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMonitorTableChanged"))
)
if mibBuilder.loadTexts:
    cfmFlowMonitorGroup.setStatus("current")

cfmFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 2, 2, 2)
)
cfmFlowGroup.setObjects(
      *(("CISCO-FLOW-MONITOR-MIB", "cfmFlowDescr"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowNext"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowCreateTime"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowDiscontinuityTime"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowExpirationTime"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowDirection"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowAdminStatus"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowOperStatus"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowIngressType"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowIngress"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowEgressType"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowEgress"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowTableChanged"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowL2VlanNext"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowL2VlanId"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowL2VlanCos"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowL2VlanTableChanged"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowIpNext"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowIpAddrType"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowIpAddrSrc"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowIpAddrDst"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowIpValid"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowIpTrafficClass"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowIpHopLimit"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowIpTableChanged"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowUdpNext"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowUdpPortSrc"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowUdpPortDst"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowUdpTableChanged"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowTcpNext"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowTcpPortSrc"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowTcpPortDst"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowTcpTableChanged"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowRtpNext"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowRtpVersion"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowRtpSsrc"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowRtpPayloadType"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowRtpTableChanged"))
)
if mibBuilder.loadTexts:
    cfmFlowGroup.setStatus("current")

cfmFlowMetricsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 2, 2, 3)
)
cfmFlowMetricsGroup.setObjects(
      *(("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsCollected"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntervalTime"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsMaxIntervals"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsElapsedTime"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntervals"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsInvalidIntervals"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsConditionsProfile"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsConditions"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsAlarms"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsAlarmSeverity"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsPkts"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsOctets"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsBitRateUnits"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsBitRate"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsPktRate"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsTableChanged"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntValid"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntTime"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntConditions"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntAlarms"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntAlarmSeverity"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntPkts"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntOctets"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntBitRateUnits"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntBitRate"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmFlowMetricsIntPktRate"))
)
if mibBuilder.loadTexts:
    cfmFlowMetricsGroup.setStatus("current")

cfmFlowConditionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 2, 2, 4)
)
cfmFlowConditionsGroup.setObjects(
      *(("CISCO-FLOW-MONITOR-MIB", "cfmConditionDescr"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionMonitoredElement"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionType"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionThreshRiseScale"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionThreshRisePrecision"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionThreshRise"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionThreshFallScale"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionThreshFallPrecision"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionThreshFall"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionSampleType"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionSampleWindow"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionAlarm"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionAlarmActions"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionAlarmSeverity"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionAlarmGroup"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmConditionTableChanged"))
)
if mibBuilder.loadTexts:
    cfmFlowConditionsGroup.setStatus("current")

cfmAlarmAggregationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 2, 2, 5)
)
cfmAlarmAggregationGroup.setObjects(
      *(("CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupDescr"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupConditionsProfile"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupConditionId"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupFlowSet"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupFlowCount"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupThresholdUnits"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupThreshold"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupRaised"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupCurrentCount"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupTableChanged"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupFlowId"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmGroupFlowTableChanged"))
)
if mibBuilder.loadTexts:
    cfmAlarmAggregationGroup.setStatus("current")

cfmAlarmHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 2, 2, 6)
)
cfmAlarmHistoryGroup.setObjects(
      *(("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistorySize"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistoryLastId"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistoryType"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistoryEntity"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistoryConditionsProfile"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistoryConditionId"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistorySeverity"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistoryTime"))
)
if mibBuilder.loadTexts:
    cfmAlarmHistoryGroup.setStatus("current")

cfmNotifySupportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 2, 2, 7)
)
cfmNotifySupportGroup.setObjects(
    ("CISCO-FLOW-MONITOR-MIB", "cfmNotifyEnable")
)
if mibBuilder.loadTexts:
    cfmNotifySupportGroup.setStatus("current")


# Notification objects

cfmNotifyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 0, 1)
)
cfmNotifyAlarm.setObjects(
      *(("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistoryType"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistoryEntity"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistoryConditionsProfile"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistoryConditionId"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistorySeverity"),
        ("CISCO-FLOW-MONITOR-MIB", "cfmAlarmHistoryTime"))
)
if mibBuilder.loadTexts:
    cfmNotifyAlarm.setStatus(
        "current"
    )


# Notifications groups

cfmNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 2, 2, 8)
)
cfmNotifyGroup.setObjects(
    ("CISCO-FLOW-MONITOR-MIB", "cfmNotifyAlarm")
)
if mibBuilder.loadTexts:
    cfmNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoFlowMonitorCompliance01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 692, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFlowMonitorCompliance01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FLOW-MONITOR-MIB",
    **{"ciscoFlowMonitorMIB": ciscoFlowMonitorMIB,
       "ciscoFlowMonitorMIBNotifs": ciscoFlowMonitorMIBNotifs,
       "cfmNotifyAlarm": cfmNotifyAlarm,
       "ciscoFlowMonitorMIBObjects": ciscoFlowMonitorMIBObjects,
       "cfmFlowMonitors": cfmFlowMonitors,
       "cfmFlowMonitorTable": cfmFlowMonitorTable,
       "cfmFlowMonitorEntry": cfmFlowMonitorEntry,
       "cfmFlowMonitorId": cfmFlowMonitorId,
       "cfmFlowMonitorDescr": cfmFlowMonitorDescr,
       "cfmFlowMonitorCaps": cfmFlowMonitorCaps,
       "cfmFlowMonitorFlowCount": cfmFlowMonitorFlowCount,
       "cfmFlowMonitorConditionsProfile": cfmFlowMonitorConditionsProfile,
       "cfmFlowMonitorConditions": cfmFlowMonitorConditions,
       "cfmFlowMonitorAlarms": cfmFlowMonitorAlarms,
       "cfmFlowMonitorAlarmSeverity": cfmFlowMonitorAlarmSeverity,
       "cfmFlowMonitorAlarmCriticalCount": cfmFlowMonitorAlarmCriticalCount,
       "cfmFlowMonitorAlarmMajorCount": cfmFlowMonitorAlarmMajorCount,
       "cfmFlowMonitorAlarmMinorCount": cfmFlowMonitorAlarmMinorCount,
       "cfmFlowMonitorAlarmWarningCount": cfmFlowMonitorAlarmWarningCount,
       "cfmFlowMonitorAlarmInfoCount": cfmFlowMonitorAlarmInfoCount,
       "cfmFlowMonitorTableChanged": cfmFlowMonitorTableChanged,
       "cfmFlows": cfmFlows,
       "cfmFlowTable": cfmFlowTable,
       "cfmFlowEntry": cfmFlowEntry,
       "cfmFlowId": cfmFlowId,
       "cfmFlowDescr": cfmFlowDescr,
       "cfmFlowNext": cfmFlowNext,
       "cfmFlowCreateTime": cfmFlowCreateTime,
       "cfmFlowDiscontinuityTime": cfmFlowDiscontinuityTime,
       "cfmFlowExpirationTime": cfmFlowExpirationTime,
       "cfmFlowDirection": cfmFlowDirection,
       "cfmFlowAdminStatus": cfmFlowAdminStatus,
       "cfmFlowOperStatus": cfmFlowOperStatus,
       "cfmFlowIngressType": cfmFlowIngressType,
       "cfmFlowIngress": cfmFlowIngress,
       "cfmFlowEgressType": cfmFlowEgressType,
       "cfmFlowEgress": cfmFlowEgress,
       "cfmFlowTableChanged": cfmFlowTableChanged,
       "cfmFlowL2VlanTable": cfmFlowL2VlanTable,
       "cfmFlowL2VlanEntry": cfmFlowL2VlanEntry,
       "cfmFlowL2VlanNext": cfmFlowL2VlanNext,
       "cfmFlowL2VlanId": cfmFlowL2VlanId,
       "cfmFlowL2VlanCos": cfmFlowL2VlanCos,
       "cfmFlowL2VlanTableChanged": cfmFlowL2VlanTableChanged,
       "cfmFlowIpTable": cfmFlowIpTable,
       "cfmFlowIpEntry": cfmFlowIpEntry,
       "cfmFlowIpNext": cfmFlowIpNext,
       "cfmFlowIpAddrType": cfmFlowIpAddrType,
       "cfmFlowIpAddrSrc": cfmFlowIpAddrSrc,
       "cfmFlowIpAddrDst": cfmFlowIpAddrDst,
       "cfmFlowIpValid": cfmFlowIpValid,
       "cfmFlowIpTrafficClass": cfmFlowIpTrafficClass,
       "cfmFlowIpHopLimit": cfmFlowIpHopLimit,
       "cfmFlowIpTableChanged": cfmFlowIpTableChanged,
       "cfmFlowUdpTable": cfmFlowUdpTable,
       "cfmFlowUdpEntry": cfmFlowUdpEntry,
       "cfmFlowUdpNext": cfmFlowUdpNext,
       "cfmFlowUdpPortSrc": cfmFlowUdpPortSrc,
       "cfmFlowUdpPortDst": cfmFlowUdpPortDst,
       "cfmFlowUdpTableChanged": cfmFlowUdpTableChanged,
       "cfmFlowTcpTable": cfmFlowTcpTable,
       "cfmFlowTcpEntry": cfmFlowTcpEntry,
       "cfmFlowTcpNext": cfmFlowTcpNext,
       "cfmFlowTcpPortSrc": cfmFlowTcpPortSrc,
       "cfmFlowTcpPortDst": cfmFlowTcpPortDst,
       "cfmFlowTcpTableChanged": cfmFlowTcpTableChanged,
       "cfmFlowRtpTable": cfmFlowRtpTable,
       "cfmFlowRtpEntry": cfmFlowRtpEntry,
       "cfmFlowRtpNext": cfmFlowRtpNext,
       "cfmFlowRtpVersion": cfmFlowRtpVersion,
       "cfmFlowRtpSsrc": cfmFlowRtpSsrc,
       "cfmFlowRtpPayloadType": cfmFlowRtpPayloadType,
       "cfmFlowRtpTableChanged": cfmFlowRtpTableChanged,
       "cfmFlowMetrics": cfmFlowMetrics,
       "cfmFlowMetricsTable": cfmFlowMetricsTable,
       "cfmFlowMetricsEntry": cfmFlowMetricsEntry,
       "cfmFlowMetricsCollected": cfmFlowMetricsCollected,
       "cfmFlowMetricsIntervalTime": cfmFlowMetricsIntervalTime,
       "cfmFlowMetricsMaxIntervals": cfmFlowMetricsMaxIntervals,
       "cfmFlowMetricsElapsedTime": cfmFlowMetricsElapsedTime,
       "cfmFlowMetricsIntervals": cfmFlowMetricsIntervals,
       "cfmFlowMetricsInvalidIntervals": cfmFlowMetricsInvalidIntervals,
       "cfmFlowMetricsConditionsProfile": cfmFlowMetricsConditionsProfile,
       "cfmFlowMetricsConditions": cfmFlowMetricsConditions,
       "cfmFlowMetricsAlarms": cfmFlowMetricsAlarms,
       "cfmFlowMetricsAlarmSeverity": cfmFlowMetricsAlarmSeverity,
       "cfmFlowMetricsPkts": cfmFlowMetricsPkts,
       "cfmFlowMetricsOctets": cfmFlowMetricsOctets,
       "cfmFlowMetricsBitRateUnits": cfmFlowMetricsBitRateUnits,
       "cfmFlowMetricsBitRate": cfmFlowMetricsBitRate,
       "cfmFlowMetricsPktRate": cfmFlowMetricsPktRate,
       "cfmFlowMetricsTableChanged": cfmFlowMetricsTableChanged,
       "cfmFlowMetricsIntTable": cfmFlowMetricsIntTable,
       "cfmFlowMetricsIntEntry": cfmFlowMetricsIntEntry,
       "cfmFlowMetricsIntNumber": cfmFlowMetricsIntNumber,
       "cfmFlowMetricsIntValid": cfmFlowMetricsIntValid,
       "cfmFlowMetricsIntTime": cfmFlowMetricsIntTime,
       "cfmFlowMetricsIntConditions": cfmFlowMetricsIntConditions,
       "cfmFlowMetricsIntAlarms": cfmFlowMetricsIntAlarms,
       "cfmFlowMetricsIntAlarmSeverity": cfmFlowMetricsIntAlarmSeverity,
       "cfmFlowMetricsIntPkts": cfmFlowMetricsIntPkts,
       "cfmFlowMetricsIntOctets": cfmFlowMetricsIntOctets,
       "cfmFlowMetricsIntBitRateUnits": cfmFlowMetricsIntBitRateUnits,
       "cfmFlowMetricsIntBitRate": cfmFlowMetricsIntBitRate,
       "cfmFlowMetricsIntPktRate": cfmFlowMetricsIntPktRate,
       "cfmConditions": cfmConditions,
       "cfmConditionTable": cfmConditionTable,
       "cfmConditionEntry": cfmConditionEntry,
       "cfmConditionProfile": cfmConditionProfile,
       "cfmConditionId": cfmConditionId,
       "cfmConditionDescr": cfmConditionDescr,
       "cfmConditionMonitoredElement": cfmConditionMonitoredElement,
       "cfmConditionType": cfmConditionType,
       "cfmConditionThreshRiseScale": cfmConditionThreshRiseScale,
       "cfmConditionThreshRisePrecision": cfmConditionThreshRisePrecision,
       "cfmConditionThreshRise": cfmConditionThreshRise,
       "cfmConditionThreshFallScale": cfmConditionThreshFallScale,
       "cfmConditionThreshFallPrecision": cfmConditionThreshFallPrecision,
       "cfmConditionThreshFall": cfmConditionThreshFall,
       "cfmConditionSampleType": cfmConditionSampleType,
       "cfmConditionSampleWindow": cfmConditionSampleWindow,
       "cfmConditionAlarm": cfmConditionAlarm,
       "cfmConditionAlarmActions": cfmConditionAlarmActions,
       "cfmConditionAlarmSeverity": cfmConditionAlarmSeverity,
       "cfmConditionAlarmGroup": cfmConditionAlarmGroup,
       "cfmConditionTableChanged": cfmConditionTableChanged,
       "cfmAlarmGroups": cfmAlarmGroups,
       "cfmAlarmGroupTable": cfmAlarmGroupTable,
       "cfmAlarmGroupEntry": cfmAlarmGroupEntry,
       "cfmAlarmGroupId": cfmAlarmGroupId,
       "cfmAlarmGroupDescr": cfmAlarmGroupDescr,
       "cfmAlarmGroupConditionsProfile": cfmAlarmGroupConditionsProfile,
       "cfmAlarmGroupConditionId": cfmAlarmGroupConditionId,
       "cfmAlarmGroupFlowSet": cfmAlarmGroupFlowSet,
       "cfmAlarmGroupFlowCount": cfmAlarmGroupFlowCount,
       "cfmAlarmGroupThresholdUnits": cfmAlarmGroupThresholdUnits,
       "cfmAlarmGroupThreshold": cfmAlarmGroupThreshold,
       "cfmAlarmGroupRaised": cfmAlarmGroupRaised,
       "cfmAlarmGroupCurrentCount": cfmAlarmGroupCurrentCount,
       "cfmAlarmGroupTableChanged": cfmAlarmGroupTableChanged,
       "cfmAlarmGroupFlowTable": cfmAlarmGroupFlowTable,
       "cfmAlarmGroupFlowEntry": cfmAlarmGroupFlowEntry,
       "cfmAlarmGroupFlowSetId": cfmAlarmGroupFlowSetId,
       "cfmAlarmGroupFlowMonitorId": cfmAlarmGroupFlowMonitorId,
       "cfmAlarmGroupFlowId": cfmAlarmGroupFlowId,
       "cfmAlarmGroupFlowTableChanged": cfmAlarmGroupFlowTableChanged,
       "cfmAlarmHistory": cfmAlarmHistory,
       "cfmAlarmHistorySize": cfmAlarmHistorySize,
       "cfmAlarmHistoryLastId": cfmAlarmHistoryLastId,
       "cfmAlarmHistoryTable": cfmAlarmHistoryTable,
       "cfmAlarmHistoryEntry": cfmAlarmHistoryEntry,
       "cfmAlarmHistoryId": cfmAlarmHistoryId,
       "cfmAlarmHistoryType": cfmAlarmHistoryType,
       "cfmAlarmHistoryEntity": cfmAlarmHistoryEntity,
       "cfmAlarmHistoryConditionsProfile": cfmAlarmHistoryConditionsProfile,
       "cfmAlarmHistoryConditionId": cfmAlarmHistoryConditionId,
       "cfmAlarmHistorySeverity": cfmAlarmHistorySeverity,
       "cfmAlarmHistoryTime": cfmAlarmHistoryTime,
       "cfmNotify": cfmNotify,
       "cfmNotifyEnable": cfmNotifyEnable,
       "ciscoFlowMonitorMIBConform": ciscoFlowMonitorMIBConform,
       "ciscoFlowMonitorMIBCompliances": ciscoFlowMonitorMIBCompliances,
       "ciscoFlowMonitorCompliance01": ciscoFlowMonitorCompliance01,
       "ciscoFlowMonitorMIBGroups": ciscoFlowMonitorMIBGroups,
       "cfmFlowMonitorGroup": cfmFlowMonitorGroup,
       "cfmFlowGroup": cfmFlowGroup,
       "cfmFlowMetricsGroup": cfmFlowMetricsGroup,
       "cfmFlowConditionsGroup": cfmFlowConditionsGroup,
       "cfmAlarmAggregationGroup": cfmAlarmAggregationGroup,
       "cfmAlarmHistoryGroup": cfmAlarmHistoryGroup,
       "cfmNotifySupportGroup": cfmNotifySupportGroup,
       "cfmNotifyGroup": cfmNotifyGroup,
       "ciscoFlowMonitorMIBIds": ciscoFlowMonitorMIBIds,
       "cfmMonitoredElements": cfmMonitoredElements,
       "cfmeOther": cfmeOther,
       "cfmeFlowCount": cfmeFlowCount,
       "cfmeFlowTimeouts": cfmeFlowTimeouts,
       "cfmeFlowStop": cfmeFlowStop,
       "cfmeFlowCumulativeBitRate": cfmeFlowCumulativeBitRate,
       "cfmeFlowCumulativePktRate": cfmeFlowCumulativePktRate,
       "cfmeFlowBitRate": cfmeFlowBitRate,
       "cfmeFlowPktRate": cfmeFlowPktRate}
)
