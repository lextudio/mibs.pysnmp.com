# SNMP MIB module (CISCO-UNIFIED-COMPUTING-STORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-STORAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:21 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsAaaConfigState,
 CucsConditionRemoteInvRslt,
 CucsEquipmentOperability,
 CucsEquipmentPowerState,
 CucsEquipmentPresence,
 CucsEquipmentSensorThresholdStatus,
 CucsFabricZoningState,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsFsmLifecycle,
 CucsLstorageBootDevice,
 CucsPolicyPolicyOwner,
 CucsStorageAccessType,
 CucsStorageActualWriteType,
 CucsStorageAdminActionTrigger,
 CucsStorageAdminActionType,
 CucsStorageAdminCtrlActionType,
 CucsStorageAdminState,
 CucsStorageBatteryType,
 CucsStorageBbuStatus,
 CucsStorageBootableType,
 CucsStorageCacheType,
 CucsStorageConfigCheckPoint,
 CucsStorageConfigState,
 CucsStorageConfiguration,
 CucsStorageConfiguredWriteType,
 CucsStorageConnectionProtocol,
 CucsStorageControllerFaultMonitoring,
 CucsStorageControllerId,
 CucsStorageControllerPinnedCacheStatus,
 CucsStorageControllerStatus,
 CucsStorageControllerType,
 CucsStorageDeployAction,
 CucsStorageDiskEnvStatsHistThresholded,
 CucsStorageDiskEnvStatsThresholded,
 CucsStorageDiskRole,
 CucsStorageDisklessAction,
 CucsStorageEnclosureId,
 CucsStorageEpAccess,
 CucsStorageEtherIfVlanType,
 CucsStorageFFCardHealth,
 CucsStorageFFCardMode,
 CucsStorageFFCardSizeMismatch,
 CucsStorageFFCardState,
 CucsStorageFFCardSync,
 CucsStorageFFCardWriteEnable,
 CucsStorageFFControllerHealth,
 CucsStorageFFControllerState,
 CucsStorageFFDriveRemovable,
 CucsStorageFFDriveState,
 CucsStorageFFDriveType,
 CucsStorageFFDriveVisible,
 CucsStorageFFFormatRunning,
 CucsStorageFFHasError,
 CucsStorageFFRAIDHealth,
 CucsStorageFFRAIDState,
 CucsStorageFFRWType,
 CucsStorageFFRaidSyncSupport,
 CucsStorageFFSlotENUM,
 CucsStorageFFType,
 CucsStorageFcZoningType,
 CucsStorageFileSystemStatus,
 CucsStorageFlexFlashControllerFsmCurrentFsm,
 CucsStorageFlexFlashControllerFsmStageName,
 CucsStorageFlexFlashControllerFsmTaskItem,
 CucsStorageFlexFlashControllerId,
 CucsStorageIOType,
 CucsStorageIniGroupOperProtocol,
 CucsStorageIniGroupOwner,
 CucsStorageIniGroupProtocol,
 CucsStorageKeyType,
 CucsStorageLearnCycleRequested,
 CucsStorageLearnMode,
 CucsStorageLinkSpeed,
 CucsStorageLocalDiskConfigFlexFlashRAIDReportingState,
 CucsStorageLocalDiskConfigFlexFlashState,
 CucsStorageLocalDiskMode,
 CucsStorageLunType,
 CucsStorageOperState,
 CucsStorageOperatingModeType,
 CucsStorageOperationRequestType,
 CucsStorageOperationState,
 CucsStorageOperationStateType,
 CucsStorageOperationType,
 CucsStorageOptionRomBootStatus,
 CucsStoragePDriveStatus,
 CucsStoragePowerState,
 CucsStorageProtocol,
 CucsStorageRaidBatteryOperabilityQualifier,
 CucsStorageReadType,
 CucsStorageSelectionDecisionType,
 CucsStorageSelectionResultType,
 CucsStorageSystemFsmCurrentFsm,
 CucsStorageSystemFsmStageName,
 CucsStorageSystemFsmTaskItem,
 CucsStorageTargetPath,
 CucsStorageTechnology,
 CucsStorageUnitOperState,
 CucsStorageVDriveState,
 CucsStorageVdChangeQualifierType,
 CucsStorageVdMemberConfigQualifierType,
 CucsStorageVirtualDriveRefAdminState,
 CucsStorageVsanRefSwitchId,
 CucsVnicConfigIssues) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsAaaConfigState",
    "CucsConditionRemoteInvRslt",
    "CucsEquipmentOperability",
    "CucsEquipmentPowerState",
    "CucsEquipmentPresence",
    "CucsEquipmentSensorThresholdStatus",
    "CucsFabricZoningState",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsFsmLifecycle",
    "CucsLstorageBootDevice",
    "CucsPolicyPolicyOwner",
    "CucsStorageAccessType",
    "CucsStorageActualWriteType",
    "CucsStorageAdminActionTrigger",
    "CucsStorageAdminActionType",
    "CucsStorageAdminCtrlActionType",
    "CucsStorageAdminState",
    "CucsStorageBatteryType",
    "CucsStorageBbuStatus",
    "CucsStorageBootableType",
    "CucsStorageCacheType",
    "CucsStorageConfigCheckPoint",
    "CucsStorageConfigState",
    "CucsStorageConfiguration",
    "CucsStorageConfiguredWriteType",
    "CucsStorageConnectionProtocol",
    "CucsStorageControllerFaultMonitoring",
    "CucsStorageControllerId",
    "CucsStorageControllerPinnedCacheStatus",
    "CucsStorageControllerStatus",
    "CucsStorageControllerType",
    "CucsStorageDeployAction",
    "CucsStorageDiskEnvStatsHistThresholded",
    "CucsStorageDiskEnvStatsThresholded",
    "CucsStorageDiskRole",
    "CucsStorageDisklessAction",
    "CucsStorageEnclosureId",
    "CucsStorageEpAccess",
    "CucsStorageEtherIfVlanType",
    "CucsStorageFFCardHealth",
    "CucsStorageFFCardMode",
    "CucsStorageFFCardSizeMismatch",
    "CucsStorageFFCardState",
    "CucsStorageFFCardSync",
    "CucsStorageFFCardWriteEnable",
    "CucsStorageFFControllerHealth",
    "CucsStorageFFControllerState",
    "CucsStorageFFDriveRemovable",
    "CucsStorageFFDriveState",
    "CucsStorageFFDriveType",
    "CucsStorageFFDriveVisible",
    "CucsStorageFFFormatRunning",
    "CucsStorageFFHasError",
    "CucsStorageFFRAIDHealth",
    "CucsStorageFFRAIDState",
    "CucsStorageFFRWType",
    "CucsStorageFFRaidSyncSupport",
    "CucsStorageFFSlotENUM",
    "CucsStorageFFType",
    "CucsStorageFcZoningType",
    "CucsStorageFileSystemStatus",
    "CucsStorageFlexFlashControllerFsmCurrentFsm",
    "CucsStorageFlexFlashControllerFsmStageName",
    "CucsStorageFlexFlashControllerFsmTaskItem",
    "CucsStorageFlexFlashControllerId",
    "CucsStorageIOType",
    "CucsStorageIniGroupOperProtocol",
    "CucsStorageIniGroupOwner",
    "CucsStorageIniGroupProtocol",
    "CucsStorageKeyType",
    "CucsStorageLearnCycleRequested",
    "CucsStorageLearnMode",
    "CucsStorageLinkSpeed",
    "CucsStorageLocalDiskConfigFlexFlashRAIDReportingState",
    "CucsStorageLocalDiskConfigFlexFlashState",
    "CucsStorageLocalDiskMode",
    "CucsStorageLunType",
    "CucsStorageOperState",
    "CucsStorageOperatingModeType",
    "CucsStorageOperationRequestType",
    "CucsStorageOperationState",
    "CucsStorageOperationStateType",
    "CucsStorageOperationType",
    "CucsStorageOptionRomBootStatus",
    "CucsStoragePDriveStatus",
    "CucsStoragePowerState",
    "CucsStorageProtocol",
    "CucsStorageRaidBatteryOperabilityQualifier",
    "CucsStorageReadType",
    "CucsStorageSelectionDecisionType",
    "CucsStorageSelectionResultType",
    "CucsStorageSystemFsmCurrentFsm",
    "CucsStorageSystemFsmStageName",
    "CucsStorageSystemFsmTaskItem",
    "CucsStorageTargetPath",
    "CucsStorageTechnology",
    "CucsStorageUnitOperState",
    "CucsStorageVDriveState",
    "CucsStorageVdChangeQualifierType",
    "CucsStorageVdMemberConfigQualifierType",
    "CucsStorageVirtualDriveRefAdminState",
    "CucsStorageVsanRefSwitchId",
    "CucsVnicConfigIssues")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsStorageObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsStorageControllerTable_Object = MibTable
cucsStorageControllerTable = _CucsStorageControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1)
)
if mibBuilder.loadTexts:
    cucsStorageControllerTable.setStatus("current")
_CucsStorageControllerEntry_Object = MibTableRow
cucsStorageControllerEntry = _CucsStorageControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1)
)
cucsStorageControllerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageControllerEntry.setStatus("current")
_CucsStorageControllerInstanceId_Type = CucsManagedObjectId
_CucsStorageControllerInstanceId_Object = MibTableColumn
cucsStorageControllerInstanceId = _CucsStorageControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 1),
    _CucsStorageControllerInstanceId_Type()
)
cucsStorageControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageControllerInstanceId.setStatus("current")
_CucsStorageControllerDn_Type = CucsManagedObjectDn
_CucsStorageControllerDn_Object = MibTableColumn
cucsStorageControllerDn = _CucsStorageControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 2),
    _CucsStorageControllerDn_Type()
)
cucsStorageControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerDn.setStatus("current")
_CucsStorageControllerRn_Type = SnmpAdminString
_CucsStorageControllerRn_Object = MibTableColumn
cucsStorageControllerRn = _CucsStorageControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 3),
    _CucsStorageControllerRn_Type()
)
cucsStorageControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerRn.setStatus("current")
_CucsStorageControllerId_Type = CucsStorageControllerId
_CucsStorageControllerId_Object = MibTableColumn
cucsStorageControllerId = _CucsStorageControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 4),
    _CucsStorageControllerId_Type()
)
cucsStorageControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerId.setStatus("current")
_CucsStorageControllerModel_Type = SnmpAdminString
_CucsStorageControllerModel_Object = MibTableColumn
cucsStorageControllerModel = _CucsStorageControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 5),
    _CucsStorageControllerModel_Type()
)
cucsStorageControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerModel.setStatus("current")
_CucsStorageControllerOperState_Type = CucsEquipmentOperability
_CucsStorageControllerOperState_Object = MibTableColumn
cucsStorageControllerOperState = _CucsStorageControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 6),
    _CucsStorageControllerOperState_Type()
)
cucsStorageControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerOperState.setStatus("current")
_CucsStorageControllerOperability_Type = CucsEquipmentOperability
_CucsStorageControllerOperability_Object = MibTableColumn
cucsStorageControllerOperability = _CucsStorageControllerOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 7),
    _CucsStorageControllerOperability_Type()
)
cucsStorageControllerOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerOperability.setStatus("current")
_CucsStorageControllerPciAddr_Type = SnmpAdminString
_CucsStorageControllerPciAddr_Object = MibTableColumn
cucsStorageControllerPciAddr = _CucsStorageControllerPciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 8),
    _CucsStorageControllerPciAddr_Type()
)
cucsStorageControllerPciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerPciAddr.setStatus("current")
_CucsStorageControllerPciSlot_Type = SnmpAdminString
_CucsStorageControllerPciSlot_Object = MibTableColumn
cucsStorageControllerPciSlot = _CucsStorageControllerPciSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 9),
    _CucsStorageControllerPciSlot_Type()
)
cucsStorageControllerPciSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerPciSlot.setStatus("current")
_CucsStorageControllerPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsStorageControllerPerf_Object = MibTableColumn
cucsStorageControllerPerf = _CucsStorageControllerPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 10),
    _CucsStorageControllerPerf_Type()
)
cucsStorageControllerPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerPerf.setStatus("current")
_CucsStorageControllerPower_Type = CucsEquipmentPowerState
_CucsStorageControllerPower_Object = MibTableColumn
cucsStorageControllerPower = _CucsStorageControllerPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 11),
    _CucsStorageControllerPower_Type()
)
cucsStorageControllerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerPower.setStatus("current")
_CucsStorageControllerPresence_Type = CucsEquipmentPresence
_CucsStorageControllerPresence_Object = MibTableColumn
cucsStorageControllerPresence = _CucsStorageControllerPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 12),
    _CucsStorageControllerPresence_Type()
)
cucsStorageControllerPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerPresence.setStatus("current")
_CucsStorageControllerRevision_Type = SnmpAdminString
_CucsStorageControllerRevision_Object = MibTableColumn
cucsStorageControllerRevision = _CucsStorageControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 13),
    _CucsStorageControllerRevision_Type()
)
cucsStorageControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerRevision.setStatus("current")
_CucsStorageControllerSerial_Type = SnmpAdminString
_CucsStorageControllerSerial_Object = MibTableColumn
cucsStorageControllerSerial = _CucsStorageControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 14),
    _CucsStorageControllerSerial_Type()
)
cucsStorageControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerSerial.setStatus("current")
_CucsStorageControllerThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsStorageControllerThermal_Object = MibTableColumn
cucsStorageControllerThermal = _CucsStorageControllerThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 15),
    _CucsStorageControllerThermal_Type()
)
cucsStorageControllerThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerThermal.setStatus("current")
_CucsStorageControllerType_Type = CucsStorageControllerType
_CucsStorageControllerType_Object = MibTableColumn
cucsStorageControllerType = _CucsStorageControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 16),
    _CucsStorageControllerType_Type()
)
cucsStorageControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerType.setStatus("current")
_CucsStorageControllerVendor_Type = SnmpAdminString
_CucsStorageControllerVendor_Object = MibTableColumn
cucsStorageControllerVendor = _CucsStorageControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 17),
    _CucsStorageControllerVendor_Type()
)
cucsStorageControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerVendor.setStatus("current")
_CucsStorageControllerVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsStorageControllerVoltage_Object = MibTableColumn
cucsStorageControllerVoltage = _CucsStorageControllerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 18),
    _CucsStorageControllerVoltage_Type()
)
cucsStorageControllerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerVoltage.setStatus("current")
_CucsStorageControllerRaidSupport_Type = SnmpAdminString
_CucsStorageControllerRaidSupport_Object = MibTableColumn
cucsStorageControllerRaidSupport = _CucsStorageControllerRaidSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 19),
    _CucsStorageControllerRaidSupport_Type()
)
cucsStorageControllerRaidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerRaidSupport.setStatus("current")
_CucsStorageControllerFaultMonitoring_Type = CucsStorageControllerFaultMonitoring
_CucsStorageControllerFaultMonitoring_Object = MibTableColumn
cucsStorageControllerFaultMonitoring = _CucsStorageControllerFaultMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 20),
    _CucsStorageControllerFaultMonitoring_Type()
)
cucsStorageControllerFaultMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerFaultMonitoring.setStatus("current")
_CucsStorageControllerHwRevision_Type = SnmpAdminString
_CucsStorageControllerHwRevision_Object = MibTableColumn
cucsStorageControllerHwRevision = _CucsStorageControllerHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 21),
    _CucsStorageControllerHwRevision_Type()
)
cucsStorageControllerHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerHwRevision.setStatus("current")
_CucsStorageControllerDeviceRaidSupport_Type = SnmpAdminString
_CucsStorageControllerDeviceRaidSupport_Object = MibTableColumn
cucsStorageControllerDeviceRaidSupport = _CucsStorageControllerDeviceRaidSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 23),
    _CucsStorageControllerDeviceRaidSupport_Type()
)
cucsStorageControllerDeviceRaidSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerDeviceRaidSupport.setStatus("current")
_CucsStorageControllerOperQualifierReason_Type = SnmpAdminString
_CucsStorageControllerOperQualifierReason_Object = MibTableColumn
cucsStorageControllerOperQualifierReason = _CucsStorageControllerOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 24),
    _CucsStorageControllerOperQualifierReason_Type()
)
cucsStorageControllerOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerOperQualifierReason.setStatus("current")
_CucsStorageControllerControllerStatus_Type = CucsStorageControllerStatus
_CucsStorageControllerControllerStatus_Object = MibTableColumn
cucsStorageControllerControllerStatus = _CucsStorageControllerControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 25),
    _CucsStorageControllerControllerStatus_Type()
)
cucsStorageControllerControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerControllerStatus.setStatus("current")
_CucsStorageControllerLc_Type = CucsFsmLifecycle
_CucsStorageControllerLc_Object = MibTableColumn
cucsStorageControllerLc = _CucsStorageControllerLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 26),
    _CucsStorageControllerLc_Type()
)
cucsStorageControllerLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerLc.setStatus("current")
_CucsStorageControllerOobControllerId_Type = Gauge32
_CucsStorageControllerOobControllerId_Object = MibTableColumn
cucsStorageControllerOobControllerId = _CucsStorageControllerOobControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 27),
    _CucsStorageControllerOobControllerId_Type()
)
cucsStorageControllerOobControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerOobControllerId.setStatus("current")
_CucsStorageControllerOobInterfaceSupported_Type = TruthValue
_CucsStorageControllerOobInterfaceSupported_Object = MibTableColumn
cucsStorageControllerOobInterfaceSupported = _CucsStorageControllerOobInterfaceSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 28),
    _CucsStorageControllerOobInterfaceSupported_Type()
)
cucsStorageControllerOobInterfaceSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerOobInterfaceSupported.setStatus("current")
_CucsStorageControllerRebuildRate_Type = Gauge32
_CucsStorageControllerRebuildRate_Object = MibTableColumn
cucsStorageControllerRebuildRate = _CucsStorageControllerRebuildRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 29),
    _CucsStorageControllerRebuildRate_Type()
)
cucsStorageControllerRebuildRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerRebuildRate.setStatus("current")
_CucsStorageControllerLocationDn_Type = SnmpAdminString
_CucsStorageControllerLocationDn_Object = MibTableColumn
cucsStorageControllerLocationDn = _CucsStorageControllerLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 30),
    _CucsStorageControllerLocationDn_Type()
)
cucsStorageControllerLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerLocationDn.setStatus("current")
_CucsStorageControllerPartNumber_Type = SnmpAdminString
_CucsStorageControllerPartNumber_Object = MibTableColumn
cucsStorageControllerPartNumber = _CucsStorageControllerPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 31),
    _CucsStorageControllerPartNumber_Type()
)
cucsStorageControllerPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerPartNumber.setStatus("current")
_CucsStorageControllerVid_Type = SnmpAdminString
_CucsStorageControllerVid_Object = MibTableColumn
cucsStorageControllerVid = _CucsStorageControllerVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 32),
    _CucsStorageControllerVid_Type()
)
cucsStorageControllerVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerVid.setStatus("current")
_CucsStorageControllerAdminAction_Type = CucsStorageAdminCtrlActionType
_CucsStorageControllerAdminAction_Object = MibTableColumn
cucsStorageControllerAdminAction = _CucsStorageControllerAdminAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 33),
    _CucsStorageControllerAdminAction_Type()
)
cucsStorageControllerAdminAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerAdminAction.setStatus("current")
_CucsStorageControllerAdminActionTrigger_Type = CucsStorageAdminActionTrigger
_CucsStorageControllerAdminActionTrigger_Object = MibTableColumn
cucsStorageControllerAdminActionTrigger = _CucsStorageControllerAdminActionTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 34),
    _CucsStorageControllerAdminActionTrigger_Type()
)
cucsStorageControllerAdminActionTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerAdminActionTrigger.setStatus("current")
_CucsStorageControllerConfigState_Type = CucsStorageConfigState
_CucsStorageControllerConfigState_Object = MibTableColumn
cucsStorageControllerConfigState = _CucsStorageControllerConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 35),
    _CucsStorageControllerConfigState_Type()
)
cucsStorageControllerConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerConfigState.setStatus("current")
_CucsStorageControllerOpromBootStatus_Type = CucsStorageOptionRomBootStatus
_CucsStorageControllerOpromBootStatus_Object = MibTableColumn
cucsStorageControllerOpromBootStatus = _CucsStorageControllerOpromBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 36),
    _CucsStorageControllerOpromBootStatus_Type()
)
cucsStorageControllerOpromBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerOpromBootStatus.setStatus("current")
_CucsStorageControllerPciSlotRawName_Type = SnmpAdminString
_CucsStorageControllerPciSlotRawName_Object = MibTableColumn
cucsStorageControllerPciSlotRawName = _CucsStorageControllerPciSlotRawName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 37),
    _CucsStorageControllerPciSlotRawName_Type()
)
cucsStorageControllerPciSlotRawName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerPciSlotRawName.setStatus("current")
_CucsStorageControllerIdCount_Type = Gauge32
_CucsStorageControllerIdCount_Object = MibTableColumn
cucsStorageControllerIdCount = _CucsStorageControllerIdCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 38),
    _CucsStorageControllerIdCount_Type()
)
cucsStorageControllerIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerIdCount.setStatus("current")
_CucsStorageControllerPinnedCacheStatus_Type = CucsStorageControllerPinnedCacheStatus
_CucsStorageControllerPinnedCacheStatus_Object = MibTableColumn
cucsStorageControllerPinnedCacheStatus = _CucsStorageControllerPinnedCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 1, 1, 39),
    _CucsStorageControllerPinnedCacheStatus_Type()
)
cucsStorageControllerPinnedCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageControllerPinnedCacheStatus.setStatus("current")
_CucsStorageDriveTable_Object = MibTable
cucsStorageDriveTable = _CucsStorageDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 2)
)
if mibBuilder.loadTexts:
    cucsStorageDriveTable.setStatus("current")
_CucsStorageDriveEntry_Object = MibTableRow
cucsStorageDriveEntry = _CucsStorageDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 2, 1)
)
cucsStorageDriveEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageDriveInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageDriveEntry.setStatus("current")
_CucsStorageDriveInstanceId_Type = CucsManagedObjectId
_CucsStorageDriveInstanceId_Object = MibTableColumn
cucsStorageDriveInstanceId = _CucsStorageDriveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 2, 1, 1),
    _CucsStorageDriveInstanceId_Type()
)
cucsStorageDriveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageDriveInstanceId.setStatus("current")
_CucsStorageDriveDn_Type = CucsManagedObjectDn
_CucsStorageDriveDn_Object = MibTableColumn
cucsStorageDriveDn = _CucsStorageDriveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 2, 1, 2),
    _CucsStorageDriveDn_Type()
)
cucsStorageDriveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDriveDn.setStatus("current")
_CucsStorageDriveRn_Type = SnmpAdminString
_CucsStorageDriveRn_Object = MibTableColumn
cucsStorageDriveRn = _CucsStorageDriveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 2, 1, 3),
    _CucsStorageDriveRn_Type()
)
cucsStorageDriveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDriveRn.setStatus("current")
_CucsStorageDriveId_Type = Gauge32
_CucsStorageDriveId_Object = MibTableColumn
cucsStorageDriveId = _CucsStorageDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 2, 1, 4),
    _CucsStorageDriveId_Type()
)
cucsStorageDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDriveId.setStatus("current")
_CucsStorageDriveModel_Type = SnmpAdminString
_CucsStorageDriveModel_Object = MibTableColumn
cucsStorageDriveModel = _CucsStorageDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 2, 1, 5),
    _CucsStorageDriveModel_Type()
)
cucsStorageDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDriveModel.setStatus("current")
_CucsStorageDrivePciAddr_Type = SnmpAdminString
_CucsStorageDrivePciAddr_Object = MibTableColumn
cucsStorageDrivePciAddr = _CucsStorageDrivePciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 2, 1, 6),
    _CucsStorageDrivePciAddr_Type()
)
cucsStorageDrivePciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDrivePciAddr.setStatus("current")
_CucsStorageDriveRevision_Type = SnmpAdminString
_CucsStorageDriveRevision_Object = MibTableColumn
cucsStorageDriveRevision = _CucsStorageDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 2, 1, 7),
    _CucsStorageDriveRevision_Type()
)
cucsStorageDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDriveRevision.setStatus("current")
_CucsStorageDriveSerial_Type = SnmpAdminString
_CucsStorageDriveSerial_Object = MibTableColumn
cucsStorageDriveSerial = _CucsStorageDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 2, 1, 8),
    _CucsStorageDriveSerial_Type()
)
cucsStorageDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDriveSerial.setStatus("current")
_CucsStorageDriveVendor_Type = SnmpAdminString
_CucsStorageDriveVendor_Object = MibTableColumn
cucsStorageDriveVendor = _CucsStorageDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 2, 1, 9),
    _CucsStorageDriveVendor_Type()
)
cucsStorageDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDriveVendor.setStatus("current")
_CucsStorageItemTable_Object = MibTable
cucsStorageItemTable = _CucsStorageItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 3)
)
if mibBuilder.loadTexts:
    cucsStorageItemTable.setStatus("current")
_CucsStorageItemEntry_Object = MibTableRow
cucsStorageItemEntry = _CucsStorageItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 3, 1)
)
cucsStorageItemEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageItemInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageItemEntry.setStatus("current")
_CucsStorageItemInstanceId_Type = CucsManagedObjectId
_CucsStorageItemInstanceId_Object = MibTableColumn
cucsStorageItemInstanceId = _CucsStorageItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 3, 1, 1),
    _CucsStorageItemInstanceId_Type()
)
cucsStorageItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageItemInstanceId.setStatus("current")
_CucsStorageItemDn_Type = CucsManagedObjectDn
_CucsStorageItemDn_Object = MibTableColumn
cucsStorageItemDn = _CucsStorageItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 3, 1, 2),
    _CucsStorageItemDn_Type()
)
cucsStorageItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageItemDn.setStatus("current")
_CucsStorageItemRn_Type = SnmpAdminString
_CucsStorageItemRn_Object = MibTableColumn
cucsStorageItemRn = _CucsStorageItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 3, 1, 3),
    _CucsStorageItemRn_Type()
)
cucsStorageItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageItemRn.setStatus("current")
_CucsStorageItemName_Type = SnmpAdminString
_CucsStorageItemName_Object = MibTableColumn
cucsStorageItemName = _CucsStorageItemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 3, 1, 4),
    _CucsStorageItemName_Type()
)
cucsStorageItemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageItemName.setStatus("current")
_CucsStorageItemSize_Type = Unsigned64
_CucsStorageItemSize_Object = MibTableColumn
cucsStorageItemSize = _CucsStorageItemSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 3, 1, 5),
    _CucsStorageItemSize_Type()
)
cucsStorageItemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageItemSize.setStatus("current")
_CucsStorageItemUsed_Type = Gauge32
_CucsStorageItemUsed_Object = MibTableColumn
cucsStorageItemUsed = _CucsStorageItemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 3, 1, 6),
    _CucsStorageItemUsed_Type()
)
cucsStorageItemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageItemUsed.setStatus("current")
_CucsStorageItemOperState_Type = CucsStorageFileSystemStatus
_CucsStorageItemOperState_Object = MibTableColumn
cucsStorageItemOperState = _CucsStorageItemOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 3, 1, 7),
    _CucsStorageItemOperState_Type()
)
cucsStorageItemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageItemOperState.setStatus("current")
_CucsStorageLocalDiskTable_Object = MibTable
cucsStorageLocalDiskTable = _CucsStorageLocalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4)
)
if mibBuilder.loadTexts:
    cucsStorageLocalDiskTable.setStatus("current")
_CucsStorageLocalDiskEntry_Object = MibTableRow
cucsStorageLocalDiskEntry = _CucsStorageLocalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1)
)
cucsStorageLocalDiskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageLocalDiskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageLocalDiskEntry.setStatus("current")
_CucsStorageLocalDiskInstanceId_Type = CucsManagedObjectId
_CucsStorageLocalDiskInstanceId_Object = MibTableColumn
cucsStorageLocalDiskInstanceId = _CucsStorageLocalDiskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 1),
    _CucsStorageLocalDiskInstanceId_Type()
)
cucsStorageLocalDiskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskInstanceId.setStatus("current")
_CucsStorageLocalDiskDn_Type = CucsManagedObjectDn
_CucsStorageLocalDiskDn_Object = MibTableColumn
cucsStorageLocalDiskDn = _CucsStorageLocalDiskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 2),
    _CucsStorageLocalDiskDn_Type()
)
cucsStorageLocalDiskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskDn.setStatus("current")
_CucsStorageLocalDiskRn_Type = SnmpAdminString
_CucsStorageLocalDiskRn_Object = MibTableColumn
cucsStorageLocalDiskRn = _CucsStorageLocalDiskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 3),
    _CucsStorageLocalDiskRn_Type()
)
cucsStorageLocalDiskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskRn.setStatus("current")
_CucsStorageLocalDiskBlockSize_Type = Gauge32
_CucsStorageLocalDiskBlockSize_Object = MibTableColumn
cucsStorageLocalDiskBlockSize = _CucsStorageLocalDiskBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 4),
    _CucsStorageLocalDiskBlockSize_Type()
)
cucsStorageLocalDiskBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskBlockSize.setStatus("current")
_CucsStorageLocalDiskConnectionProtocol_Type = CucsStorageConnectionProtocol
_CucsStorageLocalDiskConnectionProtocol_Object = MibTableColumn
cucsStorageLocalDiskConnectionProtocol = _CucsStorageLocalDiskConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 5),
    _CucsStorageLocalDiskConnectionProtocol_Type()
)
cucsStorageLocalDiskConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConnectionProtocol.setStatus("current")
_CucsStorageLocalDiskId_Type = Gauge32
_CucsStorageLocalDiskId_Object = MibTableColumn
cucsStorageLocalDiskId = _CucsStorageLocalDiskId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 6),
    _CucsStorageLocalDiskId_Type()
)
cucsStorageLocalDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskId.setStatus("current")
_CucsStorageLocalDiskModel_Type = SnmpAdminString
_CucsStorageLocalDiskModel_Object = MibTableColumn
cucsStorageLocalDiskModel = _CucsStorageLocalDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 7),
    _CucsStorageLocalDiskModel_Type()
)
cucsStorageLocalDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskModel.setStatus("current")
_CucsStorageLocalDiskNumberOfBlocks_Type = Unsigned64
_CucsStorageLocalDiskNumberOfBlocks_Object = MibTableColumn
cucsStorageLocalDiskNumberOfBlocks = _CucsStorageLocalDiskNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 8),
    _CucsStorageLocalDiskNumberOfBlocks_Type()
)
cucsStorageLocalDiskNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskNumberOfBlocks.setStatus("current")
_CucsStorageLocalDiskOperability_Type = CucsEquipmentOperability
_CucsStorageLocalDiskOperability_Object = MibTableColumn
cucsStorageLocalDiskOperability = _CucsStorageLocalDiskOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 9),
    _CucsStorageLocalDiskOperability_Type()
)
cucsStorageLocalDiskOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskOperability.setStatus("current")
_CucsStorageLocalDiskPresence_Type = CucsEquipmentPresence
_CucsStorageLocalDiskPresence_Object = MibTableColumn
cucsStorageLocalDiskPresence = _CucsStorageLocalDiskPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 10),
    _CucsStorageLocalDiskPresence_Type()
)
cucsStorageLocalDiskPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPresence.setStatus("current")
_CucsStorageLocalDiskRevision_Type = SnmpAdminString
_CucsStorageLocalDiskRevision_Object = MibTableColumn
cucsStorageLocalDiskRevision = _CucsStorageLocalDiskRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 11),
    _CucsStorageLocalDiskRevision_Type()
)
cucsStorageLocalDiskRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskRevision.setStatus("current")
_CucsStorageLocalDiskSerial_Type = SnmpAdminString
_CucsStorageLocalDiskSerial_Object = MibTableColumn
cucsStorageLocalDiskSerial = _CucsStorageLocalDiskSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 12),
    _CucsStorageLocalDiskSerial_Type()
)
cucsStorageLocalDiskSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSerial.setStatus("current")
_CucsStorageLocalDiskSize_Type = Unsigned64
_CucsStorageLocalDiskSize_Object = MibTableColumn
cucsStorageLocalDiskSize = _CucsStorageLocalDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 13),
    _CucsStorageLocalDiskSize_Type()
)
cucsStorageLocalDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSize.setStatus("current")
_CucsStorageLocalDiskVendor_Type = SnmpAdminString
_CucsStorageLocalDiskVendor_Object = MibTableColumn
cucsStorageLocalDiskVendor = _CucsStorageLocalDiskVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 14),
    _CucsStorageLocalDiskVendor_Type()
)
cucsStorageLocalDiskVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskVendor.setStatus("current")
_CucsStorageLocalDiskLc_Type = CucsFsmLifecycle
_CucsStorageLocalDiskLc_Object = MibTableColumn
cucsStorageLocalDiskLc = _CucsStorageLocalDiskLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 15),
    _CucsStorageLocalDiskLc_Type()
)
cucsStorageLocalDiskLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskLc.setStatus("current")
_CucsStorageLocalDiskOperQualifierReason_Type = SnmpAdminString
_CucsStorageLocalDiskOperQualifierReason_Object = MibTableColumn
cucsStorageLocalDiskOperQualifierReason = _CucsStorageLocalDiskOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 16),
    _CucsStorageLocalDiskOperQualifierReason_Type()
)
cucsStorageLocalDiskOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskOperQualifierReason.setStatus("current")
_CucsStorageLocalDiskDeviceType_Type = CucsStorageTechnology
_CucsStorageLocalDiskDeviceType_Object = MibTableColumn
cucsStorageLocalDiskDeviceType = _CucsStorageLocalDiskDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 17),
    _CucsStorageLocalDiskDeviceType_Type()
)
cucsStorageLocalDiskDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskDeviceType.setStatus("current")
_CucsStorageLocalDiskDiskState_Type = CucsStoragePDriveStatus
_CucsStorageLocalDiskDiskState_Object = MibTableColumn
cucsStorageLocalDiskDiskState = _CucsStorageLocalDiskDiskState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 18),
    _CucsStorageLocalDiskDiskState_Type()
)
cucsStorageLocalDiskDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskDiskState.setStatus("current")
_CucsStorageLocalDiskLinkSpeed_Type = CucsStorageLinkSpeed
_CucsStorageLocalDiskLinkSpeed_Object = MibTableColumn
cucsStorageLocalDiskLinkSpeed = _CucsStorageLocalDiskLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 19),
    _CucsStorageLocalDiskLinkSpeed_Type()
)
cucsStorageLocalDiskLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskLinkSpeed.setStatus("current")
_CucsStorageLocalDiskPowerState_Type = CucsStoragePowerState
_CucsStorageLocalDiskPowerState_Object = MibTableColumn
cucsStorageLocalDiskPowerState = _CucsStorageLocalDiskPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 20),
    _CucsStorageLocalDiskPowerState_Type()
)
cucsStorageLocalDiskPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPowerState.setStatus("current")
_CucsStorageLocalDiskAdminAction_Type = CucsStorageAdminActionType
_CucsStorageLocalDiskAdminAction_Object = MibTableColumn
cucsStorageLocalDiskAdminAction = _CucsStorageLocalDiskAdminAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 21),
    _CucsStorageLocalDiskAdminAction_Type()
)
cucsStorageLocalDiskAdminAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskAdminAction.setStatus("current")
_CucsStorageLocalDiskAdminActionTrigger_Type = CucsStorageAdminActionTrigger
_CucsStorageLocalDiskAdminActionTrigger_Object = MibTableColumn
cucsStorageLocalDiskAdminActionTrigger = _CucsStorageLocalDiskAdminActionTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 22),
    _CucsStorageLocalDiskAdminActionTrigger_Type()
)
cucsStorageLocalDiskAdminActionTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskAdminActionTrigger.setStatus("current")
_CucsStorageLocalDiskBootable_Type = CucsStorageBootableType
_CucsStorageLocalDiskBootable_Object = MibTableColumn
cucsStorageLocalDiskBootable = _CucsStorageLocalDiskBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 23),
    _CucsStorageLocalDiskBootable_Type()
)
cucsStorageLocalDiskBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskBootable.setStatus("current")
_CucsStorageLocalDiskConfigState_Type = CucsStorageConfigState
_CucsStorageLocalDiskConfigState_Object = MibTableColumn
cucsStorageLocalDiskConfigState = _CucsStorageLocalDiskConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 24),
    _CucsStorageLocalDiskConfigState_Type()
)
cucsStorageLocalDiskConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigState.setStatus("current")
_CucsStorageLocalDiskThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsStorageLocalDiskThermal_Object = MibTableColumn
cucsStorageLocalDiskThermal = _CucsStorageLocalDiskThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 25),
    _CucsStorageLocalDiskThermal_Type()
)
cucsStorageLocalDiskThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskThermal.setStatus("current")
_CucsStorageLocalDiskAdminVirtualDriveId_Type = Gauge32
_CucsStorageLocalDiskAdminVirtualDriveId_Object = MibTableColumn
cucsStorageLocalDiskAdminVirtualDriveId = _CucsStorageLocalDiskAdminVirtualDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 26),
    _CucsStorageLocalDiskAdminVirtualDriveId_Type()
)
cucsStorageLocalDiskAdminVirtualDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskAdminVirtualDriveId.setStatus("current")
_CucsStorageLocalDiskConfigCheckPoint_Type = CucsStorageConfigCheckPoint
_CucsStorageLocalDiskConfigCheckPoint_Object = MibTableColumn
cucsStorageLocalDiskConfigCheckPoint = _CucsStorageLocalDiskConfigCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 4, 1, 27),
    _CucsStorageLocalDiskConfigCheckPoint_Type()
)
cucsStorageLocalDiskConfigCheckPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigCheckPoint.setStatus("current")
_CucsStorageLocalDiskConfigDefTable_Object = MibTable
cucsStorageLocalDiskConfigDefTable = _CucsStorageLocalDiskConfigDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5)
)
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefTable.setStatus("current")
_CucsStorageLocalDiskConfigDefEntry_Object = MibTableRow
cucsStorageLocalDiskConfigDefEntry = _CucsStorageLocalDiskConfigDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1)
)
cucsStorageLocalDiskConfigDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageLocalDiskConfigDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefEntry.setStatus("current")
_CucsStorageLocalDiskConfigDefInstanceId_Type = CucsManagedObjectId
_CucsStorageLocalDiskConfigDefInstanceId_Object = MibTableColumn
cucsStorageLocalDiskConfigDefInstanceId = _CucsStorageLocalDiskConfigDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1, 1),
    _CucsStorageLocalDiskConfigDefInstanceId_Type()
)
cucsStorageLocalDiskConfigDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefInstanceId.setStatus("current")
_CucsStorageLocalDiskConfigDefDn_Type = CucsManagedObjectDn
_CucsStorageLocalDiskConfigDefDn_Object = MibTableColumn
cucsStorageLocalDiskConfigDefDn = _CucsStorageLocalDiskConfigDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1, 2),
    _CucsStorageLocalDiskConfigDefDn_Type()
)
cucsStorageLocalDiskConfigDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefDn.setStatus("current")
_CucsStorageLocalDiskConfigDefRn_Type = SnmpAdminString
_CucsStorageLocalDiskConfigDefRn_Object = MibTableColumn
cucsStorageLocalDiskConfigDefRn = _CucsStorageLocalDiskConfigDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1, 3),
    _CucsStorageLocalDiskConfigDefRn_Type()
)
cucsStorageLocalDiskConfigDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefRn.setStatus("current")
_CucsStorageLocalDiskConfigDefDescr_Type = SnmpAdminString
_CucsStorageLocalDiskConfigDefDescr_Object = MibTableColumn
cucsStorageLocalDiskConfigDefDescr = _CucsStorageLocalDiskConfigDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1, 4),
    _CucsStorageLocalDiskConfigDefDescr_Type()
)
cucsStorageLocalDiskConfigDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefDescr.setStatus("current")
_CucsStorageLocalDiskConfigDefIntId_Type = SnmpAdminString
_CucsStorageLocalDiskConfigDefIntId_Object = MibTableColumn
cucsStorageLocalDiskConfigDefIntId = _CucsStorageLocalDiskConfigDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1, 5),
    _CucsStorageLocalDiskConfigDefIntId_Type()
)
cucsStorageLocalDiskConfigDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefIntId.setStatus("current")
_CucsStorageLocalDiskConfigDefMode_Type = CucsStorageLocalDiskMode
_CucsStorageLocalDiskConfigDefMode_Object = MibTableColumn
cucsStorageLocalDiskConfigDefMode = _CucsStorageLocalDiskConfigDefMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1, 6),
    _CucsStorageLocalDiskConfigDefMode_Type()
)
cucsStorageLocalDiskConfigDefMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefMode.setStatus("current")
_CucsStorageLocalDiskConfigDefName_Type = SnmpAdminString
_CucsStorageLocalDiskConfigDefName_Object = MibTableColumn
cucsStorageLocalDiskConfigDefName = _CucsStorageLocalDiskConfigDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1, 7),
    _CucsStorageLocalDiskConfigDefName_Type()
)
cucsStorageLocalDiskConfigDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefName.setStatus("current")
_CucsStorageLocalDiskConfigDefProtectConfig_Type = TruthValue
_CucsStorageLocalDiskConfigDefProtectConfig_Object = MibTableColumn
cucsStorageLocalDiskConfigDefProtectConfig = _CucsStorageLocalDiskConfigDefProtectConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1, 8),
    _CucsStorageLocalDiskConfigDefProtectConfig_Type()
)
cucsStorageLocalDiskConfigDefProtectConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefProtectConfig.setStatus("current")
_CucsStorageLocalDiskConfigDefPolicyLevel_Type = Gauge32
_CucsStorageLocalDiskConfigDefPolicyLevel_Object = MibTableColumn
cucsStorageLocalDiskConfigDefPolicyLevel = _CucsStorageLocalDiskConfigDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1, 9),
    _CucsStorageLocalDiskConfigDefPolicyLevel_Type()
)
cucsStorageLocalDiskConfigDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefPolicyLevel.setStatus("current")
_CucsStorageLocalDiskConfigDefPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStorageLocalDiskConfigDefPolicyOwner_Object = MibTableColumn
cucsStorageLocalDiskConfigDefPolicyOwner = _CucsStorageLocalDiskConfigDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1, 10),
    _CucsStorageLocalDiskConfigDefPolicyOwner_Type()
)
cucsStorageLocalDiskConfigDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefPolicyOwner.setStatus("current")
_CucsStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Type = CucsStorageLocalDiskConfigFlexFlashRAIDReportingState
_CucsStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Object = MibTableColumn
cucsStorageLocalDiskConfigDefFlexFlashRAIDReportingState = _CucsStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1, 11),
    _CucsStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Type()
)
cucsStorageLocalDiskConfigDefFlexFlashRAIDReportingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefFlexFlashRAIDReportingState.setStatus("current")
_CucsStorageLocalDiskConfigDefFlexFlashState_Type = CucsStorageLocalDiskConfigFlexFlashState
_CucsStorageLocalDiskConfigDefFlexFlashState_Object = MibTableColumn
cucsStorageLocalDiskConfigDefFlexFlashState = _CucsStorageLocalDiskConfigDefFlexFlashState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 5, 1, 12),
    _CucsStorageLocalDiskConfigDefFlexFlashState_Type()
)
cucsStorageLocalDiskConfigDefFlexFlashState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigDefFlexFlashState.setStatus("current")
_CucsStorageLocalDiskConfigPolicyTable_Object = MibTable
cucsStorageLocalDiskConfigPolicyTable = _CucsStorageLocalDiskConfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6)
)
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyTable.setStatus("current")
_CucsStorageLocalDiskConfigPolicyEntry_Object = MibTableRow
cucsStorageLocalDiskConfigPolicyEntry = _CucsStorageLocalDiskConfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1)
)
cucsStorageLocalDiskConfigPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageLocalDiskConfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyEntry.setStatus("current")
_CucsStorageLocalDiskConfigPolicyInstanceId_Type = CucsManagedObjectId
_CucsStorageLocalDiskConfigPolicyInstanceId_Object = MibTableColumn
cucsStorageLocalDiskConfigPolicyInstanceId = _CucsStorageLocalDiskConfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1, 1),
    _CucsStorageLocalDiskConfigPolicyInstanceId_Type()
)
cucsStorageLocalDiskConfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyInstanceId.setStatus("current")
_CucsStorageLocalDiskConfigPolicyDn_Type = CucsManagedObjectDn
_CucsStorageLocalDiskConfigPolicyDn_Object = MibTableColumn
cucsStorageLocalDiskConfigPolicyDn = _CucsStorageLocalDiskConfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1, 2),
    _CucsStorageLocalDiskConfigPolicyDn_Type()
)
cucsStorageLocalDiskConfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyDn.setStatus("current")
_CucsStorageLocalDiskConfigPolicyRn_Type = SnmpAdminString
_CucsStorageLocalDiskConfigPolicyRn_Object = MibTableColumn
cucsStorageLocalDiskConfigPolicyRn = _CucsStorageLocalDiskConfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1, 3),
    _CucsStorageLocalDiskConfigPolicyRn_Type()
)
cucsStorageLocalDiskConfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyRn.setStatus("current")
_CucsStorageLocalDiskConfigPolicyDescr_Type = SnmpAdminString
_CucsStorageLocalDiskConfigPolicyDescr_Object = MibTableColumn
cucsStorageLocalDiskConfigPolicyDescr = _CucsStorageLocalDiskConfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1, 4),
    _CucsStorageLocalDiskConfigPolicyDescr_Type()
)
cucsStorageLocalDiskConfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyDescr.setStatus("current")
_CucsStorageLocalDiskConfigPolicyIntId_Type = SnmpAdminString
_CucsStorageLocalDiskConfigPolicyIntId_Object = MibTableColumn
cucsStorageLocalDiskConfigPolicyIntId = _CucsStorageLocalDiskConfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1, 5),
    _CucsStorageLocalDiskConfigPolicyIntId_Type()
)
cucsStorageLocalDiskConfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyIntId.setStatus("current")
_CucsStorageLocalDiskConfigPolicyMode_Type = CucsStorageLocalDiskMode
_CucsStorageLocalDiskConfigPolicyMode_Object = MibTableColumn
cucsStorageLocalDiskConfigPolicyMode = _CucsStorageLocalDiskConfigPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1, 6),
    _CucsStorageLocalDiskConfigPolicyMode_Type()
)
cucsStorageLocalDiskConfigPolicyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyMode.setStatus("current")
_CucsStorageLocalDiskConfigPolicyName_Type = SnmpAdminString
_CucsStorageLocalDiskConfigPolicyName_Object = MibTableColumn
cucsStorageLocalDiskConfigPolicyName = _CucsStorageLocalDiskConfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1, 7),
    _CucsStorageLocalDiskConfigPolicyName_Type()
)
cucsStorageLocalDiskConfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyName.setStatus("current")
_CucsStorageLocalDiskConfigPolicyProtectConfig_Type = TruthValue
_CucsStorageLocalDiskConfigPolicyProtectConfig_Object = MibTableColumn
cucsStorageLocalDiskConfigPolicyProtectConfig = _CucsStorageLocalDiskConfigPolicyProtectConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1, 8),
    _CucsStorageLocalDiskConfigPolicyProtectConfig_Type()
)
cucsStorageLocalDiskConfigPolicyProtectConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyProtectConfig.setStatus("current")
_CucsStorageLocalDiskConfigPolicyPolicyLevel_Type = Gauge32
_CucsStorageLocalDiskConfigPolicyPolicyLevel_Object = MibTableColumn
cucsStorageLocalDiskConfigPolicyPolicyLevel = _CucsStorageLocalDiskConfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1, 9),
    _CucsStorageLocalDiskConfigPolicyPolicyLevel_Type()
)
cucsStorageLocalDiskConfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyPolicyLevel.setStatus("current")
_CucsStorageLocalDiskConfigPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStorageLocalDiskConfigPolicyPolicyOwner_Object = MibTableColumn
cucsStorageLocalDiskConfigPolicyPolicyOwner = _CucsStorageLocalDiskConfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1, 10),
    _CucsStorageLocalDiskConfigPolicyPolicyOwner_Type()
)
cucsStorageLocalDiskConfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyPolicyOwner.setStatus("current")
_CucsStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Type = CucsStorageLocalDiskConfigFlexFlashRAIDReportingState
_CucsStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Object = MibTableColumn
cucsStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState = _CucsStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1, 11),
    _CucsStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Type()
)
cucsStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState.setStatus("current")
_CucsStorageLocalDiskConfigPolicyFlexFlashState_Type = CucsStorageLocalDiskConfigFlexFlashState
_CucsStorageLocalDiskConfigPolicyFlexFlashState_Object = MibTableColumn
cucsStorageLocalDiskConfigPolicyFlexFlashState = _CucsStorageLocalDiskConfigPolicyFlexFlashState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 6, 1, 12),
    _CucsStorageLocalDiskConfigPolicyFlexFlashState_Type()
)
cucsStorageLocalDiskConfigPolicyFlexFlashState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskConfigPolicyFlexFlashState.setStatus("current")
_CucsStorageLocalDiskPartitionTable_Object = MibTable
cucsStorageLocalDiskPartitionTable = _CucsStorageLocalDiskPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7)
)
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionTable.setStatus("current")
_CucsStorageLocalDiskPartitionEntry_Object = MibTableRow
cucsStorageLocalDiskPartitionEntry = _CucsStorageLocalDiskPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7, 1)
)
cucsStorageLocalDiskPartitionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageLocalDiskPartitionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionEntry.setStatus("current")
_CucsStorageLocalDiskPartitionInstanceId_Type = CucsManagedObjectId
_CucsStorageLocalDiskPartitionInstanceId_Object = MibTableColumn
cucsStorageLocalDiskPartitionInstanceId = _CucsStorageLocalDiskPartitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7, 1, 1),
    _CucsStorageLocalDiskPartitionInstanceId_Type()
)
cucsStorageLocalDiskPartitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionInstanceId.setStatus("current")
_CucsStorageLocalDiskPartitionDn_Type = CucsManagedObjectDn
_CucsStorageLocalDiskPartitionDn_Object = MibTableColumn
cucsStorageLocalDiskPartitionDn = _CucsStorageLocalDiskPartitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7, 1, 2),
    _CucsStorageLocalDiskPartitionDn_Type()
)
cucsStorageLocalDiskPartitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionDn.setStatus("current")
_CucsStorageLocalDiskPartitionRn_Type = SnmpAdminString
_CucsStorageLocalDiskPartitionRn_Object = MibTableColumn
cucsStorageLocalDiskPartitionRn = _CucsStorageLocalDiskPartitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7, 1, 3),
    _CucsStorageLocalDiskPartitionRn_Type()
)
cucsStorageLocalDiskPartitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionRn.setStatus("current")
_CucsStorageLocalDiskPartitionName_Type = SnmpAdminString
_CucsStorageLocalDiskPartitionName_Object = MibTableColumn
cucsStorageLocalDiskPartitionName = _CucsStorageLocalDiskPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7, 1, 6),
    _CucsStorageLocalDiskPartitionName_Type()
)
cucsStorageLocalDiskPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionName.setStatus("current")
_CucsStorageLocalDiskPartitionSize_Type = Unsigned64
_CucsStorageLocalDiskPartitionSize_Object = MibTableColumn
cucsStorageLocalDiskPartitionSize = _CucsStorageLocalDiskPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7, 1, 8),
    _CucsStorageLocalDiskPartitionSize_Type()
)
cucsStorageLocalDiskPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionSize.setStatus("current")
_CucsStorageLocalDiskPartitionType_Type = Gauge32
_CucsStorageLocalDiskPartitionType_Object = MibTableColumn
cucsStorageLocalDiskPartitionType = _CucsStorageLocalDiskPartitionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7, 1, 9),
    _CucsStorageLocalDiskPartitionType_Type()
)
cucsStorageLocalDiskPartitionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionType.setStatus("current")
_CucsStorageLocalDiskPartitionBootable_Type = CucsStorageBootableType
_CucsStorageLocalDiskPartitionBootable_Object = MibTableColumn
cucsStorageLocalDiskPartitionBootable = _CucsStorageLocalDiskPartitionBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7, 1, 12),
    _CucsStorageLocalDiskPartitionBootable_Type()
)
cucsStorageLocalDiskPartitionBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionBootable.setStatus("current")
_CucsStorageLocalDiskPartitionId_Type = Gauge32
_CucsStorageLocalDiskPartitionId_Object = MibTableColumn
cucsStorageLocalDiskPartitionId = _CucsStorageLocalDiskPartitionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7, 1, 13),
    _CucsStorageLocalDiskPartitionId_Type()
)
cucsStorageLocalDiskPartitionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionId.setStatus("current")
_CucsStorageLocalDiskPartitionPartitionEnd_Type = Unsigned64
_CucsStorageLocalDiskPartitionPartitionEnd_Object = MibTableColumn
cucsStorageLocalDiskPartitionPartitionEnd = _CucsStorageLocalDiskPartitionPartitionEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7, 1, 14),
    _CucsStorageLocalDiskPartitionPartitionEnd_Type()
)
cucsStorageLocalDiskPartitionPartitionEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionPartitionEnd.setStatus("current")
_CucsStorageLocalDiskPartitionPartitionStart_Type = Unsigned64
_CucsStorageLocalDiskPartitionPartitionStart_Object = MibTableColumn
cucsStorageLocalDiskPartitionPartitionStart = _CucsStorageLocalDiskPartitionPartitionStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7, 1, 15),
    _CucsStorageLocalDiskPartitionPartitionStart_Type()
)
cucsStorageLocalDiskPartitionPartitionStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionPartitionStart.setStatus("current")
_CucsStorageLocalDiskPartitionRawTypeDesc_Type = SnmpAdminString
_CucsStorageLocalDiskPartitionRawTypeDesc_Object = MibTableColumn
cucsStorageLocalDiskPartitionRawTypeDesc = _CucsStorageLocalDiskPartitionRawTypeDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 7, 1, 16),
    _CucsStorageLocalDiskPartitionRawTypeDesc_Type()
)
cucsStorageLocalDiskPartitionRawTypeDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskPartitionRawTypeDesc.setStatus("current")
_CucsStorageLocalLunTable_Object = MibTable
cucsStorageLocalLunTable = _CucsStorageLocalLunTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8)
)
if mibBuilder.loadTexts:
    cucsStorageLocalLunTable.setStatus("current")
_CucsStorageLocalLunEntry_Object = MibTableRow
cucsStorageLocalLunEntry = _CucsStorageLocalLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1)
)
cucsStorageLocalLunEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageLocalLunInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageLocalLunEntry.setStatus("current")
_CucsStorageLocalLunInstanceId_Type = CucsManagedObjectId
_CucsStorageLocalLunInstanceId_Object = MibTableColumn
cucsStorageLocalLunInstanceId = _CucsStorageLocalLunInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 1),
    _CucsStorageLocalLunInstanceId_Type()
)
cucsStorageLocalLunInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageLocalLunInstanceId.setStatus("current")
_CucsStorageLocalLunDn_Type = CucsManagedObjectDn
_CucsStorageLocalLunDn_Object = MibTableColumn
cucsStorageLocalLunDn = _CucsStorageLocalLunDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 2),
    _CucsStorageLocalLunDn_Type()
)
cucsStorageLocalLunDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunDn.setStatus("current")
_CucsStorageLocalLunRn_Type = SnmpAdminString
_CucsStorageLocalLunRn_Object = MibTableColumn
cucsStorageLocalLunRn = _CucsStorageLocalLunRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 3),
    _CucsStorageLocalLunRn_Type()
)
cucsStorageLocalLunRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunRn.setStatus("current")
_CucsStorageLocalLunBlockSize_Type = Gauge32
_CucsStorageLocalLunBlockSize_Object = MibTableColumn
cucsStorageLocalLunBlockSize = _CucsStorageLocalLunBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 4),
    _CucsStorageLocalLunBlockSize_Type()
)
cucsStorageLocalLunBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunBlockSize.setStatus("current")
_CucsStorageLocalLunConnectionProtocol_Type = CucsStorageConnectionProtocol
_CucsStorageLocalLunConnectionProtocol_Object = MibTableColumn
cucsStorageLocalLunConnectionProtocol = _CucsStorageLocalLunConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 5),
    _CucsStorageLocalLunConnectionProtocol_Type()
)
cucsStorageLocalLunConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunConnectionProtocol.setStatus("current")
_CucsStorageLocalLunId_Type = Gauge32
_CucsStorageLocalLunId_Object = MibTableColumn
cucsStorageLocalLunId = _CucsStorageLocalLunId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 6),
    _CucsStorageLocalLunId_Type()
)
cucsStorageLocalLunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunId.setStatus("current")
_CucsStorageLocalLunModel_Type = SnmpAdminString
_CucsStorageLocalLunModel_Object = MibTableColumn
cucsStorageLocalLunModel = _CucsStorageLocalLunModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 7),
    _CucsStorageLocalLunModel_Type()
)
cucsStorageLocalLunModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunModel.setStatus("current")
_CucsStorageLocalLunNumberOfBlocks_Type = Unsigned64
_CucsStorageLocalLunNumberOfBlocks_Object = MibTableColumn
cucsStorageLocalLunNumberOfBlocks = _CucsStorageLocalLunNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 8),
    _CucsStorageLocalLunNumberOfBlocks_Type()
)
cucsStorageLocalLunNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunNumberOfBlocks.setStatus("current")
_CucsStorageLocalLunOperability_Type = CucsEquipmentOperability
_CucsStorageLocalLunOperability_Object = MibTableColumn
cucsStorageLocalLunOperability = _CucsStorageLocalLunOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 9),
    _CucsStorageLocalLunOperability_Type()
)
cucsStorageLocalLunOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunOperability.setStatus("current")
_CucsStorageLocalLunPresence_Type = CucsEquipmentPresence
_CucsStorageLocalLunPresence_Object = MibTableColumn
cucsStorageLocalLunPresence = _CucsStorageLocalLunPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 10),
    _CucsStorageLocalLunPresence_Type()
)
cucsStorageLocalLunPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunPresence.setStatus("current")
_CucsStorageLocalLunRevision_Type = SnmpAdminString
_CucsStorageLocalLunRevision_Object = MibTableColumn
cucsStorageLocalLunRevision = _CucsStorageLocalLunRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 11),
    _CucsStorageLocalLunRevision_Type()
)
cucsStorageLocalLunRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunRevision.setStatus("current")
_CucsStorageLocalLunSerial_Type = SnmpAdminString
_CucsStorageLocalLunSerial_Object = MibTableColumn
cucsStorageLocalLunSerial = _CucsStorageLocalLunSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 12),
    _CucsStorageLocalLunSerial_Type()
)
cucsStorageLocalLunSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunSerial.setStatus("current")
_CucsStorageLocalLunSize_Type = Unsigned64
_CucsStorageLocalLunSize_Object = MibTableColumn
cucsStorageLocalLunSize = _CucsStorageLocalLunSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 13),
    _CucsStorageLocalLunSize_Type()
)
cucsStorageLocalLunSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunSize.setStatus("current")
_CucsStorageLocalLunType_Type = CucsStorageLunType
_CucsStorageLocalLunType_Object = MibTableColumn
cucsStorageLocalLunType = _CucsStorageLocalLunType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 14),
    _CucsStorageLocalLunType_Type()
)
cucsStorageLocalLunType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunType.setStatus("current")
_CucsStorageLocalLunVendor_Type = SnmpAdminString
_CucsStorageLocalLunVendor_Object = MibTableColumn
cucsStorageLocalLunVendor = _CucsStorageLocalLunVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 15),
    _CucsStorageLocalLunVendor_Type()
)
cucsStorageLocalLunVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunVendor.setStatus("current")
_CucsStorageLocalLunLc_Type = CucsFsmLifecycle
_CucsStorageLocalLunLc_Object = MibTableColumn
cucsStorageLocalLunLc = _CucsStorageLocalLunLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 16),
    _CucsStorageLocalLunLc_Type()
)
cucsStorageLocalLunLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunLc.setStatus("current")
_CucsStorageLocalLunOperQualifierReason_Type = SnmpAdminString
_CucsStorageLocalLunOperQualifierReason_Object = MibTableColumn
cucsStorageLocalLunOperQualifierReason = _CucsStorageLocalLunOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 8, 1, 17),
    _CucsStorageLocalLunOperQualifierReason_Type()
)
cucsStorageLocalLunOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalLunOperQualifierReason.setStatus("current")
_CucsStorageLunDiskTable_Object = MibTable
cucsStorageLunDiskTable = _CucsStorageLunDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 9)
)
if mibBuilder.loadTexts:
    cucsStorageLunDiskTable.setStatus("current")
_CucsStorageLunDiskEntry_Object = MibTableRow
cucsStorageLunDiskEntry = _CucsStorageLunDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 9, 1)
)
cucsStorageLunDiskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageLunDiskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageLunDiskEntry.setStatus("current")
_CucsStorageLunDiskInstanceId_Type = CucsManagedObjectId
_CucsStorageLunDiskInstanceId_Object = MibTableColumn
cucsStorageLunDiskInstanceId = _CucsStorageLunDiskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 9, 1, 1),
    _CucsStorageLunDiskInstanceId_Type()
)
cucsStorageLunDiskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageLunDiskInstanceId.setStatus("current")
_CucsStorageLunDiskDn_Type = CucsManagedObjectDn
_CucsStorageLunDiskDn_Object = MibTableColumn
cucsStorageLunDiskDn = _CucsStorageLunDiskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 9, 1, 2),
    _CucsStorageLunDiskDn_Type()
)
cucsStorageLunDiskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLunDiskDn.setStatus("current")
_CucsStorageLunDiskRn_Type = SnmpAdminString
_CucsStorageLunDiskRn_Object = MibTableColumn
cucsStorageLunDiskRn = _CucsStorageLunDiskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 9, 1, 3),
    _CucsStorageLunDiskRn_Type()
)
cucsStorageLunDiskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLunDiskRn.setStatus("current")
_CucsStorageLunDiskId_Type = Gauge32
_CucsStorageLunDiskId_Object = MibTableColumn
cucsStorageLunDiskId = _CucsStorageLunDiskId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 9, 1, 4),
    _CucsStorageLunDiskId_Type()
)
cucsStorageLunDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLunDiskId.setStatus("current")
_CucsStorageQualTable_Object = MibTable
cucsStorageQualTable = _CucsStorageQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10)
)
if mibBuilder.loadTexts:
    cucsStorageQualTable.setStatus("current")
_CucsStorageQualEntry_Object = MibTableRow
cucsStorageQualEntry = _CucsStorageQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1)
)
cucsStorageQualEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageQualInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageQualEntry.setStatus("current")
_CucsStorageQualInstanceId_Type = CucsManagedObjectId
_CucsStorageQualInstanceId_Object = MibTableColumn
cucsStorageQualInstanceId = _CucsStorageQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1, 1),
    _CucsStorageQualInstanceId_Type()
)
cucsStorageQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageQualInstanceId.setStatus("current")
_CucsStorageQualDn_Type = CucsManagedObjectDn
_CucsStorageQualDn_Object = MibTableColumn
cucsStorageQualDn = _CucsStorageQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1, 2),
    _CucsStorageQualDn_Type()
)
cucsStorageQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageQualDn.setStatus("current")
_CucsStorageQualRn_Type = SnmpAdminString
_CucsStorageQualRn_Object = MibTableColumn
cucsStorageQualRn = _CucsStorageQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1, 3),
    _CucsStorageQualRn_Type()
)
cucsStorageQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageQualRn.setStatus("current")
_CucsStorageQualBlockSize_Type = Gauge32
_CucsStorageQualBlockSize_Object = MibTableColumn
cucsStorageQualBlockSize = _CucsStorageQualBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1, 4),
    _CucsStorageQualBlockSize_Type()
)
cucsStorageQualBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageQualBlockSize.setStatus("current")
_CucsStorageQualMaxCap_Type = Unsigned64
_CucsStorageQualMaxCap_Object = MibTableColumn
cucsStorageQualMaxCap = _CucsStorageQualMaxCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1, 5),
    _CucsStorageQualMaxCap_Type()
)
cucsStorageQualMaxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageQualMaxCap.setStatus("current")
_CucsStorageQualMinCap_Type = Unsigned64
_CucsStorageQualMinCap_Object = MibTableColumn
cucsStorageQualMinCap = _CucsStorageQualMinCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1, 6),
    _CucsStorageQualMinCap_Type()
)
cucsStorageQualMinCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageQualMinCap.setStatus("current")
_CucsStorageQualNumberOfBlocks_Type = Unsigned64
_CucsStorageQualNumberOfBlocks_Object = MibTableColumn
cucsStorageQualNumberOfBlocks = _CucsStorageQualNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1, 7),
    _CucsStorageQualNumberOfBlocks_Type()
)
cucsStorageQualNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageQualNumberOfBlocks.setStatus("current")
_CucsStorageQualPerDiskCap_Type = Unsigned64
_CucsStorageQualPerDiskCap_Object = MibTableColumn
cucsStorageQualPerDiskCap = _CucsStorageQualPerDiskCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1, 8),
    _CucsStorageQualPerDiskCap_Type()
)
cucsStorageQualPerDiskCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageQualPerDiskCap.setStatus("current")
_CucsStorageQualUnits_Type = Gauge32
_CucsStorageQualUnits_Object = MibTableColumn
cucsStorageQualUnits = _CucsStorageQualUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1, 9),
    _CucsStorageQualUnits_Type()
)
cucsStorageQualUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageQualUnits.setStatus("current")
_CucsStorageQualDiskless_Type = CucsStorageDisklessAction
_CucsStorageQualDiskless_Object = MibTableColumn
cucsStorageQualDiskless = _CucsStorageQualDiskless_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1, 10),
    _CucsStorageQualDiskless_Type()
)
cucsStorageQualDiskless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageQualDiskless.setStatus("current")
_CucsStorageQualNumberOfFlexFlashCards_Type = Integer32
_CucsStorageQualNumberOfFlexFlashCards_Object = MibTableColumn
cucsStorageQualNumberOfFlexFlashCards = _CucsStorageQualNumberOfFlexFlashCards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1, 11),
    _CucsStorageQualNumberOfFlexFlashCards_Type()
)
cucsStorageQualNumberOfFlexFlashCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageQualNumberOfFlexFlashCards.setStatus("current")
_CucsStorageQualDiskType_Type = CucsStorageTechnology
_CucsStorageQualDiskType_Object = MibTableColumn
cucsStorageQualDiskType = _CucsStorageQualDiskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 10, 1, 12),
    _CucsStorageQualDiskType_Type()
)
cucsStorageQualDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageQualDiskType.setStatus("current")
_CucsStorageRaidBatteryTable_Object = MibTable
cucsStorageRaidBatteryTable = _CucsStorageRaidBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11)
)
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryTable.setStatus("current")
_CucsStorageRaidBatteryEntry_Object = MibTableRow
cucsStorageRaidBatteryEntry = _CucsStorageRaidBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1)
)
cucsStorageRaidBatteryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageRaidBatteryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryEntry.setStatus("current")
_CucsStorageRaidBatteryInstanceId_Type = CucsManagedObjectId
_CucsStorageRaidBatteryInstanceId_Object = MibTableColumn
cucsStorageRaidBatteryInstanceId = _CucsStorageRaidBatteryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 1),
    _CucsStorageRaidBatteryInstanceId_Type()
)
cucsStorageRaidBatteryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryInstanceId.setStatus("current")
_CucsStorageRaidBatteryDn_Type = CucsManagedObjectDn
_CucsStorageRaidBatteryDn_Object = MibTableColumn
cucsStorageRaidBatteryDn = _CucsStorageRaidBatteryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 2),
    _CucsStorageRaidBatteryDn_Type()
)
cucsStorageRaidBatteryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryDn.setStatus("current")
_CucsStorageRaidBatteryRn_Type = SnmpAdminString
_CucsStorageRaidBatteryRn_Object = MibTableColumn
cucsStorageRaidBatteryRn = _CucsStorageRaidBatteryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 3),
    _CucsStorageRaidBatteryRn_Type()
)
cucsStorageRaidBatteryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryRn.setStatus("current")
_CucsStorageRaidBatteryBlockSize_Type = Gauge32
_CucsStorageRaidBatteryBlockSize_Object = MibTableColumn
cucsStorageRaidBatteryBlockSize = _CucsStorageRaidBatteryBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 4),
    _CucsStorageRaidBatteryBlockSize_Type()
)
cucsStorageRaidBatteryBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryBlockSize.setStatus("current")
_CucsStorageRaidBatteryConnectionProtocol_Type = CucsStorageConnectionProtocol
_CucsStorageRaidBatteryConnectionProtocol_Object = MibTableColumn
cucsStorageRaidBatteryConnectionProtocol = _CucsStorageRaidBatteryConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 5),
    _CucsStorageRaidBatteryConnectionProtocol_Type()
)
cucsStorageRaidBatteryConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryConnectionProtocol.setStatus("current")
_CucsStorageRaidBatteryId_Type = Gauge32
_CucsStorageRaidBatteryId_Object = MibTableColumn
cucsStorageRaidBatteryId = _CucsStorageRaidBatteryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 6),
    _CucsStorageRaidBatteryId_Type()
)
cucsStorageRaidBatteryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryId.setStatus("current")
_CucsStorageRaidBatteryModel_Type = SnmpAdminString
_CucsStorageRaidBatteryModel_Object = MibTableColumn
cucsStorageRaidBatteryModel = _CucsStorageRaidBatteryModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 7),
    _CucsStorageRaidBatteryModel_Type()
)
cucsStorageRaidBatteryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryModel.setStatus("current")
_CucsStorageRaidBatteryNumberOfBlocks_Type = Unsigned64
_CucsStorageRaidBatteryNumberOfBlocks_Object = MibTableColumn
cucsStorageRaidBatteryNumberOfBlocks = _CucsStorageRaidBatteryNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 8),
    _CucsStorageRaidBatteryNumberOfBlocks_Type()
)
cucsStorageRaidBatteryNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryNumberOfBlocks.setStatus("current")
_CucsStorageRaidBatteryOperability_Type = CucsEquipmentOperability
_CucsStorageRaidBatteryOperability_Object = MibTableColumn
cucsStorageRaidBatteryOperability = _CucsStorageRaidBatteryOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 9),
    _CucsStorageRaidBatteryOperability_Type()
)
cucsStorageRaidBatteryOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryOperability.setStatus("current")
_CucsStorageRaidBatteryPresence_Type = CucsEquipmentPresence
_CucsStorageRaidBatteryPresence_Object = MibTableColumn
cucsStorageRaidBatteryPresence = _CucsStorageRaidBatteryPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 10),
    _CucsStorageRaidBatteryPresence_Type()
)
cucsStorageRaidBatteryPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryPresence.setStatus("current")
_CucsStorageRaidBatteryRevision_Type = SnmpAdminString
_CucsStorageRaidBatteryRevision_Object = MibTableColumn
cucsStorageRaidBatteryRevision = _CucsStorageRaidBatteryRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 11),
    _CucsStorageRaidBatteryRevision_Type()
)
cucsStorageRaidBatteryRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryRevision.setStatus("current")
_CucsStorageRaidBatterySerial_Type = SnmpAdminString
_CucsStorageRaidBatterySerial_Object = MibTableColumn
cucsStorageRaidBatterySerial = _CucsStorageRaidBatterySerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 12),
    _CucsStorageRaidBatterySerial_Type()
)
cucsStorageRaidBatterySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatterySerial.setStatus("current")
_CucsStorageRaidBatterySize_Type = Unsigned64
_CucsStorageRaidBatterySize_Object = MibTableColumn
cucsStorageRaidBatterySize = _CucsStorageRaidBatterySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 13),
    _CucsStorageRaidBatterySize_Type()
)
cucsStorageRaidBatterySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatterySize.setStatus("current")
_CucsStorageRaidBatteryVendor_Type = SnmpAdminString
_CucsStorageRaidBatteryVendor_Object = MibTableColumn
cucsStorageRaidBatteryVendor = _CucsStorageRaidBatteryVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 14),
    _CucsStorageRaidBatteryVendor_Type()
)
cucsStorageRaidBatteryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryVendor.setStatus("current")
_CucsStorageRaidBatteryOperQualifierReason_Type = SnmpAdminString
_CucsStorageRaidBatteryOperQualifierReason_Object = MibTableColumn
cucsStorageRaidBatteryOperQualifierReason = _CucsStorageRaidBatteryOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 15),
    _CucsStorageRaidBatteryOperQualifierReason_Type()
)
cucsStorageRaidBatteryOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryOperQualifierReason.setStatus("current")
_CucsStorageRaidBatteryBatteryType_Type = CucsStorageBatteryType
_CucsStorageRaidBatteryBatteryType_Object = MibTableColumn
cucsStorageRaidBatteryBatteryType = _CucsStorageRaidBatteryBatteryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 16),
    _CucsStorageRaidBatteryBatteryType_Type()
)
cucsStorageRaidBatteryBatteryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryBatteryType.setStatus("current")
_CucsStorageRaidBatteryCapacityPercentage_Type = Gauge32
_CucsStorageRaidBatteryCapacityPercentage_Object = MibTableColumn
cucsStorageRaidBatteryCapacityPercentage = _CucsStorageRaidBatteryCapacityPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 17),
    _CucsStorageRaidBatteryCapacityPercentage_Type()
)
cucsStorageRaidBatteryCapacityPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryCapacityPercentage.setStatus("current")
_CucsStorageRaidBatteryOperabilityQualifier_Type = CucsStorageRaidBatteryOperabilityQualifier
_CucsStorageRaidBatteryOperabilityQualifier_Object = MibTableColumn
cucsStorageRaidBatteryOperabilityQualifier = _CucsStorageRaidBatteryOperabilityQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 18),
    _CucsStorageRaidBatteryOperabilityQualifier_Type()
)
cucsStorageRaidBatteryOperabilityQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryOperabilityQualifier.setStatus("current")
_CucsStorageRaidBatteryOperabilityQualifierReason_Type = SnmpAdminString
_CucsStorageRaidBatteryOperabilityQualifierReason_Object = MibTableColumn
cucsStorageRaidBatteryOperabilityQualifierReason = _CucsStorageRaidBatteryOperabilityQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 19),
    _CucsStorageRaidBatteryOperabilityQualifierReason_Type()
)
cucsStorageRaidBatteryOperabilityQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryOperabilityQualifierReason.setStatus("current")
_CucsStorageRaidBatteryTemperature_Type = Integer32
_CucsStorageRaidBatteryTemperature_Object = MibTableColumn
cucsStorageRaidBatteryTemperature = _CucsStorageRaidBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 20),
    _CucsStorageRaidBatteryTemperature_Type()
)
cucsStorageRaidBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryTemperature.setStatus("current")
_CucsStorageRaidBatteryBbuStatus_Type = CucsStorageBbuStatus
_CucsStorageRaidBatteryBbuStatus_Object = MibTableColumn
cucsStorageRaidBatteryBbuStatus = _CucsStorageRaidBatteryBbuStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 21),
    _CucsStorageRaidBatteryBbuStatus_Type()
)
cucsStorageRaidBatteryBbuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryBbuStatus.setStatus("current")
_CucsStorageRaidBatteryLc_Type = CucsFsmLifecycle
_CucsStorageRaidBatteryLc_Object = MibTableColumn
cucsStorageRaidBatteryLc = _CucsStorageRaidBatteryLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 22),
    _CucsStorageRaidBatteryLc_Type()
)
cucsStorageRaidBatteryLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryLc.setStatus("current")
_CucsStorageRaidBatteryLearnCycleRequested_Type = CucsStorageLearnCycleRequested
_CucsStorageRaidBatteryLearnCycleRequested_Object = MibTableColumn
cucsStorageRaidBatteryLearnCycleRequested = _CucsStorageRaidBatteryLearnCycleRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 23),
    _CucsStorageRaidBatteryLearnCycleRequested_Type()
)
cucsStorageRaidBatteryLearnCycleRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryLearnCycleRequested.setStatus("current")
_CucsStorageRaidBatteryLearnMode_Type = CucsStorageLearnMode
_CucsStorageRaidBatteryLearnMode_Object = MibTableColumn
cucsStorageRaidBatteryLearnMode = _CucsStorageRaidBatteryLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 24),
    _CucsStorageRaidBatteryLearnMode_Type()
)
cucsStorageRaidBatteryLearnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryLearnMode.setStatus("current")
_CucsStorageRaidBatteryNextLearnCycleTs_Type = DateAndTime
_CucsStorageRaidBatteryNextLearnCycleTs_Object = MibTableColumn
cucsStorageRaidBatteryNextLearnCycleTs = _CucsStorageRaidBatteryNextLearnCycleTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 11, 1, 25),
    _CucsStorageRaidBatteryNextLearnCycleTs_Type()
)
cucsStorageRaidBatteryNextLearnCycleTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageRaidBatteryNextLearnCycleTs.setStatus("current")
_CucsStorageEnclosureTable_Object = MibTable
cucsStorageEnclosureTable = _CucsStorageEnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12)
)
if mibBuilder.loadTexts:
    cucsStorageEnclosureTable.setStatus("current")
_CucsStorageEnclosureEntry_Object = MibTableRow
cucsStorageEnclosureEntry = _CucsStorageEnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12, 1)
)
cucsStorageEnclosureEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageEnclosureInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageEnclosureEntry.setStatus("current")
_CucsStorageEnclosureInstanceId_Type = CucsManagedObjectId
_CucsStorageEnclosureInstanceId_Object = MibTableColumn
cucsStorageEnclosureInstanceId = _CucsStorageEnclosureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12, 1, 1),
    _CucsStorageEnclosureInstanceId_Type()
)
cucsStorageEnclosureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageEnclosureInstanceId.setStatus("current")
_CucsStorageEnclosureDn_Type = CucsManagedObjectDn
_CucsStorageEnclosureDn_Object = MibTableColumn
cucsStorageEnclosureDn = _CucsStorageEnclosureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12, 1, 2),
    _CucsStorageEnclosureDn_Type()
)
cucsStorageEnclosureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEnclosureDn.setStatus("current")
_CucsStorageEnclosureRn_Type = SnmpAdminString
_CucsStorageEnclosureRn_Object = MibTableColumn
cucsStorageEnclosureRn = _CucsStorageEnclosureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12, 1, 3),
    _CucsStorageEnclosureRn_Type()
)
cucsStorageEnclosureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEnclosureRn.setStatus("current")
_CucsStorageEnclosureId_Type = CucsStorageEnclosureId
_CucsStorageEnclosureId_Object = MibTableColumn
cucsStorageEnclosureId = _CucsStorageEnclosureId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12, 1, 4),
    _CucsStorageEnclosureId_Type()
)
cucsStorageEnclosureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEnclosureId.setStatus("current")
_CucsStorageEnclosureModel_Type = SnmpAdminString
_CucsStorageEnclosureModel_Object = MibTableColumn
cucsStorageEnclosureModel = _CucsStorageEnclosureModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12, 1, 5),
    _CucsStorageEnclosureModel_Type()
)
cucsStorageEnclosureModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEnclosureModel.setStatus("current")
_CucsStorageEnclosureNumSlots_Type = Gauge32
_CucsStorageEnclosureNumSlots_Object = MibTableColumn
cucsStorageEnclosureNumSlots = _CucsStorageEnclosureNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12, 1, 6),
    _CucsStorageEnclosureNumSlots_Type()
)
cucsStorageEnclosureNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEnclosureNumSlots.setStatus("current")
_CucsStorageEnclosureRevision_Type = SnmpAdminString
_CucsStorageEnclosureRevision_Object = MibTableColumn
cucsStorageEnclosureRevision = _CucsStorageEnclosureRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12, 1, 7),
    _CucsStorageEnclosureRevision_Type()
)
cucsStorageEnclosureRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEnclosureRevision.setStatus("current")
_CucsStorageEnclosureSerial_Type = SnmpAdminString
_CucsStorageEnclosureSerial_Object = MibTableColumn
cucsStorageEnclosureSerial = _CucsStorageEnclosureSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12, 1, 8),
    _CucsStorageEnclosureSerial_Type()
)
cucsStorageEnclosureSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEnclosureSerial.setStatus("current")
_CucsStorageEnclosureVendor_Type = SnmpAdminString
_CucsStorageEnclosureVendor_Object = MibTableColumn
cucsStorageEnclosureVendor = _CucsStorageEnclosureVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12, 1, 9),
    _CucsStorageEnclosureVendor_Type()
)
cucsStorageEnclosureVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEnclosureVendor.setStatus("current")
_CucsStorageEnclosureLc_Type = CucsFsmLifecycle
_CucsStorageEnclosureLc_Object = MibTableColumn
cucsStorageEnclosureLc = _CucsStorageEnclosureLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12, 1, 10),
    _CucsStorageEnclosureLc_Type()
)
cucsStorageEnclosureLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEnclosureLc.setStatus("current")
_CucsStorageEnclosureDescr_Type = SnmpAdminString
_CucsStorageEnclosureDescr_Object = MibTableColumn
cucsStorageEnclosureDescr = _CucsStorageEnclosureDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 12, 1, 11),
    _CucsStorageEnclosureDescr_Type()
)
cucsStorageEnclosureDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEnclosureDescr.setStatus("current")
_CucsStorageLocalDiskSlotEpTable_Object = MibTable
cucsStorageLocalDiskSlotEpTable = _CucsStorageLocalDiskSlotEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 13)
)
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSlotEpTable.setStatus("current")
_CucsStorageLocalDiskSlotEpEntry_Object = MibTableRow
cucsStorageLocalDiskSlotEpEntry = _CucsStorageLocalDiskSlotEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 13, 1)
)
cucsStorageLocalDiskSlotEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageLocalDiskSlotEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSlotEpEntry.setStatus("current")
_CucsStorageLocalDiskSlotEpInstanceId_Type = CucsManagedObjectId
_CucsStorageLocalDiskSlotEpInstanceId_Object = MibTableColumn
cucsStorageLocalDiskSlotEpInstanceId = _CucsStorageLocalDiskSlotEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 13, 1, 1),
    _CucsStorageLocalDiskSlotEpInstanceId_Type()
)
cucsStorageLocalDiskSlotEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSlotEpInstanceId.setStatus("current")
_CucsStorageLocalDiskSlotEpDn_Type = CucsManagedObjectDn
_CucsStorageLocalDiskSlotEpDn_Object = MibTableColumn
cucsStorageLocalDiskSlotEpDn = _CucsStorageLocalDiskSlotEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 13, 1, 2),
    _CucsStorageLocalDiskSlotEpDn_Type()
)
cucsStorageLocalDiskSlotEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSlotEpDn.setStatus("current")
_CucsStorageLocalDiskSlotEpRn_Type = SnmpAdminString
_CucsStorageLocalDiskSlotEpRn_Object = MibTableColumn
cucsStorageLocalDiskSlotEpRn = _CucsStorageLocalDiskSlotEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 13, 1, 3),
    _CucsStorageLocalDiskSlotEpRn_Type()
)
cucsStorageLocalDiskSlotEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSlotEpRn.setStatus("current")
_CucsStorageLocalDiskSlotEpConfiguration_Type = CucsStorageConfiguration
_CucsStorageLocalDiskSlotEpConfiguration_Object = MibTableColumn
cucsStorageLocalDiskSlotEpConfiguration = _CucsStorageLocalDiskSlotEpConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 13, 1, 4),
    _CucsStorageLocalDiskSlotEpConfiguration_Type()
)
cucsStorageLocalDiskSlotEpConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSlotEpConfiguration.setStatus("current")
_CucsStorageLocalDiskSlotEpId_Type = Gauge32
_CucsStorageLocalDiskSlotEpId_Object = MibTableColumn
cucsStorageLocalDiskSlotEpId = _CucsStorageLocalDiskSlotEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 13, 1, 5),
    _CucsStorageLocalDiskSlotEpId_Type()
)
cucsStorageLocalDiskSlotEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSlotEpId.setStatus("current")
_CucsStorageLocalDiskSlotEpOperability_Type = CucsEquipmentOperability
_CucsStorageLocalDiskSlotEpOperability_Object = MibTableColumn
cucsStorageLocalDiskSlotEpOperability = _CucsStorageLocalDiskSlotEpOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 13, 1, 6),
    _CucsStorageLocalDiskSlotEpOperability_Type()
)
cucsStorageLocalDiskSlotEpOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSlotEpOperability.setStatus("current")
_CucsStorageLocalDiskSlotEpPeerDn_Type = SnmpAdminString
_CucsStorageLocalDiskSlotEpPeerDn_Object = MibTableColumn
cucsStorageLocalDiskSlotEpPeerDn = _CucsStorageLocalDiskSlotEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 13, 1, 7),
    _CucsStorageLocalDiskSlotEpPeerDn_Type()
)
cucsStorageLocalDiskSlotEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSlotEpPeerDn.setStatus("current")
_CucsStorageLocalDiskSlotEpPresence_Type = CucsEquipmentPresence
_CucsStorageLocalDiskSlotEpPresence_Object = MibTableColumn
cucsStorageLocalDiskSlotEpPresence = _CucsStorageLocalDiskSlotEpPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 13, 1, 8),
    _CucsStorageLocalDiskSlotEpPresence_Type()
)
cucsStorageLocalDiskSlotEpPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSlotEpPresence.setStatus("current")
_CucsStorageLocalDiskSlotEpOperQualifierReason_Type = SnmpAdminString
_CucsStorageLocalDiskSlotEpOperQualifierReason_Object = MibTableColumn
cucsStorageLocalDiskSlotEpOperQualifierReason = _CucsStorageLocalDiskSlotEpOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 13, 1, 9),
    _CucsStorageLocalDiskSlotEpOperQualifierReason_Type()
)
cucsStorageLocalDiskSlotEpOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLocalDiskSlotEpOperQualifierReason.setStatus("current")
_CucsStorageAuthKeyTable_Object = MibTable
cucsStorageAuthKeyTable = _CucsStorageAuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14)
)
if mibBuilder.loadTexts:
    cucsStorageAuthKeyTable.setStatus("current")
_CucsStorageAuthKeyEntry_Object = MibTableRow
cucsStorageAuthKeyEntry = _CucsStorageAuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14, 1)
)
cucsStorageAuthKeyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageAuthKeyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageAuthKeyEntry.setStatus("current")
_CucsStorageAuthKeyInstanceId_Type = CucsManagedObjectId
_CucsStorageAuthKeyInstanceId_Object = MibTableColumn
cucsStorageAuthKeyInstanceId = _CucsStorageAuthKeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14, 1, 1),
    _CucsStorageAuthKeyInstanceId_Type()
)
cucsStorageAuthKeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageAuthKeyInstanceId.setStatus("current")
_CucsStorageAuthKeyDn_Type = CucsManagedObjectDn
_CucsStorageAuthKeyDn_Object = MibTableColumn
cucsStorageAuthKeyDn = _CucsStorageAuthKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14, 1, 2),
    _CucsStorageAuthKeyDn_Type()
)
cucsStorageAuthKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageAuthKeyDn.setStatus("current")
_CucsStorageAuthKeyRn_Type = SnmpAdminString
_CucsStorageAuthKeyRn_Object = MibTableColumn
cucsStorageAuthKeyRn = _CucsStorageAuthKeyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14, 1, 3),
    _CucsStorageAuthKeyRn_Type()
)
cucsStorageAuthKeyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageAuthKeyRn.setStatus("current")
_CucsStorageAuthKeyDescr_Type = SnmpAdminString
_CucsStorageAuthKeyDescr_Object = MibTableColumn
cucsStorageAuthKeyDescr = _CucsStorageAuthKeyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14, 1, 4),
    _CucsStorageAuthKeyDescr_Type()
)
cucsStorageAuthKeyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageAuthKeyDescr.setStatus("current")
_CucsStorageAuthKeyIntId_Type = SnmpAdminString
_CucsStorageAuthKeyIntId_Object = MibTableColumn
cucsStorageAuthKeyIntId = _CucsStorageAuthKeyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14, 1, 5),
    _CucsStorageAuthKeyIntId_Type()
)
cucsStorageAuthKeyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageAuthKeyIntId.setStatus("current")
_CucsStorageAuthKeyName_Type = SnmpAdminString
_CucsStorageAuthKeyName_Object = MibTableColumn
cucsStorageAuthKeyName = _CucsStorageAuthKeyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14, 1, 6),
    _CucsStorageAuthKeyName_Type()
)
cucsStorageAuthKeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageAuthKeyName.setStatus("current")
_CucsStorageAuthKeyPassword_Type = SnmpAdminString
_CucsStorageAuthKeyPassword_Object = MibTableColumn
cucsStorageAuthKeyPassword = _CucsStorageAuthKeyPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14, 1, 7),
    _CucsStorageAuthKeyPassword_Type()
)
cucsStorageAuthKeyPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageAuthKeyPassword.setStatus("current")
_CucsStorageAuthKeyPolicyLevel_Type = Gauge32
_CucsStorageAuthKeyPolicyLevel_Object = MibTableColumn
cucsStorageAuthKeyPolicyLevel = _CucsStorageAuthKeyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14, 1, 8),
    _CucsStorageAuthKeyPolicyLevel_Type()
)
cucsStorageAuthKeyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageAuthKeyPolicyLevel.setStatus("current")
_CucsStorageAuthKeyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStorageAuthKeyPolicyOwner_Object = MibTableColumn
cucsStorageAuthKeyPolicyOwner = _CucsStorageAuthKeyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14, 1, 9),
    _CucsStorageAuthKeyPolicyOwner_Type()
)
cucsStorageAuthKeyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageAuthKeyPolicyOwner.setStatus("current")
_CucsStorageAuthKeyType_Type = CucsStorageKeyType
_CucsStorageAuthKeyType_Object = MibTableColumn
cucsStorageAuthKeyType = _CucsStorageAuthKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14, 1, 10),
    _CucsStorageAuthKeyType_Type()
)
cucsStorageAuthKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageAuthKeyType.setStatus("current")
_CucsStorageAuthKeyUserId_Type = SnmpAdminString
_CucsStorageAuthKeyUserId_Object = MibTableColumn
cucsStorageAuthKeyUserId = _CucsStorageAuthKeyUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 14, 1, 11),
    _CucsStorageAuthKeyUserId_Type()
)
cucsStorageAuthKeyUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageAuthKeyUserId.setStatus("current")
_CucsStorageConnectionDefTable_Object = MibTable
cucsStorageConnectionDefTable = _CucsStorageConnectionDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 15)
)
if mibBuilder.loadTexts:
    cucsStorageConnectionDefTable.setStatus("current")
_CucsStorageConnectionDefEntry_Object = MibTableRow
cucsStorageConnectionDefEntry = _CucsStorageConnectionDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 15, 1)
)
cucsStorageConnectionDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageConnectionDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageConnectionDefEntry.setStatus("current")
_CucsStorageConnectionDefInstanceId_Type = CucsManagedObjectId
_CucsStorageConnectionDefInstanceId_Object = MibTableColumn
cucsStorageConnectionDefInstanceId = _CucsStorageConnectionDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 15, 1, 1),
    _CucsStorageConnectionDefInstanceId_Type()
)
cucsStorageConnectionDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageConnectionDefInstanceId.setStatus("current")
_CucsStorageConnectionDefDn_Type = CucsManagedObjectDn
_CucsStorageConnectionDefDn_Object = MibTableColumn
cucsStorageConnectionDefDn = _CucsStorageConnectionDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 15, 1, 2),
    _CucsStorageConnectionDefDn_Type()
)
cucsStorageConnectionDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionDefDn.setStatus("current")
_CucsStorageConnectionDefRn_Type = SnmpAdminString
_CucsStorageConnectionDefRn_Object = MibTableColumn
cucsStorageConnectionDefRn = _CucsStorageConnectionDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 15, 1, 3),
    _CucsStorageConnectionDefRn_Type()
)
cucsStorageConnectionDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionDefRn.setStatus("current")
_CucsStorageConnectionDefDescr_Type = SnmpAdminString
_CucsStorageConnectionDefDescr_Object = MibTableColumn
cucsStorageConnectionDefDescr = _CucsStorageConnectionDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 15, 1, 4),
    _CucsStorageConnectionDefDescr_Type()
)
cucsStorageConnectionDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionDefDescr.setStatus("current")
_CucsStorageConnectionDefIntId_Type = SnmpAdminString
_CucsStorageConnectionDefIntId_Object = MibTableColumn
cucsStorageConnectionDefIntId = _CucsStorageConnectionDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 15, 1, 5),
    _CucsStorageConnectionDefIntId_Type()
)
cucsStorageConnectionDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionDefIntId.setStatus("current")
_CucsStorageConnectionDefName_Type = SnmpAdminString
_CucsStorageConnectionDefName_Object = MibTableColumn
cucsStorageConnectionDefName = _CucsStorageConnectionDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 15, 1, 6),
    _CucsStorageConnectionDefName_Type()
)
cucsStorageConnectionDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionDefName.setStatus("current")
_CucsStorageConnectionDefOperState_Type = CucsStorageOperState
_CucsStorageConnectionDefOperState_Object = MibTableColumn
cucsStorageConnectionDefOperState = _CucsStorageConnectionDefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 15, 1, 7),
    _CucsStorageConnectionDefOperState_Type()
)
cucsStorageConnectionDefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionDefOperState.setStatus("current")
_CucsStorageConnectionDefPolicyLevel_Type = Gauge32
_CucsStorageConnectionDefPolicyLevel_Object = MibTableColumn
cucsStorageConnectionDefPolicyLevel = _CucsStorageConnectionDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 15, 1, 8),
    _CucsStorageConnectionDefPolicyLevel_Type()
)
cucsStorageConnectionDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionDefPolicyLevel.setStatus("current")
_CucsStorageConnectionDefPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStorageConnectionDefPolicyOwner_Object = MibTableColumn
cucsStorageConnectionDefPolicyOwner = _CucsStorageConnectionDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 15, 1, 9),
    _CucsStorageConnectionDefPolicyOwner_Type()
)
cucsStorageConnectionDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionDefPolicyOwner.setStatus("current")
_CucsStorageConnectionDefZoningType_Type = CucsStorageFcZoningType
_CucsStorageConnectionDefZoningType_Object = MibTableColumn
cucsStorageConnectionDefZoningType = _CucsStorageConnectionDefZoningType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 15, 1, 10),
    _CucsStorageConnectionDefZoningType_Type()
)
cucsStorageConnectionDefZoningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionDefZoningType.setStatus("current")
_CucsStorageConnectionPolicyTable_Object = MibTable
cucsStorageConnectionPolicyTable = _CucsStorageConnectionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 16)
)
if mibBuilder.loadTexts:
    cucsStorageConnectionPolicyTable.setStatus("current")
_CucsStorageConnectionPolicyEntry_Object = MibTableRow
cucsStorageConnectionPolicyEntry = _CucsStorageConnectionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 16, 1)
)
cucsStorageConnectionPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageConnectionPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageConnectionPolicyEntry.setStatus("current")
_CucsStorageConnectionPolicyInstanceId_Type = CucsManagedObjectId
_CucsStorageConnectionPolicyInstanceId_Object = MibTableColumn
cucsStorageConnectionPolicyInstanceId = _CucsStorageConnectionPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 16, 1, 1),
    _CucsStorageConnectionPolicyInstanceId_Type()
)
cucsStorageConnectionPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageConnectionPolicyInstanceId.setStatus("current")
_CucsStorageConnectionPolicyDn_Type = CucsManagedObjectDn
_CucsStorageConnectionPolicyDn_Object = MibTableColumn
cucsStorageConnectionPolicyDn = _CucsStorageConnectionPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 16, 1, 2),
    _CucsStorageConnectionPolicyDn_Type()
)
cucsStorageConnectionPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionPolicyDn.setStatus("current")
_CucsStorageConnectionPolicyRn_Type = SnmpAdminString
_CucsStorageConnectionPolicyRn_Object = MibTableColumn
cucsStorageConnectionPolicyRn = _CucsStorageConnectionPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 16, 1, 3),
    _CucsStorageConnectionPolicyRn_Type()
)
cucsStorageConnectionPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionPolicyRn.setStatus("current")
_CucsStorageConnectionPolicyDescr_Type = SnmpAdminString
_CucsStorageConnectionPolicyDescr_Object = MibTableColumn
cucsStorageConnectionPolicyDescr = _CucsStorageConnectionPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 16, 1, 4),
    _CucsStorageConnectionPolicyDescr_Type()
)
cucsStorageConnectionPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionPolicyDescr.setStatus("current")
_CucsStorageConnectionPolicyIntId_Type = SnmpAdminString
_CucsStorageConnectionPolicyIntId_Object = MibTableColumn
cucsStorageConnectionPolicyIntId = _CucsStorageConnectionPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 16, 1, 5),
    _CucsStorageConnectionPolicyIntId_Type()
)
cucsStorageConnectionPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionPolicyIntId.setStatus("current")
_CucsStorageConnectionPolicyName_Type = SnmpAdminString
_CucsStorageConnectionPolicyName_Object = MibTableColumn
cucsStorageConnectionPolicyName = _CucsStorageConnectionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 16, 1, 6),
    _CucsStorageConnectionPolicyName_Type()
)
cucsStorageConnectionPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionPolicyName.setStatus("current")
_CucsStorageConnectionPolicyOperState_Type = CucsStorageOperState
_CucsStorageConnectionPolicyOperState_Object = MibTableColumn
cucsStorageConnectionPolicyOperState = _CucsStorageConnectionPolicyOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 16, 1, 7),
    _CucsStorageConnectionPolicyOperState_Type()
)
cucsStorageConnectionPolicyOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionPolicyOperState.setStatus("current")
_CucsStorageConnectionPolicyPolicyLevel_Type = Gauge32
_CucsStorageConnectionPolicyPolicyLevel_Object = MibTableColumn
cucsStorageConnectionPolicyPolicyLevel = _CucsStorageConnectionPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 16, 1, 8),
    _CucsStorageConnectionPolicyPolicyLevel_Type()
)
cucsStorageConnectionPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionPolicyPolicyLevel.setStatus("current")
_CucsStorageConnectionPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStorageConnectionPolicyPolicyOwner_Object = MibTableColumn
cucsStorageConnectionPolicyPolicyOwner = _CucsStorageConnectionPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 16, 1, 9),
    _CucsStorageConnectionPolicyPolicyOwner_Type()
)
cucsStorageConnectionPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionPolicyPolicyOwner.setStatus("current")
_CucsStorageConnectionPolicyZoningType_Type = CucsStorageFcZoningType
_CucsStorageConnectionPolicyZoningType_Object = MibTableColumn
cucsStorageConnectionPolicyZoningType = _CucsStorageConnectionPolicyZoningType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 16, 1, 10),
    _CucsStorageConnectionPolicyZoningType_Type()
)
cucsStorageConnectionPolicyZoningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageConnectionPolicyZoningType.setStatus("current")
_CucsStorageDomainEpTable_Object = MibTable
cucsStorageDomainEpTable = _CucsStorageDomainEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 17)
)
if mibBuilder.loadTexts:
    cucsStorageDomainEpTable.setStatus("current")
_CucsStorageDomainEpEntry_Object = MibTableRow
cucsStorageDomainEpEntry = _CucsStorageDomainEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 17, 1)
)
cucsStorageDomainEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageDomainEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageDomainEpEntry.setStatus("current")
_CucsStorageDomainEpInstanceId_Type = CucsManagedObjectId
_CucsStorageDomainEpInstanceId_Object = MibTableColumn
cucsStorageDomainEpInstanceId = _CucsStorageDomainEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 17, 1, 1),
    _CucsStorageDomainEpInstanceId_Type()
)
cucsStorageDomainEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageDomainEpInstanceId.setStatus("current")
_CucsStorageDomainEpDn_Type = CucsManagedObjectDn
_CucsStorageDomainEpDn_Object = MibTableColumn
cucsStorageDomainEpDn = _CucsStorageDomainEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 17, 1, 2),
    _CucsStorageDomainEpDn_Type()
)
cucsStorageDomainEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDomainEpDn.setStatus("current")
_CucsStorageDomainEpRn_Type = SnmpAdminString
_CucsStorageDomainEpRn_Object = MibTableColumn
cucsStorageDomainEpRn = _CucsStorageDomainEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 17, 1, 3),
    _CucsStorageDomainEpRn_Type()
)
cucsStorageDomainEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDomainEpRn.setStatus("current")
_CucsStorageEpUserTable_Object = MibTable
cucsStorageEpUserTable = _CucsStorageEpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18)
)
if mibBuilder.loadTexts:
    cucsStorageEpUserTable.setStatus("current")
_CucsStorageEpUserEntry_Object = MibTableRow
cucsStorageEpUserEntry = _CucsStorageEpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18, 1)
)
cucsStorageEpUserEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageEpUserInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageEpUserEntry.setStatus("current")
_CucsStorageEpUserInstanceId_Type = CucsManagedObjectId
_CucsStorageEpUserInstanceId_Object = MibTableColumn
cucsStorageEpUserInstanceId = _CucsStorageEpUserInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18, 1, 1),
    _CucsStorageEpUserInstanceId_Type()
)
cucsStorageEpUserInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageEpUserInstanceId.setStatus("current")
_CucsStorageEpUserDn_Type = CucsManagedObjectDn
_CucsStorageEpUserDn_Object = MibTableColumn
cucsStorageEpUserDn = _CucsStorageEpUserDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18, 1, 2),
    _CucsStorageEpUserDn_Type()
)
cucsStorageEpUserDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEpUserDn.setStatus("current")
_CucsStorageEpUserRn_Type = SnmpAdminString
_CucsStorageEpUserRn_Object = MibTableColumn
cucsStorageEpUserRn = _CucsStorageEpUserRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18, 1, 3),
    _CucsStorageEpUserRn_Type()
)
cucsStorageEpUserRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEpUserRn.setStatus("current")
_CucsStorageEpUserConfigState_Type = CucsAaaConfigState
_CucsStorageEpUserConfigState_Object = MibTableColumn
cucsStorageEpUserConfigState = _CucsStorageEpUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18, 1, 4),
    _CucsStorageEpUserConfigState_Type()
)
cucsStorageEpUserConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEpUserConfigState.setStatus("current")
_CucsStorageEpUserConfigStatusMessage_Type = SnmpAdminString
_CucsStorageEpUserConfigStatusMessage_Object = MibTableColumn
cucsStorageEpUserConfigStatusMessage = _CucsStorageEpUserConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18, 1, 5),
    _CucsStorageEpUserConfigStatusMessage_Type()
)
cucsStorageEpUserConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEpUserConfigStatusMessage.setStatus("current")
_CucsStorageEpUserDescr_Type = SnmpAdminString
_CucsStorageEpUserDescr_Object = MibTableColumn
cucsStorageEpUserDescr = _CucsStorageEpUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18, 1, 6),
    _CucsStorageEpUserDescr_Type()
)
cucsStorageEpUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEpUserDescr.setStatus("current")
_CucsStorageEpUserDomain_Type = SnmpAdminString
_CucsStorageEpUserDomain_Object = MibTableColumn
cucsStorageEpUserDomain = _CucsStorageEpUserDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18, 1, 7),
    _CucsStorageEpUserDomain_Type()
)
cucsStorageEpUserDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEpUserDomain.setStatus("current")
_CucsStorageEpUserName_Type = SnmpAdminString
_CucsStorageEpUserName_Object = MibTableColumn
cucsStorageEpUserName = _CucsStorageEpUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18, 1, 8),
    _CucsStorageEpUserName_Type()
)
cucsStorageEpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEpUserName.setStatus("current")
_CucsStorageEpUserPriv_Type = CucsStorageEpAccess
_CucsStorageEpUserPriv_Object = MibTableColumn
cucsStorageEpUserPriv = _CucsStorageEpUserPriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18, 1, 9),
    _CucsStorageEpUserPriv_Type()
)
cucsStorageEpUserPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEpUserPriv.setStatus("current")
_CucsStorageEpUserPwd_Type = SnmpAdminString
_CucsStorageEpUserPwd_Object = MibTableColumn
cucsStorageEpUserPwd = _CucsStorageEpUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18, 1, 10),
    _CucsStorageEpUserPwd_Type()
)
cucsStorageEpUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEpUserPwd.setStatus("current")
_CucsStorageEpUserPwdSet_Type = TruthValue
_CucsStorageEpUserPwdSet_Object = MibTableColumn
cucsStorageEpUserPwdSet = _CucsStorageEpUserPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 18, 1, 11),
    _CucsStorageEpUserPwdSet_Type()
)
cucsStorageEpUserPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEpUserPwdSet.setStatus("current")
_CucsStorageEtherIfTable_Object = MibTable
cucsStorageEtherIfTable = _CucsStorageEtherIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 19)
)
if mibBuilder.loadTexts:
    cucsStorageEtherIfTable.setStatus("current")
_CucsStorageEtherIfEntry_Object = MibTableRow
cucsStorageEtherIfEntry = _CucsStorageEtherIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 19, 1)
)
cucsStorageEtherIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageEtherIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageEtherIfEntry.setStatus("current")
_CucsStorageEtherIfInstanceId_Type = CucsManagedObjectId
_CucsStorageEtherIfInstanceId_Object = MibTableColumn
cucsStorageEtherIfInstanceId = _CucsStorageEtherIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 19, 1, 1),
    _CucsStorageEtherIfInstanceId_Type()
)
cucsStorageEtherIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageEtherIfInstanceId.setStatus("current")
_CucsStorageEtherIfDn_Type = CucsManagedObjectDn
_CucsStorageEtherIfDn_Object = MibTableColumn
cucsStorageEtherIfDn = _CucsStorageEtherIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 19, 1, 2),
    _CucsStorageEtherIfDn_Type()
)
cucsStorageEtherIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEtherIfDn.setStatus("current")
_CucsStorageEtherIfRn_Type = SnmpAdminString
_CucsStorageEtherIfRn_Object = MibTableColumn
cucsStorageEtherIfRn = _CucsStorageEtherIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 19, 1, 3),
    _CucsStorageEtherIfRn_Type()
)
cucsStorageEtherIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEtherIfRn.setStatus("current")
_CucsStorageEtherIfName_Type = SnmpAdminString
_CucsStorageEtherIfName_Object = MibTableColumn
cucsStorageEtherIfName = _CucsStorageEtherIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 19, 1, 4),
    _CucsStorageEtherIfName_Type()
)
cucsStorageEtherIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEtherIfName.setStatus("current")
_CucsStorageEtherIfVlanType_Type = CucsStorageEtherIfVlanType
_CucsStorageEtherIfVlanType_Object = MibTableColumn
cucsStorageEtherIfVlanType = _CucsStorageEtherIfVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 19, 1, 5),
    _CucsStorageEtherIfVlanType_Type()
)
cucsStorageEtherIfVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageEtherIfVlanType.setStatus("current")
_CucsStorageFcIfTable_Object = MibTable
cucsStorageFcIfTable = _CucsStorageFcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 20)
)
if mibBuilder.loadTexts:
    cucsStorageFcIfTable.setStatus("current")
_CucsStorageFcIfEntry_Object = MibTableRow
cucsStorageFcIfEntry = _CucsStorageFcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 20, 1)
)
cucsStorageFcIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageFcIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageFcIfEntry.setStatus("current")
_CucsStorageFcIfInstanceId_Type = CucsManagedObjectId
_CucsStorageFcIfInstanceId_Object = MibTableColumn
cucsStorageFcIfInstanceId = _CucsStorageFcIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 20, 1, 1),
    _CucsStorageFcIfInstanceId_Type()
)
cucsStorageFcIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageFcIfInstanceId.setStatus("current")
_CucsStorageFcIfDn_Type = CucsManagedObjectDn
_CucsStorageFcIfDn_Object = MibTableColumn
cucsStorageFcIfDn = _CucsStorageFcIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 20, 1, 2),
    _CucsStorageFcIfDn_Type()
)
cucsStorageFcIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFcIfDn.setStatus("current")
_CucsStorageFcIfRn_Type = SnmpAdminString
_CucsStorageFcIfRn_Object = MibTableColumn
cucsStorageFcIfRn = _CucsStorageFcIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 20, 1, 3),
    _CucsStorageFcIfRn_Type()
)
cucsStorageFcIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFcIfRn.setStatus("current")
_CucsStorageFcIfName_Type = SnmpAdminString
_CucsStorageFcIfName_Object = MibTableColumn
cucsStorageFcIfName = _CucsStorageFcIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 20, 1, 4),
    _CucsStorageFcIfName_Type()
)
cucsStorageFcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFcIfName.setStatus("current")
_CucsStorageFcTargetEpTable_Object = MibTable
cucsStorageFcTargetEpTable = _CucsStorageFcTargetEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 21)
)
if mibBuilder.loadTexts:
    cucsStorageFcTargetEpTable.setStatus("current")
_CucsStorageFcTargetEpEntry_Object = MibTableRow
cucsStorageFcTargetEpEntry = _CucsStorageFcTargetEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 21, 1)
)
cucsStorageFcTargetEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageFcTargetEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageFcTargetEpEntry.setStatus("current")
_CucsStorageFcTargetEpInstanceId_Type = CucsManagedObjectId
_CucsStorageFcTargetEpInstanceId_Object = MibTableColumn
cucsStorageFcTargetEpInstanceId = _CucsStorageFcTargetEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 21, 1, 1),
    _CucsStorageFcTargetEpInstanceId_Type()
)
cucsStorageFcTargetEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageFcTargetEpInstanceId.setStatus("current")
_CucsStorageFcTargetEpDn_Type = CucsManagedObjectDn
_CucsStorageFcTargetEpDn_Object = MibTableColumn
cucsStorageFcTargetEpDn = _CucsStorageFcTargetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 21, 1, 2),
    _CucsStorageFcTargetEpDn_Type()
)
cucsStorageFcTargetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFcTargetEpDn.setStatus("current")
_CucsStorageFcTargetEpRn_Type = SnmpAdminString
_CucsStorageFcTargetEpRn_Object = MibTableColumn
cucsStorageFcTargetEpRn = _CucsStorageFcTargetEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 21, 1, 3),
    _CucsStorageFcTargetEpRn_Type()
)
cucsStorageFcTargetEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFcTargetEpRn.setStatus("current")
_CucsStorageFcTargetEpDescr_Type = SnmpAdminString
_CucsStorageFcTargetEpDescr_Object = MibTableColumn
cucsStorageFcTargetEpDescr = _CucsStorageFcTargetEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 21, 1, 4),
    _CucsStorageFcTargetEpDescr_Type()
)
cucsStorageFcTargetEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFcTargetEpDescr.setStatus("current")
_CucsStorageFcTargetEpPath_Type = CucsStorageTargetPath
_CucsStorageFcTargetEpPath_Object = MibTableColumn
cucsStorageFcTargetEpPath = _CucsStorageFcTargetEpPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 21, 1, 5),
    _CucsStorageFcTargetEpPath_Type()
)
cucsStorageFcTargetEpPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFcTargetEpPath.setStatus("current")
_CucsStorageFcTargetEpTargetwwpn_Type = SnmpAdminString
_CucsStorageFcTargetEpTargetwwpn_Object = MibTableColumn
cucsStorageFcTargetEpTargetwwpn = _CucsStorageFcTargetEpTargetwwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 21, 1, 6),
    _CucsStorageFcTargetEpTargetwwpn_Type()
)
cucsStorageFcTargetEpTargetwwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFcTargetEpTargetwwpn.setStatus("current")
_CucsStorageFcTargetIfTable_Object = MibTable
cucsStorageFcTargetIfTable = _CucsStorageFcTargetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 22)
)
if mibBuilder.loadTexts:
    cucsStorageFcTargetIfTable.setStatus("current")
_CucsStorageFcTargetIfEntry_Object = MibTableRow
cucsStorageFcTargetIfEntry = _CucsStorageFcTargetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 22, 1)
)
cucsStorageFcTargetIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageFcTargetIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageFcTargetIfEntry.setStatus("current")
_CucsStorageFcTargetIfInstanceId_Type = CucsManagedObjectId
_CucsStorageFcTargetIfInstanceId_Object = MibTableColumn
cucsStorageFcTargetIfInstanceId = _CucsStorageFcTargetIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 22, 1, 1),
    _CucsStorageFcTargetIfInstanceId_Type()
)
cucsStorageFcTargetIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageFcTargetIfInstanceId.setStatus("current")
_CucsStorageFcTargetIfDn_Type = CucsManagedObjectDn
_CucsStorageFcTargetIfDn_Object = MibTableColumn
cucsStorageFcTargetIfDn = _CucsStorageFcTargetIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 22, 1, 2),
    _CucsStorageFcTargetIfDn_Type()
)
cucsStorageFcTargetIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFcTargetIfDn.setStatus("current")
_CucsStorageFcTargetIfRn_Type = SnmpAdminString
_CucsStorageFcTargetIfRn_Object = MibTableColumn
cucsStorageFcTargetIfRn = _CucsStorageFcTargetIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 22, 1, 3),
    _CucsStorageFcTargetIfRn_Type()
)
cucsStorageFcTargetIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFcTargetIfRn.setStatus("current")
_CucsStorageFcTargetIfId_Type = Unsigned64
_CucsStorageFcTargetIfId_Object = MibTableColumn
cucsStorageFcTargetIfId = _CucsStorageFcTargetIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 22, 1, 4),
    _CucsStorageFcTargetIfId_Type()
)
cucsStorageFcTargetIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFcTargetIfId.setStatus("current")
_CucsStorageFcTargetIfProt_Type = CucsStorageProtocol
_CucsStorageFcTargetIfProt_Object = MibTableColumn
cucsStorageFcTargetIfProt = _CucsStorageFcTargetIfProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 22, 1, 5),
    _CucsStorageFcTargetIfProt_Type()
)
cucsStorageFcTargetIfProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFcTargetIfProt.setStatus("current")
_CucsStorageIScsiTargetIfTable_Object = MibTable
cucsStorageIScsiTargetIfTable = _CucsStorageIScsiTargetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 23)
)
if mibBuilder.loadTexts:
    cucsStorageIScsiTargetIfTable.setStatus("current")
_CucsStorageIScsiTargetIfEntry_Object = MibTableRow
cucsStorageIScsiTargetIfEntry = _CucsStorageIScsiTargetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 23, 1)
)
cucsStorageIScsiTargetIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageIScsiTargetIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageIScsiTargetIfEntry.setStatus("current")
_CucsStorageIScsiTargetIfInstanceId_Type = CucsManagedObjectId
_CucsStorageIScsiTargetIfInstanceId_Object = MibTableColumn
cucsStorageIScsiTargetIfInstanceId = _CucsStorageIScsiTargetIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 23, 1, 1),
    _CucsStorageIScsiTargetIfInstanceId_Type()
)
cucsStorageIScsiTargetIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageIScsiTargetIfInstanceId.setStatus("current")
_CucsStorageIScsiTargetIfDn_Type = CucsManagedObjectDn
_CucsStorageIScsiTargetIfDn_Object = MibTableColumn
cucsStorageIScsiTargetIfDn = _CucsStorageIScsiTargetIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 23, 1, 2),
    _CucsStorageIScsiTargetIfDn_Type()
)
cucsStorageIScsiTargetIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIScsiTargetIfDn.setStatus("current")
_CucsStorageIScsiTargetIfRn_Type = SnmpAdminString
_CucsStorageIScsiTargetIfRn_Object = MibTableColumn
cucsStorageIScsiTargetIfRn = _CucsStorageIScsiTargetIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 23, 1, 3),
    _CucsStorageIScsiTargetIfRn_Type()
)
cucsStorageIScsiTargetIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIScsiTargetIfRn.setStatus("current")
_CucsStorageIScsiTargetIfName_Type = SnmpAdminString
_CucsStorageIScsiTargetIfName_Object = MibTableColumn
cucsStorageIScsiTargetIfName = _CucsStorageIScsiTargetIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 23, 1, 4),
    _CucsStorageIScsiTargetIfName_Type()
)
cucsStorageIScsiTargetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIScsiTargetIfName.setStatus("current")
_CucsStorageIScsiTargetIfProt_Type = CucsStorageProtocol
_CucsStorageIScsiTargetIfProt_Object = MibTableColumn
cucsStorageIScsiTargetIfProt = _CucsStorageIScsiTargetIfProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 23, 1, 5),
    _CucsStorageIScsiTargetIfProt_Type()
)
cucsStorageIScsiTargetIfProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIScsiTargetIfProt.setStatus("current")
_CucsStorageIniGroupTable_Object = MibTable
cucsStorageIniGroupTable = _CucsStorageIniGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24)
)
if mibBuilder.loadTexts:
    cucsStorageIniGroupTable.setStatus("current")
_CucsStorageIniGroupEntry_Object = MibTableRow
cucsStorageIniGroupEntry = _CucsStorageIniGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1)
)
cucsStorageIniGroupEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageIniGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageIniGroupEntry.setStatus("current")
_CucsStorageIniGroupInstanceId_Type = CucsManagedObjectId
_CucsStorageIniGroupInstanceId_Object = MibTableColumn
cucsStorageIniGroupInstanceId = _CucsStorageIniGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 1),
    _CucsStorageIniGroupInstanceId_Type()
)
cucsStorageIniGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageIniGroupInstanceId.setStatus("current")
_CucsStorageIniGroupDn_Type = CucsManagedObjectDn
_CucsStorageIniGroupDn_Object = MibTableColumn
cucsStorageIniGroupDn = _CucsStorageIniGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 2),
    _CucsStorageIniGroupDn_Type()
)
cucsStorageIniGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupDn.setStatus("current")
_CucsStorageIniGroupRn_Type = SnmpAdminString
_CucsStorageIniGroupRn_Object = MibTableColumn
cucsStorageIniGroupRn = _CucsStorageIniGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 3),
    _CucsStorageIniGroupRn_Type()
)
cucsStorageIniGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupRn.setStatus("current")
_CucsStorageIniGroupDescr_Type = SnmpAdminString
_CucsStorageIniGroupDescr_Object = MibTableColumn
cucsStorageIniGroupDescr = _CucsStorageIniGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 4),
    _CucsStorageIniGroupDescr_Type()
)
cucsStorageIniGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupDescr.setStatus("current")
_CucsStorageIniGroupGroupPolicyName_Type = SnmpAdminString
_CucsStorageIniGroupGroupPolicyName_Object = MibTableColumn
cucsStorageIniGroupGroupPolicyName = _CucsStorageIniGroupGroupPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 5),
    _CucsStorageIniGroupGroupPolicyName_Type()
)
cucsStorageIniGroupGroupPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupGroupPolicyName.setStatus("current")
_CucsStorageIniGroupIntId_Type = SnmpAdminString
_CucsStorageIniGroupIntId_Object = MibTableColumn
cucsStorageIniGroupIntId = _CucsStorageIniGroupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 6),
    _CucsStorageIniGroupIntId_Type()
)
cucsStorageIniGroupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupIntId.setStatus("current")
_CucsStorageIniGroupName_Type = SnmpAdminString
_CucsStorageIniGroupName_Object = MibTableColumn
cucsStorageIniGroupName = _CucsStorageIniGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 7),
    _CucsStorageIniGroupName_Type()
)
cucsStorageIniGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupName.setStatus("current")
_CucsStorageIniGroupOperProtocol_Type = CucsStorageIniGroupOperProtocol
_CucsStorageIniGroupOperProtocol_Object = MibTableColumn
cucsStorageIniGroupOperProtocol = _CucsStorageIniGroupOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 8),
    _CucsStorageIniGroupOperProtocol_Type()
)
cucsStorageIniGroupOperProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupOperProtocol.setStatus("current")
_CucsStorageIniGroupOwner_Type = CucsStorageIniGroupOwner
_CucsStorageIniGroupOwner_Object = MibTableColumn
cucsStorageIniGroupOwner = _CucsStorageIniGroupOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 9),
    _CucsStorageIniGroupOwner_Type()
)
cucsStorageIniGroupOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupOwner.setStatus("current")
_CucsStorageIniGroupPolicyLevel_Type = Gauge32
_CucsStorageIniGroupPolicyLevel_Object = MibTableColumn
cucsStorageIniGroupPolicyLevel = _CucsStorageIniGroupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 10),
    _CucsStorageIniGroupPolicyLevel_Type()
)
cucsStorageIniGroupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupPolicyLevel.setStatus("current")
_CucsStorageIniGroupPolicyName_Type = SnmpAdminString
_CucsStorageIniGroupPolicyName_Object = MibTableColumn
cucsStorageIniGroupPolicyName = _CucsStorageIniGroupPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 11),
    _CucsStorageIniGroupPolicyName_Type()
)
cucsStorageIniGroupPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupPolicyName.setStatus("current")
_CucsStorageIniGroupPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStorageIniGroupPolicyOwner_Object = MibTableColumn
cucsStorageIniGroupPolicyOwner = _CucsStorageIniGroupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 12),
    _CucsStorageIniGroupPolicyOwner_Type()
)
cucsStorageIniGroupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupPolicyOwner.setStatus("current")
_CucsStorageIniGroupProtocol_Type = CucsStorageIniGroupProtocol
_CucsStorageIniGroupProtocol_Object = MibTableColumn
cucsStorageIniGroupProtocol = _CucsStorageIniGroupProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 13),
    _CucsStorageIniGroupProtocol_Type()
)
cucsStorageIniGroupProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupProtocol.setStatus("current")
_CucsStorageIniGroupRmtDiskCfgName_Type = SnmpAdminString
_CucsStorageIniGroupRmtDiskCfgName_Object = MibTableColumn
cucsStorageIniGroupRmtDiskCfgName = _CucsStorageIniGroupRmtDiskCfgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 14),
    _CucsStorageIniGroupRmtDiskCfgName_Type()
)
cucsStorageIniGroupRmtDiskCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupRmtDiskCfgName.setStatus("current")
_CucsStorageIniGroupOperState_Type = CucsStorageOperState
_CucsStorageIniGroupOperState_Object = MibTableColumn
cucsStorageIniGroupOperState = _CucsStorageIniGroupOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 24, 1, 15),
    _CucsStorageIniGroupOperState_Type()
)
cucsStorageIniGroupOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageIniGroupOperState.setStatus("current")
_CucsStorageInitiatorTable_Object = MibTable
cucsStorageInitiatorTable = _CucsStorageInitiatorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 25)
)
if mibBuilder.loadTexts:
    cucsStorageInitiatorTable.setStatus("current")
_CucsStorageInitiatorEntry_Object = MibTableRow
cucsStorageInitiatorEntry = _CucsStorageInitiatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 25, 1)
)
cucsStorageInitiatorEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageInitiatorInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageInitiatorEntry.setStatus("current")
_CucsStorageInitiatorInstanceId_Type = CucsManagedObjectId
_CucsStorageInitiatorInstanceId_Object = MibTableColumn
cucsStorageInitiatorInstanceId = _CucsStorageInitiatorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 25, 1, 1),
    _CucsStorageInitiatorInstanceId_Type()
)
cucsStorageInitiatorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageInitiatorInstanceId.setStatus("current")
_CucsStorageInitiatorDn_Type = CucsManagedObjectDn
_CucsStorageInitiatorDn_Object = MibTableColumn
cucsStorageInitiatorDn = _CucsStorageInitiatorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 25, 1, 2),
    _CucsStorageInitiatorDn_Type()
)
cucsStorageInitiatorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageInitiatorDn.setStatus("current")
_CucsStorageInitiatorRn_Type = SnmpAdminString
_CucsStorageInitiatorRn_Object = MibTableColumn
cucsStorageInitiatorRn = _CucsStorageInitiatorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 25, 1, 3),
    _CucsStorageInitiatorRn_Type()
)
cucsStorageInitiatorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageInitiatorRn.setStatus("current")
_CucsStorageInitiatorDescr_Type = SnmpAdminString
_CucsStorageInitiatorDescr_Object = MibTableColumn
cucsStorageInitiatorDescr = _CucsStorageInitiatorDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 25, 1, 4),
    _CucsStorageInitiatorDescr_Type()
)
cucsStorageInitiatorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageInitiatorDescr.setStatus("current")
_CucsStorageInitiatorIntId_Type = SnmpAdminString
_CucsStorageInitiatorIntId_Object = MibTableColumn
cucsStorageInitiatorIntId = _CucsStorageInitiatorIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 25, 1, 5),
    _CucsStorageInitiatorIntId_Type()
)
cucsStorageInitiatorIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageInitiatorIntId.setStatus("current")
_CucsStorageInitiatorName_Type = SnmpAdminString
_CucsStorageInitiatorName_Object = MibTableColumn
cucsStorageInitiatorName = _CucsStorageInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 25, 1, 6),
    _CucsStorageInitiatorName_Type()
)
cucsStorageInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageInitiatorName.setStatus("current")
_CucsStorageInitiatorOperState_Type = CucsStorageOperState
_CucsStorageInitiatorOperState_Object = MibTableColumn
cucsStorageInitiatorOperState = _CucsStorageInitiatorOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 25, 1, 7),
    _CucsStorageInitiatorOperState_Type()
)
cucsStorageInitiatorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageInitiatorOperState.setStatus("current")
_CucsStorageInitiatorPolicyLevel_Type = Gauge32
_CucsStorageInitiatorPolicyLevel_Object = MibTableColumn
cucsStorageInitiatorPolicyLevel = _CucsStorageInitiatorPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 25, 1, 8),
    _CucsStorageInitiatorPolicyLevel_Type()
)
cucsStorageInitiatorPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageInitiatorPolicyLevel.setStatus("current")
_CucsStorageInitiatorPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStorageInitiatorPolicyOwner_Object = MibTableColumn
cucsStorageInitiatorPolicyOwner = _CucsStorageInitiatorPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 25, 1, 9),
    _CucsStorageInitiatorPolicyOwner_Type()
)
cucsStorageInitiatorPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageInitiatorPolicyOwner.setStatus("current")
_CucsStorageInitiatorDuplicateTarget_Type = SnmpAdminString
_CucsStorageInitiatorDuplicateTarget_Object = MibTableColumn
cucsStorageInitiatorDuplicateTarget = _CucsStorageInitiatorDuplicateTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 25, 1, 10),
    _CucsStorageInitiatorDuplicateTarget_Type()
)
cucsStorageInitiatorDuplicateTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageInitiatorDuplicateTarget.setStatus("current")
_CucsStorageNodeEpTable_Object = MibTable
cucsStorageNodeEpTable = _CucsStorageNodeEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 26)
)
if mibBuilder.loadTexts:
    cucsStorageNodeEpTable.setStatus("current")
_CucsStorageNodeEpEntry_Object = MibTableRow
cucsStorageNodeEpEntry = _CucsStorageNodeEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 26, 1)
)
cucsStorageNodeEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageNodeEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageNodeEpEntry.setStatus("current")
_CucsStorageNodeEpInstanceId_Type = CucsManagedObjectId
_CucsStorageNodeEpInstanceId_Object = MibTableColumn
cucsStorageNodeEpInstanceId = _CucsStorageNodeEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 26, 1, 1),
    _CucsStorageNodeEpInstanceId_Type()
)
cucsStorageNodeEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageNodeEpInstanceId.setStatus("current")
_CucsStorageNodeEpDn_Type = CucsManagedObjectDn
_CucsStorageNodeEpDn_Object = MibTableColumn
cucsStorageNodeEpDn = _CucsStorageNodeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 26, 1, 2),
    _CucsStorageNodeEpDn_Type()
)
cucsStorageNodeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageNodeEpDn.setStatus("current")
_CucsStorageNodeEpRn_Type = SnmpAdminString
_CucsStorageNodeEpRn_Object = MibTableColumn
cucsStorageNodeEpRn = _CucsStorageNodeEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 26, 1, 3),
    _CucsStorageNodeEpRn_Type()
)
cucsStorageNodeEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageNodeEpRn.setStatus("current")
_CucsStorageNodeEpEpDn_Type = SnmpAdminString
_CucsStorageNodeEpEpDn_Object = MibTableColumn
cucsStorageNodeEpEpDn = _CucsStorageNodeEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 26, 1, 4),
    _CucsStorageNodeEpEpDn_Type()
)
cucsStorageNodeEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageNodeEpEpDn.setStatus("current")
_CucsStorageNodeEpId_Type = Gauge32
_CucsStorageNodeEpId_Object = MibTableColumn
cucsStorageNodeEpId = _CucsStorageNodeEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 26, 1, 5),
    _CucsStorageNodeEpId_Type()
)
cucsStorageNodeEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageNodeEpId.setStatus("current")
_CucsStorageSystemTable_Object = MibTable
cucsStorageSystemTable = _CucsStorageSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27)
)
if mibBuilder.loadTexts:
    cucsStorageSystemTable.setStatus("current")
_CucsStorageSystemEntry_Object = MibTableRow
cucsStorageSystemEntry = _CucsStorageSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1)
)
cucsStorageSystemEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageSystemEntry.setStatus("current")
_CucsStorageSystemInstanceId_Type = CucsManagedObjectId
_CucsStorageSystemInstanceId_Object = MibTableColumn
cucsStorageSystemInstanceId = _CucsStorageSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 1),
    _CucsStorageSystemInstanceId_Type()
)
cucsStorageSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageSystemInstanceId.setStatus("current")
_CucsStorageSystemDn_Type = CucsManagedObjectDn
_CucsStorageSystemDn_Object = MibTableColumn
cucsStorageSystemDn = _CucsStorageSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 2),
    _CucsStorageSystemDn_Type()
)
cucsStorageSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemDn.setStatus("current")
_CucsStorageSystemRn_Type = SnmpAdminString
_CucsStorageSystemRn_Object = MibTableColumn
cucsStorageSystemRn = _CucsStorageSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 3),
    _CucsStorageSystemRn_Type()
)
cucsStorageSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemRn.setStatus("current")
_CucsStorageSystemFsmDescr_Type = SnmpAdminString
_CucsStorageSystemFsmDescr_Object = MibTableColumn
cucsStorageSystemFsmDescr = _CucsStorageSystemFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 4),
    _CucsStorageSystemFsmDescr_Type()
)
cucsStorageSystemFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmDescr.setStatus("current")
_CucsStorageSystemFsmPrev_Type = SnmpAdminString
_CucsStorageSystemFsmPrev_Object = MibTableColumn
cucsStorageSystemFsmPrev = _CucsStorageSystemFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 5),
    _CucsStorageSystemFsmPrev_Type()
)
cucsStorageSystemFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmPrev.setStatus("current")
_CucsStorageSystemFsmProgr_Type = Gauge32
_CucsStorageSystemFsmProgr_Object = MibTableColumn
cucsStorageSystemFsmProgr = _CucsStorageSystemFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 6),
    _CucsStorageSystemFsmProgr_Type()
)
cucsStorageSystemFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmProgr.setStatus("current")
_CucsStorageSystemFsmRmtInvErrCode_Type = Gauge32
_CucsStorageSystemFsmRmtInvErrCode_Object = MibTableColumn
cucsStorageSystemFsmRmtInvErrCode = _CucsStorageSystemFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 7),
    _CucsStorageSystemFsmRmtInvErrCode_Type()
)
cucsStorageSystemFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmRmtInvErrCode.setStatus("current")
_CucsStorageSystemFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsStorageSystemFsmRmtInvErrDescr_Object = MibTableColumn
cucsStorageSystemFsmRmtInvErrDescr = _CucsStorageSystemFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 8),
    _CucsStorageSystemFsmRmtInvErrDescr_Type()
)
cucsStorageSystemFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmRmtInvErrDescr.setStatus("current")
_CucsStorageSystemFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsStorageSystemFsmRmtInvRslt_Object = MibTableColumn
cucsStorageSystemFsmRmtInvRslt = _CucsStorageSystemFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 9),
    _CucsStorageSystemFsmRmtInvRslt_Type()
)
cucsStorageSystemFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmRmtInvRslt.setStatus("current")
_CucsStorageSystemFsmStageDescr_Type = SnmpAdminString
_CucsStorageSystemFsmStageDescr_Object = MibTableColumn
cucsStorageSystemFsmStageDescr = _CucsStorageSystemFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 10),
    _CucsStorageSystemFsmStageDescr_Type()
)
cucsStorageSystemFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStageDescr.setStatus("current")
_CucsStorageSystemFsmStamp_Type = DateAndTime
_CucsStorageSystemFsmStamp_Object = MibTableColumn
cucsStorageSystemFsmStamp = _CucsStorageSystemFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 11),
    _CucsStorageSystemFsmStamp_Type()
)
cucsStorageSystemFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStamp.setStatus("current")
_CucsStorageSystemFsmStatus_Type = SnmpAdminString
_CucsStorageSystemFsmStatus_Object = MibTableColumn
cucsStorageSystemFsmStatus = _CucsStorageSystemFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 12),
    _CucsStorageSystemFsmStatus_Type()
)
cucsStorageSystemFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStatus.setStatus("current")
_CucsStorageSystemFsmTry_Type = Gauge32
_CucsStorageSystemFsmTry_Object = MibTableColumn
cucsStorageSystemFsmTry = _CucsStorageSystemFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 13),
    _CucsStorageSystemFsmTry_Type()
)
cucsStorageSystemFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmTry.setStatus("current")
_CucsStorageSystemId_Type = SnmpAdminString
_CucsStorageSystemId_Object = MibTableColumn
cucsStorageSystemId = _CucsStorageSystemId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 14),
    _CucsStorageSystemId_Type()
)
cucsStorageSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemId.setStatus("current")
_CucsStorageSystemName_Type = SnmpAdminString
_CucsStorageSystemName_Object = MibTableColumn
cucsStorageSystemName = _CucsStorageSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 27, 1, 15),
    _CucsStorageSystemName_Type()
)
cucsStorageSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemName.setStatus("current")
_CucsStorageSystemFsmTable_Object = MibTable
cucsStorageSystemFsmTable = _CucsStorageSystemFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28)
)
if mibBuilder.loadTexts:
    cucsStorageSystemFsmTable.setStatus("current")
_CucsStorageSystemFsmEntry_Object = MibTableRow
cucsStorageSystemFsmEntry = _CucsStorageSystemFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28, 1)
)
cucsStorageSystemFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageSystemFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageSystemFsmEntry.setStatus("current")
_CucsStorageSystemFsmInstanceId_Type = CucsManagedObjectId
_CucsStorageSystemFsmInstanceId_Object = MibTableColumn
cucsStorageSystemFsmInstanceId = _CucsStorageSystemFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28, 1, 1),
    _CucsStorageSystemFsmInstanceId_Type()
)
cucsStorageSystemFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmInstanceId.setStatus("current")
_CucsStorageSystemFsmDn_Type = CucsManagedObjectDn
_CucsStorageSystemFsmDn_Object = MibTableColumn
cucsStorageSystemFsmDn = _CucsStorageSystemFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28, 1, 2),
    _CucsStorageSystemFsmDn_Type()
)
cucsStorageSystemFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmDn.setStatus("current")
_CucsStorageSystemFsmRn_Type = SnmpAdminString
_CucsStorageSystemFsmRn_Object = MibTableColumn
cucsStorageSystemFsmRn = _CucsStorageSystemFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28, 1, 3),
    _CucsStorageSystemFsmRn_Type()
)
cucsStorageSystemFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmRn.setStatus("current")
_CucsStorageSystemFsmCompletionTime_Type = DateAndTime
_CucsStorageSystemFsmCompletionTime_Object = MibTableColumn
cucsStorageSystemFsmCompletionTime = _CucsStorageSystemFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28, 1, 4),
    _CucsStorageSystemFsmCompletionTime_Type()
)
cucsStorageSystemFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmCompletionTime.setStatus("current")
_CucsStorageSystemFsmCurrentFsm_Type = CucsStorageSystemFsmCurrentFsm
_CucsStorageSystemFsmCurrentFsm_Object = MibTableColumn
cucsStorageSystemFsmCurrentFsm = _CucsStorageSystemFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28, 1, 5),
    _CucsStorageSystemFsmCurrentFsm_Type()
)
cucsStorageSystemFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmCurrentFsm.setStatus("current")
_CucsStorageSystemFsmDescrData_Type = SnmpAdminString
_CucsStorageSystemFsmDescrData_Object = MibTableColumn
cucsStorageSystemFsmDescrData = _CucsStorageSystemFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28, 1, 6),
    _CucsStorageSystemFsmDescrData_Type()
)
cucsStorageSystemFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmDescrData.setStatus("current")
_CucsStorageSystemFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsStorageSystemFsmFsmStatus_Object = MibTableColumn
cucsStorageSystemFsmFsmStatus = _CucsStorageSystemFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28, 1, 7),
    _CucsStorageSystemFsmFsmStatus_Type()
)
cucsStorageSystemFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmFsmStatus.setStatus("current")
_CucsStorageSystemFsmProgress_Type = Gauge32
_CucsStorageSystemFsmProgress_Object = MibTableColumn
cucsStorageSystemFsmProgress = _CucsStorageSystemFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28, 1, 8),
    _CucsStorageSystemFsmProgress_Type()
)
cucsStorageSystemFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmProgress.setStatus("current")
_CucsStorageSystemFsmRmtErrCode_Type = Gauge32
_CucsStorageSystemFsmRmtErrCode_Object = MibTableColumn
cucsStorageSystemFsmRmtErrCode = _CucsStorageSystemFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28, 1, 9),
    _CucsStorageSystemFsmRmtErrCode_Type()
)
cucsStorageSystemFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmRmtErrCode.setStatus("current")
_CucsStorageSystemFsmRmtErrDescr_Type = SnmpAdminString
_CucsStorageSystemFsmRmtErrDescr_Object = MibTableColumn
cucsStorageSystemFsmRmtErrDescr = _CucsStorageSystemFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28, 1, 10),
    _CucsStorageSystemFsmRmtErrDescr_Type()
)
cucsStorageSystemFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmRmtErrDescr.setStatus("current")
_CucsStorageSystemFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsStorageSystemFsmRmtRslt_Object = MibTableColumn
cucsStorageSystemFsmRmtRslt = _CucsStorageSystemFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 28, 1, 11),
    _CucsStorageSystemFsmRmtRslt_Type()
)
cucsStorageSystemFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmRmtRslt.setStatus("current")
_CucsStorageSystemFsmStageTable_Object = MibTable
cucsStorageSystemFsmStageTable = _CucsStorageSystemFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 29)
)
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStageTable.setStatus("current")
_CucsStorageSystemFsmStageEntry_Object = MibTableRow
cucsStorageSystemFsmStageEntry = _CucsStorageSystemFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 29, 1)
)
cucsStorageSystemFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageSystemFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStageEntry.setStatus("current")
_CucsStorageSystemFsmStageInstanceId_Type = CucsManagedObjectId
_CucsStorageSystemFsmStageInstanceId_Object = MibTableColumn
cucsStorageSystemFsmStageInstanceId = _CucsStorageSystemFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 29, 1, 1),
    _CucsStorageSystemFsmStageInstanceId_Type()
)
cucsStorageSystemFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStageInstanceId.setStatus("current")
_CucsStorageSystemFsmStageDn_Type = CucsManagedObjectDn
_CucsStorageSystemFsmStageDn_Object = MibTableColumn
cucsStorageSystemFsmStageDn = _CucsStorageSystemFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 29, 1, 2),
    _CucsStorageSystemFsmStageDn_Type()
)
cucsStorageSystemFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStageDn.setStatus("current")
_CucsStorageSystemFsmStageRn_Type = SnmpAdminString
_CucsStorageSystemFsmStageRn_Object = MibTableColumn
cucsStorageSystemFsmStageRn = _CucsStorageSystemFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 29, 1, 3),
    _CucsStorageSystemFsmStageRn_Type()
)
cucsStorageSystemFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStageRn.setStatus("current")
_CucsStorageSystemFsmStageDescrData_Type = SnmpAdminString
_CucsStorageSystemFsmStageDescrData_Object = MibTableColumn
cucsStorageSystemFsmStageDescrData = _CucsStorageSystemFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 29, 1, 4),
    _CucsStorageSystemFsmStageDescrData_Type()
)
cucsStorageSystemFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStageDescrData.setStatus("current")
_CucsStorageSystemFsmStageLastUpdateTime_Type = DateAndTime
_CucsStorageSystemFsmStageLastUpdateTime_Object = MibTableColumn
cucsStorageSystemFsmStageLastUpdateTime = _CucsStorageSystemFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 29, 1, 5),
    _CucsStorageSystemFsmStageLastUpdateTime_Type()
)
cucsStorageSystemFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStageLastUpdateTime.setStatus("current")
_CucsStorageSystemFsmStageName_Type = CucsStorageSystemFsmStageName
_CucsStorageSystemFsmStageName_Object = MibTableColumn
cucsStorageSystemFsmStageName = _CucsStorageSystemFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 29, 1, 6),
    _CucsStorageSystemFsmStageName_Type()
)
cucsStorageSystemFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStageName.setStatus("current")
_CucsStorageSystemFsmStageOrder_Type = Gauge32
_CucsStorageSystemFsmStageOrder_Object = MibTableColumn
cucsStorageSystemFsmStageOrder = _CucsStorageSystemFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 29, 1, 7),
    _CucsStorageSystemFsmStageOrder_Type()
)
cucsStorageSystemFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStageOrder.setStatus("current")
_CucsStorageSystemFsmStageRetry_Type = Gauge32
_CucsStorageSystemFsmStageRetry_Object = MibTableColumn
cucsStorageSystemFsmStageRetry = _CucsStorageSystemFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 29, 1, 8),
    _CucsStorageSystemFsmStageRetry_Type()
)
cucsStorageSystemFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStageRetry.setStatus("current")
_CucsStorageSystemFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsStorageSystemFsmStageStageStatus_Object = MibTableColumn
cucsStorageSystemFsmStageStageStatus = _CucsStorageSystemFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 29, 1, 9),
    _CucsStorageSystemFsmStageStageStatus_Type()
)
cucsStorageSystemFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmStageStageStatus.setStatus("current")
_CucsStorageSystemFsmTaskTable_Object = MibTable
cucsStorageSystemFsmTaskTable = _CucsStorageSystemFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 30)
)
if mibBuilder.loadTexts:
    cucsStorageSystemFsmTaskTable.setStatus("current")
_CucsStorageSystemFsmTaskEntry_Object = MibTableRow
cucsStorageSystemFsmTaskEntry = _CucsStorageSystemFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 30, 1)
)
cucsStorageSystemFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageSystemFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageSystemFsmTaskEntry.setStatus("current")
_CucsStorageSystemFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsStorageSystemFsmTaskInstanceId_Object = MibTableColumn
cucsStorageSystemFsmTaskInstanceId = _CucsStorageSystemFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 30, 1, 1),
    _CucsStorageSystemFsmTaskInstanceId_Type()
)
cucsStorageSystemFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmTaskInstanceId.setStatus("current")
_CucsStorageSystemFsmTaskDn_Type = CucsManagedObjectDn
_CucsStorageSystemFsmTaskDn_Object = MibTableColumn
cucsStorageSystemFsmTaskDn = _CucsStorageSystemFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 30, 1, 2),
    _CucsStorageSystemFsmTaskDn_Type()
)
cucsStorageSystemFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmTaskDn.setStatus("current")
_CucsStorageSystemFsmTaskRn_Type = SnmpAdminString
_CucsStorageSystemFsmTaskRn_Object = MibTableColumn
cucsStorageSystemFsmTaskRn = _CucsStorageSystemFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 30, 1, 3),
    _CucsStorageSystemFsmTaskRn_Type()
)
cucsStorageSystemFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmTaskRn.setStatus("current")
_CucsStorageSystemFsmTaskCompletion_Type = CucsFsmCompletion
_CucsStorageSystemFsmTaskCompletion_Object = MibTableColumn
cucsStorageSystemFsmTaskCompletion = _CucsStorageSystemFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 30, 1, 4),
    _CucsStorageSystemFsmTaskCompletion_Type()
)
cucsStorageSystemFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmTaskCompletion.setStatus("current")
_CucsStorageSystemFsmTaskFlags_Type = CucsFsmFlags
_CucsStorageSystemFsmTaskFlags_Object = MibTableColumn
cucsStorageSystemFsmTaskFlags = _CucsStorageSystemFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 30, 1, 5),
    _CucsStorageSystemFsmTaskFlags_Type()
)
cucsStorageSystemFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmTaskFlags.setStatus("current")
_CucsStorageSystemFsmTaskItem_Type = CucsStorageSystemFsmTaskItem
_CucsStorageSystemFsmTaskItem_Object = MibTableColumn
cucsStorageSystemFsmTaskItem = _CucsStorageSystemFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 30, 1, 6),
    _CucsStorageSystemFsmTaskItem_Type()
)
cucsStorageSystemFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmTaskItem.setStatus("current")
_CucsStorageSystemFsmTaskSeqId_Type = Gauge32
_CucsStorageSystemFsmTaskSeqId_Object = MibTableColumn
cucsStorageSystemFsmTaskSeqId = _CucsStorageSystemFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 30, 1, 7),
    _CucsStorageSystemFsmTaskSeqId_Type()
)
cucsStorageSystemFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSystemFsmTaskSeqId.setStatus("current")
_CucsStorageVirtualDriveTable_Object = MibTable
cucsStorageVirtualDriveTable = _CucsStorageVirtualDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31)
)
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveTable.setStatus("current")
_CucsStorageVirtualDriveEntry_Object = MibTableRow
cucsStorageVirtualDriveEntry = _CucsStorageVirtualDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1)
)
cucsStorageVirtualDriveEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageVirtualDriveInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveEntry.setStatus("current")
_CucsStorageVirtualDriveInstanceId_Type = CucsManagedObjectId
_CucsStorageVirtualDriveInstanceId_Object = MibTableColumn
cucsStorageVirtualDriveInstanceId = _CucsStorageVirtualDriveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 1),
    _CucsStorageVirtualDriveInstanceId_Type()
)
cucsStorageVirtualDriveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveInstanceId.setStatus("current")
_CucsStorageVirtualDriveDn_Type = CucsManagedObjectDn
_CucsStorageVirtualDriveDn_Object = MibTableColumn
cucsStorageVirtualDriveDn = _CucsStorageVirtualDriveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 2),
    _CucsStorageVirtualDriveDn_Type()
)
cucsStorageVirtualDriveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveDn.setStatus("current")
_CucsStorageVirtualDriveRn_Type = SnmpAdminString
_CucsStorageVirtualDriveRn_Object = MibTableColumn
cucsStorageVirtualDriveRn = _CucsStorageVirtualDriveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 3),
    _CucsStorageVirtualDriveRn_Type()
)
cucsStorageVirtualDriveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRn.setStatus("current")
_CucsStorageVirtualDriveBlockSize_Type = Gauge32
_CucsStorageVirtualDriveBlockSize_Object = MibTableColumn
cucsStorageVirtualDriveBlockSize = _CucsStorageVirtualDriveBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 4),
    _CucsStorageVirtualDriveBlockSize_Type()
)
cucsStorageVirtualDriveBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveBlockSize.setStatus("current")
_CucsStorageVirtualDriveConnectionProtocol_Type = CucsStorageConnectionProtocol
_CucsStorageVirtualDriveConnectionProtocol_Object = MibTableColumn
cucsStorageVirtualDriveConnectionProtocol = _CucsStorageVirtualDriveConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 5),
    _CucsStorageVirtualDriveConnectionProtocol_Type()
)
cucsStorageVirtualDriveConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveConnectionProtocol.setStatus("current")
_CucsStorageVirtualDriveId_Type = Gauge32
_CucsStorageVirtualDriveId_Object = MibTableColumn
cucsStorageVirtualDriveId = _CucsStorageVirtualDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 6),
    _CucsStorageVirtualDriveId_Type()
)
cucsStorageVirtualDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveId.setStatus("current")
_CucsStorageVirtualDriveModel_Type = SnmpAdminString
_CucsStorageVirtualDriveModel_Object = MibTableColumn
cucsStorageVirtualDriveModel = _CucsStorageVirtualDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 7),
    _CucsStorageVirtualDriveModel_Type()
)
cucsStorageVirtualDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveModel.setStatus("current")
_CucsStorageVirtualDriveNumberOfBlocks_Type = Unsigned64
_CucsStorageVirtualDriveNumberOfBlocks_Object = MibTableColumn
cucsStorageVirtualDriveNumberOfBlocks = _CucsStorageVirtualDriveNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 8),
    _CucsStorageVirtualDriveNumberOfBlocks_Type()
)
cucsStorageVirtualDriveNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveNumberOfBlocks.setStatus("current")
_CucsStorageVirtualDriveOperQualifierReason_Type = SnmpAdminString
_CucsStorageVirtualDriveOperQualifierReason_Object = MibTableColumn
cucsStorageVirtualDriveOperQualifierReason = _CucsStorageVirtualDriveOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 9),
    _CucsStorageVirtualDriveOperQualifierReason_Type()
)
cucsStorageVirtualDriveOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveOperQualifierReason.setStatus("current")
_CucsStorageVirtualDriveOperability_Type = CucsEquipmentOperability
_CucsStorageVirtualDriveOperability_Object = MibTableColumn
cucsStorageVirtualDriveOperability = _CucsStorageVirtualDriveOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 10),
    _CucsStorageVirtualDriveOperability_Type()
)
cucsStorageVirtualDriveOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveOperability.setStatus("current")
_CucsStorageVirtualDrivePresence_Type = CucsEquipmentPresence
_CucsStorageVirtualDrivePresence_Object = MibTableColumn
cucsStorageVirtualDrivePresence = _CucsStorageVirtualDrivePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 11),
    _CucsStorageVirtualDrivePresence_Type()
)
cucsStorageVirtualDrivePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDrivePresence.setStatus("current")
_CucsStorageVirtualDriveRevision_Type = SnmpAdminString
_CucsStorageVirtualDriveRevision_Object = MibTableColumn
cucsStorageVirtualDriveRevision = _CucsStorageVirtualDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 12),
    _CucsStorageVirtualDriveRevision_Type()
)
cucsStorageVirtualDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRevision.setStatus("current")
_CucsStorageVirtualDriveSerial_Type = SnmpAdminString
_CucsStorageVirtualDriveSerial_Object = MibTableColumn
cucsStorageVirtualDriveSerial = _CucsStorageVirtualDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 13),
    _CucsStorageVirtualDriveSerial_Type()
)
cucsStorageVirtualDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveSerial.setStatus("current")
_CucsStorageVirtualDriveSize_Type = Unsigned64
_CucsStorageVirtualDriveSize_Object = MibTableColumn
cucsStorageVirtualDriveSize = _CucsStorageVirtualDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 14),
    _CucsStorageVirtualDriveSize_Type()
)
cucsStorageVirtualDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveSize.setStatus("current")
_CucsStorageVirtualDriveType_Type = CucsStorageLunType
_CucsStorageVirtualDriveType_Object = MibTableColumn
cucsStorageVirtualDriveType = _CucsStorageVirtualDriveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 15),
    _CucsStorageVirtualDriveType_Type()
)
cucsStorageVirtualDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveType.setStatus("current")
_CucsStorageVirtualDriveVendor_Type = SnmpAdminString
_CucsStorageVirtualDriveVendor_Object = MibTableColumn
cucsStorageVirtualDriveVendor = _CucsStorageVirtualDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 16),
    _CucsStorageVirtualDriveVendor_Type()
)
cucsStorageVirtualDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveVendor.setStatus("current")
_CucsStorageVirtualDriveAccessPolicy_Type = CucsStorageAccessType
_CucsStorageVirtualDriveAccessPolicy_Object = MibTableColumn
cucsStorageVirtualDriveAccessPolicy = _CucsStorageVirtualDriveAccessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 17),
    _CucsStorageVirtualDriveAccessPolicy_Type()
)
cucsStorageVirtualDriveAccessPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveAccessPolicy.setStatus("current")
_CucsStorageVirtualDriveActualWriteCachePolicy_Type = CucsStorageActualWriteType
_CucsStorageVirtualDriveActualWriteCachePolicy_Object = MibTableColumn
cucsStorageVirtualDriveActualWriteCachePolicy = _CucsStorageVirtualDriveActualWriteCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 18),
    _CucsStorageVirtualDriveActualWriteCachePolicy_Type()
)
cucsStorageVirtualDriveActualWriteCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveActualWriteCachePolicy.setStatus("current")
_CucsStorageVirtualDriveBootable_Type = CucsStorageBootableType
_CucsStorageVirtualDriveBootable_Object = MibTableColumn
cucsStorageVirtualDriveBootable = _CucsStorageVirtualDriveBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 19),
    _CucsStorageVirtualDriveBootable_Type()
)
cucsStorageVirtualDriveBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveBootable.setStatus("current")
_CucsStorageVirtualDriveConfiguredWriteCachePolicy_Type = CucsStorageConfiguredWriteType
_CucsStorageVirtualDriveConfiguredWriteCachePolicy_Object = MibTableColumn
cucsStorageVirtualDriveConfiguredWriteCachePolicy = _CucsStorageVirtualDriveConfiguredWriteCachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 20),
    _CucsStorageVirtualDriveConfiguredWriteCachePolicy_Type()
)
cucsStorageVirtualDriveConfiguredWriteCachePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveConfiguredWriteCachePolicy.setStatus("current")
_CucsStorageVirtualDriveDriveCache_Type = CucsStorageCacheType
_CucsStorageVirtualDriveDriveCache_Object = MibTableColumn
cucsStorageVirtualDriveDriveCache = _CucsStorageVirtualDriveDriveCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 21),
    _CucsStorageVirtualDriveDriveCache_Type()
)
cucsStorageVirtualDriveDriveCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveDriveCache.setStatus("current")
_CucsStorageVirtualDriveDriveState_Type = CucsStorageVDriveState
_CucsStorageVirtualDriveDriveState_Object = MibTableColumn
cucsStorageVirtualDriveDriveState = _CucsStorageVirtualDriveDriveState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 22),
    _CucsStorageVirtualDriveDriveState_Type()
)
cucsStorageVirtualDriveDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveDriveState.setStatus("current")
_CucsStorageVirtualDriveIoPolicy_Type = CucsStorageIOType
_CucsStorageVirtualDriveIoPolicy_Object = MibTableColumn
cucsStorageVirtualDriveIoPolicy = _CucsStorageVirtualDriveIoPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 23),
    _CucsStorageVirtualDriveIoPolicy_Type()
)
cucsStorageVirtualDriveIoPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveIoPolicy.setStatus("current")
_CucsStorageVirtualDriveLc_Type = CucsFsmLifecycle
_CucsStorageVirtualDriveLc_Object = MibTableColumn
cucsStorageVirtualDriveLc = _CucsStorageVirtualDriveLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 24),
    _CucsStorageVirtualDriveLc_Type()
)
cucsStorageVirtualDriveLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveLc.setStatus("current")
_CucsStorageVirtualDriveReadPolicy_Type = CucsStorageReadType
_CucsStorageVirtualDriveReadPolicy_Object = MibTableColumn
cucsStorageVirtualDriveReadPolicy = _CucsStorageVirtualDriveReadPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 25),
    _CucsStorageVirtualDriveReadPolicy_Type()
)
cucsStorageVirtualDriveReadPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveReadPolicy.setStatus("current")
_CucsStorageVirtualDriveStripSize_Type = Unsigned64
_CucsStorageVirtualDriveStripSize_Object = MibTableColumn
cucsStorageVirtualDriveStripSize = _CucsStorageVirtualDriveStripSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 26),
    _CucsStorageVirtualDriveStripSize_Type()
)
cucsStorageVirtualDriveStripSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveStripSize.setStatus("current")
_CucsStorageVirtualDriveAdminActionTrigger_Type = CucsStorageAdminActionTrigger
_CucsStorageVirtualDriveAdminActionTrigger_Object = MibTableColumn
cucsStorageVirtualDriveAdminActionTrigger = _CucsStorageVirtualDriveAdminActionTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 27),
    _CucsStorageVirtualDriveAdminActionTrigger_Type()
)
cucsStorageVirtualDriveAdminActionTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveAdminActionTrigger.setStatus("current")
_CucsStorageVirtualDriveAdminName_Type = SnmpAdminString
_CucsStorageVirtualDriveAdminName_Object = MibTableColumn
cucsStorageVirtualDriveAdminName = _CucsStorageVirtualDriveAdminName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 28),
    _CucsStorageVirtualDriveAdminName_Type()
)
cucsStorageVirtualDriveAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveAdminName.setStatus("current")
_CucsStorageVirtualDriveAdminState_Type = CucsStorageAdminState
_CucsStorageVirtualDriveAdminState_Object = MibTableColumn
cucsStorageVirtualDriveAdminState = _CucsStorageVirtualDriveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 29),
    _CucsStorageVirtualDriveAdminState_Type()
)
cucsStorageVirtualDriveAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveAdminState.setStatus("current")
_CucsStorageVirtualDriveChangeQualifier_Type = CucsStorageVdChangeQualifierType
_CucsStorageVirtualDriveChangeQualifier_Object = MibTableColumn
cucsStorageVirtualDriveChangeQualifier = _CucsStorageVirtualDriveChangeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 30),
    _CucsStorageVirtualDriveChangeQualifier_Type()
)
cucsStorageVirtualDriveChangeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveChangeQualifier.setStatus("current")
_CucsStorageVirtualDriveConfigQualifierReason_Type = SnmpAdminString
_CucsStorageVirtualDriveConfigQualifierReason_Object = MibTableColumn
cucsStorageVirtualDriveConfigQualifierReason = _CucsStorageVirtualDriveConfigQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 31),
    _CucsStorageVirtualDriveConfigQualifierReason_Type()
)
cucsStorageVirtualDriveConfigQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveConfigQualifierReason.setStatus("current")
_CucsStorageVirtualDriveConfigState_Type = CucsStorageConfigState
_CucsStorageVirtualDriveConfigState_Object = MibTableColumn
cucsStorageVirtualDriveConfigState = _CucsStorageVirtualDriveConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 32),
    _CucsStorageVirtualDriveConfigState_Type()
)
cucsStorageVirtualDriveConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveConfigState.setStatus("current")
_CucsStorageVirtualDriveDeployAction_Type = CucsStorageDeployAction
_CucsStorageVirtualDriveDeployAction_Object = MibTableColumn
cucsStorageVirtualDriveDeployAction = _CucsStorageVirtualDriveDeployAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 33),
    _CucsStorageVirtualDriveDeployAction_Type()
)
cucsStorageVirtualDriveDeployAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveDeployAction.setStatus("current")
_CucsStorageVirtualDriveDescr_Type = SnmpAdminString
_CucsStorageVirtualDriveDescr_Object = MibTableColumn
cucsStorageVirtualDriveDescr = _CucsStorageVirtualDriveDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 34),
    _CucsStorageVirtualDriveDescr_Type()
)
cucsStorageVirtualDriveDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveDescr.setStatus("current")
_CucsStorageVirtualDriveLocale_Type = SnmpAdminString
_CucsStorageVirtualDriveLocale_Object = MibTableColumn
cucsStorageVirtualDriveLocale = _CucsStorageVirtualDriveLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 35),
    _CucsStorageVirtualDriveLocale_Type()
)
cucsStorageVirtualDriveLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveLocale.setStatus("current")
_CucsStorageVirtualDriveName_Type = SnmpAdminString
_CucsStorageVirtualDriveName_Object = MibTableColumn
cucsStorageVirtualDriveName = _CucsStorageVirtualDriveName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 36),
    _CucsStorageVirtualDriveName_Type()
)
cucsStorageVirtualDriveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveName.setStatus("current")
_CucsStorageVirtualDriveOperDeviceId_Type = Gauge32
_CucsStorageVirtualDriveOperDeviceId_Object = MibTableColumn
cucsStorageVirtualDriveOperDeviceId = _CucsStorageVirtualDriveOperDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 37),
    _CucsStorageVirtualDriveOperDeviceId_Type()
)
cucsStorageVirtualDriveOperDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveOperDeviceId.setStatus("current")
_CucsStorageVirtualDriveOperState_Type = CucsStorageUnitOperState
_CucsStorageVirtualDriveOperState_Object = MibTableColumn
cucsStorageVirtualDriveOperState = _CucsStorageVirtualDriveOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 38),
    _CucsStorageVirtualDriveOperState_Type()
)
cucsStorageVirtualDriveOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveOperState.setStatus("current")
_CucsStorageVirtualDriveUuid_Type = SnmpAdminString
_CucsStorageVirtualDriveUuid_Object = MibTableColumn
cucsStorageVirtualDriveUuid = _CucsStorageVirtualDriveUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 39),
    _CucsStorageVirtualDriveUuid_Type()
)
cucsStorageVirtualDriveUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveUuid.setStatus("current")
_CucsStorageVirtualDriveVendorUuid_Type = SnmpAdminString
_CucsStorageVirtualDriveVendorUuid_Object = MibTableColumn
cucsStorageVirtualDriveVendorUuid = _CucsStorageVirtualDriveVendorUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 40),
    _CucsStorageVirtualDriveVendorUuid_Type()
)
cucsStorageVirtualDriveVendorUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveVendorUuid.setStatus("current")
_CucsStorageVirtualDriveAvailableSize_Type = Unsigned64
_CucsStorageVirtualDriveAvailableSize_Object = MibTableColumn
cucsStorageVirtualDriveAvailableSize = _CucsStorageVirtualDriveAvailableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 41),
    _CucsStorageVirtualDriveAvailableSize_Type()
)
cucsStorageVirtualDriveAvailableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveAvailableSize.setStatus("current")
_CucsStorageVirtualDrivePnDn_Type = SnmpAdminString
_CucsStorageVirtualDrivePnDn_Object = MibTableColumn
cucsStorageVirtualDrivePnDn = _CucsStorageVirtualDrivePnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 42),
    _CucsStorageVirtualDrivePnDn_Type()
)
cucsStorageVirtualDrivePnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDrivePnDn.setStatus("current")
_CucsStorageVirtualDriveRefDn_Type = SnmpAdminString
_CucsStorageVirtualDriveRefDn_Object = MibTableColumn
cucsStorageVirtualDriveRefDn = _CucsStorageVirtualDriveRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 31, 1, 43),
    _CucsStorageVirtualDriveRefDn_Type()
)
cucsStorageVirtualDriveRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefDn.setStatus("current")
_CucsStorageVsanRefTable_Object = MibTable
cucsStorageVsanRefTable = _CucsStorageVsanRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 32)
)
if mibBuilder.loadTexts:
    cucsStorageVsanRefTable.setStatus("current")
_CucsStorageVsanRefEntry_Object = MibTableRow
cucsStorageVsanRefEntry = _CucsStorageVsanRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 32, 1)
)
cucsStorageVsanRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageVsanRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageVsanRefEntry.setStatus("current")
_CucsStorageVsanRefInstanceId_Type = CucsManagedObjectId
_CucsStorageVsanRefInstanceId_Object = MibTableColumn
cucsStorageVsanRefInstanceId = _CucsStorageVsanRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 32, 1, 1),
    _CucsStorageVsanRefInstanceId_Type()
)
cucsStorageVsanRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageVsanRefInstanceId.setStatus("current")
_CucsStorageVsanRefDn_Type = CucsManagedObjectDn
_CucsStorageVsanRefDn_Object = MibTableColumn
cucsStorageVsanRefDn = _CucsStorageVsanRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 32, 1, 2),
    _CucsStorageVsanRefDn_Type()
)
cucsStorageVsanRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVsanRefDn.setStatus("current")
_CucsStorageVsanRefRn_Type = SnmpAdminString
_CucsStorageVsanRefRn_Object = MibTableColumn
cucsStorageVsanRefRn = _CucsStorageVsanRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 32, 1, 3),
    _CucsStorageVsanRefRn_Type()
)
cucsStorageVsanRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVsanRefRn.setStatus("current")
_CucsStorageVsanRefConfigQualifier_Type = CucsVnicConfigIssues
_CucsStorageVsanRefConfigQualifier_Object = MibTableColumn
cucsStorageVsanRefConfigQualifier = _CucsStorageVsanRefConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 32, 1, 4),
    _CucsStorageVsanRefConfigQualifier_Type()
)
cucsStorageVsanRefConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVsanRefConfigQualifier.setStatus("current")
_CucsStorageVsanRefName_Type = SnmpAdminString
_CucsStorageVsanRefName_Object = MibTableColumn
cucsStorageVsanRefName = _CucsStorageVsanRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 32, 1, 5),
    _CucsStorageVsanRefName_Type()
)
cucsStorageVsanRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVsanRefName.setStatus("current")
_CucsStorageVsanRefOperVnetDn_Type = SnmpAdminString
_CucsStorageVsanRefOperVnetDn_Object = MibTableColumn
cucsStorageVsanRefOperVnetDn = _CucsStorageVsanRefOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 32, 1, 6),
    _CucsStorageVsanRefOperVnetDn_Type()
)
cucsStorageVsanRefOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVsanRefOperVnetDn.setStatus("current")
_CucsStorageVsanRefOperVnetName_Type = SnmpAdminString
_CucsStorageVsanRefOperVnetName_Object = MibTableColumn
cucsStorageVsanRefOperVnetName = _CucsStorageVsanRefOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 32, 1, 7),
    _CucsStorageVsanRefOperVnetName_Type()
)
cucsStorageVsanRefOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVsanRefOperVnetName.setStatus("current")
_CucsStorageVsanRefSwitchId_Type = CucsStorageVsanRefSwitchId
_CucsStorageVsanRefSwitchId_Object = MibTableColumn
cucsStorageVsanRefSwitchId = _CucsStorageVsanRefSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 32, 1, 8),
    _CucsStorageVsanRefSwitchId_Type()
)
cucsStorageVsanRefSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVsanRefSwitchId.setStatus("current")
_CucsStorageVsanRefVnet_Type = Gauge32
_CucsStorageVsanRefVnet_Object = MibTableColumn
cucsStorageVsanRefVnet = _CucsStorageVsanRefVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 32, 1, 9),
    _CucsStorageVsanRefVnet_Type()
)
cucsStorageVsanRefVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVsanRefVnet.setStatus("current")
_CucsStorageVsanRefZoningState_Type = CucsFabricZoningState
_CucsStorageVsanRefZoningState_Object = MibTableColumn
cucsStorageVsanRefZoningState = _CucsStorageVsanRefZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 32, 1, 10),
    _CucsStorageVsanRefZoningState_Type()
)
cucsStorageVsanRefZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVsanRefZoningState.setStatus("current")
_CucsStorageTransportableFlashModuleTable_Object = MibTable
cucsStorageTransportableFlashModuleTable = _CucsStorageTransportableFlashModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33)
)
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleTable.setStatus("current")
_CucsStorageTransportableFlashModuleEntry_Object = MibTableRow
cucsStorageTransportableFlashModuleEntry = _CucsStorageTransportableFlashModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1)
)
cucsStorageTransportableFlashModuleEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageTransportableFlashModuleInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleEntry.setStatus("current")
_CucsStorageTransportableFlashModuleInstanceId_Type = CucsManagedObjectId
_CucsStorageTransportableFlashModuleInstanceId_Object = MibTableColumn
cucsStorageTransportableFlashModuleInstanceId = _CucsStorageTransportableFlashModuleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 1),
    _CucsStorageTransportableFlashModuleInstanceId_Type()
)
cucsStorageTransportableFlashModuleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleInstanceId.setStatus("current")
_CucsStorageTransportableFlashModuleDn_Type = CucsManagedObjectDn
_CucsStorageTransportableFlashModuleDn_Object = MibTableColumn
cucsStorageTransportableFlashModuleDn = _CucsStorageTransportableFlashModuleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 2),
    _CucsStorageTransportableFlashModuleDn_Type()
)
cucsStorageTransportableFlashModuleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleDn.setStatus("current")
_CucsStorageTransportableFlashModuleRn_Type = SnmpAdminString
_CucsStorageTransportableFlashModuleRn_Object = MibTableColumn
cucsStorageTransportableFlashModuleRn = _CucsStorageTransportableFlashModuleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 3),
    _CucsStorageTransportableFlashModuleRn_Type()
)
cucsStorageTransportableFlashModuleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleRn.setStatus("current")
_CucsStorageTransportableFlashModuleBlockSize_Type = Gauge32
_CucsStorageTransportableFlashModuleBlockSize_Object = MibTableColumn
cucsStorageTransportableFlashModuleBlockSize = _CucsStorageTransportableFlashModuleBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 4),
    _CucsStorageTransportableFlashModuleBlockSize_Type()
)
cucsStorageTransportableFlashModuleBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleBlockSize.setStatus("current")
_CucsStorageTransportableFlashModuleConnectionProtocol_Type = CucsStorageConnectionProtocol
_CucsStorageTransportableFlashModuleConnectionProtocol_Object = MibTableColumn
cucsStorageTransportableFlashModuleConnectionProtocol = _CucsStorageTransportableFlashModuleConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 5),
    _CucsStorageTransportableFlashModuleConnectionProtocol_Type()
)
cucsStorageTransportableFlashModuleConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleConnectionProtocol.setStatus("current")
_CucsStorageTransportableFlashModuleId_Type = Gauge32
_CucsStorageTransportableFlashModuleId_Object = MibTableColumn
cucsStorageTransportableFlashModuleId = _CucsStorageTransportableFlashModuleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 6),
    _CucsStorageTransportableFlashModuleId_Type()
)
cucsStorageTransportableFlashModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleId.setStatus("current")
_CucsStorageTransportableFlashModuleModel_Type = SnmpAdminString
_CucsStorageTransportableFlashModuleModel_Object = MibTableColumn
cucsStorageTransportableFlashModuleModel = _CucsStorageTransportableFlashModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 7),
    _CucsStorageTransportableFlashModuleModel_Type()
)
cucsStorageTransportableFlashModuleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleModel.setStatus("current")
_CucsStorageTransportableFlashModuleNumberOfBlocks_Type = Unsigned64
_CucsStorageTransportableFlashModuleNumberOfBlocks_Object = MibTableColumn
cucsStorageTransportableFlashModuleNumberOfBlocks = _CucsStorageTransportableFlashModuleNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 8),
    _CucsStorageTransportableFlashModuleNumberOfBlocks_Type()
)
cucsStorageTransportableFlashModuleNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleNumberOfBlocks.setStatus("current")
_CucsStorageTransportableFlashModuleOperQualifierReason_Type = SnmpAdminString
_CucsStorageTransportableFlashModuleOperQualifierReason_Object = MibTableColumn
cucsStorageTransportableFlashModuleOperQualifierReason = _CucsStorageTransportableFlashModuleOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 9),
    _CucsStorageTransportableFlashModuleOperQualifierReason_Type()
)
cucsStorageTransportableFlashModuleOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleOperQualifierReason.setStatus("current")
_CucsStorageTransportableFlashModuleOperability_Type = CucsEquipmentOperability
_CucsStorageTransportableFlashModuleOperability_Object = MibTableColumn
cucsStorageTransportableFlashModuleOperability = _CucsStorageTransportableFlashModuleOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 10),
    _CucsStorageTransportableFlashModuleOperability_Type()
)
cucsStorageTransportableFlashModuleOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleOperability.setStatus("current")
_CucsStorageTransportableFlashModulePresence_Type = CucsEquipmentPresence
_CucsStorageTransportableFlashModulePresence_Object = MibTableColumn
cucsStorageTransportableFlashModulePresence = _CucsStorageTransportableFlashModulePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 11),
    _CucsStorageTransportableFlashModulePresence_Type()
)
cucsStorageTransportableFlashModulePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModulePresence.setStatus("current")
_CucsStorageTransportableFlashModuleRevision_Type = SnmpAdminString
_CucsStorageTransportableFlashModuleRevision_Object = MibTableColumn
cucsStorageTransportableFlashModuleRevision = _CucsStorageTransportableFlashModuleRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 12),
    _CucsStorageTransportableFlashModuleRevision_Type()
)
cucsStorageTransportableFlashModuleRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleRevision.setStatus("current")
_CucsStorageTransportableFlashModuleSerial_Type = SnmpAdminString
_CucsStorageTransportableFlashModuleSerial_Object = MibTableColumn
cucsStorageTransportableFlashModuleSerial = _CucsStorageTransportableFlashModuleSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 13),
    _CucsStorageTransportableFlashModuleSerial_Type()
)
cucsStorageTransportableFlashModuleSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleSerial.setStatus("current")
_CucsStorageTransportableFlashModuleSize_Type = Unsigned64
_CucsStorageTransportableFlashModuleSize_Object = MibTableColumn
cucsStorageTransportableFlashModuleSize = _CucsStorageTransportableFlashModuleSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 14),
    _CucsStorageTransportableFlashModuleSize_Type()
)
cucsStorageTransportableFlashModuleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleSize.setStatus("current")
_CucsStorageTransportableFlashModuleVendor_Type = SnmpAdminString
_CucsStorageTransportableFlashModuleVendor_Object = MibTableColumn
cucsStorageTransportableFlashModuleVendor = _CucsStorageTransportableFlashModuleVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 33, 1, 15),
    _CucsStorageTransportableFlashModuleVendor_Type()
)
cucsStorageTransportableFlashModuleVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageTransportableFlashModuleVendor.setStatus("current")
_CucsStorageFlexFlashCardTable_Object = MibTable
cucsStorageFlexFlashCardTable = _CucsStorageFlexFlashCardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34)
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardTable.setStatus("current")
_CucsStorageFlexFlashCardEntry_Object = MibTableRow
cucsStorageFlexFlashCardEntry = _CucsStorageFlexFlashCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1)
)
cucsStorageFlexFlashCardEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageFlexFlashCardInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardEntry.setStatus("current")
_CucsStorageFlexFlashCardInstanceId_Type = CucsManagedObjectId
_CucsStorageFlexFlashCardInstanceId_Object = MibTableColumn
cucsStorageFlexFlashCardInstanceId = _CucsStorageFlexFlashCardInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 1),
    _CucsStorageFlexFlashCardInstanceId_Type()
)
cucsStorageFlexFlashCardInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardInstanceId.setStatus("current")
_CucsStorageFlexFlashCardDn_Type = CucsManagedObjectDn
_CucsStorageFlexFlashCardDn_Object = MibTableColumn
cucsStorageFlexFlashCardDn = _CucsStorageFlexFlashCardDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 2),
    _CucsStorageFlexFlashCardDn_Type()
)
cucsStorageFlexFlashCardDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardDn.setStatus("current")
_CucsStorageFlexFlashCardRn_Type = SnmpAdminString
_CucsStorageFlexFlashCardRn_Object = MibTableColumn
cucsStorageFlexFlashCardRn = _CucsStorageFlexFlashCardRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 3),
    _CucsStorageFlexFlashCardRn_Type()
)
cucsStorageFlexFlashCardRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardRn.setStatus("current")
_CucsStorageFlexFlashCardBlockSize_Type = Gauge32
_CucsStorageFlexFlashCardBlockSize_Object = MibTableColumn
cucsStorageFlexFlashCardBlockSize = _CucsStorageFlexFlashCardBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 4),
    _CucsStorageFlexFlashCardBlockSize_Type()
)
cucsStorageFlexFlashCardBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardBlockSize.setStatus("current")
_CucsStorageFlexFlashCardCardHealth_Type = CucsStorageFFCardHealth
_CucsStorageFlexFlashCardCardHealth_Object = MibTableColumn
cucsStorageFlexFlashCardCardHealth = _CucsStorageFlexFlashCardCardHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 5),
    _CucsStorageFlexFlashCardCardHealth_Type()
)
cucsStorageFlexFlashCardCardHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardCardHealth.setStatus("current")
_CucsStorageFlexFlashCardCardMode_Type = CucsStorageFFCardMode
_CucsStorageFlexFlashCardCardMode_Object = MibTableColumn
cucsStorageFlexFlashCardCardMode = _CucsStorageFlexFlashCardCardMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 6),
    _CucsStorageFlexFlashCardCardMode_Type()
)
cucsStorageFlexFlashCardCardMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardCardMode.setStatus("current")
_CucsStorageFlexFlashCardCardType_Type = SnmpAdminString
_CucsStorageFlexFlashCardCardType_Object = MibTableColumn
cucsStorageFlexFlashCardCardType = _CucsStorageFlexFlashCardCardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 7),
    _CucsStorageFlexFlashCardCardType_Type()
)
cucsStorageFlexFlashCardCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardCardType.setStatus("current")
_CucsStorageFlexFlashCardConnectionProtocol_Type = CucsStorageConnectionProtocol
_CucsStorageFlexFlashCardConnectionProtocol_Object = MibTableColumn
cucsStorageFlexFlashCardConnectionProtocol = _CucsStorageFlexFlashCardConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 8),
    _CucsStorageFlexFlashCardConnectionProtocol_Type()
)
cucsStorageFlexFlashCardConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardConnectionProtocol.setStatus("current")
_CucsStorageFlexFlashCardControllerIndex_Type = Gauge32
_CucsStorageFlexFlashCardControllerIndex_Object = MibTableColumn
cucsStorageFlexFlashCardControllerIndex = _CucsStorageFlexFlashCardControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 9),
    _CucsStorageFlexFlashCardControllerIndex_Type()
)
cucsStorageFlexFlashCardControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardControllerIndex.setStatus("current")
_CucsStorageFlexFlashCardId_Type = Gauge32
_CucsStorageFlexFlashCardId_Object = MibTableColumn
cucsStorageFlexFlashCardId = _CucsStorageFlexFlashCardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 10),
    _CucsStorageFlexFlashCardId_Type()
)
cucsStorageFlexFlashCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardId.setStatus("current")
_CucsStorageFlexFlashCardMfgDate_Type = SnmpAdminString
_CucsStorageFlexFlashCardMfgDate_Object = MibTableColumn
cucsStorageFlexFlashCardMfgDate = _CucsStorageFlexFlashCardMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 11),
    _CucsStorageFlexFlashCardMfgDate_Type()
)
cucsStorageFlexFlashCardMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardMfgDate.setStatus("current")
_CucsStorageFlexFlashCardMfgId_Type = SnmpAdminString
_CucsStorageFlexFlashCardMfgId_Object = MibTableColumn
cucsStorageFlexFlashCardMfgId = _CucsStorageFlexFlashCardMfgId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 12),
    _CucsStorageFlexFlashCardMfgId_Type()
)
cucsStorageFlexFlashCardMfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardMfgId.setStatus("current")
_CucsStorageFlexFlashCardModel_Type = SnmpAdminString
_CucsStorageFlexFlashCardModel_Object = MibTableColumn
cucsStorageFlexFlashCardModel = _CucsStorageFlexFlashCardModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 13),
    _CucsStorageFlexFlashCardModel_Type()
)
cucsStorageFlexFlashCardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardModel.setStatus("current")
_CucsStorageFlexFlashCardNumberOfBlocks_Type = Unsigned64
_CucsStorageFlexFlashCardNumberOfBlocks_Object = MibTableColumn
cucsStorageFlexFlashCardNumberOfBlocks = _CucsStorageFlexFlashCardNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 14),
    _CucsStorageFlexFlashCardNumberOfBlocks_Type()
)
cucsStorageFlexFlashCardNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardNumberOfBlocks.setStatus("current")
_CucsStorageFlexFlashCardOemId_Type = SnmpAdminString
_CucsStorageFlexFlashCardOemId_Object = MibTableColumn
cucsStorageFlexFlashCardOemId = _CucsStorageFlexFlashCardOemId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 15),
    _CucsStorageFlexFlashCardOemId_Type()
)
cucsStorageFlexFlashCardOemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardOemId.setStatus("current")
_CucsStorageFlexFlashCardOperQualifierReason_Type = SnmpAdminString
_CucsStorageFlexFlashCardOperQualifierReason_Object = MibTableColumn
cucsStorageFlexFlashCardOperQualifierReason = _CucsStorageFlexFlashCardOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 16),
    _CucsStorageFlexFlashCardOperQualifierReason_Type()
)
cucsStorageFlexFlashCardOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardOperQualifierReason.setStatus("current")
_CucsStorageFlexFlashCardOperability_Type = CucsEquipmentOperability
_CucsStorageFlexFlashCardOperability_Object = MibTableColumn
cucsStorageFlexFlashCardOperability = _CucsStorageFlexFlashCardOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 17),
    _CucsStorageFlexFlashCardOperability_Type()
)
cucsStorageFlexFlashCardOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardOperability.setStatus("current")
_CucsStorageFlexFlashCardPresence_Type = CucsEquipmentPresence
_CucsStorageFlexFlashCardPresence_Object = MibTableColumn
cucsStorageFlexFlashCardPresence = _CucsStorageFlexFlashCardPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 18),
    _CucsStorageFlexFlashCardPresence_Type()
)
cucsStorageFlexFlashCardPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardPresence.setStatus("current")
_CucsStorageFlexFlashCardReadIOErrorCount_Type = Gauge32
_CucsStorageFlexFlashCardReadIOErrorCount_Object = MibTableColumn
cucsStorageFlexFlashCardReadIOErrorCount = _CucsStorageFlexFlashCardReadIOErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 19),
    _CucsStorageFlexFlashCardReadIOErrorCount_Type()
)
cucsStorageFlexFlashCardReadIOErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardReadIOErrorCount.setStatus("current")
_CucsStorageFlexFlashCardRevision_Type = SnmpAdminString
_CucsStorageFlexFlashCardRevision_Object = MibTableColumn
cucsStorageFlexFlashCardRevision = _CucsStorageFlexFlashCardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 20),
    _CucsStorageFlexFlashCardRevision_Type()
)
cucsStorageFlexFlashCardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardRevision.setStatus("current")
_CucsStorageFlexFlashCardSerial_Type = SnmpAdminString
_CucsStorageFlexFlashCardSerial_Object = MibTableColumn
cucsStorageFlexFlashCardSerial = _CucsStorageFlexFlashCardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 21),
    _CucsStorageFlexFlashCardSerial_Type()
)
cucsStorageFlexFlashCardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardSerial.setStatus("current")
_CucsStorageFlexFlashCardSize_Type = Unsigned64
_CucsStorageFlexFlashCardSize_Object = MibTableColumn
cucsStorageFlexFlashCardSize = _CucsStorageFlexFlashCardSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 22),
    _CucsStorageFlexFlashCardSize_Type()
)
cucsStorageFlexFlashCardSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardSize.setStatus("current")
_CucsStorageFlexFlashCardSlotNumber_Type = Gauge32
_CucsStorageFlexFlashCardSlotNumber_Object = MibTableColumn
cucsStorageFlexFlashCardSlotNumber = _CucsStorageFlexFlashCardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 23),
    _CucsStorageFlexFlashCardSlotNumber_Type()
)
cucsStorageFlexFlashCardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardSlotNumber.setStatus("current")
_CucsStorageFlexFlashCardVendor_Type = SnmpAdminString
_CucsStorageFlexFlashCardVendor_Object = MibTableColumn
cucsStorageFlexFlashCardVendor = _CucsStorageFlexFlashCardVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 24),
    _CucsStorageFlexFlashCardVendor_Type()
)
cucsStorageFlexFlashCardVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardVendor.setStatus("current")
_CucsStorageFlexFlashCardWriteEnable_Type = CucsStorageFFCardWriteEnable
_CucsStorageFlexFlashCardWriteEnable_Object = MibTableColumn
cucsStorageFlexFlashCardWriteEnable = _CucsStorageFlexFlashCardWriteEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 25),
    _CucsStorageFlexFlashCardWriteEnable_Type()
)
cucsStorageFlexFlashCardWriteEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardWriteEnable.setStatus("current")
_CucsStorageFlexFlashCardWriteIOErrorCount_Type = Gauge32
_CucsStorageFlexFlashCardWriteIOErrorCount_Object = MibTableColumn
cucsStorageFlexFlashCardWriteIOErrorCount = _CucsStorageFlexFlashCardWriteIOErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 26),
    _CucsStorageFlexFlashCardWriteIOErrorCount_Type()
)
cucsStorageFlexFlashCardWriteIOErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardWriteIOErrorCount.setStatus("current")
_CucsStorageFlexFlashCardCardState_Type = CucsStorageFFCardState
_CucsStorageFlexFlashCardCardState_Object = MibTableColumn
cucsStorageFlexFlashCardCardState = _CucsStorageFlexFlashCardCardState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 27),
    _CucsStorageFlexFlashCardCardState_Type()
)
cucsStorageFlexFlashCardCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardCardState.setStatus("current")
_CucsStorageFlexFlashCardCardSync_Type = CucsStorageFFCardSync
_CucsStorageFlexFlashCardCardSync_Object = MibTableColumn
cucsStorageFlexFlashCardCardSync = _CucsStorageFlexFlashCardCardSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 28),
    _CucsStorageFlexFlashCardCardSync_Type()
)
cucsStorageFlexFlashCardCardSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardCardSync.setStatus("current")
_CucsStorageFlexFlashCardDrivesEnabled_Type = SnmpAdminString
_CucsStorageFlexFlashCardDrivesEnabled_Object = MibTableColumn
cucsStorageFlexFlashCardDrivesEnabled = _CucsStorageFlexFlashCardDrivesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 29),
    _CucsStorageFlexFlashCardDrivesEnabled_Type()
)
cucsStorageFlexFlashCardDrivesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardDrivesEnabled.setStatus("current")
_CucsStorageFlexFlashCardPartitionCount_Type = Gauge32
_CucsStorageFlexFlashCardPartitionCount_Object = MibTableColumn
cucsStorageFlexFlashCardPartitionCount = _CucsStorageFlexFlashCardPartitionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 30),
    _CucsStorageFlexFlashCardPartitionCount_Type()
)
cucsStorageFlexFlashCardPartitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardPartitionCount.setStatus("current")
_CucsStorageFlexFlashCardReadErrorThreshold_Type = Gauge32
_CucsStorageFlexFlashCardReadErrorThreshold_Object = MibTableColumn
cucsStorageFlexFlashCardReadErrorThreshold = _CucsStorageFlexFlashCardReadErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 31),
    _CucsStorageFlexFlashCardReadErrorThreshold_Type()
)
cucsStorageFlexFlashCardReadErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardReadErrorThreshold.setStatus("current")
_CucsStorageFlexFlashCardSignature_Type = SnmpAdminString
_CucsStorageFlexFlashCardSignature_Object = MibTableColumn
cucsStorageFlexFlashCardSignature = _CucsStorageFlexFlashCardSignature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 32),
    _CucsStorageFlexFlashCardSignature_Type()
)
cucsStorageFlexFlashCardSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardSignature.setStatus("current")
_CucsStorageFlexFlashCardWriteErrorThreshold_Type = Gauge32
_CucsStorageFlexFlashCardWriteErrorThreshold_Object = MibTableColumn
cucsStorageFlexFlashCardWriteErrorThreshold = _CucsStorageFlexFlashCardWriteErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 34, 1, 33),
    _CucsStorageFlexFlashCardWriteErrorThreshold_Type()
)
cucsStorageFlexFlashCardWriteErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashCardWriteErrorThreshold.setStatus("current")
_CucsStorageFlexFlashControllerTable_Object = MibTable
cucsStorageFlexFlashControllerTable = _CucsStorageFlexFlashControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35)
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerTable.setStatus("current")
_CucsStorageFlexFlashControllerEntry_Object = MibTableRow
cucsStorageFlexFlashControllerEntry = _CucsStorageFlexFlashControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1)
)
cucsStorageFlexFlashControllerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageFlexFlashControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerEntry.setStatus("current")
_CucsStorageFlexFlashControllerInstanceId_Type = CucsManagedObjectId
_CucsStorageFlexFlashControllerInstanceId_Object = MibTableColumn
cucsStorageFlexFlashControllerInstanceId = _CucsStorageFlexFlashControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 1),
    _CucsStorageFlexFlashControllerInstanceId_Type()
)
cucsStorageFlexFlashControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerInstanceId.setStatus("current")
_CucsStorageFlexFlashControllerDn_Type = CucsManagedObjectDn
_CucsStorageFlexFlashControllerDn_Object = MibTableColumn
cucsStorageFlexFlashControllerDn = _CucsStorageFlexFlashControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 2),
    _CucsStorageFlexFlashControllerDn_Type()
)
cucsStorageFlexFlashControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerDn.setStatus("current")
_CucsStorageFlexFlashControllerRn_Type = SnmpAdminString
_CucsStorageFlexFlashControllerRn_Object = MibTableColumn
cucsStorageFlexFlashControllerRn = _CucsStorageFlexFlashControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 3),
    _CucsStorageFlexFlashControllerRn_Type()
)
cucsStorageFlexFlashControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerRn.setStatus("current")
_CucsStorageFlexFlashControllerControllerHealth_Type = CucsStorageFFControllerHealth
_CucsStorageFlexFlashControllerControllerHealth_Object = MibTableColumn
cucsStorageFlexFlashControllerControllerHealth = _CucsStorageFlexFlashControllerControllerHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 4),
    _CucsStorageFlexFlashControllerControllerHealth_Type()
)
cucsStorageFlexFlashControllerControllerHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerControllerHealth.setStatus("current")
_CucsStorageFlexFlashControllerControllerState_Type = CucsStorageFFControllerState
_CucsStorageFlexFlashControllerControllerState_Object = MibTableColumn
cucsStorageFlexFlashControllerControllerState = _CucsStorageFlexFlashControllerControllerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 5),
    _CucsStorageFlexFlashControllerControllerState_Type()
)
cucsStorageFlexFlashControllerControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerControllerState.setStatus("current")
_CucsStorageFlexFlashControllerFlexFlashType_Type = CucsStorageFFType
_CucsStorageFlexFlashControllerFlexFlashType_Object = MibTableColumn
cucsStorageFlexFlashControllerFlexFlashType = _CucsStorageFlexFlashControllerFlexFlashType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 6),
    _CucsStorageFlexFlashControllerFlexFlashType_Type()
)
cucsStorageFlexFlashControllerFlexFlashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFlexFlashType.setStatus("current")
_CucsStorageFlexFlashControllerId_Type = CucsStorageFlexFlashControllerId
_CucsStorageFlexFlashControllerId_Object = MibTableColumn
cucsStorageFlexFlashControllerId = _CucsStorageFlexFlashControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 7),
    _CucsStorageFlexFlashControllerId_Type()
)
cucsStorageFlexFlashControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerId.setStatus("current")
_CucsStorageFlexFlashControllerModel_Type = SnmpAdminString
_CucsStorageFlexFlashControllerModel_Object = MibTableColumn
cucsStorageFlexFlashControllerModel = _CucsStorageFlexFlashControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 8),
    _CucsStorageFlexFlashControllerModel_Type()
)
cucsStorageFlexFlashControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerModel.setStatus("current")
_CucsStorageFlexFlashControllerOperQualifierReason_Type = SnmpAdminString
_CucsStorageFlexFlashControllerOperQualifierReason_Object = MibTableColumn
cucsStorageFlexFlashControllerOperQualifierReason = _CucsStorageFlexFlashControllerOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 9),
    _CucsStorageFlexFlashControllerOperQualifierReason_Type()
)
cucsStorageFlexFlashControllerOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerOperQualifierReason.setStatus("current")
_CucsStorageFlexFlashControllerOperState_Type = CucsEquipmentOperability
_CucsStorageFlexFlashControllerOperState_Object = MibTableColumn
cucsStorageFlexFlashControllerOperState = _CucsStorageFlexFlashControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 10),
    _CucsStorageFlexFlashControllerOperState_Type()
)
cucsStorageFlexFlashControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerOperState.setStatus("current")
_CucsStorageFlexFlashControllerOperability_Type = CucsEquipmentOperability
_CucsStorageFlexFlashControllerOperability_Object = MibTableColumn
cucsStorageFlexFlashControllerOperability = _CucsStorageFlexFlashControllerOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 11),
    _CucsStorageFlexFlashControllerOperability_Type()
)
cucsStorageFlexFlashControllerOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerOperability.setStatus("current")
_CucsStorageFlexFlashControllerPciAddr_Type = SnmpAdminString
_CucsStorageFlexFlashControllerPciAddr_Object = MibTableColumn
cucsStorageFlexFlashControllerPciAddr = _CucsStorageFlexFlashControllerPciAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 12),
    _CucsStorageFlexFlashControllerPciAddr_Type()
)
cucsStorageFlexFlashControllerPciAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerPciAddr.setStatus("current")
_CucsStorageFlexFlashControllerPciSlot_Type = SnmpAdminString
_CucsStorageFlexFlashControllerPciSlot_Object = MibTableColumn
cucsStorageFlexFlashControllerPciSlot = _CucsStorageFlexFlashControllerPciSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 13),
    _CucsStorageFlexFlashControllerPciSlot_Type()
)
cucsStorageFlexFlashControllerPciSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerPciSlot.setStatus("current")
_CucsStorageFlexFlashControllerPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsStorageFlexFlashControllerPerf_Object = MibTableColumn
cucsStorageFlexFlashControllerPerf = _CucsStorageFlexFlashControllerPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 14),
    _CucsStorageFlexFlashControllerPerf_Type()
)
cucsStorageFlexFlashControllerPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerPerf.setStatus("current")
_CucsStorageFlexFlashControllerPhysicalDriveCount_Type = Gauge32
_CucsStorageFlexFlashControllerPhysicalDriveCount_Object = MibTableColumn
cucsStorageFlexFlashControllerPhysicalDriveCount = _CucsStorageFlexFlashControllerPhysicalDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 15),
    _CucsStorageFlexFlashControllerPhysicalDriveCount_Type()
)
cucsStorageFlexFlashControllerPhysicalDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerPhysicalDriveCount.setStatus("current")
_CucsStorageFlexFlashControllerPower_Type = CucsEquipmentPowerState
_CucsStorageFlexFlashControllerPower_Object = MibTableColumn
cucsStorageFlexFlashControllerPower = _CucsStorageFlexFlashControllerPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 16),
    _CucsStorageFlexFlashControllerPower_Type()
)
cucsStorageFlexFlashControllerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerPower.setStatus("current")
_CucsStorageFlexFlashControllerPresence_Type = CucsEquipmentPresence
_CucsStorageFlexFlashControllerPresence_Object = MibTableColumn
cucsStorageFlexFlashControllerPresence = _CucsStorageFlexFlashControllerPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 17),
    _CucsStorageFlexFlashControllerPresence_Type()
)
cucsStorageFlexFlashControllerPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerPresence.setStatus("current")
_CucsStorageFlexFlashControllerPrimarySlotNumber_Type = Gauge32
_CucsStorageFlexFlashControllerPrimarySlotNumber_Object = MibTableColumn
cucsStorageFlexFlashControllerPrimarySlotNumber = _CucsStorageFlexFlashControllerPrimarySlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 18),
    _CucsStorageFlexFlashControllerPrimarySlotNumber_Type()
)
cucsStorageFlexFlashControllerPrimarySlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerPrimarySlotNumber.setStatus("current")
_CucsStorageFlexFlashControllerRaidSyncSupport_Type = CucsStorageFFRaidSyncSupport
_CucsStorageFlexFlashControllerRaidSyncSupport_Object = MibTableColumn
cucsStorageFlexFlashControllerRaidSyncSupport = _CucsStorageFlexFlashControllerRaidSyncSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 19),
    _CucsStorageFlexFlashControllerRaidSyncSupport_Type()
)
cucsStorageFlexFlashControllerRaidSyncSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerRaidSyncSupport.setStatus("current")
_CucsStorageFlexFlashControllerReadErrorThreshold_Type = Gauge32
_CucsStorageFlexFlashControllerReadErrorThreshold_Object = MibTableColumn
cucsStorageFlexFlashControllerReadErrorThreshold = _CucsStorageFlexFlashControllerReadErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 20),
    _CucsStorageFlexFlashControllerReadErrorThreshold_Type()
)
cucsStorageFlexFlashControllerReadErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerReadErrorThreshold.setStatus("current")
_CucsStorageFlexFlashControllerRevision_Type = SnmpAdminString
_CucsStorageFlexFlashControllerRevision_Object = MibTableColumn
cucsStorageFlexFlashControllerRevision = _CucsStorageFlexFlashControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 21),
    _CucsStorageFlexFlashControllerRevision_Type()
)
cucsStorageFlexFlashControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerRevision.setStatus("current")
_CucsStorageFlexFlashControllerSerial_Type = SnmpAdminString
_CucsStorageFlexFlashControllerSerial_Object = MibTableColumn
cucsStorageFlexFlashControllerSerial = _CucsStorageFlexFlashControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 22),
    _CucsStorageFlexFlashControllerSerial_Type()
)
cucsStorageFlexFlashControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerSerial.setStatus("current")
_CucsStorageFlexFlashControllerThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsStorageFlexFlashControllerThermal_Object = MibTableColumn
cucsStorageFlexFlashControllerThermal = _CucsStorageFlexFlashControllerThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 23),
    _CucsStorageFlexFlashControllerThermal_Type()
)
cucsStorageFlexFlashControllerThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerThermal.setStatus("current")
_CucsStorageFlexFlashControllerType_Type = CucsStorageControllerType
_CucsStorageFlexFlashControllerType_Object = MibTableColumn
cucsStorageFlexFlashControllerType = _CucsStorageFlexFlashControllerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 24),
    _CucsStorageFlexFlashControllerType_Type()
)
cucsStorageFlexFlashControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerType.setStatus("current")
_CucsStorageFlexFlashControllerVendor_Type = SnmpAdminString
_CucsStorageFlexFlashControllerVendor_Object = MibTableColumn
cucsStorageFlexFlashControllerVendor = _CucsStorageFlexFlashControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 25),
    _CucsStorageFlexFlashControllerVendor_Type()
)
cucsStorageFlexFlashControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerVendor.setStatus("current")
_CucsStorageFlexFlashControllerVirtualDriveCount_Type = Gauge32
_CucsStorageFlexFlashControllerVirtualDriveCount_Object = MibTableColumn
cucsStorageFlexFlashControllerVirtualDriveCount = _CucsStorageFlexFlashControllerVirtualDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 26),
    _CucsStorageFlexFlashControllerVirtualDriveCount_Type()
)
cucsStorageFlexFlashControllerVirtualDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerVirtualDriveCount.setStatus("current")
_CucsStorageFlexFlashControllerVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsStorageFlexFlashControllerVoltage_Object = MibTableColumn
cucsStorageFlexFlashControllerVoltage = _CucsStorageFlexFlashControllerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 27),
    _CucsStorageFlexFlashControllerVoltage_Type()
)
cucsStorageFlexFlashControllerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerVoltage.setStatus("current")
_CucsStorageFlexFlashControllerWriteErrorThreshold_Type = Gauge32
_CucsStorageFlexFlashControllerWriteErrorThreshold_Object = MibTableColumn
cucsStorageFlexFlashControllerWriteErrorThreshold = _CucsStorageFlexFlashControllerWriteErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 28),
    _CucsStorageFlexFlashControllerWriteErrorThreshold_Type()
)
cucsStorageFlexFlashControllerWriteErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerWriteErrorThreshold.setStatus("current")
_CucsStorageFlexFlashControllerLocationDn_Type = SnmpAdminString
_CucsStorageFlexFlashControllerLocationDn_Object = MibTableColumn
cucsStorageFlexFlashControllerLocationDn = _CucsStorageFlexFlashControllerLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 29),
    _CucsStorageFlexFlashControllerLocationDn_Type()
)
cucsStorageFlexFlashControllerLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerLocationDn.setStatus("current")
_CucsStorageFlexFlashControllerAdminSlotNumber_Type = CucsStorageFFSlotENUM
_CucsStorageFlexFlashControllerAdminSlotNumber_Object = MibTableColumn
cucsStorageFlexFlashControllerAdminSlotNumber = _CucsStorageFlexFlashControllerAdminSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 30),
    _CucsStorageFlexFlashControllerAdminSlotNumber_Type()
)
cucsStorageFlexFlashControllerAdminSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerAdminSlotNumber.setStatus("current")
_CucsStorageFlexFlashControllerConfiguredMode_Type = CucsStorageOperatingModeType
_CucsStorageFlexFlashControllerConfiguredMode_Object = MibTableColumn
cucsStorageFlexFlashControllerConfiguredMode = _CucsStorageFlexFlashControllerConfiguredMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 31),
    _CucsStorageFlexFlashControllerConfiguredMode_Type()
)
cucsStorageFlexFlashControllerConfiguredMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerConfiguredMode.setStatus("current")
_CucsStorageFlexFlashControllerFirmwareVersion_Type = SnmpAdminString
_CucsStorageFlexFlashControllerFirmwareVersion_Object = MibTableColumn
cucsStorageFlexFlashControllerFirmwareVersion = _CucsStorageFlexFlashControllerFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 32),
    _CucsStorageFlexFlashControllerFirmwareVersion_Type()
)
cucsStorageFlexFlashControllerFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFirmwareVersion.setStatus("current")
_CucsStorageFlexFlashControllerFsmDescr_Type = SnmpAdminString
_CucsStorageFlexFlashControllerFsmDescr_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmDescr = _CucsStorageFlexFlashControllerFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 33),
    _CucsStorageFlexFlashControllerFsmDescr_Type()
)
cucsStorageFlexFlashControllerFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmDescr.setStatus("current")
_CucsStorageFlexFlashControllerFsmPrev_Type = SnmpAdminString
_CucsStorageFlexFlashControllerFsmPrev_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmPrev = _CucsStorageFlexFlashControllerFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 34),
    _CucsStorageFlexFlashControllerFsmPrev_Type()
)
cucsStorageFlexFlashControllerFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmPrev.setStatus("current")
_CucsStorageFlexFlashControllerFsmProgr_Type = Gauge32
_CucsStorageFlexFlashControllerFsmProgr_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmProgr = _CucsStorageFlexFlashControllerFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 35),
    _CucsStorageFlexFlashControllerFsmProgr_Type()
)
cucsStorageFlexFlashControllerFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmProgr.setStatus("current")
_CucsStorageFlexFlashControllerFsmRmtInvErrCode_Type = Gauge32
_CucsStorageFlexFlashControllerFsmRmtInvErrCode_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmRmtInvErrCode = _CucsStorageFlexFlashControllerFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 36),
    _CucsStorageFlexFlashControllerFsmRmtInvErrCode_Type()
)
cucsStorageFlexFlashControllerFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmRmtInvErrCode.setStatus("current")
_CucsStorageFlexFlashControllerFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsStorageFlexFlashControllerFsmRmtInvErrDescr_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmRmtInvErrDescr = _CucsStorageFlexFlashControllerFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 37),
    _CucsStorageFlexFlashControllerFsmRmtInvErrDescr_Type()
)
cucsStorageFlexFlashControllerFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmRmtInvErrDescr.setStatus("current")
_CucsStorageFlexFlashControllerFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsStorageFlexFlashControllerFsmRmtInvRslt_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmRmtInvRslt = _CucsStorageFlexFlashControllerFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 38),
    _CucsStorageFlexFlashControllerFsmRmtInvRslt_Type()
)
cucsStorageFlexFlashControllerFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmRmtInvRslt.setStatus("current")
_CucsStorageFlexFlashControllerFsmStageDescr_Type = SnmpAdminString
_CucsStorageFlexFlashControllerFsmStageDescr_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmStageDescr = _CucsStorageFlexFlashControllerFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 39),
    _CucsStorageFlexFlashControllerFsmStageDescr_Type()
)
cucsStorageFlexFlashControllerFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStageDescr.setStatus("current")
_CucsStorageFlexFlashControllerFsmStamp_Type = DateAndTime
_CucsStorageFlexFlashControllerFsmStamp_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmStamp = _CucsStorageFlexFlashControllerFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 40),
    _CucsStorageFlexFlashControllerFsmStamp_Type()
)
cucsStorageFlexFlashControllerFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStamp.setStatus("current")
_CucsStorageFlexFlashControllerFsmStatus_Type = SnmpAdminString
_CucsStorageFlexFlashControllerFsmStatus_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmStatus = _CucsStorageFlexFlashControllerFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 41),
    _CucsStorageFlexFlashControllerFsmStatus_Type()
)
cucsStorageFlexFlashControllerFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStatus.setStatus("current")
_CucsStorageFlexFlashControllerFsmTry_Type = Gauge32
_CucsStorageFlexFlashControllerFsmTry_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmTry = _CucsStorageFlexFlashControllerFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 42),
    _CucsStorageFlexFlashControllerFsmTry_Type()
)
cucsStorageFlexFlashControllerFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmTry.setStatus("current")
_CucsStorageFlexFlashControllerHasError_Type = CucsStorageFFHasError
_CucsStorageFlexFlashControllerHasError_Object = MibTableColumn
cucsStorageFlexFlashControllerHasError = _CucsStorageFlexFlashControllerHasError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 43),
    _CucsStorageFlexFlashControllerHasError_Type()
)
cucsStorageFlexFlashControllerHasError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerHasError.setStatus("current")
_CucsStorageFlexFlashControllerIsCardMismatch_Type = CucsStorageFFCardSizeMismatch
_CucsStorageFlexFlashControllerIsCardMismatch_Object = MibTableColumn
cucsStorageFlexFlashControllerIsCardMismatch = _CucsStorageFlexFlashControllerIsCardMismatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 44),
    _CucsStorageFlexFlashControllerIsCardMismatch_Type()
)
cucsStorageFlexFlashControllerIsCardMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerIsCardMismatch.setStatus("current")
_CucsStorageFlexFlashControllerIsFormatFSMRunning_Type = CucsStorageFFFormatRunning
_CucsStorageFlexFlashControllerIsFormatFSMRunning_Object = MibTableColumn
cucsStorageFlexFlashControllerIsFormatFSMRunning = _CucsStorageFlexFlashControllerIsFormatFSMRunning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 45),
    _CucsStorageFlexFlashControllerIsFormatFSMRunning_Type()
)
cucsStorageFlexFlashControllerIsFormatFSMRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerIsFormatFSMRunning.setStatus("current")
_CucsStorageFlexFlashControllerOperatingMode_Type = CucsStorageOperatingModeType
_CucsStorageFlexFlashControllerOperatingMode_Object = MibTableColumn
cucsStorageFlexFlashControllerOperatingMode = _CucsStorageFlexFlashControllerOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 46),
    _CucsStorageFlexFlashControllerOperatingMode_Type()
)
cucsStorageFlexFlashControllerOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerOperatingMode.setStatus("current")
_CucsStorageFlexFlashControllerOperationRequest_Type = CucsStorageOperationRequestType
_CucsStorageFlexFlashControllerOperationRequest_Object = MibTableColumn
cucsStorageFlexFlashControllerOperationRequest = _CucsStorageFlexFlashControllerOperationRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 35, 1, 47),
    _CucsStorageFlexFlashControllerOperationRequest_Type()
)
cucsStorageFlexFlashControllerOperationRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerOperationRequest.setStatus("current")
_CucsStorageFlexFlashDriveTable_Object = MibTable
cucsStorageFlexFlashDriveTable = _CucsStorageFlexFlashDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36)
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveTable.setStatus("current")
_CucsStorageFlexFlashDriveEntry_Object = MibTableRow
cucsStorageFlexFlashDriveEntry = _CucsStorageFlexFlashDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1)
)
cucsStorageFlexFlashDriveEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageFlexFlashDriveInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveEntry.setStatus("current")
_CucsStorageFlexFlashDriveInstanceId_Type = CucsManagedObjectId
_CucsStorageFlexFlashDriveInstanceId_Object = MibTableColumn
cucsStorageFlexFlashDriveInstanceId = _CucsStorageFlexFlashDriveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 1),
    _CucsStorageFlexFlashDriveInstanceId_Type()
)
cucsStorageFlexFlashDriveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveInstanceId.setStatus("current")
_CucsStorageFlexFlashDriveDn_Type = CucsManagedObjectDn
_CucsStorageFlexFlashDriveDn_Object = MibTableColumn
cucsStorageFlexFlashDriveDn = _CucsStorageFlexFlashDriveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 2),
    _CucsStorageFlexFlashDriveDn_Type()
)
cucsStorageFlexFlashDriveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveDn.setStatus("current")
_CucsStorageFlexFlashDriveRn_Type = SnmpAdminString
_CucsStorageFlexFlashDriveRn_Object = MibTableColumn
cucsStorageFlexFlashDriveRn = _CucsStorageFlexFlashDriveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 3),
    _CucsStorageFlexFlashDriveRn_Type()
)
cucsStorageFlexFlashDriveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveRn.setStatus("current")
_CucsStorageFlexFlashDriveBlockSize_Type = Gauge32
_CucsStorageFlexFlashDriveBlockSize_Object = MibTableColumn
cucsStorageFlexFlashDriveBlockSize = _CucsStorageFlexFlashDriveBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 4),
    _CucsStorageFlexFlashDriveBlockSize_Type()
)
cucsStorageFlexFlashDriveBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveBlockSize.setStatus("current")
_CucsStorageFlexFlashDriveConnectionProtocol_Type = CucsStorageConnectionProtocol
_CucsStorageFlexFlashDriveConnectionProtocol_Object = MibTableColumn
cucsStorageFlexFlashDriveConnectionProtocol = _CucsStorageFlexFlashDriveConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 5),
    _CucsStorageFlexFlashDriveConnectionProtocol_Type()
)
cucsStorageFlexFlashDriveConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveConnectionProtocol.setStatus("current")
_CucsStorageFlexFlashDriveControllerIndex_Type = Gauge32
_CucsStorageFlexFlashDriveControllerIndex_Object = MibTableColumn
cucsStorageFlexFlashDriveControllerIndex = _CucsStorageFlexFlashDriveControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 6),
    _CucsStorageFlexFlashDriveControllerIndex_Type()
)
cucsStorageFlexFlashDriveControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveControllerIndex.setStatus("current")
_CucsStorageFlexFlashDriveDriveState_Type = CucsStorageFFDriveState
_CucsStorageFlexFlashDriveDriveState_Object = MibTableColumn
cucsStorageFlexFlashDriveDriveState = _CucsStorageFlexFlashDriveDriveState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 7),
    _CucsStorageFlexFlashDriveDriveState_Type()
)
cucsStorageFlexFlashDriveDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveDriveState.setStatus("current")
_CucsStorageFlexFlashDriveDriveType_Type = CucsStorageFFDriveType
_CucsStorageFlexFlashDriveDriveType_Object = MibTableColumn
cucsStorageFlexFlashDriveDriveType = _CucsStorageFlexFlashDriveDriveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 8),
    _CucsStorageFlexFlashDriveDriveType_Type()
)
cucsStorageFlexFlashDriveDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveDriveType.setStatus("current")
_CucsStorageFlexFlashDriveId_Type = Gauge32
_CucsStorageFlexFlashDriveId_Object = MibTableColumn
cucsStorageFlexFlashDriveId = _CucsStorageFlexFlashDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 9),
    _CucsStorageFlexFlashDriveId_Type()
)
cucsStorageFlexFlashDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveId.setStatus("current")
_CucsStorageFlexFlashDriveModel_Type = SnmpAdminString
_CucsStorageFlexFlashDriveModel_Object = MibTableColumn
cucsStorageFlexFlashDriveModel = _CucsStorageFlexFlashDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 10),
    _CucsStorageFlexFlashDriveModel_Type()
)
cucsStorageFlexFlashDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveModel.setStatus("current")
_CucsStorageFlexFlashDriveName_Type = SnmpAdminString
_CucsStorageFlexFlashDriveName_Object = MibTableColumn
cucsStorageFlexFlashDriveName = _CucsStorageFlexFlashDriveName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 11),
    _CucsStorageFlexFlashDriveName_Type()
)
cucsStorageFlexFlashDriveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveName.setStatus("current")
_CucsStorageFlexFlashDriveNumberOfBlocks_Type = Unsigned64
_CucsStorageFlexFlashDriveNumberOfBlocks_Object = MibTableColumn
cucsStorageFlexFlashDriveNumberOfBlocks = _CucsStorageFlexFlashDriveNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 12),
    _CucsStorageFlexFlashDriveNumberOfBlocks_Type()
)
cucsStorageFlexFlashDriveNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveNumberOfBlocks.setStatus("current")
_CucsStorageFlexFlashDriveOperQualifierReason_Type = SnmpAdminString
_CucsStorageFlexFlashDriveOperQualifierReason_Object = MibTableColumn
cucsStorageFlexFlashDriveOperQualifierReason = _CucsStorageFlexFlashDriveOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 13),
    _CucsStorageFlexFlashDriveOperQualifierReason_Type()
)
cucsStorageFlexFlashDriveOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveOperQualifierReason.setStatus("current")
_CucsStorageFlexFlashDriveOperability_Type = CucsEquipmentOperability
_CucsStorageFlexFlashDriveOperability_Object = MibTableColumn
cucsStorageFlexFlashDriveOperability = _CucsStorageFlexFlashDriveOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 14),
    _CucsStorageFlexFlashDriveOperability_Type()
)
cucsStorageFlexFlashDriveOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveOperability.setStatus("current")
_CucsStorageFlexFlashDrivePresence_Type = CucsEquipmentPresence
_CucsStorageFlexFlashDrivePresence_Object = MibTableColumn
cucsStorageFlexFlashDrivePresence = _CucsStorageFlexFlashDrivePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 15),
    _CucsStorageFlexFlashDrivePresence_Type()
)
cucsStorageFlexFlashDrivePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDrivePresence.setStatus("current")
_CucsStorageFlexFlashDriveRevision_Type = SnmpAdminString
_CucsStorageFlexFlashDriveRevision_Object = MibTableColumn
cucsStorageFlexFlashDriveRevision = _CucsStorageFlexFlashDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 16),
    _CucsStorageFlexFlashDriveRevision_Type()
)
cucsStorageFlexFlashDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveRevision.setStatus("current")
_CucsStorageFlexFlashDriveSerial_Type = SnmpAdminString
_CucsStorageFlexFlashDriveSerial_Object = MibTableColumn
cucsStorageFlexFlashDriveSerial = _CucsStorageFlexFlashDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 17),
    _CucsStorageFlexFlashDriveSerial_Type()
)
cucsStorageFlexFlashDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveSerial.setStatus("current")
_CucsStorageFlexFlashDriveSize_Type = Unsigned64
_CucsStorageFlexFlashDriveSize_Object = MibTableColumn
cucsStorageFlexFlashDriveSize = _CucsStorageFlexFlashDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 18),
    _CucsStorageFlexFlashDriveSize_Type()
)
cucsStorageFlexFlashDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveSize.setStatus("current")
_CucsStorageFlexFlashDriveSlotNumber_Type = Gauge32
_CucsStorageFlexFlashDriveSlotNumber_Object = MibTableColumn
cucsStorageFlexFlashDriveSlotNumber = _CucsStorageFlexFlashDriveSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 19),
    _CucsStorageFlexFlashDriveSlotNumber_Type()
)
cucsStorageFlexFlashDriveSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveSlotNumber.setStatus("current")
_CucsStorageFlexFlashDriveVendor_Type = SnmpAdminString
_CucsStorageFlexFlashDriveVendor_Object = MibTableColumn
cucsStorageFlexFlashDriveVendor = _CucsStorageFlexFlashDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 20),
    _CucsStorageFlexFlashDriveVendor_Type()
)
cucsStorageFlexFlashDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveVendor.setStatus("current")
_CucsStorageFlexFlashDriveVisible_Type = CucsStorageFFDriveVisible
_CucsStorageFlexFlashDriveVisible_Object = MibTableColumn
cucsStorageFlexFlashDriveVisible = _CucsStorageFlexFlashDriveVisible_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 21),
    _CucsStorageFlexFlashDriveVisible_Type()
)
cucsStorageFlexFlashDriveVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveVisible.setStatus("current")
_CucsStorageFlexFlashDriveRemovable_Type = CucsStorageFFDriveRemovable
_CucsStorageFlexFlashDriveRemovable_Object = MibTableColumn
cucsStorageFlexFlashDriveRemovable = _CucsStorageFlexFlashDriveRemovable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 22),
    _CucsStorageFlexFlashDriveRemovable_Type()
)
cucsStorageFlexFlashDriveRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveRemovable.setStatus("current")
_CucsStorageFlexFlashDriveRWType_Type = CucsStorageFFRWType
_CucsStorageFlexFlashDriveRWType_Object = MibTableColumn
cucsStorageFlexFlashDriveRWType = _CucsStorageFlexFlashDriveRWType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 23),
    _CucsStorageFlexFlashDriveRWType_Type()
)
cucsStorageFlexFlashDriveRWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveRWType.setStatus("current")
_CucsStorageFlexFlashDriveLastOperation_Type = CucsStorageOperationStateType
_CucsStorageFlexFlashDriveLastOperation_Object = MibTableColumn
cucsStorageFlexFlashDriveLastOperation = _CucsStorageFlexFlashDriveLastOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 24),
    _CucsStorageFlexFlashDriveLastOperation_Type()
)
cucsStorageFlexFlashDriveLastOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveLastOperation.setStatus("current")
_CucsStorageFlexFlashDriveOperationState_Type = CucsStorageOperationStateType
_CucsStorageFlexFlashDriveOperationState_Object = MibTableColumn
cucsStorageFlexFlashDriveOperationState = _CucsStorageFlexFlashDriveOperationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 36, 1, 25),
    _CucsStorageFlexFlashDriveOperationState_Type()
)
cucsStorageFlexFlashDriveOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashDriveOperationState.setStatus("current")
_CucsStorageFlexFlashVirtualDriveTable_Object = MibTable
cucsStorageFlexFlashVirtualDriveTable = _CucsStorageFlexFlashVirtualDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37)
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveTable.setStatus("current")
_CucsStorageFlexFlashVirtualDriveEntry_Object = MibTableRow
cucsStorageFlexFlashVirtualDriveEntry = _CucsStorageFlexFlashVirtualDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1)
)
cucsStorageFlexFlashVirtualDriveEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageFlexFlashVirtualDriveInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveEntry.setStatus("current")
_CucsStorageFlexFlashVirtualDriveInstanceId_Type = CucsManagedObjectId
_CucsStorageFlexFlashVirtualDriveInstanceId_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveInstanceId = _CucsStorageFlexFlashVirtualDriveInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 1),
    _CucsStorageFlexFlashVirtualDriveInstanceId_Type()
)
cucsStorageFlexFlashVirtualDriveInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveInstanceId.setStatus("current")
_CucsStorageFlexFlashVirtualDriveDn_Type = CucsManagedObjectDn
_CucsStorageFlexFlashVirtualDriveDn_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveDn = _CucsStorageFlexFlashVirtualDriveDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 2),
    _CucsStorageFlexFlashVirtualDriveDn_Type()
)
cucsStorageFlexFlashVirtualDriveDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveDn.setStatus("current")
_CucsStorageFlexFlashVirtualDriveRn_Type = SnmpAdminString
_CucsStorageFlexFlashVirtualDriveRn_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveRn = _CucsStorageFlexFlashVirtualDriveRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 3),
    _CucsStorageFlexFlashVirtualDriveRn_Type()
)
cucsStorageFlexFlashVirtualDriveRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveRn.setStatus("current")
_CucsStorageFlexFlashVirtualDriveBlockSize_Type = Gauge32
_CucsStorageFlexFlashVirtualDriveBlockSize_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveBlockSize = _CucsStorageFlexFlashVirtualDriveBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 4),
    _CucsStorageFlexFlashVirtualDriveBlockSize_Type()
)
cucsStorageFlexFlashVirtualDriveBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveBlockSize.setStatus("current")
_CucsStorageFlexFlashVirtualDriveConnectionProtocol_Type = CucsStorageConnectionProtocol
_CucsStorageFlexFlashVirtualDriveConnectionProtocol_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveConnectionProtocol = _CucsStorageFlexFlashVirtualDriveConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 5),
    _CucsStorageFlexFlashVirtualDriveConnectionProtocol_Type()
)
cucsStorageFlexFlashVirtualDriveConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveConnectionProtocol.setStatus("current")
_CucsStorageFlexFlashVirtualDriveId_Type = Gauge32
_CucsStorageFlexFlashVirtualDriveId_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveId = _CucsStorageFlexFlashVirtualDriveId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 6),
    _CucsStorageFlexFlashVirtualDriveId_Type()
)
cucsStorageFlexFlashVirtualDriveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveId.setStatus("current")
_CucsStorageFlexFlashVirtualDriveModel_Type = SnmpAdminString
_CucsStorageFlexFlashVirtualDriveModel_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveModel = _CucsStorageFlexFlashVirtualDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 7),
    _CucsStorageFlexFlashVirtualDriveModel_Type()
)
cucsStorageFlexFlashVirtualDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveModel.setStatus("current")
_CucsStorageFlexFlashVirtualDriveNumberOfBlocks_Type = Unsigned64
_CucsStorageFlexFlashVirtualDriveNumberOfBlocks_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveNumberOfBlocks = _CucsStorageFlexFlashVirtualDriveNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 8),
    _CucsStorageFlexFlashVirtualDriveNumberOfBlocks_Type()
)
cucsStorageFlexFlashVirtualDriveNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveNumberOfBlocks.setStatus("current")
_CucsStorageFlexFlashVirtualDriveOperQualifierReason_Type = SnmpAdminString
_CucsStorageFlexFlashVirtualDriveOperQualifierReason_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveOperQualifierReason = _CucsStorageFlexFlashVirtualDriveOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 9),
    _CucsStorageFlexFlashVirtualDriveOperQualifierReason_Type()
)
cucsStorageFlexFlashVirtualDriveOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveOperQualifierReason.setStatus("current")
_CucsStorageFlexFlashVirtualDriveOperability_Type = CucsEquipmentOperability
_CucsStorageFlexFlashVirtualDriveOperability_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveOperability = _CucsStorageFlexFlashVirtualDriveOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 10),
    _CucsStorageFlexFlashVirtualDriveOperability_Type()
)
cucsStorageFlexFlashVirtualDriveOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveOperability.setStatus("current")
_CucsStorageFlexFlashVirtualDrivePresence_Type = CucsEquipmentPresence
_CucsStorageFlexFlashVirtualDrivePresence_Object = MibTableColumn
cucsStorageFlexFlashVirtualDrivePresence = _CucsStorageFlexFlashVirtualDrivePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 11),
    _CucsStorageFlexFlashVirtualDrivePresence_Type()
)
cucsStorageFlexFlashVirtualDrivePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDrivePresence.setStatus("current")
_CucsStorageFlexFlashVirtualDriveRaidHealth_Type = CucsStorageFFRAIDHealth
_CucsStorageFlexFlashVirtualDriveRaidHealth_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveRaidHealth = _CucsStorageFlexFlashVirtualDriveRaidHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 12),
    _CucsStorageFlexFlashVirtualDriveRaidHealth_Type()
)
cucsStorageFlexFlashVirtualDriveRaidHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveRaidHealth.setStatus("current")
_CucsStorageFlexFlashVirtualDriveRaidState_Type = CucsStorageFFRAIDState
_CucsStorageFlexFlashVirtualDriveRaidState_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveRaidState = _CucsStorageFlexFlashVirtualDriveRaidState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 13),
    _CucsStorageFlexFlashVirtualDriveRaidState_Type()
)
cucsStorageFlexFlashVirtualDriveRaidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveRaidState.setStatus("current")
_CucsStorageFlexFlashVirtualDriveRevision_Type = SnmpAdminString
_CucsStorageFlexFlashVirtualDriveRevision_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveRevision = _CucsStorageFlexFlashVirtualDriveRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 14),
    _CucsStorageFlexFlashVirtualDriveRevision_Type()
)
cucsStorageFlexFlashVirtualDriveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveRevision.setStatus("current")
_CucsStorageFlexFlashVirtualDriveSerial_Type = SnmpAdminString
_CucsStorageFlexFlashVirtualDriveSerial_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveSerial = _CucsStorageFlexFlashVirtualDriveSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 15),
    _CucsStorageFlexFlashVirtualDriveSerial_Type()
)
cucsStorageFlexFlashVirtualDriveSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveSerial.setStatus("current")
_CucsStorageFlexFlashVirtualDriveSize_Type = Unsigned64
_CucsStorageFlexFlashVirtualDriveSize_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveSize = _CucsStorageFlexFlashVirtualDriveSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 16),
    _CucsStorageFlexFlashVirtualDriveSize_Type()
)
cucsStorageFlexFlashVirtualDriveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveSize.setStatus("current")
_CucsStorageFlexFlashVirtualDriveType_Type = CucsStorageLunType
_CucsStorageFlexFlashVirtualDriveType_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveType = _CucsStorageFlexFlashVirtualDriveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 17),
    _CucsStorageFlexFlashVirtualDriveType_Type()
)
cucsStorageFlexFlashVirtualDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveType.setStatus("current")
_CucsStorageFlexFlashVirtualDriveVendor_Type = SnmpAdminString
_CucsStorageFlexFlashVirtualDriveVendor_Object = MibTableColumn
cucsStorageFlexFlashVirtualDriveVendor = _CucsStorageFlexFlashVirtualDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 37, 1, 18),
    _CucsStorageFlexFlashVirtualDriveVendor_Type()
)
cucsStorageFlexFlashVirtualDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashVirtualDriveVendor.setStatus("current")
_CucsStorageOperationTable_Object = MibTable
cucsStorageOperationTable = _CucsStorageOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 38)
)
if mibBuilder.loadTexts:
    cucsStorageOperationTable.setStatus("current")
_CucsStorageOperationEntry_Object = MibTableRow
cucsStorageOperationEntry = _CucsStorageOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 38, 1)
)
cucsStorageOperationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageOperationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageOperationEntry.setStatus("current")
_CucsStorageOperationInstanceId_Type = CucsManagedObjectId
_CucsStorageOperationInstanceId_Object = MibTableColumn
cucsStorageOperationInstanceId = _CucsStorageOperationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 38, 1, 1),
    _CucsStorageOperationInstanceId_Type()
)
cucsStorageOperationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageOperationInstanceId.setStatus("current")
_CucsStorageOperationDn_Type = CucsManagedObjectDn
_CucsStorageOperationDn_Object = MibTableColumn
cucsStorageOperationDn = _CucsStorageOperationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 38, 1, 2),
    _CucsStorageOperationDn_Type()
)
cucsStorageOperationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageOperationDn.setStatus("current")
_CucsStorageOperationRn_Type = SnmpAdminString
_CucsStorageOperationRn_Object = MibTableColumn
cucsStorageOperationRn = _CucsStorageOperationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 38, 1, 3),
    _CucsStorageOperationRn_Type()
)
cucsStorageOperationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageOperationRn.setStatus("current")
_CucsStorageOperationEndTime_Type = DateAndTime
_CucsStorageOperationEndTime_Object = MibTableColumn
cucsStorageOperationEndTime = _CucsStorageOperationEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 38, 1, 4),
    _CucsStorageOperationEndTime_Type()
)
cucsStorageOperationEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageOperationEndTime.setStatus("current")
_CucsStorageOperationName_Type = CucsStorageOperationType
_CucsStorageOperationName_Object = MibTableColumn
cucsStorageOperationName = _CucsStorageOperationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 38, 1, 5),
    _CucsStorageOperationName_Type()
)
cucsStorageOperationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageOperationName.setStatus("current")
_CucsStorageOperationOperState_Type = CucsStorageOperationState
_CucsStorageOperationOperState_Object = MibTableColumn
cucsStorageOperationOperState = _CucsStorageOperationOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 38, 1, 6),
    _CucsStorageOperationOperState_Type()
)
cucsStorageOperationOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageOperationOperState.setStatus("current")
_CucsStorageOperationProgress_Type = Gauge32
_CucsStorageOperationProgress_Object = MibTableColumn
cucsStorageOperationProgress = _CucsStorageOperationProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 38, 1, 7),
    _CucsStorageOperationProgress_Type()
)
cucsStorageOperationProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageOperationProgress.setStatus("current")
_CucsStorageOperationStartTime_Type = DateAndTime
_CucsStorageOperationStartTime_Object = MibTableColumn
cucsStorageOperationStartTime = _CucsStorageOperationStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 38, 1, 8),
    _CucsStorageOperationStartTime_Type()
)
cucsStorageOperationStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageOperationStartTime.setStatus("current")
_CucsStorageOperationStatusDescr_Type = SnmpAdminString
_CucsStorageOperationStatusDescr_Object = MibTableColumn
cucsStorageOperationStatusDescr = _CucsStorageOperationStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 38, 1, 9),
    _CucsStorageOperationStatusDescr_Type()
)
cucsStorageOperationStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageOperationStatusDescr.setStatus("current")
_CucsStorageMezzFlashLifeTable_Object = MibTable
cucsStorageMezzFlashLifeTable = _CucsStorageMezzFlashLifeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39)
)
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeTable.setStatus("current")
_CucsStorageMezzFlashLifeEntry_Object = MibTableRow
cucsStorageMezzFlashLifeEntry = _CucsStorageMezzFlashLifeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1)
)
cucsStorageMezzFlashLifeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageMezzFlashLifeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeEntry.setStatus("current")
_CucsStorageMezzFlashLifeInstanceId_Type = CucsManagedObjectId
_CucsStorageMezzFlashLifeInstanceId_Object = MibTableColumn
cucsStorageMezzFlashLifeInstanceId = _CucsStorageMezzFlashLifeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 1),
    _CucsStorageMezzFlashLifeInstanceId_Type()
)
cucsStorageMezzFlashLifeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeInstanceId.setStatus("current")
_CucsStorageMezzFlashLifeDn_Type = CucsManagedObjectDn
_CucsStorageMezzFlashLifeDn_Object = MibTableColumn
cucsStorageMezzFlashLifeDn = _CucsStorageMezzFlashLifeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 2),
    _CucsStorageMezzFlashLifeDn_Type()
)
cucsStorageMezzFlashLifeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeDn.setStatus("current")
_CucsStorageMezzFlashLifeRn_Type = SnmpAdminString
_CucsStorageMezzFlashLifeRn_Object = MibTableColumn
cucsStorageMezzFlashLifeRn = _CucsStorageMezzFlashLifeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 3),
    _CucsStorageMezzFlashLifeRn_Type()
)
cucsStorageMezzFlashLifeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeRn.setStatus("current")
_CucsStorageMezzFlashLifeBlockSize_Type = Gauge32
_CucsStorageMezzFlashLifeBlockSize_Object = MibTableColumn
cucsStorageMezzFlashLifeBlockSize = _CucsStorageMezzFlashLifeBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 4),
    _CucsStorageMezzFlashLifeBlockSize_Type()
)
cucsStorageMezzFlashLifeBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeBlockSize.setStatus("current")
_CucsStorageMezzFlashLifeConnectionProtocol_Type = CucsStorageConnectionProtocol
_CucsStorageMezzFlashLifeConnectionProtocol_Object = MibTableColumn
cucsStorageMezzFlashLifeConnectionProtocol = _CucsStorageMezzFlashLifeConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 5),
    _CucsStorageMezzFlashLifeConnectionProtocol_Type()
)
cucsStorageMezzFlashLifeConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeConnectionProtocol.setStatus("current")
_CucsStorageMezzFlashLifeFlashPercentage_Type = SnmpAdminString
_CucsStorageMezzFlashLifeFlashPercentage_Object = MibTableColumn
cucsStorageMezzFlashLifeFlashPercentage = _CucsStorageMezzFlashLifeFlashPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 6),
    _CucsStorageMezzFlashLifeFlashPercentage_Type()
)
cucsStorageMezzFlashLifeFlashPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeFlashPercentage.setStatus("current")
_CucsStorageMezzFlashLifeFlashStatus_Type = SnmpAdminString
_CucsStorageMezzFlashLifeFlashStatus_Object = MibTableColumn
cucsStorageMezzFlashLifeFlashStatus = _CucsStorageMezzFlashLifeFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 7),
    _CucsStorageMezzFlashLifeFlashStatus_Type()
)
cucsStorageMezzFlashLifeFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeFlashStatus.setStatus("current")
_CucsStorageMezzFlashLifeId_Type = Gauge32
_CucsStorageMezzFlashLifeId_Object = MibTableColumn
cucsStorageMezzFlashLifeId = _CucsStorageMezzFlashLifeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 8),
    _CucsStorageMezzFlashLifeId_Type()
)
cucsStorageMezzFlashLifeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeId.setStatus("current")
_CucsStorageMezzFlashLifeModel_Type = SnmpAdminString
_CucsStorageMezzFlashLifeModel_Object = MibTableColumn
cucsStorageMezzFlashLifeModel = _CucsStorageMezzFlashLifeModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 9),
    _CucsStorageMezzFlashLifeModel_Type()
)
cucsStorageMezzFlashLifeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeModel.setStatus("current")
_CucsStorageMezzFlashLifeNumberOfBlocks_Type = Unsigned64
_CucsStorageMezzFlashLifeNumberOfBlocks_Object = MibTableColumn
cucsStorageMezzFlashLifeNumberOfBlocks = _CucsStorageMezzFlashLifeNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 10),
    _CucsStorageMezzFlashLifeNumberOfBlocks_Type()
)
cucsStorageMezzFlashLifeNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeNumberOfBlocks.setStatus("current")
_CucsStorageMezzFlashLifeOperQualifierReason_Type = SnmpAdminString
_CucsStorageMezzFlashLifeOperQualifierReason_Object = MibTableColumn
cucsStorageMezzFlashLifeOperQualifierReason = _CucsStorageMezzFlashLifeOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 11),
    _CucsStorageMezzFlashLifeOperQualifierReason_Type()
)
cucsStorageMezzFlashLifeOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeOperQualifierReason.setStatus("current")
_CucsStorageMezzFlashLifeOperability_Type = CucsEquipmentOperability
_CucsStorageMezzFlashLifeOperability_Object = MibTableColumn
cucsStorageMezzFlashLifeOperability = _CucsStorageMezzFlashLifeOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 12),
    _CucsStorageMezzFlashLifeOperability_Type()
)
cucsStorageMezzFlashLifeOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeOperability.setStatus("current")
_CucsStorageMezzFlashLifePresence_Type = CucsEquipmentPresence
_CucsStorageMezzFlashLifePresence_Object = MibTableColumn
cucsStorageMezzFlashLifePresence = _CucsStorageMezzFlashLifePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 13),
    _CucsStorageMezzFlashLifePresence_Type()
)
cucsStorageMezzFlashLifePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifePresence.setStatus("current")
_CucsStorageMezzFlashLifeRevision_Type = SnmpAdminString
_CucsStorageMezzFlashLifeRevision_Object = MibTableColumn
cucsStorageMezzFlashLifeRevision = _CucsStorageMezzFlashLifeRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 14),
    _CucsStorageMezzFlashLifeRevision_Type()
)
cucsStorageMezzFlashLifeRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeRevision.setStatus("current")
_CucsStorageMezzFlashLifeSerial_Type = SnmpAdminString
_CucsStorageMezzFlashLifeSerial_Object = MibTableColumn
cucsStorageMezzFlashLifeSerial = _CucsStorageMezzFlashLifeSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 15),
    _CucsStorageMezzFlashLifeSerial_Type()
)
cucsStorageMezzFlashLifeSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeSerial.setStatus("current")
_CucsStorageMezzFlashLifeSize_Type = Unsigned64
_CucsStorageMezzFlashLifeSize_Object = MibTableColumn
cucsStorageMezzFlashLifeSize = _CucsStorageMezzFlashLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 16),
    _CucsStorageMezzFlashLifeSize_Type()
)
cucsStorageMezzFlashLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeSize.setStatus("current")
_CucsStorageMezzFlashLifeVendor_Type = SnmpAdminString
_CucsStorageMezzFlashLifeVendor_Object = MibTableColumn
cucsStorageMezzFlashLifeVendor = _CucsStorageMezzFlashLifeVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 39, 1, 17),
    _CucsStorageMezzFlashLifeVendor_Type()
)
cucsStorageMezzFlashLifeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageMezzFlashLifeVendor.setStatus("current")
_CucsStorageFlexFlashControllerFsmTable_Object = MibTable
cucsStorageFlexFlashControllerFsmTable = _CucsStorageFlexFlashControllerFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40)
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmTable.setStatus("current")
_CucsStorageFlexFlashControllerFsmEntry_Object = MibTableRow
cucsStorageFlexFlashControllerFsmEntry = _CucsStorageFlexFlashControllerFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40, 1)
)
cucsStorageFlexFlashControllerFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageFlexFlashControllerFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmEntry.setStatus("current")
_CucsStorageFlexFlashControllerFsmInstanceId_Type = CucsManagedObjectId
_CucsStorageFlexFlashControllerFsmInstanceId_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmInstanceId = _CucsStorageFlexFlashControllerFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40, 1, 1),
    _CucsStorageFlexFlashControllerFsmInstanceId_Type()
)
cucsStorageFlexFlashControllerFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmInstanceId.setStatus("current")
_CucsStorageFlexFlashControllerFsmDn_Type = CucsManagedObjectDn
_CucsStorageFlexFlashControllerFsmDn_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmDn = _CucsStorageFlexFlashControllerFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40, 1, 2),
    _CucsStorageFlexFlashControllerFsmDn_Type()
)
cucsStorageFlexFlashControllerFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmDn.setStatus("current")
_CucsStorageFlexFlashControllerFsmRn_Type = SnmpAdminString
_CucsStorageFlexFlashControllerFsmRn_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmRn = _CucsStorageFlexFlashControllerFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40, 1, 3),
    _CucsStorageFlexFlashControllerFsmRn_Type()
)
cucsStorageFlexFlashControllerFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmRn.setStatus("current")
_CucsStorageFlexFlashControllerFsmCompletionTime_Type = DateAndTime
_CucsStorageFlexFlashControllerFsmCompletionTime_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmCompletionTime = _CucsStorageFlexFlashControllerFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40, 1, 4),
    _CucsStorageFlexFlashControllerFsmCompletionTime_Type()
)
cucsStorageFlexFlashControllerFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmCompletionTime.setStatus("current")
_CucsStorageFlexFlashControllerFsmCurrentFsm_Type = CucsStorageFlexFlashControllerFsmCurrentFsm
_CucsStorageFlexFlashControllerFsmCurrentFsm_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmCurrentFsm = _CucsStorageFlexFlashControllerFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40, 1, 5),
    _CucsStorageFlexFlashControllerFsmCurrentFsm_Type()
)
cucsStorageFlexFlashControllerFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmCurrentFsm.setStatus("current")
_CucsStorageFlexFlashControllerFsmDescrData_Type = SnmpAdminString
_CucsStorageFlexFlashControllerFsmDescrData_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmDescrData = _CucsStorageFlexFlashControllerFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40, 1, 6),
    _CucsStorageFlexFlashControllerFsmDescrData_Type()
)
cucsStorageFlexFlashControllerFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmDescrData.setStatus("current")
_CucsStorageFlexFlashControllerFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsStorageFlexFlashControllerFsmFsmStatus_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmFsmStatus = _CucsStorageFlexFlashControllerFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40, 1, 7),
    _CucsStorageFlexFlashControllerFsmFsmStatus_Type()
)
cucsStorageFlexFlashControllerFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmFsmStatus.setStatus("current")
_CucsStorageFlexFlashControllerFsmProgress_Type = Gauge32
_CucsStorageFlexFlashControllerFsmProgress_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmProgress = _CucsStorageFlexFlashControllerFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40, 1, 8),
    _CucsStorageFlexFlashControllerFsmProgress_Type()
)
cucsStorageFlexFlashControllerFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmProgress.setStatus("current")
_CucsStorageFlexFlashControllerFsmRmtErrCode_Type = Gauge32
_CucsStorageFlexFlashControllerFsmRmtErrCode_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmRmtErrCode = _CucsStorageFlexFlashControllerFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40, 1, 9),
    _CucsStorageFlexFlashControllerFsmRmtErrCode_Type()
)
cucsStorageFlexFlashControllerFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmRmtErrCode.setStatus("current")
_CucsStorageFlexFlashControllerFsmRmtErrDescr_Type = SnmpAdminString
_CucsStorageFlexFlashControllerFsmRmtErrDescr_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmRmtErrDescr = _CucsStorageFlexFlashControllerFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40, 1, 10),
    _CucsStorageFlexFlashControllerFsmRmtErrDescr_Type()
)
cucsStorageFlexFlashControllerFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmRmtErrDescr.setStatus("current")
_CucsStorageFlexFlashControllerFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsStorageFlexFlashControllerFsmRmtRslt_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmRmtRslt = _CucsStorageFlexFlashControllerFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 40, 1, 11),
    _CucsStorageFlexFlashControllerFsmRmtRslt_Type()
)
cucsStorageFlexFlashControllerFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmRmtRslt.setStatus("current")
_CucsStorageFlexFlashControllerFsmStageTable_Object = MibTable
cucsStorageFlexFlashControllerFsmStageTable = _CucsStorageFlexFlashControllerFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 41)
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStageTable.setStatus("current")
_CucsStorageFlexFlashControllerFsmStageEntry_Object = MibTableRow
cucsStorageFlexFlashControllerFsmStageEntry = _CucsStorageFlexFlashControllerFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 41, 1)
)
cucsStorageFlexFlashControllerFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageFlexFlashControllerFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStageEntry.setStatus("current")
_CucsStorageFlexFlashControllerFsmStageInstanceId_Type = CucsManagedObjectId
_CucsStorageFlexFlashControllerFsmStageInstanceId_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmStageInstanceId = _CucsStorageFlexFlashControllerFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 41, 1, 1),
    _CucsStorageFlexFlashControllerFsmStageInstanceId_Type()
)
cucsStorageFlexFlashControllerFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStageInstanceId.setStatus("current")
_CucsStorageFlexFlashControllerFsmStageDn_Type = CucsManagedObjectDn
_CucsStorageFlexFlashControllerFsmStageDn_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmStageDn = _CucsStorageFlexFlashControllerFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 41, 1, 2),
    _CucsStorageFlexFlashControllerFsmStageDn_Type()
)
cucsStorageFlexFlashControllerFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStageDn.setStatus("current")
_CucsStorageFlexFlashControllerFsmStageRn_Type = SnmpAdminString
_CucsStorageFlexFlashControllerFsmStageRn_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmStageRn = _CucsStorageFlexFlashControllerFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 41, 1, 3),
    _CucsStorageFlexFlashControllerFsmStageRn_Type()
)
cucsStorageFlexFlashControllerFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStageRn.setStatus("current")
_CucsStorageFlexFlashControllerFsmStageDescrData_Type = SnmpAdminString
_CucsStorageFlexFlashControllerFsmStageDescrData_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmStageDescrData = _CucsStorageFlexFlashControllerFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 41, 1, 4),
    _CucsStorageFlexFlashControllerFsmStageDescrData_Type()
)
cucsStorageFlexFlashControllerFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStageDescrData.setStatus("current")
_CucsStorageFlexFlashControllerFsmStageLastUpdateTime_Type = DateAndTime
_CucsStorageFlexFlashControllerFsmStageLastUpdateTime_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmStageLastUpdateTime = _CucsStorageFlexFlashControllerFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 41, 1, 5),
    _CucsStorageFlexFlashControllerFsmStageLastUpdateTime_Type()
)
cucsStorageFlexFlashControllerFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStageLastUpdateTime.setStatus("current")
_CucsStorageFlexFlashControllerFsmStageName_Type = CucsStorageFlexFlashControllerFsmStageName
_CucsStorageFlexFlashControllerFsmStageName_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmStageName = _CucsStorageFlexFlashControllerFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 41, 1, 6),
    _CucsStorageFlexFlashControllerFsmStageName_Type()
)
cucsStorageFlexFlashControllerFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStageName.setStatus("current")
_CucsStorageFlexFlashControllerFsmStageOrder_Type = Gauge32
_CucsStorageFlexFlashControllerFsmStageOrder_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmStageOrder = _CucsStorageFlexFlashControllerFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 41, 1, 7),
    _CucsStorageFlexFlashControllerFsmStageOrder_Type()
)
cucsStorageFlexFlashControllerFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStageOrder.setStatus("current")
_CucsStorageFlexFlashControllerFsmStageRetry_Type = Gauge32
_CucsStorageFlexFlashControllerFsmStageRetry_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmStageRetry = _CucsStorageFlexFlashControllerFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 41, 1, 8),
    _CucsStorageFlexFlashControllerFsmStageRetry_Type()
)
cucsStorageFlexFlashControllerFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStageRetry.setStatus("current")
_CucsStorageFlexFlashControllerFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsStorageFlexFlashControllerFsmStageStageStatus_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmStageStageStatus = _CucsStorageFlexFlashControllerFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 41, 1, 9),
    _CucsStorageFlexFlashControllerFsmStageStageStatus_Type()
)
cucsStorageFlexFlashControllerFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmStageStageStatus.setStatus("current")
_CucsStorageFlexFlashControllerFsmTaskTable_Object = MibTable
cucsStorageFlexFlashControllerFsmTaskTable = _CucsStorageFlexFlashControllerFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 42)
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmTaskTable.setStatus("current")
_CucsStorageFlexFlashControllerFsmTaskEntry_Object = MibTableRow
cucsStorageFlexFlashControllerFsmTaskEntry = _CucsStorageFlexFlashControllerFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 42, 1)
)
cucsStorageFlexFlashControllerFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageFlexFlashControllerFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmTaskEntry.setStatus("current")
_CucsStorageFlexFlashControllerFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsStorageFlexFlashControllerFsmTaskInstanceId_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmTaskInstanceId = _CucsStorageFlexFlashControllerFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 42, 1, 1),
    _CucsStorageFlexFlashControllerFsmTaskInstanceId_Type()
)
cucsStorageFlexFlashControllerFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmTaskInstanceId.setStatus("current")
_CucsStorageFlexFlashControllerFsmTaskDn_Type = CucsManagedObjectDn
_CucsStorageFlexFlashControllerFsmTaskDn_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmTaskDn = _CucsStorageFlexFlashControllerFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 42, 1, 2),
    _CucsStorageFlexFlashControllerFsmTaskDn_Type()
)
cucsStorageFlexFlashControllerFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmTaskDn.setStatus("current")
_CucsStorageFlexFlashControllerFsmTaskRn_Type = SnmpAdminString
_CucsStorageFlexFlashControllerFsmTaskRn_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmTaskRn = _CucsStorageFlexFlashControllerFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 42, 1, 3),
    _CucsStorageFlexFlashControllerFsmTaskRn_Type()
)
cucsStorageFlexFlashControllerFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmTaskRn.setStatus("current")
_CucsStorageFlexFlashControllerFsmTaskCompletion_Type = CucsFsmCompletion
_CucsStorageFlexFlashControllerFsmTaskCompletion_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmTaskCompletion = _CucsStorageFlexFlashControllerFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 42, 1, 4),
    _CucsStorageFlexFlashControllerFsmTaskCompletion_Type()
)
cucsStorageFlexFlashControllerFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmTaskCompletion.setStatus("current")
_CucsStorageFlexFlashControllerFsmTaskFlags_Type = CucsFsmFlags
_CucsStorageFlexFlashControllerFsmTaskFlags_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmTaskFlags = _CucsStorageFlexFlashControllerFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 42, 1, 5),
    _CucsStorageFlexFlashControllerFsmTaskFlags_Type()
)
cucsStorageFlexFlashControllerFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmTaskFlags.setStatus("current")
_CucsStorageFlexFlashControllerFsmTaskItem_Type = CucsStorageFlexFlashControllerFsmTaskItem
_CucsStorageFlexFlashControllerFsmTaskItem_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmTaskItem = _CucsStorageFlexFlashControllerFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 42, 1, 6),
    _CucsStorageFlexFlashControllerFsmTaskItem_Type()
)
cucsStorageFlexFlashControllerFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmTaskItem.setStatus("current")
_CucsStorageFlexFlashControllerFsmTaskSeqId_Type = Gauge32
_CucsStorageFlexFlashControllerFsmTaskSeqId_Object = MibTableColumn
cucsStorageFlexFlashControllerFsmTaskSeqId = _CucsStorageFlexFlashControllerFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 42, 1, 7),
    _CucsStorageFlexFlashControllerFsmTaskSeqId_Type()
)
cucsStorageFlexFlashControllerFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageFlexFlashControllerFsmTaskSeqId.setStatus("current")
_CucsStorageDiskEnvStatsTable_Object = MibTable
cucsStorageDiskEnvStatsTable = _CucsStorageDiskEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50)
)
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsTable.setStatus("current")
_CucsStorageDiskEnvStatsEntry_Object = MibTableRow
cucsStorageDiskEnvStatsEntry = _CucsStorageDiskEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1)
)
cucsStorageDiskEnvStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageDiskEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsEntry.setStatus("current")
_CucsStorageDiskEnvStatsInstanceId_Type = CucsManagedObjectId
_CucsStorageDiskEnvStatsInstanceId_Object = MibTableColumn
cucsStorageDiskEnvStatsInstanceId = _CucsStorageDiskEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 1),
    _CucsStorageDiskEnvStatsInstanceId_Type()
)
cucsStorageDiskEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsInstanceId.setStatus("current")
_CucsStorageDiskEnvStatsDn_Type = CucsManagedObjectDn
_CucsStorageDiskEnvStatsDn_Object = MibTableColumn
cucsStorageDiskEnvStatsDn = _CucsStorageDiskEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 2),
    _CucsStorageDiskEnvStatsDn_Type()
)
cucsStorageDiskEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsDn.setStatus("current")
_CucsStorageDiskEnvStatsRn_Type = SnmpAdminString
_CucsStorageDiskEnvStatsRn_Object = MibTableColumn
cucsStorageDiskEnvStatsRn = _CucsStorageDiskEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 3),
    _CucsStorageDiskEnvStatsRn_Type()
)
cucsStorageDiskEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsRn.setStatus("current")
_CucsStorageDiskEnvStatsIntervals_Type = Gauge32
_CucsStorageDiskEnvStatsIntervals_Object = MibTableColumn
cucsStorageDiskEnvStatsIntervals = _CucsStorageDiskEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 4),
    _CucsStorageDiskEnvStatsIntervals_Type()
)
cucsStorageDiskEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsIntervals.setStatus("current")
_CucsStorageDiskEnvStatsSuspect_Type = TruthValue
_CucsStorageDiskEnvStatsSuspect_Object = MibTableColumn
cucsStorageDiskEnvStatsSuspect = _CucsStorageDiskEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 5),
    _CucsStorageDiskEnvStatsSuspect_Type()
)
cucsStorageDiskEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsSuspect.setStatus("current")
_CucsStorageDiskEnvStatsTemperature_Type = Integer32
_CucsStorageDiskEnvStatsTemperature_Object = MibTableColumn
cucsStorageDiskEnvStatsTemperature = _CucsStorageDiskEnvStatsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 6),
    _CucsStorageDiskEnvStatsTemperature_Type()
)
cucsStorageDiskEnvStatsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsTemperature.setStatus("current")
_CucsStorageDiskEnvStatsTemperatureAvg_Type = Integer32
_CucsStorageDiskEnvStatsTemperatureAvg_Object = MibTableColumn
cucsStorageDiskEnvStatsTemperatureAvg = _CucsStorageDiskEnvStatsTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 7),
    _CucsStorageDiskEnvStatsTemperatureAvg_Type()
)
cucsStorageDiskEnvStatsTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsTemperatureAvg.setStatus("current")
_CucsStorageDiskEnvStatsTemperatureMax_Type = Integer32
_CucsStorageDiskEnvStatsTemperatureMax_Object = MibTableColumn
cucsStorageDiskEnvStatsTemperatureMax = _CucsStorageDiskEnvStatsTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 8),
    _CucsStorageDiskEnvStatsTemperatureMax_Type()
)
cucsStorageDiskEnvStatsTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsTemperatureMax.setStatus("current")
_CucsStorageDiskEnvStatsTemperatureMin_Type = Integer32
_CucsStorageDiskEnvStatsTemperatureMin_Object = MibTableColumn
cucsStorageDiskEnvStatsTemperatureMin = _CucsStorageDiskEnvStatsTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 9),
    _CucsStorageDiskEnvStatsTemperatureMin_Type()
)
cucsStorageDiskEnvStatsTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsTemperatureMin.setStatus("current")
_CucsStorageDiskEnvStatsThresholded_Type = CucsStorageDiskEnvStatsThresholded
_CucsStorageDiskEnvStatsThresholded_Object = MibTableColumn
cucsStorageDiskEnvStatsThresholded = _CucsStorageDiskEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 10),
    _CucsStorageDiskEnvStatsThresholded_Type()
)
cucsStorageDiskEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsThresholded.setStatus("current")
_CucsStorageDiskEnvStatsTimeCollected_Type = DateAndTime
_CucsStorageDiskEnvStatsTimeCollected_Object = MibTableColumn
cucsStorageDiskEnvStatsTimeCollected = _CucsStorageDiskEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 11),
    _CucsStorageDiskEnvStatsTimeCollected_Type()
)
cucsStorageDiskEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsTimeCollected.setStatus("current")
_CucsStorageDiskEnvStatsUpdate_Type = Gauge32
_CucsStorageDiskEnvStatsUpdate_Object = MibTableColumn
cucsStorageDiskEnvStatsUpdate = _CucsStorageDiskEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 12),
    _CucsStorageDiskEnvStatsUpdate_Type()
)
cucsStorageDiskEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsUpdate.setStatus("current")
_CucsStorageDiskEnvStatsWearPercentage_Type = Gauge32
_CucsStorageDiskEnvStatsWearPercentage_Object = MibTableColumn
cucsStorageDiskEnvStatsWearPercentage = _CucsStorageDiskEnvStatsWearPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 13),
    _CucsStorageDiskEnvStatsWearPercentage_Type()
)
cucsStorageDiskEnvStatsWearPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsWearPercentage.setStatus("current")
_CucsStorageDiskEnvStatsWearPercentageAvg_Type = Gauge32
_CucsStorageDiskEnvStatsWearPercentageAvg_Object = MibTableColumn
cucsStorageDiskEnvStatsWearPercentageAvg = _CucsStorageDiskEnvStatsWearPercentageAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 14),
    _CucsStorageDiskEnvStatsWearPercentageAvg_Type()
)
cucsStorageDiskEnvStatsWearPercentageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsWearPercentageAvg.setStatus("current")
_CucsStorageDiskEnvStatsWearPercentageMax_Type = Gauge32
_CucsStorageDiskEnvStatsWearPercentageMax_Object = MibTableColumn
cucsStorageDiskEnvStatsWearPercentageMax = _CucsStorageDiskEnvStatsWearPercentageMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 15),
    _CucsStorageDiskEnvStatsWearPercentageMax_Type()
)
cucsStorageDiskEnvStatsWearPercentageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsWearPercentageMax.setStatus("current")
_CucsStorageDiskEnvStatsWearPercentageMin_Type = Gauge32
_CucsStorageDiskEnvStatsWearPercentageMin_Object = MibTableColumn
cucsStorageDiskEnvStatsWearPercentageMin = _CucsStorageDiskEnvStatsWearPercentageMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 50, 1, 16),
    _CucsStorageDiskEnvStatsWearPercentageMin_Type()
)
cucsStorageDiskEnvStatsWearPercentageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsWearPercentageMin.setStatus("current")
_CucsStorageDiskEnvStatsHistTable_Object = MibTable
cucsStorageDiskEnvStatsHistTable = _CucsStorageDiskEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51)
)
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistTable.setStatus("current")
_CucsStorageDiskEnvStatsHistEntry_Object = MibTableRow
cucsStorageDiskEnvStatsHistEntry = _CucsStorageDiskEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1)
)
cucsStorageDiskEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageDiskEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistEntry.setStatus("current")
_CucsStorageDiskEnvStatsHistInstanceId_Type = CucsManagedObjectId
_CucsStorageDiskEnvStatsHistInstanceId_Object = MibTableColumn
cucsStorageDiskEnvStatsHistInstanceId = _CucsStorageDiskEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 1),
    _CucsStorageDiskEnvStatsHistInstanceId_Type()
)
cucsStorageDiskEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistInstanceId.setStatus("current")
_CucsStorageDiskEnvStatsHistDn_Type = CucsManagedObjectDn
_CucsStorageDiskEnvStatsHistDn_Object = MibTableColumn
cucsStorageDiskEnvStatsHistDn = _CucsStorageDiskEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 2),
    _CucsStorageDiskEnvStatsHistDn_Type()
)
cucsStorageDiskEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistDn.setStatus("current")
_CucsStorageDiskEnvStatsHistRn_Type = SnmpAdminString
_CucsStorageDiskEnvStatsHistRn_Object = MibTableColumn
cucsStorageDiskEnvStatsHistRn = _CucsStorageDiskEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 3),
    _CucsStorageDiskEnvStatsHistRn_Type()
)
cucsStorageDiskEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistRn.setStatus("current")
_CucsStorageDiskEnvStatsHistId_Type = Unsigned64
_CucsStorageDiskEnvStatsHistId_Object = MibTableColumn
cucsStorageDiskEnvStatsHistId = _CucsStorageDiskEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 4),
    _CucsStorageDiskEnvStatsHistId_Type()
)
cucsStorageDiskEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistId.setStatus("current")
_CucsStorageDiskEnvStatsHistMostRecent_Type = TruthValue
_CucsStorageDiskEnvStatsHistMostRecent_Object = MibTableColumn
cucsStorageDiskEnvStatsHistMostRecent = _CucsStorageDiskEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 5),
    _CucsStorageDiskEnvStatsHistMostRecent_Type()
)
cucsStorageDiskEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistMostRecent.setStatus("current")
_CucsStorageDiskEnvStatsHistSuspect_Type = TruthValue
_CucsStorageDiskEnvStatsHistSuspect_Object = MibTableColumn
cucsStorageDiskEnvStatsHistSuspect = _CucsStorageDiskEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 6),
    _CucsStorageDiskEnvStatsHistSuspect_Type()
)
cucsStorageDiskEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistSuspect.setStatus("current")
_CucsStorageDiskEnvStatsHistTemperature_Type = Integer32
_CucsStorageDiskEnvStatsHistTemperature_Object = MibTableColumn
cucsStorageDiskEnvStatsHistTemperature = _CucsStorageDiskEnvStatsHistTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 7),
    _CucsStorageDiskEnvStatsHistTemperature_Type()
)
cucsStorageDiskEnvStatsHistTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistTemperature.setStatus("current")
_CucsStorageDiskEnvStatsHistTemperatureAvg_Type = Integer32
_CucsStorageDiskEnvStatsHistTemperatureAvg_Object = MibTableColumn
cucsStorageDiskEnvStatsHistTemperatureAvg = _CucsStorageDiskEnvStatsHistTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 8),
    _CucsStorageDiskEnvStatsHistTemperatureAvg_Type()
)
cucsStorageDiskEnvStatsHistTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistTemperatureAvg.setStatus("current")
_CucsStorageDiskEnvStatsHistTemperatureMax_Type = Integer32
_CucsStorageDiskEnvStatsHistTemperatureMax_Object = MibTableColumn
cucsStorageDiskEnvStatsHistTemperatureMax = _CucsStorageDiskEnvStatsHistTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 9),
    _CucsStorageDiskEnvStatsHistTemperatureMax_Type()
)
cucsStorageDiskEnvStatsHistTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistTemperatureMax.setStatus("current")
_CucsStorageDiskEnvStatsHistTemperatureMin_Type = Integer32
_CucsStorageDiskEnvStatsHistTemperatureMin_Object = MibTableColumn
cucsStorageDiskEnvStatsHistTemperatureMin = _CucsStorageDiskEnvStatsHistTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 10),
    _CucsStorageDiskEnvStatsHistTemperatureMin_Type()
)
cucsStorageDiskEnvStatsHistTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistTemperatureMin.setStatus("current")
_CucsStorageDiskEnvStatsHistThresholded_Type = CucsStorageDiskEnvStatsHistThresholded
_CucsStorageDiskEnvStatsHistThresholded_Object = MibTableColumn
cucsStorageDiskEnvStatsHistThresholded = _CucsStorageDiskEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 11),
    _CucsStorageDiskEnvStatsHistThresholded_Type()
)
cucsStorageDiskEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistThresholded.setStatus("current")
_CucsStorageDiskEnvStatsHistTimeCollected_Type = DateAndTime
_CucsStorageDiskEnvStatsHistTimeCollected_Object = MibTableColumn
cucsStorageDiskEnvStatsHistTimeCollected = _CucsStorageDiskEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 12),
    _CucsStorageDiskEnvStatsHistTimeCollected_Type()
)
cucsStorageDiskEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistTimeCollected.setStatus("current")
_CucsStorageDiskEnvStatsHistWearPercentage_Type = Gauge32
_CucsStorageDiskEnvStatsHistWearPercentage_Object = MibTableColumn
cucsStorageDiskEnvStatsHistWearPercentage = _CucsStorageDiskEnvStatsHistWearPercentage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 13),
    _CucsStorageDiskEnvStatsHistWearPercentage_Type()
)
cucsStorageDiskEnvStatsHistWearPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistWearPercentage.setStatus("current")
_CucsStorageDiskEnvStatsHistWearPercentageAvg_Type = Gauge32
_CucsStorageDiskEnvStatsHistWearPercentageAvg_Object = MibTableColumn
cucsStorageDiskEnvStatsHistWearPercentageAvg = _CucsStorageDiskEnvStatsHistWearPercentageAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 14),
    _CucsStorageDiskEnvStatsHistWearPercentageAvg_Type()
)
cucsStorageDiskEnvStatsHistWearPercentageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistWearPercentageAvg.setStatus("current")
_CucsStorageDiskEnvStatsHistWearPercentageMax_Type = Gauge32
_CucsStorageDiskEnvStatsHistWearPercentageMax_Object = MibTableColumn
cucsStorageDiskEnvStatsHistWearPercentageMax = _CucsStorageDiskEnvStatsHistWearPercentageMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 15),
    _CucsStorageDiskEnvStatsHistWearPercentageMax_Type()
)
cucsStorageDiskEnvStatsHistWearPercentageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistWearPercentageMax.setStatus("current")
_CucsStorageDiskEnvStatsHistWearPercentageMin_Type = Gauge32
_CucsStorageDiskEnvStatsHistWearPercentageMin_Object = MibTableColumn
cucsStorageDiskEnvStatsHistWearPercentageMin = _CucsStorageDiskEnvStatsHistWearPercentageMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 51, 1, 16),
    _CucsStorageDiskEnvStatsHistWearPercentageMin_Type()
)
cucsStorageDiskEnvStatsHistWearPercentageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageDiskEnvStatsHistWearPercentageMin.setStatus("current")
_CucsStorageLunResourceSelectionLogTable_Object = MibTable
cucsStorageLunResourceSelectionLogTable = _CucsStorageLunResourceSelectionLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 64)
)
if mibBuilder.loadTexts:
    cucsStorageLunResourceSelectionLogTable.setStatus("current")
_CucsStorageLunResourceSelectionLogEntry_Object = MibTableRow
cucsStorageLunResourceSelectionLogEntry = _CucsStorageLunResourceSelectionLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 64, 1)
)
cucsStorageLunResourceSelectionLogEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageLunResourceSelectionLogInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageLunResourceSelectionLogEntry.setStatus("current")
_CucsStorageLunResourceSelectionLogInstanceId_Type = CucsManagedObjectId
_CucsStorageLunResourceSelectionLogInstanceId_Object = MibTableColumn
cucsStorageLunResourceSelectionLogInstanceId = _CucsStorageLunResourceSelectionLogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 64, 1, 1),
    _CucsStorageLunResourceSelectionLogInstanceId_Type()
)
cucsStorageLunResourceSelectionLogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageLunResourceSelectionLogInstanceId.setStatus("current")
_CucsStorageLunResourceSelectionLogDn_Type = CucsManagedObjectDn
_CucsStorageLunResourceSelectionLogDn_Object = MibTableColumn
cucsStorageLunResourceSelectionLogDn = _CucsStorageLunResourceSelectionLogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 64, 1, 2),
    _CucsStorageLunResourceSelectionLogDn_Type()
)
cucsStorageLunResourceSelectionLogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLunResourceSelectionLogDn.setStatus("current")
_CucsStorageLunResourceSelectionLogRn_Type = SnmpAdminString
_CucsStorageLunResourceSelectionLogRn_Object = MibTableColumn
cucsStorageLunResourceSelectionLogRn = _CucsStorageLunResourceSelectionLogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 64, 1, 3),
    _CucsStorageLunResourceSelectionLogRn_Type()
)
cucsStorageLunResourceSelectionLogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLunResourceSelectionLogRn.setStatus("current")
_CucsStorageLunResourceSelectionLogDecisionType_Type = CucsStorageSelectionDecisionType
_CucsStorageLunResourceSelectionLogDecisionType_Object = MibTableColumn
cucsStorageLunResourceSelectionLogDecisionType = _CucsStorageLunResourceSelectionLogDecisionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 64, 1, 4),
    _CucsStorageLunResourceSelectionLogDecisionType_Type()
)
cucsStorageLunResourceSelectionLogDecisionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLunResourceSelectionLogDecisionType.setStatus("current")
_CucsStorageLunResourceSelectionLogDescr_Type = SnmpAdminString
_CucsStorageLunResourceSelectionLogDescr_Object = MibTableColumn
cucsStorageLunResourceSelectionLogDescr = _CucsStorageLunResourceSelectionLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 64, 1, 5),
    _CucsStorageLunResourceSelectionLogDescr_Type()
)
cucsStorageLunResourceSelectionLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLunResourceSelectionLogDescr.setStatus("current")
_CucsStorageLunResourceSelectionLogOrder_Type = Gauge32
_CucsStorageLunResourceSelectionLogOrder_Object = MibTableColumn
cucsStorageLunResourceSelectionLogOrder = _CucsStorageLunResourceSelectionLogOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 64, 1, 6),
    _CucsStorageLunResourceSelectionLogOrder_Type()
)
cucsStorageLunResourceSelectionLogOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLunResourceSelectionLogOrder.setStatus("current")
_CucsStorageLunResourceSelectionLogResult_Type = CucsStorageSelectionResultType
_CucsStorageLunResourceSelectionLogResult_Object = MibTableColumn
cucsStorageLunResourceSelectionLogResult = _CucsStorageLunResourceSelectionLogResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 64, 1, 7),
    _CucsStorageLunResourceSelectionLogResult_Type()
)
cucsStorageLunResourceSelectionLogResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLunResourceSelectionLogResult.setStatus("current")
_CucsStorageLunResourceSelectionLogTimeStamp_Type = DateAndTime
_CucsStorageLunResourceSelectionLogTimeStamp_Object = MibTableColumn
cucsStorageLunResourceSelectionLogTimeStamp = _CucsStorageLunResourceSelectionLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 64, 1, 8),
    _CucsStorageLunResourceSelectionLogTimeStamp_Type()
)
cucsStorageLunResourceSelectionLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageLunResourceSelectionLogTimeStamp.setStatus("current")
_CucsStorageSasExpanderTable_Object = MibTable
cucsStorageSasExpanderTable = _CucsStorageSasExpanderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78)
)
if mibBuilder.loadTexts:
    cucsStorageSasExpanderTable.setStatus("current")
_CucsStorageSasExpanderEntry_Object = MibTableRow
cucsStorageSasExpanderEntry = _CucsStorageSasExpanderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1)
)
cucsStorageSasExpanderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageSasExpanderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageSasExpanderEntry.setStatus("current")
_CucsStorageSasExpanderInstanceId_Type = CucsManagedObjectId
_CucsStorageSasExpanderInstanceId_Object = MibTableColumn
cucsStorageSasExpanderInstanceId = _CucsStorageSasExpanderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 1),
    _CucsStorageSasExpanderInstanceId_Type()
)
cucsStorageSasExpanderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderInstanceId.setStatus("current")
_CucsStorageSasExpanderDn_Type = CucsManagedObjectDn
_CucsStorageSasExpanderDn_Object = MibTableColumn
cucsStorageSasExpanderDn = _CucsStorageSasExpanderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 2),
    _CucsStorageSasExpanderDn_Type()
)
cucsStorageSasExpanderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderDn.setStatus("current")
_CucsStorageSasExpanderRn_Type = SnmpAdminString
_CucsStorageSasExpanderRn_Object = MibTableColumn
cucsStorageSasExpanderRn = _CucsStorageSasExpanderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 3),
    _CucsStorageSasExpanderRn_Type()
)
cucsStorageSasExpanderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderRn.setStatus("current")
_CucsStorageSasExpanderId_Type = Gauge32
_CucsStorageSasExpanderId_Object = MibTableColumn
cucsStorageSasExpanderId = _CucsStorageSasExpanderId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 4),
    _CucsStorageSasExpanderId_Type()
)
cucsStorageSasExpanderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderId.setStatus("current")
_CucsStorageSasExpanderLocationDn_Type = SnmpAdminString
_CucsStorageSasExpanderLocationDn_Object = MibTableColumn
cucsStorageSasExpanderLocationDn = _CucsStorageSasExpanderLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 5),
    _CucsStorageSasExpanderLocationDn_Type()
)
cucsStorageSasExpanderLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderLocationDn.setStatus("current")
_CucsStorageSasExpanderModel_Type = SnmpAdminString
_CucsStorageSasExpanderModel_Object = MibTableColumn
cucsStorageSasExpanderModel = _CucsStorageSasExpanderModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 6),
    _CucsStorageSasExpanderModel_Type()
)
cucsStorageSasExpanderModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderModel.setStatus("current")
_CucsStorageSasExpanderOperQualifierReason_Type = SnmpAdminString
_CucsStorageSasExpanderOperQualifierReason_Object = MibTableColumn
cucsStorageSasExpanderOperQualifierReason = _CucsStorageSasExpanderOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 7),
    _CucsStorageSasExpanderOperQualifierReason_Type()
)
cucsStorageSasExpanderOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderOperQualifierReason.setStatus("current")
_CucsStorageSasExpanderOperState_Type = CucsEquipmentOperability
_CucsStorageSasExpanderOperState_Object = MibTableColumn
cucsStorageSasExpanderOperState = _CucsStorageSasExpanderOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 8),
    _CucsStorageSasExpanderOperState_Type()
)
cucsStorageSasExpanderOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderOperState.setStatus("current")
_CucsStorageSasExpanderOperability_Type = CucsEquipmentOperability
_CucsStorageSasExpanderOperability_Object = MibTableColumn
cucsStorageSasExpanderOperability = _CucsStorageSasExpanderOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 9),
    _CucsStorageSasExpanderOperability_Type()
)
cucsStorageSasExpanderOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderOperability.setStatus("current")
_CucsStorageSasExpanderPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsStorageSasExpanderPerf_Object = MibTableColumn
cucsStorageSasExpanderPerf = _CucsStorageSasExpanderPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 10),
    _CucsStorageSasExpanderPerf_Type()
)
cucsStorageSasExpanderPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderPerf.setStatus("current")
_CucsStorageSasExpanderPower_Type = CucsEquipmentPowerState
_CucsStorageSasExpanderPower_Object = MibTableColumn
cucsStorageSasExpanderPower = _CucsStorageSasExpanderPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 11),
    _CucsStorageSasExpanderPower_Type()
)
cucsStorageSasExpanderPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderPower.setStatus("current")
_CucsStorageSasExpanderPresence_Type = CucsEquipmentPresence
_CucsStorageSasExpanderPresence_Object = MibTableColumn
cucsStorageSasExpanderPresence = _CucsStorageSasExpanderPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 12),
    _CucsStorageSasExpanderPresence_Type()
)
cucsStorageSasExpanderPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderPresence.setStatus("current")
_CucsStorageSasExpanderRevision_Type = SnmpAdminString
_CucsStorageSasExpanderRevision_Object = MibTableColumn
cucsStorageSasExpanderRevision = _CucsStorageSasExpanderRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 13),
    _CucsStorageSasExpanderRevision_Type()
)
cucsStorageSasExpanderRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderRevision.setStatus("current")
_CucsStorageSasExpanderSerial_Type = SnmpAdminString
_CucsStorageSasExpanderSerial_Object = MibTableColumn
cucsStorageSasExpanderSerial = _CucsStorageSasExpanderSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 14),
    _CucsStorageSasExpanderSerial_Type()
)
cucsStorageSasExpanderSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderSerial.setStatus("current")
_CucsStorageSasExpanderThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsStorageSasExpanderThermal_Object = MibTableColumn
cucsStorageSasExpanderThermal = _CucsStorageSasExpanderThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 15),
    _CucsStorageSasExpanderThermal_Type()
)
cucsStorageSasExpanderThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderThermal.setStatus("current")
_CucsStorageSasExpanderVendor_Type = SnmpAdminString
_CucsStorageSasExpanderVendor_Object = MibTableColumn
cucsStorageSasExpanderVendor = _CucsStorageSasExpanderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 16),
    _CucsStorageSasExpanderVendor_Type()
)
cucsStorageSasExpanderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderVendor.setStatus("current")
_CucsStorageSasExpanderVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsStorageSasExpanderVoltage_Object = MibTableColumn
cucsStorageSasExpanderVoltage = _CucsStorageSasExpanderVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 17),
    _CucsStorageSasExpanderVoltage_Type()
)
cucsStorageSasExpanderVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderVoltage.setStatus("current")
_CucsStorageSasExpanderFwRegionOne_Type = SnmpAdminString
_CucsStorageSasExpanderFwRegionOne_Object = MibTableColumn
cucsStorageSasExpanderFwRegionOne = _CucsStorageSasExpanderFwRegionOne_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 23),
    _CucsStorageSasExpanderFwRegionOne_Type()
)
cucsStorageSasExpanderFwRegionOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderFwRegionOne.setStatus("current")
_CucsStorageSasExpanderFwRegionTwo_Type = SnmpAdminString
_CucsStorageSasExpanderFwRegionTwo_Object = MibTableColumn
cucsStorageSasExpanderFwRegionTwo = _CucsStorageSasExpanderFwRegionTwo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 24),
    _CucsStorageSasExpanderFwRegionTwo_Type()
)
cucsStorageSasExpanderFwRegionTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderFwRegionTwo.setStatus("current")
_CucsStorageSasExpanderFwRunningRegion_Type = SnmpAdminString
_CucsStorageSasExpanderFwRunningRegion_Object = MibTableColumn
cucsStorageSasExpanderFwRunningRegion = _CucsStorageSasExpanderFwRunningRegion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 25),
    _CucsStorageSasExpanderFwRunningRegion_Type()
)
cucsStorageSasExpanderFwRunningRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderFwRunningRegion.setStatus("current")
_CucsStorageSasExpanderSasAddress_Type = SnmpAdminString
_CucsStorageSasExpanderSasAddress_Object = MibTableColumn
cucsStorageSasExpanderSasAddress = _CucsStorageSasExpanderSasAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 78, 1, 26),
    _CucsStorageSasExpanderSasAddress_Type()
)
cucsStorageSasExpanderSasAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageSasExpanderSasAddress.setStatus("current")
_CucsStorageScsiLunRefTable_Object = MibTable
cucsStorageScsiLunRefTable = _CucsStorageScsiLunRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 83)
)
if mibBuilder.loadTexts:
    cucsStorageScsiLunRefTable.setStatus("current")
_CucsStorageScsiLunRefEntry_Object = MibTableRow
cucsStorageScsiLunRefEntry = _CucsStorageScsiLunRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 83, 1)
)
cucsStorageScsiLunRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageScsiLunRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageScsiLunRefEntry.setStatus("current")
_CucsStorageScsiLunRefInstanceId_Type = CucsManagedObjectId
_CucsStorageScsiLunRefInstanceId_Object = MibTableColumn
cucsStorageScsiLunRefInstanceId = _CucsStorageScsiLunRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 83, 1, 1),
    _CucsStorageScsiLunRefInstanceId_Type()
)
cucsStorageScsiLunRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageScsiLunRefInstanceId.setStatus("current")
_CucsStorageScsiLunRefDn_Type = CucsManagedObjectDn
_CucsStorageScsiLunRefDn_Object = MibTableColumn
cucsStorageScsiLunRefDn = _CucsStorageScsiLunRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 83, 1, 2),
    _CucsStorageScsiLunRefDn_Type()
)
cucsStorageScsiLunRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageScsiLunRefDn.setStatus("current")
_CucsStorageScsiLunRefRn_Type = SnmpAdminString
_CucsStorageScsiLunRefRn_Object = MibTableColumn
cucsStorageScsiLunRefRn = _CucsStorageScsiLunRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 83, 1, 3),
    _CucsStorageScsiLunRefRn_Type()
)
cucsStorageScsiLunRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageScsiLunRefRn.setStatus("current")
_CucsStorageScsiLunRefId_Type = Gauge32
_CucsStorageScsiLunRefId_Object = MibTableColumn
cucsStorageScsiLunRefId = _CucsStorageScsiLunRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 83, 1, 4),
    _CucsStorageScsiLunRefId_Type()
)
cucsStorageScsiLunRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageScsiLunRefId.setStatus("current")
_CucsStorageScsiLunRefLsDn_Type = SnmpAdminString
_CucsStorageScsiLunRefLsDn_Object = MibTableColumn
cucsStorageScsiLunRefLsDn = _CucsStorageScsiLunRefLsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 83, 1, 5),
    _CucsStorageScsiLunRefLsDn_Type()
)
cucsStorageScsiLunRefLsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageScsiLunRefLsDn.setStatus("current")
_CucsStorageScsiLunRefLunName_Type = SnmpAdminString
_CucsStorageScsiLunRefLunName_Object = MibTableColumn
cucsStorageScsiLunRefLunName = _CucsStorageScsiLunRefLunName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 83, 1, 6),
    _CucsStorageScsiLunRefLunName_Type()
)
cucsStorageScsiLunRefLunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageScsiLunRefLunName.setStatus("current")
_CucsStorageScsiLunRefProfileDn_Type = SnmpAdminString
_CucsStorageScsiLunRefProfileDn_Object = MibTableColumn
cucsStorageScsiLunRefProfileDn = _CucsStorageScsiLunRefProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 83, 1, 7),
    _CucsStorageScsiLunRefProfileDn_Type()
)
cucsStorageScsiLunRefProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageScsiLunRefProfileDn.setStatus("current")
_CucsStorageScsiLunRefPnDn_Type = SnmpAdminString
_CucsStorageScsiLunRefPnDn_Object = MibTableColumn
cucsStorageScsiLunRefPnDn = _CucsStorageScsiLunRefPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 83, 1, 8),
    _CucsStorageScsiLunRefPnDn_Type()
)
cucsStorageScsiLunRefPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageScsiLunRefPnDn.setStatus("current")
_CucsStorageVDMemberEpTable_Object = MibTable
cucsStorageVDMemberEpTable = _CucsStorageVDMemberEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90)
)
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpTable.setStatus("current")
_CucsStorageVDMemberEpEntry_Object = MibTableRow
cucsStorageVDMemberEpEntry = _CucsStorageVDMemberEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1)
)
cucsStorageVDMemberEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageVDMemberEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpEntry.setStatus("current")
_CucsStorageVDMemberEpInstanceId_Type = CucsManagedObjectId
_CucsStorageVDMemberEpInstanceId_Object = MibTableColumn
cucsStorageVDMemberEpInstanceId = _CucsStorageVDMemberEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 1),
    _CucsStorageVDMemberEpInstanceId_Type()
)
cucsStorageVDMemberEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpInstanceId.setStatus("current")
_CucsStorageVDMemberEpDn_Type = CucsManagedObjectDn
_CucsStorageVDMemberEpDn_Object = MibTableColumn
cucsStorageVDMemberEpDn = _CucsStorageVDMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 2),
    _CucsStorageVDMemberEpDn_Type()
)
cucsStorageVDMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpDn.setStatus("current")
_CucsStorageVDMemberEpRn_Type = SnmpAdminString
_CucsStorageVDMemberEpRn_Object = MibTableColumn
cucsStorageVDMemberEpRn = _CucsStorageVDMemberEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 3),
    _CucsStorageVDMemberEpRn_Type()
)
cucsStorageVDMemberEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpRn.setStatus("current")
_CucsStorageVDMemberEpConfigQual_Type = CucsStorageVdMemberConfigQualifierType
_CucsStorageVDMemberEpConfigQual_Object = MibTableColumn
cucsStorageVDMemberEpConfigQual = _CucsStorageVDMemberEpConfigQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 4),
    _CucsStorageVDMemberEpConfigQual_Type()
)
cucsStorageVDMemberEpConfigQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpConfigQual.setStatus("current")
_CucsStorageVDMemberEpConfigQualifierReason_Type = SnmpAdminString
_CucsStorageVDMemberEpConfigQualifierReason_Object = MibTableColumn
cucsStorageVDMemberEpConfigQualifierReason = _CucsStorageVDMemberEpConfigQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 5),
    _CucsStorageVDMemberEpConfigQualifierReason_Type()
)
cucsStorageVDMemberEpConfigQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpConfigQualifierReason.setStatus("current")
_CucsStorageVDMemberEpConfigState_Type = CucsStorageConfigState
_CucsStorageVDMemberEpConfigState_Object = MibTableColumn
cucsStorageVDMemberEpConfigState = _CucsStorageVDMemberEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 6),
    _CucsStorageVDMemberEpConfigState_Type()
)
cucsStorageVDMemberEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpConfigState.setStatus("current")
_CucsStorageVDMemberEpDeployAction_Type = CucsStorageDeployAction
_CucsStorageVDMemberEpDeployAction_Object = MibTableColumn
cucsStorageVDMemberEpDeployAction = _CucsStorageVDMemberEpDeployAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 7),
    _CucsStorageVDMemberEpDeployAction_Type()
)
cucsStorageVDMemberEpDeployAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpDeployAction.setStatus("current")
_CucsStorageVDMemberEpDiskDn_Type = SnmpAdminString
_CucsStorageVDMemberEpDiskDn_Object = MibTableColumn
cucsStorageVDMemberEpDiskDn = _CucsStorageVDMemberEpDiskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 8),
    _CucsStorageVDMemberEpDiskDn_Type()
)
cucsStorageVDMemberEpDiskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpDiskDn.setStatus("current")
_CucsStorageVDMemberEpId_Type = Gauge32
_CucsStorageVDMemberEpId_Object = MibTableColumn
cucsStorageVDMemberEpId = _CucsStorageVDMemberEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 9),
    _CucsStorageVDMemberEpId_Type()
)
cucsStorageVDMemberEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpId.setStatus("current")
_CucsStorageVDMemberEpModel_Type = SnmpAdminString
_CucsStorageVDMemberEpModel_Object = MibTableColumn
cucsStorageVDMemberEpModel = _CucsStorageVDMemberEpModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 10),
    _CucsStorageVDMemberEpModel_Type()
)
cucsStorageVDMemberEpModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpModel.setStatus("current")
_CucsStorageVDMemberEpOperQualifierReason_Type = SnmpAdminString
_CucsStorageVDMemberEpOperQualifierReason_Object = MibTableColumn
cucsStorageVDMemberEpOperQualifierReason = _CucsStorageVDMemberEpOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 11),
    _CucsStorageVDMemberEpOperQualifierReason_Type()
)
cucsStorageVDMemberEpOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpOperQualifierReason.setStatus("current")
_CucsStorageVDMemberEpOperability_Type = CucsEquipmentOperability
_CucsStorageVDMemberEpOperability_Object = MibTableColumn
cucsStorageVDMemberEpOperability = _CucsStorageVDMemberEpOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 12),
    _CucsStorageVDMemberEpOperability_Type()
)
cucsStorageVDMemberEpOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpOperability.setStatus("current")
_CucsStorageVDMemberEpPresence_Type = CucsEquipmentPresence
_CucsStorageVDMemberEpPresence_Object = MibTableColumn
cucsStorageVDMemberEpPresence = _CucsStorageVDMemberEpPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 13),
    _CucsStorageVDMemberEpPresence_Type()
)
cucsStorageVDMemberEpPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpPresence.setStatus("current")
_CucsStorageVDMemberEpRevision_Type = SnmpAdminString
_CucsStorageVDMemberEpRevision_Object = MibTableColumn
cucsStorageVDMemberEpRevision = _CucsStorageVDMemberEpRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 14),
    _CucsStorageVDMemberEpRevision_Type()
)
cucsStorageVDMemberEpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpRevision.setStatus("current")
_CucsStorageVDMemberEpRole_Type = CucsStorageDiskRole
_CucsStorageVDMemberEpRole_Object = MibTableColumn
cucsStorageVDMemberEpRole = _CucsStorageVDMemberEpRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 15),
    _CucsStorageVDMemberEpRole_Type()
)
cucsStorageVDMemberEpRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpRole.setStatus("current")
_CucsStorageVDMemberEpSerial_Type = SnmpAdminString
_CucsStorageVDMemberEpSerial_Object = MibTableColumn
cucsStorageVDMemberEpSerial = _CucsStorageVDMemberEpSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 16),
    _CucsStorageVDMemberEpSerial_Type()
)
cucsStorageVDMemberEpSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpSerial.setStatus("current")
_CucsStorageVDMemberEpSpanId_Type = Gauge32
_CucsStorageVDMemberEpSpanId_Object = MibTableColumn
cucsStorageVDMemberEpSpanId = _CucsStorageVDMemberEpSpanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 17),
    _CucsStorageVDMemberEpSpanId_Type()
)
cucsStorageVDMemberEpSpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpSpanId.setStatus("current")
_CucsStorageVDMemberEpVendor_Type = SnmpAdminString
_CucsStorageVDMemberEpVendor_Object = MibTableColumn
cucsStorageVDMemberEpVendor = _CucsStorageVDMemberEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 90, 1, 18),
    _CucsStorageVDMemberEpVendor_Type()
)
cucsStorageVDMemberEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVDMemberEpVendor.setStatus("current")
_CucsStorageVirtualDriveRefTable_Object = MibTable
cucsStorageVirtualDriveRefTable = _CucsStorageVirtualDriveRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91)
)
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefTable.setStatus("current")
_CucsStorageVirtualDriveRefEntry_Object = MibTableRow
cucsStorageVirtualDriveRefEntry = _CucsStorageVirtualDriveRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1)
)
cucsStorageVirtualDriveRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STORAGE-MIB", "cucsStorageVirtualDriveRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefEntry.setStatus("current")
_CucsStorageVirtualDriveRefInstanceId_Type = CucsManagedObjectId
_CucsStorageVirtualDriveRefInstanceId_Object = MibTableColumn
cucsStorageVirtualDriveRefInstanceId = _CucsStorageVirtualDriveRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 1),
    _CucsStorageVirtualDriveRefInstanceId_Type()
)
cucsStorageVirtualDriveRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefInstanceId.setStatus("current")
_CucsStorageVirtualDriveRefDnData_Type = CucsManagedObjectDn
_CucsStorageVirtualDriveRefDnData_Object = MibTableColumn
cucsStorageVirtualDriveRefDnData = _CucsStorageVirtualDriveRefDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 2),
    _CucsStorageVirtualDriveRefDnData_Type()
)
cucsStorageVirtualDriveRefDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefDnData.setStatus("current")
_CucsStorageVirtualDriveRefRn_Type = SnmpAdminString
_CucsStorageVirtualDriveRefRn_Object = MibTableColumn
cucsStorageVirtualDriveRefRn = _CucsStorageVirtualDriveRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 3),
    _CucsStorageVirtualDriveRefRn_Type()
)
cucsStorageVirtualDriveRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefRn.setStatus("current")
_CucsStorageVirtualDriveRefAdminName_Type = SnmpAdminString
_CucsStorageVirtualDriveRefAdminName_Object = MibTableColumn
cucsStorageVirtualDriveRefAdminName = _CucsStorageVirtualDriveRefAdminName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 4),
    _CucsStorageVirtualDriveRefAdminName_Type()
)
cucsStorageVirtualDriveRefAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefAdminName.setStatus("current")
_CucsStorageVirtualDriveRefAdminState_Type = CucsStorageVirtualDriveRefAdminState
_CucsStorageVirtualDriveRefAdminState_Object = MibTableColumn
cucsStorageVirtualDriveRefAdminState = _CucsStorageVirtualDriveRefAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 5),
    _CucsStorageVirtualDriveRefAdminState_Type()
)
cucsStorageVirtualDriveRefAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefAdminState.setStatus("current")
_CucsStorageVirtualDriveRefConfigState_Type = CucsStorageConfigState
_CucsStorageVirtualDriveRefConfigState_Object = MibTableColumn
cucsStorageVirtualDriveRefConfigState = _CucsStorageVirtualDriveRefConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 6),
    _CucsStorageVirtualDriveRefConfigState_Type()
)
cucsStorageVirtualDriveRefConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefConfigState.setStatus("current")
_CucsStorageVirtualDriveRefDiskSelectionOrder_Type = Gauge32
_CucsStorageVirtualDriveRefDiskSelectionOrder_Object = MibTableColumn
cucsStorageVirtualDriveRefDiskSelectionOrder = _CucsStorageVirtualDriveRefDiskSelectionOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 7),
    _CucsStorageVirtualDriveRefDiskSelectionOrder_Type()
)
cucsStorageVirtualDriveRefDiskSelectionOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefDiskSelectionOrder.setStatus("current")
_CucsStorageVirtualDriveRefDiskSelectionTs_Type = DateAndTime
_CucsStorageVirtualDriveRefDiskSelectionTs_Object = MibTableColumn
cucsStorageVirtualDriveRefDiskSelectionTs = _CucsStorageVirtualDriveRefDiskSelectionTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 8),
    _CucsStorageVirtualDriveRefDiskSelectionTs_Type()
)
cucsStorageVirtualDriveRefDiskSelectionTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefDiskSelectionTs.setStatus("current")
_CucsStorageVirtualDriveRefLunDn_Type = SnmpAdminString
_CucsStorageVirtualDriveRefLunDn_Object = MibTableColumn
cucsStorageVirtualDriveRefLunDn = _CucsStorageVirtualDriveRefLunDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 9),
    _CucsStorageVirtualDriveRefLunDn_Type()
)
cucsStorageVirtualDriveRefLunDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefLunDn.setStatus("current")
_CucsStorageVirtualDriveRefLunItemDn_Type = SnmpAdminString
_CucsStorageVirtualDriveRefLunItemDn_Object = MibTableColumn
cucsStorageVirtualDriveRefLunItemDn = _CucsStorageVirtualDriveRefLunItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 10),
    _CucsStorageVirtualDriveRefLunItemDn_Type()
)
cucsStorageVirtualDriveRefLunItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefLunItemDn.setStatus("current")
_CucsStorageVirtualDriveRefLunItemName_Type = SnmpAdminString
_CucsStorageVirtualDriveRefLunItemName_Object = MibTableColumn
cucsStorageVirtualDriveRefLunItemName = _CucsStorageVirtualDriveRefLunItemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 11),
    _CucsStorageVirtualDriveRefLunItemName_Type()
)
cucsStorageVirtualDriveRefLunItemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefLunItemName.setStatus("current")
_CucsStorageVirtualDriveRefLunName_Type = SnmpAdminString
_CucsStorageVirtualDriveRefLunName_Object = MibTableColumn
cucsStorageVirtualDriveRefLunName = _CucsStorageVirtualDriveRefLunName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 12),
    _CucsStorageVirtualDriveRefLunName_Type()
)
cucsStorageVirtualDriveRefLunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefLunName.setStatus("current")
_CucsStorageVirtualDriveRefRaidLevel_Type = CucsStorageLunType
_CucsStorageVirtualDriveRefRaidLevel_Object = MibTableColumn
cucsStorageVirtualDriveRefRaidLevel = _CucsStorageVirtualDriveRefRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 13),
    _CucsStorageVirtualDriveRefRaidLevel_Type()
)
cucsStorageVirtualDriveRefRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefRaidLevel.setStatus("current")
_CucsStorageVirtualDriveRefSize_Type = Unsigned64
_CucsStorageVirtualDriveRefSize_Object = MibTableColumn
cucsStorageVirtualDriveRefSize = _CucsStorageVirtualDriveRefSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 14),
    _CucsStorageVirtualDriveRefSize_Type()
)
cucsStorageVirtualDriveRefSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefSize.setStatus("current")
_CucsStorageVirtualDriveRefUuid_Type = SnmpAdminString
_CucsStorageVirtualDriveRefUuid_Object = MibTableColumn
cucsStorageVirtualDriveRefUuid = _CucsStorageVirtualDriveRefUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 15),
    _CucsStorageVirtualDriveRefUuid_Type()
)
cucsStorageVirtualDriveRefUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefUuid.setStatus("current")
_CucsStorageVirtualDriveRefIsBootable_Type = CucsLstorageBootDevice
_CucsStorageVirtualDriveRefIsBootable_Object = MibTableColumn
cucsStorageVirtualDriveRefIsBootable = _CucsStorageVirtualDriveRefIsBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 16),
    _CucsStorageVirtualDriveRefIsBootable_Type()
)
cucsStorageVirtualDriveRefIsBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefIsBootable.setStatus("current")
_CucsStorageVirtualDriveRefOrder_Type = Gauge32
_CucsStorageVirtualDriveRefOrder_Object = MibTableColumn
cucsStorageVirtualDriveRefOrder = _CucsStorageVirtualDriveRefOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 17),
    _CucsStorageVirtualDriveRefOrder_Type()
)
cucsStorageVirtualDriveRefOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefOrder.setStatus("current")
_CucsStorageVirtualDriveRefVendorUuid_Type = SnmpAdminString
_CucsStorageVirtualDriveRefVendorUuid_Object = MibTableColumn
cucsStorageVirtualDriveRefVendorUuid = _CucsStorageVirtualDriveRefVendorUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 45, 91, 1, 18),
    _CucsStorageVirtualDriveRefVendorUuid_Type()
)
cucsStorageVirtualDriveRefVendorUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStorageVirtualDriveRefVendorUuid.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-STORAGE-MIB",
    **{"cucsStorageObjects": cucsStorageObjects,
       "cucsStorageControllerTable": cucsStorageControllerTable,
       "cucsStorageControllerEntry": cucsStorageControllerEntry,
       "cucsStorageControllerInstanceId": cucsStorageControllerInstanceId,
       "cucsStorageControllerDn": cucsStorageControllerDn,
       "cucsStorageControllerRn": cucsStorageControllerRn,
       "cucsStorageControllerId": cucsStorageControllerId,
       "cucsStorageControllerModel": cucsStorageControllerModel,
       "cucsStorageControllerOperState": cucsStorageControllerOperState,
       "cucsStorageControllerOperability": cucsStorageControllerOperability,
       "cucsStorageControllerPciAddr": cucsStorageControllerPciAddr,
       "cucsStorageControllerPciSlot": cucsStorageControllerPciSlot,
       "cucsStorageControllerPerf": cucsStorageControllerPerf,
       "cucsStorageControllerPower": cucsStorageControllerPower,
       "cucsStorageControllerPresence": cucsStorageControllerPresence,
       "cucsStorageControllerRevision": cucsStorageControllerRevision,
       "cucsStorageControllerSerial": cucsStorageControllerSerial,
       "cucsStorageControllerThermal": cucsStorageControllerThermal,
       "cucsStorageControllerType": cucsStorageControllerType,
       "cucsStorageControllerVendor": cucsStorageControllerVendor,
       "cucsStorageControllerVoltage": cucsStorageControllerVoltage,
       "cucsStorageControllerRaidSupport": cucsStorageControllerRaidSupport,
       "cucsStorageControllerFaultMonitoring": cucsStorageControllerFaultMonitoring,
       "cucsStorageControllerHwRevision": cucsStorageControllerHwRevision,
       "cucsStorageControllerDeviceRaidSupport": cucsStorageControllerDeviceRaidSupport,
       "cucsStorageControllerOperQualifierReason": cucsStorageControllerOperQualifierReason,
       "cucsStorageControllerControllerStatus": cucsStorageControllerControllerStatus,
       "cucsStorageControllerLc": cucsStorageControllerLc,
       "cucsStorageControllerOobControllerId": cucsStorageControllerOobControllerId,
       "cucsStorageControllerOobInterfaceSupported": cucsStorageControllerOobInterfaceSupported,
       "cucsStorageControllerRebuildRate": cucsStorageControllerRebuildRate,
       "cucsStorageControllerLocationDn": cucsStorageControllerLocationDn,
       "cucsStorageControllerPartNumber": cucsStorageControllerPartNumber,
       "cucsStorageControllerVid": cucsStorageControllerVid,
       "cucsStorageControllerAdminAction": cucsStorageControllerAdminAction,
       "cucsStorageControllerAdminActionTrigger": cucsStorageControllerAdminActionTrigger,
       "cucsStorageControllerConfigState": cucsStorageControllerConfigState,
       "cucsStorageControllerOpromBootStatus": cucsStorageControllerOpromBootStatus,
       "cucsStorageControllerPciSlotRawName": cucsStorageControllerPciSlotRawName,
       "cucsStorageControllerIdCount": cucsStorageControllerIdCount,
       "cucsStorageControllerPinnedCacheStatus": cucsStorageControllerPinnedCacheStatus,
       "cucsStorageDriveTable": cucsStorageDriveTable,
       "cucsStorageDriveEntry": cucsStorageDriveEntry,
       "cucsStorageDriveInstanceId": cucsStorageDriveInstanceId,
       "cucsStorageDriveDn": cucsStorageDriveDn,
       "cucsStorageDriveRn": cucsStorageDriveRn,
       "cucsStorageDriveId": cucsStorageDriveId,
       "cucsStorageDriveModel": cucsStorageDriveModel,
       "cucsStorageDrivePciAddr": cucsStorageDrivePciAddr,
       "cucsStorageDriveRevision": cucsStorageDriveRevision,
       "cucsStorageDriveSerial": cucsStorageDriveSerial,
       "cucsStorageDriveVendor": cucsStorageDriveVendor,
       "cucsStorageItemTable": cucsStorageItemTable,
       "cucsStorageItemEntry": cucsStorageItemEntry,
       "cucsStorageItemInstanceId": cucsStorageItemInstanceId,
       "cucsStorageItemDn": cucsStorageItemDn,
       "cucsStorageItemRn": cucsStorageItemRn,
       "cucsStorageItemName": cucsStorageItemName,
       "cucsStorageItemSize": cucsStorageItemSize,
       "cucsStorageItemUsed": cucsStorageItemUsed,
       "cucsStorageItemOperState": cucsStorageItemOperState,
       "cucsStorageLocalDiskTable": cucsStorageLocalDiskTable,
       "cucsStorageLocalDiskEntry": cucsStorageLocalDiskEntry,
       "cucsStorageLocalDiskInstanceId": cucsStorageLocalDiskInstanceId,
       "cucsStorageLocalDiskDn": cucsStorageLocalDiskDn,
       "cucsStorageLocalDiskRn": cucsStorageLocalDiskRn,
       "cucsStorageLocalDiskBlockSize": cucsStorageLocalDiskBlockSize,
       "cucsStorageLocalDiskConnectionProtocol": cucsStorageLocalDiskConnectionProtocol,
       "cucsStorageLocalDiskId": cucsStorageLocalDiskId,
       "cucsStorageLocalDiskModel": cucsStorageLocalDiskModel,
       "cucsStorageLocalDiskNumberOfBlocks": cucsStorageLocalDiskNumberOfBlocks,
       "cucsStorageLocalDiskOperability": cucsStorageLocalDiskOperability,
       "cucsStorageLocalDiskPresence": cucsStorageLocalDiskPresence,
       "cucsStorageLocalDiskRevision": cucsStorageLocalDiskRevision,
       "cucsStorageLocalDiskSerial": cucsStorageLocalDiskSerial,
       "cucsStorageLocalDiskSize": cucsStorageLocalDiskSize,
       "cucsStorageLocalDiskVendor": cucsStorageLocalDiskVendor,
       "cucsStorageLocalDiskLc": cucsStorageLocalDiskLc,
       "cucsStorageLocalDiskOperQualifierReason": cucsStorageLocalDiskOperQualifierReason,
       "cucsStorageLocalDiskDeviceType": cucsStorageLocalDiskDeviceType,
       "cucsStorageLocalDiskDiskState": cucsStorageLocalDiskDiskState,
       "cucsStorageLocalDiskLinkSpeed": cucsStorageLocalDiskLinkSpeed,
       "cucsStorageLocalDiskPowerState": cucsStorageLocalDiskPowerState,
       "cucsStorageLocalDiskAdminAction": cucsStorageLocalDiskAdminAction,
       "cucsStorageLocalDiskAdminActionTrigger": cucsStorageLocalDiskAdminActionTrigger,
       "cucsStorageLocalDiskBootable": cucsStorageLocalDiskBootable,
       "cucsStorageLocalDiskConfigState": cucsStorageLocalDiskConfigState,
       "cucsStorageLocalDiskThermal": cucsStorageLocalDiskThermal,
       "cucsStorageLocalDiskAdminVirtualDriveId": cucsStorageLocalDiskAdminVirtualDriveId,
       "cucsStorageLocalDiskConfigCheckPoint": cucsStorageLocalDiskConfigCheckPoint,
       "cucsStorageLocalDiskConfigDefTable": cucsStorageLocalDiskConfigDefTable,
       "cucsStorageLocalDiskConfigDefEntry": cucsStorageLocalDiskConfigDefEntry,
       "cucsStorageLocalDiskConfigDefInstanceId": cucsStorageLocalDiskConfigDefInstanceId,
       "cucsStorageLocalDiskConfigDefDn": cucsStorageLocalDiskConfigDefDn,
       "cucsStorageLocalDiskConfigDefRn": cucsStorageLocalDiskConfigDefRn,
       "cucsStorageLocalDiskConfigDefDescr": cucsStorageLocalDiskConfigDefDescr,
       "cucsStorageLocalDiskConfigDefIntId": cucsStorageLocalDiskConfigDefIntId,
       "cucsStorageLocalDiskConfigDefMode": cucsStorageLocalDiskConfigDefMode,
       "cucsStorageLocalDiskConfigDefName": cucsStorageLocalDiskConfigDefName,
       "cucsStorageLocalDiskConfigDefProtectConfig": cucsStorageLocalDiskConfigDefProtectConfig,
       "cucsStorageLocalDiskConfigDefPolicyLevel": cucsStorageLocalDiskConfigDefPolicyLevel,
       "cucsStorageLocalDiskConfigDefPolicyOwner": cucsStorageLocalDiskConfigDefPolicyOwner,
       "cucsStorageLocalDiskConfigDefFlexFlashRAIDReportingState": cucsStorageLocalDiskConfigDefFlexFlashRAIDReportingState,
       "cucsStorageLocalDiskConfigDefFlexFlashState": cucsStorageLocalDiskConfigDefFlexFlashState,
       "cucsStorageLocalDiskConfigPolicyTable": cucsStorageLocalDiskConfigPolicyTable,
       "cucsStorageLocalDiskConfigPolicyEntry": cucsStorageLocalDiskConfigPolicyEntry,
       "cucsStorageLocalDiskConfigPolicyInstanceId": cucsStorageLocalDiskConfigPolicyInstanceId,
       "cucsStorageLocalDiskConfigPolicyDn": cucsStorageLocalDiskConfigPolicyDn,
       "cucsStorageLocalDiskConfigPolicyRn": cucsStorageLocalDiskConfigPolicyRn,
       "cucsStorageLocalDiskConfigPolicyDescr": cucsStorageLocalDiskConfigPolicyDescr,
       "cucsStorageLocalDiskConfigPolicyIntId": cucsStorageLocalDiskConfigPolicyIntId,
       "cucsStorageLocalDiskConfigPolicyMode": cucsStorageLocalDiskConfigPolicyMode,
       "cucsStorageLocalDiskConfigPolicyName": cucsStorageLocalDiskConfigPolicyName,
       "cucsStorageLocalDiskConfigPolicyProtectConfig": cucsStorageLocalDiskConfigPolicyProtectConfig,
       "cucsStorageLocalDiskConfigPolicyPolicyLevel": cucsStorageLocalDiskConfigPolicyPolicyLevel,
       "cucsStorageLocalDiskConfigPolicyPolicyOwner": cucsStorageLocalDiskConfigPolicyPolicyOwner,
       "cucsStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState": cucsStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState,
       "cucsStorageLocalDiskConfigPolicyFlexFlashState": cucsStorageLocalDiskConfigPolicyFlexFlashState,
       "cucsStorageLocalDiskPartitionTable": cucsStorageLocalDiskPartitionTable,
       "cucsStorageLocalDiskPartitionEntry": cucsStorageLocalDiskPartitionEntry,
       "cucsStorageLocalDiskPartitionInstanceId": cucsStorageLocalDiskPartitionInstanceId,
       "cucsStorageLocalDiskPartitionDn": cucsStorageLocalDiskPartitionDn,
       "cucsStorageLocalDiskPartitionRn": cucsStorageLocalDiskPartitionRn,
       "cucsStorageLocalDiskPartitionName": cucsStorageLocalDiskPartitionName,
       "cucsStorageLocalDiskPartitionSize": cucsStorageLocalDiskPartitionSize,
       "cucsStorageLocalDiskPartitionType": cucsStorageLocalDiskPartitionType,
       "cucsStorageLocalDiskPartitionBootable": cucsStorageLocalDiskPartitionBootable,
       "cucsStorageLocalDiskPartitionId": cucsStorageLocalDiskPartitionId,
       "cucsStorageLocalDiskPartitionPartitionEnd": cucsStorageLocalDiskPartitionPartitionEnd,
       "cucsStorageLocalDiskPartitionPartitionStart": cucsStorageLocalDiskPartitionPartitionStart,
       "cucsStorageLocalDiskPartitionRawTypeDesc": cucsStorageLocalDiskPartitionRawTypeDesc,
       "cucsStorageLocalLunTable": cucsStorageLocalLunTable,
       "cucsStorageLocalLunEntry": cucsStorageLocalLunEntry,
       "cucsStorageLocalLunInstanceId": cucsStorageLocalLunInstanceId,
       "cucsStorageLocalLunDn": cucsStorageLocalLunDn,
       "cucsStorageLocalLunRn": cucsStorageLocalLunRn,
       "cucsStorageLocalLunBlockSize": cucsStorageLocalLunBlockSize,
       "cucsStorageLocalLunConnectionProtocol": cucsStorageLocalLunConnectionProtocol,
       "cucsStorageLocalLunId": cucsStorageLocalLunId,
       "cucsStorageLocalLunModel": cucsStorageLocalLunModel,
       "cucsStorageLocalLunNumberOfBlocks": cucsStorageLocalLunNumberOfBlocks,
       "cucsStorageLocalLunOperability": cucsStorageLocalLunOperability,
       "cucsStorageLocalLunPresence": cucsStorageLocalLunPresence,
       "cucsStorageLocalLunRevision": cucsStorageLocalLunRevision,
       "cucsStorageLocalLunSerial": cucsStorageLocalLunSerial,
       "cucsStorageLocalLunSize": cucsStorageLocalLunSize,
       "cucsStorageLocalLunType": cucsStorageLocalLunType,
       "cucsStorageLocalLunVendor": cucsStorageLocalLunVendor,
       "cucsStorageLocalLunLc": cucsStorageLocalLunLc,
       "cucsStorageLocalLunOperQualifierReason": cucsStorageLocalLunOperQualifierReason,
       "cucsStorageLunDiskTable": cucsStorageLunDiskTable,
       "cucsStorageLunDiskEntry": cucsStorageLunDiskEntry,
       "cucsStorageLunDiskInstanceId": cucsStorageLunDiskInstanceId,
       "cucsStorageLunDiskDn": cucsStorageLunDiskDn,
       "cucsStorageLunDiskRn": cucsStorageLunDiskRn,
       "cucsStorageLunDiskId": cucsStorageLunDiskId,
       "cucsStorageQualTable": cucsStorageQualTable,
       "cucsStorageQualEntry": cucsStorageQualEntry,
       "cucsStorageQualInstanceId": cucsStorageQualInstanceId,
       "cucsStorageQualDn": cucsStorageQualDn,
       "cucsStorageQualRn": cucsStorageQualRn,
       "cucsStorageQualBlockSize": cucsStorageQualBlockSize,
       "cucsStorageQualMaxCap": cucsStorageQualMaxCap,
       "cucsStorageQualMinCap": cucsStorageQualMinCap,
       "cucsStorageQualNumberOfBlocks": cucsStorageQualNumberOfBlocks,
       "cucsStorageQualPerDiskCap": cucsStorageQualPerDiskCap,
       "cucsStorageQualUnits": cucsStorageQualUnits,
       "cucsStorageQualDiskless": cucsStorageQualDiskless,
       "cucsStorageQualNumberOfFlexFlashCards": cucsStorageQualNumberOfFlexFlashCards,
       "cucsStorageQualDiskType": cucsStorageQualDiskType,
       "cucsStorageRaidBatteryTable": cucsStorageRaidBatteryTable,
       "cucsStorageRaidBatteryEntry": cucsStorageRaidBatteryEntry,
       "cucsStorageRaidBatteryInstanceId": cucsStorageRaidBatteryInstanceId,
       "cucsStorageRaidBatteryDn": cucsStorageRaidBatteryDn,
       "cucsStorageRaidBatteryRn": cucsStorageRaidBatteryRn,
       "cucsStorageRaidBatteryBlockSize": cucsStorageRaidBatteryBlockSize,
       "cucsStorageRaidBatteryConnectionProtocol": cucsStorageRaidBatteryConnectionProtocol,
       "cucsStorageRaidBatteryId": cucsStorageRaidBatteryId,
       "cucsStorageRaidBatteryModel": cucsStorageRaidBatteryModel,
       "cucsStorageRaidBatteryNumberOfBlocks": cucsStorageRaidBatteryNumberOfBlocks,
       "cucsStorageRaidBatteryOperability": cucsStorageRaidBatteryOperability,
       "cucsStorageRaidBatteryPresence": cucsStorageRaidBatteryPresence,
       "cucsStorageRaidBatteryRevision": cucsStorageRaidBatteryRevision,
       "cucsStorageRaidBatterySerial": cucsStorageRaidBatterySerial,
       "cucsStorageRaidBatterySize": cucsStorageRaidBatterySize,
       "cucsStorageRaidBatteryVendor": cucsStorageRaidBatteryVendor,
       "cucsStorageRaidBatteryOperQualifierReason": cucsStorageRaidBatteryOperQualifierReason,
       "cucsStorageRaidBatteryBatteryType": cucsStorageRaidBatteryBatteryType,
       "cucsStorageRaidBatteryCapacityPercentage": cucsStorageRaidBatteryCapacityPercentage,
       "cucsStorageRaidBatteryOperabilityQualifier": cucsStorageRaidBatteryOperabilityQualifier,
       "cucsStorageRaidBatteryOperabilityQualifierReason": cucsStorageRaidBatteryOperabilityQualifierReason,
       "cucsStorageRaidBatteryTemperature": cucsStorageRaidBatteryTemperature,
       "cucsStorageRaidBatteryBbuStatus": cucsStorageRaidBatteryBbuStatus,
       "cucsStorageRaidBatteryLc": cucsStorageRaidBatteryLc,
       "cucsStorageRaidBatteryLearnCycleRequested": cucsStorageRaidBatteryLearnCycleRequested,
       "cucsStorageRaidBatteryLearnMode": cucsStorageRaidBatteryLearnMode,
       "cucsStorageRaidBatteryNextLearnCycleTs": cucsStorageRaidBatteryNextLearnCycleTs,
       "cucsStorageEnclosureTable": cucsStorageEnclosureTable,
       "cucsStorageEnclosureEntry": cucsStorageEnclosureEntry,
       "cucsStorageEnclosureInstanceId": cucsStorageEnclosureInstanceId,
       "cucsStorageEnclosureDn": cucsStorageEnclosureDn,
       "cucsStorageEnclosureRn": cucsStorageEnclosureRn,
       "cucsStorageEnclosureId": cucsStorageEnclosureId,
       "cucsStorageEnclosureModel": cucsStorageEnclosureModel,
       "cucsStorageEnclosureNumSlots": cucsStorageEnclosureNumSlots,
       "cucsStorageEnclosureRevision": cucsStorageEnclosureRevision,
       "cucsStorageEnclosureSerial": cucsStorageEnclosureSerial,
       "cucsStorageEnclosureVendor": cucsStorageEnclosureVendor,
       "cucsStorageEnclosureLc": cucsStorageEnclosureLc,
       "cucsStorageEnclosureDescr": cucsStorageEnclosureDescr,
       "cucsStorageLocalDiskSlotEpTable": cucsStorageLocalDiskSlotEpTable,
       "cucsStorageLocalDiskSlotEpEntry": cucsStorageLocalDiskSlotEpEntry,
       "cucsStorageLocalDiskSlotEpInstanceId": cucsStorageLocalDiskSlotEpInstanceId,
       "cucsStorageLocalDiskSlotEpDn": cucsStorageLocalDiskSlotEpDn,
       "cucsStorageLocalDiskSlotEpRn": cucsStorageLocalDiskSlotEpRn,
       "cucsStorageLocalDiskSlotEpConfiguration": cucsStorageLocalDiskSlotEpConfiguration,
       "cucsStorageLocalDiskSlotEpId": cucsStorageLocalDiskSlotEpId,
       "cucsStorageLocalDiskSlotEpOperability": cucsStorageLocalDiskSlotEpOperability,
       "cucsStorageLocalDiskSlotEpPeerDn": cucsStorageLocalDiskSlotEpPeerDn,
       "cucsStorageLocalDiskSlotEpPresence": cucsStorageLocalDiskSlotEpPresence,
       "cucsStorageLocalDiskSlotEpOperQualifierReason": cucsStorageLocalDiskSlotEpOperQualifierReason,
       "cucsStorageAuthKeyTable": cucsStorageAuthKeyTable,
       "cucsStorageAuthKeyEntry": cucsStorageAuthKeyEntry,
       "cucsStorageAuthKeyInstanceId": cucsStorageAuthKeyInstanceId,
       "cucsStorageAuthKeyDn": cucsStorageAuthKeyDn,
       "cucsStorageAuthKeyRn": cucsStorageAuthKeyRn,
       "cucsStorageAuthKeyDescr": cucsStorageAuthKeyDescr,
       "cucsStorageAuthKeyIntId": cucsStorageAuthKeyIntId,
       "cucsStorageAuthKeyName": cucsStorageAuthKeyName,
       "cucsStorageAuthKeyPassword": cucsStorageAuthKeyPassword,
       "cucsStorageAuthKeyPolicyLevel": cucsStorageAuthKeyPolicyLevel,
       "cucsStorageAuthKeyPolicyOwner": cucsStorageAuthKeyPolicyOwner,
       "cucsStorageAuthKeyType": cucsStorageAuthKeyType,
       "cucsStorageAuthKeyUserId": cucsStorageAuthKeyUserId,
       "cucsStorageConnectionDefTable": cucsStorageConnectionDefTable,
       "cucsStorageConnectionDefEntry": cucsStorageConnectionDefEntry,
       "cucsStorageConnectionDefInstanceId": cucsStorageConnectionDefInstanceId,
       "cucsStorageConnectionDefDn": cucsStorageConnectionDefDn,
       "cucsStorageConnectionDefRn": cucsStorageConnectionDefRn,
       "cucsStorageConnectionDefDescr": cucsStorageConnectionDefDescr,
       "cucsStorageConnectionDefIntId": cucsStorageConnectionDefIntId,
       "cucsStorageConnectionDefName": cucsStorageConnectionDefName,
       "cucsStorageConnectionDefOperState": cucsStorageConnectionDefOperState,
       "cucsStorageConnectionDefPolicyLevel": cucsStorageConnectionDefPolicyLevel,
       "cucsStorageConnectionDefPolicyOwner": cucsStorageConnectionDefPolicyOwner,
       "cucsStorageConnectionDefZoningType": cucsStorageConnectionDefZoningType,
       "cucsStorageConnectionPolicyTable": cucsStorageConnectionPolicyTable,
       "cucsStorageConnectionPolicyEntry": cucsStorageConnectionPolicyEntry,
       "cucsStorageConnectionPolicyInstanceId": cucsStorageConnectionPolicyInstanceId,
       "cucsStorageConnectionPolicyDn": cucsStorageConnectionPolicyDn,
       "cucsStorageConnectionPolicyRn": cucsStorageConnectionPolicyRn,
       "cucsStorageConnectionPolicyDescr": cucsStorageConnectionPolicyDescr,
       "cucsStorageConnectionPolicyIntId": cucsStorageConnectionPolicyIntId,
       "cucsStorageConnectionPolicyName": cucsStorageConnectionPolicyName,
       "cucsStorageConnectionPolicyOperState": cucsStorageConnectionPolicyOperState,
       "cucsStorageConnectionPolicyPolicyLevel": cucsStorageConnectionPolicyPolicyLevel,
       "cucsStorageConnectionPolicyPolicyOwner": cucsStorageConnectionPolicyPolicyOwner,
       "cucsStorageConnectionPolicyZoningType": cucsStorageConnectionPolicyZoningType,
       "cucsStorageDomainEpTable": cucsStorageDomainEpTable,
       "cucsStorageDomainEpEntry": cucsStorageDomainEpEntry,
       "cucsStorageDomainEpInstanceId": cucsStorageDomainEpInstanceId,
       "cucsStorageDomainEpDn": cucsStorageDomainEpDn,
       "cucsStorageDomainEpRn": cucsStorageDomainEpRn,
       "cucsStorageEpUserTable": cucsStorageEpUserTable,
       "cucsStorageEpUserEntry": cucsStorageEpUserEntry,
       "cucsStorageEpUserInstanceId": cucsStorageEpUserInstanceId,
       "cucsStorageEpUserDn": cucsStorageEpUserDn,
       "cucsStorageEpUserRn": cucsStorageEpUserRn,
       "cucsStorageEpUserConfigState": cucsStorageEpUserConfigState,
       "cucsStorageEpUserConfigStatusMessage": cucsStorageEpUserConfigStatusMessage,
       "cucsStorageEpUserDescr": cucsStorageEpUserDescr,
       "cucsStorageEpUserDomain": cucsStorageEpUserDomain,
       "cucsStorageEpUserName": cucsStorageEpUserName,
       "cucsStorageEpUserPriv": cucsStorageEpUserPriv,
       "cucsStorageEpUserPwd": cucsStorageEpUserPwd,
       "cucsStorageEpUserPwdSet": cucsStorageEpUserPwdSet,
       "cucsStorageEtherIfTable": cucsStorageEtherIfTable,
       "cucsStorageEtherIfEntry": cucsStorageEtherIfEntry,
       "cucsStorageEtherIfInstanceId": cucsStorageEtherIfInstanceId,
       "cucsStorageEtherIfDn": cucsStorageEtherIfDn,
       "cucsStorageEtherIfRn": cucsStorageEtherIfRn,
       "cucsStorageEtherIfName": cucsStorageEtherIfName,
       "cucsStorageEtherIfVlanType": cucsStorageEtherIfVlanType,
       "cucsStorageFcIfTable": cucsStorageFcIfTable,
       "cucsStorageFcIfEntry": cucsStorageFcIfEntry,
       "cucsStorageFcIfInstanceId": cucsStorageFcIfInstanceId,
       "cucsStorageFcIfDn": cucsStorageFcIfDn,
       "cucsStorageFcIfRn": cucsStorageFcIfRn,
       "cucsStorageFcIfName": cucsStorageFcIfName,
       "cucsStorageFcTargetEpTable": cucsStorageFcTargetEpTable,
       "cucsStorageFcTargetEpEntry": cucsStorageFcTargetEpEntry,
       "cucsStorageFcTargetEpInstanceId": cucsStorageFcTargetEpInstanceId,
       "cucsStorageFcTargetEpDn": cucsStorageFcTargetEpDn,
       "cucsStorageFcTargetEpRn": cucsStorageFcTargetEpRn,
       "cucsStorageFcTargetEpDescr": cucsStorageFcTargetEpDescr,
       "cucsStorageFcTargetEpPath": cucsStorageFcTargetEpPath,
       "cucsStorageFcTargetEpTargetwwpn": cucsStorageFcTargetEpTargetwwpn,
       "cucsStorageFcTargetIfTable": cucsStorageFcTargetIfTable,
       "cucsStorageFcTargetIfEntry": cucsStorageFcTargetIfEntry,
       "cucsStorageFcTargetIfInstanceId": cucsStorageFcTargetIfInstanceId,
       "cucsStorageFcTargetIfDn": cucsStorageFcTargetIfDn,
       "cucsStorageFcTargetIfRn": cucsStorageFcTargetIfRn,
       "cucsStorageFcTargetIfId": cucsStorageFcTargetIfId,
       "cucsStorageFcTargetIfProt": cucsStorageFcTargetIfProt,
       "cucsStorageIScsiTargetIfTable": cucsStorageIScsiTargetIfTable,
       "cucsStorageIScsiTargetIfEntry": cucsStorageIScsiTargetIfEntry,
       "cucsStorageIScsiTargetIfInstanceId": cucsStorageIScsiTargetIfInstanceId,
       "cucsStorageIScsiTargetIfDn": cucsStorageIScsiTargetIfDn,
       "cucsStorageIScsiTargetIfRn": cucsStorageIScsiTargetIfRn,
       "cucsStorageIScsiTargetIfName": cucsStorageIScsiTargetIfName,
       "cucsStorageIScsiTargetIfProt": cucsStorageIScsiTargetIfProt,
       "cucsStorageIniGroupTable": cucsStorageIniGroupTable,
       "cucsStorageIniGroupEntry": cucsStorageIniGroupEntry,
       "cucsStorageIniGroupInstanceId": cucsStorageIniGroupInstanceId,
       "cucsStorageIniGroupDn": cucsStorageIniGroupDn,
       "cucsStorageIniGroupRn": cucsStorageIniGroupRn,
       "cucsStorageIniGroupDescr": cucsStorageIniGroupDescr,
       "cucsStorageIniGroupGroupPolicyName": cucsStorageIniGroupGroupPolicyName,
       "cucsStorageIniGroupIntId": cucsStorageIniGroupIntId,
       "cucsStorageIniGroupName": cucsStorageIniGroupName,
       "cucsStorageIniGroupOperProtocol": cucsStorageIniGroupOperProtocol,
       "cucsStorageIniGroupOwner": cucsStorageIniGroupOwner,
       "cucsStorageIniGroupPolicyLevel": cucsStorageIniGroupPolicyLevel,
       "cucsStorageIniGroupPolicyName": cucsStorageIniGroupPolicyName,
       "cucsStorageIniGroupPolicyOwner": cucsStorageIniGroupPolicyOwner,
       "cucsStorageIniGroupProtocol": cucsStorageIniGroupProtocol,
       "cucsStorageIniGroupRmtDiskCfgName": cucsStorageIniGroupRmtDiskCfgName,
       "cucsStorageIniGroupOperState": cucsStorageIniGroupOperState,
       "cucsStorageInitiatorTable": cucsStorageInitiatorTable,
       "cucsStorageInitiatorEntry": cucsStorageInitiatorEntry,
       "cucsStorageInitiatorInstanceId": cucsStorageInitiatorInstanceId,
       "cucsStorageInitiatorDn": cucsStorageInitiatorDn,
       "cucsStorageInitiatorRn": cucsStorageInitiatorRn,
       "cucsStorageInitiatorDescr": cucsStorageInitiatorDescr,
       "cucsStorageInitiatorIntId": cucsStorageInitiatorIntId,
       "cucsStorageInitiatorName": cucsStorageInitiatorName,
       "cucsStorageInitiatorOperState": cucsStorageInitiatorOperState,
       "cucsStorageInitiatorPolicyLevel": cucsStorageInitiatorPolicyLevel,
       "cucsStorageInitiatorPolicyOwner": cucsStorageInitiatorPolicyOwner,
       "cucsStorageInitiatorDuplicateTarget": cucsStorageInitiatorDuplicateTarget,
       "cucsStorageNodeEpTable": cucsStorageNodeEpTable,
       "cucsStorageNodeEpEntry": cucsStorageNodeEpEntry,
       "cucsStorageNodeEpInstanceId": cucsStorageNodeEpInstanceId,
       "cucsStorageNodeEpDn": cucsStorageNodeEpDn,
       "cucsStorageNodeEpRn": cucsStorageNodeEpRn,
       "cucsStorageNodeEpEpDn": cucsStorageNodeEpEpDn,
       "cucsStorageNodeEpId": cucsStorageNodeEpId,
       "cucsStorageSystemTable": cucsStorageSystemTable,
       "cucsStorageSystemEntry": cucsStorageSystemEntry,
       "cucsStorageSystemInstanceId": cucsStorageSystemInstanceId,
       "cucsStorageSystemDn": cucsStorageSystemDn,
       "cucsStorageSystemRn": cucsStorageSystemRn,
       "cucsStorageSystemFsmDescr": cucsStorageSystemFsmDescr,
       "cucsStorageSystemFsmPrev": cucsStorageSystemFsmPrev,
       "cucsStorageSystemFsmProgr": cucsStorageSystemFsmProgr,
       "cucsStorageSystemFsmRmtInvErrCode": cucsStorageSystemFsmRmtInvErrCode,
       "cucsStorageSystemFsmRmtInvErrDescr": cucsStorageSystemFsmRmtInvErrDescr,
       "cucsStorageSystemFsmRmtInvRslt": cucsStorageSystemFsmRmtInvRslt,
       "cucsStorageSystemFsmStageDescr": cucsStorageSystemFsmStageDescr,
       "cucsStorageSystemFsmStamp": cucsStorageSystemFsmStamp,
       "cucsStorageSystemFsmStatus": cucsStorageSystemFsmStatus,
       "cucsStorageSystemFsmTry": cucsStorageSystemFsmTry,
       "cucsStorageSystemId": cucsStorageSystemId,
       "cucsStorageSystemName": cucsStorageSystemName,
       "cucsStorageSystemFsmTable": cucsStorageSystemFsmTable,
       "cucsStorageSystemFsmEntry": cucsStorageSystemFsmEntry,
       "cucsStorageSystemFsmInstanceId": cucsStorageSystemFsmInstanceId,
       "cucsStorageSystemFsmDn": cucsStorageSystemFsmDn,
       "cucsStorageSystemFsmRn": cucsStorageSystemFsmRn,
       "cucsStorageSystemFsmCompletionTime": cucsStorageSystemFsmCompletionTime,
       "cucsStorageSystemFsmCurrentFsm": cucsStorageSystemFsmCurrentFsm,
       "cucsStorageSystemFsmDescrData": cucsStorageSystemFsmDescrData,
       "cucsStorageSystemFsmFsmStatus": cucsStorageSystemFsmFsmStatus,
       "cucsStorageSystemFsmProgress": cucsStorageSystemFsmProgress,
       "cucsStorageSystemFsmRmtErrCode": cucsStorageSystemFsmRmtErrCode,
       "cucsStorageSystemFsmRmtErrDescr": cucsStorageSystemFsmRmtErrDescr,
       "cucsStorageSystemFsmRmtRslt": cucsStorageSystemFsmRmtRslt,
       "cucsStorageSystemFsmStageTable": cucsStorageSystemFsmStageTable,
       "cucsStorageSystemFsmStageEntry": cucsStorageSystemFsmStageEntry,
       "cucsStorageSystemFsmStageInstanceId": cucsStorageSystemFsmStageInstanceId,
       "cucsStorageSystemFsmStageDn": cucsStorageSystemFsmStageDn,
       "cucsStorageSystemFsmStageRn": cucsStorageSystemFsmStageRn,
       "cucsStorageSystemFsmStageDescrData": cucsStorageSystemFsmStageDescrData,
       "cucsStorageSystemFsmStageLastUpdateTime": cucsStorageSystemFsmStageLastUpdateTime,
       "cucsStorageSystemFsmStageName": cucsStorageSystemFsmStageName,
       "cucsStorageSystemFsmStageOrder": cucsStorageSystemFsmStageOrder,
       "cucsStorageSystemFsmStageRetry": cucsStorageSystemFsmStageRetry,
       "cucsStorageSystemFsmStageStageStatus": cucsStorageSystemFsmStageStageStatus,
       "cucsStorageSystemFsmTaskTable": cucsStorageSystemFsmTaskTable,
       "cucsStorageSystemFsmTaskEntry": cucsStorageSystemFsmTaskEntry,
       "cucsStorageSystemFsmTaskInstanceId": cucsStorageSystemFsmTaskInstanceId,
       "cucsStorageSystemFsmTaskDn": cucsStorageSystemFsmTaskDn,
       "cucsStorageSystemFsmTaskRn": cucsStorageSystemFsmTaskRn,
       "cucsStorageSystemFsmTaskCompletion": cucsStorageSystemFsmTaskCompletion,
       "cucsStorageSystemFsmTaskFlags": cucsStorageSystemFsmTaskFlags,
       "cucsStorageSystemFsmTaskItem": cucsStorageSystemFsmTaskItem,
       "cucsStorageSystemFsmTaskSeqId": cucsStorageSystemFsmTaskSeqId,
       "cucsStorageVirtualDriveTable": cucsStorageVirtualDriveTable,
       "cucsStorageVirtualDriveEntry": cucsStorageVirtualDriveEntry,
       "cucsStorageVirtualDriveInstanceId": cucsStorageVirtualDriveInstanceId,
       "cucsStorageVirtualDriveDn": cucsStorageVirtualDriveDn,
       "cucsStorageVirtualDriveRn": cucsStorageVirtualDriveRn,
       "cucsStorageVirtualDriveBlockSize": cucsStorageVirtualDriveBlockSize,
       "cucsStorageVirtualDriveConnectionProtocol": cucsStorageVirtualDriveConnectionProtocol,
       "cucsStorageVirtualDriveId": cucsStorageVirtualDriveId,
       "cucsStorageVirtualDriveModel": cucsStorageVirtualDriveModel,
       "cucsStorageVirtualDriveNumberOfBlocks": cucsStorageVirtualDriveNumberOfBlocks,
       "cucsStorageVirtualDriveOperQualifierReason": cucsStorageVirtualDriveOperQualifierReason,
       "cucsStorageVirtualDriveOperability": cucsStorageVirtualDriveOperability,
       "cucsStorageVirtualDrivePresence": cucsStorageVirtualDrivePresence,
       "cucsStorageVirtualDriveRevision": cucsStorageVirtualDriveRevision,
       "cucsStorageVirtualDriveSerial": cucsStorageVirtualDriveSerial,
       "cucsStorageVirtualDriveSize": cucsStorageVirtualDriveSize,
       "cucsStorageVirtualDriveType": cucsStorageVirtualDriveType,
       "cucsStorageVirtualDriveVendor": cucsStorageVirtualDriveVendor,
       "cucsStorageVirtualDriveAccessPolicy": cucsStorageVirtualDriveAccessPolicy,
       "cucsStorageVirtualDriveActualWriteCachePolicy": cucsStorageVirtualDriveActualWriteCachePolicy,
       "cucsStorageVirtualDriveBootable": cucsStorageVirtualDriveBootable,
       "cucsStorageVirtualDriveConfiguredWriteCachePolicy": cucsStorageVirtualDriveConfiguredWriteCachePolicy,
       "cucsStorageVirtualDriveDriveCache": cucsStorageVirtualDriveDriveCache,
       "cucsStorageVirtualDriveDriveState": cucsStorageVirtualDriveDriveState,
       "cucsStorageVirtualDriveIoPolicy": cucsStorageVirtualDriveIoPolicy,
       "cucsStorageVirtualDriveLc": cucsStorageVirtualDriveLc,
       "cucsStorageVirtualDriveReadPolicy": cucsStorageVirtualDriveReadPolicy,
       "cucsStorageVirtualDriveStripSize": cucsStorageVirtualDriveStripSize,
       "cucsStorageVirtualDriveAdminActionTrigger": cucsStorageVirtualDriveAdminActionTrigger,
       "cucsStorageVirtualDriveAdminName": cucsStorageVirtualDriveAdminName,
       "cucsStorageVirtualDriveAdminState": cucsStorageVirtualDriveAdminState,
       "cucsStorageVirtualDriveChangeQualifier": cucsStorageVirtualDriveChangeQualifier,
       "cucsStorageVirtualDriveConfigQualifierReason": cucsStorageVirtualDriveConfigQualifierReason,
       "cucsStorageVirtualDriveConfigState": cucsStorageVirtualDriveConfigState,
       "cucsStorageVirtualDriveDeployAction": cucsStorageVirtualDriveDeployAction,
       "cucsStorageVirtualDriveDescr": cucsStorageVirtualDriveDescr,
       "cucsStorageVirtualDriveLocale": cucsStorageVirtualDriveLocale,
       "cucsStorageVirtualDriveName": cucsStorageVirtualDriveName,
       "cucsStorageVirtualDriveOperDeviceId": cucsStorageVirtualDriveOperDeviceId,
       "cucsStorageVirtualDriveOperState": cucsStorageVirtualDriveOperState,
       "cucsStorageVirtualDriveUuid": cucsStorageVirtualDriveUuid,
       "cucsStorageVirtualDriveVendorUuid": cucsStorageVirtualDriveVendorUuid,
       "cucsStorageVirtualDriveAvailableSize": cucsStorageVirtualDriveAvailableSize,
       "cucsStorageVirtualDrivePnDn": cucsStorageVirtualDrivePnDn,
       "cucsStorageVirtualDriveRefDn": cucsStorageVirtualDriveRefDn,
       "cucsStorageVsanRefTable": cucsStorageVsanRefTable,
       "cucsStorageVsanRefEntry": cucsStorageVsanRefEntry,
       "cucsStorageVsanRefInstanceId": cucsStorageVsanRefInstanceId,
       "cucsStorageVsanRefDn": cucsStorageVsanRefDn,
       "cucsStorageVsanRefRn": cucsStorageVsanRefRn,
       "cucsStorageVsanRefConfigQualifier": cucsStorageVsanRefConfigQualifier,
       "cucsStorageVsanRefName": cucsStorageVsanRefName,
       "cucsStorageVsanRefOperVnetDn": cucsStorageVsanRefOperVnetDn,
       "cucsStorageVsanRefOperVnetName": cucsStorageVsanRefOperVnetName,
       "cucsStorageVsanRefSwitchId": cucsStorageVsanRefSwitchId,
       "cucsStorageVsanRefVnet": cucsStorageVsanRefVnet,
       "cucsStorageVsanRefZoningState": cucsStorageVsanRefZoningState,
       "cucsStorageTransportableFlashModuleTable": cucsStorageTransportableFlashModuleTable,
       "cucsStorageTransportableFlashModuleEntry": cucsStorageTransportableFlashModuleEntry,
       "cucsStorageTransportableFlashModuleInstanceId": cucsStorageTransportableFlashModuleInstanceId,
       "cucsStorageTransportableFlashModuleDn": cucsStorageTransportableFlashModuleDn,
       "cucsStorageTransportableFlashModuleRn": cucsStorageTransportableFlashModuleRn,
       "cucsStorageTransportableFlashModuleBlockSize": cucsStorageTransportableFlashModuleBlockSize,
       "cucsStorageTransportableFlashModuleConnectionProtocol": cucsStorageTransportableFlashModuleConnectionProtocol,
       "cucsStorageTransportableFlashModuleId": cucsStorageTransportableFlashModuleId,
       "cucsStorageTransportableFlashModuleModel": cucsStorageTransportableFlashModuleModel,
       "cucsStorageTransportableFlashModuleNumberOfBlocks": cucsStorageTransportableFlashModuleNumberOfBlocks,
       "cucsStorageTransportableFlashModuleOperQualifierReason": cucsStorageTransportableFlashModuleOperQualifierReason,
       "cucsStorageTransportableFlashModuleOperability": cucsStorageTransportableFlashModuleOperability,
       "cucsStorageTransportableFlashModulePresence": cucsStorageTransportableFlashModulePresence,
       "cucsStorageTransportableFlashModuleRevision": cucsStorageTransportableFlashModuleRevision,
       "cucsStorageTransportableFlashModuleSerial": cucsStorageTransportableFlashModuleSerial,
       "cucsStorageTransportableFlashModuleSize": cucsStorageTransportableFlashModuleSize,
       "cucsStorageTransportableFlashModuleVendor": cucsStorageTransportableFlashModuleVendor,
       "cucsStorageFlexFlashCardTable": cucsStorageFlexFlashCardTable,
       "cucsStorageFlexFlashCardEntry": cucsStorageFlexFlashCardEntry,
       "cucsStorageFlexFlashCardInstanceId": cucsStorageFlexFlashCardInstanceId,
       "cucsStorageFlexFlashCardDn": cucsStorageFlexFlashCardDn,
       "cucsStorageFlexFlashCardRn": cucsStorageFlexFlashCardRn,
       "cucsStorageFlexFlashCardBlockSize": cucsStorageFlexFlashCardBlockSize,
       "cucsStorageFlexFlashCardCardHealth": cucsStorageFlexFlashCardCardHealth,
       "cucsStorageFlexFlashCardCardMode": cucsStorageFlexFlashCardCardMode,
       "cucsStorageFlexFlashCardCardType": cucsStorageFlexFlashCardCardType,
       "cucsStorageFlexFlashCardConnectionProtocol": cucsStorageFlexFlashCardConnectionProtocol,
       "cucsStorageFlexFlashCardControllerIndex": cucsStorageFlexFlashCardControllerIndex,
       "cucsStorageFlexFlashCardId": cucsStorageFlexFlashCardId,
       "cucsStorageFlexFlashCardMfgDate": cucsStorageFlexFlashCardMfgDate,
       "cucsStorageFlexFlashCardMfgId": cucsStorageFlexFlashCardMfgId,
       "cucsStorageFlexFlashCardModel": cucsStorageFlexFlashCardModel,
       "cucsStorageFlexFlashCardNumberOfBlocks": cucsStorageFlexFlashCardNumberOfBlocks,
       "cucsStorageFlexFlashCardOemId": cucsStorageFlexFlashCardOemId,
       "cucsStorageFlexFlashCardOperQualifierReason": cucsStorageFlexFlashCardOperQualifierReason,
       "cucsStorageFlexFlashCardOperability": cucsStorageFlexFlashCardOperability,
       "cucsStorageFlexFlashCardPresence": cucsStorageFlexFlashCardPresence,
       "cucsStorageFlexFlashCardReadIOErrorCount": cucsStorageFlexFlashCardReadIOErrorCount,
       "cucsStorageFlexFlashCardRevision": cucsStorageFlexFlashCardRevision,
       "cucsStorageFlexFlashCardSerial": cucsStorageFlexFlashCardSerial,
       "cucsStorageFlexFlashCardSize": cucsStorageFlexFlashCardSize,
       "cucsStorageFlexFlashCardSlotNumber": cucsStorageFlexFlashCardSlotNumber,
       "cucsStorageFlexFlashCardVendor": cucsStorageFlexFlashCardVendor,
       "cucsStorageFlexFlashCardWriteEnable": cucsStorageFlexFlashCardWriteEnable,
       "cucsStorageFlexFlashCardWriteIOErrorCount": cucsStorageFlexFlashCardWriteIOErrorCount,
       "cucsStorageFlexFlashCardCardState": cucsStorageFlexFlashCardCardState,
       "cucsStorageFlexFlashCardCardSync": cucsStorageFlexFlashCardCardSync,
       "cucsStorageFlexFlashCardDrivesEnabled": cucsStorageFlexFlashCardDrivesEnabled,
       "cucsStorageFlexFlashCardPartitionCount": cucsStorageFlexFlashCardPartitionCount,
       "cucsStorageFlexFlashCardReadErrorThreshold": cucsStorageFlexFlashCardReadErrorThreshold,
       "cucsStorageFlexFlashCardSignature": cucsStorageFlexFlashCardSignature,
       "cucsStorageFlexFlashCardWriteErrorThreshold": cucsStorageFlexFlashCardWriteErrorThreshold,
       "cucsStorageFlexFlashControllerTable": cucsStorageFlexFlashControllerTable,
       "cucsStorageFlexFlashControllerEntry": cucsStorageFlexFlashControllerEntry,
       "cucsStorageFlexFlashControllerInstanceId": cucsStorageFlexFlashControllerInstanceId,
       "cucsStorageFlexFlashControllerDn": cucsStorageFlexFlashControllerDn,
       "cucsStorageFlexFlashControllerRn": cucsStorageFlexFlashControllerRn,
       "cucsStorageFlexFlashControllerControllerHealth": cucsStorageFlexFlashControllerControllerHealth,
       "cucsStorageFlexFlashControllerControllerState": cucsStorageFlexFlashControllerControllerState,
       "cucsStorageFlexFlashControllerFlexFlashType": cucsStorageFlexFlashControllerFlexFlashType,
       "cucsStorageFlexFlashControllerId": cucsStorageFlexFlashControllerId,
       "cucsStorageFlexFlashControllerModel": cucsStorageFlexFlashControllerModel,
       "cucsStorageFlexFlashControllerOperQualifierReason": cucsStorageFlexFlashControllerOperQualifierReason,
       "cucsStorageFlexFlashControllerOperState": cucsStorageFlexFlashControllerOperState,
       "cucsStorageFlexFlashControllerOperability": cucsStorageFlexFlashControllerOperability,
       "cucsStorageFlexFlashControllerPciAddr": cucsStorageFlexFlashControllerPciAddr,
       "cucsStorageFlexFlashControllerPciSlot": cucsStorageFlexFlashControllerPciSlot,
       "cucsStorageFlexFlashControllerPerf": cucsStorageFlexFlashControllerPerf,
       "cucsStorageFlexFlashControllerPhysicalDriveCount": cucsStorageFlexFlashControllerPhysicalDriveCount,
       "cucsStorageFlexFlashControllerPower": cucsStorageFlexFlashControllerPower,
       "cucsStorageFlexFlashControllerPresence": cucsStorageFlexFlashControllerPresence,
       "cucsStorageFlexFlashControllerPrimarySlotNumber": cucsStorageFlexFlashControllerPrimarySlotNumber,
       "cucsStorageFlexFlashControllerRaidSyncSupport": cucsStorageFlexFlashControllerRaidSyncSupport,
       "cucsStorageFlexFlashControllerReadErrorThreshold": cucsStorageFlexFlashControllerReadErrorThreshold,
       "cucsStorageFlexFlashControllerRevision": cucsStorageFlexFlashControllerRevision,
       "cucsStorageFlexFlashControllerSerial": cucsStorageFlexFlashControllerSerial,
       "cucsStorageFlexFlashControllerThermal": cucsStorageFlexFlashControllerThermal,
       "cucsStorageFlexFlashControllerType": cucsStorageFlexFlashControllerType,
       "cucsStorageFlexFlashControllerVendor": cucsStorageFlexFlashControllerVendor,
       "cucsStorageFlexFlashControllerVirtualDriveCount": cucsStorageFlexFlashControllerVirtualDriveCount,
       "cucsStorageFlexFlashControllerVoltage": cucsStorageFlexFlashControllerVoltage,
       "cucsStorageFlexFlashControllerWriteErrorThreshold": cucsStorageFlexFlashControllerWriteErrorThreshold,
       "cucsStorageFlexFlashControllerLocationDn": cucsStorageFlexFlashControllerLocationDn,
       "cucsStorageFlexFlashControllerAdminSlotNumber": cucsStorageFlexFlashControllerAdminSlotNumber,
       "cucsStorageFlexFlashControllerConfiguredMode": cucsStorageFlexFlashControllerConfiguredMode,
       "cucsStorageFlexFlashControllerFirmwareVersion": cucsStorageFlexFlashControllerFirmwareVersion,
       "cucsStorageFlexFlashControllerFsmDescr": cucsStorageFlexFlashControllerFsmDescr,
       "cucsStorageFlexFlashControllerFsmPrev": cucsStorageFlexFlashControllerFsmPrev,
       "cucsStorageFlexFlashControllerFsmProgr": cucsStorageFlexFlashControllerFsmProgr,
       "cucsStorageFlexFlashControllerFsmRmtInvErrCode": cucsStorageFlexFlashControllerFsmRmtInvErrCode,
       "cucsStorageFlexFlashControllerFsmRmtInvErrDescr": cucsStorageFlexFlashControllerFsmRmtInvErrDescr,
       "cucsStorageFlexFlashControllerFsmRmtInvRslt": cucsStorageFlexFlashControllerFsmRmtInvRslt,
       "cucsStorageFlexFlashControllerFsmStageDescr": cucsStorageFlexFlashControllerFsmStageDescr,
       "cucsStorageFlexFlashControllerFsmStamp": cucsStorageFlexFlashControllerFsmStamp,
       "cucsStorageFlexFlashControllerFsmStatus": cucsStorageFlexFlashControllerFsmStatus,
       "cucsStorageFlexFlashControllerFsmTry": cucsStorageFlexFlashControllerFsmTry,
       "cucsStorageFlexFlashControllerHasError": cucsStorageFlexFlashControllerHasError,
       "cucsStorageFlexFlashControllerIsCardMismatch": cucsStorageFlexFlashControllerIsCardMismatch,
       "cucsStorageFlexFlashControllerIsFormatFSMRunning": cucsStorageFlexFlashControllerIsFormatFSMRunning,
       "cucsStorageFlexFlashControllerOperatingMode": cucsStorageFlexFlashControllerOperatingMode,
       "cucsStorageFlexFlashControllerOperationRequest": cucsStorageFlexFlashControllerOperationRequest,
       "cucsStorageFlexFlashDriveTable": cucsStorageFlexFlashDriveTable,
       "cucsStorageFlexFlashDriveEntry": cucsStorageFlexFlashDriveEntry,
       "cucsStorageFlexFlashDriveInstanceId": cucsStorageFlexFlashDriveInstanceId,
       "cucsStorageFlexFlashDriveDn": cucsStorageFlexFlashDriveDn,
       "cucsStorageFlexFlashDriveRn": cucsStorageFlexFlashDriveRn,
       "cucsStorageFlexFlashDriveBlockSize": cucsStorageFlexFlashDriveBlockSize,
       "cucsStorageFlexFlashDriveConnectionProtocol": cucsStorageFlexFlashDriveConnectionProtocol,
       "cucsStorageFlexFlashDriveControllerIndex": cucsStorageFlexFlashDriveControllerIndex,
       "cucsStorageFlexFlashDriveDriveState": cucsStorageFlexFlashDriveDriveState,
       "cucsStorageFlexFlashDriveDriveType": cucsStorageFlexFlashDriveDriveType,
       "cucsStorageFlexFlashDriveId": cucsStorageFlexFlashDriveId,
       "cucsStorageFlexFlashDriveModel": cucsStorageFlexFlashDriveModel,
       "cucsStorageFlexFlashDriveName": cucsStorageFlexFlashDriveName,
       "cucsStorageFlexFlashDriveNumberOfBlocks": cucsStorageFlexFlashDriveNumberOfBlocks,
       "cucsStorageFlexFlashDriveOperQualifierReason": cucsStorageFlexFlashDriveOperQualifierReason,
       "cucsStorageFlexFlashDriveOperability": cucsStorageFlexFlashDriveOperability,
       "cucsStorageFlexFlashDrivePresence": cucsStorageFlexFlashDrivePresence,
       "cucsStorageFlexFlashDriveRevision": cucsStorageFlexFlashDriveRevision,
       "cucsStorageFlexFlashDriveSerial": cucsStorageFlexFlashDriveSerial,
       "cucsStorageFlexFlashDriveSize": cucsStorageFlexFlashDriveSize,
       "cucsStorageFlexFlashDriveSlotNumber": cucsStorageFlexFlashDriveSlotNumber,
       "cucsStorageFlexFlashDriveVendor": cucsStorageFlexFlashDriveVendor,
       "cucsStorageFlexFlashDriveVisible": cucsStorageFlexFlashDriveVisible,
       "cucsStorageFlexFlashDriveRemovable": cucsStorageFlexFlashDriveRemovable,
       "cucsStorageFlexFlashDriveRWType": cucsStorageFlexFlashDriveRWType,
       "cucsStorageFlexFlashDriveLastOperation": cucsStorageFlexFlashDriveLastOperation,
       "cucsStorageFlexFlashDriveOperationState": cucsStorageFlexFlashDriveOperationState,
       "cucsStorageFlexFlashVirtualDriveTable": cucsStorageFlexFlashVirtualDriveTable,
       "cucsStorageFlexFlashVirtualDriveEntry": cucsStorageFlexFlashVirtualDriveEntry,
       "cucsStorageFlexFlashVirtualDriveInstanceId": cucsStorageFlexFlashVirtualDriveInstanceId,
       "cucsStorageFlexFlashVirtualDriveDn": cucsStorageFlexFlashVirtualDriveDn,
       "cucsStorageFlexFlashVirtualDriveRn": cucsStorageFlexFlashVirtualDriveRn,
       "cucsStorageFlexFlashVirtualDriveBlockSize": cucsStorageFlexFlashVirtualDriveBlockSize,
       "cucsStorageFlexFlashVirtualDriveConnectionProtocol": cucsStorageFlexFlashVirtualDriveConnectionProtocol,
       "cucsStorageFlexFlashVirtualDriveId": cucsStorageFlexFlashVirtualDriveId,
       "cucsStorageFlexFlashVirtualDriveModel": cucsStorageFlexFlashVirtualDriveModel,
       "cucsStorageFlexFlashVirtualDriveNumberOfBlocks": cucsStorageFlexFlashVirtualDriveNumberOfBlocks,
       "cucsStorageFlexFlashVirtualDriveOperQualifierReason": cucsStorageFlexFlashVirtualDriveOperQualifierReason,
       "cucsStorageFlexFlashVirtualDriveOperability": cucsStorageFlexFlashVirtualDriveOperability,
       "cucsStorageFlexFlashVirtualDrivePresence": cucsStorageFlexFlashVirtualDrivePresence,
       "cucsStorageFlexFlashVirtualDriveRaidHealth": cucsStorageFlexFlashVirtualDriveRaidHealth,
       "cucsStorageFlexFlashVirtualDriveRaidState": cucsStorageFlexFlashVirtualDriveRaidState,
       "cucsStorageFlexFlashVirtualDriveRevision": cucsStorageFlexFlashVirtualDriveRevision,
       "cucsStorageFlexFlashVirtualDriveSerial": cucsStorageFlexFlashVirtualDriveSerial,
       "cucsStorageFlexFlashVirtualDriveSize": cucsStorageFlexFlashVirtualDriveSize,
       "cucsStorageFlexFlashVirtualDriveType": cucsStorageFlexFlashVirtualDriveType,
       "cucsStorageFlexFlashVirtualDriveVendor": cucsStorageFlexFlashVirtualDriveVendor,
       "cucsStorageOperationTable": cucsStorageOperationTable,
       "cucsStorageOperationEntry": cucsStorageOperationEntry,
       "cucsStorageOperationInstanceId": cucsStorageOperationInstanceId,
       "cucsStorageOperationDn": cucsStorageOperationDn,
       "cucsStorageOperationRn": cucsStorageOperationRn,
       "cucsStorageOperationEndTime": cucsStorageOperationEndTime,
       "cucsStorageOperationName": cucsStorageOperationName,
       "cucsStorageOperationOperState": cucsStorageOperationOperState,
       "cucsStorageOperationProgress": cucsStorageOperationProgress,
       "cucsStorageOperationStartTime": cucsStorageOperationStartTime,
       "cucsStorageOperationStatusDescr": cucsStorageOperationStatusDescr,
       "cucsStorageMezzFlashLifeTable": cucsStorageMezzFlashLifeTable,
       "cucsStorageMezzFlashLifeEntry": cucsStorageMezzFlashLifeEntry,
       "cucsStorageMezzFlashLifeInstanceId": cucsStorageMezzFlashLifeInstanceId,
       "cucsStorageMezzFlashLifeDn": cucsStorageMezzFlashLifeDn,
       "cucsStorageMezzFlashLifeRn": cucsStorageMezzFlashLifeRn,
       "cucsStorageMezzFlashLifeBlockSize": cucsStorageMezzFlashLifeBlockSize,
       "cucsStorageMezzFlashLifeConnectionProtocol": cucsStorageMezzFlashLifeConnectionProtocol,
       "cucsStorageMezzFlashLifeFlashPercentage": cucsStorageMezzFlashLifeFlashPercentage,
       "cucsStorageMezzFlashLifeFlashStatus": cucsStorageMezzFlashLifeFlashStatus,
       "cucsStorageMezzFlashLifeId": cucsStorageMezzFlashLifeId,
       "cucsStorageMezzFlashLifeModel": cucsStorageMezzFlashLifeModel,
       "cucsStorageMezzFlashLifeNumberOfBlocks": cucsStorageMezzFlashLifeNumberOfBlocks,
       "cucsStorageMezzFlashLifeOperQualifierReason": cucsStorageMezzFlashLifeOperQualifierReason,
       "cucsStorageMezzFlashLifeOperability": cucsStorageMezzFlashLifeOperability,
       "cucsStorageMezzFlashLifePresence": cucsStorageMezzFlashLifePresence,
       "cucsStorageMezzFlashLifeRevision": cucsStorageMezzFlashLifeRevision,
       "cucsStorageMezzFlashLifeSerial": cucsStorageMezzFlashLifeSerial,
       "cucsStorageMezzFlashLifeSize": cucsStorageMezzFlashLifeSize,
       "cucsStorageMezzFlashLifeVendor": cucsStorageMezzFlashLifeVendor,
       "cucsStorageFlexFlashControllerFsmTable": cucsStorageFlexFlashControllerFsmTable,
       "cucsStorageFlexFlashControllerFsmEntry": cucsStorageFlexFlashControllerFsmEntry,
       "cucsStorageFlexFlashControllerFsmInstanceId": cucsStorageFlexFlashControllerFsmInstanceId,
       "cucsStorageFlexFlashControllerFsmDn": cucsStorageFlexFlashControllerFsmDn,
       "cucsStorageFlexFlashControllerFsmRn": cucsStorageFlexFlashControllerFsmRn,
       "cucsStorageFlexFlashControllerFsmCompletionTime": cucsStorageFlexFlashControllerFsmCompletionTime,
       "cucsStorageFlexFlashControllerFsmCurrentFsm": cucsStorageFlexFlashControllerFsmCurrentFsm,
       "cucsStorageFlexFlashControllerFsmDescrData": cucsStorageFlexFlashControllerFsmDescrData,
       "cucsStorageFlexFlashControllerFsmFsmStatus": cucsStorageFlexFlashControllerFsmFsmStatus,
       "cucsStorageFlexFlashControllerFsmProgress": cucsStorageFlexFlashControllerFsmProgress,
       "cucsStorageFlexFlashControllerFsmRmtErrCode": cucsStorageFlexFlashControllerFsmRmtErrCode,
       "cucsStorageFlexFlashControllerFsmRmtErrDescr": cucsStorageFlexFlashControllerFsmRmtErrDescr,
       "cucsStorageFlexFlashControllerFsmRmtRslt": cucsStorageFlexFlashControllerFsmRmtRslt,
       "cucsStorageFlexFlashControllerFsmStageTable": cucsStorageFlexFlashControllerFsmStageTable,
       "cucsStorageFlexFlashControllerFsmStageEntry": cucsStorageFlexFlashControllerFsmStageEntry,
       "cucsStorageFlexFlashControllerFsmStageInstanceId": cucsStorageFlexFlashControllerFsmStageInstanceId,
       "cucsStorageFlexFlashControllerFsmStageDn": cucsStorageFlexFlashControllerFsmStageDn,
       "cucsStorageFlexFlashControllerFsmStageRn": cucsStorageFlexFlashControllerFsmStageRn,
       "cucsStorageFlexFlashControllerFsmStageDescrData": cucsStorageFlexFlashControllerFsmStageDescrData,
       "cucsStorageFlexFlashControllerFsmStageLastUpdateTime": cucsStorageFlexFlashControllerFsmStageLastUpdateTime,
       "cucsStorageFlexFlashControllerFsmStageName": cucsStorageFlexFlashControllerFsmStageName,
       "cucsStorageFlexFlashControllerFsmStageOrder": cucsStorageFlexFlashControllerFsmStageOrder,
       "cucsStorageFlexFlashControllerFsmStageRetry": cucsStorageFlexFlashControllerFsmStageRetry,
       "cucsStorageFlexFlashControllerFsmStageStageStatus": cucsStorageFlexFlashControllerFsmStageStageStatus,
       "cucsStorageFlexFlashControllerFsmTaskTable": cucsStorageFlexFlashControllerFsmTaskTable,
       "cucsStorageFlexFlashControllerFsmTaskEntry": cucsStorageFlexFlashControllerFsmTaskEntry,
       "cucsStorageFlexFlashControllerFsmTaskInstanceId": cucsStorageFlexFlashControllerFsmTaskInstanceId,
       "cucsStorageFlexFlashControllerFsmTaskDn": cucsStorageFlexFlashControllerFsmTaskDn,
       "cucsStorageFlexFlashControllerFsmTaskRn": cucsStorageFlexFlashControllerFsmTaskRn,
       "cucsStorageFlexFlashControllerFsmTaskCompletion": cucsStorageFlexFlashControllerFsmTaskCompletion,
       "cucsStorageFlexFlashControllerFsmTaskFlags": cucsStorageFlexFlashControllerFsmTaskFlags,
       "cucsStorageFlexFlashControllerFsmTaskItem": cucsStorageFlexFlashControllerFsmTaskItem,
       "cucsStorageFlexFlashControllerFsmTaskSeqId": cucsStorageFlexFlashControllerFsmTaskSeqId,
       "cucsStorageDiskEnvStatsTable": cucsStorageDiskEnvStatsTable,
       "cucsStorageDiskEnvStatsEntry": cucsStorageDiskEnvStatsEntry,
       "cucsStorageDiskEnvStatsInstanceId": cucsStorageDiskEnvStatsInstanceId,
       "cucsStorageDiskEnvStatsDn": cucsStorageDiskEnvStatsDn,
       "cucsStorageDiskEnvStatsRn": cucsStorageDiskEnvStatsRn,
       "cucsStorageDiskEnvStatsIntervals": cucsStorageDiskEnvStatsIntervals,
       "cucsStorageDiskEnvStatsSuspect": cucsStorageDiskEnvStatsSuspect,
       "cucsStorageDiskEnvStatsTemperature": cucsStorageDiskEnvStatsTemperature,
       "cucsStorageDiskEnvStatsTemperatureAvg": cucsStorageDiskEnvStatsTemperatureAvg,
       "cucsStorageDiskEnvStatsTemperatureMax": cucsStorageDiskEnvStatsTemperatureMax,
       "cucsStorageDiskEnvStatsTemperatureMin": cucsStorageDiskEnvStatsTemperatureMin,
       "cucsStorageDiskEnvStatsThresholded": cucsStorageDiskEnvStatsThresholded,
       "cucsStorageDiskEnvStatsTimeCollected": cucsStorageDiskEnvStatsTimeCollected,
       "cucsStorageDiskEnvStatsUpdate": cucsStorageDiskEnvStatsUpdate,
       "cucsStorageDiskEnvStatsWearPercentage": cucsStorageDiskEnvStatsWearPercentage,
       "cucsStorageDiskEnvStatsWearPercentageAvg": cucsStorageDiskEnvStatsWearPercentageAvg,
       "cucsStorageDiskEnvStatsWearPercentageMax": cucsStorageDiskEnvStatsWearPercentageMax,
       "cucsStorageDiskEnvStatsWearPercentageMin": cucsStorageDiskEnvStatsWearPercentageMin,
       "cucsStorageDiskEnvStatsHistTable": cucsStorageDiskEnvStatsHistTable,
       "cucsStorageDiskEnvStatsHistEntry": cucsStorageDiskEnvStatsHistEntry,
       "cucsStorageDiskEnvStatsHistInstanceId": cucsStorageDiskEnvStatsHistInstanceId,
       "cucsStorageDiskEnvStatsHistDn": cucsStorageDiskEnvStatsHistDn,
       "cucsStorageDiskEnvStatsHistRn": cucsStorageDiskEnvStatsHistRn,
       "cucsStorageDiskEnvStatsHistId": cucsStorageDiskEnvStatsHistId,
       "cucsStorageDiskEnvStatsHistMostRecent": cucsStorageDiskEnvStatsHistMostRecent,
       "cucsStorageDiskEnvStatsHistSuspect": cucsStorageDiskEnvStatsHistSuspect,
       "cucsStorageDiskEnvStatsHistTemperature": cucsStorageDiskEnvStatsHistTemperature,
       "cucsStorageDiskEnvStatsHistTemperatureAvg": cucsStorageDiskEnvStatsHistTemperatureAvg,
       "cucsStorageDiskEnvStatsHistTemperatureMax": cucsStorageDiskEnvStatsHistTemperatureMax,
       "cucsStorageDiskEnvStatsHistTemperatureMin": cucsStorageDiskEnvStatsHistTemperatureMin,
       "cucsStorageDiskEnvStatsHistThresholded": cucsStorageDiskEnvStatsHistThresholded,
       "cucsStorageDiskEnvStatsHistTimeCollected": cucsStorageDiskEnvStatsHistTimeCollected,
       "cucsStorageDiskEnvStatsHistWearPercentage": cucsStorageDiskEnvStatsHistWearPercentage,
       "cucsStorageDiskEnvStatsHistWearPercentageAvg": cucsStorageDiskEnvStatsHistWearPercentageAvg,
       "cucsStorageDiskEnvStatsHistWearPercentageMax": cucsStorageDiskEnvStatsHistWearPercentageMax,
       "cucsStorageDiskEnvStatsHistWearPercentageMin": cucsStorageDiskEnvStatsHistWearPercentageMin,
       "cucsStorageLunResourceSelectionLogTable": cucsStorageLunResourceSelectionLogTable,
       "cucsStorageLunResourceSelectionLogEntry": cucsStorageLunResourceSelectionLogEntry,
       "cucsStorageLunResourceSelectionLogInstanceId": cucsStorageLunResourceSelectionLogInstanceId,
       "cucsStorageLunResourceSelectionLogDn": cucsStorageLunResourceSelectionLogDn,
       "cucsStorageLunResourceSelectionLogRn": cucsStorageLunResourceSelectionLogRn,
       "cucsStorageLunResourceSelectionLogDecisionType": cucsStorageLunResourceSelectionLogDecisionType,
       "cucsStorageLunResourceSelectionLogDescr": cucsStorageLunResourceSelectionLogDescr,
       "cucsStorageLunResourceSelectionLogOrder": cucsStorageLunResourceSelectionLogOrder,
       "cucsStorageLunResourceSelectionLogResult": cucsStorageLunResourceSelectionLogResult,
       "cucsStorageLunResourceSelectionLogTimeStamp": cucsStorageLunResourceSelectionLogTimeStamp,
       "cucsStorageSasExpanderTable": cucsStorageSasExpanderTable,
       "cucsStorageSasExpanderEntry": cucsStorageSasExpanderEntry,
       "cucsStorageSasExpanderInstanceId": cucsStorageSasExpanderInstanceId,
       "cucsStorageSasExpanderDn": cucsStorageSasExpanderDn,
       "cucsStorageSasExpanderRn": cucsStorageSasExpanderRn,
       "cucsStorageSasExpanderId": cucsStorageSasExpanderId,
       "cucsStorageSasExpanderLocationDn": cucsStorageSasExpanderLocationDn,
       "cucsStorageSasExpanderModel": cucsStorageSasExpanderModel,
       "cucsStorageSasExpanderOperQualifierReason": cucsStorageSasExpanderOperQualifierReason,
       "cucsStorageSasExpanderOperState": cucsStorageSasExpanderOperState,
       "cucsStorageSasExpanderOperability": cucsStorageSasExpanderOperability,
       "cucsStorageSasExpanderPerf": cucsStorageSasExpanderPerf,
       "cucsStorageSasExpanderPower": cucsStorageSasExpanderPower,
       "cucsStorageSasExpanderPresence": cucsStorageSasExpanderPresence,
       "cucsStorageSasExpanderRevision": cucsStorageSasExpanderRevision,
       "cucsStorageSasExpanderSerial": cucsStorageSasExpanderSerial,
       "cucsStorageSasExpanderThermal": cucsStorageSasExpanderThermal,
       "cucsStorageSasExpanderVendor": cucsStorageSasExpanderVendor,
       "cucsStorageSasExpanderVoltage": cucsStorageSasExpanderVoltage,
       "cucsStorageSasExpanderFwRegionOne": cucsStorageSasExpanderFwRegionOne,
       "cucsStorageSasExpanderFwRegionTwo": cucsStorageSasExpanderFwRegionTwo,
       "cucsStorageSasExpanderFwRunningRegion": cucsStorageSasExpanderFwRunningRegion,
       "cucsStorageSasExpanderSasAddress": cucsStorageSasExpanderSasAddress,
       "cucsStorageScsiLunRefTable": cucsStorageScsiLunRefTable,
       "cucsStorageScsiLunRefEntry": cucsStorageScsiLunRefEntry,
       "cucsStorageScsiLunRefInstanceId": cucsStorageScsiLunRefInstanceId,
       "cucsStorageScsiLunRefDn": cucsStorageScsiLunRefDn,
       "cucsStorageScsiLunRefRn": cucsStorageScsiLunRefRn,
       "cucsStorageScsiLunRefId": cucsStorageScsiLunRefId,
       "cucsStorageScsiLunRefLsDn": cucsStorageScsiLunRefLsDn,
       "cucsStorageScsiLunRefLunName": cucsStorageScsiLunRefLunName,
       "cucsStorageScsiLunRefProfileDn": cucsStorageScsiLunRefProfileDn,
       "cucsStorageScsiLunRefPnDn": cucsStorageScsiLunRefPnDn,
       "cucsStorageVDMemberEpTable": cucsStorageVDMemberEpTable,
       "cucsStorageVDMemberEpEntry": cucsStorageVDMemberEpEntry,
       "cucsStorageVDMemberEpInstanceId": cucsStorageVDMemberEpInstanceId,
       "cucsStorageVDMemberEpDn": cucsStorageVDMemberEpDn,
       "cucsStorageVDMemberEpRn": cucsStorageVDMemberEpRn,
       "cucsStorageVDMemberEpConfigQual": cucsStorageVDMemberEpConfigQual,
       "cucsStorageVDMemberEpConfigQualifierReason": cucsStorageVDMemberEpConfigQualifierReason,
       "cucsStorageVDMemberEpConfigState": cucsStorageVDMemberEpConfigState,
       "cucsStorageVDMemberEpDeployAction": cucsStorageVDMemberEpDeployAction,
       "cucsStorageVDMemberEpDiskDn": cucsStorageVDMemberEpDiskDn,
       "cucsStorageVDMemberEpId": cucsStorageVDMemberEpId,
       "cucsStorageVDMemberEpModel": cucsStorageVDMemberEpModel,
       "cucsStorageVDMemberEpOperQualifierReason": cucsStorageVDMemberEpOperQualifierReason,
       "cucsStorageVDMemberEpOperability": cucsStorageVDMemberEpOperability,
       "cucsStorageVDMemberEpPresence": cucsStorageVDMemberEpPresence,
       "cucsStorageVDMemberEpRevision": cucsStorageVDMemberEpRevision,
       "cucsStorageVDMemberEpRole": cucsStorageVDMemberEpRole,
       "cucsStorageVDMemberEpSerial": cucsStorageVDMemberEpSerial,
       "cucsStorageVDMemberEpSpanId": cucsStorageVDMemberEpSpanId,
       "cucsStorageVDMemberEpVendor": cucsStorageVDMemberEpVendor,
       "cucsStorageVirtualDriveRefTable": cucsStorageVirtualDriveRefTable,
       "cucsStorageVirtualDriveRefEntry": cucsStorageVirtualDriveRefEntry,
       "cucsStorageVirtualDriveRefInstanceId": cucsStorageVirtualDriveRefInstanceId,
       "cucsStorageVirtualDriveRefDnData": cucsStorageVirtualDriveRefDnData,
       "cucsStorageVirtualDriveRefRn": cucsStorageVirtualDriveRefRn,
       "cucsStorageVirtualDriveRefAdminName": cucsStorageVirtualDriveRefAdminName,
       "cucsStorageVirtualDriveRefAdminState": cucsStorageVirtualDriveRefAdminState,
       "cucsStorageVirtualDriveRefConfigState": cucsStorageVirtualDriveRefConfigState,
       "cucsStorageVirtualDriveRefDiskSelectionOrder": cucsStorageVirtualDriveRefDiskSelectionOrder,
       "cucsStorageVirtualDriveRefDiskSelectionTs": cucsStorageVirtualDriveRefDiskSelectionTs,
       "cucsStorageVirtualDriveRefLunDn": cucsStorageVirtualDriveRefLunDn,
       "cucsStorageVirtualDriveRefLunItemDn": cucsStorageVirtualDriveRefLunItemDn,
       "cucsStorageVirtualDriveRefLunItemName": cucsStorageVirtualDriveRefLunItemName,
       "cucsStorageVirtualDriveRefLunName": cucsStorageVirtualDriveRefLunName,
       "cucsStorageVirtualDriveRefRaidLevel": cucsStorageVirtualDriveRefRaidLevel,
       "cucsStorageVirtualDriveRefSize": cucsStorageVirtualDriveRefSize,
       "cucsStorageVirtualDriveRefUuid": cucsStorageVirtualDriveRefUuid,
       "cucsStorageVirtualDriveRefIsBootable": cucsStorageVirtualDriveRefIsBootable,
       "cucsStorageVirtualDriveRefOrder": cucsStorageVirtualDriveRefOrder,
       "cucsStorageVirtualDriveRefVendorUuid": cucsStorageVirtualDriveRefVendorUuid}
)
