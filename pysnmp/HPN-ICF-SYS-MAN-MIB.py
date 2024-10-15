# SNMP MIB module (HPN-ICF-SYS-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-SYS-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:57 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfSystemMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3)
)
hpnicfSystemMan.setRevisions(
        ("2004-04-08 13:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfSystemManMIBObjects_ObjectIdentity = ObjectIdentity
hpnicfSystemManMIBObjects = _HpnicfSystemManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1)
)
_HpnicfSysClock_ObjectIdentity = ObjectIdentity
hpnicfSysClock = _HpnicfSysClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 1)
)
_HpnicfSysLocalClock_Type = DateAndTime
_HpnicfSysLocalClock_Object = MibScalar
hpnicfSysLocalClock = _HpnicfSysLocalClock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 1, 1),
    _HpnicfSysLocalClock_Type()
)
hpnicfSysLocalClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysLocalClock.setStatus("current")
_HpnicfSysSummerTime_ObjectIdentity = ObjectIdentity
hpnicfSysSummerTime = _HpnicfSysSummerTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 1, 2)
)


class _HpnicfSysSummerTimeEnable_Type(Integer32):
    """Custom type hpnicfSysSummerTimeEnable based on Integer32"""
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


_HpnicfSysSummerTimeEnable_Type.__name__ = "Integer32"
_HpnicfSysSummerTimeEnable_Object = MibScalar
hpnicfSysSummerTimeEnable = _HpnicfSysSummerTimeEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 1, 2, 1),
    _HpnicfSysSummerTimeEnable_Type()
)
hpnicfSysSummerTimeEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysSummerTimeEnable.setStatus("current")


class _HpnicfSysSummerTimeZone_Type(DisplayString):
    """Custom type hpnicfSysSummerTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysSummerTimeZone_Type.__name__ = "DisplayString"
_HpnicfSysSummerTimeZone_Object = MibScalar
hpnicfSysSummerTimeZone = _HpnicfSysSummerTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 1, 2, 2),
    _HpnicfSysSummerTimeZone_Type()
)
hpnicfSysSummerTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysSummerTimeZone.setStatus("current")


class _HpnicfSysSummerTimeMethod_Type(Integer32):
    """Custom type hpnicfSysSummerTimeMethod based on Integer32"""
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


_HpnicfSysSummerTimeMethod_Type.__name__ = "Integer32"
_HpnicfSysSummerTimeMethod_Object = MibScalar
hpnicfSysSummerTimeMethod = _HpnicfSysSummerTimeMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 1, 2, 3),
    _HpnicfSysSummerTimeMethod_Type()
)
hpnicfSysSummerTimeMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysSummerTimeMethod.setStatus("current")


class _HpnicfSysSummerTimeStart_Type(DateAndTime):
    """Custom type hpnicfSysSummerTimeStart based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpnicfSysSummerTimeStart_Type.__name__ = "DateAndTime"
_HpnicfSysSummerTimeStart_Object = MibScalar
hpnicfSysSummerTimeStart = _HpnicfSysSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 1, 2, 4),
    _HpnicfSysSummerTimeStart_Type()
)
hpnicfSysSummerTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysSummerTimeStart.setStatus("current")


class _HpnicfSysSummerTimeEnd_Type(DateAndTime):
    """Custom type hpnicfSysSummerTimeEnd based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpnicfSysSummerTimeEnd_Type.__name__ = "DateAndTime"
_HpnicfSysSummerTimeEnd_Object = MibScalar
hpnicfSysSummerTimeEnd = _HpnicfSysSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 1, 2, 5),
    _HpnicfSysSummerTimeEnd_Type()
)
hpnicfSysSummerTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysSummerTimeEnd.setStatus("current")


class _HpnicfSysSummerTimeOffset_Type(Integer32):
    """Custom type hpnicfSysSummerTimeOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_HpnicfSysSummerTimeOffset_Type.__name__ = "Integer32"
_HpnicfSysSummerTimeOffset_Object = MibScalar
hpnicfSysSummerTimeOffset = _HpnicfSysSummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 1, 2, 6),
    _HpnicfSysSummerTimeOffset_Type()
)
hpnicfSysSummerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysSummerTimeOffset.setStatus("current")


class _HpnicfSysLocalClockString_Type(OctetString):
    """Custom type hpnicfSysLocalClockString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 24),
    )


_HpnicfSysLocalClockString_Type.__name__ = "OctetString"
_HpnicfSysLocalClockString_Object = MibScalar
hpnicfSysLocalClockString = _HpnicfSysLocalClockString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 1, 3),
    _HpnicfSysLocalClockString_Type()
)
hpnicfSysLocalClockString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysLocalClockString.setStatus("current")
_HpnicfSysCurrent_ObjectIdentity = ObjectIdentity
hpnicfSysCurrent = _HpnicfSysCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 2)
)
_HpnicfSysCurTable_Object = MibTable
hpnicfSysCurTable = _HpnicfSysCurTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfSysCurTable.setStatus("current")
_HpnicfSysCurEntry_Object = MibTableRow
hpnicfSysCurEntry = _HpnicfSysCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 2, 1, 1)
)
hpnicfSysCurEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysCurEntPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysCurEntry.setStatus("current")


class _HpnicfSysCurEntPhysicalIndex_Type(Integer32):
    """Custom type hpnicfSysCurEntPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysCurEntPhysicalIndex_Type.__name__ = "Integer32"
_HpnicfSysCurEntPhysicalIndex_Object = MibTableColumn
hpnicfSysCurEntPhysicalIndex = _HpnicfSysCurEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 2, 1, 1, 1),
    _HpnicfSysCurEntPhysicalIndex_Type()
)
hpnicfSysCurEntPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysCurEntPhysicalIndex.setStatus("current")


class _HpnicfSysCurCFGFileIndex_Type(Integer32):
    """Custom type hpnicfSysCurCFGFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysCurCFGFileIndex_Type.__name__ = "Integer32"
_HpnicfSysCurCFGFileIndex_Object = MibTableColumn
hpnicfSysCurCFGFileIndex = _HpnicfSysCurCFGFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 2, 1, 1, 2),
    _HpnicfSysCurCFGFileIndex_Type()
)
hpnicfSysCurCFGFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysCurCFGFileIndex.setStatus("current")


class _HpnicfSysCurImageIndex_Type(Integer32):
    """Custom type hpnicfSysCurImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysCurImageIndex_Type.__name__ = "Integer32"
_HpnicfSysCurImageIndex_Object = MibTableColumn
hpnicfSysCurImageIndex = _HpnicfSysCurImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 2, 1, 1, 3),
    _HpnicfSysCurImageIndex_Type()
)
hpnicfSysCurImageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysCurImageIndex.setStatus("current")


class _HpnicfSysCurBtmFileName_Type(OctetString):
    """Custom type hpnicfSysCurBtmFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfSysCurBtmFileName_Type.__name__ = "OctetString"
_HpnicfSysCurBtmFileName_Object = MibTableColumn
hpnicfSysCurBtmFileName = _HpnicfSysCurBtmFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 2, 1, 1, 4),
    _HpnicfSysCurBtmFileName_Type()
)
hpnicfSysCurBtmFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysCurBtmFileName.setStatus("current")


class _HpnicfSysCurUpdateBtmFileName_Type(OctetString):
    """Custom type hpnicfSysCurUpdateBtmFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfSysCurUpdateBtmFileName_Type.__name__ = "OctetString"
_HpnicfSysCurUpdateBtmFileName_Object = MibTableColumn
hpnicfSysCurUpdateBtmFileName = _HpnicfSysCurUpdateBtmFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 2, 1, 1, 5),
    _HpnicfSysCurUpdateBtmFileName_Type()
)
hpnicfSysCurUpdateBtmFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysCurUpdateBtmFileName.setStatus("current")
_HpnicfSysReload_ObjectIdentity = ObjectIdentity
hpnicfSysReload = _HpnicfSysReload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3)
)


class _HpnicfSysReloadSchedule_Type(Integer32):
    """Custom type hpnicfSysReloadSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysReloadSchedule_Type.__name__ = "Integer32"
_HpnicfSysReloadSchedule_Object = MibScalar
hpnicfSysReloadSchedule = _HpnicfSysReloadSchedule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 1),
    _HpnicfSysReloadSchedule_Type()
)
hpnicfSysReloadSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysReloadSchedule.setStatus("current")


class _HpnicfSysReloadAction_Type(Integer32):
    """Custom type hpnicfSysReloadAction based on Integer32"""
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


_HpnicfSysReloadAction_Type.__name__ = "Integer32"
_HpnicfSysReloadAction_Object = MibScalar
hpnicfSysReloadAction = _HpnicfSysReloadAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 2),
    _HpnicfSysReloadAction_Type()
)
hpnicfSysReloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysReloadAction.setStatus("current")
_HpnicfSysReloadScheduleTable_Object = MibTable
hpnicfSysReloadScheduleTable = _HpnicfSysReloadScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfSysReloadScheduleTable.setStatus("current")
_HpnicfSysReloadScheduleEntry_Object = MibTableRow
hpnicfSysReloadScheduleEntry = _HpnicfSysReloadScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 3, 1)
)
hpnicfSysReloadScheduleEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadScheduleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysReloadScheduleEntry.setStatus("current")


class _HpnicfSysReloadScheduleIndex_Type(Integer32):
    """Custom type hpnicfSysReloadScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysReloadScheduleIndex_Type.__name__ = "Integer32"
