# SNMP MIB module (Unisphere-Data-OSPF-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-OSPF-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:12 2024
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

(ospfAreaAggregateGroup,
 ospfAreaGroup,
 ospfBasicGroup,
 ospfExtLsdbGroup,
 ospfHostGroup,
 ospfIfGroup,
 ospfIfMetricGroup,
 ospfLsdbGroup,
 ospfNbrGroup,
 ospfStubAreaGroup,
 ospfVirtIfGroup,
 ospfVirtNbrGroup) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfAreaAggregateGroup",
    "ospfAreaGroup",
    "ospfBasicGroup",
    "ospfExtLsdbGroup",
    "ospfHostGroup",
    "ospfIfGroup",
    "ospfIfMetricGroup",
    "ospfLsdbGroup",
    "ospfNbrGroup",
    "ospfStubAreaGroup",
    "ospfVirtIfGroup",
    "ospfVirtNbrGroup")

(ospfConfigErrorType,
 ospfPacketSrc,
 ospfPacketType,
 ospfTrapControlGroup) = mibBuilder.importSymbols(
    "OSPF-TRAP-MIB",
    "ospfConfigErrorType",
    "ospfPacketSrc",
    "ospfPacketType",
    "ospfTrapControlGroup")

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

(usdOspfAreaGroup,
 usdOspfBasicGroup,
 usdOspfBasicGroup2,
 usdOspfIfGroup,
 usdOspfMd5IntfGroup,
 usdOspfMd5VirtIntfGroup,
 usdOspfNbrGroup,
 usdOspfNetRangeGroup,
 usdOspfSummImportGroup,
 usdOspfVirtIfGroup) = mibBuilder.importSymbols(
    "Unisphere-Data-OSPF-MIB",
    "usdOspfAreaGroup",
    "usdOspfBasicGroup",
    "usdOspfBasicGroup2",
    "usdOspfIfGroup",
    "usdOspfMd5IntfGroup",
    "usdOspfMd5VirtIntfGroup",
    "usdOspfNbrGroup",
    "usdOspfNetRangeGroup",
    "usdOspfSummImportGroup",
    "usdOspfVirtIfGroup")


# MODULE-IDENTITY

usdOspfAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 28)
)
usdOspfAgent.setRevisions(
        ("2001-12-06 15:12",
         "2001-03-29 13:34")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdOspfAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 28, 1)
)
if mibBuilder.loadTexts:
    usdOspfAgentV1.setProductRelease("""\
Version 1 of the OSPF component of the Unisphere Routing Switch SNMP
        agent.  This version of the OSPF component was supported in the
        Unisphere RX 2.x and 3.x system releases.""")
if mibBuilder.loadTexts:
    usdOspfAgentV1.setStatus(
        "obsolete"
    )

usdOspfAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 28, 2)
)
if mibBuilder.loadTexts:
    usdOspfAgentV2.setProductRelease("""\
Version 2 of the OSPF component of the Unisphere Routing Switch SNMP
        agent.  This version of the OSPF component is supported in the Unisphere
        RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdOspfAgentV2.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-OSPF-CONF",
    **{"usdOspfAgent": usdOspfAgent,
       "usdOspfAgentV1": usdOspfAgentV1,
       "usdOspfAgentV2": usdOspfAgentV2}
)
