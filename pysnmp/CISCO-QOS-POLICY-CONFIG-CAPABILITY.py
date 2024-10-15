# SNMP MIB module (CISCO-QOS-POLICY-CONFIG-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-QOS-POLICY-CONFIG-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:21 2024
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

(ciscoAgentCapability,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoAgentCapability")

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

ciscoQosPolicyConfigCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 363)
)
ciscoQosPolicyConfigCapability.setRevisions(
        ("2007-06-28 00:00",
         "2003-10-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cqpcCapabilityCatOSV08R0101Cat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 363, 1)
)
if mibBuilder.loadTexts:
    cqpcCapabilityCatOSV08R0101Cat6k.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                      and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cqpcCapabilityCatOSV08R0101Cat6k.setStatus(
        "current"
    )

cqpcCapabilityV12R0233SXHPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 363, 2)
)
if mibBuilder.loadTexts:
    cqpcCapabilityV12R0233SXHPCat6k.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                         devices.""")
if mibBuilder.loadTexts:
    cqpcCapabilityV12R0233SXHPCat6k.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-QOS-POLICY-CONFIG-CAPABILITY",
    **{"ciscoQosPolicyConfigCapability": ciscoQosPolicyConfigCapability,
       "cqpcCapabilityCatOSV08R0101Cat6k": cqpcCapabilityCatOSV08R0101Cat6k,
       "cqpcCapabilityV12R0233SXHPCat6k": cqpcCapabilityV12R0233SXHPCat6k}
)
