# SNMP MIB module (ZYXEL-TIME-RANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-TIME-RANGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:57 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(InterfaceIndexOrZero,
 OperationResponseStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "OperationResponseStatus")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "SnmpAdminString")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelTimeRange = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZyTimeRangeWeekDayList(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_ZyxelTimeRangeSetup_ObjectIdentity = ObjectIdentity
zyxelTimeRangeSetup = _ZyxelTimeRangeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1)
)
_ZyTimeRangeMaxNumberOfProfiles_Type = Integer32
_ZyTimeRangeMaxNumberOfProfiles_Object = MibScalar
zyTimeRangeMaxNumberOfProfiles = _ZyTimeRangeMaxNumberOfProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 1),
    _ZyTimeRangeMaxNumberOfProfiles_Type()
)
zyTimeRangeMaxNumberOfProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTimeRangeMaxNumberOfProfiles.setStatus("current")
_ZyxelTimeRangeTable_Object = MibTable
zyxelTimeRangeTable = _ZyxelTimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelTimeRangeTable.setStatus("current")
_ZyxelTimeRangeEntry_Object = MibTableRow
zyxelTimeRangeEntry = _ZyxelTimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 2, 1)
)
zyxelTimeRangeEntry.setIndexNames(
    (0, "ZYXEL-TIME-RANGE-MIB", "zyTimeRangeName"),
    (0, "ZYXEL-TIME-RANGE-MIB", "zyTimeRangeType"),
)
if mibBuilder.loadTexts:
    zyxelTimeRangeEntry.setStatus("current")
_ZyTimeRangeName_Type = DisplayString
_ZyTimeRangeName_Object = MibTableColumn
zyTimeRangeName = _ZyTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 2, 1, 1),
    _ZyTimeRangeName_Type()
)
zyTimeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyTimeRangeName.setStatus("current")


