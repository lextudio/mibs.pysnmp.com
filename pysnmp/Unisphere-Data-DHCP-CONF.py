# SNMP MIB module (Unisphere-Data-DHCP-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-DHCP-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:29 2024
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

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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

(usDataAgents,) = mibBuilder.importSymbols(
    "Unisphere-Data-Agents",
    "usDataAgents")

(usdDhcpLocalServerGroup,
 usdDhcpLocalServerGroup2,
 usdDhcpProxyGroup,
 usdDhcpRelayGroup,
 usdDhcpRelayGroup2) = mibBuilder.importSymbols(
    "Unisphere-Data-DHCP-MIB",
    "usdDhcpLocalServerGroup",
    "usdDhcpLocalServerGroup2",
    "usdDhcpProxyGroup",
    "usdDhcpRelayGroup",
    "usdDhcpRelayGroup2")


# MODULE-IDENTITY

usdDhcpAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8)
)
usdDhcpAgent.setRevisions(
        ("2002-05-10 19:37",
         "2001-03-30 18:46")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdDhcpRelayAgent_ObjectIdentity = ObjectIdentity
usdDhcpRelayAgent = _UsdDhcpRelayAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1)
)
if mibBuilder.loadTexts:
    usdDhcpRelayAgent.setStatus("current")
_UsdDhcpProxyAgent_ObjectIdentity = ObjectIdentity
usdDhcpProxyAgent = _UsdDhcpProxyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 2)
)
if mibBuilder.loadTexts:
    usdDhcpProxyAgent.setStatus("current")
_UsdDhcpLocalServerAgent_ObjectIdentity = ObjectIdentity
usdDhcpLocalServerAgent = _UsdDhcpLocalServerAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3)
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerAgent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdDhcpRelayAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    usdDhcpRelayAgentV1.setProductRelease("""\
Version 1 of the DHCP relay subcomponent of the Unisphere Routing
        Switch SNMP agent.  This version of the DHCP relay subcomponent is
        supported in the Unisphere RX 1.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdDhcpRelayAgentV1.setStatus(
        "obsolete"
    )

usdDhcpRelayAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 2)
)
if mibBuilder.loadTexts:
    usdDhcpRelayAgentV2.setProductRelease("""\
Version 2 of the DHCP relay subcomponent of the Unisphere Routing
        Switch SNMP agent.  This version of the DHCP relay subcomponent is
        supported in the Unisphere RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdDhcpRelayAgentV2.setStatus(
        "current"
    )

usdDhcpProxyAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    usdDhcpProxyAgentV1.setProductRelease("""\
Version 1 of the DHCP proxy subcomponent of the Unisphere Routing
        Switch SNMP agent.  This version of the DHCP proxy subcomponent is
        supported in the Unisphere RX 1.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdDhcpProxyAgentV1.setStatus(
        "current"
    )

usdDhcpLocalServerAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 1)
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerAgentV1.setProductRelease("""\
Version 1 of the DHCP local server subcomponent of the Unisphere
        Routing Switch SNMP agent.  This version of the DHCP local server
        subcomponent was supported in the Unisphere RX 3.1 and subsequent 3.x
        system releases.""")
if mibBuilder.loadTexts:
    usdDhcpLocalServerAgentV1.setStatus(
        "obsolete"
    )

usdDhcpLocalServerAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 2)
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerAgentV2.setProductRelease("""\
Version 2 of the DHCP local server subcomponent of the Unisphere
        Routing Switch SNMP agent.  This version of the DHCP local server
        subcomponent is supported in the Unisphere RX 4.0 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    usdDhcpLocalServerAgentV2.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-DHCP-CONF",
    **{"usdDhcpAgent": usdDhcpAgent,
       "usdDhcpRelayAgent": usdDhcpRelayAgent,
       "usdDhcpRelayAgentV1": usdDhcpRelayAgentV1,
       "usdDhcpRelayAgentV2": usdDhcpRelayAgentV2,
       "usdDhcpProxyAgent": usdDhcpProxyAgent,
       "usdDhcpProxyAgentV1": usdDhcpProxyAgentV1,
       "usdDhcpLocalServerAgent": usdDhcpLocalServerAgent,
       "usdDhcpLocalServerAgentV1": usdDhcpLocalServerAgentV1,
       "usdDhcpLocalServerAgentV2": usdDhcpLocalServerAgentV2}
)