_HpnicfSysReloadScheduleIndex_Object = MibTableColumn
hpnicfSysReloadScheduleIndex = _HpnicfSysReloadScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 3, 1, 1),
    _HpnicfSysReloadScheduleIndex_Type()
)
hpnicfSysReloadScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysReloadScheduleIndex.setStatus("current")


class _HpnicfSysReloadEntity_Type(Integer32):
    """Custom type hpnicfSysReloadEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysReloadEntity_Type.__name__ = "Integer32"
_HpnicfSysReloadEntity_Object = MibTableColumn
hpnicfSysReloadEntity = _HpnicfSysReloadEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 3, 1, 2),
    _HpnicfSysReloadEntity_Type()
)
hpnicfSysReloadEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysReloadEntity.setStatus("current")


class _HpnicfSysReloadCfgFile_Type(Integer32):
    """Custom type hpnicfSysReloadCfgFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysReloadCfgFile_Type.__name__ = "Integer32"
_HpnicfSysReloadCfgFile_Object = MibTableColumn
hpnicfSysReloadCfgFile = _HpnicfSysReloadCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 3, 1, 3),
    _HpnicfSysReloadCfgFile_Type()
)
hpnicfSysReloadCfgFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysReloadCfgFile.setStatus("current")


class _HpnicfSysReloadImage_Type(Integer32):
    """Custom type hpnicfSysReloadImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysReloadImage_Type.__name__ = "Integer32"
_HpnicfSysReloadImage_Object = MibTableColumn
hpnicfSysReloadImage = _HpnicfSysReloadImage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 3, 1, 4),
    _HpnicfSysReloadImage_Type()
)
hpnicfSysReloadImage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysReloadImage.setStatus("current")


class _HpnicfSysReloadReason_Type(DisplayString):
    """Custom type hpnicfSysReloadReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysReloadReason_Type.__name__ = "DisplayString"
_HpnicfSysReloadReason_Object = MibTableColumn
hpnicfSysReloadReason = _HpnicfSysReloadReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 3, 1, 5),
    _HpnicfSysReloadReason_Type()
)
hpnicfSysReloadReason.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysReloadReason.setStatus("current")


class _HpnicfSysReloadScheduleTime_Type(DateAndTime):
    """Custom type hpnicfSysReloadScheduleTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpnicfSysReloadScheduleTime_Type.__name__ = "DateAndTime"
_HpnicfSysReloadScheduleTime_Object = MibTableColumn
hpnicfSysReloadScheduleTime = _HpnicfSysReloadScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 3, 1, 6),
    _HpnicfSysReloadScheduleTime_Type()
)
hpnicfSysReloadScheduleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysReloadScheduleTime.setStatus("current")
_HpnicfSysReloadRowStatus_Type = RowStatus
_HpnicfSysReloadRowStatus_Object = MibTableColumn
hpnicfSysReloadRowStatus = _HpnicfSysReloadRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 3, 1, 7),
    _HpnicfSysReloadRowStatus_Type()
)
hpnicfSysReloadRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysReloadRowStatus.setStatus("current")
_HpnicfSysReloadScheduleTagList_Type = SnmpTagList
_HpnicfSysReloadScheduleTagList_Object = MibTableColumn
hpnicfSysReloadScheduleTagList = _HpnicfSysReloadScheduleTagList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 3, 1, 8),
    _HpnicfSysReloadScheduleTagList_Type()
)
hpnicfSysReloadScheduleTagList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysReloadScheduleTagList.setStatus("current")
_HpnicfSysReloadTag_Type = SnmpTagValue
_HpnicfSysReloadTag_Object = MibScalar
hpnicfSysReloadTag = _HpnicfSysReloadTag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 3, 4),
    _HpnicfSysReloadTag_Type()
)
hpnicfSysReloadTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysReloadTag.setStatus("current")
_HpnicfSysImage_ObjectIdentity = ObjectIdentity
hpnicfSysImage = _HpnicfSysImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 4)
)


class _HpnicfSysImageNum_Type(Integer32):
    """Custom type hpnicfSysImageNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysImageNum_Type.__name__ = "Integer32"
_HpnicfSysImageNum_Object = MibScalar
hpnicfSysImageNum = _HpnicfSysImageNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 4, 1),
    _HpnicfSysImageNum_Type()
)
hpnicfSysImageNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysImageNum.setStatus("current")
_HpnicfSysImageTable_Object = MibTable
hpnicfSysImageTable = _HpnicfSysImageTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hpnicfSysImageTable.setStatus("current")
_HpnicfSysImageEntry_Object = MibTableRow
hpnicfSysImageEntry = _HpnicfSysImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 4, 2, 1)
)
hpnicfSysImageEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysImageIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysImageEntry.setStatus("current")


class _HpnicfSysImageIndex_Type(Integer32):
    """Custom type hpnicfSysImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysImageIndex_Type.__name__ = "Integer32"
_HpnicfSysImageIndex_Object = MibTableColumn
hpnicfSysImageIndex = _HpnicfSysImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 4, 2, 1, 1),
    _HpnicfSysImageIndex_Type()
)
hpnicfSysImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysImageIndex.setStatus("current")


class _HpnicfSysImageName_Type(DisplayString):
    """Custom type hpnicfSysImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysImageName_Type.__name__ = "DisplayString"
_HpnicfSysImageName_Object = MibTableColumn
hpnicfSysImageName = _HpnicfSysImageName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 4, 2, 1, 2),
    _HpnicfSysImageName_Type()
)
hpnicfSysImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysImageName.setStatus("current")


class _HpnicfSysImageSize_Type(Integer32):
    """Custom type hpnicfSysImageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysImageSize_Type.__name__ = "Integer32"
_HpnicfSysImageSize_Object = MibTableColumn
hpnicfSysImageSize = _HpnicfSysImageSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 4, 2, 1, 3),
    _HpnicfSysImageSize_Type()
)
hpnicfSysImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysImageSize.setStatus("current")


class _HpnicfSysImageLocation_Type(DisplayString):
    """Custom type hpnicfSysImageLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysImageLocation_Type.__name__ = "DisplayString"
_HpnicfSysImageLocation_Object = MibTableColumn
hpnicfSysImageLocation = _HpnicfSysImageLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 4, 2, 1, 4),
    _HpnicfSysImageLocation_Type()
)
hpnicfSysImageLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysImageLocation.setStatus("current")


class _HpnicfSysImageType_Type(Integer32):
    """Custom type hpnicfSysImageType based on Integer32"""
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


_HpnicfSysImageType_Type.__name__ = "Integer32"
_HpnicfSysImageType_Object = MibTableColumn
hpnicfSysImageType = _HpnicfSysImageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 4, 2, 1, 5),
    _HpnicfSysImageType_Type()
)
hpnicfSysImageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysImageType.setStatus("current")
_HpnicfSysCFGFile_ObjectIdentity = ObjectIdentity
hpnicfSysCFGFile = _HpnicfSysCFGFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 5)
)


class _HpnicfSysCFGFileNum_Type(Integer32):
    """Custom type hpnicfSysCFGFileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysCFGFileNum_Type.__name__ = "Integer32"
_HpnicfSysCFGFileNum_Object = MibScalar
hpnicfSysCFGFileNum = _HpnicfSysCFGFileNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 5, 1),
    _HpnicfSysCFGFileNum_Type()
)
hpnicfSysCFGFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysCFGFileNum.setStatus("current")
_HpnicfSysCFGFileTable_Object = MibTable
hpnicfSysCFGFileTable = _HpnicfSysCFGFileTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hpnicfSysCFGFileTable.setStatus("current")
_HpnicfSysCFGFileEntry_Object = MibTableRow
hpnicfSysCFGFileEntry = _HpnicfSysCFGFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 5, 2, 1)
)
hpnicfSysCFGFileEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysCFGFileIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysCFGFileEntry.setStatus("current")


class _HpnicfSysCFGFileIndex_Type(Integer32):
    """Custom type hpnicfSysCFGFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysCFGFileIndex_Type.__name__ = "Integer32"
_HpnicfSysCFGFileIndex_Object = MibTableColumn
hpnicfSysCFGFileIndex = _HpnicfSysCFGFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 5, 2, 1, 1),
    _HpnicfSysCFGFileIndex_Type()
)
hpnicfSysCFGFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysCFGFileIndex.setStatus("current")


