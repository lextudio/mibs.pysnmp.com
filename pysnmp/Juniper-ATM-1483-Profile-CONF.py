# SNMP MIB module (Juniper-ATM-1483-Profile-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-ATM-1483-Profile-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:39 2024
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

(juniProfileAgents,) = mibBuilder.importSymbols(
    "Juniper-Agents",
    "juniProfileAgents")

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

juniAtm1483ProfileAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6)
)
juniAtm1483ProfileAgent.setRevisions(
        ("2004-07-26 19:54",
         "2004-11-02 21:07",
         "2004-11-02 21:07")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniAtm1483ProfileAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6, 1)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileAgentV1.setProductRelease("""\
Version 1 of the ATM 1483 Profile component of the JUNOSe SNMP agent.
        This version of the ATM 1483 Profile component was supported in Juniper
        JUNOSe 5.1 and 5.2 system releases.""")
if mibBuilder.loadTexts:
    juniAtm1483ProfileAgentV1.setStatus(
        "obsolete"
    )

juniAtm1483ProfileAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6, 2)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileAgentV2.setProductRelease("""\
Version 2 of the ATM 1483 Profile component of the JUNOSe SNMP agent.
        This version of the ATM 1483 Profile component was supported in Juniper
        JUNOSe 5.3 system releases.""")
if mibBuilder.loadTexts:
    juniAtm1483ProfileAgentV2.setStatus(
        "obsolete"
    )

juniAtm1483ProfileAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6, 3)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileAgentV3.setProductRelease("""\
Version 3 of the ATM 1483 Profile component of the JUNOSe SNMP agent.
        This version of the ATM 1483 Profile component was supported in Juniper
        JUNOSe 5.1 and 5.2 system releases.""")
if mibBuilder.loadTexts:
    juniAtm1483ProfileAgentV3.setStatus(
        "obsolete"
    )

juniAtm1483ProfileAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6, 4)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileAgentV4.setProductRelease("""\
Version 4 of the ATM 1483 Profile component of the JUNOSe SNMP agent.
        This version of the ATM 1483 Profile component was supported in Juniper
        JUNOSe 5.3, 6.0, and 6.1 system releases.""")
if mibBuilder.loadTexts:
    juniAtm1483ProfileAgentV4.setStatus(
        "current"
    )

juniAtm1483ProfileAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 6, 5)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileAgentV5.setProductRelease("""\
Version 5 of the ATM 1483 Profile component of the JUNOSe SNMP agent.
        This version of the ATM 1483 Profile component is supported in Juniper
        JUNOSe 7.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAtm1483ProfileAgentV5.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-ATM-1483-Profile-CONF",
    **{"juniAtm1483ProfileAgent": juniAtm1483ProfileAgent,
       "juniAtm1483ProfileAgentV1": juniAtm1483ProfileAgentV1,
       "juniAtm1483ProfileAgentV2": juniAtm1483ProfileAgentV2,
       "juniAtm1483ProfileAgentV3": juniAtm1483ProfileAgentV3,
       "juniAtm1483ProfileAgentV4": juniAtm1483ProfileAgentV4,
       "juniAtm1483ProfileAgentV5": juniAtm1483ProfileAgentV5}
)
