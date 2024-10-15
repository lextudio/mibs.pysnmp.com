# SNMP MIB module (CISCO-HOST-RESOURCES-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-HOST-RESOURCES-CAPABILITY
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

ciscoHostResourcesCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 547)
)
ciscoHostResourcesCapability.setRevisions(
        ("2007-10-04 00:00",
         "2007-09-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoHostResourcesCapabilityV12R04 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 547, 1)
)
if mibBuilder.loadTexts:
    ciscoHostResourcesCapabilityV12R04.setProductRelease("Cisco IOS 12.4")
if mibBuilder.loadTexts:
    ciscoHostResourcesCapabilityV12R04.setStatus(
        "current"
    )

ciscoHostResourcesCapabilityCTSV120 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 547, 2)
)
if mibBuilder.loadTexts:
    ciscoHostResourcesCapabilityCTSV120.setProductRelease("Cisco TelePresence System (CTS) 1.2.0.")
if mibBuilder.loadTexts:
    ciscoHostResourcesCapabilityCTSV120.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-HOST-RESOURCES-CAPABILITY",
    **{"ciscoHostResourcesCapability": ciscoHostResourcesCapability,
       "ciscoHostResourcesCapabilityV12R04": ciscoHostResourcesCapabilityV12R04,
       "ciscoHostResourcesCapabilityCTSV120": ciscoHostResourcesCapabilityCTSV120}
)
