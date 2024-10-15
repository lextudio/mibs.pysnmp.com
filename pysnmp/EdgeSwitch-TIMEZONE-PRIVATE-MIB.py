# SNMP MIB module (EdgeSwitch-TIMEZONE-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EdgeSwitch-TIMEZONE-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:11 2024
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

(fastPath,) = mibBuilder.importSymbols(
    "EdgeSwitch-REF-MIB",
    "fastPath")

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

fastPathTimeZonePrivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42)
)
fastPathTimeZonePrivate.setRevisions(
        ("2011-01-26 00:00",
         "2007-02-28 05:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentSystemTimeGroup_ObjectIdentity = ObjectIdentity
agentSystemTimeGroup = _AgentSystemTimeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 1)
)
_AgentSystemTime_Type = DisplayString
_AgentSystemTime_Object = MibScalar
agentSystemTime = _AgentSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 1, 1),
    _AgentSystemTime_Type()
)
agentSystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSystemTime.setStatus("current")
_AgentSystemDate_Type = DisplayString
_AgentSystemDate_Object = MibScalar
agentSystemDate = _AgentSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 1, 2),
    _AgentSystemDate_Type()
)
agentSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSystemDate.setStatus("current")
_AgentSystemTimeZoneAcronym_Type = DisplayString
_AgentSystemTimeZoneAcronym_Object = MibScalar
agentSystemTimeZoneAcronym = _AgentSystemTimeZoneAcronym_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 1, 3),
    _AgentSystemTimeZoneAcronym_Type()
)
agentSystemTimeZoneAcronym.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSystemTimeZoneAcronym.setStatus("current")


class _AgentSystemTimeSource_Type(Integer32):
    """Custom type agentSystemTimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sntp", 1))
    )


_AgentSystemTimeSource_Type.__name__ = "Integer32"
_AgentSystemTimeSource_Object = MibScalar
agentSystemTimeSource = _AgentSystemTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 1, 4),
    _AgentSystemTimeSource_Type()
)
agentSystemTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSystemTimeSource.setStatus("current")


class _AgentSystemSummerTimeState_Type(Integer32):
    """Custom type agentSystemSummerTimeState based on Integer32"""
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


_AgentSystemSummerTimeState_Type.__name__ = "Integer32"
_AgentSystemSummerTimeState_Object = MibScalar
agentSystemSummerTimeState = _AgentSystemSummerTimeState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 1, 5),
    _AgentSystemSummerTimeState_Type()
)
agentSystemSummerTimeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSystemSummerTimeState.setStatus("current")
_AgentTimeZoneGroup_ObjectIdentity = ObjectIdentity
agentTimeZoneGroup = _AgentTimeZoneGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 2)
)


class _AgentTimeZoneHoursOffset_Type(Integer32):
    """Custom type agentTimeZoneHoursOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_AgentTimeZoneHoursOffset_Type.__name__ = "Integer32"
_AgentTimeZoneHoursOffset_Object = MibScalar
agentTimeZoneHoursOffset = _AgentTimeZoneHoursOffset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 2, 1),
    _AgentTimeZoneHoursOffset_Type()
)
agentTimeZoneHoursOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTimeZoneHoursOffset.setStatus("current")


