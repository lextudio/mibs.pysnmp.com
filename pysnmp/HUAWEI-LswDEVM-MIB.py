# SNMP MIB module (HUAWEI-LswDEVM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LswDEVM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:39 2024
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

(huaweiUtility,
 lswCommon) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "huaweiUtility",
    "lswCommon")

(hwLswFrameIndex,
 hwLswSlotIndex) = mibBuilder.importSymbols(
    "HUAWEI-LSW-DEV-ADM-MIB",
    "hwLswFrameIndex",
    "hwLswSlotIndex")

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


# MODULE-IDENTITY

hwLswdevMMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9)
)
hwLswdevMMib.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwLswdevMMibObject_ObjectIdentity = ObjectIdentity
hwLswdevMMibObject = _HwLswdevMMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hwLswdevMMibObject.setStatus("current")
_HwdevMFanStatusTable_Object = MibTable
hwdevMFanStatusTable = _HwdevMFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    hwdevMFanStatusTable.setStatus("current")
_HwdevMFanStatusEntry_Object = MibTableRow
hwdevMFanStatusEntry = _HwdevMFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 1, 1)
)
hwdevMFanStatusEntry.setIndexNames(
    (0, "HUAWEI-LswDEVM-MIB", "hwDevMFanNum"),
)
if mibBuilder.loadTexts:
    hwdevMFanStatusEntry.setStatus("current")
_HwDevMFanNum_Type = Integer32
_HwDevMFanNum_Object = MibTableColumn
hwDevMFanNum = _HwDevMFanNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 1, 1, 1),
    _HwDevMFanNum_Type()
)
hwDevMFanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDevMFanNum.setStatus("current")


class _HwDevMFanStatus_Type(Integer32):
    """Custom type hwDevMFanStatus based on Integer32"""
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
        *(("active", 1),
          ("deactive", 2),
          ("not-install", 3),
          ("unsupport", 4))
    )


_HwDevMFanStatus_Type.__name__ = "Integer32"
_HwDevMFanStatus_Object = MibTableColumn
hwDevMFanStatus = _HwDevMFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 1, 1, 2),
    _HwDevMFanStatus_Type()
)
hwDevMFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDevMFanStatus.setStatus("current")
_HwdevMPowerStatusTable_Object = MibTable
hwdevMPowerStatusTable = _HwdevMPowerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    hwdevMPowerStatusTable.setStatus("current")
_HwdevMPowerStatusEntry_Object = MibTableRow
hwdevMPowerStatusEntry = _HwdevMPowerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 2, 1)
)
hwdevMPowerStatusEntry.setIndexNames(
    (0, "HUAWEI-LswDEVM-MIB", "hwDevMPowerNum"),
)
if mibBuilder.loadTexts:
    hwdevMPowerStatusEntry.setStatus("current")
_HwDevMPowerNum_Type = Integer32
_HwDevMPowerNum_Object = MibTableColumn
hwDevMPowerNum = _HwDevMPowerNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 2, 1, 1),
    _HwDevMPowerNum_Type()
)
hwDevMPowerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDevMPowerNum.setStatus("current")


class _HwDevMPowerStatus_Type(Integer32):
    """Custom type hwDevMPowerStatus based on Integer32"""
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
        *(("active", 1),
          ("deactive", 2),
          ("not-install", 3),
          ("unsupport", 4))
    )


