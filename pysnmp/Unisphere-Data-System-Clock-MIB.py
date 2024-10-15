# SNMP MIB module (Unisphere-Data-System-Clock-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-System-Clock-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:44 2024
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable")


# MODULE-IDENTITY

usdSysClockMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56)
)
usdSysClockMIB.setRevisions(
        ("2002-04-04 14:56",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdSysClockMonth(Integer32, TextualConvention):
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



class UsdSysClockWeekOfTheMonth(Integer32, TextualConvention):
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



class UsdSysClockDayOfTheWeek(Integer32, TextualConvention):
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



class UsdSysClockHour(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )



class UsdSysClockMinute(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )



class UsdNtpTimeStamp(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )



class UsdNtpClockSignedTime(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )



class UsdNtpClockUnsignedTime(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )



# MIB Managed Objects in the order of their OIDs

_UsdSysClockObjects_ObjectIdentity = ObjectIdentity
usdSysClockObjects = _UsdSysClockObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1)
)
_UsdSysClockTime_ObjectIdentity = ObjectIdentity
usdSysClockTime = _UsdSysClockTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 1)
)
_UsdSysClockDateAndTime_Type = DateAndTime
_UsdSysClockDateAndTime_Object = MibScalar
usdSysClockDateAndTime = _UsdSysClockDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 1, 1),
    _UsdSysClockDateAndTime_Type()
)
usdSysClockDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDateAndTime.setStatus("current")


class _UsdSysClockTimeZoneName_Type(DisplayString):
    """Custom type usdSysClockTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UsdSysClockTimeZoneName_Type.__name__ = "DisplayString"
_UsdSysClockTimeZoneName_Object = MibScalar
usdSysClockTimeZoneName = _UsdSysClockTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 1, 2),
    _UsdSysClockTimeZoneName_Type()
)
usdSysClockTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockTimeZoneName.setStatus("current")
_UsdSysClockDst_ObjectIdentity = ObjectIdentity
usdSysClockDst = _UsdSysClockDst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2)
)


class _UsdSysClockDstName_Type(DisplayString):
    """Custom type usdSysClockDstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UsdSysClockDstName_Type.__name__ = "DisplayString"
_UsdSysClockDstName_Object = MibScalar
usdSysClockDstName = _UsdSysClockDstName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 1),
    _UsdSysClockDstName_Type()
)
usdSysClockDstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstName.setStatus("current")


class _UsdSysClockDstOffset_Type(Integer32):
    """Custom type usdSysClockDstOffset based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_UsdSysClockDstOffset_Type.__name__ = "Integer32"
_UsdSysClockDstOffset_Object = MibScalar
usdSysClockDstOffset = _UsdSysClockDstOffset_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 2),
    _UsdSysClockDstOffset_Type()
)
usdSysClockDstOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstOffset.setStatus("current")
if mibBuilder.loadTexts:
    usdSysClockDstOffset.setUnits("minutes")


class _UsdSysClockDstStatus_Type(Integer32):
    """Custom type usdSysClockDstStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 2),
          ("off", 0),
          ("recurrent", 1))
    )


_UsdSysClockDstStatus_Type.__name__ = "Integer32"
_UsdSysClockDstStatus_Object = MibScalar
usdSysClockDstStatus = _UsdSysClockDstStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 3),
    _UsdSysClockDstStatus_Type()
)
usdSysClockDstStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstStatus.setStatus("current")
_UsdSysClockDstAbsoluteStartTime_Type = DateAndTime
_UsdSysClockDstAbsoluteStartTime_Object = MibScalar
usdSysClockDstAbsoluteStartTime = _UsdSysClockDstAbsoluteStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 4),
    _UsdSysClockDstAbsoluteStartTime_Type()
)
usdSysClockDstAbsoluteStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstAbsoluteStartTime.setStatus("current")
_UsdSysClockDstAbsoluteStopTime_Type = DateAndTime
_UsdSysClockDstAbsoluteStopTime_Object = MibScalar
usdSysClockDstAbsoluteStopTime = _UsdSysClockDstAbsoluteStopTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 5),
    _UsdSysClockDstAbsoluteStopTime_Type()
)
usdSysClockDstAbsoluteStopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstAbsoluteStopTime.setStatus("current")


class _UsdSysClockDstRecurStartMonth_Type(UsdSysClockMonth):
    """Custom type usdSysClockDstRecurStartMonth based on UsdSysClockMonth"""


_UsdSysClockDstRecurStartMonth_Object = MibScalar
usdSysClockDstRecurStartMonth = _UsdSysClockDstRecurStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 6),
    _UsdSysClockDstRecurStartMonth_Type()
)
usdSysClockDstRecurStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstRecurStartMonth.setStatus("current")


class _UsdSysClockDstRecurStartWeek_Type(UsdSysClockWeekOfTheMonth):
    """Custom type usdSysClockDstRecurStartWeek based on UsdSysClockWeekOfTheMonth"""


_UsdSysClockDstRecurStartWeek_Object = MibScalar
usdSysClockDstRecurStartWeek = _UsdSysClockDstRecurStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 7),
    _UsdSysClockDstRecurStartWeek_Type()
)
usdSysClockDstRecurStartWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstRecurStartWeek.setStatus("current")


class _UsdSysClockDstRecurStartDay_Type(UsdSysClockDayOfTheWeek):
    """Custom type usdSysClockDstRecurStartDay based on UsdSysClockDayOfTheWeek"""


_UsdSysClockDstRecurStartDay_Object = MibScalar
usdSysClockDstRecurStartDay = _UsdSysClockDstRecurStartDay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 8),
    _UsdSysClockDstRecurStartDay_Type()
)
usdSysClockDstRecurStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstRecurStartDay.setStatus("current")


class _UsdSysClockDstRecurStartHour_Type(UsdSysClockHour):
    """Custom type usdSysClockDstRecurStartHour based on UsdSysClockHour"""
    defaultValue = 1