class _AgentTimeZoneMinutesOffset_Type(Integer32):
    """Custom type agentTimeZoneMinutesOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AgentTimeZoneMinutesOffset_Type.__name__ = "Integer32"
_AgentTimeZoneMinutesOffset_Object = MibScalar
agentTimeZoneMinutesOffset = _AgentTimeZoneMinutesOffset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 2, 2),
    _AgentTimeZoneMinutesOffset_Type()
)
agentTimeZoneMinutesOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTimeZoneMinutesOffset.setStatus("current")
_AgentTimeZoneAcronym_Type = DisplayString
_AgentTimeZoneAcronym_Object = MibScalar
agentTimeZoneAcronym = _AgentTimeZoneAcronym_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 2, 3),
    _AgentTimeZoneAcronym_Type()
)
agentTimeZoneAcronym.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTimeZoneAcronym.setStatus("current")
_AgentSummerTimeGroup_ObjectIdentity = ObjectIdentity
agentSummerTimeGroup = _AgentSummerTimeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3)
)


class _AgentSummerTimeMode_Type(Integer32):
    """Custom type agentSummerTimeMode based on Integer32"""
    defaultValue = 0

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
        *(("noSummertime", 0),
          ("nonrecurring", 4),
          ("recurring", 1),
          ("recurringEu", 2),
          ("recurringUsa", 3))
    )


_AgentSummerTimeMode_Type.__name__ = "Integer32"
_AgentSummerTimeMode_Object = MibScalar
agentSummerTimeMode = _AgentSummerTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 1),
    _AgentSummerTimeMode_Type()
)
agentSummerTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSummerTimeMode.setStatus("current")
_AgentSummerTimeRecurringGroup_ObjectIdentity = ObjectIdentity
agentSummerTimeRecurringGroup = _AgentSummerTimeRecurringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 2)
)


class _AgentStRecurringStartingWeek_Type(Integer32):
    """Custom type agentStRecurringStartingWeek based on Integer32"""
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


_AgentStRecurringStartingWeek_Type.__name__ = "Integer32"
_AgentStRecurringStartingWeek_Object = MibScalar
agentStRecurringStartingWeek = _AgentStRecurringStartingWeek_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 2, 1),
    _AgentStRecurringStartingWeek_Type()
)
agentStRecurringStartingWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStRecurringStartingWeek.setStatus("current")


class _AgentStRecurringStartingDay_Type(Integer32):
    """Custom type agentStRecurringStartingDay based on Integer32"""
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


_AgentStRecurringStartingDay_Type.__name__ = "Integer32"
_AgentStRecurringStartingDay_Object = MibScalar
agentStRecurringStartingDay = _AgentStRecurringStartingDay_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 2, 2),
    _AgentStRecurringStartingDay_Type()
)
agentStRecurringStartingDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStRecurringStartingDay.setStatus("current")


class _AgentStRecurringStartingMonth_Type(Integer32):
    """Custom type agentStRecurringStartingMonth based on Integer32"""
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


_AgentStRecurringStartingMonth_Type.__name__ = "Integer32"
_AgentStRecurringStartingMonth_Object = MibScalar
agentStRecurringStartingMonth = _AgentStRecurringStartingMonth_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 2, 3),
    _AgentStRecurringStartingMonth_Type()
)
agentStRecurringStartingMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStRecurringStartingMonth.setStatus("current")


class _AgentStRecurringStartingTime_Type(DisplayString):
    """Custom type agentStRecurringStartingTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_AgentStRecurringStartingTime_Type.__name__ = "DisplayString"
_AgentStRecurringStartingTime_Object = MibScalar
agentStRecurringStartingTime = _AgentStRecurringStartingTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 2, 4),
    _AgentStRecurringStartingTime_Type()
)
agentStRecurringStartingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStRecurringStartingTime.setStatus("current")


class _AgentStRecurringEndingWeek_Type(Integer32):
    """Custom type agentStRecurringEndingWeek based on Integer32"""
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


_AgentStRecurringEndingWeek_Type.__name__ = "Integer32"
_AgentStRecurringEndingWeek_Object = MibScalar
agentStRecurringEndingWeek = _AgentStRecurringEndingWeek_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 2, 5),
    _AgentStRecurringEndingWeek_Type()
)
agentStRecurringEndingWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStRecurringEndingWeek.setStatus("current")


class _AgentStRecurringEndingDay_Type(Integer32):
    """Custom type agentStRecurringEndingDay based on Integer32"""
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


_AgentStRecurringEndingDay_Type.__name__ = "Integer32"
_AgentStRecurringEndingDay_Object = MibScalar
agentStRecurringEndingDay = _AgentStRecurringEndingDay_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 2, 6),
    _AgentStRecurringEndingDay_Type()
)
agentStRecurringEndingDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStRecurringEndingDay.setStatus("current")


class _AgentStRecurringEndingMonth_Type(Integer32):
    """Custom type agentStRecurringEndingMonth based on Integer32"""
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


_AgentStRecurringEndingMonth_Type.__name__ = "Integer32"
_AgentStRecurringEndingMonth_Object = MibScalar
agentStRecurringEndingMonth = _AgentStRecurringEndingMonth_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 2, 7),
    _AgentStRecurringEndingMonth_Type()
)
agentStRecurringEndingMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStRecurringEndingMonth.setStatus("current")


class _AgentStRecurringEndingTime_Type(DisplayString):
    """Custom type agentStRecurringEndingTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_AgentStRecurringEndingTime_Type.__name__ = "DisplayString"
_AgentStRecurringEndingTime_Object = MibScalar
agentStRecurringEndingTime = _AgentStRecurringEndingTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 2, 8),
    _AgentStRecurringEndingTime_Type()
)
agentStRecurringEndingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStRecurringEndingTime.setStatus("current")


class _AgentStRecurringZoneAcronym_Type(DisplayString):
    """Custom type agentStRecurringZoneAcronym based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AgentStRecurringZoneAcronym_Type.__name__ = "DisplayString"
