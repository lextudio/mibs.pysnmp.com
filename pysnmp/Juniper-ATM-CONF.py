# SNMP MIB module (Juniper-ATM-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-ATM-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:40 2024
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

juniAtmAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3)
)
juniAtmAgent.setRevisions(
        ("2005-08-17 17:26",
         "2005-02-17 23:15",
         "2004-01-06 19:53",
         "2003-11-07 14:57",
         "2003-05-08 17:57",
         "2002-09-06 16:54",
         "2002-08-09 14:15",
         "2002-01-29 15:18",
         "2002-01-24 14:16",
         "2001-12-14 19:51",
         "2001-05-23 16:12")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniAtmVccEndPointAgent_ObjectIdentity = ObjectIdentity
juniAtmVccEndPointAgent = _JuniAtmVccEndPointAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1)
)
_JuniAtmVpTunnelAgent_ObjectIdentity = ObjectIdentity
juniAtmVpTunnelAgent = _JuniAtmVpTunnelAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 2)
)
_JuniAtmNbmaAgent_ObjectIdentity = ObjectIdentity
juniAtmNbmaAgent = _JuniAtmNbmaAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 3)
)
_JuniAtmSwitchAgent_ObjectIdentity = ObjectIdentity
juniAtmSwitchAgent = _JuniAtmSwitchAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 4)
)
_JuniAtmSwitchAgentV1_ObjectIdentity = ObjectIdentity
juniAtmSwitchAgentV1 = _JuniAtmSwitchAgentV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 4, 1)
)
_JuniAtmSwitchAgentV2_ObjectIdentity = ObjectIdentity
juniAtmSwitchAgentV2 = _JuniAtmSwitchAgentV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 4, 2)
)
_JuniAtmTrafficShapingAgent_ObjectIdentity = ObjectIdentity
juniAtmTrafficShapingAgent = _JuniAtmTrafficShapingAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniAtmVccEndPointAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV1.setProductRelease("""\
Version 1 of the ATM VCC end point agent subcomponent of the JUNOSe
        SNMP agent.  This version of the ATM end point subcomponent was
        supported in JUNOSe 3.0 and 3.1 system releases.""")
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV1.setStatus(
        "obsolete"
    )

juniAtmVccEndPointAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV2.setProductRelease("""\
Version 2 of the ATM VCC end point agent subcomponent of the JUNOSe
        SNMP agent.  This version of the ATM end point subcomponent was
        supported in JUNOSe 3.2 and JUNOSe 3.3 system releases.""")
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV2.setStatus(
        "obsolete"
    )

juniAtmVccEndPointAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV3.setProductRelease("""\
Version 3 of the ATM VCC end point agent subcomponent of the JUNOSe
        SNMP agent.  This version of the ATM end point subcomponent was
        supported in JUNOSe 3.4 and subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV3.setStatus(
        "obsolete"
    )

juniAtmVccEndPointAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV4.setProductRelease("""\
Version 4 of the ATM VCC end point agent subcomponent of the JUNOSe
        SNMP agent.  This version of the ATM end point subcomponent was
        supported in JUNOSe 4.0 system releases.""")
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV4.setStatus(
        "obsolete"
    )

juniAtmVccEndPointAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 5)
)
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV5.setProductRelease("""\
Version 5 of the ATM VCC end point agent subcomponent of the JUNOSe
        SNMP agent.  This version of the ATM end point subcomponent was
        supported in JUNOSe 4.1 thru 5.0 system releases.""")
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV5.setStatus(
        "obsolete"
    )

juniAtmVccEndPointAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 6)
)
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV6.setProductRelease("""\
Version 6 of the ATM VCC end point agent subcomponent of the JUNOSe
        SNMP agent.  This version of the ATM end point subcomponent was
        supported in JUNOSe 5.1 system releases.""")
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV6.setStatus(
        "obsolete"
    )

juniAtmVccEndPointAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 7)
)
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV7.setProductRelease("""\
Version 7 of the ATM VCC end point agent subcomponent of the JUNOSe
        SNMP agent.  This version of the ATM end point subcomponent was supported
        in JUNOSe 5.2 system release.""")
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV7.setStatus(
        "obsolete"
    )

juniAtmVccEndPointAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 8)
)
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV8.setProductRelease("""\
Version 8 of the ATM VCC end point agent subcomponent of the JUNOSe
        SNMP agent.  This version of the ATM end point subcomponent was supported
        in JUNOSe 5.3 and 6.0 system releases.""")
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV8.setStatus(
        "obsolete"
    )

juniAtmVccEndPointAgentV9 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 9)
)
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV9.setProductRelease("""\
Version 9 of the ATM VCC end point agent subcomponent of the JUNOSe
        SNMP agent.  This version of the ATM end point subcomponent was supported
        in JUNOSe 6.1 system release.""")
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV9.setStatus(
        "obsolete"
    )

juniAtmVccEndPointAgentV10 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 10)
)
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV10.setProductRelease("""\
Version 10 of the ATM VCC end point agent subcomponent of the JUNOSe
        SNMP agent.  This version of the ATM end point subcomponent is supported
        in JUNOSe 7.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV10.setStatus(
        "obsolete"
    )

juniAtmVccEndPointAgentV11 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 11)
)
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV11.setProductRelease("""\
Version 11 of the ATM VCC end point agent subcomponent of the JUNOSe
        SNMP agent.  This version of the ATM end point subcomponent is supported
        in JUNOSe 7.1 and 7.2 system releases.""")
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV11.setStatus(
        "obsolete"
    )

