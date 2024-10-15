# SNMP MIB module (ZYXEL-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:55 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelDateTimeSetup_ObjectIdentity = ObjectIdentity
zyxelDateTimeSetup = _ZyxelDateTimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1)
)


class _ZyDateTimeServerType_Type(Integer32):
    """Custom type zyDateTimeServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("daytime", 2),
          ("none", 1),
          ("ntp", 4),
          ("time", 3))
    )


_ZyDateTimeServerType_Type.__name__ = "Integer32"
_ZyDateTimeServerType_Object = MibScalar
zyDateTimeServerType = _ZyDateTimeServerType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 1),
    _ZyDateTimeServerType_Type()
)
zyDateTimeServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDateTimeServerType.setStatus("current")
_ZyDateTimeServerIpAddress_Type = IpAddress
_ZyDateTimeServerIpAddress_Object = MibScalar
zyDateTimeServerIpAddress = _ZyDateTimeServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 2),
    _ZyDateTimeServerIpAddress_Type()
)
zyDateTimeServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDateTimeServerIpAddress.setStatus("current")
_ZyDateTimeZone_Type = Integer32
_ZyDateTimeZone_Object = MibScalar
zyDateTimeZone = _ZyDateTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 3),
    _ZyDateTimeZone_Type()
)
zyDateTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDateTimeZone.setStatus("current")
_ZyDateTimeNewDateYear_Type = Integer32
_ZyDateTimeNewDateYear_Object = MibScalar
zyDateTimeNewDateYear = _ZyDateTimeNewDateYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 4),
    _ZyDateTimeNewDateYear_Type()
)
zyDateTimeNewDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDateTimeNewDateYear.setStatus("current")
_ZyDateTimeNewDateMonth_Type = Integer32
_ZyDateTimeNewDateMonth_Object = MibScalar
zyDateTimeNewDateMonth = _ZyDateTimeNewDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 5),
    _ZyDateTimeNewDateMonth_Type()
)
zyDateTimeNewDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDateTimeNewDateMonth.setStatus("current")
_ZyDateTimeNewDateDay_Type = Integer32
_ZyDateTimeNewDateDay_Object = MibScalar
zyDateTimeNewDateDay = _ZyDateTimeNewDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 6),
    _ZyDateTimeNewDateDay_Type()
)
zyDateTimeNewDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDateTimeNewDateDay.setStatus("current")
_ZyDateTimeNewTimeHour_Type = Integer32
_ZyDateTimeNewTimeHour_Object = MibScalar
zyDateTimeNewTimeHour = _ZyDateTimeNewTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 7),
    _ZyDateTimeNewTimeHour_Type()
)
zyDateTimeNewTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDateTimeNewTimeHour.setStatus("current")
_ZyDateTimeNewTimeMinute_Type = Integer32
_ZyDateTimeNewTimeMinute_Object = MibScalar
zyDateTimeNewTimeMinute = _ZyDateTimeNewTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 8),
    _ZyDateTimeNewTimeMinute_Type()
)
zyDateTimeNewTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDateTimeNewTimeMinute.setStatus("current")
_ZyDateTimeNewTimeSecond_Type = Integer32
_ZyDateTimeNewTimeSecond_Object = MibScalar
zyDateTimeNewTimeSecond = _ZyDateTimeNewTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 9),
    _ZyDateTimeNewTimeSecond_Type()
)
zyDateTimeNewTimeSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDateTimeNewTimeSecond.setStatus("current")
_ZyxelDateTimeDaylightSavingTimeSetup_ObjectIdentity = ObjectIdentity
zyxelDateTimeDaylightSavingTimeSetup = _ZyxelDateTimeDaylightSavingTimeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10)
)
_ZyDaylightSavingTimeState_Type = EnabledStatus
_ZyDaylightSavingTimeState_Object = MibScalar
zyDaylightSavingTimeState = _ZyDaylightSavingTimeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 1),
    _ZyDaylightSavingTimeState_Type()
)
zyDaylightSavingTimeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDaylightSavingTimeState.setStatus("current")


class _ZyDaylightSavingTimeStartDateWeek_Type(Integer32):
    """Custom type zyDaylightSavingTimeStartDateWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
          ("second", 2),
          ("third", 3))
    )


