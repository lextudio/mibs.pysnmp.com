# SNMP MIB module (HUAWEI-ERPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ERPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:44 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwErpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwErpsObjects_ObjectIdentity = ObjectIdentity
hwErpsObjects = _HwErpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1)
)


class _HwErpsGlobalResetRapsPktCnt_Type(Integer32):
    """Custom type hwErpsGlobalResetRapsPktCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("unused", 65535))
    )


_HwErpsGlobalResetRapsPktCnt_Type.__name__ = "Integer32"
_HwErpsGlobalResetRapsPktCnt_Object = MibScalar
hwErpsGlobalResetRapsPktCnt = _HwErpsGlobalResetRapsPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 1),
    _HwErpsGlobalResetRapsPktCnt_Type()
)
hwErpsGlobalResetRapsPktCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwErpsGlobalResetRapsPktCnt.setStatus("current")
_HwErpsRingConfigTable_Object = MibTable
hwErpsRingConfigTable = _HwErpsRingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 2)
)
if mibBuilder.loadTexts:
    hwErpsRingConfigTable.setStatus("current")
_HwErpsRingConfigEntry_Object = MibTableRow
hwErpsRingConfigEntry = _HwErpsRingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 2, 1)
)
hwErpsRingConfigEntry.setIndexNames(
    (0, "HUAWEI-ERPS-MIB", "hwConfigRingId"),
)
if mibBuilder.loadTexts:
    hwErpsRingConfigEntry.setStatus("current")


class _HwConfigRingId_Type(Integer32):
    """Custom type hwConfigRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwConfigRingId_Type.__name__ = "Integer32"
_HwConfigRingId_Object = MibTableColumn
hwConfigRingId = _HwConfigRingId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 2, 1, 1),
    _HwConfigRingId_Type()
)
hwConfigRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConfigRingId.setStatus("current")
_HwConfigRingRowStatus_Type = RowStatus
_HwConfigRingRowStatus_Object = MibTableColumn
hwConfigRingRowStatus = _HwConfigRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 2, 1, 2),
    _HwConfigRingRowStatus_Type()
)
hwConfigRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwConfigRingRowStatus.setStatus("current")


class _HwConfigDescription_Type(DisplayString):
    """Custom type hwConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HwConfigDescription_Type.__name__ = "DisplayString"
_HwConfigDescription_Object = MibTableColumn
hwConfigDescription = _HwConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 2, 1, 3),
    _HwConfigDescription_Type()
)
hwConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwConfigDescription.setStatus("current")


class _HwConfigControlVlanId_Type(Integer32):
    """Custom type hwConfigControlVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_HwConfigControlVlanId_Type.__name__ = "Integer32"
_HwConfigControlVlanId_Object = MibTableColumn
hwConfigControlVlanId = _HwConfigControlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 2, 1, 4),
    _HwConfigControlVlanId_Type()
)
hwConfigControlVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwConfigControlVlanId.setStatus("current")


class _HwConfigProtectedInstanceList_Type(OctetString):
    """Custom type hwConfigProtectedInstanceList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_HwConfigProtectedInstanceList_Type.__name__ = "OctetString"
_HwConfigProtectedInstanceList_Object = MibTableColumn
hwConfigProtectedInstanceList = _HwConfigProtectedInstanceList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 2, 1, 5),
    _HwConfigProtectedInstanceList_Type()
)
hwConfigProtectedInstanceList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwConfigProtectedInstanceList.setStatus("current")


class _HwConfigWtrTimerSettingValue_Type(Integer32):
    """Custom type hwConfigWtrTimerSettingValue based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HwConfigWtrTimerSettingValue_Type.__name__ = "Integer32"
_HwConfigWtrTimerSettingValue_Object = MibTableColumn
hwConfigWtrTimerSettingValue = _HwConfigWtrTimerSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 2, 1, 6),
    _HwConfigWtrTimerSettingValue_Type()
)
hwConfigWtrTimerSettingValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwConfigWtrTimerSettingValue.setStatus("current")
if mibBuilder.loadTexts:
    hwConfigWtrTimerSettingValue.setUnits("minutes")


