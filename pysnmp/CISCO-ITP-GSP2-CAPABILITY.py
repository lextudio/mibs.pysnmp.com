# SNMP MIB module (CISCO-ITP-GSP2-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-GSP2-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:25 2024
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

ciscoGsp2Capability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 307)
)
ciscoGsp2Capability.setRevisions(
        ("2004-08-25 00:00",
         "2003-11-24 00:00",
         "2003-07-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoGsp2CapabilityV12R0204MB4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 307, 1)
)
if mibBuilder.loadTexts:
    ciscoGsp2CapabilityV12R0204MB4.setProductRelease("Cisco IOS 12.2(4)MB10")
if mibBuilder.loadTexts:
    ciscoGsp2CapabilityV12R0204MB4.setStatus(
        "current"
    )

ciscoGsp2CapabilityV12R022004SW = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 307, 2)
)
if mibBuilder.loadTexts:
    ciscoGsp2CapabilityV12R022004SW.setProductRelease("Cisco IOS 12.2(20.4)SW")
if mibBuilder.loadTexts:
    ciscoGsp2CapabilityV12R022004SW.setStatus(
        "current"
    )

ciscoGsp2CapabilityV12R022300SW1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 307, 3)
)
if mibBuilder.loadTexts:
    ciscoGsp2CapabilityV12R022300SW1.setProductRelease("Cisco IOS 12.2(23)SW1")
if mibBuilder.loadTexts:
    ciscoGsp2CapabilityV12R022300SW1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-GSP2-CAPABILITY",
    **{"ciscoGsp2Capability": ciscoGsp2Capability,
       "ciscoGsp2CapabilityV12R0204MB4": ciscoGsp2CapabilityV12R0204MB4,
       "ciscoGsp2CapabilityV12R022004SW": ciscoGsp2CapabilityV12R022004SW,
       "ciscoGsp2CapabilityV12R022300SW1": ciscoGsp2CapabilityV12R022300SW1}
)
