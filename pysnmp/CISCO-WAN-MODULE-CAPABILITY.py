# SNMP MIB module (CISCO-WAN-MODULE-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-MODULE-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:08 2024
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

(ciscoWanAgentCapability,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWanAgentCapability")

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

ciscoWanModuleCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 160, 99999)
)
ciscoWanModuleCapability.setRevisions(
        ("2002-03-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoWanModuleCapabilityV2R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 351, 160, 99999, 1)
)
if mibBuilder.loadTexts:
    ciscoWanModuleCapabilityV2R00.setProductRelease("MGX8850 Release 2.0.00")
if mibBuilder.loadTexts:
    ciscoWanModuleCapabilityV2R00.setStatus(
        "current"
    )

ciscoWanModuleCapabilityV21R60 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 351, 160, 99999, 2)
)
if mibBuilder.loadTexts:
    ciscoWanModuleCapabilityV21R60.setProductRelease("MGX8850 Release 2.1.60")
if mibBuilder.loadTexts:
    ciscoWanModuleCapabilityV21R60.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-MODULE-CAPABILITY",
    **{"ciscoWanModuleCapability": ciscoWanModuleCapability,
       "ciscoWanModuleCapabilityV2R00": ciscoWanModuleCapabilityV2R00,
       "ciscoWanModuleCapabilityV21R60": ciscoWanModuleCapabilityV21R60}
)
