# SNMP MIB module (CISCO-RADIUS-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RADIUS-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:26 2024
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

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoRadiusCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 399)
)
ciscoRadiusCapability.setRevisions(
        ("2008-05-21 00:00",
         "2007-01-17 00:00",
         "2004-06-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoRadiusCapCatOSV08R0401 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 399, 1)
)
if mibBuilder.loadTexts:
    ciscoRadiusCapCatOSV08R0401.setProductRelease("Cisco CatOS 8.4(1).")
if mibBuilder.loadTexts:
    ciscoRadiusCapCatOSV08R0401.setStatus(
        "current"
    )

ciscoRadiusCapCatOSV08R0601 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 399, 2)
)
if mibBuilder.loadTexts:
    ciscoRadiusCapCatOSV08R0601.setProductRelease("Cisco CatOS 8.6(1).")
if mibBuilder.loadTexts:
    ciscoRadiusCapCatOSV08R0601.setStatus(
        "current"
    )

ciscoRadiusCapCatOSV08R0701 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 399, 3)
)
if mibBuilder.loadTexts:
    ciscoRadiusCapCatOSV08R0701.setProductRelease("Cisco CatOS 8.7(1).")
if mibBuilder.loadTexts:
    ciscoRadiusCapCatOSV08R0701.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RADIUS-CAPABILITY",
    **{"ciscoRadiusCapability": ciscoRadiusCapability,
       "ciscoRadiusCapCatOSV08R0401": ciscoRadiusCapCatOSV08R0401,
       "ciscoRadiusCapCatOSV08R0601": ciscoRadiusCapCatOSV08R0601,
       "ciscoRadiusCapCatOSV08R0701": ciscoRadiusCapCatOSV08R0701}
)
