# SNMP MIB module (CISCO-IGMP-SNOOPING-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IGMP-SNOOPING-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:16 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoIgmpSnoopingCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 320)
)
ciscoIgmpSnoopingCapability.setRevisions(
        ("2012-09-12 00:00",
         "2010-11-16 00:00",
         "2008-10-31 00:00",
         "2004-03-10 00:00",
         "2003-08-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cisCapCatOSV08R0101Cat6kPfc = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 320, 1)
)
if mibBuilder.loadTexts:
    cisCapCatOSV08R0101Cat6kPfc.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500
                         and Cisco 7600 series devices with PFC card.""")
if mibBuilder.loadTexts:
    cisCapCatOSV08R0101Cat6kPfc.setStatus(
        "current"
    )

cisCapCatOSV08R0101Cat6kPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 320, 2)
)
if mibBuilder.loadTexts:
    cisCapCatOSV08R0101Cat6kPfc2.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500 and
                         Cisco 7600 series devices with PFC2 card.""")
if mibBuilder.loadTexts:
    cisCapCatOSV08R0101Cat6kPfc2.setStatus(
        "current"
    )

cisCapCatOSV08R0101Cat6kPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 320, 3)
)
if mibBuilder.loadTexts:
    cisCapCatOSV08R0101Cat6kPfc3.setProductRelease("""\
Cisco CatOS 8.1(1) on Catalyst 6000/6500 and
                         Cisco 7600 series devices with PFC3 card.""")
if mibBuilder.loadTexts:
    cisCapCatOSV08R0101Cat6kPfc3.setStatus(
        "current"
    )

cisCapCatOSV08R0301Cat6kPfc2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 320, 4)
)
if mibBuilder.loadTexts:
    cisCapCatOSV08R0301Cat6kPfc2.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500 and
                         Cisco 7600 series devices with PFC2 card.""")
if mibBuilder.loadTexts:
    cisCapCatOSV08R0301Cat6kPfc2.setStatus(
        "current"
    )

cisCapCatOSV08R0301Cat6kPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 320, 5)
)
if mibBuilder.loadTexts:
    cisCapCatOSV08R0301Cat6kPfc3.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500 and
                         Cisco 7600 series devices with PFC3 card.""")
if mibBuilder.loadTexts:
    cisCapCatOSV08R0301Cat6kPfc3.setStatus(
        "current"
    )

cisCapV12R0233SXIPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 320, 6)
)
if mibBuilder.loadTexts:
    cisCapV12R0233SXIPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cisCapV12R0233SXIPCat6K.setStatus(
        "current"
    )

cisCapV12R0250SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 320, 7)
)
if mibBuilder.loadTexts:
    cisCapV12R0250SYPCat6K.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                    series devices.""")
if mibBuilder.loadTexts:
    cisCapV12R0250SYPCat6K.setStatus(
        "current"
    )

cisCapV15R0101SYPCat6kPfc3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 320, 8)
)
if mibBuilder.loadTexts:
    cisCapV15R0101SYPCat6kPfc3.setProductRelease("""\
Cisco IOS 15.1(1)SY on Catalyst 6000/6500
                    series devices with PFC3 card.""")
if mibBuilder.loadTexts:
    cisCapV15R0101SYPCat6kPfc3.setStatus(
        "current"
    )

cisCapV15R0101SYPCat6kPfc4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 320, 9)
)
if mibBuilder.loadTexts:
    cisCapV15R0101SYPCat6kPfc4.setProductRelease("""\
Cisco IOS 15.1(1)SY on Catalyst 6000/6500
                    series devices with PFC4 card.""")
if mibBuilder.loadTexts:
    cisCapV15R0101SYPCat6kPfc4.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IGMP-SNOOPING-CAPABILITY",
    **{"ciscoIgmpSnoopingCapability": ciscoIgmpSnoopingCapability,
       "cisCapCatOSV08R0101Cat6kPfc": cisCapCatOSV08R0101Cat6kPfc,
       "cisCapCatOSV08R0101Cat6kPfc2": cisCapCatOSV08R0101Cat6kPfc2,
       "cisCapCatOSV08R0101Cat6kPfc3": cisCapCatOSV08R0101Cat6kPfc3,
       "cisCapCatOSV08R0301Cat6kPfc2": cisCapCatOSV08R0301Cat6kPfc2,
       "cisCapCatOSV08R0301Cat6kPfc3": cisCapCatOSV08R0301Cat6kPfc3,
       "cisCapV12R0233SXIPCat6K": cisCapV12R0233SXIPCat6K,
       "cisCapV12R0250SYPCat6K": cisCapV12R0250SYPCat6K,
       "cisCapV15R0101SYPCat6kPfc3": cisCapV15R0101SYPCat6kPfc3,
       "cisCapV15R0101SYPCat6kPfc4": cisCapV15R0101SYPCat6kPfc4}
)
