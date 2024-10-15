# SNMP MIB module (EdgeSwitch-TIMERANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EdgeSwitch-TIMERANGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:10 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathTimeRange = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53)
)
fastPathTimeRange.setRevisions(
        ("2011-01-26 00:00",
         "2009-09-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TimeRangeAbsoluteDateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class TimeRangePeriodicTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class TimeRangePeriodicDate(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_FastPathTimeRangeGroup_ObjectIdentity = ObjectIdentity
fastPathTimeRangeGroup = _FastPathTimeRangeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1)
)


class _TimeRangeAdminMode_Type(Integer32):
    """Custom type timeRangeAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TimeRangeAdminMode_Type.__name__ = "Integer32"
_TimeRangeAdminMode_Object = MibScalar
timeRangeAdminMode = _TimeRangeAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 1),
    _TimeRangeAdminMode_Type()
)
timeRangeAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRangeAdminMode.setStatus("current")
_TimeRangeIndexNextFree_Type = Integer32
_TimeRangeIndexNextFree_Object = MibScalar
timeRangeIndexNextFree = _TimeRangeIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 2),
    _TimeRangeIndexNextFree_Type()
)
timeRangeIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRangeIndexNextFree.setStatus("current")
_TimeRangeTable_Object = MibTable
timeRangeTable = _TimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 3)
)
if mibBuilder.loadTexts:
    timeRangeTable.setStatus("current")
_TimeRangeEntry_Object = MibTableRow
timeRangeEntry = _TimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 3, 1)
)
timeRangeEntry.setIndexNames(
    (0, "EdgeSwitch-TIMERANGE-MIB", "timeRangeIndex"),
)
if mibBuilder.loadTexts:
    timeRangeEntry.setStatus("current")
_TimeRangeIndex_Type = Unsigned32
_TimeRangeIndex_Object = MibTableColumn
timeRangeIndex = _TimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 3, 1, 1),
    _TimeRangeIndex_Type()
)
timeRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeIndex.setStatus("current")


class _TimeRangeName_Type(DisplayString):
    """Custom type timeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_TimeRangeName_Type.__name__ = "DisplayString"
_TimeRangeName_Object = MibTableColumn
timeRangeName = _TimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 3, 1, 2),
    _TimeRangeName_Type()
)
timeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeName.setStatus("current")


class _TimeRangeOperState_Type(Integer32):
    """Custom type timeRangeOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_TimeRangeOperState_Type.__name__ = "Integer32"
_TimeRangeOperState_Object = MibTableColumn
timeRangeOperState = _TimeRangeOperState_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 3, 1, 3),
    _TimeRangeOperState_Type()
)
timeRangeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRangeOperState.setStatus("current")
_TimeRangeStatus_Type = RowStatus
_TimeRangeStatus_Object = MibTableColumn
timeRangeStatus = _TimeRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 3, 1, 4),
    _TimeRangeStatus_Type()
)
timeRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeStatus.setStatus("current")
_TimeRangeAbsoluteEntryTable_Object = MibTable
timeRangeAbsoluteEntryTable = _TimeRangeAbsoluteEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 4)
)
if mibBuilder.loadTexts:
    timeRangeAbsoluteEntryTable.setStatus("current")
_TimeRangeAbsoluteEntry_Object = MibTableRow
timeRangeAbsoluteEntry = _TimeRangeAbsoluteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 4, 1)
)
timeRangeAbsoluteEntry.setIndexNames(
    (0, "EdgeSwitch-TIMERANGE-MIB", "timeRangeIndex"),
    (0, "EdgeSwitch-TIMERANGE-MIB", "timeRangeAbsoluteEntryIndex"),
)
if mibBuilder.loadTexts:
    timeRangeAbsoluteEntry.setStatus("current")


class _TimeRangeAbsoluteEntryIndex_Type(Integer32):
    """Custom type timeRangeAbsoluteEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TimeRangeAbsoluteEntryIndex_Type.__name__ = "Integer32"
