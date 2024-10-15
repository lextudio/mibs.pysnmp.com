# SNMP MIB module (CISCO-ENTITY-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:30 2024
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

ciscoEntityCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 277)
)
ciscoEntityCapability.setRevisions(
        ("2014-04-03 00:00",
         "2013-07-19 00:00",
         "2009-03-24 00:00",
         "2008-07-03 00:00",
         "2006-11-16 00:00",
         "2006-05-26 00:00",
         "2006-03-24 00:00",
         "2006-02-08 00:00",
         "2003-08-12 00:00",
         "2003-08-08 00:00",
         "2002-06-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoEntityCapabilityV2R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 277, 1)
)
if mibBuilder.loadTexts:
    ciscoEntityCapabilityV2R00.setProductRelease("""\
MGX8850 Release 2.00,
                BPX SES Release 1.00""")
if mibBuilder.loadTexts:
    ciscoEntityCapabilityV2R00.setStatus(
        "current"
    )

ciscoEntityCapV12R0111bEXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 277, 2)
)
if mibBuilder.loadTexts:
    ciscoEntityCapV12R0111bEXCat6K.setProductRelease("""\
Cisco IOS 12.1(11b)EX on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoEntityCapV12R0111bEXCat6K.setStatus(
        "current"
    )

ciscoEntityCapV12R0214SXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 277, 3)
)
if mibBuilder.loadTexts:
    ciscoEntityCapV12R0214SXCat6K.setProductRelease("""\
Cisco IOS 12.2(14)SX on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoEntityCapV12R0214SXCat6K.setStatus(
        "current"
    )

ciscoEntityCapCatOSV08R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 277, 4)
)
if mibBuilder.loadTexts:
    ciscoEntityCapCatOSV08R0101.setProductRelease("Cisco CatOS 8.1(1).")
if mibBuilder.loadTexts:
    ciscoEntityCapCatOSV08R0101.setStatus(
        "current"
    )

ciscoEntityCapabilityV20CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 277, 5)
)
if mibBuilder.loadTexts:
    ciscoEntityCapabilityV20CRS1.setProductRelease("Cisco IOS XR 2.0 for CRS-1")
if mibBuilder.loadTexts:
    ciscoEntityCapabilityV20CRS1.setStatus(
        "current"
    )

ciscoEntityCapabilityACSWV03R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 277, 6)
)
if mibBuilder.loadTexts:
    ciscoEntityCapabilityACSWV03R000.setProductRelease("ACSW (Application Control Software) 3.0")
if mibBuilder.loadTexts:
    ciscoEntityCapabilityACSWV03R000.setStatus(
        "current"
    )

ciscoEntityCapabilityIOSXRV3R4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 277, 7)
)
if mibBuilder.loadTexts:
    ciscoEntityCapabilityIOSXRV3R4.setProductRelease("Cisco IOS XR 3.4 for CRS-1")
if mibBuilder.loadTexts:
    ciscoEntityCapabilityIOSXRV3R4.setStatus(
        "current"
    )

ciscoEntityCapc4710aceVA1R700 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 277, 8)
)
if mibBuilder.loadTexts:
    ciscoEntityCapc4710aceVA1R700.setProductRelease("""\
ACSW (Application Control Software) A1(7) for 
                    ACE 4710 Application Control Engine Appliance.""")
if mibBuilder.loadTexts:
    ciscoEntityCapc4710aceVA1R700.setStatus(
        "current"
    )

ciscoEntityCapabilityGssV03R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 277, 9)
)
if mibBuilder.loadTexts:
    ciscoEntityCapabilityGssV03R01.setProductRelease("Global Site Selector(GSS) 3.1(0)")
if mibBuilder.loadTexts:
    ciscoEntityCapabilityGssV03R01.setStatus(
        "current"
    )

ciscoEntityCapNxOSV06R0202PN7k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 277, 10)
)
if mibBuilder.loadTexts:
    ciscoEntityCapNxOSV06R0202PN7k.setProductRelease("""\
Cisco NX-OS 6.2(2) on Nexus 7000
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoEntityCapNxOSV06R0202PN7k.setStatus(
        "current"
    )

ciscoEntityCapNxOSV06R0201PMds = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 277, 11)
)
if mibBuilder.loadTexts:
    ciscoEntityCapNxOSV06R0201PMds.setProductRelease("""\
Cisco NX-OS 6.2(1) on MDS 9000
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoEntityCapNxOSV06R0201PMds.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-CAPABILITY",
    **{"ciscoEntityCapability": ciscoEntityCapability,
       "ciscoEntityCapabilityV2R00": ciscoEntityCapabilityV2R00,
       "ciscoEntityCapV12R0111bEXCat6K": ciscoEntityCapV12R0111bEXCat6K,
       "ciscoEntityCapV12R0214SXCat6K": ciscoEntityCapV12R0214SXCat6K,
       "ciscoEntityCapCatOSV08R0101": ciscoEntityCapCatOSV08R0101,
       "ciscoEntityCapabilityV20CRS1": ciscoEntityCapabilityV20CRS1,
       "ciscoEntityCapabilityACSWV03R000": ciscoEntityCapabilityACSWV03R000,
       "ciscoEntityCapabilityIOSXRV3R4": ciscoEntityCapabilityIOSXRV3R4,
       "ciscoEntityCapc4710aceVA1R700": ciscoEntityCapc4710aceVA1R700,
       "ciscoEntityCapabilityGssV03R01": ciscoEntityCapabilityGssV03R01,
       "ciscoEntityCapNxOSV06R0202PN7k": ciscoEntityCapNxOSV06R0202PN7k,
       "ciscoEntityCapNxOSV06R0201PMds": ciscoEntityCapNxOSV06R0201PMds}
)