class _HpnicfSysCFGFileName_Type(DisplayString):
    """Custom type hpnicfSysCFGFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysCFGFileName_Type.__name__ = "DisplayString"
_HpnicfSysCFGFileName_Object = MibTableColumn
hpnicfSysCFGFileName = _HpnicfSysCFGFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 5, 2, 1, 2),
    _HpnicfSysCFGFileName_Type()
)
hpnicfSysCFGFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysCFGFileName.setStatus("current")


class _HpnicfSysCFGFileSize_Type(Integer32):
    """Custom type hpnicfSysCFGFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysCFGFileSize_Type.__name__ = "Integer32"
_HpnicfSysCFGFileSize_Object = MibTableColumn
hpnicfSysCFGFileSize = _HpnicfSysCFGFileSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 5, 2, 1, 3),
    _HpnicfSysCFGFileSize_Type()
)
hpnicfSysCFGFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysCFGFileSize.setStatus("current")


class _HpnicfSysCFGFileLocation_Type(DisplayString):
    """Custom type hpnicfSysCFGFileLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysCFGFileLocation_Type.__name__ = "DisplayString"
_HpnicfSysCFGFileLocation_Object = MibTableColumn
hpnicfSysCFGFileLocation = _HpnicfSysCFGFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 5, 2, 1, 4),
    _HpnicfSysCFGFileLocation_Type()
)
hpnicfSysCFGFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysCFGFileLocation.setStatus("current")
_HpnicfSysBtmFile_ObjectIdentity = ObjectIdentity
hpnicfSysBtmFile = _HpnicfSysBtmFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 6)
)
_HpnicfSysBtmFileLoad_ObjectIdentity = ObjectIdentity
hpnicfSysBtmFileLoad = _HpnicfSysBtmFileLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 6, 1)
)
_HpnicfSysBtmLoadMaxNumber_Type = Integer32
_HpnicfSysBtmLoadMaxNumber_Object = MibScalar
hpnicfSysBtmLoadMaxNumber = _HpnicfSysBtmLoadMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 6, 1, 1),
    _HpnicfSysBtmLoadMaxNumber_Type()
)
hpnicfSysBtmLoadMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysBtmLoadMaxNumber.setStatus("current")
_HpnicfSysBtmLoadTable_Object = MibTable
hpnicfSysBtmLoadTable = _HpnicfSysBtmLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hpnicfSysBtmLoadTable.setStatus("current")
_HpnicfSysBtmLoadEntry_Object = MibTableRow
hpnicfSysBtmLoadEntry = _HpnicfSysBtmLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 6, 2, 1)
)
hpnicfSysBtmLoadEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysBtmLoadIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysBtmLoadEntry.setStatus("current")


class _HpnicfSysBtmLoadIndex_Type(Integer32):
    """Custom type hpnicfSysBtmLoadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysBtmLoadIndex_Type.__name__ = "Integer32"
_HpnicfSysBtmLoadIndex_Object = MibTableColumn
hpnicfSysBtmLoadIndex = _HpnicfSysBtmLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 6, 2, 1, 1),
    _HpnicfSysBtmLoadIndex_Type()
)
hpnicfSysBtmLoadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysBtmLoadIndex.setStatus("current")


class _HpnicfSysBtmFileName_Type(OctetString):
    """Custom type hpnicfSysBtmFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfSysBtmFileName_Type.__name__ = "OctetString"
_HpnicfSysBtmFileName_Object = MibTableColumn
hpnicfSysBtmFileName = _HpnicfSysBtmFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 6, 2, 1, 2),
    _HpnicfSysBtmFileName_Type()
)
hpnicfSysBtmFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysBtmFileName.setStatus("current")


class _HpnicfSysBtmFileType_Type(Integer32):
    """Custom type hpnicfSysBtmFileType based on Integer32"""
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


_HpnicfSysBtmFileType_Type.__name__ = "Integer32"
_HpnicfSysBtmFileType_Object = MibTableColumn
hpnicfSysBtmFileType = _HpnicfSysBtmFileType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 6, 2, 1, 3),
    _HpnicfSysBtmFileType_Type()
)
hpnicfSysBtmFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysBtmFileType.setStatus("current")
_HpnicfSysBtmRowStatus_Type = RowStatus
_HpnicfSysBtmRowStatus_Object = MibTableColumn
hpnicfSysBtmRowStatus = _HpnicfSysBtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 6, 2, 1, 4),
    _HpnicfSysBtmRowStatus_Type()
)
hpnicfSysBtmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysBtmRowStatus.setStatus("current")


class _HpnicfSysBtmErrorStatus_Type(Integer32):
    """Custom type hpnicfSysBtmErrorStatus based on Integer32"""
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


_HpnicfSysBtmErrorStatus_Type.__name__ = "Integer32"
_HpnicfSysBtmErrorStatus_Object = MibTableColumn
hpnicfSysBtmErrorStatus = _HpnicfSysBtmErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 6, 2, 1, 5),
    _HpnicfSysBtmErrorStatus_Type()
)
hpnicfSysBtmErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysBtmErrorStatus.setStatus("current")
_HpnicfSysBtmLoadTime_Type = TimeTicks
_HpnicfSysBtmLoadTime_Object = MibTableColumn
hpnicfSysBtmLoadTime = _HpnicfSysBtmLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 6, 2, 1, 6),
    _HpnicfSysBtmLoadTime_Type()
)
hpnicfSysBtmLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysBtmLoadTime.setStatus("current")
_HpnicfSysPackage_ObjectIdentity = ObjectIdentity
hpnicfSysPackage = _HpnicfSysPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7)
)


class _HpnicfSysPackageNum_Type(Integer32):
    """Custom type hpnicfSysPackageNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysPackageNum_Type.__name__ = "Integer32"
_HpnicfSysPackageNum_Object = MibScalar
hpnicfSysPackageNum = _HpnicfSysPackageNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 1),
    _HpnicfSysPackageNum_Type()
)
hpnicfSysPackageNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysPackageNum.setStatus("current")
_HpnicfSysPackageTable_Object = MibTable
hpnicfSysPackageTable = _HpnicfSysPackageTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hpnicfSysPackageTable.setStatus("current")
_HpnicfSysPackageEntry_Object = MibTableRow
hpnicfSysPackageEntry = _HpnicfSysPackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1)
)
hpnicfSysPackageEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysPackageIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysPackageEntry.setStatus("current")


class _HpnicfSysPackageIndex_Type(Integer32):
    """Custom type hpnicfSysPackageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysPackageIndex_Type.__name__ = "Integer32"
_HpnicfSysPackageIndex_Object = MibTableColumn
hpnicfSysPackageIndex = _HpnicfSysPackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1, 1),
    _HpnicfSysPackageIndex_Type()
)
hpnicfSysPackageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysPackageIndex.setStatus("current")


class _HpnicfSysPackageName_Type(DisplayString):
    """Custom type hpnicfSysPackageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysPackageName_Type.__name__ = "DisplayString"
_HpnicfSysPackageName_Object = MibTableColumn
hpnicfSysPackageName = _HpnicfSysPackageName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1, 2),
    _HpnicfSysPackageName_Type()
)
hpnicfSysPackageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysPackageName.setStatus("current")


class _HpnicfSysPackageSize_Type(Unsigned32):
    """Custom type hpnicfSysPackageSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfSysPackageSize_Type.__name__ = "Unsigned32"
_HpnicfSysPackageSize_Object = MibTableColumn
hpnicfSysPackageSize = _HpnicfSysPackageSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1, 3),
    _HpnicfSysPackageSize_Type()
)
hpnicfSysPackageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysPackageSize.setStatus("current")


class _HpnicfSysPackageLocation_Type(DisplayString):
    """Custom type hpnicfSysPackageLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysPackageLocation_Type.__name__ = "DisplayString"
_HpnicfSysPackageLocation_Object = MibTableColumn
hpnicfSysPackageLocation = _HpnicfSysPackageLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1, 4),
    _HpnicfSysPackageLocation_Type()
)
hpnicfSysPackageLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysPackageLocation.setStatus("current")


class _HpnicfSysPackageType_Type(Integer32):
    """Custom type hpnicfSysPackageType based on Integer32"""
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
        *(("boot", 1),
          ("feature", 3),
          ("patch", 4),
          ("system", 2))
    )


_HpnicfSysPackageType_Type.__name__ = "Integer32"
_HpnicfSysPackageType_Object = MibTableColumn
hpnicfSysPackageType = _HpnicfSysPackageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1, 5),
    _HpnicfSysPackageType_Type()
)
hpnicfSysPackageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysPackageType.setStatus("current")


class _HpnicfSysPackageAttribute_Type(Integer32):
    """Custom type hpnicfSysPackageAttribute based on Integer32"""
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
        *(("none", 1),
          ("primary", 2),
          ("primarySecondary", 4),
          ("secondary", 3))
    )