_TimeRangeAbsoluteEntryIndex_Object = MibTableColumn
timeRangeAbsoluteEntryIndex = _TimeRangeAbsoluteEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 4, 1, 1),
    _TimeRangeAbsoluteEntryIndex_Type()
)
timeRangeAbsoluteEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeAbsoluteEntryIndex.setStatus("current")
_TimeRangeAbsoluteStartDateAndTime_Type = TimeRangeAbsoluteDateAndTime
_TimeRangeAbsoluteStartDateAndTime_Object = MibTableColumn
timeRangeAbsoluteStartDateAndTime = _TimeRangeAbsoluteStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 4, 1, 2),
    _TimeRangeAbsoluteStartDateAndTime_Type()
)
timeRangeAbsoluteStartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeAbsoluteStartDateAndTime.setStatus("current")
_TimeRangeAbsoluteEndDateAndTime_Type = TimeRangeAbsoluteDateAndTime
_TimeRangeAbsoluteEndDateAndTime_Object = MibTableColumn
timeRangeAbsoluteEndDateAndTime = _TimeRangeAbsoluteEndDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 4, 1, 3),
    _TimeRangeAbsoluteEndDateAndTime_Type()
)
timeRangeAbsoluteEndDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeAbsoluteEndDateAndTime.setStatus("current")
_TimeRangeAbsoluteStatus_Type = RowStatus
_TimeRangeAbsoluteStatus_Object = MibTableColumn
timeRangeAbsoluteStatus = _TimeRangeAbsoluteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 4, 1, 4),
    _TimeRangeAbsoluteStatus_Type()
)
timeRangeAbsoluteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeAbsoluteStatus.setStatus("current")
_TimeRangePeriodicEntryTable_Object = MibTable
timeRangePeriodicEntryTable = _TimeRangePeriodicEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5)
)
if mibBuilder.loadTexts:
    timeRangePeriodicEntryTable.setStatus("current")
_TimeRangePeriodicEntry_Object = MibTableRow
timeRangePeriodicEntry = _TimeRangePeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1)
)
timeRangePeriodicEntry.setIndexNames(
    (0, "EdgeSwitch-TIMERANGE-MIB", "timeRangeIndex"),
    (0, "EdgeSwitch-TIMERANGE-MIB", "timeRangePeriodicEntryIndex"),
)
if mibBuilder.loadTexts:
    timeRangePeriodicEntry.setStatus("current")


class _TimeRangePeriodicEntryIndex_Type(Integer32):
    """Custom type timeRangePeriodicEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TimeRangePeriodicEntryIndex_Type.__name__ = "Integer32"
_TimeRangePeriodicEntryIndex_Object = MibTableColumn
timeRangePeriodicEntryIndex = _TimeRangePeriodicEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 1),
    _TimeRangePeriodicEntryIndex_Type()
)
timeRangePeriodicEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangePeriodicEntryIndex.setStatus("current")


class _TimeRangePeriodicFrequency_Type(Integer32):
    """Custom type timeRangePeriodicFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TimeRangePeriodicFrequency_Type.__name__ = "Integer32"
_TimeRangePeriodicFrequency_Object = MibTableColumn
timeRangePeriodicFrequency = _TimeRangePeriodicFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 2),
    _TimeRangePeriodicFrequency_Type()
)
timeRangePeriodicFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicFrequency.setStatus("current")


