# SNMP MIB module (HUAWEI-SYS-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SYS-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:06 2024
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

(PhysicalIndex,
 entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex",
    "entPhysicalName")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

huaweiSystemManMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19)
)
huaweiSystemManMIB.setRevisions(
        ("2015-03-10 00:00",
         "2015-01-12 00:00",
         "2014-09-15 00:00",
         "2014-09-12 00:00",
         "2014-09-03 00:00",
         "2014-07-28 00:00",
         "2014-07-23 00:00",
         "2014-07-08 00:00",
         "2014-06-03 00:00",
         "2014-05-22 00:00",
         "2014-03-27 00:00",
         "2014-03-18 00:00",
         "2014-03-17 00:00",
         "2013-10-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWPatchErrorType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              30,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              55,
              56,
              57,
              58,
              59,
              70,
              71,
              72,
              73,
              80,
              81,
              82,
              90,
              91,
              92,
              93,
              95,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              169,
              170,
              171,
              172,
              173,
              174,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("activeBaseAddrNotSuited", 46),
          ("activeCodeAddrNotSuited", 44),
          ("activeDataAddrNotSuited", 45),
          ("activeFormatUnknown", 47),
          ("activeHasBeenActived", 41),
          ("activeNotExist", 42),
          ("activeNumInvalid", 40),
          ("activeStateInvalid", 43),
          ("addlistBadParam", 105),
          ("addlistMemAllocFail", 106),
          ("appendListAddFail", 126),
          ("appendListBadParam", 125),
          ("caclcrcBadUnitCrc", 95),
          ("caclcrcFileCrcInvalid", 90),
          ("caclcrcNumInvalid", 93),
          ("caclcrcOutputIsNull", 92),
          ("caclcrcUnitCrcInvalid", 91),
          ("chgproChangeModeFailed", 30),
          ("deactBadState", 73),
          ("deactNumInvalid", 70),
          ("deactRunOrActive", 71),
          ("deactRunningState", 72),
          ("depToInterAddFail", 122),
          ("depToInterBadParam", 120),
          ("depToInterInvalidNo", 121),
          ("depToListAddItemFail", 110),
          ("depToListBadParamDep", 107),
          ("depToListBadParamList", 108),
          ("depToListMemFreeFail", 109),
          ("fetchBaseAddrNotSuited", 18),
          ("fetchBufferFail", 148),
          ("fetchBufferPara", 147),
          ("fetchCodeAddrNotSuited", 16),
          ("fetchCodeLenOverflow", 19),
          ("fetchCommonAfterTemp", 14),
          ("fetchDataAddrNotSuited", 17),
          ("fetchDataLenOverflow", 20),
          ("fetchFlagNotSame", 6),
          ("fetchFuncNumTooMany", 12),
          ("fetchInputIsNull", 5),
          ("fetchLengthNotSuited", 15),
          ("fetchOldAfterIndependent", 103),
          ("fetchPatNoInvalid", 9),
          ("fetchProgCrcInvalid", 8),
          ("fetchProgVerInvalid", 7),
          ("fetchTotalNumInvalid", 10),
          ("fetchTypeInvalid", 13),
          ("fetchUnitCrcInvalid", 11),
          ("fetchUpdateDependency", 104),
          ("getInfoBufNull", 162),
          ("getInfoFileCrcInvalid", 166),
          ("getInfoFlagNotSame", 164),
          ("getInfoOutputNull", 163),
          ("getInfoProgCrcInvalid", 165),
          ("getInfoUnitCrcInvalid", 167),
          ("getStatePara", 149),
          ("indActiveAlreadyActive", 128),
          ("indActiveAlreadyRunning", 150),
          ("indActiveBadParam", 127),
          ("indActiveBaseAddrNotSuited", 137),
          ("indActiveCodeAddrNotSuited", 135),
          ("indActiveDataAddrNotSuited", 136),
          ("indActiveDepIdle", 133),
          ("indActiveDepInvalid", 134),
          ("indActiveFuncFail", 139),
          ("indActiveIdle", 171),
          ("indActiveInvalid", 172),
          ("indActiveListAppendFail", 131),
          ("indActiveListFail", 129),
          ("indActiveListGenFail", 130),
          ("indActiveMemFreeFail", 132),
          ("indActiveNotLoaded", 138),
          ("indBitTblToArrayAllocFail", 155),
          ("indBitTblToArrayBitsetLess", 157),
          ("indBitTblToArrayBitsetMore", 156),
          ("indBitTblToArrayFreeFail", 154),
          ("indBitTblToArrayInputNull", 153),
          ("indDeactiveDeative", 173),
          ("indDeactiveFail", 142),
          ("indDeactiveFreeNull", 160),
          ("indDeactiveInvalid", 176),
          ("indDeactiveRunning", 174),
          ("indFetchActive", 183),
          ("indFetchDeactive", 184),
          ("indFetchInvalid", 186),
          ("indFetchRunning", 185),
          ("indFreeListInputNull", 151),
          ("indFreeListMemFreeErr", 152),
          ("indGetDepOfPara", 144),
          ("indGetDepOnFail", 146),
          ("indGetDepOnPara", 145),
          ("indPatchFileNoInd", 140),
          ("indPatchOpNotconfig", 169),
          ("indRemoveFail", 143),
          ("indRemoveFreeFail", 161),
          ("indRemoveIdle", 181),
          ("indRemoveInvalid", 182),
          ("indRunDeactive", 177),
          ("indRunFail", 141),
          ("indRunIdle", 179),
          ("indRunInvalid", 180),
          ("indRunRunning", 178),
          ("initMemProtectFail", 2),
          ("initNoMemory", 1),
          ("interToDepAppendFail", 124),
          ("interToDepBadParam", 123),
          ("listToDepBadParamAllocFail", 158),
          ("listToDepBadParamDep", 111),
          ("listToDepBadParamDepCount", 113),
          ("listToDepBadParamFreeFail", 159),
          ("listToDepBadParamList", 112),
          ("normalOpNotconfig", 170),
          ("patchFileNotExist", 187),
          ("patchMisoperation", 190),
          ("patchPackageError", 189),
          ("patchRestoreFailed", 188),
          ("removeBadStatus", 82),
          ("removeHasInIdle", 81),
          ("removeNumInvalid", 80),
          ("runBadState", 59),
          ("runHasInRunning", 56),
          ("runIdleState", 58),
          ("runNotActive", 57),
          ("runNumInvalid", 55),
          ("showCodeLenIsZero", 101),
          ("showDataLenIsZero", 102),
          ("showNumInvalid", 100),
          ("unknown", 65535),
          ("updateDepBadParam", 114),
          ("updateDepDepToListFail", 116),
          ("updateDepFromInterFail", 118),
          ("updateDepListToDepFail", 119),
          ("updateDepMemAllocFail", 115),
          ("updateDepToInterFail", 117))
    )



# MIB Managed Objects in the order of their OIDs

_HuaweiSystemManMIBObjects_ObjectIdentity = ObjectIdentity
huaweiSystemManMIBObjects = _HuaweiSystemManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1)
)
_HwSysClock_ObjectIdentity = ObjectIdentity
hwSysClock = _HwSysClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 1)
)
_HwSysLocalClock_Type = DateAndTime
_HwSysLocalClock_Object = MibScalar
hwSysLocalClock = _HwSysLocalClock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 1, 1),
    _HwSysLocalClock_Type()
)
hwSysLocalClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysLocalClock.setStatus("current")
_HwSysCurrent_ObjectIdentity = ObjectIdentity
hwSysCurrent = _HwSysCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 2)
)
_HwSysCurTable_Object = MibTable
hwSysCurTable = _HwSysCurTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwSysCurTable.setStatus("current")
_HwSysCurEntry_Object = MibTableRow
hwSysCurEntry = _HwSysCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 2, 1, 1)
)
hwSysCurEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysCurEntPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwSysCurEntry.setStatus("current")


class _HwSysCurEntPhysicalIndex_Type(Integer32):
    """Custom type hwSysCurEntPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysCurEntPhysicalIndex_Type.__name__ = "Integer32"
_HwSysCurEntPhysicalIndex_Object = MibTableColumn
hwSysCurEntPhysicalIndex = _HwSysCurEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 2, 1, 1, 1),
    _HwSysCurEntPhysicalIndex_Type()
)
hwSysCurEntPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysCurEntPhysicalIndex.setStatus("current")


class _HwSysCurCFGFileIndex_Type(Integer32):
    """Custom type hwSysCurCFGFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysCurCFGFileIndex_Type.__name__ = "Integer32"
_HwSysCurCFGFileIndex_Object = MibTableColumn
hwSysCurCFGFileIndex = _HwSysCurCFGFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 2, 1, 1, 2),
    _HwSysCurCFGFileIndex_Type()
)
hwSysCurCFGFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysCurCFGFileIndex.setStatus("current")


class _HwSysCurImageIndex_Type(Integer32):
    """Custom type hwSysCurImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysCurImageIndex_Type.__name__ = "Integer32"
_HwSysCurImageIndex_Object = MibTableColumn
hwSysCurImageIndex = _HwSysCurImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 2, 1, 1, 3),
    _HwSysCurImageIndex_Type()
)
hwSysCurImageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysCurImageIndex.setStatus("current")


class _HwSysCurPafFileIndex_Type(Integer32):
    """Custom type hwSysCurPafFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysCurPafFileIndex_Type.__name__ = "Integer32"
_HwSysCurPafFileIndex_Object = MibTableColumn
hwSysCurPafFileIndex = _HwSysCurPafFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 2, 1, 1, 4),
    _HwSysCurPafFileIndex_Type()
)
hwSysCurPafFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysCurPafFileIndex.setStatus("current")


class _HwSysCurLicenseIndex_Type(Integer32):
    """Custom type hwSysCurLicenseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysCurLicenseIndex_Type.__name__ = "Integer32"
_HwSysCurLicenseIndex_Object = MibTableColumn
hwSysCurLicenseIndex = _HwSysCurLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 2, 1, 1, 5),
    _HwSysCurLicenseIndex_Type()
)
hwSysCurLicenseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysCurLicenseIndex.setStatus("current")


class _HwSysCurPatchFileIndex_Type(Integer32):
    """Custom type hwSysCurPatchFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysCurPatchFileIndex_Type.__name__ = "Integer32"
_HwSysCurPatchFileIndex_Object = MibTableColumn
hwSysCurPatchFileIndex = _HwSysCurPatchFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 2, 1, 1, 6),
    _HwSysCurPatchFileIndex_Type()
)
hwSysCurPatchFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysCurPatchFileIndex.setStatus("current")


class _HwSysCurVoiceFileIndex_Type(Integer32):
    """Custom type hwSysCurVoiceFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysCurVoiceFileIndex_Type.__name__ = "Integer32"
_HwSysCurVoiceFileIndex_Object = MibTableColumn
hwSysCurVoiceFileIndex = _HwSysCurVoiceFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 2, 1, 1, 7),
    _HwSysCurVoiceFileIndex_Type()
)
hwSysCurVoiceFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysCurVoiceFileIndex.setStatus("current")
_HwSysReload_ObjectIdentity = ObjectIdentity
hwSysReload = _HwSysReload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3)
)


class _HwSysReloadSchedule_Type(Integer32):
    """Custom type hwSysReloadSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysReloadSchedule_Type.__name__ = "Integer32"
_HwSysReloadSchedule_Object = MibScalar
hwSysReloadSchedule = _HwSysReloadSchedule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 1),
    _HwSysReloadSchedule_Type()
)
hwSysReloadSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysReloadSchedule.setStatus("obsolete")


class _HwSysReloadAction_Type(Integer32):
    """Custom type hwSysReloadAction based on Integer32"""
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


_HwSysReloadAction_Type.__name__ = "Integer32"
_HwSysReloadAction_Object = MibScalar
hwSysReloadAction = _HwSysReloadAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 2),
    _HwSysReloadAction_Type()
)
hwSysReloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysReloadAction.setStatus("current")
_HwSysReloadScheduleTable_Object = MibTable
hwSysReloadScheduleTable = _HwSysReloadScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hwSysReloadScheduleTable.setStatus("current")
_HwSysReloadScheduleEntry_Object = MibTableRow
hwSysReloadScheduleEntry = _HwSysReloadScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1)
)
hwSysReloadScheduleEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysReloadScheduleIndex"),
)
if mibBuilder.loadTexts:
    hwSysReloadScheduleEntry.setStatus("current")


class _HwSysReloadScheduleIndex_Type(Integer32):
    """Custom type hwSysReloadScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysReloadScheduleIndex_Type.__name__ = "Integer32"
_HwSysReloadScheduleIndex_Object = MibTableColumn
hwSysReloadScheduleIndex = _HwSysReloadScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 1),
    _HwSysReloadScheduleIndex_Type()
)
hwSysReloadScheduleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysReloadScheduleIndex.setStatus("current")
_HwSysReloadEntity_Type = PhysicalIndex
_HwSysReloadEntity_Object = MibTableColumn
hwSysReloadEntity = _HwSysReloadEntity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 2),
    _HwSysReloadEntity_Type()
)
hwSysReloadEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadEntity.setStatus("current")


class _HwSysReloadCfgFile_Type(Integer32):
    """Custom type hwSysReloadCfgFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysReloadCfgFile_Type.__name__ = "Integer32"
_HwSysReloadCfgFile_Object = MibTableColumn
hwSysReloadCfgFile = _HwSysReloadCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 3),
    _HwSysReloadCfgFile_Type()
)
hwSysReloadCfgFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadCfgFile.setStatus("current")


class _HwSysReloadImage_Type(Integer32):
    """Custom type hwSysReloadImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysReloadImage_Type.__name__ = "Integer32"
_HwSysReloadImage_Object = MibTableColumn
hwSysReloadImage = _HwSysReloadImage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 4),
    _HwSysReloadImage_Type()
)
hwSysReloadImage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadImage.setStatus("current")


class _HwSysReloadReason_Type(DisplayString):
    """Custom type hwSysReloadReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSysReloadReason_Type.__name__ = "DisplayString"
_HwSysReloadReason_Object = MibTableColumn
hwSysReloadReason = _HwSysReloadReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 5),
    _HwSysReloadReason_Type()
)
hwSysReloadReason.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadReason.setStatus("current")


class _HwSysReloadScheduleTime_Type(DateAndTime):
    """Custom type hwSysReloadScheduleTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwSysReloadScheduleTime_Type.__name__ = "DateAndTime"
_HwSysReloadScheduleTime_Object = MibTableColumn
hwSysReloadScheduleTime = _HwSysReloadScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 6),
    _HwSysReloadScheduleTime_Type()
)
hwSysReloadScheduleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadScheduleTime.setStatus("current")
_HwSysReloadRowStatus_Type = RowStatus
_HwSysReloadRowStatus_Object = MibTableColumn
hwSysReloadRowStatus = _HwSysReloadRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 7),
    _HwSysReloadRowStatus_Type()
)
hwSysReloadRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadRowStatus.setStatus("current")
_HwSysReloadPafFile_Type = Integer32
_HwSysReloadPafFile_Object = MibTableColumn
hwSysReloadPafFile = _HwSysReloadPafFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 8),
    _HwSysReloadPafFile_Type()
)
hwSysReloadPafFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadPafFile.setStatus("current")
_HwSysReloadLicenseFile_Type = Integer32
_HwSysReloadLicenseFile_Object = MibTableColumn
hwSysReloadLicenseFile = _HwSysReloadLicenseFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 9),
    _HwSysReloadLicenseFile_Type()
)
hwSysReloadLicenseFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadLicenseFile.setStatus("current")
_HwSysReloadPatchFile_Type = Integer32
_HwSysReloadPatchFile_Object = MibTableColumn
hwSysReloadPatchFile = _HwSysReloadPatchFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 10),
    _HwSysReloadPatchFile_Type()
)
hwSysReloadPatchFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadPatchFile.setStatus("current")


class _HwSysReloadPatchState_Type(Integer32):
    """Custom type hwSysReloadPatchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("run", 1),
          ("unused", 255))
    )


_HwSysReloadPatchState_Type.__name__ = "Integer32"
_HwSysReloadPatchState_Object = MibTableColumn
hwSysReloadPatchState = _HwSysReloadPatchState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 11),
    _HwSysReloadPatchState_Type()
)
hwSysReloadPatchState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadPatchState.setStatus("current")


