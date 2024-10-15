# SNMP MIB module (AT-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-ENVMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:04 2024
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

(DisplayStringUnsized,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized")

(sysinfo,) = mibBuilder.importSymbols(
    "AT-SYSINFO-MIB",
    "sysinfo")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

envMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10)
)
envMon.setRevisions(
        ("2006-03-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnvMonPsbSensorType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fanSpeedDiscrete", 1),
          ("psbSensorTypeInvalid", 0),
          ("temperatureDiscrete", 2),
          ("voltageDiscrete", 3))
    )



# MIB Managed Objects in the order of their OIDs

_EnvMonFanTable_Object = MibTable
envMonFanTable = _EnvMonFanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1)
)
if mibBuilder.loadTexts:
    envMonFanTable.setStatus("current")
_EnvMonFanEntry_Object = MibTableRow
envMonFanEntry = _EnvMonFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1)
)
envMonFanEntry.setIndexNames(
    (0, "AT-ENVMON-MIB", "envMonFanBoardIndex"),
    (0, "AT-ENVMON-MIB", "envMonFanIndex"),
)
if mibBuilder.loadTexts:
    envMonFanEntry.setStatus("current")
_EnvMonFanBoardIndex_Type = Unsigned32
_EnvMonFanBoardIndex_Object = MibTableColumn
envMonFanBoardIndex = _EnvMonFanBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1, 1),
    _EnvMonFanBoardIndex_Type()
)
envMonFanBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonFanBoardIndex.setStatus("current")
_EnvMonFanIndex_Type = Unsigned32
_EnvMonFanIndex_Object = MibTableColumn
envMonFanIndex = _EnvMonFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1, 2),
    _EnvMonFanIndex_Type()
)
envMonFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonFanIndex.setStatus("current")


class _EnvMonFanDescription_Type(DisplayStringUnsized):
    """Custom type envMonFanDescription based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_EnvMonFanDescription_Type.__name__ = "DisplayStringUnsized"
_EnvMonFanDescription_Object = MibTableColumn
envMonFanDescription = _EnvMonFanDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1, 3),
    _EnvMonFanDescription_Type()
)
envMonFanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonFanDescription.setStatus("current")
_EnvMonFanCurrentSpeed_Type = Unsigned32
_EnvMonFanCurrentSpeed_Object = MibTableColumn
envMonFanCurrentSpeed = _EnvMonFanCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1, 4),
    _EnvMonFanCurrentSpeed_Type()
)
envMonFanCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonFanCurrentSpeed.setStatus("current")
_EnvMonFanLowerThreshold_Type = Unsigned32
_EnvMonFanLowerThreshold_Object = MibTableColumn
envMonFanLowerThreshold = _EnvMonFanLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1, 5),
    _EnvMonFanLowerThreshold_Type()
)
envMonFanLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envMonFanLowerThreshold.setStatus("current")
_EnvMonFanAlarm_Type = TruthValue
_EnvMonFanAlarm_Object = MibTableColumn
envMonFanAlarm = _EnvMonFanAlarm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 1, 1, 6),
    _EnvMonFanAlarm_Type()
)
envMonFanAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonFanAlarm.setStatus("current")
_EnvMonVoltageTable_Object = MibTable
envMonVoltageTable = _EnvMonVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2)
)
if mibBuilder.loadTexts:
    envMonVoltageTable.setStatus("current")
_EnvMonVoltageEntry_Object = MibTableRow
envMonVoltageEntry = _EnvMonVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1)
)
envMonVoltageEntry.setIndexNames(
    (0, "AT-ENVMON-MIB", "envMonVoltageBoardIndex"),
    (0, "AT-ENVMON-MIB", "envMonVoltageIndex"),
)
if mibBuilder.loadTexts:
    envMonVoltageEntry.setStatus("current")
_EnvMonVoltageBoardIndex_Type = Unsigned32
_EnvMonVoltageBoardIndex_Object = MibTableColumn
envMonVoltageBoardIndex = _EnvMonVoltageBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 1),
    _EnvMonVoltageBoardIndex_Type()
)
envMonVoltageBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonVoltageBoardIndex.setStatus("current")
_EnvMonVoltageIndex_Type = Unsigned32
_EnvMonVoltageIndex_Object = MibTableColumn
envMonVoltageIndex = _EnvMonVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 2),
    _EnvMonVoltageIndex_Type()
)
envMonVoltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonVoltageIndex.setStatus("current")


class _EnvMonVoltageDescription_Type(DisplayStringUnsized):
    """Custom type envMonVoltageDescription based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_EnvMonVoltageDescription_Type.__name__ = "DisplayStringUnsized"
