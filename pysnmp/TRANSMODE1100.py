# SNMP MIB module (TRANSMODE1100) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRANSMODE1100
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:21 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

transmode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11857)
)
transmode.setRevisions(
        ("2003-10-06 11:00",
         "2003-05-13 16:30",
         "2003-05-13 16:30",
         "2003-04-04 11:30",
         "2003-03-26 15:40",
         "2003-02-20 13:10",
         "2002-11-27 14:45",
         "2002-11-18 16:35",
         "2002-11-05 15:20",
         "2002-10-30 17:05",
         "2002-10-23 16:05",
         "2002-09-30 13:57")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmClass(Integer32, TextualConvention):
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
        *(("communications", 1),
          ("environmental", 5),
          ("equipment", 4),
          ("processing", 3),
          ("qos", 2),
          ("unknown", 0))
    )



class PerceivedSeverity(Integer32, TextualConvention):
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
        *(("cleared", 5),
          ("critical", 1),
          ("indeterminate", 0),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )



class AlarmSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("none", 5),
          ("warning", 4))
    )



class RowStatus(Integer32, TextualConvention):
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )



class OwnerString(DisplayString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class TrafficStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notraffic", 1),
          ("traffic", 2))
    )



class TxMode76(Integer32, TextualConvention):
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
        *(("disabled", 2),
          ("forcedon", 3),
          ("normal", 1))
    )



class TxMode75(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("normal", 1))
    )



class Present(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )



class PowerStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )



class PowerType(Integer32, TextualConvention):
    status = "current"
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
        *(("power9048", 2),
          ("power9122", 5),
          ("power9148", 4),
          ("power9220", 3),
          ("unknown", 1))
    )



class MuxType(Integer32, TextualConvention):
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
        *(("mux8030", 2),
          ("mux8031", 3),
          ("mux8032", 4),
          ("mux8033", 5),
          ("mux8034", 6),
          ("none", 1))
    )



class ExternalAlarmLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activehigh", 2),
          ("activelow", 1))
    )



class AlarmStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("ceased", 2))
    )



class Switch(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )



class PortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 2),
          ("line", 1))
    )



class RackNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )



class SlotNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )



class BoardNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )



class SlotNumberPS(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 15),
    )



class SlotNumberNmb(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 13),
    )



class AlarmAcknowledge(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("acknowledge", 1)
    )



class LineLoopMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("looptest", 2),
          ("normal", 1))
    )



class CDRMode(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("auto3R", 1),
          ("bypass2R", 2),
          ("custom", 3),
          ("fddiOR100Base-FX", 4),
          ("fibreChannel", 9),
          ("fibreChannelx2", 10),
          ("gigabitEthernet", 8),
          ("gigabitEthernetx2", 12),
          ("stm16orOC-48", 11),
          ("stm1orOC-3", 5),
          ("stm4orOC-12", 7),
          ("video270Mbps", 6))
    )



class TrmDate(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )



class TrmTime(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class SecurityMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )



class SpeedLimit75(Integer32, TextualConvention):
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
        *(("lowLimit", 2),
          ("mediumLimit", 3),
          ("noLimit", 1))
    )



class SpeedLimit76(Integer32, TextualConvention):
    status = "current"
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
        *(("highLimit", 4),
          ("lowLimit", 2),
          ("mediumLimit", 3),
          ("noLimit", 1))
    )



class CascadeStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("deactivated", 1),
          ("disconnecting", 5),
          ("failure", 4),
          ("initializing", 2),
          ("ok", 3))
    )



class CascadeMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2))
    )



class CDR55Mode(Integer32, TextualConvention):
    status = "current"
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
        *(("escon", 1),
          ("fddiOR100Base-FX", 3),
          ("stm1orOC-3", 2),
          ("syncSignal16-32Mbps", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_System1100_ObjectIdentity = ObjectIdentity
system1100 = _System1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1)
)
_TrmAlarmHandling_ObjectIdentity = ObjectIdentity
trmAlarmHandling = _TrmAlarmHandling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1)
)
_TrmAlarmConfig_ObjectIdentity = ObjectIdentity
trmAlarmConfig = _TrmAlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1)
)
_TrmAlarmGeneral_ObjectIdentity = ObjectIdentity
trmAlarmGeneral = _TrmAlarmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1)
)


class _TrmAutoAcknowledge_Type(Integer32):
    """Custom type trmAutoAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_TrmAutoAcknowledge_Type.__name__ = "Integer32"
_TrmAutoAcknowledge_Object = MibScalar
trmAutoAcknowledge = _TrmAutoAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 1),
    _TrmAutoAcknowledge_Type()
)
trmAutoAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmAutoAcknowledge.setStatus("current")


class _TrmClearAlarmLog_Type(Integer32):
    """Custom type trmClearAlarmLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_TrmClearAlarmLog_Type.__name__ = "Integer32"
_TrmClearAlarmLog_Object = MibScalar
trmClearAlarmLog = _TrmClearAlarmLog_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 2),
    _TrmClearAlarmLog_Type()
)
trmClearAlarmLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmClearAlarmLog.setStatus("current")


class _TrmTemperature_Type(Integer32):
    """Custom type trmTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("farenheit", 2))
    )


_TrmTemperature_Type.__name__ = "Integer32"
_TrmTemperature_Object = MibScalar
trmTemperature = _TrmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 3),
    _TrmTemperature_Type()
)
trmTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmTemperature.setStatus("current")


class _TrmAlarmTemperatureHigh_Type(Integer32):
    """Custom type trmAlarmTemperatureHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32768),
    )


_TrmAlarmTemperatureHigh_Type.__name__ = "Integer32"
_TrmAlarmTemperatureHigh_Object = MibScalar
trmAlarmTemperatureHigh = _TrmAlarmTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 4),
    _TrmAlarmTemperatureHigh_Type()
)
trmAlarmTemperatureHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmAlarmTemperatureHigh.setStatus("current")


class _TrmAlarmTemperatureHighHyst_Type(Integer32):
    """Custom type trmAlarmTemperatureHighHyst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32768),
    )


_TrmAlarmTemperatureHighHyst_Type.__name__ = "Integer32"
_TrmAlarmTemperatureHighHyst_Object = MibScalar
trmAlarmTemperatureHighHyst = _TrmAlarmTemperatureHighHyst_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 5),
    _TrmAlarmTemperatureHighHyst_Type()
)
trmAlarmTemperatureHighHyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmAlarmTemperatureHighHyst.setStatus("current")


class _TrmAlarmTemperatureLow_Type(Integer32):
    """Custom type trmAlarmTemperatureLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32768),
    )


_TrmAlarmTemperatureLow_Type.__name__ = "Integer32"
_TrmAlarmTemperatureLow_Object = MibScalar
trmAlarmTemperatureLow = _TrmAlarmTemperatureLow_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 6),
    _TrmAlarmTemperatureLow_Type()
)
trmAlarmTemperatureLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmAlarmTemperatureLow.setStatus("current")


class _TrmAlarmTemperatureLowHyst_Type(Integer32):
    """Custom type trmAlarmTemperatureLowHyst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32768),
    )


_TrmAlarmTemperatureLowHyst_Type.__name__ = "Integer32"
_TrmAlarmTemperatureLowHyst_Object = MibScalar
trmAlarmTemperatureLowHyst = _TrmAlarmTemperatureLowHyst_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 7),
    _TrmAlarmTemperatureLowHyst_Type()
)
trmAlarmTemperatureLowHyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmAlarmTemperatureLowHyst.setStatus("current")


class _TrmPluginReset_Type(Integer32):
    """Custom type trmPluginReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_TrmPluginReset_Type.__name__ = "Integer32"
_TrmPluginReset_Object = MibScalar
trmPluginReset = _TrmPluginReset_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 8),
    _TrmPluginReset_Type()
)
trmPluginReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmPluginReset.setStatus("current")
_TrmOpticalInputPowerHighPINLine_Type = Integer32
_TrmOpticalInputPowerHighPINLine_Object = MibScalar
trmOpticalInputPowerHighPINLine = _TrmOpticalInputPowerHighPINLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 9),
    _TrmOpticalInputPowerHighPINLine_Type()
)
trmOpticalInputPowerHighPINLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmOpticalInputPowerHighPINLine.setStatus("current")
_TrmOpticalInputPowerHighAPDLine_Type = Integer32
_TrmOpticalInputPowerHighAPDLine_Object = MibScalar
trmOpticalInputPowerHighAPDLine = _TrmOpticalInputPowerHighAPDLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 10),
    _TrmOpticalInputPowerHighAPDLine_Type()
)
trmOpticalInputPowerHighAPDLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmOpticalInputPowerHighAPDLine.setStatus("current")
_TrmOpticalInputPowerLowPINLine_Type = Integer32
_TrmOpticalInputPowerLowPINLine_Object = MibScalar
trmOpticalInputPowerLowPINLine = _TrmOpticalInputPowerLowPINLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 11),
    _TrmOpticalInputPowerLowPINLine_Type()
)
trmOpticalInputPowerLowPINLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmOpticalInputPowerLowPINLine.setStatus("current")
_TrmOpticalInputPowerLowAPDLine_Type = Integer32
_TrmOpticalInputPowerLowAPDLine_Object = MibScalar
trmOpticalInputPowerLowAPDLine = _TrmOpticalInputPowerLowAPDLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 12),
    _TrmOpticalInputPowerLowAPDLine_Type()
)
trmOpticalInputPowerLowAPDLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmOpticalInputPowerLowAPDLine.setStatus("current")
_TrmCascade_Type = CascadeMode
_TrmCascade_Object = MibScalar
trmCascade = _TrmCascade_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 13),
    _TrmCascade_Type()
)
trmCascade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmCascade.setStatus("current")
_TrmCascadeStatus_Type = CascadeStatus
_TrmCascadeStatus_Object = MibScalar
trmCascadeStatus = _TrmCascadeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 14),
    _TrmCascadeStatus_Type()
)
trmCascadeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmCascadeStatus.setStatus("current")
_TrmOpticalInputPowerHighAPDLine2_Type = Integer32
_TrmOpticalInputPowerHighAPDLine2_Object = MibScalar
trmOpticalInputPowerHighAPDLine2 = _TrmOpticalInputPowerHighAPDLine2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 15),
    _TrmOpticalInputPowerHighAPDLine2_Type()
)
trmOpticalInputPowerHighAPDLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmOpticalInputPowerHighAPDLine2.setStatus("current")
_TrmOpticalInputPowerLowAPDLine2_Type = Integer32
_TrmOpticalInputPowerLowAPDLine2_Object = MibScalar
trmOpticalInputPowerLowAPDLine2 = _TrmOpticalInputPowerLowAPDLine2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 16),
    _TrmOpticalInputPowerLowAPDLine2_Type()
)
trmOpticalInputPowerLowAPDLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmOpticalInputPowerLowAPDLine2.setStatus("current")
_TrmOpticalInputPowerHigh850Client_Type = Integer32
_TrmOpticalInputPowerHigh850Client_Object = MibScalar
trmOpticalInputPowerHigh850Client = _TrmOpticalInputPowerHigh850Client_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 17),
    _TrmOpticalInputPowerHigh850Client_Type()
)
trmOpticalInputPowerHigh850Client.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmOpticalInputPowerHigh850Client.setStatus("current")
_TrmOpticalInputPowerHigh1310Client_Type = Integer32
_TrmOpticalInputPowerHigh1310Client_Object = MibScalar
trmOpticalInputPowerHigh1310Client = _TrmOpticalInputPowerHigh1310Client_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 18),
    _TrmOpticalInputPowerHigh1310Client_Type()
)
trmOpticalInputPowerHigh1310Client.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmOpticalInputPowerHigh1310Client.setStatus("current")
_TrmOpticalInputPowerLow850Client_Type = Integer32
_TrmOpticalInputPowerLow850Client_Object = MibScalar
trmOpticalInputPowerLow850Client = _TrmOpticalInputPowerLow850Client_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 19),
    _TrmOpticalInputPowerLow850Client_Type()
)
trmOpticalInputPowerLow850Client.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmOpticalInputPowerLow850Client.setStatus("current")
_TrmOpticalInputPowerLow1310Client_Type = Integer32
_TrmOpticalInputPowerLow1310Client_Object = MibScalar
trmOpticalInputPowerLow1310Client = _TrmOpticalInputPowerLow1310Client_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 1, 20),
    _TrmOpticalInputPowerLow1310Client_Type()
)
trmOpticalInputPowerLow1310Client.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmOpticalInputPowerLow1310Client.setStatus("current")
_TrmAlarmSeverity_ObjectIdentity = ObjectIdentity
trmAlarmSeverity = _TrmAlarmSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 2)
)
_TrmAlarmSeverityTable_Object = MibTable
trmAlarmSeverityTable = _TrmAlarmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    trmAlarmSeverityTable.setStatus("current")
_TrmAlarmSeverityEntry_Object = MibTableRow
trmAlarmSeverityEntry = _TrmAlarmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 2, 1, 1)
)
trmAlarmSeverityEntry.setIndexNames(
    (0, "TRANSMODE1100", "trmAlarmSeverityId"),
)
if mibBuilder.loadTexts:
    trmAlarmSeverityEntry.setStatus("current")


class _TrmAlarmSeverityId_Type(Integer32):
    """Custom type trmAlarmSeverityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrmAlarmSeverityId_Type.__name__ = "Integer32"
_TrmAlarmSeverityId_Object = MibTableColumn
trmAlarmSeverityId = _TrmAlarmSeverityId_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 2, 1, 1, 1),
    _TrmAlarmSeverityId_Type()
)
trmAlarmSeverityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmAlarmSeverityId.setStatus("current")
_TrmAlarmSeverityName_Type = DisplayString
_TrmAlarmSeverityName_Object = MibTableColumn
trmAlarmSeverityName = _TrmAlarmSeverityName_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 2, 1, 1, 2),
    _TrmAlarmSeverityName_Type()
)
trmAlarmSeverityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmSeverityName.setStatus("current")
_TrmAlarmSeverityLevel_Type = AlarmSeverity
_TrmAlarmSeverityLevel_Object = MibTableColumn
trmAlarmSeverityLevel = _TrmAlarmSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 2, 1, 1, 3),
    _TrmAlarmSeverityLevel_Type()
)
trmAlarmSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmAlarmSeverityLevel.setStatus("current")
_TrmAlarmExternal_ObjectIdentity = ObjectIdentity
trmAlarmExternal = _TrmAlarmExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 3)
)
_TrmAlarmExternalTable_Object = MibTable
trmAlarmExternalTable = _TrmAlarmExternalTable_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    trmAlarmExternalTable.setStatus("current")
_TrmAlarmExternalEntry_Object = MibTableRow
trmAlarmExternalEntry = _TrmAlarmExternalEntry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 3, 1, 1)
)
trmAlarmExternalEntry.setIndexNames(
    (0, "TRANSMODE1100", "trmAlarmExternalId"),
)
if mibBuilder.loadTexts:
    trmAlarmExternalEntry.setStatus("current")


class _TrmAlarmExternalId_Type(Integer32):
    """Custom type trmAlarmExternalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrmAlarmExternalId_Type.__name__ = "Integer32"
_TrmAlarmExternalId_Object = MibTableColumn
trmAlarmExternalId = _TrmAlarmExternalId_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 3, 1, 1, 1),
    _TrmAlarmExternalId_Type()
)
trmAlarmExternalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmAlarmExternalId.setStatus("current")
_TrmAlarmExternalName_Type = DisplayString
_TrmAlarmExternalName_Object = MibTableColumn
trmAlarmExternalName = _TrmAlarmExternalName_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 3, 1, 1, 2),
    _TrmAlarmExternalName_Type()
)
trmAlarmExternalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmAlarmExternalName.setStatus("current")
_TrmAlarmExternalLevel_Type = ExternalAlarmLevel
_TrmAlarmExternalLevel_Object = MibTableColumn
trmAlarmExternalLevel = _TrmAlarmExternalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 1, 3, 1, 1, 3),
    _TrmAlarmExternalLevel_Type()
)
trmAlarmExternalLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmAlarmExternalLevel.setStatus("current")
_TrmAlarmLog_ObjectIdentity = ObjectIdentity
trmAlarmLog = _TrmAlarmLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2)
)
_TrmAlarmLogTable_Object = MibTable
trmAlarmLogTable = _TrmAlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    trmAlarmLogTable.setStatus("current")
_TrmAlarmLogEntry_Object = MibTableRow
trmAlarmLogEntry = _TrmAlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1, 1)
)
trmAlarmLogEntry.setIndexNames(
    (0, "TRANSMODE1100", "trmAlarmLogIndex"),
)
if mibBuilder.loadTexts:
    trmAlarmLogEntry.setStatus("current")