_HpnicfSysPackageAttribute_Type.__name__ = "Integer32"
_HpnicfSysPackageAttribute_Object = MibTableColumn
hpnicfSysPackageAttribute = _HpnicfSysPackageAttribute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1, 6),
    _HpnicfSysPackageAttribute_Type()
)
hpnicfSysPackageAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysPackageAttribute.setStatus("current")


class _HpnicfSysPackageStatus_Type(Integer32):
    """Custom type hpnicfSysPackageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HpnicfSysPackageStatus_Type.__name__ = "Integer32"
_HpnicfSysPackageStatus_Object = MibTableColumn
hpnicfSysPackageStatus = _HpnicfSysPackageStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1, 7),
    _HpnicfSysPackageStatus_Type()
)
hpnicfSysPackageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysPackageStatus.setStatus("current")


class _HpnicfSysPackageDescription_Type(DisplayString):
    """Custom type hpnicfSysPackageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysPackageDescription_Type.__name__ = "DisplayString"
_HpnicfSysPackageDescription_Object = MibTableColumn
hpnicfSysPackageDescription = _HpnicfSysPackageDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1, 8),
    _HpnicfSysPackageDescription_Type()
)
hpnicfSysPackageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysPackageDescription.setStatus("current")


class _HpnicfSysPackageFeature_Type(DisplayString):
    """Custom type hpnicfSysPackageFeature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysPackageFeature_Type.__name__ = "DisplayString"
_HpnicfSysPackageFeature_Object = MibTableColumn
hpnicfSysPackageFeature = _HpnicfSysPackageFeature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1, 9),
    _HpnicfSysPackageFeature_Type()
)
hpnicfSysPackageFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysPackageFeature.setStatus("current")


class _HpnicfSysPackageVersion_Type(DisplayString):
    """Custom type hpnicfSysPackageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysPackageVersion_Type.__name__ = "DisplayString"
_HpnicfSysPackageVersion_Object = MibTableColumn
hpnicfSysPackageVersion = _HpnicfSysPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1, 10),
    _HpnicfSysPackageVersion_Type()
)
hpnicfSysPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysPackageVersion.setStatus("current")


class _HpnicfSysPackageLoadAttribute_Type(Integer32):
    """Custom type hpnicfSysPackageLoadAttribute based on Integer32"""
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
        *(("none", 1),
          ("primary", 2),
          ("primarySecondary", 4),
          ("secondary", 3))
    )


_HpnicfSysPackageLoadAttribute_Type.__name__ = "Integer32"
_HpnicfSysPackageLoadAttribute_Object = MibTableColumn
hpnicfSysPackageLoadAttribute = _HpnicfSysPackageLoadAttribute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1, 11),
    _HpnicfSysPackageLoadAttribute_Type()
)
hpnicfSysPackageLoadAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysPackageLoadAttribute.setStatus("current")


class _HpnicfSysPackageModel_Type(DisplayString):
    """Custom type hpnicfSysPackageModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfSysPackageModel_Type.__name__ = "DisplayString"
_HpnicfSysPackageModel_Object = MibTableColumn
hpnicfSysPackageModel = _HpnicfSysPackageModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 2, 1, 12),
    _HpnicfSysPackageModel_Type()
)
hpnicfSysPackageModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysPackageModel.setStatus("current")


class _HpnicfSysPackageOperateEntryLimit_Type(Integer32):
    """Custom type hpnicfSysPackageOperateEntryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysPackageOperateEntryLimit_Type.__name__ = "Integer32"
_HpnicfSysPackageOperateEntryLimit_Object = MibScalar
hpnicfSysPackageOperateEntryLimit = _HpnicfSysPackageOperateEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 3),
    _HpnicfSysPackageOperateEntryLimit_Type()
)
hpnicfSysPackageOperateEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysPackageOperateEntryLimit.setStatus("current")
_HpnicfSysPackageOperateTable_Object = MibTable
hpnicfSysPackageOperateTable = _HpnicfSysPackageOperateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 4)
)
if mibBuilder.loadTexts:
    hpnicfSysPackageOperateTable.setStatus("current")
_HpnicfSysPackageOperateEntry_Object = MibTableRow
hpnicfSysPackageOperateEntry = _HpnicfSysPackageOperateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 4, 1)
)
hpnicfSysPackageOperateEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysPackageOperateIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysPackageOperateEntry.setStatus("current")


class _HpnicfSysPackageOperateIndex_Type(Integer32):
    """Custom type hpnicfSysPackageOperateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysPackageOperateIndex_Type.__name__ = "Integer32"
_HpnicfSysPackageOperateIndex_Object = MibTableColumn
hpnicfSysPackageOperateIndex = _HpnicfSysPackageOperateIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 4, 1, 1),
    _HpnicfSysPackageOperateIndex_Type()
)
hpnicfSysPackageOperateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysPackageOperateIndex.setStatus("current")


class _HpnicfSysPackageOperatePackIndex_Type(Integer32):
    """Custom type hpnicfSysPackageOperatePackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysPackageOperatePackIndex_Type.__name__ = "Integer32"
_HpnicfSysPackageOperatePackIndex_Object = MibTableColumn
hpnicfSysPackageOperatePackIndex = _HpnicfSysPackageOperatePackIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 4, 1, 2),
    _HpnicfSysPackageOperatePackIndex_Type()
)
hpnicfSysPackageOperatePackIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysPackageOperatePackIndex.setStatus("current")


class _HpnicfSysPackageOperateStatus_Type(Integer32):
    """Custom type hpnicfSysPackageOperateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HpnicfSysPackageOperateStatus_Type.__name__ = "Integer32"
_HpnicfSysPackageOperateStatus_Object = MibTableColumn
hpnicfSysPackageOperateStatus = _HpnicfSysPackageOperateStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 4, 1, 3),
    _HpnicfSysPackageOperateStatus_Type()
)
hpnicfSysPackageOperateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysPackageOperateStatus.setStatus("current")
_HpnicfSysPackageOperateRowStatus_Type = RowStatus
_HpnicfSysPackageOperateRowStatus_Object = MibTableColumn
hpnicfSysPackageOperateRowStatus = _HpnicfSysPackageOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 4, 1, 4),
    _HpnicfSysPackageOperateRowStatus_Type()
)
hpnicfSysPackageOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysPackageOperateRowStatus.setStatus("current")


class _HpnicfSysPackageOperateResult_Type(Integer32):
    """Custom type hpnicfSysPackageOperateResult based on Integer32"""
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
        *(("opInProgress", 1),
          ("opInvalidFile", 4),
          ("opNotSupport", 5),
          ("opSuccess", 2),
          ("opUnknownFailure", 3))
    )


_HpnicfSysPackageOperateResult_Type.__name__ = "Integer32"
_HpnicfSysPackageOperateResult_Object = MibTableColumn
hpnicfSysPackageOperateResult = _HpnicfSysPackageOperateResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 7, 4, 1, 5),
    _HpnicfSysPackageOperateResult_Type()
)
hpnicfSysPackageOperateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysPackageOperateResult.setStatus("current")
_HpnicfSysIpeFile_ObjectIdentity = ObjectIdentity
hpnicfSysIpeFile = _HpnicfSysIpeFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8)
)


class _HpnicfSysIpeFileNum_Type(Integer32):
    """Custom type hpnicfSysIpeFileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfSysIpeFileNum_Type.__name__ = "Integer32"
_HpnicfSysIpeFileNum_Object = MibScalar
hpnicfSysIpeFileNum = _HpnicfSysIpeFileNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 1),
    _HpnicfSysIpeFileNum_Type()
)
hpnicfSysIpeFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpeFileNum.setStatus("current")
_HpnicfSysIpeFileTable_Object = MibTable
hpnicfSysIpeFileTable = _HpnicfSysIpeFileTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 2)
)
if mibBuilder.loadTexts:
    hpnicfSysIpeFileTable.setStatus("current")
_HpnicfSysIpeFileEntry_Object = MibTableRow
hpnicfSysIpeFileEntry = _HpnicfSysIpeFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 2, 1)
)
hpnicfSysIpeFileEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysIpeFileIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysIpeFileEntry.setStatus("current")


class _HpnicfSysIpeFileIndex_Type(Integer32):
    """Custom type hpnicfSysIpeFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysIpeFileIndex_Type.__name__ = "Integer32"
_HpnicfSysIpeFileIndex_Object = MibTableColumn
hpnicfSysIpeFileIndex = _HpnicfSysIpeFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 2, 1, 1),
    _HpnicfSysIpeFileIndex_Type()
)
hpnicfSysIpeFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysIpeFileIndex.setStatus("current")


class _HpnicfSysIpeFileName_Type(DisplayString):
    """Custom type hpnicfSysIpeFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysIpeFileName_Type.__name__ = "DisplayString"
_HpnicfSysIpeFileName_Object = MibTableColumn
hpnicfSysIpeFileName = _HpnicfSysIpeFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 2, 1, 2),
    _HpnicfSysIpeFileName_Type()
)
hpnicfSysIpeFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpeFileName.setStatus("current")


