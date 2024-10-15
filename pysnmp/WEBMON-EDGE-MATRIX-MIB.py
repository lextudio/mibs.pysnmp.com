# SNMP MIB module (WEBMON-EDGE-MATRIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WEBMON-EDGE-MATRIX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:43 2024
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

moduleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 3)
)
moduleIdentity.setRevisions(
        ("2012-05-17 22:18",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DescriptionString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class DigitalState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



class Boolean(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )



class ConnectivityState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 0))
    )



class AnalogState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("highHigh", 0),
          ("low", 3),
          ("lowLow", 4),
          ("medium", 2))
    )



class Configured(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("always-in-use", 1),
          ("not-in-use", 0),
          ("schedule-a", 2),
          ("schedule-b", 3),
          ("schedule-c", 4),
          ("schedule-d", 5))
    )



class Level(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("normal", 0),
          ("status", 4))
    )



class SnmpVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 0),
          ("snmpv2c", 1),
          ("snmpv2c-inform", 3),
          ("snmpv3", 2),
          ("snmpv3-inform", 4))
    )



class CameraStyle(Integer32, TextualConvention):
    status = "current"
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
        *(("axis-210", 5),
          ("axis-2100", 2),
          ("axis-m1103", 6),
          ("d-link-dcs1000", 0),
          ("d-link-dcs2000", 3),
          ("d-link-dcs5300", 4),
          ("sony-snc-rz30n", 1))
    )



class ContactStyle(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dry-contact", 0),
          ("wet-contact", 1))
    )



class MeasureStyle(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("english", 0),
          ("metric", 1))
    )



class OutputMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 0))
    )



class OutputState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )



class BaudRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              600,
              1200,
              2400,
              4800,
              9600,
              19200,
              28800,
              38400)
        )
    )
    namedValues = NamedValues(
        *(("baud-1200", 1200),
          ("baud-19200", 19200),
          ("baud-2400", 2400),
          ("baud-28800", 28800),
          ("baud-300", 300),
          ("baud-38400", 38400),
          ("baud-4800", 4800),
          ("baud-600", 600),
          ("baud-9600", 9600))
    )



class DataBits(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("data-bits-7", 7),
          ("data-bits-8", 8))
    )



class Parity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("even-parity", 1),
          ("none", 0),
          ("odd-parity", 2))
    )



class StopBits(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop-bit-1", 1),
          ("stop-bits-2", 2))
    )



class Protocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ascii-log-single-line", 10),
          ("command-line", 1),
          ("configuration-menu", 19),
          ("configuration-transfer", 3),
          ("dcm-responder", 9),
          ("dcpf-responder", 16),
          ("e2a-host", 11),
          ("gps-reader", 12),
          ("ip-switchboard", 4),
          ("lcd-protocol", 17),
          ("modbus-interrogation", 2),
          ("modem-mode", 7),
          ("none", 0),
          ("port-redirect", 13),
          ("ppp-server", 8),
          ("sensor-hub-interrogation", 20),
          ("sensor-reader", 14),
          ("tabs-responder", 18),
          ("terminal-server", 5),
          ("tl1-responder", 15),
          ("user-login", 6))
    )



class SerialRTS(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rts-always-on", 1),
          ("rts-never-on", 0),
          ("rts-on-for-transmit", 2))
    )



class SerialCTS(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cts-ignore", 0),
          ("cts-require", 1))
    )



class SlotId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("analog-inputs", 5),
          ("discrete-inputs", 1),
          ("discrete-outputs", 2),
          ("empty", 0),
          ("onboard-sensors", 4),
          ("sensor-inputs", 7),
          ("serial-ports", 3),
          ("switch-ports", 6))
    )



class ProductType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("webmon-edge", 0),
          ("webmon-matrix", 1))
    )



class VoltageRange(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("plus-minus-100-volts", 100),
          ("sensor-port", 5))
    )



class IOFormat(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("onboard-built-in", 8),
          ("rj", 7),
          ("single-pin", 0),
          ("single-pin-with-ground", 1),
          ("three-pins", 5),
          ("three-pins-right-to-left", 6),
          ("two-pins", 2),
          ("two-pins-right-to-left", 4),
          ("two-pins-with-ground", 3))
    )



class PortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("cdma", 6),
          ("dialup", 3),
          ("e2a", 5),
          ("edge", 8),
          ("gps", 7),
          ("iden", 4),
          ("not-present", 0),
          ("rs-232", 1),
          ("rs-485", 2),
          ("t202", 9))
    )



class DiscreteFormula(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("a-and-b", 0),
          ("a-and-not-b", 2),
          ("a-or-b", 4),
          ("a-or-not-b", 6),
          ("a-xor-b", 8),
          ("a-xor-not-b", 10),
          ("not-a-and-b", 1),
          ("not-a-and-not-b", 3),
          ("not-a-or-b", 5),
          ("not-a-or-not-b", 7),
          ("not-a-xor-b", 9),
          ("not-a-xor-not-b", 11))
    )



class DayOfWeek(Integer32, TextualConvention):
    status = "current"
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
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )



class ConfiguredState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class TL1Srveff(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blank", 0),
          ("nsa", 2),
          ("sa", 1))
    )



class TL1Locn(Integer32, TextualConvention):
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
        *(("blank", 0),
          ("fend", 2),
          ("line", 3),
          ("nend", 1))
    )



class TL1Dirn(Integer32, TextualConvention):
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
        *(("blank", 0),
          ("na", 3),
          ("rcv", 2),
          ("trmt", 1))
    )



class TL1Issue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("issue-3", 3),
          ("issue-5", 5))
    )



class UseDialout(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("as-backup", 2),
          ("never", 0))
    )



class SensorType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("humidity", 2),
          ("raw", 0),
          ("temperature", 1))
    )



class SNMPCommandType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(160,
              163)
        )
    )
    namedValues = NamedValues(
        *(("get", 160),
          ("set", 163))
    )



class SNMPVarbindType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("integer", 2),
          ("string", 4))
    )



class SNMPAccess(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("authnopriv-md5", 1),
          ("authnopriv-sha", 3),
          ("authpriv-md5", 2),
          ("authpriv-sha", 4),
          ("noauthnopriv", 0))
    )



class MODBUSCommand(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("read-holding-register", 3),
          ("read-input-register", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Dantel_ObjectIdentity = ObjectIdentity
dantel = _Dantel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994)
)
_DantelProducts_ObjectIdentity = ObjectIdentity
dantelProducts = _DantelProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3)
)
_WebMon_ObjectIdentity = ObjectIdentity
webMon = _WebMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4)
)
if mibBuilder.loadTexts:
    webMon.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6)
)
if mibBuilder.loadTexts:
    traps.setStatus("current")
_AnalogInputs_ObjectIdentity = ObjectIdentity
analogInputs = _AnalogInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 1)
)
if mibBuilder.loadTexts:
    analogInputs.setStatus("current")
_AnalogInputDescription_Type = DescriptionString
_AnalogInputDescription_Object = MibScalar
analogInputDescription = _AnalogInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 1, 2),
    _AnalogInputDescription_Type()
)
analogInputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogInputDescription.setStatus("current")
_AnalogLiveLevel_Type = Level
_AnalogLiveLevel_Object = MibScalar
analogLiveLevel = _AnalogLiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 1, 3),
    _AnalogLiveLevel_Type()
)
analogLiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogLiveLevel.setStatus("current")
_AnalogLiveReading_Type = DescriptionString
_AnalogLiveReading_Object = MibScalar
analogLiveReading = _AnalogLiveReading_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 1, 5),
    _AnalogLiveReading_Type()
)
analogLiveReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogLiveReading.setStatus("current")
_AnalogUnitsOfMeasurement_Type = DescriptionString
_AnalogUnitsOfMeasurement_Object = MibScalar
analogUnitsOfMeasurement = _AnalogUnitsOfMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 1, 6),
    _AnalogUnitsOfMeasurement_Type()
)
analogUnitsOfMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogUnitsOfMeasurement.setStatus("current")
_AnalogLiveState_Type = AnalogState
_AnalogLiveState_Object = MibScalar
analogLiveState = _AnalogLiveState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 1, 7),
    _AnalogLiveState_Type()
)
analogLiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogLiveState.setStatus("current")
_AnalogLiveStateDescription_Type = DescriptionString
_AnalogLiveStateDescription_Object = MibScalar
analogLiveStateDescription = _AnalogLiveStateDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 1, 8),
    _AnalogLiveStateDescription_Type()
)
analogLiveStateDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogLiveStateDescription.setStatus("current")
_AnalogAlarmState_Type = Boolean
_AnalogAlarmState_Object = MibScalar
analogAlarmState = _AnalogAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 1, 9),
    _AnalogAlarmState_Type()
)
analogAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogAlarmState.setStatus("current")
_AnalogSourceDescription_Type = DescriptionString
_AnalogSourceDescription_Object = MibScalar
analogSourceDescription = _AnalogSourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 1, 101),
    _AnalogSourceDescription_Type()
)
analogSourceDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    analogSourceDescription.setStatus("current")
_AnalogSourceIndex_Type = Integer32
_AnalogSourceIndex_Object = MibScalar
analogSourceIndex = _AnalogSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 1, 102),
    _AnalogSourceIndex_Type()
)
analogSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    analogSourceIndex.setStatus("current")
_DigitalInputs_ObjectIdentity = ObjectIdentity
digitalInputs = _DigitalInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 2)
)
if mibBuilder.loadTexts:
    digitalInputs.setStatus("current")
_DigitalInputDescription_Type = DescriptionString
_DigitalInputDescription_Object = MibScalar
digitalInputDescription = _DigitalInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 2, 2),
    _DigitalInputDescription_Type()
)
digitalInputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInputDescription.setStatus("current")
_DigitalLiveLevel_Type = Level
_DigitalLiveLevel_Object = MibScalar
digitalLiveLevel = _DigitalLiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 2, 3),
    _DigitalLiveLevel_Type()
)
digitalLiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalLiveLevel.setStatus("current")
_DigitalLiveState_Type = DigitalState
_DigitalLiveState_Object = MibScalar
digitalLiveState = _DigitalLiveState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 2, 4),
    _DigitalLiveState_Type()
)
digitalLiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalLiveState.setStatus("current")
_DigitalLiveStateDescription_Type = DescriptionString
_DigitalLiveStateDescription_Object = MibScalar
digitalLiveStateDescription = _DigitalLiveStateDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 2, 5),
    _DigitalLiveStateDescription_Type()
)
digitalLiveStateDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalLiveStateDescription.setStatus("current")
_DigitalAlarmState_Type = Boolean
_DigitalAlarmState_Object = MibScalar
digitalAlarmState = _DigitalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 2, 6),
    _DigitalAlarmState_Type()
)
digitalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalAlarmState.setStatus("current")
_DigitalSourceDescription_Type = DescriptionString
_DigitalSourceDescription_Object = MibScalar
digitalSourceDescription = _DigitalSourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 2, 101),
    _DigitalSourceDescription_Type()
)
digitalSourceDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digitalSourceDescription.setStatus("current")
_DigitalSourceIndex_Type = Integer32
_DigitalSourceIndex_Object = MibScalar
digitalSourceIndex = _DigitalSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 2, 102),
    _DigitalSourceIndex_Type()
)
digitalSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digitalSourceIndex.setStatus("current")
_RemoteDevices_ObjectIdentity = ObjectIdentity
remoteDevices = _RemoteDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 3)
)
if mibBuilder.loadTexts:
    remoteDevices.setStatus("current")
_RemoteDeviceDescription_Type = DescriptionString
_RemoteDeviceDescription_Object = MibScalar
remoteDeviceDescription = _RemoteDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 3, 2),
    _RemoteDeviceDescription_Type()
)
remoteDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDeviceDescription.setStatus("current")
_RemoteDeviceLiveLevel_Type = Level
_RemoteDeviceLiveLevel_Object = MibScalar
remoteDeviceLiveLevel = _RemoteDeviceLiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 3, 3),
    _RemoteDeviceLiveLevel_Type()
)
remoteDeviceLiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDeviceLiveLevel.setStatus("current")
_RemoteDeviceLiveState_Type = ConnectivityState
_RemoteDeviceLiveState_Object = MibScalar
remoteDeviceLiveState = _RemoteDeviceLiveState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 3, 4),
    _RemoteDeviceLiveState_Type()
)
remoteDeviceLiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDeviceLiveState.setStatus("current")
_RemoteDeviceAlarmState_Type = Boolean
_RemoteDeviceAlarmState_Object = MibScalar
remoteDeviceAlarmState = _RemoteDeviceAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 3, 5),
    _RemoteDeviceAlarmState_Type()
)
remoteDeviceAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDeviceAlarmState.setStatus("current")
_RemoteDeviceSourceDescription_Type = DescriptionString
_RemoteDeviceSourceDescription_Object = MibScalar
remoteDeviceSourceDescription = _RemoteDeviceSourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 3, 101),
    _RemoteDeviceSourceDescription_Type()
)
remoteDeviceSourceDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteDeviceSourceDescription.setStatus("current")
_RemoteDeviceSourceIndex_Type = Integer32
_RemoteDeviceSourceIndex_Object = MibScalar
remoteDeviceSourceIndex = _RemoteDeviceSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 3, 102),
    _RemoteDeviceSourceIndex_Type()
)
remoteDeviceSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteDeviceSourceIndex.setStatus("current")
_Faults_ObjectIdentity = ObjectIdentity
faults = _Faults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 4)
)
if mibBuilder.loadTexts:
    faults.setStatus("current")
_FaultDescription_Type = DescriptionString
_FaultDescription_Object = MibScalar
faultDescription = _FaultDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 4, 2),
    _FaultDescription_Type()
)
faultDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultDescription.setStatus("current")
_FaultLiveLevel_Type = Level
_FaultLiveLevel_Object = MibScalar
faultLiveLevel = _FaultLiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 4, 3),
    _FaultLiveLevel_Type()
)
faultLiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultLiveLevel.setStatus("current")
_FaultStateDescription_Type = DescriptionString
_FaultStateDescription_Object = MibScalar
faultStateDescription = _FaultStateDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 4, 4),
    _FaultStateDescription_Type()
)
faultStateDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultStateDescription.setStatus("current")
_FaultAlarmState_Type = Boolean
_FaultAlarmState_Object = MibScalar
faultAlarmState = _FaultAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 4, 5),
    _FaultAlarmState_Type()
)
faultAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultAlarmState.setStatus("current")
_FaultSourceDescription_Type = DescriptionString
_FaultSourceDescription_Object = MibScalar
faultSourceDescription = _FaultSourceDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 4, 101),
    _FaultSourceDescription_Type()
)
faultSourceDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    faultSourceDescription.setStatus("current")
_FaultSourceIndex_Type = Integer32
_FaultSourceIndex_Object = MibScalar
faultSourceIndex = _FaultSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 4, 102),
    _FaultSourceIndex_Type()
)
faultSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    faultSourceIndex.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7)
)
_SystemGeneral_ObjectIdentity = ObjectIdentity
systemGeneral = _SystemGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 1)
)
_SystemGeneralLocation_Type = DescriptionString
_SystemGeneralLocation_Object = MibScalar
systemGeneralLocation = _SystemGeneralLocation_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 1, 2),
    _SystemGeneralLocation_Type()
)
systemGeneralLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemGeneralLocation.setStatus("current")
_SystemGeneralDescription_Type = DescriptionString
_SystemGeneralDescription_Object = MibScalar
systemGeneralDescription = _SystemGeneralDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 1, 3),
    _SystemGeneralDescription_Type()
)
systemGeneralDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemGeneralDescription.setStatus("current")
_SystemGeneralIpAddress_Type = IpAddress
_SystemGeneralIpAddress_Object = MibScalar
systemGeneralIpAddress = _SystemGeneralIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 1, 14),
    _SystemGeneralIpAddress_Type()
)
systemGeneralIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemGeneralIpAddress.setStatus("current")
_SystemGeneralSubnetMask_Type = IpAddress
_SystemGeneralSubnetMask_Object = MibScalar
systemGeneralSubnetMask = _SystemGeneralSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 1, 15),
    _SystemGeneralSubnetMask_Type()
)
systemGeneralSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemGeneralSubnetMask.setStatus("current")
_SystemGeneralGatewayAddress_Type = IpAddress
_SystemGeneralGatewayAddress_Object = MibScalar
systemGeneralGatewayAddress = _SystemGeneralGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 1, 16),
    _SystemGeneralGatewayAddress_Type()
)
systemGeneralGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemGeneralGatewayAddress.setStatus("current")
_SystemGeneralMeasureStyle_Type = MeasureStyle
_SystemGeneralMeasureStyle_Object = MibScalar
systemGeneralMeasureStyle = _SystemGeneralMeasureStyle_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 1, 45),
    _SystemGeneralMeasureStyle_Type()
)
systemGeneralMeasureStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemGeneralMeasureStyle.setStatus("current")
_SystemGeneralMacAddress_Type = DescriptionString
_SystemGeneralMacAddress_Object = MibScalar
systemGeneralMacAddress = _SystemGeneralMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 1, 54),
    _SystemGeneralMacAddress_Type()
)
systemGeneralMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemGeneralMacAddress.setStatus("current")
_SystemGeneralProductType_Type = ProductType
_SystemGeneralProductType_Object = MibScalar
systemGeneralProductType = _SystemGeneralProductType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 1, 70),
    _SystemGeneralProductType_Type()
)
systemGeneralProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemGeneralProductType.setStatus("current")
_SystemGeneralIPPortNum_Type = Integer32
_SystemGeneralIPPortNum_Object = MibScalar
systemGeneralIPPortNum = _SystemGeneralIPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 1, 73),
    _SystemGeneralIPPortNum_Type()
)
systemGeneralIPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemGeneralIPPortNum.setStatus("current")
_SystemGeneralVersion_Type = DescriptionString
_SystemGeneralVersion_Object = MibScalar
systemGeneralVersion = _SystemGeneralVersion_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 1, 82),
    _SystemGeneralVersion_Type()
)
systemGeneralVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemGeneralVersion.setStatus("current")
_PTrapTargetTable_Object = MibTable
pTrapTargetTable = _PTrapTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2)
)
if mibBuilder.loadTexts:
    pTrapTargetTable.setStatus("current")
_PTrapTargetEntry_Object = MibTableRow
pTrapTargetEntry = _PTrapTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1)
)
pTrapTargetEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pTrapTargetIndex"),
)
if mibBuilder.loadTexts:
    pTrapTargetEntry.setStatus("current")
_PTrapTargetDescription_Type = DescriptionString
_PTrapTargetDescription_Object = MibTableColumn
pTrapTargetDescription = _PTrapTargetDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 3),
    _PTrapTargetDescription_Type()
)
pTrapTargetDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapTargetDescription.setStatus("current")
_PTrapTargetConfigured_Type = Configured
_PTrapTargetConfigured_Object = MibTableColumn
pTrapTargetConfigured = _PTrapTargetConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 10),
    _PTrapTargetConfigured_Type()
)
pTrapTargetConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapTargetConfigured.setStatus("current")
_PTrapTargetIpAddress_Type = IpAddress
_PTrapTargetIpAddress_Object = MibTableColumn
pTrapTargetIpAddress = _PTrapTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 14),
    _PTrapTargetIpAddress_Type()
)
pTrapTargetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapTargetIpAddress.setStatus("current")
_PTrapTargetSnmpVersion_Type = SnmpVersion
_PTrapTargetSnmpVersion_Object = MibTableColumn
pTrapTargetSnmpVersion = _PTrapTargetSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 42),
    _PTrapTargetSnmpVersion_Type()
)
pTrapTargetSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapTargetSnmpVersion.setStatus("current")
_PTrapTargetIPPortNum_Type = Integer32
_PTrapTargetIPPortNum_Object = MibTableColumn
pTrapTargetIPPortNum = _PTrapTargetIPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 73),
    _PTrapTargetIPPortNum_Type()
)
pTrapTargetIPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapTargetIPPortNum.setStatus("current")
_PTrapTargetBackupIPAddress_Type = IpAddress
_PTrapTargetBackupIPAddress_Object = MibTableColumn
pTrapTargetBackupIPAddress = _PTrapTargetBackupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 78),
    _PTrapTargetBackupIPAddress_Type()
)
pTrapTargetBackupIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapTargetBackupIPAddress.setStatus("current")
_PTrapTargetUseDialout_Type = UseDialout
_PTrapTargetUseDialout_Object = MibTableColumn
pTrapTargetUseDialout = _PTrapTargetUseDialout_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 125),
    _PTrapTargetUseDialout_Type()
)
pTrapTargetUseDialout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapTargetUseDialout.setStatus("current")
_PTrapTargetDialoutTarget_Type = Integer32
_PTrapTargetDialoutTarget_Object = MibTableColumn
pTrapTargetDialoutTarget = _PTrapTargetDialoutTarget_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 126),
    _PTrapTargetDialoutTarget_Type()
)
pTrapTargetDialoutTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapTargetDialoutTarget.setStatus("current")
_PTrapTargetAuthKey_Type = DescriptionString
_PTrapTargetAuthKey_Object = MibTableColumn
pTrapTargetAuthKey = _PTrapTargetAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 140),
    _PTrapTargetAuthKey_Type()
)
pTrapTargetAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapTargetAuthKey.setStatus("current")
_PTrapTargetPrivKey_Type = DescriptionString
_PTrapTargetPrivKey_Object = MibTableColumn
pTrapTargetPrivKey = _PTrapTargetPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 141),
    _PTrapTargetPrivKey_Type()
)
pTrapTargetPrivKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapTargetPrivKey.setStatus("current")
_PTrapTargetSNMPAccess_Type = SNMPAccess
_PTrapTargetSNMPAccess_Object = MibTableColumn
pTrapTargetSNMPAccess = _PTrapTargetSNMPAccess_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 142),
    _PTrapTargetSNMPAccess_Type()
)
pTrapTargetSNMPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapTargetSNMPAccess.setStatus("current")
_PTrapTargetEngineID_Type = DescriptionString
_PTrapTargetEngineID_Object = MibTableColumn
pTrapTargetEngineID = _PTrapTargetEngineID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 143),
    _PTrapTargetEngineID_Type()
)
pTrapTargetEngineID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTrapTargetEngineID.setStatus("current")


class _PTrapTargetIndex_Type(Integer32):
    """Custom type pTrapTargetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PTrapTargetIndex_Type.__name__ = "Integer32"
_PTrapTargetIndex_Object = MibTableColumn
pTrapTargetIndex = _PTrapTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 2, 1, 999),
    _PTrapTargetIndex_Type()
)
pTrapTargetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTrapTargetIndex.setStatus("current")
_PEmailTable_Object = MibTable
pEmailTable = _PEmailTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 3)
)
if mibBuilder.loadTexts:
    pEmailTable.setStatus("current")
_PEmailEntry_Object = MibTableRow
pEmailEntry = _PEmailEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 3, 1)
)
pEmailEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pEmailIndex"),
)
if mibBuilder.loadTexts:
    pEmailEntry.setStatus("current")
_PEmailAddress_Type = DescriptionString
_PEmailAddress_Object = MibTableColumn
pEmailAddress = _PEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 3, 1, 1),
    _PEmailAddress_Type()
)
pEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pEmailAddress.setStatus("current")
_PEmailDescription_Type = DescriptionString
_PEmailDescription_Object = MibTableColumn
pEmailDescription = _PEmailDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 3, 1, 3),
    _PEmailDescription_Type()
)
pEmailDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pEmailDescription.setStatus("current")
_PEmailConfigured_Type = Configured
_PEmailConfigured_Object = MibTableColumn
pEmailConfigured = _PEmailConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 3, 1, 10),
    _PEmailConfigured_Type()
)
pEmailConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pEmailConfigured.setStatus("current")


class _PEmailIndex_Type(Integer32):
    """Custom type pEmailIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PEmailIndex_Type.__name__ = "Integer32"
_PEmailIndex_Object = MibTableColumn
pEmailIndex = _PEmailIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 3, 1, 999),
    _PEmailIndex_Type()
)
pEmailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pEmailIndex.setStatus("current")
_PRemoteSensorTable_Object = MibTable
pRemoteSensorTable = _PRemoteSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5)
)
if mibBuilder.loadTexts:
    pRemoteSensorTable.setStatus("current")
_PRemoteSensorEntry_Object = MibTableRow
pRemoteSensorEntry = _PRemoteSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1)
)
pRemoteSensorEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorIndex"),
)
if mibBuilder.loadTexts:
    pRemoteSensorEntry.setStatus("current")
_PRemoteSensorDescription_Type = DescriptionString
_PRemoteSensorDescription_Object = MibTableColumn
pRemoteSensorDescription = _PRemoteSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 3),
    _PRemoteSensorDescription_Type()
)
pRemoteSensorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorDescription.setStatus("current")
_PRemoteSensorDesc0_Type = DescriptionString
_PRemoteSensorDesc0_Object = MibTableColumn
pRemoteSensorDesc0 = _PRemoteSensorDesc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 4),
    _PRemoteSensorDesc0_Type()
)
pRemoteSensorDesc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorDesc0.setStatus("current")
_PRemoteSensorDesc1_Type = DescriptionString
_PRemoteSensorDesc1_Object = MibTableColumn
pRemoteSensorDesc1 = _PRemoteSensorDesc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 5),
    _PRemoteSensorDesc1_Type()
)
pRemoteSensorDesc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorDesc1.setStatus("current")
_PRemoteSensorDesc2_Type = DescriptionString
_PRemoteSensorDesc2_Object = MibTableColumn
pRemoteSensorDesc2 = _PRemoteSensorDesc2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 6),
    _PRemoteSensorDesc2_Type()
)
pRemoteSensorDesc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorDesc2.setStatus("current")
_PRemoteSensorDesc3_Type = DescriptionString
_PRemoteSensorDesc3_Object = MibTableColumn
pRemoteSensorDesc3 = _PRemoteSensorDesc3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 7),
    _PRemoteSensorDesc3_Type()
)
pRemoteSensorDesc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorDesc3.setStatus("current")
_PRemoteSensorDesc4_Type = DescriptionString
_PRemoteSensorDesc4_Object = MibTableColumn
pRemoteSensorDesc4 = _PRemoteSensorDesc4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 8),
    _PRemoteSensorDesc4_Type()
)
pRemoteSensorDesc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorDesc4.setStatus("current")
_PRemoteSensorDesc5_Type = DescriptionString
_PRemoteSensorDesc5_Object = MibTableColumn
pRemoteSensorDesc5 = _PRemoteSensorDesc5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 9),
    _PRemoteSensorDesc5_Type()
)
pRemoteSensorDesc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorDesc5.setStatus("current")
_PRemoteSensorConfigured_Type = Configured
_PRemoteSensorConfigured_Object = MibTableColumn
pRemoteSensorConfigured = _PRemoteSensorConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 10),
    _PRemoteSensorConfigured_Type()
)
pRemoteSensorConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorConfigured.setStatus("current")
_PRemoteSensorSendEmail_Type = Boolean
_PRemoteSensorSendEmail_Object = MibTableColumn
pRemoteSensorSendEmail = _PRemoteSensorSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 11),
    _PRemoteSensorSendEmail_Type()
)
pRemoteSensorSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorSendEmail.setStatus("current")
_PRemoteSensorSendSNMPTrap_Type = Boolean
_PRemoteSensorSendSNMPTrap_Object = MibTableColumn
pRemoteSensorSendSNMPTrap = _PRemoteSensorSendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 12),
    _PRemoteSensorSendSNMPTrap_Type()
)
pRemoteSensorSendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorSendSNMPTrap.setStatus("current")
_PRemoteSensorLevel0_Type = Level
_PRemoteSensorLevel0_Object = MibTableColumn
pRemoteSensorLevel0 = _PRemoteSensorLevel0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 17),
    _PRemoteSensorLevel0_Type()
)
pRemoteSensorLevel0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorLevel0.setStatus("current")
_PRemoteSensorLevel1_Type = Level
_PRemoteSensorLevel1_Object = MibTableColumn
pRemoteSensorLevel1 = _PRemoteSensorLevel1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 18),
    _PRemoteSensorLevel1_Type()
)
pRemoteSensorLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorLevel1.setStatus("current")
_PRemoteSensorLevel2_Type = Level
_PRemoteSensorLevel2_Object = MibTableColumn
pRemoteSensorLevel2 = _PRemoteSensorLevel2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 19),
    _PRemoteSensorLevel2_Type()
)
pRemoteSensorLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorLevel2.setStatus("current")
_PRemoteSensorLevel3_Type = Level
_PRemoteSensorLevel3_Object = MibTableColumn
pRemoteSensorLevel3 = _PRemoteSensorLevel3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 20),
    _PRemoteSensorLevel3_Type()
)
pRemoteSensorLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorLevel3.setStatus("current")
_PRemoteSensorLevel4_Type = Level
_PRemoteSensorLevel4_Object = MibTableColumn
pRemoteSensorLevel4 = _PRemoteSensorLevel4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 21),
    _PRemoteSensorLevel4_Type()
)
pRemoteSensorLevel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorLevel4.setStatus("current")
_PRemoteSensorLevel5_Type = Level
_PRemoteSensorLevel5_Object = MibTableColumn
pRemoteSensorLevel5 = _PRemoteSensorLevel5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 22),
    _PRemoteSensorLevel5_Type()
)
pRemoteSensorLevel5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorLevel5.setStatus("current")
_PRemoteSensorThresh0_Type = DescriptionString
_PRemoteSensorThresh0_Object = MibTableColumn
pRemoteSensorThresh0 = _PRemoteSensorThresh0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 28),
    _PRemoteSensorThresh0_Type()
)
pRemoteSensorThresh0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorThresh0.setStatus("current")
_PRemoteSensorThresh1_Type = DescriptionString
_PRemoteSensorThresh1_Object = MibTableColumn
pRemoteSensorThresh1 = _PRemoteSensorThresh1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 29),
    _PRemoteSensorThresh1_Type()
)
pRemoteSensorThresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorThresh1.setStatus("current")
_PRemoteSensorThresh2_Type = DescriptionString
_PRemoteSensorThresh2_Object = MibTableColumn
pRemoteSensorThresh2 = _PRemoteSensorThresh2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 30),
    _PRemoteSensorThresh2_Type()
)
pRemoteSensorThresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorThresh2.setStatus("current")
_PRemoteSensorThresh3_Type = DescriptionString
_PRemoteSensorThresh3_Object = MibTableColumn
pRemoteSensorThresh3 = _PRemoteSensorThresh3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 31),
    _PRemoteSensorThresh3_Type()
)
pRemoteSensorThresh3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorThresh3.setStatus("current")
_PRemoteSensorThresh4_Type = DescriptionString
_PRemoteSensorThresh4_Object = MibTableColumn
pRemoteSensorThresh4 = _PRemoteSensorThresh4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 32),
    _PRemoteSensorThresh4_Type()
)
pRemoteSensorThresh4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorThresh4.setStatus("current")
_PRemoteSensorThresh5_Type = DescriptionString
_PRemoteSensorThresh5_Object = MibTableColumn
pRemoteSensorThresh5 = _PRemoteSensorThresh5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 33),
    _PRemoteSensorThresh5_Type()
)
pRemoteSensorThresh5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorThresh5.setStatus("current")
_PRemoteSensorUnits_Type = DescriptionString
_PRemoteSensorUnits_Object = MibTableColumn
pRemoteSensorUnits = _PRemoteSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 46),
    _PRemoteSensorUnits_Type()
)
pRemoteSensorUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorUnits.setStatus("current")
_PRemoteSensorPollAddress_Type = Integer32
_PRemoteSensorPollAddress_Object = MibTableColumn
pRemoteSensorPollAddress = _PRemoteSensorPollAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 56),
    _PRemoteSensorPollAddress_Type()
)
pRemoteSensorPollAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorPollAddress.setStatus("current")
_PRemoteSensorLiveDescription_Type = DescriptionString
_PRemoteSensorLiveDescription_Object = MibTableColumn
pRemoteSensorLiveDescription = _PRemoteSensorLiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 64),
    _PRemoteSensorLiveDescription_Type()
)
pRemoteSensorLiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRemoteSensorLiveDescription.setStatus("current")
_PRemoteSensorLiveLevel_Type = DescriptionString
_PRemoteSensorLiveLevel_Object = MibTableColumn
pRemoteSensorLiveLevel = _PRemoteSensorLiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 65),
    _PRemoteSensorLiveLevel_Type()
)
pRemoteSensorLiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRemoteSensorLiveLevel.setStatus("current")
_PRemoteSensorLiveRaw_Type = DescriptionString
_PRemoteSensorLiveRaw_Object = MibTableColumn
pRemoteSensorLiveRaw = _PRemoteSensorLiveRaw_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 66),
    _PRemoteSensorLiveRaw_Type()
)
pRemoteSensorLiveRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRemoteSensorLiveRaw.setStatus("current")
_PRemoteSensorLiveTime_Type = DescriptionString
_PRemoteSensorLiveTime_Object = MibTableColumn
pRemoteSensorLiveTime = _PRemoteSensorLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 67),
    _PRemoteSensorLiveTime_Type()
)
pRemoteSensorLiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRemoteSensorLiveTime.setStatus("current")
_PRemoteSensorTL1SID_Type = DescriptionString
_PRemoteSensorTL1SID_Object = MibTableColumn
pRemoteSensorTL1SID = _PRemoteSensorTL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 116),
    _PRemoteSensorTL1SID_Type()
)
pRemoteSensorTL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorTL1SID.setStatus("current")
_PRemoteSensorTL1COND_Type = DescriptionString
_PRemoteSensorTL1COND_Object = MibTableColumn
pRemoteSensorTL1COND = _PRemoteSensorTL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 117),
    _PRemoteSensorTL1COND_Type()
)
pRemoteSensorTL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorTL1COND.setStatus("current")
_PRemoteSensorTL1Eqpt_Type = DescriptionString
_PRemoteSensorTL1Eqpt_Object = MibTableColumn
pRemoteSensorTL1Eqpt = _PRemoteSensorTL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 118),
    _PRemoteSensorTL1Eqpt_Type()
)
pRemoteSensorTL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorTL1Eqpt.setStatus("current")
_PRemoteSensorTL1Env_Type = Boolean
_PRemoteSensorTL1Env_Object = MibTableColumn
pRemoteSensorTL1Env = _PRemoteSensorTL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 119),
    _PRemoteSensorTL1Env_Type()
)
pRemoteSensorTL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorTL1Env.setStatus("current")
_PRemoteSensorTL1Srveff_Type = TL1Srveff
_PRemoteSensorTL1Srveff_Object = MibTableColumn
pRemoteSensorTL1Srveff = _PRemoteSensorTL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 120),
    _PRemoteSensorTL1Srveff_Type()
)
pRemoteSensorTL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorTL1Srveff.setStatus("current")
_PRemoteSensorTL1Locn_Type = TL1Locn
_PRemoteSensorTL1Locn_Object = MibTableColumn
pRemoteSensorTL1Locn = _PRemoteSensorTL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 121),
    _PRemoteSensorTL1Locn_Type()
)
pRemoteSensorTL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorTL1Locn.setStatus("current")
_PRemoteSensorTL1Dirn_Type = TL1Dirn
_PRemoteSensorTL1Dirn_Object = MibTableColumn
pRemoteSensorTL1Dirn = _PRemoteSensorTL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 122),
    _PRemoteSensorTL1Dirn_Type()
)
pRemoteSensorTL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorTL1Dirn.setStatus("current")
_PRemoteSensorMODBUSCommand_Type = MODBUSCommand
_PRemoteSensorMODBUSCommand_Object = MibTableColumn
pRemoteSensorMODBUSCommand = _PRemoteSensorMODBUSCommand_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 144),
    _PRemoteSensorMODBUSCommand_Type()
)
pRemoteSensorMODBUSCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorMODBUSCommand.setStatus("current")
_PRemoteSensorStartRegister_Type = Integer32
_PRemoteSensorStartRegister_Object = MibTableColumn
pRemoteSensorStartRegister = _PRemoteSensorStartRegister_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 145),
    _PRemoteSensorStartRegister_Type()
)
pRemoteSensorStartRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRemoteSensorStartRegister.setStatus("current")


class _PRemoteSensorIndex_Type(Integer32):
    """Custom type pRemoteSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PRemoteSensorIndex_Type.__name__ = "Integer32"
_PRemoteSensorIndex_Object = MibTableColumn
pRemoteSensorIndex = _PRemoteSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 5, 1, 999),
    _PRemoteSensorIndex_Type()
)
pRemoteSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRemoteSensorIndex.setStatus("current")
_POnboardSensorTable_Object = MibTable
pOnboardSensorTable = _POnboardSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6)
)
if mibBuilder.loadTexts:
    pOnboardSensorTable.setStatus("current")
_POnboardSensorEntry_Object = MibTableRow
pOnboardSensorEntry = _POnboardSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1)
)
pOnboardSensorEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorIndex"),
)
if mibBuilder.loadTexts:
    pOnboardSensorEntry.setStatus("current")
_POnboardSensorDescription_Type = DescriptionString
_POnboardSensorDescription_Object = MibTableColumn
pOnboardSensorDescription = _POnboardSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 3),
    _POnboardSensorDescription_Type()
)
pOnboardSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOnboardSensorDescription.setStatus("current")
_POnboardSensorDesc0_Type = DescriptionString
_POnboardSensorDesc0_Object = MibTableColumn
pOnboardSensorDesc0 = _POnboardSensorDesc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 4),
    _POnboardSensorDesc0_Type()
)
pOnboardSensorDesc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorDesc0.setStatus("current")
_POnboardSensorDesc1_Type = DescriptionString
_POnboardSensorDesc1_Object = MibTableColumn
pOnboardSensorDesc1 = _POnboardSensorDesc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 5),
    _POnboardSensorDesc1_Type()
)
pOnboardSensorDesc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorDesc1.setStatus("current")
_POnboardSensorDesc2_Type = DescriptionString
_POnboardSensorDesc2_Object = MibTableColumn
pOnboardSensorDesc2 = _POnboardSensorDesc2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 6),
    _POnboardSensorDesc2_Type()
)
pOnboardSensorDesc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorDesc2.setStatus("current")
_POnboardSensorDesc3_Type = DescriptionString
_POnboardSensorDesc3_Object = MibTableColumn
pOnboardSensorDesc3 = _POnboardSensorDesc3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 7),
    _POnboardSensorDesc3_Type()
)
pOnboardSensorDesc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorDesc3.setStatus("current")
_POnboardSensorDesc4_Type = DescriptionString
_POnboardSensorDesc4_Object = MibTableColumn
pOnboardSensorDesc4 = _POnboardSensorDesc4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 8),
    _POnboardSensorDesc4_Type()
)
pOnboardSensorDesc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorDesc4.setStatus("current")
_POnboardSensorDesc5_Type = DescriptionString
_POnboardSensorDesc5_Object = MibTableColumn
pOnboardSensorDesc5 = _POnboardSensorDesc5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 9),
    _POnboardSensorDesc5_Type()
)
pOnboardSensorDesc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorDesc5.setStatus("current")
_POnboardSensorConfigured_Type = Configured
_POnboardSensorConfigured_Object = MibTableColumn
pOnboardSensorConfigured = _POnboardSensorConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 10),
    _POnboardSensorConfigured_Type()
)
pOnboardSensorConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorConfigured.setStatus("current")
_POnboardSensorSendEmail_Type = Boolean
_POnboardSensorSendEmail_Object = MibTableColumn
pOnboardSensorSendEmail = _POnboardSensorSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 11),
    _POnboardSensorSendEmail_Type()
)
pOnboardSensorSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorSendEmail.setStatus("current")
_POnboardSensorSendSNMPTrap_Type = Boolean
_POnboardSensorSendSNMPTrap_Object = MibTableColumn
pOnboardSensorSendSNMPTrap = _POnboardSensorSendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 12),
    _POnboardSensorSendSNMPTrap_Type()
)
pOnboardSensorSendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorSendSNMPTrap.setStatus("current")
_POnboardSensorLevel0_Type = Level
_POnboardSensorLevel0_Object = MibTableColumn
pOnboardSensorLevel0 = _POnboardSensorLevel0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 17),
    _POnboardSensorLevel0_Type()
)
pOnboardSensorLevel0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorLevel0.setStatus("current")
_POnboardSensorLevel1_Type = Level
_POnboardSensorLevel1_Object = MibTableColumn
pOnboardSensorLevel1 = _POnboardSensorLevel1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 18),
    _POnboardSensorLevel1_Type()
)
pOnboardSensorLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorLevel1.setStatus("current")
_POnboardSensorLevel2_Type = Level
_POnboardSensorLevel2_Object = MibTableColumn
pOnboardSensorLevel2 = _POnboardSensorLevel2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 19),
    _POnboardSensorLevel2_Type()
)
pOnboardSensorLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorLevel2.setStatus("current")
_POnboardSensorLevel3_Type = Level
_POnboardSensorLevel3_Object = MibTableColumn
pOnboardSensorLevel3 = _POnboardSensorLevel3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 20),
    _POnboardSensorLevel3_Type()
)
pOnboardSensorLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorLevel3.setStatus("current")
_POnboardSensorLevel4_Type = Level
_POnboardSensorLevel4_Object = MibTableColumn
pOnboardSensorLevel4 = _POnboardSensorLevel4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 21),
    _POnboardSensorLevel4_Type()
)
pOnboardSensorLevel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorLevel4.setStatus("current")
_POnboardSensorLevel5_Type = Level
_POnboardSensorLevel5_Object = MibTableColumn
pOnboardSensorLevel5 = _POnboardSensorLevel5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 22),
    _POnboardSensorLevel5_Type()
)
pOnboardSensorLevel5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorLevel5.setStatus("current")
_POnboardSensorThresh0_Type = DescriptionString
_POnboardSensorThresh0_Object = MibTableColumn
pOnboardSensorThresh0 = _POnboardSensorThresh0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 28),
    _POnboardSensorThresh0_Type()
)
pOnboardSensorThresh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOnboardSensorThresh0.setStatus("current")
_POnboardSensorThresh1_Type = DescriptionString
_POnboardSensorThresh1_Object = MibTableColumn
pOnboardSensorThresh1 = _POnboardSensorThresh1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 29),
    _POnboardSensorThresh1_Type()
)
pOnboardSensorThresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorThresh1.setStatus("current")
_POnboardSensorThresh2_Type = DescriptionString
_POnboardSensorThresh2_Object = MibTableColumn
pOnboardSensorThresh2 = _POnboardSensorThresh2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 30),
    _POnboardSensorThresh2_Type()
)
pOnboardSensorThresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorThresh2.setStatus("current")
_POnboardSensorThresh3_Type = DescriptionString
_POnboardSensorThresh3_Object = MibTableColumn
pOnboardSensorThresh3 = _POnboardSensorThresh3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 31),
    _POnboardSensorThresh3_Type()
)
pOnboardSensorThresh3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorThresh3.setStatus("current")
_POnboardSensorThresh4_Type = DescriptionString
_POnboardSensorThresh4_Object = MibTableColumn
pOnboardSensorThresh4 = _POnboardSensorThresh4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 32),
    _POnboardSensorThresh4_Type()
)
pOnboardSensorThresh4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorThresh4.setStatus("current")
_POnboardSensorThresh5_Type = DescriptionString
_POnboardSensorThresh5_Object = MibTableColumn
pOnboardSensorThresh5 = _POnboardSensorThresh5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 33),
    _POnboardSensorThresh5_Type()
)
pOnboardSensorThresh5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOnboardSensorThresh5.setStatus("current")
_POnboardSensorUnits_Type = DescriptionString
_POnboardSensorUnits_Object = MibTableColumn
pOnboardSensorUnits = _POnboardSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 46),
    _POnboardSensorUnits_Type()
)
pOnboardSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOnboardSensorUnits.setStatus("current")
_POnboardSensorLiveDescription_Type = DescriptionString
_POnboardSensorLiveDescription_Object = MibTableColumn
pOnboardSensorLiveDescription = _POnboardSensorLiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 64),
    _POnboardSensorLiveDescription_Type()
)
pOnboardSensorLiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOnboardSensorLiveDescription.setStatus("current")
_POnboardSensorLiveLevel_Type = DescriptionString
_POnboardSensorLiveLevel_Object = MibTableColumn
pOnboardSensorLiveLevel = _POnboardSensorLiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 65),
    _POnboardSensorLiveLevel_Type()
)
pOnboardSensorLiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOnboardSensorLiveLevel.setStatus("current")
_POnboardSensorLiveRaw_Type = DescriptionString
_POnboardSensorLiveRaw_Object = MibTableColumn
pOnboardSensorLiveRaw = _POnboardSensorLiveRaw_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 66),
    _POnboardSensorLiveRaw_Type()
)
pOnboardSensorLiveRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOnboardSensorLiveRaw.setStatus("current")
_POnboardSensorLiveTime_Type = DescriptionString
_POnboardSensorLiveTime_Object = MibTableColumn
pOnboardSensorLiveTime = _POnboardSensorLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 67),
    _POnboardSensorLiveTime_Type()
)
pOnboardSensorLiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOnboardSensorLiveTime.setStatus("current")
_POnboardSensorTL1SID_Type = DescriptionString
_POnboardSensorTL1SID_Object = MibTableColumn
pOnboardSensorTL1SID = _POnboardSensorTL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 116),
    _POnboardSensorTL1SID_Type()
)
pOnboardSensorTL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorTL1SID.setStatus("current")
_POnboardSensorTL1COND_Type = DescriptionString
_POnboardSensorTL1COND_Object = MibTableColumn
pOnboardSensorTL1COND = _POnboardSensorTL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 117),
    _POnboardSensorTL1COND_Type()
)
pOnboardSensorTL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorTL1COND.setStatus("current")
_POnboardSensorTL1Eqpt_Type = DescriptionString
_POnboardSensorTL1Eqpt_Object = MibTableColumn
pOnboardSensorTL1Eqpt = _POnboardSensorTL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 118),
    _POnboardSensorTL1Eqpt_Type()
)
pOnboardSensorTL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorTL1Eqpt.setStatus("current")
_POnboardSensorTL1Env_Type = Boolean
_POnboardSensorTL1Env_Object = MibTableColumn
pOnboardSensorTL1Env = _POnboardSensorTL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 119),
    _POnboardSensorTL1Env_Type()
)
pOnboardSensorTL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorTL1Env.setStatus("current")
_POnboardSensorTL1Srveff_Type = TL1Srveff
_POnboardSensorTL1Srveff_Object = MibTableColumn
pOnboardSensorTL1Srveff = _POnboardSensorTL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 120),
    _POnboardSensorTL1Srveff_Type()
)
pOnboardSensorTL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorTL1Srveff.setStatus("current")
_POnboardSensorTL1Locn_Type = TL1Locn
_POnboardSensorTL1Locn_Object = MibTableColumn
pOnboardSensorTL1Locn = _POnboardSensorTL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 121),
    _POnboardSensorTL1Locn_Type()
)
pOnboardSensorTL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorTL1Locn.setStatus("current")
_POnboardSensorTL1Dirn_Type = TL1Dirn
_POnboardSensorTL1Dirn_Object = MibTableColumn
pOnboardSensorTL1Dirn = _POnboardSensorTL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 122),
    _POnboardSensorTL1Dirn_Type()
)
pOnboardSensorTL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pOnboardSensorTL1Dirn.setStatus("current")


class _POnboardSensorIndex_Type(Integer32):
    """Custom type pOnboardSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_POnboardSensorIndex_Type.__name__ = "Integer32"
_POnboardSensorIndex_Object = MibTableColumn
pOnboardSensorIndex = _POnboardSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 6, 1, 999),
    _POnboardSensorIndex_Type()
)
pOnboardSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pOnboardSensorIndex.setStatus("current")
_PNetDevicesTable_Object = MibTable
pNetDevicesTable = _PNetDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7)
)
if mibBuilder.loadTexts:
    pNetDevicesTable.setStatus("current")
_PNetDevicesEntry_Object = MibTableRow
pNetDevicesEntry = _PNetDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1)
)
pNetDevicesEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pNetDevicesIndex"),
)
if mibBuilder.loadTexts:
    pNetDevicesEntry.setStatus("current")
_PNetDevicesDescription_Type = DescriptionString
_PNetDevicesDescription_Object = MibTableColumn
pNetDevicesDescription = _PNetDevicesDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 3),
    _PNetDevicesDescription_Type()
)
pNetDevicesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesDescription.setStatus("current")
_PNetDevicesDesc0_Type = DescriptionString
_PNetDevicesDesc0_Object = MibTableColumn
pNetDevicesDesc0 = _PNetDevicesDesc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 4),
    _PNetDevicesDesc0_Type()
)
pNetDevicesDesc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesDesc0.setStatus("current")
_PNetDevicesDesc1_Type = DescriptionString
_PNetDevicesDesc1_Object = MibTableColumn
pNetDevicesDesc1 = _PNetDevicesDesc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 5),
    _PNetDevicesDesc1_Type()
)
pNetDevicesDesc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesDesc1.setStatus("current")
_PNetDevicesConfigured_Type = Configured
_PNetDevicesConfigured_Object = MibTableColumn
pNetDevicesConfigured = _PNetDevicesConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 10),
    _PNetDevicesConfigured_Type()
)
pNetDevicesConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesConfigured.setStatus("current")
_PNetDevicesSendEmail_Type = Boolean
_PNetDevicesSendEmail_Object = MibTableColumn
pNetDevicesSendEmail = _PNetDevicesSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 11),
    _PNetDevicesSendEmail_Type()
)
pNetDevicesSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesSendEmail.setStatus("current")
_PNetDevicesSendSNMPTrap_Type = Boolean
_PNetDevicesSendSNMPTrap_Object = MibTableColumn
pNetDevicesSendSNMPTrap = _PNetDevicesSendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 12),
    _PNetDevicesSendSNMPTrap_Type()
)
pNetDevicesSendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesSendSNMPTrap.setStatus("current")
_PNetDevicesIpAddress_Type = IpAddress
_PNetDevicesIpAddress_Object = MibTableColumn
pNetDevicesIpAddress = _PNetDevicesIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 14),
    _PNetDevicesIpAddress_Type()
)
pNetDevicesIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesIpAddress.setStatus("current")
_PNetDevicesLevel0_Type = Level
_PNetDevicesLevel0_Object = MibTableColumn
pNetDevicesLevel0 = _PNetDevicesLevel0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 17),
    _PNetDevicesLevel0_Type()
)
pNetDevicesLevel0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesLevel0.setStatus("current")
_PNetDevicesLevel1_Type = Level
_PNetDevicesLevel1_Object = MibTableColumn
pNetDevicesLevel1 = _PNetDevicesLevel1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 18),
    _PNetDevicesLevel1_Type()
)
pNetDevicesLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesLevel1.setStatus("current")
_PNetDevicesLiveDescription_Type = DescriptionString
_PNetDevicesLiveDescription_Object = MibTableColumn
pNetDevicesLiveDescription = _PNetDevicesLiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 64),
    _PNetDevicesLiveDescription_Type()
)
pNetDevicesLiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pNetDevicesLiveDescription.setStatus("current")
_PNetDevicesLiveLevel_Type = DescriptionString
_PNetDevicesLiveLevel_Object = MibTableColumn
pNetDevicesLiveLevel = _PNetDevicesLiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 65),
    _PNetDevicesLiveLevel_Type()
)
pNetDevicesLiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pNetDevicesLiveLevel.setStatus("current")
_PNetDevicesLiveRaw_Type = DescriptionString
_PNetDevicesLiveRaw_Object = MibTableColumn
pNetDevicesLiveRaw = _PNetDevicesLiveRaw_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 66),
    _PNetDevicesLiveRaw_Type()
)
pNetDevicesLiveRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pNetDevicesLiveRaw.setStatus("current")
_PNetDevicesLiveTime_Type = DescriptionString
_PNetDevicesLiveTime_Object = MibTableColumn
pNetDevicesLiveTime = _PNetDevicesLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 67),
    _PNetDevicesLiveTime_Type()
)
pNetDevicesLiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pNetDevicesLiveTime.setStatus("current")
_PNetDevicesTL1SID_Type = DescriptionString
_PNetDevicesTL1SID_Object = MibTableColumn
pNetDevicesTL1SID = _PNetDevicesTL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 116),
    _PNetDevicesTL1SID_Type()
)
pNetDevicesTL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesTL1SID.setStatus("current")
_PNetDevicesTL1COND_Type = DescriptionString
_PNetDevicesTL1COND_Object = MibTableColumn
pNetDevicesTL1COND = _PNetDevicesTL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 117),
    _PNetDevicesTL1COND_Type()
)
pNetDevicesTL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesTL1COND.setStatus("current")
_PNetDevicesTL1Eqpt_Type = DescriptionString
_PNetDevicesTL1Eqpt_Object = MibTableColumn
pNetDevicesTL1Eqpt = _PNetDevicesTL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 118),
    _PNetDevicesTL1Eqpt_Type()
)
pNetDevicesTL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesTL1Eqpt.setStatus("current")
_PNetDevicesTL1Env_Type = Boolean
_PNetDevicesTL1Env_Object = MibTableColumn
pNetDevicesTL1Env = _PNetDevicesTL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 119),
    _PNetDevicesTL1Env_Type()
)
pNetDevicesTL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesTL1Env.setStatus("current")
_PNetDevicesTL1Srveff_Type = TL1Srveff
_PNetDevicesTL1Srveff_Object = MibTableColumn
pNetDevicesTL1Srveff = _PNetDevicesTL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 120),
    _PNetDevicesTL1Srveff_Type()
)
pNetDevicesTL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesTL1Srveff.setStatus("current")
_PNetDevicesTL1Locn_Type = TL1Locn
_PNetDevicesTL1Locn_Object = MibTableColumn
pNetDevicesTL1Locn = _PNetDevicesTL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 121),
    _PNetDevicesTL1Locn_Type()
)
pNetDevicesTL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesTL1Locn.setStatus("current")
_PNetDevicesTL1Dirn_Type = TL1Dirn
_PNetDevicesTL1Dirn_Object = MibTableColumn
pNetDevicesTL1Dirn = _PNetDevicesTL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 122),
    _PNetDevicesTL1Dirn_Type()
)
pNetDevicesTL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetDevicesTL1Dirn.setStatus("current")


class _PNetDevicesIndex_Type(Integer32):
    """Custom type pNetDevicesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PNetDevicesIndex_Type.__name__ = "Integer32"
_PNetDevicesIndex_Object = MibTableColumn
pNetDevicesIndex = _PNetDevicesIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 7, 1, 999),
    _PNetDevicesIndex_Type()
)
pNetDevicesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pNetDevicesIndex.setStatus("current")
_PAccountsTable_Object = MibTable
pAccountsTable = _PAccountsTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 9)
)
if mibBuilder.loadTexts:
    pAccountsTable.setStatus("current")
_PAccountsEntry_Object = MibTableRow
pAccountsEntry = _PAccountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 9, 1)
)
pAccountsEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pAccountsIndex"),
)
if mibBuilder.loadTexts:
    pAccountsEntry.setStatus("current")
_PAccountsConfigured_Type = Configured
_PAccountsConfigured_Object = MibTableColumn
pAccountsConfigured = _PAccountsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 9, 1, 10),
    _PAccountsConfigured_Type()
)
pAccountsConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAccountsConfigured.setStatus("current")
_PAccountsName_Type = DescriptionString
_PAccountsName_Object = MibTableColumn
pAccountsName = _PAccountsName_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 9, 1, 25),
    _PAccountsName_Type()
)
pAccountsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAccountsName.setStatus("current")
_PAccountsEncPassword_Type = DescriptionString
_PAccountsEncPassword_Object = MibTableColumn
pAccountsEncPassword = _PAccountsEncPassword_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 9, 1, 27),
    _PAccountsEncPassword_Type()
)
pAccountsEncPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAccountsEncPassword.setStatus("current")
_PAccountsUserLevel_Type = Unsigned32
_PAccountsUserLevel_Object = MibTableColumn
pAccountsUserLevel = _PAccountsUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 9, 1, 55),
    _PAccountsUserLevel_Type()
)
pAccountsUserLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAccountsUserLevel.setStatus("current")
_PAccountsUnsecured_Type = Boolean
_PAccountsUnsecured_Object = MibTableColumn
pAccountsUnsecured = _PAccountsUnsecured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 9, 1, 77),
    _PAccountsUnsecured_Type()
)
pAccountsUnsecured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAccountsUnsecured.setStatus("current")
_PAccountsAuthKey_Type = DescriptionString
_PAccountsAuthKey_Object = MibTableColumn
pAccountsAuthKey = _PAccountsAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 9, 1, 140),
    _PAccountsAuthKey_Type()
)
pAccountsAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAccountsAuthKey.setStatus("current")
_PAccountsPrivKey_Type = DescriptionString
_PAccountsPrivKey_Object = MibTableColumn
pAccountsPrivKey = _PAccountsPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 9, 1, 141),
    _PAccountsPrivKey_Type()
)
pAccountsPrivKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAccountsPrivKey.setStatus("current")
_PAccountsSNMPAccess_Type = SNMPAccess
_PAccountsSNMPAccess_Object = MibTableColumn
pAccountsSNMPAccess = _PAccountsSNMPAccess_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 9, 1, 142),
    _PAccountsSNMPAccess_Type()
)
pAccountsSNMPAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pAccountsSNMPAccess.setStatus("current")


class _PAccountsIndex_Type(Integer32):
    """Custom type pAccountsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PAccountsIndex_Type.__name__ = "Integer32"
_PAccountsIndex_Object = MibTableColumn
pAccountsIndex = _PAccountsIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 9, 1, 999),
    _PAccountsIndex_Type()
)
pAccountsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pAccountsIndex.setStatus("current")
_Camera_ObjectIdentity = ObjectIdentity
camera = _Camera_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 10)
)
_CameraConfigured_Type = Configured
_CameraConfigured_Object = MibScalar
cameraConfigured = _CameraConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 10, 10),
    _CameraConfigured_Type()
)
cameraConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cameraConfigured.setStatus("current")
_CameraIpAddress_Type = IpAddress
_CameraIpAddress_Object = MibScalar
cameraIpAddress = _CameraIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 10, 14),
    _CameraIpAddress_Type()
)
cameraIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cameraIpAddress.setStatus("current")
_CameraCameraStyle_Type = CameraStyle
_CameraCameraStyle_Object = MibScalar
cameraCameraStyle = _CameraCameraStyle_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 10, 43),
    _CameraCameraStyle_Type()
)
cameraCameraStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cameraCameraStyle.setStatus("current")
_SnmpGeneral_ObjectIdentity = ObjectIdentity
snmpGeneral = _SnmpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 12)
)
_SnmpGeneralConfigured_Type = Configured
_SnmpGeneralConfigured_Object = MibScalar
snmpGeneralConfigured = _SnmpGeneralConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 12, 10),
    _SnmpGeneralConfigured_Type()
)
snmpGeneralConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGeneralConfigured.setStatus("current")
_SnmpGeneralReadPeriod_Type = Integer32
_SnmpGeneralReadPeriod_Object = MibScalar
snmpGeneralReadPeriod = _SnmpGeneralReadPeriod_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 12, 23),
    _SnmpGeneralReadPeriod_Type()
)
snmpGeneralReadPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGeneralReadPeriod.setStatus("current")
_SnmpGeneralGet_Type = DescriptionString
_SnmpGeneralGet_Object = MibScalar
snmpGeneralGet = _SnmpGeneralGet_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 12, 39),
    _SnmpGeneralGet_Type()
)
snmpGeneralGet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGeneralGet.setStatus("current")
_SnmpGeneralSet_Type = DescriptionString
_SnmpGeneralSet_Object = MibScalar
snmpGeneralSet = _SnmpGeneralSet_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 12, 40),
    _SnmpGeneralSet_Type()
)
snmpGeneralSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGeneralSet.setStatus("current")
_SnmpGeneralTrap_Type = DescriptionString
_SnmpGeneralTrap_Object = MibScalar
snmpGeneralTrap = _SnmpGeneralTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 12, 41),
    _SnmpGeneralTrap_Type()
)
snmpGeneralTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGeneralTrap.setStatus("current")
_SnmpGeneralIPPortNum_Type = Integer32
_SnmpGeneralIPPortNum_Object = MibScalar
snmpGeneralIPPortNum = _SnmpGeneralIPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 12, 73),
    _SnmpGeneralIPPortNum_Type()
)
snmpGeneralIPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGeneralIPPortNum.setStatus("current")
_SnmpGeneralEngineID_Type = DescriptionString
_SnmpGeneralEngineID_Object = MibScalar
snmpGeneralEngineID = _SnmpGeneralEngineID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 12, 143),
    _SnmpGeneralEngineID_Type()
)
snmpGeneralEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGeneralEngineID.setStatus("current")
_EmailGeneral_ObjectIdentity = ObjectIdentity
emailGeneral = _EmailGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 13)
)
_EmailGeneralAddress_Type = DescriptionString
_EmailGeneralAddress_Object = MibScalar
emailGeneralAddress = _EmailGeneralAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 13, 1),
    _EmailGeneralAddress_Type()
)
emailGeneralAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailGeneralAddress.setStatus("current")
_EmailGeneralConfigured_Type = Configured
_EmailGeneralConfigured_Object = MibScalar
emailGeneralConfigured = _EmailGeneralConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 13, 10),
    _EmailGeneralConfigured_Type()
)
emailGeneralConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailGeneralConfigured.setStatus("current")
_EmailGeneralIpAddress_Type = IpAddress
_EmailGeneralIpAddress_Object = MibScalar
emailGeneralIpAddress = _EmailGeneralIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 13, 14),
    _EmailGeneralIpAddress_Type()
)
emailGeneralIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailGeneralIpAddress.setStatus("current")
_EmailGeneralPassword_Type = DescriptionString
_EmailGeneralPassword_Object = MibScalar
emailGeneralPassword = _EmailGeneralPassword_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 13, 26),
    _EmailGeneralPassword_Type()
)
emailGeneralPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailGeneralPassword.setStatus("current")
_EmailGeneralIPPortNum_Type = Integer32
_EmailGeneralIPPortNum_Object = MibScalar
emailGeneralIPPortNum = _EmailGeneralIPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 13, 73),
    _EmailGeneralIPPortNum_Type()
)
emailGeneralIPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailGeneralIPPortNum.setStatus("current")
_PSerialTable_Object = MibTable
pSerialTable = _PSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14)
)
if mibBuilder.loadTexts:
    pSerialTable.setStatus("current")
_PSerialEntry_Object = MibTableRow
pSerialEntry = _PSerialEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1)
)
pSerialEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pSerialIndex"),
)
if mibBuilder.loadTexts:
    pSerialEntry.setStatus("current")
_PSerialDescription_Type = DescriptionString
_PSerialDescription_Object = MibTableColumn
pSerialDescription = _PSerialDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 3),
    _PSerialDescription_Type()
)
pSerialDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSerialDescription.setStatus("current")
_PSerialConfigured_Type = Configured
_PSerialConfigured_Object = MibTableColumn
pSerialConfigured = _PSerialConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 10),
    _PSerialConfigured_Type()
)
pSerialConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSerialConfigured.setStatus("current")
_PSerialIpAddress_Type = IpAddress
_PSerialIpAddress_Object = MibTableColumn
pSerialIpAddress = _PSerialIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 14),
    _PSerialIpAddress_Type()
)
pSerialIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSerialIpAddress.setStatus("current")
_PSerialReadPeriod_Type = Integer32
_PSerialReadPeriod_Object = MibTableColumn
pSerialReadPeriod = _PSerialReadPeriod_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 23),
    _PSerialReadPeriod_Type()
)
pSerialReadPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSerialReadPeriod.setStatus("current")
_PSerialBaudRate_Type = BaudRate
_PSerialBaudRate_Object = MibTableColumn
pSerialBaudRate = _PSerialBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 57),
    _PSerialBaudRate_Type()
)
pSerialBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSerialBaudRate.setStatus("current")
_PSerialDataBits_Type = DataBits
_PSerialDataBits_Object = MibTableColumn
pSerialDataBits = _PSerialDataBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 58),
    _PSerialDataBits_Type()
)
pSerialDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSerialDataBits.setStatus("current")
_PSerialParity_Type = Parity
_PSerialParity_Object = MibTableColumn
pSerialParity = _PSerialParity_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 59),
    _PSerialParity_Type()
)
pSerialParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSerialParity.setStatus("current")
_PSerialStopBits_Type = StopBits
_PSerialStopBits_Object = MibTableColumn
pSerialStopBits = _PSerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 60),
    _PSerialStopBits_Type()
)
pSerialStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSerialStopBits.setStatus("current")
_PSerialProtocol_Type = Protocol
_PSerialProtocol_Object = MibTableColumn
pSerialProtocol = _PSerialProtocol_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 61),
    _PSerialProtocol_Type()
)
pSerialProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSerialProtocol.setStatus("current")
_PSerialSerialRTS_Type = SerialRTS
_PSerialSerialRTS_Object = MibTableColumn
pSerialSerialRTS = _PSerialSerialRTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 62),
    _PSerialSerialRTS_Type()
)
pSerialSerialRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSerialSerialRTS.setStatus("current")
_PSerialSerialCTS_Type = SerialCTS
_PSerialSerialCTS_Object = MibTableColumn
pSerialSerialCTS = _PSerialSerialCTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 63),
    _PSerialSerialCTS_Type()
)
pSerialSerialCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSerialSerialCTS.setStatus("current")
_PSerialPresent_Type = Boolean
_PSerialPresent_Object = MibTableColumn
pSerialPresent = _PSerialPresent_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 68),
    _PSerialPresent_Type()
)
pSerialPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSerialPresent.setStatus("current")
_PSerialIPPortNum_Type = Integer32
_PSerialIPPortNum_Object = MibTableColumn
pSerialIPPortNum = _PSerialIPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 73),
    _PSerialIPPortNum_Type()
)
pSerialIPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSerialIPPortNum.setStatus("current")
_PSerialPortType_Type = PortType
_PSerialPortType_Object = MibTableColumn
pSerialPortType = _PSerialPortType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 76),
    _PSerialPortType_Type()
)
pSerialPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSerialPortType.setStatus("current")


class _PSerialIndex_Type(Integer32):
    """Custom type pSerialIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PSerialIndex_Type.__name__ = "Integer32"
_PSerialIndex_Object = MibTableColumn
pSerialIndex = _PSerialIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 14, 1, 999),
    _PSerialIndex_Type()
)
pSerialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSerialIndex.setStatus("current")
_PSelfTestTable_Object = MibTable
pSelfTestTable = _PSelfTestTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 15)
)
if mibBuilder.loadTexts:
    pSelfTestTable.setStatus("current")
_PSelfTestEntry_Object = MibTableRow
pSelfTestEntry = _PSelfTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 15, 1)
)
pSelfTestEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pSelfTestIndex"),
)
if mibBuilder.loadTexts:
    pSelfTestEntry.setStatus("current")
_PSelfTestDescription_Type = DescriptionString
_PSelfTestDescription_Object = MibTableColumn
pSelfTestDescription = _PSelfTestDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 15, 1, 3),
    _PSelfTestDescription_Type()
)
pSelfTestDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSelfTestDescription.setStatus("current")
_PSelfTestConfigured_Type = Configured
_PSelfTestConfigured_Object = MibTableColumn
pSelfTestConfigured = _PSelfTestConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 15, 1, 10),
    _PSelfTestConfigured_Type()
)
pSelfTestConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSelfTestConfigured.setStatus("current")


class _PSelfTestIndex_Type(Integer32):
    """Custom type pSelfTestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PSelfTestIndex_Type.__name__ = "Integer32"
_PSelfTestIndex_Object = MibTableColumn
pSelfTestIndex = _PSelfTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 15, 1, 999),
    _PSelfTestIndex_Type()
)
pSelfTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSelfTestIndex.setStatus("current")
_PInternalFaultsTable_Object = MibTable
pInternalFaultsTable = _PInternalFaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16)
)
if mibBuilder.loadTexts:
    pInternalFaultsTable.setStatus("current")
_PInternalFaultsEntry_Object = MibTableRow
pInternalFaultsEntry = _PInternalFaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1)
)
pInternalFaultsEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsIndex"),
)
if mibBuilder.loadTexts:
    pInternalFaultsEntry.setStatus("current")
_PInternalFaultsDescription_Type = DescriptionString
_PInternalFaultsDescription_Object = MibTableColumn
pInternalFaultsDescription = _PInternalFaultsDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 3),
    _PInternalFaultsDescription_Type()
)
pInternalFaultsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pInternalFaultsDescription.setStatus("current")
_PInternalFaultsDesc0_Type = DescriptionString
_PInternalFaultsDesc0_Object = MibTableColumn
pInternalFaultsDesc0 = _PInternalFaultsDesc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 4),
    _PInternalFaultsDesc0_Type()
)
pInternalFaultsDesc0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pInternalFaultsDesc0.setStatus("current")
_PInternalFaultsDesc1_Type = DescriptionString
_PInternalFaultsDesc1_Object = MibTableColumn
pInternalFaultsDesc1 = _PInternalFaultsDesc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 5),
    _PInternalFaultsDesc1_Type()
)
pInternalFaultsDesc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pInternalFaultsDesc1.setStatus("current")
_PInternalFaultsDesc2_Type = DescriptionString
_PInternalFaultsDesc2_Object = MibTableColumn
pInternalFaultsDesc2 = _PInternalFaultsDesc2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 6),
    _PInternalFaultsDesc2_Type()
)
pInternalFaultsDesc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pInternalFaultsDesc2.setStatus("current")
_PInternalFaultsDesc3_Type = DescriptionString
_PInternalFaultsDesc3_Object = MibTableColumn
pInternalFaultsDesc3 = _PInternalFaultsDesc3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 7),
    _PInternalFaultsDesc3_Type()
)
pInternalFaultsDesc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pInternalFaultsDesc3.setStatus("current")
_PInternalFaultsSendEmail_Type = Boolean
_PInternalFaultsSendEmail_Object = MibTableColumn
pInternalFaultsSendEmail = _PInternalFaultsSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 11),
    _PInternalFaultsSendEmail_Type()
)
pInternalFaultsSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pInternalFaultsSendEmail.setStatus("current")
_PInternalFaultsSendSNMPTrap_Type = Boolean
_PInternalFaultsSendSNMPTrap_Object = MibTableColumn
pInternalFaultsSendSNMPTrap = _PInternalFaultsSendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 12),
    _PInternalFaultsSendSNMPTrap_Type()
)
pInternalFaultsSendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pInternalFaultsSendSNMPTrap.setStatus("current")
_PInternalFaultsLevel0_Type = Level
_PInternalFaultsLevel0_Object = MibTableColumn
pInternalFaultsLevel0 = _PInternalFaultsLevel0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 17),
    _PInternalFaultsLevel0_Type()
)
pInternalFaultsLevel0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pInternalFaultsLevel0.setStatus("current")
_PInternalFaultsLevel1_Type = Level
_PInternalFaultsLevel1_Object = MibTableColumn
pInternalFaultsLevel1 = _PInternalFaultsLevel1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 18),
    _PInternalFaultsLevel1_Type()
)
pInternalFaultsLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pInternalFaultsLevel1.setStatus("current")
_PInternalFaultsLevel2_Type = Level
_PInternalFaultsLevel2_Object = MibTableColumn
pInternalFaultsLevel2 = _PInternalFaultsLevel2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 19),
    _PInternalFaultsLevel2_Type()
)
pInternalFaultsLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pInternalFaultsLevel2.setStatus("current")
_PInternalFaultsLevel3_Type = Level
_PInternalFaultsLevel3_Object = MibTableColumn
pInternalFaultsLevel3 = _PInternalFaultsLevel3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 20),
    _PInternalFaultsLevel3_Type()
)
pInternalFaultsLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pInternalFaultsLevel3.setStatus("current")
_PInternalFaultsIgnoreOff_Type = Boolean
_PInternalFaultsIgnoreOff_Object = MibTableColumn
pInternalFaultsIgnoreOff = _PInternalFaultsIgnoreOff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 50),
    _PInternalFaultsIgnoreOff_Type()
)
pInternalFaultsIgnoreOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pInternalFaultsIgnoreOff.setStatus("current")
_PInternalFaultsLiveDescription_Type = DescriptionString
_PInternalFaultsLiveDescription_Object = MibTableColumn
pInternalFaultsLiveDescription = _PInternalFaultsLiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 64),
    _PInternalFaultsLiveDescription_Type()
)
pInternalFaultsLiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pInternalFaultsLiveDescription.setStatus("current")
_PInternalFaultsLiveLevel_Type = DescriptionString
_PInternalFaultsLiveLevel_Object = MibTableColumn
pInternalFaultsLiveLevel = _PInternalFaultsLiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 65),
    _PInternalFaultsLiveLevel_Type()
)
pInternalFaultsLiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pInternalFaultsLiveLevel.setStatus("current")
_PInternalFaultsLiveTime_Type = DescriptionString
_PInternalFaultsLiveTime_Object = MibTableColumn
pInternalFaultsLiveTime = _PInternalFaultsLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 67),
    _PInternalFaultsLiveTime_Type()
)
pInternalFaultsLiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pInternalFaultsLiveTime.setStatus("current")


class _PInternalFaultsIndex_Type(Integer32):
    """Custom type pInternalFaultsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_PInternalFaultsIndex_Type.__name__ = "Integer32"
_PInternalFaultsIndex_Object = MibTableColumn
pInternalFaultsIndex = _PInternalFaultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 16, 1, 999),
    _PInternalFaultsIndex_Type()
)
pInternalFaultsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pInternalFaultsIndex.setStatus("current")
_PSlotInfoTable_Object = MibTable
pSlotInfoTable = _PSlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 17)
)
if mibBuilder.loadTexts:
    pSlotInfoTable.setStatus("current")
_PSlotInfoEntry_Object = MibTableRow
pSlotInfoEntry = _PSlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 17, 1)
)
pSlotInfoEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    pSlotInfoEntry.setStatus("current")
_PSlotInfoDescription_Type = DescriptionString
_PSlotInfoDescription_Object = MibTableColumn
pSlotInfoDescription = _PSlotInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 17, 1, 3),
    _PSlotInfoDescription_Type()
)
pSlotInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlotInfoDescription.setStatus("current")
_PSlotInfoRecord_Type = Integer32
_PSlotInfoRecord_Object = MibTableColumn
pSlotInfoRecord = _PSlotInfoRecord_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 17, 1, 35),
    _PSlotInfoRecord_Type()
)
pSlotInfoRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlotInfoRecord.setStatus("current")
_PSlotInfoPresent_Type = Boolean
_PSlotInfoPresent_Object = MibTableColumn
pSlotInfoPresent = _PSlotInfoPresent_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 17, 1, 68),
    _PSlotInfoPresent_Type()
)
pSlotInfoPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlotInfoPresent.setStatus("current")
_PSlotInfoSlotId_Type = SlotId
_PSlotInfoSlotId_Object = MibTableColumn
pSlotInfoSlotId = _PSlotInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 17, 1, 69),
    _PSlotInfoSlotId_Type()
)
pSlotInfoSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlotInfoSlotId.setStatus("current")


class _PSlotInfoIndex_Type(Integer32):
    """Custom type pSlotInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_PSlotInfoIndex_Type.__name__ = "Integer32"
_PSlotInfoIndex_Object = MibTableColumn
pSlotInfoIndex = _PSlotInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 17, 1, 999),
    _PSlotInfoIndex_Type()
)
pSlotInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlotInfoIndex.setStatus("current")
_PSlot1Table_Object = MibTable
pSlot1Table = _PSlot1Table_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18)
)
if mibBuilder.loadTexts:
    pSlot1Table.setStatus("current")
_PSlot1Entry_Object = MibTableRow
pSlot1Entry = _PSlot1Entry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1)
)
pSlot1Entry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pSlot1Index"),
)
if mibBuilder.loadTexts:
    pSlot1Entry.setStatus("current")
_PSlot1Description_Type = DescriptionString
_PSlot1Description_Object = MibTableColumn
pSlot1Description = _PSlot1Description_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 3),
    _PSlot1Description_Type()
)
pSlot1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Description.setStatus("current")
_PSlot1Desc0_Type = DescriptionString
_PSlot1Desc0_Object = MibTableColumn
pSlot1Desc0 = _PSlot1Desc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 4),
    _PSlot1Desc0_Type()
)
pSlot1Desc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Desc0.setStatus("current")
_PSlot1Desc1_Type = DescriptionString
_PSlot1Desc1_Object = MibTableColumn
pSlot1Desc1 = _PSlot1Desc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 5),
    _PSlot1Desc1_Type()
)
pSlot1Desc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Desc1.setStatus("current")
_PSlot1Desc2_Type = DescriptionString
_PSlot1Desc2_Object = MibTableColumn
pSlot1Desc2 = _PSlot1Desc2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 6),
    _PSlot1Desc2_Type()
)
pSlot1Desc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Desc2.setStatus("current")
_PSlot1Desc3_Type = DescriptionString
_PSlot1Desc3_Object = MibTableColumn
pSlot1Desc3 = _PSlot1Desc3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 7),
    _PSlot1Desc3_Type()
)
pSlot1Desc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Desc3.setStatus("current")
_PSlot1Desc4_Type = DescriptionString
_PSlot1Desc4_Object = MibTableColumn
pSlot1Desc4 = _PSlot1Desc4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 8),
    _PSlot1Desc4_Type()
)
pSlot1Desc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Desc4.setStatus("current")
_PSlot1Desc5_Type = DescriptionString
_PSlot1Desc5_Object = MibTableColumn
pSlot1Desc5 = _PSlot1Desc5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 9),
    _PSlot1Desc5_Type()
)
pSlot1Desc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Desc5.setStatus("current")
_PSlot1Configured_Type = Configured
_PSlot1Configured_Object = MibTableColumn
pSlot1Configured = _PSlot1Configured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 10),
    _PSlot1Configured_Type()
)
pSlot1Configured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Configured.setStatus("current")
_PSlot1SendEmail_Type = Boolean
_PSlot1SendEmail_Object = MibTableColumn
pSlot1SendEmail = _PSlot1SendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 11),
    _PSlot1SendEmail_Type()
)
pSlot1SendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1SendEmail.setStatus("current")
_PSlot1SendSNMPTrap_Type = Boolean
_PSlot1SendSNMPTrap_Object = MibTableColumn
pSlot1SendSNMPTrap = _PSlot1SendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 12),
    _PSlot1SendSNMPTrap_Type()
)
pSlot1SendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1SendSNMPTrap.setStatus("current")
_PSlot1IpAddress_Type = IpAddress
_PSlot1IpAddress_Object = MibTableColumn
pSlot1IpAddress = _PSlot1IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 14),
    _PSlot1IpAddress_Type()
)
pSlot1IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1IpAddress.setStatus("current")
_PSlot1Level0_Type = Level
_PSlot1Level0_Object = MibTableColumn
pSlot1Level0 = _PSlot1Level0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 17),
    _PSlot1Level0_Type()
)
pSlot1Level0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Level0.setStatus("current")
_PSlot1Level1_Type = Level
_PSlot1Level1_Object = MibTableColumn
pSlot1Level1 = _PSlot1Level1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 18),
    _PSlot1Level1_Type()
)
pSlot1Level1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Level1.setStatus("current")
_PSlot1Level2_Type = Level
_PSlot1Level2_Object = MibTableColumn
pSlot1Level2 = _PSlot1Level2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 19),
    _PSlot1Level2_Type()
)
pSlot1Level2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Level2.setStatus("current")
_PSlot1Level3_Type = Level
_PSlot1Level3_Object = MibTableColumn
pSlot1Level3 = _PSlot1Level3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 20),
    _PSlot1Level3_Type()
)
pSlot1Level3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Level3.setStatus("current")
_PSlot1Level4_Type = Level
_PSlot1Level4_Object = MibTableColumn
pSlot1Level4 = _PSlot1Level4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 21),
    _PSlot1Level4_Type()
)
pSlot1Level4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Level4.setStatus("current")
_PSlot1Level5_Type = Level
_PSlot1Level5_Object = MibTableColumn
pSlot1Level5 = _PSlot1Level5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 22),
    _PSlot1Level5_Type()
)
pSlot1Level5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Level5.setStatus("current")
_PSlot1ReadPeriod_Type = Integer32
_PSlot1ReadPeriod_Object = MibTableColumn
pSlot1ReadPeriod = _PSlot1ReadPeriod_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 23),
    _PSlot1ReadPeriod_Type()
)
pSlot1ReadPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1ReadPeriod.setStatus("current")
_PSlot1Thresh0_Type = DescriptionString
_PSlot1Thresh0_Object = MibTableColumn
pSlot1Thresh0 = _PSlot1Thresh0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 28),
    _PSlot1Thresh0_Type()
)
pSlot1Thresh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot1Thresh0.setStatus("current")
_PSlot1Thresh1_Type = DescriptionString
_PSlot1Thresh1_Object = MibTableColumn
pSlot1Thresh1 = _PSlot1Thresh1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 29),
    _PSlot1Thresh1_Type()
)
pSlot1Thresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Thresh1.setStatus("current")
_PSlot1Thresh2_Type = DescriptionString
_PSlot1Thresh2_Object = MibTableColumn
pSlot1Thresh2 = _PSlot1Thresh2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 30),
    _PSlot1Thresh2_Type()
)
pSlot1Thresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Thresh2.setStatus("current")
_PSlot1Thresh3_Type = DescriptionString
_PSlot1Thresh3_Object = MibTableColumn
pSlot1Thresh3 = _PSlot1Thresh3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 31),
    _PSlot1Thresh3_Type()
)
pSlot1Thresh3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Thresh3.setStatus("current")
_PSlot1Thresh4_Type = DescriptionString
_PSlot1Thresh4_Object = MibTableColumn
pSlot1Thresh4 = _PSlot1Thresh4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 32),
    _PSlot1Thresh4_Type()
)
pSlot1Thresh4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Thresh4.setStatus("current")
_PSlot1Thresh5_Type = DescriptionString
_PSlot1Thresh5_Object = MibTableColumn
pSlot1Thresh5 = _PSlot1Thresh5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 33),
    _PSlot1Thresh5_Type()
)
pSlot1Thresh5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot1Thresh5.setStatus("current")
_PSlot1ContactStyle_Type = ContactStyle
_PSlot1ContactStyle_Object = MibTableColumn
pSlot1ContactStyle = _PSlot1ContactStyle_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 44),
    _PSlot1ContactStyle_Type()
)
pSlot1ContactStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1ContactStyle.setStatus("current")
_PSlot1Units_Type = DescriptionString
_PSlot1Units_Object = MibTableColumn
pSlot1Units = _PSlot1Units_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 46),
    _PSlot1Units_Type()
)
pSlot1Units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot1Units.setStatus("current")
_PSlot1OutputMode_Type = OutputMode
_PSlot1OutputMode_Object = MibTableColumn
pSlot1OutputMode = _PSlot1OutputMode_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 47),
    _PSlot1OutputMode_Type()
)
pSlot1OutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1OutputMode.setStatus("current")
_PSlot1OutputState_Type = OutputState
_PSlot1OutputState_Object = MibTableColumn
pSlot1OutputState = _PSlot1OutputState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 48),
    _PSlot1OutputState_Type()
)
pSlot1OutputState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1OutputState.setStatus("current")
_PSlot1OutputAuto_Type = Integer32
_PSlot1OutputAuto_Object = MibTableColumn
pSlot1OutputAuto = _PSlot1OutputAuto_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 49),
    _PSlot1OutputAuto_Type()
)
pSlot1OutputAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1OutputAuto.setStatus("current")
_PSlot1BaudRate_Type = BaudRate
_PSlot1BaudRate_Object = MibTableColumn
pSlot1BaudRate = _PSlot1BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 57),
    _PSlot1BaudRate_Type()
)
pSlot1BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1BaudRate.setStatus("current")
_PSlot1DataBits_Type = DataBits
_PSlot1DataBits_Object = MibTableColumn
pSlot1DataBits = _PSlot1DataBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 58),
    _PSlot1DataBits_Type()
)
pSlot1DataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1DataBits.setStatus("current")
_PSlot1Parity_Type = Parity
_PSlot1Parity_Object = MibTableColumn
pSlot1Parity = _PSlot1Parity_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 59),
    _PSlot1Parity_Type()
)
pSlot1Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Parity.setStatus("current")
_PSlot1StopBits_Type = StopBits
_PSlot1StopBits_Object = MibTableColumn
pSlot1StopBits = _PSlot1StopBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 60),
    _PSlot1StopBits_Type()
)
pSlot1StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1StopBits.setStatus("current")
_PSlot1Protocol_Type = Protocol
_PSlot1Protocol_Object = MibTableColumn
pSlot1Protocol = _PSlot1Protocol_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 61),
    _PSlot1Protocol_Type()
)
pSlot1Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1Protocol.setStatus("current")
_PSlot1SerialRTS_Type = SerialRTS
_PSlot1SerialRTS_Object = MibTableColumn
pSlot1SerialRTS = _PSlot1SerialRTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 62),
    _PSlot1SerialRTS_Type()
)
pSlot1SerialRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1SerialRTS.setStatus("current")
_PSlot1SerialCTS_Type = SerialCTS
_PSlot1SerialCTS_Object = MibTableColumn
pSlot1SerialCTS = _PSlot1SerialCTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 63),
    _PSlot1SerialCTS_Type()
)
pSlot1SerialCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1SerialCTS.setStatus("current")
_PSlot1LiveDescription_Type = DescriptionString
_PSlot1LiveDescription_Object = MibTableColumn
pSlot1LiveDescription = _PSlot1LiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 64),
    _PSlot1LiveDescription_Type()
)
pSlot1LiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot1LiveDescription.setStatus("current")
_PSlot1LiveLevel_Type = DescriptionString
_PSlot1LiveLevel_Object = MibTableColumn
pSlot1LiveLevel = _PSlot1LiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 65),
    _PSlot1LiveLevel_Type()
)
pSlot1LiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot1LiveLevel.setStatus("current")
_PSlot1LiveRaw_Type = DescriptionString
_PSlot1LiveRaw_Object = MibTableColumn
pSlot1LiveRaw = _PSlot1LiveRaw_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 66),
    _PSlot1LiveRaw_Type()
)
pSlot1LiveRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot1LiveRaw.setStatus("current")
_PSlot1LiveTime_Type = DescriptionString
_PSlot1LiveTime_Object = MibTableColumn
pSlot1LiveTime = _PSlot1LiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 67),
    _PSlot1LiveTime_Type()
)
pSlot1LiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot1LiveTime.setStatus("current")
_PSlot1Present_Type = Boolean
_PSlot1Present_Object = MibTableColumn
pSlot1Present = _PSlot1Present_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 68),
    _PSlot1Present_Type()
)
pSlot1Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot1Present.setStatus("current")
_PSlot1OutputAutoPkg_Type = Integer32
_PSlot1OutputAutoPkg_Object = MibTableColumn
pSlot1OutputAutoPkg = _PSlot1OutputAutoPkg_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 71),
    _PSlot1OutputAutoPkg_Type()
)
pSlot1OutputAutoPkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1OutputAutoPkg.setStatus("current")
_PSlot1VoltageRange_Type = VoltageRange
_PSlot1VoltageRange_Object = MibTableColumn
pSlot1VoltageRange = _PSlot1VoltageRange_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 72),
    _PSlot1VoltageRange_Type()
)
pSlot1VoltageRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot1VoltageRange.setStatus("current")
_PSlot1IPPortNum_Type = Integer32
_PSlot1IPPortNum_Object = MibTableColumn
pSlot1IPPortNum = _PSlot1IPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 73),
    _PSlot1IPPortNum_Type()
)
pSlot1IPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1IPPortNum.setStatus("current")
_PSlot1IOFormat_Type = IOFormat
_PSlot1IOFormat_Object = MibTableColumn
pSlot1IOFormat = _PSlot1IOFormat_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 75),
    _PSlot1IOFormat_Type()
)
pSlot1IOFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot1IOFormat.setStatus("current")
_PSlot1PortType_Type = PortType
_PSlot1PortType_Object = MibTableColumn
pSlot1PortType = _PSlot1PortType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 76),
    _PSlot1PortType_Type()
)
pSlot1PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot1PortType.setStatus("current")
_PSlot1TL1SID_Type = DescriptionString
_PSlot1TL1SID_Object = MibTableColumn
pSlot1TL1SID = _PSlot1TL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 116),
    _PSlot1TL1SID_Type()
)
pSlot1TL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1TL1SID.setStatus("current")
_PSlot1TL1COND_Type = DescriptionString
_PSlot1TL1COND_Object = MibTableColumn
pSlot1TL1COND = _PSlot1TL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 117),
    _PSlot1TL1COND_Type()
)
pSlot1TL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1TL1COND.setStatus("current")
_PSlot1TL1Eqpt_Type = DescriptionString
_PSlot1TL1Eqpt_Object = MibTableColumn
pSlot1TL1Eqpt = _PSlot1TL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 118),
    _PSlot1TL1Eqpt_Type()
)
pSlot1TL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1TL1Eqpt.setStatus("current")
_PSlot1TL1Env_Type = Boolean
_PSlot1TL1Env_Object = MibTableColumn
pSlot1TL1Env = _PSlot1TL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 119),
    _PSlot1TL1Env_Type()
)
pSlot1TL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1TL1Env.setStatus("current")
_PSlot1TL1Srveff_Type = TL1Srveff
_PSlot1TL1Srveff_Object = MibTableColumn
pSlot1TL1Srveff = _PSlot1TL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 120),
    _PSlot1TL1Srveff_Type()
)
pSlot1TL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1TL1Srveff.setStatus("current")
_PSlot1TL1Locn_Type = TL1Locn
_PSlot1TL1Locn_Object = MibTableColumn
pSlot1TL1Locn = _PSlot1TL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 121),
    _PSlot1TL1Locn_Type()
)
pSlot1TL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1TL1Locn.setStatus("current")
_PSlot1TL1Dirn_Type = TL1Dirn
_PSlot1TL1Dirn_Object = MibTableColumn
pSlot1TL1Dirn = _PSlot1TL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 122),
    _PSlot1TL1Dirn_Type()
)
pSlot1TL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1TL1Dirn.setStatus("current")
_PSlot1SensorType_Type = SensorType
_PSlot1SensorType_Object = MibTableColumn
pSlot1SensorType = _PSlot1SensorType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 131),
    _PSlot1SensorType_Type()
)
pSlot1SensorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot1SensorType.setStatus("current")


class _PSlot1Index_Type(Integer32):
    """Custom type pSlot1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PSlot1Index_Type.__name__ = "Integer32"
_PSlot1Index_Object = MibTableColumn
pSlot1Index = _PSlot1Index_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 18, 1, 999),
    _PSlot1Index_Type()
)
pSlot1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot1Index.setStatus("current")
_PSlot2Table_Object = MibTable
pSlot2Table = _PSlot2Table_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19)
)
if mibBuilder.loadTexts:
    pSlot2Table.setStatus("current")
_PSlot2Entry_Object = MibTableRow
pSlot2Entry = _PSlot2Entry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1)
)
pSlot2Entry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pSlot2Index"),
)
if mibBuilder.loadTexts:
    pSlot2Entry.setStatus("current")
_PSlot2Description_Type = DescriptionString
_PSlot2Description_Object = MibTableColumn
pSlot2Description = _PSlot2Description_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 3),
    _PSlot2Description_Type()
)
pSlot2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Description.setStatus("current")
_PSlot2Desc0_Type = DescriptionString
_PSlot2Desc0_Object = MibTableColumn
pSlot2Desc0 = _PSlot2Desc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 4),
    _PSlot2Desc0_Type()
)
pSlot2Desc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Desc0.setStatus("current")
_PSlot2Desc1_Type = DescriptionString
_PSlot2Desc1_Object = MibTableColumn
pSlot2Desc1 = _PSlot2Desc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 5),
    _PSlot2Desc1_Type()
)
pSlot2Desc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Desc1.setStatus("current")
_PSlot2Desc2_Type = DescriptionString
_PSlot2Desc2_Object = MibTableColumn
pSlot2Desc2 = _PSlot2Desc2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 6),
    _PSlot2Desc2_Type()
)
pSlot2Desc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Desc2.setStatus("current")
_PSlot2Desc3_Type = DescriptionString
_PSlot2Desc3_Object = MibTableColumn
pSlot2Desc3 = _PSlot2Desc3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 7),
    _PSlot2Desc3_Type()
)
pSlot2Desc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Desc3.setStatus("current")
_PSlot2Desc4_Type = DescriptionString
_PSlot2Desc4_Object = MibTableColumn
pSlot2Desc4 = _PSlot2Desc4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 8),
    _PSlot2Desc4_Type()
)
pSlot2Desc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Desc4.setStatus("current")
_PSlot2Desc5_Type = DescriptionString
_PSlot2Desc5_Object = MibTableColumn
pSlot2Desc5 = _PSlot2Desc5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 9),
    _PSlot2Desc5_Type()
)
pSlot2Desc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Desc5.setStatus("current")
_PSlot2Configured_Type = Configured
_PSlot2Configured_Object = MibTableColumn
pSlot2Configured = _PSlot2Configured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 10),
    _PSlot2Configured_Type()
)
pSlot2Configured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Configured.setStatus("current")
_PSlot2SendEmail_Type = Boolean
_PSlot2SendEmail_Object = MibTableColumn
pSlot2SendEmail = _PSlot2SendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 11),
    _PSlot2SendEmail_Type()
)
pSlot2SendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2SendEmail.setStatus("current")
_PSlot2SendSNMPTrap_Type = Boolean
_PSlot2SendSNMPTrap_Object = MibTableColumn
pSlot2SendSNMPTrap = _PSlot2SendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 12),
    _PSlot2SendSNMPTrap_Type()
)
pSlot2SendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2SendSNMPTrap.setStatus("current")
_PSlot2IpAddress_Type = IpAddress
_PSlot2IpAddress_Object = MibTableColumn
pSlot2IpAddress = _PSlot2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 14),
    _PSlot2IpAddress_Type()
)
pSlot2IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2IpAddress.setStatus("current")
_PSlot2Level0_Type = Level
_PSlot2Level0_Object = MibTableColumn
pSlot2Level0 = _PSlot2Level0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 17),
    _PSlot2Level0_Type()
)
pSlot2Level0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Level0.setStatus("current")
_PSlot2Level1_Type = Level
_PSlot2Level1_Object = MibTableColumn
pSlot2Level1 = _PSlot2Level1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 18),
    _PSlot2Level1_Type()
)
pSlot2Level1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Level1.setStatus("current")
_PSlot2Level2_Type = Level
_PSlot2Level2_Object = MibTableColumn
pSlot2Level2 = _PSlot2Level2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 19),
    _PSlot2Level2_Type()
)
pSlot2Level2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Level2.setStatus("current")
_PSlot2Level3_Type = Level
_PSlot2Level3_Object = MibTableColumn
pSlot2Level3 = _PSlot2Level3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 20),
    _PSlot2Level3_Type()
)
pSlot2Level3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Level3.setStatus("current")
_PSlot2Level4_Type = Level
_PSlot2Level4_Object = MibTableColumn
pSlot2Level4 = _PSlot2Level4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 21),
    _PSlot2Level4_Type()
)
pSlot2Level4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Level4.setStatus("current")
_PSlot2Level5_Type = Level
_PSlot2Level5_Object = MibTableColumn
pSlot2Level5 = _PSlot2Level5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 22),
    _PSlot2Level5_Type()
)
pSlot2Level5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Level5.setStatus("current")
_PSlot2ReadPeriod_Type = Integer32
_PSlot2ReadPeriod_Object = MibTableColumn
pSlot2ReadPeriod = _PSlot2ReadPeriod_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 23),
    _PSlot2ReadPeriod_Type()
)
pSlot2ReadPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2ReadPeriod.setStatus("current")
_PSlot2Thresh0_Type = DescriptionString
_PSlot2Thresh0_Object = MibTableColumn
pSlot2Thresh0 = _PSlot2Thresh0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 28),
    _PSlot2Thresh0_Type()
)
pSlot2Thresh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot2Thresh0.setStatus("current")
_PSlot2Thresh1_Type = DescriptionString
_PSlot2Thresh1_Object = MibTableColumn
pSlot2Thresh1 = _PSlot2Thresh1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 29),
    _PSlot2Thresh1_Type()
)
pSlot2Thresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Thresh1.setStatus("current")
_PSlot2Thresh2_Type = DescriptionString
_PSlot2Thresh2_Object = MibTableColumn
pSlot2Thresh2 = _PSlot2Thresh2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 30),
    _PSlot2Thresh2_Type()
)
pSlot2Thresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Thresh2.setStatus("current")
_PSlot2Thresh3_Type = DescriptionString
_PSlot2Thresh3_Object = MibTableColumn
pSlot2Thresh3 = _PSlot2Thresh3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 31),
    _PSlot2Thresh3_Type()
)
pSlot2Thresh3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Thresh3.setStatus("current")
_PSlot2Thresh4_Type = DescriptionString
_PSlot2Thresh4_Object = MibTableColumn
pSlot2Thresh4 = _PSlot2Thresh4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 32),
    _PSlot2Thresh4_Type()
)
pSlot2Thresh4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Thresh4.setStatus("current")
_PSlot2Thresh5_Type = DescriptionString
_PSlot2Thresh5_Object = MibTableColumn
pSlot2Thresh5 = _PSlot2Thresh5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 33),
    _PSlot2Thresh5_Type()
)
pSlot2Thresh5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot2Thresh5.setStatus("current")
_PSlot2ContactStyle_Type = ContactStyle
_PSlot2ContactStyle_Object = MibTableColumn
pSlot2ContactStyle = _PSlot2ContactStyle_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 44),
    _PSlot2ContactStyle_Type()
)
pSlot2ContactStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2ContactStyle.setStatus("current")
_PSlot2Units_Type = DescriptionString
_PSlot2Units_Object = MibTableColumn
pSlot2Units = _PSlot2Units_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 46),
    _PSlot2Units_Type()
)
pSlot2Units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot2Units.setStatus("current")
_PSlot2OutputMode_Type = OutputMode
_PSlot2OutputMode_Object = MibTableColumn
pSlot2OutputMode = _PSlot2OutputMode_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 47),
    _PSlot2OutputMode_Type()
)
pSlot2OutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2OutputMode.setStatus("current")
_PSlot2OutputState_Type = OutputState
_PSlot2OutputState_Object = MibTableColumn
pSlot2OutputState = _PSlot2OutputState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 48),
    _PSlot2OutputState_Type()
)
pSlot2OutputState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2OutputState.setStatus("current")
_PSlot2OutputAuto_Type = Integer32
_PSlot2OutputAuto_Object = MibTableColumn
pSlot2OutputAuto = _PSlot2OutputAuto_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 49),
    _PSlot2OutputAuto_Type()
)
pSlot2OutputAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2OutputAuto.setStatus("current")
_PSlot2BaudRate_Type = BaudRate
_PSlot2BaudRate_Object = MibTableColumn
pSlot2BaudRate = _PSlot2BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 57),
    _PSlot2BaudRate_Type()
)
pSlot2BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2BaudRate.setStatus("current")
_PSlot2DataBits_Type = DataBits
_PSlot2DataBits_Object = MibTableColumn
pSlot2DataBits = _PSlot2DataBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 58),
    _PSlot2DataBits_Type()
)
pSlot2DataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2DataBits.setStatus("current")
_PSlot2Parity_Type = Parity
_PSlot2Parity_Object = MibTableColumn
pSlot2Parity = _PSlot2Parity_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 59),
    _PSlot2Parity_Type()
)
pSlot2Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Parity.setStatus("current")
_PSlot2StopBits_Type = StopBits
_PSlot2StopBits_Object = MibTableColumn
pSlot2StopBits = _PSlot2StopBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 60),
    _PSlot2StopBits_Type()
)
pSlot2StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2StopBits.setStatus("current")
_PSlot2Protocol_Type = Protocol
_PSlot2Protocol_Object = MibTableColumn
pSlot2Protocol = _PSlot2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 61),
    _PSlot2Protocol_Type()
)
pSlot2Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2Protocol.setStatus("current")
_PSlot2SerialRTS_Type = SerialRTS
_PSlot2SerialRTS_Object = MibTableColumn
pSlot2SerialRTS = _PSlot2SerialRTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 62),
    _PSlot2SerialRTS_Type()
)
pSlot2SerialRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2SerialRTS.setStatus("current")
_PSlot2SerialCTS_Type = SerialCTS
_PSlot2SerialCTS_Object = MibTableColumn
pSlot2SerialCTS = _PSlot2SerialCTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 63),
    _PSlot2SerialCTS_Type()
)
pSlot2SerialCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2SerialCTS.setStatus("current")
_PSlot2LiveDescription_Type = DescriptionString
_PSlot2LiveDescription_Object = MibTableColumn
pSlot2LiveDescription = _PSlot2LiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 64),
    _PSlot2LiveDescription_Type()
)
pSlot2LiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot2LiveDescription.setStatus("current")
_PSlot2LiveLevel_Type = DescriptionString
_PSlot2LiveLevel_Object = MibTableColumn
pSlot2LiveLevel = _PSlot2LiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 65),
    _PSlot2LiveLevel_Type()
)
pSlot2LiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot2LiveLevel.setStatus("current")
_PSlot2LiveRaw_Type = DescriptionString
_PSlot2LiveRaw_Object = MibTableColumn
pSlot2LiveRaw = _PSlot2LiveRaw_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 66),
    _PSlot2LiveRaw_Type()
)
pSlot2LiveRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot2LiveRaw.setStatus("current")
_PSlot2LiveTime_Type = DescriptionString
_PSlot2LiveTime_Object = MibTableColumn
pSlot2LiveTime = _PSlot2LiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 67),
    _PSlot2LiveTime_Type()
)
pSlot2LiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot2LiveTime.setStatus("current")
_PSlot2Present_Type = Boolean
_PSlot2Present_Object = MibTableColumn
pSlot2Present = _PSlot2Present_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 68),
    _PSlot2Present_Type()
)
pSlot2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot2Present.setStatus("current")
_PSlot2OutputAutoPkg_Type = Integer32
_PSlot2OutputAutoPkg_Object = MibTableColumn
pSlot2OutputAutoPkg = _PSlot2OutputAutoPkg_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 71),
    _PSlot2OutputAutoPkg_Type()
)
pSlot2OutputAutoPkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2OutputAutoPkg.setStatus("current")
_PSlot2VoltageRange_Type = VoltageRange
_PSlot2VoltageRange_Object = MibTableColumn
pSlot2VoltageRange = _PSlot2VoltageRange_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 72),
    _PSlot2VoltageRange_Type()
)
pSlot2VoltageRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot2VoltageRange.setStatus("current")
_PSlot2IPPortNum_Type = Integer32
_PSlot2IPPortNum_Object = MibTableColumn
pSlot2IPPortNum = _PSlot2IPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 73),
    _PSlot2IPPortNum_Type()
)
pSlot2IPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2IPPortNum.setStatus("current")
_PSlot2IOFormat_Type = IOFormat
_PSlot2IOFormat_Object = MibTableColumn
pSlot2IOFormat = _PSlot2IOFormat_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 75),
    _PSlot2IOFormat_Type()
)
pSlot2IOFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot2IOFormat.setStatus("current")
_PSlot2PortType_Type = PortType
_PSlot2PortType_Object = MibTableColumn
pSlot2PortType = _PSlot2PortType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 76),
    _PSlot2PortType_Type()
)
pSlot2PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot2PortType.setStatus("current")
_PSlot2TL1SID_Type = DescriptionString
_PSlot2TL1SID_Object = MibTableColumn
pSlot2TL1SID = _PSlot2TL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 116),
    _PSlot2TL1SID_Type()
)
pSlot2TL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2TL1SID.setStatus("current")
_PSlot2TL1COND_Type = DescriptionString
_PSlot2TL1COND_Object = MibTableColumn
pSlot2TL1COND = _PSlot2TL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 117),
    _PSlot2TL1COND_Type()
)
pSlot2TL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2TL1COND.setStatus("current")
_PSlot2TL1Eqpt_Type = DescriptionString
_PSlot2TL1Eqpt_Object = MibTableColumn
pSlot2TL1Eqpt = _PSlot2TL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 118),
    _PSlot2TL1Eqpt_Type()
)
pSlot2TL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2TL1Eqpt.setStatus("current")
_PSlot2TL1Env_Type = Boolean
_PSlot2TL1Env_Object = MibTableColumn
pSlot2TL1Env = _PSlot2TL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 119),
    _PSlot2TL1Env_Type()
)
pSlot2TL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2TL1Env.setStatus("current")
_PSlot2TL1Srveff_Type = TL1Srveff
_PSlot2TL1Srveff_Object = MibTableColumn
pSlot2TL1Srveff = _PSlot2TL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 120),
    _PSlot2TL1Srveff_Type()
)
pSlot2TL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2TL1Srveff.setStatus("current")
_PSlot2TL1Locn_Type = TL1Locn
_PSlot2TL1Locn_Object = MibTableColumn
pSlot2TL1Locn = _PSlot2TL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 121),
    _PSlot2TL1Locn_Type()
)
pSlot2TL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2TL1Locn.setStatus("current")
_PSlot2TL1Dirn_Type = TL1Dirn
_PSlot2TL1Dirn_Object = MibTableColumn
pSlot2TL1Dirn = _PSlot2TL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 122),
    _PSlot2TL1Dirn_Type()
)
pSlot2TL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2TL1Dirn.setStatus("current")
_PSlot2SensorType_Type = SensorType
_PSlot2SensorType_Object = MibTableColumn
pSlot2SensorType = _PSlot2SensorType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 131),
    _PSlot2SensorType_Type()
)
pSlot2SensorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot2SensorType.setStatus("current")


class _PSlot2Index_Type(Integer32):
    """Custom type pSlot2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PSlot2Index_Type.__name__ = "Integer32"
_PSlot2Index_Object = MibTableColumn
pSlot2Index = _PSlot2Index_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 19, 1, 999),
    _PSlot2Index_Type()
)
pSlot2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot2Index.setStatus("current")
_PSlot3Table_Object = MibTable
pSlot3Table = _PSlot3Table_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20)
)
if mibBuilder.loadTexts:
    pSlot3Table.setStatus("current")
_PSlot3Entry_Object = MibTableRow
pSlot3Entry = _PSlot3Entry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1)
)
pSlot3Entry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pSlot3Index"),
)
if mibBuilder.loadTexts:
    pSlot3Entry.setStatus("current")
_PSlot3Description_Type = DescriptionString
_PSlot3Description_Object = MibTableColumn
pSlot3Description = _PSlot3Description_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 3),
    _PSlot3Description_Type()
)
pSlot3Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Description.setStatus("current")
_PSlot3Desc0_Type = DescriptionString
_PSlot3Desc0_Object = MibTableColumn
pSlot3Desc0 = _PSlot3Desc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 4),
    _PSlot3Desc0_Type()
)
pSlot3Desc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Desc0.setStatus("current")
_PSlot3Desc1_Type = DescriptionString
_PSlot3Desc1_Object = MibTableColumn
pSlot3Desc1 = _PSlot3Desc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 5),
    _PSlot3Desc1_Type()
)
pSlot3Desc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Desc1.setStatus("current")
_PSlot3Desc2_Type = DescriptionString
_PSlot3Desc2_Object = MibTableColumn
pSlot3Desc2 = _PSlot3Desc2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 6),
    _PSlot3Desc2_Type()
)
pSlot3Desc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Desc2.setStatus("current")
_PSlot3Desc3_Type = DescriptionString
_PSlot3Desc3_Object = MibTableColumn
pSlot3Desc3 = _PSlot3Desc3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 7),
    _PSlot3Desc3_Type()
)
pSlot3Desc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Desc3.setStatus("current")
_PSlot3Desc4_Type = DescriptionString
_PSlot3Desc4_Object = MibTableColumn
pSlot3Desc4 = _PSlot3Desc4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 8),
    _PSlot3Desc4_Type()
)
pSlot3Desc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Desc4.setStatus("current")
_PSlot3Desc5_Type = DescriptionString
_PSlot3Desc5_Object = MibTableColumn
pSlot3Desc5 = _PSlot3Desc5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 9),
    _PSlot3Desc5_Type()
)
pSlot3Desc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Desc5.setStatus("current")
_PSlot3Configured_Type = Configured
_PSlot3Configured_Object = MibTableColumn
pSlot3Configured = _PSlot3Configured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 10),
    _PSlot3Configured_Type()
)
pSlot3Configured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Configured.setStatus("current")
_PSlot3SendEmail_Type = Boolean
_PSlot3SendEmail_Object = MibTableColumn
pSlot3SendEmail = _PSlot3SendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 11),
    _PSlot3SendEmail_Type()
)
pSlot3SendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3SendEmail.setStatus("current")
_PSlot3SendSNMPTrap_Type = Boolean
_PSlot3SendSNMPTrap_Object = MibTableColumn
pSlot3SendSNMPTrap = _PSlot3SendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 12),
    _PSlot3SendSNMPTrap_Type()
)
pSlot3SendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3SendSNMPTrap.setStatus("current")
_PSlot3IpAddress_Type = IpAddress
_PSlot3IpAddress_Object = MibTableColumn
pSlot3IpAddress = _PSlot3IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 14),
    _PSlot3IpAddress_Type()
)
pSlot3IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3IpAddress.setStatus("current")
_PSlot3Level0_Type = Level
_PSlot3Level0_Object = MibTableColumn
pSlot3Level0 = _PSlot3Level0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 17),
    _PSlot3Level0_Type()
)
pSlot3Level0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Level0.setStatus("current")
_PSlot3Level1_Type = Level
_PSlot3Level1_Object = MibTableColumn
pSlot3Level1 = _PSlot3Level1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 18),
    _PSlot3Level1_Type()
)
pSlot3Level1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Level1.setStatus("current")
_PSlot3Level2_Type = Level
_PSlot3Level2_Object = MibTableColumn
pSlot3Level2 = _PSlot3Level2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 19),
    _PSlot3Level2_Type()
)
pSlot3Level2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Level2.setStatus("current")
_PSlot3Level3_Type = Level
_PSlot3Level3_Object = MibTableColumn
pSlot3Level3 = _PSlot3Level3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 20),
    _PSlot3Level3_Type()
)
pSlot3Level3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Level3.setStatus("current")
_PSlot3Level4_Type = Level
_PSlot3Level4_Object = MibTableColumn
pSlot3Level4 = _PSlot3Level4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 21),
    _PSlot3Level4_Type()
)
pSlot3Level4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Level4.setStatus("current")
_PSlot3Level5_Type = Level
_PSlot3Level5_Object = MibTableColumn
pSlot3Level5 = _PSlot3Level5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 22),
    _PSlot3Level5_Type()
)
pSlot3Level5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Level5.setStatus("current")
_PSlot3ReadPeriod_Type = Integer32
_PSlot3ReadPeriod_Object = MibTableColumn
pSlot3ReadPeriod = _PSlot3ReadPeriod_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 23),
    _PSlot3ReadPeriod_Type()
)
pSlot3ReadPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3ReadPeriod.setStatus("current")
_PSlot3Thresh0_Type = DescriptionString
_PSlot3Thresh0_Object = MibTableColumn
pSlot3Thresh0 = _PSlot3Thresh0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 28),
    _PSlot3Thresh0_Type()
)
pSlot3Thresh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot3Thresh0.setStatus("current")
_PSlot3Thresh1_Type = DescriptionString
_PSlot3Thresh1_Object = MibTableColumn
pSlot3Thresh1 = _PSlot3Thresh1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 29),
    _PSlot3Thresh1_Type()
)
pSlot3Thresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Thresh1.setStatus("current")
_PSlot3Thresh2_Type = DescriptionString
_PSlot3Thresh2_Object = MibTableColumn
pSlot3Thresh2 = _PSlot3Thresh2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 30),
    _PSlot3Thresh2_Type()
)
pSlot3Thresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Thresh2.setStatus("current")
_PSlot3Thresh3_Type = DescriptionString
_PSlot3Thresh3_Object = MibTableColumn
pSlot3Thresh3 = _PSlot3Thresh3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 31),
    _PSlot3Thresh3_Type()
)
pSlot3Thresh3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Thresh3.setStatus("current")
_PSlot3Thresh4_Type = DescriptionString
_PSlot3Thresh4_Object = MibTableColumn
pSlot3Thresh4 = _PSlot3Thresh4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 32),
    _PSlot3Thresh4_Type()
)
pSlot3Thresh4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Thresh4.setStatus("current")
_PSlot3Thresh5_Type = DescriptionString
_PSlot3Thresh5_Object = MibTableColumn
pSlot3Thresh5 = _PSlot3Thresh5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 33),
    _PSlot3Thresh5_Type()
)
pSlot3Thresh5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot3Thresh5.setStatus("current")
_PSlot3ContactStyle_Type = ContactStyle
_PSlot3ContactStyle_Object = MibTableColumn
pSlot3ContactStyle = _PSlot3ContactStyle_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 44),
    _PSlot3ContactStyle_Type()
)
pSlot3ContactStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3ContactStyle.setStatus("current")
_PSlot3Units_Type = DescriptionString
_PSlot3Units_Object = MibTableColumn
pSlot3Units = _PSlot3Units_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 46),
    _PSlot3Units_Type()
)
pSlot3Units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot3Units.setStatus("current")
_PSlot3OutputMode_Type = OutputMode
_PSlot3OutputMode_Object = MibTableColumn
pSlot3OutputMode = _PSlot3OutputMode_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 47),
    _PSlot3OutputMode_Type()
)
pSlot3OutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3OutputMode.setStatus("current")
_PSlot3OutputState_Type = OutputState
_PSlot3OutputState_Object = MibTableColumn
pSlot3OutputState = _PSlot3OutputState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 48),
    _PSlot3OutputState_Type()
)
pSlot3OutputState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3OutputState.setStatus("current")
_PSlot3OutputAuto_Type = Integer32
_PSlot3OutputAuto_Object = MibTableColumn
pSlot3OutputAuto = _PSlot3OutputAuto_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 49),
    _PSlot3OutputAuto_Type()
)
pSlot3OutputAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3OutputAuto.setStatus("current")
_PSlot3BaudRate_Type = BaudRate
_PSlot3BaudRate_Object = MibTableColumn
pSlot3BaudRate = _PSlot3BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 57),
    _PSlot3BaudRate_Type()
)
pSlot3BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3BaudRate.setStatus("current")
_PSlot3DataBits_Type = DataBits
_PSlot3DataBits_Object = MibTableColumn
pSlot3DataBits = _PSlot3DataBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 58),
    _PSlot3DataBits_Type()
)
pSlot3DataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3DataBits.setStatus("current")
_PSlot3Parity_Type = Parity
_PSlot3Parity_Object = MibTableColumn
pSlot3Parity = _PSlot3Parity_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 59),
    _PSlot3Parity_Type()
)
pSlot3Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Parity.setStatus("current")
_PSlot3StopBits_Type = StopBits
_PSlot3StopBits_Object = MibTableColumn
pSlot3StopBits = _PSlot3StopBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 60),
    _PSlot3StopBits_Type()
)
pSlot3StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3StopBits.setStatus("current")
_PSlot3Protocol_Type = Protocol
_PSlot3Protocol_Object = MibTableColumn
pSlot3Protocol = _PSlot3Protocol_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 61),
    _PSlot3Protocol_Type()
)
pSlot3Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3Protocol.setStatus("current")
_PSlot3SerialRTS_Type = SerialRTS
_PSlot3SerialRTS_Object = MibTableColumn
pSlot3SerialRTS = _PSlot3SerialRTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 62),
    _PSlot3SerialRTS_Type()
)
pSlot3SerialRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3SerialRTS.setStatus("current")
_PSlot3SerialCTS_Type = SerialCTS
_PSlot3SerialCTS_Object = MibTableColumn
pSlot3SerialCTS = _PSlot3SerialCTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 63),
    _PSlot3SerialCTS_Type()
)
pSlot3SerialCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3SerialCTS.setStatus("current")
_PSlot3LiveDescription_Type = DescriptionString
_PSlot3LiveDescription_Object = MibTableColumn
pSlot3LiveDescription = _PSlot3LiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 64),
    _PSlot3LiveDescription_Type()
)
pSlot3LiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot3LiveDescription.setStatus("current")
_PSlot3LiveLevel_Type = DescriptionString
_PSlot3LiveLevel_Object = MibTableColumn
pSlot3LiveLevel = _PSlot3LiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 65),
    _PSlot3LiveLevel_Type()
)
pSlot3LiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot3LiveLevel.setStatus("current")
_PSlot3LiveRaw_Type = DescriptionString
_PSlot3LiveRaw_Object = MibTableColumn
pSlot3LiveRaw = _PSlot3LiveRaw_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 66),
    _PSlot3LiveRaw_Type()
)
pSlot3LiveRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot3LiveRaw.setStatus("current")
_PSlot3LiveTime_Type = DescriptionString
_PSlot3LiveTime_Object = MibTableColumn
pSlot3LiveTime = _PSlot3LiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 67),
    _PSlot3LiveTime_Type()
)
pSlot3LiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot3LiveTime.setStatus("current")
_PSlot3Present_Type = Boolean
_PSlot3Present_Object = MibTableColumn
pSlot3Present = _PSlot3Present_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 68),
    _PSlot3Present_Type()
)
pSlot3Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot3Present.setStatus("current")
_PSlot3OutputAutoPkg_Type = Integer32
_PSlot3OutputAutoPkg_Object = MibTableColumn
pSlot3OutputAutoPkg = _PSlot3OutputAutoPkg_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 71),
    _PSlot3OutputAutoPkg_Type()
)
pSlot3OutputAutoPkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3OutputAutoPkg.setStatus("current")
_PSlot3VoltageRange_Type = VoltageRange
_PSlot3VoltageRange_Object = MibTableColumn
pSlot3VoltageRange = _PSlot3VoltageRange_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 72),
    _PSlot3VoltageRange_Type()
)
pSlot3VoltageRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot3VoltageRange.setStatus("current")
_PSlot3IPPortNum_Type = Integer32
_PSlot3IPPortNum_Object = MibTableColumn
pSlot3IPPortNum = _PSlot3IPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 73),
    _PSlot3IPPortNum_Type()
)
pSlot3IPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3IPPortNum.setStatus("current")
_PSlot3IOFormat_Type = IOFormat
_PSlot3IOFormat_Object = MibTableColumn
pSlot3IOFormat = _PSlot3IOFormat_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 75),
    _PSlot3IOFormat_Type()
)
pSlot3IOFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot3IOFormat.setStatus("current")
_PSlot3PortType_Type = PortType
_PSlot3PortType_Object = MibTableColumn
pSlot3PortType = _PSlot3PortType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 76),
    _PSlot3PortType_Type()
)
pSlot3PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot3PortType.setStatus("current")
_PSlot3TL1SID_Type = DescriptionString
_PSlot3TL1SID_Object = MibTableColumn
pSlot3TL1SID = _PSlot3TL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 116),
    _PSlot3TL1SID_Type()
)
pSlot3TL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3TL1SID.setStatus("current")
_PSlot3TL1COND_Type = DescriptionString
_PSlot3TL1COND_Object = MibTableColumn
pSlot3TL1COND = _PSlot3TL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 117),
    _PSlot3TL1COND_Type()
)
pSlot3TL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3TL1COND.setStatus("current")
_PSlot3TL1Eqpt_Type = DescriptionString
_PSlot3TL1Eqpt_Object = MibTableColumn
pSlot3TL1Eqpt = _PSlot3TL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 118),
    _PSlot3TL1Eqpt_Type()
)
pSlot3TL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3TL1Eqpt.setStatus("current")
_PSlot3TL1Env_Type = Boolean
_PSlot3TL1Env_Object = MibTableColumn
pSlot3TL1Env = _PSlot3TL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 119),
    _PSlot3TL1Env_Type()
)
pSlot3TL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3TL1Env.setStatus("current")
_PSlot3TL1Srveff_Type = TL1Srveff
_PSlot3TL1Srveff_Object = MibTableColumn
pSlot3TL1Srveff = _PSlot3TL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 120),
    _PSlot3TL1Srveff_Type()
)
pSlot3TL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3TL1Srveff.setStatus("current")
_PSlot3TL1Locn_Type = TL1Locn
_PSlot3TL1Locn_Object = MibTableColumn
pSlot3TL1Locn = _PSlot3TL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 121),
    _PSlot3TL1Locn_Type()
)
pSlot3TL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3TL1Locn.setStatus("current")
_PSlot3TL1Dirn_Type = TL1Dirn
_PSlot3TL1Dirn_Object = MibTableColumn
pSlot3TL1Dirn = _PSlot3TL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 122),
    _PSlot3TL1Dirn_Type()
)
pSlot3TL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3TL1Dirn.setStatus("current")
_PSlot3SensorType_Type = SensorType
_PSlot3SensorType_Object = MibTableColumn
pSlot3SensorType = _PSlot3SensorType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 131),
    _PSlot3SensorType_Type()
)
pSlot3SensorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot3SensorType.setStatus("current")


class _PSlot3Index_Type(Integer32):
    """Custom type pSlot3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PSlot3Index_Type.__name__ = "Integer32"
_PSlot3Index_Object = MibTableColumn
pSlot3Index = _PSlot3Index_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 20, 1, 999),
    _PSlot3Index_Type()
)
pSlot3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot3Index.setStatus("current")
_PSlot4Table_Object = MibTable
pSlot4Table = _PSlot4Table_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21)
)
if mibBuilder.loadTexts:
    pSlot4Table.setStatus("current")
_PSlot4Entry_Object = MibTableRow
pSlot4Entry = _PSlot4Entry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1)
)
pSlot4Entry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pSlot4Index"),
)
if mibBuilder.loadTexts:
    pSlot4Entry.setStatus("current")
_PSlot4Description_Type = DescriptionString
_PSlot4Description_Object = MibTableColumn
pSlot4Description = _PSlot4Description_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 3),
    _PSlot4Description_Type()
)
pSlot4Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Description.setStatus("current")
_PSlot4Desc0_Type = DescriptionString
_PSlot4Desc0_Object = MibTableColumn
pSlot4Desc0 = _PSlot4Desc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 4),
    _PSlot4Desc0_Type()
)
pSlot4Desc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Desc0.setStatus("current")
_PSlot4Desc1_Type = DescriptionString
_PSlot4Desc1_Object = MibTableColumn
pSlot4Desc1 = _PSlot4Desc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 5),
    _PSlot4Desc1_Type()
)
pSlot4Desc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Desc1.setStatus("current")
_PSlot4Desc2_Type = DescriptionString
_PSlot4Desc2_Object = MibTableColumn
pSlot4Desc2 = _PSlot4Desc2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 6),
    _PSlot4Desc2_Type()
)
pSlot4Desc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Desc2.setStatus("current")
_PSlot4Desc3_Type = DescriptionString
_PSlot4Desc3_Object = MibTableColumn
pSlot4Desc3 = _PSlot4Desc3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 7),
    _PSlot4Desc3_Type()
)
pSlot4Desc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Desc3.setStatus("current")
_PSlot4Desc4_Type = DescriptionString
_PSlot4Desc4_Object = MibTableColumn
pSlot4Desc4 = _PSlot4Desc4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 8),
    _PSlot4Desc4_Type()
)
pSlot4Desc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Desc4.setStatus("current")
_PSlot4Desc5_Type = DescriptionString
_PSlot4Desc5_Object = MibTableColumn
pSlot4Desc5 = _PSlot4Desc5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 9),
    _PSlot4Desc5_Type()
)
pSlot4Desc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Desc5.setStatus("current")
_PSlot4Configured_Type = Configured
_PSlot4Configured_Object = MibTableColumn
pSlot4Configured = _PSlot4Configured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 10),
    _PSlot4Configured_Type()
)
pSlot4Configured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Configured.setStatus("current")
_PSlot4SendEmail_Type = Boolean
_PSlot4SendEmail_Object = MibTableColumn
pSlot4SendEmail = _PSlot4SendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 11),
    _PSlot4SendEmail_Type()
)
pSlot4SendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4SendEmail.setStatus("current")
_PSlot4SendSNMPTrap_Type = Boolean
_PSlot4SendSNMPTrap_Object = MibTableColumn
pSlot4SendSNMPTrap = _PSlot4SendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 12),
    _PSlot4SendSNMPTrap_Type()
)
pSlot4SendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4SendSNMPTrap.setStatus("current")
_PSlot4IpAddress_Type = IpAddress
_PSlot4IpAddress_Object = MibTableColumn
pSlot4IpAddress = _PSlot4IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 14),
    _PSlot4IpAddress_Type()
)
pSlot4IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4IpAddress.setStatus("current")
_PSlot4Level0_Type = Level
_PSlot4Level0_Object = MibTableColumn
pSlot4Level0 = _PSlot4Level0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 17),
    _PSlot4Level0_Type()
)
pSlot4Level0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Level0.setStatus("current")
_PSlot4Level1_Type = Level
_PSlot4Level1_Object = MibTableColumn
pSlot4Level1 = _PSlot4Level1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 18),
    _PSlot4Level1_Type()
)
pSlot4Level1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Level1.setStatus("current")
_PSlot4Level2_Type = Level
_PSlot4Level2_Object = MibTableColumn
pSlot4Level2 = _PSlot4Level2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 19),
    _PSlot4Level2_Type()
)
pSlot4Level2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Level2.setStatus("current")
_PSlot4Level3_Type = Level
_PSlot4Level3_Object = MibTableColumn
pSlot4Level3 = _PSlot4Level3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 20),
    _PSlot4Level3_Type()
)
pSlot4Level3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Level3.setStatus("current")
_PSlot4Level4_Type = Level
_PSlot4Level4_Object = MibTableColumn
pSlot4Level4 = _PSlot4Level4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 21),
    _PSlot4Level4_Type()
)
pSlot4Level4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Level4.setStatus("current")
_PSlot4Level5_Type = Level
_PSlot4Level5_Object = MibTableColumn
pSlot4Level5 = _PSlot4Level5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 22),
    _PSlot4Level5_Type()
)
pSlot4Level5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Level5.setStatus("current")
_PSlot4ReadPeriod_Type = Integer32
_PSlot4ReadPeriod_Object = MibTableColumn
pSlot4ReadPeriod = _PSlot4ReadPeriod_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 23),
    _PSlot4ReadPeriod_Type()
)
pSlot4ReadPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4ReadPeriod.setStatus("current")
_PSlot4Thresh0_Type = DescriptionString
_PSlot4Thresh0_Object = MibTableColumn
pSlot4Thresh0 = _PSlot4Thresh0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 28),
    _PSlot4Thresh0_Type()
)
pSlot4Thresh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot4Thresh0.setStatus("current")
_PSlot4Thresh1_Type = DescriptionString
_PSlot4Thresh1_Object = MibTableColumn
pSlot4Thresh1 = _PSlot4Thresh1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 29),
    _PSlot4Thresh1_Type()
)
pSlot4Thresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Thresh1.setStatus("current")
_PSlot4Thresh2_Type = DescriptionString
_PSlot4Thresh2_Object = MibTableColumn
pSlot4Thresh2 = _PSlot4Thresh2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 30),
    _PSlot4Thresh2_Type()
)
pSlot4Thresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Thresh2.setStatus("current")
_PSlot4Thresh3_Type = DescriptionString
_PSlot4Thresh3_Object = MibTableColumn
pSlot4Thresh3 = _PSlot4Thresh3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 31),
    _PSlot4Thresh3_Type()
)
pSlot4Thresh3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Thresh3.setStatus("current")
_PSlot4Thresh4_Type = DescriptionString
_PSlot4Thresh4_Object = MibTableColumn
pSlot4Thresh4 = _PSlot4Thresh4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 32),
    _PSlot4Thresh4_Type()
)
pSlot4Thresh4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Thresh4.setStatus("current")
_PSlot4Thresh5_Type = DescriptionString
_PSlot4Thresh5_Object = MibTableColumn
pSlot4Thresh5 = _PSlot4Thresh5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 33),
    _PSlot4Thresh5_Type()
)
pSlot4Thresh5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot4Thresh5.setStatus("current")
_PSlot4ContactStyle_Type = ContactStyle
_PSlot4ContactStyle_Object = MibTableColumn
pSlot4ContactStyle = _PSlot4ContactStyle_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 44),
    _PSlot4ContactStyle_Type()
)
pSlot4ContactStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4ContactStyle.setStatus("current")
_PSlot4Units_Type = DescriptionString
_PSlot4Units_Object = MibTableColumn
pSlot4Units = _PSlot4Units_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 46),
    _PSlot4Units_Type()
)
pSlot4Units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot4Units.setStatus("current")
_PSlot4OutputMode_Type = OutputMode
_PSlot4OutputMode_Object = MibTableColumn
pSlot4OutputMode = _PSlot4OutputMode_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 47),
    _PSlot4OutputMode_Type()
)
pSlot4OutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4OutputMode.setStatus("current")
_PSlot4OutputState_Type = OutputState
_PSlot4OutputState_Object = MibTableColumn
pSlot4OutputState = _PSlot4OutputState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 48),
    _PSlot4OutputState_Type()
)
pSlot4OutputState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4OutputState.setStatus("current")
_PSlot4OutputAuto_Type = Integer32
_PSlot4OutputAuto_Object = MibTableColumn
pSlot4OutputAuto = _PSlot4OutputAuto_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 49),
    _PSlot4OutputAuto_Type()
)
pSlot4OutputAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4OutputAuto.setStatus("current")
_PSlot4BaudRate_Type = BaudRate
_PSlot4BaudRate_Object = MibTableColumn
pSlot4BaudRate = _PSlot4BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 57),
    _PSlot4BaudRate_Type()
)
pSlot4BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4BaudRate.setStatus("current")
_PSlot4DataBits_Type = DataBits
_PSlot4DataBits_Object = MibTableColumn
pSlot4DataBits = _PSlot4DataBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 58),
    _PSlot4DataBits_Type()
)
pSlot4DataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4DataBits.setStatus("current")
_PSlot4Parity_Type = Parity
_PSlot4Parity_Object = MibTableColumn
pSlot4Parity = _PSlot4Parity_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 59),
    _PSlot4Parity_Type()
)
pSlot4Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Parity.setStatus("current")
_PSlot4StopBits_Type = StopBits
_PSlot4StopBits_Object = MibTableColumn
pSlot4StopBits = _PSlot4StopBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 60),
    _PSlot4StopBits_Type()
)
pSlot4StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4StopBits.setStatus("current")
_PSlot4Protocol_Type = Protocol
_PSlot4Protocol_Object = MibTableColumn
pSlot4Protocol = _PSlot4Protocol_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 61),
    _PSlot4Protocol_Type()
)
pSlot4Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4Protocol.setStatus("current")
_PSlot4SerialRTS_Type = SerialRTS
_PSlot4SerialRTS_Object = MibTableColumn
pSlot4SerialRTS = _PSlot4SerialRTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 62),
    _PSlot4SerialRTS_Type()
)
pSlot4SerialRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4SerialRTS.setStatus("current")
_PSlot4SerialCTS_Type = SerialCTS
_PSlot4SerialCTS_Object = MibTableColumn
pSlot4SerialCTS = _PSlot4SerialCTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 63),
    _PSlot4SerialCTS_Type()
)
pSlot4SerialCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4SerialCTS.setStatus("current")
_PSlot4LiveDescription_Type = DescriptionString
_PSlot4LiveDescription_Object = MibTableColumn
pSlot4LiveDescription = _PSlot4LiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 64),
    _PSlot4LiveDescription_Type()
)
pSlot4LiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot4LiveDescription.setStatus("current")
_PSlot4LiveLevel_Type = DescriptionString
_PSlot4LiveLevel_Object = MibTableColumn
pSlot4LiveLevel = _PSlot4LiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 65),
    _PSlot4LiveLevel_Type()
)
pSlot4LiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot4LiveLevel.setStatus("current")
_PSlot4LiveRaw_Type = DescriptionString
_PSlot4LiveRaw_Object = MibTableColumn
pSlot4LiveRaw = _PSlot4LiveRaw_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 66),
    _PSlot4LiveRaw_Type()
)
pSlot4LiveRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot4LiveRaw.setStatus("current")
_PSlot4LiveTime_Type = DescriptionString
_PSlot4LiveTime_Object = MibTableColumn
pSlot4LiveTime = _PSlot4LiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 67),
    _PSlot4LiveTime_Type()
)
pSlot4LiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot4LiveTime.setStatus("current")
_PSlot4Present_Type = Boolean
_PSlot4Present_Object = MibTableColumn
pSlot4Present = _PSlot4Present_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 68),
    _PSlot4Present_Type()
)
pSlot4Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot4Present.setStatus("current")
_PSlot4OutputAutoPkg_Type = Integer32
_PSlot4OutputAutoPkg_Object = MibTableColumn
pSlot4OutputAutoPkg = _PSlot4OutputAutoPkg_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 71),
    _PSlot4OutputAutoPkg_Type()
)
pSlot4OutputAutoPkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4OutputAutoPkg.setStatus("current")
_PSlot4VoltageRange_Type = VoltageRange
_PSlot4VoltageRange_Object = MibTableColumn
pSlot4VoltageRange = _PSlot4VoltageRange_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 72),
    _PSlot4VoltageRange_Type()
)
pSlot4VoltageRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot4VoltageRange.setStatus("current")
_PSlot4IPPortNum_Type = Integer32
_PSlot4IPPortNum_Object = MibTableColumn
pSlot4IPPortNum = _PSlot4IPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 73),
    _PSlot4IPPortNum_Type()
)
pSlot4IPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4IPPortNum.setStatus("current")
_PSlot4IOFormat_Type = IOFormat
_PSlot4IOFormat_Object = MibTableColumn
pSlot4IOFormat = _PSlot4IOFormat_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 75),
    _PSlot4IOFormat_Type()
)
pSlot4IOFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot4IOFormat.setStatus("current")
_PSlot4PortType_Type = PortType
_PSlot4PortType_Object = MibTableColumn
pSlot4PortType = _PSlot4PortType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 76),
    _PSlot4PortType_Type()
)
pSlot4PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot4PortType.setStatus("current")
_PSlot4TL1SID_Type = DescriptionString
_PSlot4TL1SID_Object = MibTableColumn
pSlot4TL1SID = _PSlot4TL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 116),
    _PSlot4TL1SID_Type()
)
pSlot4TL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4TL1SID.setStatus("current")
_PSlot4TL1COND_Type = DescriptionString
_PSlot4TL1COND_Object = MibTableColumn
pSlot4TL1COND = _PSlot4TL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 117),
    _PSlot4TL1COND_Type()
)
pSlot4TL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4TL1COND.setStatus("current")
_PSlot4TL1Eqpt_Type = DescriptionString
_PSlot4TL1Eqpt_Object = MibTableColumn
pSlot4TL1Eqpt = _PSlot4TL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 118),
    _PSlot4TL1Eqpt_Type()
)
pSlot4TL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4TL1Eqpt.setStatus("current")
_PSlot4TL1Env_Type = Boolean
_PSlot4TL1Env_Object = MibTableColumn
pSlot4TL1Env = _PSlot4TL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 119),
    _PSlot4TL1Env_Type()
)
pSlot4TL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4TL1Env.setStatus("current")
_PSlot4TL1Srveff_Type = TL1Srveff
_PSlot4TL1Srveff_Object = MibTableColumn
pSlot4TL1Srveff = _PSlot4TL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 120),
    _PSlot4TL1Srveff_Type()
)
pSlot4TL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4TL1Srveff.setStatus("current")
_PSlot4TL1Locn_Type = TL1Locn
_PSlot4TL1Locn_Object = MibTableColumn
pSlot4TL1Locn = _PSlot4TL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 121),
    _PSlot4TL1Locn_Type()
)
pSlot4TL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4TL1Locn.setStatus("current")
_PSlot4TL1Dirn_Type = TL1Dirn
_PSlot4TL1Dirn_Object = MibTableColumn
pSlot4TL1Dirn = _PSlot4TL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 122),
    _PSlot4TL1Dirn_Type()
)
pSlot4TL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4TL1Dirn.setStatus("current")
_PSlot4SensorType_Type = SensorType
_PSlot4SensorType_Object = MibTableColumn
pSlot4SensorType = _PSlot4SensorType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 131),
    _PSlot4SensorType_Type()
)
pSlot4SensorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot4SensorType.setStatus("current")


class _PSlot4Index_Type(Integer32):
    """Custom type pSlot4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PSlot4Index_Type.__name__ = "Integer32"
_PSlot4Index_Object = MibTableColumn
pSlot4Index = _PSlot4Index_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 21, 1, 999),
    _PSlot4Index_Type()
)
pSlot4Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot4Index.setStatus("current")
_PSlot5Table_Object = MibTable
pSlot5Table = _PSlot5Table_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22)
)
if mibBuilder.loadTexts:
    pSlot5Table.setStatus("current")
_PSlot5Entry_Object = MibTableRow
pSlot5Entry = _PSlot5Entry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1)
)
pSlot5Entry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pSlot5Index"),
)
if mibBuilder.loadTexts:
    pSlot5Entry.setStatus("current")
_PSlot5Description_Type = DescriptionString
_PSlot5Description_Object = MibTableColumn
pSlot5Description = _PSlot5Description_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 3),
    _PSlot5Description_Type()
)
pSlot5Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Description.setStatus("current")
_PSlot5Desc0_Type = DescriptionString
_PSlot5Desc0_Object = MibTableColumn
pSlot5Desc0 = _PSlot5Desc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 4),
    _PSlot5Desc0_Type()
)
pSlot5Desc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Desc0.setStatus("current")
_PSlot5Desc1_Type = DescriptionString
_PSlot5Desc1_Object = MibTableColumn
pSlot5Desc1 = _PSlot5Desc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 5),
    _PSlot5Desc1_Type()
)
pSlot5Desc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Desc1.setStatus("current")
_PSlot5Desc2_Type = DescriptionString
_PSlot5Desc2_Object = MibTableColumn
pSlot5Desc2 = _PSlot5Desc2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 6),
    _PSlot5Desc2_Type()
)
pSlot5Desc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Desc2.setStatus("current")
_PSlot5Desc3_Type = DescriptionString
_PSlot5Desc3_Object = MibTableColumn
pSlot5Desc3 = _PSlot5Desc3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 7),
    _PSlot5Desc3_Type()
)
pSlot5Desc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Desc3.setStatus("current")
_PSlot5Desc4_Type = DescriptionString
_PSlot5Desc4_Object = MibTableColumn
pSlot5Desc4 = _PSlot5Desc4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 8),
    _PSlot5Desc4_Type()
)
pSlot5Desc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Desc4.setStatus("current")
_PSlot5Desc5_Type = DescriptionString
_PSlot5Desc5_Object = MibTableColumn
pSlot5Desc5 = _PSlot5Desc5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 9),
    _PSlot5Desc5_Type()
)
pSlot5Desc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Desc5.setStatus("current")
_PSlot5Configured_Type = Configured
_PSlot5Configured_Object = MibTableColumn
pSlot5Configured = _PSlot5Configured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 10),
    _PSlot5Configured_Type()
)
pSlot5Configured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Configured.setStatus("current")
_PSlot5SendEmail_Type = Boolean
_PSlot5SendEmail_Object = MibTableColumn
pSlot5SendEmail = _PSlot5SendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 11),
    _PSlot5SendEmail_Type()
)
pSlot5SendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5SendEmail.setStatus("current")
_PSlot5SendSNMPTrap_Type = Boolean
_PSlot5SendSNMPTrap_Object = MibTableColumn
pSlot5SendSNMPTrap = _PSlot5SendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 12),
    _PSlot5SendSNMPTrap_Type()
)
pSlot5SendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5SendSNMPTrap.setStatus("current")
_PSlot5IpAddress_Type = IpAddress
_PSlot5IpAddress_Object = MibTableColumn
pSlot5IpAddress = _PSlot5IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 14),
    _PSlot5IpAddress_Type()
)
pSlot5IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5IpAddress.setStatus("current")
_PSlot5Level0_Type = Level
_PSlot5Level0_Object = MibTableColumn
pSlot5Level0 = _PSlot5Level0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 17),
    _PSlot5Level0_Type()
)
pSlot5Level0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Level0.setStatus("current")
_PSlot5Level1_Type = Level
_PSlot5Level1_Object = MibTableColumn
pSlot5Level1 = _PSlot5Level1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 18),
    _PSlot5Level1_Type()
)
pSlot5Level1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Level1.setStatus("current")
_PSlot5Level2_Type = Level
_PSlot5Level2_Object = MibTableColumn
pSlot5Level2 = _PSlot5Level2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 19),
    _PSlot5Level2_Type()
)
pSlot5Level2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Level2.setStatus("current")
_PSlot5Level3_Type = Level
_PSlot5Level3_Object = MibTableColumn
pSlot5Level3 = _PSlot5Level3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 20),
    _PSlot5Level3_Type()
)
pSlot5Level3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Level3.setStatus("current")
_PSlot5Level4_Type = Level
_PSlot5Level4_Object = MibTableColumn
pSlot5Level4 = _PSlot5Level4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 21),
    _PSlot5Level4_Type()
)
pSlot5Level4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Level4.setStatus("current")
_PSlot5Level5_Type = Level
_PSlot5Level5_Object = MibTableColumn
pSlot5Level5 = _PSlot5Level5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 22),
    _PSlot5Level5_Type()
)
pSlot5Level5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Level5.setStatus("current")
_PSlot5ReadPeriod_Type = Integer32
_PSlot5ReadPeriod_Object = MibTableColumn
pSlot5ReadPeriod = _PSlot5ReadPeriod_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 23),
    _PSlot5ReadPeriod_Type()
)
pSlot5ReadPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5ReadPeriod.setStatus("current")
_PSlot5Thresh0_Type = DescriptionString
_PSlot5Thresh0_Object = MibTableColumn
pSlot5Thresh0 = _PSlot5Thresh0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 28),
    _PSlot5Thresh0_Type()
)
pSlot5Thresh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot5Thresh0.setStatus("current")
_PSlot5Thresh1_Type = DescriptionString
_PSlot5Thresh1_Object = MibTableColumn
pSlot5Thresh1 = _PSlot5Thresh1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 29),
    _PSlot5Thresh1_Type()
)
pSlot5Thresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Thresh1.setStatus("current")
_PSlot5Thresh2_Type = DescriptionString
_PSlot5Thresh2_Object = MibTableColumn
pSlot5Thresh2 = _PSlot5Thresh2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 30),
    _PSlot5Thresh2_Type()
)
pSlot5Thresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Thresh2.setStatus("current")
_PSlot5Thresh3_Type = DescriptionString
_PSlot5Thresh3_Object = MibTableColumn
pSlot5Thresh3 = _PSlot5Thresh3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 31),
    _PSlot5Thresh3_Type()
)
pSlot5Thresh3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Thresh3.setStatus("current")
_PSlot5Thresh4_Type = DescriptionString
_PSlot5Thresh4_Object = MibTableColumn
pSlot5Thresh4 = _PSlot5Thresh4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 32),
    _PSlot5Thresh4_Type()
)
pSlot5Thresh4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Thresh4.setStatus("current")
_PSlot5Thresh5_Type = DescriptionString
_PSlot5Thresh5_Object = MibTableColumn
pSlot5Thresh5 = _PSlot5Thresh5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 33),
    _PSlot5Thresh5_Type()
)
pSlot5Thresh5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot5Thresh5.setStatus("current")
_PSlot5ContactStyle_Type = ContactStyle
_PSlot5ContactStyle_Object = MibTableColumn
pSlot5ContactStyle = _PSlot5ContactStyle_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 44),
    _PSlot5ContactStyle_Type()
)
pSlot5ContactStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5ContactStyle.setStatus("current")
_PSlot5Units_Type = DescriptionString
_PSlot5Units_Object = MibTableColumn
pSlot5Units = _PSlot5Units_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 46),
    _PSlot5Units_Type()
)
pSlot5Units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot5Units.setStatus("current")
_PSlot5OutputMode_Type = OutputMode
_PSlot5OutputMode_Object = MibTableColumn
pSlot5OutputMode = _PSlot5OutputMode_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 47),
    _PSlot5OutputMode_Type()
)
pSlot5OutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5OutputMode.setStatus("current")
_PSlot5OutputState_Type = OutputState
_PSlot5OutputState_Object = MibTableColumn
pSlot5OutputState = _PSlot5OutputState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 48),
    _PSlot5OutputState_Type()
)
pSlot5OutputState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5OutputState.setStatus("current")
_PSlot5OutputAuto_Type = Integer32
_PSlot5OutputAuto_Object = MibTableColumn
pSlot5OutputAuto = _PSlot5OutputAuto_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 49),
    _PSlot5OutputAuto_Type()
)
pSlot5OutputAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5OutputAuto.setStatus("current")
_PSlot5BaudRate_Type = BaudRate
_PSlot5BaudRate_Object = MibTableColumn
pSlot5BaudRate = _PSlot5BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 57),
    _PSlot5BaudRate_Type()
)
pSlot5BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5BaudRate.setStatus("current")
_PSlot5DataBits_Type = DataBits
_PSlot5DataBits_Object = MibTableColumn
pSlot5DataBits = _PSlot5DataBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 58),
    _PSlot5DataBits_Type()
)
pSlot5DataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5DataBits.setStatus("current")
_PSlot5Parity_Type = Parity
_PSlot5Parity_Object = MibTableColumn
pSlot5Parity = _PSlot5Parity_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 59),
    _PSlot5Parity_Type()
)
pSlot5Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Parity.setStatus("current")
_PSlot5StopBits_Type = StopBits
_PSlot5StopBits_Object = MibTableColumn
pSlot5StopBits = _PSlot5StopBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 60),
    _PSlot5StopBits_Type()
)
pSlot5StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5StopBits.setStatus("current")
_PSlot5Protocol_Type = Protocol
_PSlot5Protocol_Object = MibTableColumn
pSlot5Protocol = _PSlot5Protocol_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 61),
    _PSlot5Protocol_Type()
)
pSlot5Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5Protocol.setStatus("current")
_PSlot5SerialRTS_Type = SerialRTS
_PSlot5SerialRTS_Object = MibTableColumn
pSlot5SerialRTS = _PSlot5SerialRTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 62),
    _PSlot5SerialRTS_Type()
)
pSlot5SerialRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5SerialRTS.setStatus("current")
_PSlot5SerialCTS_Type = SerialCTS
_PSlot5SerialCTS_Object = MibTableColumn
pSlot5SerialCTS = _PSlot5SerialCTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 63),
    _PSlot5SerialCTS_Type()
)
pSlot5SerialCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5SerialCTS.setStatus("current")
_PSlot5LiveDescription_Type = DescriptionString
_PSlot5LiveDescription_Object = MibTableColumn
pSlot5LiveDescription = _PSlot5LiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 64),
    _PSlot5LiveDescription_Type()
)
pSlot5LiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot5LiveDescription.setStatus("current")
_PSlot5LiveLevel_Type = DescriptionString
_PSlot5LiveLevel_Object = MibTableColumn
pSlot5LiveLevel = _PSlot5LiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 65),
    _PSlot5LiveLevel_Type()
)
pSlot5LiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot5LiveLevel.setStatus("current")
_PSlot5LiveRaw_Type = DescriptionString
_PSlot5LiveRaw_Object = MibTableColumn
pSlot5LiveRaw = _PSlot5LiveRaw_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 66),
    _PSlot5LiveRaw_Type()
)
pSlot5LiveRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot5LiveRaw.setStatus("current")
_PSlot5LiveTime_Type = DescriptionString
_PSlot5LiveTime_Object = MibTableColumn
pSlot5LiveTime = _PSlot5LiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 67),
    _PSlot5LiveTime_Type()
)
pSlot5LiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot5LiveTime.setStatus("current")
_PSlot5Present_Type = Boolean
_PSlot5Present_Object = MibTableColumn
pSlot5Present = _PSlot5Present_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 68),
    _PSlot5Present_Type()
)
pSlot5Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot5Present.setStatus("current")
_PSlot5OutputAutoPkg_Type = Integer32
_PSlot5OutputAutoPkg_Object = MibTableColumn
pSlot5OutputAutoPkg = _PSlot5OutputAutoPkg_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 71),
    _PSlot5OutputAutoPkg_Type()
)
pSlot5OutputAutoPkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5OutputAutoPkg.setStatus("current")
_PSlot5VoltageRange_Type = VoltageRange
_PSlot5VoltageRange_Object = MibTableColumn
pSlot5VoltageRange = _PSlot5VoltageRange_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 72),
    _PSlot5VoltageRange_Type()
)
pSlot5VoltageRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot5VoltageRange.setStatus("current")
_PSlot5IPPortNum_Type = Integer32
_PSlot5IPPortNum_Object = MibTableColumn
pSlot5IPPortNum = _PSlot5IPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 73),
    _PSlot5IPPortNum_Type()
)
pSlot5IPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5IPPortNum.setStatus("current")
_PSlot5IOFormat_Type = IOFormat
_PSlot5IOFormat_Object = MibTableColumn
pSlot5IOFormat = _PSlot5IOFormat_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 75),
    _PSlot5IOFormat_Type()
)
pSlot5IOFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot5IOFormat.setStatus("current")
_PSlot5PortType_Type = PortType
_PSlot5PortType_Object = MibTableColumn
pSlot5PortType = _PSlot5PortType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 76),
    _PSlot5PortType_Type()
)
pSlot5PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot5PortType.setStatus("current")
_PSlot5TL1SID_Type = DescriptionString
_PSlot5TL1SID_Object = MibTableColumn
pSlot5TL1SID = _PSlot5TL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 116),
    _PSlot5TL1SID_Type()
)
pSlot5TL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5TL1SID.setStatus("current")
_PSlot5TL1COND_Type = DescriptionString
_PSlot5TL1COND_Object = MibTableColumn
pSlot5TL1COND = _PSlot5TL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 117),
    _PSlot5TL1COND_Type()
)
pSlot5TL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5TL1COND.setStatus("current")
_PSlot5TL1Eqpt_Type = DescriptionString
_PSlot5TL1Eqpt_Object = MibTableColumn
pSlot5TL1Eqpt = _PSlot5TL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 118),
    _PSlot5TL1Eqpt_Type()
)
pSlot5TL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5TL1Eqpt.setStatus("current")
_PSlot5TL1Env_Type = Boolean
_PSlot5TL1Env_Object = MibTableColumn
pSlot5TL1Env = _PSlot5TL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 119),
    _PSlot5TL1Env_Type()
)
pSlot5TL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5TL1Env.setStatus("current")
_PSlot5TL1Srveff_Type = TL1Srveff
_PSlot5TL1Srveff_Object = MibTableColumn
pSlot5TL1Srveff = _PSlot5TL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 120),
    _PSlot5TL1Srveff_Type()
)
pSlot5TL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5TL1Srveff.setStatus("current")
_PSlot5TL1Locn_Type = TL1Locn
_PSlot5TL1Locn_Object = MibTableColumn
pSlot5TL1Locn = _PSlot5TL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 121),
    _PSlot5TL1Locn_Type()
)
pSlot5TL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5TL1Locn.setStatus("current")
_PSlot5TL1Dirn_Type = TL1Dirn
_PSlot5TL1Dirn_Object = MibTableColumn
pSlot5TL1Dirn = _PSlot5TL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 122),
    _PSlot5TL1Dirn_Type()
)
pSlot5TL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5TL1Dirn.setStatus("current")
_PSlot5SensorType_Type = SensorType
_PSlot5SensorType_Object = MibTableColumn
pSlot5SensorType = _PSlot5SensorType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 131),
    _PSlot5SensorType_Type()
)
pSlot5SensorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot5SensorType.setStatus("current")


class _PSlot5Index_Type(Integer32):
    """Custom type pSlot5Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PSlot5Index_Type.__name__ = "Integer32"
_PSlot5Index_Object = MibTableColumn
pSlot5Index = _PSlot5Index_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 22, 1, 999),
    _PSlot5Index_Type()
)
pSlot5Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot5Index.setStatus("current")
_PSlot6Table_Object = MibTable
pSlot6Table = _PSlot6Table_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23)
)
if mibBuilder.loadTexts:
    pSlot6Table.setStatus("current")
_PSlot6Entry_Object = MibTableRow
pSlot6Entry = _PSlot6Entry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1)
)
pSlot6Entry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pSlot6Index"),
)
if mibBuilder.loadTexts:
    pSlot6Entry.setStatus("current")
_PSlot6Description_Type = DescriptionString
_PSlot6Description_Object = MibTableColumn
pSlot6Description = _PSlot6Description_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 3),
    _PSlot6Description_Type()
)
pSlot6Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Description.setStatus("current")
_PSlot6Desc0_Type = DescriptionString
_PSlot6Desc0_Object = MibTableColumn
pSlot6Desc0 = _PSlot6Desc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 4),
    _PSlot6Desc0_Type()
)
pSlot6Desc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Desc0.setStatus("current")
_PSlot6Desc1_Type = DescriptionString
_PSlot6Desc1_Object = MibTableColumn
pSlot6Desc1 = _PSlot6Desc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 5),
    _PSlot6Desc1_Type()
)
pSlot6Desc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Desc1.setStatus("current")
_PSlot6Desc2_Type = DescriptionString
_PSlot6Desc2_Object = MibTableColumn
pSlot6Desc2 = _PSlot6Desc2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 6),
    _PSlot6Desc2_Type()
)
pSlot6Desc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Desc2.setStatus("current")
_PSlot6Desc3_Type = DescriptionString
_PSlot6Desc3_Object = MibTableColumn
pSlot6Desc3 = _PSlot6Desc3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 7),
    _PSlot6Desc3_Type()
)
pSlot6Desc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Desc3.setStatus("current")
_PSlot6Desc4_Type = DescriptionString
_PSlot6Desc4_Object = MibTableColumn
pSlot6Desc4 = _PSlot6Desc4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 8),
    _PSlot6Desc4_Type()
)
pSlot6Desc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Desc4.setStatus("current")
_PSlot6Desc5_Type = DescriptionString
_PSlot6Desc5_Object = MibTableColumn
pSlot6Desc5 = _PSlot6Desc5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 9),
    _PSlot6Desc5_Type()
)
pSlot6Desc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Desc5.setStatus("current")
_PSlot6Configured_Type = Configured
_PSlot6Configured_Object = MibTableColumn
pSlot6Configured = _PSlot6Configured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 10),
    _PSlot6Configured_Type()
)
pSlot6Configured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Configured.setStatus("current")
_PSlot6SendEmail_Type = Boolean
_PSlot6SendEmail_Object = MibTableColumn
pSlot6SendEmail = _PSlot6SendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 11),
    _PSlot6SendEmail_Type()
)
pSlot6SendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6SendEmail.setStatus("current")
_PSlot6SendSNMPTrap_Type = Boolean
_PSlot6SendSNMPTrap_Object = MibTableColumn
pSlot6SendSNMPTrap = _PSlot6SendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 12),
    _PSlot6SendSNMPTrap_Type()
)
pSlot6SendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6SendSNMPTrap.setStatus("current")
_PSlot6IpAddress_Type = IpAddress
_PSlot6IpAddress_Object = MibTableColumn
pSlot6IpAddress = _PSlot6IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 14),
    _PSlot6IpAddress_Type()
)
pSlot6IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6IpAddress.setStatus("current")
_PSlot6Level0_Type = Level
_PSlot6Level0_Object = MibTableColumn
pSlot6Level0 = _PSlot6Level0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 17),
    _PSlot6Level0_Type()
)
pSlot6Level0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Level0.setStatus("current")
_PSlot6Level1_Type = Level
_PSlot6Level1_Object = MibTableColumn
pSlot6Level1 = _PSlot6Level1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 18),
    _PSlot6Level1_Type()
)
pSlot6Level1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Level1.setStatus("current")
_PSlot6Level2_Type = Level
_PSlot6Level2_Object = MibTableColumn
pSlot6Level2 = _PSlot6Level2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 19),
    _PSlot6Level2_Type()
)
pSlot6Level2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Level2.setStatus("current")
_PSlot6Level3_Type = Level
_PSlot6Level3_Object = MibTableColumn
pSlot6Level3 = _PSlot6Level3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 20),
    _PSlot6Level3_Type()
)
pSlot6Level3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Level3.setStatus("current")
_PSlot6Level4_Type = Level
_PSlot6Level4_Object = MibTableColumn
pSlot6Level4 = _PSlot6Level4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 21),
    _PSlot6Level4_Type()
)
pSlot6Level4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Level4.setStatus("current")
_PSlot6Level5_Type = Level
_PSlot6Level5_Object = MibTableColumn
pSlot6Level5 = _PSlot6Level5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 22),
    _PSlot6Level5_Type()
)
pSlot6Level5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Level5.setStatus("current")
_PSlot6ReadPeriod_Type = Integer32
_PSlot6ReadPeriod_Object = MibTableColumn
pSlot6ReadPeriod = _PSlot6ReadPeriod_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 23),
    _PSlot6ReadPeriod_Type()
)
pSlot6ReadPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6ReadPeriod.setStatus("current")
_PSlot6Thresh0_Type = DescriptionString
_PSlot6Thresh0_Object = MibTableColumn
pSlot6Thresh0 = _PSlot6Thresh0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 28),
    _PSlot6Thresh0_Type()
)
pSlot6Thresh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot6Thresh0.setStatus("current")
_PSlot6Thresh1_Type = DescriptionString
_PSlot6Thresh1_Object = MibTableColumn
pSlot6Thresh1 = _PSlot6Thresh1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 29),
    _PSlot6Thresh1_Type()
)
pSlot6Thresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Thresh1.setStatus("current")
_PSlot6Thresh2_Type = DescriptionString
_PSlot6Thresh2_Object = MibTableColumn
pSlot6Thresh2 = _PSlot6Thresh2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 30),
    _PSlot6Thresh2_Type()
)
pSlot6Thresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Thresh2.setStatus("current")
_PSlot6Thresh3_Type = DescriptionString
_PSlot6Thresh3_Object = MibTableColumn
pSlot6Thresh3 = _PSlot6Thresh3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 31),
    _PSlot6Thresh3_Type()
)
pSlot6Thresh3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Thresh3.setStatus("current")
_PSlot6Thresh4_Type = DescriptionString
_PSlot6Thresh4_Object = MibTableColumn
pSlot6Thresh4 = _PSlot6Thresh4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 32),
    _PSlot6Thresh4_Type()
)
pSlot6Thresh4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Thresh4.setStatus("current")
_PSlot6Thresh5_Type = DescriptionString
_PSlot6Thresh5_Object = MibTableColumn
pSlot6Thresh5 = _PSlot6Thresh5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 33),
    _PSlot6Thresh5_Type()
)
pSlot6Thresh5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot6Thresh5.setStatus("current")
_PSlot6ContactStyle_Type = ContactStyle
_PSlot6ContactStyle_Object = MibTableColumn
pSlot6ContactStyle = _PSlot6ContactStyle_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 44),
    _PSlot6ContactStyle_Type()
)
pSlot6ContactStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6ContactStyle.setStatus("current")
_PSlot6Units_Type = DescriptionString
_PSlot6Units_Object = MibTableColumn
pSlot6Units = _PSlot6Units_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 46),
    _PSlot6Units_Type()
)
pSlot6Units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot6Units.setStatus("current")
_PSlot6OutputMode_Type = OutputMode
_PSlot6OutputMode_Object = MibTableColumn
pSlot6OutputMode = _PSlot6OutputMode_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 47),
    _PSlot6OutputMode_Type()
)
pSlot6OutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6OutputMode.setStatus("current")
_PSlot6OutputState_Type = OutputState
_PSlot6OutputState_Object = MibTableColumn
pSlot6OutputState = _PSlot6OutputState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 48),
    _PSlot6OutputState_Type()
)
pSlot6OutputState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6OutputState.setStatus("current")
_PSlot6OutputAuto_Type = Integer32
_PSlot6OutputAuto_Object = MibTableColumn
pSlot6OutputAuto = _PSlot6OutputAuto_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 49),
    _PSlot6OutputAuto_Type()
)
pSlot6OutputAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6OutputAuto.setStatus("current")
_PSlot6BaudRate_Type = BaudRate
_PSlot6BaudRate_Object = MibTableColumn
pSlot6BaudRate = _PSlot6BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 57),
    _PSlot6BaudRate_Type()
)
pSlot6BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6BaudRate.setStatus("current")
_PSlot6DataBits_Type = DataBits
_PSlot6DataBits_Object = MibTableColumn
pSlot6DataBits = _PSlot6DataBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 58),
    _PSlot6DataBits_Type()
)
pSlot6DataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6DataBits.setStatus("current")
_PSlot6Parity_Type = Parity
_PSlot6Parity_Object = MibTableColumn
pSlot6Parity = _PSlot6Parity_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 59),
    _PSlot6Parity_Type()
)
pSlot6Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Parity.setStatus("current")
_PSlot6StopBits_Type = StopBits
_PSlot6StopBits_Object = MibTableColumn
pSlot6StopBits = _PSlot6StopBits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 60),
    _PSlot6StopBits_Type()
)
pSlot6StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6StopBits.setStatus("current")
_PSlot6Protocol_Type = Protocol
_PSlot6Protocol_Object = MibTableColumn
pSlot6Protocol = _PSlot6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 61),
    _PSlot6Protocol_Type()
)
pSlot6Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6Protocol.setStatus("current")
_PSlot6SerialRTS_Type = SerialRTS
_PSlot6SerialRTS_Object = MibTableColumn
pSlot6SerialRTS = _PSlot6SerialRTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 62),
    _PSlot6SerialRTS_Type()
)
pSlot6SerialRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6SerialRTS.setStatus("current")
_PSlot6SerialCTS_Type = SerialCTS
_PSlot6SerialCTS_Object = MibTableColumn
pSlot6SerialCTS = _PSlot6SerialCTS_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 63),
    _PSlot6SerialCTS_Type()
)
pSlot6SerialCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6SerialCTS.setStatus("current")
_PSlot6LiveDescription_Type = DescriptionString
_PSlot6LiveDescription_Object = MibTableColumn
pSlot6LiveDescription = _PSlot6LiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 64),
    _PSlot6LiveDescription_Type()
)
pSlot6LiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot6LiveDescription.setStatus("current")
_PSlot6LiveLevel_Type = DescriptionString
_PSlot6LiveLevel_Object = MibTableColumn
pSlot6LiveLevel = _PSlot6LiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 65),
    _PSlot6LiveLevel_Type()
)
pSlot6LiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot6LiveLevel.setStatus("current")
_PSlot6LiveRaw_Type = DescriptionString
_PSlot6LiveRaw_Object = MibTableColumn
pSlot6LiveRaw = _PSlot6LiveRaw_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 66),
    _PSlot6LiveRaw_Type()
)
pSlot6LiveRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot6LiveRaw.setStatus("current")
_PSlot6LiveTime_Type = DescriptionString
_PSlot6LiveTime_Object = MibTableColumn
pSlot6LiveTime = _PSlot6LiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 67),
    _PSlot6LiveTime_Type()
)
pSlot6LiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot6LiveTime.setStatus("current")
_PSlot6Present_Type = Boolean
_PSlot6Present_Object = MibTableColumn
pSlot6Present = _PSlot6Present_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 68),
    _PSlot6Present_Type()
)
pSlot6Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot6Present.setStatus("current")
_PSlot6OutputAutoPkg_Type = Integer32
_PSlot6OutputAutoPkg_Object = MibTableColumn
pSlot6OutputAutoPkg = _PSlot6OutputAutoPkg_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 71),
    _PSlot6OutputAutoPkg_Type()
)
pSlot6OutputAutoPkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6OutputAutoPkg.setStatus("current")
_PSlot6VoltageRange_Type = VoltageRange
_PSlot6VoltageRange_Object = MibTableColumn
pSlot6VoltageRange = _PSlot6VoltageRange_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 72),
    _PSlot6VoltageRange_Type()
)
pSlot6VoltageRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot6VoltageRange.setStatus("current")
_PSlot6IPPortNum_Type = Integer32
_PSlot6IPPortNum_Object = MibTableColumn
pSlot6IPPortNum = _PSlot6IPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 73),
    _PSlot6IPPortNum_Type()
)
pSlot6IPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6IPPortNum.setStatus("current")
_PSlot6IOFormat_Type = IOFormat
_PSlot6IOFormat_Object = MibTableColumn
pSlot6IOFormat = _PSlot6IOFormat_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 75),
    _PSlot6IOFormat_Type()
)
pSlot6IOFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot6IOFormat.setStatus("current")
_PSlot6PortType_Type = PortType
_PSlot6PortType_Object = MibTableColumn
pSlot6PortType = _PSlot6PortType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 76),
    _PSlot6PortType_Type()
)
pSlot6PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot6PortType.setStatus("current")
_PSlot6TL1SID_Type = DescriptionString
_PSlot6TL1SID_Object = MibTableColumn
pSlot6TL1SID = _PSlot6TL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 116),
    _PSlot6TL1SID_Type()
)
pSlot6TL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6TL1SID.setStatus("current")
_PSlot6TL1COND_Type = DescriptionString
_PSlot6TL1COND_Object = MibTableColumn
pSlot6TL1COND = _PSlot6TL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 117),
    _PSlot6TL1COND_Type()
)
pSlot6TL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6TL1COND.setStatus("current")
_PSlot6TL1Eqpt_Type = DescriptionString
_PSlot6TL1Eqpt_Object = MibTableColumn
pSlot6TL1Eqpt = _PSlot6TL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 118),
    _PSlot6TL1Eqpt_Type()
)
pSlot6TL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6TL1Eqpt.setStatus("current")
_PSlot6TL1Env_Type = Boolean
_PSlot6TL1Env_Object = MibTableColumn
pSlot6TL1Env = _PSlot6TL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 119),
    _PSlot6TL1Env_Type()
)
pSlot6TL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6TL1Env.setStatus("current")
_PSlot6TL1Srveff_Type = TL1Srveff
_PSlot6TL1Srveff_Object = MibTableColumn
pSlot6TL1Srveff = _PSlot6TL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 120),
    _PSlot6TL1Srveff_Type()
)
pSlot6TL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6TL1Srveff.setStatus("current")
_PSlot6TL1Locn_Type = TL1Locn
_PSlot6TL1Locn_Object = MibTableColumn
pSlot6TL1Locn = _PSlot6TL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 121),
    _PSlot6TL1Locn_Type()
)
pSlot6TL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6TL1Locn.setStatus("current")
_PSlot6TL1Dirn_Type = TL1Dirn
_PSlot6TL1Dirn_Object = MibTableColumn
pSlot6TL1Dirn = _PSlot6TL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 122),
    _PSlot6TL1Dirn_Type()
)
pSlot6TL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6TL1Dirn.setStatus("current")
_PSlot6SensorType_Type = SensorType
_PSlot6SensorType_Object = MibTableColumn
pSlot6SensorType = _PSlot6SensorType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 131),
    _PSlot6SensorType_Type()
)
pSlot6SensorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSlot6SensorType.setStatus("current")


class _PSlot6Index_Type(Integer32):
    """Custom type pSlot6Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PSlot6Index_Type.__name__ = "Integer32"
_PSlot6Index_Object = MibTableColumn
pSlot6Index = _PSlot6Index_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 23, 1, 999),
    _PSlot6Index_Type()
)
pSlot6Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSlot6Index.setStatus("current")
_PNetPortsTable_Object = MibTable
pNetPortsTable = _PNetPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 24)
)
if mibBuilder.loadTexts:
    pNetPortsTable.setStatus("current")
_PNetPortsEntry_Object = MibTableRow
pNetPortsEntry = _PNetPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 24, 1)
)
pNetPortsEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pNetPortsIndex"),
)
if mibBuilder.loadTexts:
    pNetPortsEntry.setStatus("current")
_PNetPortsDescription_Type = DescriptionString
_PNetPortsDescription_Object = MibTableColumn
pNetPortsDescription = _PNetPortsDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 24, 1, 3),
    _PNetPortsDescription_Type()
)
pNetPortsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pNetPortsDescription.setStatus("current")
_PNetPortsIPPortNum_Type = Integer32
_PNetPortsIPPortNum_Object = MibTableColumn
pNetPortsIPPortNum = _PNetPortsIPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 24, 1, 73),
    _PNetPortsIPPortNum_Type()
)
pNetPortsIPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pNetPortsIPPortNum.setStatus("current")


class _PNetPortsIndex_Type(Integer32):
    """Custom type pNetPortsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PNetPortsIndex_Type.__name__ = "Integer32"
_PNetPortsIndex_Object = MibTableColumn
pNetPortsIndex = _PNetPortsIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 24, 1, 999),
    _PNetPortsIndex_Type()
)
pNetPortsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pNetPortsIndex.setStatus("current")
_WirelessModem_ObjectIdentity = ObjectIdentity
wirelessModem = _WirelessModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 25)
)
_WirelessModemBackupIPAddress_Type = IpAddress
_WirelessModemBackupIPAddress_Object = MibScalar
wirelessModemBackupIPAddress = _WirelessModemBackupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 25, 78),
    _WirelessModemBackupIPAddress_Type()
)
wirelessModemBackupIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessModemBackupIPAddress.setStatus("current")
_WirelessModemTime_Type = DescriptionString
_WirelessModemTime_Object = MibScalar
wirelessModemTime = _WirelessModemTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 25, 81),
    _WirelessModemTime_Type()
)
wirelessModemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessModemTime.setStatus("current")
_WirelessModemTransmit_Type = DescriptionString
_WirelessModemTransmit_Object = MibScalar
wirelessModemTransmit = _WirelessModemTransmit_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 25, 96),
    _WirelessModemTransmit_Type()
)
wirelessModemTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessModemTransmit.setStatus("current")
_WirelessModemUseWirelessNetwork_Type = Boolean
_WirelessModemUseWirelessNetwork_Object = MibScalar
wirelessModemUseWirelessNetwork = _WirelessModemUseWirelessNetwork_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 25, 97),
    _WirelessModemUseWirelessNetwork_Type()
)
wirelessModemUseWirelessNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessModemUseWirelessNetwork.setStatus("current")
_WirelessModemUseResetTime_Type = Boolean
_WirelessModemUseResetTime_Object = MibScalar
wirelessModemUseResetTime = _WirelessModemUseResetTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 25, 98),
    _WirelessModemUseResetTime_Type()
)
wirelessModemUseResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessModemUseResetTime.setStatus("current")
_WirelessModemResponseWaitTime_Type = DescriptionString
_WirelessModemResponseWaitTime_Object = MibScalar
wirelessModemResponseWaitTime = _WirelessModemResponseWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 25, 99),
    _WirelessModemResponseWaitTime_Type()
)
wirelessModemResponseWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessModemResponseWaitTime.setStatus("current")
_WirelessModemSecondary_Type = Boolean
_WirelessModemSecondary_Object = MibScalar
wirelessModemSecondary = _WirelessModemSecondary_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 25, 115),
    _WirelessModemSecondary_Type()
)
wirelessModemSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessModemSecondary.setStatus("current")
_WebmonSecurity_ObjectIdentity = ObjectIdentity
webmonSecurity = _WebmonSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 26)
)
_WebmonSecurityUserLevel_Type = Unsigned32
_WebmonSecurityUserLevel_Object = MibScalar
webmonSecurityUserLevel = _WebmonSecurityUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 26, 55),
    _WebmonSecurityUserLevel_Type()
)
webmonSecurityUserLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webmonSecurityUserLevel.setStatus("current")
_WebmonSecurityUnsecured_Type = Boolean
_WebmonSecurityUnsecured_Object = MibScalar
webmonSecurityUnsecured = _WebmonSecurityUnsecured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 26, 77),
    _WebmonSecurityUnsecured_Type()
)
webmonSecurityUnsecured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webmonSecurityUnsecured.setStatus("current")
_DateTime_ObjectIdentity = ObjectIdentity
dateTime = _DateTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 27)
)
_DateTimeConfigured_Type = Configured
_DateTimeConfigured_Object = MibScalar
dateTimeConfigured = _DateTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 27, 10),
    _DateTimeConfigured_Type()
)
dateTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeConfigured.setStatus("current")
_DateTimeIpAddress_Type = IpAddress
_DateTimeIpAddress_Object = MibScalar
dateTimeIpAddress = _DateTimeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 27, 14),
    _DateTimeIpAddress_Type()
)
dateTimeIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeIpAddress.setStatus("current")
_DateTimeDaylightSaving_Type = Boolean
_DateTimeDaylightSaving_Object = MibScalar
dateTimeDaylightSaving = _DateTimeDaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 27, 53),
    _DateTimeDaylightSaving_Type()
)
dateTimeDaylightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeDaylightSaving.setStatus("current")
_DateTimeDate_Type = DescriptionString
_DateTimeDate_Object = MibScalar
dateTimeDate = _DateTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 27, 80),
    _DateTimeDate_Type()
)
dateTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeDate.setStatus("current")
_DateTimeTime_Type = DescriptionString
_DateTimeTime_Object = MibScalar
dateTimeTime = _DateTimeTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 27, 81),
    _DateTimeTime_Type()
)
dateTimeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeTime.setStatus("current")
_DateTimeNegOffset_Type = Boolean
_DateTimeNegOffset_Object = MibScalar
dateTimeNegOffset = _DateTimeNegOffset_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 27, 88),
    _DateTimeNegOffset_Type()
)
dateTimeNegOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNegOffset.setStatus("current")
_DateTimeUTCOffset_Type = DescriptionString
_DateTimeUTCOffset_Object = MibScalar
dateTimeUTCOffset = _DateTimeUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 27, 89),
    _DateTimeUTCOffset_Type()
)
dateTimeUTCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeUTCOffset.setStatus("current")
_PDCMProtocolTable_Object = MibTable
pDCMProtocolTable = _PDCMProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 28)
)
if mibBuilder.loadTexts:
    pDCMProtocolTable.setStatus("current")
_PDCMProtocolEntry_Object = MibTableRow
pDCMProtocolEntry = _PDCMProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 28, 1)
)
pDCMProtocolEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pDCMProtocolIndex"),
)
if mibBuilder.loadTexts:
    pDCMProtocolEntry.setStatus("current")
_PDCMProtocolDescription_Type = DescriptionString
_PDCMProtocolDescription_Object = MibTableColumn
pDCMProtocolDescription = _PDCMProtocolDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 28, 1, 3),
    _PDCMProtocolDescription_Type()
)
pDCMProtocolDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDCMProtocolDescription.setStatus("current")
_PDCMProtocolConfigured_Type = Configured
_PDCMProtocolConfigured_Object = MibTableColumn
pDCMProtocolConfigured = _PDCMProtocolConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 28, 1, 10),
    _PDCMProtocolConfigured_Type()
)
pDCMProtocolConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pDCMProtocolConfigured.setStatus("current")
_PDCMProtocolBaseDCMAddress_Type = Integer32
_PDCMProtocolBaseDCMAddress_Object = MibTableColumn
pDCMProtocolBaseDCMAddress = _PDCMProtocolBaseDCMAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 28, 1, 83),
    _PDCMProtocolBaseDCMAddress_Type()
)
pDCMProtocolBaseDCMAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pDCMProtocolBaseDCMAddress.setStatus("current")


class _PDCMProtocolIndex_Type(Integer32):
    """Custom type pDCMProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 27),
    )


_PDCMProtocolIndex_Type.__name__ = "Integer32"
_PDCMProtocolIndex_Object = MibTableColumn
pDCMProtocolIndex = _PDCMProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 28, 1, 999),
    _PDCMProtocolIndex_Type()
)
pDCMProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDCMProtocolIndex.setStatus("current")
_PdialOutTable_Object = MibTable
pdialOutTable = _PdialOutTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 29)
)
if mibBuilder.loadTexts:
    pdialOutTable.setStatus("current")
_PdialOutEntry_Object = MibTableRow
pdialOutEntry = _PdialOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 29, 1)
)
pdialOutEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pdialOutIndex"),
)
if mibBuilder.loadTexts:
    pdialOutEntry.setStatus("current")
_PdialOutConfigured_Type = Configured
_PdialOutConfigured_Object = MibTableColumn
pdialOutConfigured = _PdialOutConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 29, 1, 10),
    _PdialOutConfigured_Type()
)
pdialOutConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdialOutConfigured.setStatus("current")
_PdialOutName_Type = DescriptionString
_PdialOutName_Object = MibTableColumn
pdialOutName = _PdialOutName_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 29, 1, 25),
    _PdialOutName_Type()
)
pdialOutName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdialOutName.setStatus("current")
_PdialOutPassword_Type = DescriptionString
_PdialOutPassword_Object = MibTableColumn
pdialOutPassword = _PdialOutPassword_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 29, 1, 26),
    _PdialOutPassword_Type()
)
pdialOutPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdialOutPassword.setStatus("current")
_PdialOutDialOutNumber_Type = DescriptionString
_PdialOutDialOutNumber_Object = MibTableColumn
pdialOutDialOutNumber = _PdialOutDialOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 29, 1, 79),
    _PdialOutDialOutNumber_Type()
)
pdialOutDialOutNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdialOutDialOutNumber.setStatus("current")


class _PdialOutIndex_Type(Integer32):
    """Custom type pdialOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PdialOutIndex_Type.__name__ = "Integer32"
_PdialOutIndex_Object = MibTableColumn
pdialOutIndex = _PdialOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 29, 1, 999),
    _PdialOutIndex_Type()
)
pdialOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdialOutIndex.setStatus("current")
_PderivedDiscreteTable_Object = MibTable
pderivedDiscreteTable = _PderivedDiscreteTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30)
)
if mibBuilder.loadTexts:
    pderivedDiscreteTable.setStatus("current")
_PderivedDiscreteEntry_Object = MibTableRow
pderivedDiscreteEntry = _PderivedDiscreteEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1)
)
pderivedDiscreteEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteIndex"),
)
if mibBuilder.loadTexts:
    pderivedDiscreteEntry.setStatus("current")
_PderivedDiscreteDescription_Type = DescriptionString
_PderivedDiscreteDescription_Object = MibTableColumn
pderivedDiscreteDescription = _PderivedDiscreteDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 3),
    _PderivedDiscreteDescription_Type()
)
pderivedDiscreteDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteDescription.setStatus("current")
_PderivedDiscreteDesc0_Type = DescriptionString
_PderivedDiscreteDesc0_Object = MibTableColumn
pderivedDiscreteDesc0 = _PderivedDiscreteDesc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 4),
    _PderivedDiscreteDesc0_Type()
)
pderivedDiscreteDesc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteDesc0.setStatus("current")
_PderivedDiscreteDesc1_Type = DescriptionString
_PderivedDiscreteDesc1_Object = MibTableColumn
pderivedDiscreteDesc1 = _PderivedDiscreteDesc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 5),
    _PderivedDiscreteDesc1_Type()
)
pderivedDiscreteDesc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteDesc1.setStatus("current")
_PderivedDiscreteConfigured_Type = Configured
_PderivedDiscreteConfigured_Object = MibTableColumn
pderivedDiscreteConfigured = _PderivedDiscreteConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 10),
    _PderivedDiscreteConfigured_Type()
)
pderivedDiscreteConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteConfigured.setStatus("current")
_PderivedDiscreteSendEmail_Type = Boolean
_PderivedDiscreteSendEmail_Object = MibTableColumn
pderivedDiscreteSendEmail = _PderivedDiscreteSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 11),
    _PderivedDiscreteSendEmail_Type()
)
pderivedDiscreteSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteSendEmail.setStatus("current")
_PderivedDiscreteSendSNMPTrap_Type = Boolean
_PderivedDiscreteSendSNMPTrap_Object = MibTableColumn
pderivedDiscreteSendSNMPTrap = _PderivedDiscreteSendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 12),
    _PderivedDiscreteSendSNMPTrap_Type()
)
pderivedDiscreteSendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteSendSNMPTrap.setStatus("current")
_PderivedDiscreteLevel0_Type = Level
_PderivedDiscreteLevel0_Object = MibTableColumn
pderivedDiscreteLevel0 = _PderivedDiscreteLevel0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 17),
    _PderivedDiscreteLevel0_Type()
)
pderivedDiscreteLevel0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteLevel0.setStatus("current")
_PderivedDiscreteLevel1_Type = Level
_PderivedDiscreteLevel1_Object = MibTableColumn
pderivedDiscreteLevel1 = _PderivedDiscreteLevel1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 18),
    _PderivedDiscreteLevel1_Type()
)
pderivedDiscreteLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteLevel1.setStatus("current")
_PderivedDiscreteLiveDescription_Type = DescriptionString
_PderivedDiscreteLiveDescription_Object = MibTableColumn
pderivedDiscreteLiveDescription = _PderivedDiscreteLiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 64),
    _PderivedDiscreteLiveDescription_Type()
)
pderivedDiscreteLiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pderivedDiscreteLiveDescription.setStatus("current")
_PderivedDiscreteLiveLevel_Type = DescriptionString
_PderivedDiscreteLiveLevel_Object = MibTableColumn
pderivedDiscreteLiveLevel = _PderivedDiscreteLiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 65),
    _PderivedDiscreteLiveLevel_Type()
)
pderivedDiscreteLiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pderivedDiscreteLiveLevel.setStatus("current")
_PderivedDiscreteLiveTime_Type = DescriptionString
_PderivedDiscreteLiveTime_Object = MibTableColumn
pderivedDiscreteLiveTime = _PderivedDiscreteLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 67),
    _PderivedDiscreteLiveTime_Type()
)
pderivedDiscreteLiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pderivedDiscreteLiveTime.setStatus("current")
_PderivedDiscreteElementAPkg_Type = Integer32
_PderivedDiscreteElementAPkg_Object = MibTableColumn
pderivedDiscreteElementAPkg = _PderivedDiscreteElementAPkg_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 90),
    _PderivedDiscreteElementAPkg_Type()
)
pderivedDiscreteElementAPkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteElementAPkg.setStatus("current")
_PderivedDiscreteElementAPoint_Type = Integer32
_PderivedDiscreteElementAPoint_Object = MibTableColumn
pderivedDiscreteElementAPoint = _PderivedDiscreteElementAPoint_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 91),
    _PderivedDiscreteElementAPoint_Type()
)
pderivedDiscreteElementAPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteElementAPoint.setStatus("current")
_PderivedDiscreteElementBPkg_Type = Integer32
_PderivedDiscreteElementBPkg_Object = MibTableColumn
pderivedDiscreteElementBPkg = _PderivedDiscreteElementBPkg_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 92),
    _PderivedDiscreteElementBPkg_Type()
)
pderivedDiscreteElementBPkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteElementBPkg.setStatus("current")
_PderivedDiscreteElementBPoint_Type = Integer32
_PderivedDiscreteElementBPoint_Object = MibTableColumn
pderivedDiscreteElementBPoint = _PderivedDiscreteElementBPoint_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 93),
    _PderivedDiscreteElementBPoint_Type()
)
pderivedDiscreteElementBPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteElementBPoint.setStatus("current")
_PderivedDiscreteDiscreteFormula_Type = DiscreteFormula
_PderivedDiscreteDiscreteFormula_Object = MibTableColumn
pderivedDiscreteDiscreteFormula = _PderivedDiscreteDiscreteFormula_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 94),
    _PderivedDiscreteDiscreteFormula_Type()
)
pderivedDiscreteDiscreteFormula.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteDiscreteFormula.setStatus("current")
_PderivedDiscreteTL1SID_Type = DescriptionString
_PderivedDiscreteTL1SID_Object = MibTableColumn
pderivedDiscreteTL1SID = _PderivedDiscreteTL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 116),
    _PderivedDiscreteTL1SID_Type()
)
pderivedDiscreteTL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteTL1SID.setStatus("current")
_PderivedDiscreteTL1COND_Type = DescriptionString
_PderivedDiscreteTL1COND_Object = MibTableColumn
pderivedDiscreteTL1COND = _PderivedDiscreteTL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 117),
    _PderivedDiscreteTL1COND_Type()
)
pderivedDiscreteTL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteTL1COND.setStatus("current")
_PderivedDiscreteTL1Eqpt_Type = DescriptionString
_PderivedDiscreteTL1Eqpt_Object = MibTableColumn
pderivedDiscreteTL1Eqpt = _PderivedDiscreteTL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 118),
    _PderivedDiscreteTL1Eqpt_Type()
)
pderivedDiscreteTL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteTL1Eqpt.setStatus("current")
_PderivedDiscreteTL1Env_Type = Boolean
_PderivedDiscreteTL1Env_Object = MibTableColumn
pderivedDiscreteTL1Env = _PderivedDiscreteTL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 119),
    _PderivedDiscreteTL1Env_Type()
)
pderivedDiscreteTL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteTL1Env.setStatus("current")
_PderivedDiscreteTL1Srveff_Type = TL1Srveff
_PderivedDiscreteTL1Srveff_Object = MibTableColumn
pderivedDiscreteTL1Srveff = _PderivedDiscreteTL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 120),
    _PderivedDiscreteTL1Srveff_Type()
)
pderivedDiscreteTL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteTL1Srveff.setStatus("current")
_PderivedDiscreteTL1Locn_Type = TL1Locn
_PderivedDiscreteTL1Locn_Object = MibTableColumn
pderivedDiscreteTL1Locn = _PderivedDiscreteTL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 121),
    _PderivedDiscreteTL1Locn_Type()
)
pderivedDiscreteTL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteTL1Locn.setStatus("current")
_PderivedDiscreteTL1Dirn_Type = TL1Dirn
_PderivedDiscreteTL1Dirn_Object = MibTableColumn
pderivedDiscreteTL1Dirn = _PderivedDiscreteTL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 122),
    _PderivedDiscreteTL1Dirn_Type()
)
pderivedDiscreteTL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedDiscreteTL1Dirn.setStatus("current")


class _PderivedDiscreteIndex_Type(Integer32):
    """Custom type pderivedDiscreteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PderivedDiscreteIndex_Type.__name__ = "Integer32"
_PderivedDiscreteIndex_Object = MibTableColumn
pderivedDiscreteIndex = _PderivedDiscreteIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 30, 1, 999),
    _PderivedDiscreteIndex_Type()
)
pderivedDiscreteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pderivedDiscreteIndex.setStatus("current")
_License_ObjectIdentity = ObjectIdentity
license = _License_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 31)
)
_LicenseDescription_Type = DescriptionString
_LicenseDescription_Object = MibScalar
licenseDescription = _LicenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 31, 3),
    _LicenseDescription_Type()
)
licenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseDescription.setStatus("current")
_LicenseLicenseKey_Type = DescriptionString
_LicenseLicenseKey_Object = MibScalar
licenseLicenseKey = _LicenseLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 31, 84),
    _LicenseLicenseKey_Type()
)
licenseLicenseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseLicenseKey.setStatus("current")
_LicenseExpires_Type = DescriptionString
_LicenseExpires_Object = MibScalar
licenseExpires = _LicenseExpires_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 31, 85),
    _LicenseExpires_Type()
)
licenseExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseExpires.setStatus("current")
_LicenseAllowTL1_Type = Boolean
_LicenseAllowTL1_Object = MibScalar
licenseAllowTL1 = _LicenseAllowTL1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 31, 124),
    _LicenseAllowTL1_Type()
)
licenseAllowTL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseAllowTL1.setStatus("current")
_Pe2aHostTable_Object = MibTable
pe2aHostTable = _Pe2aHostTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32)
)
if mibBuilder.loadTexts:
    pe2aHostTable.setStatus("current")
_Pe2aHostEntry_Object = MibTableRow
pe2aHostEntry = _Pe2aHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1)
)
pe2aHostEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pe2aHostIndex"),
)
if mibBuilder.loadTexts:
    pe2aHostEntry.setStatus("current")
_Pe2aHostDescription_Type = DescriptionString
_Pe2aHostDescription_Object = MibTableColumn
pe2aHostDescription = _Pe2aHostDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 3),
    _Pe2aHostDescription_Type()
)
pe2aHostDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostDescription.setStatus("current")
_Pe2aHostConfigured_Type = Configured
_Pe2aHostConfigured_Object = MibTableColumn
pe2aHostConfigured = _Pe2aHostConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 10),
    _Pe2aHostConfigured_Type()
)
pe2aHostConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostConfigured.setStatus("current")
_Pe2aHostIpAddress_Type = IpAddress
_Pe2aHostIpAddress_Object = MibTableColumn
pe2aHostIpAddress = _Pe2aHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 14),
    _Pe2aHostIpAddress_Type()
)
pe2aHostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostIpAddress.setStatus("current")
_Pe2aHostLevel0_Type = Level
_Pe2aHostLevel0_Object = MibTableColumn
pe2aHostLevel0 = _Pe2aHostLevel0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 17),
    _Pe2aHostLevel0_Type()
)
pe2aHostLevel0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostLevel0.setStatus("current")
_Pe2aHostLevel1_Type = Level
_Pe2aHostLevel1_Object = MibTableColumn
pe2aHostLevel1 = _Pe2aHostLevel1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 18),
    _Pe2aHostLevel1_Type()
)
pe2aHostLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostLevel1.setStatus("current")
_Pe2aHostLevel2_Type = Level
_Pe2aHostLevel2_Object = MibTableColumn
pe2aHostLevel2 = _Pe2aHostLevel2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 19),
    _Pe2aHostLevel2_Type()
)
pe2aHostLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostLevel2.setStatus("current")
_Pe2aHostRosterID_Type = Integer32
_Pe2aHostRosterID_Object = MibTableColumn
pe2aHostRosterID = _Pe2aHostRosterID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 37),
    _Pe2aHostRosterID_Type()
)
pe2aHostRosterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostRosterID.setStatus("current")
_Pe2aHostPollAddress_Type = Integer32
_Pe2aHostPollAddress_Object = MibTableColumn
pe2aHostPollAddress = _Pe2aHostPollAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 56),
    _Pe2aHostPollAddress_Type()
)
pe2aHostPollAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostPollAddress.setStatus("current")
_Pe2aHostIPPortNum_Type = Integer32
_Pe2aHostIPPortNum_Object = MibTableColumn
pe2aHostIPPortNum = _Pe2aHostIPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 73),
    _Pe2aHostIPPortNum_Type()
)
pe2aHostIPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostIPPortNum.setStatus("current")
_Pe2aHostTL1SID_Type = DescriptionString
_Pe2aHostTL1SID_Object = MibTableColumn
pe2aHostTL1SID = _Pe2aHostTL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 116),
    _Pe2aHostTL1SID_Type()
)
pe2aHostTL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostTL1SID.setStatus("current")
_Pe2aHostTL1COND_Type = DescriptionString
_Pe2aHostTL1COND_Object = MibTableColumn
pe2aHostTL1COND = _Pe2aHostTL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 117),
    _Pe2aHostTL1COND_Type()
)
pe2aHostTL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostTL1COND.setStatus("current")
_Pe2aHostTL1Eqpt_Type = DescriptionString
_Pe2aHostTL1Eqpt_Object = MibTableColumn
pe2aHostTL1Eqpt = _Pe2aHostTL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 118),
    _Pe2aHostTL1Eqpt_Type()
)
pe2aHostTL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostTL1Eqpt.setStatus("current")
_Pe2aHostTL1Env_Type = Boolean
_Pe2aHostTL1Env_Object = MibTableColumn
pe2aHostTL1Env = _Pe2aHostTL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 119),
    _Pe2aHostTL1Env_Type()
)
pe2aHostTL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostTL1Env.setStatus("current")
_Pe2aHostTL1Srveff_Type = TL1Srveff
_Pe2aHostTL1Srveff_Object = MibTableColumn
pe2aHostTL1Srveff = _Pe2aHostTL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 120),
    _Pe2aHostTL1Srveff_Type()
)
pe2aHostTL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostTL1Srveff.setStatus("current")
_Pe2aHostTL1Locn_Type = TL1Locn
_Pe2aHostTL1Locn_Object = MibTableColumn
pe2aHostTL1Locn = _Pe2aHostTL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 121),
    _Pe2aHostTL1Locn_Type()
)
pe2aHostTL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostTL1Locn.setStatus("current")
_Pe2aHostTL1Dirn_Type = TL1Dirn
_Pe2aHostTL1Dirn_Object = MibTableColumn
pe2aHostTL1Dirn = _Pe2aHostTL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 122),
    _Pe2aHostTL1Dirn_Type()
)
pe2aHostTL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pe2aHostTL1Dirn.setStatus("current")


class _Pe2aHostIndex_Type(Integer32):
    """Custom type pe2aHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Pe2aHostIndex_Type.__name__ = "Integer32"
_Pe2aHostIndex_Object = MibTableColumn
pe2aHostIndex = _Pe2aHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 32, 1, 999),
    _Pe2aHostIndex_Type()
)
pe2aHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pe2aHostIndex.setStatus("current")
_PderivedAnalogTable_Object = MibTable
pderivedAnalogTable = _PderivedAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33)
)
if mibBuilder.loadTexts:
    pderivedAnalogTable.setStatus("current")
_PderivedAnalogEntry_Object = MibTableRow
pderivedAnalogEntry = _PderivedAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1)
)
pderivedAnalogEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogIndex"),
)
if mibBuilder.loadTexts:
    pderivedAnalogEntry.setStatus("current")
_PderivedAnalogDescription_Type = DescriptionString
_PderivedAnalogDescription_Object = MibTableColumn
pderivedAnalogDescription = _PderivedAnalogDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 3),
    _PderivedAnalogDescription_Type()
)
pderivedAnalogDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogDescription.setStatus("current")
_PderivedAnalogDesc0_Type = DescriptionString
_PderivedAnalogDesc0_Object = MibTableColumn
pderivedAnalogDesc0 = _PderivedAnalogDesc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 4),
    _PderivedAnalogDesc0_Type()
)
pderivedAnalogDesc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogDesc0.setStatus("current")
_PderivedAnalogDesc1_Type = DescriptionString
_PderivedAnalogDesc1_Object = MibTableColumn
pderivedAnalogDesc1 = _PderivedAnalogDesc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 5),
    _PderivedAnalogDesc1_Type()
)
pderivedAnalogDesc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogDesc1.setStatus("current")
_PderivedAnalogDesc2_Type = DescriptionString
_PderivedAnalogDesc2_Object = MibTableColumn
pderivedAnalogDesc2 = _PderivedAnalogDesc2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 6),
    _PderivedAnalogDesc2_Type()
)
pderivedAnalogDesc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogDesc2.setStatus("current")
_PderivedAnalogDesc3_Type = DescriptionString
_PderivedAnalogDesc3_Object = MibTableColumn
pderivedAnalogDesc3 = _PderivedAnalogDesc3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 7),
    _PderivedAnalogDesc3_Type()
)
pderivedAnalogDesc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogDesc3.setStatus("current")
_PderivedAnalogDesc4_Type = DescriptionString
_PderivedAnalogDesc4_Object = MibTableColumn
pderivedAnalogDesc4 = _PderivedAnalogDesc4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 8),
    _PderivedAnalogDesc4_Type()
)
pderivedAnalogDesc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogDesc4.setStatus("current")
_PderivedAnalogConfigured_Type = Configured
_PderivedAnalogConfigured_Object = MibTableColumn
pderivedAnalogConfigured = _PderivedAnalogConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 10),
    _PderivedAnalogConfigured_Type()
)
pderivedAnalogConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogConfigured.setStatus("current")
_PderivedAnalogSendEmail_Type = Boolean
_PderivedAnalogSendEmail_Object = MibTableColumn
pderivedAnalogSendEmail = _PderivedAnalogSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 11),
    _PderivedAnalogSendEmail_Type()
)
pderivedAnalogSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogSendEmail.setStatus("current")
_PderivedAnalogSendSNMPTrap_Type = Boolean
_PderivedAnalogSendSNMPTrap_Object = MibTableColumn
pderivedAnalogSendSNMPTrap = _PderivedAnalogSendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 12),
    _PderivedAnalogSendSNMPTrap_Type()
)
pderivedAnalogSendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogSendSNMPTrap.setStatus("current")
_PderivedAnalogLevel0_Type = Level
_PderivedAnalogLevel0_Object = MibTableColumn
pderivedAnalogLevel0 = _PderivedAnalogLevel0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 17),
    _PderivedAnalogLevel0_Type()
)
pderivedAnalogLevel0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogLevel0.setStatus("current")
_PderivedAnalogLevel1_Type = Level
_PderivedAnalogLevel1_Object = MibTableColumn
pderivedAnalogLevel1 = _PderivedAnalogLevel1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 18),
    _PderivedAnalogLevel1_Type()
)
pderivedAnalogLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogLevel1.setStatus("current")
_PderivedAnalogLevel2_Type = Level
_PderivedAnalogLevel2_Object = MibTableColumn
pderivedAnalogLevel2 = _PderivedAnalogLevel2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 19),
    _PderivedAnalogLevel2_Type()
)
pderivedAnalogLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogLevel2.setStatus("current")
_PderivedAnalogLevel3_Type = Level
_PderivedAnalogLevel3_Object = MibTableColumn
pderivedAnalogLevel3 = _PderivedAnalogLevel3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 20),
    _PderivedAnalogLevel3_Type()
)
pderivedAnalogLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogLevel3.setStatus("current")
_PderivedAnalogLevel4_Type = Level
_PderivedAnalogLevel4_Object = MibTableColumn
pderivedAnalogLevel4 = _PderivedAnalogLevel4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 21),
    _PderivedAnalogLevel4_Type()
)
pderivedAnalogLevel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogLevel4.setStatus("current")
_PderivedAnalogThresh0_Type = DescriptionString
_PderivedAnalogThresh0_Object = MibTableColumn
pderivedAnalogThresh0 = _PderivedAnalogThresh0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 28),
    _PderivedAnalogThresh0_Type()
)
pderivedAnalogThresh0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogThresh0.setStatus("current")
_PderivedAnalogThresh1_Type = DescriptionString
_PderivedAnalogThresh1_Object = MibTableColumn
pderivedAnalogThresh1 = _PderivedAnalogThresh1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 29),
    _PderivedAnalogThresh1_Type()
)
pderivedAnalogThresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogThresh1.setStatus("current")
_PderivedAnalogThresh2_Type = DescriptionString
_PderivedAnalogThresh2_Object = MibTableColumn
pderivedAnalogThresh2 = _PderivedAnalogThresh2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 30),
    _PderivedAnalogThresh2_Type()
)
pderivedAnalogThresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogThresh2.setStatus("current")
_PderivedAnalogThresh3_Type = DescriptionString
_PderivedAnalogThresh3_Object = MibTableColumn
pderivedAnalogThresh3 = _PderivedAnalogThresh3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 31),
    _PderivedAnalogThresh3_Type()
)
pderivedAnalogThresh3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogThresh3.setStatus("current")
_PderivedAnalogThresh4_Type = DescriptionString
_PderivedAnalogThresh4_Object = MibTableColumn
pderivedAnalogThresh4 = _PderivedAnalogThresh4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 32),
    _PderivedAnalogThresh4_Type()
)
pderivedAnalogThresh4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogThresh4.setStatus("current")
_PderivedAnalogThresh5_Type = DescriptionString
_PderivedAnalogThresh5_Object = MibTableColumn
pderivedAnalogThresh5 = _PderivedAnalogThresh5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 33),
    _PderivedAnalogThresh5_Type()
)
pderivedAnalogThresh5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogThresh5.setStatus("current")
_PderivedAnalogUnits_Type = DescriptionString
_PderivedAnalogUnits_Object = MibTableColumn
pderivedAnalogUnits = _PderivedAnalogUnits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 46),
    _PderivedAnalogUnits_Type()
)
pderivedAnalogUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogUnits.setStatus("current")
_PderivedAnalogLiveDescription_Type = DescriptionString
_PderivedAnalogLiveDescription_Object = MibTableColumn
pderivedAnalogLiveDescription = _PderivedAnalogLiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 64),
    _PderivedAnalogLiveDescription_Type()
)
pderivedAnalogLiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pderivedAnalogLiveDescription.setStatus("current")
_PderivedAnalogLiveLevel_Type = DescriptionString
_PderivedAnalogLiveLevel_Object = MibTableColumn
pderivedAnalogLiveLevel = _PderivedAnalogLiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 65),
    _PderivedAnalogLiveLevel_Type()
)
pderivedAnalogLiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pderivedAnalogLiveLevel.setStatus("current")
_PderivedAnalogLiveRaw_Type = DescriptionString
_PderivedAnalogLiveRaw_Object = MibTableColumn
pderivedAnalogLiveRaw = _PderivedAnalogLiveRaw_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 66),
    _PderivedAnalogLiveRaw_Type()
)
pderivedAnalogLiveRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pderivedAnalogLiveRaw.setStatus("current")
_PderivedAnalogLiveTime_Type = DescriptionString
_PderivedAnalogLiveTime_Object = MibTableColumn
pderivedAnalogLiveTime = _PderivedAnalogLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 67),
    _PderivedAnalogLiveTime_Type()
)
pderivedAnalogLiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pderivedAnalogLiveTime.setStatus("current")
_PderivedAnalogElementAPkg_Type = Integer32
_PderivedAnalogElementAPkg_Object = MibTableColumn
pderivedAnalogElementAPkg = _PderivedAnalogElementAPkg_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 90),
    _PderivedAnalogElementAPkg_Type()
)
pderivedAnalogElementAPkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogElementAPkg.setStatus("current")
_PderivedAnalogElementAPoint_Type = Integer32
_PderivedAnalogElementAPoint_Object = MibTableColumn
pderivedAnalogElementAPoint = _PderivedAnalogElementAPoint_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 91),
    _PderivedAnalogElementAPoint_Type()
)
pderivedAnalogElementAPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogElementAPoint.setStatus("current")
_PderivedAnalogElementBPkg_Type = Integer32
_PderivedAnalogElementBPkg_Object = MibTableColumn
pderivedAnalogElementBPkg = _PderivedAnalogElementBPkg_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 92),
    _PderivedAnalogElementBPkg_Type()
)
pderivedAnalogElementBPkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogElementBPkg.setStatus("current")
_PderivedAnalogElementBPoint_Type = Integer32
_PderivedAnalogElementBPoint_Object = MibTableColumn
pderivedAnalogElementBPoint = _PderivedAnalogElementBPoint_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 93),
    _PderivedAnalogElementBPoint_Type()
)
pderivedAnalogElementBPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogElementBPoint.setStatus("current")
_PderivedAnalogFormula_Type = DescriptionString
_PderivedAnalogFormula_Object = MibTableColumn
pderivedAnalogFormula = _PderivedAnalogFormula_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 95),
    _PderivedAnalogFormula_Type()
)
pderivedAnalogFormula.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogFormula.setStatus("current")
_PderivedAnalogTL1SID_Type = DescriptionString
_PderivedAnalogTL1SID_Object = MibTableColumn
pderivedAnalogTL1SID = _PderivedAnalogTL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 116),
    _PderivedAnalogTL1SID_Type()
)
pderivedAnalogTL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogTL1SID.setStatus("current")
_PderivedAnalogTL1COND_Type = DescriptionString
_PderivedAnalogTL1COND_Object = MibTableColumn
pderivedAnalogTL1COND = _PderivedAnalogTL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 117),
    _PderivedAnalogTL1COND_Type()
)
pderivedAnalogTL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogTL1COND.setStatus("current")
_PderivedAnalogTL1Eqpt_Type = DescriptionString
_PderivedAnalogTL1Eqpt_Object = MibTableColumn
pderivedAnalogTL1Eqpt = _PderivedAnalogTL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 118),
    _PderivedAnalogTL1Eqpt_Type()
)
pderivedAnalogTL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogTL1Eqpt.setStatus("current")
_PderivedAnalogTL1Env_Type = Boolean
_PderivedAnalogTL1Env_Object = MibTableColumn
pderivedAnalogTL1Env = _PderivedAnalogTL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 119),
    _PderivedAnalogTL1Env_Type()
)
pderivedAnalogTL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogTL1Env.setStatus("current")
_PderivedAnalogTL1Srveff_Type = TL1Srveff
_PderivedAnalogTL1Srveff_Object = MibTableColumn
pderivedAnalogTL1Srveff = _PderivedAnalogTL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 120),
    _PderivedAnalogTL1Srveff_Type()
)
pderivedAnalogTL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogTL1Srveff.setStatus("current")
_PderivedAnalogTL1Locn_Type = TL1Locn
_PderivedAnalogTL1Locn_Object = MibTableColumn
pderivedAnalogTL1Locn = _PderivedAnalogTL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 121),
    _PderivedAnalogTL1Locn_Type()
)
pderivedAnalogTL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogTL1Locn.setStatus("current")
_PderivedAnalogTL1Dirn_Type = TL1Dirn
_PderivedAnalogTL1Dirn_Object = MibTableColumn
pderivedAnalogTL1Dirn = _PderivedAnalogTL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 122),
    _PderivedAnalogTL1Dirn_Type()
)
pderivedAnalogTL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pderivedAnalogTL1Dirn.setStatus("current")


class _PderivedAnalogIndex_Type(Integer32):
    """Custom type pderivedAnalogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PderivedAnalogIndex_Type.__name__ = "Integer32"
_PderivedAnalogIndex_Object = MibTableColumn
pderivedAnalogIndex = _PderivedAnalogIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 33, 1, 999),
    _PderivedAnalogIndex_Type()
)
pderivedAnalogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pderivedAnalogIndex.setStatus("current")
_PgpsTable_Object = MibTable
pgpsTable = _PgpsTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34)
)
if mibBuilder.loadTexts:
    pgpsTable.setStatus("current")
_PgpsEntry_Object = MibTableRow
pgpsEntry = _PgpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1)
)
pgpsEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pgpsIndex"),
)
if mibBuilder.loadTexts:
    pgpsEntry.setStatus("current")
_PgpsDescription_Type = DescriptionString
_PgpsDescription_Object = MibTableColumn
pgpsDescription = _PgpsDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 3),
    _PgpsDescription_Type()
)
pgpsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgpsDescription.setStatus("current")
_PgpsDesc0_Type = DescriptionString
_PgpsDesc0_Object = MibTableColumn
pgpsDesc0 = _PgpsDesc0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 4),
    _PgpsDesc0_Type()
)
pgpsDesc0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsDesc0.setStatus("current")
_PgpsDesc1_Type = DescriptionString
_PgpsDesc1_Object = MibTableColumn
pgpsDesc1 = _PgpsDesc1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 5),
    _PgpsDesc1_Type()
)
pgpsDesc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsDesc1.setStatus("current")
_PgpsDesc2_Type = DescriptionString
_PgpsDesc2_Object = MibTableColumn
pgpsDesc2 = _PgpsDesc2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 6),
    _PgpsDesc2_Type()
)
pgpsDesc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsDesc2.setStatus("current")
_PgpsDesc3_Type = DescriptionString
_PgpsDesc3_Object = MibTableColumn
pgpsDesc3 = _PgpsDesc3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 7),
    _PgpsDesc3_Type()
)
pgpsDesc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsDesc3.setStatus("current")
_PgpsDesc4_Type = DescriptionString
_PgpsDesc4_Object = MibTableColumn
pgpsDesc4 = _PgpsDesc4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 8),
    _PgpsDesc4_Type()
)
pgpsDesc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsDesc4.setStatus("current")
_PgpsConfigured_Type = Configured
_PgpsConfigured_Object = MibTableColumn
pgpsConfigured = _PgpsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 10),
    _PgpsConfigured_Type()
)
pgpsConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsConfigured.setStatus("current")
_PgpsSendEmail_Type = Boolean
_PgpsSendEmail_Object = MibTableColumn
pgpsSendEmail = _PgpsSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 11),
    _PgpsSendEmail_Type()
)
pgpsSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsSendEmail.setStatus("current")
_PgpsSendSNMPTrap_Type = Boolean
_PgpsSendSNMPTrap_Object = MibTableColumn
pgpsSendSNMPTrap = _PgpsSendSNMPTrap_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 12),
    _PgpsSendSNMPTrap_Type()
)
pgpsSendSNMPTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsSendSNMPTrap.setStatus("current")
_PgpsLevel0_Type = Level
_PgpsLevel0_Object = MibTableColumn
pgpsLevel0 = _PgpsLevel0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 17),
    _PgpsLevel0_Type()
)
pgpsLevel0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsLevel0.setStatus("current")
_PgpsLevel1_Type = Level
_PgpsLevel1_Object = MibTableColumn
pgpsLevel1 = _PgpsLevel1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 18),
    _PgpsLevel1_Type()
)
pgpsLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsLevel1.setStatus("current")
_PgpsLevel2_Type = Level
_PgpsLevel2_Object = MibTableColumn
pgpsLevel2 = _PgpsLevel2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 19),
    _PgpsLevel2_Type()
)
pgpsLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsLevel2.setStatus("current")
_PgpsLevel3_Type = Level
_PgpsLevel3_Object = MibTableColumn
pgpsLevel3 = _PgpsLevel3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 20),
    _PgpsLevel3_Type()
)
pgpsLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsLevel3.setStatus("current")
_PgpsLevel4_Type = Level
_PgpsLevel4_Object = MibTableColumn
pgpsLevel4 = _PgpsLevel4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 21),
    _PgpsLevel4_Type()
)
pgpsLevel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsLevel4.setStatus("current")
_PgpsThresh0_Type = DescriptionString
_PgpsThresh0_Object = MibTableColumn
pgpsThresh0 = _PgpsThresh0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 28),
    _PgpsThresh0_Type()
)
pgpsThresh0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgpsThresh0.setStatus("current")
_PgpsThresh1_Type = DescriptionString
_PgpsThresh1_Object = MibTableColumn
pgpsThresh1 = _PgpsThresh1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 29),
    _PgpsThresh1_Type()
)
pgpsThresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsThresh1.setStatus("current")
_PgpsThresh2_Type = DescriptionString
_PgpsThresh2_Object = MibTableColumn
pgpsThresh2 = _PgpsThresh2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 30),
    _PgpsThresh2_Type()
)
pgpsThresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsThresh2.setStatus("current")
_PgpsThresh3_Type = DescriptionString
_PgpsThresh3_Object = MibTableColumn
pgpsThresh3 = _PgpsThresh3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 31),
    _PgpsThresh3_Type()
)
pgpsThresh3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsThresh3.setStatus("current")
_PgpsThresh4_Type = DescriptionString
_PgpsThresh4_Object = MibTableColumn
pgpsThresh4 = _PgpsThresh4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 32),
    _PgpsThresh4_Type()
)
pgpsThresh4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsThresh4.setStatus("current")
_PgpsThresh5_Type = DescriptionString
_PgpsThresh5_Object = MibTableColumn
pgpsThresh5 = _PgpsThresh5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 33),
    _PgpsThresh5_Type()
)
pgpsThresh5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgpsThresh5.setStatus("current")
_PgpsUnits_Type = DescriptionString
_PgpsUnits_Object = MibTableColumn
pgpsUnits = _PgpsUnits_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 46),
    _PgpsUnits_Type()
)
pgpsUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgpsUnits.setStatus("current")
_PgpsLiveDescription_Type = DescriptionString
_PgpsLiveDescription_Object = MibTableColumn
pgpsLiveDescription = _PgpsLiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 64),
    _PgpsLiveDescription_Type()
)
pgpsLiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgpsLiveDescription.setStatus("current")
_PgpsLiveLevel_Type = DescriptionString
_PgpsLiveLevel_Object = MibTableColumn
pgpsLiveLevel = _PgpsLiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 65),
    _PgpsLiveLevel_Type()
)
pgpsLiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgpsLiveLevel.setStatus("current")
_PgpsLiveRaw_Type = DescriptionString
_PgpsLiveRaw_Object = MibTableColumn
pgpsLiveRaw = _PgpsLiveRaw_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 66),
    _PgpsLiveRaw_Type()
)
pgpsLiveRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgpsLiveRaw.setStatus("current")
_PgpsLiveTime_Type = DescriptionString
_PgpsLiveTime_Object = MibTableColumn
pgpsLiveTime = _PgpsLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 67),
    _PgpsLiveTime_Type()
)
pgpsLiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgpsLiveTime.setStatus("current")
_PgpsTL1SID_Type = DescriptionString
_PgpsTL1SID_Object = MibTableColumn
pgpsTL1SID = _PgpsTL1SID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 116),
    _PgpsTL1SID_Type()
)
pgpsTL1SID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsTL1SID.setStatus("current")
_PgpsTL1COND_Type = DescriptionString
_PgpsTL1COND_Object = MibTableColumn
pgpsTL1COND = _PgpsTL1COND_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 117),
    _PgpsTL1COND_Type()
)
pgpsTL1COND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsTL1COND.setStatus("current")
_PgpsTL1Eqpt_Type = DescriptionString
_PgpsTL1Eqpt_Object = MibTableColumn
pgpsTL1Eqpt = _PgpsTL1Eqpt_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 118),
    _PgpsTL1Eqpt_Type()
)
pgpsTL1Eqpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsTL1Eqpt.setStatus("current")
_PgpsTL1Env_Type = Boolean
_PgpsTL1Env_Object = MibTableColumn
pgpsTL1Env = _PgpsTL1Env_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 119),
    _PgpsTL1Env_Type()
)
pgpsTL1Env.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsTL1Env.setStatus("current")
_PgpsTL1Srveff_Type = TL1Srveff
_PgpsTL1Srveff_Object = MibTableColumn
pgpsTL1Srveff = _PgpsTL1Srveff_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 120),
    _PgpsTL1Srveff_Type()
)
pgpsTL1Srveff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsTL1Srveff.setStatus("current")
_PgpsTL1Locn_Type = TL1Locn
_PgpsTL1Locn_Object = MibTableColumn
pgpsTL1Locn = _PgpsTL1Locn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 121),
    _PgpsTL1Locn_Type()
)
pgpsTL1Locn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsTL1Locn.setStatus("current")
_PgpsTL1Dirn_Type = TL1Dirn
_PgpsTL1Dirn_Object = MibTableColumn
pgpsTL1Dirn = _PgpsTL1Dirn_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 122),
    _PgpsTL1Dirn_Type()
)
pgpsTL1Dirn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgpsTL1Dirn.setStatus("current")


class _PgpsIndex_Type(Integer32):
    """Custom type pgpsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PgpsIndex_Type.__name__ = "Integer32"
_PgpsIndex_Object = MibTableColumn
pgpsIndex = _PgpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 34, 1, 999),
    _PgpsIndex_Type()
)
pgpsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgpsIndex.setStatus("current")
_PportRedirectTable_Object = MibTable
pportRedirectTable = _PportRedirectTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 35)
)
if mibBuilder.loadTexts:
    pportRedirectTable.setStatus("current")
_PportRedirectEntry_Object = MibTableRow
pportRedirectEntry = _PportRedirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 35, 1)
)
pportRedirectEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pportRedirectIndex"),
)
if mibBuilder.loadTexts:
    pportRedirectEntry.setStatus("current")
_PportRedirectDescription_Type = DescriptionString
_PportRedirectDescription_Object = MibTableColumn
pportRedirectDescription = _PportRedirectDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 35, 1, 3),
    _PportRedirectDescription_Type()
)
pportRedirectDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportRedirectDescription.setStatus("current")
_PportRedirectConfigured_Type = Configured
_PportRedirectConfigured_Object = MibTableColumn
pportRedirectConfigured = _PportRedirectConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 35, 1, 10),
    _PportRedirectConfigured_Type()
)
pportRedirectConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportRedirectConfigured.setStatus("current")
_PportRedirectIpAddress_Type = IpAddress
_PportRedirectIpAddress_Object = MibTableColumn
pportRedirectIpAddress = _PportRedirectIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 35, 1, 14),
    _PportRedirectIpAddress_Type()
)
pportRedirectIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportRedirectIpAddress.setStatus("current")
_PportRedirectReadPeriod_Type = Integer32
_PportRedirectReadPeriod_Object = MibTableColumn
pportRedirectReadPeriod = _PportRedirectReadPeriod_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 35, 1, 23),
    _PportRedirectReadPeriod_Type()
)
pportRedirectReadPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportRedirectReadPeriod.setStatus("current")
_PportRedirectRosterID_Type = Integer32
_PportRedirectRosterID_Object = MibTableColumn
pportRedirectRosterID = _PportRedirectRosterID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 35, 1, 37),
    _PportRedirectRosterID_Type()
)
pportRedirectRosterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportRedirectRosterID.setStatus("current")
_PportRedirectIPPortNum_Type = Integer32
_PportRedirectIPPortNum_Object = MibTableColumn
pportRedirectIPPortNum = _PportRedirectIPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 35, 1, 73),
    _PportRedirectIPPortNum_Type()
)
pportRedirectIPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pportRedirectIPPortNum.setStatus("current")


class _PportRedirectIndex_Type(Integer32):
    """Custom type pportRedirectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PportRedirectIndex_Type.__name__ = "Integer32"
_PportRedirectIndex_Object = MibTableColumn
pportRedirectIndex = _PportRedirectIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 35, 1, 999),
    _PportRedirectIndex_Type()
)
pportRedirectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pportRedirectIndex.setStatus("current")
_PscheduleATable_Object = MibTable
pscheduleATable = _PscheduleATable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36)
)
if mibBuilder.loadTexts:
    pscheduleATable.setStatus("current")
_PscheduleAEntry_Object = MibTableRow
pscheduleAEntry = _PscheduleAEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1)
)
pscheduleAEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pscheduleAIndex"),
)
if mibBuilder.loadTexts:
    pscheduleAEntry.setStatus("current")
_PscheduleADayOfWeek_Type = DayOfWeek
_PscheduleADayOfWeek_Object = MibTableColumn
pscheduleADayOfWeek = _PscheduleADayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 102),
    _PscheduleADayOfWeek_Type()
)
pscheduleADayOfWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleADayOfWeek.setStatus("current")
_PscheduleAConfiguredState_Type = ConfiguredState
_PscheduleAConfiguredState_Object = MibTableColumn
pscheduleAConfiguredState = _PscheduleAConfiguredState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 103),
    _PscheduleAConfiguredState_Type()
)
pscheduleAConfiguredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleAConfiguredState.setStatus("current")
_PscheduleAConfigured1_Type = ConfiguredState
_PscheduleAConfigured1_Object = MibTableColumn
pscheduleAConfigured1 = _PscheduleAConfigured1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 104),
    _PscheduleAConfigured1_Type()
)
pscheduleAConfigured1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleAConfigured1.setStatus("current")
_PscheduleAConfigured2_Type = ConfiguredState
_PscheduleAConfigured2_Object = MibTableColumn
pscheduleAConfigured2 = _PscheduleAConfigured2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 105),
    _PscheduleAConfigured2_Type()
)
pscheduleAConfigured2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleAConfigured2.setStatus("current")
_PscheduleAConfigured3_Type = ConfiguredState
_PscheduleAConfigured3_Object = MibTableColumn
pscheduleAConfigured3 = _PscheduleAConfigured3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 106),
    _PscheduleAConfigured3_Type()
)
pscheduleAConfigured3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleAConfigured3.setStatus("current")
_PscheduleAConfigured4_Type = ConfiguredState
_PscheduleAConfigured4_Object = MibTableColumn
pscheduleAConfigured4 = _PscheduleAConfigured4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 107),
    _PscheduleAConfigured4_Type()
)
pscheduleAConfigured4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleAConfigured4.setStatus("current")
_PscheduleATime0_Type = DescriptionString
_PscheduleATime0_Object = MibTableColumn
pscheduleATime0 = _PscheduleATime0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 108),
    _PscheduleATime0_Type()
)
pscheduleATime0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleATime0.setStatus("current")
_PscheduleATime1_Type = DescriptionString
_PscheduleATime1_Object = MibTableColumn
pscheduleATime1 = _PscheduleATime1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 109),
    _PscheduleATime1_Type()
)
pscheduleATime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleATime1.setStatus("current")
_PscheduleATime2_Type = DescriptionString
_PscheduleATime2_Object = MibTableColumn
pscheduleATime2 = _PscheduleATime2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 110),
    _PscheduleATime2_Type()
)
pscheduleATime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleATime2.setStatus("current")
_PscheduleATime3_Type = DescriptionString
_PscheduleATime3_Object = MibTableColumn
pscheduleATime3 = _PscheduleATime3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 111),
    _PscheduleATime3_Type()
)
pscheduleATime3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleATime3.setStatus("current")
_PscheduleATime4_Type = DescriptionString
_PscheduleATime4_Object = MibTableColumn
pscheduleATime4 = _PscheduleATime4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 112),
    _PscheduleATime4_Type()
)
pscheduleATime4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleATime4.setStatus("current")
_PscheduleATime5_Type = DescriptionString
_PscheduleATime5_Object = MibTableColumn
pscheduleATime5 = _PscheduleATime5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 113),
    _PscheduleATime5_Type()
)
pscheduleATime5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleATime5.setStatus("current")


class _PscheduleAIndex_Type(Integer32):
    """Custom type pscheduleAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PscheduleAIndex_Type.__name__ = "Integer32"
_PscheduleAIndex_Object = MibTableColumn
pscheduleAIndex = _PscheduleAIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 36, 1, 999),
    _PscheduleAIndex_Type()
)
pscheduleAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleAIndex.setStatus("current")
_PscheduleBTable_Object = MibTable
pscheduleBTable = _PscheduleBTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37)
)
if mibBuilder.loadTexts:
    pscheduleBTable.setStatus("current")
_PscheduleBEntry_Object = MibTableRow
pscheduleBEntry = _PscheduleBEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1)
)
pscheduleBEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pscheduleBIndex"),
)
if mibBuilder.loadTexts:
    pscheduleBEntry.setStatus("current")
_PscheduleBDayOfWeek_Type = DayOfWeek
_PscheduleBDayOfWeek_Object = MibTableColumn
pscheduleBDayOfWeek = _PscheduleBDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 102),
    _PscheduleBDayOfWeek_Type()
)
pscheduleBDayOfWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleBDayOfWeek.setStatus("current")
_PscheduleBConfiguredState_Type = ConfiguredState
_PscheduleBConfiguredState_Object = MibTableColumn
pscheduleBConfiguredState = _PscheduleBConfiguredState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 103),
    _PscheduleBConfiguredState_Type()
)
pscheduleBConfiguredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleBConfiguredState.setStatus("current")
_PscheduleBConfigured1_Type = ConfiguredState
_PscheduleBConfigured1_Object = MibTableColumn
pscheduleBConfigured1 = _PscheduleBConfigured1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 104),
    _PscheduleBConfigured1_Type()
)
pscheduleBConfigured1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleBConfigured1.setStatus("current")
_PscheduleBConfigured2_Type = ConfiguredState
_PscheduleBConfigured2_Object = MibTableColumn
pscheduleBConfigured2 = _PscheduleBConfigured2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 105),
    _PscheduleBConfigured2_Type()
)
pscheduleBConfigured2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleBConfigured2.setStatus("current")
_PscheduleBConfigured3_Type = ConfiguredState
_PscheduleBConfigured3_Object = MibTableColumn
pscheduleBConfigured3 = _PscheduleBConfigured3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 106),
    _PscheduleBConfigured3_Type()
)
pscheduleBConfigured3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleBConfigured3.setStatus("current")
_PscheduleBConfigured4_Type = ConfiguredState
_PscheduleBConfigured4_Object = MibTableColumn
pscheduleBConfigured4 = _PscheduleBConfigured4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 107),
    _PscheduleBConfigured4_Type()
)
pscheduleBConfigured4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleBConfigured4.setStatus("current")
_PscheduleBTime0_Type = DescriptionString
_PscheduleBTime0_Object = MibTableColumn
pscheduleBTime0 = _PscheduleBTime0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 108),
    _PscheduleBTime0_Type()
)
pscheduleBTime0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleBTime0.setStatus("current")
_PscheduleBTime1_Type = DescriptionString
_PscheduleBTime1_Object = MibTableColumn
pscheduleBTime1 = _PscheduleBTime1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 109),
    _PscheduleBTime1_Type()
)
pscheduleBTime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleBTime1.setStatus("current")
_PscheduleBTime2_Type = DescriptionString
_PscheduleBTime2_Object = MibTableColumn
pscheduleBTime2 = _PscheduleBTime2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 110),
    _PscheduleBTime2_Type()
)
pscheduleBTime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleBTime2.setStatus("current")
_PscheduleBTime3_Type = DescriptionString
_PscheduleBTime3_Object = MibTableColumn
pscheduleBTime3 = _PscheduleBTime3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 111),
    _PscheduleBTime3_Type()
)
pscheduleBTime3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleBTime3.setStatus("current")
_PscheduleBTime4_Type = DescriptionString
_PscheduleBTime4_Object = MibTableColumn
pscheduleBTime4 = _PscheduleBTime4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 112),
    _PscheduleBTime4_Type()
)
pscheduleBTime4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleBTime4.setStatus("current")
_PscheduleBTime5_Type = DescriptionString
_PscheduleBTime5_Object = MibTableColumn
pscheduleBTime5 = _PscheduleBTime5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 113),
    _PscheduleBTime5_Type()
)
pscheduleBTime5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleBTime5.setStatus("current")


class _PscheduleBIndex_Type(Integer32):
    """Custom type pscheduleBIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PscheduleBIndex_Type.__name__ = "Integer32"
_PscheduleBIndex_Object = MibTableColumn
pscheduleBIndex = _PscheduleBIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 37, 1, 999),
    _PscheduleBIndex_Type()
)
pscheduleBIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleBIndex.setStatus("current")
_PscheduleCTable_Object = MibTable
pscheduleCTable = _PscheduleCTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38)
)
if mibBuilder.loadTexts:
    pscheduleCTable.setStatus("current")
_PscheduleCEntry_Object = MibTableRow
pscheduleCEntry = _PscheduleCEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1)
)
pscheduleCEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pscheduleCIndex"),
)
if mibBuilder.loadTexts:
    pscheduleCEntry.setStatus("current")
_PscheduleCDayOfWeek_Type = DayOfWeek
_PscheduleCDayOfWeek_Object = MibTableColumn
pscheduleCDayOfWeek = _PscheduleCDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 102),
    _PscheduleCDayOfWeek_Type()
)
pscheduleCDayOfWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleCDayOfWeek.setStatus("current")
_PscheduleCConfiguredState_Type = ConfiguredState
_PscheduleCConfiguredState_Object = MibTableColumn
pscheduleCConfiguredState = _PscheduleCConfiguredState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 103),
    _PscheduleCConfiguredState_Type()
)
pscheduleCConfiguredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleCConfiguredState.setStatus("current")
_PscheduleCConfigured1_Type = ConfiguredState
_PscheduleCConfigured1_Object = MibTableColumn
pscheduleCConfigured1 = _PscheduleCConfigured1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 104),
    _PscheduleCConfigured1_Type()
)
pscheduleCConfigured1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleCConfigured1.setStatus("current")
_PscheduleCConfigured2_Type = ConfiguredState
_PscheduleCConfigured2_Object = MibTableColumn
pscheduleCConfigured2 = _PscheduleCConfigured2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 105),
    _PscheduleCConfigured2_Type()
)
pscheduleCConfigured2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleCConfigured2.setStatus("current")
_PscheduleCConfigured3_Type = ConfiguredState
_PscheduleCConfigured3_Object = MibTableColumn
pscheduleCConfigured3 = _PscheduleCConfigured3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 106),
    _PscheduleCConfigured3_Type()
)
pscheduleCConfigured3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleCConfigured3.setStatus("current")
_PscheduleCConfigured4_Type = ConfiguredState
_PscheduleCConfigured4_Object = MibTableColumn
pscheduleCConfigured4 = _PscheduleCConfigured4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 107),
    _PscheduleCConfigured4_Type()
)
pscheduleCConfigured4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleCConfigured4.setStatus("current")
_PscheduleCTime0_Type = DescriptionString
_PscheduleCTime0_Object = MibTableColumn
pscheduleCTime0 = _PscheduleCTime0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 108),
    _PscheduleCTime0_Type()
)
pscheduleCTime0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleCTime0.setStatus("current")
_PscheduleCTime1_Type = DescriptionString
_PscheduleCTime1_Object = MibTableColumn
pscheduleCTime1 = _PscheduleCTime1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 109),
    _PscheduleCTime1_Type()
)
pscheduleCTime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleCTime1.setStatus("current")
_PscheduleCTime2_Type = DescriptionString
_PscheduleCTime2_Object = MibTableColumn
pscheduleCTime2 = _PscheduleCTime2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 110),
    _PscheduleCTime2_Type()
)
pscheduleCTime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleCTime2.setStatus("current")
_PscheduleCTime3_Type = DescriptionString
_PscheduleCTime3_Object = MibTableColumn
pscheduleCTime3 = _PscheduleCTime3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 111),
    _PscheduleCTime3_Type()
)
pscheduleCTime3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleCTime3.setStatus("current")
_PscheduleCTime4_Type = DescriptionString
_PscheduleCTime4_Object = MibTableColumn
pscheduleCTime4 = _PscheduleCTime4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 112),
    _PscheduleCTime4_Type()
)
pscheduleCTime4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleCTime4.setStatus("current")
_PscheduleCTime5_Type = DescriptionString
_PscheduleCTime5_Object = MibTableColumn
pscheduleCTime5 = _PscheduleCTime5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 113),
    _PscheduleCTime5_Type()
)
pscheduleCTime5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleCTime5.setStatus("current")


class _PscheduleCIndex_Type(Integer32):
    """Custom type pscheduleCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PscheduleCIndex_Type.__name__ = "Integer32"
_PscheduleCIndex_Object = MibTableColumn
pscheduleCIndex = _PscheduleCIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 38, 1, 999),
    _PscheduleCIndex_Type()
)
pscheduleCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleCIndex.setStatus("current")
_PscheduleDTable_Object = MibTable
pscheduleDTable = _PscheduleDTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39)
)
if mibBuilder.loadTexts:
    pscheduleDTable.setStatus("current")
_PscheduleDEntry_Object = MibTableRow
pscheduleDEntry = _PscheduleDEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1)
)
pscheduleDEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pscheduleDIndex"),
)
if mibBuilder.loadTexts:
    pscheduleDEntry.setStatus("current")
_PscheduleDDayOfWeek_Type = DayOfWeek
_PscheduleDDayOfWeek_Object = MibTableColumn
pscheduleDDayOfWeek = _PscheduleDDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 102),
    _PscheduleDDayOfWeek_Type()
)
pscheduleDDayOfWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleDDayOfWeek.setStatus("current")
_PscheduleDConfiguredState_Type = ConfiguredState
_PscheduleDConfiguredState_Object = MibTableColumn
pscheduleDConfiguredState = _PscheduleDConfiguredState_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 103),
    _PscheduleDConfiguredState_Type()
)
pscheduleDConfiguredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleDConfiguredState.setStatus("current")
_PscheduleDConfigured1_Type = ConfiguredState
_PscheduleDConfigured1_Object = MibTableColumn
pscheduleDConfigured1 = _PscheduleDConfigured1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 104),
    _PscheduleDConfigured1_Type()
)
pscheduleDConfigured1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleDConfigured1.setStatus("current")
_PscheduleDConfigured2_Type = ConfiguredState
_PscheduleDConfigured2_Object = MibTableColumn
pscheduleDConfigured2 = _PscheduleDConfigured2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 105),
    _PscheduleDConfigured2_Type()
)
pscheduleDConfigured2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleDConfigured2.setStatus("current")
_PscheduleDConfigured3_Type = ConfiguredState
_PscheduleDConfigured3_Object = MibTableColumn
pscheduleDConfigured3 = _PscheduleDConfigured3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 106),
    _PscheduleDConfigured3_Type()
)
pscheduleDConfigured3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleDConfigured3.setStatus("current")
_PscheduleDConfigured4_Type = ConfiguredState
_PscheduleDConfigured4_Object = MibTableColumn
pscheduleDConfigured4 = _PscheduleDConfigured4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 107),
    _PscheduleDConfigured4_Type()
)
pscheduleDConfigured4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleDConfigured4.setStatus("current")
_PscheduleDTime0_Type = DescriptionString
_PscheduleDTime0_Object = MibTableColumn
pscheduleDTime0 = _PscheduleDTime0_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 108),
    _PscheduleDTime0_Type()
)
pscheduleDTime0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleDTime0.setStatus("current")
_PscheduleDTime1_Type = DescriptionString
_PscheduleDTime1_Object = MibTableColumn
pscheduleDTime1 = _PscheduleDTime1_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 109),
    _PscheduleDTime1_Type()
)
pscheduleDTime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleDTime1.setStatus("current")
_PscheduleDTime2_Type = DescriptionString
_PscheduleDTime2_Object = MibTableColumn
pscheduleDTime2 = _PscheduleDTime2_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 110),
    _PscheduleDTime2_Type()
)
pscheduleDTime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleDTime2.setStatus("current")
_PscheduleDTime3_Type = DescriptionString
_PscheduleDTime3_Object = MibTableColumn
pscheduleDTime3 = _PscheduleDTime3_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 111),
    _PscheduleDTime3_Type()
)
pscheduleDTime3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleDTime3.setStatus("current")
_PscheduleDTime4_Type = DescriptionString
_PscheduleDTime4_Object = MibTableColumn
pscheduleDTime4 = _PscheduleDTime4_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 112),
    _PscheduleDTime4_Type()
)
pscheduleDTime4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pscheduleDTime4.setStatus("current")
_PscheduleDTime5_Type = DescriptionString
_PscheduleDTime5_Object = MibTableColumn
pscheduleDTime5 = _PscheduleDTime5_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 113),
    _PscheduleDTime5_Type()
)
pscheduleDTime5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleDTime5.setStatus("current")


class _PscheduleDIndex_Type(Integer32):
    """Custom type pscheduleDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PscheduleDIndex_Type.__name__ = "Integer32"
_PscheduleDIndex_Object = MibTableColumn
pscheduleDIndex = _PscheduleDIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 39, 1, 999),
    _PscheduleDIndex_Type()
)
pscheduleDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pscheduleDIndex.setStatus("current")
_Tl1Settings_ObjectIdentity = ObjectIdentity
tl1Settings = _Tl1Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 40)
)
_Tl1SettingsTL1Issue_Type = TL1Issue
_Tl1SettingsTL1Issue_Object = MibScalar
tl1SettingsTL1Issue = _Tl1SettingsTL1Issue_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 40, 123),
    _Tl1SettingsTL1Issue_Type()
)
tl1SettingsTL1Issue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tl1SettingsTL1Issue.setStatus("current")
_PDCPFProtocolTable_Object = MibTable
pDCPFProtocolTable = _PDCPFProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 41)
)
if mibBuilder.loadTexts:
    pDCPFProtocolTable.setStatus("current")
_PDCPFProtocolEntry_Object = MibTableRow
pDCPFProtocolEntry = _PDCPFProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 41, 1)
)
pDCPFProtocolEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pDCPFProtocolIndex"),
)
if mibBuilder.loadTexts:
    pDCPFProtocolEntry.setStatus("current")
_PDCPFProtocolDescription_Type = DescriptionString
_PDCPFProtocolDescription_Object = MibTableColumn
pDCPFProtocolDescription = _PDCPFProtocolDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 41, 1, 3),
    _PDCPFProtocolDescription_Type()
)
pDCPFProtocolDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDCPFProtocolDescription.setStatus("current")
_PDCPFProtocolConfigured_Type = Configured
_PDCPFProtocolConfigured_Object = MibTableColumn
pDCPFProtocolConfigured = _PDCPFProtocolConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 41, 1, 10),
    _PDCPFProtocolConfigured_Type()
)
pDCPFProtocolConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pDCPFProtocolConfigured.setStatus("current")
_PDCPFProtocolBaseDCPFDisplay_Type = Integer32
_PDCPFProtocolBaseDCPFDisplay_Object = MibTableColumn
pDCPFProtocolBaseDCPFDisplay = _PDCPFProtocolBaseDCPFDisplay_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 41, 1, 127),
    _PDCPFProtocolBaseDCPFDisplay_Type()
)
pDCPFProtocolBaseDCPFDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pDCPFProtocolBaseDCPFDisplay.setStatus("current")


class _PDCPFProtocolIndex_Type(Integer32):
    """Custom type pDCPFProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 27),
    )


_PDCPFProtocolIndex_Type.__name__ = "Integer32"
_PDCPFProtocolIndex_Object = MibTableColumn
pDCPFProtocolIndex = _PDCPFProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 41, 1, 999),
    _PDCPFProtocolIndex_Type()
)
pDCPFProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDCPFProtocolIndex.setStatus("current")
_DcpfSettings_ObjectIdentity = ObjectIdentity
dcpfSettings = _DcpfSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 42)
)
_DcpfSettingsDCPFAddress_Type = Integer32
_DcpfSettingsDCPFAddress_Object = MibScalar
dcpfSettingsDCPFAddress = _DcpfSettingsDCPFAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 42, 128),
    _DcpfSettingsDCPFAddress_Type()
)
dcpfSettingsDCPFAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcpfSettingsDCPFAddress.setStatus("current")
_PTABSProtocolTable_Object = MibTable
pTABSProtocolTable = _PTABSProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 43)
)
if mibBuilder.loadTexts:
    pTABSProtocolTable.setStatus("current")
_PTABSProtocolEntry_Object = MibTableRow
pTABSProtocolEntry = _PTABSProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 43, 1)
)
pTABSProtocolEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pTABSProtocolIndex"),
)
if mibBuilder.loadTexts:
    pTABSProtocolEntry.setStatus("current")
_PTABSProtocolDescription_Type = DescriptionString
_PTABSProtocolDescription_Object = MibTableColumn
pTABSProtocolDescription = _PTABSProtocolDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 43, 1, 3),
    _PTABSProtocolDescription_Type()
)
pTABSProtocolDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTABSProtocolDescription.setStatus("current")
_PTABSProtocolConfigured_Type = Configured
_PTABSProtocolConfigured_Object = MibTableColumn
pTABSProtocolConfigured = _PTABSProtocolConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 43, 1, 10),
    _PTABSProtocolConfigured_Type()
)
pTABSProtocolConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTABSProtocolConfigured.setStatus("current")
_PTABSProtocolBaseTABSDisplay_Type = Integer32
_PTABSProtocolBaseTABSDisplay_Object = MibTableColumn
pTABSProtocolBaseTABSDisplay = _PTABSProtocolBaseTABSDisplay_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 43, 1, 129),
    _PTABSProtocolBaseTABSDisplay_Type()
)
pTABSProtocolBaseTABSDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pTABSProtocolBaseTABSDisplay.setStatus("current")


class _PTABSProtocolIndex_Type(Integer32):
    """Custom type pTABSProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 27),
    )


_PTABSProtocolIndex_Type.__name__ = "Integer32"
_PTABSProtocolIndex_Object = MibTableColumn
pTABSProtocolIndex = _PTABSProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 43, 1, 999),
    _PTABSProtocolIndex_Type()
)
pTABSProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTABSProtocolIndex.setStatus("current")
_TabsSettings_ObjectIdentity = ObjectIdentity
tabsSettings = _TabsSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 44)
)
_TabsSettingsTABSAddress_Type = Integer32
_TabsSettingsTABSAddress_Object = MibScalar
tabsSettingsTABSAddress = _TabsSettingsTABSAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 44, 130),
    _TabsSettingsTABSAddress_Type()
)
tabsSettingsTABSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tabsSettingsTABSAddress.setStatus("current")
_PsnmpCommandsTable_Object = MibTable
psnmpCommandsTable = _PsnmpCommandsTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45)
)
if mibBuilder.loadTexts:
    psnmpCommandsTable.setStatus("current")
_PsnmpCommandsEntry_Object = MibTableRow
psnmpCommandsEntry = _PsnmpCommandsEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1)
)
psnmpCommandsEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsIndex"),
)
if mibBuilder.loadTexts:
    psnmpCommandsEntry.setStatus("current")
_PsnmpCommandsDescription_Type = DescriptionString
_PsnmpCommandsDescription_Object = MibTableColumn
psnmpCommandsDescription = _PsnmpCommandsDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 3),
    _PsnmpCommandsDescription_Type()
)
psnmpCommandsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsDescription.setStatus("current")
_PsnmpCommandsConfigured_Type = Configured
_PsnmpCommandsConfigured_Object = MibTableColumn
psnmpCommandsConfigured = _PsnmpCommandsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 10),
    _PsnmpCommandsConfigured_Type()
)
psnmpCommandsConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsConfigured.setStatus("current")
_PsnmpCommandsIpAddress_Type = IpAddress
_PsnmpCommandsIpAddress_Object = MibTableColumn
psnmpCommandsIpAddress = _PsnmpCommandsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 14),
    _PsnmpCommandsIpAddress_Type()
)
psnmpCommandsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsIpAddress.setStatus("current")
_PsnmpCommandsGet_Type = DescriptionString
_PsnmpCommandsGet_Object = MibTableColumn
psnmpCommandsGet = _PsnmpCommandsGet_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 39),
    _PsnmpCommandsGet_Type()
)
psnmpCommandsGet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsGet.setStatus("current")
_PsnmpCommandsSnmpVersion_Type = SnmpVersion
_PsnmpCommandsSnmpVersion_Object = MibTableColumn
psnmpCommandsSnmpVersion = _PsnmpCommandsSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 42),
    _PsnmpCommandsSnmpVersion_Type()
)
psnmpCommandsSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsSnmpVersion.setStatus("current")
_PsnmpCommandsOutputAuto_Type = Integer32
_PsnmpCommandsOutputAuto_Object = MibTableColumn
psnmpCommandsOutputAuto = _PsnmpCommandsOutputAuto_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 49),
    _PsnmpCommandsOutputAuto_Type()
)
psnmpCommandsOutputAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsOutputAuto.setStatus("current")
_PsnmpCommandsOutputAutoPkg_Type = Integer32
_PsnmpCommandsOutputAutoPkg_Object = MibTableColumn
psnmpCommandsOutputAutoPkg = _PsnmpCommandsOutputAutoPkg_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 71),
    _PsnmpCommandsOutputAutoPkg_Type()
)
psnmpCommandsOutputAutoPkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsOutputAutoPkg.setStatus("current")
_PsnmpCommandsIPPortNum_Type = Integer32
_PsnmpCommandsIPPortNum_Object = MibTableColumn
psnmpCommandsIPPortNum = _PsnmpCommandsIPPortNum_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 73),
    _PsnmpCommandsIPPortNum_Type()
)
psnmpCommandsIPPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsIPPortNum.setStatus("current")
_PsnmpCommandsOID_Type = DescriptionString
_PsnmpCommandsOID_Object = MibTableColumn
psnmpCommandsOID = _PsnmpCommandsOID_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 132),
    _PsnmpCommandsOID_Type()
)
psnmpCommandsOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsOID.setStatus("current")
_PsnmpCommandsSNMPVarbindType_Type = SNMPVarbindType
_PsnmpCommandsSNMPVarbindType_Object = MibTableColumn
psnmpCommandsSNMPVarbindType = _PsnmpCommandsSNMPVarbindType_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 134),
    _PsnmpCommandsSNMPVarbindType_Type()
)
psnmpCommandsSNMPVarbindType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsSNMPVarbindType.setStatus("current")
_PsnmpCommandsTextNormal_Type = DescriptionString
_PsnmpCommandsTextNormal_Object = MibTableColumn
psnmpCommandsTextNormal = _PsnmpCommandsTextNormal_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 135),
    _PsnmpCommandsTextNormal_Type()
)
psnmpCommandsTextNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsTextNormal.setStatus("current")
_PsnmpCommandsTextCritical_Type = DescriptionString
_PsnmpCommandsTextCritical_Object = MibTableColumn
psnmpCommandsTextCritical = _PsnmpCommandsTextCritical_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 136),
    _PsnmpCommandsTextCritical_Type()
)
psnmpCommandsTextCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsTextCritical.setStatus("current")
_PsnmpCommandsTextMajor_Type = DescriptionString
_PsnmpCommandsTextMajor_Object = MibTableColumn
psnmpCommandsTextMajor = _PsnmpCommandsTextMajor_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 137),
    _PsnmpCommandsTextMajor_Type()
)
psnmpCommandsTextMajor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsTextMajor.setStatus("current")
_PsnmpCommandsTextMinor_Type = DescriptionString
_PsnmpCommandsTextMinor_Object = MibTableColumn
psnmpCommandsTextMinor = _PsnmpCommandsTextMinor_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 138),
    _PsnmpCommandsTextMinor_Type()
)
psnmpCommandsTextMinor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsTextMinor.setStatus("current")
_PsnmpCommandsTextStatus_Type = DescriptionString
_PsnmpCommandsTextStatus_Object = MibTableColumn
psnmpCommandsTextStatus = _PsnmpCommandsTextStatus_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 139),
    _PsnmpCommandsTextStatus_Type()
)
psnmpCommandsTextStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psnmpCommandsTextStatus.setStatus("current")


class _PsnmpCommandsIndex_Type(Integer32):
    """Custom type psnmpCommandsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PsnmpCommandsIndex_Type.__name__ = "Integer32"
_PsnmpCommandsIndex_Object = MibTableColumn
psnmpCommandsIndex = _PsnmpCommandsIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 45, 1, 999),
    _PsnmpCommandsIndex_Type()
)
psnmpCommandsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psnmpCommandsIndex.setStatus("current")
_BattMon_ObjectIdentity = ObjectIdentity
battMon = _BattMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 46)
)
_BattMonConfigured_Type = Configured
_BattMonConfigured_Object = MibScalar
battMonConfigured = _BattMonConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 46, 10),
    _BattMonConfigured_Type()
)
battMonConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battMonConfigured.setStatus("current")
_BattMonOutputAuto_Type = Integer32
_BattMonOutputAuto_Object = MibScalar
battMonOutputAuto = _BattMonOutputAuto_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 46, 49),
    _BattMonOutputAuto_Type()
)
battMonOutputAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battMonOutputAuto.setStatus("current")
_BattMonOutputAutoPkg_Type = Integer32
_BattMonOutputAutoPkg_Object = MibScalar
battMonOutputAutoPkg = _BattMonOutputAutoPkg_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 46, 71),
    _BattMonOutputAutoPkg_Type()
)
battMonOutputAutoPkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battMonOutputAutoPkg.setStatus("current")
_PBankInfoTable_Object = MibTable
pBankInfoTable = _PBankInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 47)
)
if mibBuilder.loadTexts:
    pBankInfoTable.setStatus("current")
_PBankInfoEntry_Object = MibTableRow
pBankInfoEntry = _PBankInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 47, 1)
)
pBankInfoEntry.setIndexNames(
    (0, "WEBMON-EDGE-MATRIX-MIB", "pBankInfoIndex"),
)
if mibBuilder.loadTexts:
    pBankInfoEntry.setStatus("current")
_PBankInfoDescription_Type = DescriptionString
_PBankInfoDescription_Object = MibTableColumn
pBankInfoDescription = _PBankInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 47, 1, 3),
    _PBankInfoDescription_Type()
)
pBankInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBankInfoDescription.setStatus("current")
_PBankInfoConfigured_Type = Configured
_PBankInfoConfigured_Object = MibTableColumn
pBankInfoConfigured = _PBankInfoConfigured_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 47, 1, 10),
    _PBankInfoConfigured_Type()
)
pBankInfoConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pBankInfoConfigured.setStatus("current")
_PBankInfoPresent_Type = Boolean
_PBankInfoPresent_Object = MibTableColumn
pBankInfoPresent = _PBankInfoPresent_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 47, 1, 68),
    _PBankInfoPresent_Type()
)
pBankInfoPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBankInfoPresent.setStatus("current")
_PBankInfoSlotId_Type = SlotId
_PBankInfoSlotId_Object = MibTableColumn
pBankInfoSlotId = _PBankInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 47, 1, 69),
    _PBankInfoSlotId_Type()
)
pBankInfoSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pBankInfoSlotId.setStatus("current")
_PBankInfoIOFormat_Type = IOFormat
_PBankInfoIOFormat_Object = MibTableColumn
pBankInfoIOFormat = _PBankInfoIOFormat_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 47, 1, 75),
    _PBankInfoIOFormat_Type()
)
pBankInfoIOFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pBankInfoIOFormat.setStatus("current")


class _PBankInfoIndex_Type(Integer32):
    """Custom type pBankInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PBankInfoIndex_Type.__name__ = "Integer32"
_PBankInfoIndex_Object = MibTableColumn
pBankInfoIndex = _PBankInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 47, 1, 999),
    _PBankInfoIndex_Type()
)
pBankInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pBankInfoIndex.setStatus("current")
_Triggers_ObjectIdentity = ObjectIdentity
triggers = _Triggers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 8)
)
_ResetDevice_Type = Boolean
_ResetDevice_Object = MibScalar
resetDevice = _ResetDevice_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 8, 1),
    _ResetDevice_Type()
)
resetDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetDevice.setStatus("current")
_CommitAccountChanges_Type = Boolean
_CommitAccountChanges_Object = MibScalar
commitAccountChanges = _CommitAccountChanges_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 8, 2),
    _CommitAccountChanges_Type()
)
commitAccountChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commitAccountChanges.setStatus("current")
_ResendEvents_Type = Boolean
_ResendEvents_Object = MibScalar
resendEvents = _ResendEvents_Object(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 8, 3),
    _ResendEvents_Type()
)
resendEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resendEvents.setStatus("current")

# Managed Objects groups

objectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 5)
)
objectGroup.setObjects(
      *(("WEBMON-EDGE-MATRIX-MIB", "systemGeneralDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralLocation"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogInputDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogLiveReading"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogUnitsOfMeasurement"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogLiveState"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogLiveStateDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogAlarmState"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogSourceDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogSourceIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalInputDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalAlarmState"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalLiveState"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalLiveStateDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalSourceDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalSourceIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceLiveState"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceAlarmState"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceSourceDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceSourceIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultStateDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultAlarmState"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultSourceDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultSourceIndex"))
)
if mibBuilder.loadTexts:
    objectGroup.setStatus("current")

configObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 7, 999)
)
configObjectGroup.setObjects(
      *(("WEBMON-EDGE-MATRIX-MIB", "systemGeneralLocation"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralIpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralSubnetMask"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralGatewayAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralMeasureStyle"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralMacAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralProductType"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralIPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralVersion"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetIpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetSnmpVersion"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetIPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetBackupIPAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetUseDialout"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetDialoutTarget"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetAuthKey"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetPrivKey"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetSNMPAccess"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetEngineID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTrapTargetIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pEmailAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pEmailDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pEmailConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pEmailIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorDesc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorDesc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorDesc2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorDesc3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorDesc4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorDesc5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorSendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorSendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorLevel0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorLevel1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorLevel2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorLevel3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorLevel4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorLevel5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorThresh0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorThresh1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorThresh2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorThresh3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorThresh4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorThresh5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorUnits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorPollAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorLiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorLiveRaw"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorLiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorTL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorTL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorTL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorTL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorTL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorTL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorTL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorMODBUSCommand"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorStartRegister"),
        ("WEBMON-EDGE-MATRIX-MIB", "pRemoteSensorIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorDesc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorDesc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorDesc2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorDesc3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorDesc4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorDesc5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorSendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorSendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorLevel0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorLevel1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorLevel2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorLevel3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorLevel4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorLevel5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorThresh0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorThresh1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorThresh2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorThresh3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorThresh4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorThresh5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorUnits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorLiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorLiveRaw"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorLiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorTL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorTL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorTL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorTL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorTL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorTL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorTL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pOnboardSensorIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesDesc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesDesc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesSendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesSendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesIpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesLevel0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesLevel1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesLiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesLiveRaw"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesLiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesTL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesTL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesTL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesTL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesTL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesTL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesTL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetDevicesIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pAccountsConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pAccountsName"),
        ("WEBMON-EDGE-MATRIX-MIB", "pAccountsEncPassword"),
        ("WEBMON-EDGE-MATRIX-MIB", "pAccountsUserLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pAccountsUnsecured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pAccountsAuthKey"),
        ("WEBMON-EDGE-MATRIX-MIB", "pAccountsPrivKey"),
        ("WEBMON-EDGE-MATRIX-MIB", "pAccountsSNMPAccess"),
        ("WEBMON-EDGE-MATRIX-MIB", "pAccountsIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "cameraConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "cameraIpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "cameraCameraStyle"),
        ("WEBMON-EDGE-MATRIX-MIB", "snmpGeneralConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "snmpGeneralReadPeriod"),
        ("WEBMON-EDGE-MATRIX-MIB", "snmpGeneralGet"),
        ("WEBMON-EDGE-MATRIX-MIB", "snmpGeneralSet"),
        ("WEBMON-EDGE-MATRIX-MIB", "snmpGeneralTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "snmpGeneralIPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "snmpGeneralEngineID"),
        ("WEBMON-EDGE-MATRIX-MIB", "emailGeneralAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "emailGeneralConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "emailGeneralIpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "emailGeneralPassword"),
        ("WEBMON-EDGE-MATRIX-MIB", "emailGeneralIPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialIpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialReadPeriod"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialBaudRate"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialDataBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialParity"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialStopBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialProtocol"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialSerialRTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialSerialCTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialPresent"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialIPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialPortType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSerialIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSelfTestDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSelfTestConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSelfTestIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsDesc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsDesc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsDesc2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsDesc3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsSendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsSendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsLevel0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsLevel1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsLevel2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsLevel3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsIgnoreOff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsLiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsLiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pInternalFaultsIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlotInfoDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlotInfoRecord"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlotInfoPresent"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlotInfoSlotId"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlotInfoIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetPortsDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetPortsIPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "pNetPortsIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "wirelessModemBackupIPAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "wirelessModemTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "wirelessModemTransmit"),
        ("WEBMON-EDGE-MATRIX-MIB", "wirelessModemUseWirelessNetwork"),
        ("WEBMON-EDGE-MATRIX-MIB", "wirelessModemUseResetTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "wirelessModemResponseWaitTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "wirelessModemSecondary"),
        ("WEBMON-EDGE-MATRIX-MIB", "webmonSecurityUserLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "webmonSecurityUnsecured"),
        ("WEBMON-EDGE-MATRIX-MIB", "dateTimeConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "dateTimeIpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "dateTimeDaylightSaving"),
        ("WEBMON-EDGE-MATRIX-MIB", "dateTimeDate"),
        ("WEBMON-EDGE-MATRIX-MIB", "dateTimeTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "dateTimeNegOffset"),
        ("WEBMON-EDGE-MATRIX-MIB", "dateTimeUTCOffset"),
        ("WEBMON-EDGE-MATRIX-MIB", "pDCMProtocolDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pDCMProtocolConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pDCMProtocolBaseDCMAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pDCMProtocolIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pdialOutConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pdialOutName"),
        ("WEBMON-EDGE-MATRIX-MIB", "pdialOutPassword"),
        ("WEBMON-EDGE-MATRIX-MIB", "pdialOutDialOutNumber"),
        ("WEBMON-EDGE-MATRIX-MIB", "pdialOutIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteDesc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteDesc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteSendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteSendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteLevel0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteLevel1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteLiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteLiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteElementAPkg"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteElementAPoint"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteElementBPkg"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteElementBPoint"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteDiscreteFormula"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteTL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteTL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteTL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteTL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteTL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteTL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteTL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedDiscreteIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "licenseDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "licenseLicenseKey"),
        ("WEBMON-EDGE-MATRIX-MIB", "licenseExpires"),
        ("WEBMON-EDGE-MATRIX-MIB", "licenseAllowTL1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostIpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostLevel0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostLevel1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostLevel2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostRosterID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostPollAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostIPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostTL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostTL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostTL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostTL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostTL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostTL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostTL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pe2aHostIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogDesc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogDesc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogDesc2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogDesc3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogDesc4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogSendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogSendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogLevel0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogLevel1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogLevel2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogLevel3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogLevel4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogThresh0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogThresh1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogThresh2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogThresh3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogThresh4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogThresh5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogUnits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogLiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogLiveRaw"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogLiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogElementAPkg"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogElementAPoint"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogElementBPkg"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogElementBPoint"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogFormula"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogTL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogTL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogTL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogTL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogTL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogTL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogTL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pderivedAnalogIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsDesc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsDesc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsDesc2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsDesc3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsDesc4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsSendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsSendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsLevel0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsLevel1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsLevel2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsLevel3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsLevel4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsThresh0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsThresh1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsThresh2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsThresh3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsThresh4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsThresh5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsUnits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsLiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsLiveRaw"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsLiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsTL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsTL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsTL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsTL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsTL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsTL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsTL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pgpsIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pportRedirectDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pportRedirectConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pportRedirectIpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pportRedirectReadPeriod"),
        ("WEBMON-EDGE-MATRIX-MIB", "pportRedirectRosterID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pportRedirectIPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "pportRedirectIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleADayOfWeek"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleAConfiguredState"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleAConfigured1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleAConfigured2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleAConfigured3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleAConfigured4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleATime0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleATime1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleATime2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleATime3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleATime4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleATime5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleAIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBDayOfWeek"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBConfiguredState"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBConfigured1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBConfigured2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBConfigured3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBConfigured4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBTime0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBTime1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBTime2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBTime3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBTime4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBTime5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleBIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCDayOfWeek"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCConfiguredState"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCConfigured1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCConfigured2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCConfigured3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCConfigured4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCTime0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCTime1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCTime2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCTime3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCTime4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCTime5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleCIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDDayOfWeek"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDConfiguredState"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDConfigured1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDConfigured2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDConfigured3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDConfigured4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDTime0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDTime1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDTime2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDTime3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDTime4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDTime5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pscheduleDIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "tl1SettingsTL1Issue"),
        ("WEBMON-EDGE-MATRIX-MIB", "pDCPFProtocolDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pDCPFProtocolConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pDCPFProtocolBaseDCPFDisplay"),
        ("WEBMON-EDGE-MATRIX-MIB", "pDCPFProtocolIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "dcpfSettingsDCPFAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTABSProtocolDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTABSProtocolConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTABSProtocolBaseTABSDisplay"),
        ("WEBMON-EDGE-MATRIX-MIB", "pTABSProtocolIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "tabsSettingsTABSAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsIpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsGet"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsSnmpVersion"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsOutputAuto"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsOutputAutoPkg"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsIPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsOID"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsSNMPVarbindType"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsTextNormal"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsTextCritical"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsTextMajor"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsTextMinor"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsTextStatus"),
        ("WEBMON-EDGE-MATRIX-MIB", "psnmpCommandsIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "battMonConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "battMonOutputAuto"),
        ("WEBMON-EDGE-MATRIX-MIB", "battMonOutputAutoPkg"),
        ("WEBMON-EDGE-MATRIX-MIB", "pBankInfoDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pBankInfoConfigured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pBankInfoPresent"),
        ("WEBMON-EDGE-MATRIX-MIB", "pBankInfoSlotId"),
        ("WEBMON-EDGE-MATRIX-MIB", "pBankInfoIOFormat"),
        ("WEBMON-EDGE-MATRIX-MIB", "pBankInfoIndex"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Description"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Desc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Desc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Desc2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Desc3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Desc4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Desc5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Configured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1SendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1SendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1IpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Level0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Level1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Level2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Level3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Level4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Level5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1ReadPeriod"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Thresh0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Thresh1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Thresh2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Thresh3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Thresh4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Thresh5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1ContactStyle"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Units"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1OutputMode"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1OutputState"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1OutputAuto"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1BaudRate"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1DataBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Parity"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1StopBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Protocol"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1SerialRTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1SerialCTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1LiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1LiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1LiveRaw"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1LiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Present"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1OutputAutoPkg"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1VoltageRange"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1IPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1IOFormat"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1PortType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1TL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1TL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1TL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1TL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1TL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1TL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1TL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1SensorType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot1Index"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Description"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Desc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Desc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Desc2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Desc3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Desc4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Desc5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Configured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2SendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2SendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2IpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Level0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Level1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Level2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Level3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Level4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Level5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2ReadPeriod"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Thresh0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Thresh1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Thresh2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Thresh3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Thresh4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Thresh5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2ContactStyle"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Units"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2OutputMode"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2OutputState"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2OutputAuto"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2BaudRate"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2DataBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Parity"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2StopBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Protocol"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2SerialRTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2SerialCTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2LiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2LiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2LiveRaw"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2LiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Present"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2OutputAutoPkg"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2VoltageRange"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2IPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2IOFormat"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2PortType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2TL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2TL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2TL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2TL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2TL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2TL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2TL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2SensorType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot2Index"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Description"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Desc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Desc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Desc2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Desc3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Desc4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Desc5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Configured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3SendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3SendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3IpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Level0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Level1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Level2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Level3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Level4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Level5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3ReadPeriod"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Thresh0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Thresh1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Thresh2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Thresh3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Thresh4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Thresh5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3ContactStyle"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Units"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3OutputMode"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3OutputState"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3OutputAuto"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3BaudRate"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3DataBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Parity"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3StopBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Protocol"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3SerialRTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3SerialCTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3LiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3LiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3LiveRaw"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3LiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Present"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3OutputAutoPkg"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3VoltageRange"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3IPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3IOFormat"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3PortType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3TL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3TL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3TL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3TL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3TL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3TL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3TL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3SensorType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot3Index"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Description"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Desc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Desc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Desc2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Desc3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Desc4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Desc5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Configured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4SendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4SendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4IpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Level0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Level1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Level2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Level3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Level4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Level5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4ReadPeriod"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Thresh0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Thresh1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Thresh2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Thresh3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Thresh4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Thresh5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4ContactStyle"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Units"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4OutputMode"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4OutputState"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4OutputAuto"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4BaudRate"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4DataBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Parity"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4StopBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Protocol"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4SerialRTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4SerialCTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4LiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4LiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4LiveRaw"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4LiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Present"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4OutputAutoPkg"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4VoltageRange"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4IPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4IOFormat"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4PortType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4TL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4TL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4TL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4TL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4TL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4TL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4TL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4SensorType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot4Index"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Description"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Desc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Desc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Desc2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Desc3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Desc4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Desc5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Configured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5SendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5SendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5IpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Level0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Level1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Level2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Level3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Level4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Level5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5ReadPeriod"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Thresh0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Thresh1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Thresh2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Thresh3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Thresh4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Thresh5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5ContactStyle"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Units"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5OutputMode"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5OutputState"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5OutputAuto"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5BaudRate"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5DataBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Parity"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5StopBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Protocol"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5SerialRTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5SerialCTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5LiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5LiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5LiveRaw"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5LiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Present"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5OutputAutoPkg"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5VoltageRange"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5IPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5IOFormat"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5PortType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5TL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5TL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5TL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5TL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5TL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5TL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5TL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5SensorType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot5Index"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Description"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Desc0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Desc1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Desc2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Desc3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Desc4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Desc5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Configured"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6SendEmail"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6SendSNMPTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6IpAddress"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Level0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Level1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Level2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Level3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Level4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Level5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6ReadPeriod"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Thresh0"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Thresh1"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Thresh2"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Thresh3"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Thresh4"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Thresh5"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6ContactStyle"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Units"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6OutputMode"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6OutputState"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6OutputAuto"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6BaudRate"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6DataBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Parity"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6StopBits"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Protocol"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6SerialRTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6SerialCTS"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6LiveDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6LiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6LiveRaw"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6LiveTime"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Present"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6OutputAutoPkg"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6VoltageRange"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6IPPortNum"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6IOFormat"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6PortType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6TL1SID"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6TL1COND"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6TL1Eqpt"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6TL1Env"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6TL1Srveff"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6TL1Locn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6TL1Dirn"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6SensorType"),
        ("WEBMON-EDGE-MATRIX-MIB", "pSlot6Index"))
)
if mibBuilder.loadTexts:
    configObjectGroup.setStatus("current")


# Notification objects

analogEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 1, 1)
)
analogEventTrap.setObjects(
      *(("WEBMON-EDGE-MATRIX-MIB", "systemGeneralDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralLocation"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogInputDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogLiveReading"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogLiveState"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogLiveStateDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogUnitsOfMeasurement"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogAlarmState"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogSourceDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "analogSourceIndex"))
)
if mibBuilder.loadTexts:
    analogEventTrap.setStatus(
        "current"
    )

digitalEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 2, 1)
)
digitalEventTrap.setObjects(
      *(("WEBMON-EDGE-MATRIX-MIB", "systemGeneralDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralLocation"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalInputDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalLiveState"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalLiveStateDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalAlarmState"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalSourceDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalSourceIndex"))
)
if mibBuilder.loadTexts:
    digitalEventTrap.setStatus(
        "current"
    )

remoteDeviceEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 3, 1)
)
remoteDeviceEventTrap.setObjects(
      *(("WEBMON-EDGE-MATRIX-MIB", "systemGeneralDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralLocation"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceLiveState"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceAlarmState"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceSourceDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceSourceIndex"))
)
if mibBuilder.loadTexts:
    remoteDeviceEventTrap.setStatus(
        "current"
    )

faultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 6, 4, 1)
)
faultTrap.setObjects(
      *(("WEBMON-EDGE-MATRIX-MIB", "systemGeneralDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "systemGeneralLocation"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultLiveLevel"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultStateDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultAlarmState"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultSourceDescription"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultSourceIndex"))
)
if mibBuilder.loadTexts:
    faultTrap.setStatus(
        "current"
    )


# Notifications groups

notificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 994, 3, 4, 4)
)
notificationGroup.setObjects(
      *(("WEBMON-EDGE-MATRIX-MIB", "analogEventTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "remoteDeviceEventTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "faultTrap"),
        ("WEBMON-EDGE-MATRIX-MIB", "digitalEventTrap"))
)
if mibBuilder.loadTexts:
    notificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WEBMON-EDGE-MATRIX-MIB",
    **{"DescriptionString": DescriptionString,
       "DigitalState": DigitalState,
       "Boolean": Boolean,
       "ConnectivityState": ConnectivityState,
       "AnalogState": AnalogState,
       "Configured": Configured,
       "Level": Level,
       "SnmpVersion": SnmpVersion,
       "CameraStyle": CameraStyle,
       "ContactStyle": ContactStyle,
       "MeasureStyle": MeasureStyle,
       "OutputMode": OutputMode,
       "OutputState": OutputState,
       "BaudRate": BaudRate,
       "DataBits": DataBits,
       "Parity": Parity,
       "StopBits": StopBits,
       "Protocol": Protocol,
       "SerialRTS": SerialRTS,
       "SerialCTS": SerialCTS,
       "SlotId": SlotId,
       "ProductType": ProductType,
       "VoltageRange": VoltageRange,
       "IOFormat": IOFormat,
       "PortType": PortType,
       "DiscreteFormula": DiscreteFormula,
       "DayOfWeek": DayOfWeek,
       "ConfiguredState": ConfiguredState,
       "TL1Srveff": TL1Srveff,
       "TL1Locn": TL1Locn,
       "TL1Dirn": TL1Dirn,
       "TL1Issue": TL1Issue,
       "UseDialout": UseDialout,
       "SensorType": SensorType,
       "SNMPCommandType": SNMPCommandType,
       "SNMPVarbindType": SNMPVarbindType,
       "SNMPAccess": SNMPAccess,
       "MODBUSCommand": MODBUSCommand,
       "dantel": dantel,
       "dantelProducts": dantelProducts,
       "webMon": webMon,
       "moduleIdentity": moduleIdentity,
       "notificationGroup": notificationGroup,
       "objectGroup": objectGroup,
       "traps": traps,
       "analogInputs": analogInputs,
       "analogEventTrap": analogEventTrap,
       "analogInputDescription": analogInputDescription,
       "analogLiveLevel": analogLiveLevel,
       "analogLiveReading": analogLiveReading,
       "analogUnitsOfMeasurement": analogUnitsOfMeasurement,
       "analogLiveState": analogLiveState,
       "analogLiveStateDescription": analogLiveStateDescription,
       "analogAlarmState": analogAlarmState,
       "analogSourceDescription": analogSourceDescription,
       "analogSourceIndex": analogSourceIndex,
       "digitalInputs": digitalInputs,
       "digitalEventTrap": digitalEventTrap,
       "digitalInputDescription": digitalInputDescription,
       "digitalLiveLevel": digitalLiveLevel,
       "digitalLiveState": digitalLiveState,
       "digitalLiveStateDescription": digitalLiveStateDescription,
       "digitalAlarmState": digitalAlarmState,
       "digitalSourceDescription": digitalSourceDescription,
       "digitalSourceIndex": digitalSourceIndex,
       "remoteDevices": remoteDevices,
       "remoteDeviceEventTrap": remoteDeviceEventTrap,
       "remoteDeviceDescription": remoteDeviceDescription,
       "remoteDeviceLiveLevel": remoteDeviceLiveLevel,
       "remoteDeviceLiveState": remoteDeviceLiveState,
       "remoteDeviceAlarmState": remoteDeviceAlarmState,
       "remoteDeviceSourceDescription": remoteDeviceSourceDescription,
       "remoteDeviceSourceIndex": remoteDeviceSourceIndex,
       "faults": faults,
       "faultTrap": faultTrap,
       "faultDescription": faultDescription,
       "faultLiveLevel": faultLiveLevel,
       "faultStateDescription": faultStateDescription,
       "faultAlarmState": faultAlarmState,
       "faultSourceDescription": faultSourceDescription,
       "faultSourceIndex": faultSourceIndex,
       "configuration": configuration,
       "systemGeneral": systemGeneral,
       "systemGeneralLocation": systemGeneralLocation,
       "systemGeneralDescription": systemGeneralDescription,
       "systemGeneralIpAddress": systemGeneralIpAddress,
       "systemGeneralSubnetMask": systemGeneralSubnetMask,
       "systemGeneralGatewayAddress": systemGeneralGatewayAddress,
       "systemGeneralMeasureStyle": systemGeneralMeasureStyle,
       "systemGeneralMacAddress": systemGeneralMacAddress,
       "systemGeneralProductType": systemGeneralProductType,
       "systemGeneralIPPortNum": systemGeneralIPPortNum,
       "systemGeneralVersion": systemGeneralVersion,
       "pTrapTargetTable": pTrapTargetTable,
       "pTrapTargetEntry": pTrapTargetEntry,
       "pTrapTargetDescription": pTrapTargetDescription,
       "pTrapTargetConfigured": pTrapTargetConfigured,
       "pTrapTargetIpAddress": pTrapTargetIpAddress,
       "pTrapTargetSnmpVersion": pTrapTargetSnmpVersion,
       "pTrapTargetIPPortNum": pTrapTargetIPPortNum,
       "pTrapTargetBackupIPAddress": pTrapTargetBackupIPAddress,
       "pTrapTargetUseDialout": pTrapTargetUseDialout,
       "pTrapTargetDialoutTarget": pTrapTargetDialoutTarget,
       "pTrapTargetAuthKey": pTrapTargetAuthKey,
       "pTrapTargetPrivKey": pTrapTargetPrivKey,
       "pTrapTargetSNMPAccess": pTrapTargetSNMPAccess,
       "pTrapTargetEngineID": pTrapTargetEngineID,
       "pTrapTargetIndex": pTrapTargetIndex,
       "pEmailTable": pEmailTable,
       "pEmailEntry": pEmailEntry,
       "pEmailAddress": pEmailAddress,
       "pEmailDescription": pEmailDescription,
       "pEmailConfigured": pEmailConfigured,
       "pEmailIndex": pEmailIndex,
       "pRemoteSensorTable": pRemoteSensorTable,
       "pRemoteSensorEntry": pRemoteSensorEntry,
       "pRemoteSensorDescription": pRemoteSensorDescription,
       "pRemoteSensorDesc0": pRemoteSensorDesc0,
       "pRemoteSensorDesc1": pRemoteSensorDesc1,
       "pRemoteSensorDesc2": pRemoteSensorDesc2,
       "pRemoteSensorDesc3": pRemoteSensorDesc3,
       "pRemoteSensorDesc4": pRemoteSensorDesc4,
       "pRemoteSensorDesc5": pRemoteSensorDesc5,
       "pRemoteSensorConfigured": pRemoteSensorConfigured,
       "pRemoteSensorSendEmail": pRemoteSensorSendEmail,
       "pRemoteSensorSendSNMPTrap": pRemoteSensorSendSNMPTrap,
       "pRemoteSensorLevel0": pRemoteSensorLevel0,
       "pRemoteSensorLevel1": pRemoteSensorLevel1,
       "pRemoteSensorLevel2": pRemoteSensorLevel2,
       "pRemoteSensorLevel3": pRemoteSensorLevel3,
       "pRemoteSensorLevel4": pRemoteSensorLevel4,
       "pRemoteSensorLevel5": pRemoteSensorLevel5,
       "pRemoteSensorThresh0": pRemoteSensorThresh0,
       "pRemoteSensorThresh1": pRemoteSensorThresh1,
       "pRemoteSensorThresh2": pRemoteSensorThresh2,
       "pRemoteSensorThresh3": pRemoteSensorThresh3,
       "pRemoteSensorThresh4": pRemoteSensorThresh4,
       "pRemoteSensorThresh5": pRemoteSensorThresh5,
       "pRemoteSensorUnits": pRemoteSensorUnits,
       "pRemoteSensorPollAddress": pRemoteSensorPollAddress,
       "pRemoteSensorLiveDescription": pRemoteSensorLiveDescription,
       "pRemoteSensorLiveLevel": pRemoteSensorLiveLevel,
       "pRemoteSensorLiveRaw": pRemoteSensorLiveRaw,
       "pRemoteSensorLiveTime": pRemoteSensorLiveTime,
       "pRemoteSensorTL1SID": pRemoteSensorTL1SID,
       "pRemoteSensorTL1COND": pRemoteSensorTL1COND,
       "pRemoteSensorTL1Eqpt": pRemoteSensorTL1Eqpt,
       "pRemoteSensorTL1Env": pRemoteSensorTL1Env,
       "pRemoteSensorTL1Srveff": pRemoteSensorTL1Srveff,
       "pRemoteSensorTL1Locn": pRemoteSensorTL1Locn,
       "pRemoteSensorTL1Dirn": pRemoteSensorTL1Dirn,
       "pRemoteSensorMODBUSCommand": pRemoteSensorMODBUSCommand,
       "pRemoteSensorStartRegister": pRemoteSensorStartRegister,
       "pRemoteSensorIndex": pRemoteSensorIndex,
       "pOnboardSensorTable": pOnboardSensorTable,
       "pOnboardSensorEntry": pOnboardSensorEntry,
       "pOnboardSensorDescription": pOnboardSensorDescription,
       "pOnboardSensorDesc0": pOnboardSensorDesc0,
       "pOnboardSensorDesc1": pOnboardSensorDesc1,
       "pOnboardSensorDesc2": pOnboardSensorDesc2,
       "pOnboardSensorDesc3": pOnboardSensorDesc3,
       "pOnboardSensorDesc4": pOnboardSensorDesc4,
       "pOnboardSensorDesc5": pOnboardSensorDesc5,
       "pOnboardSensorConfigured": pOnboardSensorConfigured,
       "pOnboardSensorSendEmail": pOnboardSensorSendEmail,
       "pOnboardSensorSendSNMPTrap": pOnboardSensorSendSNMPTrap,
       "pOnboardSensorLevel0": pOnboardSensorLevel0,
       "pOnboardSensorLevel1": pOnboardSensorLevel1,
       "pOnboardSensorLevel2": pOnboardSensorLevel2,
       "pOnboardSensorLevel3": pOnboardSensorLevel3,
       "pOnboardSensorLevel4": pOnboardSensorLevel4,
       "pOnboardSensorLevel5": pOnboardSensorLevel5,
       "pOnboardSensorThresh0": pOnboardSensorThresh0,
       "pOnboardSensorThresh1": pOnboardSensorThresh1,
       "pOnboardSensorThresh2": pOnboardSensorThresh2,
       "pOnboardSensorThresh3": pOnboardSensorThresh3,
       "pOnboardSensorThresh4": pOnboardSensorThresh4,
       "pOnboardSensorThresh5": pOnboardSensorThresh5,
       "pOnboardSensorUnits": pOnboardSensorUnits,
       "pOnboardSensorLiveDescription": pOnboardSensorLiveDescription,
       "pOnboardSensorLiveLevel": pOnboardSensorLiveLevel,
       "pOnboardSensorLiveRaw": pOnboardSensorLiveRaw,
       "pOnboardSensorLiveTime": pOnboardSensorLiveTime,
       "pOnboardSensorTL1SID": pOnboardSensorTL1SID,
       "pOnboardSensorTL1COND": pOnboardSensorTL1COND,
       "pOnboardSensorTL1Eqpt": pOnboardSensorTL1Eqpt,
       "pOnboardSensorTL1Env": pOnboardSensorTL1Env,
       "pOnboardSensorTL1Srveff": pOnboardSensorTL1Srveff,
       "pOnboardSensorTL1Locn": pOnboardSensorTL1Locn,
       "pOnboardSensorTL1Dirn": pOnboardSensorTL1Dirn,
       "pOnboardSensorIndex": pOnboardSensorIndex,
       "pNetDevicesTable": pNetDevicesTable,
       "pNetDevicesEntry": pNetDevicesEntry,
       "pNetDevicesDescription": pNetDevicesDescription,
       "pNetDevicesDesc0": pNetDevicesDesc0,
       "pNetDevicesDesc1": pNetDevicesDesc1,
       "pNetDevicesConfigured": pNetDevicesConfigured,
       "pNetDevicesSendEmail": pNetDevicesSendEmail,
       "pNetDevicesSendSNMPTrap": pNetDevicesSendSNMPTrap,
       "pNetDevicesIpAddress": pNetDevicesIpAddress,
       "pNetDevicesLevel0": pNetDevicesLevel0,
       "pNetDevicesLevel1": pNetDevicesLevel1,
       "pNetDevicesLiveDescription": pNetDevicesLiveDescription,
       "pNetDevicesLiveLevel": pNetDevicesLiveLevel,
       "pNetDevicesLiveRaw": pNetDevicesLiveRaw,
       "pNetDevicesLiveTime": pNetDevicesLiveTime,
       "pNetDevicesTL1SID": pNetDevicesTL1SID,
       "pNetDevicesTL1COND": pNetDevicesTL1COND,
       "pNetDevicesTL1Eqpt": pNetDevicesTL1Eqpt,
       "pNetDevicesTL1Env": pNetDevicesTL1Env,
       "pNetDevicesTL1Srveff": pNetDevicesTL1Srveff,
       "pNetDevicesTL1Locn": pNetDevicesTL1Locn,
       "pNetDevicesTL1Dirn": pNetDevicesTL1Dirn,
       "pNetDevicesIndex": pNetDevicesIndex,
       "pAccountsTable": pAccountsTable,
       "pAccountsEntry": pAccountsEntry,
       "pAccountsConfigured": pAccountsConfigured,
       "pAccountsName": pAccountsName,
       "pAccountsEncPassword": pAccountsEncPassword,
       "pAccountsUserLevel": pAccountsUserLevel,
       "pAccountsUnsecured": pAccountsUnsecured,
       "pAccountsAuthKey": pAccountsAuthKey,
       "pAccountsPrivKey": pAccountsPrivKey,
       "pAccountsSNMPAccess": pAccountsSNMPAccess,
       "pAccountsIndex": pAccountsIndex,
       "camera": camera,
       "cameraConfigured": cameraConfigured,
       "cameraIpAddress": cameraIpAddress,
       "cameraCameraStyle": cameraCameraStyle,
       "snmpGeneral": snmpGeneral,
       "snmpGeneralConfigured": snmpGeneralConfigured,
       "snmpGeneralReadPeriod": snmpGeneralReadPeriod,
       "snmpGeneralGet": snmpGeneralGet,
       "snmpGeneralSet": snmpGeneralSet,
       "snmpGeneralTrap": snmpGeneralTrap,
       "snmpGeneralIPPortNum": snmpGeneralIPPortNum,
       "snmpGeneralEngineID": snmpGeneralEngineID,
       "emailGeneral": emailGeneral,
       "emailGeneralAddress": emailGeneralAddress,
       "emailGeneralConfigured": emailGeneralConfigured,
       "emailGeneralIpAddress": emailGeneralIpAddress,
       "emailGeneralPassword": emailGeneralPassword,
       "emailGeneralIPPortNum": emailGeneralIPPortNum,
       "pSerialTable": pSerialTable,
       "pSerialEntry": pSerialEntry,
       "pSerialDescription": pSerialDescription,
       "pSerialConfigured": pSerialConfigured,
       "pSerialIpAddress": pSerialIpAddress,
       "pSerialReadPeriod": pSerialReadPeriod,
       "pSerialBaudRate": pSerialBaudRate,
       "pSerialDataBits": pSerialDataBits,
       "pSerialParity": pSerialParity,
       "pSerialStopBits": pSerialStopBits,
       "pSerialProtocol": pSerialProtocol,
       "pSerialSerialRTS": pSerialSerialRTS,
       "pSerialSerialCTS": pSerialSerialCTS,
       "pSerialPresent": pSerialPresent,
       "pSerialIPPortNum": pSerialIPPortNum,
       "pSerialPortType": pSerialPortType,
       "pSerialIndex": pSerialIndex,
       "pSelfTestTable": pSelfTestTable,
       "pSelfTestEntry": pSelfTestEntry,
       "pSelfTestDescription": pSelfTestDescription,
       "pSelfTestConfigured": pSelfTestConfigured,
       "pSelfTestIndex": pSelfTestIndex,
       "pInternalFaultsTable": pInternalFaultsTable,
       "pInternalFaultsEntry": pInternalFaultsEntry,
       "pInternalFaultsDescription": pInternalFaultsDescription,
       "pInternalFaultsDesc0": pInternalFaultsDesc0,
       "pInternalFaultsDesc1": pInternalFaultsDesc1,
       "pInternalFaultsDesc2": pInternalFaultsDesc2,
       "pInternalFaultsDesc3": pInternalFaultsDesc3,
       "pInternalFaultsSendEmail": pInternalFaultsSendEmail,
       "pInternalFaultsSendSNMPTrap": pInternalFaultsSendSNMPTrap,
       "pInternalFaultsLevel0": pInternalFaultsLevel0,
       "pInternalFaultsLevel1": pInternalFaultsLevel1,
       "pInternalFaultsLevel2": pInternalFaultsLevel2,
       "pInternalFaultsLevel3": pInternalFaultsLevel3,
       "pInternalFaultsIgnoreOff": pInternalFaultsIgnoreOff,
       "pInternalFaultsLiveDescription": pInternalFaultsLiveDescription,
       "pInternalFaultsLiveLevel": pInternalFaultsLiveLevel,
       "pInternalFaultsLiveTime": pInternalFaultsLiveTime,
       "pInternalFaultsIndex": pInternalFaultsIndex,
       "pSlotInfoTable": pSlotInfoTable,
       "pSlotInfoEntry": pSlotInfoEntry,
       "pSlotInfoDescription": pSlotInfoDescription,
       "pSlotInfoRecord": pSlotInfoRecord,
       "pSlotInfoPresent": pSlotInfoPresent,
       "pSlotInfoSlotId": pSlotInfoSlotId,
       "pSlotInfoIndex": pSlotInfoIndex,
       "pSlot1Table": pSlot1Table,
       "pSlot1Entry": pSlot1Entry,
       "pSlot1Description": pSlot1Description,
       "pSlot1Desc0": pSlot1Desc0,
       "pSlot1Desc1": pSlot1Desc1,
       "pSlot1Desc2": pSlot1Desc2,
       "pSlot1Desc3": pSlot1Desc3,
       "pSlot1Desc4": pSlot1Desc4,
       "pSlot1Desc5": pSlot1Desc5,
       "pSlot1Configured": pSlot1Configured,
       "pSlot1SendEmail": pSlot1SendEmail,
       "pSlot1SendSNMPTrap": pSlot1SendSNMPTrap,
       "pSlot1IpAddress": pSlot1IpAddress,
       "pSlot1Level0": pSlot1Level0,
       "pSlot1Level1": pSlot1Level1,
       "pSlot1Level2": pSlot1Level2,
       "pSlot1Level3": pSlot1Level3,
       "pSlot1Level4": pSlot1Level4,
       "pSlot1Level5": pSlot1Level5,
       "pSlot1ReadPeriod": pSlot1ReadPeriod,
       "pSlot1Thresh0": pSlot1Thresh0,
       "pSlot1Thresh1": pSlot1Thresh1,
       "pSlot1Thresh2": pSlot1Thresh2,
       "pSlot1Thresh3": pSlot1Thresh3,
       "pSlot1Thresh4": pSlot1Thresh4,
       "pSlot1Thresh5": pSlot1Thresh5,
       "pSlot1ContactStyle": pSlot1ContactStyle,
       "pSlot1Units": pSlot1Units,
       "pSlot1OutputMode": pSlot1OutputMode,
       "pSlot1OutputState": pSlot1OutputState,
       "pSlot1OutputAuto": pSlot1OutputAuto,
       "pSlot1BaudRate": pSlot1BaudRate,
       "pSlot1DataBits": pSlot1DataBits,
       "pSlot1Parity": pSlot1Parity,
       "pSlot1StopBits": pSlot1StopBits,
       "pSlot1Protocol": pSlot1Protocol,
       "pSlot1SerialRTS": pSlot1SerialRTS,
       "pSlot1SerialCTS": pSlot1SerialCTS,
       "pSlot1LiveDescription": pSlot1LiveDescription,
       "pSlot1LiveLevel": pSlot1LiveLevel,
       "pSlot1LiveRaw": pSlot1LiveRaw,
       "pSlot1LiveTime": pSlot1LiveTime,
       "pSlot1Present": pSlot1Present,
       "pSlot1OutputAutoPkg": pSlot1OutputAutoPkg,
       "pSlot1VoltageRange": pSlot1VoltageRange,
       "pSlot1IPPortNum": pSlot1IPPortNum,
       "pSlot1IOFormat": pSlot1IOFormat,
       "pSlot1PortType": pSlot1PortType,
       "pSlot1TL1SID": pSlot1TL1SID,
       "pSlot1TL1COND": pSlot1TL1COND,
       "pSlot1TL1Eqpt": pSlot1TL1Eqpt,
       "pSlot1TL1Env": pSlot1TL1Env,
       "pSlot1TL1Srveff": pSlot1TL1Srveff,
       "pSlot1TL1Locn": pSlot1TL1Locn,
       "pSlot1TL1Dirn": pSlot1TL1Dirn,
       "pSlot1SensorType": pSlot1SensorType,
       "pSlot1Index": pSlot1Index,
       "pSlot2Table": pSlot2Table,
       "pSlot2Entry": pSlot2Entry,
       "pSlot2Description": pSlot2Description,
       "pSlot2Desc0": pSlot2Desc0,
       "pSlot2Desc1": pSlot2Desc1,
       "pSlot2Desc2": pSlot2Desc2,
       "pSlot2Desc3": pSlot2Desc3,
       "pSlot2Desc4": pSlot2Desc4,
       "pSlot2Desc5": pSlot2Desc5,
       "pSlot2Configured": pSlot2Configured,
       "pSlot2SendEmail": pSlot2SendEmail,
       "pSlot2SendSNMPTrap": pSlot2SendSNMPTrap,
       "pSlot2IpAddress": pSlot2IpAddress,
       "pSlot2Level0": pSlot2Level0,
       "pSlot2Level1": pSlot2Level1,
       "pSlot2Level2": pSlot2Level2,
       "pSlot2Level3": pSlot2Level3,
       "pSlot2Level4": pSlot2Level4,
       "pSlot2Level5": pSlot2Level5,
       "pSlot2ReadPeriod": pSlot2ReadPeriod,
       "pSlot2Thresh0": pSlot2Thresh0,
       "pSlot2Thresh1": pSlot2Thresh1,
       "pSlot2Thresh2": pSlot2Thresh2,
       "pSlot2Thresh3": pSlot2Thresh3,
       "pSlot2Thresh4": pSlot2Thresh4,
       "pSlot2Thresh5": pSlot2Thresh5,
       "pSlot2ContactStyle": pSlot2ContactStyle,
       "pSlot2Units": pSlot2Units,
       "pSlot2OutputMode": pSlot2OutputMode,
       "pSlot2OutputState": pSlot2OutputState,
       "pSlot2OutputAuto": pSlot2OutputAuto,
       "pSlot2BaudRate": pSlot2BaudRate,
       "pSlot2DataBits": pSlot2DataBits,
       "pSlot2Parity": pSlot2Parity,
       "pSlot2StopBits": pSlot2StopBits,
       "pSlot2Protocol": pSlot2Protocol,
       "pSlot2SerialRTS": pSlot2SerialRTS,
       "pSlot2SerialCTS": pSlot2SerialCTS,
       "pSlot2LiveDescription": pSlot2LiveDescription,
       "pSlot2LiveLevel": pSlot2LiveLevel,
       "pSlot2LiveRaw": pSlot2LiveRaw,
       "pSlot2LiveTime": pSlot2LiveTime,
       "pSlot2Present": pSlot2Present,
       "pSlot2OutputAutoPkg": pSlot2OutputAutoPkg,
       "pSlot2VoltageRange": pSlot2VoltageRange,
       "pSlot2IPPortNum": pSlot2IPPortNum,
       "pSlot2IOFormat": pSlot2IOFormat,
       "pSlot2PortType": pSlot2PortType,
       "pSlot2TL1SID": pSlot2TL1SID,
       "pSlot2TL1COND": pSlot2TL1COND,
       "pSlot2TL1Eqpt": pSlot2TL1Eqpt,
       "pSlot2TL1Env": pSlot2TL1Env,
       "pSlot2TL1Srveff": pSlot2TL1Srveff,
       "pSlot2TL1Locn": pSlot2TL1Locn,
       "pSlot2TL1Dirn": pSlot2TL1Dirn,
       "pSlot2SensorType": pSlot2SensorType,
       "pSlot2Index": pSlot2Index,
       "pSlot3Table": pSlot3Table,
       "pSlot3Entry": pSlot3Entry,
       "pSlot3Description": pSlot3Description,
       "pSlot3Desc0": pSlot3Desc0,
       "pSlot3Desc1": pSlot3Desc1,
       "pSlot3Desc2": pSlot3Desc2,
       "pSlot3Desc3": pSlot3Desc3,
       "pSlot3Desc4": pSlot3Desc4,
       "pSlot3Desc5": pSlot3Desc5,
       "pSlot3Configured": pSlot3Configured,
       "pSlot3SendEmail": pSlot3SendEmail,
       "pSlot3SendSNMPTrap": pSlot3SendSNMPTrap,
       "pSlot3IpAddress": pSlot3IpAddress,
       "pSlot3Level0": pSlot3Level0,
       "pSlot3Level1": pSlot3Level1,
       "pSlot3Level2": pSlot3Level2,
       "pSlot3Level3": pSlot3Level3,
       "pSlot3Level4": pSlot3Level4,
       "pSlot3Level5": pSlot3Level5,
       "pSlot3ReadPeriod": pSlot3ReadPeriod,
       "pSlot3Thresh0": pSlot3Thresh0,
       "pSlot3Thresh1": pSlot3Thresh1,
       "pSlot3Thresh2": pSlot3Thresh2,
       "pSlot3Thresh3": pSlot3Thresh3,
       "pSlot3Thresh4": pSlot3Thresh4,
       "pSlot3Thresh5": pSlot3Thresh5,
       "pSlot3ContactStyle": pSlot3ContactStyle,
       "pSlot3Units": pSlot3Units,
       "pSlot3OutputMode": pSlot3OutputMode,
       "pSlot3OutputState": pSlot3OutputState,
       "pSlot3OutputAuto": pSlot3OutputAuto,
       "pSlot3BaudRate": pSlot3BaudRate,
       "pSlot3DataBits": pSlot3DataBits,
       "pSlot3Parity": pSlot3Parity,
       "pSlot3StopBits": pSlot3StopBits,
       "pSlot3Protocol": pSlot3Protocol,
       "pSlot3SerialRTS": pSlot3SerialRTS,
       "pSlot3SerialCTS": pSlot3SerialCTS,
       "pSlot3LiveDescription": pSlot3LiveDescription,
       "pSlot3LiveLevel": pSlot3LiveLevel,
       "pSlot3LiveRaw": pSlot3LiveRaw,
       "pSlot3LiveTime": pSlot3LiveTime,
       "pSlot3Present": pSlot3Present,
       "pSlot3OutputAutoPkg": pSlot3OutputAutoPkg,
       "pSlot3VoltageRange": pSlot3VoltageRange,
       "pSlot3IPPortNum": pSlot3IPPortNum,
       "pSlot3IOFormat": pSlot3IOFormat,
       "pSlot3PortType": pSlot3PortType,
       "pSlot3TL1SID": pSlot3TL1SID,
       "pSlot3TL1COND": pSlot3TL1COND,
       "pSlot3TL1Eqpt": pSlot3TL1Eqpt,
       "pSlot3TL1Env": pSlot3TL1Env,
       "pSlot3TL1Srveff": pSlot3TL1Srveff,
       "pSlot3TL1Locn": pSlot3TL1Locn,
       "pSlot3TL1Dirn": pSlot3TL1Dirn,
       "pSlot3SensorType": pSlot3SensorType,
       "pSlot3Index": pSlot3Index,
       "pSlot4Table": pSlot4Table,
       "pSlot4Entry": pSlot4Entry,
       "pSlot4Description": pSlot4Description,
       "pSlot4Desc0": pSlot4Desc0,
       "pSlot4Desc1": pSlot4Desc1,
       "pSlot4Desc2": pSlot4Desc2,
       "pSlot4Desc3": pSlot4Desc3,
       "pSlot4Desc4": pSlot4Desc4,
       "pSlot4Desc5": pSlot4Desc5,
       "pSlot4Configured": pSlot4Configured,
       "pSlot4SendEmail": pSlot4SendEmail,
       "pSlot4SendSNMPTrap": pSlot4SendSNMPTrap,
       "pSlot4IpAddress": pSlot4IpAddress,
       "pSlot4Level0": pSlot4Level0,
       "pSlot4Level1": pSlot4Level1,
       "pSlot4Level2": pSlot4Level2,
       "pSlot4Level3": pSlot4Level3,
       "pSlot4Level4": pSlot4Level4,
       "pSlot4Level5": pSlot4Level5,
       "pSlot4ReadPeriod": pSlot4ReadPeriod,
       "pSlot4Thresh0": pSlot4Thresh0,
       "pSlot4Thresh1": pSlot4Thresh1,
       "pSlot4Thresh2": pSlot4Thresh2,
       "pSlot4Thresh3": pSlot4Thresh3,
       "pSlot4Thresh4": pSlot4Thresh4,
       "pSlot4Thresh5": pSlot4Thresh5,
       "pSlot4ContactStyle": pSlot4ContactStyle,
       "pSlot4Units": pSlot4Units,
       "pSlot4OutputMode": pSlot4OutputMode,
       "pSlot4OutputState": pSlot4OutputState,
       "pSlot4OutputAuto": pSlot4OutputAuto,
       "pSlot4BaudRate": pSlot4BaudRate,
       "pSlot4DataBits": pSlot4DataBits,
       "pSlot4Parity": pSlot4Parity,
       "pSlot4StopBits": pSlot4StopBits,
       "pSlot4Protocol": pSlot4Protocol,
       "pSlot4SerialRTS": pSlot4SerialRTS,
       "pSlot4SerialCTS": pSlot4SerialCTS,
       "pSlot4LiveDescription": pSlot4LiveDescription,
       "pSlot4LiveLevel": pSlot4LiveLevel,
       "pSlot4LiveRaw": pSlot4LiveRaw,
       "pSlot4LiveTime": pSlot4LiveTime,
       "pSlot4Present": pSlot4Present,
       "pSlot4OutputAutoPkg": pSlot4OutputAutoPkg,
       "pSlot4VoltageRange": pSlot4VoltageRange,
       "pSlot4IPPortNum": pSlot4IPPortNum,
       "pSlot4IOFormat": pSlot4IOFormat,
       "pSlot4PortType": pSlot4PortType,
       "pSlot4TL1SID": pSlot4TL1SID,
       "pSlot4TL1COND": pSlot4TL1COND,
       "pSlot4TL1Eqpt": pSlot4TL1Eqpt,
       "pSlot4TL1Env": pSlot4TL1Env,
       "pSlot4TL1Srveff": pSlot4TL1Srveff,
       "pSlot4TL1Locn": pSlot4TL1Locn,
       "pSlot4TL1Dirn": pSlot4TL1Dirn,
       "pSlot4SensorType": pSlot4SensorType,
       "pSlot4Index": pSlot4Index,
       "pSlot5Table": pSlot5Table,
       "pSlot5Entry": pSlot5Entry,
       "pSlot5Description": pSlot5Description,
       "pSlot5Desc0": pSlot5Desc0,
       "pSlot5Desc1": pSlot5Desc1,
       "pSlot5Desc2": pSlot5Desc2,
       "pSlot5Desc3": pSlot5Desc3,
       "pSlot5Desc4": pSlot5Desc4,
       "pSlot5Desc5": pSlot5Desc5,
       "pSlot5Configured": pSlot5Configured,
       "pSlot5SendEmail": pSlot5SendEmail,
       "pSlot5SendSNMPTrap": pSlot5SendSNMPTrap,
       "pSlot5IpAddress": pSlot5IpAddress,
       "pSlot5Level0": pSlot5Level0,
       "pSlot5Level1": pSlot5Level1,
       "pSlot5Level2": pSlot5Level2,
       "pSlot5Level3": pSlot5Level3,
       "pSlot5Level4": pSlot5Level4,
       "pSlot5Level5": pSlot5Level5,
       "pSlot5ReadPeriod": pSlot5ReadPeriod,
       "pSlot5Thresh0": pSlot5Thresh0,
       "pSlot5Thresh1": pSlot5Thresh1,
       "pSlot5Thresh2": pSlot5Thresh2,
       "pSlot5Thresh3": pSlot5Thresh3,
       "pSlot5Thresh4": pSlot5Thresh4,
       "pSlot5Thresh5": pSlot5Thresh5,
       "pSlot5ContactStyle": pSlot5ContactStyle,
       "pSlot5Units": pSlot5Units,
       "pSlot5OutputMode": pSlot5OutputMode,
       "pSlot5OutputState": pSlot5OutputState,
       "pSlot5OutputAuto": pSlot5OutputAuto,
       "pSlot5BaudRate": pSlot5BaudRate,
       "pSlot5DataBits": pSlot5DataBits,
       "pSlot5Parity": pSlot5Parity,
       "pSlot5StopBits": pSlot5StopBits,
       "pSlot5Protocol": pSlot5Protocol,
       "pSlot5SerialRTS": pSlot5SerialRTS,
       "pSlot5SerialCTS": pSlot5SerialCTS,
       "pSlot5LiveDescription": pSlot5LiveDescription,
       "pSlot5LiveLevel": pSlot5LiveLevel,
       "pSlot5LiveRaw": pSlot5LiveRaw,
       "pSlot5LiveTime": pSlot5LiveTime,
       "pSlot5Present": pSlot5Present,
       "pSlot5OutputAutoPkg": pSlot5OutputAutoPkg,
       "pSlot5VoltageRange": pSlot5VoltageRange,
       "pSlot5IPPortNum": pSlot5IPPortNum,
       "pSlot5IOFormat": pSlot5IOFormat,
       "pSlot5PortType": pSlot5PortType,
       "pSlot5TL1SID": pSlot5TL1SID,
       "pSlot5TL1COND": pSlot5TL1COND,
       "pSlot5TL1Eqpt": pSlot5TL1Eqpt,
       "pSlot5TL1Env": pSlot5TL1Env,
       "pSlot5TL1Srveff": pSlot5TL1Srveff,
       "pSlot5TL1Locn": pSlot5TL1Locn,
       "pSlot5TL1Dirn": pSlot5TL1Dirn,
       "pSlot5SensorType": pSlot5SensorType,
       "pSlot5Index": pSlot5Index,
       "pSlot6Table": pSlot6Table,
       "pSlot6Entry": pSlot6Entry,
       "pSlot6Description": pSlot6Description,
       "pSlot6Desc0": pSlot6Desc0,
       "pSlot6Desc1": pSlot6Desc1,
       "pSlot6Desc2": pSlot6Desc2,
       "pSlot6Desc3": pSlot6Desc3,
       "pSlot6Desc4": pSlot6Desc4,
       "pSlot6Desc5": pSlot6Desc5,
       "pSlot6Configured": pSlot6Configured,
       "pSlot6SendEmail": pSlot6SendEmail,
       "pSlot6SendSNMPTrap": pSlot6SendSNMPTrap,
       "pSlot6IpAddress": pSlot6IpAddress,
       "pSlot6Level0": pSlot6Level0,
       "pSlot6Level1": pSlot6Level1,
       "pSlot6Level2": pSlot6Level2,
       "pSlot6Level3": pSlot6Level3,
       "pSlot6Level4": pSlot6Level4,
       "pSlot6Level5": pSlot6Level5,
       "pSlot6ReadPeriod": pSlot6ReadPeriod,
       "pSlot6Thresh0": pSlot6Thresh0,
       "pSlot6Thresh1": pSlot6Thresh1,
       "pSlot6Thresh2": pSlot6Thresh2,
       "pSlot6Thresh3": pSlot6Thresh3,
       "pSlot6Thresh4": pSlot6Thresh4,
       "pSlot6Thresh5": pSlot6Thresh5,
       "pSlot6ContactStyle": pSlot6ContactStyle,
       "pSlot6Units": pSlot6Units,
       "pSlot6OutputMode": pSlot6OutputMode,
       "pSlot6OutputState": pSlot6OutputState,
       "pSlot6OutputAuto": pSlot6OutputAuto,
       "pSlot6BaudRate": pSlot6BaudRate,
       "pSlot6DataBits": pSlot6DataBits,
       "pSlot6Parity": pSlot6Parity,
       "pSlot6StopBits": pSlot6StopBits,
       "pSlot6Protocol": pSlot6Protocol,
       "pSlot6SerialRTS": pSlot6SerialRTS,
       "pSlot6SerialCTS": pSlot6SerialCTS,
       "pSlot6LiveDescription": pSlot6LiveDescription,
       "pSlot6LiveLevel": pSlot6LiveLevel,
       "pSlot6LiveRaw": pSlot6LiveRaw,
       "pSlot6LiveTime": pSlot6LiveTime,
       "pSlot6Present": pSlot6Present,
       "pSlot6OutputAutoPkg": pSlot6OutputAutoPkg,
       "pSlot6VoltageRange": pSlot6VoltageRange,
       "pSlot6IPPortNum": pSlot6IPPortNum,
       "pSlot6IOFormat": pSlot6IOFormat,
       "pSlot6PortType": pSlot6PortType,
       "pSlot6TL1SID": pSlot6TL1SID,
       "pSlot6TL1COND": pSlot6TL1COND,
       "pSlot6TL1Eqpt": pSlot6TL1Eqpt,
       "pSlot6TL1Env": pSlot6TL1Env,
       "pSlot6TL1Srveff": pSlot6TL1Srveff,
       "pSlot6TL1Locn": pSlot6TL1Locn,
       "pSlot6TL1Dirn": pSlot6TL1Dirn,
       "pSlot6SensorType": pSlot6SensorType,
       "pSlot6Index": pSlot6Index,
       "pNetPortsTable": pNetPortsTable,
       "pNetPortsEntry": pNetPortsEntry,
       "pNetPortsDescription": pNetPortsDescription,
       "pNetPortsIPPortNum": pNetPortsIPPortNum,
       "pNetPortsIndex": pNetPortsIndex,
       "wirelessModem": wirelessModem,
       "wirelessModemBackupIPAddress": wirelessModemBackupIPAddress,
       "wirelessModemTime": wirelessModemTime,
       "wirelessModemTransmit": wirelessModemTransmit,
       "wirelessModemUseWirelessNetwork": wirelessModemUseWirelessNetwork,
       "wirelessModemUseResetTime": wirelessModemUseResetTime,
       "wirelessModemResponseWaitTime": wirelessModemResponseWaitTime,
       "wirelessModemSecondary": wirelessModemSecondary,
       "webmonSecurity": webmonSecurity,
       "webmonSecurityUserLevel": webmonSecurityUserLevel,
       "webmonSecurityUnsecured": webmonSecurityUnsecured,
       "dateTime": dateTime,
       "dateTimeConfigured": dateTimeConfigured,
       "dateTimeIpAddress": dateTimeIpAddress,
       "dateTimeDaylightSaving": dateTimeDaylightSaving,
       "dateTimeDate": dateTimeDate,
       "dateTimeTime": dateTimeTime,
       "dateTimeNegOffset": dateTimeNegOffset,
       "dateTimeUTCOffset": dateTimeUTCOffset,
       "pDCMProtocolTable": pDCMProtocolTable,
       "pDCMProtocolEntry": pDCMProtocolEntry,
       "pDCMProtocolDescription": pDCMProtocolDescription,
       "pDCMProtocolConfigured": pDCMProtocolConfigured,
       "pDCMProtocolBaseDCMAddress": pDCMProtocolBaseDCMAddress,
       "pDCMProtocolIndex": pDCMProtocolIndex,
       "pdialOutTable": pdialOutTable,
       "pdialOutEntry": pdialOutEntry,
       "pdialOutConfigured": pdialOutConfigured,
       "pdialOutName": pdialOutName,
       "pdialOutPassword": pdialOutPassword,
       "pdialOutDialOutNumber": pdialOutDialOutNumber,
       "pdialOutIndex": pdialOutIndex,
       "pderivedDiscreteTable": pderivedDiscreteTable,
       "pderivedDiscreteEntry": pderivedDiscreteEntry,
       "pderivedDiscreteDescription": pderivedDiscreteDescription,
       "pderivedDiscreteDesc0": pderivedDiscreteDesc0,
       "pderivedDiscreteDesc1": pderivedDiscreteDesc1,
       "pderivedDiscreteConfigured": pderivedDiscreteConfigured,
       "pderivedDiscreteSendEmail": pderivedDiscreteSendEmail,
       "pderivedDiscreteSendSNMPTrap": pderivedDiscreteSendSNMPTrap,
       "pderivedDiscreteLevel0": pderivedDiscreteLevel0,
       "pderivedDiscreteLevel1": pderivedDiscreteLevel1,
       "pderivedDiscreteLiveDescription": pderivedDiscreteLiveDescription,
       "pderivedDiscreteLiveLevel": pderivedDiscreteLiveLevel,
       "pderivedDiscreteLiveTime": pderivedDiscreteLiveTime,
       "pderivedDiscreteElementAPkg": pderivedDiscreteElementAPkg,
       "pderivedDiscreteElementAPoint": pderivedDiscreteElementAPoint,
       "pderivedDiscreteElementBPkg": pderivedDiscreteElementBPkg,
       "pderivedDiscreteElementBPoint": pderivedDiscreteElementBPoint,
       "pderivedDiscreteDiscreteFormula": pderivedDiscreteDiscreteFormula,
       "pderivedDiscreteTL1SID": pderivedDiscreteTL1SID,
       "pderivedDiscreteTL1COND": pderivedDiscreteTL1COND,
       "pderivedDiscreteTL1Eqpt": pderivedDiscreteTL1Eqpt,
       "pderivedDiscreteTL1Env": pderivedDiscreteTL1Env,
       "pderivedDiscreteTL1Srveff": pderivedDiscreteTL1Srveff,
       "pderivedDiscreteTL1Locn": pderivedDiscreteTL1Locn,
       "pderivedDiscreteTL1Dirn": pderivedDiscreteTL1Dirn,
       "pderivedDiscreteIndex": pderivedDiscreteIndex,
       "license": license,
       "licenseDescription": licenseDescription,
       "licenseLicenseKey": licenseLicenseKey,
       "licenseExpires": licenseExpires,
       "licenseAllowTL1": licenseAllowTL1,
       "pe2aHostTable": pe2aHostTable,
       "pe2aHostEntry": pe2aHostEntry,
       "pe2aHostDescription": pe2aHostDescription,
       "pe2aHostConfigured": pe2aHostConfigured,
       "pe2aHostIpAddress": pe2aHostIpAddress,
       "pe2aHostLevel0": pe2aHostLevel0,
       "pe2aHostLevel1": pe2aHostLevel1,
       "pe2aHostLevel2": pe2aHostLevel2,
       "pe2aHostRosterID": pe2aHostRosterID,
       "pe2aHostPollAddress": pe2aHostPollAddress,
       "pe2aHostIPPortNum": pe2aHostIPPortNum,
       "pe2aHostTL1SID": pe2aHostTL1SID,
       "pe2aHostTL1COND": pe2aHostTL1COND,
       "pe2aHostTL1Eqpt": pe2aHostTL1Eqpt,
       "pe2aHostTL1Env": pe2aHostTL1Env,
       "pe2aHostTL1Srveff": pe2aHostTL1Srveff,
       "pe2aHostTL1Locn": pe2aHostTL1Locn,
       "pe2aHostTL1Dirn": pe2aHostTL1Dirn,
       "pe2aHostIndex": pe2aHostIndex,
       "pderivedAnalogTable": pderivedAnalogTable,
       "pderivedAnalogEntry": pderivedAnalogEntry,
       "pderivedAnalogDescription": pderivedAnalogDescription,
       "pderivedAnalogDesc0": pderivedAnalogDesc0,
       "pderivedAnalogDesc1": pderivedAnalogDesc1,
       "pderivedAnalogDesc2": pderivedAnalogDesc2,
       "pderivedAnalogDesc3": pderivedAnalogDesc3,
       "pderivedAnalogDesc4": pderivedAnalogDesc4,
       "pderivedAnalogConfigured": pderivedAnalogConfigured,
       "pderivedAnalogSendEmail": pderivedAnalogSendEmail,
       "pderivedAnalogSendSNMPTrap": pderivedAnalogSendSNMPTrap,
       "pderivedAnalogLevel0": pderivedAnalogLevel0,
       "pderivedAnalogLevel1": pderivedAnalogLevel1,
       "pderivedAnalogLevel2": pderivedAnalogLevel2,
       "pderivedAnalogLevel3": pderivedAnalogLevel3,
       "pderivedAnalogLevel4": pderivedAnalogLevel4,
       "pderivedAnalogThresh0": pderivedAnalogThresh0,
       "pderivedAnalogThresh1": pderivedAnalogThresh1,
       "pderivedAnalogThresh2": pderivedAnalogThresh2,
       "pderivedAnalogThresh3": pderivedAnalogThresh3,
       "pderivedAnalogThresh4": pderivedAnalogThresh4,
       "pderivedAnalogThresh5": pderivedAnalogThresh5,
       "pderivedAnalogUnits": pderivedAnalogUnits,
       "pderivedAnalogLiveDescription": pderivedAnalogLiveDescription,
       "pderivedAnalogLiveLevel": pderivedAnalogLiveLevel,
       "pderivedAnalogLiveRaw": pderivedAnalogLiveRaw,
       "pderivedAnalogLiveTime": pderivedAnalogLiveTime,
       "pderivedAnalogElementAPkg": pderivedAnalogElementAPkg,
       "pderivedAnalogElementAPoint": pderivedAnalogElementAPoint,
       "pderivedAnalogElementBPkg": pderivedAnalogElementBPkg,
       "pderivedAnalogElementBPoint": pderivedAnalogElementBPoint,
       "pderivedAnalogFormula": pderivedAnalogFormula,
       "pderivedAnalogTL1SID": pderivedAnalogTL1SID,
       "pderivedAnalogTL1COND": pderivedAnalogTL1COND,
       "pderivedAnalogTL1Eqpt": pderivedAnalogTL1Eqpt,
       "pderivedAnalogTL1Env": pderivedAnalogTL1Env,
       "pderivedAnalogTL1Srveff": pderivedAnalogTL1Srveff,
       "pderivedAnalogTL1Locn": pderivedAnalogTL1Locn,
       "pderivedAnalogTL1Dirn": pderivedAnalogTL1Dirn,
       "pderivedAnalogIndex": pderivedAnalogIndex,
       "pgpsTable": pgpsTable,
       "pgpsEntry": pgpsEntry,
       "pgpsDescription": pgpsDescription,
       "pgpsDesc0": pgpsDesc0,
       "pgpsDesc1": pgpsDesc1,
       "pgpsDesc2": pgpsDesc2,
       "pgpsDesc3": pgpsDesc3,
       "pgpsDesc4": pgpsDesc4,
       "pgpsConfigured": pgpsConfigured,
       "pgpsSendEmail": pgpsSendEmail,
       "pgpsSendSNMPTrap": pgpsSendSNMPTrap,
       "pgpsLevel0": pgpsLevel0,
       "pgpsLevel1": pgpsLevel1,
       "pgpsLevel2": pgpsLevel2,
       "pgpsLevel3": pgpsLevel3,
       "pgpsLevel4": pgpsLevel4,
       "pgpsThresh0": pgpsThresh0,
       "pgpsThresh1": pgpsThresh1,
       "pgpsThresh2": pgpsThresh2,
       "pgpsThresh3": pgpsThresh3,
       "pgpsThresh4": pgpsThresh4,
       "pgpsThresh5": pgpsThresh5,
       "pgpsUnits": pgpsUnits,
       "pgpsLiveDescription": pgpsLiveDescription,
       "pgpsLiveLevel": pgpsLiveLevel,
       "pgpsLiveRaw": pgpsLiveRaw,
       "pgpsLiveTime": pgpsLiveTime,
       "pgpsTL1SID": pgpsTL1SID,
       "pgpsTL1COND": pgpsTL1COND,
       "pgpsTL1Eqpt": pgpsTL1Eqpt,
       "pgpsTL1Env": pgpsTL1Env,
       "pgpsTL1Srveff": pgpsTL1Srveff,
       "pgpsTL1Locn": pgpsTL1Locn,
       "pgpsTL1Dirn": pgpsTL1Dirn,
       "pgpsIndex": pgpsIndex,
       "pportRedirectTable": pportRedirectTable,
       "pportRedirectEntry": pportRedirectEntry,
       "pportRedirectDescription": pportRedirectDescription,
       "pportRedirectConfigured": pportRedirectConfigured,
       "pportRedirectIpAddress": pportRedirectIpAddress,
       "pportRedirectReadPeriod": pportRedirectReadPeriod,
       "pportRedirectRosterID": pportRedirectRosterID,
       "pportRedirectIPPortNum": pportRedirectIPPortNum,
       "pportRedirectIndex": pportRedirectIndex,
       "pscheduleATable": pscheduleATable,
       "pscheduleAEntry": pscheduleAEntry,
       "pscheduleADayOfWeek": pscheduleADayOfWeek,
       "pscheduleAConfiguredState": pscheduleAConfiguredState,
       "pscheduleAConfigured1": pscheduleAConfigured1,
       "pscheduleAConfigured2": pscheduleAConfigured2,
       "pscheduleAConfigured3": pscheduleAConfigured3,
       "pscheduleAConfigured4": pscheduleAConfigured4,
       "pscheduleATime0": pscheduleATime0,
       "pscheduleATime1": pscheduleATime1,
       "pscheduleATime2": pscheduleATime2,
       "pscheduleATime3": pscheduleATime3,
       "pscheduleATime4": pscheduleATime4,
       "pscheduleATime5": pscheduleATime5,
       "pscheduleAIndex": pscheduleAIndex,
       "pscheduleBTable": pscheduleBTable,
       "pscheduleBEntry": pscheduleBEntry,
       "pscheduleBDayOfWeek": pscheduleBDayOfWeek,
       "pscheduleBConfiguredState": pscheduleBConfiguredState,
       "pscheduleBConfigured1": pscheduleBConfigured1,
       "pscheduleBConfigured2": pscheduleBConfigured2,
       "pscheduleBConfigured3": pscheduleBConfigured3,
       "pscheduleBConfigured4": pscheduleBConfigured4,
       "pscheduleBTime0": pscheduleBTime0,
       "pscheduleBTime1": pscheduleBTime1,
       "pscheduleBTime2": pscheduleBTime2,
       "pscheduleBTime3": pscheduleBTime3,
       "pscheduleBTime4": pscheduleBTime4,
       "pscheduleBTime5": pscheduleBTime5,
       "pscheduleBIndex": pscheduleBIndex,
       "pscheduleCTable": pscheduleCTable,
       "pscheduleCEntry": pscheduleCEntry,
       "pscheduleCDayOfWeek": pscheduleCDayOfWeek,
       "pscheduleCConfiguredState": pscheduleCConfiguredState,
       "pscheduleCConfigured1": pscheduleCConfigured1,
       "pscheduleCConfigured2": pscheduleCConfigured2,
       "pscheduleCConfigured3": pscheduleCConfigured3,
       "pscheduleCConfigured4": pscheduleCConfigured4,
       "pscheduleCTime0": pscheduleCTime0,
       "pscheduleCTime1": pscheduleCTime1,
       "pscheduleCTime2": pscheduleCTime2,
       "pscheduleCTime3": pscheduleCTime3,
       "pscheduleCTime4": pscheduleCTime4,
       "pscheduleCTime5": pscheduleCTime5,
       "pscheduleCIndex": pscheduleCIndex,
       "pscheduleDTable": pscheduleDTable,
       "pscheduleDEntry": pscheduleDEntry,
       "pscheduleDDayOfWeek": pscheduleDDayOfWeek,
       "pscheduleDConfiguredState": pscheduleDConfiguredState,
       "pscheduleDConfigured1": pscheduleDConfigured1,
       "pscheduleDConfigured2": pscheduleDConfigured2,
       "pscheduleDConfigured3": pscheduleDConfigured3,
       "pscheduleDConfigured4": pscheduleDConfigured4,
       "pscheduleDTime0": pscheduleDTime0,
       "pscheduleDTime1": pscheduleDTime1,
       "pscheduleDTime2": pscheduleDTime2,
       "pscheduleDTime3": pscheduleDTime3,
       "pscheduleDTime4": pscheduleDTime4,
       "pscheduleDTime5": pscheduleDTime5,
       "pscheduleDIndex": pscheduleDIndex,
       "tl1Settings": tl1Settings,
       "tl1SettingsTL1Issue": tl1SettingsTL1Issue,
       "pDCPFProtocolTable": pDCPFProtocolTable,
       "pDCPFProtocolEntry": pDCPFProtocolEntry,
       "pDCPFProtocolDescription": pDCPFProtocolDescription,
       "pDCPFProtocolConfigured": pDCPFProtocolConfigured,
       "pDCPFProtocolBaseDCPFDisplay": pDCPFProtocolBaseDCPFDisplay,
       "pDCPFProtocolIndex": pDCPFProtocolIndex,
       "dcpfSettings": dcpfSettings,
       "dcpfSettingsDCPFAddress": dcpfSettingsDCPFAddress,
       "pTABSProtocolTable": pTABSProtocolTable,
       "pTABSProtocolEntry": pTABSProtocolEntry,
       "pTABSProtocolDescription": pTABSProtocolDescription,
       "pTABSProtocolConfigured": pTABSProtocolConfigured,
       "pTABSProtocolBaseTABSDisplay": pTABSProtocolBaseTABSDisplay,
       "pTABSProtocolIndex": pTABSProtocolIndex,
       "tabsSettings": tabsSettings,
       "tabsSettingsTABSAddress": tabsSettingsTABSAddress,
       "psnmpCommandsTable": psnmpCommandsTable,
       "psnmpCommandsEntry": psnmpCommandsEntry,
       "psnmpCommandsDescription": psnmpCommandsDescription,
       "psnmpCommandsConfigured": psnmpCommandsConfigured,
       "psnmpCommandsIpAddress": psnmpCommandsIpAddress,
       "psnmpCommandsGet": psnmpCommandsGet,
       "psnmpCommandsSnmpVersion": psnmpCommandsSnmpVersion,
       "psnmpCommandsOutputAuto": psnmpCommandsOutputAuto,
       "psnmpCommandsOutputAutoPkg": psnmpCommandsOutputAutoPkg,
       "psnmpCommandsIPPortNum": psnmpCommandsIPPortNum,
       "psnmpCommandsOID": psnmpCommandsOID,
       "psnmpCommandsSNMPVarbindType": psnmpCommandsSNMPVarbindType,
       "psnmpCommandsTextNormal": psnmpCommandsTextNormal,
       "psnmpCommandsTextCritical": psnmpCommandsTextCritical,
       "psnmpCommandsTextMajor": psnmpCommandsTextMajor,
       "psnmpCommandsTextMinor": psnmpCommandsTextMinor,
       "psnmpCommandsTextStatus": psnmpCommandsTextStatus,
       "psnmpCommandsIndex": psnmpCommandsIndex,
       "battMon": battMon,
       "battMonConfigured": battMonConfigured,
       "battMonOutputAuto": battMonOutputAuto,
       "battMonOutputAutoPkg": battMonOutputAutoPkg,
       "pBankInfoTable": pBankInfoTable,
       "pBankInfoEntry": pBankInfoEntry,
       "pBankInfoDescription": pBankInfoDescription,
       "pBankInfoConfigured": pBankInfoConfigured,
       "pBankInfoPresent": pBankInfoPresent,
       "pBankInfoSlotId": pBankInfoSlotId,
       "pBankInfoIOFormat": pBankInfoIOFormat,
       "pBankInfoIndex": pBankInfoIndex,
       "configObjectGroup": configObjectGroup,
       "triggers": triggers,
       "resetDevice": resetDevice,
       "commitAccountChanges": commitAccountChanges,
       "resendEvents": resendEvents}
)
