# SNMP MIB module (CISCO-ENTITY-ASSET-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-ASSET-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:29 2024
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

ciscoEntityAssetCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 300)
)
ciscoEntityAssetCapability.setRevisions(
        ("2003-09-04 00:00",
         "2003-04-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ceAssetCapabilityV4R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 300, 1)
)
if mibBuilder.loadTexts:
    ceAssetCapabilityV4R00.setProductRelease("MGX8850 Release 4.0.00")
if mibBuilder.loadTexts:
    ceAssetCapabilityV4R00.setStatus(
        "current"
    )

ceAssetCapV12R0214SXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 300, 2)
)
if mibBuilder.loadTexts:
    ceAssetCapV12R0214SXCat6K.setProductRelease("""\
Cisco IOS 12.2(14)SX on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ceAssetCapV12R0214SXCat6K.setStatus(
        "current"
    )

ceAssetCapCatOSV08R0101Cat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 300, 3)
)
if mibBuilder.loadTexts:
    ceAssetCapCatOSV08R0101Cat6K.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ceAssetCapCatOSV08R0101Cat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-ASSET-CAPABILITY",
    **{"ciscoEntityAssetCapability": ciscoEntityAssetCapability,
       "ceAssetCapabilityV4R00": ceAssetCapabilityV4R00,
       "ceAssetCapV12R0214SXCat6K": ceAssetCapV12R0214SXCat6K,
       "ceAssetCapCatOSV08R0101Cat6K": ceAssetCapCatOSV08R0101Cat6K}
)
