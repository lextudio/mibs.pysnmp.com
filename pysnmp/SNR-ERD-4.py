# SNMP MIB module (SNR-ERD-4) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNR-ERD-4
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:26 2024
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
_Snr_erd_4_ObjectIdentity = ObjectIdentity
snr_erd_4 = _Snr_erd_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6)
)
_Erd4Traps_ObjectIdentity = ObjectIdentity
erd4Traps = _Erd4Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0)
)
_Measurements_ObjectIdentity = ObjectIdentity
measurements = _Measurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1)
)
_SnrSensors_ObjectIdentity = ObjectIdentity
snrSensors = _SnrSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1)
)
_TemperatureSensors_ObjectIdentity = ObjectIdentity
temperatureSensors = _TemperatureSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1)
)
_TemperatureS1_Type = Integer32
_TemperatureS1_Object = MibScalar
temperatureS1 = _TemperatureS1_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 1),
    _TemperatureS1_Type()
)
temperatureS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureS1.setStatus("current")
_TemperatureS2_Type = Integer32
_TemperatureS2_Object = MibScalar
temperatureS2 = _TemperatureS2_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 2),
    _TemperatureS2_Type()
)
temperatureS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureS2.setStatus("current")
_TemperatureS3_Type = Integer32
_TemperatureS3_Object = MibScalar
temperatureS3 = _TemperatureS3_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 3),
    _TemperatureS3_Type()
)
temperatureS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureS3.setStatus("current")
_TemperatureS4_Type = Integer32
_TemperatureS4_Object = MibScalar
temperatureS4 = _TemperatureS4_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 4),
    _TemperatureS4_Type()
)
temperatureS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureS4.setStatus("current")
_TemperatureS5_Type = Integer32
_TemperatureS5_Object = MibScalar
temperatureS5 = _TemperatureS5_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 5),
    _TemperatureS5_Type()
)
temperatureS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureS5.setStatus("current")
_TemperatureS6_Type = Integer32
_TemperatureS6_Object = MibScalar
temperatureS6 = _TemperatureS6_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 6),
    _TemperatureS6_Type()
)
temperatureS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureS6.setStatus("current")
_TemperatureS7_Type = Integer32
_TemperatureS7_Object = MibScalar
temperatureS7 = _TemperatureS7_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 7),
    _TemperatureS7_Type()
)
temperatureS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureS7.setStatus("current")
_TemperatureS8_Type = Integer32
_TemperatureS8_Object = MibScalar
temperatureS8 = _TemperatureS8_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 8),
    _TemperatureS8_Type()
)
temperatureS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureS8.setStatus("current")
_TemperatureS9_Type = Integer32
_TemperatureS9_Object = MibScalar
temperatureS9 = _TemperatureS9_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 9),
    _TemperatureS9_Type()
)
temperatureS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureS9.setStatus("current")
_TemperatureS10_Type = Integer32
_TemperatureS10_Object = MibScalar
temperatureS10 = _TemperatureS10_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 10),
    _TemperatureS10_Type()
)
temperatureS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureS10.setStatus("current")
_PowerSensors_ObjectIdentity = ObjectIdentity
powerSensors = _PowerSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2)
)
_VoltageS1_Type = Integer32
_VoltageS1_Object = MibScalar
voltageS1 = _VoltageS1_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 1),
    _VoltageS1_Type()
)
voltageS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageS1.setStatus("current")
_CurrentS1_Type = Integer32
_CurrentS1_Object = MibScalar
currentS1 = _CurrentS1_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 2),
    _CurrentS1_Type()
)
currentS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentS1.setStatus("current")
_VoltageS2_Type = Integer32
_VoltageS2_Object = MibScalar
voltageS2 = _VoltageS2_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 4),
    _VoltageS2_Type()
)
voltageS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageS2.setStatus("current")
_CurrentS2_Type = Integer32
_CurrentS2_Object = MibScalar
currentS2 = _CurrentS2_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 5),
    _CurrentS2_Type()
)
currentS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentS2.setStatus("current")
_VoltageS3_Type = Integer32
_VoltageS3_Object = MibScalar
voltageS3 = _VoltageS3_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 7),
    _VoltageS3_Type()
)
voltageS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageS3.setStatus("current")
_CurrentS3_Type = Integer32
_CurrentS3_Object = MibScalar
currentS3 = _CurrentS3_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 8),
    _CurrentS3_Type()
)
currentS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentS3.setStatus("current")
_VoltageS4_Type = Integer32
_VoltageS4_Object = MibScalar
voltageS4 = _VoltageS4_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 10),
    _VoltageS4_Type()
)
voltageS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageS4.setStatus("current")
_CurrentS4_Type = Integer32
_CurrentS4_Object = MibScalar
currentS4 = _CurrentS4_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 11),
    _CurrentS4_Type()
)
currentS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentS4.setStatus("current")
_VoltageS5_Type = Integer32
_VoltageS5_Object = MibScalar
voltageS5 = _VoltageS5_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 13),
    _VoltageS5_Type()
)
voltageS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageS5.setStatus("current")
_CurrentS5_Type = Integer32
_CurrentS5_Object = MibScalar
currentS5 = _CurrentS5_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 14),
    _CurrentS5_Type()
)
currentS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentS5.setStatus("current")
_VoltageS6_Type = Integer32
_VoltageS6_Object = MibScalar
voltageS6 = _VoltageS6_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 16),
    _VoltageS6_Type()
)
voltageS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageS6.setStatus("current")
_CurrentS6_Type = Integer32
_CurrentS6_Object = MibScalar
currentS6 = _CurrentS6_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 17),
    _CurrentS6_Type()
)
currentS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentS6.setStatus("current")
_VoltageS7_Type = Integer32
_VoltageS7_Object = MibScalar
voltageS7 = _VoltageS7_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 19),
    _VoltageS7_Type()
)
voltageS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageS7.setStatus("current")
_CurrentS7_Type = Integer32
_CurrentS7_Object = MibScalar
currentS7 = _CurrentS7_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 20),
    _CurrentS7_Type()
)
currentS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentS7.setStatus("current")
_VoltageS8_Type = Integer32
_VoltageS8_Object = MibScalar
voltageS8 = _VoltageS8_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 22),
    _VoltageS8_Type()
)
voltageS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageS8.setStatus("current")
_CurrentS8_Type = Integer32
_CurrentS8_Object = MibScalar
currentS8 = _CurrentS8_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 23),
    _CurrentS8_Type()
)
currentS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentS8.setStatus("current")
_VoltageS9_Type = Integer32
_VoltageS9_Object = MibScalar
voltageS9 = _VoltageS9_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 25),
    _VoltageS9_Type()
)
voltageS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageS9.setStatus("current")
_CurrentS9_Type = Integer32
_CurrentS9_Object = MibScalar
currentS9 = _CurrentS9_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 26),
    _CurrentS9_Type()
)
currentS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentS9.setStatus("current")
_VoltageS10_Type = Integer32
_VoltageS10_Object = MibScalar
voltageS10 = _VoltageS10_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 28),
    _VoltageS10_Type()
)
voltageS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageS10.setStatus("current")
_CurrentS10_Type = Integer32
_CurrentS10_Object = MibScalar
currentS10 = _CurrentS10_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 29),
    _CurrentS10_Type()
)
currentS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentS10.setStatus("current")
_SerialS1_Type = OctetString
_SerialS1_Object = MibScalar
serialS1 = _SerialS1_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 10),
    _SerialS1_Type()
)
serialS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialS1.setStatus("current")
_SerialS2_Type = OctetString
_SerialS2_Object = MibScalar
serialS2 = _SerialS2_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 11),
    _SerialS2_Type()
)
serialS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialS2.setStatus("current")
_SerialS3_Type = OctetString
_SerialS3_Object = MibScalar
serialS3 = _SerialS3_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 12),
    _SerialS3_Type()
)
serialS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialS3.setStatus("current")
_SerialS4_Type = OctetString
_SerialS4_Object = MibScalar
serialS4 = _SerialS4_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 13),
    _SerialS4_Type()
)
serialS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialS4.setStatus("current")
_SerialS5_Type = OctetString
_SerialS5_Object = MibScalar
serialS5 = _SerialS5_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 14),
    _SerialS5_Type()
)
serialS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialS5.setStatus("current")
_SerialS6_Type = OctetString
_SerialS6_Object = MibScalar
serialS6 = _SerialS6_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 15),
    _SerialS6_Type()
)
serialS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialS6.setStatus("current")
_SerialS7_Type = OctetString
_SerialS7_Object = MibScalar
serialS7 = _SerialS7_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 16),
    _SerialS7_Type()
)
serialS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialS7.setStatus("current")
_SerialS8_Type = OctetString
_SerialS8_Object = MibScalar
serialS8 = _SerialS8_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 17),
    _SerialS8_Type()
)
serialS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialS8.setStatus("current")
_SerialS9_Type = OctetString
_SerialS9_Object = MibScalar
serialS9 = _SerialS9_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 18),
    _SerialS9_Type()
)
serialS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialS9.setStatus("current")
_SerialS10_Type = OctetString
_SerialS10_Object = MibScalar
serialS10 = _SerialS10_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 19),
    _SerialS10_Type()
)
serialS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialS10.setStatus("current")
_VoltageSensor_Type = Integer32
_VoltageSensor_Object = MibScalar
voltageSensor = _VoltageSensor_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 2),
    _VoltageSensor_Type()
)
voltageSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensor.setStatus("current")
_Sensesstate_ObjectIdentity = ObjectIdentity
sensesstate = _Sensesstate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 2)
)


