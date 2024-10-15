# SNMP MIB module (SNR-ERD-3) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNR-ERD-3
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:25 2024
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
_Snr_erd_3_ObjectIdentity = ObjectIdentity
snr_erd_3 = _Snr_erd_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3)
)
_Erd3Traps_ObjectIdentity = ObjectIdentity
erd3Traps = _Erd3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0)
)
_IpAddressEntry_ObjectIdentity = ObjectIdentity
ipAddressEntry = _IpAddressEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 1)
)
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 1, 1),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_IpGatewayAddress_Type = IpAddress
_IpGatewayAddress_Object = MibScalar
ipGatewayAddress = _IpGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 1, 2),
    _IpGatewayAddress_Type()
)
ipGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGatewayAddress.setStatus("current")
_IpMonitoringDevice_Type = IpAddress
_IpMonitoringDevice_Object = MibScalar
ipMonitoringDevice = _IpMonitoringDevice_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 1, 3),
    _IpMonitoringDevice_Type()
)
ipMonitoringDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMonitoringDevice.setStatus("current")
_IpForTrap_Type = IpAddress
_IpForTrap_Object = MibScalar
ipForTrap = _IpForTrap_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 1, 4),
    _IpForTrap_Type()
)
ipForTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForTrap.setStatus("current")
_ResetsSet_ObjectIdentity = ObjectIdentity
resetsSet = _ResetsSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 2)
)


class _ResetSmartContact7_Type(Integer32):
    """Custom type resetSmartContact7 based on Integer32"""
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


_ResetSmartContact7_Type.__name__ = "Integer32"
_ResetSmartContact7_Object = MibScalar
resetSmartContact7 = _ResetSmartContact7_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 2, 1),
    _ResetSmartContact7_Type()
)
resetSmartContact7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetSmartContact7.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 2, 3),
    _RemoteControlContact8_Type()
)
remoteControlContact8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteControlContact8.setStatus("current")
_SensesSet1_ObjectIdentity = ObjectIdentity
sensesSet1 = _SensesSet1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 3)
)


class _MonitorAlarmSignal1Contact5_Type(Integer32):
    """Custom type monitorAlarmSignal1Contact5 based on Integer32"""
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


_MonitorAlarmSignal1Contact5_Type.__name__ = "Integer32"
_MonitorAlarmSignal1Contact5_Object = MibScalar
monitorAlarmSignal1Contact5 = _MonitorAlarmSignal1Contact5_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 3, 1),
    _MonitorAlarmSignal1Contact5_Type()
)
monitorAlarmSignal1Contact5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAlarmSignal1Contact5.setStatus("current")


class _MonitorAlarmSignal2Contact6_Type(Integer32):
    """Custom type monitorAlarmSignal2Contact6 based on Integer32"""
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


_MonitorAlarmSignal2Contact6_Type.__name__ = "Integer32"
_MonitorAlarmSignal2Contact6_Object = MibScalar
monitorAlarmSignal2Contact6 = _MonitorAlarmSignal2Contact6_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 3, 2),
    _MonitorAlarmSignal2Contact6_Type()
)
monitorAlarmSignal2Contact6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAlarmSignal2Contact6.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 3, 3),
    _NumberOfAlarmPositives_Type()
)
numberOfAlarmPositives.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfAlarmPositives.setStatus("current")


class _MonitorAnySensorSignal1contact2_Type(Integer32):
    """Custom type monitorAnySensorSignal1contact2 based on Integer32"""
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


_MonitorAnySensorSignal1contact2_Type.__name__ = "Integer32"
_MonitorAnySensorSignal1contact2_Object = MibScalar
monitorAnySensorSignal1contact2 = _MonitorAnySensorSignal1contact2_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 3, 4),
    _MonitorAnySensorSignal1contact2_Type()
)
monitorAnySensorSignal1contact2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAnySensorSignal1contact2.setStatus("current")


class _MonitorAnySensorSignal2contact3_Type(Integer32):
    """Custom type monitorAnySensorSignal2contact3 based on Integer32"""
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


_MonitorAnySensorSignal2contact3_Type.__name__ = "Integer32"
_MonitorAnySensorSignal2contact3_Object = MibScalar
monitorAnySensorSignal2contact3 = _MonitorAnySensorSignal2contact3_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 3, 5),
    _MonitorAnySensorSignal2contact3_Type()
)
monitorAnySensorSignal2contact3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAnySensorSignal2contact3.setStatus("current")


class _MonitorAnySensorSignal3contact4_Type(Integer32):
    """Custom type monitorAnySensorSignal3contact4 based on Integer32"""
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


