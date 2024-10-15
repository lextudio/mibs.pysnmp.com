# SNMP MIB module (Juniper-PPPoE-Profile-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-PPPoE-Profile-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:02 2024
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

juniPppoeProfileAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4)
)
juniPppoeProfileAgent.setRevisions(
        ("2005-07-13 11:40",
         "2004-06-14 20:48",
         "2003-03-13 18:01",
         "2002-09-06 16:54",
         "2002-08-15 20:38",
         "2002-05-31 18:21")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniPppoeProfileAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 1)
)
if mibBuilder.loadTexts:
    juniPppoeProfileAgentV1.setProductRelease("""\
Version 1 of the PPPoE Profile component of the JUNOSe SNMP agent.
        This version of the PPPoE Profile component was supported in JUNOSe 3.0
        and 3.1 system releases.""")
if mibBuilder.loadTexts:
    juniPppoeProfileAgentV1.setStatus(
        "obsolete"
    )

juniPppoeProfileAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 2)
)
if mibBuilder.loadTexts:
    juniPppoeProfileAgentV2.setProductRelease("""\
Version 2 of the PPPoE Profile component of the JUNOSe SNMP agent.
        This version of the PPPoE Profile component was supported in JUNOSe 3.2
        and subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    juniPppoeProfileAgentV2.setStatus(
        "obsolete"
    )

juniPppoeProfileAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 3)
)
if mibBuilder.loadTexts:
    juniPppoeProfileAgentV3.setProductRelease("""\
Version 3 of the PPPoE Profile component of the JUNOSe SNMP agent.
        This version of the PPPoE Profile component was supported in JUNOSe 4.0
        thru 5.0 system releases.""")
if mibBuilder.loadTexts:
    juniPppoeProfileAgentV3.setStatus(
        "obsolete"
    )

juniPppoeProfileAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 4)
)
if mibBuilder.loadTexts:
    juniPppoeProfileAgentV4.setProductRelease("""\
Version 4 of the PPPoE component of the JUNOSe SNMP agent.  This
        version of the PPPoE component was supported in JUNOSe 5.1 through 7.0
        system releases.""")
if mibBuilder.loadTexts:
    juniPppoeProfileAgentV4.setStatus(
        "obsolete"
    )

juniPppoeProfileAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 5)
)
if mibBuilder.loadTexts:
    juniPppoeProfileAgentV5.setProductRelease("""\
Version 5 of the PPPoE Profile component of the JUNOSe SNMP agent.
        This version of the PPPoE Profile component is supported in JUNOSe 7.0
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPppoeProfileAgentV5.setStatus(
        "obsolete"
    )

juniPppoeProfileAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 4, 6)
)
if mibBuilder.loadTexts:
    juniPppoeProfileAgentV6.setProductRelease("""\
Version 6 of the PPPoE Profile component of the JUNOSe SNMP agent.
        This version of the PPPoE Profile component is supported in JUNOSe 7.0.1
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniPppoeProfileAgentV6.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-PPPoE-Profile-CONF",
    **{"juniPppoeProfileAgent": juniPppoeProfileAgent,
       "juniPppoeProfileAgentV1": juniPppoeProfileAgentV1,
       "juniPppoeProfileAgentV2": juniPppoeProfileAgentV2,
       "juniPppoeProfileAgentV3": juniPppoeProfileAgentV3,
       "juniPppoeProfileAgentV4": juniPppoeProfileAgentV4,
       "juniPppoeProfileAgentV5": juniPppoeProfileAgentV5,
       "juniPppoeProfileAgentV6": juniPppoeProfileAgentV6}
)