class _TrmAlarmLogIndex_Type(Integer32):
    """Custom type trmAlarmLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrmAlarmLogIndex_Type.__name__ = "Integer32"
_TrmAlarmLogIndex_Object = MibTableColumn
trmAlarmLogIndex = _TrmAlarmLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1, 1, 1),
    _TrmAlarmLogIndex_Type()
)
trmAlarmLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmAlarmLogIndex.setStatus("current")
_TrmAlarmLogRackNumber_Type = RackNumber
_TrmAlarmLogRackNumber_Object = MibTableColumn
trmAlarmLogRackNumber = _TrmAlarmLogRackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1, 1, 2),
    _TrmAlarmLogRackNumber_Type()
)
trmAlarmLogRackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmLogRackNumber.setStatus("current")
_TrmAlarmLogSlotNumber_Type = SlotNumber
_TrmAlarmLogSlotNumber_Object = MibTableColumn
trmAlarmLogSlotNumber = _TrmAlarmLogSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1, 1, 3),
    _TrmAlarmLogSlotNumber_Type()
)
trmAlarmLogSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmLogSlotNumber.setStatus("current")
_TrmAlarmLogName_Type = DisplayString
_TrmAlarmLogName_Object = MibTableColumn
trmAlarmLogName = _TrmAlarmLogName_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1, 1, 4),
    _TrmAlarmLogName_Type()
)
trmAlarmLogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmLogName.setStatus("current")
_TrmAlarmLogSeverity_Type = PerceivedSeverity
_TrmAlarmLogSeverity_Object = MibTableColumn
trmAlarmLogSeverity = _TrmAlarmLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1, 1, 5),
    _TrmAlarmLogSeverity_Type()
)
trmAlarmLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmLogSeverity.setStatus("current")
_TrmAlarmLogUnit_Type = DisplayString
_TrmAlarmLogUnit_Object = MibTableColumn
trmAlarmLogUnit = _TrmAlarmLogUnit_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1, 1, 6),
    _TrmAlarmLogUnit_Type()
)
trmAlarmLogUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmLogUnit.setStatus("current")
_TrmAlarmLogSerialNumber_Type = DisplayString
_TrmAlarmLogSerialNumber_Object = MibTableColumn
trmAlarmLogSerialNumber = _TrmAlarmLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1, 1, 7),
    _TrmAlarmLogSerialNumber_Type()
)
trmAlarmLogSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmLogSerialNumber.setStatus("current")
_TrmAlarmLogActTime_Type = DisplayString
_TrmAlarmLogActTime_Object = MibTableColumn
trmAlarmLogActTime = _TrmAlarmLogActTime_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1, 1, 8),
    _TrmAlarmLogActTime_Type()
)
trmAlarmLogActTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmLogActTime.setStatus("current")
_TrmAlarmLogDeactTime_Type = DisplayString
_TrmAlarmLogDeactTime_Object = MibTableColumn
trmAlarmLogDeactTime = _TrmAlarmLogDeactTime_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1, 1, 9),
    _TrmAlarmLogDeactTime_Type()
)
trmAlarmLogDeactTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmLogDeactTime.setStatus("current")
_TrmAlarmLogAckTime_Type = DisplayString
_TrmAlarmLogAckTime_Object = MibTableColumn
trmAlarmLogAckTime = _TrmAlarmLogAckTime_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1, 1, 10),
    _TrmAlarmLogAckTime_Type()
)
trmAlarmLogAckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmLogAckTime.setStatus("current")
_TrmAlarmLogAckUser_Type = DisplayString
_TrmAlarmLogAckUser_Object = MibTableColumn
trmAlarmLogAckUser = _TrmAlarmLogAckUser_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 2, 1, 1, 11),
    _TrmAlarmLogAckUser_Type()
)
trmAlarmLogAckUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmLogAckUser.setStatus("current")
_TrmAlarmActive_ObjectIdentity = ObjectIdentity
trmAlarmActive = _TrmAlarmActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3)
)
_TrmAlarmActiveGeneral_ObjectIdentity = ObjectIdentity
trmAlarmActiveGeneral = _TrmAlarmActiveGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 1)
)


class _TrmAlarmActiveCounter_Type(Integer32):
    """Custom type trmAlarmActiveCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32768),
    )


_TrmAlarmActiveCounter_Type.__name__ = "Integer32"
_TrmAlarmActiveCounter_Object = MibScalar
trmAlarmActiveCounter = _TrmAlarmActiveCounter_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 1, 1),
    _TrmAlarmActiveCounter_Type()
)
trmAlarmActiveCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmActiveCounter.setStatus("current")
_TrmAlarmActiveAcknowledgeAllDeact_Type = AlarmAcknowledge
_TrmAlarmActiveAcknowledgeAllDeact_Object = MibScalar
trmAlarmActiveAcknowledgeAllDeact = _TrmAlarmActiveAcknowledgeAllDeact_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 1, 2),
    _TrmAlarmActiveAcknowledgeAllDeact_Type()
)
trmAlarmActiveAcknowledgeAllDeact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmAlarmActiveAcknowledgeAllDeact.setStatus("current")
_TrmAlarmActiveAcknowledgeAll_Type = AlarmAcknowledge
_TrmAlarmActiveAcknowledgeAll_Object = MibScalar
trmAlarmActiveAcknowledgeAll = _TrmAlarmActiveAcknowledgeAll_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 1, 3),
    _TrmAlarmActiveAcknowledgeAll_Type()
)
trmAlarmActiveAcknowledgeAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmAlarmActiveAcknowledgeAll.setStatus("current")
_TrmAlarmActiveTable_Object = MibTable
trmAlarmActiveTable = _TrmAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    trmAlarmActiveTable.setStatus("current")
_TrmAlarmActiveEntry_Object = MibTableRow
trmAlarmActiveEntry = _TrmAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 2, 1)
)
trmAlarmActiveEntry.setIndexNames(
    (0, "TRANSMODE1100", "trmAlarmActiveIndex"),
)
if mibBuilder.loadTexts:
    trmAlarmActiveEntry.setStatus("current")


class _TrmAlarmActiveIndex_Type(Integer32):
    """Custom type trmAlarmActiveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrmAlarmActiveIndex_Type.__name__ = "Integer32"
_TrmAlarmActiveIndex_Object = MibTableColumn
trmAlarmActiveIndex = _TrmAlarmActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 2, 1, 1),
    _TrmAlarmActiveIndex_Type()
)
trmAlarmActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmAlarmActiveIndex.setStatus("current")
_TrmAlarmActiveRackNumber_Type = RackNumber
_TrmAlarmActiveRackNumber_Object = MibTableColumn
trmAlarmActiveRackNumber = _TrmAlarmActiveRackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 2, 1, 2),
    _TrmAlarmActiveRackNumber_Type()
)
trmAlarmActiveRackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmActiveRackNumber.setStatus("current")
_TrmAlarmActiveSlotNumber_Type = SlotNumber
_TrmAlarmActiveSlotNumber_Object = MibTableColumn
trmAlarmActiveSlotNumber = _TrmAlarmActiveSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 2, 1, 3),
    _TrmAlarmActiveSlotNumber_Type()
)
trmAlarmActiveSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmActiveSlotNumber.setStatus("current")
_TrmAlarmActiveName_Type = DisplayString
_TrmAlarmActiveName_Object = MibTableColumn
trmAlarmActiveName = _TrmAlarmActiveName_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 2, 1, 4),
    _TrmAlarmActiveName_Type()
)
trmAlarmActiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmActiveName.setStatus("current")
_TrmAlarmActiveSeverity_Type = PerceivedSeverity
_TrmAlarmActiveSeverity_Object = MibTableColumn
trmAlarmActiveSeverity = _TrmAlarmActiveSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 2, 1, 5),
    _TrmAlarmActiveSeverity_Type()
)
trmAlarmActiveSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmActiveSeverity.setStatus("current")
_TrmAlarmActiveUnit_Type = DisplayString
_TrmAlarmActiveUnit_Object = MibTableColumn
trmAlarmActiveUnit = _TrmAlarmActiveUnit_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 2, 1, 6),
    _TrmAlarmActiveUnit_Type()
)
trmAlarmActiveUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmActiveUnit.setStatus("current")
_TrmAlarmActiveSerialNumber_Type = DisplayString
_TrmAlarmActiveSerialNumber_Object = MibTableColumn
trmAlarmActiveSerialNumber = _TrmAlarmActiveSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 2, 1, 7),
    _TrmAlarmActiveSerialNumber_Type()
)
trmAlarmActiveSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmActiveSerialNumber.setStatus("current")
_TrmAlarmActiveActTime_Type = DisplayString
_TrmAlarmActiveActTime_Object = MibTableColumn
trmAlarmActiveActTime = _TrmAlarmActiveActTime_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 2, 1, 8),
    _TrmAlarmActiveActTime_Type()
)
trmAlarmActiveActTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmActiveActTime.setStatus("current")
_TrmAlarmActiveDeactTime_Type = DisplayString
_TrmAlarmActiveDeactTime_Object = MibTableColumn
trmAlarmActiveDeactTime = _TrmAlarmActiveDeactTime_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 2, 1, 9),
    _TrmAlarmActiveDeactTime_Type()
)
trmAlarmActiveDeactTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmAlarmActiveDeactTime.setStatus("current")
_TrmAlarmActiveAcknowledge_Type = AlarmAcknowledge
_TrmAlarmActiveAcknowledge_Object = MibTableColumn
trmAlarmActiveAcknowledge = _TrmAlarmActiveAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 1, 3, 2, 1, 10),
    _TrmAlarmActiveAcknowledge_Type()
)
trmAlarmActiveAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trmAlarmActiveAcknowledge.setStatus("current")
_TrmSubrack_ObjectIdentity = ObjectIdentity
trmSubrack = _TrmSubrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2)
)
_TrmSubrackList_ObjectIdentity = ObjectIdentity
trmSubrackList = _TrmSubrackList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1)
)
_TrmSubrackListTable_Object = MibTable
trmSubrackListTable = _TrmSubrackListTable_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trmSubrackListTable.setStatus("current")
_TrmSubrackListEntry_Object = MibTableRow
trmSubrackListEntry = _TrmSubrackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1, 1, 1)
)
trmSubrackListEntry.setIndexNames(
    (0, "TRANSMODE1100", "trmListRackNumber"),
    (0, "TRANSMODE1100", "trmListSlotNumber"),
)
if mibBuilder.loadTexts:
    trmSubrackListEntry.setStatus("current")
_TrmListRackNumber_Type = RackNumber
_TrmListRackNumber_Object = MibTableColumn
trmListRackNumber = _TrmListRackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1, 1, 1, 1),
    _TrmListRackNumber_Type()
)
trmListRackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmListRackNumber.setStatus("current")
_TrmListSlotNumber_Type = SlotNumber
_TrmListSlotNumber_Object = MibTableColumn
trmListSlotNumber = _TrmListSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1, 1, 1, 2),
    _TrmListSlotNumber_Type()
)
trmListSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trmListSlotNumber.setStatus("current")
_TrmListUnitPresent_Type = Present
_TrmListUnitPresent_Object = MibTableColumn
trmListUnitPresent = _TrmListUnitPresent_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1, 1, 1, 3),
    _TrmListUnitPresent_Type()
)
trmListUnitPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmListUnitPresent.setStatus("current")
_TrmListProductNumber_Type = DisplayString
_TrmListProductNumber_Object = MibTableColumn
trmListProductNumber = _TrmListProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1, 1, 1, 4),
    _TrmListProductNumber_Type()
)
trmListProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmListProductNumber.setStatus("current")
_TrmListProductDescription_Type = DisplayString
_TrmListProductDescription_Object = MibTableColumn
trmListProductDescription = _TrmListProductDescription_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1, 1, 1, 5),
    _TrmListProductDescription_Type()
)
trmListProductDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmListProductDescription.setStatus("current")
_TrmListHwRevision_Type = DisplayString
_TrmListHwRevision_Object = MibTableColumn
trmListHwRevision = _TrmListHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1, 1, 1, 6),
    _TrmListHwRevision_Type()
)
trmListHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmListHwRevision.setStatus("current")
_TrmListSerialNumber_Type = DisplayString
_TrmListSerialNumber_Object = MibTableColumn
trmListSerialNumber = _TrmListSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1, 1, 1, 7),
    _TrmListSerialNumber_Type()
)
trmListSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmListSerialNumber.setStatus("current")
_TrmListManufacturingDate_Type = DisplayString
_TrmListManufacturingDate_Object = MibTableColumn
trmListManufacturingDate = _TrmListManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1, 1, 1, 8),
    _TrmListManufacturingDate_Type()
)
trmListManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmListManufacturingDate.setStatus("current")
_TrmListSoftwareProdNo_Type = DisplayString
_TrmListSoftwareProdNo_Object = MibTableColumn
trmListSoftwareProdNo = _TrmListSoftwareProdNo_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1, 1, 1, 9),
    _TrmListSoftwareProdNo_Type()
)
trmListSoftwareProdNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmListSoftwareProdNo.setStatus("current")
_TrmListSwVersion_Type = DisplayString
_TrmListSwVersion_Object = MibTableColumn
trmListSwVersion = _TrmListSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 1, 1, 1, 10),
    _TrmListSwVersion_Type()
)
trmListSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trmListSwVersion.setStatus("current")
_TrmSubrackUnits_ObjectIdentity = ObjectIdentity
trmSubrackUnits = _TrmSubrackUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2)
)
_Trm6001_ObjectIdentity = ObjectIdentity
trm6001 = _Trm6001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1)
)
_Trm6001PM_ObjectIdentity = ObjectIdentity
trm6001PM = _Trm6001PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 1)
)
_Trm6001Table_Object = MibTable
trm6001Table = _Trm6001Table_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    trm6001Table.setStatus("current")
_Trm6001Entry_Object = MibTableRow
trm6001Entry = _Trm6001Entry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 1, 1, 1)
)
trm6001Entry.setIndexNames(
    (0, "TRANSMODE1100", "trm6001RackNumber"),
    (0, "TRANSMODE1100", "trm6001SlotNumber"),
)
if mibBuilder.loadTexts:
    trm6001Entry.setStatus("current")
_Trm6001RackNumber_Type = RackNumber
_Trm6001RackNumber_Object = MibTableColumn
trm6001RackNumber = _Trm6001RackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 1, 1, 1, 1),
    _Trm6001RackNumber_Type()
)
trm6001RackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm6001RackNumber.setStatus("current")
_Trm6001SlotNumber_Type = SlotNumberNmb
_Trm6001SlotNumber_Object = MibTableColumn
trm6001SlotNumber = _Trm6001SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 1, 1, 1, 2),
    _Trm6001SlotNumber_Type()
)
trm6001SlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm6001SlotNumber.setStatus("current")
_Trm6001IPAddress_Type = DisplayString
_Trm6001IPAddress_Object = MibTableColumn
trm6001IPAddress = _Trm6001IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 1, 1, 1, 3),
    _Trm6001IPAddress_Type()
)
trm6001IPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm6001IPAddress.setStatus("current")
_Trm6001MACAddress_Type = DisplayString
_Trm6001MACAddress_Object = MibTableColumn
trm6001MACAddress = _Trm6001MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 1, 1, 1, 4),
    _Trm6001MACAddress_Type()
)
trm6001MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm6001MACAddress.setStatus("current")


class _Trm6001Temperature_Type(Integer32):
    """Custom type trm6001Temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Trm6001Temperature_Type.__name__ = "Integer32"
