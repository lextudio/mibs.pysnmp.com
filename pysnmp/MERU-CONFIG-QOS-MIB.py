# SNMP MIB module (MERU-CONFIG-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:05 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlAdmissionControl,
 MwlDropPolicy,
 MwlDscpType,
 MwlOnOffSwitch,
 MwlQosAction,
 MwlQosCodec,
 MwlQosCodecProtocol,
 MwlQosProtocol,
 MwlQosRulesMatchClass,
 MwlQosRulesMatchClassBits) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlAdmissionControl",
    "MwlDropPolicy",
    "MwlDscpType",
    "MwlOnOffSwitch",
    "MwlQosAction",
    "MwlQosCodec",
    "MwlQosCodecProtocol",
    "MwlQosProtocol",
    "MwlQosRulesMatchClass",
    "MwlQosRulesMatchClassBits")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigQoS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwQosVars_ObjectIdentity = ObjectIdentity
mwQosVars = _MwQosVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1)
)
_MwQosVarsQosOnOff_Type = MwlOnOffSwitch
_MwQosVarsQosOnOff_Object = MibScalar
mwQosVarsQosOnOff = _MwQosVarsQosOnOff_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 1),
    _MwQosVarsQosOnOff_Type()
)
mwQosVarsQosOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosOnOff.setStatus("current")
_MwQosVarsQosAdmissionControl_Type = MwlAdmissionControl
_MwQosVarsQosAdmissionControl_Object = MibScalar
mwQosVarsQosAdmissionControl = _MwQosVarsQosAdmissionControl_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 2),
    _MwQosVarsQosAdmissionControl_Type()
)
mwQosVarsQosAdmissionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosAdmissionControl.setStatus("current")
_MwQosVarsQosDropPolicy_Type = MwlDropPolicy
_MwQosVarsQosDropPolicy_Object = MibScalar
mwQosVarsQosDropPolicy = _MwQosVarsQosDropPolicy_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 3),
    _MwQosVarsQosDropPolicy_Type()
)
mwQosVarsQosDropPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosDropPolicy.setStatus("current")
_MwQosVarsQosDefaultTimeToLive_Type = Unsigned32
_MwQosVarsQosDefaultTimeToLive_Object = MibScalar
mwQosVarsQosDefaultTimeToLive = _MwQosVarsQosDefaultTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 4),
    _MwQosVarsQosDefaultTimeToLive_Type()
)
mwQosVarsQosDefaultTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosDefaultTimeToLive.setStatus("current")
_MwQosVarsQosUdpTimeToLive_Type = Unsigned32
_MwQosVarsQosUdpTimeToLive_Object = MibScalar
mwQosVarsQosUdpTimeToLive = _MwQosVarsQosUdpTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 5),
    _MwQosVarsQosUdpTimeToLive_Type()
)
mwQosVarsQosUdpTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosUdpTimeToLive.setStatus("current")
_MwQosVarsQosTcpTimeToLive_Type = Unsigned32
_MwQosVarsQosTcpTimeToLive_Object = MibScalar
mwQosVarsQosTcpTimeToLive = _MwQosVarsQosTcpTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 6),
    _MwQosVarsQosTcpTimeToLive_Type()
)
mwQosVarsQosTcpTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosTcpTimeToLive.setStatus("current")
_MwQosVarsPercentBWScaling_Type = Unsigned32
_MwQosVarsPercentBWScaling_Object = MibScalar
mwQosVarsPercentBWScaling = _MwQosVarsPercentBWScaling_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 7),
    _MwQosVarsPercentBWScaling_Type()
)
mwQosVarsPercentBWScaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsPercentBWScaling.setStatus("current")
_MwQosVarsQosMaxCallsPerAp_Type = Unsigned32
_MwQosVarsQosMaxCallsPerAp_Object = MibScalar
mwQosVarsQosMaxCallsPerAp = _MwQosVarsQosMaxCallsPerAp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 8),
    _MwQosVarsQosMaxCallsPerAp_Type()
)
mwQosVarsQosMaxCallsPerAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosMaxCallsPerAp.setStatus("current")
_MwQosVarsQosMaxCallsPerInterfRegion_Type = Unsigned32
_MwQosVarsQosMaxCallsPerInterfRegion_Object = MibScalar
mwQosVarsQosMaxCallsPerInterfRegion = _MwQosVarsQosMaxCallsPerInterfRegion_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 9),
    _MwQosVarsQosMaxCallsPerInterfRegion_Type()
)
mwQosVarsQosMaxCallsPerInterfRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosMaxCallsPerInterfRegion.setStatus("current")
_MwQosVarsQosLoadBalanceMaxStationsPerAp_Type = Unsigned32
_MwQosVarsQosLoadBalanceMaxStationsPerAp_Object = MibScalar
mwQosVarsQosLoadBalanceMaxStationsPerAp = _MwQosVarsQosLoadBalanceMaxStationsPerAp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 10),
    _MwQosVarsQosLoadBalanceMaxStationsPerAp_Type()
)
mwQosVarsQosLoadBalanceMaxStationsPerAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosLoadBalanceMaxStationsPerAp.setStatus("current")
_MwQosVarsQosLoadBalanceMaxStationsPerBssid_Type = Unsigned32
_MwQosVarsQosLoadBalanceMaxStationsPerBssid_Object = MibScalar
mwQosVarsQosLoadBalanceMaxStationsPerBssid = _MwQosVarsQosLoadBalanceMaxStationsPerBssid_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 11),
    _MwQosVarsQosLoadBalanceMaxStationsPerBssid_Type()
)
mwQosVarsQosLoadBalanceMaxStationsPerBssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosLoadBalanceMaxStationsPerBssid.setStatus("current")
_MwQosVarsQosLoadBalanceOverflow_Type = MwlOnOffSwitch
_MwQosVarsQosLoadBalanceOverflow_Object = MibScalar
mwQosVarsQosLoadBalanceOverflow = _MwQosVarsQosLoadBalanceOverflow_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 12),
    _MwQosVarsQosLoadBalanceOverflow_Type()
)
mwQosVarsQosLoadBalanceOverflow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosLoadBalanceOverflow.setStatus("current")
_MwQosVarsQosMaxCallsPerBssid_Type = Unsigned32
_MwQosVarsQosMaxCallsPerBssid_Object = MibScalar
mwQosVarsQosMaxCallsPerBssid = _MwQosVarsQosMaxCallsPerBssid_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 13),
    _MwQosVarsQosMaxCallsPerBssid_Type()
)
mwQosVarsQosMaxCallsPerBssid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosMaxCallsPerBssid.setStatus("current")
_MwQosVarsQosCacDeauth_Type = MwlOnOffSwitch
_MwQosVarsQosCacDeauth_Object = MibScalar
mwQosVarsQosCacDeauth = _MwQosVarsQosCacDeauth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 14),
    _MwQosVarsQosCacDeauth_Type()
)
mwQosVarsQosCacDeauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosCacDeauth.setStatus("current")
_MwQosVarsQosStationAssignAge_Type = Unsigned32
_MwQosVarsQosStationAssignAge_Object = MibScalar
mwQosVarsQosStationAssignAge = _MwQosVarsQosStationAssignAge_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 15),
    _MwQosVarsQosStationAssignAge_Type()
)
mwQosVarsQosStationAssignAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosStationAssignAge.setStatus("current")
_MwQosVarsQosSipIdleTimeout_Type = Unsigned32
_MwQosVarsQosSipIdleTimeout_Object = MibScalar
mwQosVarsQosSipIdleTimeout = _MwQosVarsQosSipIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 1, 16),
    _MwQosVarsQosSipIdleTimeout_Type()
)
mwQosVarsQosSipIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwQosVarsQosSipIdleTimeout.setStatus("current")
_MwQosRuleTable_Object = MibTable
mwQosRuleTable = _MwQosRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2)
)
if mibBuilder.loadTexts:
    mwQosRuleTable.setStatus("current")
