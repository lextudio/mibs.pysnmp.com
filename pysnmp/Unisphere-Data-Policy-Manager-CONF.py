# SNMP MIB module (Unisphere-Data-Policy-Manager-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-Policy-Manager-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:26 2024
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

(usdClassifierControlListGroup2,
 usdColorRulesGroup,
 usdFilterRulesGroup,
 usdForwardRulesGroup,
 usdLogRuleGroup,
 usdMarkingRulesGroup,
 usdNextHopRulesGroup,
 usdNextInterfaceRulesGroup,
 usdPolicyAttachProfileGroup,
 usdPolicyAttachStatisticsGroup,
 usdPolicyBaseGroup,
 usdPolicyIfAttachGroup,
 usdRateLimitGroup,
 usdRateLimitGroup2,
 usdTrafficClassRulesGroup,
 usdTrafficShapeGroup) = mibBuilder.importSymbols(
    "Unisphere-Data-POLICY-MIB",
    "usdClassifierControlListGroup2",
    "usdColorRulesGroup",
    "usdFilterRulesGroup",
    "usdForwardRulesGroup",
    "usdLogRuleGroup",
    "usdMarkingRulesGroup",
    "usdNextHopRulesGroup",
    "usdNextInterfaceRulesGroup",
    "usdPolicyAttachProfileGroup",
    "usdPolicyAttachStatisticsGroup",
    "usdPolicyBaseGroup",
    "usdPolicyIfAttachGroup",
    "usdRateLimitGroup",
    "usdRateLimitGroup2",
    "usdTrafficClassRulesGroup",
    "usdTrafficShapeGroup")


# MODULE-IDENTITY

usdPolicyManagerAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31)
)
usdPolicyManagerAgent.setRevisions(
        ("2002-08-02 12:07",
         "2001-09-07 15:27")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdPolicyManagerBaseAgent_ObjectIdentity = ObjectIdentity
usdPolicyManagerBaseAgent = _UsdPolicyManagerBaseAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1)
)
if mibBuilder.loadTexts:
    usdPolicyManagerBaseAgent.setStatus("current")
_UsdPolicyManagerRateLimitAgent_ObjectIdentity = ObjectIdentity
usdPolicyManagerRateLimitAgent = _UsdPolicyManagerRateLimitAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2)
)
if mibBuilder.loadTexts:
    usdPolicyManagerRateLimitAgent.setStatus("current")
_UsdPolicyManagerTrafficShapeAgent_ObjectIdentity = ObjectIdentity
usdPolicyManagerTrafficShapeAgent = _UsdPolicyManagerTrafficShapeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 3)
)
if mibBuilder.loadTexts:
    usdPolicyManagerTrafficShapeAgent.setStatus("current")
_UsdPolicyManagerLogRulesAgent_ObjectIdentity = ObjectIdentity
usdPolicyManagerLogRulesAgent = _UsdPolicyManagerLogRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4)
)
if mibBuilder.loadTexts:
    usdPolicyManagerLogRulesAgent.setStatus("current")
_UsdPolicyManagerNextHopRulesAgent_ObjectIdentity = ObjectIdentity
usdPolicyManagerNextHopRulesAgent = _UsdPolicyManagerNextHopRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5)
)
if mibBuilder.loadTexts:
    usdPolicyManagerNextHopRulesAgent.setStatus("current")
_UsdPolicyManagerFilterRulesAgent_ObjectIdentity = ObjectIdentity
usdPolicyManagerFilterRulesAgent = _UsdPolicyManagerFilterRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6)
)
if mibBuilder.loadTexts:
    usdPolicyManagerFilterRulesAgent.setStatus("current")
_UsdPolicyManagerNextInterfaceRulesAgent_ObjectIdentity = ObjectIdentity
usdPolicyManagerNextInterfaceRulesAgent = _UsdPolicyManagerNextInterfaceRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7)
)
if mibBuilder.loadTexts:
    usdPolicyManagerNextInterfaceRulesAgent.setStatus("current")
_UsdPolicyManagerMarkingRulesAgent_ObjectIdentity = ObjectIdentity
usdPolicyManagerMarkingRulesAgent = _UsdPolicyManagerMarkingRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8)
)
if mibBuilder.loadTexts:
    usdPolicyManagerMarkingRulesAgent.setStatus("current")
_UsdPolicyManagerForwardRulesAgent_ObjectIdentity = ObjectIdentity
usdPolicyManagerForwardRulesAgent = _UsdPolicyManagerForwardRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9)
)
if mibBuilder.loadTexts:
    usdPolicyManagerForwardRulesAgent.setStatus("current")
