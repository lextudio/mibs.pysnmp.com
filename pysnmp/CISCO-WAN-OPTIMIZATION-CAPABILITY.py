# SNMP MIB module (CISCO-WAN-OPTIMIZATION-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-OPTIMIZATION-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:11 2024
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

ciscoWanOptimizationCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 611)
)
ciscoWanOptimizationCapability.setRevisions(
        ("2015-11-09 00:00",
         "2015-10-05 00:00",
         "2012-06-23 00:00",
         "2012-06-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoWanOptimizationCapabilityWAASV4R4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 611, 1)
)
if mibBuilder.loadTexts:
    ciscoWanOptimizationCapabilityWAASV4R4.setProductRelease("""\
OS=WAAS
                     OSVERSION=V4R4""")
if mibBuilder.loadTexts:
    ciscoWanOptimizationCapabilityWAASV4R4.setStatus(
        "current"
    )

ciscoWanOptimizationCapabilityWAASV5R0 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 611, 2)
)
if mibBuilder.loadTexts:
    ciscoWanOptimizationCapabilityWAASV5R0.setProductRelease("""\
OS=WAAS
                     OSVERSION=V5R0""")
if mibBuilder.loadTexts:
    ciscoWanOptimizationCapabilityWAASV5R0.setStatus(
        "current"
    )

ciscoWanOptimizationCapabilityWAASV6R0 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 611, 3)
)
if mibBuilder.loadTexts:
    ciscoWanOptimizationCapabilityWAASV6R0.setProductRelease("""\
OS=WAAS
                     OSVERSION=V6R0""")
if mibBuilder.loadTexts:
    ciscoWanOptimizationCapabilityWAASV6R0.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-OPTIMIZATION-CAPABILITY",
    **{"ciscoWanOptimizationCapability": ciscoWanOptimizationCapability,
       "ciscoWanOptimizationCapabilityWAASV4R4": ciscoWanOptimizationCapabilityWAASV4R4,
       "ciscoWanOptimizationCapabilityWAASV5R0": ciscoWanOptimizationCapabilityWAASV5R0,
       "ciscoWanOptimizationCapabilityWAASV6R0": ciscoWanOptimizationCapabilityWAASV6R0}
)
