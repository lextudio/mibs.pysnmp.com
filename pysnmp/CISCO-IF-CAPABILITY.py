# SNMP MIB module (CISCO-IF-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IF-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:09 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIfCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 125)
)
ciscoIfCapability.setRevisions(
        ("2008-03-17 00:00",
         "2006-11-03 00:00",
         "2006-10-30 00:00",
         "2006-07-17 00:00",
         "2006-02-02 00:00",
         "2004-08-09 00:00",
         "2004-02-21 00:00",
         "2004-02-20 00:00",
         "2003-03-14 00:00",
         "2002-06-12 00:00",
         "2000-02-09 00:00",
         "1998-11-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoIfCapabilityV11R03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 1)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityV11R03.setProductRelease("Cisco IOS 11.3")
if mibBuilder.loadTexts:
    ciscoIfCapabilityV11R03.setStatus(
        "current"
    )

ciscoIfCapabilityV12R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 2)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityV12R00.setProductRelease("Cisco IOS 12.0")
if mibBuilder.loadTexts:
    ciscoIfCapabilityV12R00.setStatus(
        "current"
    )

ciscoIfCapabilityV12R01T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 3)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityV12R01T.setProductRelease("Cisco IOS 12.1T")
if mibBuilder.loadTexts:
    ciscoIfCapabilityV12R01T.setStatus(
        "current"
    )

ciscoIfCapabilityPxmVR200 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 4)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityPxmVR200.setProductRelease("MGX8850 Release 2.00,BPX SES Release 1.00.")
if mibBuilder.loadTexts:
    ciscoIfCapabilityPxmVR200.setStatus(
        "current"
    )

ciscoIfCapabilityAxsmVR200 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 5)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityAxsmVR200.setProductRelease("MGX8850 Release 2.00.")
if mibBuilder.loadTexts:
    ciscoIfCapabilityAxsmVR200.setStatus(
        "current"
    )

ciscoIfCapabilityAxsmeV21R60 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 6)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityAxsmeV21R60.setProductRelease("MGX8850 Release 2.1.60")
if mibBuilder.loadTexts:
    ciscoIfCapabilityAxsmeV21R60.setStatus(
        "current"
    )

ciscoIfCapabilityFrsm12V3R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 7)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityFrsm12V3R00.setProductRelease("MGX8850 Release 3.0.00")
if mibBuilder.loadTexts:
    ciscoIfCapabilityFrsm12V3R00.setStatus(
        "current"
    )

ciscoIfCapabilityV4R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 8)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityV4R00.setProductRelease("MGX8950, MGX8850 Release 4.0.00")
if mibBuilder.loadTexts:
    ciscoIfCapabilityV4R00.setStatus(
        "current"
    )

ciscoIfCapabilityV5R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 9)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityV5R00.setProductRelease("MGX8850 Release 5.0.0")
if mibBuilder.loadTexts:
    ciscoIfCapabilityV5R00.setStatus(
        "current"
    )

ciscoIfCapabilityCatOSV08R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 10)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityCatOSV08R0101.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoIfCapabilityCatOSV08R0101.setStatus(
        "current"
    )

ciscoIfCapabilityCatOSV08R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 11)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityCatOSV08R0301.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoIfCapabilityCatOSV08R0301.setStatus(
        "current"
    )

ciscoIfCapabilityV5R015 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 12)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityV5R015.setProductRelease("MGX8850 Release 5.0.15")
if mibBuilder.loadTexts:
    ciscoIfCapabilityV5R015.setStatus(
        "current"
    )

ciscoIfCapabilityIOSXRV2R0CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 13)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityIOSXRV2R0CRS1.setProductRelease("Cisco IOS XR 2.0 for CRS-1")
if mibBuilder.loadTexts:
    ciscoIfCapabilityIOSXRV2R0CRS1.setStatus(
        "current"
    )

ciscoIfCapabilityACSWV03R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 14)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityACSWV03R000.setProductRelease("""\
ACSW (Application Control Software) 3.0
                    for Application Control Engine (ACE) 
                    Service Module.""")
if mibBuilder.loadTexts:
    ciscoIfCapabilityACSWV03R000.setStatus(
        "current"
    )

ciscoIfCapabilityCTSV100 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 15)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityCTSV100.setProductRelease("Cisco TelePresence System (CTS) 1.0.0")
if mibBuilder.loadTexts:
    ciscoIfCapabilityCTSV100.setStatus(
        "current"
    )

ciscoIfCapabilityCTMV1000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 16)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityCTMV1000.setProductRelease("Cisco TelePresence Manager (CTM) 1.0.0.0")
if mibBuilder.loadTexts:
    ciscoIfCapabilityCTMV1000.setStatus(
        "current"
    )

ciscoIfCapabilityIOSXRV3R4CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 17)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityIOSXRV3R4CRS1.setProductRelease("Cisco IOS XR 3.4 for CRS-1")
if mibBuilder.loadTexts:
    ciscoIfCapabilityIOSXRV3R4CRS1.setStatus(
        "current"
    )

ciscoIfCapabilityc4710aceVA1R700 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 125, 18)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityc4710aceVA1R700.setProductRelease("""\
ACSW (Application Control Software) A1(7)
                     for ACE 4710 Application Control Engine 
                     Appliance""")
if mibBuilder.loadTexts:
    ciscoIfCapabilityc4710aceVA1R700.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IF-CAPABILITY",
    **{"ciscoIfCapability": ciscoIfCapability,
       "ciscoIfCapabilityV11R03": ciscoIfCapabilityV11R03,
       "ciscoIfCapabilityV12R00": ciscoIfCapabilityV12R00,
       "ciscoIfCapabilityV12R01T": ciscoIfCapabilityV12R01T,
       "ciscoIfCapabilityPxmVR200": ciscoIfCapabilityPxmVR200,
       "ciscoIfCapabilityAxsmVR200": ciscoIfCapabilityAxsmVR200,
       "ciscoIfCapabilityAxsmeV21R60": ciscoIfCapabilityAxsmeV21R60,
       "ciscoIfCapabilityFrsm12V3R00": ciscoIfCapabilityFrsm12V3R00,
       "ciscoIfCapabilityV4R00": ciscoIfCapabilityV4R00,
       "ciscoIfCapabilityV5R00": ciscoIfCapabilityV5R00,
       "ciscoIfCapabilityCatOSV08R0101": ciscoIfCapabilityCatOSV08R0101,
       "ciscoIfCapabilityCatOSV08R0301": ciscoIfCapabilityCatOSV08R0301,
       "ciscoIfCapabilityV5R015": ciscoIfCapabilityV5R015,
       "ciscoIfCapabilityIOSXRV2R0CRS1": ciscoIfCapabilityIOSXRV2R0CRS1,
       "ciscoIfCapabilityACSWV03R000": ciscoIfCapabilityACSWV03R000,
       "ciscoIfCapabilityCTSV100": ciscoIfCapabilityCTSV100,
       "ciscoIfCapabilityCTMV1000": ciscoIfCapabilityCTMV1000,
       "ciscoIfCapabilityIOSXRV3R4CRS1": ciscoIfCapabilityIOSXRV3R4CRS1,
       "ciscoIfCapabilityc4710aceVA1R700": ciscoIfCapabilityc4710aceVA1R700}
)
