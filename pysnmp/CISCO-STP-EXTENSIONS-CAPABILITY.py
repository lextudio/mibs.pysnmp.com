# SNMP MIB module (CISCO-STP-EXTENSIONS-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-STP-EXTENSIONS-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:55 2024
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

ciscoStpExtensionsCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 360)
)
ciscoStpExtensionsCapability.setRevisions(
        ("2014-03-27 00:00",
         "2013-09-30 00:00",
         "2011-09-30 00:00",
         "2007-02-23 00:00",
         "2005-09-15 00:00",
         "2005-06-15 00:00",
         "2004-11-20 00:00",
         "2004-06-02 00:00",
         "2004-04-02 00:00",
         "2004-01-21 00:00",
         "2003-09-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cstpxCapCatOSV08R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 1)
)
if mibBuilder.loadTexts:
    cstpxCapCatOSV08R0101.setProductRelease("Cisco CatOS 8.1(1).")
if mibBuilder.loadTexts:
    cstpxCapCatOSV08R0101.setStatus(
        "current"
    )

cstpxCapV12R0113E = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 2)
)
if mibBuilder.loadTexts:
    cstpxCapV12R0113E.setProductRelease("""\
Cisco IOS 12.1(13)E on Catalyst 6000/6500
                        and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cstpxCapV12R0113E.setStatus(
        "current"
    )

cstpxCapV12R0214SX = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 3)
)
if mibBuilder.loadTexts:
    cstpxCapV12R0214SX.setProductRelease("""\
Cisco IOS 12.2(14)SX on Catalyst 6000/6500
                        and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cstpxCapV12R0214SX.setStatus(
        "current"
    )

cstpxCapCatOSV08R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 4)
)
if mibBuilder.loadTexts:
    cstpxCapCatOSV08R0301.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                        and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cstpxCapCatOSV08R0301.setStatus(
        "current"
    )

cstpxCapV12R0217bSXACat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 5)
)
if mibBuilder.loadTexts:
    cstpxCapV12R0217bSXACat6k.setProductRelease("""\
Cisco IOS 12.2(17b)SXA on Catalyst 6000/6500
                        and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cstpxCapV12R0217bSXACat6k.setStatus(
        "current"
    )

cstpxCapCatOSV08R0401 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 6)
)
if mibBuilder.loadTexts:
    cstpxCapCatOSV08R0401.setProductRelease("""\
Cisco CatOS 8.4(1) on Catalyst 6000/6500
                        and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cstpxCapCatOSV08R0401.setStatus(
        "current"
    )

cstpxCapV12R0218SXEPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 7)
)
if mibBuilder.loadTexts:
    cstpxCapV12R0218SXEPCat6k.setProductRelease("""\
Cisco IOS 12.2(18)SXE on Catalyst 6000/6500
                        and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cstpxCapV12R0218SXEPCat6k.setStatus(
        "current"
    )

cstpxCapCatOSV08R0501 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 8)
)
if mibBuilder.loadTexts:
    cstpxCapCatOSV08R0501.setProductRelease("Cisco CatOS 8.5(1).")
if mibBuilder.loadTexts:
    cstpxCapCatOSV08R0501.setStatus(
        "current"
    )

cstpxCapV12R0218SXFPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 9)
)
if mibBuilder.loadTexts:
    cstpxCapV12R0218SXFPCat6k.setProductRelease("""\
Cisco IOS 12.2(18)SXF on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cstpxCapV12R0218SXFPCat6k.setStatus(
        "current"
    )

cstpxCapV15R0001SYPCat6kSup2T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 10)
)
if mibBuilder.loadTexts:
    cstpxCapV15R0001SYPCat6kSup2T.setProductRelease("""\
Cisco IOS 15.0(1)SY on Catalyst 6000/6500
                    series devices with Supervisor 2T present.""")
if mibBuilder.loadTexts:
    cstpxCapV15R0001SYPCat6kSup2T.setStatus(
        "current"
    )

cstpxCapV15R0102SYPCat6k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 11)
)
if mibBuilder.loadTexts:
    cstpxCapV15R0102SYPCat6k.setProductRelease("Cisco IOS 15.1(2)SY on Catalyst 6000/6500 series devices.")
if mibBuilder.loadTexts:
    cstpxCapV15R0102SYPCat6k.setStatus(
        "current"
    )

cstpxCapV15R0102SYPCat6kSup2T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 12)
)
if mibBuilder.loadTexts:
    cstpxCapV15R0102SYPCat6kSup2T.setProductRelease("""\
Cisco IOS 15.1(2)SY on Catalyst 6000/6500
                    series devices with Supervisor 2T present.""")
if mibBuilder.loadTexts:
    cstpxCapV15R0102SYPCat6kSup2T.setStatus(
        "current"
    )

cstpxCapNxOSV05R0201PN7k = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 360, 13)
)
if mibBuilder.loadTexts:
    cstpxCapNxOSV05R0201PN7k.setProductRelease("""\
Cisco NX-OS 5.2(1) on Nexus 7000
                    series devices.""")
if mibBuilder.loadTexts:
    cstpxCapNxOSV05R0201PN7k.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-STP-EXTENSIONS-CAPABILITY",
    **{"ciscoStpExtensionsCapability": ciscoStpExtensionsCapability,
       "cstpxCapCatOSV08R0101": cstpxCapCatOSV08R0101,
       "cstpxCapV12R0113E": cstpxCapV12R0113E,
       "cstpxCapV12R0214SX": cstpxCapV12R0214SX,
       "cstpxCapCatOSV08R0301": cstpxCapCatOSV08R0301,
       "cstpxCapV12R0217bSXACat6k": cstpxCapV12R0217bSXACat6k,
       "cstpxCapCatOSV08R0401": cstpxCapCatOSV08R0401,
       "cstpxCapV12R0218SXEPCat6k": cstpxCapV12R0218SXEPCat6k,
       "cstpxCapCatOSV08R0501": cstpxCapCatOSV08R0501,
       "cstpxCapV12R0218SXFPCat6k": cstpxCapV12R0218SXFPCat6k,
       "cstpxCapV15R0001SYPCat6kSup2T": cstpxCapV15R0001SYPCat6kSup2T,
       "cstpxCapV15R0102SYPCat6k": cstpxCapV15R0102SYPCat6k,
       "cstpxCapV15R0102SYPCat6kSup2T": cstpxCapV15R0102SYPCat6kSup2T,
       "cstpxCapNxOSV05R0201PN7k": cstpxCapNxOSV05R0201PN7k}
)
