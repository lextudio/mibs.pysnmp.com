# SNMP MIB module (HH3C-SYS-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-SYS-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:03 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(SnmpTagList,
 SnmpTagValue) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagList",
    "SnmpTagValue")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cSystemMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3)
)
hh3cSystemMan.setRevisions(
        ("2004-04-08 13:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSystemManMIBObjects_ObjectIdentity = ObjectIdentity
hh3cSystemManMIBObjects = _Hh3cSystemManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1)
)
_Hh3cSysClock_ObjectIdentity = ObjectIdentity
hh3cSysClock = _Hh3cSysClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1)
)
_Hh3cSysLocalClock_Type = DateAndTime
_Hh3cSysLocalClock_Object = MibScalar
hh3cSysLocalClock = _Hh3cSysLocalClock_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 1),
    _Hh3cSysLocalClock_Type()
)
hh3cSysLocalClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysLocalClock.setStatus("current")
_Hh3cSysSummerTime_ObjectIdentity = ObjectIdentity
hh3cSysSummerTime = _Hh3cSysSummerTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2)
)


class _Hh3cSysSummerTimeEnable_Type(Integer32):
    """Custom type hh3cSysSummerTimeEnable based on Integer32"""
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


_Hh3cSysSummerTimeEnable_Type.__name__ = "Integer32"
_Hh3cSysSummerTimeEnable_Object = MibScalar
hh3cSysSummerTimeEnable = _Hh3cSysSummerTimeEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2, 1),
    _Hh3cSysSummerTimeEnable_Type()
)
hh3cSysSummerTimeEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysSummerTimeEnable.setStatus("current")
_Hh3cSysSummerTimeZone_Type = DisplayString
_Hh3cSysSummerTimeZone_Object = MibScalar
hh3cSysSummerTimeZone = _Hh3cSysSummerTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2, 2),
    _Hh3cSysSummerTimeZone_Type()
)
hh3cSysSummerTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSummerTimeZone.setStatus("current")


class _Hh3cSysSummerTimeMethod_Type(Integer32):
    """Custom type hh3cSysSummerTimeMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneOff", 1),
          ("repeating", 2))
    )


_Hh3cSysSummerTimeMethod_Type.__name__ = "Integer32"
_Hh3cSysSummerTimeMethod_Object = MibScalar
hh3cSysSummerTimeMethod = _Hh3cSysSummerTimeMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2, 3),
    _Hh3cSysSummerTimeMethod_Type()
)
hh3cSysSummerTimeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSummerTimeMethod.setStatus("current")


class _Hh3cSysSummerTimeStart_Type(DateAndTime):
    """Custom type hh3cSysSummerTimeStart based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hh3cSysSummerTimeStart_Type.__name__ = "DateAndTime"
_Hh3cSysSummerTimeStart_Object = MibScalar
hh3cSysSummerTimeStart = _Hh3cSysSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2, 4),
    _Hh3cSysSummerTimeStart_Type()
)
hh3cSysSummerTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSummerTimeStart.setStatus("current")


class _Hh3cSysSummerTimeEnd_Type(DateAndTime):
    """Custom type hh3cSysSummerTimeEnd based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hh3cSysSummerTimeEnd_Type.__name__ = "DateAndTime"
_Hh3cSysSummerTimeEnd_Object = MibScalar
hh3cSysSummerTimeEnd = _Hh3cSysSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2, 5),
    _Hh3cSysSummerTimeEnd_Type()
)
hh3cSysSummerTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSummerTimeEnd.setStatus("current")


class _Hh3cSysSummerTimeOffset_Type(Integer32):
    """Custom type hh3cSysSummerTimeOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_Hh3cSysSummerTimeOffset_Type.__name__ = "Integer32"
_Hh3cSysSummerTimeOffset_Object = MibScalar
hh3cSysSummerTimeOffset = _Hh3cSysSummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 2, 6),
    _Hh3cSysSummerTimeOffset_Type()
)
hh3cSysSummerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSummerTimeOffset.setStatus("current")