class _HwSysReloadOperateDestType_Type(Integer32):
    """Custom type hwSysReloadOperateDestType based on Integer32"""
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
        *(("all", 1),
          ("chassis", 3),
          ("slave", 2),
          ("unused", 4))
    )


_HwSysReloadOperateDestType_Type.__name__ = "Integer32"
_HwSysReloadOperateDestType_Object = MibTableColumn
hwSysReloadOperateDestType = _HwSysReloadOperateDestType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 12),
    _HwSysReloadOperateDestType_Type()
)
hwSysReloadOperateDestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadOperateDestType.setStatus("current")
_HwSysReloadOperateDestIndex_Type = DisplayString
_HwSysReloadOperateDestIndex_Object = MibTableColumn
hwSysReloadOperateDestIndex = _HwSysReloadOperateDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 13),
    _HwSysReloadOperateDestIndex_Type()
)
hwSysReloadOperateDestIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadOperateDestIndex.setStatus("current")
_HwSysReloadVoiceFile_Type = Integer32
_HwSysReloadVoiceFile_Object = MibTableColumn
hwSysReloadVoiceFile = _HwSysReloadVoiceFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 14),
    _HwSysReloadVoiceFile_Type()
)
hwSysReloadVoiceFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadVoiceFile.setStatus("current")


class _HwSysReloadAndroidFile_Type(Integer32):
    """Custom type hwSysReloadAndroidFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysReloadAndroidFile_Type.__name__ = "Integer32"
_HwSysReloadAndroidFile_Object = MibTableColumn
hwSysReloadAndroidFile = _HwSysReloadAndroidFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 3, 1, 15),
    _HwSysReloadAndroidFile_Type()
)
hwSysReloadAndroidFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSysReloadAndroidFile.setStatus("current")


class _HwSysReboot_Type(Integer32):
    """Custom type hwSysReboot based on Integer32"""
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
        *(("rebootSlave", 3),
          ("rebootWholeRoute", 2),
          ("slaveSwitch", 4),
          ("unused", 1))
    )


_HwSysReboot_Type.__name__ = "Integer32"
_HwSysReboot_Object = MibScalar
hwSysReboot = _HwSysReboot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 4),
    _HwSysReboot_Type()
)
hwSysReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysReboot.setStatus("current")
_HwSysSlaveSwitchEnable_Type = EnabledStatus
_HwSysSlaveSwitchEnable_Object = MibScalar
hwSysSlaveSwitchEnable = _HwSysSlaveSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 5),
    _HwSysSlaveSwitchEnable_Type()
)
hwSysSlaveSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysSlaveSwitchEnable.setStatus("current")
_HwSysLatestRebootErrorInfo_Type = DisplayString
_HwSysLatestRebootErrorInfo_Object = MibScalar
hwSysLatestRebootErrorInfo = _HwSysLatestRebootErrorInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 6),
    _HwSysLatestRebootErrorInfo_Type()
)
hwSysLatestRebootErrorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysLatestRebootErrorInfo.setStatus("current")
_HwSysSlaveSwitchTable_Object = MibTable
hwSysSlaveSwitchTable = _HwSysSlaveSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 7)
)
if mibBuilder.loadTexts:
    hwSysSlaveSwitchTable.setStatus("current")
_HwSysSlaveSwitchEntry_Object = MibTableRow
hwSysSlaveSwitchEntry = _HwSysSlaveSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 7, 1)
)
hwSysSlaveSwitchEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysSlaveSwitchIndex"),
)
if mibBuilder.loadTexts:
    hwSysSlaveSwitchEntry.setStatus("current")


class _HwSysSlaveSwitchIndex_Type(Integer32):
    """Custom type hwSysSlaveSwitchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_HwSysSlaveSwitchIndex_Type.__name__ = "Integer32"
_HwSysSlaveSwitchIndex_Object = MibTableColumn
hwSysSlaveSwitchIndex = _HwSysSlaveSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 7, 1, 1),
    _HwSysSlaveSwitchIndex_Type()
)
hwSysSlaveSwitchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysSlaveSwitchIndex.setStatus("current")
_HwSysSlaveSwitchChassisNum_Type = DisplayString
_HwSysSlaveSwitchChassisNum_Object = MibTableColumn
hwSysSlaveSwitchChassisNum = _HwSysSlaveSwitchChassisNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 7, 1, 2),
    _HwSysSlaveSwitchChassisNum_Type()
)
hwSysSlaveSwitchChassisNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysSlaveSwitchChassisNum.setStatus("current")


class _HwSysSlaveSwitchOperType_Type(Integer32):
    """Custom type hwSysSlaveSwitchOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("slaveSwitch", 2),
          ("slaveSwitchLock", 3),
          ("unused", 1))
    )


_HwSysSlaveSwitchOperType_Type.__name__ = "Integer32"
_HwSysSlaveSwitchOperType_Object = MibTableColumn
hwSysSlaveSwitchOperType = _HwSysSlaveSwitchOperType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 7, 1, 3),
    _HwSysSlaveSwitchOperType_Type()
)
hwSysSlaveSwitchOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysSlaveSwitchOperType.setStatus("current")
_HwSysSlaveSwitchEnableStatus_Type = EnabledStatus
_HwSysSlaveSwitchEnableStatus_Object = MibTableColumn
hwSysSlaveSwitchEnableStatus = _HwSysSlaveSwitchEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 7, 1, 4),
    _HwSysSlaveSwitchEnableStatus_Type()
)
hwSysSlaveSwitchEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysSlaveSwitchEnableStatus.setStatus("current")
_HwSysSlaveSwitchSrc_Type = DisplayString
_HwSysSlaveSwitchSrc_Object = MibTableColumn
hwSysSlaveSwitchSrc = _HwSysSlaveSwitchSrc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 7, 1, 5),
    _HwSysSlaveSwitchSrc_Type()
)
hwSysSlaveSwitchSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysSlaveSwitchSrc.setStatus("current")
_HwSysSlaveSwitchDst_Type = DisplayString
_HwSysSlaveSwitchDst_Object = MibTableColumn
hwSysSlaveSwitchDst = _HwSysSlaveSwitchDst_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 7, 1, 6),
    _HwSysSlaveSwitchDst_Type()
)
hwSysSlaveSwitchDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysSlaveSwitchDst.setStatus("current")


class _HwSysDelayReboot_Type(Integer32):
    """Custom type hwSysDelayReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysDelayReboot_Type.__name__ = "Integer32"
_HwSysDelayReboot_Object = MibScalar
hwSysDelayReboot = _HwSysDelayReboot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 3, 8),
    _HwSysDelayReboot_Type()
)
hwSysDelayReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysDelayReboot.setStatus("current")
_HwSysImage_ObjectIdentity = ObjectIdentity
hwSysImage = _HwSysImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 4)
)


class _HwSysImageNum_Type(Integer32):
    """Custom type hwSysImageNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysImageNum_Type.__name__ = "Integer32"
_HwSysImageNum_Object = MibScalar
hwSysImageNum = _HwSysImageNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 4, 1),
    _HwSysImageNum_Type()
)
hwSysImageNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysImageNum.setStatus("current")
_HwSysImageTable_Object = MibTable
hwSysImageTable = _HwSysImageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hwSysImageTable.setStatus("current")
_HwSysImageEntry_Object = MibTableRow
hwSysImageEntry = _HwSysImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 4, 2, 1)
)
hwSysImageEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysImageIndex"),
)
if mibBuilder.loadTexts:
    hwSysImageEntry.setStatus("current")


class _HwSysImageIndex_Type(Integer32):
    """Custom type hwSysImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSysImageIndex_Type.__name__ = "Integer32"
_HwSysImageIndex_Object = MibTableColumn
hwSysImageIndex = _HwSysImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 4, 2, 1, 1),
    _HwSysImageIndex_Type()
)
hwSysImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysImageIndex.setStatus("current")
_HwSysImageName_Type = DisplayString
_HwSysImageName_Object = MibTableColumn
hwSysImageName = _HwSysImageName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 4, 2, 1, 2),
    _HwSysImageName_Type()
)
hwSysImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysImageName.setStatus("current")


class _HwSysImageSize_Type(Integer32):
    """Custom type hwSysImageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysImageSize_Type.__name__ = "Integer32"
_HwSysImageSize_Object = MibTableColumn
hwSysImageSize = _HwSysImageSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 4, 2, 1, 3),
    _HwSysImageSize_Type()
)
hwSysImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysImageSize.setStatus("current")
_HwSysImageLocation_Type = DisplayString
_HwSysImageLocation_Object = MibTableColumn
hwSysImageLocation = _HwSysImageLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 4, 2, 1, 4),
    _HwSysImageLocation_Type()
)
hwSysImageLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysImageLocation.setStatus("current")
_HwSysImageVersion_Type = DisplayString
_HwSysImageVersion_Object = MibTableColumn
hwSysImageVersion = _HwSysImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 4, 2, 1, 5),
    _HwSysImageVersion_Type()
)
hwSysImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysImageVersion.setStatus("current")


class _HwSysImageReason_Type(DisplayString):
    """Custom type hwSysImageReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSysImageReason_Type.__name__ = "DisplayString"
_HwSysImageReason_Object = MibTableColumn
hwSysImageReason = _HwSysImageReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 4, 2, 1, 6),
    _HwSysImageReason_Type()
)
hwSysImageReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysImageReason.setStatus("current")
_HwSysCFGFile_ObjectIdentity = ObjectIdentity
hwSysCFGFile = _HwSysCFGFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 5)
)


class _HwSysCFGFileNum_Type(Integer32):
    """Custom type hwSysCFGFileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysCFGFileNum_Type.__name__ = "Integer32"
_HwSysCFGFileNum_Object = MibScalar
hwSysCFGFileNum = _HwSysCFGFileNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 5, 1),
    _HwSysCFGFileNum_Type()
)
hwSysCFGFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysCFGFileNum.setStatus("current")
_HwSysCFGFileTable_Object = MibTable
hwSysCFGFileTable = _HwSysCFGFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hwSysCFGFileTable.setStatus("current")
_HwSysCFGFileEntry_Object = MibTableRow
hwSysCFGFileEntry = _HwSysCFGFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 5, 2, 1)
)
hwSysCFGFileEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysCFGFileIndex"),
)
if mibBuilder.loadTexts:
    hwSysCFGFileEntry.setStatus("current")


class _HwSysCFGFileIndex_Type(Integer32):
    """Custom type hwSysCFGFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSysCFGFileIndex_Type.__name__ = "Integer32"
_HwSysCFGFileIndex_Object = MibTableColumn
hwSysCFGFileIndex = _HwSysCFGFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 5, 2, 1, 1),
    _HwSysCFGFileIndex_Type()
)
hwSysCFGFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysCFGFileIndex.setStatus("current")
_HwSysCFGFileName_Type = DisplayString
_HwSysCFGFileName_Object = MibTableColumn
hwSysCFGFileName = _HwSysCFGFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 5, 2, 1, 2),
    _HwSysCFGFileName_Type()
)
hwSysCFGFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysCFGFileName.setStatus("current")


class _HwSysCFGFileSize_Type(Integer32):
    """Custom type hwSysCFGFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysCFGFileSize_Type.__name__ = "Integer32"
_HwSysCFGFileSize_Object = MibTableColumn
hwSysCFGFileSize = _HwSysCFGFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 5, 2, 1, 3),
    _HwSysCFGFileSize_Type()
)
hwSysCFGFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysCFGFileSize.setStatus("current")
_HwSysCFGFileLocation_Type = DisplayString
_HwSysCFGFileLocation_Object = MibTableColumn
hwSysCFGFileLocation = _HwSysCFGFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 5, 2, 1, 4),
    _HwSysCFGFileLocation_Type()
)
hwSysCFGFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysCFGFileLocation.setStatus("current")


class _HwSysCFGFileReason_Type(DisplayString):
    """Custom type hwSysCFGFileReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSysCFGFileReason_Type.__name__ = "DisplayString"
_HwSysCFGFileReason_Object = MibTableColumn
hwSysCFGFileReason = _HwSysCFGFileReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 5, 2, 1, 5),
    _HwSysCFGFileReason_Type()
)
hwSysCFGFileReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysCFGFileReason.setStatus("current")
_HwSysPafFile_ObjectIdentity = ObjectIdentity
hwSysPafFile = _HwSysPafFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 6)
)


class _HwSysPafFileNum_Type(Integer32):
    """Custom type hwSysPafFileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysPafFileNum_Type.__name__ = "Integer32"
_HwSysPafFileNum_Object = MibScalar
hwSysPafFileNum = _HwSysPafFileNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 6, 1),
    _HwSysPafFileNum_Type()
)
hwSysPafFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysPafFileNum.setStatus("current")
_HwSysPafFileTable_Object = MibTable
hwSysPafFileTable = _HwSysPafFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hwSysPafFileTable.setStatus("current")
_HwSysPafFileEntry_Object = MibTableRow
hwSysPafFileEntry = _HwSysPafFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 6, 2, 1)
)
hwSysPafFileEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysPafFileIndex"),
)
if mibBuilder.loadTexts:
    hwSysPafFileEntry.setStatus("current")


class _HwSysPafFileIndex_Type(Integer32):
    """Custom type hwSysPafFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSysPafFileIndex_Type.__name__ = "Integer32"
_HwSysPafFileIndex_Object = MibTableColumn
hwSysPafFileIndex = _HwSysPafFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 6, 2, 1, 1),
    _HwSysPafFileIndex_Type()
)
hwSysPafFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysPafFileIndex.setStatus("current")
_HwSysPafFileName_Type = DisplayString
_HwSysPafFileName_Object = MibTableColumn
hwSysPafFileName = _HwSysPafFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 6, 2, 1, 2),
    _HwSysPafFileName_Type()
)
hwSysPafFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysPafFileName.setStatus("current")
_HwSysPafFileSize_Type = Integer32
_HwSysPafFileSize_Object = MibTableColumn
hwSysPafFileSize = _HwSysPafFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 6, 2, 1, 3),
    _HwSysPafFileSize_Type()
)
hwSysPafFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysPafFileSize.setStatus("current")
_HwSysPafFileLocation_Type = DisplayString
_HwSysPafFileLocation_Object = MibTableColumn
hwSysPafFileLocation = _HwSysPafFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 6, 2, 1, 4),
    _HwSysPafFileLocation_Type()
)
hwSysPafFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysPafFileLocation.setStatus("current")
_HwSysPafFileVersion_Type = DisplayString
_HwSysPafFileVersion_Object = MibTableColumn
hwSysPafFileVersion = _HwSysPafFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 6, 2, 1, 5),
    _HwSysPafFileVersion_Type()
)
hwSysPafFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysPafFileVersion.setStatus("current")
_HwSysLicenseFile_ObjectIdentity = ObjectIdentity
hwSysLicenseFile = _HwSysLicenseFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 7)
)


class _HwSysLicenseFileNum_Type(Integer32):
    """Custom type hwSysLicenseFileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysLicenseFileNum_Type.__name__ = "Integer32"
_HwSysLicenseFileNum_Object = MibScalar
hwSysLicenseFileNum = _HwSysLicenseFileNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 7, 1),
    _HwSysLicenseFileNum_Type()
)
hwSysLicenseFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysLicenseFileNum.setStatus("current")
_HwSysLicenseFileTable_Object = MibTable
hwSysLicenseFileTable = _HwSysLicenseFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hwSysLicenseFileTable.setStatus("current")
_HwSysLicenseFileEntry_Object = MibTableRow
hwSysLicenseFileEntry = _HwSysLicenseFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 7, 2, 1)
)
hwSysLicenseFileEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysLicenseFileIndex"),
)
if mibBuilder.loadTexts:
    hwSysLicenseFileEntry.setStatus("current")


class _HwSysLicenseFileIndex_Type(Integer32):
    """Custom type hwSysLicenseFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSysLicenseFileIndex_Type.__name__ = "Integer32"
