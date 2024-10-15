# SNMP MIB module (SNR-ERD-3s) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNR-ERD-3s
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
 Opaque,
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
    "Opaque",
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



class Float(Opaque, TextualConvention):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )



# MIB Managed Objects in the order of their OIDs

_Snr_erd_ObjectIdentity = ObjectIdentity
snr_erd = _Snr_erd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2)
)
_Snr_erd_3s_ObjectIdentity = ObjectIdentity
snr_erd_3s = _Snr_erd_3s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4)
)
_Erd3sTraps_ObjectIdentity = ObjectIdentity
erd3sTraps = _Erd3sTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0)
)
_IpAddressEntry_ObjectIdentity = ObjectIdentity
ipAddressEntry = _IpAddressEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 1)
)
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 1, 1),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_IpGatewayAddress_Type = IpAddress
_IpGatewayAddress_Object = MibScalar
ipGatewayAddress = _IpGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 1, 2),
    _IpGatewayAddress_Type()
)
ipGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGatewayAddress.setStatus("current")
_IpMonitoringDevice_Type = IpAddress
_IpMonitoringDevice_Object = MibScalar
ipMonitoringDevice = _IpMonitoringDevice_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 1, 3),
    _IpMonitoringDevice_Type()
)
ipMonitoringDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMonitoringDevice.setStatus("current")
_IpForTrap_Type = IpAddress
_IpForTrap_Object = MibScalar
ipForTrap = _IpForTrap_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 1, 4),
    _IpForTrap_Type()
)
ipForTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForTrap.setStatus("current")
_ResetsSet_ObjectIdentity = ObjectIdentity
resetsSet = _ResetsSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 2)
)


class _ResetSmartContact10_Type(Integer32):
    """Custom type resetSmartContact10 based on Integer32"""
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


_ResetSmartContact10_Type.__name__ = "Integer32"
_ResetSmartContact10_Object = MibScalar
resetSmartContact10 = _ResetSmartContact10_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 2, 1),
    _ResetSmartContact10_Type()
)
resetSmartContact10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetSmartContact10.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 2, 2),
    _NumberOfResetPositives_Type()
)
numberOfResetPositives.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfResetPositives.setStatus("current")


class _RemoteControlContact11_Type(Integer32):
    """Custom type remoteControlContact11 based on Integer32"""
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


_RemoteControlContact11_Type.__name__ = "Integer32"
_RemoteControlContact11_Object = MibScalar
remoteControlContact11 = _RemoteControlContact11_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 2, 3),
    _RemoteControlContact11_Type()
)
remoteControlContact11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteControlContact11.setStatus("current")
_SensesSet1_ObjectIdentity = ObjectIdentity
sensesSet1 = _SensesSet1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 3)
)


class _MonitorAlarmSignal1Contact8_Type(Integer32):
    """Custom type monitorAlarmSignal1Contact8 based on Integer32"""
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


_MonitorAlarmSignal1Contact8_Type.__name__ = "Integer32"
_MonitorAlarmSignal1Contact8_Object = MibScalar
monitorAlarmSignal1Contact8 = _MonitorAlarmSignal1Contact8_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 3, 1),
    _MonitorAlarmSignal1Contact8_Type()
)
monitorAlarmSignal1Contact8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAlarmSignal1Contact8.setStatus("current")


class _MonitorAlarmSignal2Contact9_Type(Integer32):
    """Custom type monitorAlarmSignal2Contact9 based on Integer32"""
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


_MonitorAlarmSignal2Contact9_Type.__name__ = "Integer32"
_MonitorAlarmSignal2Contact9_Object = MibScalar
monitorAlarmSignal2Contact9 = _MonitorAlarmSignal2Contact9_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 3, 2),
    _MonitorAlarmSignal2Contact9_Type()
)
monitorAlarmSignal2Contact9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAlarmSignal2Contact9.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 3, 3),
    _NumberOfAlarmPositives_Type()
)
numberOfAlarmPositives.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfAlarmPositives.setStatus("current")


class _MonitorAnySensorSignal1contact5_Type(Integer32):
    """Custom type monitorAnySensorSignal1contact5 based on Integer32"""
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


_MonitorAnySensorSignal1contact5_Type.__name__ = "Integer32"
_MonitorAnySensorSignal1contact5_Object = MibScalar
monitorAnySensorSignal1contact5 = _MonitorAnySensorSignal1contact5_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 3, 4),
    _MonitorAnySensorSignal1contact5_Type()
)
monitorAnySensorSignal1contact5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAnySensorSignal1contact5.setStatus("current")


