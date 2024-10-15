# SNMP MIB module (Unisphere-Data-Agents) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-Agents
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:15 2024
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

(usAgentCapability,) = mibBuilder.importSymbols(
    "Unisphere-SMI",
    "usAgentCapability")


# MODULE-IDENTITY

usDataAgents = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2)
)
usDataAgents.setRevisions(
        ("2002-01-25 14:19",
         "2002-01-24 15:23",
         "2001-04-13 17:16")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdAaaServerAgent_ObjectIdentity = ObjectIdentity
usdAaaServerAgent = _UsdAaaServerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1)
)
_UsdAccountingAgent_ObjectIdentity = ObjectIdentity
usdAccountingAgent = _UsdAccountingAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 2)
)
_UsdAtmAgent_ObjectIdentity = ObjectIdentity
usdAtmAgent = _UsdAtmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3)
)
_UsdBgpAgent_ObjectIdentity = ObjectIdentity
usdBgpAgent = _UsdBgpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4)
)
_UsdBridgedEthernetAgent_ObjectIdentity = ObjectIdentity
usdBridgedEthernetAgent = _UsdBridgedEthernetAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 5)
)
_UsdCliAgent_ObjectIdentity = ObjectIdentity
usdCliAgent = _UsdCliAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 6)
)
_UsdCopsAgent_ObjectIdentity = ObjectIdentity
usdCopsAgent = _UsdCopsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 7)
)
_UsdDhcpAgent_ObjectIdentity = ObjectIdentity
usdDhcpAgent = _UsdDhcpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8)
)
_UsdDnsAgent_ObjectIdentity = ObjectIdentity
usdDnsAgent = _UsdDnsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 9)
)
_UsdDs1Agent_ObjectIdentity = ObjectIdentity
usdDs1Agent = _UsdDs1Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10)
)
_UsdDs3Agent_ObjectIdentity = ObjectIdentity
usdDs3Agent = _UsdDs3Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 11)
)
_UsdDvmrpAgent_ObjectIdentity = ObjectIdentity
usdDvmrpAgent = _UsdDvmrpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 12)
)
_UsdEntityAgent_ObjectIdentity = ObjectIdentity
usdEntityAgent = _UsdEntityAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 13)
)
_UsdEthernetAgent_ObjectIdentity = ObjectIdentity
usdEthernetAgent = _UsdEthernetAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 14)
)
_UsdFileTransferAgent_ObjectIdentity = ObjectIdentity
usdFileTransferAgent = _UsdFileTransferAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 15)
)
_UsdFractionalT1Agent_ObjectIdentity = ObjectIdentity
usdFractionalT1Agent = _UsdFractionalT1Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 16)
)
_UsdFrameRelayAgent_ObjectIdentity = ObjectIdentity
usdFrameRelayAgent = _UsdFrameRelayAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 17)
)
_UsdHdlcAgent_ObjectIdentity = ObjectIdentity
usdHdlcAgent = _UsdHdlcAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 18)
)
_UsdIgmpAgent_ObjectIdentity = ObjectIdentity
usdIgmpAgent = _UsdIgmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 19)
)
_UsdInterfacesAgent_ObjectIdentity = ObjectIdentity
usdInterfacesAgent = _UsdInterfacesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 20)
)
_UsdInternetAgent_ObjectIdentity = ObjectIdentity
usdInternetAgent = _UsdInternetAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 21)
)
_UsdIpPolicyAgent_ObjectIdentity = ObjectIdentity
usdIpPolicyAgent = _UsdIpPolicyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 22)
)
_UsdIsisAgent_ObjectIdentity = ObjectIdentity
usdIsisAgent = _UsdIsisAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 23)
)
_UsdL2tpAgent_ObjectIdentity = ObjectIdentity
usdL2tpAgent = _UsdL2tpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24)
)
_UsdLocalAddressServerAgent_ObjectIdentity = ObjectIdentity
usdLocalAddressServerAgent = _UsdLocalAddressServerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 25)
)
_UsdLogAgent_ObjectIdentity = ObjectIdentity
usdLogAgent = _UsdLogAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 26)
)
_UsdNsLookupAgent_ObjectIdentity = ObjectIdentity
usdNsLookupAgent = _UsdNsLookupAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 27)
)
_UsdOspfAgent_ObjectIdentity = ObjectIdentity
usdOspfAgent = _UsdOspfAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 28)
)
_UsdPimAgent_ObjectIdentity = ObjectIdentity
usdPimAgent = _UsdPimAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 29)
)
_UsdPingAgent_ObjectIdentity = ObjectIdentity
usdPingAgent = _UsdPingAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 30)
)
_UsdPolicyManagerAgent_ObjectIdentity = ObjectIdentity
usdPolicyManagerAgent = _UsdPolicyManagerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31)
)
_UsdPppAgent_ObjectIdentity = ObjectIdentity
usdPppAgent = _UsdPppAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32)
)
_UsdPppoeAgent_ObjectIdentity = ObjectIdentity
usdPppoeAgent = _UsdPppoeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 33)
)
_UsdProfileAgents_ObjectIdentity = ObjectIdentity
usdProfileAgents = _UsdProfileAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34)
)
if mibBuilder.loadTexts:
    usdProfileAgents.setStatus("current")
