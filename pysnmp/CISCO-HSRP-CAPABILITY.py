# SNMP MIB module (CISCO-HSRP-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-HSRP-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:14 2024
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

ciscoHsrpCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 10000)
)
ciscoHsrpCapability.setRevisions(
        ("2007-11-27 00:00",
         "1998-08-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoHsrpCapabilityV12R0 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 10000, 1)
)
if mibBuilder.loadTexts:
    ciscoHsrpCapabilityV12R0.setProductRelease("Cisco IOS 12.0(3)T")
if mibBuilder.loadTexts:
    ciscoHsrpCapabilityV12R0.setStatus(
        "current"
    )

ciscoHsrpCapabilityV3R6CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 10000, 2)
)
if mibBuilder.loadTexts:
    ciscoHsrpCapabilityV3R6CRS1.setProductRelease("Cisco IOS XR 3.6 on CRS-1")
if mibBuilder.loadTexts:
    ciscoHsrpCapabilityV3R6CRS1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-HSRP-CAPABILITY",
    **{"ciscoHsrpCapability": ciscoHsrpCapability,
       "ciscoHsrpCapabilityV12R0": ciscoHsrpCapabilityV12R0,
       "ciscoHsrpCapabilityV3R6CRS1": ciscoHsrpCapabilityV3R6CRS1}
)
