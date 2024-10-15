# SNMP MIB module (BATTERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BATTERY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:47 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

batteryMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 233)
)
batteryMIB.setRevisions(
        ("2015-06-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BatteryNotifications_ObjectIdentity = ObjectIdentity
batteryNotifications = _BatteryNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 233, 0)
)
_BatteryObjects_ObjectIdentity = ObjectIdentity
batteryObjects = _BatteryObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 233, 1)
)
_BatteryTable_Object = MibTable
batteryTable = _BatteryTable_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1)
)
if mibBuilder.loadTexts:
    batteryTable.setStatus("current")
_BatteryEntry_Object = MibTableRow
batteryEntry = _BatteryEntry_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1)
)
batteryEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    batteryEntry.setStatus("current")
_BatteryIdentifier_Type = SnmpAdminString
_BatteryIdentifier_Object = MibTableColumn
batteryIdentifier = _BatteryIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 1),
    _BatteryIdentifier_Type()
)
batteryIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryIdentifier.setStatus("current")
_BatteryFirmwareVersion_Type = SnmpAdminString
_BatteryFirmwareVersion_Object = MibTableColumn
batteryFirmwareVersion = _BatteryFirmwareVersion_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 2),
    _BatteryFirmwareVersion_Type()
)
batteryFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryFirmwareVersion.setStatus("current")


class _BatteryType_Type(Integer32):
    """Custom type batteryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("capacitor", 5),
          ("other", 2),
          ("primary", 3),
          ("rechargeable", 4),
          ("unknown", 1))
    )


_BatteryType_Type.__name__ = "Integer32"
_BatteryType_Object = MibTableColumn
batteryType = _BatteryType_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 3),
    _BatteryType_Type()
)
batteryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryType.setStatus("current")
_BatteryTechnology_Type = Unsigned32
_BatteryTechnology_Object = MibTableColumn
batteryTechnology = _BatteryTechnology_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 4),
    _BatteryTechnology_Type()
)
batteryTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTechnology.setStatus("current")
_BatteryDesignVoltage_Type = Unsigned32
_BatteryDesignVoltage_Object = MibTableColumn
batteryDesignVoltage = _BatteryDesignVoltage_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 5),
    _BatteryDesignVoltage_Type()
)
batteryDesignVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryDesignVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryDesignVoltage.setUnits("millivolt")
_BatteryNumberOfCells_Type = Unsigned32
_BatteryNumberOfCells_Object = MibTableColumn
batteryNumberOfCells = _BatteryNumberOfCells_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 6),
    _BatteryNumberOfCells_Type()
)
batteryNumberOfCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryNumberOfCells.setStatus("current")
_BatteryDesignCapacity_Type = Unsigned32
_BatteryDesignCapacity_Object = MibTableColumn
batteryDesignCapacity = _BatteryDesignCapacity_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 7),
    _BatteryDesignCapacity_Type()
)
batteryDesignCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryDesignCapacity.setStatus("current")
if mibBuilder.loadTexts:
    batteryDesignCapacity.setUnits("milliampere hours")
_BatteryMaxChargingCurrent_Type = Unsigned32
_BatteryMaxChargingCurrent_Object = MibTableColumn
batteryMaxChargingCurrent = _BatteryMaxChargingCurrent_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 8),
    _BatteryMaxChargingCurrent_Type()
)
batteryMaxChargingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMaxChargingCurrent.setStatus("current")
if mibBuilder.loadTexts:
    batteryMaxChargingCurrent.setUnits("milliampere")
_BatteryTrickleChargingCurrent_Type = Unsigned32
_BatteryTrickleChargingCurrent_Object = MibTableColumn
batteryTrickleChargingCurrent = _BatteryTrickleChargingCurrent_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 9),
    _BatteryTrickleChargingCurrent_Type()
)
batteryTrickleChargingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTrickleChargingCurrent.setStatus("current")
if mibBuilder.loadTexts:
    batteryTrickleChargingCurrent.setUnits("milliampere")
_BatteryActualCapacity_Type = Unsigned32
_BatteryActualCapacity_Object = MibTableColumn
batteryActualCapacity = _BatteryActualCapacity_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 10),
    _BatteryActualCapacity_Type()
)
batteryActualCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryActualCapacity.setStatus("current")
if mibBuilder.loadTexts:
    batteryActualCapacity.setUnits("milliampere hours")
_BatteryChargingCycleCount_Type = Unsigned32
_BatteryChargingCycleCount_Object = MibTableColumn
batteryChargingCycleCount = _BatteryChargingCycleCount_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 11),
    _BatteryChargingCycleCount_Type()
)
batteryChargingCycleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryChargingCycleCount.setStatus("current")
_BatteryLastChargingCycleTime_Type = DateAndTime
_BatteryLastChargingCycleTime_Object = MibTableColumn
batteryLastChargingCycleTime = _BatteryLastChargingCycleTime_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 12),
    _BatteryLastChargingCycleTime_Type()
)
batteryLastChargingCycleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryLastChargingCycleTime.setStatus("current")


class _BatteryChargingOperState_Type(Integer32):
    """Custom type batteryChargingOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("charging", 2),
          ("discharging", 5),
          ("maintainingCharge", 3),
          ("noCharging", 4),
          ("unknown", 1))
    )


