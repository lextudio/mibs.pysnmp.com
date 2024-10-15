# SNMP MIB module (Juniper-DS1-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-DS1-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:02 2024
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

juniDs1Agent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10)
)
juniDs1Agent.setRevisions(
        ("2003-09-25 15:23",
         "2003-01-31 17:15",
         "2003-01-31 16:37",
         "2002-05-13 16:34",
         "2001-03-29 20:36")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniDs1AgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 1)
)
if mibBuilder.loadTexts:
    juniDs1AgentV1.setProductRelease("""\
Version 1 of the DS1 component of the JUNOSe SNMP agent.  This version
        of the DS1 component was supported in JUNOSe 1.0 system releases.""")
if mibBuilder.loadTexts:
    juniDs1AgentV1.setStatus(
        "obsolete"
    )

juniDs1AgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 2)
)
if mibBuilder.loadTexts:
    juniDs1AgentV2.setProductRelease("""\
Version 2 of the DS1 component of the JUNOSe SNMP agent.  This version
        of the DS1 component was supported in JUNOSe 1.1 thru JUNOSe 2.x system
        releases.""")
if mibBuilder.loadTexts:
    juniDs1AgentV2.setStatus(
        "obsolete"
    )

juniDs1AgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 3)
)
if mibBuilder.loadTexts:
    juniDs1AgentV3.setProductRelease("""\
Version 3 of the DS1 component of the JUNOSe SNMP agent.  This version
        of the DS1 component was supported in JUNOSe 3.x system releases.""")
if mibBuilder.loadTexts:
    juniDs1AgentV3.setStatus(
        "obsolete"
    )

juniDs1AgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 4)
)
if mibBuilder.loadTexts:
    juniDs1AgentV4.setProductRelease("""\
Version 4 of the DS1 component of the JUNOSe SNMP agent.  This version
        of the DS1 component was supported in JUNOSe 4.0 system releases.""")
if mibBuilder.loadTexts:
    juniDs1AgentV4.setStatus(
        "obsolete"
    )

juniDs1AgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 5)
)
if mibBuilder.loadTexts:
    juniDs1AgentV5.setProductRelease("""\
Version 5 of the DS1 component of the JUNOSe SNMP agent.  This version
        of the DS1 component is supported in JUNOSe 4.1 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniDs1AgentV5.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-DS1-CONF",
    **{"juniDs1Agent": juniDs1Agent,
       "juniDs1AgentV1": juniDs1AgentV1,
       "juniDs1AgentV2": juniDs1AgentV2,
       "juniDs1AgentV3": juniDs1AgentV3,
       "juniDs1AgentV4": juniDs1AgentV4,
       "juniDs1AgentV5": juniDs1AgentV5}
)
