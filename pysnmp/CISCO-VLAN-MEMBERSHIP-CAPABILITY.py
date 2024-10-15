# SNMP MIB module (CISCO-VLAN-MEMBERSHIP-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VLAN-MEMBERSHIP-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:06 2024
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

ciscoVlanMembershipCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 316)
)
ciscoVlanMembershipCapability.setRevisions(
        ("2010-10-29 00:00",
         "2010-03-21 00:00",
         "2007-07-12 00:00",
         "2004-01-15 00:00",
         "2003-09-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cVlanMembershipCapV12R0119ECat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 316, 1)
)
if mibBuilder.loadTexts:
    cVlanMembershipCapV12R0119ECat6K.setProductRelease("""\
Cisco IOS 12.1(19E) on Catalyst 6000/6500
                        and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cVlanMembershipCapV12R0119ECat6K.setStatus(
        "current"
    )

cVlanMembershipCapV12R0217SXCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 316, 2)
)
if mibBuilder.loadTexts:
    cVlanMembershipCapV12R0217SXCat6K.setProductRelease("""\
Cisco IOS 12.2(17SX) on Catalyst 6000/6500
                        and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cVlanMembershipCapV12R0217SXCat6K.setStatus(
        "current"
    )

ciscoVlanMembershipCapCatOSV08R0101 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 316, 3)
)
if mibBuilder.loadTexts:
    ciscoVlanMembershipCapCatOSV08R0101.setProductRelease("Cisco CatOS 8.1(1).")
if mibBuilder.loadTexts:
    ciscoVlanMembershipCapCatOSV08R0101.setStatus(
        "current"
    )

ciscoVlanMembershipCapCatOSV08R0201 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 316, 4)
)
if mibBuilder.loadTexts:
    ciscoVlanMembershipCapCatOSV08R0201.setProductRelease("Cisco CatOS 8.2(1).")
if mibBuilder.loadTexts:
    ciscoVlanMembershipCapCatOSV08R0201.setStatus(
        "current"
    )

cVlanMembershipCapCatOSV08R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 316, 5)
)
if mibBuilder.loadTexts:
    cVlanMembershipCapCatOSV08R0301.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500
                        and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cVlanMembershipCapCatOSV08R0301.setStatus(
        "current"
    )

cVlanMemberCapV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 316, 6)
)
if mibBuilder.loadTexts:
    cVlanMemberCapV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                        and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cVlanMemberCapV12R0233SXHPCat6K.setStatus(
        "current"
    )

cVlanMemberCapV12R0233SXI4PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 316, 7)
)
if mibBuilder.loadTexts:
    cVlanMemberCapV12R0233SXI4PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 
                    6000/6500 series devices.""")
if mibBuilder.loadTexts:
    cVlanMemberCapV12R0233SXI4PCat6K.setStatus(
        "current"
    )

cVlanMemberCapV12R0250SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 316, 8)
)
if mibBuilder.loadTexts:
    cVlanMemberCapV12R0250SYPCat6K.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 
                    6000/6500 series devices.""")
if mibBuilder.loadTexts:
    cVlanMemberCapV12R0250SYPCat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VLAN-MEMBERSHIP-CAPABILITY",
    **{"ciscoVlanMembershipCapability": ciscoVlanMembershipCapability,
       "cVlanMembershipCapV12R0119ECat6K": cVlanMembershipCapV12R0119ECat6K,
       "cVlanMembershipCapV12R0217SXCat6K": cVlanMembershipCapV12R0217SXCat6K,
       "ciscoVlanMembershipCapCatOSV08R0101": ciscoVlanMembershipCapCatOSV08R0101,
       "ciscoVlanMembershipCapCatOSV08R0201": ciscoVlanMembershipCapCatOSV08R0201,
       "cVlanMembershipCapCatOSV08R0301": cVlanMembershipCapCatOSV08R0301,
       "cVlanMemberCapV12R0233SXHPCat6K": cVlanMemberCapV12R0233SXHPCat6K,
       "cVlanMemberCapV12R0233SXI4PCat6K": cVlanMemberCapV12R0233SXI4PCat6K,
       "cVlanMemberCapV12R0250SYPCat6K": cVlanMemberCapV12R0250SYPCat6K}
)