class _HwConfigGuardTimerSettingValue_Type(Integer32):
    """Custom type hwConfigGuardTimerSettingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_HwConfigGuardTimerSettingValue_Type.__name__ = "Integer32"
_HwConfigGuardTimerSettingValue_Object = MibTableColumn
hwConfigGuardTimerSettingValue = _HwConfigGuardTimerSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 2, 1, 7),
    _HwConfigGuardTimerSettingValue_Type()
)
hwConfigGuardTimerSettingValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwConfigGuardTimerSettingValue.setStatus("current")
if mibBuilder.loadTexts:
    hwConfigGuardTimerSettingValue.setUnits("centiseconds")


class _HwConfigHoldoffTimerSettingValue_Type(Integer32):
    """Custom type hwConfigHoldoffTimerSettingValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwConfigHoldoffTimerSettingValue_Type.__name__ = "Integer32"
_HwConfigHoldoffTimerSettingValue_Object = MibTableColumn
hwConfigHoldoffTimerSettingValue = _HwConfigHoldoffTimerSettingValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 2, 1, 8),
    _HwConfigHoldoffTimerSettingValue_Type()
)
hwConfigHoldoffTimerSettingValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwConfigHoldoffTimerSettingValue.setStatus("current")
if mibBuilder.loadTexts:
    hwConfigHoldoffTimerSettingValue.setUnits("deciseconds")


class _HwConfigResetRapsPktCnt_Type(Integer32):
    """Custom type hwConfigResetRapsPktCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("unused", 65535))
    )


_HwConfigResetRapsPktCnt_Type.__name__ = "Integer32"
_HwConfigResetRapsPktCnt_Object = MibTableColumn
hwConfigResetRapsPktCnt = _HwConfigResetRapsPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 2, 1, 9),
    _HwConfigResetRapsPktCnt_Type()
)
hwConfigResetRapsPktCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwConfigResetRapsPktCnt.setStatus("current")


class _HwConfigRapsMel_Type(Integer32):
    """Custom type hwConfigRapsMel based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwConfigRapsMel_Type.__name__ = "Integer32"
_HwConfigRapsMel_Object = MibTableColumn
hwConfigRapsMel = _HwConfigRapsMel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 2, 1, 10),
    _HwConfigRapsMel_Type()
)
hwConfigRapsMel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwConfigRapsMel.setStatus("current")
_HwErpsRingStatusTable_Object = MibTable
hwErpsRingStatusTable = _HwErpsRingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 3)
)
if mibBuilder.loadTexts:
    hwErpsRingStatusTable.setStatus("current")
_HwErpsRingStatusEntry_Object = MibTableRow
hwErpsRingStatusEntry = _HwErpsRingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 3, 1)
)
hwErpsRingStatusEntry.setIndexNames(
    (0, "HUAWEI-ERPS-MIB", "hwConfigRingId"),
)
if mibBuilder.loadTexts:
    hwErpsRingStatusEntry.setStatus("current")


class _HwStatusWtrTimerRunningValue_Type(Integer32):
    """Custom type hwStatusWtrTimerRunningValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_HwStatusWtrTimerRunningValue_Type.__name__ = "Integer32"
_HwStatusWtrTimerRunningValue_Object = MibTableColumn
hwStatusWtrTimerRunningValue = _HwStatusWtrTimerRunningValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 3, 1, 1),
    _HwStatusWtrTimerRunningValue_Type()
)
hwStatusWtrTimerRunningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStatusWtrTimerRunningValue.setStatus("current")
if mibBuilder.loadTexts:
    hwStatusWtrTimerRunningValue.setUnits("seconds")


class _HwStatusGuardTimerRunningValue_Type(Integer32):
    """Custom type hwStatusGuardTimerRunningValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_HwStatusGuardTimerRunningValue_Type.__name__ = "Integer32"
_HwStatusGuardTimerRunningValue_Object = MibTableColumn
hwStatusGuardTimerRunningValue = _HwStatusGuardTimerRunningValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 3, 1, 2),
    _HwStatusGuardTimerRunningValue_Type()
)
hwStatusGuardTimerRunningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStatusGuardTimerRunningValue.setStatus("current")
if mibBuilder.loadTexts:
    hwStatusGuardTimerRunningValue.setUnits("centiseconds")


