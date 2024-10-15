# SNMP MIB module (SNR-ERD-2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNR-ERD-2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:24 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

snr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40418)
)
snr.setRevisions(
        ("2015-04-29 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Snr_erd_ObjectIdentity = ObjectIdentity
snr_erd = _Snr_erd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2)
)
_Snr_erd_2_ObjectIdentity = ObjectIdentity
snr_erd_2 = _Snr_erd_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2)
)
_Erd2Traps_ObjectIdentity = ObjectIdentity
erd2Traps = _Erd2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0)
)
_IpAddressEntry_ObjectIdentity = ObjectIdentity
ipAddressEntry = _IpAddressEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 1)
)
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 1, 1),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_IpGatewayAddress_Type = IpAddress
_IpGatewayAddress_Object = MibScalar
ipGatewayAddress = _IpGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 1, 2),
    _IpGatewayAddress_Type()
)
ipGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGatewayAddress.setStatus("current")
_IpMonitoringDevice_Type = IpAddress
_IpMonitoringDevice_Object = MibScalar
ipMonitoringDevice = _IpMonitoringDevice_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 1, 3),
    _IpMonitoringDevice_Type()
)
ipMonitoringDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMonitoringDevice.setStatus("current")
_IpForTrap_Type = IpAddress
_IpForTrap_Object = MibScalar
ipForTrap = _IpForTrap_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 1, 4),
    _IpForTrap_Type()
)
ipForTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForTrap.setStatus("current")
_ResetsSet_ObjectIdentity = ObjectIdentity
resetsSet = _ResetsSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 2)
)


class _ResetSmartContact6_Type(Integer32):
    """Custom type resetSmartContact6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 0),
          ("reset", 1))
    )


_ResetSmartContact6_Type.__name__ = "Integer32"
_ResetSmartContact6_Object = MibScalar
resetSmartContact6 = _ResetSmartContact6_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 2, 1),
    _ResetSmartContact6_Type()
)
resetSmartContact6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetSmartContact6.setStatus("current")


class _NumberOfResetPositives_Type(Integer32):
    """Custom type numberOfResetPositives based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("resetPositives", 0)
    )


_NumberOfResetPositives_Type.__name__ = "Integer32"
_NumberOfResetPositives_Object = MibScalar
numberOfResetPositives = _NumberOfResetPositives_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 2, 2),
    _NumberOfResetPositives_Type()
)
numberOfResetPositives.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfResetPositives.setStatus("current")


class _RemoteControlContact8_Type(Integer32):
    """Custom type remoteControlContact8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("autoOFF", 6),
          ("autoON", 5),
          ("manOFF", 1),
          ("manON", 0),
          ("manualSetON", 2),
          ("switch", 4),
          ("termostatSetON", 3))
    )


_RemoteControlContact8_Type.__name__ = "Integer32"
_RemoteControlContact8_Object = MibScalar
remoteControlContact8 = _RemoteControlContact8_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 2, 3),
    _RemoteControlContact8_Type()
)
remoteControlContact8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteControlContact8.setStatus("current")
_SensesSet1_ObjectIdentity = ObjectIdentity
sensesSet1 = _SensesSet1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 3)
)


class _MonitorAlarmSignalContact3_Type(Integer32):
    """Custom type monitorAlarmSignalContact3 based on Integer32"""
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
        *(("doorIsClose", 1),
          ("doorIsOpen", 2),
          ("sensorOff", 0),
          ("sensorOn", 3))
    )


_MonitorAlarmSignalContact3_Type.__name__ = "Integer32"
_MonitorAlarmSignalContact3_Object = MibScalar
monitorAlarmSignalContact3 = _MonitorAlarmSignalContact3_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 3, 1),
    _MonitorAlarmSignalContact3_Type()
)
monitorAlarmSignalContact3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAlarmSignalContact3.setStatus("current")


class _NumberOfAlarmPositives_Type(Integer32):
    """Custom type numberOfAlarmPositives based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("resetPositives", 0)
    )


_NumberOfAlarmPositives_Type.__name__ = "Integer32"
_NumberOfAlarmPositives_Object = MibScalar
numberOfAlarmPositives = _NumberOfAlarmPositives_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 3, 2),
    _NumberOfAlarmPositives_Type()
)
numberOfAlarmPositives.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfAlarmPositives.setStatus("current")