_HwSysLicenseFileIndex_Object = MibTableColumn
hwSysLicenseFileIndex = _HwSysLicenseFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 7, 2, 1, 1),
    _HwSysLicenseFileIndex_Type()
)
hwSysLicenseFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysLicenseFileIndex.setStatus("current")
_HwSysLicenseFileName_Type = DisplayString
_HwSysLicenseFileName_Object = MibTableColumn
hwSysLicenseFileName = _HwSysLicenseFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 7, 2, 1, 2),
    _HwSysLicenseFileName_Type()
)
hwSysLicenseFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysLicenseFileName.setStatus("current")
_HwSysLicenseFileSize_Type = Integer32
_HwSysLicenseFileSize_Object = MibTableColumn
hwSysLicenseFileSize = _HwSysLicenseFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 7, 2, 1, 3),
    _HwSysLicenseFileSize_Type()
)
hwSysLicenseFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysLicenseFileSize.setStatus("current")
_HwSysLicenseFileLocation_Type = DisplayString
_HwSysLicenseFileLocation_Object = MibTableColumn
hwSysLicenseFileLocation = _HwSysLicenseFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 7, 2, 1, 4),
    _HwSysLicenseFileLocation_Type()
)
hwSysLicenseFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysLicenseFileLocation.setStatus("current")
_HwPatch_ObjectIdentity = ObjectIdentity
hwPatch = _HwPatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8)
)
_HwPatchBase_ObjectIdentity = ObjectIdentity
hwPatchBase = _HwPatchBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 1)
)


class _HwPatchFileNum_Type(Integer32):
    """Custom type hwPatchFileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwPatchFileNum_Type.__name__ = "Integer32"
_HwPatchFileNum_Object = MibScalar
hwPatchFileNum = _HwPatchFileNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 1, 1),
    _HwPatchFileNum_Type()
)
hwPatchFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchFileNum.setStatus("current")


class _HwPatchRecordReset_Type(Integer32):
    """Custom type hwPatchRecordReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("resetPatchError", 3),
          ("resetPatchHistory", 2),
          ("unused", 1))
    )


_HwPatchRecordReset_Type.__name__ = "Integer32"
_HwPatchRecordReset_Object = MibScalar
hwPatchRecordReset = _HwPatchRecordReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 1, 2),
    _HwPatchRecordReset_Type()
)
hwPatchRecordReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPatchRecordReset.setStatus("current")


class _HwPatchHistoryTableMax_Type(Integer32):
    """Custom type hwPatchHistoryTableMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwPatchHistoryTableMax_Type.__name__ = "Integer32"
_HwPatchHistoryTableMax_Object = MibScalar
hwPatchHistoryTableMax = _HwPatchHistoryTableMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 1, 3),
    _HwPatchHistoryTableMax_Type()
)
hwPatchHistoryTableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPatchHistoryTableMax.setStatus("current")
_HwPatchTrapEnble_Type = EnabledStatus
_HwPatchTrapEnble_Object = MibScalar
hwPatchTrapEnble = _HwPatchTrapEnble_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 1, 4),
    _HwPatchTrapEnble_Type()
)
hwPatchTrapEnble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPatchTrapEnble.setStatus("current")


class _HwPatchErrorTableMax_Type(Integer32):
    """Custom type hwPatchErrorTableMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwPatchErrorTableMax_Type.__name__ = "Integer32"
_HwPatchErrorTableMax_Object = MibScalar
hwPatchErrorTableMax = _HwPatchErrorTableMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 1, 5),
    _HwPatchErrorTableMax_Type()
)
hwPatchErrorTableMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPatchErrorTableMax.setStatus("current")
_HwPatchId_Type = DisplayString
_HwPatchId_Object = MibScalar
hwPatchId = _HwPatchId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 1, 6),
    _HwPatchId_Type()
)
hwPatchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchId.setStatus("current")
_HwPatchLatestId_Type = DisplayString
_HwPatchLatestId_Object = MibScalar
hwPatchLatestId = _HwPatchLatestId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 1, 7),
    _HwPatchLatestId_Type()
)
hwPatchLatestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchLatestId.setStatus("current")


class _HwPatchFailReason_Type(Integer32):
    """Custom type hwPatchFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("getPatchErr", 2),
          ("patchConfigInconsistError", 9),
          ("patchConflict", 4),
          ("patchOpenErr", 1),
          ("patchSpaceShortage", 3),
          ("synchronizePatchPackageError", 8),
          ("versionErr", 5))
    )


_HwPatchFailReason_Type.__name__ = "Integer32"
_HwPatchFailReason_Object = MibScalar
hwPatchFailReason = _HwPatchFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 1, 8),
    _HwPatchFailReason_Type()
)
hwPatchFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchFailReason.setStatus("current")
_HwPatchFileTable_Object = MibTable
hwPatchFileTable = _HwPatchFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 2)
)
if mibBuilder.loadTexts:
    hwPatchFileTable.setStatus("current")
_HwPatchFileEntry_Object = MibTableRow
hwPatchFileEntry = _HwPatchFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 2, 1)
)
hwPatchFileEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwPatchFileIndex"),
)
if mibBuilder.loadTexts:
    hwPatchFileEntry.setStatus("current")


class _HwPatchFileIndex_Type(Unsigned32):
    """Custom type hwPatchFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwPatchFileIndex_Type.__name__ = "Unsigned32"
_HwPatchFileIndex_Object = MibTableColumn
hwPatchFileIndex = _HwPatchFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 2, 1, 1),
    _HwPatchFileIndex_Type()
)
hwPatchFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPatchFileIndex.setStatus("current")
_HwPatchFileName_Type = DisplayString
_HwPatchFileName_Object = MibTableColumn
hwPatchFileName = _HwPatchFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 2, 1, 2),
    _HwPatchFileName_Type()
)
hwPatchFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchFileName.setStatus("current")
_HwPatchFileSize_Type = Integer32
_HwPatchFileSize_Object = MibTableColumn
hwPatchFileSize = _HwPatchFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 2, 1, 3),
    _HwPatchFileSize_Type()
)
hwPatchFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchFileSize.setStatus("current")
_HwPatchFileLocation_Type = DisplayString
_HwPatchFileLocation_Object = MibTableColumn
hwPatchFileLocation = _HwPatchFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 2, 1, 4),
    _HwPatchFileLocation_Type()
)
hwPatchFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchFileLocation.setStatus("current")
_HwPatchFileVersion_Type = DisplayString
_HwPatchFileVersion_Object = MibTableColumn
hwPatchFileVersion = _HwPatchFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 2, 1, 5),
    _HwPatchFileVersion_Type()
)
hwPatchFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchFileVersion.setStatus("current")
_HwLoadPatchTable_Object = MibTable
hwLoadPatchTable = _HwLoadPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 4)
)
if mibBuilder.loadTexts:
    hwLoadPatchTable.setStatus("current")
_HwLoadPatchEntry_Object = MibTableRow
hwLoadPatchEntry = _HwLoadPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 4, 1)
)
hwLoadPatchEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwPatchSlotIndex"),
    (0, "HUAWEI-SYS-MAN-MIB", "hwPatchFileIndex"),
)
if mibBuilder.loadTexts:
    hwLoadPatchEntry.setStatus("current")


class _HwPatchLoadDestType_Type(Integer32):
    """Custom type hwPatchLoadDestType based on Integer32"""
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
        *(("all", 1),
          ("chassis", 4),
          ("slave", 2),
          ("slot", 3),
          ("unused", 5))
    )


_HwPatchLoadDestType_Type.__name__ = "Integer32"
_HwPatchLoadDestType_Object = MibTableColumn
hwPatchLoadDestType = _HwPatchLoadDestType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 4, 1, 1),
    _HwPatchLoadDestType_Type()
)
hwPatchLoadDestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPatchLoadDestType.setStatus("current")
_HwPatchLoadDestIndex_Type = DisplayString
_HwPatchLoadDestIndex_Object = MibTableColumn
hwPatchLoadDestIndex = _HwPatchLoadDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 4, 1, 2),
    _HwPatchLoadDestIndex_Type()
)
hwPatchLoadDestIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPatchLoadDestIndex.setStatus("current")


class _HwPatchLoadState_Type(Integer32):
    """Custom type hwPatchLoadState based on Integer32"""
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
        *(("failure", 3),
          ("loading", 1),
          ("none", 4),
          ("success", 2))
    )


_HwPatchLoadState_Type.__name__ = "Integer32"
_HwPatchLoadState_Object = MibTableColumn
hwPatchLoadState = _HwPatchLoadState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 4, 1, 3),
    _HwPatchLoadState_Type()
)
hwPatchLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchLoadState.setStatus("current")
_HwLoadPatchRowState_Type = RowStatus
_HwLoadPatchRowState_Object = MibTableColumn
hwLoadPatchRowState = _HwLoadPatchRowState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 4, 1, 51),
    _HwLoadPatchRowState_Type()
)
hwLoadPatchRowState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLoadPatchRowState.setStatus("current")
_HwPatchInfo_ObjectIdentity = ObjectIdentity
hwPatchInfo = _HwPatchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5)
)
_HwPatchTable_Object = MibTable
hwPatchTable = _HwPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1)
)
if mibBuilder.loadTexts:
    hwPatchTable.setStatus("current")
_HwPatchEntry_Object = MibTableRow
hwPatchEntry = _HwPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1)
)
hwPatchEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwPatchSlotIndex"),
    (0, "HUAWEI-SYS-MAN-MIB", "hwPatchIndex"),
)
if mibBuilder.loadTexts:
    hwPatchEntry.setStatus("current")


class _HwPatchSlotIndex_Type(Integer32):
    """Custom type hwPatchSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwPatchSlotIndex_Type.__name__ = "Integer32"
_HwPatchSlotIndex_Object = MibTableColumn
hwPatchSlotIndex = _HwPatchSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 1),
    _HwPatchSlotIndex_Type()
)
hwPatchSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPatchSlotIndex.setStatus("current")


class _HwPatchIndex_Type(Unsigned32):
    """Custom type hwPatchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPatchIndex_Type.__name__ = "Unsigned32"
_HwPatchIndex_Object = MibTableColumn
hwPatchIndex = _HwPatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 2),
    _HwPatchIndex_Type()
)
hwPatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPatchIndex.setStatus("current")
_HwPatchUsedFileName_Type = DisplayString
_HwPatchUsedFileName_Object = MibTableColumn
hwPatchUsedFileName = _HwPatchUsedFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 3),
    _HwPatchUsedFileName_Type()
)
hwPatchUsedFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchUsedFileName.setStatus("current")
_HwPatchVersion_Type = DisplayString
_HwPatchVersion_Object = MibTableColumn
hwPatchVersion = _HwPatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 4),
    _HwPatchVersion_Type()
)
hwPatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchVersion.setStatus("current")
_HwPatchDescription_Type = DisplayString
_HwPatchDescription_Object = MibTableColumn
hwPatchDescription = _HwPatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 5),
    _HwPatchDescription_Type()
)
hwPatchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchDescription.setStatus("current")
_HwPatchProgramVersion_Type = DisplayString
_HwPatchProgramVersion_Object = MibTableColumn
hwPatchProgramVersion = _HwPatchProgramVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 6),
    _HwPatchProgramVersion_Type()
)
hwPatchProgramVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchProgramVersion.setStatus("current")
_HwPatchFuncNum_Type = Integer32
_HwPatchFuncNum_Object = MibTableColumn
hwPatchFuncNum = _HwPatchFuncNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 7),
    _HwPatchFuncNum_Type()
)
hwPatchFuncNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchFuncNum.setStatus("current")
_HwPatchTextLen_Type = Integer32
_HwPatchTextLen_Object = MibTableColumn
hwPatchTextLen = _HwPatchTextLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 8),
    _HwPatchTextLen_Type()
)
hwPatchTextLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchTextLen.setStatus("current")
_HwPatchDataLen_Type = Integer32
_HwPatchDataLen_Object = MibTableColumn
hwPatchDataLen = _HwPatchDataLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 9),
    _HwPatchDataLen_Type()
)
hwPatchDataLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchDataLen.setStatus("current")


class _HwPatchType_Type(Integer32):
    """Custom type hwPatchType based on Integer32"""
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
        *(("coolCommon", 3),
          ("coolTemporary", 4),
          ("hotCommon", 1),
          ("hotTemporary", 2))
    )


_HwPatchType_Type.__name__ = "Integer32"
_HwPatchType_Object = MibTableColumn
hwPatchType = _HwPatchType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 10),
    _HwPatchType_Type()
)
hwPatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchType.setStatus("current")
_HwPatchBuildTime_Type = DateAndTime
_HwPatchBuildTime_Object = MibTableColumn
hwPatchBuildTime = _HwPatchBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 11),
    _HwPatchBuildTime_Type()
)
hwPatchBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchBuildTime.setStatus("current")
_HwPatchActiveTime_Type = DateAndTime
_HwPatchActiveTime_Object = MibTableColumn
hwPatchActiveTime = _HwPatchActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 12),
    _HwPatchActiveTime_Type()
)
hwPatchActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchActiveTime.setStatus("current")


class _HwPatchAdminStatus_Type(Integer32):
    """Custom type hwPatchAdminStatus based on Integer32"""
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
        *(("active", 2),
          ("deactive", 3),
          ("delete", 4),
          ("run", 1))
    )


_HwPatchAdminStatus_Type.__name__ = "Integer32"
_HwPatchAdminStatus_Object = MibTableColumn
hwPatchAdminStatus = _HwPatchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 13),
    _HwPatchAdminStatus_Type()
)
hwPatchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPatchAdminStatus.setStatus("current")


class _HwPatchOperateState_Type(Integer32):
    """Custom type hwPatchOperateState based on Integer32"""
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
        *(("patchActive", 2),
          ("patchDeactive", 3),
          ("patchDeleting", 4),
          ("patchRunning", 1))
    )


_HwPatchOperateState_Type.__name__ = "Integer32"
_HwPatchOperateState_Object = MibTableColumn
hwPatchOperateState = _HwPatchOperateState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 14),
    _HwPatchOperateState_Type()
)
hwPatchOperateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchOperateState.setStatus("current")


class _HwPatchOperateDestType_Type(Integer32):
    """Custom type hwPatchOperateDestType based on Integer32"""
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
        *(("all", 1),
          ("chassis", 4),
          ("slave", 2),
          ("slot", 3),
          ("unused", 5))
    )


_HwPatchOperateDestType_Type.__name__ = "Integer32"
_HwPatchOperateDestType_Object = MibTableColumn
hwPatchOperateDestType = _HwPatchOperateDestType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 15),
    _HwPatchOperateDestType_Type()
)
hwPatchOperateDestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPatchOperateDestType.setStatus("current")
_HwPatchOperateDestIndex_Type = DisplayString
_HwPatchOperateDestIndex_Object = MibTableColumn
hwPatchOperateDestIndex = _HwPatchOperateDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 1, 1, 16),
    _HwPatchOperateDestIndex_Type()
)
hwPatchOperateDestIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPatchOperateDestIndex.setStatus("current")
_HwPatchStateTable_Object = MibTable
hwPatchStateTable = _HwPatchStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2)
)
if mibBuilder.loadTexts:
    hwPatchStateTable.setStatus("current")
_HwPatchStateEntry_Object = MibTableRow
hwPatchStateEntry = _HwPatchStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1)
)
hwPatchStateEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwPatchSlotIndex"),
)
if mibBuilder.loadTexts:
    hwPatchStateEntry.setStatus("current")