class _ZyTimeRangeType_Type(Integer32):
    """Custom type zyTimeRangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("periodic", 2))
    )


_ZyTimeRangeType_Type.__name__ = "Integer32"
_ZyTimeRangeType_Object = MibTableColumn
zyTimeRangeType = _ZyTimeRangeType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 2, 1, 2),
    _ZyTimeRangeType_Type()
)
zyTimeRangeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyTimeRangeType.setStatus("current")
_ZyTimeRangeRowStatus_Type = RowStatus
_ZyTimeRangeRowStatus_Object = MibTableColumn
zyTimeRangeRowStatus = _ZyTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 2, 1, 3),
    _ZyTimeRangeRowStatus_Type()
)
zyTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyTimeRangeRowStatus.setStatus("current")
_ZyxelTimeRangeAbsoluteTable_Object = MibTable
zyxelTimeRangeAbsoluteTable = _ZyxelTimeRangeAbsoluteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelTimeRangeAbsoluteTable.setStatus("current")
_ZyxelTimeRangeAbsoluteEntry_Object = MibTableRow
zyxelTimeRangeAbsoluteEntry = _ZyxelTimeRangeAbsoluteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 3, 1)
)
zyxelTimeRangeAbsoluteEntry.setIndexNames(
    (0, "ZYXEL-TIME-RANGE-MIB", "zyTimeRangeName"),
    (0, "ZYXEL-TIME-RANGE-MIB", "zyTimeRangeType"),
)
if mibBuilder.loadTexts:
    zyxelTimeRangeAbsoluteEntry.setStatus("current")
_ZyTimeRangeAbsoluteStartYear_Type = Integer32
_ZyTimeRangeAbsoluteStartYear_Object = MibTableColumn
zyTimeRangeAbsoluteStartYear = _ZyTimeRangeAbsoluteStartYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 3, 1, 1),
    _ZyTimeRangeAbsoluteStartYear_Type()
)
zyTimeRangeAbsoluteStartYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangeAbsoluteStartYear.setStatus("current")
_ZyTimeRangeAbsoluteStartMonth_Type = Integer32
_ZyTimeRangeAbsoluteStartMonth_Object = MibTableColumn
zyTimeRangeAbsoluteStartMonth = _ZyTimeRangeAbsoluteStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 3, 1, 2),
    _ZyTimeRangeAbsoluteStartMonth_Type()
)
zyTimeRangeAbsoluteStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangeAbsoluteStartMonth.setStatus("current")
_ZyTimeRangeAbsoluteStartDate_Type = Integer32
_ZyTimeRangeAbsoluteStartDate_Object = MibTableColumn
zyTimeRangeAbsoluteStartDate = _ZyTimeRangeAbsoluteStartDate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 3, 1, 3),
    _ZyTimeRangeAbsoluteStartDate_Type()
)
zyTimeRangeAbsoluteStartDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangeAbsoluteStartDate.setStatus("current")
_ZyTimeRangeAbsoluteStartHour_Type = Integer32
_ZyTimeRangeAbsoluteStartHour_Object = MibTableColumn
zyTimeRangeAbsoluteStartHour = _ZyTimeRangeAbsoluteStartHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 3, 1, 4),
    _ZyTimeRangeAbsoluteStartHour_Type()
)
zyTimeRangeAbsoluteStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangeAbsoluteStartHour.setStatus("current")
_ZyTimeRangeAbsoluteStartMinute_Type = Integer32
_ZyTimeRangeAbsoluteStartMinute_Object = MibTableColumn
zyTimeRangeAbsoluteStartMinute = _ZyTimeRangeAbsoluteStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 3, 1, 5),
    _ZyTimeRangeAbsoluteStartMinute_Type()
)
zyTimeRangeAbsoluteStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangeAbsoluteStartMinute.setStatus("current")
_ZyTimeRangeAbsoluteEndYear_Type = Integer32
_ZyTimeRangeAbsoluteEndYear_Object = MibTableColumn
zyTimeRangeAbsoluteEndYear = _ZyTimeRangeAbsoluteEndYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 3, 1, 6),
    _ZyTimeRangeAbsoluteEndYear_Type()
)
zyTimeRangeAbsoluteEndYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangeAbsoluteEndYear.setStatus("current")
_ZyTimeRangeAbsoluteEndMonth_Type = Integer32
_ZyTimeRangeAbsoluteEndMonth_Object = MibTableColumn
zyTimeRangeAbsoluteEndMonth = _ZyTimeRangeAbsoluteEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 3, 1, 7),
    _ZyTimeRangeAbsoluteEndMonth_Type()
)
zyTimeRangeAbsoluteEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangeAbsoluteEndMonth.setStatus("current")
_ZyTimeRangeAbsoluteEndDate_Type = Integer32
_ZyTimeRangeAbsoluteEndDate_Object = MibTableColumn
zyTimeRangeAbsoluteEndDate = _ZyTimeRangeAbsoluteEndDate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 3, 1, 8),
    _ZyTimeRangeAbsoluteEndDate_Type()
)
zyTimeRangeAbsoluteEndDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangeAbsoluteEndDate.setStatus("current")
_ZyTimeRangeAbsoluteEndHour_Type = Integer32
_ZyTimeRangeAbsoluteEndHour_Object = MibTableColumn
zyTimeRangeAbsoluteEndHour = _ZyTimeRangeAbsoluteEndHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 3, 1, 9),
    _ZyTimeRangeAbsoluteEndHour_Type()
)
zyTimeRangeAbsoluteEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangeAbsoluteEndHour.setStatus("current")
_ZyTimeRangeAbsoluteEndMinute_Type = Integer32
_ZyTimeRangeAbsoluteEndMinute_Object = MibTableColumn
zyTimeRangeAbsoluteEndMinute = _ZyTimeRangeAbsoluteEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 3, 1, 10),
    _ZyTimeRangeAbsoluteEndMinute_Type()
)
zyTimeRangeAbsoluteEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangeAbsoluteEndMinute.setStatus("current")
_ZyxelTimeRangePeriodicTable_Object = MibTable
zyxelTimeRangePeriodicTable = _ZyxelTimeRangePeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelTimeRangePeriodicTable.setStatus("current")
_ZyxelTimeRangePeriodicEntry_Object = MibTableRow
zyxelTimeRangePeriodicEntry = _ZyxelTimeRangePeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 4, 1)
)
zyxelTimeRangePeriodicEntry.setIndexNames(
    (0, "ZYXEL-TIME-RANGE-MIB", "zyTimeRangeName"),
    (0, "ZYXEL-TIME-RANGE-MIB", "zyTimeRangeType"),
)
if mibBuilder.loadTexts:
    zyxelTimeRangePeriodicEntry.setStatus("current")


class _ZyTimeRangePeriodicWeekDayList_Type(Bits):
    """Custom type zyTimeRangePeriodicWeekDayList based on Bits"""
    namedValues = NamedValues(
        *(("friday", 4),
          ("monday", 0),
          ("saturday", 5),
          ("sunday", 6),
          ("thursday", 3),
          ("tuesday", 1),
          ("wednesday", 2))
    )

_ZyTimeRangePeriodicWeekDayList_Type.__name__ = "Bits"
_ZyTimeRangePeriodicWeekDayList_Object = MibTableColumn
zyTimeRangePeriodicWeekDayList = _ZyTimeRangePeriodicWeekDayList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 4, 1, 1),
    _ZyTimeRangePeriodicWeekDayList_Type()
)
zyTimeRangePeriodicWeekDayList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangePeriodicWeekDayList.setStatus("current")


class _ZyTimeRangePeriodicStartWeekDay_Type(Integer32):
    """Custom type zyTimeRangePeriodicStartWeekDay based on Integer32"""
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
        *(("friday", 5),
          ("monday", 1),
          ("none", 0),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_ZyTimeRangePeriodicStartWeekDay_Type.__name__ = "Integer32"
_ZyTimeRangePeriodicStartWeekDay_Object = MibTableColumn
zyTimeRangePeriodicStartWeekDay = _ZyTimeRangePeriodicStartWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 4, 1, 2),
    _ZyTimeRangePeriodicStartWeekDay_Type()
)
zyTimeRangePeriodicStartWeekDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangePeriodicStartWeekDay.setStatus("current")
_ZyTimeRangePeriodicStartHour_Type = Integer32
_ZyTimeRangePeriodicStartHour_Object = MibTableColumn
zyTimeRangePeriodicStartHour = _ZyTimeRangePeriodicStartHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 4, 1, 3),
    _ZyTimeRangePeriodicStartHour_Type()
)
zyTimeRangePeriodicStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangePeriodicStartHour.setStatus("current")
_ZyTimeRangePeriodicStartMinute_Type = Integer32
_ZyTimeRangePeriodicStartMinute_Object = MibTableColumn
zyTimeRangePeriodicStartMinute = _ZyTimeRangePeriodicStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 4, 1, 4),
    _ZyTimeRangePeriodicStartMinute_Type()
)
zyTimeRangePeriodicStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangePeriodicStartMinute.setStatus("current")


class _ZyTimeRangePeriodicEndWeekDay_Type(Integer32):
    """Custom type zyTimeRangePeriodicEndWeekDay based on Integer32"""
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
        *(("friday", 5),
          ("monday", 1),
          ("none", 0),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_ZyTimeRangePeriodicEndWeekDay_Type.__name__ = "Integer32"
_ZyTimeRangePeriodicEndWeekDay_Object = MibTableColumn
zyTimeRangePeriodicEndWeekDay = _ZyTimeRangePeriodicEndWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 4, 1, 5),
    _ZyTimeRangePeriodicEndWeekDay_Type()
)
zyTimeRangePeriodicEndWeekDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangePeriodicEndWeekDay.setStatus("current")
_ZyTimeRangePeriodicEndHour_Type = Integer32
_ZyTimeRangePeriodicEndHour_Object = MibTableColumn
zyTimeRangePeriodicEndHour = _ZyTimeRangePeriodicEndHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 4, 1, 6),
    _ZyTimeRangePeriodicEndHour_Type()
)
zyTimeRangePeriodicEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangePeriodicEndHour.setStatus("current")
_ZyTimeRangePeriodicEndMinute_Type = Integer32
_ZyTimeRangePeriodicEndMinute_Object = MibTableColumn
zyTimeRangePeriodicEndMinute = _ZyTimeRangePeriodicEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 98, 1, 4, 1, 7),
    _ZyTimeRangePeriodicEndMinute_Type()
)
zyTimeRangePeriodicEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTimeRangePeriodicEndMinute.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-TIME-RANGE-MIB",
    **{"ZyTimeRangeWeekDayList": ZyTimeRangeWeekDayList,
       "zyxelTimeRange": zyxelTimeRange,
       "zyxelTimeRangeSetup": zyxelTimeRangeSetup,
       "zyTimeRangeMaxNumberOfProfiles": zyTimeRangeMaxNumberOfProfiles,
       "zyxelTimeRangeTable": zyxelTimeRangeTable,
       "zyxelTimeRangeEntry": zyxelTimeRangeEntry,
       "zyTimeRangeName": zyTimeRangeName,
       "zyTimeRangeType": zyTimeRangeType,
       "zyTimeRangeRowStatus": zyTimeRangeRowStatus,
       "zyxelTimeRangeAbsoluteTable": zyxelTimeRangeAbsoluteTable,
       "zyxelTimeRangeAbsoluteEntry": zyxelTimeRangeAbsoluteEntry,
       "zyTimeRangeAbsoluteStartYear": zyTimeRangeAbsoluteStartYear,
       "zyTimeRangeAbsoluteStartMonth": zyTimeRangeAbsoluteStartMonth,
       "zyTimeRangeAbsoluteStartDate": zyTimeRangeAbsoluteStartDate,
       "zyTimeRangeAbsoluteStartHour": zyTimeRangeAbsoluteStartHour,
       "zyTimeRangeAbsoluteStartMinute": zyTimeRangeAbsoluteStartMinute,
       "zyTimeRangeAbsoluteEndYear": zyTimeRangeAbsoluteEndYear,
       "zyTimeRangeAbsoluteEndMonth": zyTimeRangeAbsoluteEndMonth,
       "zyTimeRangeAbsoluteEndDate": zyTimeRangeAbsoluteEndDate,
       "zyTimeRangeAbsoluteEndHour": zyTimeRangeAbsoluteEndHour,
       "zyTimeRangeAbsoluteEndMinute": zyTimeRangeAbsoluteEndMinute,
       "zyxelTimeRangePeriodicTable": zyxelTimeRangePeriodicTable,
       "zyxelTimeRangePeriodicEntry": zyxelTimeRangePeriodicEntry,
       "zyTimeRangePeriodicWeekDayList": zyTimeRangePeriodicWeekDayList,
       "zyTimeRangePeriodicStartWeekDay": zyTimeRangePeriodicStartWeekDay,
       "zyTimeRangePeriodicStartHour": zyTimeRangePeriodicStartHour,
       "zyTimeRangePeriodicStartMinute": zyTimeRangePeriodicStartMinute,
       "zyTimeRangePeriodicEndWeekDay": zyTimeRangePeriodicEndWeekDay,
       "zyTimeRangePeriodicEndHour": zyTimeRangePeriodicEndHour,
       "zyTimeRangePeriodicEndMinute": zyTimeRangePeriodicEndMinute}
)