class _HpnicfSysIpeFileSize_Type(Unsigned32):
    """Custom type hpnicfSysIpeFileSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfSysIpeFileSize_Type.__name__ = "Unsigned32"
_HpnicfSysIpeFileSize_Object = MibTableColumn
hpnicfSysIpeFileSize = _HpnicfSysIpeFileSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 2, 1, 3),
    _HpnicfSysIpeFileSize_Type()
)
hpnicfSysIpeFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpeFileSize.setStatus("current")


class _HpnicfSysIpeFileLocation_Type(DisplayString):
    """Custom type hpnicfSysIpeFileLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysIpeFileLocation_Type.__name__ = "DisplayString"
_HpnicfSysIpeFileLocation_Object = MibTableColumn
hpnicfSysIpeFileLocation = _HpnicfSysIpeFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 2, 1, 4),
    _HpnicfSysIpeFileLocation_Type()
)
hpnicfSysIpeFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpeFileLocation.setStatus("current")
_HpnicfSysIpeFileModel_Type = SnmpTagList
_HpnicfSysIpeFileModel_Object = MibTableColumn
hpnicfSysIpeFileModel = _HpnicfSysIpeFileModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 2, 1, 5),
    _HpnicfSysIpeFileModel_Type()
)
hpnicfSysIpeFileModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpeFileModel.setStatus("current")
_HpnicfSysIpePackageTable_Object = MibTable
hpnicfSysIpePackageTable = _HpnicfSysIpePackageTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 3)
)
if mibBuilder.loadTexts:
    hpnicfSysIpePackageTable.setStatus("current")
_HpnicfSysIpePackageEntry_Object = MibTableRow
hpnicfSysIpePackageEntry = _HpnicfSysIpePackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 3, 1)
)
hpnicfSysIpePackageEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysIpeFileIndex"),
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysIpePackageIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysIpePackageEntry.setStatus("current")


class _HpnicfSysIpePackageIndex_Type(Integer32):
    """Custom type hpnicfSysIpePackageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysIpePackageIndex_Type.__name__ = "Integer32"
_HpnicfSysIpePackageIndex_Object = MibTableColumn
hpnicfSysIpePackageIndex = _HpnicfSysIpePackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 3, 1, 1),
    _HpnicfSysIpePackageIndex_Type()
)
hpnicfSysIpePackageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysIpePackageIndex.setStatus("current")


class _HpnicfSysIpePackageName_Type(DisplayString):
    """Custom type hpnicfSysIpePackageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysIpePackageName_Type.__name__ = "DisplayString"
_HpnicfSysIpePackageName_Object = MibTableColumn
hpnicfSysIpePackageName = _HpnicfSysIpePackageName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 3, 1, 2),
    _HpnicfSysIpePackageName_Type()
)
hpnicfSysIpePackageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpePackageName.setStatus("current")


class _HpnicfSysIpePackageSize_Type(Unsigned32):
    """Custom type hpnicfSysIpePackageSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpnicfSysIpePackageSize_Type.__name__ = "Unsigned32"
_HpnicfSysIpePackageSize_Object = MibTableColumn
hpnicfSysIpePackageSize = _HpnicfSysIpePackageSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 3, 1, 3),
    _HpnicfSysIpePackageSize_Type()
)
hpnicfSysIpePackageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpePackageSize.setStatus("current")


class _HpnicfSysIpePackageType_Type(Integer32):
    """Custom type hpnicfSysIpePackageType based on Integer32"""
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
        *(("boot", 1),
          ("feature", 3),
          ("patch", 4),
          ("system", 2))
    )


_HpnicfSysIpePackageType_Type.__name__ = "Integer32"
_HpnicfSysIpePackageType_Object = MibTableColumn
hpnicfSysIpePackageType = _HpnicfSysIpePackageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 3, 1, 4),
    _HpnicfSysIpePackageType_Type()
)
hpnicfSysIpePackageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpePackageType.setStatus("current")


class _HpnicfSysIpePackageDescription_Type(DisplayString):
    """Custom type hpnicfSysIpePackageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysIpePackageDescription_Type.__name__ = "DisplayString"
_HpnicfSysIpePackageDescription_Object = MibTableColumn
hpnicfSysIpePackageDescription = _HpnicfSysIpePackageDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 3, 1, 5),
    _HpnicfSysIpePackageDescription_Type()
)
hpnicfSysIpePackageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpePackageDescription.setStatus("current")


class _HpnicfSysIpePackageFeature_Type(DisplayString):
    """Custom type hpnicfSysIpePackageFeature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysIpePackageFeature_Type.__name__ = "DisplayString"
_HpnicfSysIpePackageFeature_Object = MibTableColumn
hpnicfSysIpePackageFeature = _HpnicfSysIpePackageFeature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 3, 1, 6),
    _HpnicfSysIpePackageFeature_Type()
)
hpnicfSysIpePackageFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpePackageFeature.setStatus("current")


class _HpnicfSysIpePackageVersion_Type(DisplayString):
    """Custom type hpnicfSysIpePackageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysIpePackageVersion_Type.__name__ = "DisplayString"
_HpnicfSysIpePackageVersion_Object = MibTableColumn
hpnicfSysIpePackageVersion = _HpnicfSysIpePackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 3, 1, 7),
    _HpnicfSysIpePackageVersion_Type()
)
hpnicfSysIpePackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpePackageVersion.setStatus("current")


class _HpnicfSysIpePackageModel_Type(DisplayString):
    """Custom type hpnicfSysIpePackageModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfSysIpePackageModel_Type.__name__ = "DisplayString"
_HpnicfSysIpePackageModel_Object = MibTableColumn
hpnicfSysIpePackageModel = _HpnicfSysIpePackageModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 3, 1, 8),
    _HpnicfSysIpePackageModel_Type()
)
hpnicfSysIpePackageModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpePackageModel.setStatus("current")
_HpnicfSysIpeFileOperateTable_Object = MibTable
hpnicfSysIpeFileOperateTable = _HpnicfSysIpeFileOperateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 4)
)
if mibBuilder.loadTexts:
    hpnicfSysIpeFileOperateTable.setStatus("current")
_HpnicfSysIpeFileOperateEntry_Object = MibTableRow
hpnicfSysIpeFileOperateEntry = _HpnicfSysIpeFileOperateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 4, 1)
)
hpnicfSysIpeFileOperateEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysIpeFileOperateIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysIpeFileOperateEntry.setStatus("current")


class _HpnicfSysIpeFileOperateIndex_Type(Integer32):
    """Custom type hpnicfSysIpeFileOperateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysIpeFileOperateIndex_Type.__name__ = "Integer32"
_HpnicfSysIpeFileOperateIndex_Object = MibTableColumn
hpnicfSysIpeFileOperateIndex = _HpnicfSysIpeFileOperateIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 4, 1, 1),
    _HpnicfSysIpeFileOperateIndex_Type()
)
hpnicfSysIpeFileOperateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysIpeFileOperateIndex.setStatus("current")


class _HpnicfSysIpeFileOperateFileIndex_Type(Integer32):
    """Custom type hpnicfSysIpeFileOperateFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysIpeFileOperateFileIndex_Type.__name__ = "Integer32"
_HpnicfSysIpeFileOperateFileIndex_Object = MibTableColumn
hpnicfSysIpeFileOperateFileIndex = _HpnicfSysIpeFileOperateFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 4, 1, 2),
    _HpnicfSysIpeFileOperateFileIndex_Type()
)
hpnicfSysIpeFileOperateFileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysIpeFileOperateFileIndex.setStatus("current")


class _HpnicfSysIpeFileOperateAttribute_Type(Integer32):
    """Custom type hpnicfSysIpeFileOperateAttribute based on Integer32"""
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
        *(("none", 1),
          ("primary", 2),
          ("primarySecondary", 4),
          ("secondary", 3))
    )


_HpnicfSysIpeFileOperateAttribute_Type.__name__ = "Integer32"
_HpnicfSysIpeFileOperateAttribute_Object = MibTableColumn
hpnicfSysIpeFileOperateAttribute = _HpnicfSysIpeFileOperateAttribute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 4, 1, 3),
    _HpnicfSysIpeFileOperateAttribute_Type()
)
hpnicfSysIpeFileOperateAttribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysIpeFileOperateAttribute.setStatus("current")
_HpnicfSysIpeFileOperateRowStatus_Type = RowStatus
_HpnicfSysIpeFileOperateRowStatus_Object = MibTableColumn
hpnicfSysIpeFileOperateRowStatus = _HpnicfSysIpeFileOperateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 4, 1, 4),
    _HpnicfSysIpeFileOperateRowStatus_Type()
)
hpnicfSysIpeFileOperateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysIpeFileOperateRowStatus.setStatus("current")


class _HpnicfSysIpeFileOperateResult_Type(Integer32):
    """Custom type hpnicfSysIpeFileOperateResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("opDeviceFull", 5),
          ("opFileOpenError", 6),
          ("opInProgress", 1),
          ("opInvalidFile", 4),
          ("opSuccess", 2),
          ("opUnknownFailure", 3))
    )


