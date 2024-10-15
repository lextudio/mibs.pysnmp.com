# SNMP MIB module (CISCO-ENHANCED-MEMPOOL-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENHANCED-MEMPOOL-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:24 2024
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

cempCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 462)
)
cempCapability.setRevisions(
        ("2011-09-21 00:00",
         "2011-01-31 00:00",
         "2010-10-28 00:00",
         "2009-08-21 00:00",
         "2009-04-23 00:00",
         "2007-05-09 00:00",
         "2005-12-29 00:00",
         "2005-10-26 00:00",
         "2005-01-27 00:00",
         "2004-10-01 00:00",
         "2004-06-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cempCapabilityV12R03T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 1)
)
if mibBuilder.loadTexts:
    cempCapabilityV12R03T.setProductRelease("Cisco IOS 12.3T")
if mibBuilder.loadTexts:
    cempCapabilityV12R03T.setStatus(
        "current"
    )

cempCapabilityV12R03TP5000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 2)
)
if mibBuilder.loadTexts:
    cempCapabilityV12R03TP5000.setProductRelease("""\
Cisco IOS 12.3T for AS5350, AS5400 and AS5850
                        platforms""")
if mibBuilder.loadTexts:
    cempCapabilityV12R03TP5000.setStatus(
        "current"
    )

cempCapabilityV12R04TP37xx = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 3)
)
if mibBuilder.loadTexts:
    cempCapabilityV12R04TP37xx.setProductRelease("""\
Cisco IOS 12.4T for c3725 and c3745
                        platforms""")
if mibBuilder.loadTexts:
    cempCapabilityV12R04TP37xx.setStatus(
        "current"
    )

cempCapabilityV12R04TP26xx = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 4)
)
if mibBuilder.loadTexts:
    cempCapabilityV12R04TP26xx.setProductRelease("""\
Cisco IOS 12.4T for c26xx and c2691
                        platforms""")
if mibBuilder.loadTexts:
    cempCapabilityV12R04TP26xx.setStatus(
        "current"
    )

cempCapabilityV12R04TP38xx = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 5)
)
if mibBuilder.loadTexts:
    cempCapabilityV12R04TP38xx.setProductRelease("""\
Cisco IOS 12.4T for c3825 and c3845
                        platforms""")
if mibBuilder.loadTexts:
    cempCapabilityV12R04TP38xx.setStatus(
        "current"
    )

cempCapabilityV12R04TP28xx = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 6)
)
if mibBuilder.loadTexts:
    cempCapabilityV12R04TP28xx.setProductRelease("Cisco IOS 12.4T for c28xx platforms")
if mibBuilder.loadTexts:
    cempCapabilityV12R04TP28xx.setStatus(
        "current"
    )

cempCapabilityV12R04TPVG224 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 7)
)
if mibBuilder.loadTexts:
    cempCapabilityV12R04TPVG224.setProductRelease("Cisco IOS 12.4T for VG224 platforms")
if mibBuilder.loadTexts:
    cempCapabilityV12R04TPVG224.setStatus(
        "current"
    )

cempCapabilityV12R04TPIAD243x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 8)
)
if mibBuilder.loadTexts:
    cempCapabilityV12R04TPIAD243x.setProductRelease("Cisco IOS 12.4T for IAD243x platforms")
if mibBuilder.loadTexts:
    cempCapabilityV12R04TPIAD243x.setStatus(
        "current"
    )

cempCapabilityIOSXRV2R0CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 9)
)
if mibBuilder.loadTexts:
    cempCapabilityIOSXRV2R0CRS1.setProductRelease("Cisco IOS XR 2.0 for CRS-1")
if mibBuilder.loadTexts:
    cempCapabilityIOSXRV2R0CRS1.setStatus(
        "current"
    )

cempCapabilityCatOSV08R0601 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 10)
)
if mibBuilder.loadTexts:
    cempCapabilityCatOSV08R0601.setProductRelease("Cisco CatOS 8.6(1).")
if mibBuilder.loadTexts:
    cempCapabilityCatOSV08R0601.setStatus(
        "current"
    )

cempCapabilityV12R05TP184x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 11)
)
if mibBuilder.loadTexts:
    cempCapabilityV12R05TP184x.setProductRelease("Cisco IOS 12.5T for 184x platforms")
if mibBuilder.loadTexts:
    cempCapabilityV12R05TP184x.setStatus(
        "current"
    )

cempCapabilityV12R05TP2801 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 12)
)
if mibBuilder.loadTexts:
    cempCapabilityV12R05TP2801.setProductRelease("Cisco IOS 12.5T for the 2801 platform")
if mibBuilder.loadTexts:
    cempCapabilityV12R05TP2801.setStatus(
        "current"
    )

cempCapabilityNXOS501 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 13)
)
if mibBuilder.loadTexts:
    cempCapabilityNXOS501.setProductRelease("Cisco MDS & Nexus NX-OS 5.0 and above")
if mibBuilder.loadTexts:
    cempCapabilityNXOS501.setStatus(
        "current"
    )

cempCapabilityNXOSV05R0201 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 14)
)
if mibBuilder.loadTexts:
    cempCapabilityNXOSV05R0201.setProductRelease("Cisco Nexus NX-OS 5.2(1).")
if mibBuilder.loadTexts:
    cempCapabilityNXOSV05R0201.setStatus(
        "current"
    )

cempCapabilityASA = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 15)
)
if mibBuilder.loadTexts:
    cempCapabilityASA.setProductRelease("8.4.x")
if mibBuilder.loadTexts:
    cempCapabilityASA.setStatus(
        "current"
    )

cempCapabilityNXOSV06R0001 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 462, 16)
)
if mibBuilder.loadTexts:
    cempCapabilityNXOSV06R0001.setProductRelease("Cisco Nexus NX-OS 6.0(1).")
if mibBuilder.loadTexts:
    cempCapabilityNXOSV06R0001.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENHANCED-MEMPOOL-CAPABILITY",
    **{"cempCapability": cempCapability,
       "cempCapabilityV12R03T": cempCapabilityV12R03T,
       "cempCapabilityV12R03TP5000": cempCapabilityV12R03TP5000,
       "cempCapabilityV12R04TP37xx": cempCapabilityV12R04TP37xx,
       "cempCapabilityV12R04TP26xx": cempCapabilityV12R04TP26xx,
       "cempCapabilityV12R04TP38xx": cempCapabilityV12R04TP38xx,
       "cempCapabilityV12R04TP28xx": cempCapabilityV12R04TP28xx,
       "cempCapabilityV12R04TPVG224": cempCapabilityV12R04TPVG224,
       "cempCapabilityV12R04TPIAD243x": cempCapabilityV12R04TPIAD243x,
       "cempCapabilityIOSXRV2R0CRS1": cempCapabilityIOSXRV2R0CRS1,
       "cempCapabilityCatOSV08R0601": cempCapabilityCatOSV08R0601,
       "cempCapabilityV12R05TP184x": cempCapabilityV12R05TP184x,
       "cempCapabilityV12R05TP2801": cempCapabilityV12R05TP2801,
       "cempCapabilityNXOS501": cempCapabilityNXOS501,
       "cempCapabilityNXOSV05R0201": cempCapabilityNXOSV05R0201,
       "cempCapabilityASA": cempCapabilityASA,
       "cempCapabilityNXOSV06R0001": cempCapabilityNXOSV06R0001}
)
