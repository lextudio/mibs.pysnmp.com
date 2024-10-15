# SNMP MIB module (Unisphere-Data-SSC-Client-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-SSC-Client-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:41 2024
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

(usDataAgents,) = mibBuilder.importSymbols(
    "Unisphere-Data-Agents",
    "usDataAgents")

(usdSscClientGroup,
 usdSscClientGroup2,
 usdSscClientGroup3) = mibBuilder.importSymbols(
    "Unisphere-Data-SSC-CLIENT-MIB",
    "usdSscClientGroup",
    "usdSscClientGroup2",
    "usdSscClientGroup3")


# MODULE-IDENTITY

usdSscClientAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 41)
)
usdSscClientAgent.setRevisions(
        ("2001-09-19 20:29",
         "2001-03-30 15:18")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdSscClientAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 1)
)
if mibBuilder.loadTexts:
    usdSscClientAgentV1.setProductRelease("""\
Version 1 of the SSC Client component of the Unisphere Routing Switch
        SNMP agent.  This version of the SSC Client component was supported in
        the Unisphere RX 2.0 thru 3.0 system releases.""")
if mibBuilder.loadTexts:
    usdSscClientAgentV1.setStatus(
        "obsolete"
    )

usdSscClientAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 2)
)
if mibBuilder.loadTexts:
    usdSscClientAgentV2.setProductRelease("""\
Version 2 of the SSC Client component of the Unisphere Routing Switch
        SNMP agent.  This version of the SSC Client component is supported in
        the Unisphere RX 3.1 thru 3.x system releases.""")
if mibBuilder.loadTexts:
    usdSscClientAgentV2.setStatus(
        "obsolete"
    )

usdSscClientAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 41, 3)
)
if mibBuilder.loadTexts:
    usdSscClientAgentV3.setProductRelease("""\
Version 3 of the SSC Client component of the Unisphere Routing Switch
        SNMP agent.  This version of the SSC Client component is supported in
        the Unisphere RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdSscClientAgentV3.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-SSC-Client-CONF",
    **{"usdSscClientAgent": usdSscClientAgent,
       "usdSscClientAgentV1": usdSscClientAgentV1,
       "usdSscClientAgentV2": usdSscClientAgentV2,
       "usdSscClientAgentV3": usdSscClientAgentV3}
)
