# SNMP MIB module (Juniper-System-Clock-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-System-Clock-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:25 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniSysClockMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56)
)
juniSysClockMIB.setRevisions(
        ("2007-03-22 14:00",
         "2005-12-14 14:01",
         "2003-09-15 14:01",
         "2003-09-12 13:37",
         "2002-04-04 14:56")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniSysClockMonth(Integer32, TextualConvention):
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
        *(("april", 4),
          ("august", 8),
          ("december", 12),
          ("february", 2),
          ("january", 1),
          ("july", 7),
          ("june", 6),
          ("march", 3),
          ("may", 5),
          ("november", 11),
          ("october", 10),
          ("september", 9))
    )



class JuniSysClockWeekOfTheMonth(Integer32, TextualConvention):
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
        *(("weekFirst", 0),
          ("weekFive", 5),
          ("weekFour", 4),
          ("weekLast", 6),
          ("weekOne", 1),
          ("weekThree", 3),
          ("weekTwo", 2))
    )



class JuniSysClockDayOfTheWeek(Integer32, TextualConvention):
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



class JuniSysClockHour(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )



class JuniSysClockMinute(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )



class JuniNtpTimeStamp(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )



class JuniNtpClockSignedTime(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )



class JuniNtpClockUnsignedTime(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )



# MIB Managed Objects in the order of their OIDs

_JuniSysClockObjects_ObjectIdentity = ObjectIdentity
juniSysClockObjects = _JuniSysClockObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1)
)
_JuniSysClockTime_ObjectIdentity = ObjectIdentity
juniSysClockTime = _JuniSysClockTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 1)
)
_JuniSysClockDateAndTime_Type = DateAndTime
_JuniSysClockDateAndTime_Object = MibScalar
juniSysClockDateAndTime = _JuniSysClockDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 1, 1),
    _JuniSysClockDateAndTime_Type()
)
juniSysClockDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDateAndTime.setStatus("current")


class _JuniSysClockTimeZoneName_Type(DisplayString):
    """Custom type juniSysClockTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JuniSysClockTimeZoneName_Type.__name__ = "DisplayString"
_JuniSysClockTimeZoneName_Object = MibScalar
juniSysClockTimeZoneName = _JuniSysClockTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 1, 2),
    _JuniSysClockTimeZoneName_Type()
)
juniSysClockTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockTimeZoneName.setStatus("current")
_JuniSysClockDst_ObjectIdentity = ObjectIdentity
juniSysClockDst = _JuniSysClockDst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2)
)


class _JuniSysClockDstName_Type(DisplayString):
    """Custom type juniSysClockDstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JuniSysClockDstName_Type.__name__ = "DisplayString"
_JuniSysClockDstName_Object = MibScalar
juniSysClockDstName = _JuniSysClockDstName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 1),
    _JuniSysClockDstName_Type()
)
juniSysClockDstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstName.setStatus("current")


