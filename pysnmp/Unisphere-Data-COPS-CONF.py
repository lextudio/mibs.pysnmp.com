# SNMP MIB module (Unisphere-Data-COPS-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-COPS-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:28 2024
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

(usdCopsProtocolGroup,
 usdCopsProtocolGroup2) = mibBuilder.importSymbols(
    "Unisphere-Data-COPS-MIB",
    "usdCopsProtocolGroup",
    "usdCopsProtocolGroup2")


# MODULE-IDENTITY

usdCopsAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 7)
)
usdCopsAgent.setRevisions(
        ("2002-01-14 19:36",
         "2001-03-27 22:45")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdCopsAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 7, 1)
)
if mibBuilder.loadTexts:
    usdCopsAgentV1.setProductRelease("""\
Version 1 of the COPS component of the Unisphere Routing Switch SNMP
        agent.  This version of the COPS component was supported in the
        Unisphere RX 2.x and 3.x system releases.""")
if mibBuilder.loadTexts:
    usdCopsAgentV1.setStatus(
        "current"
    )

usdCopsAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 7, 2)
)
if mibBuilder.loadTexts:
    usdCopsAgentV2.setProductRelease("""\
Version 2 of the COPS component of the Unisphere Routing Switch SNMP
        agent.  This version of the COPS component is supported in the Unisphere
        RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdCopsAgentV2.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-COPS-CONF",
    **{"usdCopsAgent": usdCopsAgent,
       "usdCopsAgentV1": usdCopsAgentV1,
       "usdCopsAgentV2": usdCopsAgentV2}
)
