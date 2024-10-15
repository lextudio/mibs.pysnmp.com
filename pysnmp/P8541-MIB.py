# SNMP MIB module (P8541-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/P8541-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:59 2024
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
_P8541_ObjectIdentity = ObjectIdentity
p8541 = _P8541_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5)
)
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 1)
)


class _SensorName_Type(DisplayString):
    """Custom type sensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SensorName_Type.__name__ = "DisplayString"
_SensorName_Object = MibScalar
sensorName = _SensorName_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 1, 1),
    _SensorName_Type()
)
sensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorName.setStatus("mandatory")
_Channels_ObjectIdentity = ObjectIdentity
channels = _Channels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2)
)
_Channel1_ObjectIdentity = ObjectIdentity
channel1 = _Channel1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1)
)


class _Ch1Name_Type(DisplayString):
    """Custom type ch1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ch1Name_Type.__name__ = "DisplayString"
_Ch1Name_Object = MibScalar
ch1Name = _Ch1Name_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 1),
    _Ch1Name_Type()
)
ch1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1Name.setStatus("mandatory")


class _Ch1Val_Type(DisplayString):
    """Custom type ch1Val based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch1Val_Type.__name__ = "DisplayString"
_Ch1Val_Object = MibScalar
ch1Val = _Ch1Val_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 2),
    _Ch1Val_Type()
)
ch1Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1Val.setStatus("mandatory")


class _Ch1IntVal_Type(Integer32):
    """Custom type ch1IntVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-550, 1250),
    )


_Ch1IntVal_Type.__name__ = "Integer32"
_Ch1IntVal_Object = MibScalar
ch1IntVal = _Ch1IntVal_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 3),
    _Ch1IntVal_Type()
)
ch1IntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1IntVal.setStatus("mandatory")


class _Ch1Alarm_Type(Integer32):
    """Custom type ch1Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ch1Alarm_Type.__name__ = "Integer32"
_Ch1Alarm_Object = MibScalar
ch1Alarm = _Ch1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 4),
    _Ch1Alarm_Type()
)
ch1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1Alarm.setStatus("mandatory")


class _Ch1LimHi_Type(DisplayString):
    """Custom type ch1LimHi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch1LimHi_Type.__name__ = "DisplayString"
_Ch1LimHi_Object = MibScalar
ch1LimHi = _Ch1LimHi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 5),
    _Ch1LimHi_Type()
)
ch1LimHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1LimHi.setStatus("mandatory")


class _Ch1LimLo_Type(DisplayString):
    """Custom type ch1LimLo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch1LimLo_Type.__name__ = "DisplayString"
_Ch1LimLo_Object = MibScalar
ch1LimLo = _Ch1LimLo_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 6),
    _Ch1LimLo_Type()
)
ch1LimLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1LimLo.setStatus("mandatory")


class _Ch1LimHyst_Type(DisplayString):
    """Custom type ch1LimHyst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch1LimHyst_Type.__name__ = "DisplayString"
_Ch1LimHyst_Object = MibScalar
ch1LimHyst = _Ch1LimHyst_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 7),
    _Ch1LimHyst_Type()
)
ch1LimHyst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1LimHyst.setStatus("mandatory")


class _Ch1Delay_Type(Integer32):
    """Custom type ch1Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Ch1Delay_Type.__name__ = "Integer32"
_Ch1Delay_Object = MibScalar
ch1Delay = _Ch1Delay_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 1, 8),
    _Ch1Delay_Type()
)
ch1Delay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1Delay.setStatus("mandatory")
_Channel2_ObjectIdentity = ObjectIdentity
channel2 = _Channel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2)
)


class _Ch2Name_Type(DisplayString):
    """Custom type ch2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ch2Name_Type.__name__ = "DisplayString"
_Ch2Name_Object = MibScalar
ch2Name = _Ch2Name_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 1),
    _Ch2Name_Type()
)
ch2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch2Name.setStatus("mandatory")