_HwDevMPowerStatus_Type.__name__ = "Integer32"
_HwDevMPowerStatus_Object = MibTableColumn
hwDevMPowerStatus = _HwDevMPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 2, 1, 2),
    _HwDevMPowerStatus_Type()
)
hwDevMPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDevMPowerStatus.setStatus("current")
_HwdevMSlotEnvironmentTable_Object = MibTable
hwdevMSlotEnvironmentTable = _HwdevMSlotEnvironmentTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    hwdevMSlotEnvironmentTable.setStatus("current")
_HwdevMSlotEnvironmentEntry_Object = MibTableRow
hwdevMSlotEnvironmentEntry = _HwdevMSlotEnvironmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 3, 1)
)
hwdevMSlotEnvironmentEntry.setIndexNames(
    (0, "HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
    (0, "HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
    (0, "HUAWEI-LswDEVM-MIB", "hwdevMSlotEnvironmentType"),
)
if mibBuilder.loadTexts:
    hwdevMSlotEnvironmentEntry.setStatus("current")


class _HwdevMSlotEnvironmentType_Type(Integer32):
    """Custom type hwdevMSlotEnvironmentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fog", 3),
          ("humidity", 2),
          ("temperature", 1))
    )


_HwdevMSlotEnvironmentType_Type.__name__ = "Integer32"
_HwdevMSlotEnvironmentType_Object = MibTableColumn
hwdevMSlotEnvironmentType = _HwdevMSlotEnvironmentType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 3, 1, 1),
    _HwdevMSlotEnvironmentType_Type()
)
hwdevMSlotEnvironmentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwdevMSlotEnvironmentType.setStatus("current")


class _HwDevMSlotEnvironmentStatus_Type(Integer32):
    """Custom type hwDevMSlotEnvironmentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lower", 3),
          ("normal", 1),
          ("upper", 2))
    )


_HwDevMSlotEnvironmentStatus_Type.__name__ = "Integer32"
_HwDevMSlotEnvironmentStatus_Object = MibTableColumn
hwDevMSlotEnvironmentStatus = _HwDevMSlotEnvironmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 3, 1, 2),
    _HwDevMSlotEnvironmentStatus_Type()
)
hwDevMSlotEnvironmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDevMSlotEnvironmentStatus.setStatus("current")
_HwDevMSlotEnvironmentValue_Type = Integer32
_HwDevMSlotEnvironmentValue_Object = MibTableColumn
hwDevMSlotEnvironmentValue = _HwDevMSlotEnvironmentValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 3, 1, 3),
    _HwDevMSlotEnvironmentValue_Type()
)
hwDevMSlotEnvironmentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDevMSlotEnvironmentValue.setStatus("current")
_HwDevMSlotEnvironmentUpperLimit_Type = Integer32
_HwDevMSlotEnvironmentUpperLimit_Object = MibTableColumn
hwDevMSlotEnvironmentUpperLimit = _HwDevMSlotEnvironmentUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 3, 1, 4),
    _HwDevMSlotEnvironmentUpperLimit_Type()
)
hwDevMSlotEnvironmentUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDevMSlotEnvironmentUpperLimit.setStatus("current")
_HwDevMSlotEnvironmentLowerLimit_Type = Integer32
_HwDevMSlotEnvironmentLowerLimit_Object = MibTableColumn
hwDevMSlotEnvironmentLowerLimit = _HwDevMSlotEnvironmentLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 3, 1, 5),
    _HwDevMSlotEnvironmentLowerLimit_Type()
)
hwDevMSlotEnvironmentLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDevMSlotEnvironmentLowerLimit.setStatus("current")


class _HwLinkUpDownTrapEnable_Type(Integer32):
    """Custom type hwLinkUpDownTrapEnable based on Integer32"""
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
        *(("disableBoth", 2),
          ("enableBoth", 1),
          ("enableLinkDownTrapOnly", 4),
          ("enableLinkUpTrapOnly", 3))
    )


_HwLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_HwLinkUpDownTrapEnable_Object = MibScalar
hwLinkUpDownTrapEnable = _HwLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 9),
    _HwLinkUpDownTrapEnable_Type()
)
hwLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLinkUpDownTrapEnable.setStatus("current")


class _Hwdot1qTpFdbLearnStatus_Type(Integer32):
    """Custom type hwdot1qTpFdbLearnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Hwdot1qTpFdbLearnStatus_Type.__name__ = "Integer32"
_Hwdot1qTpFdbLearnStatus_Object = MibScalar
hwdot1qTpFdbLearnStatus = _Hwdot1qTpFdbLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 10),
    _Hwdot1qTpFdbLearnStatus_Type()
)
hwdot1qTpFdbLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qTpFdbLearnStatus.setStatus("current")


class _HwCfmWriteFlash_Type(Integer32):
    """Custom type hwCfmWriteFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("write", 1)
    )


