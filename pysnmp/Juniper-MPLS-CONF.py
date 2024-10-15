# SNMP MIB module (Juniper-MPLS-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-MPLS-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:47 2024
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

juniMplsAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 51)
)
juniMplsAgent.setRevisions(
        ("2004-06-11 21:36",
         "2003-01-24 18:34",
         "2002-11-04 15:47",
         "2001-12-05 21:41")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniMplsAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 1)
)
if mibBuilder.loadTexts:
    juniMplsAgentV1.setProductRelease("""\
Version 1 of the MultiProtocol Label Switching (MPLS) component of the
        JUNOSe SNMP agent.  This version of the MPLS component was supported in
        JUNOSe 4.0 system releases.""")
if mibBuilder.loadTexts:
    juniMplsAgentV1.setStatus(
        "obsolete"
    )

juniMplsAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 2)
)
if mibBuilder.loadTexts:
    juniMplsAgentV2.setProductRelease("""\
Version 2 of the MultiProtocol Label Switching (MPLS) component of the
        JUNOSe SNMP agent.  This version of the MPLS component was supported in
        JUNOSe 4.1 and subsequent 4.x system releases.""")
if mibBuilder.loadTexts:
    juniMplsAgentV2.setStatus(
        "obsolete"
    )

juniMplsAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 3)
)
if mibBuilder.loadTexts:
    juniMplsAgentV3.setProductRelease("""\
Version 3 of the MultiProtocol Label Switching (MPLS) component of the
        JUNOSe SNMP agent.  This version of the MPLS component is supported in
        JUNOSe 5.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniMplsAgentV3.setStatus(
        "obsolete"
    )

juniMplsAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 4)
)
if mibBuilder.loadTexts:
    juniMplsAgentV4.setProductRelease("""\
Version 4 of the MultiProtocol Label Switching (MPLS) component of the
        JUNOSe SNMP agent.  This version of the MPLS component is supported in
        JUNOSe 6.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniMplsAgentV4.setStatus(
        "obsolete"
    )

juniMplsAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 5)
)
if mibBuilder.loadTexts:
    juniMplsAgentV5.setProductRelease("""\
Version 5 of the MultiProtocol Label Switching (MPLS) component of the
        JUNOSe SNMP agent.  This version of the MPLS component is supported in
        JUNOSe 6.1 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniMplsAgentV5.setStatus(
        "obsolete"
    )

juniMplsAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 51, 6)
)
if mibBuilder.loadTexts:
    juniMplsAgentV6.setProductRelease("""\
Version 6 of the MultiProtocol Label Switching (MPLS) component of the
        JUNOSe SNMP agent.  This version of the MPLS component is supported in
        JUNOSe 7.1 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniMplsAgentV6.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-MPLS-CONF",
    **{"juniMplsAgent": juniMplsAgent,
       "juniMplsAgentV1": juniMplsAgentV1,
       "juniMplsAgentV2": juniMplsAgentV2,
       "juniMplsAgentV3": juniMplsAgentV3,
       "juniMplsAgentV4": juniMplsAgentV4,
       "juniMplsAgentV5": juniMplsAgentV5,
       "juniMplsAgentV6": juniMplsAgentV6}
)
