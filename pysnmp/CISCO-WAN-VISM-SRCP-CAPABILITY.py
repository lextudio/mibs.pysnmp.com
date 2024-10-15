# SNMP MIB module (CISCO-WAN-VISM-SRCP-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-VISM-SRCP-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:28 2024
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

ciscoWanVismSrcpCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 160, 321)
)
ciscoWanVismSrcpCapability.setRevisions(
        ("2000-07-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoWanVismSrcpCapabilityV2R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 351, 160, 321, 1)
)
if mibBuilder.loadTexts:
    ciscoWanVismSrcpCapabilityV2R00.setProductRelease("VISM Release1.5,VISM Release2.0")
if mibBuilder.loadTexts:
    ciscoWanVismSrcpCapabilityV2R00.setStatus(
        "current"
    )

ciscoWanVismSrcpCapabilityV2R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 351, 160, 321, 2)
)
if mibBuilder.loadTexts:
    ciscoWanVismSrcpCapabilityV2R01.setProductRelease("VISM release 2.0.3")
if mibBuilder.loadTexts:
    ciscoWanVismSrcpCapabilityV2R01.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-VISM-SRCP-CAPABILITY",
    **{"ciscoWanVismSrcpCapability": ciscoWanVismSrcpCapability,
       "ciscoWanVismSrcpCapabilityV2R00": ciscoWanVismSrcpCapabilityV2R00,
       "ciscoWanVismSrcpCapabilityV2R01": ciscoWanVismSrcpCapabilityV2R01}
)