juniAtmVccEndPointAgentV12 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 1, 12)
)
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV12.setProductRelease("""\
Version 12 of the ATM VCC end point agent subcomponent of the JUNOSe
        SNMP agent.  This version of the ATM end point subcomponent is supported
        in JUNOSe 7.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAtmVccEndPointAgentV12.setStatus(
        "current"
    )

juniAtmVpTunnelAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    juniAtmVpTunnelAgentV1.setProductRelease("""\
Version 1 of the ATM VP tunnel subcomponent of the JUNOSe SNMP agent.
        This version of the ATM tunnel subcomponent is supported in JUNOSe 3.0
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAtmVpTunnelAgentV1.setStatus(
        "current"
    )

juniAtmNbmaAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    juniAtmNbmaAgentV1.setProductRelease("""\
Version 1 of the ATM NBMA interface subcomponent of the JUNOSe SNMP
        agent.  This version of the ATM NBMA subcomponent is supported in JUNOSe
        3.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAtmNbmaAgentV1.setStatus(
        "current"
    )

juniAtmTrafficShapingAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    juniAtmTrafficShapingAgentV1.setProductRelease("""\
Version 1 of the ATM traffic shaping subcomponent of the JUNOSe SNMP
        agent.  This version of the ATM traffic shaping subcomponent is
        supported in JUNOSe 3.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAtmTrafficShapingAgentV1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-ATM-CONF",
    **{"juniAtmAgent": juniAtmAgent,
       "juniAtmVccEndPointAgent": juniAtmVccEndPointAgent,
       "juniAtmVccEndPointAgentV1": juniAtmVccEndPointAgentV1,
       "juniAtmVccEndPointAgentV2": juniAtmVccEndPointAgentV2,
       "juniAtmVccEndPointAgentV3": juniAtmVccEndPointAgentV3,
       "juniAtmVccEndPointAgentV4": juniAtmVccEndPointAgentV4,
       "juniAtmVccEndPointAgentV5": juniAtmVccEndPointAgentV5,
       "juniAtmVccEndPointAgentV6": juniAtmVccEndPointAgentV6,
       "juniAtmVccEndPointAgentV7": juniAtmVccEndPointAgentV7,
       "juniAtmVccEndPointAgentV8": juniAtmVccEndPointAgentV8,
       "juniAtmVccEndPointAgentV9": juniAtmVccEndPointAgentV9,
       "juniAtmVccEndPointAgentV10": juniAtmVccEndPointAgentV10,
       "juniAtmVccEndPointAgentV11": juniAtmVccEndPointAgentV11,
       "juniAtmVccEndPointAgentV12": juniAtmVccEndPointAgentV12,
       "juniAtmVpTunnelAgent": juniAtmVpTunnelAgent,
       "juniAtmVpTunnelAgentV1": juniAtmVpTunnelAgentV1,
       "juniAtmNbmaAgent": juniAtmNbmaAgent,
       "juniAtmNbmaAgentV1": juniAtmNbmaAgentV1,
       "juniAtmSwitchAgent": juniAtmSwitchAgent,
       "juniAtmSwitchAgentV1": juniAtmSwitchAgentV1,
       "juniAtmSwitchAgentV2": juniAtmSwitchAgentV2,
       "juniAtmTrafficShapingAgent": juniAtmTrafficShapingAgent,
       "juniAtmTrafficShapingAgentV1": juniAtmTrafficShapingAgentV1}
)
