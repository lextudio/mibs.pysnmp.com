# SNMP MIB module (T3511-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T3511-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:48 2024
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
_T3511_ObjectIdentity = ObjectIdentity
t3511 = _T3511_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2)
)
_Readings_ObjectIdentity = ObjectIdentity
readings = _Readings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1)
)


class _Temperature_Type(DisplayString):
    """Custom type temperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Temperature_Type.__name__ = "DisplayString"
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 1),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("mandatory")


class _Humidity_Type(DisplayString):
    """Custom type humidity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Humidity_Type.__name__ = "DisplayString"
_Humidity_Object = MibScalar
humidity = _Humidity_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 2),
    _Humidity_Type()
)
humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity.setStatus("mandatory")


class _ComputedValue_Type(DisplayString):
    """Custom type computedValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ComputedValue_Type.__name__ = "DisplayString"
_ComputedValue_Object = MibScalar
computedValue = _ComputedValue_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 3),
    _ComputedValue_Type()
)
computedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    computedValue.setStatus("mandatory")
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2)
)


class _Templow_Type(DisplayString):
    """Custom type templow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Templow_Type.__name__ = "DisplayString"
_Templow_Object = MibScalar
templow = _Templow_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 1),
    _Templow_Type()
)
templow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    templow.setStatus("mandatory")


class _Temphigh_Type(DisplayString):
    """Custom type temphigh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Temphigh_Type.__name__ = "DisplayString"
_Temphigh_Object = MibScalar
temphigh = _Temphigh_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 2),
    _Temphigh_Type()
)
temphigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temphigh.setStatus("mandatory")


class _Humiditylow_Type(DisplayString):
    """Custom type humiditylow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Humiditylow_Type.__name__ = "DisplayString"
_Humiditylow_Object = MibScalar
humiditylow = _Humiditylow_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 3),
    _Humiditylow_Type()
)
humiditylow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiditylow.setStatus("mandatory")


class _Humidityhigh_Type(DisplayString):
    """Custom type humidityhigh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Humidityhigh_Type.__name__ = "DisplayString"
_Humidityhigh_Object = MibScalar
humidityhigh = _Humidityhigh_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 4),
    _Humidityhigh_Type()
)
humidityhigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityhigh.setStatus("mandatory")


class _Cvlow_Type(DisplayString):
    """Custom type cvlow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cvlow_Type.__name__ = "DisplayString"
_Cvlow_Object = MibScalar
cvlow = _Cvlow_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 5),
    _Cvlow_Type()
)
cvlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvlow.setStatus("mandatory")


class _Cvhigh_Type(DisplayString):
    """Custom type cvhigh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cvhigh_Type.__name__ = "DisplayString"
_Cvhigh_Object = MibScalar
cvhigh = _Cvhigh_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 6),
    _Cvhigh_Type()
)
cvhigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvhigh.setStatus("mandatory")


class _Temptime_Type(Integer32):
    """Custom type temptime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Temptime_Type.__name__ = "Integer32"
_Temptime_Object = MibScalar
temptime = _Temptime_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 7),
    _Temptime_Type()
)
temptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temptime.setStatus("mandatory")


class _HumidityTime_Type(Integer32):
    """Custom type humidityTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HumidityTime_Type.__name__ = "Integer32"
_HumidityTime_Object = MibScalar
humidityTime = _HumidityTime_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 8),
    _HumidityTime_Type()
)
humidityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityTime.setStatus("mandatory")


class _CvTime_Type(Integer32):
    """Custom type cvTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvTime_Type.__name__ = "Integer32"
_CvTime_Object = MibScalar
cvTime = _CvTime_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 9),
    _CvTime_Type()
)
cvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTime.setStatus("mandatory")


class _TempHyst_Type(DisplayString):
    """Custom type tempHyst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TempHyst_Type.__name__ = "DisplayString"
_TempHyst_Object = MibScalar
tempHyst = _TempHyst_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 10),
    _TempHyst_Type()
)
tempHyst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHyst.setStatus("mandatory")


class _HumidityHyst_Type(DisplayString):
    """Custom type humidityHyst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HumidityHyst_Type.__name__ = "DisplayString"
_HumidityHyst_Object = MibScalar
humidityHyst = _HumidityHyst_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 11),
    _HumidityHyst_Type()
)
humidityHyst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityHyst.setStatus("mandatory")


