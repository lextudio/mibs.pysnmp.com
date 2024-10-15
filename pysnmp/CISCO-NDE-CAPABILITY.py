# SNMP MIB module (CISCO-NDE-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NDE-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:04 2024
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

ciscoNdeCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 328)
)
ciscoNdeCapability.setRevisions(
        ("2010-11-04 00:00",
         "2004-01-27 00:00",
         "2003-08-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoNdeCapabilityV12R0119E = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 328, 1)
)
if mibBuilder.loadTexts:
    ciscoNdeCapabilityV12R0119E.setProductRelease("""\
Cisco IOS 12.1(19E) on Catalyst 6000/6500 
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoNdeCapabilityV12R0119E.setStatus(
        "current"
    )

ciscoNdeCapCatOSV08R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 328, 2)
)
if mibBuilder.loadTexts:
    ciscoNdeCapCatOSV08R0301.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500 
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoNdeCapCatOSV08R0301.setStatus(
        "current"
    )

ciscoNdeCapV12R0250SYPCat6kPfc4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 328, 3)
)
if mibBuilder.loadTexts:
    ciscoNdeCapV12R0250SYPCat6kPfc4.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500 
                    series devices with PFC4 card.""")
if mibBuilder.loadTexts:
    ciscoNdeCapV12R0250SYPCat6kPfc4.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NDE-CAPABILITY",
    **{"ciscoNdeCapability": ciscoNdeCapability,
       "ciscoNdeCapabilityV12R0119E": ciscoNdeCapabilityV12R0119E,
       "ciscoNdeCapCatOSV08R0301": ciscoNdeCapCatOSV08R0301,
       "ciscoNdeCapV12R0250SYPCat6kPfc4": ciscoNdeCapV12R0250SYPCat6kPfc4}
)