class _TimeRangePeriodicPattern_Type(Integer32):
    """Custom type timeRangePeriodicPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TimeRangePeriodicPattern_Type.__name__ = "Integer32"
_TimeRangePeriodicPattern_Object = MibTableColumn
timeRangePeriodicPattern = _TimeRangePeriodicPattern_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 3),
    _TimeRangePeriodicPattern_Type()
)
timeRangePeriodicPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicPattern.setStatus("current")
_TimeRangePeriodicDayMask_Type = Integer32
_TimeRangePeriodicDayMask_Object = MibTableColumn
timeRangePeriodicDayMask = _TimeRangePeriodicDayMask_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 4),
    _TimeRangePeriodicDayMask_Type()
)
timeRangePeriodicDayMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicDayMask.setStatus("current")
_TimeRangePeriodicStartDate_Type = TimeRangePeriodicDate
_TimeRangePeriodicStartDate_Object = MibTableColumn
timeRangePeriodicStartDate = _TimeRangePeriodicStartDate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 5),
    _TimeRangePeriodicStartDate_Type()
)
timeRangePeriodicStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicStartDate.setStatus("current")


class _TimeRangePeriodicStartDay_Type(Bits):
    """Custom type timeRangePeriodicStartDay based on Bits"""
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )

_TimeRangePeriodicStartDay_Type.__name__ = "Bits"
_TimeRangePeriodicStartDay_Object = MibTableColumn
timeRangePeriodicStartDay = _TimeRangePeriodicStartDay_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 6),
    _TimeRangePeriodicStartDay_Type()
)
timeRangePeriodicStartDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicStartDay.setStatus("current")
_TimeRangePeriodicStartTime_Type = TimeRangePeriodicTime
_TimeRangePeriodicStartTime_Object = MibTableColumn
timeRangePeriodicStartTime = _TimeRangePeriodicStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 7),
    _TimeRangePeriodicStartTime_Type()
)
timeRangePeriodicStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicStartTime.setStatus("current")
_TimeRangePeriodicEndDate_Type = TimeRangePeriodicDate
_TimeRangePeriodicEndDate_Object = MibTableColumn
timeRangePeriodicEndDate = _TimeRangePeriodicEndDate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 8),
    _TimeRangePeriodicEndDate_Type()
)
timeRangePeriodicEndDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicEndDate.setStatus("current")


class _TimeRangePeriodicEndDay_Type(Bits):
    """Custom type timeRangePeriodicEndDay based on Bits"""
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )

_TimeRangePeriodicEndDay_Type.__name__ = "Bits"
_TimeRangePeriodicEndDay_Object = MibTableColumn
timeRangePeriodicEndDay = _TimeRangePeriodicEndDay_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 9),
    _TimeRangePeriodicEndDay_Type()
)
timeRangePeriodicEndDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicEndDay.setStatus("current")
_TimeRangePeriodicEndTime_Type = TimeRangePeriodicTime
_TimeRangePeriodicEndTime_Object = MibTableColumn
timeRangePeriodicEndTime = _TimeRangePeriodicEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 10),
    _TimeRangePeriodicEndTime_Type()
)
timeRangePeriodicEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicEndTime.setStatus("current")
_TimeRangePeriodicStatus_Type = RowStatus
_TimeRangePeriodicStatus_Object = MibTableColumn
timeRangePeriodicStatus = _TimeRangePeriodicStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 53, 1, 5, 1, 11),
    _TimeRangePeriodicStatus_Type()
)
timeRangePeriodicStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EdgeSwitch-TIMERANGE-MIB",
    **{"TimeRangeAbsoluteDateAndTime": TimeRangeAbsoluteDateAndTime,
       "TimeRangePeriodicTime": TimeRangePeriodicTime,
       "TimeRangePeriodicDate": TimeRangePeriodicDate,
       "fastPathTimeRange": fastPathTimeRange,
       "fastPathTimeRangeGroup": fastPathTimeRangeGroup,
       "timeRangeAdminMode": timeRangeAdminMode,
       "timeRangeIndexNextFree": timeRangeIndexNextFree,
       "timeRangeTable": timeRangeTable,
       "timeRangeEntry": timeRangeEntry,
       "timeRangeIndex": timeRangeIndex,
       "timeRangeName": timeRangeName,
       "timeRangeOperState": timeRangeOperState,
       "timeRangeStatus": timeRangeStatus,
       "timeRangeAbsoluteEntryTable": timeRangeAbsoluteEntryTable,
       "timeRangeAbsoluteEntry": timeRangeAbsoluteEntry,
       "timeRangeAbsoluteEntryIndex": timeRangeAbsoluteEntryIndex,
       "timeRangeAbsoluteStartDateAndTime": timeRangeAbsoluteStartDateAndTime,
       "timeRangeAbsoluteEndDateAndTime": timeRangeAbsoluteEndDateAndTime,
       "timeRangeAbsoluteStatus": timeRangeAbsoluteStatus,
       "timeRangePeriodicEntryTable": timeRangePeriodicEntryTable,
       "timeRangePeriodicEntry": timeRangePeriodicEntry,
       "timeRangePeriodicEntryIndex": timeRangePeriodicEntryIndex,
       "timeRangePeriodicFrequency": timeRangePeriodicFrequency,
       "timeRangePeriodicPattern": timeRangePeriodicPattern,
       "timeRangePeriodicDayMask": timeRangePeriodicDayMask,
       "timeRangePeriodicStartDate": timeRangePeriodicStartDate,
       "timeRangePeriodicStartDay": timeRangePeriodicStartDay,
       "timeRangePeriodicStartTime": timeRangePeriodicStartTime,
       "timeRangePeriodicEndDate": timeRangePeriodicEndDate,
       "timeRangePeriodicEndDay": timeRangePeriodicEndDay,
       "timeRangePeriodicEndTime": timeRangePeriodicEndTime,
       "timeRangePeriodicStatus": timeRangePeriodicStatus}
)
