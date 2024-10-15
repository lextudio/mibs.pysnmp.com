# SNMP MIB module (HUAWEI-MA5200-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MA5200-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:49 2024
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

(hwFrameIndex,
 hwSlotIndex) = mibBuilder.importSymbols(
    "HUAWEI-DEVICE-MIB",
    "hwFrameIndex",
    "hwSlotIndex")

(hwMA5200Mib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwMA5200Mib")

(HWFrameType,
 HWPCBType,
 HWPortType,
 HWSubPCBType) = mibBuilder.importSymbols(
    "HUAWEI-TC-MIB",
    "HWFrameType",
    "HWPCBType",
    "HWPortType",
    "HWSubPCBType")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwMA5200Device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hw52DevSlot_ObjectIdentity = ObjectIdentity
hw52DevSlot = _Hw52DevSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 1)
)


class _Hw52DevSlotNum_Type(Integer32):
    """Custom type hw52DevSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hw52DevSlotNum_Type.__name__ = "Integer32"
_Hw52DevSlotNum_Object = MibScalar
hw52DevSlotNum = _Hw52DevSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 1, 1),
    _Hw52DevSlotNum_Type()
)
hw52DevSlotNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevSlotNum.setStatus("current")


class _Hw52DevSubSlotNum_Type(Integer32):
    """Custom type hw52DevSubSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hw52DevSubSlotNum_Type.__name__ = "Integer32"
_Hw52DevSubSlotNum_Object = MibScalar
hw52DevSubSlotNum = _Hw52DevSubSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 1, 2),
    _Hw52DevSubSlotNum_Type()
)
hw52DevSubSlotNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevSubSlotNum.setStatus("current")


class _Hw52DevPortNum_Type(Integer32):
    """Custom type hw52DevPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hw52DevPortNum_Type.__name__ = "Integer32"
_Hw52DevPortNum_Object = MibScalar
hw52DevPortNum = _Hw52DevPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 1, 3),
    _Hw52DevPortNum_Type()
)
hw52DevPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevPortNum.setStatus("current")
_Hw52DevPortOperateStatus_Type = Integer32
_Hw52DevPortOperateStatus_Object = MibScalar
hw52DevPortOperateStatus = _Hw52DevPortOperateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 1, 4),
    _Hw52DevPortOperateStatus_Type()
)
hw52DevPortOperateStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevPortOperateStatus.setStatus("current")
_Hw52DevSlotTrap_ObjectIdentity = ObjectIdentity
hw52DevSlotTrap = _Hw52DevSlotTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 2)
)
_HwHdDev_ObjectIdentity = ObjectIdentity
hwHdDev = _HwHdDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 5)
)
_HwHdDevTable_Object = MibTable
hwHdDevTable = _HwHdDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 5, 1)
)
if mibBuilder.loadTexts:
    hwHdDevTable.setStatus("current")
_HwHdDevEntry_Object = MibTableRow
hwHdDevEntry = _HwHdDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 5, 1, 1)
)
hwHdDevEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
    (0, "HUAWEI-MA5200-DEVICE-MIB", "hwHdDevIndex"),
)
if mibBuilder.loadTexts:
    hwHdDevEntry.setStatus("current")


class _HwHdDevIndex_Type(Integer32):
    """Custom type hwHdDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwHdDevIndex_Type.__name__ = "Integer32"
