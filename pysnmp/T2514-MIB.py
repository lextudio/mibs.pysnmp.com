# SNMP MIB module (T2514-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T2514-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:46 2024
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
_T2514_ObjectIdentity = ObjectIdentity
t2514 = _T2514_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2)
)
_Readings_ObjectIdentity = ObjectIdentity
readings = _Readings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1)
)


class _Pressure_Type(DisplayString):
    """Custom type pressure based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Pressure_Type.__name__ = "DisplayString"
_Pressure_Object = MibScalar
pressure = _Pressure_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 4),
    _Pressure_Type()
)
pressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressure.setStatus("mandatory")
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2)
)


class _Presslow_Type(DisplayString):
    """Custom type presslow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Presslow_Type.__name__ = "DisplayString"
_Presslow_Object = MibScalar
presslow = _Presslow_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 13),
    _Presslow_Type()
)
presslow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    presslow.setStatus("mandatory")


class _Presshigh_Type(DisplayString):
    """Custom type presshigh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Presshigh_Type.__name__ = "DisplayString"
_Presshigh_Object = MibScalar
presshigh = _Presshigh_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 14),
    _Presshigh_Type()
)
presshigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    presshigh.setStatus("mandatory")


class _Presstime_Type(Integer32):
    """Custom type presstime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Presstime_Type.__name__ = "Integer32"
_Presstime_Object = MibScalar
presstime = _Presstime_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 15),
    _Presstime_Type()
)
presstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    presstime.setStatus("mandatory")


class _PressureHyst_Type(DisplayString):
    """Custom type pressureHyst based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PressureHyst_Type.__name__ = "DisplayString"
_PressureHyst_Object = MibScalar
pressureHyst = _PressureHyst_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 16),
    _PressureHyst_Type()
)
pressureHyst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressureHyst.setStatus("mandatory")
_Readingsint_ObjectIdentity = ObjectIdentity
readingsint = _Readingsint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3)
)


class _Pressurei_Type(Integer32):
    """Custom type pressurei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 6000),
    )


_Pressurei_Type.__name__ = "Integer32"
_Pressurei_Object = MibScalar
pressurei = _Pressurei_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 4),
    _Pressurei_Type()
)
pressurei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressurei.setStatus("mandatory")
_Settingsint_ObjectIdentity = ObjectIdentity
settingsint = _Settingsint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4)
)


class _Presslowi_Type(Integer32):
    """Custom type presslowi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Presslowi_Type.__name__ = "Integer32"
_Presslowi_Object = MibScalar
presslowi = _Presslowi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 13),
    _Presslowi_Type()
)
presslowi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    presslowi.setStatus("mandatory")


class _Presshighi_Type(Integer32):
    """Custom type presshighi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11000),
    )


_Presshighi_Type.__name__ = "Integer32"
_Presshighi_Object = MibScalar
presshighi = _Presshighi_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 14),
    _Presshighi_Type()
)
presshighi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    presshighi.setStatus("mandatory")


class _Presstimei_Type(Integer32):
    """Custom type presstimei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Presstimei_Type.__name__ = "Integer32"
_Presstimei_Object = MibScalar
presstimei = _Presstimei_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 15),
    _Presstimei_Type()
)
presstimei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    presstimei.setStatus("mandatory")


class _PressHysti_Type(Integer32):
    """Custom type pressHysti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 6000),
    )


_PressHysti_Type.__name__ = "Integer32"
_PressHysti_Object = MibScalar
pressHysti = _PressHysti_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 16),
    _PressHysti_Type()
)
pressHysti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pressHysti.setStatus("mandatory")
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


class _AlarmPressure_Type(Integer32):
    """Custom type alarmPressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AlarmPressure_Type.__name__ = "Integer32"
_AlarmPressure_Object = MibScalar
alarmPressure = _AlarmPressure_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 5),
    _AlarmPressure_Type()
)
alarmPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPressure.setStatus("mandatory")
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
    (0, "T2514-MIB", "histpressure"),
)
if mibBuilder.loadTexts:
    historyEntry.setStatus("optional")


class _Histpressure_Type(Integer32):
    """Custom type histpressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Histpressure_Type.__name__ = "Integer32"
_Histpressure_Object = MibTableColumn
histpressure = _Histpressure_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 4),
    _Histpressure_Type()
)
histpressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histpressure.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T2514-MIB",
    **{"DisplayString": DisplayString,
       "comet": comet,
       "products": products,
       "t2514": t2514,
       "readings": readings,
       "pressure": pressure,
       "settings": settings,
       "presslow": presslow,
       "presshigh": presshigh,
       "presstime": presstime,
       "pressureHyst": pressureHyst,
       "readingsint": readingsint,
       "pressurei": pressurei,
       "settingsint": settingsint,
       "presslowi": presslowi,
       "presshighi": presshighi,
       "presstimei": presstimei,
       "pressHysti": pressHysti,
       "traps": traps,
       "messageString": messageString,
       "alarmPressure": alarmPressure,
       "tables": tables,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "histpressure": histpressure}
)