_BatteryChargingOperState_Type.__name__ = "Integer32"
_BatteryChargingOperState_Object = MibTableColumn
batteryChargingOperState = _BatteryChargingOperState_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 13),
    _BatteryChargingOperState_Type()
)
batteryChargingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryChargingOperState.setStatus("current")


class _BatteryChargingAdminState_Type(Integer32):
    """Custom type batteryChargingAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("charge", 2),
          ("discharge", 4),
          ("doNotCharge", 3),
          ("notSet", 1))
    )


_BatteryChargingAdminState_Type.__name__ = "Integer32"
_BatteryChargingAdminState_Object = MibTableColumn
batteryChargingAdminState = _BatteryChargingAdminState_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 14),
    _BatteryChargingAdminState_Type()
)
batteryChargingAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryChargingAdminState.setStatus("current")
_BatteryActualCharge_Type = Unsigned32
_BatteryActualCharge_Object = MibTableColumn
batteryActualCharge = _BatteryActualCharge_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 15),
    _BatteryActualCharge_Type()
)
batteryActualCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryActualCharge.setStatus("current")
if mibBuilder.loadTexts:
    batteryActualCharge.setUnits("milliampere hours")
_BatteryActualVoltage_Type = Unsigned32
_BatteryActualVoltage_Object = MibTableColumn
batteryActualVoltage = _BatteryActualVoltage_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 16),
    _BatteryActualVoltage_Type()
)
batteryActualVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryActualVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryActualVoltage.setUnits("millivolt")
_BatteryActualCurrent_Type = Integer32
_BatteryActualCurrent_Object = MibTableColumn
batteryActualCurrent = _BatteryActualCurrent_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 17),
    _BatteryActualCurrent_Type()
)
batteryActualCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryActualCurrent.setStatus("current")
if mibBuilder.loadTexts:
    batteryActualCurrent.setUnits("milliampere")
_BatteryTemperature_Type = Integer32
_BatteryTemperature_Object = MibTableColumn
batteryTemperature = _BatteryTemperature_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 18),
    _BatteryTemperature_Type()
)
batteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperature.setStatus("current")
if mibBuilder.loadTexts:
    batteryTemperature.setUnits("deci-degrees Celsius")
_BatteryAlarmLowCharge_Type = Unsigned32
_BatteryAlarmLowCharge_Object = MibTableColumn
batteryAlarmLowCharge = _BatteryAlarmLowCharge_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 19),
    _BatteryAlarmLowCharge_Type()
)
batteryAlarmLowCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAlarmLowCharge.setStatus("current")
if mibBuilder.loadTexts:
    batteryAlarmLowCharge.setUnits("milliampere hours")
_BatteryAlarmLowVoltage_Type = Unsigned32
_BatteryAlarmLowVoltage_Object = MibTableColumn
batteryAlarmLowVoltage = _BatteryAlarmLowVoltage_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 20),
    _BatteryAlarmLowVoltage_Type()
)
batteryAlarmLowVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAlarmLowVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryAlarmLowVoltage.setUnits("millivolt")
_BatteryAlarmLowCapacity_Type = Unsigned32
_BatteryAlarmLowCapacity_Object = MibTableColumn
batteryAlarmLowCapacity = _BatteryAlarmLowCapacity_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 21),
    _BatteryAlarmLowCapacity_Type()
)
batteryAlarmLowCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAlarmLowCapacity.setStatus("current")
if mibBuilder.loadTexts:
    batteryAlarmLowCapacity.setUnits("milliampere hours")
_BatteryAlarmHighCycleCount_Type = Unsigned32
_BatteryAlarmHighCycleCount_Object = MibTableColumn
batteryAlarmHighCycleCount = _BatteryAlarmHighCycleCount_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 22),
    _BatteryAlarmHighCycleCount_Type()
)
batteryAlarmHighCycleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAlarmHighCycleCount.setStatus("current")
_BatteryAlarmHighTemperature_Type = Integer32
_BatteryAlarmHighTemperature_Object = MibTableColumn
batteryAlarmHighTemperature = _BatteryAlarmHighTemperature_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 23),
    _BatteryAlarmHighTemperature_Type()
)
batteryAlarmHighTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAlarmHighTemperature.setStatus("current")
if mibBuilder.loadTexts:
    batteryAlarmHighTemperature.setUnits("deci-degrees Celsius")
_BatteryAlarmLowTemperature_Type = Integer32
_BatteryAlarmLowTemperature_Object = MibTableColumn
batteryAlarmLowTemperature = _BatteryAlarmLowTemperature_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 24),
    _BatteryAlarmLowTemperature_Type()
)
batteryAlarmLowTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAlarmLowTemperature.setStatus("current")
if mibBuilder.loadTexts:
    batteryAlarmLowTemperature.setUnits("deci-degrees Celsius")
_BatteryCellIdentifier_Type = SnmpAdminString
_BatteryCellIdentifier_Object = MibTableColumn
batteryCellIdentifier = _BatteryCellIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 233, 1, 1, 1, 25),
    _BatteryCellIdentifier_Type()
)
batteryCellIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCellIdentifier.setStatus("current")
_BatteryConformance_ObjectIdentity = ObjectIdentity
batteryConformance = _BatteryConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 233, 2)
)
_BatteryCompliances_ObjectIdentity = ObjectIdentity
batteryCompliances = _BatteryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 233, 2, 1)
)
_BatteryGroups_ObjectIdentity = ObjectIdentity
batteryGroups = _BatteryGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 233, 2, 2)
)

# Managed Objects groups

batteryDescriptionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 233, 2, 2, 1)
)
batteryDescriptionGroup.setObjects(
      *(("BATTERY-MIB", "batteryIdentifier"),
        ("BATTERY-MIB", "batteryFirmwareVersion"),
        ("BATTERY-MIB", "batteryType"),
        ("BATTERY-MIB", "batteryTechnology"),
        ("BATTERY-MIB", "batteryDesignVoltage"),
        ("BATTERY-MIB", "batteryNumberOfCells"),
        ("BATTERY-MIB", "batteryDesignCapacity"),
        ("BATTERY-MIB", "batteryMaxChargingCurrent"),
        ("BATTERY-MIB", "batteryTrickleChargingCurrent"))
)
if mibBuilder.loadTexts:
    batteryDescriptionGroup.setStatus("current")

batteryStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 233, 2, 2, 2)
)
batteryStatusGroup.setObjects(
      *(("BATTERY-MIB", "batteryActualCapacity"),
        ("BATTERY-MIB", "batteryChargingCycleCount"),
        ("BATTERY-MIB", "batteryLastChargingCycleTime"),
        ("BATTERY-MIB", "batteryChargingOperState"),
        ("BATTERY-MIB", "batteryActualCharge"),
        ("BATTERY-MIB", "batteryActualVoltage"),
        ("BATTERY-MIB", "batteryActualCurrent"),
        ("BATTERY-MIB", "batteryTemperature"))
)
if mibBuilder.loadTexts:
    batteryStatusGroup.setStatus("current")

batteryAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 233, 2, 2, 3)
)
batteryAdminGroup.setObjects(
    ("BATTERY-MIB", "batteryChargingAdminState")
)
if mibBuilder.loadTexts:
    batteryAdminGroup.setStatus("current")

batteryAlarmThresholdsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 233, 2, 2, 4)
)
batteryAlarmThresholdsGroup.setObjects(
      *(("BATTERY-MIB", "batteryAlarmLowCharge"),
        ("BATTERY-MIB", "batteryAlarmLowVoltage"),
        ("BATTERY-MIB", "batteryAlarmLowCapacity"),
        ("BATTERY-MIB", "batteryAlarmHighCycleCount"),
        ("BATTERY-MIB", "batteryAlarmHighTemperature"),
        ("BATTERY-MIB", "batteryAlarmLowTemperature"))
)
if mibBuilder.loadTexts:
    batteryAlarmThresholdsGroup.setStatus("current")

batteryPerCellNotificationsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 233, 2, 2, 6)
)
batteryPerCellNotificationsGroup.setObjects(
    ("BATTERY-MIB", "batteryCellIdentifier")
)
if mibBuilder.loadTexts:
    batteryPerCellNotificationsGroup.setStatus("current")


# Notification objects

batteryChargingStateNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 233, 0, 1)
)
batteryChargingStateNotification.setObjects(
    ("BATTERY-MIB", "batteryChargingOperState")
)
if mibBuilder.loadTexts:
    batteryChargingStateNotification.setStatus(
        "current"
    )

batteryLowNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 233, 0, 2)
)
batteryLowNotification.setObjects(
      *(("BATTERY-MIB", "batteryActualCharge"),
        ("BATTERY-MIB", "batteryActualVoltage"),
        ("BATTERY-MIB", "batteryCellIdentifier"))
)
if mibBuilder.loadTexts:
    batteryLowNotification.setStatus(
        "current"
    )

batteryCriticalNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 233, 0, 3)
)
batteryCriticalNotification.setObjects(
      *(("BATTERY-MIB", "batteryActualCharge"),
        ("BATTERY-MIB", "batteryActualVoltage"),
        ("BATTERY-MIB", "batteryCellIdentifier"))
)
if mibBuilder.loadTexts:
    batteryCriticalNotification.setStatus(
        "current"
    )

batteryTemperatureNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 233, 0, 4)
)
batteryTemperatureNotification.setObjects(
      *(("BATTERY-MIB", "batteryTemperature"),
        ("BATTERY-MIB", "batteryCellIdentifier"))
)
if mibBuilder.loadTexts:
    batteryTemperatureNotification.setStatus(
        "current"
    )

batteryAgingNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 233, 0, 5)
)
batteryAgingNotification.setObjects(
      *(("BATTERY-MIB", "batteryActualCapacity"),
        ("BATTERY-MIB", "batteryChargingCycleCount"),
        ("BATTERY-MIB", "batteryCellIdentifier"))
)
if mibBuilder.loadTexts:
    batteryAgingNotification.setStatus(
        "current"
    )

batteryConnectedNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 233, 0, 6)
)
batteryConnectedNotification.setObjects(
    ("BATTERY-MIB", "batteryIdentifier")
)
if mibBuilder.loadTexts:
    batteryConnectedNotification.setStatus(
        "current"
    )

batteryDisconnectedNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 233, 0, 7)
)
if mibBuilder.loadTexts:
    batteryDisconnectedNotification.setStatus(
        "current"
    )


# Notifications groups

batteryNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 233, 2, 2, 5)
)
batteryNotificationsGroup.setObjects(
      *(("BATTERY-MIB", "batteryChargingStateNotification"),
        ("BATTERY-MIB", "batteryLowNotification"),
        ("BATTERY-MIB", "batteryCriticalNotification"),
        ("BATTERY-MIB", "batteryAgingNotification"),
        ("BATTERY-MIB", "batteryTemperatureNotification"),
        ("BATTERY-MIB", "batteryConnectedNotification"),
        ("BATTERY-MIB", "batteryDisconnectedNotification"))
)
if mibBuilder.loadTexts:
    batteryNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

batteryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 233, 2, 1, 1)
)
if mibBuilder.loadTexts:
    batteryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BATTERY-MIB",
    **{"batteryMIB": batteryMIB,
       "batteryNotifications": batteryNotifications,
       "batteryChargingStateNotification": batteryChargingStateNotification,
       "batteryLowNotification": batteryLowNotification,
       "batteryCriticalNotification": batteryCriticalNotification,
       "batteryTemperatureNotification": batteryTemperatureNotification,
       "batteryAgingNotification": batteryAgingNotification,
       "batteryConnectedNotification": batteryConnectedNotification,
       "batteryDisconnectedNotification": batteryDisconnectedNotification,
       "batteryObjects": batteryObjects,
       "batteryTable": batteryTable,
       "batteryEntry": batteryEntry,
       "batteryIdentifier": batteryIdentifier,
       "batteryFirmwareVersion": batteryFirmwareVersion,
       "batteryType": batteryType,
       "batteryTechnology": batteryTechnology,
       "batteryDesignVoltage": batteryDesignVoltage,
       "batteryNumberOfCells": batteryNumberOfCells,
       "batteryDesignCapacity": batteryDesignCapacity,
       "batteryMaxChargingCurrent": batteryMaxChargingCurrent,
       "batteryTrickleChargingCurrent": batteryTrickleChargingCurrent,
       "batteryActualCapacity": batteryActualCapacity,
       "batteryChargingCycleCount": batteryChargingCycleCount,
       "batteryLastChargingCycleTime": batteryLastChargingCycleTime,
       "batteryChargingOperState": batteryChargingOperState,
       "batteryChargingAdminState": batteryChargingAdminState,
       "batteryActualCharge": batteryActualCharge,
       "batteryActualVoltage": batteryActualVoltage,
       "batteryActualCurrent": batteryActualCurrent,
       "batteryTemperature": batteryTemperature,
       "batteryAlarmLowCharge": batteryAlarmLowCharge,
       "batteryAlarmLowVoltage": batteryAlarmLowVoltage,
       "batteryAlarmLowCapacity": batteryAlarmLowCapacity,
       "batteryAlarmHighCycleCount": batteryAlarmHighCycleCount,
       "batteryAlarmHighTemperature": batteryAlarmHighTemperature,
       "batteryAlarmLowTemperature": batteryAlarmLowTemperature,
       "batteryCellIdentifier": batteryCellIdentifier,
       "batteryConformance": batteryConformance,
       "batteryCompliances": batteryCompliances,
       "batteryCompliance": batteryCompliance,
       "batteryGroups": batteryGroups,
       "batteryDescriptionGroup": batteryDescriptionGroup,
       "batteryStatusGroup": batteryStatusGroup,
       "batteryAdminGroup": batteryAdminGroup,
       "batteryAlarmThresholdsGroup": batteryAlarmThresholdsGroup,
       "batteryNotificationsGroup": batteryNotificationsGroup,
       "batteryPerCellNotificationsGroup": batteryPerCellNotificationsGroup}
)