class _Hh3cSysLocalClockString_Type(OctetString):
    """Custom type hh3cSysLocalClockString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 24),
    )


_Hh3cSysLocalClockString_Type.__name__ = "OctetString"
_Hh3cSysLocalClockString_Object = MibScalar
hh3cSysLocalClockString = _Hh3cSysLocalClockString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 1, 3),
    _Hh3cSysLocalClockString_Type()
)
hh3cSysLocalClockString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysLocalClockString.setStatus("current")
_Hh3cSysCurrent_ObjectIdentity = ObjectIdentity
hh3cSysCurrent = _Hh3cSysCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2)
)
_Hh3cSysCurTable_Object = MibTable
hh3cSysCurTable = _Hh3cSysCurTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cSysCurTable.setStatus("current")
_Hh3cSysCurEntry_Object = MibTableRow
hh3cSysCurEntry = _Hh3cSysCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1, 1)
)
hh3cSysCurEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysCurEntPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysCurEntry.setStatus("current")


class _Hh3cSysCurEntPhysicalIndex_Type(Integer32):
    """Custom type hh3cSysCurEntPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysCurEntPhysicalIndex_Type.__name__ = "Integer32"
_Hh3cSysCurEntPhysicalIndex_Object = MibTableColumn
hh3cSysCurEntPhysicalIndex = _Hh3cSysCurEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1, 1, 1),
    _Hh3cSysCurEntPhysicalIndex_Type()
)
hh3cSysCurEntPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysCurEntPhysicalIndex.setStatus("current")


class _Hh3cSysCurCFGFileIndex_Type(Integer32):
    """Custom type hh3cSysCurCFGFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysCurCFGFileIndex_Type.__name__ = "Integer32"
_Hh3cSysCurCFGFileIndex_Object = MibTableColumn
hh3cSysCurCFGFileIndex = _Hh3cSysCurCFGFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1, 1, 2),
    _Hh3cSysCurCFGFileIndex_Type()
)
hh3cSysCurCFGFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCurCFGFileIndex.setStatus("current")


class _Hh3cSysCurImageIndex_Type(Integer32):
    """Custom type hh3cSysCurImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysCurImageIndex_Type.__name__ = "Integer32"
_Hh3cSysCurImageIndex_Object = MibTableColumn
hh3cSysCurImageIndex = _Hh3cSysCurImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1, 1, 3),
    _Hh3cSysCurImageIndex_Type()
)
hh3cSysCurImageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCurImageIndex.setStatus("current")


class _Hh3cSysCurBtmFileName_Type(OctetString):
    """Custom type hh3cSysCurBtmFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cSysCurBtmFileName_Type.__name__ = "OctetString"
_Hh3cSysCurBtmFileName_Object = MibTableColumn
hh3cSysCurBtmFileName = _Hh3cSysCurBtmFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1, 1, 4),
    _Hh3cSysCurBtmFileName_Type()
)
hh3cSysCurBtmFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCurBtmFileName.setStatus("current")


class _Hh3cSysCurUpdateBtmFileName_Type(OctetString):
    """Custom type hh3cSysCurUpdateBtmFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cSysCurUpdateBtmFileName_Type.__name__ = "OctetString"
_Hh3cSysCurUpdateBtmFileName_Object = MibTableColumn
hh3cSysCurUpdateBtmFileName = _Hh3cSysCurUpdateBtmFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 2, 1, 1, 5),
    _Hh3cSysCurUpdateBtmFileName_Type()
)
hh3cSysCurUpdateBtmFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCurUpdateBtmFileName.setStatus("current")
_Hh3cSysReload_ObjectIdentity = ObjectIdentity
hh3cSysReload = _Hh3cSysReload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3)
)


