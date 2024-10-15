# SNMP MIB module (CISCO-DS1-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DS1-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:03 2024
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

ciscoDs1Capability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 273)
)
ciscoDs1Capability.setRevisions(
        ("2007-10-31 00:00",
         "2007-09-10 00:00",
         "2007-05-11 00:00",
         "2006-06-16 00:00",
         "2005-07-11 00:00",
         "2003-12-22 00:00",
         "2002-04-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoDs1AxsmeCapabilityV3R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 273, 1)
)
if mibBuilder.loadTexts:
    ciscoDs1AxsmeCapabilityV3R00.setProductRelease("MGX8850 Release 3.0")
if mibBuilder.loadTexts:
    ciscoDs1AxsmeCapabilityV3R00.setStatus(
        "current"
    )

ciscoDs1CapabilityV5R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 273, 2)
)
if mibBuilder.loadTexts:
    ciscoDs1CapabilityV5R00.setProductRelease("MGX8850 Release 5.0.0")
if mibBuilder.loadTexts:
    ciscoDs1CapabilityV5R00.setStatus(
        "current"
    )

ciscoDs1CapabilityV5R100 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 273, 3)
)
if mibBuilder.loadTexts:
    ciscoDs1CapabilityV5R100.setProductRelease("MGX8880 Release 5.1.0")
if mibBuilder.loadTexts:
    ciscoDs1CapabilityV5R100.setStatus(
        "current"
    )

ciscoDs1CapabilityV5R310 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 273, 4)
)
if mibBuilder.loadTexts:
    ciscoDs1CapabilityV5R310.setProductRelease("MGX8880 Release 5.3.1")
if mibBuilder.loadTexts:
    ciscoDs1CapabilityV5R310.setStatus(
        "current"
    )

ciscoDs1CapabilityMARsV12R5T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 273, 6)
)
if mibBuilder.loadTexts:
    ciscoDs1CapabilityMARsV12R5T.setProductRelease("IOS 12.5T for Cisco Access Routers and ISRs")
if mibBuilder.loadTexts:
    ciscoDs1CapabilityMARsV12R5T.setStatus(
        "current"
    )

ciscoDs1CapabilityAS5xxxV12R5T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 273, 7)
)
if mibBuilder.loadTexts:
    ciscoDs1CapabilityAS5xxxV12R5T.setProductRelease("IOS 12.5T for Cisco Access Servers")
if mibBuilder.loadTexts:
    ciscoDs1CapabilityAS5xxxV12R5T.setStatus(
        "current"
    )

ciscoDs1CapabilityV5R500 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 273, 8)
)
if mibBuilder.loadTexts:
    ciscoDs1CapabilityV5R500.setProductRelease("MGX8880 Release 5.5.0")
if mibBuilder.loadTexts:
    ciscoDs1CapabilityV5R500.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DS1-CAPABILITY",
    **{"ciscoDs1Capability": ciscoDs1Capability,
       "ciscoDs1AxsmeCapabilityV3R00": ciscoDs1AxsmeCapabilityV3R00,
       "ciscoDs1CapabilityV5R00": ciscoDs1CapabilityV5R00,
       "ciscoDs1CapabilityV5R100": ciscoDs1CapabilityV5R100,
       "ciscoDs1CapabilityV5R310": ciscoDs1CapabilityV5R310,
       "ciscoDs1CapabilityMARsV12R5T": ciscoDs1CapabilityMARsV12R5T,
       "ciscoDs1CapabilityAS5xxxV12R5T": ciscoDs1CapabilityAS5xxxV12R5T,
       "ciscoDs1CapabilityV5R500": ciscoDs1CapabilityV5R500}
)