_ZyDaylightSavingTimeStartDateWeek_Type.__name__ = "Integer32"
_ZyDaylightSavingTimeStartDateWeek_Object = MibScalar
zyDaylightSavingTimeStartDateWeek = _ZyDaylightSavingTimeStartDateWeek_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 2),
    _ZyDaylightSavingTimeStartDateWeek_Type()
)
zyDaylightSavingTimeStartDateWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDaylightSavingTimeStartDateWeek.setStatus("current")


class _ZyDaylightSavingTimeStartDateDay_Type(Integer32):
    """Custom type zyDaylightSavingTimeStartDateDay based on Integer32"""
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


_ZyDaylightSavingTimeStartDateDay_Type.__name__ = "Integer32"
_ZyDaylightSavingTimeStartDateDay_Object = MibScalar
zyDaylightSavingTimeStartDateDay = _ZyDaylightSavingTimeStartDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 3),
    _ZyDaylightSavingTimeStartDateDay_Type()
)
zyDaylightSavingTimeStartDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDaylightSavingTimeStartDateDay.setStatus("current")


class _ZyDaylightSavingTimeStartDateMonth_Type(Integer32):
    """Custom type zyDaylightSavingTimeStartDateMonth based on Integer32"""
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


_ZyDaylightSavingTimeStartDateMonth_Type.__name__ = "Integer32"
_ZyDaylightSavingTimeStartDateMonth_Object = MibScalar
zyDaylightSavingTimeStartDateMonth = _ZyDaylightSavingTimeStartDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 4),
    _ZyDaylightSavingTimeStartDateMonth_Type()
)
zyDaylightSavingTimeStartDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDaylightSavingTimeStartDateMonth.setStatus("current")
_ZyDaylightSavingTimeStartDateHour_Type = Integer32
_ZyDaylightSavingTimeStartDateHour_Object = MibScalar
zyDaylightSavingTimeStartDateHour = _ZyDaylightSavingTimeStartDateHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 5),
    _ZyDaylightSavingTimeStartDateHour_Type()
)
zyDaylightSavingTimeStartDateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDaylightSavingTimeStartDateHour.setStatus("current")