_HwPatchNumMax_Type = Unsigned32
_HwPatchNumMax_Object = MibTableColumn
hwPatchNumMax = _HwPatchNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1, 1),
    _HwPatchNumMax_Type()
)
hwPatchNumMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchNumMax.setStatus("current")
_HwPatchIdleNum_Type = Integer32
_HwPatchIdleNum_Object = MibTableColumn
hwPatchIdleNum = _HwPatchIdleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1, 2),
    _HwPatchIdleNum_Type()
)
hwPatchIdleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchIdleNum.setStatus("current")
_HwPatchTextMax_Type = Integer32
_HwPatchTextMax_Object = MibTableColumn
hwPatchTextMax = _HwPatchTextMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1, 3),
    _HwPatchTextMax_Type()
)
hwPatchTextMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchTextMax.setStatus("current")
_HwPatchDataMax_Type = Integer32
_HwPatchDataMax_Object = MibTableColumn
hwPatchDataMax = _HwPatchDataMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1, 4),
    _HwPatchDataMax_Type()
)
hwPatchDataMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchDataMax.setStatus("current")
_HwPatchStateTextUsed_Type = Integer32
_HwPatchStateTextUsed_Object = MibTableColumn
hwPatchStateTextUsed = _HwPatchStateTextUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1, 5),
    _HwPatchStateTextUsed_Type()
)
hwPatchStateTextUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStateTextUsed.setStatus("current")
_HwPatchStateDataUsed_Type = Integer32
_HwPatchStateDataUsed_Object = MibTableColumn
hwPatchStateDataUsed = _HwPatchStateDataUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1, 6),
    _HwPatchStateDataUsed_Type()
)
hwPatchStateDataUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStateDataUsed.setStatus("current")
_HwPatchStateTotalPatchNum_Type = Integer32
_HwPatchStateTotalPatchNum_Object = MibTableColumn
hwPatchStateTotalPatchNum = _HwPatchStateTotalPatchNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1, 7),
    _HwPatchStateTotalPatchNum_Type()
)
hwPatchStateTotalPatchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStateTotalPatchNum.setStatus("current")
_HwPatchStateTempPatchNum_Type = Integer32
_HwPatchStateTempPatchNum_Object = MibTableColumn
hwPatchStateTempPatchNum = _HwPatchStateTempPatchNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1, 8),
    _HwPatchStateTempPatchNum_Type()
)
hwPatchStateTempPatchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStateTempPatchNum.setStatus("current")
_HwPatchStateCommonPatchNum_Type = Integer32
_HwPatchStateCommonPatchNum_Object = MibTableColumn
hwPatchStateCommonPatchNum = _HwPatchStateCommonPatchNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1, 9),
    _HwPatchStateCommonPatchNum_Type()
)
hwPatchStateCommonPatchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStateCommonPatchNum.setStatus("current")
_HwPatchStateRuningPatchNum_Type = Integer32
_HwPatchStateRuningPatchNum_Object = MibTableColumn
hwPatchStateRuningPatchNum = _HwPatchStateRuningPatchNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1, 10),
    _HwPatchStateRuningPatchNum_Type()
)
hwPatchStateRuningPatchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStateRuningPatchNum.setStatus("current")
_HwPatchStateActivePatchNum_Type = Integer32
_HwPatchStateActivePatchNum_Object = MibTableColumn
hwPatchStateActivePatchNum = _HwPatchStateActivePatchNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1, 11),
    _HwPatchStateActivePatchNum_Type()
)
hwPatchStateActivePatchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStateActivePatchNum.setStatus("current")
_HwPatchStateDeactivePatchNum_Type = Integer32
_HwPatchStateDeactivePatchNum_Object = MibTableColumn
hwPatchStateDeactivePatchNum = _HwPatchStateDeactivePatchNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 2, 1, 12),
    _HwPatchStateDeactivePatchNum_Type()
)
hwPatchStateDeactivePatchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStateDeactivePatchNum.setStatus("current")
_HwPatchHistoryTable_Object = MibTable
hwPatchHistoryTable = _HwPatchHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 3)
)
if mibBuilder.loadTexts:
    hwPatchHistoryTable.setStatus("current")
_HwPatchHistoryEntry_Object = MibTableRow
hwPatchHistoryEntry = _HwPatchHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 3, 1)
)
hwPatchHistoryEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwPatchHistoryIndex"),
)
if mibBuilder.loadTexts:
    hwPatchHistoryEntry.setStatus("current")
_HwPatchHistoryIndex_Type = Unsigned32
_HwPatchHistoryIndex_Object = MibTableColumn
hwPatchHistoryIndex = _HwPatchHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 3, 1, 1),
    _HwPatchHistoryIndex_Type()
)
hwPatchHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPatchHistoryIndex.setStatus("current")
_HwPatchHistoryProgrameVersion_Type = DisplayString
_HwPatchHistoryProgrameVersion_Object = MibTableColumn
hwPatchHistoryProgrameVersion = _HwPatchHistoryProgrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 3, 1, 2),
    _HwPatchHistoryProgrameVersion_Type()
)
hwPatchHistoryProgrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchHistoryProgrameVersion.setStatus("current")
_HwPatchHistoryVersion_Type = DisplayString
_HwPatchHistoryVersion_Object = MibTableColumn
hwPatchHistoryVersion = _HwPatchHistoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 3, 1, 3),
    _HwPatchHistoryVersion_Type()
)
hwPatchHistoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchHistoryVersion.setStatus("current")
_HwSlotId_Type = Integer32
_HwSlotId_Object = MibTableColumn
hwSlotId = _HwSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 3, 1, 4),
    _HwSlotId_Type()
)
hwSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotId.setStatus("current")
_HwPatchBeginIndex_Type = Integer32
_HwPatchBeginIndex_Object = MibTableColumn
hwPatchBeginIndex = _HwPatchBeginIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 3, 1, 5),
    _HwPatchBeginIndex_Type()
)
hwPatchBeginIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchBeginIndex.setStatus("current")
_HwPatchEndIndex_Type = Integer32
_HwPatchEndIndex_Object = MibTableColumn
hwPatchEndIndex = _HwPatchEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 3, 1, 6),
    _HwPatchEndIndex_Type()
)
hwPatchEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchEndIndex.setStatus("current")


class _HwPatchHistoryAction_Type(Integer32):
    """Custom type hwPatchHistoryAction based on Integer32"""
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
        *(("active", 2),
          ("deactive", 3),
          ("delete", 4),
          ("running", 1))
    )


_HwPatchHistoryAction_Type.__name__ = "Integer32"
_HwPatchHistoryAction_Object = MibTableColumn
hwPatchHistoryAction = _HwPatchHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 3, 1, 7),
    _HwPatchHistoryAction_Type()
)
hwPatchHistoryAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchHistoryAction.setStatus("current")
_HwPatchHistoryBeginTime_Type = DateAndTime
_HwPatchHistoryBeginTime_Object = MibTableColumn
hwPatchHistoryBeginTime = _HwPatchHistoryBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 3, 1, 8),
    _HwPatchHistoryBeginTime_Type()
)
hwPatchHistoryBeginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchHistoryBeginTime.setStatus("current")
_HwPatchHistoryEndTime_Type = DateAndTime
_HwPatchHistoryEndTime_Object = MibTableColumn
hwPatchHistoryEndTime = _HwPatchHistoryEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 3, 1, 9),
    _HwPatchHistoryEndTime_Type()
)
hwPatchHistoryEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchHistoryEndTime.setStatus("current")
_HwPatchErrorTable_Object = MibTable
hwPatchErrorTable = _HwPatchErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 4)
)
if mibBuilder.loadTexts:
    hwPatchErrorTable.setStatus("current")
_HwPatchErrorEntry_Object = MibTableRow
hwPatchErrorEntry = _HwPatchErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 4, 1)
)
hwPatchErrorEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwPatchErrorIndex"),
)
if mibBuilder.loadTexts:
    hwPatchErrorEntry.setStatus("current")
_HwPatchErrorIndex_Type = Unsigned32
_HwPatchErrorIndex_Object = MibTableColumn
hwPatchErrorIndex = _HwPatchErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 4, 1, 1),
    _HwPatchErrorIndex_Type()
)
hwPatchErrorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPatchErrorIndex.setStatus("current")
_HwPatchErrorSlot_Type = Unsigned32
_HwPatchErrorSlot_Object = MibTableColumn
hwPatchErrorSlot = _HwPatchErrorSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 4, 1, 2),
    _HwPatchErrorSlot_Type()
)
hwPatchErrorSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchErrorSlot.setStatus("current")
_HwPatchErrorPatchFileName_Type = DisplayString
_HwPatchErrorPatchFileName_Object = MibTableColumn
hwPatchErrorPatchFileName = _HwPatchErrorPatchFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 4, 1, 3),
    _HwPatchErrorPatchFileName_Type()
)
hwPatchErrorPatchFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchErrorPatchFileName.setStatus("current")


class _HwPatchErrorPatchIndex_Type(Unsigned32):
    """Custom type hwPatchErrorPatchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPatchErrorPatchIndex_Type.__name__ = "Unsigned32"
_HwPatchErrorPatchIndex_Object = MibTableColumn
hwPatchErrorPatchIndex = _HwPatchErrorPatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 4, 1, 4),
    _HwPatchErrorPatchIndex_Type()
)
hwPatchErrorPatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchErrorPatchIndex.setStatus("current")
_HwPatchErrorCode_Type = HWPatchErrorType
_HwPatchErrorCode_Object = MibTableColumn
hwPatchErrorCode = _HwPatchErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 8, 5, 4, 1, 5),
    _HwPatchErrorCode_Type()
)
hwPatchErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchErrorCode.setStatus("current")
_HwBootRom_ObjectIdentity = ObjectIdentity
hwBootRom = _HwBootRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11)
)
_HwBootRomTable_Object = MibTable
hwBootRomTable = _HwBootRomTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1)
)
if mibBuilder.loadTexts:
    hwBootRomTable.setStatus("current")
_HwBootRomEntry_Object = MibTableRow
hwBootRomEntry = _HwBootRomEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1)
)
hwBootRomEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwBootRomIndex"),
)
if mibBuilder.loadTexts:
    hwBootRomEntry.setStatus("current")


class _HwBootRomIndex_Type(Integer32):
    """Custom type hwBootRomIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_HwBootRomIndex_Type.__name__ = "Integer32"
_HwBootRomIndex_Object = MibTableColumn
hwBootRomIndex = _HwBootRomIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 1),
    _HwBootRomIndex_Type()
)
hwBootRomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBootRomIndex.setStatus("current")
_HwBootRomBootDevice_Type = DisplayString
_HwBootRomBootDevice_Object = MibTableColumn
hwBootRomBootDevice = _HwBootRomBootDevice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 2),
    _HwBootRomBootDevice_Type()
)
hwBootRomBootDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomBootDevice.setStatus("current")
_HwBootRomProcessorNo_Type = Integer32
_HwBootRomProcessorNo_Object = MibTableColumn
hwBootRomProcessorNo = _HwBootRomProcessorNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 3),
    _HwBootRomProcessorNo_Type()
)
hwBootRomProcessorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomProcessorNo.setStatus("current")
_HwBootRomHostName_Type = DisplayString
_HwBootRomHostName_Object = MibTableColumn
hwBootRomHostName = _HwBootRomHostName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 4),
    _HwBootRomHostName_Type()
)
hwBootRomHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomHostName.setStatus("current")
_HwBootRomFileName_Type = DisplayString
_HwBootRomFileName_Object = MibTableColumn
hwBootRomFileName = _HwBootRomFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 5),
    _HwBootRomFileName_Type()
)
hwBootRomFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomFileName.setStatus("current")
_HwBootRomIpOnEthernet_Type = IpAddress
_HwBootRomIpOnEthernet_Object = MibTableColumn
hwBootRomIpOnEthernet = _HwBootRomIpOnEthernet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 6),
    _HwBootRomIpOnEthernet_Type()
)
hwBootRomIpOnEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomIpOnEthernet.setStatus("current")
_HwBootRomIpOnBackPlane_Type = IpAddress
_HwBootRomIpOnBackPlane_Object = MibTableColumn
hwBootRomIpOnBackPlane = _HwBootRomIpOnBackPlane_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 7),
    _HwBootRomIpOnBackPlane_Type()
)
hwBootRomIpOnBackPlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomIpOnBackPlane.setStatus("current")
_HwBootRomHostIp_Type = IpAddress
_HwBootRomHostIp_Object = MibTableColumn
hwBootRomHostIp = _HwBootRomHostIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 8),
    _HwBootRomHostIp_Type()
)
hwBootRomHostIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomHostIp.setStatus("current")
_HwBootRomGatewayIp_Type = IpAddress
_HwBootRomGatewayIp_Object = MibTableColumn
hwBootRomGatewayIp = _HwBootRomGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 9),
    _HwBootRomGatewayIp_Type()
)
hwBootRomGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomGatewayIp.setStatus("current")
_HwBootRomUserName_Type = DisplayString
_HwBootRomUserName_Object = MibTableColumn
hwBootRomUserName = _HwBootRomUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 10),
    _HwBootRomUserName_Type()
)
hwBootRomUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomUserName.setStatus("current")
_HwBootRomPassword_Type = DisplayString
_HwBootRomPassword_Object = MibTableColumn
hwBootRomPassword = _HwBootRomPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 11),
    _HwBootRomPassword_Type()
)
hwBootRomPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomPassword.setStatus("current")
_HwBootRomTargetName_Type = DisplayString
_HwBootRomTargetName_Object = MibTableColumn
hwBootRomTargetName = _HwBootRomTargetName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 12),
    _HwBootRomTargetName_Type()
)
hwBootRomTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomTargetName.setStatus("current")
_HwBootRomStartupScript_Type = DisplayString
_HwBootRomStartupScript_Object = MibTableColumn
hwBootRomStartupScript = _HwBootRomStartupScript_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 13),
    _HwBootRomStartupScript_Type()
)
hwBootRomStartupScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomStartupScript.setStatus("current")
_HwBootRomXModemBaudRate_Type = Integer32
_HwBootRomXModemBaudRate_Object = MibTableColumn
hwBootRomXModemBaudRate = _HwBootRomXModemBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 14),
    _HwBootRomXModemBaudRate_Type()
)
hwBootRomXModemBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomXModemBaudRate.setStatus("current")
_HwBootRomVersion_Type = Integer32
_HwBootRomVersion_Object = MibTableColumn
hwBootRomVersion = _HwBootRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 11, 1, 1, 15),
    _HwBootRomVersion_Type()
)
hwBootRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBootRomVersion.setStatus("current")
_HwSysUpgrade_ObjectIdentity = ObjectIdentity
hwSysUpgrade = _HwSysUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 12)
)
_HwSysUpgradeTable_Object = MibTable
hwSysUpgradeTable = _HwSysUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 12, 1)
)
if mibBuilder.loadTexts:
    hwSysUpgradeTable.setStatus("current")
_HwSysUpgradeEntry_Object = MibTableRow
hwSysUpgradeEntry = _HwSysUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 12, 1, 1)
)
hwSysUpgradeEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwIssuIndex"),
)
if mibBuilder.loadTexts:
    hwSysUpgradeEntry.setStatus("current")
_HwIssuIndex_Type = Integer32
_HwIssuIndex_Object = MibTableColumn
hwIssuIndex = _HwIssuIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 12, 1, 1, 1),
    _HwIssuIndex_Type()
)
hwIssuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIssuIndex.setStatus("current")


class _HwIssuMode_Type(Integer32):
    """Custom type hwIssuMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("issuPrecheck", 2),
          ("issuUpgrade", 1))
    )


_HwIssuMode_Type.__name__ = "Integer32"
_HwIssuMode_Object = MibTableColumn
hwIssuMode = _HwIssuMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 12, 1, 1, 2),
    _HwIssuMode_Type()
)
hwIssuMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIssuMode.setStatus("current")


class _HwIssuImageFile_Type(DisplayString):
    """Custom type hwIssuImageFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HwIssuImageFile_Type.__name__ = "DisplayString"
_HwIssuImageFile_Object = MibTableColumn
hwIssuImageFile = _HwIssuImageFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 12, 1, 1, 3),
    _HwIssuImageFile_Type()
)
hwIssuImageFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIssuImageFile.setStatus("current")


class _HwIssuPafFile_Type(DisplayString):
    """Custom type hwIssuPafFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HwIssuPafFile_Type.__name__ = "DisplayString"
_HwIssuPafFile_Object = MibTableColumn
hwIssuPafFile = _HwIssuPafFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 12, 1, 1, 4),
    _HwIssuPafFile_Type()
)
hwIssuPafFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIssuPafFile.setStatus("current")


class _HwIssuLicenseFile_Type(DisplayString):
    """Custom type hwIssuLicenseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HwIssuLicenseFile_Type.__name__ = "DisplayString"
_HwIssuLicenseFile_Object = MibTableColumn
hwIssuLicenseFile = _HwIssuLicenseFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 12, 1, 1, 5),
    _HwIssuLicenseFile_Type()
)
hwIssuLicenseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIssuLicenseFile.setStatus("current")