class _Ch2Val_Type(DisplayString):
    """Custom type ch2Val based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch2Val_Type.__name__ = "DisplayString"
_Ch2Val_Object = MibScalar
ch2Val = _Ch2Val_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 2),
    _Ch2Val_Type()
)
ch2Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch2Val.setStatus("mandatory")


class _Ch2IntVal_Type(Integer32):
    """Custom type ch2IntVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-550, 1250),
    )


_Ch2IntVal_Type.__name__ = "Integer32"
_Ch2IntVal_Object = MibScalar
ch2IntVal = _Ch2IntVal_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 3),
    _Ch2IntVal_Type()
)
ch2IntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch2IntVal.setStatus("mandatory")


class _Ch2Alarm_Type(Integer32):
    """Custom type ch2Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ch2Alarm_Type.__name__ = "Integer32"
_Ch2Alarm_Object = MibScalar
ch2Alarm = _Ch2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 4),
    _Ch2Alarm_Type()
)
ch2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch2Alarm.setStatus("mandatory")


class _Ch2LimHi_Type(DisplayString):
    """Custom type ch2LimHi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch2LimHi_Type.__name__ = "DisplayString"
_Ch2LimHi_Object = MibScalar
ch2LimHi = _Ch2LimHi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 5),
    _Ch2LimHi_Type()
)
ch2LimHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch2LimHi.setStatus("mandatory")


class _Ch2LimLo_Type(DisplayString):
    """Custom type ch2LimLo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch2LimLo_Type.__name__ = "DisplayString"
_Ch2LimLo_Object = MibScalar
ch2LimLo = _Ch2LimLo_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 6),
    _Ch2LimLo_Type()
)
ch2LimLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch2LimLo.setStatus("mandatory")


class _Ch2LimHyst_Type(DisplayString):
    """Custom type ch2LimHyst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch2LimHyst_Type.__name__ = "DisplayString"
_Ch2LimHyst_Object = MibScalar
ch2LimHyst = _Ch2LimHyst_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 7),
    _Ch2LimHyst_Type()
)
ch2LimHyst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch2LimHyst.setStatus("mandatory")


class _Ch2Delay_Type(Integer32):
    """Custom type ch2Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Ch2Delay_Type.__name__ = "Integer32"
_Ch2Delay_Object = MibScalar
ch2Delay = _Ch2Delay_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 2, 8),
    _Ch2Delay_Type()
)
ch2Delay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch2Delay.setStatus("mandatory")
_Channel3_ObjectIdentity = ObjectIdentity
channel3 = _Channel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3)
)


class _Ch3Name_Type(DisplayString):
    """Custom type ch3Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ch3Name_Type.__name__ = "DisplayString"
_Ch3Name_Object = MibScalar
ch3Name = _Ch3Name_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 1),
    _Ch3Name_Type()
)
ch3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch3Name.setStatus("mandatory")


class _Ch3Val_Type(DisplayString):
    """Custom type ch3Val based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch3Val_Type.__name__ = "DisplayString"
_Ch3Val_Object = MibScalar
ch3Val = _Ch3Val_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 2),
    _Ch3Val_Type()
)
ch3Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch3Val.setStatus("mandatory")


class _Ch3IntVal_Type(Integer32):
    """Custom type ch3IntVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-550, 1250),
    )


_Ch3IntVal_Type.__name__ = "Integer32"
_Ch3IntVal_Object = MibScalar
ch3IntVal = _Ch3IntVal_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 3),
    _Ch3IntVal_Type()
)
ch3IntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch3IntVal.setStatus("mandatory")


class _Ch3Alarm_Type(Integer32):
    """Custom type ch3Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ch3Alarm_Type.__name__ = "Integer32"
_Ch3Alarm_Object = MibScalar
ch3Alarm = _Ch3Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 4),
    _Ch3Alarm_Type()
)
ch3Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch3Alarm.setStatus("mandatory")


class _Ch3LimHi_Type(DisplayString):
    """Custom type ch3LimHi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch3LimHi_Type.__name__ = "DisplayString"