class _Hh3cSysReloadSchedule_Type(Integer32):
    """Custom type hh3cSysReloadSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysReloadSchedule_Type.__name__ = "Integer32"
_Hh3cSysReloadSchedule_Object = MibScalar
hh3cSysReloadSchedule = _Hh3cSysReloadSchedule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 1),
    _Hh3cSysReloadSchedule_Type()
)
hh3cSysReloadSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysReloadSchedule.setStatus("current")


class _Hh3cSysReloadAction_Type(Integer32):
    """Custom type hh3cSysReloadAction based on Integer32"""
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
        *(("reloadAtOnce", 3),
          ("reloadCancel", 4),
          ("reloadOnSchedule", 2),
          ("reloadUnavailable", 1))
    )


_Hh3cSysReloadAction_Type.__name__ = "Integer32"
_Hh3cSysReloadAction_Object = MibScalar
hh3cSysReloadAction = _Hh3cSysReloadAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 2),
    _Hh3cSysReloadAction_Type()
)
hh3cSysReloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysReloadAction.setStatus("current")
_Hh3cSysReloadScheduleTable_Object = MibTable
hh3cSysReloadScheduleTable = _Hh3cSysReloadScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cSysReloadScheduleTable.setStatus("current")
_Hh3cSysReloadScheduleEntry_Object = MibTableRow
hh3cSysReloadScheduleEntry = _Hh3cSysReloadScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1)
)
hh3cSysReloadScheduleEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysReloadScheduleIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysReloadScheduleEntry.setStatus("current")


class _Hh3cSysReloadScheduleIndex_Type(Integer32):
    """Custom type hh3cSysReloadScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysReloadScheduleIndex_Type.__name__ = "Integer32"
_Hh3cSysReloadScheduleIndex_Object = MibTableColumn
hh3cSysReloadScheduleIndex = _Hh3cSysReloadScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 1),
    _Hh3cSysReloadScheduleIndex_Type()
)
hh3cSysReloadScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysReloadScheduleIndex.setStatus("current")


class _Hh3cSysReloadEntity_Type(Integer32):
    """Custom type hh3cSysReloadEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysReloadEntity_Type.__name__ = "Integer32"
_Hh3cSysReloadEntity_Object = MibTableColumn
hh3cSysReloadEntity = _Hh3cSysReloadEntity_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 2),
    _Hh3cSysReloadEntity_Type()
)
hh3cSysReloadEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadEntity.setStatus("current")


class _Hh3cSysReloadCfgFile_Type(Integer32):
    """Custom type hh3cSysReloadCfgFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysReloadCfgFile_Type.__name__ = "Integer32"
_Hh3cSysReloadCfgFile_Object = MibTableColumn
hh3cSysReloadCfgFile = _Hh3cSysReloadCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 3),
    _Hh3cSysReloadCfgFile_Type()
)
hh3cSysReloadCfgFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadCfgFile.setStatus("current")


class _Hh3cSysReloadImage_Type(Integer32):
    """Custom type hh3cSysReloadImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysReloadImage_Type.__name__ = "Integer32"
_Hh3cSysReloadImage_Object = MibTableColumn
hh3cSysReloadImage = _Hh3cSysReloadImage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 4),
    _Hh3cSysReloadImage_Type()
)
hh3cSysReloadImage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadImage.setStatus("current")


class _Hh3cSysReloadReason_Type(DisplayString):
    """Custom type hh3cSysReloadReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSysReloadReason_Type.__name__ = "DisplayString"
_Hh3cSysReloadReason_Object = MibTableColumn
hh3cSysReloadReason = _Hh3cSysReloadReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 5),
    _Hh3cSysReloadReason_Type()
)
hh3cSysReloadReason.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadReason.setStatus("current")