class _ZyDaylightSavingTimeEndDateWeek_Type(Integer32):
    """Custom type zyDaylightSavingTimeEndDateWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
          ("second", 2),
          ("third", 3))
    )


_ZyDaylightSavingTimeEndDateWeek_Type.__name__ = "Integer32"
_ZyDaylightSavingTimeEndDateWeek_Object = MibScalar
zyDaylightSavingTimeEndDateWeek = _ZyDaylightSavingTimeEndDateWeek_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 6),
    _ZyDaylightSavingTimeEndDateWeek_Type()
)
zyDaylightSavingTimeEndDateWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDaylightSavingTimeEndDateWeek.setStatus("current")


class _ZyDaylightSavingTimeEndDateDay_Type(Integer32):
    """Custom type zyDaylightSavingTimeEndDateDay based on Integer32"""
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


_ZyDaylightSavingTimeEndDateDay_Type.__name__ = "Integer32"
_ZyDaylightSavingTimeEndDateDay_Object = MibScalar
zyDaylightSavingTimeEndDateDay = _ZyDaylightSavingTimeEndDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 7),
    _ZyDaylightSavingTimeEndDateDay_Type()
)
zyDaylightSavingTimeEndDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDaylightSavingTimeEndDateDay.setStatus("current")


class _ZyDaylightSavingTimeEndDateMonth_Type(Integer32):
    """Custom type zyDaylightSavingTimeEndDateMonth based on Integer32"""
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


_ZyDaylightSavingTimeEndDateMonth_Type.__name__ = "Integer32"
_ZyDaylightSavingTimeEndDateMonth_Object = MibScalar
zyDaylightSavingTimeEndDateMonth = _ZyDaylightSavingTimeEndDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 8),
    _ZyDaylightSavingTimeEndDateMonth_Type()
)
zyDaylightSavingTimeEndDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDaylightSavingTimeEndDateMonth.setStatus("current")
_ZyDaylightSavingTimeEndDateHour_Type = Integer32
_ZyDaylightSavingTimeEndDateHour_Object = MibScalar
zyDaylightSavingTimeEndDateHour = _ZyDaylightSavingTimeEndDateHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 1, 10, 9),
    _ZyDaylightSavingTimeEndDateHour_Type()
)
zyDaylightSavingTimeEndDateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDaylightSavingTimeEndDateHour.setStatus("current")
_ZyxelSysInfo_ObjectIdentity = ObjectIdentity
zyxelSysInfo = _ZyxelSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2)
)
_ZySysSwPlatformMajorVers_Type = Integer32
_ZySysSwPlatformMajorVers_Object = MibScalar
zySysSwPlatformMajorVers = _ZySysSwPlatformMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 1),
    _ZySysSwPlatformMajorVers_Type()
)
zySysSwPlatformMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysSwPlatformMajorVers.setStatus("current")
_ZySysSwPlatformMinorVers_Type = Integer32
_ZySysSwPlatformMinorVers_Object = MibScalar
zySysSwPlatformMinorVers = _ZySysSwPlatformMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 2),
    _ZySysSwPlatformMinorVers_Type()
)
zySysSwPlatformMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysSwPlatformMinorVers.setStatus("current")
_ZySysSwModelString_Type = DisplayString
_ZySysSwModelString_Object = MibScalar
zySysSwModelString = _ZySysSwModelString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 3),
    _ZySysSwModelString_Type()
)
zySysSwModelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysSwModelString.setStatus("current")
_ZySysSwVersionControlNbr_Type = Integer32
_ZySysSwVersionControlNbr_Object = MibScalar
zySysSwVersionControlNbr = _ZySysSwVersionControlNbr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 4),
    _ZySysSwVersionControlNbr_Type()
)
zySysSwVersionControlNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysSwVersionControlNbr.setStatus("current")
_ZySysSwDay_Type = Integer32
_ZySysSwDay_Object = MibScalar
zySysSwDay = _ZySysSwDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 5),
    _ZySysSwDay_Type()
)
zySysSwDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysSwDay.setStatus("current")
_ZySysSwMonth_Type = Integer32
_ZySysSwMonth_Object = MibScalar
zySysSwMonth = _ZySysSwMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 6),
    _ZySysSwMonth_Type()
)
zySysSwMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysSwMonth.setStatus("current")
_ZySysSwYear_Type = Integer32
_ZySysSwYear_Object = MibScalar
zySysSwYear = _ZySysSwYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 7),
    _ZySysSwYear_Type()
)
zySysSwYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysSwYear.setStatus("current")
_ZySysHwMajorVers_Type = Integer32
_ZySysHwMajorVers_Object = MibScalar
zySysHwMajorVers = _ZySysHwMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 8),
    _ZySysHwMajorVers_Type()
)
zySysHwMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysHwMajorVers.setStatus("current")
_ZySysHwMinorVers_Type = Integer32
_ZySysHwMinorVers_Object = MibScalar
zySysHwMinorVers = _ZySysHwMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 9),
    _ZySysHwMinorVers_Type()
)
zySysHwMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysHwMinorVers.setStatus("current")
_ZySysSerialNumber_Type = DisplayString
_ZySysSerialNumber_Object = MibScalar
zySysSerialNumber = _ZySysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 10),
    _ZySysSerialNumber_Type()
)
zySysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysSerialNumber.setStatus("current")


class _ZySysSwBootUpImage_Type(Integer32):
    """Custom type zySysSwBootUpImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2))
    )