_MonitorAnySensorSignal3contact4_Type.__name__ = "Integer32"
_MonitorAnySensorSignal3contact4_Object = MibScalar
monitorAnySensorSignal3contact4 = _MonitorAnySensorSignal3contact4_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 3, 6),
    _MonitorAnySensorSignal3contact4_Type()
)
monitorAnySensorSignal3contact4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAnySensorSignal3contact4.setStatus("current")


class _MonitorVoltageSignal1_Type(Integer32):
    """Custom type monitorVoltageSignal1 based on Integer32"""
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


_MonitorVoltageSignal1_Type.__name__ = "Integer32"
_MonitorVoltageSignal1_Object = MibScalar
monitorVoltageSignal1 = _MonitorVoltageSignal1_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 3, 7),
    _MonitorVoltageSignal1_Type()
)
monitorVoltageSignal1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorVoltageSignal1.setStatus("current")


class _MonitorVoltageSignal2_Type(Integer32):
    """Custom type monitorVoltageSignal2 based on Integer32"""
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


_MonitorVoltageSignal2_Type.__name__ = "Integer32"
_MonitorVoltageSignal2_Object = MibScalar
monitorVoltageSignal2 = _MonitorVoltageSignal2_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 3, 8),
    _MonitorVoltageSignal2_Type()
)
monitorVoltageSignal2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorVoltageSignal2.setStatus("current")
_SensesSet2_ObjectIdentity = ObjectIdentity
sensesSet2 = _SensesSet2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4)
)
_TemperatureSensor_Type = Integer32
_TemperatureSensor_Object = MibScalar
temperatureSensor = _TemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 1),
    _TemperatureSensor_Type()
)
temperatureSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor.setStatus("current")
_TemperatureSensorsOut_ObjectIdentity = ObjectIdentity
temperatureSensorsOut = _TemperatureSensorsOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 2)
)
_TemperatureSensorOutSerial1_Type = OctetString
_TemperatureSensorOutSerial1_Object = MibScalar
temperatureSensorOutSerial1 = _TemperatureSensorOutSerial1_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 2, 1),
    _TemperatureSensorOutSerial1_Type()
)
temperatureSensorOutSerial1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOutSerial1.setStatus("current")
_TemperatureSensorOut1_Type = Integer32
_TemperatureSensorOut1_Object = MibScalar
temperatureSensorOut1 = _TemperatureSensorOut1_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 2, 2),
    _TemperatureSensorOut1_Type()
)
temperatureSensorOut1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOut1.setStatus("current")
_TemperatureSensorOutSerial2_Type = OctetString
_TemperatureSensorOutSerial2_Object = MibScalar
temperatureSensorOutSerial2 = _TemperatureSensorOutSerial2_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 2, 3),
    _TemperatureSensorOutSerial2_Type()
)
temperatureSensorOutSerial2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOutSerial2.setStatus("current")
_TemperatureSensorOut2_Type = Integer32
_TemperatureSensorOut2_Object = MibScalar
temperatureSensorOut2 = _TemperatureSensorOut2_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 2, 4),
    _TemperatureSensorOut2_Type()
)
temperatureSensorOut2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOut2.setStatus("current")
_TemperatureSensorOutSerial3_Type = OctetString
_TemperatureSensorOutSerial3_Object = MibScalar
temperatureSensorOutSerial3 = _TemperatureSensorOutSerial3_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 2, 5),
    _TemperatureSensorOutSerial3_Type()
)
temperatureSensorOutSerial3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOutSerial3.setStatus("current")
_TemperatureSensorOut3_Type = Integer32
_TemperatureSensorOut3_Object = MibScalar
temperatureSensorOut3 = _TemperatureSensorOut3_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 2, 6),
    _TemperatureSensorOut3_Type()
)
temperatureSensorOut3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOut3.setStatus("current")
_TemperatureSensorOutSerial4_Type = OctetString
_TemperatureSensorOutSerial4_Object = MibScalar
temperatureSensorOutSerial4 = _TemperatureSensorOutSerial4_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 2, 7),
    _TemperatureSensorOutSerial4_Type()
)
temperatureSensorOutSerial4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOutSerial4.setStatus("current")
_TemperatureSensorOut4_Type = Integer32
_TemperatureSensorOut4_Object = MibScalar
temperatureSensorOut4 = _TemperatureSensorOut4_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 2, 8),
    _TemperatureSensorOut4_Type()
)
temperatureSensorOut4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOut4.setStatus("current")
_TemperatureSensorOutSerial5_Type = OctetString
_TemperatureSensorOutSerial5_Object = MibScalar
temperatureSensorOutSerial5 = _TemperatureSensorOutSerial5_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 2, 9),
    _TemperatureSensorOutSerial5_Type()
)
temperatureSensorOutSerial5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOutSerial5.setStatus("current")
_TemperatureSensorOut5_Type = Integer32
_TemperatureSensorOut5_Object = MibScalar
temperatureSensorOut5 = _TemperatureSensorOut5_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 2, 10),
    _TemperatureSensorOut5_Type()
)
temperatureSensorOut5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOut5.setStatus("current")
_VoltageSensor1Contact10_Type = Integer32
_VoltageSensor1Contact10_Object = MibScalar
voltageSensor1Contact10 = _VoltageSensor1Contact10_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 3),
    _VoltageSensor1Contact10_Type()
)
voltageSensor1Contact10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensor1Contact10.setStatus("current")
_SysVoltageAlarm_Type = Integer32
_SysVoltageAlarm_Object = MibScalar
sysVoltageAlarm = _SysVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 4),
    _SysVoltageAlarm_Type()
)
sysVoltageAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysVoltageAlarm.setStatus("current")
_VoltageSensor2Contact11_Type = Integer32
_VoltageSensor2Contact11_Object = MibScalar
voltageSensor2Contact11 = _VoltageSensor2Contact11_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 5),
    _VoltageSensor2Contact11_Type()
)
voltageSensor2Contact11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensor2Contact11.setStatus("current")
_SysVoltage2Alarm_Type = Integer32
_SysVoltage2Alarm_Object = MibScalar
sysVoltage2Alarm = _SysVoltage2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 4, 6),
    _SysVoltage2Alarm_Type()
)
sysVoltage2Alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysVoltage2Alarm.setStatus("current")
_CommS_ObjectIdentity = ObjectIdentity
commS = _CommS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 5)
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 5, 2),
    _TrapMode_Type()
)
trapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapMode.setStatus("current")


