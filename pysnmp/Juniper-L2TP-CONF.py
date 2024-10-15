# SNMP MIB module (Juniper-L2TP-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-L2TP-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:40 2024
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

juniL2tpAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24)
)
juniL2tpAgent.setRevisions(
        ("2005-09-16 15:58",
         "2005-07-28 22:00",
         "2005-02-17 02:24",
         "2004-09-02 23:47",
         "2004-05-04 14:31",
         "2004-03-08 18:04",
         "2004-03-08 18:04",
         "2003-02-13 21:12",
         "2003-02-12 21:03",
         "2003-02-07 22:26",
         "2001-10-17 16:03",
         "2001-10-17 14:21")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniL2tpAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 1)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV1.setProductRelease("""\
Version 1 of the L2TP component of the JUNOSe SNMP agent.  This version
        of the L2TP component was supported in JUNOSe 2.x system releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV1.setStatus(
        "obsolete"
    )

juniL2tpAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 2)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV2.setProductRelease("""\
Version 2 of the L2TP component of the JUNOSe SNMP agent.  This version
        of the L2TP component was supported in JUNOSe 3.0 and 3.1 system
        releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV2.setStatus(
        "obsolete"
    )

juniL2tpAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 3)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV3.setProductRelease("""\
Version 3 of the L2TP component of the JUNOSe SNMP agent.  This version
        of the L2TP component was supported in JUNOSe 3.2 system releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV3.setStatus(
        "obsolete"
    )

juniL2tpAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 4)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV4.setProductRelease("""\
Version 4 of the L2TP component of the JUNOSe SNMP agent.  This version
        of the L2TP component was supported in JUNOSe 3.3 system releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV4.setStatus(
        "obsolete"
    )

juniL2tpAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 5)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV5.setProductRelease("""\
Version 5 of the L2TP component of the JUNOSe SNMP agent.  This version
        of the L2TP component was supported in JUNOSe 3.4 thru 4.0 system
        releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV5.setStatus(
        "obsolete"
    )

juniL2tpAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 6)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV6.setProductRelease("""\
Version 6 of the L2TP component of the JUNOSe SNMP agent.  This version
        of the L2TP component was supported in JUNOSe 4.1 and subsequent 4.x
        system releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV6.setStatus(
        "obsolete"
    )

juniL2tpAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 7)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV7.setProductRelease("""\
Version 7 of the L2TP component of the JUNOSe SNMP agent.  This version
        of the L2TP component was supported in JUNOSe 5.0 system releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV7.setStatus(
        "obsolete"
    )

juniL2tpAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 8)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV8.setProductRelease("""\
Version 8 of the L2TP component of the JUNOSe SNMP agent.  This version
        of the L2TP component was supported in JUNOSe 5.1 and 5.1 system
        releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV8.setStatus(
        "obsolete"
    )

juniL2tpAgentV9 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 9)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV9.setProductRelease("""\
Version 9 of the L2TP component of the JUNOSe SNMP agent.  This version
        of the L2TP component is supported in JUNOSe 5.3 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV9.setStatus(
        "obsolete"
    )

juniL2tpAgentV10 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 10)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV10.setProductRelease("""\
Version 10 of the L2TP component of the JUNOSe SNMP agent.  This version
        of the L2TP component is supported in JUNOSe 6.0 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV10.setStatus(
        "obsolete"
    )

juniL2tpAgentV11 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 11)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV11.setProductRelease("""\
Version 11 of the L2TP component of the JUNOSe SNMP agent.  This version
        of the L2TP component is supported in JUNOSe 7.0 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV11.setStatus(
        "obsolete"
    )

juniL2tpAgentV12 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 12)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV12.setProductRelease("""\
Version 12 of the L2TP component of the JUNOSe SNMP agent.  This
        version of the L2TP component is supported in JUNOSe 7.1 and subsequent
        system releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV12.setStatus(
        "obsolete"
    )

juniL2tpAgentV13 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 13)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV13.setProductRelease("""\
Version 13 of the L2TP component of the JUNOSe SNMP agent.  This
        version of the L2TP component is supported in JUNOSe Kyoto and subsequent
        system releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV13.setStatus(
        "current"
    )

juniL2tpAgentV14 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 14)
)
if mibBuilder.loadTexts:
    juniL2tpAgentV14.setProductRelease("""\
Version 14 of the L2TP component of the JUNOSe SNMP agent.  This
        version of the L2TP component is supported in JUNOSe 8.0 and subsequent
        system releases.""")
if mibBuilder.loadTexts:
    juniL2tpAgentV14.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-L2TP-CONF",
    **{"juniL2tpAgent": juniL2tpAgent,
       "juniL2tpAgentV1": juniL2tpAgentV1,
       "juniL2tpAgentV2": juniL2tpAgentV2,
       "juniL2tpAgentV3": juniL2tpAgentV3,
       "juniL2tpAgentV4": juniL2tpAgentV4,
       "juniL2tpAgentV5": juniL2tpAgentV5,
       "juniL2tpAgentV6": juniL2tpAgentV6,
       "juniL2tpAgentV7": juniL2tpAgentV7,
       "juniL2tpAgentV8": juniL2tpAgentV8,
       "juniL2tpAgentV9": juniL2tpAgentV9,
       "juniL2tpAgentV10": juniL2tpAgentV10,
       "juniL2tpAgentV11": juniL2tpAgentV11,
       "juniL2tpAgentV12": juniL2tpAgentV12,
       "juniL2tpAgentV13": juniL2tpAgentV13,
       "juniL2tpAgentV14": juniL2tpAgentV14}
)