class _MonitorAnySensorSignal1contact4_Type(Integer32):
    """Custom type monitorAnySensorSignal1contact4 based on Integer32"""
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
        *(("sensorIs0", 1),
          ("sensorIs1", 2),
          ("sensorOff", 0),
          ("sensorOn", 3))
    )


_MonitorAnySensorSignal1contact4_Type.__name__ = "Integer32"
_MonitorAnySensorSignal1contact4_Object = MibScalar
monitorAnySensorSignal1contact4 = _MonitorAnySensorSignal1contact4_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 3, 3),
    _MonitorAnySensorSignal1contact4_Type()
)
monitorAnySensorSignal1contact4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAnySensorSignal1contact4.setStatus("current")


class _MonitorAnySensorSignal2contact7_Type(Integer32):
    """Custom type monitorAnySensorSignal2contact7 based on Integer32"""
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
        *(("sensorIs0", 1),
          ("sensorIs1", 2),
          ("sensorOff", 0),
          ("sensorOn", 3))
    )


_MonitorAnySensorSignal2contact7_Type.__name__ = "Integer32"
_MonitorAnySensorSignal2contact7_Object = MibScalar
monitorAnySensorSignal2contact7 = _MonitorAnySensorSignal2contact7_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 3, 4),
    _MonitorAnySensorSignal2contact7_Type()
)
monitorAnySensorSignal2contact7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAnySensorSignal2contact7.setStatus("current")


class _MonitorAnySensorSignal3contact9_Type(Integer32):
    """Custom type monitorAnySensorSignal3contact9 based on Integer32"""
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
        *(("sensorIs0", 1),
          ("sensorIs1", 2),
          ("sensorOff", 0),
          ("sensorOn", 3))
    )


_MonitorAnySensorSignal3contact9_Type.__name__ = "Integer32"
_MonitorAnySensorSignal3contact9_Object = MibScalar
monitorAnySensorSignal3contact9 = _MonitorAnySensorSignal3contact9_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 3, 5),
    _MonitorAnySensorSignal3contact9_Type()
)
monitorAnySensorSignal3contact9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAnySensorSignal3contact9.setStatus("current")


class _MonitorVoltageSignal_Type(Integer32):
    """Custom type monitorVoltageSignal based on Integer32"""
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
        *(("sensorOff", 0),
          ("sensorOn", 3),
          ("voltageIsNo", 1),
          ("voltageIsYes", 2))
    )


_MonitorVoltageSignal_Type.__name__ = "Integer32"
_MonitorVoltageSignal_Object = MibScalar
monitorVoltageSignal = _MonitorVoltageSignal_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 3, 6),
    _MonitorVoltageSignal_Type()
)
monitorVoltageSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorVoltageSignal.setStatus("current")
_SensesSet2_ObjectIdentity = ObjectIdentity
sensesSet2 = _SensesSet2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 4)
)
_TemperatureSensor_Type = Integer32
_TemperatureSensor_Object = MibScalar
temperatureSensor = _TemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 4, 1),
    _TemperatureSensor_Type()
)
temperatureSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor.setStatus("current")
_VoltageSensorContact10_Type = Integer32
_VoltageSensorContact10_Object = MibScalar
voltageSensorContact10 = _VoltageSensorContact10_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 4, 2),
    _VoltageSensorContact10_Type()
)
voltageSensorContact10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorContact10.setStatus("current")
_SysVoltageAlarm_Type = Integer32
_SysVoltageAlarm_Object = MibScalar
sysVoltageAlarm = _SysVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 4, 3),
    _SysVoltageAlarm_Type()
)
sysVoltageAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysVoltageAlarm.setStatus("current")
_CommS_ObjectIdentity = ObjectIdentity
commS = _CommS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 5)
)


class _CommunityString_Type(DisplayString):
    """Custom type communityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CommunityString_Type.__name__ = "DisplayString"
_CommunityString_Object = MibScalar
communityString = _CommunityString_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 5, 1),
    _CommunityString_Type()
)
communityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityString.setStatus("current")


class _TrapMode_Type(Integer32):
    """Custom type trapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cyclically", 0),
          ("once", 1))
    )


