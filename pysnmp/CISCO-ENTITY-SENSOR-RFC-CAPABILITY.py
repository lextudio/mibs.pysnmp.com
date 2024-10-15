# SNMP MIB module (CISCO-ENTITY-SENSOR-RFC-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-SENSOR-RFC-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:46 2024
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

ciscoEntitySensorRfcCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 430)
)
ciscoEntitySensorRfcCapability.setRevisions(
        ("2008-02-08 00:00",
         "2006-05-31 00:00",
         "2005-01-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cEntSensorRfcCapCatOSV08R0501 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 430, 1)
)
if mibBuilder.loadTexts:
    cEntSensorRfcCapCatOSV08R0501.setProductRelease("Cisco CatOS 8.5(1).")
if mibBuilder.loadTexts:
    cEntSensorRfcCapCatOSV08R0501.setStatus(
        "current"
    )

cEntSensorRfcCapACSWV03R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 430, 2)
)
if mibBuilder.loadTexts:
    cEntSensorRfcCapACSWV03R000.setProductRelease("""\
ACSW (Application Control Software) 3.0
                    for Application Control Engine(ACE) 
                    Service Module.""")
if mibBuilder.loadTexts:
    cEntSensorRfcCapACSWV03R000.setStatus(
        "current"
    )

cEntSensorRfcCapc4710aceVA1R70 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 430, 3)
)
if mibBuilder.loadTexts:
    cEntSensorRfcCapc4710aceVA1R70.setProductRelease("""\
ACSW (Application Control Software) A1(7)
                    for ACE 4710 Application Control Engine 
                    Appliance.""")
if mibBuilder.loadTexts:
    cEntSensorRfcCapc4710aceVA1R70.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-SENSOR-RFC-CAPABILITY",
    **{"ciscoEntitySensorRfcCapability": ciscoEntitySensorRfcCapability,
       "cEntSensorRfcCapCatOSV08R0501": cEntSensorRfcCapCatOSV08R0501,
       "cEntSensorRfcCapACSWV03R000": cEntSensorRfcCapACSWV03R000,
       "cEntSensorRfcCapc4710aceVA1R70": cEntSensorRfcCapc4710aceVA1R70}
)
