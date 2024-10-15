# SNMP MIB module (Juniper-Agents) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-Agents
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:36 2024
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

(juniAgentCapability,) = mibBuilder.importSymbols(
    "Juniper-UNI-SMI",
    "juniAgentCapability")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

juniAgents = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2)
)
juniAgents.setRevisions(
        ("2008-01-07 11:12",
         "2006-10-18 14:36",
         "2006-07-22 07:26",
         "2006-03-29 18:03",
         "2006-01-01 00:00",
         "2005-06-30 18:03",
         "2004-06-23 17:41",
         "2004-06-08 15:39",
         "2003-10-03 18:35",
         "2003-05-08 17:44",
         "2003-05-02 18:18",
         "2003-04-29 14:14",
         "2003-04-23 13:56",
         "2002-01-24 15:23",
         "2001-04-13 17:16")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniAaaServerAgent_ObjectIdentity = ObjectIdentity
juniAaaServerAgent = _JuniAaaServerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1)
)
_JuniAccountingAgent_ObjectIdentity = ObjectIdentity
juniAccountingAgent = _JuniAccountingAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 2)
)
_JuniAtmAgent_ObjectIdentity = ObjectIdentity
juniAtmAgent = _JuniAtmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3)
)
_JuniBgpAgent_ObjectIdentity = ObjectIdentity
juniBgpAgent = _JuniBgpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4)
)
_JuniBridgedEthernetAgent_ObjectIdentity = ObjectIdentity
juniBridgedEthernetAgent = _JuniBridgedEthernetAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 5)
)
_JuniCliAgent_ObjectIdentity = ObjectIdentity
juniCliAgent = _JuniCliAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 6)
)
_JuniCopsAgent_ObjectIdentity = ObjectIdentity
juniCopsAgent = _JuniCopsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 7)
)
_JuniDhcpAgent_ObjectIdentity = ObjectIdentity
juniDhcpAgent = _JuniDhcpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8)
)
_JuniDnsAgent_ObjectIdentity = ObjectIdentity
juniDnsAgent = _JuniDnsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 9)
)
_JuniDs1Agent_ObjectIdentity = ObjectIdentity
juniDs1Agent = _JuniDs1Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10)
)
_JuniDs3Agent_ObjectIdentity = ObjectIdentity
juniDs3Agent = _JuniDs3Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11)
)
_JuniDvmrpAgent_ObjectIdentity = ObjectIdentity
juniDvmrpAgent = _JuniDvmrpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 12)
)
_JuniEntityAgent_ObjectIdentity = ObjectIdentity
juniEntityAgent = _JuniEntityAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 13)
)
_JuniEthernetAgent_ObjectIdentity = ObjectIdentity
juniEthernetAgent = _JuniEthernetAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 14)
)
_JuniFileTransferAgent_ObjectIdentity = ObjectIdentity
juniFileTransferAgent = _JuniFileTransferAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 15)
)
_JuniFractionalT1Agent_ObjectIdentity = ObjectIdentity
juniFractionalT1Agent = _JuniFractionalT1Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 16)
)
_JuniFrameRelayAgent_ObjectIdentity = ObjectIdentity
juniFrameRelayAgent = _JuniFrameRelayAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 17)
)
_JuniHdlcAgent_ObjectIdentity = ObjectIdentity
juniHdlcAgent = _JuniHdlcAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 18)
)
_JuniIgmpAgent_ObjectIdentity = ObjectIdentity
juniIgmpAgent = _JuniIgmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 19)
)
_JuniInterfacesAgent_ObjectIdentity = ObjectIdentity
juniInterfacesAgent = _JuniInterfacesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 20)
)
_JuniInternetAgent_ObjectIdentity = ObjectIdentity
juniInternetAgent = _JuniInternetAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 21)
)
_JuniIpPolicyAgent_ObjectIdentity = ObjectIdentity
juniIpPolicyAgent = _JuniIpPolicyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 22)
)
_JuniIsisAgent_ObjectIdentity = ObjectIdentity
juniIsisAgent = _JuniIsisAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 23)
)
_JuniL2tpAgent_ObjectIdentity = ObjectIdentity
juniL2tpAgent = _JuniL2tpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24)
)
_JuniLocalAddressServerAgent_ObjectIdentity = ObjectIdentity
juniLocalAddressServerAgent = _JuniLocalAddressServerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25)
)
_JuniLogAgent_ObjectIdentity = ObjectIdentity
juniLogAgent = _JuniLogAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 26)
)
_JuniNsLookupAgent_ObjectIdentity = ObjectIdentity
juniNsLookupAgent = _JuniNsLookupAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 27)
)
_JuniOspfAgent_ObjectIdentity = ObjectIdentity
juniOspfAgent = _JuniOspfAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 28)
)
_JuniPimAgent_ObjectIdentity = ObjectIdentity
juniPimAgent = _JuniPimAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 29)
)
_JuniPingAgent_ObjectIdentity = ObjectIdentity
juniPingAgent = _JuniPingAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 30)
)
_JuniPolicyManagerAgent_ObjectIdentity = ObjectIdentity
juniPolicyManagerAgent = _JuniPolicyManagerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31)
)
_JuniPppAgent_ObjectIdentity = ObjectIdentity
juniPppAgent = _JuniPppAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32)
)
_JuniPppoeAgent_ObjectIdentity = ObjectIdentity
juniPppoeAgent = _JuniPppoeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 33)
)
_JuniProfileAgents_ObjectIdentity = ObjectIdentity
juniProfileAgents = _JuniProfileAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34)
)
if mibBuilder.loadTexts:
    juniProfileAgents.setStatus("current")
