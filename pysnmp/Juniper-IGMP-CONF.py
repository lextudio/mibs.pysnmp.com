# SNMP MIB module (Juniper-IGMP-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-IGMP-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:25 2024
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

juniIgmpAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 19)
)
juniIgmpAgent.setRevisions(
        ("2006-08-25 05:40",
         "2003-09-29 18:22",
         "2002-10-28 15:06",
         "2002-08-29 20:48",
         "2001-03-28 17:20")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniIgmpAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 1)
)
if mibBuilder.loadTexts:
    juniIgmpAgentV1.setProductRelease("""\
Version 1 of the IGMP component of the JUNOSe SNMP agent.  This version
        of the IGMP component was supported in JUNOSe 3.0 thru 4.0 system
        releases.""")
if mibBuilder.loadTexts:
    juniIgmpAgentV1.setStatus(
        "obsolete"
    )

juniIgmpAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 2)
)
if mibBuilder.loadTexts:
    juniIgmpAgentV2.setProductRelease("""\
Version 2 of the IGMP component of the JUNOSe SNMP agent.  This version
        of the IGMP component was supported in JUNOSe 4.1 and subsequent 4.x
        system releases.""")
if mibBuilder.loadTexts:
    juniIgmpAgentV2.setStatus(
        "obsolete"
    )

juniIgmpAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 3)
)
if mibBuilder.loadTexts:
    juniIgmpAgentV3.setProductRelease("""\
Version 3 of the IGMP component of the JUNOSe SNMP agent.  This version
        of the IGMP component was supported in JUNOSe 5.0 system releases.""")
if mibBuilder.loadTexts:
    juniIgmpAgentV3.setStatus(
        "obsolete"
    )

juniIgmpAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 4)
)
if mibBuilder.loadTexts:
    juniIgmpAgentV4.setProductRelease("""\
Version 4 of the IGMP component of the JUNOSe SNMP agent.  This version
        of the IGMP component is supported in JUNOSe 5.1 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniIgmpAgentV4.setStatus(
        "deprecated"
    )

juniIgmpAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 5)
)
if mibBuilder.loadTexts:
    juniIgmpAgentV5.setProductRelease("""\
Version 5 of the IGMP component of the JUNOSe SNMP agent.  This version
        of the IGMP component is supported in JUNOSe 7.0 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniIgmpAgentV5.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-IGMP-CONF",
    **{"juniIgmpAgent": juniIgmpAgent,
       "juniIgmpAgentV1": juniIgmpAgentV1,
       "juniIgmpAgentV2": juniIgmpAgentV2,
       "juniIgmpAgentV3": juniIgmpAgentV3,
       "juniIgmpAgentV4": juniIgmpAgentV4,
       "juniIgmpAgentV5": juniIgmpAgentV5}
)
