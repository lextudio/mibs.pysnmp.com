# SNMP MIB module (CISCO-ITP-GSP-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-GSP-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:23 2024
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

ciscoGspCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 306)
)
ciscoGspCapability.setRevisions(
        ("2007-07-16 00:00",
         "2006-01-06 00:00",
         "2003-10-15 00:00",
         "2003-07-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoGspCapabilityV12R0204MB10 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 306, 1)
)
if mibBuilder.loadTexts:
    ciscoGspCapabilityV12R0204MB10.setProductRelease("Cisco IOS 12.2(4)MB10")
if mibBuilder.loadTexts:
    ciscoGspCapabilityV12R0204MB10.setStatus(
        "current"
    )

ciscoGspCapabilityV12R0219SW = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 306, 2)
)
if mibBuilder.loadTexts:
    ciscoGspCapabilityV12R0219SW.setProductRelease("Cisco IOS 12.2(19)SW")
if mibBuilder.loadTexts:
    ciscoGspCapabilityV12R0219SW.setStatus(
        "current"
    )

ciscoGspCapabilityV12R0225SW3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 306, 3)
)
if mibBuilder.loadTexts:
    ciscoGspCapabilityV12R0225SW3.setProductRelease("Cisco IOS 12.2(25)SW3")
if mibBuilder.loadTexts:
    ciscoGspCapabilityV12R0225SW3.setStatus(
        "current"
    )

ciscoGspCapabilityV12R0218IXA = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 306, 4)
)
if mibBuilder.loadTexts:
    ciscoGspCapabilityV12R0218IXA.setProductRelease("Cisco IOS 12.2(18)IXA")
if mibBuilder.loadTexts:
    ciscoGspCapabilityV12R0218IXA.setStatus(
        "current"
    )

ciscoGspCapabilityV12R0411SW = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 306, 5)
)
if mibBuilder.loadTexts:
    ciscoGspCapabilityV12R0411SW.setProductRelease("Cisco IOS 12.4(11)SW")
if mibBuilder.loadTexts:
    ciscoGspCapabilityV12R0411SW.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-GSP-CAPABILITY",
    **{"ciscoGspCapability": ciscoGspCapability,
       "ciscoGspCapabilityV12R0204MB10": ciscoGspCapabilityV12R0204MB10,
       "ciscoGspCapabilityV12R0219SW": ciscoGspCapabilityV12R0219SW,
       "ciscoGspCapabilityV12R0225SW3": ciscoGspCapabilityV12R0225SW3,
       "ciscoGspCapabilityV12R0218IXA": ciscoGspCapabilityV12R0218IXA,
       "ciscoGspCapabilityV12R0411SW": ciscoGspCapabilityV12R0411SW}
)