_UsdSysClockDstRecurStartHour_Object = MibScalar
usdSysClockDstRecurStartHour = _UsdSysClockDstRecurStartHour_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 9),
    _UsdSysClockDstRecurStartHour_Type()
)
usdSysClockDstRecurStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstRecurStartHour.setStatus("current")


class _UsdSysClockDstRecurStartMinute_Type(UsdSysClockMinute):
    """Custom type usdSysClockDstRecurStartMinute based on UsdSysClockMinute"""
    defaultValue = 0


_UsdSysClockDstRecurStartMinute_Object = MibScalar
usdSysClockDstRecurStartMinute = _UsdSysClockDstRecurStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 10),
    _UsdSysClockDstRecurStartMinute_Type()
)
usdSysClockDstRecurStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstRecurStartMinute.setStatus("current")


class _UsdSysClockDstRecurStopMonth_Type(UsdSysClockMonth):
    """Custom type usdSysClockDstRecurStopMonth based on UsdSysClockMonth"""


_UsdSysClockDstRecurStopMonth_Object = MibScalar
usdSysClockDstRecurStopMonth = _UsdSysClockDstRecurStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 11),
    _UsdSysClockDstRecurStopMonth_Type()
)
usdSysClockDstRecurStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstRecurStopMonth.setStatus("current")


class _UsdSysClockDstRecurStopWeek_Type(UsdSysClockWeekOfTheMonth):
    """Custom type usdSysClockDstRecurStopWeek based on UsdSysClockWeekOfTheMonth"""


_UsdSysClockDstRecurStopWeek_Object = MibScalar
usdSysClockDstRecurStopWeek = _UsdSysClockDstRecurStopWeek_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 12),
    _UsdSysClockDstRecurStopWeek_Type()
)
usdSysClockDstRecurStopWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstRecurStopWeek.setStatus("current")


class _UsdSysClockDstRecurStopDay_Type(UsdSysClockDayOfTheWeek):
    """Custom type usdSysClockDstRecurStopDay based on UsdSysClockDayOfTheWeek"""


_UsdSysClockDstRecurStopDay_Object = MibScalar
usdSysClockDstRecurStopDay = _UsdSysClockDstRecurStopDay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 13),
    _UsdSysClockDstRecurStopDay_Type()
)
usdSysClockDstRecurStopDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstRecurStopDay.setStatus("current")


class _UsdSysClockDstRecurStopHour_Type(UsdSysClockHour):
    """Custom type usdSysClockDstRecurStopHour based on UsdSysClockHour"""
    defaultValue = 2


_UsdSysClockDstRecurStopHour_Object = MibScalar
usdSysClockDstRecurStopHour = _UsdSysClockDstRecurStopHour_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 14),
    _UsdSysClockDstRecurStopHour_Type()
)
usdSysClockDstRecurStopHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstRecurStopHour.setStatus("current")


class _UsdSysClockDstRecurStopMinute_Type(UsdSysClockMinute):
    """Custom type usdSysClockDstRecurStopMinute based on UsdSysClockMinute"""
    defaultValue = 0


_UsdSysClockDstRecurStopMinute_Object = MibScalar
usdSysClockDstRecurStopMinute = _UsdSysClockDstRecurStopMinute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 1, 2, 15),
    _UsdSysClockDstRecurStopMinute_Type()
)
usdSysClockDstRecurStopMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSysClockDstRecurStopMinute.setStatus("current")
_UsdNtpObjects_ObjectIdentity = ObjectIdentity
usdNtpObjects = _UsdNtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2)
)
_UsdNtpSysClock_ObjectIdentity = ObjectIdentity
usdNtpSysClock = _UsdNtpSysClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1)
)


class _UsdNtpSysClockState_Type(Integer32):
    """Custom type usdNtpSysClockState based on Integer32"""
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


_UsdNtpSysClockState_Type.__name__ = "Integer32"
_UsdNtpSysClockState_Object = MibScalar
usdNtpSysClockState = _UsdNtpSysClockState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 1),
    _UsdNtpSysClockState_Type()
)
usdNtpSysClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpSysClockState.setStatus("current")
_UsdNtpSysClockOffsetError_Type = UsdNtpClockSignedTime
_UsdNtpSysClockOffsetError_Object = MibScalar
usdNtpSysClockOffsetError = _UsdNtpSysClockOffsetError_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 2),
    _UsdNtpSysClockOffsetError_Type()
)
usdNtpSysClockOffsetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpSysClockOffsetError.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpSysClockOffsetError.setUnits("seconds")
_UsdNtpSysClockFrequencyError_Type = Integer32
_UsdNtpSysClockFrequencyError_Object = MibScalar
usdNtpSysClockFrequencyError = _UsdNtpSysClockFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 3),
    _UsdNtpSysClockFrequencyError_Type()
)
usdNtpSysClockFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpSysClockFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpSysClockFrequencyError.setUnits("ppm")
_UsdNtpSysClockRootDelay_Type = UsdNtpClockSignedTime
_UsdNtpSysClockRootDelay_Object = MibScalar
usdNtpSysClockRootDelay = _UsdNtpSysClockRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 4),
    _UsdNtpSysClockRootDelay_Type()
)
usdNtpSysClockRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpSysClockRootDelay.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpSysClockRootDelay.setUnits("seconds")
_UsdNtpSysClockRootDispersion_Type = UsdNtpClockUnsignedTime
_UsdNtpSysClockRootDispersion_Object = MibScalar
usdNtpSysClockRootDispersion = _UsdNtpSysClockRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 5),
    _UsdNtpSysClockRootDispersion_Type()
)
usdNtpSysClockRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpSysClockRootDispersion.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpSysClockRootDispersion.setUnits("seconds")