_HwHdDevIndex_Object = MibTableColumn
hwHdDevIndex = _HwHdDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 5, 1, 1, 1),
    _HwHdDevIndex_Type()
)
hwHdDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwHdDevIndex.setStatus("current")
_HwHdDevSize_Type = Integer32
_HwHdDevSize_Object = MibTableColumn
hwHdDevSize = _HwHdDevSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 5, 1, 1, 2),
    _HwHdDevSize_Type()
)
hwHdDevSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHdDevSize.setStatus("current")
_HwHdDevFree_Type = Integer32
_HwHdDevFree_Object = MibTableColumn
hwHdDevFree = _HwHdDevFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 5, 1, 1, 3),
    _HwHdDevFree_Type()
)
hwHdDevFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHdDevFree.setStatus("current")
_Hw52DevPortTrap_ObjectIdentity = ObjectIdentity
hw52DevPortTrap = _Hw52DevPortTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 6)
)
_Hw52DevUserAttackInfo_ObjectIdentity = ObjectIdentity
hw52DevUserAttackInfo = _Hw52DevUserAttackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 7)
)
_Hw52DevUserIPAddr_Type = IpAddress
_Hw52DevUserIPAddr_Object = MibScalar
hw52DevUserIPAddr = _Hw52DevUserIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 7, 1),
    _Hw52DevUserIPAddr_Type()
)
hw52DevUserIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevUserIPAddr.setStatus("current")
_Hw52DevUserMac_Type = MacAddress
_Hw52DevUserMac_Object = MibScalar
hw52DevUserMac = _Hw52DevUserMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 7, 2),
    _Hw52DevUserMac_Type()
)
hw52DevUserMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevUserMac.setStatus("current")
_Hw52DevUserIndex_Type = Integer32
_Hw52DevUserIndex_Object = MibScalar
hw52DevUserIndex = _Hw52DevUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 7, 3),
    _Hw52DevUserIndex_Type()
)
hw52DevUserIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevUserIndex.setStatus("current")
_Hw52DevUserOuterVlan_Type = VlanIdOrNone
_Hw52DevUserOuterVlan_Object = MibScalar
hw52DevUserOuterVlan = _Hw52DevUserOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 7, 4),
    _Hw52DevUserOuterVlan_Type()
)
hw52DevUserOuterVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevUserOuterVlan.setStatus("current")
_Hw52DevUserAttack_ObjectIdentity = ObjectIdentity
hw52DevUserAttack = _Hw52DevUserAttack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 8)
)
_Hw52TrapSwitch_ObjectIdentity = ObjectIdentity
hw52TrapSwitch = _Hw52TrapSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 9)
)


