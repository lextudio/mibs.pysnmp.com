# SNMP MIB module (HM2-PLATFORM-TIMEZONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-TIMEZONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:27 2024
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

(hm2PlatformMibs,) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "hm2PlatformMibs")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hm2PlatformTimeZone = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 42)
)
hm2PlatformTimeZone.setRevisions(
        ("2011-10-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2AgentSystemTimeGroup_ObjectIdentity = ObjectIdentity
hm2AgentSystemTimeGroup = _Hm2AgentSystemTimeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 1)
)
_Hm2AgentSystemTime_Type = DisplayString
_Hm2AgentSystemTime_Object = MibScalar
hm2AgentSystemTime = _Hm2AgentSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 1, 1),
    _Hm2AgentSystemTime_Type()
)
hm2AgentSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSystemTime.setStatus("current")
_Hm2AgentSystemDate_Type = DisplayString
_Hm2AgentSystemDate_Object = MibScalar
hm2AgentSystemDate = _Hm2AgentSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 1, 2),
    _Hm2AgentSystemDate_Type()
)
hm2AgentSystemDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSystemDate.setStatus("current")
_Hm2AgentSystemTimeZoneAcronym_Type = DisplayString
_Hm2AgentSystemTimeZoneAcronym_Object = MibScalar
hm2AgentSystemTimeZoneAcronym = _Hm2AgentSystemTimeZoneAcronym_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 1, 3),
    _Hm2AgentSystemTimeZoneAcronym_Type()
)
hm2AgentSystemTimeZoneAcronym.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSystemTimeZoneAcronym.setStatus("current")


class _Hm2AgentSystemSummerTimeState_Type(Integer32):
    """Custom type hm2AgentSystemSummerTimeState based on Integer32"""
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


_Hm2AgentSystemSummerTimeState_Type.__name__ = "Integer32"
_Hm2AgentSystemSummerTimeState_Object = MibScalar
hm2AgentSystemSummerTimeState = _Hm2AgentSystemSummerTimeState_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 1, 5),
    _Hm2AgentSystemSummerTimeState_Type()
)
hm2AgentSystemSummerTimeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSystemSummerTimeState.setStatus("current")
_Hm2AgentTimeZoneGroup_ObjectIdentity = ObjectIdentity
hm2AgentTimeZoneGroup = _Hm2AgentTimeZoneGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 2)
)


class _Hm2AgentTimeZoneHoursOffset_Type(Integer32):
    """Custom type hm2AgentTimeZoneHoursOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 14),
    )


_Hm2AgentTimeZoneHoursOffset_Type.__name__ = "Integer32"
_Hm2AgentTimeZoneHoursOffset_Object = MibScalar
hm2AgentTimeZoneHoursOffset = _Hm2AgentTimeZoneHoursOffset_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 2, 1),
    _Hm2AgentTimeZoneHoursOffset_Type()
)
hm2AgentTimeZoneHoursOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentTimeZoneHoursOffset.setStatus("current")


class _Hm2AgentTimeZoneMinutesOffset_Type(Integer32):
    """Custom type hm2AgentTimeZoneMinutesOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Hm2AgentTimeZoneMinutesOffset_Type.__name__ = "Integer32"
_Hm2AgentTimeZoneMinutesOffset_Object = MibScalar
hm2AgentTimeZoneMinutesOffset = _Hm2AgentTimeZoneMinutesOffset_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 2, 2),
    _Hm2AgentTimeZoneMinutesOffset_Type()
)
hm2AgentTimeZoneMinutesOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentTimeZoneMinutesOffset.setStatus("current")