_HwCfmWriteFlash_Type.__name__ = "Integer32"
_HwCfmWriteFlash_Object = MibScalar
hwCfmWriteFlash = _HwCfmWriteFlash_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 11),
    _HwCfmWriteFlash_Type()
)
hwCfmWriteFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCfmWriteFlash.setStatus("current")


class _HwCfmEraseFlash_Type(Integer32):
    """Custom type hwCfmEraseFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("erase", 1)
    )


_HwCfmEraseFlash_Type.__name__ = "Integer32"
_HwCfmEraseFlash_Object = MibScalar
hwCfmEraseFlash = _HwCfmEraseFlash_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 9, 1, 12),
    _HwCfmEraseFlash_Type()
)
hwCfmEraseFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCfmEraseFlash.setStatus("current")
_HwDevice_ObjectIdentity = ObjectIdentity
hwDevice = _HwDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1)
)
_HwCpuTable_Object = MibTable
hwCpuTable = _HwCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hwCpuTable.setStatus("current")
_HwCpuEntry_Object = MibTableRow
hwCpuEntry = _HwCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 1, 1)
)
hwCpuEntry.setIndexNames(
    (0, "HUAWEI-LswDEVM-MIB", "hwCpuIndex"),
)
if mibBuilder.loadTexts:
    hwCpuEntry.setStatus("current")
_HwCpuIndex_Type = Integer32
_HwCpuIndex_Object = MibTableColumn
hwCpuIndex = _HwCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 1, 1, 1),
    _HwCpuIndex_Type()
)
hwCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCpuIndex.setStatus("current")
_HwCpuCostRate_Type = Gauge32
_HwCpuCostRate_Object = MibTableColumn
hwCpuCostRate = _HwCpuCostRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 1, 1, 2),
    _HwCpuCostRate_Type()
)
hwCpuCostRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCpuCostRate.setStatus("current")
_HwCpuCostRatePer1Min_Type = Gauge32
_HwCpuCostRatePer1Min_Object = MibTableColumn
hwCpuCostRatePer1Min = _HwCpuCostRatePer1Min_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 1, 1, 3),
    _HwCpuCostRatePer1Min_Type()
)
hwCpuCostRatePer1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCpuCostRatePer1Min.setStatus("current")
_HwCpuCostRatePer5Min_Type = Gauge32
_HwCpuCostRatePer5Min_Object = MibTableColumn
hwCpuCostRatePer5Min = _HwCpuCostRatePer5Min_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 1, 1, 4),
    _HwCpuCostRatePer5Min_Type()
)
hwCpuCostRatePer5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCpuCostRatePer5Min.setStatus("current")
_HwMem_ObjectIdentity = ObjectIdentity
hwMem = _HwMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2)
)
_HwMemTable_Object = MibTable
hwMemTable = _HwMemTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwMemTable.setStatus("current")
_HwMemEntry_Object = MibTableRow
hwMemEntry = _HwMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 1, 1)
)
hwMemEntry.setIndexNames(
    (0, "HUAWEI-LswDEVM-MIB", "hwMemModuleIndex"),
)
if mibBuilder.loadTexts:
    hwMemEntry.setStatus("current")
_HwMemModuleIndex_Type = Integer32
_HwMemModuleIndex_Object = MibTableColumn
hwMemModuleIndex = _HwMemModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 1, 1, 1),
    _HwMemModuleIndex_Type()
)
hwMemModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMemModuleIndex.setStatus("current")
_HwMemSize_Type = Gauge32
_HwMemSize_Object = MibTableColumn
hwMemSize = _HwMemSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 1, 1, 2),
    _HwMemSize_Type()
)
hwMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemSize.setStatus("current")
_HwMemFree_Type = Gauge32
_HwMemFree_Object = MibTableColumn
hwMemFree = _HwMemFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 1, 1, 3),
    _HwMemFree_Type()
)
hwMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemFree.setStatus("current")
_HwMemRawSliceUsed_Type = Gauge32
_HwMemRawSliceUsed_Object = MibTableColumn
hwMemRawSliceUsed = _HwMemRawSliceUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 1, 1, 4),
    _HwMemRawSliceUsed_Type()
)
hwMemRawSliceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemRawSliceUsed.setStatus("current")
_HwMemLgFree_Type = Gauge32
_HwMemLgFree_Object = MibTableColumn
hwMemLgFree = _HwMemLgFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 1, 1, 5),
    _HwMemLgFree_Type()
)
hwMemLgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemLgFree.setStatus("current")
_HwMemFail_Type = Gauge32
_HwMemFail_Object = MibTableColumn
hwMemFail = _HwMemFail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 1, 1, 6),
    _HwMemFail_Type()
)
hwMemFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemFail.setStatus("current")
_HwMemFailNoMem_Type = Gauge32
_HwMemFailNoMem_Object = MibTableColumn
hwMemFailNoMem = _HwMemFailNoMem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 1, 1, 7),
    _HwMemFailNoMem_Type()
)
hwMemFailNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemFailNoMem.setStatus("current")
_HwBufTable_Object = MibTable
hwBufTable = _HwBufTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwBufTable.setStatus("current")
_HwBufEntry_Object = MibTableRow
hwBufEntry = _HwBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 2, 1)
)
hwBufEntry.setIndexNames(
    (0, "HUAWEI-LswDEVM-MIB", "hwBufModuleIndex"),
    (0, "HUAWEI-LswDEVM-MIB", "hwBufSize"),
)
if mibBuilder.loadTexts:
    hwBufEntry.setStatus("current")
_HwBufModuleIndex_Type = Integer32
_HwBufModuleIndex_Object = MibTableColumn
hwBufModuleIndex = _HwBufModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 2, 1, 1),
    _HwBufModuleIndex_Type()
)
hwBufModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBufModuleIndex.setStatus("current")
_HwBufSize_Type = Integer32
_HwBufSize_Object = MibTableColumn
hwBufSize = _HwBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 2, 1, 2),
    _HwBufSize_Type()
)
hwBufSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBufSize.setStatus("current")
_HwBufCurrentTotal_Type = Gauge32
_HwBufCurrentTotal_Object = MibTableColumn
hwBufCurrentTotal = _HwBufCurrentTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 2, 1, 3),
    _HwBufCurrentTotal_Type()
)
hwBufCurrentTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBufCurrentTotal.setStatus("current")
_HwBufCurrentUsed_Type = Gauge32
_HwBufCurrentUsed_Object = MibTableColumn
hwBufCurrentUsed = _HwBufCurrentUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 2, 2, 1, 4),
    _HwBufCurrentUsed_Type()
)
hwBufCurrentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBufCurrentUsed.setStatus("current")
_HwFlh_ObjectIdentity = ObjectIdentity
hwFlh = _HwFlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 3)
)
_HwFlhTotalSize_Type = Integer32
_HwFlhTotalSize_Object = MibScalar
hwFlhTotalSize = _HwFlhTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 3, 1),
    _HwFlhTotalSize_Type()
)
hwFlhTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhTotalSize.setStatus("current")
_HwFlhTotalFree_Type = Integer32
_HwFlhTotalFree_Object = MibScalar
hwFlhTotalFree = _HwFlhTotalFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 3, 2),
    _HwFlhTotalFree_Type()
)
hwFlhTotalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhTotalFree.setStatus("current")


class _HwFlhLastDelTime_Type(TimeTicks):
    """Custom type hwFlhLastDelTime based on TimeTicks"""
    defaultValue = 0


_HwFlhLastDelTime_Object = MibScalar
hwFlhLastDelTime = _HwFlhLastDelTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 3, 3),
    _HwFlhLastDelTime_Type()
)
hwFlhLastDelTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhLastDelTime.setStatus("current")


class _HwFlhDelState_Type(Integer32):
    """Custom type hwFlhDelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("blockMallocFail", 6),
          ("error", 3),
          ("executing", 1),
          ("failtoopen", 5),
          ("noneDelOperationSinceStart", 7),
          ("ok", 2),
          ("readOnly", 4))
    )


