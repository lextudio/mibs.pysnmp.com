# SNMP MIB module (CISCO-FLEX-LINKS-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FLEX-LINKS-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:36 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoFlexLinksCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 444)
)
ciscoFlexLinksCapability.setRevisions(
        ("2010-05-18 00:00",
         "2005-07-28 00:00",
         "2005-06-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoFlexLinksCapCatOSV08R0501 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 444, 1)
)
if mibBuilder.loadTexts:
    ciscoFlexLinksCapCatOSV08R0501.setProductRelease("Cisco CatOS 8.5(1).")
if mibBuilder.loadTexts:
    ciscoFlexLinksCapCatOSV08R0501.setStatus(
        "current"
    )

cFlexLinksCapV12R0218SXFPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 444, 2)
)
if mibBuilder.loadTexts:
    cFlexLinksCapV12R0218SXFPCat6k.setProductRelease("""\
Cisco IOS 12.2(18)SXF on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cFlexLinksCapV12R0218SXFPCat6k.setStatus(
        "current"
    )

cFlexLinksCapV12R0254SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 444, 3)
)
if mibBuilder.loadTexts:
    cFlexLinksCapV12R0254SGPCat4K.setProductRelease("Cisco IOS 12.2(54)SG on CAT4K family switches.")
if mibBuilder.loadTexts:
    cFlexLinksCapV12R0254SGPCat4K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FLEX-LINKS-CAPABILITY",
    **{"ciscoFlexLinksCapability": ciscoFlexLinksCapability,
       "ciscoFlexLinksCapCatOSV08R0501": ciscoFlexLinksCapCatOSV08R0501,
       "cFlexLinksCapV12R0218SXFPCat6k": cFlexLinksCapV12R0218SXFPCat6k,
       "cFlexLinksCapV12R0254SGPCat4K": cFlexLinksCapV12R0254SGPCat4K}
)
