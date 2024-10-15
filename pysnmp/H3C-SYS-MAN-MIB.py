# SNMP MIB module (H3C-SYS-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-SYS-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:30 2024
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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
 RowPointer,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cSystemMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3)
)
h3cSystemMan.setRevisions(
        ("2004-04-08 13:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cSystemManMIBObjects_ObjectIdentity = ObjectIdentity
h3cSystemManMIBObjects = _H3cSystemManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1)
)
_H3cSysClock_ObjectIdentity = ObjectIdentity
h3cSysClock = _H3cSysClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 1)
)
_H3cSysLocalClock_Type = DateAndTime
_H3cSysLocalClock_Object = MibScalar
h3cSysLocalClock = _H3cSysLocalClock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 1, 1),
    _H3cSysLocalClock_Type()
)
h3cSysLocalClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSysLocalClock.setStatus("current")
_H3cSysSummerTime_ObjectIdentity = ObjectIdentity
h3cSysSummerTime = _H3cSysSummerTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 1, 2)
)


class _H3cSysSummerTimeEnable_Type(Integer32):
    """Custom type h3cSysSummerTimeEnable based on Integer32"""
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


_H3cSysSummerTimeEnable_Type.__name__ = "Integer32"
_H3cSysSummerTimeEnable_Object = MibScalar
h3cSysSummerTimeEnable = _H3cSysSummerTimeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 1, 2, 1),
    _H3cSysSummerTimeEnable_Type()
)
h3cSysSummerTimeEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysSummerTimeEnable.setStatus("current")
_H3cSysSummerTimeZone_Type = DisplayString
_H3cSysSummerTimeZone_Object = MibScalar
h3cSysSummerTimeZone = _H3cSysSummerTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 1, 2, 2),
    _H3cSysSummerTimeZone_Type()
)
h3cSysSummerTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSysSummerTimeZone.setStatus("current")


class _H3cSysSummerTimeMethod_Type(Integer32):
    """Custom type h3cSysSummerTimeMethod based on Integer32"""
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


_H3cSysSummerTimeMethod_Type.__name__ = "Integer32"
_H3cSysSummerTimeMethod_Object = MibScalar
h3cSysSummerTimeMethod = _H3cSysSummerTimeMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 1, 2, 3),
    _H3cSysSummerTimeMethod_Type()
)
h3cSysSummerTimeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSysSummerTimeMethod.setStatus("current")


class _H3cSysSummerTimeStart_Type(DateAndTime):
    """Custom type h3cSysSummerTimeStart based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_H3cSysSummerTimeStart_Type.__name__ = "DateAndTime"
_H3cSysSummerTimeStart_Object = MibScalar
h3cSysSummerTimeStart = _H3cSysSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 1, 2, 4),
    _H3cSysSummerTimeStart_Type()
)
h3cSysSummerTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSysSummerTimeStart.setStatus("current")


class _H3cSysSummerTimeEnd_Type(DateAndTime):
    """Custom type h3cSysSummerTimeEnd based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_H3cSysSummerTimeEnd_Type.__name__ = "DateAndTime"
_H3cSysSummerTimeEnd_Object = MibScalar
h3cSysSummerTimeEnd = _H3cSysSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 1, 2, 5),
    _H3cSysSummerTimeEnd_Type()
)
h3cSysSummerTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSysSummerTimeEnd.setStatus("current")


class _H3cSysSummerTimeOffset_Type(Integer32):
    """Custom type h3cSysSummerTimeOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_H3cSysSummerTimeOffset_Type.__name__ = "Integer32"
_H3cSysSummerTimeOffset_Object = MibScalar
h3cSysSummerTimeOffset = _H3cSysSummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 1, 2, 6),
    _H3cSysSummerTimeOffset_Type()
)
h3cSysSummerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSysSummerTimeOffset.setStatus("current")
_H3cSysCurrent_ObjectIdentity = ObjectIdentity
h3cSysCurrent = _H3cSysCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 2)
)
_H3cSysCurTable_Object = MibTable
h3cSysCurTable = _H3cSysCurTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cSysCurTable.setStatus("current")
_H3cSysCurEntry_Object = MibTableRow
h3cSysCurEntry = _H3cSysCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 2, 1, 1)
)
h3cSysCurEntry.setIndexNames(
    (0, "H3C-SYS-MAN-MIB", "h3cSysCurEntPhysicalIndex"),
)
if mibBuilder.loadTexts:
    h3cSysCurEntry.setStatus("current")


class _H3cSysCurEntPhysicalIndex_Type(Integer32):
    """Custom type h3cSysCurEntPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cSysCurEntPhysicalIndex_Type.__name__ = "Integer32"