_Ch3LimHi_Object = MibScalar
ch3LimHi = _Ch3LimHi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 5),
    _Ch3LimHi_Type()
)
ch3LimHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch3LimHi.setStatus("mandatory")


class _Ch3LimLo_Type(DisplayString):
    """Custom type ch3LimLo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch3LimLo_Type.__name__ = "DisplayString"
_Ch3LimLo_Object = MibScalar
ch3LimLo = _Ch3LimLo_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 6),
    _Ch3LimLo_Type()
)
ch3LimLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch3LimLo.setStatus("mandatory")


class _Ch3LimHyst_Type(DisplayString):
    """Custom type ch3LimHyst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch3LimHyst_Type.__name__ = "DisplayString"
_Ch3LimHyst_Object = MibScalar
ch3LimHyst = _Ch3LimHyst_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 7),
    _Ch3LimHyst_Type()
)
ch3LimHyst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch3LimHyst.setStatus("mandatory")


class _Ch3Delay_Type(Integer32):
    """Custom type ch3Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Ch3Delay_Type.__name__ = "Integer32"
_Ch3Delay_Object = MibScalar
ch3Delay = _Ch3Delay_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 3, 8),
    _Ch3Delay_Type()
)
ch3Delay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch3Delay.setStatus("mandatory")
_Channel4_ObjectIdentity = ObjectIdentity
channel4 = _Channel4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4)
)


class _Ch4Name_Type(DisplayString):
    """Custom type ch4Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ch4Name_Type.__name__ = "DisplayString"
_Ch4Name_Object = MibScalar
ch4Name = _Ch4Name_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 1),
    _Ch4Name_Type()
)
ch4Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch4Name.setStatus("mandatory")


class _Ch4Val_Type(DisplayString):
    """Custom type ch4Val based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch4Val_Type.__name__ = "DisplayString"
_Ch4Val_Object = MibScalar
ch4Val = _Ch4Val_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 2),
    _Ch4Val_Type()
)
ch4Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch4Val.setStatus("mandatory")


class _Ch4IntVal_Type(Integer32):
    """Custom type ch4IntVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-550, 1250),
    )


_Ch4IntVal_Type.__name__ = "Integer32"
_Ch4IntVal_Object = MibScalar
ch4IntVal = _Ch4IntVal_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 3),
    _Ch4IntVal_Type()
)
ch4IntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch4IntVal.setStatus("mandatory")


class _Ch4Alarm_Type(Integer32):
    """Custom type ch4Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ch4Alarm_Type.__name__ = "Integer32"
_Ch4Alarm_Object = MibScalar
ch4Alarm = _Ch4Alarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 4),
    _Ch4Alarm_Type()
)
ch4Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch4Alarm.setStatus("mandatory")


class _Ch4LimHi_Type(DisplayString):
    """Custom type ch4LimHi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch4LimHi_Type.__name__ = "DisplayString"
_Ch4LimHi_Object = MibScalar
ch4LimHi = _Ch4LimHi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 5),
    _Ch4LimHi_Type()
)
ch4LimHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch4LimHi.setStatus("mandatory")


class _Ch4LimLo_Type(DisplayString):
    """Custom type ch4LimLo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch4LimLo_Type.__name__ = "DisplayString"
_Ch4LimLo_Object = MibScalar
ch4LimLo = _Ch4LimLo_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 6),
    _Ch4LimLo_Type()
)
ch4LimLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch4LimLo.setStatus("mandatory")


class _Ch4LimHyst_Type(DisplayString):
    """Custom type ch4LimHyst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Ch4LimHyst_Type.__name__ = "DisplayString"
_Ch4LimHyst_Object = MibScalar
ch4LimHyst = _Ch4LimHyst_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 7),
    _Ch4LimHyst_Type()
)
ch4LimHyst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch4LimHyst.setStatus("mandatory")


