# SNMP MIB module (T0510-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T0510-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:24 2024
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
_T0510_ObjectIdentity = ObjectIdentity
t0510 = _T0510_ObjectIdentity(
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
    (0, "T0510-MIB", "histtemperature"),
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

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T0510-MIB",
    **{"DisplayString": DisplayString,
       "comet": comet,
       "products": products,
       "t0510": t0510,
       "readings": readings,
       "temperature": temperature,
       "settings": settings,
       "templow": templow,
       "temphigh": temphigh,
       "temptime": temptime,
       "tempHyst": tempHyst,
       "readingsint": readingsint,
       "temperaturei": temperaturei,
       "settingsint": settingsint,
       "templowi": templowi,
       "temphighi": temphighi,
       "humiditylowi": humiditylowi,
       "temptimei": temptimei,
       "tempHysti": tempHysti,
       "humidityHysti": humidityHysti,
       "traps": traps,
       "messageString": messageString,
       "alarmTemperature": alarmTemperature,
       "tables": tables,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "histtemperature": histtemperature}
)