_EnvMonVoltageDescription_Object = MibTableColumn
envMonVoltageDescription = _EnvMonVoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 3),
    _EnvMonVoltageDescription_Type()
)
envMonVoltageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonVoltageDescription.setStatus("current")
_EnvMonVoltageCurrent_Type = Integer32
_EnvMonVoltageCurrent_Object = MibTableColumn
envMonVoltageCurrent = _EnvMonVoltageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 4),
    _EnvMonVoltageCurrent_Type()
)
envMonVoltageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonVoltageCurrent.setStatus("current")
_EnvMonVoltageUpperThreshold_Type = Integer32
_EnvMonVoltageUpperThreshold_Object = MibTableColumn
envMonVoltageUpperThreshold = _EnvMonVoltageUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 5),
    _EnvMonVoltageUpperThreshold_Type()
)
envMonVoltageUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envMonVoltageUpperThreshold.setStatus("current")
_EnvMonVoltageLowerThreshold_Type = Integer32
_EnvMonVoltageLowerThreshold_Object = MibTableColumn
envMonVoltageLowerThreshold = _EnvMonVoltageLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 6),
    _EnvMonVoltageLowerThreshold_Type()
)
envMonVoltageLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envMonVoltageLowerThreshold.setStatus("current")
_EnvMonVoltageAlarm_Type = TruthValue
_EnvMonVoltageAlarm_Object = MibTableColumn
envMonVoltageAlarm = _EnvMonVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 2, 1, 7),
    _EnvMonVoltageAlarm_Type()
)
envMonVoltageAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonVoltageAlarm.setStatus("current")
_EnvMonTemperatureTable_Object = MibTable
envMonTemperatureTable = _EnvMonTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3)
)
if mibBuilder.loadTexts:
    envMonTemperatureTable.setStatus("current")
_EnvMonTemperatureEntry_Object = MibTableRow
envMonTemperatureEntry = _EnvMonTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1)
)
envMonTemperatureEntry.setIndexNames(
    (0, "AT-ENVMON-MIB", "envMonTemperatureBoardIndex"),
    (0, "AT-ENVMON-MIB", "envMonTemperatureIndex"),
)
if mibBuilder.loadTexts:
    envMonTemperatureEntry.setStatus("current")
_EnvMonTemperatureBoardIndex_Type = Unsigned32
_EnvMonTemperatureBoardIndex_Object = MibTableColumn
envMonTemperatureBoardIndex = _EnvMonTemperatureBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1, 1),
    _EnvMonTemperatureBoardIndex_Type()
)
envMonTemperatureBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonTemperatureBoardIndex.setStatus("current")
_EnvMonTemperatureIndex_Type = Unsigned32
_EnvMonTemperatureIndex_Object = MibTableColumn
envMonTemperatureIndex = _EnvMonTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1, 2),
    _EnvMonTemperatureIndex_Type()
)
envMonTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonTemperatureIndex.setStatus("current")