_Trm6001Temperature_Object = MibTableColumn
trm6001Temperature = _Trm6001Temperature_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 1, 1, 1, 5),
    _Trm6001Temperature_Type()
)
trm6001Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm6001Temperature.setStatus("current")
_Trm6001UpTime_Type = DisplayString
_Trm6001UpTime_Object = MibTableColumn
trm6001UpTime = _Trm6001UpTime_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 1, 1, 1, 6),
    _Trm6001UpTime_Type()
)
trm6001UpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm6001UpTime.setStatus("current")
_Trm6001Date_Type = TrmDate
_Trm6001Date_Object = MibTableColumn
trm6001Date = _Trm6001Date_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 1, 1, 1, 7),
    _Trm6001Date_Type()
)
trm6001Date.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm6001Date.setStatus("current")
_Trm6001Time_Type = TrmTime
_Trm6001Time_Object = MibTableColumn
trm6001Time = _Trm6001Time_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 1, 1, 1, 8),
    _Trm6001Time_Type()
)
trm6001Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm6001Time.setStatus("current")


class _Trm6001SwReset_Type(Integer32):
    """Custom type trm6001SwReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Trm6001SwReset_Type.__name__ = "Integer32"
_Trm6001SwReset_Object = MibTableColumn
trm6001SwReset = _Trm6001SwReset_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 1, 1, 1, 9),
    _Trm6001SwReset_Type()
)
trm6001SwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm6001SwReset.setStatus("current")
_Trm6001FM_ObjectIdentity = ObjectIdentity
trm6001FM = _Trm6001FM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 2)
)
_Trm6001Traps_ObjectIdentity = ObjectIdentity
trm6001Traps = _Trm6001Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 2, 0)
)
_Trm9xxx_ObjectIdentity = ObjectIdentity
trm9xxx = _Trm9xxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2)
)
_Trm9xxxPM_ObjectIdentity = ObjectIdentity
trm9xxxPM = _Trm9xxxPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2, 1)
)
_Trm9xxxTable_Object = MibTable
trm9xxxTable = _Trm9xxxTable_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trm9xxxTable.setStatus("current")
_Trm9xxxEntry_Object = MibTableRow
trm9xxxEntry = _Trm9xxxEntry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2, 1, 1, 1)
)
trm9xxxEntry.setIndexNames(
    (0, "TRANSMODE1100", "trm9xxxRackNumber"),
    (0, "TRANSMODE1100", "trm9xxxSlotNumber"),
)
if mibBuilder.loadTexts:
    trm9xxxEntry.setStatus("current")
_Trm9xxxRackNumber_Type = RackNumber
_Trm9xxxRackNumber_Object = MibTableColumn
trm9xxxRackNumber = _Trm9xxxRackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2, 1, 1, 1, 1),
    _Trm9xxxRackNumber_Type()
)
trm9xxxRackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm9xxxRackNumber.setStatus("current")
_Trm9xxxSlotNumber_Type = SlotNumberPS
_Trm9xxxSlotNumber_Object = MibTableColumn
trm9xxxSlotNumber = _Trm9xxxSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2, 1, 1, 1, 2),
    _Trm9xxxSlotNumber_Type()
)
trm9xxxSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm9xxxSlotNumber.setStatus("current")
_Trm9xxxPresent_Type = Present
_Trm9xxxPresent_Object = MibTableColumn
trm9xxxPresent = _Trm9xxxPresent_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2, 1, 1, 1, 3),
    _Trm9xxxPresent_Type()
)
trm9xxxPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm9xxxPresent.setStatus("current")
_Trm9xxxType_Type = PowerType
_Trm9xxxType_Object = MibTableColumn
trm9xxxType = _Trm9xxxType_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2, 1, 1, 1, 4),
    _Trm9xxxType_Type()
)
trm9xxxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm9xxxType.setStatus("current")
_Trm9xxxStatus_Type = PowerStatus
_Trm9xxxStatus_Object = MibTableColumn
trm9xxxStatus = _Trm9xxxStatus_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2, 1, 1, 1, 5),
    _Trm9xxxStatus_Type()
)
trm9xxxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm9xxxStatus.setStatus("current")
_Trm9xxxFM_ObjectIdentity = ObjectIdentity
trm9xxxFM = _Trm9xxxFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2, 2)
)
_Trm9xxxTraps_ObjectIdentity = ObjectIdentity
trm9xxxTraps = _Trm9xxxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2, 2, 0)
)
_Trm75xx_ObjectIdentity = ObjectIdentity
trm75xx = _Trm75xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3)
)
_Trm75xxPM_ObjectIdentity = ObjectIdentity
trm75xxPM = _Trm75xxPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1)
)
_Trm75xxTable_Object = MibTable
trm75xxTable = _Trm75xxTable_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    trm75xxTable.setStatus("current")
_Trm75xxEntry_Object = MibTableRow
trm75xxEntry = _Trm75xxEntry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1)
)
trm75xxEntry.setIndexNames(
    (0, "TRANSMODE1100", "trm75xxRackNumber"),
    (0, "TRANSMODE1100", "trm75xxSlotNumber"),
)
if mibBuilder.loadTexts:
    trm75xxEntry.setStatus("current")
_Trm75xxRackNumber_Type = RackNumber
_Trm75xxRackNumber_Object = MibTableColumn
trm75xxRackNumber = _Trm75xxRackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 1),
    _Trm75xxRackNumber_Type()
)
trm75xxRackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm75xxRackNumber.setStatus("current")
_Trm75xxSlotNumber_Type = BoardNumber
_Trm75xxSlotNumber_Object = MibTableColumn
trm75xxSlotNumber = _Trm75xxSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 2),
    _Trm75xxSlotNumber_Type()
)
trm75xxSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm75xxSlotNumber.setStatus("current")
_Trm75xxRxLine_Type = DisplayString
_Trm75xxRxLine_Object = MibTableColumn
trm75xxRxLine = _Trm75xxRxLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 3),
    _Trm75xxRxLine_Type()
)
trm75xxRxLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm75xxRxLine.setStatus("current")
_Trm75xxEstProtLine_Type = DisplayString
_Trm75xxEstProtLine_Object = MibTableColumn
trm75xxEstProtLine = _Trm75xxEstProtLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 4),
    _Trm75xxEstProtLine_Type()
)
trm75xxEstProtLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm75xxEstProtLine.setStatus("current")
_Trm75xxEstFibRateLine_Type = DisplayString
_Trm75xxEstFibRateLine_Object = MibTableColumn
trm75xxEstFibRateLine = _Trm75xxEstFibRateLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 5),
    _Trm75xxEstFibRateLine_Type()
)
trm75xxEstFibRateLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm75xxEstFibRateLine.setStatus("current")
_Trm75xxTxLine_Type = DisplayString
_Trm75xxTxLine_Object = MibTableColumn
trm75xxTxLine = _Trm75xxTxLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 6),
    _Trm75xxTxLine_Type()
)
trm75xxTxLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm75xxTxLine.setStatus("current")
_Trm75xxTxMode_Type = TxMode75
_Trm75xxTxMode_Object = MibTableColumn
trm75xxTxMode = _Trm75xxTxMode_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 7),
    _Trm75xxTxMode_Type()
)
trm75xxTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm75xxTxMode.setStatus("current")
_Trm75xxWavelengthLine_Type = DisplayString
_Trm75xxWavelengthLine_Object = MibTableColumn
trm75xxWavelengthLine = _Trm75xxWavelengthLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 8),
    _Trm75xxWavelengthLine_Type()
)
trm75xxWavelengthLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm75xxWavelengthLine.setStatus("current")
_Trm75xxRxClient_Type = DisplayString
_Trm75xxRxClient_Object = MibTableColumn
trm75xxRxClient = _Trm75xxRxClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 9),
    _Trm75xxRxClient_Type()
)
trm75xxRxClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm75xxRxClient.setStatus("current")
_Trm75xxEstProtClient_Type = DisplayString
_Trm75xxEstProtClient_Object = MibTableColumn
trm75xxEstProtClient = _Trm75xxEstProtClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 10),
    _Trm75xxEstProtClient_Type()
)
trm75xxEstProtClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm75xxEstProtClient.setStatus("current")
_Trm75xxEstFibRateClient_Type = DisplayString
_Trm75xxEstFibRateClient_Object = MibTableColumn
trm75xxEstFibRateClient = _Trm75xxEstFibRateClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 11),
    _Trm75xxEstFibRateClient_Type()
)
trm75xxEstFibRateClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm75xxEstFibRateClient.setStatus("current")
_Trm75xxTxClient_Type = DisplayString
_Trm75xxTxClient_Object = MibTableColumn
trm75xxTxClient = _Trm75xxTxClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 12),
    _Trm75xxTxClient_Type()
)
trm75xxTxClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm75xxTxClient.setStatus("current")
_Trm75xxTxModeClient_Type = TxMode75
_Trm75xxTxModeClient_Object = MibTableColumn
trm75xxTxModeClient = _Trm75xxTxModeClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 13),
    _Trm75xxTxModeClient_Type()
)
trm75xxTxModeClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm75xxTxModeClient.setStatus("obsolete")
_Trm75xxIDStringClient_Type = DisplayString
_Trm75xxIDStringClient_Object = MibTableColumn
trm75xxIDStringClient = _Trm75xxIDStringClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 14),
    _Trm75xxIDStringClient_Type()
)
trm75xxIDStringClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm75xxIDStringClient.setStatus("current")
_Trm75xxIPAddressClient_Type = DisplayString
_Trm75xxIPAddressClient_Object = MibTableColumn
trm75xxIPAddressClient = _Trm75xxIPAddressClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 15),
    _Trm75xxIPAddressClient_Type()
)
trm75xxIPAddressClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm75xxIPAddressClient.setStatus("current")
_Trm75xxWavelengthClient_Type = DisplayString
_Trm75xxWavelengthClient_Object = MibTableColumn
trm75xxWavelengthClient = _Trm75xxWavelengthClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 16),
    _Trm75xxWavelengthClient_Type()
)
trm75xxWavelengthClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm75xxWavelengthClient.setStatus("current")
_Trm75xxSpeedLimit_Type = SpeedLimit75
_Trm75xxSpeedLimit_Object = MibTableColumn
trm75xxSpeedLimit = _Trm75xxSpeedLimit_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 1, 1, 1, 17),
    _Trm75xxSpeedLimit_Type()
)
trm75xxSpeedLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm75xxSpeedLimit.setStatus("current")
_Trm75xxFM_ObjectIdentity = ObjectIdentity
trm75xxFM = _Trm75xxFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 2)
)
_Trm75xxTraps_ObjectIdentity = ObjectIdentity
trm75xxTraps = _Trm75xxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 2, 0)
)
_Trm76xx_ObjectIdentity = ObjectIdentity
trm76xx = _Trm76xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4)
)
_Trm76xxPM_ObjectIdentity = ObjectIdentity
trm76xxPM = _Trm76xxPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1)
)
_Trm76xxTable_Object = MibTable
trm76xxTable = _Trm76xxTable_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    trm76xxTable.setStatus("current")
_Trm76xxEntry_Object = MibTableRow
trm76xxEntry = _Trm76xxEntry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1)
)
trm76xxEntry.setIndexNames(
    (0, "TRANSMODE1100", "trm76xxRackNumber"),
    (0, "TRANSMODE1100", "trm76xxSlotNumber"),
)
if mibBuilder.loadTexts:
    trm76xxEntry.setStatus("current")
_Trm76xxRackNumber_Type = RackNumber
_Trm76xxRackNumber_Object = MibTableColumn
trm76xxRackNumber = _Trm76xxRackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 1),
    _Trm76xxRackNumber_Type()
)
trm76xxRackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm76xxRackNumber.setStatus("current")
_Trm76xxSlotNumber_Type = BoardNumber
_Trm76xxSlotNumber_Object = MibTableColumn
trm76xxSlotNumber = _Trm76xxSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 2),
    _Trm76xxSlotNumber_Type()
)
trm76xxSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm76xxSlotNumber.setStatus("current")
_Trm76xxTemperature_Type = Integer32
_Trm76xxTemperature_Object = MibTableColumn
trm76xxTemperature = _Trm76xxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 3),
    _Trm76xxTemperature_Type()
)
trm76xxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxTemperature.setStatus("current")
_Trm76xxCDR_Type = CDRMode
_Trm76xxCDR_Object = MibTableColumn
trm76xxCDR = _Trm76xxCDR_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 4),
    _Trm76xxCDR_Type()
)
trm76xxCDR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm76xxCDR.setStatus("current")
_Trm76xxCustomFibRate_Type = Integer32
_Trm76xxCustomFibRate_Object = MibTableColumn
trm76xxCustomFibRate = _Trm76xxCustomFibRate_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 5),
    _Trm76xxCustomFibRate_Type()
)
trm76xxCustomFibRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm76xxCustomFibRate.setStatus("current")
_Trm76xxTxMode_Type = TxMode76
_Trm76xxTxMode_Object = MibTableColumn
trm76xxTxMode = _Trm76xxTxMode_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 6),
    _Trm76xxTxMode_Type()
)
trm76xxTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm76xxTxMode.setStatus("current")
_Trm76xxLineLoopMode_Type = LineLoopMode
_Trm76xxLineLoopMode_Object = MibTableColumn
trm76xxLineLoopMode = _Trm76xxLineLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 7),
    _Trm76xxLineLoopMode_Type()
)
trm76xxLineLoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm76xxLineLoopMode.setStatus("current")


class _Trm76xxSwReset_Type(Integer32):
    """Custom type trm76xxSwReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Trm76xxSwReset_Type.__name__ = "Integer32"