class _MonitorAnySensorSignal2contact6_Type(Integer32):
    """Custom type monitorAnySensorSignal2contact6 based on Integer32"""
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


_MonitorAnySensorSignal2contact6_Type.__name__ = "Integer32"
_MonitorAnySensorSignal2contact6_Object = MibScalar
monitorAnySensorSignal2contact6 = _MonitorAnySensorSignal2contact6_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 3, 5),
    _MonitorAnySensorSignal2contact6_Type()
)
monitorAnySensorSignal2contact6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAnySensorSignal2contact6.setStatus("current")


class _MonitorAnySensorSignal3contact7_Type(Integer32):
    """Custom type monitorAnySensorSignal3contact7 based on Integer32"""
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


_MonitorAnySensorSignal3contact7_Type.__name__ = "Integer32"
_MonitorAnySensorSignal3contact7_Object = MibScalar
monitorAnySensorSignal3contact7 = _MonitorAnySensorSignal3contact7_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 3, 6),
    _MonitorAnySensorSignal3contact7_Type()
)
monitorAnySensorSignal3contact7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAnySensorSignal3contact7.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 3, 7),
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 3, 8),
    _MonitorVoltageSignal2_Type()
)
monitorVoltageSignal2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorVoltageSignal2.setStatus("current")
_SensesSet2_ObjectIdentity = ObjectIdentity
sensesSet2 = _SensesSet2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4)
)
_TemperatureSensor_Type = Integer32
_TemperatureSensor_Object = MibScalar
temperatureSensor = _TemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 1),
    _TemperatureSensor_Type()
)
temperatureSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor.setStatus("current")
_TemperatureSensorsOut_ObjectIdentity = ObjectIdentity
temperatureSensorsOut = _TemperatureSensorsOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 2)
)
_TemperatureSensorOutSerial1_Type = OctetString
_TemperatureSensorOutSerial1_Object = MibScalar
temperatureSensorOutSerial1 = _TemperatureSensorOutSerial1_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 2, 1),
    _TemperatureSensorOutSerial1_Type()
)
temperatureSensorOutSerial1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOutSerial1.setStatus("current")
_TemperatureSensorOut1_Type = Integer32
_TemperatureSensorOut1_Object = MibScalar
temperatureSensorOut1 = _TemperatureSensorOut1_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 2, 2),
    _TemperatureSensorOut1_Type()
)
temperatureSensorOut1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOut1.setStatus("current")
_TemperatureSensorOutSerial2_Type = OctetString
_TemperatureSensorOutSerial2_Object = MibScalar
temperatureSensorOutSerial2 = _TemperatureSensorOutSerial2_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 2, 3),
    _TemperatureSensorOutSerial2_Type()
)
temperatureSensorOutSerial2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOutSerial2.setStatus("current")
_TemperatureSensorOut2_Type = Integer32
_TemperatureSensorOut2_Object = MibScalar
temperatureSensorOut2 = _TemperatureSensorOut2_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 2, 4),
    _TemperatureSensorOut2_Type()
)
temperatureSensorOut2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOut2.setStatus("current")
_TemperatureSensorOutSerial3_Type = OctetString
_TemperatureSensorOutSerial3_Object = MibScalar
temperatureSensorOutSerial3 = _TemperatureSensorOutSerial3_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 2, 5),
    _TemperatureSensorOutSerial3_Type()
)
temperatureSensorOutSerial3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOutSerial3.setStatus("current")
_TemperatureSensorOut3_Type = Integer32
_TemperatureSensorOut3_Object = MibScalar
temperatureSensorOut3 = _TemperatureSensorOut3_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 2, 6),
    _TemperatureSensorOut3_Type()
)
temperatureSensorOut3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOut3.setStatus("current")
_TemperatureSensorOutSerial4_Type = OctetString
_TemperatureSensorOutSerial4_Object = MibScalar
temperatureSensorOutSerial4 = _TemperatureSensorOutSerial4_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 2, 7),
    _TemperatureSensorOutSerial4_Type()
)
temperatureSensorOutSerial4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOutSerial4.setStatus("current")
_TemperatureSensorOut4_Type = Integer32
_TemperatureSensorOut4_Object = MibScalar
temperatureSensorOut4 = _TemperatureSensorOut4_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 2, 8),
    _TemperatureSensorOut4_Type()
)
temperatureSensorOut4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOut4.setStatus("current")
_TemperatureSensorOutSerial5_Type = OctetString
_TemperatureSensorOutSerial5_Object = MibScalar
temperatureSensorOutSerial5 = _TemperatureSensorOutSerial5_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 2, 9),
    _TemperatureSensorOutSerial5_Type()
)
temperatureSensorOutSerial5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOutSerial5.setStatus("current")
_TemperatureSensorOut5_Type = Integer32
_TemperatureSensorOut5_Object = MibScalar
temperatureSensorOut5 = _TemperatureSensorOut5_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 2, 10),
    _TemperatureSensorOut5_Type()
)
temperatureSensorOut5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorOut5.setStatus("current")
_VoltageSensorContact12_Type = Integer32
_VoltageSensorContact12_Object = MibScalar
voltageSensorContact12 = _VoltageSensorContact12_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 3),
    _VoltageSensorContact12_Type()
)
voltageSensorContact12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorContact12.setStatus("current")
_SysVoltageAlarm_Type = Integer32
_SysVoltageAlarm_Object = MibScalar
sysVoltageAlarm = _SysVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 4, 4),
    _SysVoltageAlarm_Type()
)
sysVoltageAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysVoltageAlarm.setStatus("current")
_CommS_ObjectIdentity = ObjectIdentity
commS = _CommS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 5)
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 5, 5),
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 5, 6),
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
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 5, 7),
    _UserSense3Name_Type()
)
userSense3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSense3Name.setStatus("current")