class _EnvMonTemperatureDescription_Type(DisplayStringUnsized):
    """Custom type envMonTemperatureDescription based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_EnvMonTemperatureDescription_Type.__name__ = "DisplayStringUnsized"
_EnvMonTemperatureDescription_Object = MibTableColumn
envMonTemperatureDescription = _EnvMonTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1, 3),
    _EnvMonTemperatureDescription_Type()
)
envMonTemperatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonTemperatureDescription.setStatus("current")
_EnvMonTemperatureCurrent_Type = Integer32
_EnvMonTemperatureCurrent_Object = MibTableColumn
envMonTemperatureCurrent = _EnvMonTemperatureCurrent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1, 4),
    _EnvMonTemperatureCurrent_Type()
)
envMonTemperatureCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonTemperatureCurrent.setStatus("current")
_EnvMonTemperatureUpperThreshold_Type = Integer32
_EnvMonTemperatureUpperThreshold_Object = MibTableColumn
envMonTemperatureUpperThreshold = _EnvMonTemperatureUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1, 5),
    _EnvMonTemperatureUpperThreshold_Type()
)
envMonTemperatureUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envMonTemperatureUpperThreshold.setStatus("current")
_EnvMonTemperatureAlarm_Type = TruthValue
_EnvMonTemperatureAlarm_Object = MibTableColumn
envMonTemperatureAlarm = _EnvMonTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 3, 1, 6),
    _EnvMonTemperatureAlarm_Type()
)
envMonTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonTemperatureAlarm.setStatus("current")
_EnvMonPsbObjects_ObjectIdentity = ObjectIdentity
envMonPsbObjects = _EnvMonPsbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4)
)
_EnvMonPsbTable_Object = MibTable
envMonPsbTable = _EnvMonPsbTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1)
)
if mibBuilder.loadTexts:
    envMonPsbTable.setStatus("current")
_EnvMonPsbEntry_Object = MibTableRow
envMonPsbEntry = _EnvMonPsbEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1, 1)
)
envMonPsbEntry.setIndexNames(
    (0, "AT-ENVMON-MIB", "envMonPsbHostBoardIndex"),
    (0, "AT-ENVMON-MIB", "envMonPsbHostSlotIndex"),
)
if mibBuilder.loadTexts:
    envMonPsbEntry.setStatus("current")
_EnvMonPsbHostBoardIndex_Type = Unsigned32
_EnvMonPsbHostBoardIndex_Object = MibTableColumn
envMonPsbHostBoardIndex = _EnvMonPsbHostBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1, 1, 1),
    _EnvMonPsbHostBoardIndex_Type()
)
envMonPsbHostBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonPsbHostBoardIndex.setStatus("current")
_EnvMonPsbHostSlotIndex_Type = Unsigned32
_EnvMonPsbHostSlotIndex_Object = MibTableColumn
envMonPsbHostSlotIndex = _EnvMonPsbHostSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1, 1, 2),
    _EnvMonPsbHostSlotIndex_Type()
)
envMonPsbHostSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonPsbHostSlotIndex.setStatus("current")
_EnvMonPsbHeldBoardIndex_Type = Unsigned32
_EnvMonPsbHeldBoardIndex_Object = MibTableColumn
envMonPsbHeldBoardIndex = _EnvMonPsbHeldBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1, 1, 3),
    _EnvMonPsbHeldBoardIndex_Type()
)
envMonPsbHeldBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonPsbHeldBoardIndex.setStatus("current")
_EnvMonPsbHeldBoardId_Type = ObjectIdentifier
_EnvMonPsbHeldBoardId_Object = MibTableColumn
envMonPsbHeldBoardId = _EnvMonPsbHeldBoardId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1, 1, 4),
    _EnvMonPsbHeldBoardId_Type()
)
envMonPsbHeldBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonPsbHeldBoardId.setStatus("current")


class _EnvMonPsbDescription_Type(DisplayStringUnsized):
    """Custom type envMonPsbDescription based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_EnvMonPsbDescription_Type.__name__ = "DisplayStringUnsized"
