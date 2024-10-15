# SNMP MIB module (LANADPTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANADPTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:55 2024
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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Comet_ObjectIdentity = ObjectIdentity
comet = _Comet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1)
)
_Lanadapter_ObjectIdentity = ObjectIdentity
lanadapter = _Lanadapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 1)
)


class _MessageString_Type(DisplayString):
    """Custom type messageString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MessageString_Type.__name__ = "DisplayString"
_MessageString_Object = MibScalar
messageString = _MessageString_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 1),
    _MessageString_Type()
)
messageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messageString.setStatus("mandatory")


class _ChannelAlarm_Type(Integer32):
    """Custom type channelAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ChannelAlarm_Type.__name__ = "Integer32"
_ChannelAlarm_Object = MibScalar
channelAlarm = _ChannelAlarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 2),
    _ChannelAlarm_Type()
)
channelAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelAlarm.setStatus("mandatory")


class _Memmory90Full_Type(Integer32):
    """Custom type memmory90Full based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Memmory90Full_Type.__name__ = "Integer32"
_Memmory90Full_Object = MibScalar
memmory90Full = _Memmory90Full_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 3),
    _Memmory90Full_Type()
)
memmory90Full.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memmory90Full.setStatus("mandatory")


class _Memmory100Full_Type(Integer32):
    """Custom type memmory100Full based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Memmory100Full_Type.__name__ = "Integer32"
_Memmory100Full_Object = MibScalar
memmory100Full = _Memmory100Full_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 4),
    _Memmory100Full_Type()
)
memmory100Full.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memmory100Full.setStatus("mandatory")


class _VccLow_Type(Integer32):
    """Custom type vccLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VccLow_Type.__name__ = "Integer32"
_VccLow_Object = MibScalar
vccLow = _VccLow_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 5),
    _VccLow_Type()
)
vccLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vccLow.setStatus("mandatory")


class _BatteryEnd_Type(Integer32):
    """Custom type batteryEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BatteryEnd_Type.__name__ = "Integer32"
_BatteryEnd_Object = MibScalar
batteryEnd = _BatteryEnd_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 6),
    _BatteryEnd_Type()
)
batteryEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnd.setStatus("mandatory")


class _BatteryLow_Type(Integer32):
    """Custom type batteryLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BatteryLow_Type.__name__ = "Integer32"
_BatteryLow_Object = MibScalar
batteryLow = _BatteryLow_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 7),
    _BatteryLow_Type()
)
batteryLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryLow.setStatus("mandatory")


class _CommunicationError_Type(Integer32):
    """Custom type communicationError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CommunicationError_Type.__name__ = "Integer32"
_CommunicationError_Object = MibScalar
communicationError = _CommunicationError_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 8),
    _CommunicationError_Type()
)
communicationError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communicationError.setStatus("mandatory")


class _LoggerOff_Type(Integer32):
    """Custom type loggerOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LoggerOff_Type.__name__ = "Integer32"
_LoggerOff_Object = MibScalar
loggerOff = _LoggerOff_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 1, 9),
    _LoggerOff_Type()
)
loggerOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loggerOff.setStatus("mandatory")
_Channels_ObjectIdentity = ObjectIdentity
channels = _Channels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2)
)
_Channel1_ObjectIdentity = ObjectIdentity
channel1 = _Channel1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 1)
)


class _Ch1Alarm_Type(Integer32):
    """Custom type ch1Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ch1Alarm_Type.__name__ = "Integer32"
_Ch1Alarm_Object = MibScalar
ch1Alarm = _Ch1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 1, 1),
    _Ch1Alarm_Type()
)
ch1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1Alarm.setStatus("mandatory")
_Channel2_ObjectIdentity = ObjectIdentity
channel2 = _Channel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 2)
)


class _Ch2Alarm_Type(Integer32):
    """Custom type ch2Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ch2Alarm_Type.__name__ = "Integer32"
_Ch2Alarm_Object = MibScalar
ch2Alarm = _Ch2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 2, 1),
    _Ch2Alarm_Type()
)
ch2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch2Alarm.setStatus("mandatory")
_Channel3_ObjectIdentity = ObjectIdentity
channel3 = _Channel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 3)
)


class _Ch3Alarm_Type(Integer32):
    """Custom type ch3Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ch3Alarm_Type.__name__ = "Integer32"
_Ch3Alarm_Object = MibScalar
ch3Alarm = _Ch3Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 3, 1),
    _Ch3Alarm_Type()
)
ch3Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch3Alarm.setStatus("mandatory")
_Channel4_ObjectIdentity = ObjectIdentity
channel4 = _Channel4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 4)
)


class _Ch4Alarm_Type(Integer32):
    """Custom type ch4Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ch4Alarm_Type.__name__ = "Integer32"
_Ch4Alarm_Object = MibScalar
ch4Alarm = _Ch4Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 4, 1),
    _Ch4Alarm_Type()
)
ch4Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch4Alarm.setStatus("mandatory")
_Channel5_ObjectIdentity = ObjectIdentity
channel5 = _Channel5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 5)
)


class _Ch5Alarm_Type(Integer32):
    """Custom type ch5Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ch5Alarm_Type.__name__ = "Integer32"
_Ch5Alarm_Object = MibScalar
ch5Alarm = _Ch5Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 5, 1),
    _Ch5Alarm_Type()
)
ch5Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch5Alarm.setStatus("mandatory")
_Channel6_ObjectIdentity = ObjectIdentity
channel6 = _Channel6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 6)
)


class _Ch6Alarm_Type(Integer32):
    """Custom type ch6Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ch6Alarm_Type.__name__ = "Integer32"
_Ch6Alarm_Object = MibScalar
ch6Alarm = _Ch6Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 3, 2, 6, 1),
    _Ch6Alarm_Type()
)
ch6Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch6Alarm.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANADPTER-MIB",
    **{"DisplayString": DisplayString,
       "comet": comet,
       "products": products,
       "lanadapter": lanadapter,
       "traps": traps,
       "messageString": messageString,
       "channelAlarm": channelAlarm,
       "memmory90Full": memmory90Full,
       "memmory100Full": memmory100Full,
       "vccLow": vccLow,
       "batteryEnd": batteryEnd,
       "batteryLow": batteryLow,
       "communicationError": communicationError,
       "loggerOff": loggerOff,
       "channels": channels,
       "channel1": channel1,
       "ch1Alarm": ch1Alarm,
       "channel2": channel2,
       "ch2Alarm": ch2Alarm,
       "channel3": channel3,
       "ch3Alarm": ch3Alarm,
       "channel4": channel4,
       "ch4Alarm": ch4Alarm,
       "channel5": channel5,
       "ch5Alarm": ch5Alarm,
       "channel6": channel6,
       "ch6Alarm": ch6Alarm}
)