class _AlarmSensor1_Type(Integer32):
    """Custom type alarmSensor1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0),
          ("off", 2))
    )


_AlarmSensor1_Type.__name__ = "Integer32"
_AlarmSensor1_Object = MibScalar
alarmSensor1 = _AlarmSensor1_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 2, 1),
    _AlarmSensor1_Type()
)
alarmSensor1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSensor1.setStatus("current")


class _AlarmSensor2_Type(Integer32):
    """Custom type alarmSensor2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0),
          ("off", 2))
    )


_AlarmSensor2_Type.__name__ = "Integer32"
_AlarmSensor2_Object = MibScalar
alarmSensor2 = _AlarmSensor2_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 2, 2),
    _AlarmSensor2_Type()
)
alarmSensor2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSensor2.setStatus("current")


class _AlarmSensor3_Type(Integer32):
    """Custom type alarmSensor3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0),
          ("off", 2))
    )


_AlarmSensor3_Type.__name__ = "Integer32"
_AlarmSensor3_Object = MibScalar
alarmSensor3 = _AlarmSensor3_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 2, 3),
    _AlarmSensor3_Type()
)
alarmSensor3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSensor3.setStatus("current")


class _AlarmSensor4_Type(Integer32):
    """Custom type alarmSensor4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0),
          ("off", 2))
    )


