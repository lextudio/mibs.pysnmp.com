# SNMP MIB module (Juniper-SSC-Client-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-SSC-Client-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:23 2024
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

juniSscClientAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 41)
)
juniSscClientAgent.setRevisions(
        ("2003-11-18 21:11",
         "2002-09-06 16:54",
         "2001-09-19 20:29",
         "2001-03-30 15:18")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniSscClientAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 1)
)
if mibBuilder.loadTexts:
    juniSscClientAgentV1.setProductRelease("""\
Version 1 of the SSC Client component of the JUNOSe SNMP agent.  This
        version of the SSC Client component was supported in JUNOSe 2.0 thru 3.0
        system releases.""")
if mibBuilder.loadTexts:
    juniSscClientAgentV1.setStatus(
        "obsolete"
    )

juniSscClientAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 2)
)
if mibBuilder.loadTexts:
    juniSscClientAgentV2.setProductRelease("""\
Version 2 of the SSC Client component of the JUNOSe SNMP agent.  This
        version of the SSC Client component was supported in JUNOSe 3.1 and
        subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    juniSscClientAgentV2.setStatus(
        "obsolete"
    )

juniSscClientAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 3)
)
if mibBuilder.loadTexts:
    juniSscClientAgentV3.setProductRelease("""\
Version 3 of the SSC Client component of the JUNOSe SNMP agent.  This
        version of the SSC Client component was supported in JUNOSe 4.0 through
        5.2 system releases.""")
if mibBuilder.loadTexts:
    juniSscClientAgentV3.setStatus(
        "obsolete"
    )

juniSscClientAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 4)
)
if mibBuilder.loadTexts:
    juniSscClientAgentV4.setProductRelease("""\
Version 4 of the SSC Client component of the JUNOSe SNMP agent.  This
        version of the SSC Client component is supported in JUNOSe 5.3 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniSscClientAgentV4.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-SSC-Client-CONF",
    **{"juniSscClientAgent": juniSscClientAgent,
       "juniSscClientAgentV1": juniSscClientAgentV1,
       "juniSscClientAgentV2": juniSscClientAgentV2,
       "juniSscClientAgentV3": juniSscClientAgentV3,
       "juniSscClientAgentV4": juniSscClientAgentV4}
)
