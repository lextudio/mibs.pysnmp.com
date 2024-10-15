# SNMP MIB module (CISCOSB-SENSORENTMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-SENSORENTMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:49 2024
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

(rlEnv,) = mibBuilder.importSymbols(
    "CISCOSB-HWENVIROMENT",
    "rlEnv")

(entPhysicalIndex,
 entityPhysicalGroup) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entityPhysicalGroup")

(EntitySensorValue,
 entPhySensorEntry) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "EntitySensorValue",
    "entPhySensorEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

rlSensor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 4)
)
rlSensor.setRevisions(
        ("2003-09-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlEntPhySensorTable_Object = MibTable
rlEntPhySensorTable = _RlEntPhySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 3)
)
if mibBuilder.loadTexts:
    rlEntPhySensorTable.setStatus("current")
_RlEntPhySensorEntry_Object = MibTableRow
rlEntPhySensorEntry = _RlEntPhySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 3, 1)
)
if mibBuilder.loadTexts:
    rlEntPhySensorEntry.setStatus("current")
_RlEnvPhySensorMinValue_Type = EntitySensorValue
_RlEnvPhySensorMinValue_Object = MibTableColumn
rlEnvPhySensorMinValue = _RlEnvPhySensorMinValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 3, 1, 1),
    _RlEnvPhySensorMinValue_Type()
)
rlEnvPhySensorMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvPhySensorMinValue.setStatus("current")
_RlEnvPhySensorMaxValue_Type = EntitySensorValue
_RlEnvPhySensorMaxValue_Object = MibTableColumn
rlEnvPhySensorMaxValue = _RlEnvPhySensorMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 3, 1, 2),
    _RlEnvPhySensorMaxValue_Type()
)
rlEnvPhySensorMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEnvPhySensorMaxValue.setStatus("current")
_RlEnvPhySensorTestValue_Type = EntitySensorValue
_RlEnvPhySensorTestValue_Object = MibTableColumn
rlEnvPhySensorTestValue = _RlEnvPhySensorTestValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 83, 3, 1, 3),
    _RlEnvPhySensorTestValue_Type()
)
rlEnvPhySensorTestValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEnvPhySensorTestValue.setStatus("current")
entPhySensorEntry.registerAugmentions(
    ("CISCOSB-SENSORENTMIB",
     "rlEntPhySensorEntry")
)
rlEntPhySensorEntry.setIndexNames(*entPhySensorEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-SENSORENTMIB",
    **{"rlEntPhySensorTable": rlEntPhySensorTable,
       "rlEntPhySensorEntry": rlEntPhySensorEntry,
       "rlEnvPhySensorMinValue": rlEnvPhySensorMinValue,
       "rlEnvPhySensorMaxValue": rlEnvPhySensorMaxValue,
       "rlEnvPhySensorTestValue": rlEnvPhySensorTestValue,
       "rlSensor": rlSensor}
)