_AlarmSensor4_Type.__name__ = "Integer32"
_AlarmSensor4_Object = MibScalar
alarmSensor4 = _AlarmSensor4_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 2, 4),
    _AlarmSensor4_Type()
)
alarmSensor4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSensor4.setStatus("current")


class _AlarmSensor5_Type(Integer32):
    """Custom type alarmSensor5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0),
          ("off", 2))
    )


_AlarmSensor5_Type.__name__ = "Integer32"
_AlarmSensor5_Object = MibScalar
alarmSensor5 = _AlarmSensor5_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 2, 5),
    _AlarmSensor5_Type()
)
alarmSensor5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSensor5.setStatus("current")


class _USensor_Type(Integer32):
    """Custom type uSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_USensor_Type.__name__ = "Integer32"
_USensor_Object = MibScalar
uSensor = _USensor_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 2, 6),
    _USensor_Type()
)
uSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uSensor.setStatus("current")
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3)
)


class _ReleState_Type(Integer32):
    """Custom type releState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("reset", 2))
    )


_ReleState_Type.__name__ = "Integer32"
_ReleState_Object = MibScalar
releState = _ReleState_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 1),
    _ReleState_Type()
)
releState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    releState.setStatus("current")


class _Smart1State_Type(Integer32):
    """Custom type smart1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("reset", 2))
    )


