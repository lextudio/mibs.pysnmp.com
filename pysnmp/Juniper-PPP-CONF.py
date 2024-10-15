# SNMP MIB module (Juniper-PPP-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-PPP-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:56 2024
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

juniPppAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32)
)
juniPppAgent.setRevisions(
        ("2010-02-09 11:06",
         "2009-09-18 07:24",
         "2009-08-10 14:23",
         "2008-08-27 13:18",
         "2007-07-12 12:15",
         "2005-10-19 16:26",
         "2004-10-01 21:41",
         "2003-11-03 18:32",
         "2003-09-24 20:11",
         "2003-01-28 15:47",
         "2002-08-30 20:36",
         "2002-05-09 21:03",
         "2002-05-08 20:25",
         "2001-04-10 18:23")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniPppGeneralAgent_ObjectIdentity = ObjectIdentity
juniPppGeneralAgent = _JuniPppGeneralAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2)
)
if mibBuilder.loadTexts:
    juniPppGeneralAgent.setStatus("current")
_JuniPppMultiLinkAgent_ObjectIdentity = ObjectIdentity
juniPppMultiLinkAgent = _JuniPppMultiLinkAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3)
)
if mibBuilder.loadTexts:
    juniPppMultiLinkAgent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniPppAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 1)
)
if mibBuilder.loadTexts:
    juniPppAgentV1.setProductRelease("""\
Version 1 of the PPP component of the JUNOSe SNMP agent.  This version
        of the PPP component was supported in JUNOSe 2.4 thru 3.2 system
        releases.""")
if mibBuilder.loadTexts:
    juniPppAgentV1.setStatus(
        "obsolete"
    )

juniPppGeneralAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 1)
)
if mibBuilder.loadTexts:
    juniPppGeneralAgentV1.setProductRelease("""\
Version 1 of the general PPP component of the JUNOSe SNMP agent.  This
        version of the PPP component was supported in JUNOSe 3.3 and subsequent
        3.x system releases.""")
if mibBuilder.loadTexts:
    juniPppGeneralAgentV1.setStatus(
        "obsolete"
    )

juniPppGeneralAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 2)
)
if mibBuilder.loadTexts:
    juniPppGeneralAgentV2.setProductRelease("""\
Version 2 of the general PPP component of the JUNOSe SNMP agent.  This
        version of the PPP component was supported in JUNOSe 4.0 system
        releases.""")
if mibBuilder.loadTexts:
    juniPppGeneralAgentV2.setStatus(
        "obsolete"
    )

juniPppGeneralAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 3)
)
if mibBuilder.loadTexts:
    juniPppGeneralAgentV3.setProductRelease("""\
Version 3 of the general PPP component of the JUNOSe SNMP agent.  This
        version of the PPP component was supported in JUNOSe 4.1 through 5.0
        system releases.""")
if mibBuilder.loadTexts:
    juniPppGeneralAgentV3.setStatus(
        "obsolete"
    )

juniPppGeneralAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 4)
)
if mibBuilder.loadTexts:
    juniPppGeneralAgentV4.setProductRelease("""\
Version 4 of the general PPP component of the JUNOSe SNMP agent.  This
        version of the PPP component was supported in JUNOSe 5.1 and subsequent
        5.x system releases.""")
if mibBuilder.loadTexts:
    juniPppGeneralAgentV4.setStatus(
        "obsolete"
    )

juniPppGeneralAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 5)
)
if mibBuilder.loadTexts:
    juniPppGeneralAgentV5.setProductRelease("""\
Version 5 of the general PPP component of the JUNOSe SNMP agent.  This
        version of the PPP component is supported in JUNOSe 6.0 throught 7.2
        system releases.""")
if mibBuilder.loadTexts:
    juniPppGeneralAgentV5.setStatus(
        "obsolete"
    )

juniPppGeneralAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 6)
)
if mibBuilder.loadTexts:
    juniPppGeneralAgentV6.setProductRelease("""\
Version 6 of the general PPP component of the JUNOSe SNMP agent.  This
        version of the PPP component is supported in JUNOSe 7.3 and subsequent
        system releases.""")
if mibBuilder.loadTexts:
    juniPppGeneralAgentV6.setStatus(
        "obsolete"
    )

juniPppGeneralAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 7)
)
if mibBuilder.loadTexts:
    juniPppGeneralAgentV7.setProductRelease("""\
Version 7 of the general PPP component of the JUNOSe SNMP agent.  This
        version of the PPP component is supported in JUNOSe 10.1 and subsequent
        system releases.""")
if mibBuilder.loadTexts:
    juniPppGeneralAgentV7.setStatus(
        "obsolete"
    )

juniPppGeneralAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 8)
)
if mibBuilder.loadTexts:
    juniPppGeneralAgentV8.setProductRelease("""\
Version 8 of the general PPP component of the JUNOSe SNMP agent.  This
        version of the PPP component is supported in JUNOSe 11.0 and subsequent
        system releases.""")
if mibBuilder.loadTexts:
    juniPppGeneralAgentV8.setStatus(
        "obsolete"
    )