_UsdProfileManagerAgent_ObjectIdentity = ObjectIdentity
usdProfileManagerAgent = _UsdProfileManagerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 1)
)
_UsdIpProfileAgent_ObjectIdentity = ObjectIdentity
usdIpProfileAgent = _UsdIpProfileAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2)
)
_UsdPppProfileAgent_ObjectIdentity = ObjectIdentity
usdPppProfileAgent = _UsdPppProfileAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 3)
)
_UsdPppoeProfileAgent_ObjectIdentity = ObjectIdentity
usdPppoeProfileAgent = _UsdPppoeProfileAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4)
)
_UsdRadiusClientAgent_ObjectIdentity = ObjectIdentity
usdRadiusClientAgent = _UsdRadiusClientAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35)
)
_UsdRipAgent_ObjectIdentity = ObjectIdentity
usdRipAgent = _UsdRipAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 36)
)
_UsdRouterAgent_ObjectIdentity = ObjectIdentity
usdRouterAgent = _UsdRouterAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 37)
)
_UsdSlepAgent_ObjectIdentity = ObjectIdentity
usdSlepAgent = _UsdSlepAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 38)
)
_UsdSnmpAgent_ObjectIdentity = ObjectIdentity
usdSnmpAgent = _UsdSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39)
)
_UsdSonetAgent_ObjectIdentity = ObjectIdentity
usdSonetAgent = _UsdSonetAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40)
)
_UsdSscClientAgent_ObjectIdentity = ObjectIdentity
usdSscClientAgent = _UsdSscClientAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 41)
)
_UsdSystemAgents_ObjectIdentity = ObjectIdentity
usdSystemAgents = _UsdSystemAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42)
)
if mibBuilder.loadTexts:
    usdSystemAgents.setStatus("current")
