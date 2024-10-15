# SNMP MIB module (CISCO-ATM-VIRTUAL-IF-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-VIRTUAL-IF-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:08 2024
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

ciscoAtmVirtualIfCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 279)
)
ciscoAtmVirtualIfCapability.setRevisions(
        ("2005-11-14 00:00",
         "2003-09-10 00:00",
         "2003-03-24 00:00",
         "2002-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cavIfCapabilityAxsmV2R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 279, 1)
)
if mibBuilder.loadTexts:
    cavIfCapabilityAxsmV2R00.setProductRelease("MGX8850 Release 2.00")
if mibBuilder.loadTexts:
    cavIfCapabilityAxsmV2R00.setStatus(
        "current"
    )

cavIfCapabilityAxsmV2R0010 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 279, 2)
)
if mibBuilder.loadTexts:
    cavIfCapabilityAxsmV2R0010.setProductRelease("MGX8850 Release 2.0.10")
if mibBuilder.loadTexts:
    cavIfCapabilityAxsmV2R0010.setStatus(
        "current"
    )

cavIfCapabilityAxsmeV2R0160 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 279, 3)
)
if mibBuilder.loadTexts:
    cavIfCapabilityAxsmeV2R0160.setProductRelease("MGX8850 Release 2.1.60")
if mibBuilder.loadTexts:
    cavIfCapabilityAxsmeV2R0160.setStatus(
        "current"
    )

cavIfCapabilityV4R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 279, 4)
)
if mibBuilder.loadTexts:
    cavIfCapabilityV4R00.setProductRelease("MGX8950, MGX8850 Release 4.00.00")
if mibBuilder.loadTexts:
    cavIfCapabilityV4R00.setStatus(
        "current"
    )

cavIfCapabilityV5R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 279, 5)
)
if mibBuilder.loadTexts:
    cavIfCapabilityV5R00.setProductRelease("MGX8950, MGX8850 Release 5.00.00")
if mibBuilder.loadTexts:
    cavIfCapabilityV5R00.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-VIRTUAL-IF-CAPABILITY",
    **{"ciscoAtmVirtualIfCapability": ciscoAtmVirtualIfCapability,
       "cavIfCapabilityAxsmV2R00": cavIfCapabilityAxsmV2R00,
       "cavIfCapabilityAxsmV2R0010": cavIfCapabilityAxsmV2R0010,
       "cavIfCapabilityAxsmeV2R0160": cavIfCapabilityAxsmeV2R0160,
       "cavIfCapabilityV4R00": cavIfCapabilityV4R00,
       "cavIfCapabilityV5R00": cavIfCapabilityV5R00}
)