class _JuniSysClockDstOffset_Type(Integer32):
    """Custom type juniSysClockDstOffset based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_JuniSysClockDstOffset_Type.__name__ = "Integer32"
_JuniSysClockDstOffset_Object = MibScalar
juniSysClockDstOffset = _JuniSysClockDstOffset_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 2),
    _JuniSysClockDstOffset_Type()
)
juniSysClockDstOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstOffset.setStatus("current")
if mibBuilder.loadTexts:
    juniSysClockDstOffset.setUnits("minutes")


class _JuniSysClockDstStatus_Type(Integer32):
    """Custom type juniSysClockDstStatus based on Integer32"""
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
        *(("absolute", 2),
          ("off", 0),
          ("recognizedUS", 3),
          ("recurrent", 1))
    )


_JuniSysClockDstStatus_Type.__name__ = "Integer32"
_JuniSysClockDstStatus_Object = MibScalar
juniSysClockDstStatus = _JuniSysClockDstStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 3),
    _JuniSysClockDstStatus_Type()
)
juniSysClockDstStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstStatus.setStatus("current")
_JuniSysClockDstAbsoluteStartTime_Type = DateAndTime
_JuniSysClockDstAbsoluteStartTime_Object = MibScalar
juniSysClockDstAbsoluteStartTime = _JuniSysClockDstAbsoluteStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 4),
    _JuniSysClockDstAbsoluteStartTime_Type()
)
juniSysClockDstAbsoluteStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstAbsoluteStartTime.setStatus("current")
_JuniSysClockDstAbsoluteStopTime_Type = DateAndTime
_JuniSysClockDstAbsoluteStopTime_Object = MibScalar
juniSysClockDstAbsoluteStopTime = _JuniSysClockDstAbsoluteStopTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 5),
    _JuniSysClockDstAbsoluteStopTime_Type()
)
juniSysClockDstAbsoluteStopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstAbsoluteStopTime.setStatus("current")


class _JuniSysClockDstRecurStartMonth_Type(JuniSysClockMonth):
    """Custom type juniSysClockDstRecurStartMonth based on JuniSysClockMonth"""


_JuniSysClockDstRecurStartMonth_Object = MibScalar
juniSysClockDstRecurStartMonth = _JuniSysClockDstRecurStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 6),
    _JuniSysClockDstRecurStartMonth_Type()
)
juniSysClockDstRecurStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstRecurStartMonth.setStatus("current")


class _JuniSysClockDstRecurStartWeek_Type(JuniSysClockWeekOfTheMonth):
    """Custom type juniSysClockDstRecurStartWeek based on JuniSysClockWeekOfTheMonth"""


_JuniSysClockDstRecurStartWeek_Object = MibScalar
juniSysClockDstRecurStartWeek = _JuniSysClockDstRecurStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 7),
    _JuniSysClockDstRecurStartWeek_Type()
)
juniSysClockDstRecurStartWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstRecurStartWeek.setStatus("current")


class _JuniSysClockDstRecurStartDay_Type(JuniSysClockDayOfTheWeek):
    """Custom type juniSysClockDstRecurStartDay based on JuniSysClockDayOfTheWeek"""


_JuniSysClockDstRecurStartDay_Object = MibScalar
juniSysClockDstRecurStartDay = _JuniSysClockDstRecurStartDay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 8),
    _JuniSysClockDstRecurStartDay_Type()
)
juniSysClockDstRecurStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstRecurStartDay.setStatus("current")


class _JuniSysClockDstRecurStartHour_Type(JuniSysClockHour):
    """Custom type juniSysClockDstRecurStartHour based on JuniSysClockHour"""
    defaultValue = 1


_JuniSysClockDstRecurStartHour_Object = MibScalar
juniSysClockDstRecurStartHour = _JuniSysClockDstRecurStartHour_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 9),
    _JuniSysClockDstRecurStartHour_Type()
)
juniSysClockDstRecurStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstRecurStartHour.setStatus("current")


class _JuniSysClockDstRecurStartMinute_Type(JuniSysClockMinute):
    """Custom type juniSysClockDstRecurStartMinute based on JuniSysClockMinute"""
    defaultValue = 0


_JuniSysClockDstRecurStartMinute_Object = MibScalar
juniSysClockDstRecurStartMinute = _JuniSysClockDstRecurStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 10),
    _JuniSysClockDstRecurStartMinute_Type()
)
juniSysClockDstRecurStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstRecurStartMinute.setStatus("current")


class _JuniSysClockDstRecurStopMonth_Type(JuniSysClockMonth):
    """Custom type juniSysClockDstRecurStopMonth based on JuniSysClockMonth"""


_JuniSysClockDstRecurStopMonth_Object = MibScalar
juniSysClockDstRecurStopMonth = _JuniSysClockDstRecurStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 11),
    _JuniSysClockDstRecurStopMonth_Type()
)
juniSysClockDstRecurStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstRecurStopMonth.setStatus("current")


class _JuniSysClockDstRecurStopWeek_Type(JuniSysClockWeekOfTheMonth):
    """Custom type juniSysClockDstRecurStopWeek based on JuniSysClockWeekOfTheMonth"""


_JuniSysClockDstRecurStopWeek_Object = MibScalar
juniSysClockDstRecurStopWeek = _JuniSysClockDstRecurStopWeek_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 12),
    _JuniSysClockDstRecurStopWeek_Type()
)
juniSysClockDstRecurStopWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstRecurStopWeek.setStatus("current")


class _JuniSysClockDstRecurStopDay_Type(JuniSysClockDayOfTheWeek):
    """Custom type juniSysClockDstRecurStopDay based on JuniSysClockDayOfTheWeek"""


_JuniSysClockDstRecurStopDay_Object = MibScalar
juniSysClockDstRecurStopDay = _JuniSysClockDstRecurStopDay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 13),
    _JuniSysClockDstRecurStopDay_Type()
)
juniSysClockDstRecurStopDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstRecurStopDay.setStatus("current")


class _JuniSysClockDstRecurStopHour_Type(JuniSysClockHour):
    """Custom type juniSysClockDstRecurStopHour based on JuniSysClockHour"""
    defaultValue = 2


_JuniSysClockDstRecurStopHour_Object = MibScalar
juniSysClockDstRecurStopHour = _JuniSysClockDstRecurStopHour_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 14),
    _JuniSysClockDstRecurStopHour_Type()
)
juniSysClockDstRecurStopHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstRecurStopHour.setStatus("current")


class _JuniSysClockDstRecurStopMinute_Type(JuniSysClockMinute):
    """Custom type juniSysClockDstRecurStopMinute based on JuniSysClockMinute"""
    defaultValue = 0


_JuniSysClockDstRecurStopMinute_Object = MibScalar
juniSysClockDstRecurStopMinute = _JuniSysClockDstRecurStopMinute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 15),
    _JuniSysClockDstRecurStopMinute_Type()
)
juniSysClockDstRecurStopMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSysClockDstRecurStopMinute.setStatus("current")
_JuniNtpObjects_ObjectIdentity = ObjectIdentity
juniNtpObjects = _JuniNtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2)
)
_JuniNtpTraps_ObjectIdentity = ObjectIdentity
juniNtpTraps = _JuniNtpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 0)
)
_JuniNtpSysClock_ObjectIdentity = ObjectIdentity
juniNtpSysClock = _JuniNtpSysClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1)
)


class _JuniNtpSysClockState_Type(Integer32):
    """Custom type juniNtpSysClockState based on Integer32"""
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
        *(("frequencyCalibrated", 1),
          ("frequencyCalibrationIsGoingOn", 3),
          ("neverFrequencyCalibrated", 0),
          ("setToServerTime", 2),
          ("spikeDetected", 5),
          ("synchronized", 4))
    )


_JuniNtpSysClockState_Type.__name__ = "Integer32"
_JuniNtpSysClockState_Object = MibScalar
juniNtpSysClockState = _JuniNtpSysClockState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 1),
    _JuniNtpSysClockState_Type()
)
juniNtpSysClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpSysClockState.setStatus("current")
_JuniNtpSysClockOffsetError_Type = JuniNtpClockSignedTime
_JuniNtpSysClockOffsetError_Object = MibScalar
juniNtpSysClockOffsetError = _JuniNtpSysClockOffsetError_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 2),
    _JuniNtpSysClockOffsetError_Type()
)
juniNtpSysClockOffsetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpSysClockOffsetError.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniNtpSysClockOffsetError.setUnits("seconds")
_JuniNtpSysClockFrequencyError_Type = Integer32
_JuniNtpSysClockFrequencyError_Object = MibScalar
juniNtpSysClockFrequencyError = _JuniNtpSysClockFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 3),
    _JuniNtpSysClockFrequencyError_Type()
)
juniNtpSysClockFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpSysClockFrequencyError.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniNtpSysClockFrequencyError.setUnits("ppm")
_JuniNtpSysClockRootDelay_Type = JuniNtpClockSignedTime
_JuniNtpSysClockRootDelay_Object = MibScalar
juniNtpSysClockRootDelay = _JuniNtpSysClockRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 4),
    _JuniNtpSysClockRootDelay_Type()
)
juniNtpSysClockRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpSysClockRootDelay.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpSysClockRootDelay.setUnits("seconds")
_JuniNtpSysClockRootDispersion_Type = JuniNtpClockUnsignedTime
_JuniNtpSysClockRootDispersion_Object = MibScalar
juniNtpSysClockRootDispersion = _JuniNtpSysClockRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 5),
    _JuniNtpSysClockRootDispersion_Type()
)
juniNtpSysClockRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpSysClockRootDispersion.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpSysClockRootDispersion.setUnits("seconds")


class _JuniNtpSysClockStratumNumber_Type(Integer32):
    """Custom type juniNtpSysClockStratumNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_JuniNtpSysClockStratumNumber_Type.__name__ = "Integer32"
_JuniNtpSysClockStratumNumber_Object = MibScalar
juniNtpSysClockStratumNumber = _JuniNtpSysClockStratumNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 6),
    _JuniNtpSysClockStratumNumber_Type()
)
juniNtpSysClockStratumNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpSysClockStratumNumber.setStatus("current")
_JuniNtpSysClockLastUpdateTime_Type = JuniNtpTimeStamp
_JuniNtpSysClockLastUpdateTime_Object = MibScalar
juniNtpSysClockLastUpdateTime = _JuniNtpSysClockLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 7),
    _JuniNtpSysClockLastUpdateTime_Type()
)
juniNtpSysClockLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpSysClockLastUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpSysClockLastUpdateTime.setUnits("seconds")
_JuniNtpSysClockLastUpdateServer_Type = IpAddress
_JuniNtpSysClockLastUpdateServer_Object = MibScalar
juniNtpSysClockLastUpdateServer = _JuniNtpSysClockLastUpdateServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 8),
    _JuniNtpSysClockLastUpdateServer_Type()
)
juniNtpSysClockLastUpdateServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpSysClockLastUpdateServer.setStatus("current")


class _JuniNtpSysClockOffsetErrorNew_Type(DisplayString):
    """Custom type juniNtpSysClockOffsetErrorNew based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_JuniNtpSysClockOffsetErrorNew_Type.__name__ = "DisplayString"
_JuniNtpSysClockOffsetErrorNew_Object = MibScalar
juniNtpSysClockOffsetErrorNew = _JuniNtpSysClockOffsetErrorNew_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 9),
    _JuniNtpSysClockOffsetErrorNew_Type()
)
juniNtpSysClockOffsetErrorNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpSysClockOffsetErrorNew.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpSysClockOffsetErrorNew.setUnits("seconds")


class _JuniNtpSysClockFrequencyErrorNew_Type(DisplayString):
    """Custom type juniNtpSysClockFrequencyErrorNew based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_JuniNtpSysClockFrequencyErrorNew_Type.__name__ = "DisplayString"
