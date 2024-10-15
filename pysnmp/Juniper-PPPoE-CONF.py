# SNMP MIB module (Juniper-PPPoE-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-PPPoE-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:01 2024
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

juniPppoeAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 33)
)
juniPppoeAgent.setRevisions(
        ("2008-11-27 10:23",
         "2005-08-03 20:58",
         "2005-07-13 11:40",
         "2004-06-14 20:48",
         "2003-03-10 18:48",
         "2002-12-23 19:41",
         "2002-10-01 18:37",
         "2002-08-19 15:14",
         "2001-06-19 14:27",
         "2001-04-02 19:21")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniPppoeAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 1)
)
if mibBuilder.loadTexts:
    juniPppoeAgentV1.setProductRelease("""\
Version 1 of the PPPoE component of the JUNOSe SNMP agent.  This
        version of the PPPoE component was supported in JUNOSe 3.0 thru 3.2.2
        system releases.""")
if mibBuilder.loadTexts:
    juniPppoeAgentV1.setStatus(
        "obsolete"
    )

juniPppoeAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 2)
)
if mibBuilder.loadTexts:
    juniPppoeAgentV2.setProductRelease("""\
Version 2 of the PPPoE component of the JUNOSe SNMP agent.  This
        version of the PPPoE component was supported in JUNOSe 3.2.3 through 3.x
        system releases.""")
if mibBuilder.loadTexts:
    juniPppoeAgentV2.setStatus(
        "obsolete"
    )

juniPppoeAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 3)
)
if mibBuilder.loadTexts:
    juniPppoeAgentV3.setProductRelease("""\
Version 3 of the PPPoE component of the JUNOSe SNMP agent.  This
        version of the PPPoE component was supported in JUNOSe 4.0 system
        releases.""")
if mibBuilder.loadTexts:
    juniPppoeAgentV3.setStatus(
        "obsolete"
    )

juniPppoeAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 4)
)
if mibBuilder.loadTexts:
    juniPppoeAgentV4.setProductRelease("""\
Version 4 of the PPPoE component of the JUNOSe SNMP agent.  This
        version of the PPPoE component was supported in JUNOSe 4.1 through 5.0
        system releases.""")
if mibBuilder.loadTexts:
    juniPppoeAgentV4.setStatus(
        "obsolete"
    )

juniPppoeAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 5)
)
if mibBuilder.loadTexts:
    juniPppoeAgentV5.setProductRelease("""\
Version 5 of the PPPoE component of the JUNOSe SNMP agent.  This
        version of the PPPoE component was supported in JUNOSe 5.1 through 7.0
        system releases.""")
if mibBuilder.loadTexts:
    juniPppoeAgentV5.setStatus(
        "obsolete"
    )

juniPppoeAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 6)
)
if mibBuilder.loadTexts:
    juniPppoeAgentV6.setProductRelease("""\
Version 6 of the PPPoE component of the JUNOSe SNMP agent.  This
        version of the PPPoE component is supported in JUNOSe 7.0 system
        release.""")
if mibBuilder.loadTexts:
    juniPppoeAgentV6.setStatus(
        "obsolete"
    )

juniPppoeAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 7)
)
if mibBuilder.loadTexts:
    juniPppoeAgentV7.setProductRelease("""\
Version 7 of the PPPoE component of the JUNOSe SNMP agent.  This
        version of the PPPoE component is supported in JUNOSe 7.0.1 through 7.1
        system releases.""")
if mibBuilder.loadTexts:
    juniPppoeAgentV7.setStatus(
        "obsolete"
    )

juniPppoeAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 8)
)
if mibBuilder.loadTexts:
    juniPppoeAgentV8.setProductRelease("""\
Version 8 of the PPPoE component of the JUNOSe SNMP agent.  This
        version of the PPPoE component is supported in JUNOSe 7.2 through 9.3 
        system releases.""")
if mibBuilder.loadTexts:
    juniPppoeAgentV8.setStatus(
        "obsolete"
    )

juniPppoeAgentV9 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 33, 9)
)
if mibBuilder.loadTexts:
    juniPppoeAgentV9.setProductRelease("""\
Version 9 of the PPPoE component of the JUNOSe SNMP agent.  This
        version of the PPPoE component is supported in JUNOSe 10.1 and subsequent
        system releases.""")
if mibBuilder.loadTexts:
    juniPppoeAgentV9.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-PPPoE-CONF",
    **{"juniPppoeAgent": juniPppoeAgent,
       "juniPppoeAgentV1": juniPppoeAgentV1,
       "juniPppoeAgentV2": juniPppoeAgentV2,
       "juniPppoeAgentV3": juniPppoeAgentV3,
       "juniPppoeAgentV4": juniPppoeAgentV4,
       "juniPppoeAgentV5": juniPppoeAgentV5,
       "juniPppoeAgentV6": juniPppoeAgentV6,
       "juniPppoeAgentV7": juniPppoeAgentV7,
       "juniPppoeAgentV8": juniPppoeAgentV8,
       "juniPppoeAgentV9": juniPppoeAgentV9}
)