_H3cSysCurEntPhysicalIndex_Object = MibTableColumn
h3cSysCurEntPhysicalIndex = _H3cSysCurEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 2, 1, 1, 1),
    _H3cSysCurEntPhysicalIndex_Type()
)
h3cSysCurEntPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSysCurEntPhysicalIndex.setStatus("current")


class _H3cSysCurCFGFileIndex_Type(Integer32):
    """Custom type h3cSysCurCFGFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cSysCurCFGFileIndex_Type.__name__ = "Integer32"
_H3cSysCurCFGFileIndex_Object = MibTableColumn
h3cSysCurCFGFileIndex = _H3cSysCurCFGFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 2, 1, 1, 2),
    _H3cSysCurCFGFileIndex_Type()
)
h3cSysCurCFGFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysCurCFGFileIndex.setStatus("current")


class _H3cSysCurImageIndex_Type(Integer32):
    """Custom type h3cSysCurImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cSysCurImageIndex_Type.__name__ = "Integer32"
_H3cSysCurImageIndex_Object = MibTableColumn
h3cSysCurImageIndex = _H3cSysCurImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 2, 1, 1, 3),
    _H3cSysCurImageIndex_Type()
)
h3cSysCurImageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysCurImageIndex.setStatus("current")


class _H3cSysCurBtmFileName_Type(OctetString):
    """Custom type h3cSysCurBtmFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cSysCurBtmFileName_Type.__name__ = "OctetString"
_H3cSysCurBtmFileName_Object = MibTableColumn
h3cSysCurBtmFileName = _H3cSysCurBtmFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 2, 1, 1, 4),
    _H3cSysCurBtmFileName_Type()
)
h3cSysCurBtmFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysCurBtmFileName.setStatus("current")


class _H3cSysCurUpdateBtmFileName_Type(OctetString):
    """Custom type h3cSysCurUpdateBtmFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cSysCurUpdateBtmFileName_Type.__name__ = "OctetString"
_H3cSysCurUpdateBtmFileName_Object = MibTableColumn
h3cSysCurUpdateBtmFileName = _H3cSysCurUpdateBtmFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 2, 1, 1, 5),
    _H3cSysCurUpdateBtmFileName_Type()
)
h3cSysCurUpdateBtmFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysCurUpdateBtmFileName.setStatus("current")
_H3cSysReload_ObjectIdentity = ObjectIdentity
h3cSysReload = _H3cSysReload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3)
)


class _H3cSysReloadSchedule_Type(Integer32):
    """Custom type h3cSysReloadSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cSysReloadSchedule_Type.__name__ = "Integer32"
_H3cSysReloadSchedule_Object = MibScalar
h3cSysReloadSchedule = _H3cSysReloadSchedule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 1),
    _H3cSysReloadSchedule_Type()
)
h3cSysReloadSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSysReloadSchedule.setStatus("current")


class _H3cSysReloadAction_Type(Integer32):
    """Custom type h3cSysReloadAction based on Integer32"""
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


_H3cSysReloadAction_Type.__name__ = "Integer32"
_H3cSysReloadAction_Object = MibScalar
h3cSysReloadAction = _H3cSysReloadAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 2),
    _H3cSysReloadAction_Type()
)
h3cSysReloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSysReloadAction.setStatus("current")
_H3cSysReloadScheduleTable_Object = MibTable
h3cSysReloadScheduleTable = _H3cSysReloadScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    h3cSysReloadScheduleTable.setStatus("current")
_H3cSysReloadScheduleEntry_Object = MibTableRow
h3cSysReloadScheduleEntry = _H3cSysReloadScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 3, 1)
)
h3cSysReloadScheduleEntry.setIndexNames(
    (0, "H3C-SYS-MAN-MIB", "h3cSysReloadScheduleIndex"),
)
if mibBuilder.loadTexts:
    h3cSysReloadScheduleEntry.setStatus("current")


class _H3cSysReloadScheduleIndex_Type(Integer32):
    """Custom type h3cSysReloadScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cSysReloadScheduleIndex_Type.__name__ = "Integer32"