_MwQosRuleEntry_Object = MibTableRow
mwQosRuleEntry = _MwQosRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1)
)
mwQosRuleEntry.setIndexNames(
    (0, "MERU-CONFIG-QOS-MIB", "mwQosRuleTableIndex"),
)
if mibBuilder.loadTexts:
    mwQosRuleEntry.setStatus("current")
_MwQosRuleTableIndex_Type = Integer32
_MwQosRuleTableIndex_Object = MibTableColumn
mwQosRuleTableIndex = _MwQosRuleTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 1),
    _MwQosRuleTableIndex_Type()
)
mwQosRuleTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwQosRuleTableIndex.setStatus("current")
_MwQosRuleId_Type = Unsigned32
_MwQosRuleId_Object = MibTableColumn
mwQosRuleId = _MwQosRuleId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 2),
    _MwQosRuleId_Type()
)
mwQosRuleId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleId.setStatus("current")
_MwQosRuleDscp_Type = MwlDscpType
_MwQosRuleDscp_Object = MibTableColumn
mwQosRuleDscp = _MwQosRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 3),
    _MwQosRuleDscp_Type()
)
mwQosRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleDscp.setStatus("current")
_MwQosRuleDstIp_Type = IpAddress
_MwQosRuleDstIp_Object = MibTableColumn
mwQosRuleDstIp = _MwQosRuleDstIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 4),
    _MwQosRuleDstIp_Type()
)
mwQosRuleDstIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleDstIp.setStatus("current")
_MwQosRuleSrcIp_Type = IpAddress
_MwQosRuleSrcIp_Object = MibTableColumn
mwQosRuleSrcIp = _MwQosRuleSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 5),
    _MwQosRuleSrcIp_Type()
)
mwQosRuleSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleSrcIp.setStatus("current")
_MwQosRuleAction_Type = MwlQosAction
_MwQosRuleAction_Object = MibTableColumn
mwQosRuleAction = _MwQosRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 6),
    _MwQosRuleAction_Type()
)
mwQosRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleAction.setStatus("current")
_MwQosRuleDstMask_Type = IpAddress
_MwQosRuleDstMask_Object = MibTableColumn
mwQosRuleDstMask = _MwQosRuleDstMask_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 7),
    _MwQosRuleDstMask_Type()
)
mwQosRuleDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleDstMask.setStatus("current")