class _UsdNtpSysClockStratumNumber_Type(Integer32):
    """Custom type usdNtpSysClockStratumNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdNtpSysClockStratumNumber_Type.__name__ = "Integer32"
_UsdNtpSysClockStratumNumber_Object = MibScalar
usdNtpSysClockStratumNumber = _UsdNtpSysClockStratumNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 6),
    _UsdNtpSysClockStratumNumber_Type()
)
usdNtpSysClockStratumNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpSysClockStratumNumber.setStatus("current")
_UsdNtpSysClockLastUpdateTime_Type = UsdNtpTimeStamp
_UsdNtpSysClockLastUpdateTime_Object = MibScalar
usdNtpSysClockLastUpdateTime = _UsdNtpSysClockLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 7),
    _UsdNtpSysClockLastUpdateTime_Type()
)
usdNtpSysClockLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpSysClockLastUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpSysClockLastUpdateTime.setUnits("seconds")
_UsdNtpSysClockLastUpdateServer_Type = IpAddress
_UsdNtpSysClockLastUpdateServer_Object = MibScalar
usdNtpSysClockLastUpdateServer = _UsdNtpSysClockLastUpdateServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 1, 8),
    _UsdNtpSysClockLastUpdateServer_Type()
)
usdNtpSysClockLastUpdateServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpSysClockLastUpdateServer.setStatus("current")
_UsdNtpClient_ObjectIdentity = ObjectIdentity
usdNtpClient = _UsdNtpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2)
)


class _UsdNtpClientAdminStatus_Type(UsdEnable):
    """Custom type usdNtpClientAdminStatus based on UsdEnable"""


_UsdNtpClientAdminStatus_Object = MibScalar
usdNtpClientAdminStatus = _UsdNtpClientAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 1),
    _UsdNtpClientAdminStatus_Type()
)
usdNtpClientAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdNtpClientAdminStatus.setStatus("current")
_UsdNtpClientSystemRouterIndex_Type = Unsigned32
_UsdNtpClientSystemRouterIndex_Object = MibScalar
usdNtpClientSystemRouterIndex = _UsdNtpClientSystemRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 2),
    _UsdNtpClientSystemRouterIndex_Type()
)
usdNtpClientSystemRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpClientSystemRouterIndex.setStatus("current")


class _UsdNtpClientPacketSourceIfIndex_Type(Integer32):
    """Custom type usdNtpClientPacketSourceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdNtpClientPacketSourceIfIndex_Type.__name__ = "Integer32"
_UsdNtpClientPacketSourceIfIndex_Object = MibScalar
usdNtpClientPacketSourceIfIndex = _UsdNtpClientPacketSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 3),
    _UsdNtpClientPacketSourceIfIndex_Type()
)
usdNtpClientPacketSourceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdNtpClientPacketSourceIfIndex.setStatus("current")


class _UsdNtpClientBroadcastDelay_Type(Integer32):
    """Custom type usdNtpClientBroadcastDelay based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_UsdNtpClientBroadcastDelay_Type.__name__ = "Integer32"
_UsdNtpClientBroadcastDelay_Object = MibScalar
usdNtpClientBroadcastDelay = _UsdNtpClientBroadcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 4),
    _UsdNtpClientBroadcastDelay_Type()
)
usdNtpClientBroadcastDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdNtpClientBroadcastDelay.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpClientBroadcastDelay.setUnits("microseconds")
_UsdNtpClientIfTable_Object = MibTable
usdNtpClientIfTable = _UsdNtpClientIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5)
)
if mibBuilder.loadTexts:
    usdNtpClientIfTable.setStatus("current")
_UsdNtpClientIfEntry_Object = MibTableRow
usdNtpClientIfEntry = _UsdNtpClientIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1)
)
usdNtpClientIfEntry.setIndexNames(
    (0, "Unisphere-Data-System-Clock-MIB", "usdNtpClientIfRouterIndex"),
    (0, "Unisphere-Data-System-Clock-MIB", "usdNtpClientIfIfIndex"),
)
if mibBuilder.loadTexts:
    usdNtpClientIfEntry.setStatus("current")
_UsdNtpClientIfRouterIndex_Type = Unsigned32
_UsdNtpClientIfRouterIndex_Object = MibTableColumn
usdNtpClientIfRouterIndex = _UsdNtpClientIfRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1, 1),
    _UsdNtpClientIfRouterIndex_Type()
)
usdNtpClientIfRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdNtpClientIfRouterIndex.setStatus("current")


class _UsdNtpClientIfIfIndex_Type(Integer32):
    """Custom type usdNtpClientIfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdNtpClientIfIfIndex_Type.__name__ = "Integer32"
_UsdNtpClientIfIfIndex_Object = MibTableColumn
usdNtpClientIfIfIndex = _UsdNtpClientIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1, 2),
    _UsdNtpClientIfIfIndex_Type()
)
usdNtpClientIfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdNtpClientIfIfIndex.setStatus("current")
_UsdNtpClientIfStatus_Type = TruthValue
_UsdNtpClientIfStatus_Object = MibTableColumn
usdNtpClientIfStatus = _UsdNtpClientIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1, 3),
    _UsdNtpClientIfStatus_Type()
)
usdNtpClientIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNtpClientIfStatus.setStatus("current")
_UsdNtpClientIfIsBroadcastClient_Type = TruthValue
_UsdNtpClientIfIsBroadcastClient_Object = MibTableColumn
usdNtpClientIfIsBroadcastClient = _UsdNtpClientIfIsBroadcastClient_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 2, 5, 1, 4),
    _UsdNtpClientIfIsBroadcastClient_Type()
)
usdNtpClientIfIsBroadcastClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNtpClientIfIsBroadcastClient.setStatus("current")
_UsdNtpServer_ObjectIdentity = ObjectIdentity
usdNtpServer = _UsdNtpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 3)
)