_EnvMonPsbDescription_Object = MibTableColumn
envMonPsbDescription = _EnvMonPsbDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 1, 1, 5),
    _EnvMonPsbDescription_Type()
)
envMonPsbDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonPsbDescription.setStatus("current")
_EnvMonPsbSensorTable_Object = MibTable
envMonPsbSensorTable = _EnvMonPsbSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2)
)
if mibBuilder.loadTexts:
    envMonPsbSensorTable.setStatus("current")
_EnvMonPsbSensorEntry_Object = MibTableRow
envMonPsbSensorEntry = _EnvMonPsbSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2, 1)
)
envMonPsbSensorEntry.setIndexNames(
    (0, "AT-ENVMON-MIB", "envMonPsbSensorBoardIndex"),
    (0, "AT-ENVMON-MIB", "envMonPsbSensorIndex"),
)
if mibBuilder.loadTexts:
    envMonPsbSensorEntry.setStatus("current")
_EnvMonPsbSensorBoardIndex_Type = Unsigned32
_EnvMonPsbSensorBoardIndex_Object = MibTableColumn
envMonPsbSensorBoardIndex = _EnvMonPsbSensorBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2, 1, 1),
    _EnvMonPsbSensorBoardIndex_Type()
)
envMonPsbSensorBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonPsbSensorBoardIndex.setStatus("current")
_EnvMonPsbSensorIndex_Type = Unsigned32
_EnvMonPsbSensorIndex_Object = MibTableColumn
envMonPsbSensorIndex = _EnvMonPsbSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2, 1, 2),
    _EnvMonPsbSensorIndex_Type()
)
envMonPsbSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonPsbSensorIndex.setStatus("current")
_EnvMonPsbSensorType_Type = EnvMonPsbSensorType
_EnvMonPsbSensorType_Object = MibTableColumn
envMonPsbSensorType = _EnvMonPsbSensorType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2, 1, 3),
    _EnvMonPsbSensorType_Type()
)
envMonPsbSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonPsbSensorType.setStatus("current")