class _MwQosRuleDstPort_Type(Integer32):
    """Custom type mwQosRuleDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MwQosRuleDstPort_Type.__name__ = "Integer32"
_MwQosRuleDstPort_Object = MibTableColumn
mwQosRuleDstPort = _MwQosRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 8),
    _MwQosRuleDstPort_Type()
)
mwQosRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleDstPort.setStatus("current")
_MwQosRuleSrcMask_Type = IpAddress
_MwQosRuleSrcMask_Object = MibTableColumn
mwQosRuleSrcMask = _MwQosRuleSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 9),
    _MwQosRuleSrcMask_Type()
)
mwQosRuleSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleSrcMask.setStatus("current")


class _MwQosRuleSrcPort_Type(Integer32):
    """Custom type mwQosRuleSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MwQosRuleSrcPort_Type.__name__ = "Integer32"
_MwQosRuleSrcPort_Object = MibTableColumn
mwQosRuleSrcPort = _MwQosRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 10),
    _MwQosRuleSrcPort_Type()
)
mwQosRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleSrcPort.setStatus("current")
_MwQosRuleProtocol_Type = MwlQosProtocol
_MwQosRuleProtocol_Object = MibTableColumn
mwQosRuleProtocol = _MwQosRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 11),
    _MwQosRuleProtocol_Type()
)
mwQosRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleProtocol.setStatus("current")


class _MwQosRulePriority_Type(Integer32):
    """Custom type mwQosRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MwQosRulePriority_Type.__name__ = "Integer32"
_MwQosRulePriority_Object = MibTableColumn
mwQosRulePriority = _MwQosRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 12),
    _MwQosRulePriority_Type()
)
mwQosRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRulePriority.setStatus("current")
_MwQosRuleIdUfcFlag_Type = MwlQosRulesMatchClass
_MwQosRuleIdUfcFlag_Object = MibTableColumn
mwQosRuleIdUfcFlag = _MwQosRuleIdUfcFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 13),
    _MwQosRuleIdUfcFlag_Type()
)
mwQosRuleIdUfcFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleIdUfcFlag.setStatus("current")
_MwQosRuleDstIpFlag_Type = MwlQosRulesMatchClassBits
_MwQosRuleDstIpFlag_Object = MibTableColumn
mwQosRuleDstIpFlag = _MwQosRuleDstIpFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 14),
    _MwQosRuleDstIpFlag_Type()
)
mwQosRuleDstIpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleDstIpFlag.setStatus("current")
_MwQosRuleSrcIpFlag_Type = MwlQosRulesMatchClassBits
_MwQosRuleSrcIpFlag_Object = MibTableColumn
mwQosRuleSrcIpFlag = _MwQosRuleSrcIpFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 15),
    _MwQosRuleSrcIpFlag_Type()
)
mwQosRuleSrcIpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleSrcIpFlag.setStatus("current")


class _MwQosRuleL4Protocol_Type(Integer32):
    """Custom type mwQosRuleL4Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MwQosRuleL4Protocol_Type.__name__ = "Integer32"