_JuniProfileManagerAgent_ObjectIdentity = ObjectIdentity
juniProfileManagerAgent = _JuniProfileManagerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1)
)
_JuniIpProfileAgent_ObjectIdentity = ObjectIdentity
juniIpProfileAgent = _JuniIpProfileAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2)
)
_JuniPppProfileAgent_ObjectIdentity = ObjectIdentity
juniPppProfileAgent = _JuniPppProfileAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3)
)
_JuniPppoeProfileAgent_ObjectIdentity = ObjectIdentity
juniPppoeProfileAgent = _JuniPppoeProfileAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4)
)
_JuniIpv6ProfileAgent_ObjectIdentity = ObjectIdentity
juniIpv6ProfileAgent = _JuniIpv6ProfileAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 5)
)
_JuniAtm1483ProfileAgent_ObjectIdentity = ObjectIdentity
juniAtm1483ProfileAgent = _JuniAtm1483ProfileAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6)
)
_JuniHttpProfileAgent_ObjectIdentity = ObjectIdentity
juniHttpProfileAgent = _JuniHttpProfileAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 7)
)
_JuniRadiusClientAgent_ObjectIdentity = ObjectIdentity
juniRadiusClientAgent = _JuniRadiusClientAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35)
)
_JuniRipAgent_ObjectIdentity = ObjectIdentity
juniRipAgent = _JuniRipAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 36)
)
_JuniRouterAgent_ObjectIdentity = ObjectIdentity
juniRouterAgent = _JuniRouterAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 37)
)
_JuniSlepAgent_ObjectIdentity = ObjectIdentity
juniSlepAgent = _JuniSlepAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 38)
)
_JuniSnmpAgent_ObjectIdentity = ObjectIdentity
juniSnmpAgent = _JuniSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39)
)
_JuniSonetAgent_ObjectIdentity = ObjectIdentity
juniSonetAgent = _JuniSonetAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40)
)
_JuniSscClientAgent_ObjectIdentity = ObjectIdentity
juniSscClientAgent = _JuniSscClientAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 41)
)
_JuniSystemAgents_ObjectIdentity = ObjectIdentity
juniSystemAgents = _JuniSystemAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42)
)
if mibBuilder.loadTexts:
    juniSystemAgents.setStatus("current")