class _HwStatusHoldoffTimerRunningValue_Type(Integer32):
    """Custom type hwStatusHoldoffTimerRunningValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwStatusHoldoffTimerRunningValue_Type.__name__ = "Integer32"
_HwStatusHoldoffTimerRunningValue_Object = MibTableColumn
hwStatusHoldoffTimerRunningValue = _HwStatusHoldoffTimerRunningValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 3, 1, 3),
    _HwStatusHoldoffTimerRunningValue_Type()
)
hwStatusHoldoffTimerRunningValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStatusHoldoffTimerRunningValue.setStatus("current")
if mibBuilder.loadTexts:
    hwStatusHoldoffTimerRunningValue.setUnits("deciseconds")


class _HwStatusMachineState_Type(Integer32):
    """Custom type hwStatusMachineState based on Integer32"""
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
        *(("forcedSwitch", 4),
          ("idle", 1),
          ("manualSwitch", 3),
          ("pending", 5),
          ("protection", 2))
    )


_HwStatusMachineState_Type.__name__ = "Integer32"
_HwStatusMachineState_Object = MibTableColumn
hwStatusMachineState = _HwStatusMachineState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 3, 1, 4),
    _HwStatusMachineState_Type()
)
hwStatusMachineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStatusMachineState.setStatus("current")
_HwStatusTopoLastChangeTime_Type = TimeTicks
_HwStatusTopoLastChangeTime_Object = MibTableColumn
hwStatusTopoLastChangeTime = _HwStatusTopoLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 3, 1, 5),
    _HwStatusTopoLastChangeTime_Type()
)
hwStatusTopoLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStatusTopoLastChangeTime.setStatus("current")
_HwErpsPortConfigTable_Object = MibTable
hwErpsPortConfigTable = _HwErpsPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 4)
)
if mibBuilder.loadTexts:
    hwErpsPortConfigTable.setStatus("current")
_HwErpsPortConfigEntry_Object = MibTableRow
hwErpsPortConfigEntry = _HwErpsPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 4, 1)
)
hwErpsPortConfigEntry.setIndexNames(
    (0, "HUAWEI-ERPS-MIB", "hwConfigRingId"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortType"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortId1"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortId2"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortId3"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortId4"),
)
if mibBuilder.loadTexts:
    hwErpsPortConfigEntry.setStatus("current")


class _HwConfigPortType_Type(Unsigned32):
    """Custom type hwConfigPortType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwConfigPortType_Type.__name__ = "Unsigned32"
_HwConfigPortType_Object = MibTableColumn
hwConfigPortType = _HwConfigPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 4, 1, 1),
    _HwConfigPortType_Type()
)
hwConfigPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConfigPortType.setStatus("current")


class _HwConfigPortId1_Type(Unsigned32):
    """Custom type hwConfigPortId1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwConfigPortId1_Type.__name__ = "Unsigned32"
_HwConfigPortId1_Object = MibTableColumn
hwConfigPortId1 = _HwConfigPortId1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 4, 1, 2),
    _HwConfigPortId1_Type()
)
hwConfigPortId1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConfigPortId1.setStatus("current")


class _HwConfigPortId2_Type(Unsigned32):
    """Custom type hwConfigPortId2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwConfigPortId2_Type.__name__ = "Unsigned32"
_HwConfigPortId2_Object = MibTableColumn
hwConfigPortId2 = _HwConfigPortId2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 4, 1, 3),
    _HwConfigPortId2_Type()
)
hwConfigPortId2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConfigPortId2.setStatus("current")


class _HwConfigPortId3_Type(Unsigned32):
    """Custom type hwConfigPortId3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwConfigPortId3_Type.__name__ = "Unsigned32"
_HwConfigPortId3_Object = MibTableColumn
hwConfigPortId3 = _HwConfigPortId3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 4, 1, 4),
    _HwConfigPortId3_Type()
)
hwConfigPortId3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConfigPortId3.setStatus("current")


class _HwConfigPortId4_Type(Unsigned32):
    """Custom type hwConfigPortId4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwConfigPortId4_Type.__name__ = "Unsigned32"
_HwConfigPortId4_Object = MibTableColumn
hwConfigPortId4 = _HwConfigPortId4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 4, 1, 5),
    _HwConfigPortId4_Type()
)
hwConfigPortId4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwConfigPortId4.setStatus("current")
_HwConfigPortRowStatus_Type = RowStatus
_HwConfigPortRowStatus_Object = MibTableColumn
hwConfigPortRowStatus = _HwConfigPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 4, 1, 6),
    _HwConfigPortRowStatus_Type()
)
hwConfigPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwConfigPortRowStatus.setStatus("current")
_HwConfigPortConfigRole_Type = Integer32
_HwConfigPortConfigRole_Object = MibTableColumn
hwConfigPortConfigRole = _HwConfigPortConfigRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 4, 1, 7),
    _HwConfigPortConfigRole_Type()
)
hwConfigPortConfigRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwConfigPortConfigRole.setStatus("current")
_HwErpsPortStatusTable_Object = MibTable
hwErpsPortStatusTable = _HwErpsPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 5)
)
if mibBuilder.loadTexts:
    hwErpsPortStatusTable.setStatus("current")