class _UsdNtpServerStratumNumber_Type(Integer32):
    """Custom type usdNtpServerStratumNumber based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdNtpServerStratumNumber_Type.__name__ = "Integer32"
_UsdNtpServerStratumNumber_Object = MibScalar
usdNtpServerStratumNumber = _UsdNtpServerStratumNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 3, 1),
    _UsdNtpServerStratumNumber_Type()
)
usdNtpServerStratumNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdNtpServerStratumNumber.setStatus("current")
_UsdNtpServerAdminStatus_Type = UsdEnable
_UsdNtpServerAdminStatus_Object = MibScalar
usdNtpServerAdminStatus = _UsdNtpServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 3, 2),
    _UsdNtpServerAdminStatus_Type()
)
usdNtpServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdNtpServerAdminStatus.setStatus("current")
_UsdNtpPeers_ObjectIdentity = ObjectIdentity
usdNtpPeers = _UsdNtpPeers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4)
)
_UsdNtpPeerCfgTable_Object = MibTable
usdNtpPeerCfgTable = _UsdNtpPeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1)
)
if mibBuilder.loadTexts:
    usdNtpPeerCfgTable.setStatus("current")
_UsdNtpPeerCfgEntry_Object = MibTableRow
usdNtpPeerCfgEntry = _UsdNtpPeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1, 1)
)
usdNtpPeerCfgEntry.setIndexNames(
    (0, "Unisphere-Data-System-Clock-MIB", "usdNtpClientIfRouterIndex"),
    (0, "Unisphere-Data-System-Clock-MIB", "usdNtpPeerCfgIpAddress"),
)
if mibBuilder.loadTexts:
    usdNtpPeerCfgEntry.setStatus("current")
_UsdNtpPeerCfgIpAddress_Type = IpAddress
_UsdNtpPeerCfgIpAddress_Object = MibTableColumn
usdNtpPeerCfgIpAddress = _UsdNtpPeerCfgIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1, 1, 1),
    _UsdNtpPeerCfgIpAddress_Type()
)
usdNtpPeerCfgIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdNtpPeerCfgIpAddress.setStatus("current")


class _UsdNtpPeerCfgNtpVersion_Type(Integer32):
    """Custom type usdNtpPeerCfgNtpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_UsdNtpPeerCfgNtpVersion_Type.__name__ = "Integer32"
_UsdNtpPeerCfgNtpVersion_Object = MibTableColumn
usdNtpPeerCfgNtpVersion = _UsdNtpPeerCfgNtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1, 1, 2),
    _UsdNtpPeerCfgNtpVersion_Type()
)
usdNtpPeerCfgNtpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNtpPeerCfgNtpVersion.setStatus("current")


class _UsdNtpPeerCfgPacketSourceIfIndex_Type(Integer32):
    """Custom type usdNtpPeerCfgPacketSourceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdNtpPeerCfgPacketSourceIfIndex_Type.__name__ = "Integer32"
_UsdNtpPeerCfgPacketSourceIfIndex_Object = MibTableColumn
usdNtpPeerCfgPacketSourceIfIndex = _UsdNtpPeerCfgPacketSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1, 1, 3),
    _UsdNtpPeerCfgPacketSourceIfIndex_Type()
)
usdNtpPeerCfgPacketSourceIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNtpPeerCfgPacketSourceIfIndex.setStatus("current")
_UsdNtpPeerCfgIsPreferred_Type = TruthValue
_UsdNtpPeerCfgIsPreferred_Object = MibTableColumn
usdNtpPeerCfgIsPreferred = _UsdNtpPeerCfgIsPreferred_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1, 1, 4),
    _UsdNtpPeerCfgIsPreferred_Type()
)
usdNtpPeerCfgIsPreferred.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNtpPeerCfgIsPreferred.setStatus("current")
_UsdNtpPeerCfgRowStatus_Type = RowStatus
_UsdNtpPeerCfgRowStatus_Object = MibTableColumn
usdNtpPeerCfgRowStatus = _UsdNtpPeerCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 1, 1, 5),
    _UsdNtpPeerCfgRowStatus_Type()
)
usdNtpPeerCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNtpPeerCfgRowStatus.setStatus("current")
_UsdNtpPeerTable_Object = MibTable
usdNtpPeerTable = _UsdNtpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2)
)
if mibBuilder.loadTexts:
    usdNtpPeerTable.setStatus("current")
_UsdNtpPeerEntry_Object = MibTableRow
usdNtpPeerEntry = _UsdNtpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1)
)
usdNtpPeerEntry.setIndexNames(
    (0, "Unisphere-Data-System-Clock-MIB", "usdNtpClientIfRouterIndex"),
    (0, "Unisphere-Data-System-Clock-MIB", "usdNtpPeerCfgIpAddress"),
)
if mibBuilder.loadTexts:
    usdNtpPeerEntry.setStatus("current")


class _UsdNtpPeerState_Type(OctetString):
    """Custom type usdNtpPeerState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_UsdNtpPeerState_Type.__name__ = "OctetString"
_UsdNtpPeerState_Object = MibTableColumn
usdNtpPeerState = _UsdNtpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 1),
    _UsdNtpPeerState_Type()
)
usdNtpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerState.setStatus("current")