_HpnicfSysIpeFileOperateResult_Type.__name__ = "Integer32"
_HpnicfSysIpeFileOperateResult_Object = MibTableColumn
hpnicfSysIpeFileOperateResult = _HpnicfSysIpeFileOperateResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 8, 4, 1, 5),
    _HpnicfSysIpeFileOperateResult_Type()
)
hpnicfSysIpeFileOperateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysIpeFileOperateResult.setStatus("current")
_HpnicfSysSetBootImage_ObjectIdentity = ObjectIdentity
hpnicfSysSetBootImage = _HpnicfSysSetBootImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9)
)
_HpnicfSysSetBootImageOp_ObjectIdentity = ObjectIdentity
hpnicfSysSetBootImageOp = _HpnicfSysSetBootImageOp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 1)
)


class _HpnicfSysSetBootImageAction_Type(Integer32):
    """Custom type hpnicfSysSetBootImageAction based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("bootLoadPrimary", 3),
          ("bootLoadPrimarySecondary", 5),
          ("bootLoadSecondary", 4),
          ("bootPrimary", 6),
          ("bootPrimarySecondary", 8),
          ("bootSecondary", 7),
          ("done", 2),
          ("loadPrimary", 9),
          ("loadPrimarySecondary", 11),
          ("loadSecondary", 10),
          ("none", 1))
    )


_HpnicfSysSetBootImageAction_Type.__name__ = "Integer32"
_HpnicfSysSetBootImageAction_Object = MibScalar
hpnicfSysSetBootImageAction = _HpnicfSysSetBootImageAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 1, 1),
    _HpnicfSysSetBootImageAction_Type()
)
hpnicfSysSetBootImageAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysSetBootImageAction.setStatus("current")


class _HpnicfSysSetBootImageFileOverWrite_Type(TruthValue):
    """Custom type hpnicfSysSetBootImageFileOverWrite based on TruthValue"""


_HpnicfSysSetBootImageFileOverWrite_Object = MibScalar
hpnicfSysSetBootImageFileOverWrite = _HpnicfSysSetBootImageFileOverWrite_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 1, 2),
    _HpnicfSysSetBootImageFileOverWrite_Type()
)
hpnicfSysSetBootImageFileOverWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysSetBootImageFileOverWrite.setStatus("current")


class _HpnicfSysSetBootImageRemoveIpeFile_Type(TruthValue):
    """Custom type hpnicfSysSetBootImageRemoveIpeFile based on TruthValue"""


_HpnicfSysSetBootImageRemoveIpeFile_Object = MibScalar
hpnicfSysSetBootImageRemoveIpeFile = _HpnicfSysSetBootImageRemoveIpeFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 1, 3),
    _HpnicfSysSetBootImageRemoveIpeFile_Type()
)
hpnicfSysSetBootImageRemoveIpeFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysSetBootImageRemoveIpeFile.setStatus("current")


class _HpnicfSysSetBootImageStatus_Type(Integer32):
    """Custom type hpnicfSysSetBootImageStatus based on Integer32"""
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
        *(("doing", 2),
          ("failed", 4),
          ("none", 1),
          ("success", 3))
    )


_HpnicfSysSetBootImageStatus_Type.__name__ = "Integer32"
_HpnicfSysSetBootImageStatus_Object = MibScalar
hpnicfSysSetBootImageStatus = _HpnicfSysSetBootImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 1, 4),
    _HpnicfSysSetBootImageStatus_Type()
)
hpnicfSysSetBootImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysSetBootImageStatus.setStatus("current")


class _HpnicfSysSetBootImageFailedReason_Type(DisplayString):
    """Custom type hpnicfSysSetBootImageFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysSetBootImageFailedReason_Type.__name__ = "DisplayString"
_HpnicfSysSetBootImageFailedReason_Object = MibScalar
hpnicfSysSetBootImageFailedReason = _HpnicfSysSetBootImageFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 1, 5),
    _HpnicfSysSetBootImageFailedReason_Type()
)
hpnicfSysSetBootImageFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysSetBootImageFailedReason.setStatus("current")
_HpnicfSysBootPackageTable_Object = MibTable
hpnicfSysBootPackageTable = _HpnicfSysBootPackageTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 2)
)
if mibBuilder.loadTexts:
    hpnicfSysBootPackageTable.setStatus("current")
_HpnicfSysBootPackageEntry_Object = MibTableRow
hpnicfSysBootPackageEntry = _HpnicfSysBootPackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 2, 1)
)
hpnicfSysBootPackageEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysBootPackageIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysBootPackageEntry.setStatus("current")


class _HpnicfSysBootPackageIndex_Type(Integer32):
    """Custom type hpnicfSysBootPackageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysBootPackageIndex_Type.__name__ = "Integer32"
_HpnicfSysBootPackageIndex_Object = MibTableColumn
hpnicfSysBootPackageIndex = _HpnicfSysBootPackageIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 2, 1, 1),
    _HpnicfSysBootPackageIndex_Type()
)
hpnicfSysBootPackageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysBootPackageIndex.setStatus("current")
_HpnicfSysBootPackageRowStatus_Type = RowStatus
_HpnicfSysBootPackageRowStatus_Object = MibTableColumn
hpnicfSysBootPackageRowStatus = _HpnicfSysBootPackageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 2, 1, 2),
    _HpnicfSysBootPackageRowStatus_Type()
)
hpnicfSysBootPackageRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysBootPackageRowStatus.setStatus("current")
_HpnicfSysBootIpeTable_Object = MibTable
hpnicfSysBootIpeTable = _HpnicfSysBootIpeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 3)
)
if mibBuilder.loadTexts:
    hpnicfSysBootIpeTable.setStatus("current")
_HpnicfSysBootIpeEntry_Object = MibTableRow
hpnicfSysBootIpeEntry = _HpnicfSysBootIpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 3, 1)
)
hpnicfSysBootIpeEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysBootIpeIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysBootIpeEntry.setStatus("current")


class _HpnicfSysBootIpeIndex_Type(Integer32):
    """Custom type hpnicfSysBootIpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfSysBootIpeIndex_Type.__name__ = "Integer32"
_HpnicfSysBootIpeIndex_Object = MibTableColumn
hpnicfSysBootIpeIndex = _HpnicfSysBootIpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 3, 1, 1),
    _HpnicfSysBootIpeIndex_Type()
)
hpnicfSysBootIpeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysBootIpeIndex.setStatus("current")
_HpnicfSysBootIpeRowStatus_Type = RowStatus
_HpnicfSysBootIpeRowStatus_Object = MibTableColumn
hpnicfSysBootIpeRowStatus = _HpnicfSysBootIpeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 3, 1, 2),
    _HpnicfSysBootIpeRowStatus_Type()
)
hpnicfSysBootIpeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSysBootIpeRowStatus.setStatus("current")
_HpnicfSysSetBootImageResultTable_Object = MibTable
hpnicfSysSetBootImageResultTable = _HpnicfSysSetBootImageResultTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 4)
)
if mibBuilder.loadTexts:
    hpnicfSysSetBootImageResultTable.setStatus("current")
