# SNMP MIB module (Juniper-ERX-System-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-ERX-System-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:10 2024
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

(juniSystemAgents,) = mibBuilder.importSymbols(
    "Juniper-Agents",
    "juniSystemAgents")

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

juniErxSystemAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1)
)
juniErxSystemAgent.setRevisions(
        ("2003-11-24 19:53",
         "2003-01-28 21:48",
         "2002-08-19 13:17",
         "2002-04-01 22:32",
         "2001-04-13 13:03")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniErxSystemAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 1)
)
if mibBuilder.loadTexts:
    juniErxSystemAgentV1.setProductRelease("""\
Version 1 of the System component of the JUNOSe SNMP agent.  This
        version of the ERX System component was supported in the JUNOSe 1.3
        system release.""")
if mibBuilder.loadTexts:
    juniErxSystemAgentV1.setStatus(
        "obsolete"
    )

juniErxSystemAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 2)
)
if mibBuilder.loadTexts:
    juniErxSystemAgentV2.setProductRelease("""\
Version 2 of the System component of the JUNOSe SNMP agent.  This
        version of the ERX System component was supported in the JUNOSe 2.x
        system releases.""")
if mibBuilder.loadTexts:
    juniErxSystemAgentV2.setStatus(
        "obsolete"
    )

juniErxSystemAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 3)
)
if mibBuilder.loadTexts:
    juniErxSystemAgentV3.setProductRelease("""\
Version 3 of the System component of the JUNOSe SNMP agent.  This
        version of the ERX System component was supported in the JUNOSe 3.0 and
        3.1 system releases.""")
if mibBuilder.loadTexts:
    juniErxSystemAgentV3.setStatus(
        "obsolete"
    )

juniErxSystemAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 4)
)
if mibBuilder.loadTexts:
    juniErxSystemAgentV4.setProductRelease("""\
Version 4 of the System component of the JUNOSe SNMP agent.  This
        version of the ERX System component was supported in the JUNOSe 3.2
        system release.""")
if mibBuilder.loadTexts:
    juniErxSystemAgentV4.setStatus(
        "obsolete"
    )

juniErxSystemAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 5)
)
if mibBuilder.loadTexts:
    juniErxSystemAgentV5.setProductRelease("""\
Version 5 of the System component of the JUNOSe SNMP agent.  This
        version of the ERX System component is supported in the JUNOSe 3.3 thru
        4.0 system releases.""")
if mibBuilder.loadTexts:
    juniErxSystemAgentV5.setStatus(
        "obsolete"
    )

juniErxSystemAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 6)
)
if mibBuilder.loadTexts:
    juniErxSystemAgentV6.setProductRelease("""\
Version 6 of the System component of the JUNOSe SNMP agent.  This
        version of the ERX System component was supported in the JUNOSe 4.1 and
        subsequent 4.x system releases.""")
if mibBuilder.loadTexts:
    juniErxSystemAgentV6.setStatus(
        "obsolete"
    )

juniErxSystemAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 7)
)
if mibBuilder.loadTexts:
    juniErxSystemAgentV7.setProductRelease("""\
Version 7 of the System component of the JUNOSe SNMP agent.  This
        version of the ERX System component was supported in the JUNOSe 5.0 and
        5.1 system releases.""")
if mibBuilder.loadTexts:
    juniErxSystemAgentV7.setStatus(
        "obsolete"
    )

juniErxSystemAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 42, 1, 8)
)
if mibBuilder.loadTexts:
    juniErxSystemAgentV8.setProductRelease("""\
Version 8 of the System component of the JUNOSe SNMP agent.  This
        version of the ERX System component is supported in the JUNOSe 5.2 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniErxSystemAgentV8.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-ERX-System-CONF",
    **{"juniErxSystemAgent": juniErxSystemAgent,
       "juniErxSystemAgentV1": juniErxSystemAgentV1,
       "juniErxSystemAgentV2": juniErxSystemAgentV2,
       "juniErxSystemAgentV3": juniErxSystemAgentV3,
       "juniErxSystemAgentV4": juniErxSystemAgentV4,
       "juniErxSystemAgentV5": juniErxSystemAgentV5,
       "juniErxSystemAgentV6": juniErxSystemAgentV6,
       "juniErxSystemAgentV7": juniErxSystemAgentV7,
       "juniErxSystemAgentV8": juniErxSystemAgentV8}
)
