# SNMP MIB module (CISCO-ITP-GSCCP-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-GSCCP-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:22 2024
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

ciscoGsccpCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 539)
)
ciscoGsccpCapability.setRevisions(
        ("2007-05-17 00:00",
         "2005-01-14 00:00",
         "2004-10-07 00:00",
         "2003-12-08 00:00",
         "2003-10-28 00:00",
         "2003-05-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoGsccpCapabilityV12R0204MB10 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 539, 1)
)
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R0204MB10.setProductRelease("Cisco IOS 12.2(4)MB10")
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R0204MB10.setStatus(
        "current"
    )

ciscoGsccpCapabilityV12R0204MB13 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 539, 2)
)
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R0204MB13.setProductRelease("Cisco IOS 12.2(4)MB13")
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R0204MB13.setStatus(
        "current"
    )

ciscoGsccpCapabilityV12R022004SW = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 539, 3)
)
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R022004SW.setProductRelease("Cisco IOS 12.2(20.4)SW")
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R022004SW.setStatus(
        "current"
    )

ciscoGsccpCapabilityV12R023000SW1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 539, 4)
)
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R023000SW1.setProductRelease("Cisco IOS 12.2(23)SW1")
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R023000SW1.setStatus(
        "current"
    )

ciscoGsccpCapabilityV12R025000SW1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 539, 5)
)
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R025000SW1.setProductRelease("Cisco IOS 12.2(25)SW1")
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R025000SW1.setStatus(
        "current"
    )

ciscoGsccpCapabilityV12R0218IXA = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 539, 6)
)
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R0218IXA.setProductRelease("Cisco IOS 12.2(18)IXA")
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R0218IXA.setStatus(
        "current"
    )

ciscoGsccpCapabilityV12R0411SW = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 539, 7)
)
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R0411SW.setProductRelease("Cisco IOS IOS 12.4(11)SW")
if mibBuilder.loadTexts:
    ciscoGsccpCapabilityV12R0411SW.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-GSCCP-CAPABILITY",
    **{"ciscoGsccpCapability": ciscoGsccpCapability,
       "ciscoGsccpCapabilityV12R0204MB10": ciscoGsccpCapabilityV12R0204MB10,
       "ciscoGsccpCapabilityV12R0204MB13": ciscoGsccpCapabilityV12R0204MB13,
       "ciscoGsccpCapabilityV12R022004SW": ciscoGsccpCapabilityV12R022004SW,
       "ciscoGsccpCapabilityV12R023000SW1": ciscoGsccpCapabilityV12R023000SW1,
       "ciscoGsccpCapabilityV12R025000SW1": ciscoGsccpCapabilityV12R025000SW1,
       "ciscoGsccpCapabilityV12R0218IXA": ciscoGsccpCapabilityV12R0218IXA,
       "ciscoGsccpCapabilityV12R0411SW": ciscoGsccpCapabilityV12R0411SW}
)