_AgentStRecurringZoneAcronym_Object = MibScalar
agentStRecurringZoneAcronym = _AgentStRecurringZoneAcronym_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 2, 9),
    _AgentStRecurringZoneAcronym_Type()
)
agentStRecurringZoneAcronym.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStRecurringZoneAcronym.setStatus("current")


class _AgentStRecurringZoneOffset_Type(Integer32):
    """Custom type agentStRecurringZoneOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1440),
    )


_AgentStRecurringZoneOffset_Type.__name__ = "Integer32"
_AgentStRecurringZoneOffset_Object = MibScalar
agentStRecurringZoneOffset = _AgentStRecurringZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 2, 10),
    _AgentStRecurringZoneOffset_Type()
)
agentStRecurringZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStRecurringZoneOffset.setStatus("current")
_AgentSummerTimeNonRecurringGroup_ObjectIdentity = ObjectIdentity
agentSummerTimeNonRecurringGroup = _AgentSummerTimeNonRecurringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 3)
)


class _AgentStNonRecurringStartingDay_Type(Integer32):
    """Custom type agentStNonRecurringStartingDay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 31),
    )


_AgentStNonRecurringStartingDay_Type.__name__ = "Integer32"
_AgentStNonRecurringStartingDay_Object = MibScalar
agentStNonRecurringStartingDay = _AgentStNonRecurringStartingDay_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 3, 1),
    _AgentStNonRecurringStartingDay_Type()
)
agentStNonRecurringStartingDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStNonRecurringStartingDay.setStatus("current")


class _AgentStNonRecurringStartingMonth_Type(Integer32):
    """Custom type agentStNonRecurringStartingMonth based on Integer32"""
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


_AgentStNonRecurringStartingMonth_Type.__name__ = "Integer32"
_AgentStNonRecurringStartingMonth_Object = MibScalar
agentStNonRecurringStartingMonth = _AgentStNonRecurringStartingMonth_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 3, 2),
    _AgentStNonRecurringStartingMonth_Type()
)
agentStNonRecurringStartingMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStNonRecurringStartingMonth.setStatus("current")


class _AgentStNonRecurringStartingYear_Type(Integer32):
    """Custom type agentStNonRecurringStartingYear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2097),
    )


_AgentStNonRecurringStartingYear_Type.__name__ = "Integer32"
_AgentStNonRecurringStartingYear_Object = MibScalar
agentStNonRecurringStartingYear = _AgentStNonRecurringStartingYear_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 3, 3),
    _AgentStNonRecurringStartingYear_Type()
)
agentStNonRecurringStartingYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStNonRecurringStartingYear.setStatus("current")


class _AgentStNonRecurringStartingTime_Type(DisplayString):
    """Custom type agentStNonRecurringStartingTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_AgentStNonRecurringStartingTime_Type.__name__ = "DisplayString"
_AgentStNonRecurringStartingTime_Object = MibScalar
agentStNonRecurringStartingTime = _AgentStNonRecurringStartingTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 3, 4),
    _AgentStNonRecurringStartingTime_Type()
)
agentStNonRecurringStartingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStNonRecurringStartingTime.setStatus("current")


class _AgentStNonRecurringEndingDay_Type(Integer32):
    """Custom type agentStNonRecurringEndingDay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 31),
    )


_AgentStNonRecurringEndingDay_Type.__name__ = "Integer32"
_AgentStNonRecurringEndingDay_Object = MibScalar
agentStNonRecurringEndingDay = _AgentStNonRecurringEndingDay_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 3, 5),
    _AgentStNonRecurringEndingDay_Type()
)
agentStNonRecurringEndingDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStNonRecurringEndingDay.setStatus("current")


class _AgentStNonRecurringEndingMonth_Type(Integer32):
    """Custom type agentStNonRecurringEndingMonth based on Integer32"""
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


_AgentStNonRecurringEndingMonth_Type.__name__ = "Integer32"
_AgentStNonRecurringEndingMonth_Object = MibScalar
agentStNonRecurringEndingMonth = _AgentStNonRecurringEndingMonth_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 3, 6),
    _AgentStNonRecurringEndingMonth_Type()
)
agentStNonRecurringEndingMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStNonRecurringEndingMonth.setStatus("current")


class _AgentStNonRecurringEndingYear_Type(Integer32):
    """Custom type agentStNonRecurringEndingYear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2097),
    )


_AgentStNonRecurringEndingYear_Type.__name__ = "Integer32"
_AgentStNonRecurringEndingYear_Object = MibScalar
agentStNonRecurringEndingYear = _AgentStNonRecurringEndingYear_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 3, 7),
    _AgentStNonRecurringEndingYear_Type()
)
agentStNonRecurringEndingYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStNonRecurringEndingYear.setStatus("current")


