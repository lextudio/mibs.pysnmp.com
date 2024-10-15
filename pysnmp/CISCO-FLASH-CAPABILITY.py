# SNMP MIB module (CISCO-FLASH-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FLASH-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:35 2024
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

ciscoFlashCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 222)
)
ciscoFlashCapability.setRevisions(
        ("2008-01-18 00:00",
         "2004-04-01 00:00",
         "2003-10-21 00:00",
         "2001-09-25 12:34")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoFlashCapabilityV12R00S = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 222, 1)
)
if mibBuilder.loadTexts:
    ciscoFlashCapabilityV12R00S.setProductRelease("Cisco IOS 12.0S")
if mibBuilder.loadTexts:
    ciscoFlashCapabilityV12R00S.setStatus(
        "current"
    )

ciscoFlashCapabilityV12R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 222, 2)
)
if mibBuilder.loadTexts:
    ciscoFlashCapabilityV12R01.setProductRelease("Cisco IOS 12.1")
if mibBuilder.loadTexts:
    ciscoFlashCapabilityV12R01.setStatus(
        "current"
    )

ciscoFlashCapabilityV12R02 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 222, 3)
)
if mibBuilder.loadTexts:
    ciscoFlashCapabilityV12R02.setProductRelease("Cisco IOS 12.2")
if mibBuilder.loadTexts:
    ciscoFlashCapabilityV12R02.setStatus(
        "current"
    )

ciscoFlashMibCapCatOSV7R0501Cat4k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 222, 4)
)
if mibBuilder.loadTexts:
    ciscoFlashMibCapCatOSV7R0501Cat4k.setProductRelease("Cisco CatOS 7.5(1) on  Catalyst 4000.")
if mibBuilder.loadTexts:
    ciscoFlashMibCapCatOSV7R0501Cat4k.setStatus(
        "current"
    )

ciscoFlashMibCapCatOSV7R0501Cat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 222, 5)
)
if mibBuilder.loadTexts:
    ciscoFlashMibCapCatOSV7R0501Cat6k.setProductRelease("Cisco CatOS 7.5(1) on Catalyst 6000.")
if mibBuilder.loadTexts:
    ciscoFlashMibCapCatOSV7R0501Cat6k.setStatus(
        "current"
    )

ciscoFlashMibCapV12R0113ECat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 222, 6)
)
if mibBuilder.loadTexts:
    ciscoFlashMibCapV12R0113ECat6K.setProductRelease("""\
Cisco IOS 12.1(13E) on Catalyst 6000/6500 and Cisco
                7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoFlashMibCapV12R0113ECat6K.setStatus(
        "current"
    )

ciscoFlashMibCapCatOSV08R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 222, 7)
)
if mibBuilder.loadTexts:
    ciscoFlashMibCapCatOSV08R0301.setProductRelease("""\
Cisco CatOS 8.3(1)on Catalyst 6000/6500
                and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoFlashMibCapCatOSV08R0301.setStatus(
        "current"
    )

ciscoFlashMibCapXRV03R06PCRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 222, 8)
)
if mibBuilder.loadTexts:
    ciscoFlashMibCapXRV03R06PCRS1.setProductRelease("Cisco IOS XR 3.6 on CRS-1")
if mibBuilder.loadTexts:
    ciscoFlashMibCapXRV03R06PCRS1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FLASH-CAPABILITY",
    **{"ciscoFlashCapability": ciscoFlashCapability,
       "ciscoFlashCapabilityV12R00S": ciscoFlashCapabilityV12R00S,
       "ciscoFlashCapabilityV12R01": ciscoFlashCapabilityV12R01,
       "ciscoFlashCapabilityV12R02": ciscoFlashCapabilityV12R02,
       "ciscoFlashMibCapCatOSV7R0501Cat4k": ciscoFlashMibCapCatOSV7R0501Cat4k,
       "ciscoFlashMibCapCatOSV7R0501Cat6k": ciscoFlashMibCapCatOSV7R0501Cat6k,
       "ciscoFlashMibCapV12R0113ECat6K": ciscoFlashMibCapV12R0113ECat6K,
       "ciscoFlashMibCapCatOSV08R0301": ciscoFlashMibCapCatOSV08R0301,
       "ciscoFlashMibCapXRV03R06PCRS1": ciscoFlashMibCapXRV03R06PCRS1}
)