_ZySysSwBootUpImage_Type.__name__ = "Integer32"
_ZySysSwBootUpImage_Object = MibScalar
zySysSwBootUpImage = _ZySysSwBootUpImage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 2, 11),
    _ZySysSwBootUpImage_Type()
)
zySysSwBootUpImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysSwBootUpImage.setStatus("current")
_ZyxelDateTimeTrapNotifications_ObjectIdentity = ObjectIdentity
zyxelDateTimeTrapNotifications = _ZyxelDateTimeTrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 3)
)

# Managed Objects groups


# Notification objects

zyDateTimeTrapTimeServerNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 3, 1)
)
if mibBuilder.loadTexts:
    zyDateTimeTrapTimeServerNotReachable.setStatus(
        "current"
    )

zyDateTimeTrapTimeServerNotReachableRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 82, 3, 2)
)
if mibBuilder.loadTexts:
    zyDateTimeTrapTimeServerNotReachableRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-SYSTEM-MIB",
    **{"zyxelSystem": zyxelSystem,
       "zyxelDateTimeSetup": zyxelDateTimeSetup,
       "zyDateTimeServerType": zyDateTimeServerType,
       "zyDateTimeServerIpAddress": zyDateTimeServerIpAddress,
       "zyDateTimeZone": zyDateTimeZone,
       "zyDateTimeNewDateYear": zyDateTimeNewDateYear,
       "zyDateTimeNewDateMonth": zyDateTimeNewDateMonth,
       "zyDateTimeNewDateDay": zyDateTimeNewDateDay,
       "zyDateTimeNewTimeHour": zyDateTimeNewTimeHour,
       "zyDateTimeNewTimeMinute": zyDateTimeNewTimeMinute,
       "zyDateTimeNewTimeSecond": zyDateTimeNewTimeSecond,
       "zyxelDateTimeDaylightSavingTimeSetup": zyxelDateTimeDaylightSavingTimeSetup,
       "zyDaylightSavingTimeState": zyDaylightSavingTimeState,
       "zyDaylightSavingTimeStartDateWeek": zyDaylightSavingTimeStartDateWeek,
       "zyDaylightSavingTimeStartDateDay": zyDaylightSavingTimeStartDateDay,
       "zyDaylightSavingTimeStartDateMonth": zyDaylightSavingTimeStartDateMonth,
       "zyDaylightSavingTimeStartDateHour": zyDaylightSavingTimeStartDateHour,
       "zyDaylightSavingTimeEndDateWeek": zyDaylightSavingTimeEndDateWeek,
       "zyDaylightSavingTimeEndDateDay": zyDaylightSavingTimeEndDateDay,
       "zyDaylightSavingTimeEndDateMonth": zyDaylightSavingTimeEndDateMonth,
       "zyDaylightSavingTimeEndDateHour": zyDaylightSavingTimeEndDateHour,
       "zyxelSysInfo": zyxelSysInfo,
       "zySysSwPlatformMajorVers": zySysSwPlatformMajorVers,
       "zySysSwPlatformMinorVers": zySysSwPlatformMinorVers,
       "zySysSwModelString": zySysSwModelString,
       "zySysSwVersionControlNbr": zySysSwVersionControlNbr,
       "zySysSwDay": zySysSwDay,
       "zySysSwMonth": zySysSwMonth,
       "zySysSwYear": zySysSwYear,
       "zySysHwMajorVers": zySysHwMajorVers,
       "zySysHwMinorVers": zySysHwMinorVers,
       "zySysSerialNumber": zySysSerialNumber,
       "zySysSwBootUpImage": zySysSwBootUpImage,
       "zyxelDateTimeTrapNotifications": zyxelDateTimeTrapNotifications,
       "zyDateTimeTrapTimeServerNotReachable": zyDateTimeTrapTimeServerNotReachable,
       "zyDateTimeTrapTimeServerNotReachableRecovered": zyDateTimeTrapTimeServerNotReachableRecovered}
)