_JuniNtpSysClockFrequencyErrorNew_Object = MibScalar
juniNtpSysClockFrequencyErrorNew = _JuniNtpSysClockFrequencyErrorNew_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 10),
    _JuniNtpSysClockFrequencyErrorNew_Type()
)
juniNtpSysClockFrequencyErrorNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpSysClockFrequencyErrorNew.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpSysClockFrequencyErrorNew.setUnits("ppm")
_JuniNtpClient_ObjectIdentity = ObjectIdentity
juniNtpClient = _JuniNtpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2)
)


class _JuniNtpClientAdminStatus_Type(JuniEnable):
    """Custom type juniNtpClientAdminStatus based on JuniEnable"""


_JuniNtpClientAdminStatus_Object = MibScalar
juniNtpClientAdminStatus = _JuniNtpClientAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 1),
    _JuniNtpClientAdminStatus_Type()
)
juniNtpClientAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniNtpClientAdminStatus.setStatus("current")
_JuniNtpClientSystemRouterIndex_Type = Unsigned32
_JuniNtpClientSystemRouterIndex_Object = MibScalar
juniNtpClientSystemRouterIndex = _JuniNtpClientSystemRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 2),
    _JuniNtpClientSystemRouterIndex_Type()
)
juniNtpClientSystemRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpClientSystemRouterIndex.setStatus("current")


class _JuniNtpClientPacketSourceIfIndex_Type(Integer32):
    """Custom type juniNtpClientPacketSourceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniNtpClientPacketSourceIfIndex_Type.__name__ = "Integer32"
_JuniNtpClientPacketSourceIfIndex_Object = MibScalar
juniNtpClientPacketSourceIfIndex = _JuniNtpClientPacketSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 3),
    _JuniNtpClientPacketSourceIfIndex_Type()
)
juniNtpClientPacketSourceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniNtpClientPacketSourceIfIndex.setStatus("current")


class _JuniNtpClientBroadcastDelay_Type(Integer32):
    """Custom type juniNtpClientBroadcastDelay based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_JuniNtpClientBroadcastDelay_Type.__name__ = "Integer32"
_JuniNtpClientBroadcastDelay_Object = MibScalar
juniNtpClientBroadcastDelay = _JuniNtpClientBroadcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 4),
    _JuniNtpClientBroadcastDelay_Type()
)
juniNtpClientBroadcastDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniNtpClientBroadcastDelay.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpClientBroadcastDelay.setUnits("microseconds")
_JuniNtpClientIfTable_Object = MibTable
juniNtpClientIfTable = _JuniNtpClientIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5)
)
if mibBuilder.loadTexts:
    juniNtpClientIfTable.setStatus("current")
_JuniNtpClientIfEntry_Object = MibTableRow
juniNtpClientIfEntry = _JuniNtpClientIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1)
)
juniNtpClientIfEntry.setIndexNames(
    (0, "Juniper-System-Clock-MIB", "juniNtpClientIfRouterIndex"),
    (0, "Juniper-System-Clock-MIB", "juniNtpClientIfIfIndex"),
)
if mibBuilder.loadTexts:
    juniNtpClientIfEntry.setStatus("current")
_JuniNtpClientIfRouterIndex_Type = Unsigned32
_JuniNtpClientIfRouterIndex_Object = MibTableColumn
juniNtpClientIfRouterIndex = _JuniNtpClientIfRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1, 1),
    _JuniNtpClientIfRouterIndex_Type()
)
juniNtpClientIfRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniNtpClientIfRouterIndex.setStatus("current")


class _JuniNtpClientIfIfIndex_Type(Integer32):
    """Custom type juniNtpClientIfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniNtpClientIfIfIndex_Type.__name__ = "Integer32"
_JuniNtpClientIfIfIndex_Object = MibTableColumn
juniNtpClientIfIfIndex = _JuniNtpClientIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1, 2),
    _JuniNtpClientIfIfIndex_Type()
)
juniNtpClientIfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniNtpClientIfIfIndex.setStatus("current")
_JuniNtpClientIfDisable_Type = TruthValue
_JuniNtpClientIfDisable_Object = MibTableColumn
juniNtpClientIfDisable = _JuniNtpClientIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1, 3),
    _JuniNtpClientIfDisable_Type()
)
juniNtpClientIfDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNtpClientIfDisable.setStatus("current")
_JuniNtpClientIfIsBroadcastClient_Type = TruthValue
_JuniNtpClientIfIsBroadcastClient_Object = MibTableColumn
juniNtpClientIfIsBroadcastClient = _JuniNtpClientIfIsBroadcastClient_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1, 4),
    _JuniNtpClientIfIsBroadcastClient_Type()
)
juniNtpClientIfIsBroadcastClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNtpClientIfIsBroadcastClient.setStatus("current")
_JuniNtpClientIfIsBroadcastServer_Type = TruthValue
_JuniNtpClientIfIsBroadcastServer_Object = MibTableColumn
juniNtpClientIfIsBroadcastServer = _JuniNtpClientIfIsBroadcastServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1, 5),
    _JuniNtpClientIfIsBroadcastServer_Type()
)
juniNtpClientIfIsBroadcastServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNtpClientIfIsBroadcastServer.setStatus("current")


class _JuniNtpClientIfIsBroadcastServerVersion_Type(Integer32):
    """Custom type juniNtpClientIfIsBroadcastServerVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_JuniNtpClientIfIsBroadcastServerVersion_Type.__name__ = "Integer32"
_JuniNtpClientIfIsBroadcastServerVersion_Object = MibTableColumn
juniNtpClientIfIsBroadcastServerVersion = _JuniNtpClientIfIsBroadcastServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1, 6),
    _JuniNtpClientIfIsBroadcastServerVersion_Type()
)
juniNtpClientIfIsBroadcastServerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniNtpClientIfIsBroadcastServerVersion.setStatus("current")


class _JuniNtpClientIfIsBroadcastServerDelay_Type(Integer32):
    """Custom type juniNtpClientIfIsBroadcastServerDelay based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 17),
    )


_JuniNtpClientIfIsBroadcastServerDelay_Type.__name__ = "Integer32"
_JuniNtpClientIfIsBroadcastServerDelay_Object = MibTableColumn
juniNtpClientIfIsBroadcastServerDelay = _JuniNtpClientIfIsBroadcastServerDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1, 7),
    _JuniNtpClientIfIsBroadcastServerDelay_Type()
)
juniNtpClientIfIsBroadcastServerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniNtpClientIfIsBroadcastServerDelay.setStatus("current")
_JuniNtpServer_ObjectIdentity = ObjectIdentity
juniNtpServer = _JuniNtpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 3)
)


class _JuniNtpServerStratumNumber_Type(Integer32):
    """Custom type juniNtpServerStratumNumber based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniNtpServerStratumNumber_Type.__name__ = "Integer32"