class _HwIssuPatchFile_Type(DisplayString):
    """Custom type hwIssuPatchFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 127),
    )


_HwIssuPatchFile_Type.__name__ = "DisplayString"
_HwIssuPatchFile_Object = MibTableColumn
hwIssuPatchFile = _HwIssuPatchFile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 12, 1, 1, 6),
    _HwIssuPatchFile_Type()
)
hwIssuPatchFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIssuPatchFile.setStatus("current")


class _HwIssuState_Type(Integer32):
    """Custom type hwIssuState based on Integer32"""
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
        *(("issuExceptional", 3),
          ("issuRollBackByExceptional", 5),
          ("issuRollBackByUserCancel", 4),
          ("issuUpgrading", 2),
          ("noIssuUpgrading", 1))
    )


_HwIssuState_Type.__name__ = "Integer32"
_HwIssuState_Object = MibScalar
hwIssuState = _HwIssuState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 12, 2),
    _HwIssuState_Type()
)
hwIssuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIssuState.setStatus("current")


class _HwIssuConditionCheck_Type(Integer32):
    """Custom type hwIssuConditionCheck based on Integer32"""
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
        *(("configurationChange", 4),
          ("normal", 1),
          ("notRealtimeBackup", 2),
          ("otherAbnormal", 5),
          ("slotAbnormal", 3))
    )


_HwIssuConditionCheck_Type.__name__ = "Integer32"
_HwIssuConditionCheck_Object = MibScalar
hwIssuConditionCheck = _HwIssuConditionCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 12, 3),
    _HwIssuConditionCheck_Type()
)
hwIssuConditionCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIssuConditionCheck.setStatus("current")
_HwSysSourceIndex_ObjectIdentity = ObjectIdentity
hwSysSourceIndex = _HwSysSourceIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 13)
)
_HwSysSourceIndexTable_Object = MibTable
hwSysSourceIndexTable = _HwSysSourceIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 13, 1)
)
if mibBuilder.loadTexts:
    hwSysSourceIndexTable.setStatus("current")
_HwSysSourceIndexEntry_Object = MibTableRow
hwSysSourceIndexEntry = _HwSysSourceIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 13, 1, 1)
)
hwSysSourceIndexEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysFileType"),
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysFileName"),
)
if mibBuilder.loadTexts:
    hwSysSourceIndexEntry.setStatus("current")


class _HwSysFileType_Type(Integer32):
    """Custom type hwSysFileType based on Integer32"""
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
        *(("config", 2),
          ("image", 1),
          ("license", 4),
          ("paf", 3),
          ("patch", 5))
    )


_HwSysFileType_Type.__name__ = "Integer32"
_HwSysFileType_Object = MibTableColumn
hwSysFileType = _HwSysFileType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 13, 1, 1, 1),
    _HwSysFileType_Type()
)
hwSysFileType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysFileType.setStatus("current")


class _HwSysFileName_Type(OctetString):
    """Custom type hwSysFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 110),
    )


_HwSysFileName_Type.__name__ = "OctetString"
_HwSysFileName_Object = MibTableColumn
hwSysFileName = _HwSysFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 13, 1, 1, 2),
    _HwSysFileName_Type()
)
hwSysFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysFileName.setStatus("current")


class _HwSysFileIndex_Type(Integer32):
    """Custom type hwSysFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysFileIndex_Type.__name__ = "Integer32"
_HwSysFileIndex_Object = MibTableColumn
hwSysFileIndex = _HwSysFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 13, 1, 1, 3),
    _HwSysFileIndex_Type()
)
hwSysFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysFileIndex.setStatus("current")
_HwSysRebootInfo_ObjectIdentity = ObjectIdentity
hwSysRebootInfo = _HwSysRebootInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 14)
)


class _HwSysRebootTimes_Type(Integer32):
    """Custom type hwSysRebootTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysRebootTimes_Type.__name__ = "Integer32"
_HwSysRebootTimes_Object = MibScalar
hwSysRebootTimes = _HwSysRebootTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 14, 1),
    _HwSysRebootTimes_Type()
)
hwSysRebootTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysRebootTimes.setStatus("current")
_HwSysRebootRecordTable_Object = MibTable
hwSysRebootRecordTable = _HwSysRebootRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 14, 2)
)
if mibBuilder.loadTexts:
    hwSysRebootRecordTable.setStatus("current")
_HwSysRebootRecordEntry_Object = MibTableRow
hwSysRebootRecordEntry = _HwSysRebootRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 14, 2, 1)
)
hwSysRebootRecordEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysRebootRecordIndex"),
)
if mibBuilder.loadTexts:
    hwSysRebootRecordEntry.setStatus("current")


class _HwSysRebootRecordIndex_Type(Integer32):
    """Custom type hwSysRebootRecordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSysRebootRecordIndex_Type.__name__ = "Integer32"
_HwSysRebootRecordIndex_Object = MibTableColumn
hwSysRebootRecordIndex = _HwSysRebootRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 14, 2, 1, 1),
    _HwSysRebootRecordIndex_Type()
)
hwSysRebootRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysRebootRecordIndex.setStatus("current")


class _HwSysRebootReason_Type(Integer32):
    """Custom type hwSysRebootReason based on Integer32"""
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
        *(("manual", 1),
          ("powerOff", 2),
          ("schedule", 4),
          ("software", 5),
          ("unknown", 3))
    )


_HwSysRebootReason_Type.__name__ = "Integer32"
_HwSysRebootReason_Object = MibTableColumn
hwSysRebootReason = _HwSysRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 14, 2, 1, 2),
    _HwSysRebootReason_Type()
)
hwSysRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysRebootReason.setStatus("current")


class _HwSysRebootTime_Type(DateAndTime):
    """Custom type hwSysRebootTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwSysRebootTime_Type.__name__ = "DateAndTime"
_HwSysRebootTime_Object = MibTableColumn
hwSysRebootTime = _HwSysRebootTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 14, 2, 1, 3),
    _HwSysRebootTime_Type()
)
hwSysRebootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysRebootTime.setStatus("current")
_HwSysDeviceCheck_ObjectIdentity = ObjectIdentity
hwSysDeviceCheck = _HwSysDeviceCheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 15)
)


class _HwSysDeviceCheckStart_Type(Integer32):
    """Custom type hwSysDeviceCheckStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("checkStart", 1)
    )


_HwSysDeviceCheckStart_Type.__name__ = "Integer32"
_HwSysDeviceCheckStart_Object = MibScalar
hwSysDeviceCheckStart = _HwSysDeviceCheckStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 15, 1),
    _HwSysDeviceCheckStart_Type()
)
hwSysDeviceCheckStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysDeviceCheckStart.setStatus("current")


class _HwSysDeviceCheckState_Type(Integer32):
    """Custom type hwSysDeviceCheckState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checking", 2),
          ("done", 1))
    )


_HwSysDeviceCheckState_Type.__name__ = "Integer32"
_HwSysDeviceCheckState_Object = MibScalar
hwSysDeviceCheckState = _HwSysDeviceCheckState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 15, 2),
    _HwSysDeviceCheckState_Type()
)
hwSysDeviceCheckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysDeviceCheckState.setStatus("current")
_HwSysSwitchoverState_ObjectIdentity = ObjectIdentity
hwSysSwitchoverState = _HwSysSwitchoverState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19)
)
_HwSysSwitchoverStateTable_Object = MibTable
hwSysSwitchoverStateTable = _HwSysSwitchoverStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 1)
)
if mibBuilder.loadTexts:
    hwSysSwitchoverStateTable.setStatus("current")
_HwSysSwitchoverStateEntry_Object = MibTableRow
hwSysSwitchoverStateEntry = _HwSysSwitchoverStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 1, 1)
)
hwSysSwitchoverStateEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysSwitchoverStateIndex"),
)
if mibBuilder.loadTexts:
    hwSysSwitchoverStateEntry.setStatus("current")


class _HwSysSwitchoverStateIndex_Type(Integer32):
    """Custom type hwSysSwitchoverStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSysSwitchoverStateIndex_Type.__name__ = "Integer32"
_HwSysSwitchoverStateIndex_Object = MibTableColumn
hwSysSwitchoverStateIndex = _HwSysSwitchoverStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 1, 1, 1),
    _HwSysSwitchoverStateIndex_Type()
)
hwSysSwitchoverStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysSwitchoverStateIndex.setStatus("current")


class _HwSysSwitchoverSlotId_Type(Integer32):
    """Custom type hwSysSwitchoverSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSysSwitchoverSlotId_Type.__name__ = "Integer32"
_HwSysSwitchoverSlotId_Object = MibTableColumn
hwSysSwitchoverSlotId = _HwSysSwitchoverSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 1, 1, 2),
    _HwSysSwitchoverSlotId_Type()
)
hwSysSwitchoverSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysSwitchoverSlotId.setStatus("current")


class _HwSysSwitchoverBoardType_Type(Integer32):
    """Custom type hwSysSwitchoverBoardType based on Integer32"""
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
        *(("issuNewMaster", 6),
          ("issuOldMaster", 5),
          ("master", 1),
          ("slave", 2),
          ("systemMaster", 3),
          ("systemSlave", 4))
    )


_HwSysSwitchoverBoardType_Type.__name__ = "Integer32"
_HwSysSwitchoverBoardType_Object = MibTableColumn
hwSysSwitchoverBoardType = _HwSysSwitchoverBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 1, 1, 3),
    _HwSysSwitchoverBoardType_Type()
)
hwSysSwitchoverBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysSwitchoverBoardType.setStatus("current")


class _HwSysSwitchoverInfo_Type(OctetString):
    """Custom type hwSysSwitchoverInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 190),
    )


_HwSysSwitchoverInfo_Type.__name__ = "OctetString"
_HwSysSwitchoverInfo_Object = MibTableColumn
hwSysSwitchoverInfo = _HwSysSwitchoverInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 1, 1, 4),
    _HwSysSwitchoverInfo_Type()
)
hwSysSwitchoverInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysSwitchoverInfo.setStatus("current")
_HwSysSwitchoverStateMultiTable_Object = MibTable
hwSysSwitchoverStateMultiTable = _HwSysSwitchoverStateMultiTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 2)
)
if mibBuilder.loadTexts:
    hwSysSwitchoverStateMultiTable.setStatus("current")
_HwSysSwitchoverStateMultiEntry_Object = MibTableRow
hwSysSwitchoverStateMultiEntry = _HwSysSwitchoverStateMultiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 2, 1)
)
hwSysSwitchoverStateMultiEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysMultiSwtStateIndex"),
)
if mibBuilder.loadTexts:
    hwSysSwitchoverStateMultiEntry.setStatus("current")


class _HwSysMultiSwtStateIndex_Type(Integer32):
    """Custom type hwSysMultiSwtStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSysMultiSwtStateIndex_Type.__name__ = "Integer32"
_HwSysMultiSwtStateIndex_Object = MibTableColumn
hwSysMultiSwtStateIndex = _HwSysMultiSwtStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 2, 1, 1),
    _HwSysMultiSwtStateIndex_Type()
)
hwSysMultiSwtStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysMultiSwtStateIndex.setStatus("current")


class _HwSysMultiSwtChassisId_Type(OctetString):
    """Custom type hwSysMultiSwtChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwSysMultiSwtChassisId_Type.__name__ = "OctetString"
_HwSysMultiSwtChassisId_Object = MibTableColumn
hwSysMultiSwtChassisId = _HwSysMultiSwtChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 2, 1, 2),
    _HwSysMultiSwtChassisId_Type()
)
hwSysMultiSwtChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysMultiSwtChassisId.setStatus("current")


class _HwSysMultiSwtSlotId_Type(Integer32):
    """Custom type hwSysMultiSwtSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSysMultiSwtSlotId_Type.__name__ = "Integer32"
_HwSysMultiSwtSlotId_Object = MibTableColumn
hwSysMultiSwtSlotId = _HwSysMultiSwtSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 2, 1, 3),
    _HwSysMultiSwtSlotId_Type()
)
hwSysMultiSwtSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysMultiSwtSlotId.setStatus("current")


class _HwSysMultiSwtBoardType_Type(Integer32):
    """Custom type hwSysMultiSwtBoardType based on Integer32"""
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
        *(("issuNewMaster", 6),
          ("issuOldMaster", 5),
          ("master", 1),
          ("slave", 2),
          ("systemMaster", 3),
          ("systemSlave", 4))
    )


_HwSysMultiSwtBoardType_Type.__name__ = "Integer32"
_HwSysMultiSwtBoardType_Object = MibTableColumn
hwSysMultiSwtBoardType = _HwSysMultiSwtBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 2, 1, 4),
    _HwSysMultiSwtBoardType_Type()
)
hwSysMultiSwtBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysMultiSwtBoardType.setStatus("current")


class _HwSysMultiSwtInfo_Type(OctetString):
    """Custom type hwSysMultiSwtInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 190),
    )


_HwSysMultiSwtInfo_Type.__name__ = "OctetString"
_HwSysMultiSwtInfo_Object = MibTableColumn
hwSysMultiSwtInfo = _HwSysMultiSwtInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 19, 2, 1, 5),
    _HwSysMultiSwtInfo_Type()
)
hwSysMultiSwtInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysMultiSwtInfo.setStatus("current")
_HwSysVoiceFile_ObjectIdentity = ObjectIdentity
hwSysVoiceFile = _HwSysVoiceFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 20)
)


class _HwSysVoiceFileNum_Type(Integer32):
    """Custom type hwSysVoiceFileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysVoiceFileNum_Type.__name__ = "Integer32"
_HwSysVoiceFileNum_Object = MibScalar
hwSysVoiceFileNum = _HwSysVoiceFileNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 20, 1),
    _HwSysVoiceFileNum_Type()
)
hwSysVoiceFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysVoiceFileNum.setStatus("current")
_HwSysVoiceFileTable_Object = MibTable
hwSysVoiceFileTable = _HwSysVoiceFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 20, 2)
)
if mibBuilder.loadTexts:
    hwSysVoiceFileTable.setStatus("current")
_HwSysVoiceFileEntry_Object = MibTableRow
hwSysVoiceFileEntry = _HwSysVoiceFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 20, 2, 1)
)
hwSysVoiceFileEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysVoiceFileIndex"),
)
if mibBuilder.loadTexts:
    hwSysVoiceFileEntry.setStatus("current")


class _HwSysVoiceFileIndex_Type(Integer32):
    """Custom type hwSysVoiceFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSysVoiceFileIndex_Type.__name__ = "Integer32"
_HwSysVoiceFileIndex_Object = MibTableColumn
hwSysVoiceFileIndex = _HwSysVoiceFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 20, 2, 1, 1),
    _HwSysVoiceFileIndex_Type()
)
hwSysVoiceFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysVoiceFileIndex.setStatus("current")
_HwSysVoiceFileName_Type = DisplayString
_HwSysVoiceFileName_Object = MibTableColumn
hwSysVoiceFileName = _HwSysVoiceFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 20, 2, 1, 2),
    _HwSysVoiceFileName_Type()
)
hwSysVoiceFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysVoiceFileName.setStatus("current")


class _HwSysVoiceFileSize_Type(Integer32):
    """Custom type hwSysVoiceFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysVoiceFileSize_Type.__name__ = "Integer32"
_HwSysVoiceFileSize_Object = MibTableColumn
hwSysVoiceFileSize = _HwSysVoiceFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 20, 2, 1, 3),
    _HwSysVoiceFileSize_Type()
)
hwSysVoiceFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysVoiceFileSize.setStatus("current")
_HwSysVoiceFileLocation_Type = DisplayString
_HwSysVoiceFileLocation_Object = MibTableColumn
hwSysVoiceFileLocation = _HwSysVoiceFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 20, 2, 1, 4),
    _HwSysVoiceFileLocation_Type()
)
hwSysVoiceFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysVoiceFileLocation.setStatus("current")
_HwSysWlanApUpgrade_ObjectIdentity = ObjectIdentity
hwSysWlanApUpgrade = _HwSysWlanApUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24)
)
_HwSysWlanApUpgradeCmd_ObjectIdentity = ObjectIdentity
hwSysWlanApUpgradeCmd = _HwSysWlanApUpgradeCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 1)
)


class _HwSysWlanApUpgradeMode_Type(Integer32):
    """Custom type hwSysWlanApUpgradeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2),
          ("tftp", 3))
    )


_HwSysWlanApUpgradeMode_Type.__name__ = "Integer32"
_HwSysWlanApUpgradeMode_Object = MibScalar
hwSysWlanApUpgradeMode = _HwSysWlanApUpgradeMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 1, 1),
    _HwSysWlanApUpgradeMode_Type()
)
hwSysWlanApUpgradeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeMode.setStatus("current")


class _HwSysWlanApUpgradeFileName_Type(DisplayString):
    """Custom type hwSysWlanApUpgradeFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HwSysWlanApUpgradeFileName_Type.__name__ = "DisplayString"