class _UsdNtpPeerStratumNumber_Type(Integer32):
    """Custom type usdNtpPeerStratumNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdNtpPeerStratumNumber_Type.__name__ = "Integer32"
_UsdNtpPeerStratumNumber_Object = MibTableColumn
usdNtpPeerStratumNumber = _UsdNtpPeerStratumNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 2),
    _UsdNtpPeerStratumNumber_Type()
)
usdNtpPeerStratumNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerStratumNumber.setStatus("current")


class _UsdNtpPeerAssociationMode_Type(Integer32):
    """Custom type usdNtpPeerAssociationMode based on Integer32"""
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


_UsdNtpPeerAssociationMode_Type.__name__ = "Integer32"
_UsdNtpPeerAssociationMode_Object = MibTableColumn
usdNtpPeerAssociationMode = _UsdNtpPeerAssociationMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 3),
    _UsdNtpPeerAssociationMode_Type()
)
usdNtpPeerAssociationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerAssociationMode.setStatus("current")
_UsdNtpPeerBroadcastInterval_Type = Integer32
_UsdNtpPeerBroadcastInterval_Object = MibTableColumn
usdNtpPeerBroadcastInterval = _UsdNtpPeerBroadcastInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 4),
    _UsdNtpPeerBroadcastInterval_Type()
)
usdNtpPeerBroadcastInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerBroadcastInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerBroadcastInterval.setUnits("seconds")
_UsdNtpPeerPolledInterval_Type = Integer32
_UsdNtpPeerPolledInterval_Object = MibTableColumn
usdNtpPeerPolledInterval = _UsdNtpPeerPolledInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 5),
    _UsdNtpPeerPolledInterval_Type()
)
usdNtpPeerPolledInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerPolledInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerPolledInterval.setUnits("seconds")
_UsdNtpPeerPollingInterval_Type = Integer32
_UsdNtpPeerPollingInterval_Object = MibTableColumn
usdNtpPeerPollingInterval = _UsdNtpPeerPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 6),
    _UsdNtpPeerPollingInterval_Type()
)
usdNtpPeerPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerPollingInterval.setUnits("seconds")
_UsdNtpPeerDelay_Type = UsdNtpClockSignedTime
_UsdNtpPeerDelay_Object = MibTableColumn
usdNtpPeerDelay = _UsdNtpPeerDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 7),
    _UsdNtpPeerDelay_Type()
)
usdNtpPeerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerDelay.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerDelay.setUnits("seconds")
_UsdNtpPeerDispersion_Type = UsdNtpClockUnsignedTime
_UsdNtpPeerDispersion_Object = MibTableColumn
usdNtpPeerDispersion = _UsdNtpPeerDispersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 8),
    _UsdNtpPeerDispersion_Type()
)
usdNtpPeerDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerDispersion.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerDispersion.setUnits("seconds")
_UsdNtpPeerOffsetError_Type = UsdNtpClockSignedTime
_UsdNtpPeerOffsetError_Object = MibTableColumn
usdNtpPeerOffsetError = _UsdNtpPeerOffsetError_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 9),
    _UsdNtpPeerOffsetError_Type()
)
usdNtpPeerOffsetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerOffsetError.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerOffsetError.setUnits("seconds")


class _UsdNtpPeerReachability_Type(OctetString):
    """Custom type usdNtpPeerReachability based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_UsdNtpPeerReachability_Type.__name__ = "OctetString"
_UsdNtpPeerReachability_Object = MibTableColumn
usdNtpPeerReachability = _UsdNtpPeerReachability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 10),
    _UsdNtpPeerReachability_Type()
)
usdNtpPeerReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerReachability.setStatus("current")
_UsdNtpPeerRootDelay_Type = UsdNtpClockSignedTime
_UsdNtpPeerRootDelay_Object = MibTableColumn
usdNtpPeerRootDelay = _UsdNtpPeerRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 11),
    _UsdNtpPeerRootDelay_Type()
)
usdNtpPeerRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerRootDelay.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerRootDelay.setUnits("seconds")
_UsdNtpPeerRootDispersion_Type = UsdNtpClockUnsignedTime
_UsdNtpPeerRootDispersion_Object = MibTableColumn
usdNtpPeerRootDispersion = _UsdNtpPeerRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 12),
    _UsdNtpPeerRootDispersion_Type()
)
usdNtpPeerRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerRootDispersion.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerRootDispersion.setUnits("seconds")
_UsdNtpPeerRootSyncDistance_Type = UsdNtpClockSignedTime
_UsdNtpPeerRootSyncDistance_Object = MibTableColumn
usdNtpPeerRootSyncDistance = _UsdNtpPeerRootSyncDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 13),
    _UsdNtpPeerRootSyncDistance_Type()
)
usdNtpPeerRootSyncDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerRootSyncDistance.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerRootSyncDistance.setUnits("seconds")
_UsdNtpPeerRootTime_Type = UsdNtpTimeStamp
_UsdNtpPeerRootTime_Object = MibTableColumn
usdNtpPeerRootTime = _UsdNtpPeerRootTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 14),
    _UsdNtpPeerRootTime_Type()
)
usdNtpPeerRootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerRootTime.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerRootTime.setUnits("seconds")
_UsdNtpPeerRootTimeUpdateServer_Type = IpAddress
_UsdNtpPeerRootTimeUpdateServer_Object = MibTableColumn
usdNtpPeerRootTimeUpdateServer = _UsdNtpPeerRootTimeUpdateServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 15),
    _UsdNtpPeerRootTimeUpdateServer_Type()
)
usdNtpPeerRootTimeUpdateServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerRootTimeUpdateServer.setStatus("current")
_UsdNtpPeerReceiveTime_Type = UsdNtpTimeStamp
_UsdNtpPeerReceiveTime_Object = MibTableColumn
usdNtpPeerReceiveTime = _UsdNtpPeerReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 16),
    _UsdNtpPeerReceiveTime_Type()
)
usdNtpPeerReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerReceiveTime.setStatus("current")
_UsdNtpPeerTransmitTime_Type = UsdNtpTimeStamp
_UsdNtpPeerTransmitTime_Object = MibTableColumn
usdNtpPeerTransmitTime = _UsdNtpPeerTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 17),
    _UsdNtpPeerTransmitTime_Type()
)
usdNtpPeerTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerTransmitTime.setStatus("current")
_UsdNtpPeerRequestTime_Type = UsdNtpTimeStamp
_UsdNtpPeerRequestTime_Object = MibTableColumn
usdNtpPeerRequestTime = _UsdNtpPeerRequestTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 18),
    _UsdNtpPeerRequestTime_Type()
)
usdNtpPeerRequestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerRequestTime.setStatus("current")
_UsdNtpPeerPrecision_Type = UsdNtpClockSignedTime
_UsdNtpPeerPrecision_Object = MibTableColumn
usdNtpPeerPrecision = _UsdNtpPeerPrecision_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 2, 1, 19),
    _UsdNtpPeerPrecision_Type()
)
usdNtpPeerPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerPrecision.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerPrecision.setUnits("seconds")
_UsdNtpPeerFilterRegisterTable_Object = MibTable
usdNtpPeerFilterRegisterTable = _UsdNtpPeerFilterRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 3)
)
if mibBuilder.loadTexts:
    usdNtpPeerFilterRegisterTable.setStatus("current")