_H3cSysReloadScheduleIndex_Object = MibTableColumn
h3cSysReloadScheduleIndex = _H3cSysReloadScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 3, 1, 1),
    _H3cSysReloadScheduleIndex_Type()
)
h3cSysReloadScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSysReloadScheduleIndex.setStatus("current")


class _H3cSysReloadEntity_Type(Integer32):
    """Custom type h3cSysReloadEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cSysReloadEntity_Type.__name__ = "Integer32"
_H3cSysReloadEntity_Object = MibTableColumn
h3cSysReloadEntity = _H3cSysReloadEntity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 3, 1, 2),
    _H3cSysReloadEntity_Type()
)
h3cSysReloadEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSysReloadEntity.setStatus("current")


class _H3cSysReloadCfgFile_Type(Integer32):
    """Custom type h3cSysReloadCfgFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cSysReloadCfgFile_Type.__name__ = "Integer32"
_H3cSysReloadCfgFile_Object = MibTableColumn
h3cSysReloadCfgFile = _H3cSysReloadCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 3, 1, 3),
    _H3cSysReloadCfgFile_Type()
)
h3cSysReloadCfgFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSysReloadCfgFile.setStatus("current")


class _H3cSysReloadImage_Type(Integer32):
    """Custom type h3cSysReloadImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cSysReloadImage_Type.__name__ = "Integer32"
_H3cSysReloadImage_Object = MibTableColumn
h3cSysReloadImage = _H3cSysReloadImage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 3, 1, 4),
    _H3cSysReloadImage_Type()
)
h3cSysReloadImage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSysReloadImage.setStatus("current")


class _H3cSysReloadReason_Type(DisplayString):
    """Custom type h3cSysReloadReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cSysReloadReason_Type.__name__ = "DisplayString"
_H3cSysReloadReason_Object = MibTableColumn
h3cSysReloadReason = _H3cSysReloadReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 3, 1, 5),
    _H3cSysReloadReason_Type()
)
h3cSysReloadReason.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSysReloadReason.setStatus("current")


class _H3cSysReloadScheduleTime_Type(DateAndTime):
    """Custom type h3cSysReloadScheduleTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_H3cSysReloadScheduleTime_Type.__name__ = "DateAndTime"
_H3cSysReloadScheduleTime_Object = MibTableColumn
h3cSysReloadScheduleTime = _H3cSysReloadScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 3, 1, 6),
    _H3cSysReloadScheduleTime_Type()
)
h3cSysReloadScheduleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSysReloadScheduleTime.setStatus("current")
_H3cSysReloadRowStatus_Type = RowStatus
_H3cSysReloadRowStatus_Object = MibTableColumn
h3cSysReloadRowStatus = _H3cSysReloadRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 3, 1, 7),
    _H3cSysReloadRowStatus_Type()
)
h3cSysReloadRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSysReloadRowStatus.setStatus("current")
_H3cSysReloadScheduleTagList_Type = SnmpTagList
_H3cSysReloadScheduleTagList_Object = MibTableColumn
h3cSysReloadScheduleTagList = _H3cSysReloadScheduleTagList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 3, 1, 8),
    _H3cSysReloadScheduleTagList_Type()
)
h3cSysReloadScheduleTagList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSysReloadScheduleTagList.setStatus("current")
_H3cSysReloadTag_Type = SnmpTagValue
_H3cSysReloadTag_Object = MibScalar
h3cSysReloadTag = _H3cSysReloadTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 3, 4),
    _H3cSysReloadTag_Type()
)
h3cSysReloadTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSysReloadTag.setStatus("current")
_H3cSysImage_ObjectIdentity = ObjectIdentity
h3cSysImage = _H3cSysImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 4)
)


class _H3cSysImageNum_Type(Integer32):
    """Custom type h3cSysImageNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cSysImageNum_Type.__name__ = "Integer32"
