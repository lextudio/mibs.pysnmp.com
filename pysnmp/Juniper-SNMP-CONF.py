# SNMP MIB module (Juniper-SNMP-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-SNMP-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:20 2024
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

juniSnmpAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39)
)
juniSnmpAgent.setRevisions(
        ("2003-03-10 20:27",
         "2002-09-06 16:54",
         "2002-08-20 13:29",
         "2002-08-14 19:23",
         "2001-10-16 13:44",
         "2001-04-13 15:44")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniSnmpAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 1)
)
if mibBuilder.loadTexts:
    juniSnmpAgentV1.setProductRelease("""\
Version 1 of the SNMP entity component of the JUNOSe SNMP agent.  This
        version of the SNMP entity component was supported in JUNOSe 1.x system
        releases.""")
if mibBuilder.loadTexts:
    juniSnmpAgentV1.setStatus(
        "obsolete"
    )

juniSnmpAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 2)
)
if mibBuilder.loadTexts:
    juniSnmpAgentV2.setProductRelease("""\
Version 2 of the SNMP entity component of the JUNOSe SNMP agent.  This
        version of the SNMP entity component was supported in JUNOSe 2.0 thru
        2.2 system releases.""")
if mibBuilder.loadTexts:
    juniSnmpAgentV2.setStatus(
        "obsolete"
    )

juniSnmpAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 3)
)
if mibBuilder.loadTexts:
    juniSnmpAgentV3.setProductRelease("""\
Version 3 of the SNMP entity component of the JUNOSe SNMP agent.  This
        version of the SNMP entity component was supported in JUNOSe 2.3 thru
        3.1 system releases.""")
if mibBuilder.loadTexts:
    juniSnmpAgentV3.setStatus(
        "obsolete"
    )

juniSnmpAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 4)
)
if mibBuilder.loadTexts:
    juniSnmpAgentV4.setProductRelease("""\
Version 4 of the SNMP entity component of the JUNOSe SNMP agent.  This
        version of the SNMP entity component was supported in JUNOSe 3.2 system
        releases.""")
if mibBuilder.loadTexts:
    juniSnmpAgentV4.setStatus(
        "obsolete"
    )

juniSnmpAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 5)
)
if mibBuilder.loadTexts:
    juniSnmpAgentV5.setProductRelease("""\
Version 5 of the SNMP entity component of the JUNOSe SNMP agent.  This
        version of the SNMP entity component was supported in JUNOSe 3.3 system
        releases.""")
if mibBuilder.loadTexts:
    juniSnmpAgentV5.setStatus(
        "obsolete"
    )

juniSnmpAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 6)
)
if mibBuilder.loadTexts:
    juniSnmpAgentV6.setProductRelease("""\
Version 6 of the SNMP entity component of the JUNOSe SNMP agent.  This
        version of the SNMP entity component was supported in JUNOSe 3.4 thru
        4.0 system releases.""")
if mibBuilder.loadTexts:
    juniSnmpAgentV6.setStatus(
        "obsolete"
    )

juniSnmpAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 7)
)
if mibBuilder.loadTexts:
    juniSnmpAgentV7.setProductRelease("""\
Version 7 of the SNMP entity component of the JUNOSe SNMP
        agent.  This version of the SNMP entity component is supported in the
        JUNOSe 4.1 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniSnmpAgentV7.setStatus(
        "obsolete"
    )

juniSnmpAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 8)
)
if mibBuilder.loadTexts:
    juniSnmpAgentV8.setProductRelease("""\
Version 8 of the SNMP entity component of the JUNOSe SNMP agent.  This
        version of the SNMP entity component is supported in JUNOSe 5.1 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniSnmpAgentV8.setStatus(
        "obsolete"
    )

juniSnmpAgentV9 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 9)
)
if mibBuilder.loadTexts:
    juniSnmpAgentV9.setProductRelease("""\
Version 9 of the SNMP entity component of the JUNOSe SNMP agent.  This
        version of the SNMP entity component is supported in JUNOSe 9.3 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniSnmpAgentV9.setStatus(
        "obsolete"
    )

juniSnmpAgentV10 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 39, 10)
)
if mibBuilder.loadTexts:
    juniSnmpAgentV10.setProductRelease("""\
Version 10 of the SNMP entity component of the JUNOSe SNMP agent.  This
        version of the SNMP entity component is supported in JUNOSe 10.2 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniSnmpAgentV10.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-SNMP-CONF",
    **{"juniSnmpAgent": juniSnmpAgent,
       "juniSnmpAgentV1": juniSnmpAgentV1,
       "juniSnmpAgentV2": juniSnmpAgentV2,
       "juniSnmpAgentV3": juniSnmpAgentV3,
       "juniSnmpAgentV4": juniSnmpAgentV4,
       "juniSnmpAgentV5": juniSnmpAgentV5,
       "juniSnmpAgentV6": juniSnmpAgentV6,
       "juniSnmpAgentV7": juniSnmpAgentV7,
       "juniSnmpAgentV8": juniSnmpAgentV8,
       "juniSnmpAgentV9": juniSnmpAgentV9,
       "juniSnmpAgentV10": juniSnmpAgentV10}
)
