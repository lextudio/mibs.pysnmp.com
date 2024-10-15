# SNMP MIB module (CISCO-IMA-EXT-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IMA-EXT-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:23 2024
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

(MilliSeconds,) = mibBuilder.importSymbols(
    "IMA-MIB",
    "MilliSeconds")

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

ciscoImaExtCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 524)
)
ciscoImaExtCapability.setRevisions(
        ("2006-11-24 00:00",
         "2006-09-26 00:00",
         "2002-03-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoImaExtAxsmeCapabilityV3R0 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 524, 1)
)
if mibBuilder.loadTexts:
    ciscoImaExtAxsmeCapabilityV3R0.setProductRelease("MGX8850 Release 3.0")
if mibBuilder.loadTexts:
    ciscoImaExtAxsmeCapabilityV3R0.setStatus(
        "current"
    )

ciscoImaExtAxsmeCapabilityV5R320 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 524, 2)
)
if mibBuilder.loadTexts:
    ciscoImaExtAxsmeCapabilityV5R320.setProductRelease("MGX8850 Release 5.3.20")
if mibBuilder.loadTexts:
    ciscoImaExtAxsmeCapabilityV5R320.setStatus(
        "current"
    )

ciscoImaExtCapabilityV5R320 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 524, 3)
)
if mibBuilder.loadTexts:
    ciscoImaExtCapabilityV5R320.setProductRelease("MGX8950  and MGX8850 Release 5.3.20")
if mibBuilder.loadTexts:
    ciscoImaExtCapabilityV5R320.setStatus(
        "current"
    )

ciscoImaExtCapabilityV12R05 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 524, 4)
)
if mibBuilder.loadTexts:
    ciscoImaExtCapabilityV12R05.setProductRelease("IOS 12.5 for Cisco Access Routers and ISRs")
if mibBuilder.loadTexts:
    ciscoImaExtCapabilityV12R05.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IMA-EXT-CAPABILITY",
    **{"ciscoImaExtCapability": ciscoImaExtCapability,
       "ciscoImaExtAxsmeCapabilityV3R0": ciscoImaExtAxsmeCapabilityV3R0,
       "ciscoImaExtAxsmeCapabilityV5R320": ciscoImaExtAxsmeCapabilityV5R320,
       "ciscoImaExtCapabilityV5R320": ciscoImaExtCapabilityV5R320,
       "ciscoImaExtCapabilityV12R05": ciscoImaExtCapabilityV12R05}
)
