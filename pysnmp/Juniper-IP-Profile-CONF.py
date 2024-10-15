# SNMP MIB module (Juniper-IP-Profile-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-IP-Profile-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:32 2024
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

juniIpProfileAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2)
)
juniIpProfileAgent.setRevisions(
        ("2006-09-08 10:26",
         "2005-09-13 17:21",
         "2004-10-05 14:04",
         "2003-09-24 15:33",
         "2002-10-09 14:31",
         "2001-03-28 21:43")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniIpProfileAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 1)
)
if mibBuilder.loadTexts:
    juniIpProfileAgentV1.setProductRelease("""\
Version 1 of the IP Profile component of the JUNOSe SNMP agent.  This
        version of the IP Profile Manager component was supported in JUNOSe 1.x
        system releases.""")
if mibBuilder.loadTexts:
    juniIpProfileAgentV1.setStatus(
        "obsolete"
    )

juniIpProfileAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 2)
)
if mibBuilder.loadTexts:
    juniIpProfileAgentV2.setProductRelease("""\
Version 2 of the IP Profile component of the JUNOSe SNMP agent.  This
        version of the IP Profile Manager component was supported in JUNOSe 2.x
        system releases.""")
if mibBuilder.loadTexts:
    juniIpProfileAgentV2.setStatus(
        "obsolete"
    )

juniIpProfileAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 3)
)
if mibBuilder.loadTexts:
    juniIpProfileAgentV3.setProductRelease("""\
Version 3 of the IP Profile component of the JUNOSe SNMP agent.  This
        version of the IP Profile Manager component was supported in JUNOSe 3.0
        through 4.x system releases.""")
if mibBuilder.loadTexts:
    juniIpProfileAgentV3.setStatus(
        "obsolete"
    )

juniIpProfileAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 4)
)
if mibBuilder.loadTexts:
    juniIpProfileAgentV4.setProductRelease("""\
Version 4 of the IP Profile component of the JUNOSe SNMP agent.  This
        version of the IP Profile Manager component was supported in JUNOSe 5.0
        and 5.1 system releases.""")
if mibBuilder.loadTexts:
    juniIpProfileAgentV4.setStatus(
        "obsolete"
    )

juniIpProfileAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 5)
)
if mibBuilder.loadTexts:
    juniIpProfileAgentV5.setProductRelease("""\
Version 5 of the IP Profile component of the JUNOSe SNMP agent.  This
        version of the IP Profile Manager component was supported in JUNOSe 5.2, 5.3, and 6.x
        Now obsolete after IP filter options all support""")
if mibBuilder.loadTexts:
    juniIpProfileAgentV5.setStatus(
        "obsolete"
    )

juniIpProfileAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 6)
)
if mibBuilder.loadTexts:
    juniIpProfileAgentV6.setProductRelease("""\
Version 6 of the IP Profile component of the JUNOSe SNMP agent.  This
        version of the IP Profile Manager component is supported in JUNOSe 7.0
        and subsequent system releases. """)
if mibBuilder.loadTexts:
    juniIpProfileAgentV6.setStatus(
        "obsolete"
    )

juniIpProfileAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 7)
)
if mibBuilder.loadTexts:
    juniIpProfileAgentV7.setProductRelease("""\
Version 7 of the IP Profile component of the JUNOSe SNMP agent.  This
        version of the IP Profile Manager component is supported in JUNOSe 7.2
        and subsequent system releases. """)
if mibBuilder.loadTexts:
    juniIpProfileAgentV7.setStatus(
        "obsolete"
    )

juniIpProfileAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 34, 2, 8)
)
if mibBuilder.loadTexts:
    juniIpProfileAgentV8.setProductRelease("""\
Version 8 of the IP Profile component of the JUNOSe SNMP agent.  This
        version of the IP Profile Manager component is supported in JUNOSe 8.1
        and subsequent system releases. """)
if mibBuilder.loadTexts:
    juniIpProfileAgentV8.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-IP-Profile-CONF",
    **{"juniIpProfileAgent": juniIpProfileAgent,
       "juniIpProfileAgentV1": juniIpProfileAgentV1,
       "juniIpProfileAgentV2": juniIpProfileAgentV2,
       "juniIpProfileAgentV3": juniIpProfileAgentV3,
       "juniIpProfileAgentV4": juniIpProfileAgentV4,
       "juniIpProfileAgentV5": juniIpProfileAgentV5,
       "juniIpProfileAgentV6": juniIpProfileAgentV6,
       "juniIpProfileAgentV7": juniIpProfileAgentV7,
       "juniIpProfileAgentV8": juniIpProfileAgentV8}
)