class _AgentStNonRecurringEndingTime_Type(DisplayString):
    """Custom type agentStNonRecurringEndingTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_AgentStNonRecurringEndingTime_Type.__name__ = "DisplayString"
_AgentStNonRecurringEndingTime_Object = MibScalar
agentStNonRecurringEndingTime = _AgentStNonRecurringEndingTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 3, 8),
    _AgentStNonRecurringEndingTime_Type()
)
agentStNonRecurringEndingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStNonRecurringEndingTime.setStatus("current")


class _AgentStNonRecurringZoneOffset_Type(Integer32):
    """Custom type agentStNonRecurringZoneOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1440),
    )


_AgentStNonRecurringZoneOffset_Type.__name__ = "Integer32"
_AgentStNonRecurringZoneOffset_Object = MibScalar
agentStNonRecurringZoneOffset = _AgentStNonRecurringZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 3, 9),
    _AgentStNonRecurringZoneOffset_Type()
)
agentStNonRecurringZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStNonRecurringZoneOffset.setStatus("current")


class _AgentStNonRecurringZoneAcronym_Type(DisplayString):
    """Custom type agentStNonRecurringZoneAcronym based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AgentStNonRecurringZoneAcronym_Type.__name__ = "DisplayString"
_AgentStNonRecurringZoneAcronym_Object = MibScalar
agentStNonRecurringZoneAcronym = _AgentStNonRecurringZoneAcronym_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 42, 3, 3, 10),
    _AgentStNonRecurringZoneAcronym_Type()
)
agentStNonRecurringZoneAcronym.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentStNonRecurringZoneAcronym.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EdgeSwitch-TIMEZONE-PRIVATE-MIB",
    **{"fastPathTimeZonePrivate": fastPathTimeZonePrivate,
       "agentSystemTimeGroup": agentSystemTimeGroup,
       "agentSystemTime": agentSystemTime,
       "agentSystemDate": agentSystemDate,
       "agentSystemTimeZoneAcronym": agentSystemTimeZoneAcronym,
       "agentSystemTimeSource": agentSystemTimeSource,
       "agentSystemSummerTimeState": agentSystemSummerTimeState,
       "agentTimeZoneGroup": agentTimeZoneGroup,
       "agentTimeZoneHoursOffset": agentTimeZoneHoursOffset,
       "agentTimeZoneMinutesOffset": agentTimeZoneMinutesOffset,
       "agentTimeZoneAcronym": agentTimeZoneAcronym,
       "agentSummerTimeGroup": agentSummerTimeGroup,
       "agentSummerTimeMode": agentSummerTimeMode,
       "agentSummerTimeRecurringGroup": agentSummerTimeRecurringGroup,
       "agentStRecurringStartingWeek": agentStRecurringStartingWeek,
       "agentStRecurringStartingDay": agentStRecurringStartingDay,
       "agentStRecurringStartingMonth": agentStRecurringStartingMonth,
       "agentStRecurringStartingTime": agentStRecurringStartingTime,
       "agentStRecurringEndingWeek": agentStRecurringEndingWeek,
       "agentStRecurringEndingDay": agentStRecurringEndingDay,
       "agentStRecurringEndingMonth": agentStRecurringEndingMonth,
       "agentStRecurringEndingTime": agentStRecurringEndingTime,
       "agentStRecurringZoneAcronym": agentStRecurringZoneAcronym,
       "agentStRecurringZoneOffset": agentStRecurringZoneOffset,
       "agentSummerTimeNonRecurringGroup": agentSummerTimeNonRecurringGroup,
       "agentStNonRecurringStartingDay": agentStNonRecurringStartingDay,
       "agentStNonRecurringStartingMonth": agentStNonRecurringStartingMonth,
       "agentStNonRecurringStartingYear": agentStNonRecurringStartingYear,
       "agentStNonRecurringStartingTime": agentStNonRecurringStartingTime,
       "agentStNonRecurringEndingDay": agentStNonRecurringEndingDay,
       "agentStNonRecurringEndingMonth": agentStNonRecurringEndingMonth,
       "agentStNonRecurringEndingYear": agentStNonRecurringEndingYear,
       "agentStNonRecurringEndingTime": agentStNonRecurringEndingTime,
       "agentStNonRecurringZoneOffset": agentStNonRecurringZoneOffset,
       "agentStNonRecurringZoneAcronym": agentStNonRecurringZoneAcronym}
)
