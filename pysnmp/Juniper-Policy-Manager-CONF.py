# SNMP MIB module (Juniper-Policy-Manager-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-Policy-Manager-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:05 2024
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

(juniAgents,) = mibBuilder.importSymbols(
    "Juniper-Agents",
    "juniAgents")

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


# MODULE-IDENTITY

juniPolicyManagerAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31)
)
juniPolicyManagerAgent.setRevisions(
        ("2005-08-08 18:21",
         "2005-02-01 15:58",
         "2003-10-21 19:20",
         "2003-08-26 12:51",
         "2002-09-06 16:54",
         "2002-08-02 12:07",
         "2001-09-07 15:27")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniPolicyManagerBaseAgent_ObjectIdentity = ObjectIdentity
juniPolicyManagerBaseAgent = _JuniPolicyManagerBaseAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1)
)
if mibBuilder.loadTexts:
    juniPolicyManagerBaseAgent.setStatus("current")
_JuniPolicyManagerRateLimitAgent_ObjectIdentity = ObjectIdentity
juniPolicyManagerRateLimitAgent = _JuniPolicyManagerRateLimitAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerRateLimitAgent.setStatus("current")
_JuniPolicyManagerTrafficShapeAgent_ObjectIdentity = ObjectIdentity
juniPolicyManagerTrafficShapeAgent = _JuniPolicyManagerTrafficShapeAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 3)
)
if mibBuilder.loadTexts:
    juniPolicyManagerTrafficShapeAgent.setStatus("obsolete")
_JuniPolicyManagerLogRulesAgent_ObjectIdentity = ObjectIdentity
juniPolicyManagerLogRulesAgent = _JuniPolicyManagerLogRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4)
)
if mibBuilder.loadTexts:
    juniPolicyManagerLogRulesAgent.setStatus("current")
_JuniPolicyManagerNextHopRulesAgent_ObjectIdentity = ObjectIdentity
juniPolicyManagerNextHopRulesAgent = _JuniPolicyManagerNextHopRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5)
)
if mibBuilder.loadTexts:
    juniPolicyManagerNextHopRulesAgent.setStatus("current")
_JuniPolicyManagerFilterRulesAgent_ObjectIdentity = ObjectIdentity
juniPolicyManagerFilterRulesAgent = _JuniPolicyManagerFilterRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6)
)
if mibBuilder.loadTexts:
    juniPolicyManagerFilterRulesAgent.setStatus("current")
_JuniPolicyManagerNextInterfaceRulesAgent_ObjectIdentity = ObjectIdentity
juniPolicyManagerNextInterfaceRulesAgent = _JuniPolicyManagerNextInterfaceRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7)
)
if mibBuilder.loadTexts:
    juniPolicyManagerNextInterfaceRulesAgent.setStatus("current")
_JuniPolicyManagerMarkingRulesAgent_ObjectIdentity = ObjectIdentity
juniPolicyManagerMarkingRulesAgent = _JuniPolicyManagerMarkingRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8)
)
if mibBuilder.loadTexts:
    juniPolicyManagerMarkingRulesAgent.setStatus("current")
_JuniPolicyManagerForwardRulesAgent_ObjectIdentity = ObjectIdentity
juniPolicyManagerForwardRulesAgent = _JuniPolicyManagerForwardRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9)
)
if mibBuilder.loadTexts:
    juniPolicyManagerForwardRulesAgent.setStatus("current")
_JuniPolicyManagerColorRulesAgent_ObjectIdentity = ObjectIdentity
juniPolicyManagerColorRulesAgent = _JuniPolicyManagerColorRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10)
)
if mibBuilder.loadTexts:
    juniPolicyManagerColorRulesAgent.setStatus("current")
