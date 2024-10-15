# SNMP MIB module (Juniper-System-Clock-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-System-Clock-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:24 2024
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

juniSysClockAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 52)
)
juniSysClockAgent.setRevisions(
        ("2005-12-14 14:01",
         "2003-09-15 14:03",
         "2003-09-12 14:39",
         "2002-04-04 18:47")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniSysClockAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 1)
)
if mibBuilder.loadTexts:
    juniSysClockAgentV1.setProductRelease("""\
Version 1 of the system clock component of the JUNOSe SNMP agent.  This
        version of the system clock component was supported in JUNOSe 4.0 system
        releases.""")
if mibBuilder.loadTexts:
    juniSysClockAgentV1.setStatus(
        "obsolete"
    )

juniSysClockAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 2)
)
if mibBuilder.loadTexts:
    juniSysClockAgentV2.setProductRelease("""\
Version 2 of the system clock component of the JUNOSe SNMP agent.  This
        version of the system clock component was supported in early JUNOSe 4.1
        and 5.0 system releases.""")
if mibBuilder.loadTexts:
    juniSysClockAgentV2.setStatus(
        "obsolete"
    )

juniSysClockAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 3)
)
if mibBuilder.loadTexts:
    juniSysClockAgentV3.setProductRelease("""\
Version 3 of the system clock component of the JUNOSe SNMP agent.  This
        version of the system clock component is supported in JUNOSe 4.1.2,
        5.0.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniSysClockAgentV3.setStatus(
        "obsolete"
    )

juniSysClockAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 4)
)
if mibBuilder.loadTexts:
    juniSysClockAgentV4.setProductRelease("""\
Version 4 of the system clock component of the JUNOSe SNMP agent.  This
        version of the system clock component is supported in JUNOSe 7.0 and 
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniSysClockAgentV4.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-System-Clock-CONF",
    **{"juniSysClockAgent": juniSysClockAgent,
       "juniSysClockAgentV1": juniSysClockAgentV1,
       "juniSysClockAgentV2": juniSysClockAgentV2,
       "juniSysClockAgentV3": juniSysClockAgentV3,
       "juniSysClockAgentV4": juniSysClockAgentV4}
)