_UsdPolicyManagerColorRulesAgent_ObjectIdentity = ObjectIdentity
usdPolicyManagerColorRulesAgent = _UsdPolicyManagerColorRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10)
)
if mibBuilder.loadTexts:
    usdPolicyManagerColorRulesAgent.setStatus("current")
_UsdPolicyManagerTrafficClassRulesAgent_ObjectIdentity = ObjectIdentity
usdPolicyManagerTrafficClassRulesAgent = _UsdPolicyManagerTrafficClassRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11)
)
if mibBuilder.loadTexts:
    usdPolicyManagerTrafficClassRulesAgent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdPolicyManagerBaseAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 1)
)
if mibBuilder.loadTexts:
    usdPolicyManagerBaseAgentV1.setProductRelease("""\
Version 1 of the Policy Manager base component of the Unisphere Routing
        Switch SNMP agent.  This version of the Policy Manager base component is
        supported in the Unisphere RX 3.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPolicyManagerBaseAgentV1.setStatus(
        "current"
    )

usdPolicyManagerRateLimitAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 1)
)
if mibBuilder.loadTexts:
    usdPolicyManagerRateLimitAgentV1.setProductRelease("""\
Version 1 of the rate limit management subcomponent of the Policy
        Manager component of the Unisphere Routing Switch SNMP agent.  This
        version of the rate limit policy management subcomponent was supported
        in the Unisphere RX 3.2 and subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    usdPolicyManagerRateLimitAgentV1.setStatus(
        "obsolete"
    )

usdPolicyManagerRateLimitAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 2)
)
if mibBuilder.loadTexts:
    usdPolicyManagerRateLimitAgentV2.setProductRelease("""\
Version 2 of the rate limit management subcomponent of the Policy
        Manager component of the Unisphere Routing Switch SNMP agent.  This
        version of the rate limit policy management subcomponent is supported in
        the Unisphere RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPolicyManagerRateLimitAgentV2.setStatus(
        "current"
    )

usdPolicyManagerTrafficShapeAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 3, 1)
)
if mibBuilder.loadTexts:
    usdPolicyManagerTrafficShapeAgentV1.setProductRelease("""\
Version 1 of the traffic shape management subcomponent of the Policy
        Manager component of the Unisphere Routing Switch SNMP agent.  This
        version of the traffic shape policy management subcomponent was
        supported in the Unisphere RX 3.2 and subsequent 3.x system releases. """)
if mibBuilder.loadTexts:
    usdPolicyManagerTrafficShapeAgentV1.setStatus(
        "obsolete"
    )

usdPolicyManagerLogRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4, 1)
)
if mibBuilder.loadTexts:
    usdPolicyManagerLogRulesAgentV1.setProductRelease("""\
Version 1 of the log rules subcomponent of the Policy Manager component
        of the Unisphere Routing Switch SNMP agent.  This version of the log
        policy rules subcomponent is supported in the Unisphere RX 3.2 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPolicyManagerLogRulesAgentV1.setStatus(
        "current"
    )

usdPolicyManagerNextHopRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5, 1)
)
if mibBuilder.loadTexts:
    usdPolicyManagerNextHopRulesAgentV1.setProductRelease("""\
Version 1 of the next-hop rules subcomponent of the Policy Manager
        component of the Unisphere Routing Switch SNMP agent.  This version of
        the next-hop policy rules subcomponent is supported in the Unisphere RX
        3.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPolicyManagerNextHopRulesAgentV1.setStatus(
        "current"
    )

usdPolicyManagerFilterRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6, 1)
)
if mibBuilder.loadTexts:
    usdPolicyManagerFilterRulesAgentV1.setProductRelease("""\
Version 1 of the filter rules subcomponent of the Policy Manager
        component of the Unisphere Routing Switch SNMP agent.  This version of
        the filter policy rules subcomponent is supported in the Unisphere RX
        3.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPolicyManagerFilterRulesAgentV1.setStatus(
        "current"
    )

usdPolicyManagerNextInterfaceRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7, 1)
)
if mibBuilder.loadTexts:
    usdPolicyManagerNextInterfaceRulesAgentV1.setProductRelease("""\
Version 1 of the next-interface rules subcomponent of the Policy
        Manager component of the Unisphere Routing Switch SNMP agent.  This
        version of the next-interface policy rules subcomponent is supported in
        the Unisphere RX 3.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPolicyManagerNextInterfaceRulesAgentV1.setStatus(
        "current"
    )

usdPolicyManagerMarkingRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8, 1)
)
if mibBuilder.loadTexts:
    usdPolicyManagerMarkingRulesAgentV1.setProductRelease("""\
Version 1 of the marking rules subcomponent of the Policy Manager
        component of the Unisphere Routing Switch SNMP agent.  This version of
        the marking policy rules subcomponent is supported in the Unisphere RX
        3.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPolicyManagerMarkingRulesAgentV1.setStatus(
        "current"
    )

usdPolicyManagerForwardRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9, 1)
)
if mibBuilder.loadTexts:
    usdPolicyManagerForwardRulesAgentV1.setProductRelease("""\
Version 1 of the forward rules subcomponent of the Policy Manager
        component of the Unisphere Routing Switch SNMP agent.  This version of
        the forward policy rules subcomponent is supported in the Unisphere RX
        3.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPolicyManagerForwardRulesAgentV1.setStatus(
        "current"
    )

usdPolicyManagerColorRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10, 1)
)
if mibBuilder.loadTexts:
    usdPolicyManagerColorRulesAgentV1.setProductRelease("""\
Version 1 of the color rules subcomponent of the Policy Manager
        component of the Unisphere Routing Switch SNMP agent.  This version of
        the color policy rules subcomponent is supported in the Unisphere RX 3.2
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPolicyManagerColorRulesAgentV1.setStatus(
        "current"
    )

usdPolicyManagerTrafficClassRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11, 1)
)
if mibBuilder.loadTexts:
    usdPolicyManagerTrafficClassRulesAgentV1.setProductRelease("""\
Version 1 of the traffic class rules subcomponent of the Policy Manager
        component of the Unisphere Routing Switch SNMP agent.  This version of
        the traffic class policy rules subcomponent is supported in the
        Unisphere RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdPolicyManagerTrafficClassRulesAgentV1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-Policy-Manager-CONF",
    **{"usdPolicyManagerAgent": usdPolicyManagerAgent,
       "usdPolicyManagerBaseAgent": usdPolicyManagerBaseAgent,
       "usdPolicyManagerBaseAgentV1": usdPolicyManagerBaseAgentV1,
       "usdPolicyManagerRateLimitAgent": usdPolicyManagerRateLimitAgent,
       "usdPolicyManagerRateLimitAgentV1": usdPolicyManagerRateLimitAgentV1,
       "usdPolicyManagerRateLimitAgentV2": usdPolicyManagerRateLimitAgentV2,
       "usdPolicyManagerTrafficShapeAgent": usdPolicyManagerTrafficShapeAgent,
       "usdPolicyManagerTrafficShapeAgentV1": usdPolicyManagerTrafficShapeAgentV1,
       "usdPolicyManagerLogRulesAgent": usdPolicyManagerLogRulesAgent,
       "usdPolicyManagerLogRulesAgentV1": usdPolicyManagerLogRulesAgentV1,
       "usdPolicyManagerNextHopRulesAgent": usdPolicyManagerNextHopRulesAgent,
       "usdPolicyManagerNextHopRulesAgentV1": usdPolicyManagerNextHopRulesAgentV1,
       "usdPolicyManagerFilterRulesAgent": usdPolicyManagerFilterRulesAgent,
       "usdPolicyManagerFilterRulesAgentV1": usdPolicyManagerFilterRulesAgentV1,
       "usdPolicyManagerNextInterfaceRulesAgent": usdPolicyManagerNextInterfaceRulesAgent,
       "usdPolicyManagerNextInterfaceRulesAgentV1": usdPolicyManagerNextInterfaceRulesAgentV1,
       "usdPolicyManagerMarkingRulesAgent": usdPolicyManagerMarkingRulesAgent,
       "usdPolicyManagerMarkingRulesAgentV1": usdPolicyManagerMarkingRulesAgentV1,
       "usdPolicyManagerForwardRulesAgent": usdPolicyManagerForwardRulesAgent,
       "usdPolicyManagerForwardRulesAgentV1": usdPolicyManagerForwardRulesAgentV1,
       "usdPolicyManagerColorRulesAgent": usdPolicyManagerColorRulesAgent,
       "usdPolicyManagerColorRulesAgentV1": usdPolicyManagerColorRulesAgentV1,
       "usdPolicyManagerTrafficClassRulesAgent": usdPolicyManagerTrafficClassRulesAgent,
       "usdPolicyManagerTrafficClassRulesAgentV1": usdPolicyManagerTrafficClassRulesAgentV1}
)
