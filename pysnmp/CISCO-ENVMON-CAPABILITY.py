# SNMP MIB module (CISCO-ENVMON-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENVMON-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:47 2024
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

ciscoEnvMonCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 33)
)
ciscoEnvMonCapability.setRevisions(
        ("2009-12-16 00:00",
         "2009-01-05 00:00",
         "2007-05-18 00:00",
         "2006-12-12 00:00",
         "2006-07-19 00:00",
         "2006-04-19 00:00",
         "2004-12-16 01:00",
         "2004-03-26 00:00",
         "1996-11-12 00:00",
         "1995-01-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoEnvMonCapabilityV10R03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 1)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapabilityV10R03.setProductRelease("Cisco IOS 10.3")
if mibBuilder.loadTexts:
    ciscoEnvMonCapabilityV10R03.setStatus(
        "obsolete"
    )

ciscoEnvMonCapabilityV11R02 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 2)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapabilityV11R02.setProductRelease("Cisco IOS 11.2 on mid-range platforms C3600.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapabilityV11R02.setStatus(
        "current"
    )

ciscoEnvMonCapCatOSV08R0101Cat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 3)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapCatOSV08R0101Cat6k.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                          and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoEnvMonCapCatOSV08R0101Cat6k.setStatus(
        "current"
    )

ciscoEnvMonCapCatOSV08R0101Cat4k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 4)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapCatOSV08R0101Cat4k.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 4000/4500
                          series devices.""")
if mibBuilder.loadTexts:
    ciscoEnvMonCapCatOSV08R0101Cat4k.setStatus(
        "current"
    )

ciscoEnvMonCapV12R0119ECat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 5)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R0119ECat6K.setProductRelease("""\
Cisco IOS 12.1(19E) on Catalyst 6000/6500
                       and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R0119ECat6K.setStatus(
        "current"
    )

ciscoEnvMonCapV12R04TP37xx = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 6)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TP37xx.setProductRelease("Cisco IOS 12.4T on c37xx devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TP37xx.setStatus(
        "current"
    )

ciscoEnvMonCapV12R04TP28xx = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 7)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TP28xx.setProductRelease("Cisco IOS 12.4T on c28xx devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TP28xx.setStatus(
        "current"
    )

ciscoEnvMonCapV12R04TP26xx = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 8)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TP26xx.setProductRelease("Cisco IOS 12.4T on c26xx devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TP26xx.setStatus(
        "current"
    )

ciscoEnvMonCapV12R04TPIAD243x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 9)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TPIAD243x.setProductRelease("Cisco IOS 12.4T on IAD243x devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TPIAD243x.setStatus(
        "current"
    )

ciscoEnvMonCapV12R04TPVG224 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 10)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TPVG224.setProductRelease("Cisco IOS 12.4T on VG224 devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TPVG224.setStatus(
        "current"
    )

ciscoEnvMonCapV12R04TP3825 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 11)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TP3825.setProductRelease("Cisco IOS 12.4T on c3825 devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TP3825.setStatus(
        "current"
    )

ciscoEnvMonCapV12R04TP3845 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 12)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TP3845.setProductRelease("Cisco IOS 12.4T on c3845 devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TP3845.setStatus(
        "current"
    )

ciscoEnvMonCapV12R04TP2691 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 13)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TP2691.setProductRelease("Cisco IOS 12.4T on c2691 devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R04TP2691.setStatus(
        "current"
    )

ciscoEnvMonCapV12R05TPMARS = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 14)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TPMARS.setProductRelease("Cisco IOS 12.5T on MARS devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TPMARS.setStatus(
        "current"
    )

ciscoEnvMonCapV12R05TP180x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 15)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP180x.setProductRelease("Cisco IOS 12.5T on 180x PCBU devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP180x.setStatus(
        "current"
    )

ciscoEnvMonCapV12R05TP181x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 16)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP181x.setProductRelease("Cisco IOS 12.5T on 181x PCBU devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP181x.setStatus(
        "current"
    )

ciscoEnvMonCapV12R05TP1841 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 17)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP1841.setProductRelease("Cisco IOS 12.5T on 1841 & 2801 PCBU devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP1841.setStatus(
        "obsolete"
    )