class _AlarmSense1Name_Type(DisplayString):
    """Custom type alarmSense1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AlarmSense1Name_Type.__name__ = "DisplayString"
_AlarmSense1Name_Object = MibScalar
alarmSense1Name = _AlarmSense1Name_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 5, 3),
    _AlarmSense1Name_Type()
)
alarmSense1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSense1Name.setStatus("current")


class _AlarmSense2Name_Type(DisplayString):
    """Custom type alarmSense2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AlarmSense2Name_Type.__name__ = "DisplayString"
_AlarmSense2Name_Object = MibScalar
alarmSense2Name = _AlarmSense2Name_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 5, 4),
    _AlarmSense2Name_Type()
)
alarmSense2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSense2Name.setStatus("current")


class _UserSense1Name_Type(DisplayString):
    """Custom type userSense1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UserSense1Name_Type.__name__ = "DisplayString"
_UserSense1Name_Object = MibScalar
userSense1Name = _UserSense1Name_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 5, 5),
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 5, 6),
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 5, 7),
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 5, 10),
    _Message_Type()
)
message.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    message.setStatus("current")

# Managed Objects groups


# Notification objects

temperatureSensorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 0)
)
if mibBuilder.loadTexts:
    temperatureSensorAlarm.setStatus(
        "current"
    )

temperatureSensorRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 1)
)
if mibBuilder.loadTexts:
    temperatureSensorRelease.setStatus(
        "current"
    )

signal1Contact5Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 2)
)
if mibBuilder.loadTexts:
    signal1Contact5Alarm.setStatus(
        "current"
    )

signal1Contact5Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 3)
)
if mibBuilder.loadTexts:
    signal1Contact5Ok.setStatus(
        "current"
    )

signal2Contact6Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 4)
)
if mibBuilder.loadTexts:
    signal2Contact6Alarm.setStatus(
        "current"
    )

signal2Contact6Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 5)
)
if mibBuilder.loadTexts:
    signal2Contact6Ok.setStatus(
        "current"
    )

voltageSignal1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 6)
)
if mibBuilder.loadTexts:
    voltageSignal1Alarm.setStatus(
        "current"
    )

voltageSignal1Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 7)
)
if mibBuilder.loadTexts:
    voltageSignal1Ok.setStatus(
        "current"
    )

voltageSignal2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 8)
)
if mibBuilder.loadTexts:
    voltageSignal2Alarm.setStatus(
        "current"
    )

voltageSignal2Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 9)
)
if mibBuilder.loadTexts:
    voltageSignal2Ok.setStatus(
        "current"
    )

anySensorSignal1contact2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 10)
)
if mibBuilder.loadTexts:
    anySensorSignal1contact2Alarm.setStatus(
        "current"
    )

anySensorSignal1contact2Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 11)
)
if mibBuilder.loadTexts:
    anySensorSignal1contact2Ok.setStatus(
        "current"
    )

anySensorSignal2contact3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 12)
)
if mibBuilder.loadTexts:
    anySensorSignal2contact3Alarm.setStatus(
        "current"
    )

anySensorSignal2contact3Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 13)
)
if mibBuilder.loadTexts:
    anySensorSignal2contact3Ok.setStatus(
        "current"
    )

anySensorSignal3contact4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 14)
)
if mibBuilder.loadTexts:
    anySensorSignal3contact4Alarm.setStatus(
        "current"
    )

anySensorSignal3contact4Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 15)
)
if mibBuilder.loadTexts:
    anySensorSignal3contact4Ok.setStatus(
        "current"
    )

voltage1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 16)
)
if mibBuilder.loadTexts:
    voltage1Alarm.setStatus(
        "current"
    )

voltage1Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 17)
)
if mibBuilder.loadTexts:
    voltage1Ok.setStatus(
        "current"
    )

voltage2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 18)
)
if mibBuilder.loadTexts:
    voltage2Alarm.setStatus(
        "current"
    )

voltage2Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 19)
)
if mibBuilder.loadTexts:
    voltage2Ok.setStatus(
        "current"
    )

remoteControlContact8On = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 20)
)
if mibBuilder.loadTexts:
    remoteControlContact8On.setStatus(
        "current"
    )

remoteControlContact8Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 21)
)
if mibBuilder.loadTexts:
    remoteControlContact8Off.setStatus(
        "current"
    )

resetedSmartContact7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 22)
)
if mibBuilder.loadTexts:
    resetedSmartContact7.setStatus(
        "current"
    )

temperatureSensorOutAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 23)
)
if mibBuilder.loadTexts:
    temperatureSensorOutAlarm.setStatus(
        "current"
    )

temperatureSensorOutRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 24)
)
if mibBuilder.loadTexts:
    temperatureSensorOutRelease.setStatus(
        "current"
    )

temperatureSensorOutFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 25)
)
if mibBuilder.loadTexts:
    temperatureSensorOutFail.setStatus(
        "current"
    )

temperatureSensorOutOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 0, 26)
)
if mibBuilder.loadTexts:
    temperatureSensorOutOk.setStatus(
        "current"
    )


# Notifications groups

erd3TrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 40418, 2, 3, 99)
)
erd3TrapGroup.setObjects(
      *(("SNR-ERD-3", "temperatureSensorAlarm"),
        ("SNR-ERD-3", "temperatureSensorRelease"),
        ("SNR-ERD-3", "signal1Contact5Alarm"),
        ("SNR-ERD-3", "signal1Contact5Ok"),
        ("SNR-ERD-3", "signal2Contact6Alarm"),
        ("SNR-ERD-3", "signal2Contact6Ok"),
        ("SNR-ERD-3", "voltageSignal1Alarm"),
        ("SNR-ERD-3", "voltageSignal1Ok"),
        ("SNR-ERD-3", "voltageSignal2Alarm"),
        ("SNR-ERD-3", "voltageSignal2Ok"),
        ("SNR-ERD-3", "anySensorSignal1contact2Alarm"),
        ("SNR-ERD-3", "anySensorSignal1contact2Ok"),
        ("SNR-ERD-3", "anySensorSignal2contact3Alarm"),
        ("SNR-ERD-3", "anySensorSignal2contact3Ok"),
        ("SNR-ERD-3", "anySensorSignal3contact4Alarm"),
        ("SNR-ERD-3", "anySensorSignal3contact4Ok"),
        ("SNR-ERD-3", "voltage1Alarm"),
        ("SNR-ERD-3", "voltage1Ok"),
        ("SNR-ERD-3", "voltage2Alarm"),
        ("SNR-ERD-3", "voltage2Ok"),
        ("SNR-ERD-3", "remoteControlContact8On"),
        ("SNR-ERD-3", "remoteControlContact8Off"),
        ("SNR-ERD-3", "resetedSmartContact7"),
        ("SNR-ERD-3", "temperatureSensorOutAlarm"),
        ("SNR-ERD-3", "temperatureSensorOutRelease"),
        ("SNR-ERD-3", "temperatureSensorOutFail"),
        ("SNR-ERD-3", "temperatureSensorOutOk"))
)
if mibBuilder.loadTexts:
    erd3TrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNR-ERD-3",
    **{"snr": snr,
       "snr-erd": snr_erd,
       "snr-erd-3": snr_erd_3,
       "erd3Traps": erd3Traps,
       "temperatureSensorAlarm": temperatureSensorAlarm,
       "temperatureSensorRelease": temperatureSensorRelease,
       "signal1Contact5Alarm": signal1Contact5Alarm,
       "signal1Contact5Ok": signal1Contact5Ok,
       "signal2Contact6Alarm": signal2Contact6Alarm,
       "signal2Contact6Ok": signal2Contact6Ok,
       "voltageSignal1Alarm": voltageSignal1Alarm,
       "voltageSignal1Ok": voltageSignal1Ok,
       "voltageSignal2Alarm": voltageSignal2Alarm,
       "voltageSignal2Ok": voltageSignal2Ok,
       "anySensorSignal1contact2Alarm": anySensorSignal1contact2Alarm,
       "anySensorSignal1contact2Ok": anySensorSignal1contact2Ok,
       "anySensorSignal2contact3Alarm": anySensorSignal2contact3Alarm,
       "anySensorSignal2contact3Ok": anySensorSignal2contact3Ok,
       "anySensorSignal3contact4Alarm": anySensorSignal3contact4Alarm,
       "anySensorSignal3contact4Ok": anySensorSignal3contact4Ok,
       "voltage1Alarm": voltage1Alarm,
       "voltage1Ok": voltage1Ok,
       "voltage2Alarm": voltage2Alarm,
       "voltage2Ok": voltage2Ok,
       "remoteControlContact8On": remoteControlContact8On,
       "remoteControlContact8Off": remoteControlContact8Off,
       "resetedSmartContact7": resetedSmartContact7,
       "temperatureSensorOutAlarm": temperatureSensorOutAlarm,
       "temperatureSensorOutRelease": temperatureSensorOutRelease,
       "temperatureSensorOutFail": temperatureSensorOutFail,
       "temperatureSensorOutOk": temperatureSensorOutOk,
       "ipAddressEntry": ipAddressEntry,
       "ipAddress": ipAddress,
       "ipGatewayAddress": ipGatewayAddress,
       "ipMonitoringDevice": ipMonitoringDevice,
       "ipForTrap": ipForTrap,
       "resetsSet": resetsSet,
       "resetSmartContact7": resetSmartContact7,
       "numberOfResetPositives": numberOfResetPositives,
       "remoteControlContact8": remoteControlContact8,
       "sensesSet1": sensesSet1,
       "monitorAlarmSignal1Contact5": monitorAlarmSignal1Contact5,
       "monitorAlarmSignal2Contact6": monitorAlarmSignal2Contact6,
       "numberOfAlarmPositives": numberOfAlarmPositives,
       "monitorAnySensorSignal1contact2": monitorAnySensorSignal1contact2,
       "monitorAnySensorSignal2contact3": monitorAnySensorSignal2contact3,
       "monitorAnySensorSignal3contact4": monitorAnySensorSignal3contact4,
       "monitorVoltageSignal1": monitorVoltageSignal1,
       "monitorVoltageSignal2": monitorVoltageSignal2,
       "sensesSet2": sensesSet2,
       "temperatureSensor": temperatureSensor,
       "temperatureSensorsOut": temperatureSensorsOut,
       "temperatureSensorOutSerial1": temperatureSensorOutSerial1,
       "temperatureSensorOut1": temperatureSensorOut1,
       "temperatureSensorOutSerial2": temperatureSensorOutSerial2,
       "temperatureSensorOut2": temperatureSensorOut2,
       "temperatureSensorOutSerial3": temperatureSensorOutSerial3,
       "temperatureSensorOut3": temperatureSensorOut3,
       "temperatureSensorOutSerial4": temperatureSensorOutSerial4,
       "temperatureSensorOut4": temperatureSensorOut4,
       "temperatureSensorOutSerial5": temperatureSensorOutSerial5,
       "temperatureSensorOut5": temperatureSensorOut5,
       "voltageSensor1Contact10": voltageSensor1Contact10,
       "sysVoltageAlarm": sysVoltageAlarm,
       "voltageSensor2Contact11": voltageSensor2Contact11,
       "sysVoltage2Alarm": sysVoltage2Alarm,
       "commS": commS,
       "communityString": communityString,
       "trapMode": trapMode,
       "alarmSense1Name": alarmSense1Name,
       "alarmSense2Name": alarmSense2Name,
       "userSense1Name": userSense1Name,
       "userSense2Name": userSense2Name,
       "userSense3Name": userSense3Name,
       "message": message,
       "erd3TrapGroup": erd3TrapGroup}
)