juniPppGeneralAgentV9 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 2, 9)
)
if mibBuilder.loadTexts:
    juniPppGeneralAgentV9.setProductRelease("""\
Version 9 of the general PPP component of the JUNOSe SNMP agent. This
        version of the PPP component is supported in JUNOSe 11.2 and subsequent
        system releases.""")
if mibBuilder.loadTexts:
    juniPppGeneralAgentV9.setStatus(
        "current"
    )

juniPppMultiLinkAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 1)
)
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV1.setProductRelease("""\
Version 1 of the multi-link PPP component of the JUNOSe SNMP agent.
        This version of the PPP component was supported in JUNOSe 3.3 and
        subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV1.setStatus(
        "obsolete"
    )

juniPppMultiLinkAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 2)
)
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV2.setProductRelease("""\
Version 2 of the multi-link PPP component of the JUNOSe SNMP agent.
        This version of the PPP component was supported in JUNOSe 4.0 system
        releases.""")
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV2.setStatus(
        "obsolete"
    )

juniPppMultiLinkAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 3)
)
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV3.setProductRelease("""\
Version 3 of the multi-link PPP component of the JUNOSe SNMP agent.
        This version of the PPP component was supported in JUNOSe 4.1 and
        subsequent 4.x system releases.""")
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV3.setStatus(
        "obsolete"
    )

juniPppMultiLinkAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 4)
)
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV4.setProductRelease("""\
Version 4 of the multi-link PPP component of the JUNOSe SNMP agent.
        This version of the PPP component was supported in JUNOSe 5.0 system
        releases.""")
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV4.setStatus(
        "obsolete"
    )

juniPppMultiLinkAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 5)
)
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV5.setProductRelease("""\
Version 5 of the multi-link PPP component of the JUNOSe SNMP agent.
        This version of the PPP component was supported in JUNOSe 5.1 and 5.2
        system releases.""")
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV5.setStatus(
        "obsolete"
    )

juniPppMultiLinkAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 6)
)
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV6.setProductRelease("""\
Version 6 of the multi-link PPP component of the JUNOSe SNMP agent.
        This version of the PPP component was supported in JUNOSe 5.1 and 
        subsequent 5.x system releases.""")
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV6.setStatus(
        "obsolete"
    )

juniPppMultiLinkAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 7)
)
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV7.setProductRelease("""\
Version 7 of the multi-link PPP component of the JUNOSe SNMP agent.
        This version of the PPP component is supported in JUNOSe 6.0 through
        7.2 system releases.""")
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV7.setStatus(
        "obsolete"
    )

juniPppMultiLinkAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 8)
)
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV8.setProductRelease("""\
Version 8 of the multi-link PPP component of the JUNOSe SNMP agent.
        This version of the PPP component is supported in JUNOSe 7.2 system
        releases.""")
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV8.setStatus(
        "obsolete"
    )

juniPppMultiLinkAgentV9 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 9)
)
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV9.setProductRelease("""\
Version 9 of the multi-link PPP component of the JUNOSe SNMP agent.
        This version of the PPP component was supported in JUNOSe 7.3 and 
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV9.setStatus(
        "obsolete"
    )

juniPppMultiLinkAgentV10 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 32, 3, 10)
)
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV10.setProductRelease("""\
Version 10 of the multi-link PPP component of the JUNOSe SNMP agent.
        This version of the PPP component was supported in JUNOSe 11.1 and 
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPppMultiLinkAgentV10.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-PPP-CONF",
    **{"juniPppAgent": juniPppAgent,
       "juniPppAgentV1": juniPppAgentV1,
       "juniPppGeneralAgent": juniPppGeneralAgent,
       "juniPppGeneralAgentV1": juniPppGeneralAgentV1,
       "juniPppGeneralAgentV2": juniPppGeneralAgentV2,
       "juniPppGeneralAgentV3": juniPppGeneralAgentV3,
       "juniPppGeneralAgentV4": juniPppGeneralAgentV4,
       "juniPppGeneralAgentV5": juniPppGeneralAgentV5,
       "juniPppGeneralAgentV6": juniPppGeneralAgentV6,
       "juniPppGeneralAgentV7": juniPppGeneralAgentV7,
       "juniPppGeneralAgentV8": juniPppGeneralAgentV8,
       "juniPppGeneralAgentV9": juniPppGeneralAgentV9,
       "juniPppMultiLinkAgent": juniPppMultiLinkAgent,
       "juniPppMultiLinkAgentV1": juniPppMultiLinkAgentV1,
       "juniPppMultiLinkAgentV2": juniPppMultiLinkAgentV2,
       "juniPppMultiLinkAgentV3": juniPppMultiLinkAgentV3,
       "juniPppMultiLinkAgentV4": juniPppMultiLinkAgentV4,
       "juniPppMultiLinkAgentV5": juniPppMultiLinkAgentV5,
       "juniPppMultiLinkAgentV6": juniPppMultiLinkAgentV6,
       "juniPppMultiLinkAgentV7": juniPppMultiLinkAgentV7,
       "juniPppMultiLinkAgentV8": juniPppMultiLinkAgentV8,
       "juniPppMultiLinkAgentV9": juniPppMultiLinkAgentV9,
       "juniPppMultiLinkAgentV10": juniPppMultiLinkAgentV10}
)