class _Hh3cSysReloadScheduleTime_Type(DateAndTime):
    """Custom type hh3cSysReloadScheduleTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hh3cSysReloadScheduleTime_Type.__name__ = "DateAndTime"
_Hh3cSysReloadScheduleTime_Object = MibTableColumn
hh3cSysReloadScheduleTime = _Hh3cSysReloadScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 6),
    _Hh3cSysReloadScheduleTime_Type()
)
hh3cSysReloadScheduleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadScheduleTime.setStatus("current")
_Hh3cSysReloadRowStatus_Type = RowStatus
_Hh3cSysReloadRowStatus_Object = MibTableColumn
hh3cSysReloadRowStatus = _Hh3cSysReloadRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 7),
    _Hh3cSysReloadRowStatus_Type()
)
hh3cSysReloadRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadRowStatus.setStatus("current")
_Hh3cSysReloadScheduleTagList_Type = SnmpTagList
_Hh3cSysReloadScheduleTagList_Object = MibTableColumn
hh3cSysReloadScheduleTagList = _Hh3cSysReloadScheduleTagList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 3, 1, 8),
    _Hh3cSysReloadScheduleTagList_Type()
)
hh3cSysReloadScheduleTagList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysReloadScheduleTagList.setStatus("current")
_Hh3cSysReloadTag_Type = SnmpTagValue
_Hh3cSysReloadTag_Object = MibScalar
hh3cSysReloadTag = _Hh3cSysReloadTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 3, 4),
    _Hh3cSysReloadTag_Type()
)
hh3cSysReloadTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysReloadTag.setStatus("current")
_Hh3cSysImage_ObjectIdentity = ObjectIdentity
hh3cSysImage = _Hh3cSysImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4)
)


class _Hh3cSysImageNum_Type(Integer32):
    """Custom type hh3cSysImageNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysImageNum_Type.__name__ = "Integer32"
_Hh3cSysImageNum_Object = MibScalar
hh3cSysImageNum = _Hh3cSysImageNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 1),
    _Hh3cSysImageNum_Type()
)
hh3cSysImageNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysImageNum.setStatus("current")
_Hh3cSysImageTable_Object = MibTable
hh3cSysImageTable = _Hh3cSysImageTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cSysImageTable.setStatus("current")
_Hh3cSysImageEntry_Object = MibTableRow
hh3cSysImageEntry = _Hh3cSysImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2, 1)
)
hh3cSysImageEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysImageIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysImageEntry.setStatus("current")


class _Hh3cSysImageIndex_Type(Integer32):
    """Custom type hh3cSysImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysImageIndex_Type.__name__ = "Integer32"
_Hh3cSysImageIndex_Object = MibTableColumn
hh3cSysImageIndex = _Hh3cSysImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2, 1, 1),
    _Hh3cSysImageIndex_Type()
)
hh3cSysImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysImageIndex.setStatus("current")
_Hh3cSysImageName_Type = DisplayString
_Hh3cSysImageName_Object = MibTableColumn
hh3cSysImageName = _Hh3cSysImageName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2, 1, 2),
    _Hh3cSysImageName_Type()
)
hh3cSysImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysImageName.setStatus("current")


class _Hh3cSysImageSize_Type(Integer32):
    """Custom type hh3cSysImageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysImageSize_Type.__name__ = "Integer32"
_Hh3cSysImageSize_Object = MibTableColumn
hh3cSysImageSize = _Hh3cSysImageSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2, 1, 3),
    _Hh3cSysImageSize_Type()
)
hh3cSysImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysImageSize.setStatus("current")
_Hh3cSysImageLocation_Type = DisplayString
_Hh3cSysImageLocation_Object = MibTableColumn
hh3cSysImageLocation = _Hh3cSysImageLocation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2, 1, 4),
    _Hh3cSysImageLocation_Type()
)
hh3cSysImageLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysImageLocation.setStatus("current")


class _Hh3cSysImageType_Type(Integer32):
    """Custom type hh3cSysImageType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("backup-secure", 7),
          ("main", 1),
          ("main-backup", 5),
          ("main-backup-secure", 8),
          ("main-secure", 6),
          ("none", 3),
          ("secure", 4))
    )


_Hh3cSysImageType_Type.__name__ = "Integer32"
_Hh3cSysImageType_Object = MibTableColumn
hh3cSysImageType = _Hh3cSysImageType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 4, 2, 1, 5),
    _Hh3cSysImageType_Type()
)
hh3cSysImageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysImageType.setStatus("current")
_Hh3cSysCFGFile_ObjectIdentity = ObjectIdentity
hh3cSysCFGFile = _Hh3cSysCFGFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5)
)


class _Hh3cSysCFGFileNum_Type(Integer32):
    """Custom type hh3cSysCFGFileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysCFGFileNum_Type.__name__ = "Integer32"