_HwErpsPortStatusEntry_Object = MibTableRow
hwErpsPortStatusEntry = _HwErpsPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 5, 1)
)
hwErpsPortStatusEntry.setIndexNames(
    (0, "HUAWEI-ERPS-MIB", "hwConfigRingId"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortType"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortId1"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortId2"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortId3"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortId4"),
)
if mibBuilder.loadTexts:
    hwErpsPortStatusEntry.setStatus("current")
_HwPortStatusActiveRole_Type = Integer32
_HwPortStatusActiveRole_Object = MibTableColumn
hwPortStatusActiveRole = _HwPortStatusActiveRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 5, 1, 1),
    _HwPortStatusActiveRole_Type()
)
hwPortStatusActiveRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortStatusActiveRole.setStatus("current")


class _HwPortStatusSignalStatus_Type(Integer32):
    """Custom type hwPortStatusSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("nonFailed", 2))
    )


_HwPortStatusSignalStatus_Type.__name__ = "Integer32"
_HwPortStatusSignalStatus_Object = MibTableColumn
hwPortStatusSignalStatus = _HwPortStatusSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 5, 1, 2),
    _HwPortStatusSignalStatus_Type()
)
hwPortStatusSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortStatusSignalStatus.setStatus("current")


class _HwPortStatusFwdStatus_Type(Integer32):
    """Custom type hwPortStatusFwdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 1),
          ("forwarding", 2))
    )


_HwPortStatusFwdStatus_Type.__name__ = "Integer32"
_HwPortStatusFwdStatus_Object = MibTableColumn
hwPortStatusFwdStatus = _HwPortStatusFwdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 5, 1, 3),
    _HwPortStatusFwdStatus_Type()
)
hwPortStatusFwdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortStatusFwdStatus.setStatus("current")
_HwErpsPortStatisticsTable_Object = MibTable
hwErpsPortStatisticsTable = _HwErpsPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 6)
)
if mibBuilder.loadTexts:
    hwErpsPortStatisticsTable.setStatus("current")
_HwErpsPortStatisticsEntry_Object = MibTableRow
hwErpsPortStatisticsEntry = _HwErpsPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 6, 1)
)
hwErpsPortStatisticsEntry.setIndexNames(
    (0, "HUAWEI-ERPS-MIB", "hwConfigRingId"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortType"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortId1"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortId2"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortId3"),
    (0, "HUAWEI-ERPS-MIB", "hwConfigPortId4"),
)
if mibBuilder.loadTexts:
    hwErpsPortStatisticsEntry.setStatus("current")
_HwRxRapsSfPktCnt_Type = Counter32
_HwRxRapsSfPktCnt_Object = MibTableColumn
hwRxRapsSfPktCnt = _HwRxRapsSfPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 6, 1, 1),
    _HwRxRapsSfPktCnt_Type()
)
hwRxRapsSfPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRxRapsSfPktCnt.setStatus("current")
_HwTxRapsSfPktCnt_Type = Counter32
_HwTxRapsSfPktCnt_Object = MibTableColumn
hwTxRapsSfPktCnt = _HwTxRapsSfPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 6, 1, 2),
    _HwTxRapsSfPktCnt_Type()
)
hwTxRapsSfPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTxRapsSfPktCnt.setStatus("current")
_HwRxRapsNrPktCnt_Type = Counter32
_HwRxRapsNrPktCnt_Object = MibTableColumn
hwRxRapsNrPktCnt = _HwRxRapsNrPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 6, 1, 3),
    _HwRxRapsNrPktCnt_Type()
)
hwRxRapsNrPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRxRapsNrPktCnt.setStatus("current")
_HwTxRapsNrPktCnt_Type = Counter32
_HwTxRapsNrPktCnt_Object = MibTableColumn
hwTxRapsNrPktCnt = _HwTxRapsNrPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 6, 1, 4),
    _HwTxRapsNrPktCnt_Type()
)
hwTxRapsNrPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTxRapsNrPktCnt.setStatus("current")
_HwRxRapsNrRbPktCnt_Type = Counter32
_HwRxRapsNrRbPktCnt_Object = MibTableColumn
hwRxRapsNrRbPktCnt = _HwRxRapsNrRbPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 6, 1, 5),
    _HwRxRapsNrRbPktCnt_Type()
)
hwRxRapsNrRbPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRxRapsNrRbPktCnt.setStatus("current")
_HwTxRapsNrRbPktCnt_Type = Counter32
_HwTxRapsNrRbPktCnt_Object = MibTableColumn
hwTxRapsNrRbPktCnt = _HwTxRapsNrRbPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 1, 6, 1, 6),
    _HwTxRapsNrRbPktCnt_Type()
)
hwTxRapsNrRbPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTxRapsNrRbPktCnt.setStatus("current")
_HwErpsGroups_ObjectIdentity = ObjectIdentity
hwErpsGroups = _HwErpsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 2)
)