_TrapMode_Type.__name__ = "Integer32"
_TrapMode_Object = MibScalar
trapMode = _TrapMode_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 5, 2),
    _TrapMode_Type()
)
trapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapMode.setStatus("current")


class _AlarmSenseName_Type(DisplayString):
    """Custom type alarmSenseName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AlarmSenseName_Type.__name__ = "DisplayString"
_AlarmSenseName_Object = MibScalar
alarmSenseName = _AlarmSenseName_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 5, 3),
    _AlarmSenseName_Type()
)
alarmSenseName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSenseName.setStatus("current")


class _UserSense1Name_Type(DisplayString):
    """Custom type userSense1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UserSense1Name_Type.__name__ = "DisplayString"
_UserSense1Name_Object = MibScalar
userSense1Name = _UserSense1Name_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 5, 5),
    _UserSense1Name_Type()
)
userSense1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSense1Name.setStatus("current")


class _UserSense2Name_Type(DisplayString):
    """Custom type userSense2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UserSense2Name_Type.__name__ = "DisplayString"
_UserSense2Name_Object = MibScalar
userSense2Name = _UserSense2Name_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 5, 6),
    _UserSense2Name_Type()
)
userSense2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSense2Name.setStatus("current")


class _UserSense3Name_Type(DisplayString):
    """Custom type userSense3Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UserSense3Name_Type.__name__ = "DisplayString"
_UserSense3Name_Object = MibScalar
userSense3Name = _UserSense3Name_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 5, 7),
    _UserSense3Name_Type()
)
userSense3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSense3Name.setStatus("current")