class _DataType_Type(Integer32):
    """Custom type dataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("float", 1),
          ("integer", 0),
          ("uni", 2))
    )


_DataType_Type.__name__ = "Integer32"
_DataType_Object = MibScalar
dataType = _DataType_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 5, 10),
    _DataType_Type()
)
dataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataType.setStatus("current")
_UpsMonitoring_ObjectIdentity = ObjectIdentity
upsMonitoring = _UpsMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 6)
)
_BatteryVoltage_Type = Float
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 6, 1),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("current")
_UpsTemperature_Type = Float
_UpsTemperature_Object = MibScalar
upsTemperature = _UpsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 6, 2),
    _UpsTemperature_Type()
)
upsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTemperature.setStatus("current")
_InputVoltage_Type = Float
_InputVoltage_Object = MibScalar
inputVoltage = _InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 6, 3),
    _InputVoltage_Type()
)
inputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltage.setStatus("current")
_OutputVoltage_Type = Float
_OutputVoltage_Object = MibScalar
outputVoltage = _OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 6, 4),
    _OutputVoltage_Type()
)
outputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputVoltage.setStatus("current")
_UpsLoading_Type = Integer32
_UpsLoading_Object = MibScalar
upsLoading = _UpsLoading_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 6, 5),
    _UpsLoading_Type()
)
upsLoading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsLoading.setStatus("current")


class _UpsStatus_Type(Integer32):
    """Custom type upsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 2),
          ("utilityFail", 1),
          ("utilityOk", 0))
    )


_UpsStatus_Type.__name__ = "Integer32"
_UpsStatus_Object = MibScalar
upsStatus = _UpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 6, 6),
    _UpsStatus_Type()
)
upsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsStatus.setStatus("current")

# Managed Objects groups


# Notification objects

temperatureSensorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 0)
)
if mibBuilder.loadTexts:
    temperatureSensorAlarm.setStatus(
        "current"
    )

temperatureSensorRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 1)
)
if mibBuilder.loadTexts:
    temperatureSensorRelease.setStatus(
        "current"
    )

signal1Contact8Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 2)
)
if mibBuilder.loadTexts:
    signal1Contact8Alarm.setStatus(
        "current"
    )

signal1Contact8Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 3)
)
if mibBuilder.loadTexts:
    signal1Contact8Ok.setStatus(
        "current"
    )

signal2Contact9Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 4)
)
if mibBuilder.loadTexts:
    signal2Contact9Alarm.setStatus(
        "current"
    )

signal2Contact9Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 5)
)
if mibBuilder.loadTexts:
    signal2Contact9Ok.setStatus(
        "current"
    )

voltageSignal1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 6)
)
if mibBuilder.loadTexts:
    voltageSignal1Alarm.setStatus(
        "current"
    )

voltageSignal1Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 7)
)
if mibBuilder.loadTexts:
    voltageSignal1Ok.setStatus(
        "current"
    )