_HwSysWlanApUpgradeFileName_Object = MibScalar
hwSysWlanApUpgradeFileName = _HwSysWlanApUpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 1, 2),
    _HwSysWlanApUpgradeFileName_Type()
)
hwSysWlanApUpgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeFileName.setStatus("current")
_HwSysWlanApUpgradeServerIp_Type = IpAddress
_HwSysWlanApUpgradeServerIp_Object = MibScalar
hwSysWlanApUpgradeServerIp = _HwSysWlanApUpgradeServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 1, 3),
    _HwSysWlanApUpgradeServerIp_Type()
)
hwSysWlanApUpgradeServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeServerIp.setStatus("current")


class _HwSysWlanApUpgradeServerUserName_Type(DisplayString):
    """Custom type hwSysWlanApUpgradeServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwSysWlanApUpgradeServerUserName_Type.__name__ = "DisplayString"
_HwSysWlanApUpgradeServerUserName_Object = MibScalar
hwSysWlanApUpgradeServerUserName = _HwSysWlanApUpgradeServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 1, 4),
    _HwSysWlanApUpgradeServerUserName_Type()
)
hwSysWlanApUpgradeServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeServerUserName.setStatus("current")


class _HwSysWlanApUpgradeServerPassword_Type(DisplayString):
    """Custom type hwSysWlanApUpgradeServerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwSysWlanApUpgradeServerPassword_Type.__name__ = "DisplayString"
_HwSysWlanApUpgradeServerPassword_Object = MibScalar
hwSysWlanApUpgradeServerPassword = _HwSysWlanApUpgradeServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 1, 5),
    _HwSysWlanApUpgradeServerPassword_Type()
)
hwSysWlanApUpgradeServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeServerPassword.setStatus("current")
_HwSysWlanApUpgradeStatus_ObjectIdentity = ObjectIdentity
hwSysWlanApUpgradeStatus = _HwSysWlanApUpgradeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 2)
)


class _HwSysWlanApUpgradeProgressStatus_Type(Integer32):
    """Custom type hwSysWlanApUpgradeProgressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("efsAndApTypeMismatched", 7),
          ("efsAndVersionMismatched", 5),
          ("failToDownloadFile", 4),
          ("fileContentError", 8),
          ("invalidFileName", 6),
          ("noUpdateResult", 10),
          ("updateFailed", 2),
          ("updateSuccessful", 1),
          ("updating", 0),
          ("writingMemoryError", 9))
    )


_HwSysWlanApUpgradeProgressStatus_Type.__name__ = "Integer32"
_HwSysWlanApUpgradeProgressStatus_Object = MibScalar
hwSysWlanApUpgradeProgressStatus = _HwSysWlanApUpgradeProgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 2, 1),
    _HwSysWlanApUpgradeProgressStatus_Type()
)
hwSysWlanApUpgradeProgressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeProgressStatus.setStatus("current")


class _HwSysWlanApUpgradeLoadProgress_Type(Integer32):
    """Custom type hwSysWlanApUpgradeLoadProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwSysWlanApUpgradeLoadProgress_Type.__name__ = "Integer32"
_HwSysWlanApUpgradeLoadProgress_Object = MibScalar
hwSysWlanApUpgradeLoadProgress = _HwSysWlanApUpgradeLoadProgress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 2, 2),
    _HwSysWlanApUpgradeLoadProgress_Type()
)
hwSysWlanApUpgradeLoadProgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeLoadProgress.setStatus("current")


class _HwSysWlanApUpgradeStorageProgress_Type(Integer32):
    """Custom type hwSysWlanApUpgradeStorageProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwSysWlanApUpgradeStorageProgress_Type.__name__ = "Integer32"
_HwSysWlanApUpgradeStorageProgress_Object = MibScalar
hwSysWlanApUpgradeStorageProgress = _HwSysWlanApUpgradeStorageProgress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 2, 3),
    _HwSysWlanApUpgradeStorageProgress_Type()
)
hwSysWlanApUpgradeStorageProgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeStorageProgress.setStatus("current")
_HwSysWlanApUpgradeNotifications_ObjectIdentity = ObjectIdentity
hwSysWlanApUpgradeNotifications = _HwSysWlanApUpgradeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 3)
)
_HwSysAndroidFile_ObjectIdentity = ObjectIdentity
hwSysAndroidFile = _HwSysAndroidFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 25)
)


class _HwSysAndroidFileNum_Type(Integer32):
    """Custom type hwSysAndroidFileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysAndroidFileNum_Type.__name__ = "Integer32"
_HwSysAndroidFileNum_Object = MibScalar
hwSysAndroidFileNum = _HwSysAndroidFileNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 25, 1),
    _HwSysAndroidFileNum_Type()
)
hwSysAndroidFileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysAndroidFileNum.setStatus("current")
_HwSysAndroidFileTable_Object = MibTable
hwSysAndroidFileTable = _HwSysAndroidFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 25, 2)
)
if mibBuilder.loadTexts:
    hwSysAndroidFileTable.setStatus("current")
_HwSysAndroidFileEntry_Object = MibTableRow
hwSysAndroidFileEntry = _HwSysAndroidFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 25, 2, 1)
)
hwSysAndroidFileEntry.setIndexNames(
    (0, "HUAWEI-SYS-MAN-MIB", "hwSysAndroidFileIndex"),
)
if mibBuilder.loadTexts:
    hwSysAndroidFileEntry.setStatus("current")


class _HwSysAndroidFileIndex_Type(Integer32):
    """Custom type hwSysAndroidFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSysAndroidFileIndex_Type.__name__ = "Integer32"
_HwSysAndroidFileIndex_Object = MibTableColumn
hwSysAndroidFileIndex = _HwSysAndroidFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 25, 2, 1, 1),
    _HwSysAndroidFileIndex_Type()
)
hwSysAndroidFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSysAndroidFileIndex.setStatus("current")
_HwSysAndroidFileName_Type = DisplayString
_HwSysAndroidFileName_Object = MibTableColumn
hwSysAndroidFileName = _HwSysAndroidFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 25, 2, 1, 2),
    _HwSysAndroidFileName_Type()
)
hwSysAndroidFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysAndroidFileName.setStatus("current")


class _HwSysAndroidFileSize_Type(Integer32):
    """Custom type hwSysAndroidFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSysAndroidFileSize_Type.__name__ = "Integer32"
_HwSysAndroidFileSize_Object = MibTableColumn
hwSysAndroidFileSize = _HwSysAndroidFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 25, 2, 1, 3),
    _HwSysAndroidFileSize_Type()
)
hwSysAndroidFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysAndroidFileSize.setStatus("current")
_HwSysAndroidFileLocation_Type = DisplayString
_HwSysAndroidFileLocation_Object = MibTableColumn
hwSysAndroidFileLocation = _HwSysAndroidFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 25, 2, 1, 4),
    _HwSysAndroidFileLocation_Type()
)
hwSysAndroidFileLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysAndroidFileLocation.setStatus("current")