_HwFlhDelState_Type.__name__ = "Integer32"
_HwFlhDelState_Object = MibScalar
hwFlhDelState = _HwFlhDelState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 3, 4),
    _HwFlhDelState_Type()
)
hwFlhDelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhDelState.setStatus("current")


class _HwFlhState_Type(Integer32):
    """Custom type hwFlhState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("free", 2))
    )


_HwFlhState_Type.__name__ = "Integer32"
_HwFlhState_Object = MibScalar
hwFlhState = _HwFlhState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 1, 3, 5),
    _HwFlhState_Type()
)
hwFlhState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlhState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LswDEVM-MIB",
    **{"hwLswdevMMib": hwLswdevMMib,
       "hwLswdevMMibObject": hwLswdevMMibObject,
       "hwdevMFanStatusTable": hwdevMFanStatusTable,
       "hwdevMFanStatusEntry": hwdevMFanStatusEntry,
       "hwDevMFanNum": hwDevMFanNum,
       "hwDevMFanStatus": hwDevMFanStatus,
       "hwdevMPowerStatusTable": hwdevMPowerStatusTable,
       "hwdevMPowerStatusEntry": hwdevMPowerStatusEntry,
       "hwDevMPowerNum": hwDevMPowerNum,
       "hwDevMPowerStatus": hwDevMPowerStatus,
       "hwdevMSlotEnvironmentTable": hwdevMSlotEnvironmentTable,
       "hwdevMSlotEnvironmentEntry": hwdevMSlotEnvironmentEntry,
       "hwdevMSlotEnvironmentType": hwdevMSlotEnvironmentType,
       "hwDevMSlotEnvironmentStatus": hwDevMSlotEnvironmentStatus,
       "hwDevMSlotEnvironmentValue": hwDevMSlotEnvironmentValue,
       "hwDevMSlotEnvironmentUpperLimit": hwDevMSlotEnvironmentUpperLimit,
       "hwDevMSlotEnvironmentLowerLimit": hwDevMSlotEnvironmentLowerLimit,
       "hwLinkUpDownTrapEnable": hwLinkUpDownTrapEnable,
       "hwdot1qTpFdbLearnStatus": hwdot1qTpFdbLearnStatus,
       "hwCfmWriteFlash": hwCfmWriteFlash,
       "hwCfmEraseFlash": hwCfmEraseFlash,
       "hwDevice": hwDevice,
       "hwCpuTable": hwCpuTable,
       "hwCpuEntry": hwCpuEntry,
       "hwCpuIndex": hwCpuIndex,
       "hwCpuCostRate": hwCpuCostRate,
       "hwCpuCostRatePer1Min": hwCpuCostRatePer1Min,
       "hwCpuCostRatePer5Min": hwCpuCostRatePer5Min,
       "hwMem": hwMem,
       "hwMemTable": hwMemTable,
       "hwMemEntry": hwMemEntry,
       "hwMemModuleIndex": hwMemModuleIndex,
       "hwMemSize": hwMemSize,
       "hwMemFree": hwMemFree,
       "hwMemRawSliceUsed": hwMemRawSliceUsed,
       "hwMemLgFree": hwMemLgFree,
       "hwMemFail": hwMemFail,
       "hwMemFailNoMem": hwMemFailNoMem,
       "hwBufTable": hwBufTable,
       "hwBufEntry": hwBufEntry,
       "hwBufModuleIndex": hwBufModuleIndex,
       "hwBufSize": hwBufSize,
       "hwBufCurrentTotal": hwBufCurrentTotal,
       "hwBufCurrentUsed": hwBufCurrentUsed,
       "hwFlh": hwFlh,
       "hwFlhTotalSize": hwFlhTotalSize,
       "hwFlhTotalFree": hwFlhTotalFree,
       "hwFlhLastDelTime": hwFlhLastDelTime,
       "hwFlhDelState": hwFlhDelState,
       "hwFlhState": hwFlhState}
)