_H3cSysImageNum_Object = MibScalar
h3cSysImageNum = _H3cSysImageNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 4, 1),
    _H3cSysImageNum_Type()
)
h3cSysImageNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysImageNum.setStatus("current")
_H3cSysImageTable_Object = MibTable
h3cSysImageTable = _H3cSysImageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    h3cSysImageTable.setStatus("current")
_H3cSysImageEntry_Object = MibTableRow
h3cSysImageEntry = _H3cSysImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 4, 2, 1)
)
h3cSysImageEntry.setIndexNames(
    (0, "H3C-SYS-MAN-MIB", "h3cSysImageIndex"),
)
if mibBuilder.loadTexts:
    h3cSysImageEntry.setStatus("current")


class _H3cSysImageIndex_Type(Integer32):
    """Custom type h3cSysImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cSysImageIndex_Type.__name__ = "Integer32"
_H3cSysImageIndex_Object = MibTableColumn
h3cSysImageIndex = _H3cSysImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 4, 2, 1, 1),
    _H3cSysImageIndex_Type()
)
h3cSysImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSysImageIndex.setStatus("current")
_H3cSysImageName_Type = DisplayString
_H3cSysImageName_Object = MibTableColumn
h3cSysImageName = _H3cSysImageName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 4, 2, 1, 2),
    _H3cSysImageName_Type()
)
h3cSysImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysImageName.setStatus("current")


class _H3cSysImageSize_Type(Integer32):
    """Custom type h3cSysImageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cSysImageSize_Type.__name__ = "Integer32"
_H3cSysImageSize_Object = MibTableColumn
h3cSysImageSize = _H3cSysImageSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 4, 2, 1, 3),
    _H3cSysImageSize_Type()
)
h3cSysImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysImageSize.setStatus("current")
_H3cSysImageLocation_Type = DisplayString
_H3cSysImageLocation_Object = MibTableColumn
h3cSysImageLocation = _H3cSysImageLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 4, 2, 1, 4),
    _H3cSysImageLocation_Type()
)
h3cSysImageLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysImageLocation.setStatus("current")


class _H3cSysImageType_Type(Integer32):
    """Custom type h3cSysImageType based on Integer32"""
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


_H3cSysImageType_Type.__name__ = "Integer32"
_H3cSysImageType_Object = MibTableColumn
h3cSysImageType = _H3cSysImageType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 4, 2, 1, 5),
    _H3cSysImageType_Type()
)
h3cSysImageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSysImageType.setStatus("current")
_H3cSysCFGFile_ObjectIdentity = ObjectIdentity
h3cSysCFGFile = _H3cSysCFGFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 5)
)


class _H3cSysCFGFileNum_Type(Integer32):
    """Custom type h3cSysCFGFileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cSysCFGFileNum_Type.__name__ = "Integer32"
_H3cSysCFGFileNum_Object = MibScalar
h3cSysCFGFileNum = _H3cSysCFGFileNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 5, 1),
    _H3cSysCFGFileNum_Type()
)
h3cSysCFGFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysCFGFileNum.setStatus("current")
_H3cSysCFGFileTable_Object = MibTable
h3cSysCFGFileTable = _H3cSysCFGFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    h3cSysCFGFileTable.setStatus("current")
_H3cSysCFGFileEntry_Object = MibTableRow
h3cSysCFGFileEntry = _H3cSysCFGFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 5, 2, 1)
)
h3cSysCFGFileEntry.setIndexNames(
    (0, "H3C-SYS-MAN-MIB", "h3cSysCFGFileIndex"),
)
if mibBuilder.loadTexts:
    h3cSysCFGFileEntry.setStatus("current")


class _H3cSysCFGFileIndex_Type(Integer32):
    """Custom type h3cSysCFGFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cSysCFGFileIndex_Type.__name__ = "Integer32"