_UsdNtpPeerFilterRegisterEntry_Object = MibTableRow
usdNtpPeerFilterRegisterEntry = _UsdNtpPeerFilterRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 3, 1)
)
usdNtpPeerFilterRegisterEntry.setIndexNames(
    (0, "Unisphere-Data-System-Clock-MIB", "usdNtpPeerCfgIpAddress"),
    (0, "Unisphere-Data-System-Clock-MIB", "usdNtpPeerFilterIndex"),
)
if mibBuilder.loadTexts:
    usdNtpPeerFilterRegisterEntry.setStatus("current")
_UsdNtpPeerFilterIndex_Type = Unsigned32
_UsdNtpPeerFilterIndex_Object = MibTableColumn
usdNtpPeerFilterIndex = _UsdNtpPeerFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 3, 1, 1),
    _UsdNtpPeerFilterIndex_Type()
)
usdNtpPeerFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdNtpPeerFilterIndex.setStatus("current")
_UsdNtpPeerFilterOffset_Type = UsdNtpClockSignedTime
_UsdNtpPeerFilterOffset_Object = MibTableColumn
usdNtpPeerFilterOffset = _UsdNtpPeerFilterOffset_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 3, 1, 2),
    _UsdNtpPeerFilterOffset_Type()
)
usdNtpPeerFilterOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerFilterOffset.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerFilterOffset.setUnits("seconds")
_UsdNtpPeerFilterDelay_Type = UsdNtpClockSignedTime
_UsdNtpPeerFilterDelay_Object = MibTableColumn
usdNtpPeerFilterDelay = _UsdNtpPeerFilterDelay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 3, 1, 3),
    _UsdNtpPeerFilterDelay_Type()
)
usdNtpPeerFilterDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerFilterDelay.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerFilterDelay.setUnits("seconds")
_UsdNtpPeerFilterDispersion_Type = UsdNtpClockUnsignedTime
_UsdNtpPeerFilterDispersion_Object = MibTableColumn
usdNtpPeerFilterDispersion = _UsdNtpPeerFilterDispersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 4, 3, 1, 4),
    _UsdNtpPeerFilterDispersion_Type()
)
usdNtpPeerFilterDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdNtpPeerFilterDispersion.setStatus("current")
if mibBuilder.loadTexts:
    usdNtpPeerFilterDispersion.setUnits("seconds")
_UsdNtpAccessGroup_ObjectIdentity = ObjectIdentity
usdNtpAccessGroup = _UsdNtpAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 5)
)
_UsdNtpRouterAccessGroupPeer_Type = DisplayString
_UsdNtpRouterAccessGroupPeer_Object = MibScalar
usdNtpRouterAccessGroupPeer = _UsdNtpRouterAccessGroupPeer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 5, 1),
    _UsdNtpRouterAccessGroupPeer_Type()
)
usdNtpRouterAccessGroupPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdNtpRouterAccessGroupPeer.setStatus("current")
_UsdNtpRouterAccessGroupServe_Type = DisplayString
_UsdNtpRouterAccessGroupServe_Object = MibScalar
usdNtpRouterAccessGroupServe = _UsdNtpRouterAccessGroupServe_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 5, 2),
    _UsdNtpRouterAccessGroupServe_Type()
)
usdNtpRouterAccessGroupServe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdNtpRouterAccessGroupServe.setStatus("current")
_UsdNtpRouterAccessGroupServeOnly_Type = DisplayString
_UsdNtpRouterAccessGroupServeOnly_Object = MibScalar
usdNtpRouterAccessGroupServeOnly = _UsdNtpRouterAccessGroupServeOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 5, 3),
    _UsdNtpRouterAccessGroupServeOnly_Type()
)
usdNtpRouterAccessGroupServeOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdNtpRouterAccessGroupServeOnly.setStatus("current")
_UsdNtpRouterAccessGroupQueryOnly_Type = DisplayString
_UsdNtpRouterAccessGroupQueryOnly_Object = MibScalar
usdNtpRouterAccessGroupQueryOnly = _UsdNtpRouterAccessGroupQueryOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 2, 5, 4),
    _UsdNtpRouterAccessGroupQueryOnly_Type()
)
usdNtpRouterAccessGroupQueryOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdNtpRouterAccessGroupQueryOnly.setStatus("current")
_UsdSysClockConformance_ObjectIdentity = ObjectIdentity
usdSysClockConformance = _UsdSysClockConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3)
)
_UsdSysClockCompliances_ObjectIdentity = ObjectIdentity
usdSysClockCompliances = _UsdSysClockCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 1)
)
_UsdSysClockGroups_ObjectIdentity = ObjectIdentity
usdSysClockGroups = _UsdSysClockGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2)
)

# Managed Objects groups

usdSysClockTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 1)
)
usdSysClockTimeGroup.setObjects(
      *(("Unisphere-Data-System-Clock-MIB", "usdSysClockDateAndTime"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockTimeZoneName"))
)
if mibBuilder.loadTexts:
    usdSysClockTimeGroup.setStatus("current")

usdSysClockDstGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 2)
)
usdSysClockDstGroup.setObjects(
      *(("Unisphere-Data-System-Clock-MIB", "usdSysClockDstName"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstOffset"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstStatus"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstAbsoluteStartTime"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstAbsoluteStopTime"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstRecurStartMonth"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstRecurStartWeek"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstRecurStartDay"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstRecurStartHour"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstRecurStartMinute"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstRecurStopMonth"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstRecurStopWeek"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstRecurStopDay"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstRecurStopHour"),
        ("Unisphere-Data-System-Clock-MIB", "usdSysClockDstRecurStopMinute"))
)
if mibBuilder.loadTexts:
    usdSysClockDstGroup.setStatus("current")

usdNtpSysClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 3)
)
usdNtpSysClockGroup.setObjects(
      *(("Unisphere-Data-System-Clock-MIB", "usdNtpSysClockState"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpSysClockOffsetError"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpSysClockFrequencyError"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpSysClockRootDelay"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpSysClockRootDispersion"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpSysClockStratumNumber"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpSysClockLastUpdateTime"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpSysClockLastUpdateServer"))
)
if mibBuilder.loadTexts:
    usdNtpSysClockGroup.setStatus("current")

usdNtpClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 4)
)
usdNtpClientGroup.setObjects(
      *(("Unisphere-Data-System-Clock-MIB", "usdNtpClientAdminStatus"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpClientSystemRouterIndex"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpClientPacketSourceIfIndex"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpClientBroadcastDelay"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpClientIfStatus"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpClientIfIsBroadcastClient"))
)
if mibBuilder.loadTexts:
    usdNtpClientGroup.setStatus("current")

usdNtpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 5)
)
usdNtpServerGroup.setObjects(
      *(("Unisphere-Data-System-Clock-MIB", "usdNtpServerAdminStatus"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpServerStratumNumber"))
)
if mibBuilder.loadTexts:
    usdNtpServerGroup.setStatus("current")

usdNtpPeersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 6)
)
usdNtpPeersGroup.setObjects(
      *(("Unisphere-Data-System-Clock-MIB", "usdNtpPeerState"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerStratumNumber"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerAssociationMode"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerBroadcastInterval"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerPolledInterval"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerPollingInterval"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerDelay"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerDispersion"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerOffsetError"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerReachability"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerPrecision"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerRootDelay"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerRootDispersion"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerRootSyncDistance"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerRootTime"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerRootTimeUpdateServer"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerReceiveTime"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerTransmitTime"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerRequestTime"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerFilterOffset"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerFilterDelay"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerFilterDispersion"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerCfgNtpVersion"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerCfgPacketSourceIfIndex"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerCfgIsPreferred"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpPeerCfgRowStatus"))
)
if mibBuilder.loadTexts:
    usdNtpPeersGroup.setStatus("current")

usdNtpAccessGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 2, 7)
)
usdNtpAccessGroupGroup.setObjects(
      *(("Unisphere-Data-System-Clock-MIB", "usdNtpRouterAccessGroupPeer"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpRouterAccessGroupServe"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpRouterAccessGroupServeOnly"),
        ("Unisphere-Data-System-Clock-MIB", "usdNtpRouterAccessGroupQueryOnly"))
)
if mibBuilder.loadTexts:
    usdNtpAccessGroupGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdSysClockCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56, 3, 1, 1)
)
if mibBuilder.loadTexts:
    usdSysClockCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-System-Clock-MIB",
    **{"UsdSysClockMonth": UsdSysClockMonth,
       "UsdSysClockWeekOfTheMonth": UsdSysClockWeekOfTheMonth,
       "UsdSysClockDayOfTheWeek": UsdSysClockDayOfTheWeek,
       "UsdSysClockHour": UsdSysClockHour,
       "UsdSysClockMinute": UsdSysClockMinute,
       "UsdNtpTimeStamp": UsdNtpTimeStamp,
       "UsdNtpClockSignedTime": UsdNtpClockSignedTime,
       "UsdNtpClockUnsignedTime": UsdNtpClockUnsignedTime,
       "usdSysClockMIB": usdSysClockMIB,
       "usdSysClockObjects": usdSysClockObjects,
       "usdSysClockTime": usdSysClockTime,
       "usdSysClockDateAndTime": usdSysClockDateAndTime,
       "usdSysClockTimeZoneName": usdSysClockTimeZoneName,
       "usdSysClockDst": usdSysClockDst,
       "usdSysClockDstName": usdSysClockDstName,
       "usdSysClockDstOffset": usdSysClockDstOffset,
       "usdSysClockDstStatus": usdSysClockDstStatus,
       "usdSysClockDstAbsoluteStartTime": usdSysClockDstAbsoluteStartTime,
       "usdSysClockDstAbsoluteStopTime": usdSysClockDstAbsoluteStopTime,
       "usdSysClockDstRecurStartMonth": usdSysClockDstRecurStartMonth,
       "usdSysClockDstRecurStartWeek": usdSysClockDstRecurStartWeek,
       "usdSysClockDstRecurStartDay": usdSysClockDstRecurStartDay,
       "usdSysClockDstRecurStartHour": usdSysClockDstRecurStartHour,
       "usdSysClockDstRecurStartMinute": usdSysClockDstRecurStartMinute,
       "usdSysClockDstRecurStopMonth": usdSysClockDstRecurStopMonth,
       "usdSysClockDstRecurStopWeek": usdSysClockDstRecurStopWeek,
       "usdSysClockDstRecurStopDay": usdSysClockDstRecurStopDay,
       "usdSysClockDstRecurStopHour": usdSysClockDstRecurStopHour,
       "usdSysClockDstRecurStopMinute": usdSysClockDstRecurStopMinute,
       "usdNtpObjects": usdNtpObjects,
       "usdNtpSysClock": usdNtpSysClock,
       "usdNtpSysClockState": usdNtpSysClockState,
       "usdNtpSysClockOffsetError": usdNtpSysClockOffsetError,
       "usdNtpSysClockFrequencyError": usdNtpSysClockFrequencyError,
       "usdNtpSysClockRootDelay": usdNtpSysClockRootDelay,
       "usdNtpSysClockRootDispersion": usdNtpSysClockRootDispersion,
       "usdNtpSysClockStratumNumber": usdNtpSysClockStratumNumber,
       "usdNtpSysClockLastUpdateTime": usdNtpSysClockLastUpdateTime,
       "usdNtpSysClockLastUpdateServer": usdNtpSysClockLastUpdateServer,
       "usdNtpClient": usdNtpClient,
       "usdNtpClientAdminStatus": usdNtpClientAdminStatus,
       "usdNtpClientSystemRouterIndex": usdNtpClientSystemRouterIndex,
       "usdNtpClientPacketSourceIfIndex": usdNtpClientPacketSourceIfIndex,
       "usdNtpClientBroadcastDelay": usdNtpClientBroadcastDelay,
       "usdNtpClientIfTable": usdNtpClientIfTable,
       "usdNtpClientIfEntry": usdNtpClientIfEntry,
       "usdNtpClientIfRouterIndex": usdNtpClientIfRouterIndex,
       "usdNtpClientIfIfIndex": usdNtpClientIfIfIndex,
       "usdNtpClientIfStatus": usdNtpClientIfStatus,
       "usdNtpClientIfIsBroadcastClient": usdNtpClientIfIsBroadcastClient,
       "usdNtpServer": usdNtpServer,
       "usdNtpServerStratumNumber": usdNtpServerStratumNumber,
       "usdNtpServerAdminStatus": usdNtpServerAdminStatus,
       "usdNtpPeers": usdNtpPeers,
       "usdNtpPeerCfgTable": usdNtpPeerCfgTable,
       "usdNtpPeerCfgEntry": usdNtpPeerCfgEntry,
       "usdNtpPeerCfgIpAddress": usdNtpPeerCfgIpAddress,
       "usdNtpPeerCfgNtpVersion": usdNtpPeerCfgNtpVersion,
       "usdNtpPeerCfgPacketSourceIfIndex": usdNtpPeerCfgPacketSourceIfIndex,
       "usdNtpPeerCfgIsPreferred": usdNtpPeerCfgIsPreferred,
       "usdNtpPeerCfgRowStatus": usdNtpPeerCfgRowStatus,
       "usdNtpPeerTable": usdNtpPeerTable,
       "usdNtpPeerEntry": usdNtpPeerEntry,
       "usdNtpPeerState": usdNtpPeerState,
       "usdNtpPeerStratumNumber": usdNtpPeerStratumNumber,
       "usdNtpPeerAssociationMode": usdNtpPeerAssociationMode,
       "usdNtpPeerBroadcastInterval": usdNtpPeerBroadcastInterval,
       "usdNtpPeerPolledInterval": usdNtpPeerPolledInterval,
       "usdNtpPeerPollingInterval": usdNtpPeerPollingInterval,
       "usdNtpPeerDelay": usdNtpPeerDelay,
       "usdNtpPeerDispersion": usdNtpPeerDispersion,
       "usdNtpPeerOffsetError": usdNtpPeerOffsetError,
       "usdNtpPeerReachability": usdNtpPeerReachability,
       "usdNtpPeerRootDelay": usdNtpPeerRootDelay,
       "usdNtpPeerRootDispersion": usdNtpPeerRootDispersion,
       "usdNtpPeerRootSyncDistance": usdNtpPeerRootSyncDistance,
       "usdNtpPeerRootTime": usdNtpPeerRootTime,
       "usdNtpPeerRootTimeUpdateServer": usdNtpPeerRootTimeUpdateServer,
       "usdNtpPeerReceiveTime": usdNtpPeerReceiveTime,
       "usdNtpPeerTransmitTime": usdNtpPeerTransmitTime,
       "usdNtpPeerRequestTime": usdNtpPeerRequestTime,
       "usdNtpPeerPrecision": usdNtpPeerPrecision,
       "usdNtpPeerFilterRegisterTable": usdNtpPeerFilterRegisterTable,
       "usdNtpPeerFilterRegisterEntry": usdNtpPeerFilterRegisterEntry,
       "usdNtpPeerFilterIndex": usdNtpPeerFilterIndex,
       "usdNtpPeerFilterOffset": usdNtpPeerFilterOffset,
       "usdNtpPeerFilterDelay": usdNtpPeerFilterDelay,
       "usdNtpPeerFilterDispersion": usdNtpPeerFilterDispersion,
       "usdNtpAccessGroup": usdNtpAccessGroup,
       "usdNtpRouterAccessGroupPeer": usdNtpRouterAccessGroupPeer,
       "usdNtpRouterAccessGroupServe": usdNtpRouterAccessGroupServe,
       "usdNtpRouterAccessGroupServeOnly": usdNtpRouterAccessGroupServeOnly,
       "usdNtpRouterAccessGroupQueryOnly": usdNtpRouterAccessGroupQueryOnly,
       "usdSysClockConformance": usdSysClockConformance,
       "usdSysClockCompliances": usdSysClockCompliances,
       "usdSysClockCompliance": usdSysClockCompliance,
       "usdSysClockGroups": usdSysClockGroups,
       "usdSysClockTimeGroup": usdSysClockTimeGroup,
       "usdSysClockDstGroup": usdSysClockDstGroup,
       "usdNtpSysClockGroup": usdNtpSysClockGroup,
       "usdNtpClientGroup": usdNtpClientGroup,
       "usdNtpServerGroup": usdNtpServerGroup,
       "usdNtpPeersGroup": usdNtpPeersGroup,
       "usdNtpAccessGroupGroup": usdNtpAccessGroupGroup}
)
