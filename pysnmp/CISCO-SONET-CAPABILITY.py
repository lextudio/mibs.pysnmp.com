# SNMP MIB module (CISCO-SONET-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SONET-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:40 2024
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

ciscoSonetCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 266)
)
ciscoSonetCapability.setRevisions(
        ("2004-02-19 00:00",
         "2003-03-11 00:00",
         "2002-03-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoSonetCapabilityAxsmV2R0100 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 266, 1)
)
if mibBuilder.loadTexts:
    ciscoSonetCapabilityAxsmV2R0100.setProductRelease("MGX8850 Release 2.1.00")
if mibBuilder.loadTexts:
    ciscoSonetCapabilityAxsmV2R0100.setStatus(
        "current"
    )

ciscoSonetCapabilitySrmeV3R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 266, 2)
)
if mibBuilder.loadTexts:
    ciscoSonetCapabilitySrmeV3R00.setProductRelease("MGX8850 Release 3.00")
if mibBuilder.loadTexts:
    ciscoSonetCapabilitySrmeV3R00.setStatus(
        "current"
    )

ciscoSonetCapabilityV4R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 266, 3)
)
if mibBuilder.loadTexts:
    ciscoSonetCapabilityV4R00.setProductRelease("MGX8950  and MGX8850 Release 4.0.00")
if mibBuilder.loadTexts:
    ciscoSonetCapabilityV4R00.setStatus(
        "current"
    )

ciscoSonetCapabilityV5R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 266, 4)
)
if mibBuilder.loadTexts:
    ciscoSonetCapabilityV5R00.setProductRelease("MGX8850 Release 5.0.0")
if mibBuilder.loadTexts:
    ciscoSonetCapabilityV5R00.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SONET-CAPABILITY",
    **{"ciscoSonetCapability": ciscoSonetCapability,
       "ciscoSonetCapabilityAxsmV2R0100": ciscoSonetCapabilityAxsmV2R0100,
       "ciscoSonetCapabilitySrmeV3R00": ciscoSonetCapabilitySrmeV3R00,
       "ciscoSonetCapabilityV4R00": ciscoSonetCapabilityV4R00,
       "ciscoSonetCapabilityV5R00": ciscoSonetCapabilityV5R00}
)