ciscoEnvMonCapV12R05TP28xx = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 18)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP28xx.setProductRelease("Cisco IOS 12.5T on c28xx devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP28xx.setStatus(
        "current"
    )

ciscoEnvMonCapV12R05TP3825 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 19)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP3825.setProductRelease("Cisco IOS 12.5T on c3825 devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP3825.setStatus(
        "current"
    )

ciscoEnvMonCapV12R05TP3845 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 20)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP3845.setProductRelease("Cisco IOS 12.5T on c3845 devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP3845.setStatus(
        "current"
    )

ciscoEnvMonCapV12R05TP1841Rev1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 21)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP1841Rev1.setProductRelease("Cisco IOS 12.5T on 1841 and 2801 PCBU devices.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapV12R05TP1841Rev1.setStatus(
        "current"
    )

ciscoEnvMonCapabilityCTSV140 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 22)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapabilityCTSV140.setProductRelease("Cisco TelePresence System (CTS) 1.4.0.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapabilityCTSV140.setStatus(
        "current"
    )

ciscoEnvMonCapabilityWLCV70 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 33, 23)
)
if mibBuilder.loadTexts:
    ciscoEnvMonCapabilityWLCV70.setProductRelease("Cisco Wireless LAN Controller version 7.0.")
if mibBuilder.loadTexts:
    ciscoEnvMonCapabilityWLCV70.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENVMON-CAPABILITY",
    **{"ciscoEnvMonCapability": ciscoEnvMonCapability,
       "ciscoEnvMonCapabilityV10R03": ciscoEnvMonCapabilityV10R03,
       "ciscoEnvMonCapabilityV11R02": ciscoEnvMonCapabilityV11R02,
       "ciscoEnvMonCapCatOSV08R0101Cat6k": ciscoEnvMonCapCatOSV08R0101Cat6k,
       "ciscoEnvMonCapCatOSV08R0101Cat4k": ciscoEnvMonCapCatOSV08R0101Cat4k,
       "ciscoEnvMonCapV12R0119ECat6K": ciscoEnvMonCapV12R0119ECat6K,
       "ciscoEnvMonCapV12R04TP37xx": ciscoEnvMonCapV12R04TP37xx,
       "ciscoEnvMonCapV12R04TP28xx": ciscoEnvMonCapV12R04TP28xx,
       "ciscoEnvMonCapV12R04TP26xx": ciscoEnvMonCapV12R04TP26xx,
       "ciscoEnvMonCapV12R04TPIAD243x": ciscoEnvMonCapV12R04TPIAD243x,
       "ciscoEnvMonCapV12R04TPVG224": ciscoEnvMonCapV12R04TPVG224,
       "ciscoEnvMonCapV12R04TP3825": ciscoEnvMonCapV12R04TP3825,
       "ciscoEnvMonCapV12R04TP3845": ciscoEnvMonCapV12R04TP3845,
       "ciscoEnvMonCapV12R04TP2691": ciscoEnvMonCapV12R04TP2691,
       "ciscoEnvMonCapV12R05TPMARS": ciscoEnvMonCapV12R05TPMARS,
       "ciscoEnvMonCapV12R05TP180x": ciscoEnvMonCapV12R05TP180x,
       "ciscoEnvMonCapV12R05TP181x": ciscoEnvMonCapV12R05TP181x,
       "ciscoEnvMonCapV12R05TP1841": ciscoEnvMonCapV12R05TP1841,
       "ciscoEnvMonCapV12R05TP28xx": ciscoEnvMonCapV12R05TP28xx,
       "ciscoEnvMonCapV12R05TP3825": ciscoEnvMonCapV12R05TP3825,
       "ciscoEnvMonCapV12R05TP3845": ciscoEnvMonCapV12R05TP3845,
       "ciscoEnvMonCapV12R05TP1841Rev1": ciscoEnvMonCapV12R05TP1841Rev1,
       "ciscoEnvMonCapabilityCTSV140": ciscoEnvMonCapabilityCTSV140,
       "ciscoEnvMonCapabilityWLCV70": ciscoEnvMonCapabilityWLCV70}
)