_MwQosRuleL4Protocol_Object = MibTableColumn
mwQosRuleL4Protocol = _MwQosRuleL4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 16),
    _MwQosRuleL4Protocol_Type()
)
mwQosRuleL4Protocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleL4Protocol.setStatus("current")
_MwQosRuleDstPortFlag_Type = MwlQosRulesMatchClassBits
_MwQosRuleDstPortFlag_Object = MibTableColumn
mwQosRuleDstPortFlag = _MwQosRuleDstPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 18),
    _MwQosRuleDstPortFlag_Type()
)
mwQosRuleDstPortFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleDstPortFlag.setStatus("current")
_MwQosRuleSrcPortFlag_Type = MwlQosRulesMatchClassBits
_MwQosRuleSrcPortFlag_Object = MibTableColumn
mwQosRuleSrcPortFlag = _MwQosRuleSrcPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 19),
    _MwQosRuleSrcPortFlag_Type()
)
mwQosRuleSrcPortFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleSrcPortFlag.setStatus("current")
_MwQosRuleDstIpUfcFlag_Type = MwlQosRulesMatchClassBits
_MwQosRuleDstIpUfcFlag_Object = MibTableColumn
mwQosRuleDstIpUfcFlag = _MwQosRuleDstIpUfcFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 20),
    _MwQosRuleDstIpUfcFlag_Type()
)
mwQosRuleDstIpUfcFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleDstIpUfcFlag.setStatus("current")
_MwQosRuleSrcIpUfcFlag_Type = MwlQosRulesMatchClassBits
_MwQosRuleSrcIpUfcFlag_Object = MibTableColumn
mwQosRuleSrcIpUfcFlag = _MwQosRuleSrcIpUfcFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 21),
    _MwQosRuleSrcIpUfcFlag_Type()
)
mwQosRuleSrcIpUfcFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleSrcIpUfcFlag.setStatus("current")
_MwQosRuleAvgPacketRate_Type = Unsigned32
_MwQosRuleAvgPacketRate_Object = MibTableColumn
mwQosRuleAvgPacketRate = _MwQosRuleAvgPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 22),
    _MwQosRuleAvgPacketRate_Type()
)
mwQosRuleAvgPacketRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleAvgPacketRate.setStatus("current")
_MwQosRuleDstPortUfcFlag_Type = MwlQosRulesMatchClassBits
_MwQosRuleDstPortUfcFlag_Object = MibTableColumn
mwQosRuleDstPortUfcFlag = _MwQosRuleDstPortUfcFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 23),
    _MwQosRuleDstPortUfcFlag_Type()
)
mwQosRuleDstPortUfcFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleDstPortUfcFlag.setStatus("current")
_MwQosRuleSrcPortUfcFlag_Type = MwlQosRulesMatchClassBits
_MwQosRuleSrcPortUfcFlag_Object = MibTableColumn
mwQosRuleSrcPortUfcFlag = _MwQosRuleSrcPortUfcFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 24),
    _MwQosRuleSrcPortUfcFlag_Type()
)
mwQosRuleSrcPortUfcFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleSrcPortUfcFlag.setStatus("current")
_MwQosRuleL4ProtocolFlag_Type = MwlQosRulesMatchClassBits
_MwQosRuleL4ProtocolFlag_Object = MibTableColumn
mwQosRuleL4ProtocolFlag = _MwQosRuleL4ProtocolFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 25),
    _MwQosRuleL4ProtocolFlag_Type()
)
mwQosRuleL4ProtocolFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleL4ProtocolFlag.setStatus("current")
_MwQosRuleTrafficControl_Type = MwlOnOffSwitch
_MwQosRuleTrafficControl_Object = MibTableColumn
mwQosRuleTrafficControl = _MwQosRuleTrafficControl_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 26),
    _MwQosRuleTrafficControl_Type()
)
mwQosRuleTrafficControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleTrafficControl.setStatus("current")
_MwQosRuleLogging_Type = MwlOnOffSwitch
_MwQosRuleLogging_Object = MibTableColumn
mwQosRuleLogging = _MwQosRuleLogging_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 27),
    _MwQosRuleLogging_Type()
)
mwQosRuleLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleLogging.setStatus("current")
_MwQosRulePacketMinLength_Type = Unsigned32
_MwQosRulePacketMinLength_Object = MibTableColumn
mwQosRulePacketMinLength = _MwQosRulePacketMinLength_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 28),
    _MwQosRulePacketMinLength_Type()
)
mwQosRulePacketMinLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRulePacketMinLength.setStatus("current")
_MwQosRulePacketMaxLength_Type = Unsigned32
_MwQosRulePacketMaxLength_Object = MibTableColumn
mwQosRulePacketMaxLength = _MwQosRulePacketMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 29),
    _MwQosRulePacketMaxLength_Type()
)
mwQosRulePacketMaxLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRulePacketMaxLength.setStatus("current")
_MwQosRuleTokenBucketRate_Type = Unsigned32
_MwQosRuleTokenBucketRate_Object = MibTableColumn
mwQosRuleTokenBucketRate = _MwQosRuleTokenBucketRate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 30),
    _MwQosRuleTokenBucketRate_Type()
)
mwQosRuleTokenBucketRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleTokenBucketRate.setStatus("current")


