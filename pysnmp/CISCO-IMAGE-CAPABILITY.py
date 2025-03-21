# SNMP MIB module (CISCO-IMAGE-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IMAGE-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:24 2024
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

ciscoImageMIBCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 580)
)
ciscoImageMIBCapability.setRevisions(
        ("2009-03-26 00:00",
         "2003-09-15 00:00",
         "1995-01-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoImageMIBCapabilityV10R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 580, 1)
)
if mibBuilder.loadTexts:
    ciscoImageMIBCapabilityV10R01.setProductRelease("Cisco IOS 10.2")
if mibBuilder.loadTexts:
    ciscoImageMIBCapabilityV10R01.setStatus(
        "current"
    )

ciscoImageCapabilityV12R0119ECat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 580, 2)
)
if mibBuilder.loadTexts:
    ciscoImageCapabilityV12R0119ECat6K.setProductRelease("""\
Cisco IOS 12.1(19E) on Catalyst 6000/6500
                      and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoImageCapabilityV12R0119ECat6K.setStatus(
        "current"
    )

ciscoImageCapabilityV12R0217SXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 580, 3)
)
if mibBuilder.loadTexts:
    ciscoImageCapabilityV12R0217SXCat6K.setProductRelease("""\
Cisco IOS 12.2(17SX) on Catalyst 6000/6500
                      and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoImageCapabilityV12R0217SXCat6K.setStatus(
        "current"
    )

ciscoImageCapabilityCatOSV08R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 580, 4)
)
if mibBuilder.loadTexts:
    ciscoImageCapabilityCatOSV08R0101.setProductRelease("Cisco CatOS 8.1(1).")
if mibBuilder.loadTexts:
    ciscoImageCapabilityCatOSV08R0101.setStatus(
        "current"
    )

ciscoImageCapabilityGssV03R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 580, 5)
)
if mibBuilder.loadTexts:
    ciscoImageCapabilityGssV03R01.setProductRelease("Global Site Selector(GSS) 3.1(0)")
if mibBuilder.loadTexts:
    ciscoImageCapabilityGssV03R01.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IMAGE-CAPABILITY",
    **{"ciscoImageMIBCapability": ciscoImageMIBCapability,
       "ciscoImageMIBCapabilityV10R01": ciscoImageMIBCapabilityV10R01,
       "ciscoImageCapabilityV12R0119ECat6K": ciscoImageCapabilityV12R0119ECat6K,
       "ciscoImageCapabilityV12R0217SXCat6K": ciscoImageCapabilityV12R0217SXCat6K,
       "ciscoImageCapabilityCatOSV08R0101": ciscoImageCapabilityCatOSV08R0101,
       "ciscoImageCapabilityGssV03R01": ciscoImageCapabilityGssV03R01}
)
