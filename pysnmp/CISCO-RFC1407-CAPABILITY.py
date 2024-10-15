# SNMP MIB module (CISCO-RFC1407-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RFC1407-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:35 2024
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

ciscoRFC1407Capability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 102)
)
ciscoRFC1407Capability.setRevisions(
        ("2001-08-17 00:00",
         "1996-06-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoRFC1407CapabilityV11R02 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 102, 1)
)
if mibBuilder.loadTexts:
    ciscoRFC1407CapabilityV11R02.setProductRelease("Cisco IOS 11.2")
if mibBuilder.loadTexts:
    ciscoRFC1407CapabilityV11R02.setStatus(
        "current"
    )

ciscoRFC1407CapabilityV122R12 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 102, 2)
)
if mibBuilder.loadTexts:
    ciscoRFC1407CapabilityV122R12.setProductRelease("Cisco IOS 12.2(12)T")
if mibBuilder.loadTexts:
    ciscoRFC1407CapabilityV122R12.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RFC1407-CAPABILITY",
    **{"ciscoRFC1407Capability": ciscoRFC1407Capability,
       "ciscoRFC1407CapabilityV11R02": ciscoRFC1407CapabilityV11R02,
       "ciscoRFC1407CapabilityV122R12": ciscoRFC1407CapabilityV122R12}
)