# Managed Objects groups

hwErpsGlobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 2, 1)
)
hwErpsGlobalInfoGroup.setObjects(
    ("HUAWEI-ERPS-MIB", "hwErpsGlobalResetRapsPktCnt")
)
if mibBuilder.loadTexts:
    hwErpsGlobalInfoGroup.setStatus("current")

hwErpsRingConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 2, 2)
)
hwErpsRingConfigInfoGroup.setObjects(
      *(("HUAWEI-ERPS-MIB", "hwConfigRingRowStatus"),
        ("HUAWEI-ERPS-MIB", "hwConfigDescription"),
        ("HUAWEI-ERPS-MIB", "hwConfigControlVlanId"),
        ("HUAWEI-ERPS-MIB", "hwConfigProtectedInstanceList"),
        ("HUAWEI-ERPS-MIB", "hwConfigWtrTimerSettingValue"),
        ("HUAWEI-ERPS-MIB", "hwConfigGuardTimerSettingValue"),
        ("HUAWEI-ERPS-MIB", "hwConfigHoldoffTimerSettingValue"),
        ("HUAWEI-ERPS-MIB", "hwConfigResetRapsPktCnt"),
        ("HUAWEI-ERPS-MIB", "hwConfigRapsMel"))
)
if mibBuilder.loadTexts:
    hwErpsRingConfigInfoGroup.setStatus("current")

hwErpsRingStatusInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 2, 3)
)
hwErpsRingStatusInfoGroup.setObjects(
      *(("HUAWEI-ERPS-MIB", "hwStatusWtrTimerRunningValue"),
        ("HUAWEI-ERPS-MIB", "hwStatusGuardTimerRunningValue"),
        ("HUAWEI-ERPS-MIB", "hwStatusHoldoffTimerRunningValue"),
        ("HUAWEI-ERPS-MIB", "hwStatusMachineState"),
        ("HUAWEI-ERPS-MIB", "hwStatusTopoLastChangeTime"))
)
if mibBuilder.loadTexts:
    hwErpsRingStatusInfoGroup.setStatus("current")

hwErpsPortConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 2, 4)
)
hwErpsPortConfigInfoGroup.setObjects(
      *(("HUAWEI-ERPS-MIB", "hwConfigPortRowStatus"),
        ("HUAWEI-ERPS-MIB", "hwConfigPortConfigRole"))
)
if mibBuilder.loadTexts:
    hwErpsPortConfigInfoGroup.setStatus("current")

hwErpsPortStatusInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 2, 5)
)
hwErpsPortStatusInfoGroup.setObjects(
      *(("HUAWEI-ERPS-MIB", "hwPortStatusActiveRole"),
        ("HUAWEI-ERPS-MIB", "hwPortStatusSignalStatus"),
        ("HUAWEI-ERPS-MIB", "hwPortStatusFwdStatus"))
)
if mibBuilder.loadTexts:
    hwErpsPortStatusInfoGroup.setStatus("current")

hwErpsPortStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 256, 2, 6)
)
hwErpsPortStatisticsInfoGroup.setObjects(
      *(("HUAWEI-ERPS-MIB", "hwRxRapsSfPktCnt"),
        ("HUAWEI-ERPS-MIB", "hwTxRapsSfPktCnt"),
        ("HUAWEI-ERPS-MIB", "hwRxRapsNrPktCnt"),
        ("HUAWEI-ERPS-MIB", "hwTxRapsNrPktCnt"),
        ("HUAWEI-ERPS-MIB", "hwRxRapsNrRbPktCnt"),
        ("HUAWEI-ERPS-MIB", "hwTxRapsNrRbPktCnt"))
)
if mibBuilder.loadTexts:
    hwErpsPortStatisticsInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ERPS-MIB",
    **{"hwErpsMIB": hwErpsMIB,
       "hwErpsObjects": hwErpsObjects,
       "hwErpsGlobalResetRapsPktCnt": hwErpsGlobalResetRapsPktCnt,
       "hwErpsRingConfigTable": hwErpsRingConfigTable,
       "hwErpsRingConfigEntry": hwErpsRingConfigEntry,
       "hwConfigRingId": hwConfigRingId,
       "hwConfigRingRowStatus": hwConfigRingRowStatus,
       "hwConfigDescription": hwConfigDescription,
       "hwConfigControlVlanId": hwConfigControlVlanId,
       "hwConfigProtectedInstanceList": hwConfigProtectedInstanceList,
       "hwConfigWtrTimerSettingValue": hwConfigWtrTimerSettingValue,
       "hwConfigGuardTimerSettingValue": hwConfigGuardTimerSettingValue,
       "hwConfigHoldoffTimerSettingValue": hwConfigHoldoffTimerSettingValue,
       "hwConfigResetRapsPktCnt": hwConfigResetRapsPktCnt,
       "hwConfigRapsMel": hwConfigRapsMel,
       "hwErpsRingStatusTable": hwErpsRingStatusTable,
       "hwErpsRingStatusEntry": hwErpsRingStatusEntry,
       "hwStatusWtrTimerRunningValue": hwStatusWtrTimerRunningValue,
       "hwStatusGuardTimerRunningValue": hwStatusGuardTimerRunningValue,
       "hwStatusHoldoffTimerRunningValue": hwStatusHoldoffTimerRunningValue,
       "hwStatusMachineState": hwStatusMachineState,
       "hwStatusTopoLastChangeTime": hwStatusTopoLastChangeTime,
       "hwErpsPortConfigTable": hwErpsPortConfigTable,
       "hwErpsPortConfigEntry": hwErpsPortConfigEntry,
       "hwConfigPortType": hwConfigPortType,
       "hwConfigPortId1": hwConfigPortId1,
       "hwConfigPortId2": hwConfigPortId2,
       "hwConfigPortId3": hwConfigPortId3,
       "hwConfigPortId4": hwConfigPortId4,
       "hwConfigPortRowStatus": hwConfigPortRowStatus,
       "hwConfigPortConfigRole": hwConfigPortConfigRole,
       "hwErpsPortStatusTable": hwErpsPortStatusTable,
       "hwErpsPortStatusEntry": hwErpsPortStatusEntry,
       "hwPortStatusActiveRole": hwPortStatusActiveRole,
       "hwPortStatusSignalStatus": hwPortStatusSignalStatus,
       "hwPortStatusFwdStatus": hwPortStatusFwdStatus,
       "hwErpsPortStatisticsTable": hwErpsPortStatisticsTable,
       "hwErpsPortStatisticsEntry": hwErpsPortStatisticsEntry,
       "hwRxRapsSfPktCnt": hwRxRapsSfPktCnt,
       "hwTxRapsSfPktCnt": hwTxRapsSfPktCnt,
       "hwRxRapsNrPktCnt": hwRxRapsNrPktCnt,
       "hwTxRapsNrPktCnt": hwTxRapsNrPktCnt,
       "hwRxRapsNrRbPktCnt": hwRxRapsNrRbPktCnt,
       "hwTxRapsNrRbPktCnt": hwTxRapsNrRbPktCnt,
       "hwErpsGroups": hwErpsGroups,
       "hwErpsGlobalInfoGroup": hwErpsGlobalInfoGroup,
       "hwErpsRingConfigInfoGroup": hwErpsRingConfigInfoGroup,
       "hwErpsRingStatusInfoGroup": hwErpsRingStatusInfoGroup,
       "hwErpsPortConfigInfoGroup": hwErpsPortConfigInfoGroup,
       "hwErpsPortStatusInfoGroup": hwErpsPortStatusInfoGroup,
       "hwErpsPortStatisticsInfoGroup": hwErpsPortStatisticsInfoGroup}
)
