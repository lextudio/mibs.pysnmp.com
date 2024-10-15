# SNMP MIB module (HM2-PLATFORM-TIMERANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-TIMERANGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:26 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hm2PlatformTimeRange = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 53)
)
hm2PlatformTimeRange.setRevisions(
        ("2011-01-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2AgentTimeRangeAbsoluteDateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class Hm2AgentTimeRangePeriodicTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



# MIB Managed Objects in the order of their OIDs

_Hm2AgentTimeRangeGroup_ObjectIdentity = ObjectIdentity
hm2AgentTimeRangeGroup = _Hm2AgentTimeRangeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1)
)
_Hm2AgentTimeRangeIndexNextFree_Type = Integer32
_Hm2AgentTimeRangeIndexNextFree_Object = MibScalar
hm2AgentTimeRangeIndexNextFree = _Hm2AgentTimeRangeIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 1),
    _Hm2AgentTimeRangeIndexNextFree_Type()
)
hm2AgentTimeRangeIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentTimeRangeIndexNextFree.setStatus("current")
_Hm2AgentTimeRangeTable_Object = MibTable
hm2AgentTimeRangeTable = _Hm2AgentTimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 2)
)
if mibBuilder.loadTexts:
    hm2AgentTimeRangeTable.setStatus("current")
_Hm2AgentTimeRangeEntry_Object = MibTableRow
hm2AgentTimeRangeEntry = _Hm2AgentTimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 2, 1)
)
hm2AgentTimeRangeEntry.setIndexNames(
    (0, "HM2-PLATFORM-TIMERANGE-MIB", "hm2AgentTimeRangeIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentTimeRangeEntry.setStatus("current")
_Hm2AgentTimeRangeIndex_Type = Unsigned32
_Hm2AgentTimeRangeIndex_Object = MibTableColumn
hm2AgentTimeRangeIndex = _Hm2AgentTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 2, 1, 1),
    _Hm2AgentTimeRangeIndex_Type()
)
hm2AgentTimeRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentTimeRangeIndex.setStatus("current")


class _Hm2AgentTimeRangeName_Type(DisplayString):
    """Custom type hm2AgentTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hm2AgentTimeRangeName_Type.__name__ = "DisplayString"
_Hm2AgentTimeRangeName_Object = MibTableColumn
hm2AgentTimeRangeName = _Hm2AgentTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 2, 1, 2),
    _Hm2AgentTimeRangeName_Type()
)
hm2AgentTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentTimeRangeName.setStatus("current")


class _Hm2AgentTimeRangeOperState_Type(Integer32):
    """Custom type hm2AgentTimeRangeOperState based on Integer32"""
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


_Hm2AgentTimeRangeOperState_Type.__name__ = "Integer32"
_Hm2AgentTimeRangeOperState_Object = MibTableColumn
hm2AgentTimeRangeOperState = _Hm2AgentTimeRangeOperState_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 2, 1, 3),
    _Hm2AgentTimeRangeOperState_Type()
)
hm2AgentTimeRangeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentTimeRangeOperState.setStatus("current")
_Hm2AgentTimeRangeStatus_Type = RowStatus
_Hm2AgentTimeRangeStatus_Object = MibTableColumn
hm2AgentTimeRangeStatus = _Hm2AgentTimeRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 2, 1, 4),
    _Hm2AgentTimeRangeStatus_Type()
)
hm2AgentTimeRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentTimeRangeStatus.setStatus("current")
_Hm2AgentTimeRangeAbsoluteTable_Object = MibTable
hm2AgentTimeRangeAbsoluteTable = _Hm2AgentTimeRangeAbsoluteTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 3)
)
if mibBuilder.loadTexts:
    hm2AgentTimeRangeAbsoluteTable.setStatus("current")
_Hm2AgentTimeRangeAbsoluteEntry_Object = MibTableRow
hm2AgentTimeRangeAbsoluteEntry = _Hm2AgentTimeRangeAbsoluteEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 3, 1)
)
hm2AgentTimeRangeAbsoluteEntry.setIndexNames(
    (0, "HM2-PLATFORM-TIMERANGE-MIB", "hm2AgentTimeRangeIndex"),
    (0, "HM2-PLATFORM-TIMERANGE-MIB", "hm2AgentTimeRangeAbsoluteEntryIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentTimeRangeAbsoluteEntry.setStatus("current")


class _Hm2AgentTimeRangeAbsoluteEntryIndex_Type(Integer32):
    """Custom type hm2AgentTimeRangeAbsoluteEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Hm2AgentTimeRangeAbsoluteEntryIndex_Type.__name__ = "Integer32"