voltageSignal2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 8)
)
if mibBuilder.loadTexts:
    voltageSignal2Alarm.setStatus(
        "current"
    )

voltageSignal2Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 9)
)
if mibBuilder.loadTexts:
    voltageSignal2Ok.setStatus(
        "current"
    )

anySensorSignal1contact5Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 10)
)
if mibBuilder.loadTexts:
    anySensorSignal1contact5Alarm.setStatus(
        "current"
    )

anySensorSignal1contact5Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 11)
)
if mibBuilder.loadTexts:
    anySensorSignal1contact5Ok.setStatus(
        "current"
    )

anySensorSignal2contact6Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 12)
)
if mibBuilder.loadTexts:
    anySensorSignal2contact6Alarm.setStatus(
        "current"
    )

anySensorSignal2contact6Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 13)
)
if mibBuilder.loadTexts:
    anySensorSignal2contact6Ok.setStatus(
        "current"
    )

anySensorSignal3contact7Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 14)
)
if mibBuilder.loadTexts:
    anySensorSignal3contact7Alarm.setStatus(
        "current"
    )

anySensorSignal3contact7Ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 15)
)
if mibBuilder.loadTexts:
    anySensorSignal3contact7Ok.setStatus(
        "current"
    )

voltageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 16)
)
if mibBuilder.loadTexts:
    voltageAlarm.setStatus(
        "current"
    )

voltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 17)
)
if mibBuilder.loadTexts:
    voltageOk.setStatus(
        "current"
    )

remoteControlContact11On = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 18)
)
if mibBuilder.loadTexts:
    remoteControlContact11On.setStatus(
        "current"
    )

remoteControlContact11Off = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 19)
)
if mibBuilder.loadTexts:
    remoteControlContact11Off.setStatus(
        "current"
    )

resetedSmartContact10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 20)
)
if mibBuilder.loadTexts:
    resetedSmartContact10.setStatus(
        "current"
    )

temperatureSensorOutAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 23)
)
if mibBuilder.loadTexts:
    temperatureSensorOutAlarm.setStatus(
        "current"
    )

temperatureSensorOutRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 24)
)
if mibBuilder.loadTexts:
    temperatureSensorOutRelease.setStatus(
        "current"
    )

temperatureSensorOutFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 25)
)
if mibBuilder.loadTexts:
    temperatureSensorOutFail.setStatus(
        "current"
    )

temperatureSensorOutOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 26)
)
if mibBuilder.loadTexts:
    temperatureSensorOutOk.setStatus(
        "current"
    )

upsUtilityFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 30)
)
if mibBuilder.loadTexts:
    upsUtilityFail.setStatus(
        "current"
    )

upsUtilityOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 0, 31)
)
if mibBuilder.loadTexts:
    upsUtilityOk.setStatus(
        "current"
    )


# Notifications groups