class _Hm2AgentTimeZoneAcronym_Type(DisplayString):
    """Custom type hm2AgentTimeZoneAcronym based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_Hm2AgentTimeZoneAcronym_Type.__name__ = "DisplayString"
_Hm2AgentTimeZoneAcronym_Object = MibScalar
hm2AgentTimeZoneAcronym = _Hm2AgentTimeZoneAcronym_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 2, 3),
    _Hm2AgentTimeZoneAcronym_Type()
)
hm2AgentTimeZoneAcronym.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentTimeZoneAcronym.setStatus("current")
_Hm2AgentSummerTimeGroup_ObjectIdentity = ObjectIdentity
hm2AgentSummerTimeGroup = _Hm2AgentSummerTimeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3)
)


class _Hm2AgentSummerTimeMode_Type(Integer32):
    """Custom type hm2AgentSummerTimeMode based on Integer32"""
    defaultValue = 0

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
        *(("noSummertime", 0),
          ("recurring", 1),
          ("recurringEu", 2),
          ("recurringUsa", 3))
    )


_Hm2AgentSummerTimeMode_Type.__name__ = "Integer32"
_Hm2AgentSummerTimeMode_Object = MibScalar
hm2AgentSummerTimeMode = _Hm2AgentSummerTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3, 1),
    _Hm2AgentSummerTimeMode_Type()
)
hm2AgentSummerTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSummerTimeMode.setStatus("current")
_Hm2AgentSummerTimeRecurringGroup_ObjectIdentity = ObjectIdentity
hm2AgentSummerTimeRecurringGroup = _Hm2AgentSummerTimeRecurringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3, 2)
)


class _Hm2AgentStRecurringStartingWeek_Type(Integer32):
    """Custom type hm2AgentStRecurringStartingWeek based on Integer32"""
    defaultValue = 0

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
        *(("first", 1),
          ("fourth", 4),
          ("last", 5),
          ("none", 0),
          ("second", 2),
          ("third", 3))
    )


_Hm2AgentStRecurringStartingWeek_Type.__name__ = "Integer32"
_Hm2AgentStRecurringStartingWeek_Object = MibScalar
hm2AgentStRecurringStartingWeek = _Hm2AgentStRecurringStartingWeek_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3, 2, 1),
    _Hm2AgentStRecurringStartingWeek_Type()
)
hm2AgentStRecurringStartingWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStRecurringStartingWeek.setStatus("current")


class _Hm2AgentStRecurringStartingDay_Type(Integer32):
    """Custom type hm2AgentStRecurringStartingDay based on Integer32"""
    defaultValue = 0

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
        *(("fri", 6),
          ("mon", 2),
          ("none", 0),
          ("sat", 7),
          ("sun", 1),
          ("thu", 5),
          ("tue", 3),
          ("wed", 4))
    )


_Hm2AgentStRecurringStartingDay_Type.__name__ = "Integer32"
_Hm2AgentStRecurringStartingDay_Object = MibScalar
hm2AgentStRecurringStartingDay = _Hm2AgentStRecurringStartingDay_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3, 2, 2),
    _Hm2AgentStRecurringStartingDay_Type()
)
hm2AgentStRecurringStartingDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStRecurringStartingDay.setStatus("current")


class _Hm2AgentStRecurringStartingMonth_Type(Integer32):
    """Custom type hm2AgentStRecurringStartingMonth based on Integer32"""
    defaultValue = 0

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
              12)
        )
    )
    namedValues = NamedValues(
        *(("apr", 4),
          ("aug", 8),
          ("dec", 12),
          ("feb", 2),
          ("jan", 1),
          ("jul", 7),
          ("jun", 6),
          ("mar", 3),
          ("may", 5),
          ("none", 0),
          ("nov", 11),
          ("oct", 10),
          ("sep", 9))
    )


_Hm2AgentStRecurringStartingMonth_Type.__name__ = "Integer32"
_Hm2AgentStRecurringStartingMonth_Object = MibScalar
hm2AgentStRecurringStartingMonth = _Hm2AgentStRecurringStartingMonth_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3, 2, 3),
    _Hm2AgentStRecurringStartingMonth_Type()
)
hm2AgentStRecurringStartingMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStRecurringStartingMonth.setStatus("current")


class _Hm2AgentStRecurringStartingTime_Type(DisplayString):
    """Custom type hm2AgentStRecurringStartingTime based on DisplayString"""
    defaultValue = OctetString("00:00")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Hm2AgentStRecurringStartingTime_Type.__name__ = "DisplayString"
_Hm2AgentStRecurringStartingTime_Object = MibScalar
hm2AgentStRecurringStartingTime = _Hm2AgentStRecurringStartingTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3, 2, 4),
    _Hm2AgentStRecurringStartingTime_Type()
)
hm2AgentStRecurringStartingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStRecurringStartingTime.setStatus("current")


class _Hm2AgentStRecurringEndingWeek_Type(Integer32):
    """Custom type hm2AgentStRecurringEndingWeek based on Integer32"""
    defaultValue = 0

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
        *(("first", 1),
          ("fourth", 4),
          ("last", 5),
          ("none", 0),
          ("second", 2),
          ("third", 3))
    )


_Hm2AgentStRecurringEndingWeek_Type.__name__ = "Integer32"
_Hm2AgentStRecurringEndingWeek_Object = MibScalar
hm2AgentStRecurringEndingWeek = _Hm2AgentStRecurringEndingWeek_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3, 2, 5),
    _Hm2AgentStRecurringEndingWeek_Type()
)
hm2AgentStRecurringEndingWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStRecurringEndingWeek.setStatus("current")


class _Hm2AgentStRecurringEndingDay_Type(Integer32):
    """Custom type hm2AgentStRecurringEndingDay based on Integer32"""
    defaultValue = 0

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
        *(("fri", 6),
          ("mon", 2),
          ("none", 0),
          ("sat", 7),
          ("sun", 1),
          ("thu", 5),
          ("tue", 3),
          ("wed", 4))
    )


_Hm2AgentStRecurringEndingDay_Type.__name__ = "Integer32"
_Hm2AgentStRecurringEndingDay_Object = MibScalar
hm2AgentStRecurringEndingDay = _Hm2AgentStRecurringEndingDay_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3, 2, 6),
    _Hm2AgentStRecurringEndingDay_Type()
)
hm2AgentStRecurringEndingDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStRecurringEndingDay.setStatus("current")


class _Hm2AgentStRecurringEndingMonth_Type(Integer32):
    """Custom type hm2AgentStRecurringEndingMonth based on Integer32"""
    defaultValue = 0

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
              12)
        )
    )
    namedValues = NamedValues(
        *(("apr", 4),
          ("aug", 8),
          ("dec", 12),
          ("feb", 2),
          ("jan", 1),
          ("jul", 7),
          ("jun", 6),
          ("mar", 3),
          ("may", 5),
          ("none", 0),
          ("nov", 11),
          ("oct", 10),
          ("sep", 9))
    )


_Hm2AgentStRecurringEndingMonth_Type.__name__ = "Integer32"
_Hm2AgentStRecurringEndingMonth_Object = MibScalar
hm2AgentStRecurringEndingMonth = _Hm2AgentStRecurringEndingMonth_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3, 2, 7),
    _Hm2AgentStRecurringEndingMonth_Type()
)
hm2AgentStRecurringEndingMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStRecurringEndingMonth.setStatus("current")


class _Hm2AgentStRecurringEndingTime_Type(DisplayString):
    """Custom type hm2AgentStRecurringEndingTime based on DisplayString"""
    defaultValue = OctetString("00:00")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Hm2AgentStRecurringEndingTime_Type.__name__ = "DisplayString"
_Hm2AgentStRecurringEndingTime_Object = MibScalar
hm2AgentStRecurringEndingTime = _Hm2AgentStRecurringEndingTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3, 2, 8),
    _Hm2AgentStRecurringEndingTime_Type()
)
hm2AgentStRecurringEndingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStRecurringEndingTime.setStatus("current")


class _Hm2AgentStRecurringZoneAcronym_Type(DisplayString):
    """Custom type hm2AgentStRecurringZoneAcronym based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_Hm2AgentStRecurringZoneAcronym_Type.__name__ = "DisplayString"
