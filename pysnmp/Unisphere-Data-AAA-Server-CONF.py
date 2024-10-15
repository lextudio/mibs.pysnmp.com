# SNMP MIB module (Unisphere-Data-AAA-Server-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-AAA-Server-CONF
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

(usdAaaAccountingGroup,
 usdAaaAccountingGroup2,
 usdAaaAddressGroup,
 usdAaaAuthenticationGroup,
 usdAaaBasicGroup,
 usdAaaBrasGroup,
 usdAaaBrasGroup2,
 usdAaaBrasGroup3,
 usdAaaBrasGroup4,
 usdAaaCapabilitiesGroup,
 usdAaaGroup,
 usdAaaGroup2,
 usdAaaSubscriberGroup,
 usdAaaSubscriberGroup2,
 usdAaaSubscriberGroup3,
 usdAaaTunnelGroup) = mibBuilder.importSymbols(
    "Unisphere-Data-AAA-MIB",
    "usdAaaAccountingGroup",
    "usdAaaAccountingGroup2",
    "usdAaaAddressGroup",
    "usdAaaAuthenticationGroup",
    "usdAaaBasicGroup",
    "usdAaaBrasGroup",
    "usdAaaBrasGroup2",
    "usdAaaBrasGroup3",
    "usdAaaBrasGroup4",
    "usdAaaCapabilitiesGroup",
    "usdAaaGroup",
    "usdAaaGroup2",
    "usdAaaSubscriberGroup",
    "usdAaaSubscriberGroup2",
    "usdAaaSubscriberGroup3",
    "usdAaaTunnelGroup")

(usDataAgents,) = mibBuilder.importSymbols(
    "Unisphere-Data-Agents",
    "usDataAgents")


# MODULE-IDENTITY

usdAaaServerAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1)
)
usdAaaServerAgent.setRevisions(
        ("2002-05-13 19:32",
         "2002-01-03 20:30",
         "2001-09-18 21:13",
         "2001-04-10 14:02")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdAaaServerBaseAgent_ObjectIdentity = ObjectIdentity
usdAaaServerBaseAgent = _UsdAaaServerBaseAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6)
)
if mibBuilder.loadTexts:
    usdAaaServerBaseAgent.setStatus("current")
_UsdAaaServerBrasAgent_ObjectIdentity = ObjectIdentity
usdAaaServerBrasAgent = _UsdAaaServerBrasAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7)
)
if mibBuilder.loadTexts:
    usdAaaServerBrasAgent.setStatus("current")
_UsdAaaServerTunnelAgent_ObjectIdentity = ObjectIdentity
usdAaaServerTunnelAgent = _UsdAaaServerTunnelAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8)
)
if mibBuilder.loadTexts:
    usdAaaServerTunnelAgent.setStatus("current")
_UsdAaaServerAccountingAgent_ObjectIdentity = ObjectIdentity
usdAaaServerAccountingAgent = _UsdAaaServerAccountingAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9)
)
if mibBuilder.loadTexts:
    usdAaaServerAccountingAgent.setStatus("current")
_UsdAaaServerAddressAgent_ObjectIdentity = ObjectIdentity
usdAaaServerAddressAgent = _UsdAaaServerAddressAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10)
)
if mibBuilder.loadTexts:
    usdAaaServerAddressAgent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdAaaServerAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdAaaServerAgentV1.setProductRelease("""\
Version 1 of the AAA Server component of the Unisphere Routing Switch
        SNMP agent.  This version was supported in the Unisphere RX 1.x system
        releases.""")
if mibBuilder.loadTexts:
    usdAaaServerAgentV1.setStatus(
        "obsolete"
    )

usdAaaServerAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    usdAaaServerAgentV2.setProductRelease("""\
Version 2 of the AAA Server component of the Unisphere Routing Switch
        SNMP agent.  This version was supported in the Unisphere RX 2.x system
        releases.""")
if mibBuilder.loadTexts:
    usdAaaServerAgentV2.setStatus(
        "obsolete"
    )

usdAaaServerAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    usdAaaServerAgentV3.setProductRelease("""\
Version 3 of the AAA Server component of the Unisphere Routing Switch
        SNMP agent.  This version was supported in the Unisphere RX 3.0 system
        release.""")
if mibBuilder.loadTexts:
    usdAaaServerAgentV3.setStatus(
        "obsolete"
    )

usdAaaServerAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    usdAaaServerAgentV4.setProductRelease("""\
Version 4 of the AAA Server component of the Unisphere Routing Switch
        SNMP agent.  This version was supported in the Unisphere RX 3.1 system
        release.""")
if mibBuilder.loadTexts:
    usdAaaServerAgentV4.setStatus(
        "obsolete"
    )

usdAaaServerAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 5)
)
if mibBuilder.loadTexts:
    usdAaaServerAgentV5.setProductRelease("""\
Version 5 of the AAA Server component of the Unisphere Routing Switch
        SNMP agent.  This version was supported in the Unisphere RX 3.2 system
        release.""")
if mibBuilder.loadTexts:
    usdAaaServerAgentV5.setStatus(
        "obsolete"
    )

usdAaaServerBaseAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    usdAaaServerBaseAgentV1.setProductRelease("""\
Version 1 of the basic AAA Server component of the Unisphere Routing
        Switch SNMP agent.  This version is supported in the Unisphere RX 3.3
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdAaaServerBaseAgentV1.setStatus(
        "current"
    )

usdAaaServerBrasAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    usdAaaServerBrasAgentV1.setProductRelease("""\
Version 1 of the B-RAS option of the AAA Server component of the
        Unisphere Routing Switch SNMP agent.  This version was supported in the
        Unisphere RX 3.3 system release.""")
if mibBuilder.loadTexts:
    usdAaaServerBrasAgentV1.setStatus(
        "obsolete"
    )

usdAaaServerBrasAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    usdAaaServerBrasAgentV2.setProductRelease("""\
Version 2 of the B-RAS option of the AAA Server component of the
        Unisphere Routing Switch SNMP agent.  This version was supported in the
        Unisphere RX 3.4 and subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    usdAaaServerBrasAgentV2.setStatus(
        "obsolete"
    )

usdAaaServerBrasAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    usdAaaServerBrasAgentV3.setProductRelease("""\
Version 3 of the B-RAS option of the AAA Server component of the
        Unisphere Routing Switch SNMP agent.  This version is supported in the
        Unisphere RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdAaaServerBrasAgentV3.setStatus(
        "current"
    )

usdAaaServerTunnelAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    usdAaaServerTunnelAgentV1.setProductRelease("""\
Version 1 of the tunneling option of the AAA Server component of the
        Unisphere Routing Switch SNMP agent.  This version is supported in the
        Unisphere RX 3.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdAaaServerTunnelAgentV1.setStatus(
        "current"
    )

usdAaaServerAccountingAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    usdAaaServerAccountingAgentV1.setProductRelease("""\
Version 1 of the accounting option of the AAA Server component of the
        Unisphere Routing Switch SNMP agent.  This version was supported in the
        Unisphere RX 3.3 and subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    usdAaaServerAccountingAgentV1.setStatus(
        "obsolete"
    )

usdAaaServerAccountingAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    usdAaaServerAccountingAgentV2.setProductRelease("""\
Version 2 of the accounting option of the AAA Server component of the
        Unisphere Routing Switch SNMP agent.  This version is supported in the
        Unisphere RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdAaaServerAccountingAgentV2.setStatus(
        "current"
    )

usdAaaServerAddressAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    usdAaaServerAddressAgentV1.setProductRelease("""\
Version 1 of the address assignment option of the AAA Server component
        of the Unisphere Routing Switch SNMP agent.  This version is supported
        in the Unisphere RX 3.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdAaaServerAddressAgentV1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-AAA-Server-CONF",
    **{"usdAaaServerAgent": usdAaaServerAgent,
       "usdAaaServerAgentV1": usdAaaServerAgentV1,
       "usdAaaServerAgentV2": usdAaaServerAgentV2,
       "usdAaaServerAgentV3": usdAaaServerAgentV3,
       "usdAaaServerAgentV4": usdAaaServerAgentV4,
       "usdAaaServerAgentV5": usdAaaServerAgentV5,
       "usdAaaServerBaseAgent": usdAaaServerBaseAgent,
       "usdAaaServerBaseAgentV1": usdAaaServerBaseAgentV1,
       "usdAaaServerBrasAgent": usdAaaServerBrasAgent,
       "usdAaaServerBrasAgentV1": usdAaaServerBrasAgentV1,
       "usdAaaServerBrasAgentV2": usdAaaServerBrasAgentV2,
       "usdAaaServerBrasAgentV3": usdAaaServerBrasAgentV3,
       "usdAaaServerTunnelAgent": usdAaaServerTunnelAgent,
       "usdAaaServerTunnelAgentV1": usdAaaServerTunnelAgentV1,
       "usdAaaServerAccountingAgent": usdAaaServerAccountingAgent,
       "usdAaaServerAccountingAgentV1": usdAaaServerAccountingAgentV1,
       "usdAaaServerAccountingAgentV2": usdAaaServerAccountingAgentV2,
       "usdAaaServerAddressAgent": usdAaaServerAddressAgent,
       "usdAaaServerAddressAgentV1": usdAaaServerAddressAgentV1}
)