class _MwQosRuleFirewallFilterId_Type(DisplayString):
    """Custom type mwQosRuleFirewallFilterId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MwQosRuleFirewallFilterId_Type.__name__ = "DisplayString"
_MwQosRuleFirewallFilterId_Object = MibTableColumn
mwQosRuleFirewallFilterId = _MwQosRuleFirewallFilterId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 31),
    _MwQosRuleFirewallFilterId_Type()
)
mwQosRuleFirewallFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleFirewallFilterId.setStatus("current")
_MwQosRuleL4ProtocolUfcFlag_Type = MwlQosRulesMatchClassBits
_MwQosRuleL4ProtocolUfcFlag_Object = MibTableColumn
mwQosRuleL4ProtocolUfcFlag = _MwQosRuleL4ProtocolUfcFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 32),
    _MwQosRuleL4ProtocolUfcFlag_Type()
)
mwQosRuleL4ProtocolUfcFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleL4ProtocolUfcFlag.setStatus("current")
_MwQosRulePacketMinLengthFlag_Type = MwlQosRulesMatchClassBits
_MwQosRulePacketMinLengthFlag_Object = MibTableColumn
mwQosRulePacketMinLengthFlag = _MwQosRulePacketMinLengthFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 33),
    _MwQosRulePacketMinLengthFlag_Type()
)
mwQosRulePacketMinLengthFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRulePacketMinLengthFlag.setStatus("current")
_MwQosRuleFirewallFilterIdFlag_Type = MwlQosRulesMatchClassBits
_MwQosRuleFirewallFilterIdFlag_Object = MibTableColumn
mwQosRuleFirewallFilterIdFlag = _MwQosRuleFirewallFilterIdFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 34),
    _MwQosRuleFirewallFilterIdFlag_Type()
)
mwQosRuleFirewallFilterIdFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleFirewallFilterIdFlag.setStatus("current")
_MwQosRulePacketMinLengthUfcFlag_Type = MwlQosRulesMatchClassBits
_MwQosRulePacketMinLengthUfcFlag_Object = MibTableColumn
mwQosRulePacketMinLengthUfcFlag = _MwQosRulePacketMinLengthUfcFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 35),
    _MwQosRulePacketMinLengthUfcFlag_Type()
)
mwQosRulePacketMinLengthUfcFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRulePacketMinLengthUfcFlag.setStatus("current")
_MwQosRuleFirewallFilterIdUfcFlag_Type = MwlQosRulesMatchClassBits
_MwQosRuleFirewallFilterIdUfcFlag_Object = MibTableColumn
mwQosRuleFirewallFilterIdUfcFlag = _MwQosRuleFirewallFilterIdUfcFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 36),
    _MwQosRuleFirewallFilterIdUfcFlag_Type()
)
mwQosRuleFirewallFilterIdUfcFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleFirewallFilterIdUfcFlag.setStatus("current")


class _MwQosRuleLoggingFrequency_Type(Integer32):
    """Custom type mwQosRuleLoggingFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 60),
    )


