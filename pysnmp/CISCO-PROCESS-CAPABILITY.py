# SNMP MIB module (CISCO-PROCESS-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PROCESS-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:07 2024
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

ciscoProcessCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 256)
)
ciscoProcessCapability.setRevisions(
        ("2013-08-29 00:00",
         "2009-03-18 00:00",
         "2008-09-15 00:00",
         "2007-11-27 00:00",
         "2007-11-22 00:00",
         "2006-03-22 00:00",
         "2006-02-21 00:00",
         "2005-12-12 00:00",
         "2004-11-05 00:00",
         "2003-08-06 00:00",
         "2001-11-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoProcessCapabilityV12R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 1)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilityV12R00.setProductRelease("Cisco IOS 12.0S")
if mibBuilder.loadTexts:
    ciscoProcessCapabilityV12R00.setStatus(
        "current"
    )

ciscoProcessCapabilityV12R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 2)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilityV12R01.setProductRelease("Cisco IOS 12.1")
if mibBuilder.loadTexts:
    ciscoProcessCapabilityV12R01.setStatus(
        "current"
    )

ciscoProcessCapabilityV12R02 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 3)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilityV12R02.setProductRelease("Cisco IOS 12.2")
if mibBuilder.loadTexts:
    ciscoProcessCapabilityV12R02.setStatus(
        "current"
    )

ciscoProcessCapCatOSV07R0201 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 4)
)
if mibBuilder.loadTexts:
    ciscoProcessCapCatOSV07R0201.setProductRelease("Cisco CatOS 7.2(1)")
if mibBuilder.loadTexts:
    ciscoProcessCapCatOSV07R0201.setStatus(
        "current"
    )

ciscoProcessCapabilityV12R02S = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 5)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilityV12R02S.setProductRelease("Cisco IOS 12.2S")
if mibBuilder.loadTexts:
    ciscoProcessCapabilityV12R02S.setStatus(
        "current"
    )

ciscoProcessCapabilityV12R03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 6)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilityV12R03.setProductRelease("Cisco IOS 12.3")
if mibBuilder.loadTexts:
    ciscoProcessCapabilityV12R03.setStatus(
        "current"
    )

ciscoProcessCapabilityV12R03T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 7)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilityV12R03T.setProductRelease("Cisco IOS 12.3T")
if mibBuilder.loadTexts:
    ciscoProcessCapabilityV12R03T.setStatus(
        "current"
    )

ciscoProcessCapabilitySAN3R0001 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 8)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilitySAN3R0001.setProductRelease("SAN-OS 3.0(1)")
if mibBuilder.loadTexts:
    ciscoProcessCapabilitySAN3R0001.setStatus(
        "current"
    )

ciscoProcessCapabilityACSWV03R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 9)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilityACSWV03R000.setProductRelease("ACSW (Application Control Software) 3.0")
if mibBuilder.loadTexts:
    ciscoProcessCapabilityACSWV03R000.setStatus(
        "current"
    )

ciscoProcessCapIOSXRV2R0CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 10)
)
if mibBuilder.loadTexts:
    ciscoProcessCapIOSXRV2R0CRS1.setProductRelease("Cisco IOS XR 2.0 for CRS-1")
if mibBuilder.loadTexts:
    ciscoProcessCapIOSXRV2R0CRS1.setStatus(
        "current"
    )

ciscoProcessCapc4710aceVA1R700 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 11)
)
if mibBuilder.loadTexts:
    ciscoProcessCapc4710aceVA1R700.setProductRelease("""\
ACSW (Application Control Software) A1(7)
                for ACE 4710 Application Control Engine 
                Appliance""")
if mibBuilder.loadTexts:
    ciscoProcessCapc4710aceVA1R700.setStatus(
        "current"
    )

ciscoProcessCapabilityIONV12R02SXH33 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 12)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilityIONV12R02SXH33.setProductRelease("Modular IOS(ION) 12.2SXH33")
if mibBuilder.loadTexts:
    ciscoProcessCapabilityIONV12R02SXH33.setStatus(
        "current"
    )

ciscoProcessCapabilityIOSV12R02SXH33 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 13)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilityIOSV12R02SXH33.setProductRelease("Cisco IOS 12.2SXH33")
if mibBuilder.loadTexts:
    ciscoProcessCapabilityIOSV12R02SXH33.setStatus(
        "current"
    )

ciscoProcessCapabilityGssV03R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 14)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilityGssV03R00.setProductRelease("Global Site Selector(GSS) 3.0")
if mibBuilder.loadTexts:
    ciscoProcessCapabilityGssV03R00.setStatus(
        "current"
    )

ciscoProcessCapabilityGssV03R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 15)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilityGssV03R01.setProductRelease("Global Site Selector(GSS) 3.1(0)")
if mibBuilder.loadTexts:
    ciscoProcessCapabilityGssV03R01.setStatus(
        "current"
    )

ciscoProcessCapabilityWAASV05R03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 256, 16)
)
if mibBuilder.loadTexts:
    ciscoProcessCapabilityWAASV05R03.setProductRelease("""\
OS=WAAS
                     OSVERSION=5.3.0""")
if mibBuilder.loadTexts:
    ciscoProcessCapabilityWAASV05R03.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PROCESS-CAPABILITY",
    **{"ciscoProcessCapability": ciscoProcessCapability,
       "ciscoProcessCapabilityV12R00": ciscoProcessCapabilityV12R00,
       "ciscoProcessCapabilityV12R01": ciscoProcessCapabilityV12R01,
       "ciscoProcessCapabilityV12R02": ciscoProcessCapabilityV12R02,
       "ciscoProcessCapCatOSV07R0201": ciscoProcessCapCatOSV07R0201,
       "ciscoProcessCapabilityV12R02S": ciscoProcessCapabilityV12R02S,
       "ciscoProcessCapabilityV12R03": ciscoProcessCapabilityV12R03,
       "ciscoProcessCapabilityV12R03T": ciscoProcessCapabilityV12R03T,
       "ciscoProcessCapabilitySAN3R0001": ciscoProcessCapabilitySAN3R0001,
       "ciscoProcessCapabilityACSWV03R000": ciscoProcessCapabilityACSWV03R000,
       "ciscoProcessCapIOSXRV2R0CRS1": ciscoProcessCapIOSXRV2R0CRS1,
       "ciscoProcessCapc4710aceVA1R700": ciscoProcessCapc4710aceVA1R700,
       "ciscoProcessCapabilityIONV12R02SXH33": ciscoProcessCapabilityIONV12R02SXH33,
       "ciscoProcessCapabilityIOSV12R02SXH33": ciscoProcessCapabilityIOSV12R02SXH33,
       "ciscoProcessCapabilityGssV03R00": ciscoProcessCapabilityGssV03R00,
       "ciscoProcessCapabilityGssV03R01": ciscoProcessCapabilityGssV03R01,
       "ciscoProcessCapabilityWAASV05R03": ciscoProcessCapabilityWAASV05R03}
)