class _Hw52HwdeviceOrBasetrap_Type(Integer32):
    """Custom type hw52HwdeviceOrBasetrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("basetrap", 3),
          ("disable", 1),
          ("hwdevice", 2))
    )


_Hw52HwdeviceOrBasetrap_Type.__name__ = "Integer32"
_Hw52HwdeviceOrBasetrap_Object = MibScalar
hw52HwdeviceOrBasetrap = _Hw52HwdeviceOrBasetrap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 9, 1),
    _Hw52HwdeviceOrBasetrap_Type()
)
hw52HwdeviceOrBasetrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hw52HwdeviceOrBasetrap.setStatus("current")
_Hw52DevMemUsage_ObjectIdentity = ObjectIdentity
hw52DevMemUsage = _Hw52DevMemUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 10)
)
_Hw52DevMemUsageThreshold_Type = Integer32
_Hw52DevMemUsageThreshold_Object = MibScalar
hw52DevMemUsageThreshold = _Hw52DevMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 10, 1),
    _Hw52DevMemUsageThreshold_Type()
)
hw52DevMemUsageThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevMemUsageThreshold.setStatus("current")
_Hw52DevMemUsageTrap_ObjectIdentity = ObjectIdentity
hw52DevMemUsageTrap = _Hw52DevMemUsageTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 11)
)
_Hw52DevStartupFileFail_ObjectIdentity = ObjectIdentity
hw52DevStartupFileFail = _Hw52DevStartupFileFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 12)
)
_Hw52DevDefaultStartupFileName_Type = OctetString
_Hw52DevDefaultStartupFileName_Object = MibScalar
hw52DevDefaultStartupFileName = _Hw52DevDefaultStartupFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 12, 1),
    _Hw52DevDefaultStartupFileName_Type()
)
hw52DevDefaultStartupFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevDefaultStartupFileName.setStatus("current")
_Hw52DevCurrentStartupFileName_Type = OctetString
_Hw52DevCurrentStartupFileName_Object = MibScalar
hw52DevCurrentStartupFileName = _Hw52DevCurrentStartupFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 12, 2),
    _Hw52DevCurrentStartupFileName_Type()
)
hw52DevCurrentStartupFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevCurrentStartupFileName.setStatus("current")
_Hw52DevStartupFileFailTrap_ObjectIdentity = ObjectIdentity
hw52DevStartupFileFailTrap = _Hw52DevStartupFileFailTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 13)
)
_Hw52DevDiskSelfTestFail_ObjectIdentity = ObjectIdentity
hw52DevDiskSelfTestFail = _Hw52DevDiskSelfTestFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 14)
)
_Hw52DevDiskSelfTestDiskType_Type = OctetString
_Hw52DevDiskSelfTestDiskType_Object = MibScalar
hw52DevDiskSelfTestDiskType = _Hw52DevDiskSelfTestDiskType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 14, 1),
    _Hw52DevDiskSelfTestDiskType_Type()
)
hw52DevDiskSelfTestDiskType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevDiskSelfTestDiskType.setStatus("current")
_Hw52DevDiskSelfTestFailStep_Type = OctetString
_Hw52DevDiskSelfTestFailStep_Object = MibScalar
hw52DevDiskSelfTestFailStep = _Hw52DevDiskSelfTestFailStep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 14, 2),
    _Hw52DevDiskSelfTestFailStep_Type()
)
hw52DevDiskSelfTestFailStep.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hw52DevDiskSelfTestFailStep.setStatus("current")
_Hw52DevDiskSelfTestFailTrap_ObjectIdentity = ObjectIdentity
hw52DevDiskSelfTestFailTrap = _Hw52DevDiskSelfTestFailTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 15)
)
_Hw52DevCfUnregisterTrap_ObjectIdentity = ObjectIdentity
hw52DevCfUnregisterTrap = _Hw52DevCfUnregisterTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 16)
)
_Hw52DevHpt372ErrorTrap_ObjectIdentity = ObjectIdentity
hw52DevHpt372ErrorTrap = _Hw52DevHpt372ErrorTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 17)
)
_Hw52DevHarddiskUsageTrap_ObjectIdentity = ObjectIdentity
hw52DevHarddiskUsageTrap = _Hw52DevHarddiskUsageTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 18)
)
_Hw52PacketError_ObjectIdentity = ObjectIdentity
hw52PacketError = _Hw52PacketError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 19)
)
_Hw52DevCfcardUsageTrap_ObjectIdentity = ObjectIdentity
hw52DevCfcardUsageTrap = _Hw52DevCfcardUsageTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 20)
)
_Hw52DevFlashUsageTrap_ObjectIdentity = ObjectIdentity
hw52DevFlashUsageTrap = _Hw52DevFlashUsageTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 21)
)
_Hw52DevConformance_ObjectIdentity = ObjectIdentity
hw52DevConformance = _Hw52DevConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 200)
)
_Hw52DevCompliances_ObjectIdentity = ObjectIdentity
hw52DevCompliances = _Hw52DevCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 200, 1)
)
_Hw52DevObjectGroups_ObjectIdentity = ObjectIdentity
hw52DevObjectGroups = _Hw52DevObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 200, 2)
)

# Managed Objects groups

hw52DevSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 200, 2, 1)
)
hw52DevSlotGroup.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSubSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevPortNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevPortOperateStatus"))
)
if mibBuilder.loadTexts:
    hw52DevSlotGroup.setStatus("current")

hw52DevHdTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 200, 2, 2)
)
hw52DevHdTableGroup.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hwHdDevSize"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hwHdDevFree"))
)
if mibBuilder.loadTexts:
    hw52DevHdTableGroup.setStatus("current")

hw52DevTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 200, 2, 4)
)
hw52DevTrapObjectsGroup.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hw52DevUserIPAddr"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevUserMac"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevUserIndex"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevUserOuterVlan"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52HwdeviceOrBasetrap"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevMemUsageThreshold"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevDefaultStartupFileName"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevCurrentStartupFileName"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevDiskSelfTestDiskType"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevDiskSelfTestFailStep"))
)
if mibBuilder.loadTexts:
    hw52DevTrapObjectsGroup.setStatus("current")


# Notification objects

hw52DevSlotReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 2, 1006)
)
hw52DevSlotReset.setObjects(
    ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum")
)
if mibBuilder.loadTexts:
    hw52DevSlotReset.setStatus(
        "current"
    )

hw52DevSlotRegOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 2, 1007)
)
hw52DevSlotRegOK.setObjects(
    ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum")
)
if mibBuilder.loadTexts:
    hw52DevSlotRegOK.setStatus(
        "current"
    )

hw52DevSlotPlugOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 2, 1008)
)
hw52DevSlotPlugOut.setObjects(
    ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum")
)
if mibBuilder.loadTexts:
    hw52DevSlotPlugOut.setStatus(
        "current"
    )

hw52DevPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 6, 1)
)
hw52DevPortUp.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSubSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevPortNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevPortOperateStatus"))
)
if mibBuilder.loadTexts:
    hw52DevPortUp.setStatus(
        "current"
    )

hw52DevPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 6, 2)
)
hw52DevPortDown.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSubSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevPortNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevPortOperateStatus"))
)
if mibBuilder.loadTexts:
    hw52DevPortDown.setStatus(
        "current"
    )

hw52DevUserAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 8, 1)
)
hw52DevUserAttackTrap.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hw52DevUserIPAddr"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevUserMac"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSubSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevPortNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevUserIndex"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevUserOuterVlan"))
)
if mibBuilder.loadTexts:
    hw52DevUserAttackTrap.setStatus(
        "current"
    )

hw52DevMemUsageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 11, 1)
)
hw52DevMemUsageAlarm.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevMemUsageThreshold"))
)
if mibBuilder.loadTexts:
    hw52DevMemUsageAlarm.setStatus(
        "current"
    )

hw52DevMemUsageResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 11, 2)
)
hw52DevMemUsageResume.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevMemUsageThreshold"))
)
if mibBuilder.loadTexts:
    hw52DevMemUsageResume.setStatus(
        "current"
    )

hw52DevStartupFileReloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 13, 1)
)
hw52DevStartupFileReloadAlarm.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hw52DevDefaultStartupFileName"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevCurrentStartupFileName"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum"))
)
if mibBuilder.loadTexts:
    hw52DevStartupFileReloadAlarm.setStatus(
        "current"
    )

hw52DevDiskSelfTestFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 15, 1)
)
hw52DevDiskSelfTestFailAlarm.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hw52DevDiskSelfTestDiskType"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevDiskSelfTestFailStep"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum"))
)
if mibBuilder.loadTexts:
    hw52DevDiskSelfTestFailAlarm.setStatus(
        "current"
    )

hw52DevCfUnregisteredAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 16, 1)
)
hw52DevCfUnregisteredAlarm.setObjects(
    ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum")
)
if mibBuilder.loadTexts:
    hw52DevCfUnregisteredAlarm.setStatus(
        "current"
    )

hw52DevHpt372ErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 17, 1)
)
hw52DevHpt372ErrorAlarm.setObjects(
    ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum")
)
if mibBuilder.loadTexts:
    hw52DevHpt372ErrorAlarm.setStatus(
        "current"
    )

hw52DevHarddiskUsageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 18, 1)
)
hw52DevHarddiskUsageAlarm.setObjects(
    ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum")
)
if mibBuilder.loadTexts:
    hw52DevHarddiskUsageAlarm.setStatus(
        "current"
    )

hw52DevHarddiskUsageResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 18, 2)
)
hw52DevHarddiskUsageResume.setObjects(
    ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum")
)
if mibBuilder.loadTexts:
    hw52DevHarddiskUsageResume.setStatus(
        "current"
    )

hw52InPacketErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 19, 1)
)
hw52InPacketErrorTrap.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSubSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevPortNum"))
)
if mibBuilder.loadTexts:
    hw52InPacketErrorTrap.setStatus(
        "current"
    )

hw52OutPacketErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 19, 2)
)
hw52OutPacketErrorTrap.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSubSlotNum"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevPortNum"))
)
if mibBuilder.loadTexts:
    hw52OutPacketErrorTrap.setStatus(
        "current"
    )

hw52DevCfcardUsageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 20, 1)
)
hw52DevCfcardUsageAlarm.setObjects(
    ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum")
)
if mibBuilder.loadTexts:
    hw52DevCfcardUsageAlarm.setStatus(
        "current"
    )

hw52DevCfcardUsageResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 20, 2)
)
hw52DevCfcardUsageResume.setObjects(
    ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum")
)
if mibBuilder.loadTexts:
    hw52DevCfcardUsageResume.setStatus(
        "current"
    )

hw52DevFlashUsageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 21, 1)
)
hw52DevFlashUsageAlarm.setObjects(
    ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum")
)
if mibBuilder.loadTexts:
    hw52DevFlashUsageAlarm.setStatus(
        "current"
    )

hw52DevFlashUsageResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 21, 2)
)
hw52DevFlashUsageResume.setObjects(
    ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotNum")
)
if mibBuilder.loadTexts:
    hw52DevFlashUsageResume.setStatus(
        "current"
    )


# Notifications groups

hw52DevTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 200, 2, 3)
)
hw52DevTrapsGroup.setObjects(
      *(("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotReset"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotRegOK"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevSlotPlugOut"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevPortUp"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevPortDown"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevUserAttackTrap"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevMemUsageAlarm"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevMemUsageResume"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevStartupFileReloadAlarm"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevDiskSelfTestFailAlarm"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevCfUnregisteredAlarm"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevHpt372ErrorAlarm"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevHarddiskUsageAlarm"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevHarddiskUsageResume"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52InPacketErrorTrap"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52OutPacketErrorTrap"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevCfcardUsageAlarm"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevCfcardUsageResume"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevFlashUsageAlarm"),
        ("HUAWEI-MA5200-DEVICE-MIB", "hw52DevFlashUsageResume"))
)
if mibBuilder.loadTexts:
    hw52DevTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hw52DevCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 2, 201, 200, 1, 1)
)
if mibBuilder.loadTexts:
    hw52DevCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MA5200-DEVICE-MIB",
    **{"hwMA5200Device": hwMA5200Device,
       "hw52DevSlot": hw52DevSlot,
       "hw52DevSlotNum": hw52DevSlotNum,
       "hw52DevSubSlotNum": hw52DevSubSlotNum,
       "hw52DevPortNum": hw52DevPortNum,
       "hw52DevPortOperateStatus": hw52DevPortOperateStatus,
       "hw52DevSlotTrap": hw52DevSlotTrap,
       "hw52DevSlotReset": hw52DevSlotReset,
       "hw52DevSlotRegOK": hw52DevSlotRegOK,
       "hw52DevSlotPlugOut": hw52DevSlotPlugOut,
       "hwHdDev": hwHdDev,
       "hwHdDevTable": hwHdDevTable,
       "hwHdDevEntry": hwHdDevEntry,
       "hwHdDevIndex": hwHdDevIndex,
       "hwHdDevSize": hwHdDevSize,
       "hwHdDevFree": hwHdDevFree,
       "hw52DevPortTrap": hw52DevPortTrap,
       "hw52DevPortUp": hw52DevPortUp,
       "hw52DevPortDown": hw52DevPortDown,
       "hw52DevUserAttackInfo": hw52DevUserAttackInfo,
       "hw52DevUserIPAddr": hw52DevUserIPAddr,
       "hw52DevUserMac": hw52DevUserMac,
       "hw52DevUserIndex": hw52DevUserIndex,
       "hw52DevUserOuterVlan": hw52DevUserOuterVlan,
       "hw52DevUserAttack": hw52DevUserAttack,
       "hw52DevUserAttackTrap": hw52DevUserAttackTrap,
       "hw52TrapSwitch": hw52TrapSwitch,
       "hw52HwdeviceOrBasetrap": hw52HwdeviceOrBasetrap,
       "hw52DevMemUsage": hw52DevMemUsage,
       "hw52DevMemUsageThreshold": hw52DevMemUsageThreshold,
       "hw52DevMemUsageTrap": hw52DevMemUsageTrap,
       "hw52DevMemUsageAlarm": hw52DevMemUsageAlarm,
       "hw52DevMemUsageResume": hw52DevMemUsageResume,
       "hw52DevStartupFileFail": hw52DevStartupFileFail,
       "hw52DevDefaultStartupFileName": hw52DevDefaultStartupFileName,
       "hw52DevCurrentStartupFileName": hw52DevCurrentStartupFileName,
       "hw52DevStartupFileFailTrap": hw52DevStartupFileFailTrap,
       "hw52DevStartupFileReloadAlarm": hw52DevStartupFileReloadAlarm,
       "hw52DevDiskSelfTestFail": hw52DevDiskSelfTestFail,
       "hw52DevDiskSelfTestDiskType": hw52DevDiskSelfTestDiskType,
       "hw52DevDiskSelfTestFailStep": hw52DevDiskSelfTestFailStep,
       "hw52DevDiskSelfTestFailTrap": hw52DevDiskSelfTestFailTrap,
       "hw52DevDiskSelfTestFailAlarm": hw52DevDiskSelfTestFailAlarm,
       "hw52DevCfUnregisterTrap": hw52DevCfUnregisterTrap,
       "hw52DevCfUnregisteredAlarm": hw52DevCfUnregisteredAlarm,
       "hw52DevHpt372ErrorTrap": hw52DevHpt372ErrorTrap,
       "hw52DevHpt372ErrorAlarm": hw52DevHpt372ErrorAlarm,
       "hw52DevHarddiskUsageTrap": hw52DevHarddiskUsageTrap,
       "hw52DevHarddiskUsageAlarm": hw52DevHarddiskUsageAlarm,
       "hw52DevHarddiskUsageResume": hw52DevHarddiskUsageResume,
       "hw52PacketError": hw52PacketError,
       "hw52InPacketErrorTrap": hw52InPacketErrorTrap,
       "hw52OutPacketErrorTrap": hw52OutPacketErrorTrap,
       "hw52DevCfcardUsageTrap": hw52DevCfcardUsageTrap,
       "hw52DevCfcardUsageAlarm": hw52DevCfcardUsageAlarm,
       "hw52DevCfcardUsageResume": hw52DevCfcardUsageResume,
       "hw52DevFlashUsageTrap": hw52DevFlashUsageTrap,
       "hw52DevFlashUsageAlarm": hw52DevFlashUsageAlarm,
       "hw52DevFlashUsageResume": hw52DevFlashUsageResume,
       "hw52DevConformance": hw52DevConformance,
       "hw52DevCompliances": hw52DevCompliances,
       "hw52DevCompliance": hw52DevCompliance,
       "hw52DevObjectGroups": hw52DevObjectGroups,
       "hw52DevSlotGroup": hw52DevSlotGroup,
       "hw52DevHdTableGroup": hw52DevHdTableGroup,
       "hw52DevTrapsGroup": hw52DevTrapsGroup,
       "hw52DevTrapObjectsGroup": hw52DevTrapObjectsGroup}
)