_Hh3cSysCFGFileNum_Object = MibScalar
hh3cSysCFGFileNum = _Hh3cSysCFGFileNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 1),
    _Hh3cSysCFGFileNum_Type()
)
hh3cSysCFGFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCFGFileNum.setStatus("current")
_Hh3cSysCFGFileTable_Object = MibTable
hh3cSysCFGFileTable = _Hh3cSysCFGFileTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hh3cSysCFGFileTable.setStatus("current")
_Hh3cSysCFGFileEntry_Object = MibTableRow
hh3cSysCFGFileEntry = _Hh3cSysCFGFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 2, 1)
)
hh3cSysCFGFileEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysCFGFileIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysCFGFileEntry.setStatus("current")


class _Hh3cSysCFGFileIndex_Type(Integer32):
    """Custom type hh3cSysCFGFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cSysCFGFileIndex_Type.__name__ = "Integer32"
_Hh3cSysCFGFileIndex_Object = MibTableColumn
hh3cSysCFGFileIndex = _Hh3cSysCFGFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 2, 1, 1),
    _Hh3cSysCFGFileIndex_Type()
)
hh3cSysCFGFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysCFGFileIndex.setStatus("current")
_Hh3cSysCFGFileName_Type = DisplayString
_Hh3cSysCFGFileName_Object = MibTableColumn
hh3cSysCFGFileName = _Hh3cSysCFGFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 2, 1, 2),
    _Hh3cSysCFGFileName_Type()
)
hh3cSysCFGFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCFGFileName.setStatus("current")


class _Hh3cSysCFGFileSize_Type(Integer32):
    """Custom type hh3cSysCFGFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysCFGFileSize_Type.__name__ = "Integer32"
_Hh3cSysCFGFileSize_Object = MibTableColumn
hh3cSysCFGFileSize = _Hh3cSysCFGFileSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 2, 1, 3),
    _Hh3cSysCFGFileSize_Type()
)
hh3cSysCFGFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCFGFileSize.setStatus("current")
_Hh3cSysCFGFileLocation_Type = DisplayString
_Hh3cSysCFGFileLocation_Object = MibTableColumn
hh3cSysCFGFileLocation = _Hh3cSysCFGFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 5, 2, 1, 4),
    _Hh3cSysCFGFileLocation_Type()
)
hh3cSysCFGFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysCFGFileLocation.setStatus("current")
_Hh3cSysBtmFile_ObjectIdentity = ObjectIdentity
hh3cSysBtmFile = _Hh3cSysBtmFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6)
)
_Hh3cSysBtmFileLoad_ObjectIdentity = ObjectIdentity
hh3cSysBtmFileLoad = _Hh3cSysBtmFileLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 1)
)
_Hh3cSysBtmLoadMaxNumber_Type = Integer32
_Hh3cSysBtmLoadMaxNumber_Object = MibScalar
hh3cSysBtmLoadMaxNumber = _Hh3cSysBtmLoadMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 1, 1),
    _Hh3cSysBtmLoadMaxNumber_Type()
)
hh3cSysBtmLoadMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysBtmLoadMaxNumber.setStatus("current")
_Hh3cSysBtmLoadTable_Object = MibTable
hh3cSysBtmLoadTable = _Hh3cSysBtmLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hh3cSysBtmLoadTable.setStatus("current")
_Hh3cSysBtmLoadEntry_Object = MibTableRow
hh3cSysBtmLoadEntry = _Hh3cSysBtmLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1)
)
hh3cSysBtmLoadEntry.setIndexNames(
    (0, "HH3C-SYS-MAN-MIB", "hh3cSysBtmLoadIndex"),
)
if mibBuilder.loadTexts:
    hh3cSysBtmLoadEntry.setStatus("current")


class _Hh3cSysBtmLoadIndex_Type(Integer32):
    """Custom type hh3cSysBtmLoadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSysBtmLoadIndex_Type.__name__ = "Integer32"
_Hh3cSysBtmLoadIndex_Object = MibTableColumn
hh3cSysBtmLoadIndex = _Hh3cSysBtmLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1, 1),
    _Hh3cSysBtmLoadIndex_Type()
)
hh3cSysBtmLoadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSysBtmLoadIndex.setStatus("current")


class _Hh3cSysBtmFileName_Type(OctetString):
    """Custom type hh3cSysBtmFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cSysBtmFileName_Type.__name__ = "OctetString"