_JuniNtpServerStratumNumber_Object = MibScalar
juniNtpServerStratumNumber = _JuniNtpServerStratumNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 3, 1),
    _JuniNtpServerStratumNumber_Type()
)
juniNtpServerStratumNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniNtpServerStratumNumber.setStatus("current")
_JuniNtpServerAdminStatus_Type = JuniEnable
_JuniNtpServerAdminStatus_Object = MibScalar
juniNtpServerAdminStatus = _JuniNtpServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 3, 2),
    _JuniNtpServerAdminStatus_Type()
)
juniNtpServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniNtpServerAdminStatus.setStatus("current")
_JuniNtpPeers_ObjectIdentity = ObjectIdentity
juniNtpPeers = _JuniNtpPeers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4)
)
_JuniNtpPeerCfgTable_Object = MibTable
juniNtpPeerCfgTable = _JuniNtpPeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1)
)
if mibBuilder.loadTexts:
    juniNtpPeerCfgTable.setStatus("current")
_JuniNtpPeerCfgEntry_Object = MibTableRow
juniNtpPeerCfgEntry = _JuniNtpPeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1, 1)
)
juniNtpPeerCfgEntry.setIndexNames(
    (0, "Juniper-System-Clock-MIB", "juniNtpClientIfRouterIndex"),
    (0, "Juniper-System-Clock-MIB", "juniNtpPeerCfgIpAddress"),
)
if mibBuilder.loadTexts:
    juniNtpPeerCfgEntry.setStatus("current")
_JuniNtpPeerCfgIpAddress_Type = IpAddress
_JuniNtpPeerCfgIpAddress_Object = MibTableColumn
juniNtpPeerCfgIpAddress = _JuniNtpPeerCfgIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1, 1, 1),
    _JuniNtpPeerCfgIpAddress_Type()
)
juniNtpPeerCfgIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniNtpPeerCfgIpAddress.setStatus("current")


class _JuniNtpPeerCfgNtpVersion_Type(Integer32):
    """Custom type juniNtpPeerCfgNtpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_JuniNtpPeerCfgNtpVersion_Type.__name__ = "Integer32"
_JuniNtpPeerCfgNtpVersion_Object = MibTableColumn
juniNtpPeerCfgNtpVersion = _JuniNtpPeerCfgNtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1, 1, 2),
    _JuniNtpPeerCfgNtpVersion_Type()
)
juniNtpPeerCfgNtpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNtpPeerCfgNtpVersion.setStatus("current")


class _JuniNtpPeerCfgPacketSourceIfIndex_Type(Integer32):
    """Custom type juniNtpPeerCfgPacketSourceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniNtpPeerCfgPacketSourceIfIndex_Type.__name__ = "Integer32"
_JuniNtpPeerCfgPacketSourceIfIndex_Object = MibTableColumn
juniNtpPeerCfgPacketSourceIfIndex = _JuniNtpPeerCfgPacketSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1, 1, 3),
    _JuniNtpPeerCfgPacketSourceIfIndex_Type()
)
juniNtpPeerCfgPacketSourceIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNtpPeerCfgPacketSourceIfIndex.setStatus("current")
_JuniNtpPeerCfgIsPreferred_Type = TruthValue
_JuniNtpPeerCfgIsPreferred_Object = MibTableColumn
juniNtpPeerCfgIsPreferred = _JuniNtpPeerCfgIsPreferred_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1, 1, 4),
    _JuniNtpPeerCfgIsPreferred_Type()
)
juniNtpPeerCfgIsPreferred.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNtpPeerCfgIsPreferred.setStatus("current")
_JuniNtpPeerCfgRowStatus_Type = RowStatus
_JuniNtpPeerCfgRowStatus_Object = MibTableColumn
juniNtpPeerCfgRowStatus = _JuniNtpPeerCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1, 1, 5),
    _JuniNtpPeerCfgRowStatus_Type()
)
juniNtpPeerCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNtpPeerCfgRowStatus.setStatus("current")
_JuniNtpPeerTable_Object = MibTable
juniNtpPeerTable = _JuniNtpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2)
)
if mibBuilder.loadTexts:
    juniNtpPeerTable.setStatus("current")
_JuniNtpPeerEntry_Object = MibTableRow
juniNtpPeerEntry = _JuniNtpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1)
)
juniNtpPeerEntry.setIndexNames(
    (0, "Juniper-System-Clock-MIB", "juniNtpClientIfRouterIndex"),
    (0, "Juniper-System-Clock-MIB", "juniNtpPeerCfgIpAddress"),
)
if mibBuilder.loadTexts:
    juniNtpPeerEntry.setStatus("current")


class _JuniNtpPeerState_Type(OctetString):
    """Custom type juniNtpPeerState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_JuniNtpPeerState_Type.__name__ = "OctetString"
_JuniNtpPeerState_Object = MibTableColumn
juniNtpPeerState = _JuniNtpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 1),
    _JuniNtpPeerState_Type()
)
juniNtpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerState.setStatus("current")


class _JuniNtpPeerStratumNumber_Type(Integer32):
    """Custom type juniNtpPeerStratumNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniNtpPeerStratumNumber_Type.__name__ = "Integer32"
_JuniNtpPeerStratumNumber_Object = MibTableColumn
juniNtpPeerStratumNumber = _JuniNtpPeerStratumNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 2),
    _JuniNtpPeerStratumNumber_Type()
)
juniNtpPeerStratumNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerStratumNumber.setStatus("current")


class _JuniNtpPeerAssociationMode_Type(Integer32):
    """Custom type juniNtpPeerAssociationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broacastServer", 0),
          ("multicastServer", 1),
          ("unicastServer", 2))
    )


_JuniNtpPeerAssociationMode_Type.__name__ = "Integer32"
_JuniNtpPeerAssociationMode_Object = MibTableColumn
juniNtpPeerAssociationMode = _JuniNtpPeerAssociationMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 3),
    _JuniNtpPeerAssociationMode_Type()
)
juniNtpPeerAssociationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerAssociationMode.setStatus("current")
_JuniNtpPeerBroadcastInterval_Type = Integer32
_JuniNtpPeerBroadcastInterval_Object = MibTableColumn
juniNtpPeerBroadcastInterval = _JuniNtpPeerBroadcastInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 4),
    _JuniNtpPeerBroadcastInterval_Type()
)
juniNtpPeerBroadcastInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerBroadcastInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerBroadcastInterval.setUnits("seconds")
_JuniNtpPeerPolledInterval_Type = Integer32
_JuniNtpPeerPolledInterval_Object = MibTableColumn
juniNtpPeerPolledInterval = _JuniNtpPeerPolledInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 5),
    _JuniNtpPeerPolledInterval_Type()
)
juniNtpPeerPolledInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerPolledInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerPolledInterval.setUnits("seconds")
_JuniNtpPeerPollingInterval_Type = Integer32
_JuniNtpPeerPollingInterval_Object = MibTableColumn
juniNtpPeerPollingInterval = _JuniNtpPeerPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 6),
    _JuniNtpPeerPollingInterval_Type()
)
juniNtpPeerPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerPollingInterval.setUnits("seconds")
_JuniNtpPeerDelay_Type = JuniNtpClockSignedTime
_JuniNtpPeerDelay_Object = MibTableColumn
juniNtpPeerDelay = _JuniNtpPeerDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 7),
    _JuniNtpPeerDelay_Type()
)
juniNtpPeerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerDelay.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerDelay.setUnits("seconds")
_JuniNtpPeerDispersion_Type = JuniNtpClockUnsignedTime
_JuniNtpPeerDispersion_Object = MibTableColumn
juniNtpPeerDispersion = _JuniNtpPeerDispersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 8),
    _JuniNtpPeerDispersion_Type()
)
juniNtpPeerDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerDispersion.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerDispersion.setUnits("seconds")
_JuniNtpPeerOffsetError_Type = JuniNtpClockSignedTime
_JuniNtpPeerOffsetError_Object = MibTableColumn
juniNtpPeerOffsetError = _JuniNtpPeerOffsetError_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 9),
    _JuniNtpPeerOffsetError_Type()
)
juniNtpPeerOffsetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerOffsetError.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerOffsetError.setUnits("seconds")


class _JuniNtpPeerReachability_Type(OctetString):
    """Custom type juniNtpPeerReachability based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_JuniNtpPeerReachability_Type.__name__ = "OctetString"