_H3cSysCFGFileIndex_Object = MibTableColumn
h3cSysCFGFileIndex = _H3cSysCFGFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 5, 2, 1, 1),
    _H3cSysCFGFileIndex_Type()
)
h3cSysCFGFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSysCFGFileIndex.setStatus("current")
_H3cSysCFGFileName_Type = DisplayString
_H3cSysCFGFileName_Object = MibTableColumn
h3cSysCFGFileName = _H3cSysCFGFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 5, 2, 1, 2),
    _H3cSysCFGFileName_Type()
)
h3cSysCFGFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysCFGFileName.setStatus("current")


class _H3cSysCFGFileSize_Type(Integer32):
    """Custom type h3cSysCFGFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cSysCFGFileSize_Type.__name__ = "Integer32"
_H3cSysCFGFileSize_Object = MibTableColumn
h3cSysCFGFileSize = _H3cSysCFGFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 5, 2, 1, 3),
    _H3cSysCFGFileSize_Type()
)
h3cSysCFGFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysCFGFileSize.setStatus("current")
_H3cSysCFGFileLocation_Type = DisplayString
_H3cSysCFGFileLocation_Object = MibTableColumn
h3cSysCFGFileLocation = _H3cSysCFGFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 5, 2, 1, 4),
    _H3cSysCFGFileLocation_Type()
)
h3cSysCFGFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysCFGFileLocation.setStatus("current")
_H3cSysBtmFile_ObjectIdentity = ObjectIdentity
h3cSysBtmFile = _H3cSysBtmFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 6)
)
_H3cSysBtmFileLoad_ObjectIdentity = ObjectIdentity
h3cSysBtmFileLoad = _H3cSysBtmFileLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 6, 1)
)
_H3cSysBtmLoadMaxNumber_Type = Integer32
_H3cSysBtmLoadMaxNumber_Object = MibScalar
h3cSysBtmLoadMaxNumber = _H3cSysBtmLoadMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 6, 1, 1),
    _H3cSysBtmLoadMaxNumber_Type()
)
h3cSysBtmLoadMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysBtmLoadMaxNumber.setStatus("current")
_H3cSysBtmLoadTable_Object = MibTable
h3cSysBtmLoadTable = _H3cSysBtmLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    h3cSysBtmLoadTable.setStatus("current")
_H3cSysBtmLoadEntry_Object = MibTableRow
h3cSysBtmLoadEntry = _H3cSysBtmLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 6, 2, 1)
)
h3cSysBtmLoadEntry.setIndexNames(
    (0, "H3C-SYS-MAN-MIB", "h3cSysBtmLoadIndex"),
)
if mibBuilder.loadTexts:
    h3cSysBtmLoadEntry.setStatus("current")


class _H3cSysBtmLoadIndex_Type(Integer32):
    """Custom type h3cSysBtmLoadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cSysBtmLoadIndex_Type.__name__ = "Integer32"
_H3cSysBtmLoadIndex_Object = MibTableColumn
h3cSysBtmLoadIndex = _H3cSysBtmLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 6, 2, 1, 1),
    _H3cSysBtmLoadIndex_Type()
)
h3cSysBtmLoadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSysBtmLoadIndex.setStatus("current")