class _Ch4Delay_Type(Integer32):
    """Custom type ch4Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Ch4Delay_Type.__name__ = "Integer32"
_Ch4Delay_Object = MibScalar
ch4Delay = _Ch4Delay_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 2, 4, 8),
    _Ch4Delay_Type()
)
ch4Delay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch4Delay.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 3)
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
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 3, 1),
    _MessageString_Type()
)
messageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messageString.setStatus("mandatory")
_Tables_ObjectIdentity = ObjectIdentity
tables = _Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 4)
)
_HistoryTable_Object = MibTable
historyTable = _HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    historyTable.setStatus("mandatory")
_HistoryEntry_Object = MibTableRow
historyEntry = _HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1)
)
historyEntry.setIndexNames(
    (0, "P8541-MIB", "ch1temperature"),
)
if mibBuilder.loadTexts:
    historyEntry.setStatus("optional")


class _Ch1temperature_Type(Integer32):
    """Custom type ch1temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ch1temperature_Type.__name__ = "Integer32"
_Ch1temperature_Object = MibTableColumn
ch1temperature = _Ch1temperature_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1, 1),
    _Ch1temperature_Type()
)
ch1temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch1temperature.setStatus("mandatory")


class _Ch2temperature_Type(Integer32):
    """Custom type ch2temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ch2temperature_Type.__name__ = "Integer32"
_Ch2temperature_Object = MibTableColumn
ch2temperature = _Ch2temperature_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1, 2),
    _Ch2temperature_Type()
)
ch2temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch2temperature.setStatus("mandatory")


class _Ch3temperature_Type(Integer32):
    """Custom type ch3temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ch3temperature_Type.__name__ = "Integer32"
_Ch3temperature_Object = MibTableColumn
ch3temperature = _Ch3temperature_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1, 3),
    _Ch3temperature_Type()
)
ch3temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch3temperature.setStatus("mandatory")


class _Ch4temperature_Type(Integer32):
    """Custom type ch4temperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ch4temperature_Type.__name__ = "Integer32"
_Ch4temperature_Object = MibTableColumn
ch4temperature = _Ch4temperature_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 5, 4, 1, 1, 4),
    _Ch4temperature_Type()
)
ch4temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ch4temperature.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "P8541-MIB",
    **{"DisplayString": DisplayString,
       "comet": comet,
       "products": products,
       "p8541": p8541,
       "settings": settings,
       "sensorName": sensorName,
       "channels": channels,
       "channel1": channel1,
       "ch1Name": ch1Name,
       "ch1Val": ch1Val,
       "ch1IntVal": ch1IntVal,
       "ch1Alarm": ch1Alarm,
       "ch1LimHi": ch1LimHi,
       "ch1LimLo": ch1LimLo,
       "ch1LimHyst": ch1LimHyst,
       "ch1Delay": ch1Delay,
       "channel2": channel2,
       "ch2Name": ch2Name,
       "ch2Val": ch2Val,
       "ch2IntVal": ch2IntVal,
       "ch2Alarm": ch2Alarm,
       "ch2LimHi": ch2LimHi,
       "ch2LimLo": ch2LimLo,
       "ch2LimHyst": ch2LimHyst,
       "ch2Delay": ch2Delay,
       "channel3": channel3,
       "ch3Name": ch3Name,
       "ch3Val": ch3Val,
       "ch3IntVal": ch3IntVal,
       "ch3Alarm": ch3Alarm,
       "ch3LimHi": ch3LimHi,
       "ch3LimLo": ch3LimLo,
       "ch3LimHyst": ch3LimHyst,
       "ch3Delay": ch3Delay,
       "channel4": channel4,
       "ch4Name": ch4Name,
       "ch4Val": ch4Val,
       "ch4IntVal": ch4IntVal,
       "ch4Alarm": ch4Alarm,
       "ch4LimHi": ch4LimHi,
       "ch4LimLo": ch4LimLo,
       "ch4LimHyst": ch4LimHyst,
       "ch4Delay": ch4Delay,
       "traps": traps,
       "messageString": messageString,
       "tables": tables,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "ch1temperature": ch1temperature,
       "ch2temperature": ch2temperature,
       "ch3temperature": ch3temperature,
       "ch4temperature": ch4temperature}
)