_Trm76xxSwReset_Object = MibTableColumn
trm76xxSwReset = _Trm76xxSwReset_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 8),
    _Trm76xxSwReset_Type()
)
trm76xxSwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm76xxSwReset.setStatus("current")
_Trm76xxRxLine_Type = DisplayString
_Trm76xxRxLine_Object = MibTableColumn
trm76xxRxLine = _Trm76xxRxLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 9),
    _Trm76xxRxLine_Type()
)
trm76xxRxLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxRxLine.setStatus("current")
_Trm76xxOpticalInPowLine_Type = Integer32
_Trm76xxOpticalInPowLine_Object = MibTableColumn
trm76xxOpticalInPowLine = _Trm76xxOpticalInPowLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 10),
    _Trm76xxOpticalInPowLine_Type()
)
trm76xxOpticalInPowLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxOpticalInPowLine.setStatus("current")
_Trm76xxSpeedLimit_Type = SpeedLimit76
_Trm76xxSpeedLimit_Object = MibTableColumn
trm76xxSpeedLimit = _Trm76xxSpeedLimit_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 11),
    _Trm76xxSpeedLimit_Type()
)
trm76xxSpeedLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm76xxSpeedLimit.setStatus("current")
_Trm76xxEstProtLine_Type = DisplayString
_Trm76xxEstProtLine_Object = MibTableColumn
trm76xxEstProtLine = _Trm76xxEstProtLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 12),
    _Trm76xxEstProtLine_Type()
)
trm76xxEstProtLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxEstProtLine.setStatus("current")
_Trm76xxEstFibRateLine_Type = DisplayString
_Trm76xxEstFibRateLine_Object = MibTableColumn
trm76xxEstFibRateLine = _Trm76xxEstFibRateLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 13),
    _Trm76xxEstFibRateLine_Type()
)
trm76xxEstFibRateLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxEstFibRateLine.setStatus("current")
_Trm76xxTxLine_Type = DisplayString
_Trm76xxTxLine_Object = MibTableColumn
trm76xxTxLine = _Trm76xxTxLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 14),
    _Trm76xxTxLine_Type()
)
trm76xxTxLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxTxLine.setStatus("current")
_Trm76xxOpticalOutPowLine_Type = Integer32
_Trm76xxOpticalOutPowLine_Object = MibTableColumn
trm76xxOpticalOutPowLine = _Trm76xxOpticalOutPowLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 15),
    _Trm76xxOpticalOutPowLine_Type()
)
trm76xxOpticalOutPowLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxOpticalOutPowLine.setStatus("current")
_Trm76xxProdOutPowLine_Type = Integer32
_Trm76xxProdOutPowLine_Object = MibTableColumn
trm76xxProdOutPowLine = _Trm76xxProdOutPowLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 16),
    _Trm76xxProdOutPowLine_Type()
)
trm76xxProdOutPowLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxProdOutPowLine.setStatus("current")
_Trm76xxLaserBiasCurLine_Type = Integer32
_Trm76xxLaserBiasCurLine_Object = MibTableColumn
trm76xxLaserBiasCurLine = _Trm76xxLaserBiasCurLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 17),
    _Trm76xxLaserBiasCurLine_Type()
)
trm76xxLaserBiasCurLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxLaserBiasCurLine.setStatus("current")
_Trm76xxProdLaserBiasCurLine_Type = Integer32
_Trm76xxProdLaserBiasCurLine_Object = MibTableColumn
trm76xxProdLaserBiasCurLine = _Trm76xxProdLaserBiasCurLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 18),
    _Trm76xxProdLaserBiasCurLine_Type()
)
trm76xxProdLaserBiasCurLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxProdLaserBiasCurLine.setStatus("current")
_Trm76xxWavelengthLine_Type = DisplayString
_Trm76xxWavelengthLine_Object = MibTableColumn
trm76xxWavelengthLine = _Trm76xxWavelengthLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 19),
    _Trm76xxWavelengthLine_Type()
)
trm76xxWavelengthLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxWavelengthLine.setStatus("current")
_Trm76xxRxClient_Type = DisplayString
_Trm76xxRxClient_Object = MibTableColumn
trm76xxRxClient = _Trm76xxRxClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 20),
    _Trm76xxRxClient_Type()
)
trm76xxRxClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxRxClient.setStatus("current")
_Trm76xxEstProtClient_Type = DisplayString
_Trm76xxEstProtClient_Object = MibTableColumn
trm76xxEstProtClient = _Trm76xxEstProtClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 21),
    _Trm76xxEstProtClient_Type()
)
trm76xxEstProtClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxEstProtClient.setStatus("current")
_Trm76xxEstFibRateClient_Type = DisplayString
_Trm76xxEstFibRateClient_Object = MibTableColumn
trm76xxEstFibRateClient = _Trm76xxEstFibRateClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 22),
    _Trm76xxEstFibRateClient_Type()
)
trm76xxEstFibRateClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxEstFibRateClient.setStatus("current")
_Trm76xxTxClient_Type = DisplayString
_Trm76xxTxClient_Object = MibTableColumn
trm76xxTxClient = _Trm76xxTxClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 23),
    _Trm76xxTxClient_Type()
)
trm76xxTxClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxTxClient.setStatus("current")
_Trm76xxIDStringClient_Type = DisplayString
_Trm76xxIDStringClient_Object = MibTableColumn
trm76xxIDStringClient = _Trm76xxIDStringClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 24),
    _Trm76xxIDStringClient_Type()
)
trm76xxIDStringClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm76xxIDStringClient.setStatus("current")
_Trm76xxIPAddressClient_Type = DisplayString
_Trm76xxIPAddressClient_Object = MibTableColumn
trm76xxIPAddressClient = _Trm76xxIPAddressClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 25),
    _Trm76xxIPAddressClient_Type()
)
trm76xxIPAddressClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm76xxIPAddressClient.setStatus("current")
_Trm76xxWavelengthClient_Type = DisplayString
_Trm76xxWavelengthClient_Object = MibTableColumn
trm76xxWavelengthClient = _Trm76xxWavelengthClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 26),
    _Trm76xxWavelengthClient_Type()
)
trm76xxWavelengthClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxWavelengthClient.setStatus("current")
_Trm76xxOpticalInPowClient_Type = Integer32
_Trm76xxOpticalInPowClient_Object = MibTableColumn
trm76xxOpticalInPowClient = _Trm76xxOpticalInPowClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 27),
    _Trm76xxOpticalInPowClient_Type()
)
trm76xxOpticalInPowClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxOpticalInPowClient.setStatus("current")
_Trm76xxOpticalOutPowClient_Type = Integer32
_Trm76xxOpticalOutPowClient_Object = MibTableColumn
trm76xxOpticalOutPowClient = _Trm76xxOpticalOutPowClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 28),
    _Trm76xxOpticalOutPowClient_Type()
)
trm76xxOpticalOutPowClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxOpticalOutPowClient.setStatus("current")
_Trm76xxLaserBiasCurClient_Type = Integer32
_Trm76xxLaserBiasCurClient_Object = MibTableColumn
trm76xxLaserBiasCurClient = _Trm76xxLaserBiasCurClient_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 1, 1, 1, 29),
    _Trm76xxLaserBiasCurClient_Type()
)
trm76xxLaserBiasCurClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm76xxLaserBiasCurClient.setStatus("current")
_Trm76xxFM_ObjectIdentity = ObjectIdentity
trm76xxFM = _Trm76xxFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2)
)
_Trm76xxTraps_ObjectIdentity = ObjectIdentity
trm76xxTraps = _Trm76xxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0)
)
_Trm803x_ObjectIdentity = ObjectIdentity
trm803x = _Trm803x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 5)
)
_Trm803xPM_ObjectIdentity = ObjectIdentity
trm803xPM = _Trm803xPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 5, 1)
)
_Trm803xTable_Object = MibTable
trm803xTable = _Trm803xTable_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    trm803xTable.setStatus("current")
_Trm803xEntry_Object = MibTableRow
trm803xEntry = _Trm803xEntry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 5, 1, 1, 1)
)
trm803xEntry.setIndexNames(
    (0, "TRANSMODE1100", "trm803xRackNumber"),
    (0, "TRANSMODE1100", "trm803xSlotNumber"),
)
if mibBuilder.loadTexts:
    trm803xEntry.setStatus("current")
_Trm803xRackNumber_Type = RackNumber
_Trm803xRackNumber_Object = MibTableColumn
trm803xRackNumber = _Trm803xRackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 5, 1, 1, 1, 1),
    _Trm803xRackNumber_Type()
)
trm803xRackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm803xRackNumber.setStatus("current")
_Trm803xSlotNumber_Type = Integer32
_Trm803xSlotNumber_Object = MibTableColumn
trm803xSlotNumber = _Trm803xSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 5, 1, 1, 1, 2),
    _Trm803xSlotNumber_Type()
)
trm803xSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm803xSlotNumber.setStatus("current")
_Trm803xMuxType_Type = MuxType
_Trm803xMuxType_Object = MibTableColumn
trm803xMuxType = _Trm803xMuxType_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 5, 1, 1, 1, 3),
    _Trm803xMuxType_Type()
)
trm803xMuxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm803xMuxType.setStatus("current")
_Trm803xIDStringLine_Type = DisplayString
_Trm803xIDStringLine_Object = MibTableColumn
trm803xIDStringLine = _Trm803xIDStringLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 5, 1, 1, 1, 4),
    _Trm803xIDStringLine_Type()
)
trm803xIDStringLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm803xIDStringLine.setStatus("current")
_Trm803xIPAddressLine_Type = DisplayString
_Trm803xIPAddressLine_Object = MibTableColumn
trm803xIPAddressLine = _Trm803xIPAddressLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 5, 1, 1, 1, 5),
    _Trm803xIPAddressLine_Type()
)
trm803xIPAddressLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm803xIPAddressLine.setStatus("current")
_Trm2204_ObjectIdentity = ObjectIdentity
trm2204 = _Trm2204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 6)
)
_Trm2204PM_ObjectIdentity = ObjectIdentity
trm2204PM = _Trm2204PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 6, 1)
)
_Trm2204Table_Object = MibTable
trm2204Table = _Trm2204Table_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    trm2204Table.setStatus("current")
_Trm2204Entry_Object = MibTableRow
trm2204Entry = _Trm2204Entry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 6, 1, 1, 1)
)
trm2204Entry.setIndexNames(
    (0, "TRANSMODE1100", "trm2204RackNumber"),
    (0, "TRANSMODE1100", "trm2204SlotNumber"),
)
if mibBuilder.loadTexts:
    trm2204Entry.setStatus("current")
_Trm2204RackNumber_Type = RackNumber
_Trm2204RackNumber_Object = MibTableColumn
trm2204RackNumber = _Trm2204RackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 6, 1, 1, 1, 1),
    _Trm2204RackNumber_Type()
)
trm2204RackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm2204RackNumber.setStatus("current")
_Trm2204SlotNumber_Type = Integer32
_Trm2204SlotNumber_Object = MibTableColumn
trm2204SlotNumber = _Trm2204SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 6, 1, 1, 1, 2),
    _Trm2204SlotNumber_Type()
)
trm2204SlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm2204SlotNumber.setStatus("current")
_Trm2204SecurityMode_Type = SecurityMode
_Trm2204SecurityMode_Object = MibTableColumn
trm2204SecurityMode = _Trm2204SecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 6, 1, 1, 1, 3),
    _Trm2204SecurityMode_Type()
)
trm2204SecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm2204SecurityMode.setStatus("current")
_Trm26xx_ObjectIdentity = ObjectIdentity
trm26xx = _Trm26xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7)
)
_Trm26xxPM_ObjectIdentity = ObjectIdentity
trm26xxPM = _Trm26xxPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1)
)
_Trm26xxTable_Object = MibTable
trm26xxTable = _Trm26xxTable_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    trm26xxTable.setStatus("current")
_Trm26xxEntry_Object = MibTableRow
trm26xxEntry = _Trm26xxEntry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1)
)
trm26xxEntry.setIndexNames(
    (0, "TRANSMODE1100", "trm26xxRackNumber"),
    (0, "TRANSMODE1100", "trm26xxSlotNumber"),
)
if mibBuilder.loadTexts:
    trm26xxEntry.setStatus("current")
_Trm26xxRackNumber_Type = RackNumber
_Trm26xxRackNumber_Object = MibTableColumn
trm26xxRackNumber = _Trm26xxRackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 1),
    _Trm26xxRackNumber_Type()
)
trm26xxRackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm26xxRackNumber.setStatus("current")
_Trm26xxSlotNumber_Type = BoardNumber
_Trm26xxSlotNumber_Object = MibTableColumn
trm26xxSlotNumber = _Trm26xxSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 2),
    _Trm26xxSlotNumber_Type()
)
trm26xxSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm26xxSlotNumber.setStatus("current")
_Trm26xxStatus_Type = DisplayString
_Trm26xxStatus_Object = MibTableColumn
trm26xxStatus = _Trm26xxStatus_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 3),
    _Trm26xxStatus_Type()
)
trm26xxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxStatus.setStatus("current")
_Trm26xxTemperature_Type = Integer32
_Trm26xxTemperature_Object = MibTableColumn
trm26xxTemperature = _Trm26xxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 4),
    _Trm26xxTemperature_Type()
)
trm26xxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxTemperature.setStatus("current")
_Trm26xxTxMode_Type = TxMode75
_Trm26xxTxMode_Object = MibTableColumn
trm26xxTxMode = _Trm26xxTxMode_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 5),
    _Trm26xxTxMode_Type()
)
trm26xxTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm26xxTxMode.setStatus("current")


class _Trm26xxSwReset_Type(Integer32):
    """Custom type trm26xxSwReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Trm26xxSwReset_Type.__name__ = "Integer32"
_Trm26xxSwReset_Object = MibTableColumn
trm26xxSwReset = _Trm26xxSwReset_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 6),
    _Trm26xxSwReset_Type()
)
trm26xxSwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm26xxSwReset.setStatus("current")
_Trm26xxOpticalPowerPIN1_Type = Integer32
_Trm26xxOpticalPowerPIN1_Object = MibTableColumn
trm26xxOpticalPowerPIN1 = _Trm26xxOpticalPowerPIN1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 7),
    _Trm26xxOpticalPowerPIN1_Type()
)
trm26xxOpticalPowerPIN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxOpticalPowerPIN1.setStatus("current")
_Trm26xxOpticalPowerPIN2_Type = Integer32
_Trm26xxOpticalPowerPIN2_Object = MibTableColumn
trm26xxOpticalPowerPIN2 = _Trm26xxOpticalPowerPIN2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 8),
    _Trm26xxOpticalPowerPIN2_Type()
)
trm26xxOpticalPowerPIN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxOpticalPowerPIN2.setStatus("current")
_Trm26xxLogOpticalPower_Type = Integer32
_Trm26xxLogOpticalPower_Object = MibTableColumn
trm26xxLogOpticalPower = _Trm26xxLogOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 9),
    _Trm26xxLogOpticalPower_Type()
)
trm26xxLogOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxLogOpticalPower.setStatus("current")
_Trm26xxTemperatureTEC1_Type = Integer32
_Trm26xxTemperatureTEC1_Object = MibTableColumn
trm26xxTemperatureTEC1 = _Trm26xxTemperatureTEC1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 10),
    _Trm26xxTemperatureTEC1_Type()
)
trm26xxTemperatureTEC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxTemperatureTEC1.setStatus("current")
_Trm26xxTemperatureTEC2_Type = Integer32
_Trm26xxTemperatureTEC2_Object = MibTableColumn
trm26xxTemperatureTEC2 = _Trm26xxTemperatureTEC2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 11),
    _Trm26xxTemperatureTEC2_Type()
)
trm26xxTemperatureTEC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxTemperatureTEC2.setStatus("current")
_Trm26xxVoltageTEC1_Type = Integer32
_Trm26xxVoltageTEC1_Object = MibTableColumn
trm26xxVoltageTEC1 = _Trm26xxVoltageTEC1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 12),
    _Trm26xxVoltageTEC1_Type()
)
trm26xxVoltageTEC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxVoltageTEC1.setStatus("current")
_Trm26xxVoltageTEC2_Type = Integer32
_Trm26xxVoltageTEC2_Object = MibTableColumn
trm26xxVoltageTEC2 = _Trm26xxVoltageTEC2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 13),
    _Trm26xxVoltageTEC2_Type()
)
trm26xxVoltageTEC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxVoltageTEC2.setStatus("obsolete")
_Trm26xxCurrentTEC1_Type = Integer32
_Trm26xxCurrentTEC1_Object = MibTableColumn
trm26xxCurrentTEC1 = _Trm26xxCurrentTEC1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 14),
    _Trm26xxCurrentTEC1_Type()
)
trm26xxCurrentTEC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxCurrentTEC1.setStatus("current")
_Trm26xxCurrentTEC2_Type = Integer32
_Trm26xxCurrentTEC2_Object = MibTableColumn
trm26xxCurrentTEC2 = _Trm26xxCurrentTEC2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 15),
    _Trm26xxCurrentTEC2_Type()
)
trm26xxCurrentTEC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxCurrentTEC2.setStatus("current")
_Trm26xxCurrentBIAS1_Type = Integer32
_Trm26xxCurrentBIAS1_Object = MibTableColumn
trm26xxCurrentBIAS1 = _Trm26xxCurrentBIAS1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 16),
    _Trm26xxCurrentBIAS1_Type()
)
trm26xxCurrentBIAS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxCurrentBIAS1.setStatus("current")
_Trm26xxCurrentBIAS2_Type = Integer32
_Trm26xxCurrentBIAS2_Object = MibTableColumn
trm26xxCurrentBIAS2 = _Trm26xxCurrentBIAS2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 17),
    _Trm26xxCurrentBIAS2_Type()
)
trm26xxCurrentBIAS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxCurrentBIAS2.setStatus("current")
_Trm26xxVoltageBIAS1_Type = Integer32
_Trm26xxVoltageBIAS1_Object = MibTableColumn
trm26xxVoltageBIAS1 = _Trm26xxVoltageBIAS1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 18),
    _Trm26xxVoltageBIAS1_Type()
)
trm26xxVoltageBIAS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxVoltageBIAS1.setStatus("current")
_Trm26xxVoltageBIAS2_Type = Integer32
_Trm26xxVoltageBIAS2_Object = MibTableColumn
trm26xxVoltageBIAS2 = _Trm26xxVoltageBIAS2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 1, 1, 1, 19),
    _Trm26xxVoltageBIAS2_Type()
)
trm26xxVoltageBIAS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm26xxVoltageBIAS2.setStatus("current")
_Trm26xxFM_ObjectIdentity = ObjectIdentity
trm26xxFM = _Trm26xxFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 2)
)
_Trm26xxTraps_ObjectIdentity = ObjectIdentity
trm26xxTraps = _Trm26xxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 2, 0)
)
_Trm25xx_ObjectIdentity = ObjectIdentity
trm25xx = _Trm25xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8)
)
_Trm25xxPM_ObjectIdentity = ObjectIdentity
trm25xxPM = _Trm25xxPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1)
)
_Trm25xxTable_Object = MibTable
trm25xxTable = _Trm25xxTable_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    trm25xxTable.setStatus("current")
_Trm25xxEntry_Object = MibTableRow
trm25xxEntry = _Trm25xxEntry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1)
)
trm25xxEntry.setIndexNames(
    (0, "TRANSMODE1100", "trm25xxRackNumber"),
    (0, "TRANSMODE1100", "trm25xxSlotNumber"),
)
if mibBuilder.loadTexts:
    trm25xxEntry.setStatus("current")
_Trm25xxRackNumber_Type = RackNumber
_Trm25xxRackNumber_Object = MibTableColumn
trm25xxRackNumber = _Trm25xxRackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 1),
    _Trm25xxRackNumber_Type()
)
trm25xxRackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm25xxRackNumber.setStatus("current")
_Trm25xxSlotNumber_Type = BoardNumber
_Trm25xxSlotNumber_Object = MibTableColumn
trm25xxSlotNumber = _Trm25xxSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 2),
    _Trm25xxSlotNumber_Type()
)
trm25xxSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm25xxSlotNumber.setStatus("current")
_Trm25xxWorkingLineStatus_Type = DisplayString
_Trm25xxWorkingLineStatus_Object = MibTableColumn
trm25xxWorkingLineStatus = _Trm25xxWorkingLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 3),
    _Trm25xxWorkingLineStatus_Type()
)
trm25xxWorkingLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm25xxWorkingLineStatus.setStatus("current")
_Trm25xxProtectingLineStatus_Type = DisplayString
_Trm25xxProtectingLineStatus_Object = MibTableColumn
trm25xxProtectingLineStatus = _Trm25xxProtectingLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 4),
    _Trm25xxProtectingLineStatus_Type()
)
trm25xxProtectingLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm25xxProtectingLineStatus.setStatus("current")
_Trm25xxTemperature_Type = Integer32
_Trm25xxTemperature_Object = MibTableColumn
trm25xxTemperature = _Trm25xxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 5),
    _Trm25xxTemperature_Type()
)
trm25xxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm25xxTemperature.setStatus("current")


class _Trm25xxSwReset_Type(Integer32):
    """Custom type trm25xxSwReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Trm25xxSwReset_Type.__name__ = "Integer32"
