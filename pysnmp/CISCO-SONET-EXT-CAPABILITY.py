# SNMP MIB module (CISCO-SONET-EXT-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SONET-EXT-CAPABILITY
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

ciscoSonetExtCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 261)
)
ciscoSonetExtCapability.setRevisions(
        ("2003-12-23 00:00",
         "2003-03-13 00:00",
         "2002-02-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoSonetExtAxsmCapabilityV2R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 261, 1)
)
if mibBuilder.loadTexts:
    ciscoSonetExtAxsmCapabilityV2R00.setProductRelease("MGX8850 Release 2.0.00")
if mibBuilder.loadTexts:
    ciscoSonetExtAxsmCapabilityV2R00.setStatus(
        "current"
    )

ciscoSonetExtAxsmCapabilityV2R11 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 261, 2)
)
if mibBuilder.loadTexts:
    ciscoSonetExtAxsmCapabilityV2R11.setProductRelease("MGX8850 Release 2.0.11")
if mibBuilder.loadTexts:
    ciscoSonetExtAxsmCapabilityV2R11.setStatus(
        "current"
    )

ciscoSonetExtAxsmeCapabilityV21R60 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 261, 3)
)
if mibBuilder.loadTexts:
    ciscoSonetExtAxsmeCapabilityV21R60.setProductRelease("MGX8850 Release 2.1.60.")
if mibBuilder.loadTexts:
    ciscoSonetExtAxsmeCapabilityV21R60.setStatus(
        "current"
    )

ciscoSonetExtSrmeCapabilityV3R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 261, 4)
)
if mibBuilder.loadTexts:
    ciscoSonetExtSrmeCapabilityV3R00.setProductRelease("MGX8800 Release 3.0")
if mibBuilder.loadTexts:
    ciscoSonetExtSrmeCapabilityV3R00.setStatus(
        "current"
    )

ciscoSonetExtCapabilityV4R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 261, 5)
)
if mibBuilder.loadTexts:
    ciscoSonetExtCapabilityV4R00.setProductRelease("MGX8850, MGX8950 Release 4.0.00.")
if mibBuilder.loadTexts:
    ciscoSonetExtCapabilityV4R00.setStatus(
        "current"
    )

ciscoSonetExtCapabilityV5R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 261, 6)
)
if mibBuilder.loadTexts:
    ciscoSonetExtCapabilityV5R00.setProductRelease("MGX8850 Release 5.0.0")
if mibBuilder.loadTexts:
    ciscoSonetExtCapabilityV5R00.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SONET-EXT-CAPABILITY",
    **{"ciscoSonetExtCapability": ciscoSonetExtCapability,
       "ciscoSonetExtAxsmCapabilityV2R00": ciscoSonetExtAxsmCapabilityV2R00,
       "ciscoSonetExtAxsmCapabilityV2R11": ciscoSonetExtAxsmCapabilityV2R11,
       "ciscoSonetExtAxsmeCapabilityV21R60": ciscoSonetExtAxsmeCapabilityV21R60,
       "ciscoSonetExtSrmeCapabilityV3R00": ciscoSonetExtSrmeCapabilityV3R00,
       "ciscoSonetExtCapabilityV4R00": ciscoSonetExtCapabilityV4R00,
       "ciscoSonetExtCapabilityV5R00": ciscoSonetExtCapabilityV5R00}
)