_Hh3cSysBtmFileName_Object = MibTableColumn
hh3cSysBtmFileName = _Hh3cSysBtmFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1, 2),
    _Hh3cSysBtmFileName_Type()
)
hh3cSysBtmFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysBtmFileName.setStatus("current")


class _Hh3cSysBtmFileType_Type(Integer32):
    """Custom type hh3cSysBtmFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("none", 2))
    )


_Hh3cSysBtmFileType_Type.__name__ = "Integer32"
_Hh3cSysBtmFileType_Object = MibTableColumn
hh3cSysBtmFileType = _Hh3cSysBtmFileType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1, 3),
    _Hh3cSysBtmFileType_Type()
)
hh3cSysBtmFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysBtmFileType.setStatus("current")
_Hh3cSysBtmRowStatus_Type = RowStatus
_Hh3cSysBtmRowStatus_Object = MibTableColumn
hh3cSysBtmRowStatus = _Hh3cSysBtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1, 4),
    _Hh3cSysBtmRowStatus_Type()
)
hh3cSysBtmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSysBtmRowStatus.setStatus("current")


class _Hh3cSysBtmErrorStatus_Type(Integer32):
    """Custom type hh3cSysBtmErrorStatus based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("invalidFile", 1),
          ("success", 3))
    )


_Hh3cSysBtmErrorStatus_Type.__name__ = "Integer32"
_Hh3cSysBtmErrorStatus_Object = MibTableColumn
hh3cSysBtmErrorStatus = _Hh3cSysBtmErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1, 5),
    _Hh3cSysBtmErrorStatus_Type()
)
hh3cSysBtmErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysBtmErrorStatus.setStatus("current")
_Hh3cSysBtmLoadTime_Type = TimeTicks
_Hh3cSysBtmLoadTime_Object = MibTableColumn
hh3cSysBtmLoadTime = _Hh3cSysBtmLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 1, 6, 2, 1, 6),
    _Hh3cSysBtmLoadTime_Type()
)
hh3cSysBtmLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysBtmLoadTime.setStatus("current")
_Hh3cSystemManMIBNotifications_ObjectIdentity = ObjectIdentity
hh3cSystemManMIBNotifications = _Hh3cSystemManMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 2)
)
_Hh3cSystemManMIBConformance_ObjectIdentity = ObjectIdentity
hh3cSystemManMIBConformance = _Hh3cSystemManMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3)
)
_Hh3cSystemManMIBCompliances_ObjectIdentity = ObjectIdentity
hh3cSystemManMIBCompliances = _Hh3cSystemManMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 1)
)
_Hh3cSystemManMIBGroups_ObjectIdentity = ObjectIdentity
hh3cSystemManMIBGroups = _Hh3cSystemManMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2)
)

# Managed Objects groups

hh3cSysClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 1)
)
hh3cSysClockGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysLocalClock"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysSummerTimeEnable"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysSummerTimeZone"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysSummerTimeMethod"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysSummerTimeStart"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysSummerTimeEnd"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysSummerTimeOffset"))
)
if mibBuilder.loadTexts:
    hh3cSysClockGroup.setStatus("current")

hh3cSysReloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 2)
)
hh3cSysReloadGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysReloadSchedule"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadAction"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadImage"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadCfgFile"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadReason"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadScheduleTagList"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadTag"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadScheduleTime"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadEntity"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cSysReloadGroup.setStatus("current")

hh3cSysImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 3)
)
hh3cSysImageGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysImageNum"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysImageName"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysImageSize"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysImageLocation"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysImageType"))
)
if mibBuilder.loadTexts:
    hh3cSysImageGroup.setStatus("current")

