# SNMP MIB module (Unisphere-Data-IS-IS-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-IS-IS-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:58 2024
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

(usdIsisCircuitMgmtGroup,
 usdIsisCircuitMgmtGroup2,
 usdIsisSystemMgmtGroup,
 usdIsisSystemMgmtGroup2) = mibBuilder.importSymbols(
    "Unisphere-Data-ISIS-MIB",
    "usdIsisCircuitMgmtGroup",
    "usdIsisCircuitMgmtGroup2",
    "usdIsisSystemMgmtGroup",
    "usdIsisSystemMgmtGroup2")


# MODULE-IDENTITY

usdIsisAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 23)
)
usdIsisAgent.setRevisions(
        ("2002-04-04 20:37",
         "2001-04-24 19:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdIsisAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 1)
)
if mibBuilder.loadTexts:
    usdIsisAgentV1.setProductRelease("""\
Version 1 of the IS-IS component of the Unisphere Routing Switch SNMP
        agent.  This version of the IS-IS component was supported in the
        Unisphere RX 2.x system releases.""")
if mibBuilder.loadTexts:
    usdIsisAgentV1.setStatus(
        "obsolete"
    )

usdIsisAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 2)
)
if mibBuilder.loadTexts:
    usdIsisAgentV2.setProductRelease("""\
Version 2 of the IS-IS component of the Unisphere Routing Switch SNMP
        agent.  This version of the IS-IS component was supported in the
        Unisphere RX 3.x system releases.""")
if mibBuilder.loadTexts:
    usdIsisAgentV2.setStatus(
        "current"
    )

usdIsisAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 23, 3)
)
if mibBuilder.loadTexts:
    usdIsisAgentV3.setProductRelease("""\
Version 3 of the IS-IS component of the Unisphere Routing Switch SNMP
        agent.  This version of the IS-IS component is supported in the
        Unisphere RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdIsisAgentV3.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-IS-IS-CONF",
    **{"usdIsisAgent": usdIsisAgent,
       "usdIsisAgentV1": usdIsisAgentV1,
       "usdIsisAgentV2": usdIsisAgentV2,
       "usdIsisAgentV3": usdIsisAgentV3}
)
