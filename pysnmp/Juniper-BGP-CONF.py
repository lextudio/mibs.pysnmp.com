# SNMP MIB module (Juniper-BGP-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-BGP-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:44 2024
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

juniBgpAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4)
)
juniBgpAgent.setRevisions(
        ("2007-05-11 05:17",
         "2003-12-18 15:28",
         "2003-12-18 14:27",
         "2003-07-09 21:35",
         "2002-11-06 16:33",
         "2002-09-05 12:56",
         "2002-09-04 17:56",
         "2002-03-01 17:51",
         "2002-01-23 13:16",
         "2001-12-04 16:09",
         "2001-12-03 18:48")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniBgpAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 1)
)
if mibBuilder.loadTexts:
    juniBgpAgentV1.setProductRelease("""\
Version 1 of the BGP component of the JUNOSe SNMP agent.  This version
        of the BGP component was supported in JUNOSe 3.0 and 3.1 system
        releases.""")
if mibBuilder.loadTexts:
    juniBgpAgentV1.setStatus(
        "obsolete"
    )

juniBgpAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 2)
)
if mibBuilder.loadTexts:
    juniBgpAgentV2.setProductRelease("""\
Version 2 of the BGP component of the JUNOSe SNMP agent.  This version
        of the BGP component was supported in JUNOSe 3.2 system releases.""")
if mibBuilder.loadTexts:
    juniBgpAgentV2.setStatus(
        "obsolete"
    )

juniBgpAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 3)
)
if mibBuilder.loadTexts:
    juniBgpAgentV3.setProductRelease("""\
Version 3 of the BGP component of the JUNOSe SNMP agent.  This version
        of the BGP component was supported in JUNOSe 3.3 system release.""")
if mibBuilder.loadTexts:
    juniBgpAgentV3.setStatus(
        "obsolete"
    )

juniBgpAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 4)
)
if mibBuilder.loadTexts:
    juniBgpAgentV4.setProductRelease("""\
Version 4 of the BGP component of the JUNOSe SNMP agent.  This version
        of the BGP component was supported in JUNOSe 3.4 system releases.""")
if mibBuilder.loadTexts:
    juniBgpAgentV4.setStatus(
        "obsolete"
    )

juniBgpAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 5)
)
if mibBuilder.loadTexts:
    juniBgpAgentV5.setProductRelease("""\
Version 5 of the BGP component of the JUNOSe SNMP agent.  This version
        of the BGP component was supported in JUNOSe 3.5 and subseguent 3.x
        system releases.""")
if mibBuilder.loadTexts:
    juniBgpAgentV5.setStatus(
        "obsolete"
    )

juniBgpAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 6)
)
if mibBuilder.loadTexts:
    juniBgpAgentV6.setProductRelease("""\
Version 6 of the BGP component of the JUNOSe SNMP agent.  This version
        of the BGP component was supported in JUNOSe 4.0 system releases.""")
if mibBuilder.loadTexts:
    juniBgpAgentV6.setStatus(
        "obsolete"
    )

juniBgpAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 7)
)
if mibBuilder.loadTexts:
    juniBgpAgentV7.setProductRelease("""\
Version 7 of the BGP component of the JUNOSe SNMP agent.  This version
        of the BGP component was supported in JUNOSe 4.1 system releases.""")
if mibBuilder.loadTexts:
    juniBgpAgentV7.setStatus(
        "obsolete"
    )

juniBgpAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 8)
)
if mibBuilder.loadTexts:
    juniBgpAgentV8.setProductRelease("""\
Version 8 of the BGP component of the JUNOSe SNMP agent.  This version
        of the BGP component was supported in JUNOSe 5.0 system releases.""")
if mibBuilder.loadTexts:
    juniBgpAgentV8.setStatus(
        "obsolete"
    )

juniBgpAgentV9 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 9)
)
if mibBuilder.loadTexts:
    juniBgpAgentV9.setProductRelease("""\
Version 9 of the BGP component of the JUNOSe SNMP agent.  This version
        of the BGP component was supported in JUNOSe 5.1 system releases.""")
if mibBuilder.loadTexts:
    juniBgpAgentV9.setStatus(
        "obsolete"
    )

juniBgpAgentV10 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 10)
)
if mibBuilder.loadTexts:
    juniBgpAgentV10.setProductRelease("""\
Version 10 of the BGP component of the JUNOSe SNMP agent.  This version
        of the BGP component was supported in JUNOSe 5.2 system releases.""")
if mibBuilder.loadTexts:
    juniBgpAgentV10.setStatus(
        "obsolete"
    )

juniBgpAgentV11 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 11)
)
if mibBuilder.loadTexts:
    juniBgpAgentV11.setProductRelease("""\
Version 11 of the BGP component of the JUNOSe SNMP agent.  This version
        of the BGP component is supported in JUNOSe 5.3 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniBgpAgentV11.setStatus(
        "obsolete"
    )

juniBgpAgentV12 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 4, 12)
)
if mibBuilder.loadTexts:
    juniBgpAgentV12.setProductRelease("""\
Version 12 of the BGP component of the JUNOSe SNMP agent.  This version
        of the BGP component is supported in JUNOSe 9.0 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniBgpAgentV12.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-BGP-CONF",
    **{"juniBgpAgent": juniBgpAgent,
       "juniBgpAgentV1": juniBgpAgentV1,
       "juniBgpAgentV2": juniBgpAgentV2,
       "juniBgpAgentV3": juniBgpAgentV3,
       "juniBgpAgentV4": juniBgpAgentV4,
       "juniBgpAgentV5": juniBgpAgentV5,
       "juniBgpAgentV6": juniBgpAgentV6,
       "juniBgpAgentV7": juniBgpAgentV7,
       "juniBgpAgentV8": juniBgpAgentV8,
       "juniBgpAgentV9": juniBgpAgentV9,
       "juniBgpAgentV10": juniBgpAgentV10,
       "juniBgpAgentV11": juniBgpAgentV11,
       "juniBgpAgentV12": juniBgpAgentV12}
)