_JuniPolicyManagerTrafficClassRulesAgent_ObjectIdentity = ObjectIdentity
juniPolicyManagerTrafficClassRulesAgent = _JuniPolicyManagerTrafficClassRulesAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11)
)
if mibBuilder.loadTexts:
    juniPolicyManagerTrafficClassRulesAgent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniPolicyManagerBaseAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 1)
)
if mibBuilder.loadTexts:
    juniPolicyManagerBaseAgentV1.setProductRelease("""\
Version 1 of the Policy Manager base component of the JUNOSe SNMP
        agent.  This version of the Policy Manager base component was supported
        in JUNOSe 3.2 thru 5.2 system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerBaseAgentV1.setStatus(
        "obsolete"
    )

juniPolicyManagerBaseAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerBaseAgentV2.setProductRelease("""\
Version 2 of the Policy Manager base component of the JUNOSe SNMP
        agent.  This version of the Policy Manager base component is supported
        in JUNOSe 5.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerBaseAgentV2.setStatus(
        "obsolete"
    )

juniPolicyManagerBaseAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerBaseAgentV3.setProductRelease("""\
Version 3 of the Policy Manager base component of the JUNOSe SNMP
        agent.  This version of the Policy Manager base component is supported
        in JUNOSe 6.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerBaseAgentV3.setStatus(
        "obsolete"
    )

juniPolicyManagerBaseAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 1, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerBaseAgentV4.setProductRelease("""\
Version 4 of the Policy Manager base component of the JUNOSe SNMP
        agent.  This version of the Policy Manager base component is supported
        in JUNOSe 7.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerBaseAgentV4.setStatus(
        "current"
    )

juniPolicyManagerRateLimitAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 1)
)
if mibBuilder.loadTexts:
    juniPolicyManagerRateLimitAgentV1.setProductRelease("""\
Version 1 of the rate limit management subcomponent of the Policy
        Manager component of the JUNOSe SNMP agent.  This version of the rate
        limit policy management subcomponent was supported in JUNOSe 3.2 and
        subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerRateLimitAgentV1.setStatus(
        "obsolete"
    )

juniPolicyManagerRateLimitAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerRateLimitAgentV2.setProductRelease("""\
Version 2 of the rate limit management subcomponent of the Policy
        Manager component of the JUNOSe SNMP agent.  This version of the rate
        limit policy management subcomponent was supported in JUNOSe 4.0 thru
        5.2 system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerRateLimitAgentV2.setStatus(
        "obsolete"
    )

juniPolicyManagerRateLimitAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 2, 3)
)
if mibBuilder.loadTexts:
    juniPolicyManagerRateLimitAgentV3.setProductRelease("""\
Version 3 of the rate limit management subcomponent of the Policy
        Manager component of JUNOSe SNMP agent.  This version of the rate limit
        policy management subcomponent is supported in the Juniper RX 5.3 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerRateLimitAgentV3.setStatus(
        "current"
    )

juniPolicyManagerTrafficShapeAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 3, 1)
)
if mibBuilder.loadTexts:
    juniPolicyManagerTrafficShapeAgentV1.setProductRelease("""\
Version 1 of the traffic shape management subcomponent of the Policy
        Manager component of the JUNOSe SNMP agent.  This version of the traffic
        shape policy management subcomponent was supported in JUNOSe 3.2 and
        subsequent 3.x system releases. """)
if mibBuilder.loadTexts:
    juniPolicyManagerTrafficShapeAgentV1.setStatus(
        "obsolete"
    )

juniPolicyManagerLogRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4, 1)
)
if mibBuilder.loadTexts:
    juniPolicyManagerLogRulesAgentV1.setProductRelease("""\
Version 1 of the log rules subcomponent of the Policy Manager component
        of the JUNOSe SNMP agent.  This version of the log policy rules
        subcomponent was supported in JUNOSe 3.2 thru 5.2 system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerLogRulesAgentV1.setStatus(
        "obsolete"
    )

juniPolicyManagerLogRulesAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 4, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerLogRulesAgentV2.setProductRelease("""\
Version 2 of the log rules subcomponent of the Policy Manager component
        of the JUNOSe SNMP agent.  This version of the log policy rules
        subcomponent is supported in JUNOSe 5.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerLogRulesAgentV2.setStatus(
        "current"
    )

juniPolicyManagerNextHopRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5, 1)
)
if mibBuilder.loadTexts:
    juniPolicyManagerNextHopRulesAgentV1.setProductRelease("""\
Version 1 of the next-hop rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the next-hop policy
        rules subcomponent was supported in JUNOSe 3.2 thru 5.2 system
        releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerNextHopRulesAgentV1.setStatus(
        "obsolete"
    )

juniPolicyManagerNextHopRulesAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 5, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerNextHopRulesAgentV2.setProductRelease("""\
Version 2 of the next-hop rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the next-hop policy
        rules subcomponent is supported in JUNOSe 5.3 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerNextHopRulesAgentV2.setStatus(
        "current"
    )

juniPolicyManagerFilterRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6, 1)
)
if mibBuilder.loadTexts:
    juniPolicyManagerFilterRulesAgentV1.setProductRelease("""\
Version 1 of the filter rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the filter policy
        rules subcomponent is supported in JUNOSe 3.2 thru 5.2 system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerFilterRulesAgentV1.setStatus(
        "obsolete"
    )

juniPolicyManagerFilterRulesAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 6, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerFilterRulesAgentV2.setProductRelease("""\
Version 2 of the filter rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the filter policy
        rules subcomponent is supported in JUNOSe 5.3 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerFilterRulesAgentV2.setStatus(
        "current"
    )

juniPolicyManagerNextInterfaceRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7, 1)
)
if mibBuilder.loadTexts:
    juniPolicyManagerNextInterfaceRulesAgentV1.setProductRelease("""\
Version 1 of the next-interface rules subcomponent of the Policy
        Manager component of the JUNOSe SNMP agent.  This version of the
        next-interface policy rules subcomponent was supported in JUNOSe 3.2
        thru 5.2 system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerNextInterfaceRulesAgentV1.setStatus(
        "obsolete"
    )

juniPolicyManagerNextInterfaceRulesAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 7, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerNextInterfaceRulesAgentV2.setProductRelease("""\
Version 2 of the next-interface rules subcomponent of the Policy
        Manager component of the JUNOSe SNMP agent.  This version of the
        next-interface policy rules subcomponent is supported in JUNOSe 5.3 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerNextInterfaceRulesAgentV2.setStatus(
        "current"
    )

juniPolicyManagerMarkingRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8, 1)
)
if mibBuilder.loadTexts:
    juniPolicyManagerMarkingRulesAgentV1.setProductRelease("""\
Version 1 of the marking rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the marking policy
        rules subcomponent was supported in JUNOSe 3.2 thru 5.2 system
        releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerMarkingRulesAgentV1.setStatus(
        "obsolete"
    )

juniPolicyManagerMarkingRulesAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 8, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerMarkingRulesAgentV2.setProductRelease("""\
Version 2 of the marking rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the marking policy
        rules subcomponent is supported in JUNOSe 5.3 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerMarkingRulesAgentV2.setStatus(
        "current"
    )

juniPolicyManagerForwardRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9, 1)
)
if mibBuilder.loadTexts:
    juniPolicyManagerForwardRulesAgentV1.setProductRelease("""\
Version 1 of the forward rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the forward policy
        rules subcomponent was supported in JUNOSe 3.2 thru 5.1 system
        releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerForwardRulesAgentV1.setStatus(
        "obsolete"
    )

juniPolicyManagerForwardRulesAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerForwardRulesAgentV2.setProductRelease("""\
Version 2 of the forward rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the forward policy
        rules subcomponent was supported in JUNOSe 5.2 system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerForwardRulesAgentV2.setStatus(
        "obsolete"
    )

juniPolicyManagerForwardRulesAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 9, 3)
)
if mibBuilder.loadTexts:
    juniPolicyManagerForwardRulesAgentV3.setProductRelease("""\
Version 3 of the forward rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the forward policy
        rules subcomponent is supported in JUNOSe 5.3 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerForwardRulesAgentV3.setStatus(
        "current"
    )

juniPolicyManagerColorRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10, 1)
)
if mibBuilder.loadTexts:
    juniPolicyManagerColorRulesAgentV1.setProductRelease("""\
Version 1 of the color rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the color policy
        rules subcomponent was supported in JUNOSe 3.2 thru 5.2 system
        releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerColorRulesAgentV1.setStatus(
        "obsolete"
    )

juniPolicyManagerColorRulesAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 10, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerColorRulesAgentV2.setProductRelease("""\
Version 2 of the color rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the color policy
        rules subcomponent is supported in JUNOSe 5.3 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerColorRulesAgentV2.setStatus(
        "current"
    )

juniPolicyManagerTrafficClassRulesAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11, 1)
)
if mibBuilder.loadTexts:
    juniPolicyManagerTrafficClassRulesAgentV1.setProductRelease("""\
Version 1 of the traffic class rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the traffic class
        policy rules subcomponent was supported in JUNOSe 4.0 thru 5.2 system
        releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerTrafficClassRulesAgentV1.setStatus(
        "obsolete"
    )

juniPolicyManagerTrafficClassRulesAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 31, 11, 2)
)
if mibBuilder.loadTexts:
    juniPolicyManagerTrafficClassRulesAgentV2.setProductRelease("""\
Version 2 of the traffic class rules subcomponent of the Policy Manager
        component of the JUNOSe SNMP agent.  This version of the traffic class
        policy rules subcomponent is supported in JUNOSe 5.3 and subsequent
        system releases.""")
if mibBuilder.loadTexts:
    juniPolicyManagerTrafficClassRulesAgentV2.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-Policy-Manager-CONF",
    **{"juniPolicyManagerAgent": juniPolicyManagerAgent,
       "juniPolicyManagerBaseAgent": juniPolicyManagerBaseAgent,
       "juniPolicyManagerBaseAgentV1": juniPolicyManagerBaseAgentV1,
       "juniPolicyManagerBaseAgentV2": juniPolicyManagerBaseAgentV2,
       "juniPolicyManagerBaseAgentV3": juniPolicyManagerBaseAgentV3,
       "juniPolicyManagerBaseAgentV4": juniPolicyManagerBaseAgentV4,
       "juniPolicyManagerRateLimitAgent": juniPolicyManagerRateLimitAgent,
       "juniPolicyManagerRateLimitAgentV1": juniPolicyManagerRateLimitAgentV1,
       "juniPolicyManagerRateLimitAgentV2": juniPolicyManagerRateLimitAgentV2,
       "juniPolicyManagerRateLimitAgentV3": juniPolicyManagerRateLimitAgentV3,
       "juniPolicyManagerTrafficShapeAgent": juniPolicyManagerTrafficShapeAgent,
       "juniPolicyManagerTrafficShapeAgentV1": juniPolicyManagerTrafficShapeAgentV1,
       "juniPolicyManagerLogRulesAgent": juniPolicyManagerLogRulesAgent,
       "juniPolicyManagerLogRulesAgentV1": juniPolicyManagerLogRulesAgentV1,
       "juniPolicyManagerLogRulesAgentV2": juniPolicyManagerLogRulesAgentV2,
       "juniPolicyManagerNextHopRulesAgent": juniPolicyManagerNextHopRulesAgent,
       "juniPolicyManagerNextHopRulesAgentV1": juniPolicyManagerNextHopRulesAgentV1,
       "juniPolicyManagerNextHopRulesAgentV2": juniPolicyManagerNextHopRulesAgentV2,
       "juniPolicyManagerFilterRulesAgent": juniPolicyManagerFilterRulesAgent,
       "juniPolicyManagerFilterRulesAgentV1": juniPolicyManagerFilterRulesAgentV1,
       "juniPolicyManagerFilterRulesAgentV2": juniPolicyManagerFilterRulesAgentV2,
       "juniPolicyManagerNextInterfaceRulesAgent": juniPolicyManagerNextInterfaceRulesAgent,
       "juniPolicyManagerNextInterfaceRulesAgentV1": juniPolicyManagerNextInterfaceRulesAgentV1,
       "juniPolicyManagerNextInterfaceRulesAgentV2": juniPolicyManagerNextInterfaceRulesAgentV2,
       "juniPolicyManagerMarkingRulesAgent": juniPolicyManagerMarkingRulesAgent,
       "juniPolicyManagerMarkingRulesAgentV1": juniPolicyManagerMarkingRulesAgentV1,
       "juniPolicyManagerMarkingRulesAgentV2": juniPolicyManagerMarkingRulesAgentV2,
       "juniPolicyManagerForwardRulesAgent": juniPolicyManagerForwardRulesAgent,
       "juniPolicyManagerForwardRulesAgentV1": juniPolicyManagerForwardRulesAgentV1,
       "juniPolicyManagerForwardRulesAgentV2": juniPolicyManagerForwardRulesAgentV2,
       "juniPolicyManagerForwardRulesAgentV3": juniPolicyManagerForwardRulesAgentV3,
       "juniPolicyManagerColorRulesAgent": juniPolicyManagerColorRulesAgent,
       "juniPolicyManagerColorRulesAgentV1": juniPolicyManagerColorRulesAgentV1,
       "juniPolicyManagerColorRulesAgentV2": juniPolicyManagerColorRulesAgentV2,
       "juniPolicyManagerTrafficClassRulesAgent": juniPolicyManagerTrafficClassRulesAgent,
       "juniPolicyManagerTrafficClassRulesAgentV1": juniPolicyManagerTrafficClassRulesAgentV1,
       "juniPolicyManagerTrafficClassRulesAgentV2": juniPolicyManagerTrafficClassRulesAgentV2}
)