hh3cSysCFGFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 4)
)
hh3cSysCFGFileGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysCFGFileNum"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysCFGFileName"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysCFGFileSize"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysCFGFileLocation"))
)
if mibBuilder.loadTexts:
    hh3cSysCFGFileGroup.setStatus("current")

hh3cSysCurGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 5)
)
hh3cSysCurGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysCurCFGFileIndex"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysCurImageIndex"))
)
if mibBuilder.loadTexts:
    hh3cSysCurGroup.setStatus("current")

hh3cSystemBtmLoadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 7)
)
hh3cSystemBtmLoadGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysCurBtmFileName"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysCurUpdateBtmFileName"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysBtmLoadMaxNumber"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysBtmFileName"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysBtmFileType"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysBtmRowStatus"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysBtmErrorStatus"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysBtmLoadTime"))
)
if mibBuilder.loadTexts:
    hh3cSystemBtmLoadGroup.setStatus("current")


# Notification objects

hh3cSysClockChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 2, 1)
)
hh3cSysClockChangedNotification.setObjects(
    ("HH3C-SYS-MAN-MIB", "hh3cSysLocalClock")
)
if mibBuilder.loadTexts:
    hh3cSysClockChangedNotification.setStatus(
        "current"
    )

hh3cSysReloadNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 2, 2)
)
hh3cSysReloadNotification.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysReloadImage"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadCfgFile"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadReason"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadScheduleTime"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadAction"))
)
if mibBuilder.loadTexts:
    hh3cSysReloadNotification.setStatus(
        "current"
    )

hh3cSysStartUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 2, 3)
)
hh3cSysStartUpNotification.setObjects(
    ("HH3C-SYS-MAN-MIB", "hh3cSysImageType")
)
if mibBuilder.loadTexts:
    hh3cSysStartUpNotification.setStatus(
        "current"
    )


# Notifications groups