_HpnicfSysSetBootImageResultEntry_Object = MibTableRow
hpnicfSysSetBootImageResultEntry = _HpnicfSysSetBootImageResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 4, 1)
)
hpnicfSysSetBootImageResultEntry.setIndexNames(
    (0, "HPN-ICF-SYS-MAN-MIB", "hpnicfSysSetBootImageResultIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSysSetBootImageResultEntry.setStatus("current")


class _HpnicfSysSetBootImageResultIndex_Type(Integer32):
    """Custom type hpnicfSysSetBootImageResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfSysSetBootImageResultIndex_Type.__name__ = "Integer32"
_HpnicfSysSetBootImageResultIndex_Object = MibTableColumn
hpnicfSysSetBootImageResultIndex = _HpnicfSysSetBootImageResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 4, 1, 1),
    _HpnicfSysSetBootImageResultIndex_Type()
)
hpnicfSysSetBootImageResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSysSetBootImageResultIndex.setStatus("current")


class _HpnicfSysSetBootImageResultStatusOfEachCard_Type(Integer32):
    """Custom type hpnicfSysSetBootImageResultStatusOfEachCard based on Integer32"""
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
        *(("doing", 2),
          ("failed", 4),
          ("none", 1),
          ("success", 3))
    )


_HpnicfSysSetBootImageResultStatusOfEachCard_Type.__name__ = "Integer32"
_HpnicfSysSetBootImageResultStatusOfEachCard_Object = MibTableColumn
hpnicfSysSetBootImageResultStatusOfEachCard = _HpnicfSysSetBootImageResultStatusOfEachCard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 4, 1, 2),
    _HpnicfSysSetBootImageResultStatusOfEachCard_Type()
)
hpnicfSysSetBootImageResultStatusOfEachCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysSetBootImageResultStatusOfEachCard.setStatus("current")


class _HpnicfSysSetBootImageFailedReasonOfEachCard_Type(DisplayString):
    """Custom type hpnicfSysSetBootImageFailedReasonOfEachCard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSysSetBootImageFailedReasonOfEachCard_Type.__name__ = "DisplayString"
_HpnicfSysSetBootImageFailedReasonOfEachCard_Object = MibTableColumn
hpnicfSysSetBootImageFailedReasonOfEachCard = _HpnicfSysSetBootImageFailedReasonOfEachCard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 1, 9, 4, 1, 3),
    _HpnicfSysSetBootImageFailedReasonOfEachCard_Type()
)
hpnicfSysSetBootImageFailedReasonOfEachCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysSetBootImageFailedReasonOfEachCard.setStatus("current")
_HpnicfSystemManMIBNotifications_ObjectIdentity = ObjectIdentity
hpnicfSystemManMIBNotifications = _HpnicfSystemManMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 2)
)
_HpnicfSystemManMIBConformance_ObjectIdentity = ObjectIdentity
hpnicfSystemManMIBConformance = _HpnicfSystemManMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 3)
)
_HpnicfSystemManMIBCompliances_ObjectIdentity = ObjectIdentity
hpnicfSystemManMIBCompliances = _HpnicfSystemManMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 3, 1)
)
_HpnicfSystemManMIBGroups_ObjectIdentity = ObjectIdentity
hpnicfSystemManMIBGroups = _HpnicfSystemManMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 3, 2)
)

# Managed Objects groups

hpnicfSysClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 3, 2, 1)
)
hpnicfSysClockGroup.setObjects(
      *(("HPN-ICF-SYS-MAN-MIB", "hpnicfSysLocalClock"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysSummerTimeEnable"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysSummerTimeZone"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysSummerTimeMethod"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysSummerTimeStart"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysSummerTimeEnd"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysSummerTimeOffset"))
)
if mibBuilder.loadTexts:
    hpnicfSysClockGroup.setStatus("current")

hpnicfSysReloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 3, 2, 2)
)
hpnicfSysReloadGroup.setObjects(
      *(("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadSchedule"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadAction"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadImage"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadCfgFile"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadReason"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadScheduleTagList"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadTag"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadScheduleTime"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadEntity"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfSysReloadGroup.setStatus("current")

hpnicfSysImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 3, 2, 3)
)
hpnicfSysImageGroup.setObjects(
      *(("HPN-ICF-SYS-MAN-MIB", "hpnicfSysImageNum"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysImageName"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysImageSize"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysImageLocation"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysImageType"))
)
if mibBuilder.loadTexts:
    hpnicfSysImageGroup.setStatus("current")

hpnicfSysCFGFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 3, 2, 4)
)
hpnicfSysCFGFileGroup.setObjects(
      *(("HPN-ICF-SYS-MAN-MIB", "hpnicfSysCFGFileNum"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysCFGFileName"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysCFGFileSize"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysCFGFileLocation"))
)
if mibBuilder.loadTexts:
    hpnicfSysCFGFileGroup.setStatus("current")

hpnicfSysCurGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 3, 2, 5)
)
hpnicfSysCurGroup.setObjects(
      *(("HPN-ICF-SYS-MAN-MIB", "hpnicfSysCurCFGFileIndex"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysCurImageIndex"))
)
if mibBuilder.loadTexts:
    hpnicfSysCurGroup.setStatus("current")

hpnicfSystemBtmLoadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 3, 2, 7)
)
hpnicfSystemBtmLoadGroup.setObjects(
      *(("HPN-ICF-SYS-MAN-MIB", "hpnicfSysCurBtmFileName"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysCurUpdateBtmFileName"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysBtmLoadMaxNumber"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysBtmFileName"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysBtmFileType"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysBtmRowStatus"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysBtmErrorStatus"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysBtmLoadTime"))
)
if mibBuilder.loadTexts:
    hpnicfSystemBtmLoadGroup.setStatus("current")


# Notification objects

hpnicfSysClockChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 2, 1)
)
hpnicfSysClockChangedNotification.setObjects(
    ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysLocalClock")
)
if mibBuilder.loadTexts:
    hpnicfSysClockChangedNotification.setStatus(
        "current"
    )

hpnicfSysReloadNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 2, 2)
)
hpnicfSysReloadNotification.setObjects(
      *(("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadImage"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadCfgFile"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadReason"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadScheduleTime"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadAction"))
)
if mibBuilder.loadTexts:
    hpnicfSysReloadNotification.setStatus(
        "current"
    )

hpnicfSysStartUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 2, 3)
)
hpnicfSysStartUpNotification.setObjects(
    ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysImageType")
)
if mibBuilder.loadTexts:
    hpnicfSysStartUpNotification.setStatus(
        "current"
    )


# Notifications groups

hpnicfSystemManNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 3, 2, 6)
)
hpnicfSystemManNotificationGroup.setObjects(
      *(("HPN-ICF-SYS-MAN-MIB", "hpnicfSysClockChangedNotification"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysReloadNotification"),
        ("HPN-ICF-SYS-MAN-MIB", "hpnicfSysStartUpNotification"))
)
if mibBuilder.loadTexts:
    hpnicfSystemManNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfSystemManMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfSystemManMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-SYS-MAN-MIB",
    **{"hpnicfSystemMan": hpnicfSystemMan,
       "hpnicfSystemManMIBObjects": hpnicfSystemManMIBObjects,
       "hpnicfSysClock": hpnicfSysClock,
       "hpnicfSysLocalClock": hpnicfSysLocalClock,
       "hpnicfSysSummerTime": hpnicfSysSummerTime,
       "hpnicfSysSummerTimeEnable": hpnicfSysSummerTimeEnable,
       "hpnicfSysSummerTimeZone": hpnicfSysSummerTimeZone,
       "hpnicfSysSummerTimeMethod": hpnicfSysSummerTimeMethod,
       "hpnicfSysSummerTimeStart": hpnicfSysSummerTimeStart,
       "hpnicfSysSummerTimeEnd": hpnicfSysSummerTimeEnd,
       "hpnicfSysSummerTimeOffset": hpnicfSysSummerTimeOffset,
       "hpnicfSysLocalClockString": hpnicfSysLocalClockString,
       "hpnicfSysCurrent": hpnicfSysCurrent,
       "hpnicfSysCurTable": hpnicfSysCurTable,
       "hpnicfSysCurEntry": hpnicfSysCurEntry,
       "hpnicfSysCurEntPhysicalIndex": hpnicfSysCurEntPhysicalIndex,
       "hpnicfSysCurCFGFileIndex": hpnicfSysCurCFGFileIndex,
       "hpnicfSysCurImageIndex": hpnicfSysCurImageIndex,
       "hpnicfSysCurBtmFileName": hpnicfSysCurBtmFileName,
       "hpnicfSysCurUpdateBtmFileName": hpnicfSysCurUpdateBtmFileName,
       "hpnicfSysReload": hpnicfSysReload,
       "hpnicfSysReloadSchedule": hpnicfSysReloadSchedule,
       "hpnicfSysReloadAction": hpnicfSysReloadAction,
       "hpnicfSysReloadScheduleTable": hpnicfSysReloadScheduleTable,
       "hpnicfSysReloadScheduleEntry": hpnicfSysReloadScheduleEntry,
       "hpnicfSysReloadScheduleIndex": hpnicfSysReloadScheduleIndex,
       "hpnicfSysReloadEntity": hpnicfSysReloadEntity,
       "hpnicfSysReloadCfgFile": hpnicfSysReloadCfgFile,
       "hpnicfSysReloadImage": hpnicfSysReloadImage,
       "hpnicfSysReloadReason": hpnicfSysReloadReason,
       "hpnicfSysReloadScheduleTime": hpnicfSysReloadScheduleTime,
       "hpnicfSysReloadRowStatus": hpnicfSysReloadRowStatus,
       "hpnicfSysReloadScheduleTagList": hpnicfSysReloadScheduleTagList,
       "hpnicfSysReloadTag": hpnicfSysReloadTag,
       "hpnicfSysImage": hpnicfSysImage,
       "hpnicfSysImageNum": hpnicfSysImageNum,
       "hpnicfSysImageTable": hpnicfSysImageTable,
       "hpnicfSysImageEntry": hpnicfSysImageEntry,
       "hpnicfSysImageIndex": hpnicfSysImageIndex,
       "hpnicfSysImageName": hpnicfSysImageName,
       "hpnicfSysImageSize": hpnicfSysImageSize,
       "hpnicfSysImageLocation": hpnicfSysImageLocation,
       "hpnicfSysImageType": hpnicfSysImageType,
       "hpnicfSysCFGFile": hpnicfSysCFGFile,
       "hpnicfSysCFGFileNum": hpnicfSysCFGFileNum,
       "hpnicfSysCFGFileTable": hpnicfSysCFGFileTable,
       "hpnicfSysCFGFileEntry": hpnicfSysCFGFileEntry,
       "hpnicfSysCFGFileIndex": hpnicfSysCFGFileIndex,
       "hpnicfSysCFGFileName": hpnicfSysCFGFileName,
       "hpnicfSysCFGFileSize": hpnicfSysCFGFileSize,
       "hpnicfSysCFGFileLocation": hpnicfSysCFGFileLocation,
       "hpnicfSysBtmFile": hpnicfSysBtmFile,
       "hpnicfSysBtmFileLoad": hpnicfSysBtmFileLoad,
       "hpnicfSysBtmLoadMaxNumber": hpnicfSysBtmLoadMaxNumber,
       "hpnicfSysBtmLoadTable": hpnicfSysBtmLoadTable,
       "hpnicfSysBtmLoadEntry": hpnicfSysBtmLoadEntry,
       "hpnicfSysBtmLoadIndex": hpnicfSysBtmLoadIndex,
       "hpnicfSysBtmFileName": hpnicfSysBtmFileName,
       "hpnicfSysBtmFileType": hpnicfSysBtmFileType,
       "hpnicfSysBtmRowStatus": hpnicfSysBtmRowStatus,
       "hpnicfSysBtmErrorStatus": hpnicfSysBtmErrorStatus,
       "hpnicfSysBtmLoadTime": hpnicfSysBtmLoadTime,
       "hpnicfSysPackage": hpnicfSysPackage,
       "hpnicfSysPackageNum": hpnicfSysPackageNum,
       "hpnicfSysPackageTable": hpnicfSysPackageTable,
       "hpnicfSysPackageEntry": hpnicfSysPackageEntry,
       "hpnicfSysPackageIndex": hpnicfSysPackageIndex,
       "hpnicfSysPackageName": hpnicfSysPackageName,
       "hpnicfSysPackageSize": hpnicfSysPackageSize,
       "hpnicfSysPackageLocation": hpnicfSysPackageLocation,
       "hpnicfSysPackageType": hpnicfSysPackageType,
       "hpnicfSysPackageAttribute": hpnicfSysPackageAttribute,
       "hpnicfSysPackageStatus": hpnicfSysPackageStatus,
       "hpnicfSysPackageDescription": hpnicfSysPackageDescription,
       "hpnicfSysPackageFeature": hpnicfSysPackageFeature,
       "hpnicfSysPackageVersion": hpnicfSysPackageVersion,
       "hpnicfSysPackageLoadAttribute": hpnicfSysPackageLoadAttribute,
       "hpnicfSysPackageModel": hpnicfSysPackageModel,
       "hpnicfSysPackageOperateEntryLimit": hpnicfSysPackageOperateEntryLimit,
       "hpnicfSysPackageOperateTable": hpnicfSysPackageOperateTable,
       "hpnicfSysPackageOperateEntry": hpnicfSysPackageOperateEntry,
       "hpnicfSysPackageOperateIndex": hpnicfSysPackageOperateIndex,
       "hpnicfSysPackageOperatePackIndex": hpnicfSysPackageOperatePackIndex,
       "hpnicfSysPackageOperateStatus": hpnicfSysPackageOperateStatus,
       "hpnicfSysPackageOperateRowStatus": hpnicfSysPackageOperateRowStatus,
       "hpnicfSysPackageOperateResult": hpnicfSysPackageOperateResult,
       "hpnicfSysIpeFile": hpnicfSysIpeFile,
       "hpnicfSysIpeFileNum": hpnicfSysIpeFileNum,
       "hpnicfSysIpeFileTable": hpnicfSysIpeFileTable,
       "hpnicfSysIpeFileEntry": hpnicfSysIpeFileEntry,
       "hpnicfSysIpeFileIndex": hpnicfSysIpeFileIndex,
       "hpnicfSysIpeFileName": hpnicfSysIpeFileName,
       "hpnicfSysIpeFileSize": hpnicfSysIpeFileSize,
       "hpnicfSysIpeFileLocation": hpnicfSysIpeFileLocation,
       "hpnicfSysIpeFileModel": hpnicfSysIpeFileModel,
       "hpnicfSysIpePackageTable": hpnicfSysIpePackageTable,
       "hpnicfSysIpePackageEntry": hpnicfSysIpePackageEntry,
       "hpnicfSysIpePackageIndex": hpnicfSysIpePackageIndex,
       "hpnicfSysIpePackageName": hpnicfSysIpePackageName,
       "hpnicfSysIpePackageSize": hpnicfSysIpePackageSize,
       "hpnicfSysIpePackageType": hpnicfSysIpePackageType,
       "hpnicfSysIpePackageDescription": hpnicfSysIpePackageDescription,
       "hpnicfSysIpePackageFeature": hpnicfSysIpePackageFeature,
       "hpnicfSysIpePackageVersion": hpnicfSysIpePackageVersion,
       "hpnicfSysIpePackageModel": hpnicfSysIpePackageModel,
       "hpnicfSysIpeFileOperateTable": hpnicfSysIpeFileOperateTable,
       "hpnicfSysIpeFileOperateEntry": hpnicfSysIpeFileOperateEntry,
       "hpnicfSysIpeFileOperateIndex": hpnicfSysIpeFileOperateIndex,
       "hpnicfSysIpeFileOperateFileIndex": hpnicfSysIpeFileOperateFileIndex,
       "hpnicfSysIpeFileOperateAttribute": hpnicfSysIpeFileOperateAttribute,
       "hpnicfSysIpeFileOperateRowStatus": hpnicfSysIpeFileOperateRowStatus,
       "hpnicfSysIpeFileOperateResult": hpnicfSysIpeFileOperateResult,
       "hpnicfSysSetBootImage": hpnicfSysSetBootImage,
       "hpnicfSysSetBootImageOp": hpnicfSysSetBootImageOp,
       "hpnicfSysSetBootImageAction": hpnicfSysSetBootImageAction,
       "hpnicfSysSetBootImageFileOverWrite": hpnicfSysSetBootImageFileOverWrite,
       "hpnicfSysSetBootImageRemoveIpeFile": hpnicfSysSetBootImageRemoveIpeFile,
       "hpnicfSysSetBootImageStatus": hpnicfSysSetBootImageStatus,
       "hpnicfSysSetBootImageFailedReason": hpnicfSysSetBootImageFailedReason,
       "hpnicfSysBootPackageTable": hpnicfSysBootPackageTable,
       "hpnicfSysBootPackageEntry": hpnicfSysBootPackageEntry,
       "hpnicfSysBootPackageIndex": hpnicfSysBootPackageIndex,
       "hpnicfSysBootPackageRowStatus": hpnicfSysBootPackageRowStatus,
       "hpnicfSysBootIpeTable": hpnicfSysBootIpeTable,
       "hpnicfSysBootIpeEntry": hpnicfSysBootIpeEntry,
       "hpnicfSysBootIpeIndex": hpnicfSysBootIpeIndex,
       "hpnicfSysBootIpeRowStatus": hpnicfSysBootIpeRowStatus,
       "hpnicfSysSetBootImageResultTable": hpnicfSysSetBootImageResultTable,
       "hpnicfSysSetBootImageResultEntry": hpnicfSysSetBootImageResultEntry,
       "hpnicfSysSetBootImageResultIndex": hpnicfSysSetBootImageResultIndex,
       "hpnicfSysSetBootImageResultStatusOfEachCard": hpnicfSysSetBootImageResultStatusOfEachCard,
       "hpnicfSysSetBootImageFailedReasonOfEachCard": hpnicfSysSetBootImageFailedReasonOfEachCard,
       "hpnicfSystemManMIBNotifications": hpnicfSystemManMIBNotifications,
       "hpnicfSysClockChangedNotification": hpnicfSysClockChangedNotification,
       "hpnicfSysReloadNotification": hpnicfSysReloadNotification,
       "hpnicfSysStartUpNotification": hpnicfSysStartUpNotification,
       "hpnicfSystemManMIBConformance": hpnicfSystemManMIBConformance,
       "hpnicfSystemManMIBCompliances": hpnicfSystemManMIBCompliances,
       "hpnicfSystemManMIBCompliance": hpnicfSystemManMIBCompliance,
       "hpnicfSystemManMIBGroups": hpnicfSystemManMIBGroups,
       "hpnicfSysClockGroup": hpnicfSysClockGroup,
       "hpnicfSysReloadGroup": hpnicfSysReloadGroup,
       "hpnicfSysImageGroup": hpnicfSysImageGroup,
       "hpnicfSysCFGFileGroup": hpnicfSysCFGFileGroup,
       "hpnicfSysCurGroup": hpnicfSysCurGroup,
       "hpnicfSystemManNotificationGroup": hpnicfSystemManNotificationGroup,
       "hpnicfSystemBtmLoadGroup": hpnicfSystemBtmLoadGroup}
)