_Hm2AgentTimeRangeAbsoluteEntryIndex_Object = MibTableColumn
hm2AgentTimeRangeAbsoluteEntryIndex = _Hm2AgentTimeRangeAbsoluteEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 3, 1, 1),
    _Hm2AgentTimeRangeAbsoluteEntryIndex_Type()
)
hm2AgentTimeRangeAbsoluteEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentTimeRangeAbsoluteEntryIndex.setStatus("current")
_Hm2AgentTimeRangeAbsoluteStartDateAndTime_Type = Hm2AgentTimeRangeAbsoluteDateAndTime
_Hm2AgentTimeRangeAbsoluteStartDateAndTime_Object = MibTableColumn
hm2AgentTimeRangeAbsoluteStartDateAndTime = _Hm2AgentTimeRangeAbsoluteStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 3, 1, 2),
    _Hm2AgentTimeRangeAbsoluteStartDateAndTime_Type()
)
hm2AgentTimeRangeAbsoluteStartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentTimeRangeAbsoluteStartDateAndTime.setStatus("current")
_Hm2AgentTimeRangeAbsoluteEndDateAndTime_Type = Hm2AgentTimeRangeAbsoluteDateAndTime
_Hm2AgentTimeRangeAbsoluteEndDateAndTime_Object = MibTableColumn
hm2AgentTimeRangeAbsoluteEndDateAndTime = _Hm2AgentTimeRangeAbsoluteEndDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 3, 1, 3),
    _Hm2AgentTimeRangeAbsoluteEndDateAndTime_Type()
)
hm2AgentTimeRangeAbsoluteEndDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentTimeRangeAbsoluteEndDateAndTime.setStatus("current")
_Hm2AgentTimeRangeAbsoluteStatus_Type = RowStatus
_Hm2AgentTimeRangeAbsoluteStatus_Object = MibTableColumn
hm2AgentTimeRangeAbsoluteStatus = _Hm2AgentTimeRangeAbsoluteStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 3, 1, 4),
    _Hm2AgentTimeRangeAbsoluteStatus_Type()
)
hm2AgentTimeRangeAbsoluteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentTimeRangeAbsoluteStatus.setStatus("current")
_Hm2AgentTimeRangePeriodicTable_Object = MibTable
hm2AgentTimeRangePeriodicTable = _Hm2AgentTimeRangePeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4)
)
if mibBuilder.loadTexts:
    hm2AgentTimeRangePeriodicTable.setStatus("current")