class _H3cSysBtmFileName_Type(OctetString):
    """Custom type h3cSysBtmFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cSysBtmFileName_Type.__name__ = "OctetString"
_H3cSysBtmFileName_Object = MibTableColumn
h3cSysBtmFileName = _H3cSysBtmFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 6, 2, 1, 2),
    _H3cSysBtmFileName_Type()
)
h3cSysBtmFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSysBtmFileName.setStatus("current")


class _H3cSysBtmFileType_Type(Integer32):
    """Custom type h3cSysBtmFileType based on Integer32"""
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


_H3cSysBtmFileType_Type.__name__ = "Integer32"
_H3cSysBtmFileType_Object = MibTableColumn
h3cSysBtmFileType = _H3cSysBtmFileType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 6, 2, 1, 3),
    _H3cSysBtmFileType_Type()
)
h3cSysBtmFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSysBtmFileType.setStatus("current")
_H3cSysBtmRowStatus_Type = RowStatus
_H3cSysBtmRowStatus_Object = MibTableColumn
h3cSysBtmRowStatus = _H3cSysBtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 6, 2, 1, 4),
    _H3cSysBtmRowStatus_Type()
)
h3cSysBtmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSysBtmRowStatus.setStatus("current")


class _H3cSysBtmErrorStatus_Type(Integer32):
    """Custom type h3cSysBtmErrorStatus based on Integer32"""
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


_H3cSysBtmErrorStatus_Type.__name__ = "Integer32"
_H3cSysBtmErrorStatus_Object = MibTableColumn
h3cSysBtmErrorStatus = _H3cSysBtmErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 6, 2, 1, 5),
    _H3cSysBtmErrorStatus_Type()
)
h3cSysBtmErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysBtmErrorStatus.setStatus("current")
_H3cSysBtmLoadTime_Type = TimeTicks
_H3cSysBtmLoadTime_Object = MibTableColumn
h3cSysBtmLoadTime = _H3cSysBtmLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 1, 6, 2, 1, 6),
    _H3cSysBtmLoadTime_Type()
)
h3cSysBtmLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSysBtmLoadTime.setStatus("current")
_H3cSystemManMIBNotifications_ObjectIdentity = ObjectIdentity
h3cSystemManMIBNotifications = _H3cSystemManMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 2)
)
_H3cSystemManMIBConformance_ObjectIdentity = ObjectIdentity
h3cSystemManMIBConformance = _H3cSystemManMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 3)
)
_H3cSystemManMIBCompliances_ObjectIdentity = ObjectIdentity
h3cSystemManMIBCompliances = _H3cSystemManMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 3, 1)
)
_H3cSystemManMIBGroups_ObjectIdentity = ObjectIdentity
h3cSystemManMIBGroups = _H3cSystemManMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 3, 2)
)

# Managed Objects groups

h3cSysClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 3, 2, 1)
)
h3cSysClockGroup.setObjects(
      *(("H3C-SYS-MAN-MIB", "h3cSysLocalClock"),
        ("H3C-SYS-MAN-MIB", "h3cSysSummerTimeEnable"),
        ("H3C-SYS-MAN-MIB", "h3cSysSummerTimeZone"),
        ("H3C-SYS-MAN-MIB", "h3cSysSummerTimeMethod"),
        ("H3C-SYS-MAN-MIB", "h3cSysSummerTimeStart"),
        ("H3C-SYS-MAN-MIB", "h3cSysSummerTimeEnd"),
        ("H3C-SYS-MAN-MIB", "h3cSysSummerTimeOffset"))
)
if mibBuilder.loadTexts:
    h3cSysClockGroup.setStatus("current")

h3cSysReloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 3, 2, 2)
)
h3cSysReloadGroup.setObjects(
      *(("H3C-SYS-MAN-MIB", "h3cSysReloadSchedule"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadAction"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadImage"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadCfgFile"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadReason"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadScheduleTagList"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadTag"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadScheduleTime"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadEntity"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadRowStatus"))
)
if mibBuilder.loadTexts:
    h3cSysReloadGroup.setStatus("current")

h3cSysImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 3, 2, 3)
)
h3cSysImageGroup.setObjects(
      *(("H3C-SYS-MAN-MIB", "h3cSysImageNum"),
        ("H3C-SYS-MAN-MIB", "h3cSysImageName"),
        ("H3C-SYS-MAN-MIB", "h3cSysImageSize"),
        ("H3C-SYS-MAN-MIB", "h3cSysImageLocation"),
        ("H3C-SYS-MAN-MIB", "h3cSysImageType"))
)
if mibBuilder.loadTexts:
    h3cSysImageGroup.setStatus("current")

h3cSysCFGFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 3, 2, 4)
)
h3cSysCFGFileGroup.setObjects(
      *(("H3C-SYS-MAN-MIB", "h3cSysCFGFileNum"),
        ("H3C-SYS-MAN-MIB", "h3cSysCFGFileName"),
        ("H3C-SYS-MAN-MIB", "h3cSysCFGFileSize"),
        ("H3C-SYS-MAN-MIB", "h3cSysCFGFileLocation"))
)
if mibBuilder.loadTexts:
    h3cSysCFGFileGroup.setStatus("current")

h3cSysCurGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 3, 2, 5)
)
h3cSysCurGroup.setObjects(
      *(("H3C-SYS-MAN-MIB", "h3cSysCurCFGFileIndex"),
        ("H3C-SYS-MAN-MIB", "h3cSysCurImageIndex"))
)
if mibBuilder.loadTexts:
    h3cSysCurGroup.setStatus("current")

h3cSystemBtmLoadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 3, 2, 7)
)
h3cSystemBtmLoadGroup.setObjects(
      *(("H3C-SYS-MAN-MIB", "h3cSysCurBtmFileName"),
        ("H3C-SYS-MAN-MIB", "h3cSysCurUpdateBtmFileName"),
        ("H3C-SYS-MAN-MIB", "h3cSysBtmLoadMaxNumber"),
        ("H3C-SYS-MAN-MIB", "h3cSysBtmFileName"),
        ("H3C-SYS-MAN-MIB", "h3cSysBtmFileType"),
        ("H3C-SYS-MAN-MIB", "h3cSysBtmRowStatus"),
        ("H3C-SYS-MAN-MIB", "h3cSysBtmErrorStatus"),
        ("H3C-SYS-MAN-MIB", "h3cSysBtmLoadTime"))
)
if mibBuilder.loadTexts:
    h3cSystemBtmLoadGroup.setStatus("current")


# Notification objects

h3cSysClockChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 2, 1)
)
h3cSysClockChangedNotification.setObjects(
    ("H3C-SYS-MAN-MIB", "h3cSysLocalClock")
)
if mibBuilder.loadTexts:
    h3cSysClockChangedNotification.setStatus(
        "current"
    )

h3cSysReloadNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 2, 2)
)
h3cSysReloadNotification.setObjects(
      *(("H3C-SYS-MAN-MIB", "h3cSysReloadImage"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadCfgFile"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadReason"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadScheduleTime"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadAction"))
)
if mibBuilder.loadTexts:
    h3cSysReloadNotification.setStatus(
        "current"
    )

h3cSysStartUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 2, 3)
)
h3cSysStartUpNotification.setObjects(
    ("H3C-SYS-MAN-MIB", "h3cSysImageType")
)
if mibBuilder.loadTexts:
    h3cSysStartUpNotification.setStatus(
        "current"
    )


# Notifications groups

h3cSystemManNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 3, 2, 6)
)
h3cSystemManNotificationGroup.setObjects(
      *(("H3C-SYS-MAN-MIB", "h3cSysClockChangedNotification"),
        ("H3C-SYS-MAN-MIB", "h3cSysReloadNotification"),
        ("H3C-SYS-MAN-MIB", "h3cSysStartUpNotification"))
)
if mibBuilder.loadTexts:
    h3cSystemManNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cSystemManMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cSystemManMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-SYS-MAN-MIB",
    **{"h3cSystemMan": h3cSystemMan,
       "h3cSystemManMIBObjects": h3cSystemManMIBObjects,
       "h3cSysClock": h3cSysClock,
       "h3cSysLocalClock": h3cSysLocalClock,
       "h3cSysSummerTime": h3cSysSummerTime,
       "h3cSysSummerTimeEnable": h3cSysSummerTimeEnable,
       "h3cSysSummerTimeZone": h3cSysSummerTimeZone,
       "h3cSysSummerTimeMethod": h3cSysSummerTimeMethod,
       "h3cSysSummerTimeStart": h3cSysSummerTimeStart,
       "h3cSysSummerTimeEnd": h3cSysSummerTimeEnd,
       "h3cSysSummerTimeOffset": h3cSysSummerTimeOffset,
       "h3cSysCurrent": h3cSysCurrent,
       "h3cSysCurTable": h3cSysCurTable,
       "h3cSysCurEntry": h3cSysCurEntry,
       "h3cSysCurEntPhysicalIndex": h3cSysCurEntPhysicalIndex,
       "h3cSysCurCFGFileIndex": h3cSysCurCFGFileIndex,
       "h3cSysCurImageIndex": h3cSysCurImageIndex,
       "h3cSysCurBtmFileName": h3cSysCurBtmFileName,
       "h3cSysCurUpdateBtmFileName": h3cSysCurUpdateBtmFileName,
       "h3cSysReload": h3cSysReload,
       "h3cSysReloadSchedule": h3cSysReloadSchedule,
       "h3cSysReloadAction": h3cSysReloadAction,
       "h3cSysReloadScheduleTable": h3cSysReloadScheduleTable,
       "h3cSysReloadScheduleEntry": h3cSysReloadScheduleEntry,
       "h3cSysReloadScheduleIndex": h3cSysReloadScheduleIndex,
       "h3cSysReloadEntity": h3cSysReloadEntity,
       "h3cSysReloadCfgFile": h3cSysReloadCfgFile,
       "h3cSysReloadImage": h3cSysReloadImage,
       "h3cSysReloadReason": h3cSysReloadReason,
       "h3cSysReloadScheduleTime": h3cSysReloadScheduleTime,
       "h3cSysReloadRowStatus": h3cSysReloadRowStatus,
       "h3cSysReloadScheduleTagList": h3cSysReloadScheduleTagList,
       "h3cSysReloadTag": h3cSysReloadTag,
       "h3cSysImage": h3cSysImage,
       "h3cSysImageNum": h3cSysImageNum,
       "h3cSysImageTable": h3cSysImageTable,
       "h3cSysImageEntry": h3cSysImageEntry,
       "h3cSysImageIndex": h3cSysImageIndex,
       "h3cSysImageName": h3cSysImageName,
       "h3cSysImageSize": h3cSysImageSize,
       "h3cSysImageLocation": h3cSysImageLocation,
       "h3cSysImageType": h3cSysImageType,
       "h3cSysCFGFile": h3cSysCFGFile,
       "h3cSysCFGFileNum": h3cSysCFGFileNum,
       "h3cSysCFGFileTable": h3cSysCFGFileTable,
       "h3cSysCFGFileEntry": h3cSysCFGFileEntry,
       "h3cSysCFGFileIndex": h3cSysCFGFileIndex,
       "h3cSysCFGFileName": h3cSysCFGFileName,
       "h3cSysCFGFileSize": h3cSysCFGFileSize,
       "h3cSysCFGFileLocation": h3cSysCFGFileLocation,
       "h3cSysBtmFile": h3cSysBtmFile,
       "h3cSysBtmFileLoad": h3cSysBtmFileLoad,
       "h3cSysBtmLoadMaxNumber": h3cSysBtmLoadMaxNumber,
       "h3cSysBtmLoadTable": h3cSysBtmLoadTable,
       "h3cSysBtmLoadEntry": h3cSysBtmLoadEntry,
       "h3cSysBtmLoadIndex": h3cSysBtmLoadIndex,
       "h3cSysBtmFileName": h3cSysBtmFileName,
       "h3cSysBtmFileType": h3cSysBtmFileType,
       "h3cSysBtmRowStatus": h3cSysBtmRowStatus,
       "h3cSysBtmErrorStatus": h3cSysBtmErrorStatus,
       "h3cSysBtmLoadTime": h3cSysBtmLoadTime,
       "h3cSystemManMIBNotifications": h3cSystemManMIBNotifications,
       "h3cSysClockChangedNotification": h3cSysClockChangedNotification,
       "h3cSysReloadNotification": h3cSysReloadNotification,
       "h3cSysStartUpNotification": h3cSysStartUpNotification,
       "h3cSystemManMIBConformance": h3cSystemManMIBConformance,
       "h3cSystemManMIBCompliances": h3cSystemManMIBCompliances,
       "h3cSystemManMIBCompliance": h3cSystemManMIBCompliance,
       "h3cSystemManMIBGroups": h3cSystemManMIBGroups,
       "h3cSysClockGroup": h3cSysClockGroup,
       "h3cSysReloadGroup": h3cSysReloadGroup,
       "h3cSysImageGroup": h3cSysImageGroup,
       "h3cSysCFGFileGroup": h3cSysCFGFileGroup,
       "h3cSysCurGroup": h3cSysCurGroup,
       "h3cSystemManNotificationGroup": h3cSystemManNotificationGroup,
       "h3cSystemBtmLoadGroup": h3cSystemBtmLoadGroup}
)