_UsdErxSystemAgent_ObjectIdentity = ObjectIdentity
usdErxSystemAgent = _UsdErxSystemAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1)
)
_UsdMrxSystemAgent_ObjectIdentity = ObjectIdentity
usdMrxSystemAgent = _UsdMrxSystemAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 2)
)
_UsdTraceRouteAgent_ObjectIdentity = ObjectIdentity
usdTraceRouteAgent = _UsdTraceRouteAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 43)
)
_UsdAutoConfAgent_ObjectIdentity = ObjectIdentity
usdAutoConfAgent = _UsdAutoConfAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 44)
)
_UsdSubscriberAgent_ObjectIdentity = ObjectIdentity
usdSubscriberAgent = _UsdSubscriberAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 45)
)
_UsdSmdsAgent_ObjectIdentity = ObjectIdentity
usdSmdsAgent = _UsdSmdsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 46)
)
_UsdIpTunnelAgent_ObjectIdentity = ObjectIdentity
usdIpTunnelAgent = _UsdIpTunnelAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 47)
)
_UsdCbfAgent_ObjectIdentity = ObjectIdentity
usdCbfAgent = _UsdCbfAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 48)
)
_UsdL2fAgent_ObjectIdentity = ObjectIdentity
usdL2fAgent = _UsdL2fAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 49)
)
_UsdQosManagerAgent_ObjectIdentity = ObjectIdentity
usdQosManagerAgent = _UsdQosManagerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 50)
)
_UsdMplsAgent_ObjectIdentity = ObjectIdentity
usdMplsAgent = _UsdMplsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 51)
)
_UsdSysClockAgent_ObjectIdentity = ObjectIdentity
usdSysClockAgent = _UsdSysClockAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 52)
)
_UsdVrrpAgent_ObjectIdentity = ObjectIdentity
usdVrrpAgent = _UsdVrrpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 53)
)
_UsdV35Agent_ObjectIdentity = ObjectIdentity
usdV35Agent = _UsdV35Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 54)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-Agents",
    **{"usDataAgents": usDataAgents,
       "usdAaaServerAgent": usdAaaServerAgent,
       "usdAccountingAgent": usdAccountingAgent,
       "usdAtmAgent": usdAtmAgent,
       "usdBgpAgent": usdBgpAgent,
       "usdBridgedEthernetAgent": usdBridgedEthernetAgent,
       "usdCliAgent": usdCliAgent,
       "usdCopsAgent": usdCopsAgent,
       "usdDhcpAgent": usdDhcpAgent,
       "usdDnsAgent": usdDnsAgent,
       "usdDs1Agent": usdDs1Agent,
       "usdDs3Agent": usdDs3Agent,
       "usdDvmrpAgent": usdDvmrpAgent,
       "usdEntityAgent": usdEntityAgent,
       "usdEthernetAgent": usdEthernetAgent,
       "usdFileTransferAgent": usdFileTransferAgent,
       "usdFractionalT1Agent": usdFractionalT1Agent,
       "usdFrameRelayAgent": usdFrameRelayAgent,
       "usdHdlcAgent": usdHdlcAgent,
       "usdIgmpAgent": usdIgmpAgent,
       "usdInterfacesAgent": usdInterfacesAgent,
       "usdInternetAgent": usdInternetAgent,
       "usdIpPolicyAgent": usdIpPolicyAgent,
       "usdIsisAgent": usdIsisAgent,
       "usdL2tpAgent": usdL2tpAgent,
       "usdLocalAddressServerAgent": usdLocalAddressServerAgent,
       "usdLogAgent": usdLogAgent,
       "usdNsLookupAgent": usdNsLookupAgent,
       "usdOspfAgent": usdOspfAgent,
       "usdPimAgent": usdPimAgent,
       "usdPingAgent": usdPingAgent,
       "usdPolicyManagerAgent": usdPolicyManagerAgent,
       "usdPppAgent": usdPppAgent,
       "usdPppoeAgent": usdPppoeAgent,
       "usdProfileAgents": usdProfileAgents,
       "usdProfileManagerAgent": usdProfileManagerAgent,
       "usdIpProfileAgent": usdIpProfileAgent,
       "usdPppProfileAgent": usdPppProfileAgent,
       "usdPppoeProfileAgent": usdPppoeProfileAgent,
       "usdRadiusClientAgent": usdRadiusClientAgent,
       "usdRipAgent": usdRipAgent,
       "usdRouterAgent": usdRouterAgent,
       "usdSlepAgent": usdSlepAgent,
       "usdSnmpAgent": usdSnmpAgent,
       "usdSonetAgent": usdSonetAgent,
       "usdSscClientAgent": usdSscClientAgent,
       "usdSystemAgents": usdSystemAgents,
       "usdErxSystemAgent": usdErxSystemAgent,
       "usdMrxSystemAgent": usdMrxSystemAgent,
       "usdTraceRouteAgent": usdTraceRouteAgent,
       "usdAutoConfAgent": usdAutoConfAgent,
       "usdSubscriberAgent": usdSubscriberAgent,
       "usdSmdsAgent": usdSmdsAgent,
       "usdIpTunnelAgent": usdIpTunnelAgent,
       "usdCbfAgent": usdCbfAgent,
       "usdL2fAgent": usdL2fAgent,
       "usdQosManagerAgent": usdQosManagerAgent,
       "usdMplsAgent": usdMplsAgent,
       "usdSysClockAgent": usdSysClockAgent,
       "usdVrrpAgent": usdVrrpAgent,
       "usdV35Agent": usdV35Agent}
)
