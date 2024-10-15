# SNMP MIB module (Unisphere-Data-L2TP-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-L2TP-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:04 2024
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

(usdL2tpConfigGroup,
 usdL2tpConfigGroup2,
 usdL2tpConfigGroup3,
 usdL2tpMapGroup,
 usdL2tpStatGroup,
 usdL2tpStatGroup2,
 usdL2tpStatusGroup,
 usdL2tpStatusGroup2,
 usdL2tpUdpIpGroup) = mibBuilder.importSymbols(
    "Unisphere-Data-L2TP-MIB",
    "usdL2tpConfigGroup",
    "usdL2tpConfigGroup2",
    "usdL2tpConfigGroup3",
    "usdL2tpMapGroup",
    "usdL2tpStatGroup",
    "usdL2tpStatGroup2",
    "usdL2tpStatusGroup",
    "usdL2tpStatusGroup2",
    "usdL2tpUdpIpGroup")


# MODULE-IDENTITY

usdL2tpAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24)
)
usdL2tpAgent.setRevisions(
        ("2001-10-17 16:03",
         "2001-10-17 14:21")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdL2tpAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 1)
)
if mibBuilder.loadTexts:
    usdL2tpAgentV1.setProductRelease("""\
Version 1 of the L2TP component of the Unisphere Routing Switch SNMP
        agent.  This version of the L2TP component was supported in the
        Unisphere RX 2.x system releases.""")
if mibBuilder.loadTexts:
    usdL2tpAgentV1.setStatus(
        "obsolete"
    )

usdL2tpAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 2)
)
if mibBuilder.loadTexts:
    usdL2tpAgentV2.setProductRelease("""\
Version 2 of the L2TP component of the Unisphere Routing Switch SNMP
        agent.  This version of the L2TP component was supported in the
        Unisphere RX 3.0 and 3.1 system releases.""")
if mibBuilder.loadTexts:
    usdL2tpAgentV2.setStatus(
        "obsolete"
    )

usdL2tpAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 3)
)
if mibBuilder.loadTexts:
    usdL2tpAgentV3.setProductRelease("""\
Version 3 of the L2TP component of the Unisphere Routing Switch SNMP
        agent.  This version of the L2TP component was supported in the
        Unisphere RX 3.2 system release.""")
if mibBuilder.loadTexts:
    usdL2tpAgentV3.setStatus(
        "obsolete"
    )

usdL2tpAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 4)
)
if mibBuilder.loadTexts:
    usdL2tpAgentV4.setProductRelease("""\
Version 4 of the L2TP component of the Unisphere Routing Switch SNMP
        agent.  This version of the L2TP component is supported in the Unisphere
        RX 3.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdL2tpAgentV4.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-L2TP-CONF",
    **{"usdL2tpAgent": usdL2tpAgent,
       "usdL2tpAgentV1": usdL2tpAgentV1,
       "usdL2tpAgentV2": usdL2tpAgentV2,
       "usdL2tpAgentV3": usdL2tpAgentV3,
       "usdL2tpAgentV4": usdL2tpAgentV4}
)