_Hm2AgentStRecurringZoneAcronym_Object = MibScalar
hm2AgentStRecurringZoneAcronym = _Hm2AgentStRecurringZoneAcronym_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3, 2, 9),
    _Hm2AgentStRecurringZoneAcronym_Type()
)
hm2AgentStRecurringZoneAcronym.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStRecurringZoneAcronym.setStatus("current")


class _Hm2AgentStRecurringZoneOffset_Type(Integer32):
    """Custom type hm2AgentStRecurringZoneOffset based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Hm2AgentStRecurringZoneOffset_Type.__name__ = "Integer32"
_Hm2AgentStRecurringZoneOffset_Object = MibScalar
hm2AgentStRecurringZoneOffset = _Hm2AgentStRecurringZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 42, 3, 2, 10),
    _Hm2AgentStRecurringZoneOffset_Type()
)
hm2AgentStRecurringZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStRecurringZoneOffset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-TIMEZONE-MIB",
    **{"hm2PlatformTimeZone": hm2PlatformTimeZone,
       "hm2AgentSystemTimeGroup": hm2AgentSystemTimeGroup,
       "hm2AgentSystemTime": hm2AgentSystemTime,
       "hm2AgentSystemDate": hm2AgentSystemDate,
       "hm2AgentSystemTimeZoneAcronym": hm2AgentSystemTimeZoneAcronym,
       "hm2AgentSystemSummerTimeState": hm2AgentSystemSummerTimeState,
       "hm2AgentTimeZoneGroup": hm2AgentTimeZoneGroup,
       "hm2AgentTimeZoneHoursOffset": hm2AgentTimeZoneHoursOffset,
       "hm2AgentTimeZoneMinutesOffset": hm2AgentTimeZoneMinutesOffset,
       "hm2AgentTimeZoneAcronym": hm2AgentTimeZoneAcronym,
       "hm2AgentSummerTimeGroup": hm2AgentSummerTimeGroup,
       "hm2AgentSummerTimeMode": hm2AgentSummerTimeMode,
       "hm2AgentSummerTimeRecurringGroup": hm2AgentSummerTimeRecurringGroup,
       "hm2AgentStRecurringStartingWeek": hm2AgentStRecurringStartingWeek,
       "hm2AgentStRecurringStartingDay": hm2AgentStRecurringStartingDay,
       "hm2AgentStRecurringStartingMonth": hm2AgentStRecurringStartingMonth,
       "hm2AgentStRecurringStartingTime": hm2AgentStRecurringStartingTime,
       "hm2AgentStRecurringEndingWeek": hm2AgentStRecurringEndingWeek,
       "hm2AgentStRecurringEndingDay": hm2AgentStRecurringEndingDay,
       "hm2AgentStRecurringEndingMonth": hm2AgentStRecurringEndingMonth,
       "hm2AgentStRecurringEndingTime": hm2AgentStRecurringEndingTime,
       "hm2AgentStRecurringZoneAcronym": hm2AgentStRecurringZoneAcronym,
       "hm2AgentStRecurringZoneOffset": hm2AgentStRecurringZoneOffset}
)
