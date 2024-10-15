# SNMP MIB module (CISCO-CDP-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDP-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:13 2024
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

ciscoCdpCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 43)
)
ciscoCdpCapability.setRevisions(
        ("2007-07-18 00:00",
         "2006-10-26 00:00",
         "2006-02-06 00:00",
         "2005-05-24 00:00",
         "2003-09-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoCdpCapV12R0111bEXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 43, 1)
)
if mibBuilder.loadTexts:
    ciscoCdpCapV12R0111bEXCat6K.setProductRelease("""\
Cisco IOS 12.1(11b)EX on Catalyst 6000/6500

                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoCdpCapV12R0111bEXCat6K.setStatus(
        "current"
    )

ciscoCdpCapV12R0217SXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 43, 2)
)
if mibBuilder.loadTexts:
    ciscoCdpCapV12R0217SXCat6K.setProductRelease("""\
Cisco IOS 12.2(17)SX on Catalyst 6000/6500

                     and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoCdpCapV12R0217SXCat6K.setStatus(
        "current"
    )

ciscoCdpCapCatOSV08R0101Cat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 43, 3)
)
if mibBuilder.loadTexts:
    ciscoCdpCapCatOSV08R0101Cat6K.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500

                     and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoCdpCapCatOSV08R0101Cat6K.setStatus(
        "current"
    )

ciscoCdpCapCatOSV08R0101Cat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 43, 4)
)
if mibBuilder.loadTexts:
    ciscoCdpCapCatOSV08R0101Cat4K.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 4000 series

                     devices.""")
if mibBuilder.loadTexts:
    ciscoCdpCapCatOSV08R0101Cat4K.setStatus(
        "current"
    )

ciscoCdpCapSanOSV03R0001 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 43, 5)
)
if mibBuilder.loadTexts:
    ciscoCdpCapSanOSV03R0001.setProductRelease("Cisco SAN-OS 3.0(1) on MDS platform.")
if mibBuilder.loadTexts:
    ciscoCdpCapSanOSV03R0001.setStatus(
        "current"
    )

ciscoCdpCapIOSXRV2R0CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 43, 6)
)
if mibBuilder.loadTexts:
    ciscoCdpCapIOSXRV2R0CRS1.setProductRelease("Cisco IOS XR 2.0 for CRS-1")
if mibBuilder.loadTexts:
    ciscoCdpCapIOSXRV2R0CRS1.setStatus(
        "current"
    )

ciscoCdpCapCTSV100 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 43, 7)
)
if mibBuilder.loadTexts:
    ciscoCdpCapCTSV100.setProductRelease("Cisco TelePresence System (CTS) 1.0.0.")
if mibBuilder.loadTexts:
    ciscoCdpCapCTSV100.setStatus(
        "current"
    )

ciscoCdpCapCTMV1000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 43, 8)
)
if mibBuilder.loadTexts:
    ciscoCdpCapCTMV1000.setProductRelease("Cisco TelePresence Manager (CTM) 1.0.0.0.")
if mibBuilder.loadTexts:
    ciscoCdpCapCTMV1000.setStatus(
        "current"
    )

ciscoCdpCapV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 43, 9)
)
if mibBuilder.loadTexts:
    ciscoCdpCapV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500 
                    series devices.""")
if mibBuilder.loadTexts:
    ciscoCdpCapV12R0233SXHPCat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDP-CAPABILITY",
    **{"ciscoCdpCapability": ciscoCdpCapability,
       "ciscoCdpCapV12R0111bEXCat6K": ciscoCdpCapV12R0111bEXCat6K,
       "ciscoCdpCapV12R0217SXCat6K": ciscoCdpCapV12R0217SXCat6K,
       "ciscoCdpCapCatOSV08R0101Cat6K": ciscoCdpCapCatOSV08R0101Cat6K,
       "ciscoCdpCapCatOSV08R0101Cat4K": ciscoCdpCapCatOSV08R0101Cat4K,
       "ciscoCdpCapSanOSV03R0001": ciscoCdpCapSanOSV03R0001,
       "ciscoCdpCapIOSXRV2R0CRS1": ciscoCdpCapIOSXRV2R0CRS1,
       "ciscoCdpCapCTSV100": ciscoCdpCapCTSV100,
       "ciscoCdpCapCTMV1000": ciscoCdpCapCTMV1000,
       "ciscoCdpCapV12R0233SXHPCat6K": ciscoCdpCapV12R0233SXHPCat6K}
)