_Trm25xxSwReset_Object = MibTableColumn
trm25xxSwReset = _Trm25xxSwReset_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 6),
    _Trm25xxSwReset_Type()
)
trm25xxSwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm25xxSwReset.setStatus("current")
_Trm25xxRxLine_Type = DisplayString
_Trm25xxRxLine_Object = MibTableColumn
trm25xxRxLine = _Trm25xxRxLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 7),
    _Trm25xxRxLine_Type()
)
trm25xxRxLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm25xxRxLine.setStatus("current")
_Trm25xxOpticalInPowLine_Type = Integer32
_Trm25xxOpticalInPowLine_Object = MibTableColumn
trm25xxOpticalInPowLine = _Trm25xxOpticalInPowLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 8),
    _Trm25xxOpticalInPowLine_Type()
)
trm25xxOpticalInPowLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm25xxOpticalInPowLine.setStatus("current")
_Trm25xxSpeedLimit_Type = SpeedLimit76
_Trm25xxSpeedLimit_Object = MibTableColumn
trm25xxSpeedLimit = _Trm25xxSpeedLimit_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 9),
    _Trm25xxSpeedLimit_Type()
)
trm25xxSpeedLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm25xxSpeedLimit.setStatus("current")
_Trm25xxEstProtLine_Type = DisplayString
_Trm25xxEstProtLine_Object = MibTableColumn
trm25xxEstProtLine = _Trm25xxEstProtLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 10),
    _Trm25xxEstProtLine_Type()
)
trm25xxEstProtLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm25xxEstProtLine.setStatus("current")
_Trm25xxEstFibRateLine_Type = DisplayString
_Trm25xxEstFibRateLine_Object = MibTableColumn
trm25xxEstFibRateLine = _Trm25xxEstFibRateLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 11),
    _Trm25xxEstFibRateLine_Type()
)
trm25xxEstFibRateLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm25xxEstFibRateLine.setStatus("current")
_Trm25xxTxLine_Type = DisplayString
_Trm25xxTxLine_Object = MibTableColumn
trm25xxTxLine = _Trm25xxTxLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 12),
    _Trm25xxTxLine_Type()
)
trm25xxTxLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm25xxTxLine.setStatus("current")
_Trm25xxOpticalOutPowLine_Type = Integer32
_Trm25xxOpticalOutPowLine_Object = MibTableColumn
trm25xxOpticalOutPowLine = _Trm25xxOpticalOutPowLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 13),
    _Trm25xxOpticalOutPowLine_Type()
)
trm25xxOpticalOutPowLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm25xxOpticalOutPowLine.setStatus("current")
_Trm25xxProdOutPowLine_Type = Integer32
_Trm25xxProdOutPowLine_Object = MibTableColumn
trm25xxProdOutPowLine = _Trm25xxProdOutPowLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 14),
    _Trm25xxProdOutPowLine_Type()
)
trm25xxProdOutPowLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm25xxProdOutPowLine.setStatus("current")
_Trm25xxLaserBiasCurLine_Type = Integer32
_Trm25xxLaserBiasCurLine_Object = MibTableColumn
trm25xxLaserBiasCurLine = _Trm25xxLaserBiasCurLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 15),
    _Trm25xxLaserBiasCurLine_Type()
)
trm25xxLaserBiasCurLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm25xxLaserBiasCurLine.setStatus("current")
_Trm25xxProdLaserBiasCurLine_Type = Integer32
_Trm25xxProdLaserBiasCurLine_Object = MibTableColumn
trm25xxProdLaserBiasCurLine = _Trm25xxProdLaserBiasCurLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 16),
    _Trm25xxProdLaserBiasCurLine_Type()
)
trm25xxProdLaserBiasCurLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm25xxProdLaserBiasCurLine.setStatus("current")
_Trm25xxCDR_Type = CDRMode
_Trm25xxCDR_Object = MibTableColumn
trm25xxCDR = _Trm25xxCDR_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 17),
    _Trm25xxCDR_Type()
)
trm25xxCDR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm25xxCDR.setStatus("current")
_Trm25xxCustomFibRate_Type = Integer32
_Trm25xxCustomFibRate_Object = MibTableColumn
trm25xxCustomFibRate = _Trm25xxCustomFibRate_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 18),
    _Trm25xxCustomFibRate_Type()
)
trm25xxCustomFibRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm25xxCustomFibRate.setStatus("current")
_Trm25xxTxMode_Type = TxMode76
_Trm25xxTxMode_Object = MibTableColumn
trm25xxTxMode = _Trm25xxTxMode_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 1, 1, 1, 19),
    _Trm25xxTxMode_Type()
)
trm25xxTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm25xxTxMode.setStatus("current")
_Trm25xxFM_ObjectIdentity = ObjectIdentity
trm25xxFM = _Trm25xxFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 2)
)
_Trm25xxTraps_ObjectIdentity = ObjectIdentity
trm25xxTraps = _Trm25xxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 2, 0)
)
_Trm53005500_ObjectIdentity = ObjectIdentity
trm53005500 = _Trm53005500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9)
)
_Trm53005500PM_ObjectIdentity = ObjectIdentity
trm53005500PM = _Trm53005500PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1)
)
_Trm53005500Table_Object = MibTable
trm53005500Table = _Trm53005500Table_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    trm53005500Table.setStatus("current")
_Trm53005500Entry_Object = MibTableRow
trm53005500Entry = _Trm53005500Entry_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1)
)
trm53005500Entry.setIndexNames(
    (0, "TRANSMODE1100", "trm53005500RackNumber"),
    (0, "TRANSMODE1100", "trm53005500SlotNumber"),
)
if mibBuilder.loadTexts:
    trm53005500Entry.setStatus("current")
_Trm53005500RackNumber_Type = RackNumber
_Trm53005500RackNumber_Object = MibTableColumn
trm53005500RackNumber = _Trm53005500RackNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 1),
    _Trm53005500RackNumber_Type()
)
trm53005500RackNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm53005500RackNumber.setStatus("current")
_Trm53005500SlotNumber_Type = BoardNumber
_Trm53005500SlotNumber_Object = MibTableColumn
trm53005500SlotNumber = _Trm53005500SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 2),
    _Trm53005500SlotNumber_Type()
)
trm53005500SlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trm53005500SlotNumber.setStatus("current")
_Trm53005500Temperature_Type = Integer32
_Trm53005500Temperature_Object = MibTableColumn
trm53005500Temperature = _Trm53005500Temperature_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 3),
    _Trm53005500Temperature_Type()
)
trm53005500Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500Temperature.setStatus("current")


