# SNMP MIB module (SENSOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SENSOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:22 2024
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

deviceSensorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SensorUnits(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 5),
          ("other", 1),
          ("rpm", 6),
          ("specialEnum", 3),
          ("truthvalue", 2),
          ("volts", 4))
    )



class SensorCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("fan-slow-critical", 14),
          ("fan-slow-warning", 13),
          ("fan-stopped", 15),
          ("no-power", 6),
          ("not-installed", 3),
          ("ok", 1),
          ("temperature-high-critical", 11),
          ("temperature-high-severe", 12),
          ("temperature-high-warning", 10),
          ("unknown", 2),
          ("voltage-high-critical", 8),
          ("voltage-high-severe", 9),
          ("voltage-high-warning", 7),
          ("voltage-low-critical", 5),
          ("voltage-low-warning", 4))
    )



class ExpBase10(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 24),
    )



class SensorValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )



class SensorStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonoperational", 3),
          ("ok", 1),
          ("unavailable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DeviceSensorMIBObjects_ObjectIdentity = ObjectIdentity
deviceSensorMIBObjects = _DeviceSensorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1)
)
_DeviceSensorValues_ObjectIdentity = ObjectIdentity
deviceSensorValues = _DeviceSensorValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1)
)
_DeviceSensorValueTable_Object = MibTable
deviceSensorValueTable = _DeviceSensorValueTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    deviceSensorValueTable.setStatus("current")
_DeviceSensorValueEntry_Object = MibTableRow
deviceSensorValueEntry = _DeviceSensorValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1)
)
deviceSensorValueEntry.setIndexNames(
    (0, "SENSOR-MIB", "deviceSensorIndex"),
)
if mibBuilder.loadTexts:
    deviceSensorValueEntry.setStatus("current")


class _DeviceSensorIndex_Type(Integer32):
    """Custom type deviceSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceSensorIndex_Type.__name__ = "Integer32"
_DeviceSensorIndex_Object = MibTableColumn
deviceSensorIndex = _DeviceSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 1),
    _DeviceSensorIndex_Type()
)
deviceSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceSensorIndex.setStatus("current")
_DeviceSensorTrapEnabled_Type = TruthValue
_DeviceSensorTrapEnabled_Object = MibTableColumn
deviceSensorTrapEnabled = _DeviceSensorTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 2),
    _DeviceSensorTrapEnabled_Type()
)
deviceSensorTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceSensorTrapEnabled.setStatus("current")
_DeviceSensorUnits_Type = SensorUnits
_DeviceSensorUnits_Object = MibTableColumn
deviceSensorUnits = _DeviceSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 3),
    _DeviceSensorUnits_Type()
)
deviceSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSensorUnits.setStatus("current")
_DeviceSensorScale_Type = ExpBase10
_DeviceSensorScale_Object = MibTableColumn
deviceSensorScale = _DeviceSensorScale_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 4),
    _DeviceSensorScale_Type()
)
deviceSensorScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSensorScale.setStatus("current")
_DeviceSensorValue_Type = SensorValue
_DeviceSensorValue_Object = MibTableColumn
deviceSensorValue = _DeviceSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 5),
    _DeviceSensorValue_Type()
)
deviceSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSensorValue.setStatus("current")
_DeviceSensorCode_Type = SensorCode
_DeviceSensorCode_Object = MibTableColumn
deviceSensorCode = _DeviceSensorCode_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 6),
    _DeviceSensorCode_Type()
)
deviceSensorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSensorCode.setStatus("current")
_DeviceSensorStatus_Type = SensorStatus
_DeviceSensorStatus_Object = MibTableColumn
deviceSensorStatus = _DeviceSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 7),
    _DeviceSensorStatus_Type()
)
deviceSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSensorStatus.setStatus("current")
_DeviceSensorTimeStamp_Type = TimeStamp
_DeviceSensorTimeStamp_Object = MibTableColumn
deviceSensorTimeStamp = _DeviceSensorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 8),
    _DeviceSensorTimeStamp_Type()
)
deviceSensorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSensorTimeStamp.setStatus("current")
_DeviceSensorName_Type = DisplayString
_DeviceSensorName_Object = MibTableColumn
deviceSensorName = _DeviceSensorName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 1, 1, 1, 1, 9),
    _DeviceSensorName_Type()
)
deviceSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSensorName.setStatus("current")
_DeviceSensorMIBNotifications_ObjectIdentity = ObjectIdentity
deviceSensorMIBNotifications = _DeviceSensorMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 2)
)
_DeviceSensorMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
deviceSensorMIBNotificationsPrefix = _DeviceSensorMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 2, 0)
)

# Managed Objects groups


# Notification objects

deviceSensorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 1, 2, 0, 1)
)
deviceSensorTrap.setObjects(
      *(("SENSOR-MIB", "deviceSensorName"),
        ("SENSOR-MIB", "deviceSensorValue"),
        ("SENSOR-MIB", "deviceSensorCode"))
)
if mibBuilder.loadTexts:
    deviceSensorTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SENSOR-MIB",
    **{"SensorUnits": SensorUnits,
       "SensorCode": SensorCode,
       "ExpBase10": ExpBase10,
       "SensorValue": SensorValue,
       "SensorStatus": SensorStatus,
       "deviceSensorMIB": deviceSensorMIB,
       "deviceSensorMIBObjects": deviceSensorMIBObjects,
       "deviceSensorValues": deviceSensorValues,
       "deviceSensorValueTable": deviceSensorValueTable,
       "deviceSensorValueEntry": deviceSensorValueEntry,
       "deviceSensorIndex": deviceSensorIndex,
       "deviceSensorTrapEnabled": deviceSensorTrapEnabled,
       "deviceSensorUnits": deviceSensorUnits,
       "deviceSensorScale": deviceSensorScale,
       "deviceSensorValue": deviceSensorValue,
       "deviceSensorCode": deviceSensorCode,
       "deviceSensorStatus": deviceSensorStatus,
       "deviceSensorTimeStamp": deviceSensorTimeStamp,
       "deviceSensorName": deviceSensorName,
       "deviceSensorMIBNotifications": deviceSensorMIBNotifications,
       "deviceSensorMIBNotificationsPrefix": deviceSensorMIBNotificationsPrefix,
       "deviceSensorTrap": deviceSensorTrap}
)