class _EnvMonPsbSensorDescription_Type(DisplayStringUnsized):
    """Custom type envMonPsbSensorDescription based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_EnvMonPsbSensorDescription_Type.__name__ = "DisplayStringUnsized"
_EnvMonPsbSensorDescription_Object = MibTableColumn
envMonPsbSensorDescription = _EnvMonPsbSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2, 1, 4),
    _EnvMonPsbSensorDescription_Type()
)
envMonPsbSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonPsbSensorDescription.setStatus("current")
_EnvMonPsbSensorAlarm_Type = TruthValue
_EnvMonPsbSensorAlarm_Object = MibTableColumn
envMonPsbSensorAlarm = _EnvMonPsbSensorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 4, 2, 1, 5),
    _EnvMonPsbSensorAlarm_Type()
)
envMonPsbSensorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envMonPsbSensorAlarm.setStatus("current")
_EnvMonTraps_ObjectIdentity = ObjectIdentity
envMonTraps = _EnvMonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5)
)

# Managed Objects groups


# Notification objects

envMonFanAlarmSetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 1)
)
envMonFanAlarmSetEvent.setObjects(
      *(("AT-ENVMON-MIB", "envMonFanBoardIndex"),
        ("AT-ENVMON-MIB", "envMonFanIndex"),
        ("AT-ENVMON-MIB", "envMonFanDescription"),
        ("AT-ENVMON-MIB", "envMonFanLowerThreshold"),
        ("AT-ENVMON-MIB", "envMonFanCurrentSpeed"))
)
if mibBuilder.loadTexts:
    envMonFanAlarmSetEvent.setStatus(
        "current"
    )

envMonFanAlarmClearedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 2)
)
envMonFanAlarmClearedEvent.setObjects(
      *(("AT-ENVMON-MIB", "envMonFanBoardIndex"),
        ("AT-ENVMON-MIB", "envMonFanIndex"),
        ("AT-ENVMON-MIB", "envMonFanDescription"),
        ("AT-ENVMON-MIB", "envMonFanLowerThreshold"),
        ("AT-ENVMON-MIB", "envMonFanCurrentSpeed"))
)
if mibBuilder.loadTexts:
    envMonFanAlarmClearedEvent.setStatus(
        "current"
    )

envMonVoltAlarmSetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 3)
)
envMonVoltAlarmSetEvent.setObjects(
      *(("AT-ENVMON-MIB", "envMonVoltageBoardIndex"),
        ("AT-ENVMON-MIB", "envMonVoltageIndex"),
        ("AT-ENVMON-MIB", "envMonVoltageDescription"),
        ("AT-ENVMON-MIB", "envMonVoltageUpperThreshold"),
        ("AT-ENVMON-MIB", "envMonVoltageLowerThreshold"),
        ("AT-ENVMON-MIB", "envMonVoltageCurrent"))
)
if mibBuilder.loadTexts:
    envMonVoltAlarmSetEvent.setStatus(
        "current"
    )

envMonVoltAlarmClearedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 4)
)
envMonVoltAlarmClearedEvent.setObjects(
      *(("AT-ENVMON-MIB", "envMonVoltageBoardIndex"),
        ("AT-ENVMON-MIB", "envMonVoltageIndex"),
        ("AT-ENVMON-MIB", "envMonVoltageDescription"),
        ("AT-ENVMON-MIB", "envMonVoltageUpperThreshold"),
        ("AT-ENVMON-MIB", "envMonVoltageLowerThreshold"),
        ("AT-ENVMON-MIB", "envMonVoltageCurrent"))
)
if mibBuilder.loadTexts:
    envMonVoltAlarmClearedEvent.setStatus(
        "current"
    )

envMonTempAlarmSetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 5)
)
envMonTempAlarmSetEvent.setObjects(
      *(("AT-ENVMON-MIB", "envMonTemperatureBoardIndex"),
        ("AT-ENVMON-MIB", "envMonTemperatureIndex"),
        ("AT-ENVMON-MIB", "envMonTemperatureDescription"),
        ("AT-ENVMON-MIB", "envMonTemperatureUpperThreshold"),
        ("AT-ENVMON-MIB", "envMonTemperatureCurrent"))
)
if mibBuilder.loadTexts:
    envMonTempAlarmSetEvent.setStatus(
        "current"
    )

envMonTempAlarmClearedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 6)
)
envMonTempAlarmClearedEvent.setObjects(
      *(("AT-ENVMON-MIB", "envMonTemperatureBoardIndex"),
        ("AT-ENVMON-MIB", "envMonTemperatureIndex"),
        ("AT-ENVMON-MIB", "envMonTemperatureDescription"),
        ("AT-ENVMON-MIB", "envMonTemperatureUpperThreshold"),
        ("AT-ENVMON-MIB", "envMonTemperatureCurrent"))
)
if mibBuilder.loadTexts:
    envMonTempAlarmClearedEvent.setStatus(
        "current"
    )

envMonPsbAlarmSetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 7)
)
envMonPsbAlarmSetEvent.setObjects(
      *(("AT-ENVMON-MIB", "envMonPsbSensorBoardIndex"),
        ("AT-ENVMON-MIB", "envMonPsbSensorIndex"),
        ("AT-ENVMON-MIB", "envMonPsbSensorType"),
        ("AT-ENVMON-MIB", "envMonPsbSensorDescription"))
)
if mibBuilder.loadTexts:
    envMonPsbAlarmSetEvent.setStatus(
        "current"
    )

envMonPsbAlarmClearedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 10, 5, 8)
)
envMonPsbAlarmClearedEvent.setObjects(
      *(("AT-ENVMON-MIB", "envMonPsbSensorBoardIndex"),
        ("AT-ENVMON-MIB", "envMonPsbSensorIndex"),
        ("AT-ENVMON-MIB", "envMonPsbSensorType"),
        ("AT-ENVMON-MIB", "envMonPsbSensorDescription"))
)
if mibBuilder.loadTexts:
    envMonPsbAlarmClearedEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-ENVMON-MIB",
    **{"EnvMonPsbSensorType": EnvMonPsbSensorType,
       "envMon": envMon,
       "envMonFanTable": envMonFanTable,
       "envMonFanEntry": envMonFanEntry,
       "envMonFanBoardIndex": envMonFanBoardIndex,
       "envMonFanIndex": envMonFanIndex,
       "envMonFanDescription": envMonFanDescription,
       "envMonFanCurrentSpeed": envMonFanCurrentSpeed,
       "envMonFanLowerThreshold": envMonFanLowerThreshold,
       "envMonFanAlarm": envMonFanAlarm,
       "envMonVoltageTable": envMonVoltageTable,
       "envMonVoltageEntry": envMonVoltageEntry,
       "envMonVoltageBoardIndex": envMonVoltageBoardIndex,
       "envMonVoltageIndex": envMonVoltageIndex,
       "envMonVoltageDescription": envMonVoltageDescription,
       "envMonVoltageCurrent": envMonVoltageCurrent,
       "envMonVoltageUpperThreshold": envMonVoltageUpperThreshold,
       "envMonVoltageLowerThreshold": envMonVoltageLowerThreshold,
       "envMonVoltageAlarm": envMonVoltageAlarm,
       "envMonTemperatureTable": envMonTemperatureTable,
       "envMonTemperatureEntry": envMonTemperatureEntry,
       "envMonTemperatureBoardIndex": envMonTemperatureBoardIndex,
       "envMonTemperatureIndex": envMonTemperatureIndex,
       "envMonTemperatureDescription": envMonTemperatureDescription,
       "envMonTemperatureCurrent": envMonTemperatureCurrent,
       "envMonTemperatureUpperThreshold": envMonTemperatureUpperThreshold,
       "envMonTemperatureAlarm": envMonTemperatureAlarm,
       "envMonPsbObjects": envMonPsbObjects,
       "envMonPsbTable": envMonPsbTable,
       "envMonPsbEntry": envMonPsbEntry,
       "envMonPsbHostBoardIndex": envMonPsbHostBoardIndex,
       "envMonPsbHostSlotIndex": envMonPsbHostSlotIndex,
       "envMonPsbHeldBoardIndex": envMonPsbHeldBoardIndex,
       "envMonPsbHeldBoardId": envMonPsbHeldBoardId,
       "envMonPsbDescription": envMonPsbDescription,
       "envMonPsbSensorTable": envMonPsbSensorTable,
       "envMonPsbSensorEntry": envMonPsbSensorEntry,
       "envMonPsbSensorBoardIndex": envMonPsbSensorBoardIndex,
       "envMonPsbSensorIndex": envMonPsbSensorIndex,
       "envMonPsbSensorType": envMonPsbSensorType,
       "envMonPsbSensorDescription": envMonPsbSensorDescription,
       "envMonPsbSensorAlarm": envMonPsbSensorAlarm,
       "envMonTraps": envMonTraps,
       "envMonFanAlarmSetEvent": envMonFanAlarmSetEvent,
       "envMonFanAlarmClearedEvent": envMonFanAlarmClearedEvent,
       "envMonVoltAlarmSetEvent": envMonVoltAlarmSetEvent,
       "envMonVoltAlarmClearedEvent": envMonVoltAlarmClearedEvent,
       "envMonTempAlarmSetEvent": envMonTempAlarmSetEvent,
       "envMonTempAlarmClearedEvent": envMonTempAlarmClearedEvent,
       "envMonPsbAlarmSetEvent": envMonPsbAlarmSetEvent,
       "envMonPsbAlarmClearedEvent": envMonPsbAlarmClearedEvent}
)
