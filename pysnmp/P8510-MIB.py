# SNMP MIB module (P8510-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/P8510-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:57 2024
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
_P8510_ObjectIdentity = ObjectIdentity
p8510 = _P8510_ObjectIdentity(
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
    (0, "P8510-MIB", "ch1temperature"),
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

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "P8510-MIB",
    **{"DisplayString": DisplayString,
       "comet": comet,
       "products": products,
       "p8510": p8510,
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
       "traps": traps,
       "messageString": messageString,
       "tables": tables,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "ch1temperature": ch1temperature}
)
