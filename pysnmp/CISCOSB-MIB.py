# SNMP MIB module (CISCOSB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:53 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

switch001 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101)
)
switch001.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions



class Percents(Integer32):
    """Custom type Percents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class VlanPriority(Integer32):
    """Custom type VlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RndNotifications_ObjectIdentity = ObjectIdentity
rndNotifications = _RndNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0)
)
if mibBuilder.loadTexts:
    rndNotifications.setStatus("current")
_RndMng_ObjectIdentity = ObjectIdentity
rndMng = _RndMng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1)
)
_RndDeviceParams_ObjectIdentity = ObjectIdentity
rndDeviceParams = _RndDeviceParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 2)
)
_RndBootP_ObjectIdentity = ObjectIdentity
rndBootP = _RndBootP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 24)
)
_IpSpec_ObjectIdentity = ObjectIdentity
ipSpec = _IpSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 26)
)
_RsTunning_ObjectIdentity = ObjectIdentity
rsTunning = _RsTunning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 29)
)
_RndApplications_ObjectIdentity = ObjectIdentity
rndApplications = _RndApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35)
)
_RsUDP_ObjectIdentity = ObjectIdentity
rsUDP = _RsUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 42)
)
_SwInterfaces_ObjectIdentity = ObjectIdentity
swInterfaces = _SwInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 43)
)
_RlIPmulticast_ObjectIdentity = ObjectIdentity
rlIPmulticast = _RlIPmulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 46)
)
_RlFFT_ObjectIdentity = ObjectIdentity
rlFFT = _RlFFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 47)
)
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48)
)
_RlRmonControl_ObjectIdentity = ObjectIdentity
rlRmonControl = _RlRmonControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 49)
)
_RlBrgMacSwitch_ObjectIdentity = ObjectIdentity
rlBrgMacSwitch = _RlBrgMacSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50)
)
_RlExperience_ObjectIdentity = ObjectIdentity
rlExperience = _RlExperience_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 51)
)
_RlCli_ObjectIdentity = ObjectIdentity
rlCli = _RlCli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52)
)
_RlPhysicalDescription_ObjectIdentity = ObjectIdentity
rlPhysicalDescription = _RlPhysicalDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 53)
)
_RlIfInterfaces_ObjectIdentity = ObjectIdentity
rlIfInterfaces = _RlIfInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 54)
)
_RlMacMulticast_ObjectIdentity = ObjectIdentity
rlMacMulticast = _RlMacMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55)
)
_RlGalileo_ObjectIdentity = ObjectIdentity
rlGalileo = _RlGalileo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 56)
)
_RlpBridgeMIBObjects_ObjectIdentity = ObjectIdentity
rlpBridgeMIBObjects = _RlpBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 57)
)
_RlTelnet_ObjectIdentity = ObjectIdentity
rlTelnet = _RlTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 58)
)
_RlPolicy_ObjectIdentity = ObjectIdentity
rlPolicy = _RlPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 59)
)
_RlArpSpoofing_ObjectIdentity = ObjectIdentity
rlArpSpoofing = _RlArpSpoofing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 60)
)
_RlMir_ObjectIdentity = ObjectIdentity
rlMir = _RlMir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 61)
)
_RlIpMRouteStdMIB_ObjectIdentity = ObjectIdentity
rlIpMRouteStdMIB = _RlIpMRouteStdMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 62)
)
_Rl3sw2swTables_ObjectIdentity = ObjectIdentity
rl3sw2swTables = _Rl3sw2swTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 63)
)
_RlGvrp_ObjectIdentity = ObjectIdentity
rlGvrp = _RlGvrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 64)
)
_RlDot3adAgg_ObjectIdentity = ObjectIdentity
rlDot3adAgg = _RlDot3adAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 65)
)
_RlEmbWeb_ObjectIdentity = ObjectIdentity
rlEmbWeb = _RlEmbWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 66)
)
_RlSwPackageVersion_ObjectIdentity = ObjectIdentity
rlSwPackageVersion = _RlSwPackageVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 67)
)
_RlBroadcom_ObjectIdentity = ObjectIdentity
rlBroadcom = _RlBroadcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 68)
)
_RlMultiSessionTerminal_ObjectIdentity = ObjectIdentity
rlMultiSessionTerminal = _RlMultiSessionTerminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 69)
)
_RlRCli_ObjectIdentity = ObjectIdentity
rlRCli = _RlRCli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 70)
)
_RlBgp_ObjectIdentity = ObjectIdentity
rlBgp = _RlBgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 71)
)
_RlAgentsCapabilitiesGroups_ObjectIdentity = ObjectIdentity
rlAgentsCapabilitiesGroups = _RlAgentsCapabilitiesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 72)
)
_RlAggregateVlan_ObjectIdentity = ObjectIdentity
rlAggregateVlan = _RlAggregateVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 73)
)
_RlGmrp_ObjectIdentity = ObjectIdentity
rlGmrp = _RlGmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 75)
)
_RlDhcpCl_ObjectIdentity = ObjectIdentity
rlDhcpCl = _RlDhcpCl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76)
)
_RlStormCtrl_ObjectIdentity = ObjectIdentity
rlStormCtrl = _RlStormCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 77)
)
_RlSsh_ObjectIdentity = ObjectIdentity
rlSsh = _RlSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 78)
)
_RlAAA_ObjectIdentity = ObjectIdentity
rlAAA = _RlAAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 79)
)
_RlRadius_ObjectIdentity = ObjectIdentity
rlRadius = _RlRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 80)
)
_RlTraceRoute_ObjectIdentity = ObjectIdentity
rlTraceRoute = _RlTraceRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 81)
)
_RlSyslog_ObjectIdentity = ObjectIdentity
rlSyslog = _RlSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 82)
)
_RlEnv_ObjectIdentity = ObjectIdentity
rlEnv = _RlEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83)
)
_RlSmon_ObjectIdentity = ObjectIdentity
rlSmon = _RlSmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 84)
)
_RlSocket_ObjectIdentity = ObjectIdentity
rlSocket = _RlSocket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 85)
)
_RlDigitalKeyManage_ObjectIdentity = ObjectIdentity
rlDigitalKeyManage = _RlDigitalKeyManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86)
)
_RlCopy_ObjectIdentity = ObjectIdentity
rlCopy = _RlCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 87)
)
_RlQosCliMib_ObjectIdentity = ObjectIdentity
rlQosCliMib = _RlQosCliMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88)
)
_RlMngInf_ObjectIdentity = ObjectIdentity
rlMngInf = _RlMngInf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 89)
)
_RlPhy_ObjectIdentity = ObjectIdentity
rlPhy = _RlPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 90)
)
_RlJumboFrames_ObjectIdentity = ObjectIdentity
rlJumboFrames = _RlJumboFrames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91)
)
_RlTimeSynchronization_ObjectIdentity = ObjectIdentity
rlTimeSynchronization = _RlTimeSynchronization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 92)
)
_RlDnsCl_ObjectIdentity = ObjectIdentity
rlDnsCl = _RlDnsCl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 93)
)
_RlCDB_ObjectIdentity = ObjectIdentity
rlCDB = _RlCDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94)
)
_Rldot1x_ObjectIdentity = ObjectIdentity
rldot1x = _Rldot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 95)
)
_RlFile_ObjectIdentity = ObjectIdentity
rlFile = _RlFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 96)
)
_RlAAAEap_ObjectIdentity = ObjectIdentity
rlAAAEap = _RlAAAEap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 97)
)
_RlSNMP_ObjectIdentity = ObjectIdentity
rlSNMP = _RlSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 98)
)
_RlSsl_ObjectIdentity = ObjectIdentity
rlSsl = _RlSsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 100)
)
_RlMacBasePrio_ObjectIdentity = ObjectIdentity
rlMacBasePrio = _RlMacBasePrio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 101)
)
_RlWlanAccessPoint_ObjectIdentity = ObjectIdentity
rlWlanAccessPoint = _RlWlanAccessPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 102)
)
_RlLocalization_ObjectIdentity = ObjectIdentity
rlLocalization = _RlLocalization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 103)
)
_RlRs232_ObjectIdentity = ObjectIdentity
rlRs232 = _RlRs232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 104)
)
_RlNicRedundancy_ObjectIdentity = ObjectIdentity
rlNicRedundancy = _RlNicRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 105)
)
_RlAmap_ObjectIdentity = ObjectIdentity
rlAmap = _RlAmap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 106)
)
_RlStack_ObjectIdentity = ObjectIdentity
rlStack = _RlStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 107)
)
_RlPoe_ObjectIdentity = ObjectIdentity
rlPoe = _RlPoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 108)
)
_RlUPnP_ObjectIdentity = ObjectIdentity
rlUPnP = _RlUPnP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 109)
)
_RlLldp_ObjectIdentity = ObjectIdentity
rlLldp = _RlLldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 110)
)
_RlOib_ObjectIdentity = ObjectIdentity
rlOib = _RlOib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 111)
)
_RlBridgeSecurity_ObjectIdentity = ObjectIdentity
rlBridgeSecurity = _RlBridgeSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 112)
)
_RlDhcpSpoofing_ObjectIdentity = ObjectIdentity
rlDhcpSpoofing = _RlDhcpSpoofing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 113)
)
_RlBonjour_ObjectIdentity = ObjectIdentity
rlBonjour = _RlBonjour_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114)
)
_RlCiscoSmartMIB_ObjectIdentity = ObjectIdentity
rlCiscoSmartMIB = _RlCiscoSmartMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 115)
)
_RlBrgMulticast_ObjectIdentity = ObjectIdentity
rlBrgMulticast = _RlBrgMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116)
)
_RlBrgMcMngr_ObjectIdentity = ObjectIdentity
rlBrgMcMngr = _RlBrgMcMngr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 117)
)
_RlGlobalIpAddrTable_ObjectIdentity = ObjectIdentity
rlGlobalIpAddrTable = _RlGlobalIpAddrTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 118)
)
_DlPrivate_ObjectIdentity = ObjectIdentity
dlPrivate = _DlPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 119)
)
_RlSecuritySuiteMib_ObjectIdentity = ObjectIdentity
rlSecuritySuiteMib = _RlSecuritySuiteMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120)
)
_RlIntel_ObjectIdentity = ObjectIdentity
rlIntel = _RlIntel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 121)
)
_RlTunnel_ObjectIdentity = ObjectIdentity
rlTunnel = _RlTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122)
)
_RlAutoUpdate_ObjectIdentity = ObjectIdentity
rlAutoUpdate = _RlAutoUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 123)
)
_RlCpuCounters_ObjectIdentity = ObjectIdentity
rlCpuCounters = _RlCpuCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 124)
)
_RlLbd_ObjectIdentity = ObjectIdentity
rlLbd = _RlLbd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 127)
)
_RlErrdisableRecovery_ObjectIdentity = ObjectIdentity
rlErrdisableRecovery = _RlErrdisableRecovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128)
)
_RlIPv6_ObjectIdentity = ObjectIdentity
rlIPv6 = _RlIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 129)
)
_RlActionAcl_ObjectIdentity = ObjectIdentity
rlActionAcl = _RlActionAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 130)
)
_RlSafeGuard_ObjectIdentity = ObjectIdentity
rlSafeGuard = _RlSafeGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 131)
)
_RlProtectedPorts_ObjectIdentity = ObjectIdentity
rlProtectedPorts = _RlProtectedPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 132)
)
_RlBanner_ObjectIdentity = ObjectIdentity
rlBanner = _RlBanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133)
)
_RlGreenEth_ObjectIdentity = ObjectIdentity
rlGreenEth = _RlGreenEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134)
)
_RlDlf_ObjectIdentity = ObjectIdentity
rlDlf = _RlDlf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 135)
)
_RlVlanTrunking_ObjectIdentity = ObjectIdentity
rlVlanTrunking = _RlVlanTrunking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 136)
)
_RlCdp_ObjectIdentity = ObjectIdentity
rlCdp = _RlCdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 137)
)
_RlTrafficSeg_ObjectIdentity = ObjectIdentity
rlTrafficSeg = _RlTrafficSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 138)
)
_RlImpbFeatures_ObjectIdentity = ObjectIdentity
rlImpbFeatures = _RlImpbFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 139)
)
_RlSmartPorts_ObjectIdentity = ObjectIdentity
rlSmartPorts = _RlSmartPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 140)
)
_RlStatistics_ObjectIdentity = ObjectIdentity
rlStatistics = _RlStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 141)
)
_RlDeleteImg_ObjectIdentity = ObjectIdentity
rlDeleteImg = _RlDeleteImg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 142)
)
_RlCustom1BonjourService_ObjectIdentity = ObjectIdentity
rlCustom1BonjourService = _RlCustom1BonjourService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 143)
)
_RlSpecialBpdu_ObjectIdentity = ObjectIdentity
rlSpecialBpdu = _RlSpecialBpdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144)
)
_RlTBIMib_ObjectIdentity = ObjectIdentity
rlTBIMib = _RlTBIMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 145)
)
_RlWeightedRandomTailDrop_ObjectIdentity = ObjectIdentity
rlWeightedRandomTailDrop = _RlWeightedRandomTailDrop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146)
)
_RlsFlowMib_ObjectIdentity = ObjectIdentity
rlsFlowMib = _RlsFlowMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 147)
)
_RlPfcMib_ObjectIdentity = ObjectIdentity
rlPfcMib = _RlPfcMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 148)
)
_RlEee_ObjectIdentity = ObjectIdentity
rlEee = _RlEee_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 149)
)
_RlEventsMib_ObjectIdentity = ObjectIdentity
rlEventsMib = _RlEventsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 150)
)
_RlWlanMIB_ObjectIdentity = ObjectIdentity
rlWlanMIB = _RlWlanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 200)
)
_RlEtsMib_ObjectIdentity = ObjectIdentity
rlEtsMib = _RlEtsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 201)
)
_RlQcnMib_ObjectIdentity = ObjectIdentity
rlQcnMib = _RlQcnMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 202)
)
_RlSctMib_ObjectIdentity = ObjectIdentity
rlSctMib = _RlSctMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203)
)
_RlSysmngMib_ObjectIdentity = ObjectIdentity
rlSysmngMib = _RlSysmngMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 204)
)
_RlFip_ObjectIdentity = ObjectIdentity
rlFip = _RlFip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 205)
)
_RlDebugCapabilities_ObjectIdentity = ObjectIdentity
rlDebugCapabilities = _RlDebugCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 206)
)
_RlIpStdAcl_ObjectIdentity = ObjectIdentity
rlIpStdAcl = _RlIpStdAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 207)
)
_RlWBA_ObjectIdentity = ObjectIdentity
rlWBA = _RlWBA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 208)
)
_RlSecSd_ObjectIdentity = ObjectIdentity
rlSecSd = _RlSecSd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209)
)
_RlOspf_ObjectIdentity = ObjectIdentity
rlOspf = _RlOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 210)
)
_RlRtRedist_ObjectIdentity = ObjectIdentity
rlRtRedist = _RlRtRedist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 211)
)
_RlIpPrefList_ObjectIdentity = ObjectIdentity
rlIpPrefList = _RlIpPrefList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 212)
)
_RlVoipSnoop_ObjectIdentity = ObjectIdentity
rlVoipSnoop = _RlVoipSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 213)
)
_RlDhcpv6_ObjectIdentity = ObjectIdentity
rlDhcpv6 = _RlDhcpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214)
)
_RlIpv6Fhs_ObjectIdentity = ObjectIdentity
rlIpv6Fhs = _RlIpv6Fhs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 215)
)
_RlInventoryEnt_ObjectIdentity = ObjectIdentity
rlInventoryEnt = _RlInventoryEnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217)
)
_RlUdld_ObjectIdentity = ObjectIdentity
rlUdld = _RlUdld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218)
)
_RndEndOfMibGroup_ObjectIdentity = ObjectIdentity
rndEndOfMibGroup = _RndEndOfMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1000)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-MIB",
    **{"Percents": Percents,
       "NetNumber": NetNumber,
       "VlanPriority": VlanPriority,
       "switch001": switch001,
       "rndNotifications": rndNotifications,
       "rndMng": rndMng,
       "rndDeviceParams": rndDeviceParams,
       "rndBootP": rndBootP,
       "ipSpec": ipSpec,
       "rsTunning": rsTunning,
       "rndApplications": rndApplications,
       "rsUDP": rsUDP,
       "swInterfaces": swInterfaces,
       "rlIPmulticast": rlIPmulticast,
       "rlFFT": rlFFT,
       "vlan": vlan,
       "rlRmonControl": rlRmonControl,
       "rlBrgMacSwitch": rlBrgMacSwitch,
       "rlExperience": rlExperience,
       "rlCli": rlCli,
       "rlPhysicalDescription": rlPhysicalDescription,
       "rlIfInterfaces": rlIfInterfaces,
       "rlMacMulticast": rlMacMulticast,
       "rlGalileo": rlGalileo,
       "rlpBridgeMIBObjects": rlpBridgeMIBObjects,
       "rlTelnet": rlTelnet,
       "rlPolicy": rlPolicy,
       "rlArpSpoofing": rlArpSpoofing,
       "rlMir": rlMir,
       "rlIpMRouteStdMIB": rlIpMRouteStdMIB,
       "rl3sw2swTables": rl3sw2swTables,
       "rlGvrp": rlGvrp,
       "rlDot3adAgg": rlDot3adAgg,
       "rlEmbWeb": rlEmbWeb,
       "rlSwPackageVersion": rlSwPackageVersion,
       "rlBroadcom": rlBroadcom,
       "rlMultiSessionTerminal": rlMultiSessionTerminal,
       "rlRCli": rlRCli,
       "rlBgp": rlBgp,
       "rlAgentsCapabilitiesGroups": rlAgentsCapabilitiesGroups,
       "rlAggregateVlan": rlAggregateVlan,
       "rlGmrp": rlGmrp,
       "rlDhcpCl": rlDhcpCl,
       "rlStormCtrl": rlStormCtrl,
       "rlSsh": rlSsh,
       "rlAAA": rlAAA,
       "rlRadius": rlRadius,
       "rlTraceRoute": rlTraceRoute,
       "rlSyslog": rlSyslog,
       "rlEnv": rlEnv,
       "rlSmon": rlSmon,
       "rlSocket": rlSocket,
       "rlDigitalKeyManage": rlDigitalKeyManage,
       "rlCopy": rlCopy,
       "rlQosCliMib": rlQosCliMib,
       "rlMngInf": rlMngInf,
       "rlPhy": rlPhy,
       "rlJumboFrames": rlJumboFrames,
       "rlTimeSynchronization": rlTimeSynchronization,
       "rlDnsCl": rlDnsCl,
       "rlCDB": rlCDB,
       "rldot1x": rldot1x,
       "rlFile": rlFile,
       "rlAAAEap": rlAAAEap,
       "rlSNMP": rlSNMP,
       "rlSsl": rlSsl,
       "rlMacBasePrio": rlMacBasePrio,
       "rlWlanAccessPoint": rlWlanAccessPoint,
       "rlLocalization": rlLocalization,
       "rlRs232": rlRs232,
       "rlNicRedundancy": rlNicRedundancy,
       "rlAmap": rlAmap,
       "rlStack": rlStack,
       "rlPoe": rlPoe,
       "rlUPnP": rlUPnP,
       "rlLldp": rlLldp,
       "rlOib": rlOib,
       "rlBridgeSecurity": rlBridgeSecurity,
       "rlDhcpSpoofing": rlDhcpSpoofing,
       "rlBonjour": rlBonjour,
       "rlCiscoSmartMIB": rlCiscoSmartMIB,
       "rlBrgMulticast": rlBrgMulticast,
       "rlBrgMcMngr": rlBrgMcMngr,
       "rlGlobalIpAddrTable": rlGlobalIpAddrTable,
       "dlPrivate": dlPrivate,
       "rlSecuritySuiteMib": rlSecuritySuiteMib,
       "rlIntel": rlIntel,
       "rlTunnel": rlTunnel,
       "rlAutoUpdate": rlAutoUpdate,
       "rlCpuCounters": rlCpuCounters,
       "rlLbd": rlLbd,
       "rlErrdisableRecovery": rlErrdisableRecovery,
       "rlIPv6": rlIPv6,
       "rlActionAcl": rlActionAcl,
       "rlSafeGuard": rlSafeGuard,
       "rlProtectedPorts": rlProtectedPorts,
       "rlBanner": rlBanner,
       "rlGreenEth": rlGreenEth,
       "rlDlf": rlDlf,
       "rlVlanTrunking": rlVlanTrunking,
       "rlCdp": rlCdp,
       "rlTrafficSeg": rlTrafficSeg,
       "rlImpbFeatures": rlImpbFeatures,
       "rlSmartPorts": rlSmartPorts,
       "rlStatistics": rlStatistics,
       "rlDeleteImg": rlDeleteImg,
       "rlCustom1BonjourService": rlCustom1BonjourService,
       "rlSpecialBpdu": rlSpecialBpdu,
       "rlTBIMib": rlTBIMib,
       "rlWeightedRandomTailDrop": rlWeightedRandomTailDrop,
       "rlsFlowMib": rlsFlowMib,
       "rlPfcMib": rlPfcMib,
       "rlEee": rlEee,
       "rlEventsMib": rlEventsMib,
       "rlWlanMIB": rlWlanMIB,
       "rlEtsMib": rlEtsMib,
       "rlQcnMib": rlQcnMib,
       "rlSctMib": rlSctMib,
       "rlSysmngMib": rlSysmngMib,
       "rlFip": rlFip,
       "rlDebugCapabilities": rlDebugCapabilities,
       "rlIpStdAcl": rlIpStdAcl,
       "rlWBA": rlWBA,
       "rlSecSd": rlSecSd,
       "rlOspf": rlOspf,
       "rlRtRedist": rlRtRedist,
       "rlIpPrefList": rlIpPrefList,
       "rlVoipSnoop": rlVoipSnoop,
       "rlDhcpv6": rlDhcpv6,
       "rlIpv6Fhs": rlIpv6Fhs,
       "rlInventoryEnt": rlInventoryEnt,
       "rlUdld": rlUdld,
       "rndEndOfMibGroup": rndEndOfMibGroup}
)
