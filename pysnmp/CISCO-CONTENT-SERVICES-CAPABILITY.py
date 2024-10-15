# SNMP MIB module (CISCO-CONTENT-SERVICES-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CONTENT-SERVICES-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:44 2024
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

ciscoContentServicesCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 581)
)
ciscoContentServicesCapability.setRevisions(
        ("2010-12-23 00:00",
         "2010-02-11 00:00",
         "2009-08-21 00:00",
         "2009-05-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoContentServicesCapabilityAdcV01R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 581, 1)
)
if mibBuilder.loadTexts:
    ciscoContentServicesCapabilityAdcV01R00.setProductRelease("Cisco IOS 12.4MF")
if mibBuilder.loadTexts:
    ciscoContentServicesCapabilityAdcV01R00.setStatus(
        "current"
    )

ciscoContentServicesCapabilityCSG2R03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 581, 2)
)
if mibBuilder.loadTexts:
    ciscoContentServicesCapabilityCSG2R03.setProductRelease("Cisco IOS 12.4(22)MD")
if mibBuilder.loadTexts:
    ciscoContentServicesCapabilityCSG2R03.setStatus(
        "current"
    )

ciscoContentServicesCapabilityCSG2R0305 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 581, 3)
)
if mibBuilder.loadTexts:
    ciscoContentServicesCapabilityCSG2R0305.setProductRelease("Cisco IOS 12.4(22)MDA")
if mibBuilder.loadTexts:
    ciscoContentServicesCapabilityCSG2R0305.setStatus(
        "current"
    )

ciscoContentServicesCapabilityCSG2R04 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 581, 4)
)
if mibBuilder.loadTexts:
    ciscoContentServicesCapabilityCSG2R04.setProductRelease("Cisco IOS 12.4(24)MD")
if mibBuilder.loadTexts:
    ciscoContentServicesCapabilityCSG2R04.setStatus(
        "current"
    )

ciscoContentServicesCapabilityCSG2R06 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 581, 5)
)
if mibBuilder.loadTexts:
    ciscoContentServicesCapabilityCSG2R06.setProductRelease("Cisco IOS R6")
if mibBuilder.loadTexts:
    ciscoContentServicesCapabilityCSG2R06.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CONTENT-SERVICES-CAPABILITY",
    **{"ciscoContentServicesCapability": ciscoContentServicesCapability,
       "ciscoContentServicesCapabilityAdcV01R00": ciscoContentServicesCapabilityAdcV01R00,
       "ciscoContentServicesCapabilityCSG2R03": ciscoContentServicesCapabilityCSG2R03,
       "ciscoContentServicesCapabilityCSG2R0305": ciscoContentServicesCapabilityCSG2R0305,
       "ciscoContentServicesCapabilityCSG2R04": ciscoContentServicesCapabilityCSG2R04,
       "ciscoContentServicesCapabilityCSG2R06": ciscoContentServicesCapabilityCSG2R06}
)