class _Trm53005500SwReset_Type(Integer32):
    """Custom type trm53005500SwReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Trm53005500SwReset_Type.__name__ = "Integer32"
_Trm53005500SwReset_Object = MibTableColumn
trm53005500SwReset = _Trm53005500SwReset_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 4),
    _Trm53005500SwReset_Type()
)
trm53005500SwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500SwReset.setStatus("current")
_Trm53005500WavelengthLine_Type = DisplayString
_Trm53005500WavelengthLine_Object = MibTableColumn
trm53005500WavelengthLine = _Trm53005500WavelengthLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 5),
    _Trm53005500WavelengthLine_Type()
)
trm53005500WavelengthLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500WavelengthLine.setStatus("current")
_Trm53005500RxLine_Type = DisplayString
_Trm53005500RxLine_Object = MibTableColumn
trm53005500RxLine = _Trm53005500RxLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 6),
    _Trm53005500RxLine_Type()
)
trm53005500RxLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500RxLine.setStatus("current")
_Trm53005500OpticalInPowLine_Type = Integer32
_Trm53005500OpticalInPowLine_Object = MibTableColumn
trm53005500OpticalInPowLine = _Trm53005500OpticalInPowLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 7),
    _Trm53005500OpticalInPowLine_Type()
)
trm53005500OpticalInPowLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500OpticalInPowLine.setStatus("current")
_Trm53005500TxLine_Type = DisplayString
_Trm53005500TxLine_Object = MibTableColumn
trm53005500TxLine = _Trm53005500TxLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 8),
    _Trm53005500TxLine_Type()
)
trm53005500TxLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500TxLine.setStatus("current")
_Trm53005500TxModeLine_Type = TxMode75
_Trm53005500TxModeLine_Object = MibTableColumn
trm53005500TxModeLine = _Trm53005500TxModeLine_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 9),
    _Trm53005500TxModeLine_Type()
)
trm53005500TxModeLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500TxModeLine.setStatus("current")
_Trm53005500WavelengthClient1_Type = DisplayString
_Trm53005500WavelengthClient1_Object = MibTableColumn
trm53005500WavelengthClient1 = _Trm53005500WavelengthClient1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 10),
    _Trm53005500WavelengthClient1_Type()
)
trm53005500WavelengthClient1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500WavelengthClient1.setStatus("current")
_Trm53005500RxClient1_Type = DisplayString
_Trm53005500RxClient1_Object = MibTableColumn
trm53005500RxClient1 = _Trm53005500RxClient1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 11),
    _Trm53005500RxClient1_Type()
)
trm53005500RxClient1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500RxClient1.setStatus("current")
_Trm53005500CDRClient1_Type = CDR55Mode
_Trm53005500CDRClient1_Object = MibTableColumn
trm53005500CDRClient1 = _Trm53005500CDRClient1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 12),
    _Trm53005500CDRClient1_Type()
)
trm53005500CDRClient1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500CDRClient1.setStatus("current")
_Trm53005500TxClient1_Type = DisplayString
_Trm53005500TxClient1_Object = MibTableColumn
trm53005500TxClient1 = _Trm53005500TxClient1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 13),
    _Trm53005500TxClient1_Type()
)
trm53005500TxClient1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500TxClient1.setStatus("current")
_Trm53005500TxModeClient1_Type = TxMode76
_Trm53005500TxModeClient1_Object = MibTableColumn
trm53005500TxModeClient1 = _Trm53005500TxModeClient1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 14),
    _Trm53005500TxModeClient1_Type()
)
trm53005500TxModeClient1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500TxModeClient1.setStatus("current")
_Trm53005500IDStringClient1_Type = DisplayString
_Trm53005500IDStringClient1_Object = MibTableColumn
trm53005500IDStringClient1 = _Trm53005500IDStringClient1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 15),
    _Trm53005500IDStringClient1_Type()
)
trm53005500IDStringClient1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500IDStringClient1.setStatus("current")
_Trm53005500IPAddressClient1_Type = DisplayString
_Trm53005500IPAddressClient1_Object = MibTableColumn
trm53005500IPAddressClient1 = _Trm53005500IPAddressClient1_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 16),
    _Trm53005500IPAddressClient1_Type()
)
trm53005500IPAddressClient1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500IPAddressClient1.setStatus("current")
_Trm53005500WavelengthClient2_Type = DisplayString
_Trm53005500WavelengthClient2_Object = MibTableColumn
trm53005500WavelengthClient2 = _Trm53005500WavelengthClient2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 17),
    _Trm53005500WavelengthClient2_Type()
)
trm53005500WavelengthClient2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500WavelengthClient2.setStatus("current")
_Trm53005500RxClient2_Type = DisplayString
_Trm53005500RxClient2_Object = MibTableColumn
trm53005500RxClient2 = _Trm53005500RxClient2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 18),
    _Trm53005500RxClient2_Type()
)
trm53005500RxClient2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500RxClient2.setStatus("current")
_Trm53005500CDRClient2_Type = CDR55Mode
_Trm53005500CDRClient2_Object = MibTableColumn
trm53005500CDRClient2 = _Trm53005500CDRClient2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 19),
    _Trm53005500CDRClient2_Type()
)
trm53005500CDRClient2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500CDRClient2.setStatus("current")
_Trm53005500TxClient2_Type = DisplayString
_Trm53005500TxClient2_Object = MibTableColumn
trm53005500TxClient2 = _Trm53005500TxClient2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 20),
    _Trm53005500TxClient2_Type()
)
trm53005500TxClient2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500TxClient2.setStatus("current")
_Trm53005500TxModeClient2_Type = TxMode76
_Trm53005500TxModeClient2_Object = MibTableColumn
trm53005500TxModeClient2 = _Trm53005500TxModeClient2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 21),
    _Trm53005500TxModeClient2_Type()
)
trm53005500TxModeClient2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500TxModeClient2.setStatus("current")
_Trm53005500IDStringClient2_Type = DisplayString
_Trm53005500IDStringClient2_Object = MibTableColumn
trm53005500IDStringClient2 = _Trm53005500IDStringClient2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 22),
    _Trm53005500IDStringClient2_Type()
)
trm53005500IDStringClient2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500IDStringClient2.setStatus("current")
_Trm53005500IPAddressClient2_Type = DisplayString
_Trm53005500IPAddressClient2_Object = MibTableColumn
trm53005500IPAddressClient2 = _Trm53005500IPAddressClient2_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 23),
    _Trm53005500IPAddressClient2_Type()
)
trm53005500IPAddressClient2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500IPAddressClient2.setStatus("current")
_Trm53005500WavelengthClient3_Type = DisplayString
_Trm53005500WavelengthClient3_Object = MibTableColumn
trm53005500WavelengthClient3 = _Trm53005500WavelengthClient3_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 24),
    _Trm53005500WavelengthClient3_Type()
)
trm53005500WavelengthClient3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500WavelengthClient3.setStatus("current")
_Trm53005500RxClient3_Type = DisplayString
_Trm53005500RxClient3_Object = MibTableColumn
trm53005500RxClient3 = _Trm53005500RxClient3_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 25),
    _Trm53005500RxClient3_Type()
)
trm53005500RxClient3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500RxClient3.setStatus("current")
_Trm53005500CDRClient3_Type = CDR55Mode
_Trm53005500CDRClient3_Object = MibTableColumn
trm53005500CDRClient3 = _Trm53005500CDRClient3_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 26),
    _Trm53005500CDRClient3_Type()
)
trm53005500CDRClient3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500CDRClient3.setStatus("current")
_Trm53005500TxClient3_Type = DisplayString
_Trm53005500TxClient3_Object = MibTableColumn
trm53005500TxClient3 = _Trm53005500TxClient3_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 27),
    _Trm53005500TxClient3_Type()
)
trm53005500TxClient3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500TxClient3.setStatus("current")
_Trm53005500TxModeClient3_Type = TxMode76
_Trm53005500TxModeClient3_Object = MibTableColumn
trm53005500TxModeClient3 = _Trm53005500TxModeClient3_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 28),
    _Trm53005500TxModeClient3_Type()
)
trm53005500TxModeClient3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500TxModeClient3.setStatus("current")
_Trm53005500IDStringClient3_Type = DisplayString
_Trm53005500IDStringClient3_Object = MibTableColumn
trm53005500IDStringClient3 = _Trm53005500IDStringClient3_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 29),
    _Trm53005500IDStringClient3_Type()
)
trm53005500IDStringClient3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500IDStringClient3.setStatus("current")
_Trm53005500IPAddressClient3_Type = DisplayString
_Trm53005500IPAddressClient3_Object = MibTableColumn
trm53005500IPAddressClient3 = _Trm53005500IPAddressClient3_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 30),
    _Trm53005500IPAddressClient3_Type()
)
trm53005500IPAddressClient3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500IPAddressClient3.setStatus("current")
_Trm53005500WavelengthClient4_Type = DisplayString
_Trm53005500WavelengthClient4_Object = MibTableColumn
trm53005500WavelengthClient4 = _Trm53005500WavelengthClient4_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 31),
    _Trm53005500WavelengthClient4_Type()
)
trm53005500WavelengthClient4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500WavelengthClient4.setStatus("current")
_Trm53005500RxClient4_Type = DisplayString
_Trm53005500RxClient4_Object = MibTableColumn
trm53005500RxClient4 = _Trm53005500RxClient4_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 32),
    _Trm53005500RxClient4_Type()
)
trm53005500RxClient4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500RxClient4.setStatus("current")
_Trm53005500CDRClient4_Type = CDR55Mode
_Trm53005500CDRClient4_Object = MibTableColumn
trm53005500CDRClient4 = _Trm53005500CDRClient4_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 33),
    _Trm53005500CDRClient4_Type()
)
trm53005500CDRClient4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500CDRClient4.setStatus("current")
_Trm53005500TxClient4_Type = DisplayString
_Trm53005500TxClient4_Object = MibTableColumn
trm53005500TxClient4 = _Trm53005500TxClient4_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 34),
    _Trm53005500TxClient4_Type()
)
trm53005500TxClient4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trm53005500TxClient4.setStatus("current")
_Trm53005500TxModeClient4_Type = TxMode76
_Trm53005500TxModeClient4_Object = MibTableColumn
trm53005500TxModeClient4 = _Trm53005500TxModeClient4_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 35),
    _Trm53005500TxModeClient4_Type()
)
trm53005500TxModeClient4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500TxModeClient4.setStatus("current")
_Trm53005500IDStringClient4_Type = DisplayString
_Trm53005500IDStringClient4_Object = MibTableColumn
trm53005500IDStringClient4 = _Trm53005500IDStringClient4_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 36),
    _Trm53005500IDStringClient4_Type()
)
trm53005500IDStringClient4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500IDStringClient4.setStatus("current")
_Trm53005500IPAddressClient4_Type = DisplayString
_Trm53005500IPAddressClient4_Object = MibTableColumn
trm53005500IPAddressClient4 = _Trm53005500IPAddressClient4_Object(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 1, 1, 1, 37),
    _Trm53005500IPAddressClient4_Type()
)
trm53005500IPAddressClient4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trm53005500IPAddressClient4.setStatus("current")
_Trm53005500FM_ObjectIdentity = ObjectIdentity
trm53005500FM = _Trm53005500FM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2)
)
_Trm53005500Traps_ObjectIdentity = ObjectIdentity
trm53005500Traps = _Trm53005500Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0)
)
_TrmSubrackFM_ObjectIdentity = ObjectIdentity
trmSubrackFM = _TrmSubrackFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 3)
)
_TrmSubrackTraps_ObjectIdentity = ObjectIdentity
trmSubrackTraps = _TrmSubrackTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 3, 0)
)

# Managed Objects groups


# Notification objects

trm6001TrapExternal1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 2, 0, 1)
)
trm6001TrapExternal1.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm6001TrapExternal1.setStatus(
        "current"
    )

trm6001TrapExternal2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 2, 0, 2)
)
trm6001TrapExternal2.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm6001TrapExternal2.setStatus(
        "current"
    )

trm6001TrapExternal3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 2, 0, 3)
)
trm6001TrapExternal3.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm6001TrapExternal3.setStatus(
        "current"
    )

trm6001CascadeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 1, 2, 0, 4)
)
trm6001CascadeFailure.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm6001CascadeFailure.setStatus(
        "current"
    )

trm9xxxTrapFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2, 2, 0, 1)
)
trm9xxxTrapFailure.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm9xxxTrapFailure.setStatus(
        "current"
    )

trm9xxxTrapMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 2, 2, 0, 2)
)
trm9xxxTrapMissing.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm9xxxTrapMissing.setStatus(
        "current"
    )

trm75xxTrapGlitchLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 2, 0, 1)
)
trm75xxTrapGlitchLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm75xxTrapGlitchLine.setStatus(
        "current"
    )

trm75xxTrapLopLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 2, 0, 2)
)
trm75xxTrapLopLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm75xxTrapLopLine.setStatus(
        "current"
    )

trm75xxTrapTxLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 2, 0, 3)
)
trm75xxTrapTxLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm75xxTrapTxLine.setStatus(
        "current"
    )

trm75xxTrapTxDisableLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 2, 0, 4)
)
trm75xxTrapTxDisableLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm75xxTrapTxDisableLine.setStatus(
        "current"
    )

trm75xxTrapGlitchClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 2, 0, 5)
)
trm75xxTrapGlitchClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm75xxTrapGlitchClient.setStatus(
        "current"
    )

trm75xxTrapLopClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 2, 0, 6)
)
trm75xxTrapLopClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm75xxTrapLopClient.setStatus(
        "current"
    )

trm75xxTrapTxClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 2, 0, 7)
)
trm75xxTrapTxClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm75xxTrapTxClient.setStatus(
        "current"
    )

trm75xxTrapTxDisableClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 3, 2, 0, 8)
)
trm75xxTrapTxDisableClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm75xxTrapTxDisableClient.setStatus(
        "current"
    )

trm76xxTrapCDRAutoModeRangeChangeLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 1)
)
trm76xxTrapCDRAutoModeRangeChangeLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapCDRAutoModeRangeChangeLine.setStatus(
        "current"
    )

trm76xxTrapRxGlitchLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 2)
)
trm76xxTrapRxGlitchLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapRxGlitchLine.setStatus(
        "current"
    )

trm76xxTrapLopLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 3)
)
trm76xxTrapLopLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapLopLine.setStatus(
        "current"
    )

trm76xxTrapRxHighPowerLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 4)
)
trm76xxTrapRxHighPowerLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapRxHighPowerLine.setStatus(
        "current"
    )

trm76xxTrapRxLowPowerLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 5)
)
trm76xxTrapRxLowPowerLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapRxLowPowerLine.setStatus(
        "current"
    )

trm76xxTrapLoLLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 6)
)
trm76xxTrapLoLLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapLoLLine.setStatus(
        "current"
    )

trm76xxTrapTxLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 7)
)
trm76xxTrapTxLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapTxLine.setStatus(
        "current"
    )

trm76xxTrapSFPFailureLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 8)
)
trm76xxTrapSFPFailureLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapSFPFailureLine.setStatus(
        "obsolete"
    )

trm76xxTrapSFPMissingLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 9)
)
trm76xxTrapSFPMissingLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapSFPMissingLine.setStatus(
        "obsolete"
    )

trm76xxTrapCDRAutoModeRangeChangeClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 10)
)
trm76xxTrapCDRAutoModeRangeChangeClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapCDRAutoModeRangeChangeClient.setStatus(
        "current"
    )

trm76xxTrapRxGlitchClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 11)
)
trm76xxTrapRxGlitchClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapRxGlitchClient.setStatus(
        "current"
    )

trm76xxTrapLopClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 12)
)
trm76xxTrapLopClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapLopClient.setStatus(
        "current"
    )

trm76xxTrapRxHighPowerClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 13)
)
trm76xxTrapRxHighPowerClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapRxHighPowerClient.setStatus(
        "obsolete"
    )

trm76xxTrapRxLowPowerClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 14)
)
trm76xxTrapRxLowPowerClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapRxLowPowerClient.setStatus(
        "obsolete"
    )

trm76xxTrapLoLClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 15)
)
trm76xxTrapLoLClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapLoLClient.setStatus(
        "current"
    )

trm76xxTrapTxClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 16)
)
trm76xxTrapTxClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapTxClient.setStatus(
        "current"
    )

trm76xxTrapSFPFailureClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 17)
)
trm76xxTrapSFPFailureClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapSFPFailureClient.setStatus(
        "current"
    )

trm76xxTrapSFPMissingClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 18)
)
trm76xxTrapSFPMissingClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapSFPMissingClient.setStatus(
        "current"
    )

trm76xxTrapTxDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 19)
)
trm76xxTrapTxDisable.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapTxDisable.setStatus(
        "current"
    )

trm76xxTrapLaserDegradationLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 20)
)
trm76xxTrapLaserDegradationLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapLaserDegradationLine.setStatus(
        "current"
    )

trm76xxTrapEyeQualityLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 21)
)
trm76xxTrapEyeQualityLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapEyeQualityLine.setStatus(
        "current"
    )

trm76xxTrapEyeQualityClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 4, 2, 0, 22)
)
trm76xxTrapEyeQualityClient.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm76xxTrapEyeQualityClient.setStatus(
        "current"
    )

trm26xxTrapTEC1Faulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 2, 0, 1)
)
trm26xxTrapTEC1Faulty.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm26xxTrapTEC1Faulty.setStatus(
        "current"
    )

trm26xxTrapTEC2Faulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 2, 0, 2)
)
trm26xxTrapTEC2Faulty.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm26xxTrapTEC2Faulty.setStatus(
        "current"
    )

trm26xxTrapBIAS1Faulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 2, 0, 3)
)
trm26xxTrapBIAS1Faulty.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm26xxTrapBIAS1Faulty.setStatus(
        "current"
    )

trm26xxTrapBIAS2Faulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 2, 0, 4)
)
trm26xxTrapBIAS2Faulty.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm26xxTrapBIAS2Faulty.setStatus(
        "current"
    )

trm26xxTrapPIUTempShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 2, 0, 5)
)
trm26xxTrapPIUTempShutdown.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm26xxTrapPIUTempShutdown.setStatus(
        "current"
    )

trm26xxTrapOpticalLinkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 2, 0, 6)
)
trm26xxTrapOpticalLinkdown.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm26xxTrapOpticalLinkdown.setStatus(
        "current"
    )

trm26xxTrapTxDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 7, 2, 0, 7)
)
trm26xxTrapTxDisable.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm26xxTrapTxDisable.setStatus(
        "current"
    )

trm25xxTrapWorkingLineFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 2, 0, 1)
)
trm25xxTrapWorkingLineFailure.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm25xxTrapWorkingLineFailure.setStatus(
        "current"
    )

trm25xxTrapProtectingLineFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 2, 0, 2)
)
trm25xxTrapProtectingLineFailure.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm25xxTrapProtectingLineFailure.setStatus(
        "current"
    )

trm25xxTrapWorkingAndProtectingLineFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 8, 2, 0, 3)
)
trm25xxTrapWorkingAndProtectingLineFailure.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm25xxTrapWorkingAndProtectingLineFailure.setStatus(
        "current"
    )

trm53005500TrapRxLinkdownLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 1)
)
trm53005500TrapRxLinkdownLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapRxLinkdownLine.setStatus(
        "current"
    )

trm53005500TrapExternalsyncFailureLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 2)
)
trm53005500TrapExternalsyncFailureLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapExternalsyncFailureLine.setStatus(
        "current"
    )

trm53005500TrapSfpMissingLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 3)
)
trm53005500TrapSfpMissingLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpMissingLine.setStatus(
        "current"
    )

trm53005500TrapSfpBadTypeLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 4)
)
trm53005500TrapSfpBadTypeLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpBadTypeLine.setStatus(
        "current"
    )

trm53005500TrapSfpFaultyLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 5)
)
trm53005500TrapSfpFaultyLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpFaultyLine.setStatus(
        "current"
    )

trm53005500TrapRxGlitchLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 6)
)
trm53005500TrapRxGlitchLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapRxGlitchLine.setStatus(
        "current"
    )

trm53005500TrapTxGlitchLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 7)
)
trm53005500TrapTxGlitchLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxGlitchLine.setStatus(
        "current"
    )

trm53005500TrapTxDisabledLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 8)
)
trm53005500TrapTxDisabledLine.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxDisabledLine.setStatus(
        "current"
    )

trm53005500TrapRxLinkDownClient1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 9)
)
trm53005500TrapRxLinkDownClient1.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapRxLinkDownClient1.setStatus(
        "current"
    )

trm53005500TrapTxOutOfSyncClient1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 10)
)
trm53005500TrapTxOutOfSyncClient1.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxOutOfSyncClient1.setStatus(
        "current"
    )

trm53005500TrapSfpMissingClient1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 11)
)
trm53005500TrapSfpMissingClient1.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpMissingClient1.setStatus(
        "current"
    )

trm53005500TrapSfpBadTypeClient1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 12)
)
trm53005500TrapSfpBadTypeClient1.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpBadTypeClient1.setStatus(
        "current"
    )

trm53005500TrapSfpFaultyClient1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 13)
)
trm53005500TrapSfpFaultyClient1.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpFaultyClient1.setStatus(
        "current"
    )

trm53005500TrapTxGlitchClient1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 14)
)
trm53005500TrapTxGlitchClient1.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxGlitchClient1.setStatus(
        "current"
    )

trm53005500TrapRxGlitchClient1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 15)
)
trm53005500TrapRxGlitchClient1.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapRxGlitchClient1.setStatus(
        "current"
    )

trm53005500TrapTxDisabledClient1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 16)
)
trm53005500TrapTxDisabledClient1.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxDisabledClient1.setStatus(
        "current"
    )

trm53005500TrapRxLinkDownClient2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 17)
)
trm53005500TrapRxLinkDownClient2.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapRxLinkDownClient2.setStatus(
        "current"
    )

trm53005500TrapTxOutOfSyncClient2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 18)
)
trm53005500TrapTxOutOfSyncClient2.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxOutOfSyncClient2.setStatus(
        "current"
    )

trm53005500TrapSfpMissingClient2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 19)
)
trm53005500TrapSfpMissingClient2.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpMissingClient2.setStatus(
        "current"
    )

trm53005500TrapSfpBadTypeClient2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 20)
)
trm53005500TrapSfpBadTypeClient2.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpBadTypeClient2.setStatus(
        "current"
    )

trm53005500TrapSfpFaultyClient2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 21)
)
trm53005500TrapSfpFaultyClient2.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpFaultyClient2.setStatus(
        "current"
    )

trm53005500TrapTxGlitchClient2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 22)
)
trm53005500TrapTxGlitchClient2.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxGlitchClient2.setStatus(
        "current"
    )

trm53005500TrapRxGlitchClient2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 23)
)
trm53005500TrapRxGlitchClient2.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapRxGlitchClient2.setStatus(
        "current"
    )

trm53005500TrapTxDisabledClient2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 24)
)
trm53005500TrapTxDisabledClient2.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxDisabledClient2.setStatus(
        "current"
    )

trm53005500TrapRxLinkDownClient3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 25)
)
trm53005500TrapRxLinkDownClient3.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapRxLinkDownClient3.setStatus(
        "current"
    )

trm53005500TrapTxOutOfSyncClient3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 26)
)
trm53005500TrapTxOutOfSyncClient3.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxOutOfSyncClient3.setStatus(
        "current"
    )

trm53005500TrapSfpMissingClient3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 27)
)
trm53005500TrapSfpMissingClient3.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpMissingClient3.setStatus(
        "current"
    )

trm53005500TrapSfpBadTypeClient3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 28)
)
trm53005500TrapSfpBadTypeClient3.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpBadTypeClient3.setStatus(
        "current"
    )

trm53005500TrapSfpFaultyClient3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 29)
)
trm53005500TrapSfpFaultyClient3.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpFaultyClient3.setStatus(
        "current"
    )

trm53005500TrapTxGlitchClient3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 30)
)
trm53005500TrapTxGlitchClient3.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxGlitchClient3.setStatus(
        "current"
    )

trm53005500TrapRxGlitchClient3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 31)
)
trm53005500TrapRxGlitchClient3.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapRxGlitchClient3.setStatus(
        "current"
    )

trm53005500TrapTxDisabledClient3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 32)
)
trm53005500TrapTxDisabledClient3.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxDisabledClient3.setStatus(
        "current"
    )

trm53005500TrapRxLinkDownClient4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 33)
)
trm53005500TrapRxLinkDownClient4.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapRxLinkDownClient4.setStatus(
        "current"
    )

trm53005500TrapTxOutOfSyncClient4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 34)
)
trm53005500TrapTxOutOfSyncClient4.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxOutOfSyncClient4.setStatus(
        "current"
    )

trm53005500TrapSfpMissingClient4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 35)
)
trm53005500TrapSfpMissingClient4.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpMissingClient4.setStatus(
        "current"
    )

trm53005500TrapSfpBadTypeClient4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 36)
)
trm53005500TrapSfpBadTypeClient4.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpBadTypeClient4.setStatus(
        "current"
    )

trm53005500TrapSfpFaultyClient4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 37)
)
trm53005500TrapSfpFaultyClient4.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapSfpFaultyClient4.setStatus(
        "current"
    )

trm53005500TrapTxGlitchClient4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 38)
)
trm53005500TrapTxGlitchClient4.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxGlitchClient4.setStatus(
        "current"
    )

trm53005500TrapRxGlitchClient4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 39)
)
trm53005500TrapRxGlitchClient4.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapRxGlitchClient4.setStatus(
        "current"
    )

trm53005500TrapTxDisabledClient4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 40)
)
trm53005500TrapTxDisabledClient4.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapTxDisabledClient4.setStatus(
        "current"
    )

trm53005500TrapHwFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 2, 9, 2, 0, 41)
)
trm53005500TrapHwFailure.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trm53005500TrapHwFailure.setStatus(
        "current"
    )

trmTrapBmiLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 3, 0, 1)
)
trmTrapBmiLost.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trmTrapBmiLost.setStatus(
        "current"
    )

trmTrapBmiError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 3, 0, 2)
)
trmTrapBmiError.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trmTrapBmiError.setStatus(
        "current"
    )

trmTrapHighTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 3, 0, 3)
)
trmTrapHighTemp.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trmTrapHighTemp.setStatus(
        "current"
    )

trmTrapLowTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 3, 0, 4)
)
trmTrapLowTemp.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trmTrapLowTemp.setStatus(
        "current"
    )

trmTrapVeryHighTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 3, 0, 5)
)
trmTrapVeryHighTemp.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trmTrapVeryHighTemp.setStatus(
        "current"
    )

trmTrapSpeedLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11857, 1, 2, 3, 0, 6)
)
trmTrapSpeedLimitExceeded.setObjects(
      *(("TRANSMODE1100", "trmAlarmActiveName"),
        ("TRANSMODE1100", "trmAlarmActiveSeverity"),
        ("TRANSMODE1100", "trmAlarmActiveActTime"),
        ("TRANSMODE1100", "trmAlarmActiveUnit"),
        ("TRANSMODE1100", "trmAlarmActiveRackNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSlotNumber"),
        ("TRANSMODE1100", "trmAlarmActiveSerialNumber"))
)
if mibBuilder.loadTexts:
    trmTrapSpeedLimitExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRANSMODE1100",
    **{"AlarmClass": AlarmClass,
       "PerceivedSeverity": PerceivedSeverity,
       "AlarmSeverity": AlarmSeverity,
       "RowStatus": RowStatus,
       "OwnerString": OwnerString,
       "TrafficStatus": TrafficStatus,
       "TxMode76": TxMode76,
       "TxMode75": TxMode75,
       "Present": Present,
       "PowerStatus": PowerStatus,
       "PowerType": PowerType,
       "MuxType": MuxType,
       "ExternalAlarmLevel": ExternalAlarmLevel,
       "AlarmStatus": AlarmStatus,
       "Switch": Switch,
       "PortType": PortType,
       "RackNumber": RackNumber,
       "SlotNumber": SlotNumber,
       "BoardNumber": BoardNumber,
       "SlotNumberPS": SlotNumberPS,
       "SlotNumberNmb": SlotNumberNmb,
       "AlarmAcknowledge": AlarmAcknowledge,
       "LineLoopMode": LineLoopMode,
       "CDRMode": CDRMode,
       "TrmDate": TrmDate,
       "TrmTime": TrmTime,
       "SecurityMode": SecurityMode,
       "SpeedLimit75": SpeedLimit75,
       "SpeedLimit76": SpeedLimit76,
       "CascadeStatus": CascadeStatus,
       "CascadeMode": CascadeMode,
       "CDR55Mode": CDR55Mode,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "transmode": transmode,
       "system1100": system1100,
       "trmAlarmHandling": trmAlarmHandling,
       "trmAlarmConfig": trmAlarmConfig,
       "trmAlarmGeneral": trmAlarmGeneral,
       "trmAutoAcknowledge": trmAutoAcknowledge,
       "trmClearAlarmLog": trmClearAlarmLog,
       "trmTemperature": trmTemperature,
       "trmAlarmTemperatureHigh": trmAlarmTemperatureHigh,
       "trmAlarmTemperatureHighHyst": trmAlarmTemperatureHighHyst,
       "trmAlarmTemperatureLow": trmAlarmTemperatureLow,
       "trmAlarmTemperatureLowHyst": trmAlarmTemperatureLowHyst,
       "trmPluginReset": trmPluginReset,
       "trmOpticalInputPowerHighPINLine": trmOpticalInputPowerHighPINLine,
       "trmOpticalInputPowerHighAPDLine": trmOpticalInputPowerHighAPDLine,
       "trmOpticalInputPowerLowPINLine": trmOpticalInputPowerLowPINLine,
       "trmOpticalInputPowerLowAPDLine": trmOpticalInputPowerLowAPDLine,
       "trmCascade": trmCascade,
       "trmCascadeStatus": trmCascadeStatus,
       "trmOpticalInputPowerHighAPDLine2": trmOpticalInputPowerHighAPDLine2,
       "trmOpticalInputPowerLowAPDLine2": trmOpticalInputPowerLowAPDLine2,
       "trmOpticalInputPowerHigh850Client": trmOpticalInputPowerHigh850Client,
       "trmOpticalInputPowerHigh1310Client": trmOpticalInputPowerHigh1310Client,
       "trmOpticalInputPowerLow850Client": trmOpticalInputPowerLow850Client,
       "trmOpticalInputPowerLow1310Client": trmOpticalInputPowerLow1310Client,
       "trmAlarmSeverity": trmAlarmSeverity,
       "trmAlarmSeverityTable": trmAlarmSeverityTable,
       "trmAlarmSeverityEntry": trmAlarmSeverityEntry,
       "trmAlarmSeverityId": trmAlarmSeverityId,
       "trmAlarmSeverityName": trmAlarmSeverityName,
       "trmAlarmSeverityLevel": trmAlarmSeverityLevel,
       "trmAlarmExternal": trmAlarmExternal,
       "trmAlarmExternalTable": trmAlarmExternalTable,
       "trmAlarmExternalEntry": trmAlarmExternalEntry,
       "trmAlarmExternalId": trmAlarmExternalId,
       "trmAlarmExternalName": trmAlarmExternalName,
       "trmAlarmExternalLevel": trmAlarmExternalLevel,
       "trmAlarmLog": trmAlarmLog,
       "trmAlarmLogTable": trmAlarmLogTable,
       "trmAlarmLogEntry": trmAlarmLogEntry,
       "trmAlarmLogIndex": trmAlarmLogIndex,
       "trmAlarmLogRackNumber": trmAlarmLogRackNumber,
       "trmAlarmLogSlotNumber": trmAlarmLogSlotNumber,
       "trmAlarmLogName": trmAlarmLogName,
       "trmAlarmLogSeverity": trmAlarmLogSeverity,
       "trmAlarmLogUnit": trmAlarmLogUnit,
       "trmAlarmLogSerialNumber": trmAlarmLogSerialNumber,
       "trmAlarmLogActTime": trmAlarmLogActTime,
       "trmAlarmLogDeactTime": trmAlarmLogDeactTime,
       "trmAlarmLogAckTime": trmAlarmLogAckTime,
       "trmAlarmLogAckUser": trmAlarmLogAckUser,
       "trmAlarmActive": trmAlarmActive,
       "trmAlarmActiveGeneral": trmAlarmActiveGeneral,
       "trmAlarmActiveCounter": trmAlarmActiveCounter,
       "trmAlarmActiveAcknowledgeAllDeact": trmAlarmActiveAcknowledgeAllDeact,
       "trmAlarmActiveAcknowledgeAll": trmAlarmActiveAcknowledgeAll,
       "trmAlarmActiveTable": trmAlarmActiveTable,
       "trmAlarmActiveEntry": trmAlarmActiveEntry,
       "trmAlarmActiveIndex": trmAlarmActiveIndex,
       "trmAlarmActiveRackNumber": trmAlarmActiveRackNumber,
       "trmAlarmActiveSlotNumber": trmAlarmActiveSlotNumber,
       "trmAlarmActiveName": trmAlarmActiveName,
       "trmAlarmActiveSeverity": trmAlarmActiveSeverity,
       "trmAlarmActiveUnit": trmAlarmActiveUnit,
       "trmAlarmActiveSerialNumber": trmAlarmActiveSerialNumber,
       "trmAlarmActiveActTime": trmAlarmActiveActTime,
       "trmAlarmActiveDeactTime": trmAlarmActiveDeactTime,
       "trmAlarmActiveAcknowledge": trmAlarmActiveAcknowledge,
       "trmSubrack": trmSubrack,
       "trmSubrackList": trmSubrackList,
       "trmSubrackListTable": trmSubrackListTable,
       "trmSubrackListEntry": trmSubrackListEntry,
       "trmListRackNumber": trmListRackNumber,
       "trmListSlotNumber": trmListSlotNumber,
       "trmListUnitPresent": trmListUnitPresent,
       "trmListProductNumber": trmListProductNumber,
       "trmListProductDescription": trmListProductDescription,
       "trmListHwRevision": trmListHwRevision,
       "trmListSerialNumber": trmListSerialNumber,
       "trmListManufacturingDate": trmListManufacturingDate,
       "trmListSoftwareProdNo": trmListSoftwareProdNo,
       "trmListSwVersion": trmListSwVersion,
       "trmSubrackUnits": trmSubrackUnits,
       "trm6001": trm6001,
       "trm6001PM": trm6001PM,
       "trm6001Table": trm6001Table,
       "trm6001Entry": trm6001Entry,
       "trm6001RackNumber": trm6001RackNumber,
       "trm6001SlotNumber": trm6001SlotNumber,
       "trm6001IPAddress": trm6001IPAddress,
       "trm6001MACAddress": trm6001MACAddress,
       "trm6001Temperature": trm6001Temperature,
       "trm6001UpTime": trm6001UpTime,
       "trm6001Date": trm6001Date,
       "trm6001Time": trm6001Time,
       "trm6001SwReset": trm6001SwReset,
       "trm6001FM": trm6001FM,
       "trm6001Traps": trm6001Traps,
       "trm6001TrapExternal1": trm6001TrapExternal1,
       "trm6001TrapExternal2": trm6001TrapExternal2,
       "trm6001TrapExternal3": trm6001TrapExternal3,
       "trm6001CascadeFailure": trm6001CascadeFailure,
       "trm9xxx": trm9xxx,
       "trm9xxxPM": trm9xxxPM,
       "trm9xxxTable": trm9xxxTable,
       "trm9xxxEntry": trm9xxxEntry,
       "trm9xxxRackNumber": trm9xxxRackNumber,
       "trm9xxxSlotNumber": trm9xxxSlotNumber,
       "trm9xxxPresent": trm9xxxPresent,
       "trm9xxxType": trm9xxxType,
       "trm9xxxStatus": trm9xxxStatus,
       "trm9xxxFM": trm9xxxFM,
       "trm9xxxTraps": trm9xxxTraps,
       "trm9xxxTrapFailure": trm9xxxTrapFailure,
       "trm9xxxTrapMissing": trm9xxxTrapMissing,
       "trm75xx": trm75xx,
       "trm75xxPM": trm75xxPM,
       "trm75xxTable": trm75xxTable,
       "trm75xxEntry": trm75xxEntry,
       "trm75xxRackNumber": trm75xxRackNumber,
       "trm75xxSlotNumber": trm75xxSlotNumber,
       "trm75xxRxLine": trm75xxRxLine,
       "trm75xxEstProtLine": trm75xxEstProtLine,
       "trm75xxEstFibRateLine": trm75xxEstFibRateLine,
       "trm75xxTxLine": trm75xxTxLine,
       "trm75xxTxMode": trm75xxTxMode,
       "trm75xxWavelengthLine": trm75xxWavelengthLine,
       "trm75xxRxClient": trm75xxRxClient,
       "trm75xxEstProtClient": trm75xxEstProtClient,
       "trm75xxEstFibRateClient": trm75xxEstFibRateClient,
       "trm75xxTxClient": trm75xxTxClient,
       "trm75xxTxModeClient": trm75xxTxModeClient,
       "trm75xxIDStringClient": trm75xxIDStringClient,
       "trm75xxIPAddressClient": trm75xxIPAddressClient,
       "trm75xxWavelengthClient": trm75xxWavelengthClient,
       "trm75xxSpeedLimit": trm75xxSpeedLimit,
       "trm75xxFM": trm75xxFM,
       "trm75xxTraps": trm75xxTraps,
       "trm75xxTrapGlitchLine": trm75xxTrapGlitchLine,
       "trm75xxTrapLopLine": trm75xxTrapLopLine,
       "trm75xxTrapTxLine": trm75xxTrapTxLine,
       "trm75xxTrapTxDisableLine": trm75xxTrapTxDisableLine,
       "trm75xxTrapGlitchClient": trm75xxTrapGlitchClient,
       "trm75xxTrapLopClient": trm75xxTrapLopClient,
       "trm75xxTrapTxClient": trm75xxTrapTxClient,
       "trm75xxTrapTxDisableClient": trm75xxTrapTxDisableClient,
       "trm76xx": trm76xx,
       "trm76xxPM": trm76xxPM,
       "trm76xxTable": trm76xxTable,
       "trm76xxEntry": trm76xxEntry,
       "trm76xxRackNumber": trm76xxRackNumber,
       "trm76xxSlotNumber": trm76xxSlotNumber,
       "trm76xxTemperature": trm76xxTemperature,
       "trm76xxCDR": trm76xxCDR,
       "trm76xxCustomFibRate": trm76xxCustomFibRate,
       "trm76xxTxMode": trm76xxTxMode,
       "trm76xxLineLoopMode": trm76xxLineLoopMode,
       "trm76xxSwReset": trm76xxSwReset,
       "trm76xxRxLine": trm76xxRxLine,
       "trm76xxOpticalInPowLine": trm76xxOpticalInPowLine,
       "trm76xxSpeedLimit": trm76xxSpeedLimit,
       "trm76xxEstProtLine": trm76xxEstProtLine,
       "trm76xxEstFibRateLine": trm76xxEstFibRateLine,
       "trm76xxTxLine": trm76xxTxLine,
       "trm76xxOpticalOutPowLine": trm76xxOpticalOutPowLine,
       "trm76xxProdOutPowLine": trm76xxProdOutPowLine,
       "trm76xxLaserBiasCurLine": trm76xxLaserBiasCurLine,
       "trm76xxProdLaserBiasCurLine": trm76xxProdLaserBiasCurLine,
       "trm76xxWavelengthLine": trm76xxWavelengthLine,
       "trm76xxRxClient": trm76xxRxClient,
       "trm76xxEstProtClient": trm76xxEstProtClient,
       "trm76xxEstFibRateClient": trm76xxEstFibRateClient,
       "trm76xxTxClient": trm76xxTxClient,
       "trm76xxIDStringClient": trm76xxIDStringClient,
       "trm76xxIPAddressClient": trm76xxIPAddressClient,
       "trm76xxWavelengthClient": trm76xxWavelengthClient,
       "trm76xxOpticalInPowClient": trm76xxOpticalInPowClient,
       "trm76xxOpticalOutPowClient": trm76xxOpticalOutPowClient,
       "trm76xxLaserBiasCurClient": trm76xxLaserBiasCurClient,
       "trm76xxFM": trm76xxFM,
       "trm76xxTraps": trm76xxTraps,
       "trm76xxTrapCDRAutoModeRangeChangeLine": trm76xxTrapCDRAutoModeRangeChangeLine,
       "trm76xxTrapRxGlitchLine": trm76xxTrapRxGlitchLine,
       "trm76xxTrapLopLine": trm76xxTrapLopLine,
       "trm76xxTrapRxHighPowerLine": trm76xxTrapRxHighPowerLine,
       "trm76xxTrapRxLowPowerLine": trm76xxTrapRxLowPowerLine,
       "trm76xxTrapLoLLine": trm76xxTrapLoLLine,
       "trm76xxTrapTxLine": trm76xxTrapTxLine,
       "trm76xxTrapSFPFailureLine": trm76xxTrapSFPFailureLine,
       "trm76xxTrapSFPMissingLine": trm76xxTrapSFPMissingLine,
       "trm76xxTrapCDRAutoModeRangeChangeClient": trm76xxTrapCDRAutoModeRangeChangeClient,
       "trm76xxTrapRxGlitchClient": trm76xxTrapRxGlitchClient,
       "trm76xxTrapLopClient": trm76xxTrapLopClient,
       "trm76xxTrapRxHighPowerClient": trm76xxTrapRxHighPowerClient,
       "trm76xxTrapRxLowPowerClient": trm76xxTrapRxLowPowerClient,
       "trm76xxTrapLoLClient": trm76xxTrapLoLClient,
       "trm76xxTrapTxClient": trm76xxTrapTxClient,
       "trm76xxTrapSFPFailureClient": trm76xxTrapSFPFailureClient,
       "trm76xxTrapSFPMissingClient": trm76xxTrapSFPMissingClient,
       "trm76xxTrapTxDisable": trm76xxTrapTxDisable,
       "trm76xxTrapLaserDegradationLine": trm76xxTrapLaserDegradationLine,
       "trm76xxTrapEyeQualityLine": trm76xxTrapEyeQualityLine,
       "trm76xxTrapEyeQualityClient": trm76xxTrapEyeQualityClient,
       "trm803x": trm803x,
       "trm803xPM": trm803xPM,
       "trm803xTable": trm803xTable,
       "trm803xEntry": trm803xEntry,
       "trm803xRackNumber": trm803xRackNumber,
       "trm803xSlotNumber": trm803xSlotNumber,
       "trm803xMuxType": trm803xMuxType,
       "trm803xIDStringLine": trm803xIDStringLine,
       "trm803xIPAddressLine": trm803xIPAddressLine,
       "trm2204": trm2204,
       "trm2204PM": trm2204PM,
       "trm2204Table": trm2204Table,
       "trm2204Entry": trm2204Entry,
       "trm2204RackNumber": trm2204RackNumber,
       "trm2204SlotNumber": trm2204SlotNumber,
       "trm2204SecurityMode": trm2204SecurityMode,
       "trm26xx": trm26xx,
       "trm26xxPM": trm26xxPM,
       "trm26xxTable": trm26xxTable,
       "trm26xxEntry": trm26xxEntry,
       "trm26xxRackNumber": trm26xxRackNumber,
       "trm26xxSlotNumber": trm26xxSlotNumber,
       "trm26xxStatus": trm26xxStatus,
       "trm26xxTemperature": trm26xxTemperature,
       "trm26xxTxMode": trm26xxTxMode,
       "trm26xxSwReset": trm26xxSwReset,
       "trm26xxOpticalPowerPIN1": trm26xxOpticalPowerPIN1,
       "trm26xxOpticalPowerPIN2": trm26xxOpticalPowerPIN2,
       "trm26xxLogOpticalPower": trm26xxLogOpticalPower,
       "trm26xxTemperatureTEC1": trm26xxTemperatureTEC1,
       "trm26xxTemperatureTEC2": trm26xxTemperatureTEC2,
       "trm26xxVoltageTEC1": trm26xxVoltageTEC1,
       "trm26xxVoltageTEC2": trm26xxVoltageTEC2,
       "trm26xxCurrentTEC1": trm26xxCurrentTEC1,
       "trm26xxCurrentTEC2": trm26xxCurrentTEC2,
       "trm26xxCurrentBIAS1": trm26xxCurrentBIAS1,
       "trm26xxCurrentBIAS2": trm26xxCurrentBIAS2,
       "trm26xxVoltageBIAS1": trm26xxVoltageBIAS1,
       "trm26xxVoltageBIAS2": trm26xxVoltageBIAS2,
       "trm26xxFM": trm26xxFM,
       "trm26xxTraps": trm26xxTraps,
       "trm26xxTrapTEC1Faulty": trm26xxTrapTEC1Faulty,
       "trm26xxTrapTEC2Faulty": trm26xxTrapTEC2Faulty,
       "trm26xxTrapBIAS1Faulty": trm26xxTrapBIAS1Faulty,
       "trm26xxTrapBIAS2Faulty": trm26xxTrapBIAS2Faulty,
       "trm26xxTrapPIUTempShutdown": trm26xxTrapPIUTempShutdown,
       "trm26xxTrapOpticalLinkdown": trm26xxTrapOpticalLinkdown,
       "trm26xxTrapTxDisable": trm26xxTrapTxDisable,
       "trm25xx": trm25xx,
       "trm25xxPM": trm25xxPM,
       "trm25xxTable": trm25xxTable,
       "trm25xxEntry": trm25xxEntry,
       "trm25xxRackNumber": trm25xxRackNumber,
       "trm25xxSlotNumber": trm25xxSlotNumber,
       "trm25xxWorkingLineStatus": trm25xxWorkingLineStatus,
       "trm25xxProtectingLineStatus": trm25xxProtectingLineStatus,
       "trm25xxTemperature": trm25xxTemperature,
       "trm25xxSwReset": trm25xxSwReset,
       "trm25xxRxLine": trm25xxRxLine,
       "trm25xxOpticalInPowLine": trm25xxOpticalInPowLine,
       "trm25xxSpeedLimit": trm25xxSpeedLimit,
       "trm25xxEstProtLine": trm25xxEstProtLine,
       "trm25xxEstFibRateLine": trm25xxEstFibRateLine,
       "trm25xxTxLine": trm25xxTxLine,
       "trm25xxOpticalOutPowLine": trm25xxOpticalOutPowLine,
       "trm25xxProdOutPowLine": trm25xxProdOutPowLine,
       "trm25xxLaserBiasCurLine": trm25xxLaserBiasCurLine,
       "trm25xxProdLaserBiasCurLine": trm25xxProdLaserBiasCurLine,
       "trm25xxCDR": trm25xxCDR,
       "trm25xxCustomFibRate": trm25xxCustomFibRate,
       "trm25xxTxMode": trm25xxTxMode,
       "trm25xxFM": trm25xxFM,
       "trm25xxTraps": trm25xxTraps,
       "trm25xxTrapWorkingLineFailure": trm25xxTrapWorkingLineFailure,
       "trm25xxTrapProtectingLineFailure": trm25xxTrapProtectingLineFailure,
       "trm25xxTrapWorkingAndProtectingLineFailure": trm25xxTrapWorkingAndProtectingLineFailure,
       "trm53005500": trm53005500,
       "trm53005500PM": trm53005500PM,
       "trm53005500Table": trm53005500Table,
       "trm53005500Entry": trm53005500Entry,
       "trm53005500RackNumber": trm53005500RackNumber,
       "trm53005500SlotNumber": trm53005500SlotNumber,
       "trm53005500Temperature": trm53005500Temperature,
       "trm53005500SwReset": trm53005500SwReset,
       "trm53005500WavelengthLine": trm53005500WavelengthLine,
       "trm53005500RxLine": trm53005500RxLine,
       "trm53005500OpticalInPowLine": trm53005500OpticalInPowLine,
       "trm53005500TxLine": trm53005500TxLine,
       "trm53005500TxModeLine": trm53005500TxModeLine,
       "trm53005500WavelengthClient1": trm53005500WavelengthClient1,
       "trm53005500RxClient1": trm53005500RxClient1,
       "trm53005500CDRClient1": trm53005500CDRClient1,
       "trm53005500TxClient1": trm53005500TxClient1,
       "trm53005500TxModeClient1": trm53005500TxModeClient1,
       "trm53005500IDStringClient1": trm53005500IDStringClient1,
       "trm53005500IPAddressClient1": trm53005500IPAddressClient1,
       "trm53005500WavelengthClient2": trm53005500WavelengthClient2,
       "trm53005500RxClient2": trm53005500RxClient2,
       "trm53005500CDRClient2": trm53005500CDRClient2,
       "trm53005500TxClient2": trm53005500TxClient2,
       "trm53005500TxModeClient2": trm53005500TxModeClient2,
       "trm53005500IDStringClient2": trm53005500IDStringClient2,
       "trm53005500IPAddressClient2": trm53005500IPAddressClient2,
       "trm53005500WavelengthClient3": trm53005500WavelengthClient3,
       "trm53005500RxClient3": trm53005500RxClient3,
       "trm53005500CDRClient3": trm53005500CDRClient3,
       "trm53005500TxClient3": trm53005500TxClient3,
       "trm53005500TxModeClient3": trm53005500TxModeClient3,
       "trm53005500IDStringClient3": trm53005500IDStringClient3,
       "trm53005500IPAddressClient3": trm53005500IPAddressClient3,
       "trm53005500WavelengthClient4": trm53005500WavelengthClient4,
       "trm53005500RxClient4": trm53005500RxClient4,
       "trm53005500CDRClient4": trm53005500CDRClient4,
       "trm53005500TxClient4": trm53005500TxClient4,
       "trm53005500TxModeClient4": trm53005500TxModeClient4,
       "trm53005500IDStringClient4": trm53005500IDStringClient4,
       "trm53005500IPAddressClient4": trm53005500IPAddressClient4,
       "trm53005500FM": trm53005500FM,
       "trm53005500Traps": trm53005500Traps,
       "trm53005500TrapRxLinkdownLine": trm53005500TrapRxLinkdownLine,
       "trm53005500TrapExternalsyncFailureLine": trm53005500TrapExternalsyncFailureLine,
       "trm53005500TrapSfpMissingLine": trm53005500TrapSfpMissingLine,
       "trm53005500TrapSfpBadTypeLine": trm53005500TrapSfpBadTypeLine,
       "trm53005500TrapSfpFaultyLine": trm53005500TrapSfpFaultyLine,
       "trm53005500TrapRxGlitchLine": trm53005500TrapRxGlitchLine,
       "trm53005500TrapTxGlitchLine": trm53005500TrapTxGlitchLine,
       "trm53005500TrapTxDisabledLine": trm53005500TrapTxDisabledLine,
       "trm53005500TrapRxLinkDownClient1": trm53005500TrapRxLinkDownClient1,
       "trm53005500TrapTxOutOfSyncClient1": trm53005500TrapTxOutOfSyncClient1,
       "trm53005500TrapSfpMissingClient1": trm53005500TrapSfpMissingClient1,
       "trm53005500TrapSfpBadTypeClient1": trm53005500TrapSfpBadTypeClient1,
       "trm53005500TrapSfpFaultyClient1": trm53005500TrapSfpFaultyClient1,
       "trm53005500TrapTxGlitchClient1": trm53005500TrapTxGlitchClient1,
       "trm53005500TrapRxGlitchClient1": trm53005500TrapRxGlitchClient1,
       "trm53005500TrapTxDisabledClient1": trm53005500TrapTxDisabledClient1,
       "trm53005500TrapRxLinkDownClient2": trm53005500TrapRxLinkDownClient2,
       "trm53005500TrapTxOutOfSyncClient2": trm53005500TrapTxOutOfSyncClient2,
       "trm53005500TrapSfpMissingClient2": trm53005500TrapSfpMissingClient2,
       "trm53005500TrapSfpBadTypeClient2": trm53005500TrapSfpBadTypeClient2,
       "trm53005500TrapSfpFaultyClient2": trm53005500TrapSfpFaultyClient2,
       "trm53005500TrapTxGlitchClient2": trm53005500TrapTxGlitchClient2,
       "trm53005500TrapRxGlitchClient2": trm53005500TrapRxGlitchClient2,
       "trm53005500TrapTxDisabledClient2": trm53005500TrapTxDisabledClient2,
       "trm53005500TrapRxLinkDownClient3": trm53005500TrapRxLinkDownClient3,
       "trm53005500TrapTxOutOfSyncClient3": trm53005500TrapTxOutOfSyncClient3,
       "trm53005500TrapSfpMissingClient3": trm53005500TrapSfpMissingClient3,
       "trm53005500TrapSfpBadTypeClient3": trm53005500TrapSfpBadTypeClient3,
       "trm53005500TrapSfpFaultyClient3": trm53005500TrapSfpFaultyClient3,
       "trm53005500TrapTxGlitchClient3": trm53005500TrapTxGlitchClient3,
       "trm53005500TrapRxGlitchClient3": trm53005500TrapRxGlitchClient3,
       "trm53005500TrapTxDisabledClient3": trm53005500TrapTxDisabledClient3,
       "trm53005500TrapRxLinkDownClient4": trm53005500TrapRxLinkDownClient4,
       "trm53005500TrapTxOutOfSyncClient4": trm53005500TrapTxOutOfSyncClient4,
       "trm53005500TrapSfpMissingClient4": trm53005500TrapSfpMissingClient4,
       "trm53005500TrapSfpBadTypeClient4": trm53005500TrapSfpBadTypeClient4,
       "trm53005500TrapSfpFaultyClient4": trm53005500TrapSfpFaultyClient4,
       "trm53005500TrapTxGlitchClient4": trm53005500TrapTxGlitchClient4,
       "trm53005500TrapRxGlitchClient4": trm53005500TrapRxGlitchClient4,
       "trm53005500TrapTxDisabledClient4": trm53005500TrapTxDisabledClient4,
       "trm53005500TrapHwFailure": trm53005500TrapHwFailure,
       "trmSubrackFM": trmSubrackFM,
       "trmSubrackTraps": trmSubrackTraps,
       "trmTrapBmiLost": trmTrapBmiLost,
       "trmTrapBmiError": trmTrapBmiError,
       "trmTrapHighTemp": trmTrapHighTemp,
       "trmTrapLowTemp": trmTrapLowTemp,
       "trmTrapVeryHighTemp": trmTrapVeryHighTemp,
       "trmTrapSpeedLimitExceeded": trmTrapSpeedLimitExceeded}
)
