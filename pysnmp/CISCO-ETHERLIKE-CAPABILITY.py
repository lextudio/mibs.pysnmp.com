# SNMP MIB module (CISCO-ETHERLIKE-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ETHERLIKE-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:57 2024
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

ciscoEtherlikeCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 130)
)
ciscoEtherlikeCapability.setRevisions(
        ("2011-04-01 00:00",
         "2010-10-29 00:00",
         "2010-03-17 00:00",
         "2007-07-03 00:00",
         "2003-09-08 00:00",
         "2000-01-21 14:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoEtherlikeCapabilityV12R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 130, 1)
)
if mibBuilder.loadTexts:
    ciscoEtherlikeCapabilityV12R01.setProductRelease("Cisco IOS 12.1")
if mibBuilder.loadTexts:
    ciscoEtherlikeCapabilityV12R01.setStatus(
        "current"
    )

ciscoEtherlikeCapV12R0111bEX = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 130, 2)
)
if mibBuilder.loadTexts:
    ciscoEtherlikeCapV12R0111bEX.setProductRelease("""\
Cisco IOS 12.1(11b)EX on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoEtherlikeCapV12R0111bEX.setStatus(
        "current"
    )

ciscoEtherlikeCapV12R0214SX = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 130, 3)
)
if mibBuilder.loadTexts:
    ciscoEtherlikeCapV12R0214SX.setProductRelease("""\
Cisco IOS 12.2(14)SX on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoEtherlikeCapV12R0214SX.setStatus(
        "current"
    )

ciscoEtherlikeCapV08R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 130, 4)
)
if mibBuilder.loadTexts:
    ciscoEtherlikeCapV08R0101.setProductRelease("Cisco CatOS 8.1(1).")
if mibBuilder.loadTexts:
    ciscoEtherlikeCapV08R0101.setStatus(
        "current"
    )

cEtherlikeCapV12R0233SXHPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 130, 5)
)
if mibBuilder.loadTexts:
    cEtherlikeCapV12R0233SXHPCat6k.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                         series devices.""")
if mibBuilder.loadTexts:
    cEtherlikeCapV12R0233SXHPCat6k.setStatus(
        "current"
    )

cEtherlikeCapV12R0233SXI4PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 130, 6)
)
if mibBuilder.loadTexts:
    cEtherlikeCapV12R0233SXI4PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500
                         series devices.""")
if mibBuilder.loadTexts:
    cEtherlikeCapV12R0233SXI4PCat6K.setStatus(
        "current"
    )

cEtherlikeCapV12R0250SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 130, 7)
)
if mibBuilder.loadTexts:
    cEtherlikeCapV12R0250SYPCat6K.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                         series devices.""")
if mibBuilder.loadTexts:
    cEtherlikeCapV12R0250SYPCat6K.setStatus(
        "current"
    )

cEtherlikeCapV15R0002SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 130, 8)
)
if mibBuilder.loadTexts:
    cEtherlikeCapV15R0002SGPCat4K.setProductRelease("Cisco IOS 15.0(2)SG on Cat4K family switches.")
if mibBuilder.loadTexts:
    cEtherlikeCapV15R0002SGPCat4K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ETHERLIKE-CAPABILITY",
    **{"ciscoEtherlikeCapability": ciscoEtherlikeCapability,
       "ciscoEtherlikeCapabilityV12R01": ciscoEtherlikeCapabilityV12R01,
       "ciscoEtherlikeCapV12R0111bEX": ciscoEtherlikeCapV12R0111bEX,
       "ciscoEtherlikeCapV12R0214SX": ciscoEtherlikeCapV12R0214SX,
       "ciscoEtherlikeCapV08R0101": ciscoEtherlikeCapV08R0101,
       "cEtherlikeCapV12R0233SXHPCat6k": cEtherlikeCapV12R0233SXHPCat6k,
       "cEtherlikeCapV12R0233SXI4PCat6K": cEtherlikeCapV12R0233SXI4PCat6K,
       "cEtherlikeCapV12R0250SYPCat6K": cEtherlikeCapV12R0250SYPCat6K,
       "cEtherlikeCapV15R0002SGPCat4K": cEtherlikeCapV15R0002SGPCat4K}
)