_JuniNtpPeerReachability_Object = MibTableColumn
juniNtpPeerReachability = _JuniNtpPeerReachability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 10),
    _JuniNtpPeerReachability_Type()
)
juniNtpPeerReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerReachability.setStatus("current")
_JuniNtpPeerRootDelay_Type = JuniNtpClockSignedTime
_JuniNtpPeerRootDelay_Object = MibTableColumn
juniNtpPeerRootDelay = _JuniNtpPeerRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 11),
    _JuniNtpPeerRootDelay_Type()
)
juniNtpPeerRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerRootDelay.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerRootDelay.setUnits("seconds")
_JuniNtpPeerRootDispersion_Type = JuniNtpClockUnsignedTime
_JuniNtpPeerRootDispersion_Object = MibTableColumn
juniNtpPeerRootDispersion = _JuniNtpPeerRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 12),
    _JuniNtpPeerRootDispersion_Type()
)
juniNtpPeerRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerRootDispersion.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerRootDispersion.setUnits("seconds")
_JuniNtpPeerRootSyncDistance_Type = JuniNtpClockSignedTime
_JuniNtpPeerRootSyncDistance_Object = MibTableColumn
juniNtpPeerRootSyncDistance = _JuniNtpPeerRootSyncDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 13),
    _JuniNtpPeerRootSyncDistance_Type()
)
juniNtpPeerRootSyncDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerRootSyncDistance.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerRootSyncDistance.setUnits("seconds")
_JuniNtpPeerRootTime_Type = JuniNtpTimeStamp
_JuniNtpPeerRootTime_Object = MibTableColumn
juniNtpPeerRootTime = _JuniNtpPeerRootTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 14),
    _JuniNtpPeerRootTime_Type()
)
juniNtpPeerRootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerRootTime.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerRootTime.setUnits("seconds")
_JuniNtpPeerRootTimeUpdateServer_Type = IpAddress
_JuniNtpPeerRootTimeUpdateServer_Object = MibTableColumn
juniNtpPeerRootTimeUpdateServer = _JuniNtpPeerRootTimeUpdateServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 15),
    _JuniNtpPeerRootTimeUpdateServer_Type()
)
juniNtpPeerRootTimeUpdateServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerRootTimeUpdateServer.setStatus("current")
_JuniNtpPeerReceiveTime_Type = JuniNtpTimeStamp
_JuniNtpPeerReceiveTime_Object = MibTableColumn
juniNtpPeerReceiveTime = _JuniNtpPeerReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 16),
    _JuniNtpPeerReceiveTime_Type()
)
juniNtpPeerReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerReceiveTime.setStatus("current")
_JuniNtpPeerTransmitTime_Type = JuniNtpTimeStamp
_JuniNtpPeerTransmitTime_Object = MibTableColumn
juniNtpPeerTransmitTime = _JuniNtpPeerTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 17),
    _JuniNtpPeerTransmitTime_Type()
)
juniNtpPeerTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerTransmitTime.setStatus("current")
_JuniNtpPeerRequestTime_Type = JuniNtpTimeStamp
_JuniNtpPeerRequestTime_Object = MibTableColumn
juniNtpPeerRequestTime = _JuniNtpPeerRequestTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 18),
    _JuniNtpPeerRequestTime_Type()
)
juniNtpPeerRequestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerRequestTime.setStatus("current")
_JuniNtpPeerPrecision_Type = JuniNtpClockSignedTime
_JuniNtpPeerPrecision_Object = MibTableColumn
juniNtpPeerPrecision = _JuniNtpPeerPrecision_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 19),
    _JuniNtpPeerPrecision_Type()
)
juniNtpPeerPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerPrecision.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerPrecision.setUnits("seconds")
_JuniNtpPeerLastUpdateTime_Type = Unsigned32
_JuniNtpPeerLastUpdateTime_Object = MibTableColumn
juniNtpPeerLastUpdateTime = _JuniNtpPeerLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 20),
    _JuniNtpPeerLastUpdateTime_Type()
)
juniNtpPeerLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerLastUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerLastUpdateTime.setUnits("seconds")
_JuniNtpPeerFilterRegisterTable_Object = MibTable
juniNtpPeerFilterRegisterTable = _JuniNtpPeerFilterRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 3)
)
if mibBuilder.loadTexts:
    juniNtpPeerFilterRegisterTable.setStatus("current")
_JuniNtpPeerFilterRegisterEntry_Object = MibTableRow
juniNtpPeerFilterRegisterEntry = _JuniNtpPeerFilterRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 3, 1)
)
juniNtpPeerFilterRegisterEntry.setIndexNames(
    (0, "Juniper-System-Clock-MIB", "juniNtpPeerCfgIpAddress"),
    (0, "Juniper-System-Clock-MIB", "juniNtpPeerFilterIndex"),
)
if mibBuilder.loadTexts:
    juniNtpPeerFilterRegisterEntry.setStatus("current")
_JuniNtpPeerFilterIndex_Type = Unsigned32
_JuniNtpPeerFilterIndex_Object = MibTableColumn
juniNtpPeerFilterIndex = _JuniNtpPeerFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 3, 1, 1),
    _JuniNtpPeerFilterIndex_Type()
)
juniNtpPeerFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniNtpPeerFilterIndex.setStatus("current")
_JuniNtpPeerFilterOffset_Type = JuniNtpClockSignedTime
_JuniNtpPeerFilterOffset_Object = MibTableColumn
juniNtpPeerFilterOffset = _JuniNtpPeerFilterOffset_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 3, 1, 2),
    _JuniNtpPeerFilterOffset_Type()
)
juniNtpPeerFilterOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerFilterOffset.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerFilterOffset.setUnits("seconds")
_JuniNtpPeerFilterDelay_Type = JuniNtpClockSignedTime
_JuniNtpPeerFilterDelay_Object = MibTableColumn
juniNtpPeerFilterDelay = _JuniNtpPeerFilterDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 3, 1, 3),
    _JuniNtpPeerFilterDelay_Type()
)
juniNtpPeerFilterDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerFilterDelay.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerFilterDelay.setUnits("seconds")
_JuniNtpPeerFilterDispersion_Type = JuniNtpClockUnsignedTime
_JuniNtpPeerFilterDispersion_Object = MibTableColumn
juniNtpPeerFilterDispersion = _JuniNtpPeerFilterDispersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 3, 1, 4),
    _JuniNtpPeerFilterDispersion_Type()
)
juniNtpPeerFilterDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniNtpPeerFilterDispersion.setStatus("current")
if mibBuilder.loadTexts:
    juniNtpPeerFilterDispersion.setUnits("seconds")