class _HwSysAndroidFileReason_Type(DisplayString):
    """Custom type hwSysAndroidFileReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSysAndroidFileReason_Type.__name__ = "DisplayString"
_HwSysAndroidFileReason_Object = MibTableColumn
hwSysAndroidFileReason = _HwSysAndroidFileReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 25, 2, 1, 5),
    _HwSysAndroidFileReason_Type()
)
hwSysAndroidFileReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysAndroidFileReason.setStatus("current")
_HuaweiSystemManMIBNotifications_ObjectIdentity = ObjectIdentity
huaweiSystemManMIBNotifications = _HuaweiSystemManMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2)
)
_HwPatchTrap_ObjectIdentity = ObjectIdentity
hwPatchTrap = _HwPatchTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 5)
)
_HwSysEvmTraps_ObjectIdentity = ObjectIdentity
hwSysEvmTraps = _HwSysEvmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 20)
)
_HwSysEvmTrapsObject_ObjectIdentity = ObjectIdentity
hwSysEvmTrapsObject = _HwSysEvmTrapsObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 20, 1)
)
_HwSysEvmRoleName_Type = OctetString
_HwSysEvmRoleName_Object = MibScalar
hwSysEvmRoleName = _HwSysEvmRoleName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 20, 1, 1),
    _HwSysEvmRoleName_Type()
)
hwSysEvmRoleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSysEvmRoleName.setStatus("current")
_HwSysEvmDownloadFileName_Type = OctetString
_HwSysEvmDownloadFileName_Object = MibScalar
hwSysEvmDownloadFileName = _HwSysEvmDownloadFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 20, 1, 2),
    _HwSysEvmDownloadFileName_Type()
)
hwSysEvmDownloadFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSysEvmDownloadFileName.setStatus("current")
_HwSysEvmInstallFileName_Type = OctetString
_HwSysEvmInstallFileName_Object = MibScalar
hwSysEvmInstallFileName = _HwSysEvmInstallFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 20, 1, 3),
    _HwSysEvmInstallFileName_Type()
)
hwSysEvmInstallFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSysEvmInstallFileName.setStatus("current")
_HwSysEvmNotifications_ObjectIdentity = ObjectIdentity
hwSysEvmNotifications = _HwSysEvmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 20, 2)
)
_HuaweiSystemManMIBConformance_ObjectIdentity = ObjectIdentity
huaweiSystemManMIBConformance = _HuaweiSystemManMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3)
)
_HuaweiSystemManMIBCompliances_ObjectIdentity = ObjectIdentity
huaweiSystemManMIBCompliances = _HuaweiSystemManMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 1)
)
_HuaweiSystemManMIBGroups_ObjectIdentity = ObjectIdentity
huaweiSystemManMIBGroups = _HuaweiSystemManMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2)
)

# Managed Objects groups

huaweiSysClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 1)
)
huaweiSysClockGroup.setObjects(
    ("HUAWEI-SYS-MAN-MIB", "hwSysLocalClock")
)
if mibBuilder.loadTexts:
    huaweiSysClockGroup.setStatus("current")

huaweiSysReloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 2)
)
huaweiSysReloadGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysReloadSchedule"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadAction"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadImage"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadCfgFile"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadReason"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadPatchFile"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadLicenseFile"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadPafFile"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadPatchState"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysLatestRebootErrorInfo"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadScheduleTime"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadEntity"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadRowStatus"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadOperateDestType"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadOperateDestIndex"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysSlaveSwitchChassisNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysSlaveSwitchOperType"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysSlaveSwitchEnableStatus"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysDelayReboot"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadAndroidFile"))
)
if mibBuilder.loadTexts:
    huaweiSysReloadGroup.setStatus("current")

huaweiSysImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 3)
)
huaweiSysImageGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysImageNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysImageName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysImageSize"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysImageLocation"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysImageVersion"))
)
if mibBuilder.loadTexts:
    huaweiSysImageGroup.setStatus("current")

huaweiSysCFGFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 4)
)
huaweiSysCFGFileGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysCFGFileNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysCFGFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysCFGFileSize"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysCFGFileLocation"))
)
if mibBuilder.loadTexts:
    huaweiSysCFGFileGroup.setStatus("current")

hwSysCurGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 5)
)
hwSysCurGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysCurCFGFileIndex"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysCurImageIndex"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysCurPafFileIndex"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysCurLicenseIndex"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysCurPatchFileIndex"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysCurVoiceFileIndex"))
)
if mibBuilder.loadTexts:
    hwSysCurGroup.setStatus("current")

hwPatchLoadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 8)
)
hwPatchLoadGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwPatchLoadDestType"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchLoadDestIndex"),
        ("HUAWEI-SYS-MAN-MIB", "hwLoadPatchRowState"))
)
if mibBuilder.loadTexts:
    hwPatchLoadGroup.setStatus("current")

hwPatchInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 10)
)
hwPatchInfoGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwPatchDescription"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchFuncNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchTextLen"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchDataLen"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchType"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchAdminStatus"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchStateTempPatchNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchStateCommonPatchNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchStateRuningPatchNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchStateActivePatchNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchStateDeactivePatchNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchHistoryVersion"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchStateTotalPatchNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchStateDataUsed"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchStateTextUsed"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchDataMax"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchTextMax"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchIdleNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchNumMax"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchActiveTime"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchBuildTime"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchVersion"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchHistoryProgrameVersion"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchUsedFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchErrorTableMax"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchHistoryTableMax"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchRecordReset"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchProgramVersion"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchOperateState"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchErrorSlot"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchErrorPatchIndex"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchErrorCode"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchHistoryBeginTime"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchHistoryEndTime"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchHistoryAction"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchEndIndex"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchTrapEnble"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchBeginIndex"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchId"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchLatestId"),
        ("HUAWEI-SYS-MAN-MIB", "hwSlotId"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchErrorPatchFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchFailReason"))
)
if mibBuilder.loadTexts:
    hwPatchInfoGroup.setStatus("current")

hwPatchFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 11)
)
hwPatchFileGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwPatchFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchFileSize"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchFileLocation"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchFileVersion"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchFileNum"))
)
if mibBuilder.loadTexts:
    hwPatchFileGroup.setStatus("current")

hwSysPafFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 13)
)
hwSysPafFileGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysPafFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysPafFileSize"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysPafFileLocation"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysPafFileVersion"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysPafFileNum"))
)
if mibBuilder.loadTexts:
    hwSysPafFileGroup.setStatus("current")

hwSysPafLicenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 14)
)
hwSysPafLicenseGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysLicenseFileNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysLicenseFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysLicenseFileSize"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysLicenseFileLocation"))
)
if mibBuilder.loadTexts:
    hwSysPafLicenseGroup.setStatus("current")

hwSysRebootAndSwitchGrop = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 15)
)
hwSysRebootAndSwitchGrop.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysReboot"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysSlaveSwitchEnable"))
)
if mibBuilder.loadTexts:
    hwSysRebootAndSwitchGrop.setStatus("current")

hwBootRomGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 16)
)
hwBootRomGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwBootRomBootDevice"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomHostName"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomIpOnEthernet"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomIpOnBackPlane"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomHostIp"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomGatewayIp"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomUserName"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomPassword"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomTargetName"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomStartupScript"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomXModemBaudRate"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomVersion"),
        ("HUAWEI-SYS-MAN-MIB", "hwBootRomProcessorNo"))
)
if mibBuilder.loadTexts:
    hwBootRomGroup.setStatus("current")

hwSysUpgradeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 18)
)
hwSysUpgradeGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwIssuMode"),
        ("HUAWEI-SYS-MAN-MIB", "hwIssuImageFile"),
        ("HUAWEI-SYS-MAN-MIB", "hwIssuPafFile"),
        ("HUAWEI-SYS-MAN-MIB", "hwIssuLicenseFile"),
        ("HUAWEI-SYS-MAN-MIB", "hwIssuPatchFile"),
        ("HUAWEI-SYS-MAN-MIB", "hwIssuState"),
        ("HUAWEI-SYS-MAN-MIB", "hwIssuConditionCheck"))
)
if mibBuilder.loadTexts:
    hwSysUpgradeGroup.setStatus("current")

hwSysRebootInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 19)
)
hwSysRebootInfoGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysRebootTimes"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysRebootReason"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysRebootTime"))
)
if mibBuilder.loadTexts:
    hwSysRebootInfoGroup.setStatus("current")

hwSysDeviceCheckGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 20)
)
hwSysDeviceCheckGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysDeviceCheckStart"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysDeviceCheckState"))
)
if mibBuilder.loadTexts:
    hwSysDeviceCheckGroup.setStatus("current")

huaweiSysVoiceFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 21)
)
huaweiSysVoiceFileGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysVoiceFileNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysVoiceFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysVoiceFileSize"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysVoiceFileLocation"))
)
if mibBuilder.loadTexts:
    huaweiSysVoiceFileGroup.setStatus("current")

hwSysWlanApUpgradeCmdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 22)
)
hwSysWlanApUpgradeCmdGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeMode"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeServerIp"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeServerUserName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeServerPassword"))
)
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeCmdGroup.setStatus("current")

hwSysWlanApUpgradeStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 23)
)
hwSysWlanApUpgradeStatusGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeProgressStatus"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeLoadProgress"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeStorageProgress"))
)
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeStatusGroup.setStatus("current")

huaweiSysAndroidFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 25)
)
huaweiSysAndroidFileGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysAndroidFileNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysAndroidFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysAndroidFileSize"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysAndroidFileLocation"))
)
if mibBuilder.loadTexts:
    huaweiSysAndroidFileGroup.setStatus("current")

huaweihwSysEvmTrapsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 26)
)
huaweihwSysEvmTrapsObjectGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysEvmRoleName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysEvmDownloadFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysEvmInstallFileName"))
)
if mibBuilder.loadTexts:
    huaweihwSysEvmTrapsObjectGroup.setStatus("current")


# Notification objects

hwSysWlanApUpgradeBeginNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 3, 1)
)
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeBeginNotify.setStatus(
        "current"
    )

hwSysWlanApUpgradeResultNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 3, 2)
)
hwSysWlanApUpgradeResultNotify.setObjects(
    ("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeProgressStatus")
)
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeResultNotify.setStatus(
        "current"
    )

hwSysWlanApUpgradeUbootNotMatchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 3, 3)
)
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeUbootNotMatchNotify.setStatus(
        "current"
    )

hwSysWlanApUpgradeAssistantPackageNotMatchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 1, 24, 3, 4)
)
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeAssistantPackageNotMatchNotify.setStatus(
        "current"
    )

hwSysClockChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 1)
)
hwSysClockChangedNotification.setObjects(
    ("HUAWEI-SYS-MAN-MIB", "hwSysLocalClock")
)
if mibBuilder.loadTexts:
    hwSysClockChangedNotification.setStatus(
        "current"
    )

hwSysReloadNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 2)
)
hwSysReloadNotification.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysReloadImage"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadCfgFile"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadReason"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadScheduleTime"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadAction"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadPafFile"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadLicenseFile"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadPatchFile"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadAndroidFile"))
)
if mibBuilder.loadTexts:
    hwSysReloadNotification.setStatus(
        "current"
    )

hwSysMasterHDError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 3)
)
if mibBuilder.loadTexts:
    hwSysMasterHDError.setStatus(
        "current"
    )

hwSysSlaveHDError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 4)
)
if mibBuilder.loadTexts:
    hwSysSlaveHDError.setStatus(
        "current"
    )

hwPatchErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 5, 1)
)
hwPatchErrorTrap.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwPatchErrorSlot"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchErrorPatchIndex"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchErrorCode"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchErrorPatchFileName"))
)
if mibBuilder.loadTexts:
    hwPatchErrorTrap.setStatus(
        "current"
    )

hwPatchActiveOverTimeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 5, 2)
)
hwPatchActiveOverTimeTrap.setObjects(
    ("HUAWEI-SYS-MAN-MIB", "hwPatchOperateState")
)
if mibBuilder.loadTexts:
    hwPatchActiveOverTimeTrap.setStatus(
        "current"
    )

hwPatchMalfunctionComebackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 5, 3)
)
hwPatchMalfunctionComebackTrap.setObjects(
    ("HUAWEI-SYS-MAN-MIB", "hwPatchOperateState")
)
if mibBuilder.loadTexts:
    hwPatchMalfunctionComebackTrap.setStatus(
        "current"
    )

hwPatchUpdateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 5, 4)
)
hwPatchUpdateTrap.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwPatchVersion"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchType"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchOperateState"))
)
if mibBuilder.loadTexts:
    hwPatchUpdateTrap.setStatus(
        "current"
    )

hwSysMasterCfcardError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 6)
)
if mibBuilder.loadTexts:
    hwSysMasterCfcardError.setStatus(
        "current"
    )

hwSysSlaveCfcardError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 7)
)
if mibBuilder.loadTexts:
    hwSysSlaveCfcardError.setStatus(
        "current"
    )

hwSysSlaveSwitchSuccessNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 8)
)
hwSysSlaveSwitchSuccessNotification.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysSlaveSwitchChassisNum"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysSlaveSwitchSrc"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysSlaveSwitchDst"))
)
if mibBuilder.loadTexts:
    hwSysSlaveSwitchSuccessNotification.setStatus(
        "current"
    )

hwSysSlaveSwitchFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 9)
)
hwSysSlaveSwitchFailNotification.setObjects(
    ("HUAWEI-SYS-MAN-MIB", "hwSysSlaveSwitchChassisNum")
)
if mibBuilder.loadTexts:
    hwSysSlaveSwitchFailNotification.setStatus(
        "current"
    )

hwSysIssuNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 10)
)
hwSysIssuNotification.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwIssuState"),
        ("HUAWEI-SYS-MAN-MIB", "hwIssuConditionCheck"))
)
if mibBuilder.loadTexts:
    hwSysIssuNotification.setStatus(
        "current"
    )

hwPatchInstallFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 11)
)
hwPatchInstallFail.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwPatchUsedFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchVersion"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchFailReason"))
)
if mibBuilder.loadTexts:
    hwPatchInstallFail.setStatus(
        "current"
    )

hwPatchInstallFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 12)
)
hwPatchInstallFailClear.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwPatchUsedFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchVersion"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchFailReason"))
)
if mibBuilder.loadTexts:
    hwPatchInstallFailClear.setStatus(
        "current"
    )

hwSumUpgradeSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 13)
)
hwSumUpgradeSuccess.setObjects(
    ("HUAWEI-SYS-MAN-MIB", "hwSysImageVersion")
)
if mibBuilder.loadTexts:
    hwSumUpgradeSuccess.setStatus(
        "current"
    )

hwSysCfgFileErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 14)
)
hwSysCfgFileErrorNotification.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysCFGFileName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysCFGFileReason"))
)
if mibBuilder.loadTexts:
    hwSysCfgFileErrorNotification.setStatus(
        "current"
    )

hwSysImageErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 15)
)
hwSysImageErrorNotification.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysImageName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysImageName"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysImageReason"))
)
if mibBuilder.loadTexts:
    hwSysImageErrorNotification.setStatus(
        "current"
    )

hwSysPafChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 16)
)
hwSysPafChangeNotification.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysReloadEntity"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysPafFileName"))
)
if mibBuilder.loadTexts:
    hwSysPafChangeNotification.setStatus(
        "current"
    )

hwSysLicenseChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 17)
)
hwSysLicenseChangeNotification.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysReloadEntity"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysLicenseFileName"))
)
if mibBuilder.loadTexts:
    hwSysLicenseChangeNotification.setStatus(
        "current"
    )

hwSystemBoardExclude = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 18)
)
hwSystemBoardExclude.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwSystemBoardExclude.setStatus(
        "current"
    )

hwSystemBoardExcludeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 19)
)
hwSystemBoardExcludeClear.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwSystemBoardExcludeClear.setStatus(
        "current"
    )

hwEvmVmAbnormalRunNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 20, 2, 1)
)
hwEvmVmAbnormalRunNotification.setObjects(
    ("HUAWEI-SYS-MAN-MIB", "hwSysEvmRoleName")
)
if mibBuilder.loadTexts:
    hwEvmVmAbnormalRunNotification.setStatus(
        "current"
    )

hwEvmVmNotRunningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 20, 2, 2)
)
hwEvmVmNotRunningNotification.setObjects(
    ("HUAWEI-SYS-MAN-MIB", "hwSysEvmRoleName")
)
if mibBuilder.loadTexts:
    hwEvmVmNotRunningNotification.setStatus(
        "current"
    )

hwEvmVmAbnormalRestartNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 20, 2, 3)
)
hwEvmVmAbnormalRestartNotification.setObjects(
    ("HUAWEI-SYS-MAN-MIB", "hwSysEvmRoleName")
)
if mibBuilder.loadTexts:
    hwEvmVmAbnormalRestartNotification.setStatus(
        "current"
    )

hwEvmDownloadFailedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 20, 2, 4)
)
hwEvmDownloadFailedNotification.setObjects(
    ("HUAWEI-SYS-MAN-MIB", "hwSysEvmDownloadFileName")
)
if mibBuilder.loadTexts:
    hwEvmDownloadFailedNotification.setStatus(
        "current"
    )

hwEvmInstallFailedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 2, 20, 2, 5)
)
hwEvmInstallFailedNotification.setObjects(
    ("HUAWEI-SYS-MAN-MIB", "hwSysEvmInstallFileName")
)
if mibBuilder.loadTexts:
    hwEvmInstallFailedNotification.setStatus(
        "current"
    )


# Notifications groups

huaweiSystemManNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 6)
)
huaweiSystemManNotificationGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysClockChangedNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysReloadNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysSlaveSwitchSuccessNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysSlaveSwitchFailNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysIssuNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchInstallFail"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchInstallFailClear"),
        ("HUAWEI-SYS-MAN-MIB", "hwSumUpgradeSuccess"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysCfgFileErrorNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysImageErrorNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysPafChangeNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysLicenseChangeNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwSystemBoardExclude"),
        ("HUAWEI-SYS-MAN-MIB", "hwSystemBoardExcludeClear"),
        ("HUAWEI-SYS-MAN-MIB", "hwEvmVmAbnormalRunNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwEvmVmNotRunningNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwEvmVmAbnormalRestartNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwEvmDownloadFailedNotification"),
        ("HUAWEI-SYS-MAN-MIB", "hwEvmInstallFailedNotification"))
)
if mibBuilder.loadTexts:
    huaweiSystemManNotificationGroup.setStatus(
        "current"
    )

huaweiSystemHDNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 7)
)
huaweiSystemHDNotificationGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysMasterHDError"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysSlaveHDError"))
)
if mibBuilder.loadTexts:
    huaweiSystemHDNotificationGroup.setStatus(
        "current"
    )

hwPatchTrapsGrop = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 9)
)
hwPatchTrapsGrop.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwPatchErrorTrap"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchActiveOverTimeTrap"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchMalfunctionComebackTrap"),
        ("HUAWEI-SYS-MAN-MIB", "hwPatchUpdateTrap"))
)
if mibBuilder.loadTexts:
    hwPatchTrapsGrop.setStatus(
        "current"
    )

hwSystemCfcardNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 17)
)
hwSystemCfcardNotificationGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysMasterCfcardError"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysSlaveCfcardError"))
)
if mibBuilder.loadTexts:
    hwSystemCfcardNotificationGroup.setStatus(
        "current"
    )

hwSysWlanApUpgradeNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 2, 24)
)
hwSysWlanApUpgradeNotificationsGroup.setObjects(
      *(("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeBeginNotify"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeResultNotify"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeUbootNotMatchNotify"),
        ("HUAWEI-SYS-MAN-MIB", "hwSysWlanApUpgradeAssistantPackageNotMatchNotify"))
)
if mibBuilder.loadTexts:
    hwSysWlanApUpgradeNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

huaweiSystemManMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 19, 3, 1, 1)
)
if mibBuilder.loadTexts:
    huaweiSystemManMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SYS-MAN-MIB",
    **{"HWPatchErrorType": HWPatchErrorType,
       "huaweiSystemManMIB": huaweiSystemManMIB,
       "huaweiSystemManMIBObjects": huaweiSystemManMIBObjects,
       "hwSysClock": hwSysClock,
       "hwSysLocalClock": hwSysLocalClock,
       "hwSysCurrent": hwSysCurrent,
       "hwSysCurTable": hwSysCurTable,
       "hwSysCurEntry": hwSysCurEntry,
       "hwSysCurEntPhysicalIndex": hwSysCurEntPhysicalIndex,
       "hwSysCurCFGFileIndex": hwSysCurCFGFileIndex,
       "hwSysCurImageIndex": hwSysCurImageIndex,
       "hwSysCurPafFileIndex": hwSysCurPafFileIndex,
       "hwSysCurLicenseIndex": hwSysCurLicenseIndex,
       "hwSysCurPatchFileIndex": hwSysCurPatchFileIndex,
       "hwSysCurVoiceFileIndex": hwSysCurVoiceFileIndex,
       "hwSysReload": hwSysReload,
       "hwSysReloadSchedule": hwSysReloadSchedule,
       "hwSysReloadAction": hwSysReloadAction,
       "hwSysReloadScheduleTable": hwSysReloadScheduleTable,
       "hwSysReloadScheduleEntry": hwSysReloadScheduleEntry,
       "hwSysReloadScheduleIndex": hwSysReloadScheduleIndex,
       "hwSysReloadEntity": hwSysReloadEntity,
       "hwSysReloadCfgFile": hwSysReloadCfgFile,
       "hwSysReloadImage": hwSysReloadImage,
       "hwSysReloadReason": hwSysReloadReason,
       "hwSysReloadScheduleTime": hwSysReloadScheduleTime,
       "hwSysReloadRowStatus": hwSysReloadRowStatus,
       "hwSysReloadPafFile": hwSysReloadPafFile,
       "hwSysReloadLicenseFile": hwSysReloadLicenseFile,
       "hwSysReloadPatchFile": hwSysReloadPatchFile,
       "hwSysReloadPatchState": hwSysReloadPatchState,
       "hwSysReloadOperateDestType": hwSysReloadOperateDestType,
       "hwSysReloadOperateDestIndex": hwSysReloadOperateDestIndex,
       "hwSysReloadVoiceFile": hwSysReloadVoiceFile,
       "hwSysReloadAndroidFile": hwSysReloadAndroidFile,
       "hwSysReboot": hwSysReboot,
       "hwSysSlaveSwitchEnable": hwSysSlaveSwitchEnable,
       "hwSysLatestRebootErrorInfo": hwSysLatestRebootErrorInfo,
       "hwSysSlaveSwitchTable": hwSysSlaveSwitchTable,
       "hwSysSlaveSwitchEntry": hwSysSlaveSwitchEntry,
       "hwSysSlaveSwitchIndex": hwSysSlaveSwitchIndex,
       "hwSysSlaveSwitchChassisNum": hwSysSlaveSwitchChassisNum,
       "hwSysSlaveSwitchOperType": hwSysSlaveSwitchOperType,
       "hwSysSlaveSwitchEnableStatus": hwSysSlaveSwitchEnableStatus,
       "hwSysSlaveSwitchSrc": hwSysSlaveSwitchSrc,
       "hwSysSlaveSwitchDst": hwSysSlaveSwitchDst,
       "hwSysDelayReboot": hwSysDelayReboot,
       "hwSysImage": hwSysImage,
       "hwSysImageNum": hwSysImageNum,
       "hwSysImageTable": hwSysImageTable,
       "hwSysImageEntry": hwSysImageEntry,
       "hwSysImageIndex": hwSysImageIndex,
       "hwSysImageName": hwSysImageName,
       "hwSysImageSize": hwSysImageSize,
       "hwSysImageLocation": hwSysImageLocation,
       "hwSysImageVersion": hwSysImageVersion,
       "hwSysImageReason": hwSysImageReason,
       "hwSysCFGFile": hwSysCFGFile,
       "hwSysCFGFileNum": hwSysCFGFileNum,
       "hwSysCFGFileTable": hwSysCFGFileTable,
       "hwSysCFGFileEntry": hwSysCFGFileEntry,
       "hwSysCFGFileIndex": hwSysCFGFileIndex,
       "hwSysCFGFileName": hwSysCFGFileName,
       "hwSysCFGFileSize": hwSysCFGFileSize,
       "hwSysCFGFileLocation": hwSysCFGFileLocation,
       "hwSysCFGFileReason": hwSysCFGFileReason,
       "hwSysPafFile": hwSysPafFile,
       "hwSysPafFileNum": hwSysPafFileNum,
       "hwSysPafFileTable": hwSysPafFileTable,
       "hwSysPafFileEntry": hwSysPafFileEntry,
       "hwSysPafFileIndex": hwSysPafFileIndex,
       "hwSysPafFileName": hwSysPafFileName,
       "hwSysPafFileSize": hwSysPafFileSize,
       "hwSysPafFileLocation": hwSysPafFileLocation,
       "hwSysPafFileVersion": hwSysPafFileVersion,
       "hwSysLicenseFile": hwSysLicenseFile,
       "hwSysLicenseFileNum": hwSysLicenseFileNum,
       "hwSysLicenseFileTable": hwSysLicenseFileTable,
       "hwSysLicenseFileEntry": hwSysLicenseFileEntry,
       "hwSysLicenseFileIndex": hwSysLicenseFileIndex,
       "hwSysLicenseFileName": hwSysLicenseFileName,
       "hwSysLicenseFileSize": hwSysLicenseFileSize,
       "hwSysLicenseFileLocation": hwSysLicenseFileLocation,
       "hwPatch": hwPatch,
       "hwPatchBase": hwPatchBase,
       "hwPatchFileNum": hwPatchFileNum,
       "hwPatchRecordReset": hwPatchRecordReset,
       "hwPatchHistoryTableMax": hwPatchHistoryTableMax,
       "hwPatchTrapEnble": hwPatchTrapEnble,
       "hwPatchErrorTableMax": hwPatchErrorTableMax,
       "hwPatchId": hwPatchId,
       "hwPatchLatestId": hwPatchLatestId,
       "hwPatchFailReason": hwPatchFailReason,
       "hwPatchFileTable": hwPatchFileTable,
       "hwPatchFileEntry": hwPatchFileEntry,
       "hwPatchFileIndex": hwPatchFileIndex,
       "hwPatchFileName": hwPatchFileName,
       "hwPatchFileSize": hwPatchFileSize,
       "hwPatchFileLocation": hwPatchFileLocation,
       "hwPatchFileVersion": hwPatchFileVersion,
       "hwLoadPatchTable": hwLoadPatchTable,
       "hwLoadPatchEntry": hwLoadPatchEntry,
       "hwPatchLoadDestType": hwPatchLoadDestType,
       "hwPatchLoadDestIndex": hwPatchLoadDestIndex,
       "hwPatchLoadState": hwPatchLoadState,
       "hwLoadPatchRowState": hwLoadPatchRowState,
       "hwPatchInfo": hwPatchInfo,
       "hwPatchTable": hwPatchTable,
       "hwPatchEntry": hwPatchEntry,
       "hwPatchSlotIndex": hwPatchSlotIndex,
       "hwPatchIndex": hwPatchIndex,
       "hwPatchUsedFileName": hwPatchUsedFileName,
       "hwPatchVersion": hwPatchVersion,
       "hwPatchDescription": hwPatchDescription,
       "hwPatchProgramVersion": hwPatchProgramVersion,
       "hwPatchFuncNum": hwPatchFuncNum,
       "hwPatchTextLen": hwPatchTextLen,
       "hwPatchDataLen": hwPatchDataLen,
       "hwPatchType": hwPatchType,
       "hwPatchBuildTime": hwPatchBuildTime,
       "hwPatchActiveTime": hwPatchActiveTime,
       "hwPatchAdminStatus": hwPatchAdminStatus,
       "hwPatchOperateState": hwPatchOperateState,
       "hwPatchOperateDestType": hwPatchOperateDestType,
       "hwPatchOperateDestIndex": hwPatchOperateDestIndex,
       "hwPatchStateTable": hwPatchStateTable,
       "hwPatchStateEntry": hwPatchStateEntry,
       "hwPatchNumMax": hwPatchNumMax,
       "hwPatchIdleNum": hwPatchIdleNum,
       "hwPatchTextMax": hwPatchTextMax,
       "hwPatchDataMax": hwPatchDataMax,
       "hwPatchStateTextUsed": hwPatchStateTextUsed,
       "hwPatchStateDataUsed": hwPatchStateDataUsed,
       "hwPatchStateTotalPatchNum": hwPatchStateTotalPatchNum,
       "hwPatchStateTempPatchNum": hwPatchStateTempPatchNum,
       "hwPatchStateCommonPatchNum": hwPatchStateCommonPatchNum,
       "hwPatchStateRuningPatchNum": hwPatchStateRuningPatchNum,
       "hwPatchStateActivePatchNum": hwPatchStateActivePatchNum,
       "hwPatchStateDeactivePatchNum": hwPatchStateDeactivePatchNum,
       "hwPatchHistoryTable": hwPatchHistoryTable,
       "hwPatchHistoryEntry": hwPatchHistoryEntry,
       "hwPatchHistoryIndex": hwPatchHistoryIndex,
       "hwPatchHistoryProgrameVersion": hwPatchHistoryProgrameVersion,
       "hwPatchHistoryVersion": hwPatchHistoryVersion,
       "hwSlotId": hwSlotId,
       "hwPatchBeginIndex": hwPatchBeginIndex,
       "hwPatchEndIndex": hwPatchEndIndex,
       "hwPatchHistoryAction": hwPatchHistoryAction,
       "hwPatchHistoryBeginTime": hwPatchHistoryBeginTime,
       "hwPatchHistoryEndTime": hwPatchHistoryEndTime,
       "hwPatchErrorTable": hwPatchErrorTable,
       "hwPatchErrorEntry": hwPatchErrorEntry,
       "hwPatchErrorIndex": hwPatchErrorIndex,
       "hwPatchErrorSlot": hwPatchErrorSlot,
       "hwPatchErrorPatchFileName": hwPatchErrorPatchFileName,
       "hwPatchErrorPatchIndex": hwPatchErrorPatchIndex,
       "hwPatchErrorCode": hwPatchErrorCode,
       "hwBootRom": hwBootRom,
       "hwBootRomTable": hwBootRomTable,
       "hwBootRomEntry": hwBootRomEntry,
       "hwBootRomIndex": hwBootRomIndex,
       "hwBootRomBootDevice": hwBootRomBootDevice,
       "hwBootRomProcessorNo": hwBootRomProcessorNo,
       "hwBootRomHostName": hwBootRomHostName,
       "hwBootRomFileName": hwBootRomFileName,
       "hwBootRomIpOnEthernet": hwBootRomIpOnEthernet,
       "hwBootRomIpOnBackPlane": hwBootRomIpOnBackPlane,
       "hwBootRomHostIp": hwBootRomHostIp,
       "hwBootRomGatewayIp": hwBootRomGatewayIp,
       "hwBootRomUserName": hwBootRomUserName,
       "hwBootRomPassword": hwBootRomPassword,
       "hwBootRomTargetName": hwBootRomTargetName,
       "hwBootRomStartupScript": hwBootRomStartupScript,
       "hwBootRomXModemBaudRate": hwBootRomXModemBaudRate,
       "hwBootRomVersion": hwBootRomVersion,
       "hwSysUpgrade": hwSysUpgrade,
       "hwSysUpgradeTable": hwSysUpgradeTable,
       "hwSysUpgradeEntry": hwSysUpgradeEntry,
       "hwIssuIndex": hwIssuIndex,
       "hwIssuMode": hwIssuMode,
       "hwIssuImageFile": hwIssuImageFile,
       "hwIssuPafFile": hwIssuPafFile,
       "hwIssuLicenseFile": hwIssuLicenseFile,
       "hwIssuPatchFile": hwIssuPatchFile,
       "hwIssuState": hwIssuState,
       "hwIssuConditionCheck": hwIssuConditionCheck,
       "hwSysSourceIndex": hwSysSourceIndex,
       "hwSysSourceIndexTable": hwSysSourceIndexTable,
       "hwSysSourceIndexEntry": hwSysSourceIndexEntry,
       "hwSysFileType": hwSysFileType,
       "hwSysFileName": hwSysFileName,
       "hwSysFileIndex": hwSysFileIndex,
       "hwSysRebootInfo": hwSysRebootInfo,
       "hwSysRebootTimes": hwSysRebootTimes,
       "hwSysRebootRecordTable": hwSysRebootRecordTable,
       "hwSysRebootRecordEntry": hwSysRebootRecordEntry,
       "hwSysRebootRecordIndex": hwSysRebootRecordIndex,
       "hwSysRebootReason": hwSysRebootReason,
       "hwSysRebootTime": hwSysRebootTime,
       "hwSysDeviceCheck": hwSysDeviceCheck,
       "hwSysDeviceCheckStart": hwSysDeviceCheckStart,
       "hwSysDeviceCheckState": hwSysDeviceCheckState,
       "hwSysSwitchoverState": hwSysSwitchoverState,
       "hwSysSwitchoverStateTable": hwSysSwitchoverStateTable,
       "hwSysSwitchoverStateEntry": hwSysSwitchoverStateEntry,
       "hwSysSwitchoverStateIndex": hwSysSwitchoverStateIndex,
       "hwSysSwitchoverSlotId": hwSysSwitchoverSlotId,
       "hwSysSwitchoverBoardType": hwSysSwitchoverBoardType,
       "hwSysSwitchoverInfo": hwSysSwitchoverInfo,
       "hwSysSwitchoverStateMultiTable": hwSysSwitchoverStateMultiTable,
       "hwSysSwitchoverStateMultiEntry": hwSysSwitchoverStateMultiEntry,
       "hwSysMultiSwtStateIndex": hwSysMultiSwtStateIndex,
       "hwSysMultiSwtChassisId": hwSysMultiSwtChassisId,
       "hwSysMultiSwtSlotId": hwSysMultiSwtSlotId,
       "hwSysMultiSwtBoardType": hwSysMultiSwtBoardType,
       "hwSysMultiSwtInfo": hwSysMultiSwtInfo,
       "hwSysVoiceFile": hwSysVoiceFile,
       "hwSysVoiceFileNum": hwSysVoiceFileNum,
       "hwSysVoiceFileTable": hwSysVoiceFileTable,
       "hwSysVoiceFileEntry": hwSysVoiceFileEntry,
       "hwSysVoiceFileIndex": hwSysVoiceFileIndex,
       "hwSysVoiceFileName": hwSysVoiceFileName,
       "hwSysVoiceFileSize": hwSysVoiceFileSize,
       "hwSysVoiceFileLocation": hwSysVoiceFileLocation,
       "hwSysWlanApUpgrade": hwSysWlanApUpgrade,
       "hwSysWlanApUpgradeCmd": hwSysWlanApUpgradeCmd,
       "hwSysWlanApUpgradeMode": hwSysWlanApUpgradeMode,
       "hwSysWlanApUpgradeFileName": hwSysWlanApUpgradeFileName,
       "hwSysWlanApUpgradeServerIp": hwSysWlanApUpgradeServerIp,
       "hwSysWlanApUpgradeServerUserName": hwSysWlanApUpgradeServerUserName,
       "hwSysWlanApUpgradeServerPassword": hwSysWlanApUpgradeServerPassword,
       "hwSysWlanApUpgradeStatus": hwSysWlanApUpgradeStatus,
       "hwSysWlanApUpgradeProgressStatus": hwSysWlanApUpgradeProgressStatus,
       "hwSysWlanApUpgradeLoadProgress": hwSysWlanApUpgradeLoadProgress,
       "hwSysWlanApUpgradeStorageProgress": hwSysWlanApUpgradeStorageProgress,
       "hwSysWlanApUpgradeNotifications": hwSysWlanApUpgradeNotifications,
       "hwSysWlanApUpgradeBeginNotify": hwSysWlanApUpgradeBeginNotify,
       "hwSysWlanApUpgradeResultNotify": hwSysWlanApUpgradeResultNotify,
       "hwSysWlanApUpgradeUbootNotMatchNotify": hwSysWlanApUpgradeUbootNotMatchNotify,
       "hwSysWlanApUpgradeAssistantPackageNotMatchNotify": hwSysWlanApUpgradeAssistantPackageNotMatchNotify,
       "hwSysAndroidFile": hwSysAndroidFile,
       "hwSysAndroidFileNum": hwSysAndroidFileNum,
       "hwSysAndroidFileTable": hwSysAndroidFileTable,
       "hwSysAndroidFileEntry": hwSysAndroidFileEntry,
       "hwSysAndroidFileIndex": hwSysAndroidFileIndex,
       "hwSysAndroidFileName": hwSysAndroidFileName,
       "hwSysAndroidFileSize": hwSysAndroidFileSize,
       "hwSysAndroidFileLocation": hwSysAndroidFileLocation,
       "hwSysAndroidFileReason": hwSysAndroidFileReason,
       "huaweiSystemManMIBNotifications": huaweiSystemManMIBNotifications,
       "hwSysClockChangedNotification": hwSysClockChangedNotification,
       "hwSysReloadNotification": hwSysReloadNotification,
       "hwSysMasterHDError": hwSysMasterHDError,
       "hwSysSlaveHDError": hwSysSlaveHDError,
       "hwPatchTrap": hwPatchTrap,
       "hwPatchErrorTrap": hwPatchErrorTrap,
       "hwPatchActiveOverTimeTrap": hwPatchActiveOverTimeTrap,
       "hwPatchMalfunctionComebackTrap": hwPatchMalfunctionComebackTrap,
       "hwPatchUpdateTrap": hwPatchUpdateTrap,
       "hwSysMasterCfcardError": hwSysMasterCfcardError,
       "hwSysSlaveCfcardError": hwSysSlaveCfcardError,
       "hwSysSlaveSwitchSuccessNotification": hwSysSlaveSwitchSuccessNotification,
       "hwSysSlaveSwitchFailNotification": hwSysSlaveSwitchFailNotification,
       "hwSysIssuNotification": hwSysIssuNotification,
       "hwPatchInstallFail": hwPatchInstallFail,
       "hwPatchInstallFailClear": hwPatchInstallFailClear,
       "hwSumUpgradeSuccess": hwSumUpgradeSuccess,
       "hwSysCfgFileErrorNotification": hwSysCfgFileErrorNotification,
       "hwSysImageErrorNotification": hwSysImageErrorNotification,
       "hwSysPafChangeNotification": hwSysPafChangeNotification,
       "hwSysLicenseChangeNotification": hwSysLicenseChangeNotification,
       "hwSystemBoardExclude": hwSystemBoardExclude,
       "hwSystemBoardExcludeClear": hwSystemBoardExcludeClear,
       "hwSysEvmTraps": hwSysEvmTraps,
       "hwSysEvmTrapsObject": hwSysEvmTrapsObject,
       "hwSysEvmRoleName": hwSysEvmRoleName,
       "hwSysEvmDownloadFileName": hwSysEvmDownloadFileName,
       "hwSysEvmInstallFileName": hwSysEvmInstallFileName,
       "hwSysEvmNotifications": hwSysEvmNotifications,
       "hwEvmVmAbnormalRunNotification": hwEvmVmAbnormalRunNotification,
       "hwEvmVmNotRunningNotification": hwEvmVmNotRunningNotification,
       "hwEvmVmAbnormalRestartNotification": hwEvmVmAbnormalRestartNotification,
       "hwEvmDownloadFailedNotification": hwEvmDownloadFailedNotification,
       "hwEvmInstallFailedNotification": hwEvmInstallFailedNotification,
       "huaweiSystemManMIBConformance": huaweiSystemManMIBConformance,
       "huaweiSystemManMIBCompliances": huaweiSystemManMIBCompliances,
       "huaweiSystemManMIBCompliance": huaweiSystemManMIBCompliance,
       "huaweiSystemManMIBGroups": huaweiSystemManMIBGroups,
       "huaweiSysClockGroup": huaweiSysClockGroup,
       "huaweiSysReloadGroup": huaweiSysReloadGroup,
       "huaweiSysImageGroup": huaweiSysImageGroup,
       "huaweiSysCFGFileGroup": huaweiSysCFGFileGroup,
       "hwSysCurGroup": hwSysCurGroup,
       "huaweiSystemManNotificationGroup": huaweiSystemManNotificationGroup,
       "huaweiSystemHDNotificationGroup": huaweiSystemHDNotificationGroup,
       "hwPatchLoadGroup": hwPatchLoadGroup,
       "hwPatchTrapsGrop": hwPatchTrapsGrop,
       "hwPatchInfoGroup": hwPatchInfoGroup,
       "hwPatchFileGroup": hwPatchFileGroup,
       "hwSysPafFileGroup": hwSysPafFileGroup,
       "hwSysPafLicenseGroup": hwSysPafLicenseGroup,
       "hwSysRebootAndSwitchGrop": hwSysRebootAndSwitchGrop,
       "hwBootRomGroup": hwBootRomGroup,
       "hwSystemCfcardNotificationGroup": hwSystemCfcardNotificationGroup,
       "hwSysUpgradeGroup": hwSysUpgradeGroup,
       "hwSysRebootInfoGroup": hwSysRebootInfoGroup,
       "hwSysDeviceCheckGroup": hwSysDeviceCheckGroup,
       "huaweiSysVoiceFileGroup": huaweiSysVoiceFileGroup,
       "hwSysWlanApUpgradeCmdGroup": hwSysWlanApUpgradeCmdGroup,
       "hwSysWlanApUpgradeStatusGroup": hwSysWlanApUpgradeStatusGroup,
       "hwSysWlanApUpgradeNotificationsGroup": hwSysWlanApUpgradeNotificationsGroup,
       "huaweiSysAndroidFileGroup": huaweiSysAndroidFileGroup,
       "huaweihwSysEvmTrapsObjectGroup": huaweihwSysEvmTrapsObjectGroup}
)