_MwQosRuleLoggingFrequency_Type.__name__ = "Integer32"
_MwQosRuleLoggingFrequency_Object = MibTableColumn
mwQosRuleLoggingFrequency = _MwQosRuleLoggingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 37),
    _MwQosRuleLoggingFrequency_Type()
)
mwQosRuleLoggingFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleLoggingFrequency.setStatus("current")
_MwQosRuleRowStatus_Type = RowStatus
_MwQosRuleRowStatus_Object = MibTableColumn
mwQosRuleRowStatus = _MwQosRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 2, 1, 40),
    _MwQosRuleRowStatus_Type()
)
mwQosRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosRuleRowStatus.setStatus("current")
_MwQosCodecTranslRuleTable_Object = MibTable
mwQosCodecTranslRuleTable = _MwQosCodecTranslRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3)
)
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleTable.setStatus("current")
_MwQosCodecTranslRuleEntry_Object = MibTableRow
mwQosCodecTranslRuleEntry = _MwQosCodecTranslRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1)
)
mwQosCodecTranslRuleEntry.setIndexNames(
    (0, "MERU-CONFIG-QOS-MIB", "mwQosCodecTranslRuleTableIndex"),
)
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleEntry.setStatus("current")
_MwQosCodecTranslRuleTableIndex_Type = Integer32
_MwQosCodecTranslRuleTableIndex_Object = MibTableColumn
mwQosCodecTranslRuleTableIndex = _MwQosCodecTranslRuleTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 1),
    _MwQosCodecTranslRuleTableIndex_Type()
)
mwQosCodecTranslRuleTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleTableIndex.setStatus("current")
_MwQosCodecTranslRuleId_Type = Unsigned32
_MwQosCodecTranslRuleId_Object = MibTableColumn
mwQosCodecTranslRuleId = _MwQosCodecTranslRuleId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 2),
    _MwQosCodecTranslRuleId_Type()
)
mwQosCodecTranslRuleId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleId.setStatus("current")
_MwQosCodecTranslRuleQosCtrProtocol_Type = MwlQosCodecProtocol
_MwQosCodecTranslRuleQosCtrProtocol_Object = MibTableColumn
mwQosCodecTranslRuleQosCtrProtocol = _MwQosCodecTranslRuleQosCtrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 3),
    _MwQosCodecTranslRuleQosCtrProtocol_Type()
)
mwQosCodecTranslRuleQosCtrProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleQosCtrProtocol.setStatus("current")
_MwQosCodecTranslRuleQosCtrCodecEnum_Type = MwlQosCodec
_MwQosCodecTranslRuleQosCtrCodecEnum_Object = MibTableColumn
mwQosCodecTranslRuleQosCtrCodecEnum = _MwQosCodecTranslRuleQosCtrCodecEnum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 4),
    _MwQosCodecTranslRuleQosCtrCodecEnum_Type()
)
mwQosCodecTranslRuleQosCtrCodecEnum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleQosCtrCodecEnum.setStatus("current")
_MwQosCodecTranslRuleQosCtrRspecRate_Type = Unsigned32
_MwQosCodecTranslRuleQosCtrRspecRate_Object = MibTableColumn
mwQosCodecTranslRuleQosCtrRspecRate = _MwQosCodecTranslRuleQosCtrRspecRate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 5),
    _MwQosCodecTranslRuleQosCtrRspecRate_Type()
)
mwQosCodecTranslRuleQosCtrRspecRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleQosCtrRspecRate.setStatus("current")
_MwQosCodecTranslRuleQosCtrRspecSlack_Type = Unsigned32
_MwQosCodecTranslRuleQosCtrRspecSlack_Object = MibTableColumn
mwQosCodecTranslRuleQosCtrRspecSlack = _MwQosCodecTranslRuleQosCtrRspecSlack_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 6),
    _MwQosCodecTranslRuleQosCtrRspecSlack_Type()
)
mwQosCodecTranslRuleQosCtrRspecSlack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleQosCtrRspecSlack.setStatus("current")
_MwQosCodecTranslRuleQosCtrSampleRate_Type = Unsigned32
_MwQosCodecTranslRuleQosCtrSampleRate_Object = MibTableColumn
mwQosCodecTranslRuleQosCtrSampleRate = _MwQosCodecTranslRuleQosCtrSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 7),
    _MwQosCodecTranslRuleQosCtrSampleRate_Type()
)
mwQosCodecTranslRuleQosCtrSampleRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleQosCtrSampleRate.setStatus("current")
_MwQosCodecTranslRuleQosCtrTspecPeakRate_Type = Unsigned32
_MwQosCodecTranslRuleQosCtrTspecPeakRate_Object = MibTableColumn
mwQosCodecTranslRuleQosCtrTspecPeakRate = _MwQosCodecTranslRuleQosCtrTspecPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 8),
    _MwQosCodecTranslRuleQosCtrTspecPeakRate_Type()
)
mwQosCodecTranslRuleQosCtrTspecPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleQosCtrTspecPeakRate.setStatus("current")
_MwQosCodecTranslRuleQosCtrTspecMinPolicedUnit_Type = Unsigned32
_MwQosCodecTranslRuleQosCtrTspecMinPolicedUnit_Object = MibTableColumn
mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit = _MwQosCodecTranslRuleQosCtrTspecMinPolicedUnit_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 9),
    _MwQosCodecTranslRuleQosCtrTspecMinPolicedUnit_Type()
)
mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit.setStatus("current")
_MwQosCodecTranslRuleQosCtrTspecTokenBucketRate_Type = Unsigned32
_MwQosCodecTranslRuleQosCtrTspecTokenBucketRate_Object = MibTableColumn
mwQosCodecTranslRuleQosCtrTspecTokenBucketRate = _MwQosCodecTranslRuleQosCtrTspecTokenBucketRate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 10),
    _MwQosCodecTranslRuleQosCtrTspecTokenBucketRate_Type()
)
mwQosCodecTranslRuleQosCtrTspecTokenBucketRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleQosCtrTspecTokenBucketRate.setStatus("current")
_MwQosCodecTranslRuleQosCtrTspecTokenBucketSize_Type = Unsigned32
_MwQosCodecTranslRuleQosCtrTspecTokenBucketSize_Object = MibTableColumn
mwQosCodecTranslRuleQosCtrTspecTokenBucketSize = _MwQosCodecTranslRuleQosCtrTspecTokenBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 11),
    _MwQosCodecTranslRuleQosCtrTspecTokenBucketSize_Type()
)
mwQosCodecTranslRuleQosCtrTspecTokenBucketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleQosCtrTspecTokenBucketSize.setStatus("current")
_MwQosCodecTranslRuleQosCtrTspecMaxDatagramSize_Type = Unsigned32
_MwQosCodecTranslRuleQosCtrTspecMaxDatagramSize_Object = MibTableColumn
mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize = _MwQosCodecTranslRuleQosCtrTspecMaxDatagramSize_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 12),
    _MwQosCodecTranslRuleQosCtrTspecMaxDatagramSize_Type()
)
mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize.setStatus("current")
_MwQosCodecTranslRuleRowStatus_Type = RowStatus
_MwQosCodecTranslRuleRowStatus_Object = MibTableColumn
mwQosCodecTranslRuleRowStatus = _MwQosCodecTranslRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 8, 3, 1, 14),
    _MwQosCodecTranslRuleRowStatus_Type()
)
mwQosCodecTranslRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwQosCodecTranslRuleRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-QOS-MIB",
    **{"mwConfigQoS": mwConfigQoS,
       "mwQosVars": mwQosVars,
       "mwQosVarsQosOnOff": mwQosVarsQosOnOff,
       "mwQosVarsQosAdmissionControl": mwQosVarsQosAdmissionControl,
       "mwQosVarsQosDropPolicy": mwQosVarsQosDropPolicy,
       "mwQosVarsQosDefaultTimeToLive": mwQosVarsQosDefaultTimeToLive,
       "mwQosVarsQosUdpTimeToLive": mwQosVarsQosUdpTimeToLive,
       "mwQosVarsQosTcpTimeToLive": mwQosVarsQosTcpTimeToLive,
       "mwQosVarsPercentBWScaling": mwQosVarsPercentBWScaling,
       "mwQosVarsQosMaxCallsPerAp": mwQosVarsQosMaxCallsPerAp,
       "mwQosVarsQosMaxCallsPerInterfRegion": mwQosVarsQosMaxCallsPerInterfRegion,
       "mwQosVarsQosLoadBalanceMaxStationsPerAp": mwQosVarsQosLoadBalanceMaxStationsPerAp,
       "mwQosVarsQosLoadBalanceMaxStationsPerBssid": mwQosVarsQosLoadBalanceMaxStationsPerBssid,
       "mwQosVarsQosLoadBalanceOverflow": mwQosVarsQosLoadBalanceOverflow,
       "mwQosVarsQosMaxCallsPerBssid": mwQosVarsQosMaxCallsPerBssid,
       "mwQosVarsQosCacDeauth": mwQosVarsQosCacDeauth,
       "mwQosVarsQosStationAssignAge": mwQosVarsQosStationAssignAge,
       "mwQosVarsQosSipIdleTimeout": mwQosVarsQosSipIdleTimeout,
       "mwQosRuleTable": mwQosRuleTable,
       "mwQosRuleEntry": mwQosRuleEntry,
       "mwQosRuleTableIndex": mwQosRuleTableIndex,
       "mwQosRuleId": mwQosRuleId,
       "mwQosRuleDscp": mwQosRuleDscp,
       "mwQosRuleDstIp": mwQosRuleDstIp,
       "mwQosRuleSrcIp": mwQosRuleSrcIp,
       "mwQosRuleAction": mwQosRuleAction,
       "mwQosRuleDstMask": mwQosRuleDstMask,
       "mwQosRuleDstPort": mwQosRuleDstPort,
       "mwQosRuleSrcMask": mwQosRuleSrcMask,
       "mwQosRuleSrcPort": mwQosRuleSrcPort,
       "mwQosRuleProtocol": mwQosRuleProtocol,
       "mwQosRulePriority": mwQosRulePriority,
       "mwQosRuleIdUfcFlag": mwQosRuleIdUfcFlag,
       "mwQosRuleDstIpFlag": mwQosRuleDstIpFlag,
       "mwQosRuleSrcIpFlag": mwQosRuleSrcIpFlag,
       "mwQosRuleL4Protocol": mwQosRuleL4Protocol,
       "mwQosRuleDstPortFlag": mwQosRuleDstPortFlag,
       "mwQosRuleSrcPortFlag": mwQosRuleSrcPortFlag,
       "mwQosRuleDstIpUfcFlag": mwQosRuleDstIpUfcFlag,
       "mwQosRuleSrcIpUfcFlag": mwQosRuleSrcIpUfcFlag,
       "mwQosRuleAvgPacketRate": mwQosRuleAvgPacketRate,
       "mwQosRuleDstPortUfcFlag": mwQosRuleDstPortUfcFlag,
       "mwQosRuleSrcPortUfcFlag": mwQosRuleSrcPortUfcFlag,
       "mwQosRuleL4ProtocolFlag": mwQosRuleL4ProtocolFlag,
       "mwQosRuleTrafficControl": mwQosRuleTrafficControl,
       "mwQosRuleLogging": mwQosRuleLogging,
       "mwQosRulePacketMinLength": mwQosRulePacketMinLength,
       "mwQosRulePacketMaxLength": mwQosRulePacketMaxLength,
       "mwQosRuleTokenBucketRate": mwQosRuleTokenBucketRate,
       "mwQosRuleFirewallFilterId": mwQosRuleFirewallFilterId,
       "mwQosRuleL4ProtocolUfcFlag": mwQosRuleL4ProtocolUfcFlag,
       "mwQosRulePacketMinLengthFlag": mwQosRulePacketMinLengthFlag,
       "mwQosRuleFirewallFilterIdFlag": mwQosRuleFirewallFilterIdFlag,
       "mwQosRulePacketMinLengthUfcFlag": mwQosRulePacketMinLengthUfcFlag,
       "mwQosRuleFirewallFilterIdUfcFlag": mwQosRuleFirewallFilterIdUfcFlag,
       "mwQosRuleLoggingFrequency": mwQosRuleLoggingFrequency,
       "mwQosRuleRowStatus": mwQosRuleRowStatus,
       "mwQosCodecTranslRuleTable": mwQosCodecTranslRuleTable,
       "mwQosCodecTranslRuleEntry": mwQosCodecTranslRuleEntry,
       "mwQosCodecTranslRuleTableIndex": mwQosCodecTranslRuleTableIndex,
       "mwQosCodecTranslRuleId": mwQosCodecTranslRuleId,
       "mwQosCodecTranslRuleQosCtrProtocol": mwQosCodecTranslRuleQosCtrProtocol,
       "mwQosCodecTranslRuleQosCtrCodecEnum": mwQosCodecTranslRuleQosCtrCodecEnum,
       "mwQosCodecTranslRuleQosCtrRspecRate": mwQosCodecTranslRuleQosCtrRspecRate,
       "mwQosCodecTranslRuleQosCtrRspecSlack": mwQosCodecTranslRuleQosCtrRspecSlack,
       "mwQosCodecTranslRuleQosCtrSampleRate": mwQosCodecTranslRuleQosCtrSampleRate,
       "mwQosCodecTranslRuleQosCtrTspecPeakRate": mwQosCodecTranslRuleQosCtrTspecPeakRate,
       "mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit": mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit,
       "mwQosCodecTranslRuleQosCtrTspecTokenBucketRate": mwQosCodecTranslRuleQosCtrTspecTokenBucketRate,
       "mwQosCodecTranslRuleQosCtrTspecTokenBucketSize": mwQosCodecTranslRuleQosCtrTspecTokenBucketSize,
       "mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize": mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize,
       "mwQosCodecTranslRuleRowStatus": mwQosCodecTranslRuleRowStatus}
)