_JuniNtpAccessGroup_ObjectIdentity = ObjectIdentity
juniNtpAccessGroup = _JuniNtpAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 5)
)
_JuniNtpRouterAccessGroupPeer_Type = DisplayString
_JuniNtpRouterAccessGroupPeer_Object = MibScalar
juniNtpRouterAccessGroupPeer = _JuniNtpRouterAccessGroupPeer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 5, 1),
    _JuniNtpRouterAccessGroupPeer_Type()
)
juniNtpRouterAccessGroupPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniNtpRouterAccessGroupPeer.setStatus("current")
_JuniNtpRouterAccessGroupServe_Type = DisplayString
_JuniNtpRouterAccessGroupServe_Object = MibScalar
juniNtpRouterAccessGroupServe = _JuniNtpRouterAccessGroupServe_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 5, 2),
    _JuniNtpRouterAccessGroupServe_Type()
)
juniNtpRouterAccessGroupServe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniNtpRouterAccessGroupServe.setStatus("current")
_JuniNtpRouterAccessGroupServeOnly_Type = DisplayString
_JuniNtpRouterAccessGroupServeOnly_Object = MibScalar
juniNtpRouterAccessGroupServeOnly = _JuniNtpRouterAccessGroupServeOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 5, 3),
    _JuniNtpRouterAccessGroupServeOnly_Type()
)
juniNtpRouterAccessGroupServeOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniNtpRouterAccessGroupServeOnly.setStatus("current")
_JuniNtpRouterAccessGroupQueryOnly_Type = DisplayString
_JuniNtpRouterAccessGroupQueryOnly_Object = MibScalar
juniNtpRouterAccessGroupQueryOnly = _JuniNtpRouterAccessGroupQueryOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 5, 4),
    _JuniNtpRouterAccessGroupQueryOnly_Type()
)
juniNtpRouterAccessGroupQueryOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniNtpRouterAccessGroupQueryOnly.setStatus("current")
_JuniSysClockConformance_ObjectIdentity = ObjectIdentity
juniSysClockConformance = _JuniSysClockConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3)
)
_JuniSysClockCompliances_ObjectIdentity = ObjectIdentity
juniSysClockCompliances = _JuniSysClockCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 1)
)
_JuniSysClockGroups_ObjectIdentity = ObjectIdentity
juniSysClockGroups = _JuniSysClockGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2)
)

# Managed Objects groups

juniSysClockTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 1)
)
juniSysClockTimeGroup.setObjects(
      *(("Juniper-System-Clock-MIB", "juniSysClockDateAndTime"),
        ("Juniper-System-Clock-MIB", "juniSysClockTimeZoneName"))
)
if mibBuilder.loadTexts:
    juniSysClockTimeGroup.setStatus("current")

juniSysClockDstGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 2)
)
juniSysClockDstGroup.setObjects(
      *(("Juniper-System-Clock-MIB", "juniSysClockDstName"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstOffset"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstStatus"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstAbsoluteStartTime"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstAbsoluteStopTime"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstRecurStartMonth"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstRecurStartWeek"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstRecurStartDay"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstRecurStartHour"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstRecurStartMinute"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstRecurStopMonth"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstRecurStopWeek"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstRecurStopDay"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstRecurStopHour"),
        ("Juniper-System-Clock-MIB", "juniSysClockDstRecurStopMinute"))
)
if mibBuilder.loadTexts:
    juniSysClockDstGroup.setStatus("current")

juniNtpSysClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 3)
)
juniNtpSysClockGroup.setObjects(
      *(("Juniper-System-Clock-MIB", "juniNtpSysClockState"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockOffsetError"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockFrequencyError"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockRootDelay"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockRootDispersion"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockStratumNumber"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockLastUpdateTime"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockLastUpdateServer"))
)
if mibBuilder.loadTexts:
    juniNtpSysClockGroup.setStatus("obsolete")

juniNtpClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 4)
)
juniNtpClientGroup.setObjects(
      *(("Juniper-System-Clock-MIB", "juniNtpClientAdminStatus"),
        ("Juniper-System-Clock-MIB", "juniNtpClientSystemRouterIndex"),
        ("Juniper-System-Clock-MIB", "juniNtpClientPacketSourceIfIndex"),
        ("Juniper-System-Clock-MIB", "juniNtpClientBroadcastDelay"),
        ("Juniper-System-Clock-MIB", "juniNtpClientIfDisable"),
        ("Juniper-System-Clock-MIB", "juniNtpClientIfIsBroadcastClient"))
)
if mibBuilder.loadTexts:
    juniNtpClientGroup.setStatus("current")

juniNtpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 5)
)
juniNtpServerGroup.setObjects(
      *(("Juniper-System-Clock-MIB", "juniNtpServerAdminStatus"),
        ("Juniper-System-Clock-MIB", "juniNtpServerStratumNumber"))
)
if mibBuilder.loadTexts:
    juniNtpServerGroup.setStatus("current")

juniNtpPeersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 6)
)
juniNtpPeersGroup.setObjects(
      *(("Juniper-System-Clock-MIB", "juniNtpPeerState"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerStratumNumber"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerAssociationMode"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerBroadcastInterval"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerPolledInterval"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerPollingInterval"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerDelay"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerDispersion"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerOffsetError"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerReachability"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerPrecision"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerRootDelay"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerRootDispersion"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerRootSyncDistance"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerRootTime"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerRootTimeUpdateServer"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerReceiveTime"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerTransmitTime"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerRequestTime"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerFilterOffset"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerFilterDelay"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerFilterDispersion"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerCfgNtpVersion"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerCfgPacketSourceIfIndex"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerCfgIsPreferred"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerCfgRowStatus"))
)
if mibBuilder.loadTexts:
    juniNtpPeersGroup.setStatus("obsolete")

juniNtpAccessGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 7)
)
juniNtpAccessGroupGroup.setObjects(
      *(("Juniper-System-Clock-MIB", "juniNtpRouterAccessGroupPeer"),
        ("Juniper-System-Clock-MIB", "juniNtpRouterAccessGroupServe"),
        ("Juniper-System-Clock-MIB", "juniNtpRouterAccessGroupServeOnly"),
        ("Juniper-System-Clock-MIB", "juniNtpRouterAccessGroupQueryOnly"))
)
if mibBuilder.loadTexts:
    juniNtpAccessGroupGroup.setStatus("current")

juniNtpSysClockGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 9)
)
juniNtpSysClockGroup2.setObjects(
      *(("Juniper-System-Clock-MIB", "juniNtpSysClockState"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockRootDelay"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockRootDispersion"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockStratumNumber"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockLastUpdateTime"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockLastUpdateServer"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockOffsetErrorNew"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockFrequencyErrorNew"))
)
if mibBuilder.loadTexts:
    juniNtpSysClockGroup2.setStatus("current")

juniNtpSysClockDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 10)
)
juniNtpSysClockDeprecatedGroup.setObjects(
      *(("Juniper-System-Clock-MIB", "juniNtpSysClockOffsetError"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockFrequencyError"))
)
if mibBuilder.loadTexts:
    juniNtpSysClockDeprecatedGroup.setStatus("deprecated")

juniNtpPeersGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 11)
)
juniNtpPeersGroup1.setObjects(
      *(("Juniper-System-Clock-MIB", "juniNtpPeerState"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerStratumNumber"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerAssociationMode"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerBroadcastInterval"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerPolledInterval"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerPollingInterval"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerDelay"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerDispersion"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerOffsetError"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerReachability"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerPrecision"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerRootDelay"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerRootDispersion"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerRootSyncDistance"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerRootTime"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerRootTimeUpdateServer"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerReceiveTime"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerTransmitTime"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerRequestTime"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerFilterOffset"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerFilterDelay"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerFilterDispersion"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerCfgNtpVersion"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerCfgPacketSourceIfIndex"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerCfgIsPreferred"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerCfgRowStatus"),
        ("Juniper-System-Clock-MIB", "juniNtpPeerLastUpdateTime"))
)
if mibBuilder.loadTexts:
    juniNtpPeersGroup1.setStatus("current")


# Notification objects

juniNtpFrequencyCalibrationStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 0, 1)
)
juniNtpFrequencyCalibrationStart.setObjects(
    ("Juniper-System-Clock-MIB", "juniNtpSysClockFrequencyError")
)
if mibBuilder.loadTexts:
    juniNtpFrequencyCalibrationStart.setStatus(
        "current"
    )

juniNtpFrequencyCalibrationEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 0, 2)
)
juniNtpFrequencyCalibrationEnd.setObjects(
    ("Juniper-System-Clock-MIB", "juniNtpSysClockFrequencyError")
)
if mibBuilder.loadTexts:
    juniNtpFrequencyCalibrationEnd.setStatus(
        "current"
    )

juniNtpTimeSynUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 0, 3)
)
if mibBuilder.loadTexts:
    juniNtpTimeSynUp.setStatus(
        "current"
    )

juniNtpTimeSynDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 0, 4)
)
if mibBuilder.loadTexts:
    juniNtpTimeSynDown.setStatus(
        "current"
    )

juniNtpTimeServerSynUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 0, 5)
)
juniNtpTimeServerSynUp.setObjects(
    ("Juniper-System-Clock-MIB", "juniNtpPeerCfgIsPreferred")
)
if mibBuilder.loadTexts:
    juniNtpTimeServerSynUp.setStatus(
        "current"
    )

juniNtpTimeServerSynDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 0, 6)
)
juniNtpTimeServerSynDown.setObjects(
    ("Juniper-System-Clock-MIB", "juniNtpPeerCfgIsPreferred")
)
if mibBuilder.loadTexts:
    juniNtpTimeServerSynDown.setStatus(
        "current"
    )

juniNtpFirstSystemClockSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 0, 7)
)
juniNtpFirstSystemClockSet.setObjects(
      *(("Juniper-System-Clock-MIB", "juniNtpSysClockOffsetError"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockState"))
)
if mibBuilder.loadTexts:
    juniNtpFirstSystemClockSet.setStatus(
        "current"
    )

juniNtpClockOffSetLimitCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 0, 8)
)
juniNtpClockOffSetLimitCrossed.setObjects(
      *(("Juniper-System-Clock-MIB", "juniNtpSysClockOffsetError"),
        ("Juniper-System-Clock-MIB", "juniNtpSysClockState"))
)
if mibBuilder.loadTexts:
    juniNtpClockOffSetLimitCrossed.setStatus(
        "current"
    )


# Notifications groups

juniNtpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 8)
)
juniNtpNotificationGroup.setObjects(
      *(("Juniper-System-Clock-MIB", "juniNtpFrequencyCalibrationStart"),
        ("Juniper-System-Clock-MIB", "juniNtpFrequencyCalibrationEnd"),
        ("Juniper-System-Clock-MIB", "juniNtpTimeSynUp"),
        ("Juniper-System-Clock-MIB", "juniNtpTimeSynDown"),
        ("Juniper-System-Clock-MIB", "juniNtpTimeServerSynUp"),
        ("Juniper-System-Clock-MIB", "juniNtpTimeServerSynDown"),
        ("Juniper-System-Clock-MIB", "juniNtpFirstSystemClockSet"),
        ("Juniper-System-Clock-MIB", "juniNtpClockOffSetLimitCrossed"))
)
if mibBuilder.loadTexts:
    juniNtpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniSysClockCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 1, 1)
)
if mibBuilder.loadTexts:
    juniSysClockCompliance.setStatus(
        "obsolete"
    )

juniSysClockCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 1, 2)
)
if mibBuilder.loadTexts:
    juniSysClockCompliance2.setStatus(
        "obsolete"
    )

juniSysClockCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 1, 3)
)
if mibBuilder.loadTexts:
    juniSysClockCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-System-Clock-MIB",
    **{"JuniSysClockMonth": JuniSysClockMonth,
       "JuniSysClockWeekOfTheMonth": JuniSysClockWeekOfTheMonth,
       "JuniSysClockDayOfTheWeek": JuniSysClockDayOfTheWeek,
       "JuniSysClockHour": JuniSysClockHour,
       "JuniSysClockMinute": JuniSysClockMinute,
       "JuniNtpTimeStamp": JuniNtpTimeStamp,
       "JuniNtpClockSignedTime": JuniNtpClockSignedTime,
       "JuniNtpClockUnsignedTime": JuniNtpClockUnsignedTime,
       "juniSysClockMIB": juniSysClockMIB,
       "juniSysClockObjects": juniSysClockObjects,
       "juniSysClockTime": juniSysClockTime,
       "juniSysClockDateAndTime": juniSysClockDateAndTime,
       "juniSysClockTimeZoneName": juniSysClockTimeZoneName,
       "juniSysClockDst": juniSysClockDst,
       "juniSysClockDstName": juniSysClockDstName,
       "juniSysClockDstOffset": juniSysClockDstOffset,
       "juniSysClockDstStatus": juniSysClockDstStatus,
       "juniSysClockDstAbsoluteStartTime": juniSysClockDstAbsoluteStartTime,
       "juniSysClockDstAbsoluteStopTime": juniSysClockDstAbsoluteStopTime,
       "juniSysClockDstRecurStartMonth": juniSysClockDstRecurStartMonth,
       "juniSysClockDstRecurStartWeek": juniSysClockDstRecurStartWeek,
       "juniSysClockDstRecurStartDay": juniSysClockDstRecurStartDay,
       "juniSysClockDstRecurStartHour": juniSysClockDstRecurStartHour,
       "juniSysClockDstRecurStartMinute": juniSysClockDstRecurStartMinute,
       "juniSysClockDstRecurStopMonth": juniSysClockDstRecurStopMonth,
       "juniSysClockDstRecurStopWeek": juniSysClockDstRecurStopWeek,
       "juniSysClockDstRecurStopDay": juniSysClockDstRecurStopDay,
       "juniSysClockDstRecurStopHour": juniSysClockDstRecurStopHour,
       "juniSysClockDstRecurStopMinute": juniSysClockDstRecurStopMinute,
       "juniNtpObjects": juniNtpObjects,
       "juniNtpTraps": juniNtpTraps,
       "juniNtpFrequencyCalibrationStart": juniNtpFrequencyCalibrationStart,
       "juniNtpFrequencyCalibrationEnd": juniNtpFrequencyCalibrationEnd,
       "juniNtpTimeSynUp": juniNtpTimeSynUp,
       "juniNtpTimeSynDown": juniNtpTimeSynDown,
       "juniNtpTimeServerSynUp": juniNtpTimeServerSynUp,
       "juniNtpTimeServerSynDown": juniNtpTimeServerSynDown,
       "juniNtpFirstSystemClockSet": juniNtpFirstSystemClockSet,
       "juniNtpClockOffSetLimitCrossed": juniNtpClockOffSetLimitCrossed,
       "juniNtpSysClock": juniNtpSysClock,
       "juniNtpSysClockState": juniNtpSysClockState,
       "juniNtpSysClockOffsetError": juniNtpSysClockOffsetError,
       "juniNtpSysClockFrequencyError": juniNtpSysClockFrequencyError,
       "juniNtpSysClockRootDelay": juniNtpSysClockRootDelay,
       "juniNtpSysClockRootDispersion": juniNtpSysClockRootDispersion,
       "juniNtpSysClockStratumNumber": juniNtpSysClockStratumNumber,
       "juniNtpSysClockLastUpdateTime": juniNtpSysClockLastUpdateTime,
       "juniNtpSysClockLastUpdateServer": juniNtpSysClockLastUpdateServer,
       "juniNtpSysClockOffsetErrorNew": juniNtpSysClockOffsetErrorNew,
       "juniNtpSysClockFrequencyErrorNew": juniNtpSysClockFrequencyErrorNew,
       "juniNtpClient": juniNtpClient,
       "juniNtpClientAdminStatus": juniNtpClientAdminStatus,
       "juniNtpClientSystemRouterIndex": juniNtpClientSystemRouterIndex,
       "juniNtpClientPacketSourceIfIndex": juniNtpClientPacketSourceIfIndex,
       "juniNtpClientBroadcastDelay": juniNtpClientBroadcastDelay,
       "juniNtpClientIfTable": juniNtpClientIfTable,
       "juniNtpClientIfEntry": juniNtpClientIfEntry,
       "juniNtpClientIfRouterIndex": juniNtpClientIfRouterIndex,
       "juniNtpClientIfIfIndex": juniNtpClientIfIfIndex,
       "juniNtpClientIfDisable": juniNtpClientIfDisable,
       "juniNtpClientIfIsBroadcastClient": juniNtpClientIfIsBroadcastClient,
       "juniNtpClientIfIsBroadcastServer": juniNtpClientIfIsBroadcastServer,
       "juniNtpClientIfIsBroadcastServerVersion": juniNtpClientIfIsBroadcastServerVersion,
       "juniNtpClientIfIsBroadcastServerDelay": juniNtpClientIfIsBroadcastServerDelay,
       "juniNtpServer": juniNtpServer,
       "juniNtpServerStratumNumber": juniNtpServerStratumNumber,
       "juniNtpServerAdminStatus": juniNtpServerAdminStatus,
       "juniNtpPeers": juniNtpPeers,
       "juniNtpPeerCfgTable": juniNtpPeerCfgTable,
       "juniNtpPeerCfgEntry": juniNtpPeerCfgEntry,
       "juniNtpPeerCfgIpAddress": juniNtpPeerCfgIpAddress,
       "juniNtpPeerCfgNtpVersion": juniNtpPeerCfgNtpVersion,
       "juniNtpPeerCfgPacketSourceIfIndex": juniNtpPeerCfgPacketSourceIfIndex,
       "juniNtpPeerCfgIsPreferred": juniNtpPeerCfgIsPreferred,
       "juniNtpPeerCfgRowStatus": juniNtpPeerCfgRowStatus,
       "juniNtpPeerTable": juniNtpPeerTable,
       "juniNtpPeerEntry": juniNtpPeerEntry,
       "juniNtpPeerState": juniNtpPeerState,
       "juniNtpPeerStratumNumber": juniNtpPeerStratumNumber,
       "juniNtpPeerAssociationMode": juniNtpPeerAssociationMode,
       "juniNtpPeerBroadcastInterval": juniNtpPeerBroadcastInterval,
       "juniNtpPeerPolledInterval": juniNtpPeerPolledInterval,
       "juniNtpPeerPollingInterval": juniNtpPeerPollingInterval,
       "juniNtpPeerDelay": juniNtpPeerDelay,
       "juniNtpPeerDispersion": juniNtpPeerDispersion,
       "juniNtpPeerOffsetError": juniNtpPeerOffsetError,
       "juniNtpPeerReachability": juniNtpPeerReachability,
       "juniNtpPeerRootDelay": juniNtpPeerRootDelay,
       "juniNtpPeerRootDispersion": juniNtpPeerRootDispersion,
       "juniNtpPeerRootSyncDistance": juniNtpPeerRootSyncDistance,
       "juniNtpPeerRootTime": juniNtpPeerRootTime,
       "juniNtpPeerRootTimeUpdateServer": juniNtpPeerRootTimeUpdateServer,
       "juniNtpPeerReceiveTime": juniNtpPeerReceiveTime,
       "juniNtpPeerTransmitTime": juniNtpPeerTransmitTime,
       "juniNtpPeerRequestTime": juniNtpPeerRequestTime,
       "juniNtpPeerPrecision": juniNtpPeerPrecision,
       "juniNtpPeerLastUpdateTime": juniNtpPeerLastUpdateTime,
       "juniNtpPeerFilterRegisterTable": juniNtpPeerFilterRegisterTable,
       "juniNtpPeerFilterRegisterEntry": juniNtpPeerFilterRegisterEntry,
       "juniNtpPeerFilterIndex": juniNtpPeerFilterIndex,
       "juniNtpPeerFilterOffset": juniNtpPeerFilterOffset,
       "juniNtpPeerFilterDelay": juniNtpPeerFilterDelay,
       "juniNtpPeerFilterDispersion": juniNtpPeerFilterDispersion,
       "juniNtpAccessGroup": juniNtpAccessGroup,
       "juniNtpRouterAccessGroupPeer": juniNtpRouterAccessGroupPeer,
       "juniNtpRouterAccessGroupServe": juniNtpRouterAccessGroupServe,
       "juniNtpRouterAccessGroupServeOnly": juniNtpRouterAccessGroupServeOnly,
       "juniNtpRouterAccessGroupQueryOnly": juniNtpRouterAccessGroupQueryOnly,
       "juniSysClockConformance": juniSysClockConformance,
       "juniSysClockCompliances": juniSysClockCompliances,
       "juniSysClockCompliance": juniSysClockCompliance,
       "juniSysClockCompliance2": juniSysClockCompliance2,
       "juniSysClockCompliance3": juniSysClockCompliance3,
       "juniSysClockGroups": juniSysClockGroups,
       "juniSysClockTimeGroup": juniSysClockTimeGroup,
       "juniSysClockDstGroup": juniSysClockDstGroup,
       "juniNtpSysClockGroup": juniNtpSysClockGroup,
       "juniNtpClientGroup": juniNtpClientGroup,
       "juniNtpServerGroup": juniNtpServerGroup,
       "juniNtpPeersGroup": juniNtpPeersGroup,
       "juniNtpAccessGroupGroup": juniNtpAccessGroupGroup,
       "juniNtpNotificationGroup": juniNtpNotificationGroup,
       "juniNtpSysClockGroup2": juniNtpSysClockGroup2,
       "juniNtpSysClockDeprecatedGroup": juniNtpSysClockDeprecatedGroup,
       "juniNtpPeersGroup1": juniNtpPeersGroup1}
)