_Smart1State_Type.__name__ = "Integer32"
_Smart1State_Object = MibScalar
smart1State = _Smart1State_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 2),
    _Smart1State_Type()
)
smart1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smart1State.setStatus("current")


class _Smart2State_Type(Integer32):
    """Custom type smart2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("reset", 2))
    )


_Smart2State_Type.__name__ = "Integer32"
_Smart2State_Object = MibScalar
smart2State = _Smart2State_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 3),
    _Smart2State_Type()
)
smart2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smart2State.setStatus("current")


class _Smart3State_Type(Integer32):
    """Custom type smart3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("reset", 2))
    )


_Smart3State_Type.__name__ = "Integer32"
_Smart3State_Object = MibScalar
smart3State = _Smart3State_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 4),
    _Smart3State_Type()
)
smart3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smart3State.setStatus("current")


class _Smart4State_Type(Integer32):
    """Custom type smart4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("reset", 2))
    )


_Smart4State_Type.__name__ = "Integer32"
_Smart4State_Object = MibScalar
smart4State = _Smart4State_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 5),
    _Smart4State_Type()
)
smart4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smart4State.setStatus("current")


class _Smart5State_Type(Integer32):
    """Custom type smart5State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("reset", 2))
    )


_Smart5State_Type.__name__ = "Integer32"
_Smart5State_Object = MibScalar
smart5State = _Smart5State_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 6),
    _Smart5State_Type()
)
smart5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smart5State.setStatus("current")
_ReleResetTime_Type = Integer32
_ReleResetTime_Object = MibScalar
releResetTime = _ReleResetTime_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 11),
    _ReleResetTime_Type()
)
releResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    releResetTime.setStatus("current")
_Smart1ResetTime_Type = Integer32
_Smart1ResetTime_Object = MibScalar
smart1ResetTime = _Smart1ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 12),
    _Smart1ResetTime_Type()
)
smart1ResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smart1ResetTime.setStatus("current")
_Smart2ResetTime_Type = Integer32
_Smart2ResetTime_Object = MibScalar
smart2ResetTime = _Smart2ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 13),
    _Smart2ResetTime_Type()
)
smart2ResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smart2ResetTime.setStatus("current")
_Smart3ResetTime_Type = Integer32
_Smart3ResetTime_Object = MibScalar
smart3ResetTime = _Smart3ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 14),
    _Smart3ResetTime_Type()
)
smart3ResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smart3ResetTime.setStatus("current")
_Smart4ResetTime_Type = Integer32
_Smart4ResetTime_Object = MibScalar
smart4ResetTime = _Smart4ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 15),
    _Smart4ResetTime_Type()
)
smart4ResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smart4ResetTime.setStatus("current")
_Smart5ResetTime_Type = Integer32
_Smart5ResetTime_Object = MibScalar
smart5ResetTime = _Smart5ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 16),
    _Smart5ResetTime_Type()
)
smart5ResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smart5ResetTime.setStatus("current")
_Counters_ObjectIdentity = ObjectIdentity
counters = _Counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 8)
)
_AlarmSensCnts_ObjectIdentity = ObjectIdentity
alarmSensCnts = _AlarmSensCnts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 8, 2)
)
_AlarmSensor1cnt_Type = Counter32
_AlarmSensor1cnt_Object = MibScalar
alarmSensor1cnt = _AlarmSensor1cnt_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 8, 2, 1),
    _AlarmSensor1cnt_Type()
)
alarmSensor1cnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSensor1cnt.setStatus("current")
_AlarmSensor2cnt_Type = Counter32
_AlarmSensor2cnt_Object = MibScalar
alarmSensor2cnt = _AlarmSensor2cnt_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 8, 2, 2),
    _AlarmSensor2cnt_Type()
)
alarmSensor2cnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSensor2cnt.setStatus("current")
_AlarmSensor3cnt_Type = Counter32
_AlarmSensor3cnt_Object = MibScalar
alarmSensor3cnt = _AlarmSensor3cnt_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 8, 2, 3),
    _AlarmSensor3cnt_Type()
)
alarmSensor3cnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSensor3cnt.setStatus("current")
_AlarmSensor4cnt_Type = Counter32
_AlarmSensor4cnt_Object = MibScalar
alarmSensor4cnt = _AlarmSensor4cnt_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 8, 2, 4),
    _AlarmSensor4cnt_Type()
)
alarmSensor4cnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSensor4cnt.setStatus("current")
_AlarmSensor5cnt_Type = Counter32
_AlarmSensor5cnt_Object = MibScalar
alarmSensor5cnt = _AlarmSensor5cnt_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 8, 2, 5),
    _AlarmSensor5cnt_Type()
)
alarmSensor5cnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSensor5cnt.setStatus("current")
_Options_ObjectIdentity = ObjectIdentity
options = _Options_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 10)
)


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
          ("ufloat", 2))
    )