_Hm2AgentTimeRangePeriodicEntry_Object = MibTableRow
hm2AgentTimeRangePeriodicEntry = _Hm2AgentTimeRangePeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1)
)
hm2AgentTimeRangePeriodicEntry.setIndexNames(
    (0, "HM2-PLATFORM-TIMERANGE-MIB", "hm2AgentTimeRangeIndex"),
    (0, "HM2-PLATFORM-TIMERANGE-MIB", "hm2AgentTimeRangePeriodicEntryIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentTimeRangePeriodicEntry.setStatus("current")


class _Hm2AgentTimeRangePeriodicEntryIndex_Type(Integer32):
    """Custom type hm2AgentTimeRangePeriodicEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Hm2AgentTimeRangePeriodicEntryIndex_Type.__name__ = "Integer32"
_Hm2AgentTimeRangePeriodicEntryIndex_Object = MibTableColumn
hm2AgentTimeRangePeriodicEntryIndex = _Hm2AgentTimeRangePeriodicEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1, 1),
    _Hm2AgentTimeRangePeriodicEntryIndex_Type()
)
hm2AgentTimeRangePeriodicEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentTimeRangePeriodicEntryIndex.setStatus("current")


class _Hm2AgentTimeRangePeriodicStartDay_Type(Bits):
    """Custom type hm2AgentTimeRangePeriodicStartDay based on Bits"""
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )

_Hm2AgentTimeRangePeriodicStartDay_Type.__name__ = "Bits"
_Hm2AgentTimeRangePeriodicStartDay_Object = MibTableColumn
hm2AgentTimeRangePeriodicStartDay = _Hm2AgentTimeRangePeriodicStartDay_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1, 2),
    _Hm2AgentTimeRangePeriodicStartDay_Type()
)
hm2AgentTimeRangePeriodicStartDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentTimeRangePeriodicStartDay.setStatus("current")
_Hm2AgentTimeRangePeriodicStartTime_Type = Hm2AgentTimeRangePeriodicTime
_Hm2AgentTimeRangePeriodicStartTime_Object = MibTableColumn
hm2AgentTimeRangePeriodicStartTime = _Hm2AgentTimeRangePeriodicStartTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1, 3),
    _Hm2AgentTimeRangePeriodicStartTime_Type()
)
hm2AgentTimeRangePeriodicStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentTimeRangePeriodicStartTime.setStatus("current")


class _Hm2AgentTimeRangePeriodicEndDay_Type(Bits):
    """Custom type hm2AgentTimeRangePeriodicEndDay based on Bits"""
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )

_Hm2AgentTimeRangePeriodicEndDay_Type.__name__ = "Bits"
_Hm2AgentTimeRangePeriodicEndDay_Object = MibTableColumn
hm2AgentTimeRangePeriodicEndDay = _Hm2AgentTimeRangePeriodicEndDay_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1, 4),
    _Hm2AgentTimeRangePeriodicEndDay_Type()
)
hm2AgentTimeRangePeriodicEndDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentTimeRangePeriodicEndDay.setStatus("current")
_Hm2AgentTimeRangePeriodicEndTime_Type = Hm2AgentTimeRangePeriodicTime
_Hm2AgentTimeRangePeriodicEndTime_Object = MibTableColumn
hm2AgentTimeRangePeriodicEndTime = _Hm2AgentTimeRangePeriodicEndTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1, 5),
    _Hm2AgentTimeRangePeriodicEndTime_Type()
)
hm2AgentTimeRangePeriodicEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentTimeRangePeriodicEndTime.setStatus("current")
_Hm2AgentTimeRangePeriodicStatus_Type = RowStatus
_Hm2AgentTimeRangePeriodicStatus_Object = MibTableColumn
hm2AgentTimeRangePeriodicStatus = _Hm2AgentTimeRangePeriodicStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1, 6),
    _Hm2AgentTimeRangePeriodicStatus_Type()
)
hm2AgentTimeRangePeriodicStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentTimeRangePeriodicStatus.setStatus("current")


class _Hm2AgentTimeRangeAdminMode_Type(Integer32):
    """Custom type hm2AgentTimeRangeAdminMode based on Integer32"""
    defaultValue = 1

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


_Hm2AgentTimeRangeAdminMode_Type.__name__ = "Integer32"
_Hm2AgentTimeRangeAdminMode_Object = MibScalar
hm2AgentTimeRangeAdminMode = _Hm2AgentTimeRangeAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 248),
    _Hm2AgentTimeRangeAdminMode_Type()
)
hm2AgentTimeRangeAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentTimeRangeAdminMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-TIMERANGE-MIB",
    **{"Hm2AgentTimeRangeAbsoluteDateAndTime": Hm2AgentTimeRangeAbsoluteDateAndTime,
       "Hm2AgentTimeRangePeriodicTime": Hm2AgentTimeRangePeriodicTime,
       "hm2PlatformTimeRange": hm2PlatformTimeRange,
       "hm2AgentTimeRangeGroup": hm2AgentTimeRangeGroup,
       "hm2AgentTimeRangeIndexNextFree": hm2AgentTimeRangeIndexNextFree,
       "hm2AgentTimeRangeTable": hm2AgentTimeRangeTable,
       "hm2AgentTimeRangeEntry": hm2AgentTimeRangeEntry,
       "hm2AgentTimeRangeIndex": hm2AgentTimeRangeIndex,
       "hm2AgentTimeRangeName": hm2AgentTimeRangeName,
       "hm2AgentTimeRangeOperState": hm2AgentTimeRangeOperState,
       "hm2AgentTimeRangeStatus": hm2AgentTimeRangeStatus,
       "hm2AgentTimeRangeAbsoluteTable": hm2AgentTimeRangeAbsoluteTable,
       "hm2AgentTimeRangeAbsoluteEntry": hm2AgentTimeRangeAbsoluteEntry,
       "hm2AgentTimeRangeAbsoluteEntryIndex": hm2AgentTimeRangeAbsoluteEntryIndex,
       "hm2AgentTimeRangeAbsoluteStartDateAndTime": hm2AgentTimeRangeAbsoluteStartDateAndTime,
       "hm2AgentTimeRangeAbsoluteEndDateAndTime": hm2AgentTimeRangeAbsoluteEndDateAndTime,
       "hm2AgentTimeRangeAbsoluteStatus": hm2AgentTimeRangeAbsoluteStatus,
       "hm2AgentTimeRangePeriodicTable": hm2AgentTimeRangePeriodicTable,
       "hm2AgentTimeRangePeriodicEntry": hm2AgentTimeRangePeriodicEntry,
       "hm2AgentTimeRangePeriodicEntryIndex": hm2AgentTimeRangePeriodicEntryIndex,
       "hm2AgentTimeRangePeriodicStartDay": hm2AgentTimeRangePeriodicStartDay,
       "hm2AgentTimeRangePeriodicStartTime": hm2AgentTimeRangePeriodicStartTime,
       "hm2AgentTimeRangePeriodicEndDay": hm2AgentTimeRangePeriodicEndDay,
       "hm2AgentTimeRangePeriodicEndTime": hm2AgentTimeRangePeriodicEndTime,
       "hm2AgentTimeRangePeriodicStatus": hm2AgentTimeRangePeriodicStatus,
       "hm2AgentTimeRangeAdminMode": hm2AgentTimeRangeAdminMode}
)