class _Message_Type(DisplayString):
    """Custom type message based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Message_Type.__name__ = "DisplayString"
_Message_Object = MibScalar
message = _Message_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 5, 10),
    _Message_Type()
)
message.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    message.setStatus("current")

# Managed Objects groups


# Notification objects

temperatureSensorAlarM = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 0)
)
if mibBuilder.loadTexts:
    temperatureSensorAlarM.setStatus(
        "current"
    )

temperatureSensorReleasE = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 1)
)
if mibBuilder.loadTexts:
    temperatureSensorReleasE.setStatus(
        "current"
    )

signalContact3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 2)
)
if mibBuilder.loadTexts:
    signalContact3Alarm.setStatus(
        "current"
    )

signalContact3Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 3)
)
if mibBuilder.loadTexts:
    signalContact3Ok.setStatus(
        "current"
    )

voltageSignalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 4)
)
if mibBuilder.loadTexts:
    voltageSignalAlarm.setStatus(
        "current"
    )

voltageSignalOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 5)
)
if mibBuilder.loadTexts:
    voltageSignalOk.setStatus(
        "current"
    )

anySensorSignal1contact4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 6)
)
if mibBuilder.loadTexts:
    anySensorSignal1contact4Alarm.setStatus(
        "current"
    )

anySensorSignal1contact4Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 7)
)
if mibBuilder.loadTexts:
    anySensorSignal1contact4Ok.setStatus(
        "current"
    )

anySensorSignal2contact7Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 8)
)
if mibBuilder.loadTexts:
    anySensorSignal2contact7Alarm.setStatus(
        "current"
    )

anySensorSignal2contact7Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 9)
)
if mibBuilder.loadTexts:
    anySensorSignal2contact7Ok.setStatus(
        "current"
    )

anySensorSignal3contact9Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 10)
)
if mibBuilder.loadTexts:
    anySensorSignal3contact9Alarm.setStatus(
        "current"
    )

anySensorSignal3contact9Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 11)
)
if mibBuilder.loadTexts:
    anySensorSignal3contact9Ok.setStatus(
        "current"
    )

voltageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 12)
)
if mibBuilder.loadTexts:
    voltageAlarm.setStatus(
        "current"
    )

voltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 13)
)
if mibBuilder.loadTexts:
    voltageOk.setStatus(
        "current"
    )

remoteControlContact8ON = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 14)
)
if mibBuilder.loadTexts:
    remoteControlContact8ON.setStatus(
        "current"
    )

remoteControlContact8OFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 15)
)
if mibBuilder.loadTexts:
    remoteControlContact8OFF.setStatus(
        "current"
    )

resetedSmartContact6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 0, 16)
)
if mibBuilder.loadTexts:
    resetedSmartContact6.setStatus(
        "current"
    )


# Notifications groups

erd2TrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 40418, 2, 2, 99)
)
erd2TrapGroup.setObjects(
      *(("SNR-ERD-2", "temperatureSensorAlarM"),
        ("SNR-ERD-2", "temperatureSensorReleasE"),
        ("SNR-ERD-2", "signalContact3Alarm"),
        ("SNR-ERD-2", "signalContact3Ok"),
        ("SNR-ERD-2", "voltageSignalAlarm"),
        ("SNR-ERD-2", "voltageSignalOk"),
        ("SNR-ERD-2", "anySensorSignal1contact4Alarm"),
        ("SNR-ERD-2", "anySensorSignal1contact4Ok"),
        ("SNR-ERD-2", "anySensorSignal2contact7Alarm"),
        ("SNR-ERD-2", "anySensorSignal2contact7Ok"),
        ("SNR-ERD-2", "anySensorSignal3contact9Alarm"),
        ("SNR-ERD-2", "anySensorSignal3contact9Ok"),
        ("SNR-ERD-2", "voltageAlarm"),
        ("SNR-ERD-2", "voltageOk"),
        ("SNR-ERD-2", "remoteControlContact8ON"),
        ("SNR-ERD-2", "remoteControlContact8OFF"),
        ("SNR-ERD-2", "resetedSmartContact6"))
)
if mibBuilder.loadTexts:
    erd2TrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNR-ERD-2",
    **{"snr": snr,
       "snr-erd": snr_erd,
       "snr-erd-2": snr_erd_2,
       "erd2Traps": erd2Traps,
       "temperatureSensorAlarM": temperatureSensorAlarM,
       "temperatureSensorReleasE": temperatureSensorReleasE,
       "signalContact3Alarm": signalContact3Alarm,
       "signalContact3Ok": signalContact3Ok,
       "voltageSignalAlarm": voltageSignalAlarm,
       "voltageSignalOk": voltageSignalOk,
       "anySensorSignal1contact4Alarm": anySensorSignal1contact4Alarm,
       "anySensorSignal1contact4Ok": anySensorSignal1contact4Ok,
       "anySensorSignal2contact7Alarm": anySensorSignal2contact7Alarm,
       "anySensorSignal2contact7Ok": anySensorSignal2contact7Ok,
       "anySensorSignal3contact9Alarm": anySensorSignal3contact9Alarm,
       "anySensorSignal3contact9Ok": anySensorSignal3contact9Ok,
       "voltageAlarm": voltageAlarm,
       "voltageOk": voltageOk,
       "remoteControlContact8ON": remoteControlContact8ON,
       "remoteControlContact8OFF": remoteControlContact8OFF,
       "resetedSmartContact6": resetedSmartContact6,
       "ipAddressEntry": ipAddressEntry,
       "ipAddress": ipAddress,
       "ipGatewayAddress": ipGatewayAddress,
       "ipMonitoringDevice": ipMonitoringDevice,
       "ipForTrap": ipForTrap,
       "resetsSet": resetsSet,
       "resetSmartContact6": resetSmartContact6,
       "numberOfResetPositives": numberOfResetPositives,
       "remoteControlContact8": remoteControlContact8,
       "sensesSet1": sensesSet1,
       "monitorAlarmSignalContact3": monitorAlarmSignalContact3,
       "numberOfAlarmPositives": numberOfAlarmPositives,
       "monitorAnySensorSignal1contact4": monitorAnySensorSignal1contact4,
       "monitorAnySensorSignal2contact7": monitorAnySensorSignal2contact7,
       "monitorAnySensorSignal3contact9": monitorAnySensorSignal3contact9,
       "monitorVoltageSignal": monitorVoltageSignal,
       "sensesSet2": sensesSet2,
       "temperatureSensor": temperatureSensor,
       "voltageSensorContact10": voltageSensorContact10,
       "sysVoltageAlarm": sysVoltageAlarm,
       "commS": commS,
       "communityString": communityString,
       "trapMode": trapMode,
       "alarmSenseName": alarmSenseName,
       "userSense1Name": userSense1Name,
       "userSense2Name": userSense2Name,
       "userSense3Name": userSense3Name,
       "message": message,
       "erd2TrapGroup": erd2TrapGroup}
)