hh3cSystemManNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 2, 6)
)
hh3cSystemManNotificationGroup.setObjects(
      *(("HH3C-SYS-MAN-MIB", "hh3cSysClockChangedNotification"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysReloadNotification"),
        ("HH3C-SYS-MAN-MIB", "hh3cSysStartUpNotification"))
)
if mibBuilder.loadTexts:
    hh3cSystemManNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cSystemManMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cSystemManMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SYS-MAN-MIB",
    **{"hh3cSystemMan": hh3cSystemMan,
       "hh3cSystemManMIBObjects": hh3cSystemManMIBObjects,
       "hh3cSysClock": hh3cSysClock,
       "hh3cSysLocalClock": hh3cSysLocalClock,
       "hh3cSysSummerTime": hh3cSysSummerTime,
       "hh3cSysSummerTimeEnable": hh3cSysSummerTimeEnable,
       "hh3cSysSummerTimeZone": hh3cSysSummerTimeZone,
       "hh3cSysSummerTimeMethod": hh3cSysSummerTimeMethod,
       "hh3cSysSummerTimeStart": hh3cSysSummerTimeStart,
       "hh3cSysSummerTimeEnd": hh3cSysSummerTimeEnd,
       "hh3cSysSummerTimeOffset": hh3cSysSummerTimeOffset,
       "hh3cSysLocalClockString": hh3cSysLocalClockString,
       "hh3cSysCurrent": hh3cSysCurrent,
       "hh3cSysCurTable": hh3cSysCurTable,
       "hh3cSysCurEntry": hh3cSysCurEntry,
       "hh3cSysCurEntPhysicalIndex": hh3cSysCurEntPhysicalIndex,
       "hh3cSysCurCFGFileIndex": hh3cSysCurCFGFileIndex,
       "hh3cSysCurImageIndex": hh3cSysCurImageIndex,
       "hh3cSysCurBtmFileName": hh3cSysCurBtmFileName,
       "hh3cSysCurUpdateBtmFileName": hh3cSysCurUpdateBtmFileName,
       "hh3cSysReload": hh3cSysReload,
       "hh3cSysReloadSchedule": hh3cSysReloadSchedule,
       "hh3cSysReloadAction": hh3cSysReloadAction,
       "hh3cSysReloadScheduleTable": hh3cSysReloadScheduleTable,
       "hh3cSysReloadScheduleEntry": hh3cSysReloadScheduleEntry,
       "hh3cSysReloadScheduleIndex": hh3cSysReloadScheduleIndex,
       "hh3cSysReloadEntity": hh3cSysReloadEntity,
       "hh3cSysReloadCfgFile": hh3cSysReloadCfgFile,
       "hh3cSysReloadImage": hh3cSysReloadImage,
       "hh3cSysReloadReason": hh3cSysReloadReason,
       "hh3cSysReloadScheduleTime": hh3cSysReloadScheduleTime,
       "hh3cSysReloadRowStatus": hh3cSysReloadRowStatus,
       "hh3cSysReloadScheduleTagList": hh3cSysReloadScheduleTagList,
       "hh3cSysReloadTag": hh3cSysReloadTag,
       "hh3cSysImage": hh3cSysImage,
       "hh3cSysImageNum": hh3cSysImageNum,
       "hh3cSysImageTable": hh3cSysImageTable,
       "hh3cSysImageEntry": hh3cSysImageEntry,
       "hh3cSysImageIndex": hh3cSysImageIndex,
       "hh3cSysImageName": hh3cSysImageName,
       "hh3cSysImageSize": hh3cSysImageSize,
       "hh3cSysImageLocation": hh3cSysImageLocation,
       "hh3cSysImageType": hh3cSysImageType,
       "hh3cSysCFGFile": hh3cSysCFGFile,
       "hh3cSysCFGFileNum": hh3cSysCFGFileNum,
       "hh3cSysCFGFileTable": hh3cSysCFGFileTable,
       "hh3cSysCFGFileEntry": hh3cSysCFGFileEntry,
       "hh3cSysCFGFileIndex": hh3cSysCFGFileIndex,
       "hh3cSysCFGFileName": hh3cSysCFGFileName,
       "hh3cSysCFGFileSize": hh3cSysCFGFileSize,
       "hh3cSysCFGFileLocation": hh3cSysCFGFileLocation,
       "hh3cSysBtmFile": hh3cSysBtmFile,
       "hh3cSysBtmFileLoad": hh3cSysBtmFileLoad,
       "hh3cSysBtmLoadMaxNumber": hh3cSysBtmLoadMaxNumber,
       "hh3cSysBtmLoadTable": hh3cSysBtmLoadTable,
       "hh3cSysBtmLoadEntry": hh3cSysBtmLoadEntry,
       "hh3cSysBtmLoadIndex": hh3cSysBtmLoadIndex,
       "hh3cSysBtmFileName": hh3cSysBtmFileName,
       "hh3cSysBtmFileType": hh3cSysBtmFileType,
       "hh3cSysBtmRowStatus": hh3cSysBtmRowStatus,
       "hh3cSysBtmErrorStatus": hh3cSysBtmErrorStatus,
       "hh3cSysBtmLoadTime": hh3cSysBtmLoadTime,
       "hh3cSystemManMIBNotifications": hh3cSystemManMIBNotifications,
       "hh3cSysClockChangedNotification": hh3cSysClockChangedNotification,
       "hh3cSysReloadNotification": hh3cSysReloadNotification,
       "hh3cSysStartUpNotification": hh3cSysStartUpNotification,
       "hh3cSystemManMIBConformance": hh3cSystemManMIBConformance,
       "hh3cSystemManMIBCompliances": hh3cSystemManMIBCompliances,
       "hh3cSystemManMIBCompliance": hh3cSystemManMIBCompliance,
       "hh3cSystemManMIBGroups": hh3cSystemManMIBGroups,
       "hh3cSysClockGroup": hh3cSysClockGroup,
       "hh3cSysReloadGroup": hh3cSysReloadGroup,
       "hh3cSysImageGroup": hh3cSysImageGroup,
       "hh3cSysCFGFileGroup": hh3cSysCFGFileGroup,
       "hh3cSysCurGroup": hh3cSysCurGroup,
       "hh3cSystemManNotificationGroup": hh3cSystemManNotificationGroup,
       "hh3cSystemBtmLoadGroup": hh3cSystemBtmLoadGroup}
)