_DataType_Type.__name__ = "Integer32"
_DataType_Object = MibScalar
dataType = _DataType_Object(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 10, 1),
    _DataType_Type()
)
dataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataType.setStatus("current")

# Managed Objects groups


# Notification objects

aSense1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 1)
)
if mibBuilder.loadTexts:
    aSense1Alarm.setStatus(
        "current"
    )

aSense1Release = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 2)
)
if mibBuilder.loadTexts:
    aSense1Release.setStatus(
        "current"
    )

aSense2Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 3)
)
if mibBuilder.loadTexts:
    aSense2Alarm.setStatus(
        "current"
    )

aSense2Release = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 4)
)
if mibBuilder.loadTexts:
    aSense2Release.setStatus(
        "current"
    )

aSense3Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 5)
)
if mibBuilder.loadTexts:
    aSense3Alarm.setStatus(
        "current"
    )

aSense3Release = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 6)
)
if mibBuilder.loadTexts:
    aSense3Release.setStatus(
        "current"
    )

aSense4Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 7)
)
if mibBuilder.loadTexts:
    aSense4Alarm.setStatus(
        "current"
    )

aSense4Release = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 8)
)
if mibBuilder.loadTexts:
    aSense4Release.setStatus(
        "current"
    )

aSense5Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 9)
)
if mibBuilder.loadTexts:
    aSense5Alarm.setStatus(
        "current"
    )

aSense5Release = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 10)
)
if mibBuilder.loadTexts:
    aSense5Release.setStatus(
        "current"
    )

uSenseAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 11)
)
if mibBuilder.loadTexts:
    uSenseAlarm.setStatus(
        "current"
    )

uSenseRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 12)
)
if mibBuilder.loadTexts:
    uSenseRelease.setStatus(
        "current"
    )

reloutThermoOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 13)
)
if mibBuilder.loadTexts:
    reloutThermoOn.setStatus(
        "current"
    )

reloutThermoOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 14)
)
if mibBuilder.loadTexts:
    reloutThermoOff.setStatus(
        "current"
    )

smart1ThermoOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 15)
)
if mibBuilder.loadTexts:
    smart1ThermoOn.setStatus(
        "current"
    )

smart1ThermoOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 16)
)
if mibBuilder.loadTexts:
    smart1ThermoOff.setStatus(
        "current"
    )

smart2ThermoOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 17)
)
if mibBuilder.loadTexts:
    smart2ThermoOn.setStatus(
        "current"
    )

smart2ThermoOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 18)
)
if mibBuilder.loadTexts:
    smart2ThermoOff.setStatus(
        "current"
    )

smart3ThermoOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 19)
)
if mibBuilder.loadTexts:
    smart3ThermoOn.setStatus(
        "current"
    )

smart3ThermoOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 20)
)
if mibBuilder.loadTexts:
    smart3ThermoOff.setStatus(
        "current"
    )

smart4ThermoOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 21)
)
if mibBuilder.loadTexts:
    smart4ThermoOn.setStatus(
        "current"
    )

smart4ThermoOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 22)
)
if mibBuilder.loadTexts:
    smart4ThermoOff.setStatus(
        "current"
    )

smart5ThermoOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 23)
)
if mibBuilder.loadTexts:
    smart5ThermoOn.setStatus(
        "current"
    )

smart5ThermoOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 24)
)
if mibBuilder.loadTexts:
    smart5ThermoOff.setStatus(
        "current"
    )

tempSensorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 29)
)
if mibBuilder.loadTexts:
    tempSensorAlarm.setStatus(
        "current"
    )

tempSensorRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 30)
)
if mibBuilder.loadTexts:
    tempSensorRelease.setStatus(
        "current"
    )

voltSensorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 31)
)
if mibBuilder.loadTexts:
    voltSensorAlarm.setStatus(
        "current"
    )

voltSensorRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 32)
)
if mibBuilder.loadTexts:
    voltSensorRelease.setStatus(
        "current"
    )

task1Done = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 36)
)
if mibBuilder.loadTexts:
    task1Done.setStatus(
        "current"
    )

task2Done = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 37)
)
if mibBuilder.loadTexts:
    task2Done.setStatus(
        "current"
    )

task3Done = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 38)
)
if mibBuilder.loadTexts:
    task3Done.setStatus(
        "current"
    )

task4Done = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 39)
)
if mibBuilder.loadTexts:
    task4Done.setStatus(
        "current"
    )

pingLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 45)
)
if mibBuilder.loadTexts:
    pingLost.setStatus(
        "current"
    )

batteryChargeLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 47)
)
if mibBuilder.loadTexts:
    batteryChargeLow.setStatus(
        "current"
    )


# Notifications groups

erd4Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 40418, 2, 6, 99)
)
erd4Group.setObjects(
      *(("SNR-ERD-4", "aSense1Alarm"),
        ("SNR-ERD-4", "aSense1Release"),
        ("SNR-ERD-4", "aSense2Alarm"),
        ("SNR-ERD-4", "aSense2Release"),
        ("SNR-ERD-4", "aSense3Alarm"),
        ("SNR-ERD-4", "aSense3Release"),
        ("SNR-ERD-4", "aSense4Alarm"),
        ("SNR-ERD-4", "aSense4Release"),
        ("SNR-ERD-4", "aSense5Alarm"),
        ("SNR-ERD-4", "aSense5Release"),
        ("SNR-ERD-4", "uSenseAlarm"),
        ("SNR-ERD-4", "uSenseRelease"),
        ("SNR-ERD-4", "reloutThermoOn"),
        ("SNR-ERD-4", "reloutThermoOff"),
        ("SNR-ERD-4", "smart1ThermoOn"),
        ("SNR-ERD-4", "smart1ThermoOff"),
        ("SNR-ERD-4", "smart2ThermoOn"),
        ("SNR-ERD-4", "smart2ThermoOff"),
        ("SNR-ERD-4", "smart3ThermoOn"),
        ("SNR-ERD-4", "smart3ThermoOff"),
        ("SNR-ERD-4", "smart4ThermoOn"),
        ("SNR-ERD-4", "smart4ThermoOff"),
        ("SNR-ERD-4", "smart5ThermoOn"),
        ("SNR-ERD-4", "smart5ThermoOff"),
        ("SNR-ERD-4", "tempSensorAlarm"),
        ("SNR-ERD-4", "tempSensorRelease"),
        ("SNR-ERD-4", "voltSensorAlarm"),
        ("SNR-ERD-4", "voltSensorRelease"),
        ("SNR-ERD-4", "task1Done"),
        ("SNR-ERD-4", "task2Done"),
        ("SNR-ERD-4", "task3Done"),
        ("SNR-ERD-4", "task4Done"),
        ("SNR-ERD-4", "pingLost"),
        ("SNR-ERD-4", "batteryChargeLow"))
)
if mibBuilder.loadTexts:
    erd4Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNR-ERD-4",
    **{"snr": snr,
       "snr-erd": snr_erd,
       "snr-erd-4": snr_erd_4,
       "erd4Traps": erd4Traps,
       "aSense1Alarm": aSense1Alarm,
       "aSense1Release": aSense1Release,
       "aSense2Alarm": aSense2Alarm,
       "aSense2Release": aSense2Release,
       "aSense3Alarm": aSense3Alarm,
       "aSense3Release": aSense3Release,
       "aSense4Alarm": aSense4Alarm,
       "aSense4Release": aSense4Release,
       "aSense5Alarm": aSense5Alarm,
       "aSense5Release": aSense5Release,
       "uSenseAlarm": uSenseAlarm,
       "uSenseRelease": uSenseRelease,
       "reloutThermoOn": reloutThermoOn,
       "reloutThermoOff": reloutThermoOff,
       "smart1ThermoOn": smart1ThermoOn,
       "smart1ThermoOff": smart1ThermoOff,
       "smart2ThermoOn": smart2ThermoOn,
       "smart2ThermoOff": smart2ThermoOff,
       "smart3ThermoOn": smart3ThermoOn,
       "smart3ThermoOff": smart3ThermoOff,
       "smart4ThermoOn": smart4ThermoOn,
       "smart4ThermoOff": smart4ThermoOff,
       "smart5ThermoOn": smart5ThermoOn,
       "smart5ThermoOff": smart5ThermoOff,
       "tempSensorAlarm": tempSensorAlarm,
       "tempSensorRelease": tempSensorRelease,
       "voltSensorAlarm": voltSensorAlarm,
       "voltSensorRelease": voltSensorRelease,
       "task1Done": task1Done,
       "task2Done": task2Done,
       "task3Done": task3Done,
       "task4Done": task4Done,
       "pingLost": pingLost,
       "batteryChargeLow": batteryChargeLow,
       "measurements": measurements,
       "snrSensors": snrSensors,
       "temperatureSensors": temperatureSensors,
       "temperatureS1": temperatureS1,
       "temperatureS2": temperatureS2,
       "temperatureS3": temperatureS3,
       "temperatureS4": temperatureS4,
       "temperatureS5": temperatureS5,
       "temperatureS6": temperatureS6,
       "temperatureS7": temperatureS7,
       "temperatureS8": temperatureS8,
       "temperatureS9": temperatureS9,
       "temperatureS10": temperatureS10,
       "powerSensors": powerSensors,
       "voltageS1": voltageS1,
       "currentS1": currentS1,
       "voltageS2": voltageS2,
       "currentS2": currentS2,
       "voltageS3": voltageS3,
       "currentS3": currentS3,
       "voltageS4": voltageS4,
       "currentS4": currentS4,
       "voltageS5": voltageS5,
       "currentS5": currentS5,
       "voltageS6": voltageS6,
       "currentS6": currentS6,
       "voltageS7": voltageS7,
       "currentS7": currentS7,
       "voltageS8": voltageS8,
       "currentS8": currentS8,
       "voltageS9": voltageS9,
       "currentS9": currentS9,
       "voltageS10": voltageS10,
       "currentS10": currentS10,
       "serialS1": serialS1,
       "serialS2": serialS2,
       "serialS3": serialS3,
       "serialS4": serialS4,
       "serialS5": serialS5,
       "serialS6": serialS6,
       "serialS7": serialS7,
       "serialS8": serialS8,
       "serialS9": serialS9,
       "serialS10": serialS10,
       "voltageSensor": voltageSensor,
       "sensesstate": sensesstate,
       "alarmSensor1": alarmSensor1,
       "alarmSensor2": alarmSensor2,
       "alarmSensor3": alarmSensor3,
       "alarmSensor4": alarmSensor4,
       "alarmSensor5": alarmSensor5,
       "uSensor": uSensor,
       "management": management,
       "releState": releState,
       "smart1State": smart1State,
       "smart2State": smart2State,
       "smart3State": smart3State,
       "smart4State": smart4State,
       "smart5State": smart5State,
       "releResetTime": releResetTime,
       "smart1ResetTime": smart1ResetTime,
       "smart2ResetTime": smart2ResetTime,
       "smart3ResetTime": smart3ResetTime,
       "smart4ResetTime": smart4ResetTime,
       "smart5ResetTime": smart5ResetTime,
       "counters": counters,
       "alarmSensCnts": alarmSensCnts,
       "alarmSensor1cnt": alarmSensor1cnt,
       "alarmSensor2cnt": alarmSensor2cnt,
       "alarmSensor3cnt": alarmSensor3cnt,
       "alarmSensor4cnt": alarmSensor4cnt,
       "alarmSensor5cnt": alarmSensor5cnt,
       "options": options,
       "dataType": dataType,
       "erd4Group": erd4Group}
)