class _CvHyst_Type(DisplayString):
    """Custom type cvHyst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CvHyst_Type.__name__ = "DisplayString"
_CvHyst_Object = MibScalar
cvHyst = _CvHyst_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 12),
    _CvHyst_Type()
)
cvHyst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvHyst.setStatus("mandatory")
_Readingsint_ObjectIdentity = ObjectIdentity
readingsint = _Readingsint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3)
)


class _Temperaturei_Type(Integer32):
    """Custom type temperaturei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 6000),
    )


_Temperaturei_Type.__name__ = "Integer32"
_Temperaturei_Object = MibScalar
temperaturei = _Temperaturei_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 1),
    _Temperaturei_Type()
)
temperaturei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperaturei.setStatus("mandatory")


class _Humidityi_Type(Integer32):
    """Custom type humidityi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidityi_Type.__name__ = "Integer32"
_Humidityi_Object = MibScalar
humidityi = _Humidityi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 2),
    _Humidityi_Type()
)
humidityi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityi.setStatus("mandatory")


class _Cvi_Type(Integer32):
    """Custom type cvi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 6000),
    )


_Cvi_Type.__name__ = "Integer32"
_Cvi_Object = MibScalar
cvi = _Cvi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 3),
    _Cvi_Type()
)
cvi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvi.setStatus("mandatory")
_Settingsint_ObjectIdentity = ObjectIdentity
settingsint = _Settingsint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4)
)


class _Templowi_Type(Integer32):
    """Custom type templowi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Templowi_Type.__name__ = "Integer32"
_Templowi_Object = MibScalar
templowi = _Templowi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 1),
    _Templowi_Type()
)
templowi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    templowi.setStatus("mandatory")


class _Temphighi_Type(Integer32):
    """Custom type temphighi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 6000),
    )


_Temphighi_Type.__name__ = "Integer32"
_Temphighi_Object = MibScalar
temphighi = _Temphighi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 2),
    _Temphighi_Type()
)
temphighi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temphighi.setStatus("mandatory")


class _Humiditylowi_Type(Integer32):
    """Custom type humiditylowi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 6000),
    )


_Humiditylowi_Type.__name__ = "Integer32"
_Humiditylowi_Object = MibScalar
humiditylowi = _Humiditylowi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 3),
    _Humiditylowi_Type()
)
humiditylowi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humiditylowi.setStatus("mandatory")


class _Humidityhighi_Type(Integer32):
    """Custom type humidityhighi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 6000),
    )


_Humidityhighi_Type.__name__ = "Integer32"
_Humidityhighi_Object = MibScalar
humidityhighi = _Humidityhighi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 4),
    _Humidityhighi_Type()
)
humidityhighi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityhighi.setStatus("mandatory")


class _Cvlowi_Type(Integer32):
    """Custom type cvlowi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 6000),
    )


_Cvlowi_Type.__name__ = "Integer32"
_Cvlowi_Object = MibScalar
cvlowi = _Cvlowi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 5),
    _Cvlowi_Type()
)
cvlowi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvlowi.setStatus("mandatory")


class _Cvhighi_Type(Integer32):
    """Custom type cvhighi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 6000),
    )


_Cvhighi_Type.__name__ = "Integer32"
_Cvhighi_Object = MibScalar
cvhighi = _Cvhighi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 6),
    _Cvhighi_Type()
)
cvhighi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvhighi.setStatus("mandatory")


class _Temptimei_Type(Integer32):
    """Custom type temptimei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Temptimei_Type.__name__ = "Integer32"
_Temptimei_Object = MibScalar
temptimei = _Temptimei_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 7),
    _Temptimei_Type()
)
temptimei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temptimei.setStatus("mandatory")


class _HumidityTimei_Type(Integer32):
    """Custom type humidityTimei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HumidityTimei_Type.__name__ = "Integer32"
_HumidityTimei_Object = MibScalar
humidityTimei = _HumidityTimei_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 8),
    _HumidityTimei_Type()
)
humidityTimei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityTimei.setStatus("mandatory")


class _CvTimei_Type(Integer32):
    """Custom type cvTimei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CvTimei_Type.__name__ = "Integer32"
_CvTimei_Object = MibScalar
cvTimei = _CvTimei_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 9),
    _CvTimei_Type()
)
cvTimei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvTimei.setStatus("mandatory")


class _TempHysti_Type(Integer32):
    """Custom type tempHysti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 6000),
    )


_TempHysti_Type.__name__ = "Integer32"
_TempHysti_Object = MibScalar
tempHysti = _TempHysti_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 10),
    _TempHysti_Type()
)
tempHysti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHysti.setStatus("mandatory")