erd3sTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 40418, 2, 4, 99)
)
erd3sTrapGroup.setObjects(
      *(("SNR-ERD-3s", "temperatureSensorAlarm"),
        ("SNR-ERD-3s", "temperatureSensorRelease"),
        ("SNR-ERD-3s", "signal1Contact8Alarm"),
        ("SNR-ERD-3s", "signal1Contact8Ok"),
        ("SNR-ERD-3s", "signal2Contact9Alarm"),
        ("SNR-ERD-3s", "signal2Contact9Ok"),
        ("SNR-ERD-3s", "voltageSignal1Alarm"),
        ("SNR-ERD-3s", "voltageSignal1Ok"),
        ("SNR-ERD-3s", "voltageSignal2Alarm"),
        ("SNR-ERD-3s", "voltageSignal2Ok"),
        ("SNR-ERD-3s", "anySensorSignal1contact5Alarm"),
        ("SNR-ERD-3s", "anySensorSignal1contact5Ok"),
        ("SNR-ERD-3s", "anySensorSignal2contact6Alarm"),
        ("SNR-ERD-3s", "anySensorSignal2contact6Ok"),
        ("SNR-ERD-3s", "anySensorSignal3contact7Alarm"),
        ("SNR-ERD-3s", "anySensorSignal3contact7Ok"),
        ("SNR-ERD-3s", "voltageAlarm"),
        ("SNR-ERD-3s", "voltageOk"),
        ("SNR-ERD-3s", "remoteControlContact11On"),
        ("SNR-ERD-3s", "remoteControlContact11Off"),
        ("SNR-ERD-3s", "resetedSmartContact10"),
        ("SNR-ERD-3s", "temperatureSensorOutAlarm"),
        ("SNR-ERD-3s", "temperatureSensorOutRelease"),
        ("SNR-ERD-3s", "temperatureSensorOutFail"),
        ("SNR-ERD-3s", "temperatureSensorOutOk"),
        ("SNR-ERD-3s", "upsUtilityFail"),
        ("SNR-ERD-3s", "upsUtilityOk"))
)
if mibBuilder.loadTexts:
    erd3sTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNR-ERD-3s",
    **{"Float": Float,
       "snr": snr,
       "snr-erd": snr_erd,
       "snr-erd-3s": snr_erd_3s,
       "erd3sTraps": erd3sTraps,
       "temperatureSensorAlarm": temperatureSensorAlarm,
       "temperatureSensorRelease": temperatureSensorRelease,
       "signal1Contact8Alarm": signal1Contact8Alarm,
       "signal1Contact8Ok": signal1Contact8Ok,
       "signal2Contact9Alarm": signal2Contact9Alarm,
       "signal2Contact9Ok": signal2Contact9Ok,
       "voltageSignal1Alarm": voltageSignal1Alarm,
       "voltageSignal1Ok": voltageSignal1Ok,
       "voltageSignal2Alarm": voltageSignal2Alarm,
       "voltageSignal2Ok": voltageSignal2Ok,
       "anySensorSignal1contact5Alarm": anySensorSignal1contact5Alarm,
       "anySensorSignal1contact5Ok": anySensorSignal1contact5Ok,
       "anySensorSignal2contact6Alarm": anySensorSignal2contact6Alarm,
       "anySensorSignal2contact6Ok": anySensorSignal2contact6Ok,
       "anySensorSignal3contact7Alarm": anySensorSignal3contact7Alarm,
       "anySensorSignal3contact7Ok": anySensorSignal3contact7Ok,
       "voltageAlarm": voltageAlarm,
       "voltageOk": voltageOk,
       "remoteControlContact11On": remoteControlContact11On,
       "remoteControlContact11Off": remoteControlContact11Off,
       "resetedSmartContact10": resetedSmartContact10,
       "temperatureSensorOutAlarm": temperatureSensorOutAlarm,
       "temperatureSensorOutRelease": temperatureSensorOutRelease,
       "temperatureSensorOutFail": temperatureSensorOutFail,
       "temperatureSensorOutOk": temperatureSensorOutOk,
       "upsUtilityFail": upsUtilityFail,
       "upsUtilityOk": upsUtilityOk,
       "ipAddressEntry": ipAddressEntry,
       "ipAddress": ipAddress,
       "ipGatewayAddress": ipGatewayAddress,
       "ipMonitoringDevice": ipMonitoringDevice,
       "ipForTrap": ipForTrap,
       "resetsSet": resetsSet,
       "resetSmartContact10": resetSmartContact10,
       "numberOfResetPositives": numberOfResetPositives,
       "remoteControlContact11": remoteControlContact11,
       "sensesSet1": sensesSet1,
       "monitorAlarmSignal1Contact8": monitorAlarmSignal1Contact8,
       "monitorAlarmSignal2Contact9": monitorAlarmSignal2Contact9,
       "numberOfAlarmPositives": numberOfAlarmPositives,
       "monitorAnySensorSignal1contact5": monitorAnySensorSignal1contact5,
       "monitorAnySensorSignal2contact6": monitorAnySensorSignal2contact6,
       "monitorAnySensorSignal3contact7": monitorAnySensorSignal3contact7,
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
       "voltageSensorContact12": voltageSensorContact12,
       "sysVoltageAlarm": sysVoltageAlarm,
       "commS": commS,
       "communityString": communityString,
       "trapMode": trapMode,
       "alarmSense1Name": alarmSense1Name,
       "alarmSense2Name": alarmSense2Name,
       "userSense1Name": userSense1Name,
       "userSense2Name": userSense2Name,
       "userSense3Name": userSense3Name,
       "dataType": dataType,
       "upsMonitoring": upsMonitoring,
       "batteryVoltage": batteryVoltage,
       "upsTemperature": upsTemperature,
       "inputVoltage": inputVoltage,
       "outputVoltage": outputVoltage,
       "upsLoading": upsLoading,
       "upsStatus": upsStatus,
       "erd3sTrapGroup": erd3sTrapGroup}
)
