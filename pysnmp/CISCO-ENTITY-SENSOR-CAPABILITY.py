# SNMP MIB module (CISCO-ENTITY-SENSOR-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-SENSOR-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:42 2024
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

ciscoEntitySensorCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 350)
)
ciscoEntitySensorCapability.setRevisions(
        ("2011-02-03 00:00",
         "2008-10-06 00:00",
         "2007-07-09 00:00",
         "2007-06-29 00:00",
         "2006-06-29 00:00",
         "2005-09-15 00:00",
         "2005-04-22 00:00",
         "2004-09-09 00:00",
         "2003-08-12 00:00",
         "2003-03-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoEntitySensorCapabilityV5R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 350, 1)
)
if mibBuilder.loadTexts:
    ciscoEntitySensorCapabilityV5R000.setProductRelease("MGX8850 Release 5.0.")
if mibBuilder.loadTexts:
    ciscoEntitySensorCapabilityV5R000.setStatus(
        "current"
    )

cEntitySensorCapV12R0119ECat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 350, 2)
)
if mibBuilder.loadTexts:
    cEntitySensorCapV12R0119ECat6K.setProductRelease("""\
Cisco IOS 12.1(19)E on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cEntitySensorCapV12R0119ECat6K.setStatus(
        "current"
    )

cEntitySensorCapV12R0214SXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 350, 3)
)
if mibBuilder.loadTexts:
    cEntitySensorCapV12R0214SXCat6K.setProductRelease("""\
Cisco IOS 12.2(14)SX on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cEntitySensorCapV12R0214SXCat6K.setStatus(
        "current"
    )

cEntitySensorCapCatOSV08R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 350, 4)
)
if mibBuilder.loadTexts:
    cEntitySensorCapCatOSV08R0101.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cEntitySensorCapCatOSV08R0101.setStatus(
        "current"
    )

cEntitySensorCapabilityV5R015 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 350, 5)
)
if mibBuilder.loadTexts:
    cEntitySensorCapabilityV5R015.setProductRelease("MGX8850 Release 5.0.15")
if mibBuilder.loadTexts:
    cEntitySensorCapabilityV5R015.setStatus(
        "current"
    )

cEntitySensorCapMDS3R0 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 350, 6)
)
if mibBuilder.loadTexts:
    cEntitySensorCapMDS3R0.setProductRelease("Cisco MDS 3.0(1).")
if mibBuilder.loadTexts:
    cEntitySensorCapMDS3R0.setStatus(
        "current"
    )

cEntitySensorCapCatOSV08R0601 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 350, 7)
)
if mibBuilder.loadTexts:
    cEntitySensorCapCatOSV08R0601.setProductRelease("Cisco CatOS 8.6(1).")
if mibBuilder.loadTexts:
    cEntitySensorCapCatOSV08R0601.setStatus(
        "current"
    )

cEntitySensorCapIOSXRV3R06CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 350, 8)
)
if mibBuilder.loadTexts:
    cEntitySensorCapIOSXRV3R06CRS1.setProductRelease("Cisco IOS-XR Release 3.6 for CRS-1.")
if mibBuilder.loadTexts:
    cEntitySensorCapIOSXRV3R06CRS1.setStatus(
        "current"
    )

cEntitySensorCapMDS3R1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 350, 9)
)
if mibBuilder.loadTexts:
    cEntitySensorCapMDS3R1.setProductRelease("""\
Cisco MDS Series Storage switches
                         Release 3.1 onwards.""")
if mibBuilder.loadTexts:
    cEntitySensorCapMDS3R1.setStatus(
        "current"
    )

cEntitySensorCapDCOSNEXUS = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 350, 10)
)
if mibBuilder.loadTexts:
    cEntitySensorCapDCOSNEXUS.setProductRelease("Cisco Nexus7000 Series Storage switches.")
if mibBuilder.loadTexts:
    cEntitySensorCapDCOSNEXUS.setStatus(
        "current"
    )

cEntitySensorCapV12R0250SE = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 350, 11)
)
if mibBuilder.loadTexts:
    cEntitySensorCapV12R0250SE.setProductRelease("Cisco IOS 12.2(50)SE")
if mibBuilder.loadTexts:
    cEntitySensorCapV12R0250SE.setStatus(
        "current"
    )

cEntitySensorCapV12R0250SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 350, 12)
)
if mibBuilder.loadTexts:
    cEntitySensorCapV12R0250SYPCat6K.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cEntitySensorCapV12R0250SYPCat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-SENSOR-CAPABILITY",
    **{"ciscoEntitySensorCapability": ciscoEntitySensorCapability,
       "ciscoEntitySensorCapabilityV5R000": ciscoEntitySensorCapabilityV5R000,
       "cEntitySensorCapV12R0119ECat6K": cEntitySensorCapV12R0119ECat6K,
       "cEntitySensorCapV12R0214SXCat6K": cEntitySensorCapV12R0214SXCat6K,
       "cEntitySensorCapCatOSV08R0101": cEntitySensorCapCatOSV08R0101,
       "cEntitySensorCapabilityV5R015": cEntitySensorCapabilityV5R015,
       "cEntitySensorCapMDS3R0": cEntitySensorCapMDS3R0,
       "cEntitySensorCapCatOSV08R0601": cEntitySensorCapCatOSV08R0601,
       "cEntitySensorCapIOSXRV3R06CRS1": cEntitySensorCapIOSXRV3R06CRS1,
       "cEntitySensorCapMDS3R1": cEntitySensorCapMDS3R1,
       "cEntitySensorCapDCOSNEXUS": cEntitySensorCapDCOSNEXUS,
       "cEntitySensorCapV12R0250SE": cEntitySensorCapV12R0250SE,
       "cEntitySensorCapV12R0250SYPCat6K": cEntitySensorCapV12R0250SYPCat6K}
)