class _HumidityHysti_Type(Integer32):
    """Custom type humidityHysti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 6000),
    )


_HumidityHysti_Type.__name__ = "Integer32"
_HumidityHysti_Object = MibScalar
humidityHysti = _HumidityHysti_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 11),
    _HumidityHysti_Type()
)
humidityHysti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityHysti.setStatus("mandatory")


class _CvHysti_Type(Integer32):
    """Custom type cvHysti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 6000),
    )


_CvHysti_Type.__name__ = "Integer32"
_CvHysti_Object = MibScalar
cvHysti = _CvHysti_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 12),
    _CvHysti_Type()
)
cvHysti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvHysti.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 5)
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
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 1),
    _MessageString_Type()
)
messageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messageString.setStatus("mandatory")


class _AlarmTemperature_Type(Integer32):
    """Custom type alarmTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AlarmTemperature_Type.__name__ = "Integer32"
_AlarmTemperature_Object = MibScalar
alarmTemperature = _AlarmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 2),
    _AlarmTemperature_Type()
)
alarmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTemperature.setStatus("mandatory")


class _Alarmhumidity_Type(Integer32):
    """Custom type alarmhumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Alarmhumidity_Type.__name__ = "Integer32"
_Alarmhumidity_Object = MibScalar
alarmhumidity = _Alarmhumidity_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 3),
    _Alarmhumidity_Type()
)
alarmhumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmhumidity.setStatus("mandatory")


class _AlarmCv_Type(Integer32):
    """Custom type alarmCv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AlarmCv_Type.__name__ = "Integer32"
_AlarmCv_Object = MibScalar
alarmCv = _AlarmCv_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 4),
    _AlarmCv_Type()
)
alarmCv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCv.setStatus("mandatory")
_Tables_ObjectIdentity = ObjectIdentity
tables = _Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6)
)
_HistoryTable_Object = MibTable
historyTable = _HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    historyTable.setStatus("mandatory")
_HistoryEntry_Object = MibTableRow
historyEntry = _HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1)
)
historyEntry.setIndexNames(
    (0, "T3511-MIB", "histtemperature"),
)
if mibBuilder.loadTexts:
    historyEntry.setStatus("optional")


class _Histtemperature_Type(Integer32):
    """Custom type histtemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Histtemperature_Type.__name__ = "Integer32"
_Histtemperature_Object = MibTableColumn
histtemperature = _Histtemperature_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 1),
    _Histtemperature_Type()
)
histtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histtemperature.setStatus("mandatory")


class _Histhumidity_Type(Integer32):
    """Custom type histhumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Histhumidity_Type.__name__ = "Integer32"
_Histhumidity_Object = MibTableColumn
histhumidity = _Histhumidity_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 2),
    _Histhumidity_Type()
)
histhumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histhumidity.setStatus("mandatory")


class _HistcomputedValue_Type(Integer32):
    """Custom type histcomputedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HistcomputedValue_Type.__name__ = "Integer32"
_HistcomputedValue_Object = MibTableColumn
histcomputedValue = _HistcomputedValue_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 3),
    _HistcomputedValue_Type()
)
histcomputedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histcomputedValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T3511-MIB",
    **{"DisplayString": DisplayString,
       "comet": comet,
       "products": products,
       "t3511": t3511,
       "readings": readings,
       "temperature": temperature,
       "humidity": humidity,
       "computedValue": computedValue,
       "settings": settings,
       "templow": templow,
       "temphigh": temphigh,
       "humiditylow": humiditylow,
       "humidityhigh": humidityhigh,
       "cvlow": cvlow,
       "cvhigh": cvhigh,
       "temptime": temptime,
       "humidityTime": humidityTime,
       "cvTime": cvTime,
       "tempHyst": tempHyst,
       "humidityHyst": humidityHyst,
       "cvHyst": cvHyst,
       "readingsint": readingsint,
       "temperaturei": temperaturei,
       "humidityi": humidityi,
       "cvi": cvi,
       "settingsint": settingsint,
       "templowi": templowi,
       "temphighi": temphighi,
       "humiditylowi": humiditylowi,
       "humidityhighi": humidityhighi,
       "cvlowi": cvlowi,
       "cvhighi": cvhighi,
       "temptimei": temptimei,
       "humidityTimei": humidityTimei,
       "cvTimei": cvTimei,
       "tempHysti": tempHysti,
       "humidityHysti": humidityHysti,
       "cvHysti": cvHysti,
       "traps": traps,
       "messageString": messageString,
       "alarmTemperature": alarmTemperature,
       "alarmhumidity": alarmhumidity,
       "alarmCv": alarmCv,
       "tables": tables,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "histtemperature": histtemperature,
       "histhumidity": histhumidity,
       "histcomputedValue": histcomputedValue}
)
