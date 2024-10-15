# SNMP MIB module (Unisphere-Data-RADIUS-Client-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-RADIUS-Client-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:30 2024
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

(usdRadiusAcctClientGroup,
 usdRadiusAuthClientGroup,
 usdRadiusBasicClientGroup,
 usdRadiusBasicClientGroup2,
 usdRadiusBrasClientGroup,
 usdRadiusBrasClientGroup2,
 usdRadiusBrasClientGroup3,
 usdRadiusBrasClientGroup4,
 usdRadiusBrasClientGroup5,
 usdRadiusGeneralClientGroup,
 usdRadiusGeneralClientGroup2,
 usdRadiusTunnelClientGroup) = mibBuilder.importSymbols(
    "Unisphere-Data-RADIUS-CLIENT-MIB",
    "usdRadiusAcctClientGroup",
    "usdRadiusAuthClientGroup",
    "usdRadiusBasicClientGroup",
    "usdRadiusBasicClientGroup2",
    "usdRadiusBrasClientGroup",
    "usdRadiusBrasClientGroup2",
    "usdRadiusBrasClientGroup3",
    "usdRadiusBrasClientGroup4",
    "usdRadiusBrasClientGroup5",
    "usdRadiusGeneralClientGroup",
    "usdRadiusGeneralClientGroup2",
    "usdRadiusTunnelClientGroup")


# MODULE-IDENTITY

usdRadiusClientAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35)
)
usdRadiusClientAgent.setRevisions(
        ("2001-10-19 14:44",
         "2001-10-16 20:45",
         "2001-09-07 12:35")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdRadiusClientDynamicAgent_ObjectIdentity = ObjectIdentity
usdRadiusClientDynamicAgent = _UsdRadiusClientDynamicAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1)
)
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgent.setStatus("current")
_UsdRadiusClientBasicAgent_ObjectIdentity = ObjectIdentity
usdRadiusClientBasicAgent = _UsdRadiusClientBasicAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 2)
)
if mibBuilder.loadTexts:
    usdRadiusClientBasicAgent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdRadiusClientDynamicAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 1)
)
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV1.setProductRelease("""\
Version 1 of the RADIUS Client dynamic interface component of the
        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client
        component was supported in the Unisphere RX 1.x system releases.""")
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV1.setStatus(
        "obsolete"
    )

usdRadiusClientDynamicAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 2)
)
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV2.setProductRelease("""\
Version 2 of the RADIUS Client dynamic interface component of the
        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client
        component was supported in the Unisphere RX 2.x system releases.""")
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV2.setStatus(
        "obsolete"
    )

usdRadiusClientDynamicAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 3)
)
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV3.setProductRelease("""\
Version 3 of the RADIUS Client dynamic interface component of the
        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client
        component was supported in the Unisphere RX 3.0 system release.""")
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV3.setStatus(
        "obsolete"
    )

usdRadiusClientDynamicAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 4)
)
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV4.setProductRelease("""\
Version 4 of the RADIUS Client dynamic interface component of the
        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client
        component was supported in the Unisphere RX 3.1 system release.""")
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV4.setStatus(
        "obsolete"
    )

usdRadiusClientDynamicAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 5)
)
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV5.setProductRelease("""\
Version 5 of the RADIUS Client dynamic interface component of the
        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client
        component was supported in the Unisphere RX 3.2 system release.""")
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV5.setStatus(
        "obsolete"
    )

usdRadiusClientDynamicAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 6)
)
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV6.setProductRelease("""\
Version 6 of the RADIUS Client dynamic interface component of the
        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client
        component was supported in the Unisphere RX 3.3 and subsequent RX 3.x
        system releases.""")
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV6.setStatus(
        "obsolete"
    )

usdRadiusClientDynamicAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 7)
)
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV7.setProductRelease("""\
Version 7 of the RADIUS Client dynamic interface component of the
        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client
        component is supported in the Unisphere RX 4.0 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    usdRadiusClientDynamicAgentV7.setStatus(
        "current"
    )

usdRadiusClientBasicAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 2, 1)
)
if mibBuilder.loadTexts:
    usdRadiusClientBasicAgentV1.setProductRelease("""\
Version 1 of the basic authentication RADIUS Client component of the
        Unisphere Routing Switch SNMP agent.  This version of the RADIUS Client
        component is supported in the Unisphere RX 3.2 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    usdRadiusClientBasicAgentV1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-RADIUS-Client-CONF",
    **{"usdRadiusClientAgent": usdRadiusClientAgent,
       "usdRadiusClientDynamicAgent": usdRadiusClientDynamicAgent,
       "usdRadiusClientDynamicAgentV1": usdRadiusClientDynamicAgentV1,
       "usdRadiusClientDynamicAgentV2": usdRadiusClientDynamicAgentV2,
       "usdRadiusClientDynamicAgentV3": usdRadiusClientDynamicAgentV3,
       "usdRadiusClientDynamicAgentV4": usdRadiusClientDynamicAgentV4,
       "usdRadiusClientDynamicAgentV5": usdRadiusClientDynamicAgentV5,
       "usdRadiusClientDynamicAgentV6": usdRadiusClientDynamicAgentV6,
       "usdRadiusClientDynamicAgentV7": usdRadiusClientDynamicAgentV7,
       "usdRadiusClientBasicAgent": usdRadiusClientBasicAgent,
       "usdRadiusClientBasicAgentV1": usdRadiusClientBasicAgentV1}
)