_JuniErxSystemAgent_ObjectIdentity = ObjectIdentity
juniErxSystemAgent = _JuniErxSystemAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1)
)
_JuniSystemAgent_ObjectIdentity = ObjectIdentity
juniSystemAgent = _JuniSystemAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 2)
)
_JuniTraceRouteAgent_ObjectIdentity = ObjectIdentity
juniTraceRouteAgent = _JuniTraceRouteAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 43)
)
_JuniAutoConfAgent_ObjectIdentity = ObjectIdentity
juniAutoConfAgent = _JuniAutoConfAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 44)
)
_JuniSubscriberAgent_ObjectIdentity = ObjectIdentity
juniSubscriberAgent = _JuniSubscriberAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 45)
)
_JuniSmdsAgent_ObjectIdentity = ObjectIdentity
juniSmdsAgent = _JuniSmdsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 46)
)
_JuniIpTunnelAgent_ObjectIdentity = ObjectIdentity
juniIpTunnelAgent = _JuniIpTunnelAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 47)
)
_JuniCbfAgent_ObjectIdentity = ObjectIdentity
juniCbfAgent = _JuniCbfAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 48)
)
_JuniL2fAgent_ObjectIdentity = ObjectIdentity
juniL2fAgent = _JuniL2fAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 49)
)
_JuniQosManagerAgent_ObjectIdentity = ObjectIdentity
juniQosManagerAgent = _JuniQosManagerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 50)
)
_JuniMplsAgent_ObjectIdentity = ObjectIdentity
juniMplsAgent = _JuniMplsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 51)
)
_JuniSysClockAgent_ObjectIdentity = ObjectIdentity
juniSysClockAgent = _JuniSysClockAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 52)
)
_JuniVrrpAgent_ObjectIdentity = ObjectIdentity
juniVrrpAgent = _JuniVrrpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 53)
)
_JuniV35Agent_ObjectIdentity = ObjectIdentity
juniV35Agent = _JuniV35Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 54)
)
_JuniMRouterAgent_ObjectIdentity = ObjectIdentity
juniMRouterAgent = _JuniMRouterAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 55)
)
_JuniNotificationLogAgent_ObjectIdentity = ObjectIdentity
juniNotificationLogAgent = _JuniNotificationLogAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 56)
)
_JuniTacacsPlusClientAgent_ObjectIdentity = ObjectIdentity
juniTacacsPlusClientAgent = _JuniTacacsPlusClientAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 57)
)
_JuniL2tpDialoutAgent_ObjectIdentity = ObjectIdentity
juniL2tpDialoutAgent = _JuniL2tpDialoutAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 59)
)
_JuniBridgeAgent_ObjectIdentity = ObjectIdentity
juniBridgeAgent = _JuniBridgeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 60)
)
_JuniBridgingMgrAgent_ObjectIdentity = ObjectIdentity
juniBridgingMgrAgent = _JuniBridgingMgrAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 61)
)
_JuniEventManagerAgent_ObjectIdentity = ObjectIdentity
juniEventManagerAgent = _JuniEventManagerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 62)
)
_JuniRadiusDisconnectAgent_ObjectIdentity = ObjectIdentity
juniRadiusDisconnectAgent = _JuniRadiusDisconnectAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 63)
)
_JuniDhcpv6Agent_ObjectIdentity = ObjectIdentity
juniDhcpv6Agent = _JuniDhcpv6Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 64)
)
_JuniIpsecTunnelAgent_ObjectIdentity = ObjectIdentity
juniIpsecTunnelAgent = _JuniIpsecTunnelAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 65)
)
_JuniIkeAgent_ObjectIdentity = ObjectIdentity
juniIkeAgent = _JuniIkeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 66)
)
_JuniTsmAgent_ObjectIdentity = ObjectIdentity
juniTsmAgent = _JuniTsmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 67)
)
_JuniRadiusProxyAgent_ObjectIdentity = ObjectIdentity
juniRadiusProxyAgent = _JuniRadiusProxyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 68)
)
_JuniHaRedundancyAgent_ObjectIdentity = ObjectIdentity
juniHaRedundancyAgent = _JuniHaRedundancyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 69)
)
_JuniRadiusRequestAgent_ObjectIdentity = ObjectIdentity
juniRadiusRequestAgent = _JuniRadiusRequestAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 70)
)
_JuniLicenseMgrAgent_ObjectIdentity = ObjectIdentity
juniLicenseMgrAgent = _JuniLicenseMgrAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 71)
)
_JuniPacketMirrorAgent_ObjectIdentity = ObjectIdentity
juniPacketMirrorAgent = _JuniPacketMirrorAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 72)
)
_JuniVpnmibAgent_ObjectIdentity = ObjectIdentity
juniVpnmibAgent = _JuniVpnmibAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 73)
)
_JuniHttpAgent_ObjectIdentity = ObjectIdentity
juniHttpAgent = _JuniHttpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 74)
)
_JuniBfdmibAgent_ObjectIdentity = ObjectIdentity
juniBfdmibAgent = _JuniBfdmibAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 75)
)
_JuniDosProtectionAgent_ObjectIdentity = ObjectIdentity
juniDosProtectionAgent = _JuniDosProtectionAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 76)
)
_JuniDosProtectionPlatformAgent_ObjectIdentity = ObjectIdentity
juniDosProtectionPlatformAgent = _JuniDosProtectionPlatformAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 77)
)
_JuniMplsteAgent_ObjectIdentity = ObjectIdentity
juniMplsteAgent = _JuniMplsteAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 78)
)
_JuniMplsLdpAgent_ObjectIdentity = ObjectIdentity
juniMplsLdpAgent = _JuniMplsLdpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 79)
)
_JuniMobileIpv4HaAgent_ObjectIdentity = ObjectIdentity
juniMobileIpv4HaAgent = _JuniMobileIpv4HaAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 80)
)
_JuniFtnMgrAgent_ObjectIdentity = ObjectIdentity
juniFtnMgrAgent = _JuniFtnMgrAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 81)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-Agents",
    **{"juniAgents": juniAgents,
       "juniAaaServerAgent": juniAaaServerAgent,
       "juniAccountingAgent": juniAccountingAgent,
       "juniAtmAgent": juniAtmAgent,
       "juniBgpAgent": juniBgpAgent,
       "juniBridgedEthernetAgent": juniBridgedEthernetAgent,
       "juniCliAgent": juniCliAgent,
       "juniCopsAgent": juniCopsAgent,
       "juniDhcpAgent": juniDhcpAgent,
       "juniDnsAgent": juniDnsAgent,
       "juniDs1Agent": juniDs1Agent,
       "juniDs3Agent": juniDs3Agent,
       "juniDvmrpAgent": juniDvmrpAgent,
       "juniEntityAgent": juniEntityAgent,
       "juniEthernetAgent": juniEthernetAgent,
       "juniFileTransferAgent": juniFileTransferAgent,
       "juniFractionalT1Agent": juniFractionalT1Agent,
       "juniFrameRelayAgent": juniFrameRelayAgent,
       "juniHdlcAgent": juniHdlcAgent,
       "juniIgmpAgent": juniIgmpAgent,
       "juniInterfacesAgent": juniInterfacesAgent,
       "juniInternetAgent": juniInternetAgent,
       "juniIpPolicyAgent": juniIpPolicyAgent,
       "juniIsisAgent": juniIsisAgent,
       "juniL2tpAgent": juniL2tpAgent,
       "juniLocalAddressServerAgent": juniLocalAddressServerAgent,
       "juniLogAgent": juniLogAgent,
       "juniNsLookupAgent": juniNsLookupAgent,
       "juniOspfAgent": juniOspfAgent,
       "juniPimAgent": juniPimAgent,
       "juniPingAgent": juniPingAgent,
       "juniPolicyManagerAgent": juniPolicyManagerAgent,
       "juniPppAgent": juniPppAgent,
       "juniPppoeAgent": juniPppoeAgent,
       "juniProfileAgents": juniProfileAgents,
       "juniProfileManagerAgent": juniProfileManagerAgent,
       "juniIpProfileAgent": juniIpProfileAgent,
       "juniPppProfileAgent": juniPppProfileAgent,
       "juniPppoeProfileAgent": juniPppoeProfileAgent,
       "juniIpv6ProfileAgent": juniIpv6ProfileAgent,
       "juniAtm1483ProfileAgent": juniAtm1483ProfileAgent,
       "juniHttpProfileAgent": juniHttpProfileAgent,
       "juniRadiusClientAgent": juniRadiusClientAgent,
       "juniRipAgent": juniRipAgent,
       "juniRouterAgent": juniRouterAgent,
       "juniSlepAgent": juniSlepAgent,
       "juniSnmpAgent": juniSnmpAgent,
       "juniSonetAgent": juniSonetAgent,
       "juniSscClientAgent": juniSscClientAgent,
       "juniSystemAgents": juniSystemAgents,
       "juniErxSystemAgent": juniErxSystemAgent,
       "juniSystemAgent": juniSystemAgent,
       "juniTraceRouteAgent": juniTraceRouteAgent,
       "juniAutoConfAgent": juniAutoConfAgent,
       "juniSubscriberAgent": juniSubscriberAgent,
       "juniSmdsAgent": juniSmdsAgent,
       "juniIpTunnelAgent": juniIpTunnelAgent,
       "juniCbfAgent": juniCbfAgent,
       "juniL2fAgent": juniL2fAgent,
       "juniQosManagerAgent": juniQosManagerAgent,
       "juniMplsAgent": juniMplsAgent,
       "juniSysClockAgent": juniSysClockAgent,
       "juniVrrpAgent": juniVrrpAgent,
       "juniV35Agent": juniV35Agent,
       "juniMRouterAgent": juniMRouterAgent,
       "juniNotificationLogAgent": juniNotificationLogAgent,
       "juniTacacsPlusClientAgent": juniTacacsPlusClientAgent,
       "juniL2tpDialoutAgent": juniL2tpDialoutAgent,
       "juniBridgeAgent": juniBridgeAgent,
       "juniBridgingMgrAgent": juniBridgingMgrAgent,
       "juniEventManagerAgent": juniEventManagerAgent,
       "juniRadiusDisconnectAgent": juniRadiusDisconnectAgent,
       "juniDhcpv6Agent": juniDhcpv6Agent,
       "juniIpsecTunnelAgent": juniIpsecTunnelAgent,
       "juniIkeAgent": juniIkeAgent,
       "juniTsmAgent": juniTsmAgent,
       "juniRadiusProxyAgent": juniRadiusProxyAgent,
       "juniHaRedundancyAgent": juniHaRedundancyAgent,
       "juniRadiusRequestAgent": juniRadiusRequestAgent,
       "juniLicenseMgrAgent": juniLicenseMgrAgent,
       "juniPacketMirrorAgent": juniPacketMirrorAgent,
       "juniVpnmibAgent": juniVpnmibAgent,
       "juniHttpAgent": juniHttpAgent,
       "juniBfdmibAgent": juniBfdmibAgent,
       "juniDosProtectionAgent": juniDosProtectionAgent,
       "juniDosProtectionPlatformAgent": juniDosProtectionPlatformAgent,
       "juniMplsteAgent": juniMplsteAgent,
       "juniMplsLdpAgent": juniMplsLdpAgent,
       "juniMobileIpv4HaAgent": juniMobileIpv4HaAgent,
       "juniFtnMgrAgent": juniFtnMgrAgent}
)
