# SNMP MIB module (CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:34 2024
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

(CucsConditionRemoteInvRslt,
 CucsExtpolConnProtocol,
 CucsFirmwareActivityServersPowerState,
 CucsFirmwareActivityUpgradePriorityInfo,
 CucsFirmwareAdminState,
 CucsFirmwareAutoSyncConfigIssue,
 CucsFirmwareAutoSyncState,
 CucsFirmwareBladeType,
 CucsFirmwareBootUnitImage,
 CucsFirmwareBootUnitMode,
 CucsFirmwareCatalogPackConfigState,
 CucsFirmwareCompleteness,
 CucsFirmwareComponentType,
 CucsFirmwareDependencyRelationship,
 CucsFirmwareDependencyScope,
 CucsFirmwareDependencySensitivity,
 CucsFirmwareDistributableFsmCurrentFsm,
 CucsFirmwareDistributableFsmStageName,
 CucsFirmwareDistributableFsmTaskItem,
 CucsFirmwareDistributableType,
 CucsFirmwareDownloadActivity,
 CucsFirmwareDownloaderFsmCurrentFsm,
 CucsFirmwareDownloaderFsmStageName,
 CucsFirmwareDownloaderFsmTaskItem,
 CucsFirmwareEquipmentType,
 CucsFirmwareFileType,
 CucsFirmwareFirmwareState,
 CucsFirmwareFwState,
 CucsFirmwareHostPackConfigQualifier,
 CucsFirmwareImageDeleted,
 CucsFirmwareImageError,
 CucsFirmwareImageFsmCurrentFsm,
 CucsFirmwareImageFsmStageName,
 CucsFirmwareImageFsmTaskItem,
 CucsFirmwareImagePresence,
 CucsFirmwareImageState,
 CucsFirmwareImpactType,
 CucsFirmwareInstallState,
 CucsFirmwareItemType,
 CucsFirmwarePackItemPresence,
 CucsFirmwarePackMode,
 CucsFirmwarePlatformType,
 CucsFirmwareRunningDeployment,
 CucsFirmwareSystemFsmCurrentFsm,
 CucsFirmwareSystemFsmStageName,
 CucsFirmwareSystemFsmTaskFlags,
 CucsFirmwareSystemFsmTaskItem,
 CucsFirmwareTransferState,
 CucsFirmwareTransport,
 CucsFirmwareTriggerState,
 CucsFirmwareType,
 CucsFirmwareUpdatableDeployment,
 CucsFirmwareUpgradeCategory,
 CucsFirmwareUpgradeSeverity,
 CucsFirmwareUpgradeStatus,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsPolicyPolicyOwner,
 CucsTrigAckChangeDetails,
 CucsTrigAckChanges,
 CucsTrigAckDisr,
 CucsTrigAckOperState,
 CucsTrigAckPrevOperState,
 CucsTrigAdminState,
 CucsTrigTrigOperState,
 CucsTrigTrigState) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsExtpolConnProtocol",
    "CucsFirmwareActivityServersPowerState",
    "CucsFirmwareActivityUpgradePriorityInfo",
    "CucsFirmwareAdminState",
    "CucsFirmwareAutoSyncConfigIssue",
    "CucsFirmwareAutoSyncState",
    "CucsFirmwareBladeType",
    "CucsFirmwareBootUnitImage",
    "CucsFirmwareBootUnitMode",
    "CucsFirmwareCatalogPackConfigState",
    "CucsFirmwareCompleteness",
    "CucsFirmwareComponentType",
    "CucsFirmwareDependencyRelationship",
    "CucsFirmwareDependencyScope",
    "CucsFirmwareDependencySensitivity",
    "CucsFirmwareDistributableFsmCurrentFsm",
    "CucsFirmwareDistributableFsmStageName",
    "CucsFirmwareDistributableFsmTaskItem",
    "CucsFirmwareDistributableType",
    "CucsFirmwareDownloadActivity",
    "CucsFirmwareDownloaderFsmCurrentFsm",
    "CucsFirmwareDownloaderFsmStageName",
    "CucsFirmwareDownloaderFsmTaskItem",
    "CucsFirmwareEquipmentType",
    "CucsFirmwareFileType",
    "CucsFirmwareFirmwareState",
    "CucsFirmwareFwState",
    "CucsFirmwareHostPackConfigQualifier",
    "CucsFirmwareImageDeleted",
    "CucsFirmwareImageError",
    "CucsFirmwareImageFsmCurrentFsm",
    "CucsFirmwareImageFsmStageName",
    "CucsFirmwareImageFsmTaskItem",
    "CucsFirmwareImagePresence",
    "CucsFirmwareImageState",
    "CucsFirmwareImpactType",
    "CucsFirmwareInstallState",
    "CucsFirmwareItemType",
    "CucsFirmwarePackItemPresence",
    "CucsFirmwarePackMode",
    "CucsFirmwarePlatformType",
    "CucsFirmwareRunningDeployment",
    "CucsFirmwareSystemFsmCurrentFsm",
    "CucsFirmwareSystemFsmStageName",
    "CucsFirmwareSystemFsmTaskFlags",
    "CucsFirmwareSystemFsmTaskItem",
    "CucsFirmwareTransferState",
    "CucsFirmwareTransport",
    "CucsFirmwareTriggerState",
    "CucsFirmwareType",
    "CucsFirmwareUpdatableDeployment",
    "CucsFirmwareUpgradeCategory",
    "CucsFirmwareUpgradeSeverity",
    "CucsFirmwareUpgradeStatus",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsPolicyPolicyOwner",
    "CucsTrigAckChangeDetails",
    "CucsTrigAckChanges",
    "CucsTrigAckDisr",
    "CucsTrigAckOperState",
    "CucsTrigAckPrevOperState",
    "CucsTrigAdminState",
    "CucsTrigTrigOperState",
    "CucsTrigTrigState")

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

cucsFirmwareObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsFirmwareBootDefinitionTable_Object = MibTable
cucsFirmwareBootDefinitionTable = _CucsFirmwareBootDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 1)
)
if mibBuilder.loadTexts:
    cucsFirmwareBootDefinitionTable.setStatus("current")
_CucsFirmwareBootDefinitionEntry_Object = MibTableRow
cucsFirmwareBootDefinitionEntry = _CucsFirmwareBootDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 1, 1)
)
cucsFirmwareBootDefinitionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareBootDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareBootDefinitionEntry.setStatus("current")
_CucsFirmwareBootDefinitionInstanceId_Type = CucsManagedObjectId
_CucsFirmwareBootDefinitionInstanceId_Object = MibTableColumn
cucsFirmwareBootDefinitionInstanceId = _CucsFirmwareBootDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 1, 1, 1),
    _CucsFirmwareBootDefinitionInstanceId_Type()
)
cucsFirmwareBootDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareBootDefinitionInstanceId.setStatus("current")
_CucsFirmwareBootDefinitionDn_Type = CucsManagedObjectDn
_CucsFirmwareBootDefinitionDn_Object = MibTableColumn
cucsFirmwareBootDefinitionDn = _CucsFirmwareBootDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 1, 1, 2),
    _CucsFirmwareBootDefinitionDn_Type()
)
cucsFirmwareBootDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootDefinitionDn.setStatus("current")
_CucsFirmwareBootDefinitionRn_Type = SnmpAdminString
_CucsFirmwareBootDefinitionRn_Object = MibTableColumn
cucsFirmwareBootDefinitionRn = _CucsFirmwareBootDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 1, 1, 3),
    _CucsFirmwareBootDefinitionRn_Type()
)
cucsFirmwareBootDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootDefinitionRn.setStatus("current")
_CucsFirmwareBootDefinitionType_Type = CucsFirmwareType
_CucsFirmwareBootDefinitionType_Object = MibTableColumn
cucsFirmwareBootDefinitionType = _CucsFirmwareBootDefinitionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 1, 1, 4),
    _CucsFirmwareBootDefinitionType_Type()
)
cucsFirmwareBootDefinitionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootDefinitionType.setStatus("current")
_CucsFirmwareBootUnitTable_Object = MibTable
cucsFirmwareBootUnitTable = _CucsFirmwareBootUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2)
)
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitTable.setStatus("current")
_CucsFirmwareBootUnitEntry_Object = MibTableRow
cucsFirmwareBootUnitEntry = _CucsFirmwareBootUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1)
)
cucsFirmwareBootUnitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareBootUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitEntry.setStatus("current")
_CucsFirmwareBootUnitInstanceId_Type = CucsManagedObjectId
_CucsFirmwareBootUnitInstanceId_Object = MibTableColumn
cucsFirmwareBootUnitInstanceId = _CucsFirmwareBootUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 1),
    _CucsFirmwareBootUnitInstanceId_Type()
)
cucsFirmwareBootUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitInstanceId.setStatus("current")
_CucsFirmwareBootUnitDn_Type = CucsManagedObjectDn
_CucsFirmwareBootUnitDn_Object = MibTableColumn
cucsFirmwareBootUnitDn = _CucsFirmwareBootUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 2),
    _CucsFirmwareBootUnitDn_Type()
)
cucsFirmwareBootUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitDn.setStatus("current")
_CucsFirmwareBootUnitRn_Type = SnmpAdminString
_CucsFirmwareBootUnitRn_Object = MibTableColumn
cucsFirmwareBootUnitRn = _CucsFirmwareBootUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 3),
    _CucsFirmwareBootUnitRn_Type()
)
cucsFirmwareBootUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitRn.setStatus("current")
_CucsFirmwareBootUnitAdminState_Type = CucsFirmwareTriggerState
_CucsFirmwareBootUnitAdminState_Object = MibTableColumn
cucsFirmwareBootUnitAdminState = _CucsFirmwareBootUnitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 4),
    _CucsFirmwareBootUnitAdminState_Type()
)
cucsFirmwareBootUnitAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitAdminState.setStatus("current")
_CucsFirmwareBootUnitIgnoreCompCheck_Type = TruthValue
_CucsFirmwareBootUnitIgnoreCompCheck_Object = MibTableColumn
cucsFirmwareBootUnitIgnoreCompCheck = _CucsFirmwareBootUnitIgnoreCompCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 5),
    _CucsFirmwareBootUnitIgnoreCompCheck_Type()
)
cucsFirmwareBootUnitIgnoreCompCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitIgnoreCompCheck.setStatus("current")
_CucsFirmwareBootUnitImage_Type = CucsFirmwareBootUnitImage
_CucsFirmwareBootUnitImage_Object = MibTableColumn
cucsFirmwareBootUnitImage = _CucsFirmwareBootUnitImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 6),
    _CucsFirmwareBootUnitImage_Type()
)
cucsFirmwareBootUnitImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitImage.setStatus("current")
_CucsFirmwareBootUnitOperState_Type = CucsFirmwareImageState
_CucsFirmwareBootUnitOperState_Object = MibTableColumn
cucsFirmwareBootUnitOperState = _CucsFirmwareBootUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 7),
    _CucsFirmwareBootUnitOperState_Type()
)
cucsFirmwareBootUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitOperState.setStatus("current")
_CucsFirmwareBootUnitPrevVersion_Type = SnmpAdminString
_CucsFirmwareBootUnitPrevVersion_Object = MibTableColumn
cucsFirmwareBootUnitPrevVersion = _CucsFirmwareBootUnitPrevVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 8),
    _CucsFirmwareBootUnitPrevVersion_Type()
)
cucsFirmwareBootUnitPrevVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitPrevVersion.setStatus("current")
_CucsFirmwareBootUnitResetOnActivate_Type = TruthValue
_CucsFirmwareBootUnitResetOnActivate_Object = MibTableColumn
cucsFirmwareBootUnitResetOnActivate = _CucsFirmwareBootUnitResetOnActivate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 9),
    _CucsFirmwareBootUnitResetOnActivate_Type()
)
cucsFirmwareBootUnitResetOnActivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitResetOnActivate.setStatus("current")
_CucsFirmwareBootUnitType_Type = CucsFirmwareComponentType
_CucsFirmwareBootUnitType_Object = MibTableColumn
cucsFirmwareBootUnitType = _CucsFirmwareBootUnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 10),
    _CucsFirmwareBootUnitType_Type()
)
cucsFirmwareBootUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitType.setStatus("current")
_CucsFirmwareBootUnitVersion_Type = SnmpAdminString
_CucsFirmwareBootUnitVersion_Object = MibTableColumn
cucsFirmwareBootUnitVersion = _CucsFirmwareBootUnitVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 11),
    _CucsFirmwareBootUnitVersion_Type()
)
cucsFirmwareBootUnitVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitVersion.setStatus("current")
_CucsFirmwareBootUnitSkipValidation_Type = TruthValue
_CucsFirmwareBootUnitSkipValidation_Object = MibTableColumn
cucsFirmwareBootUnitSkipValidation = _CucsFirmwareBootUnitSkipValidation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 12),
    _CucsFirmwareBootUnitSkipValidation_Type()
)
cucsFirmwareBootUnitSkipValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitSkipValidation.setStatus("current")
_CucsFirmwareBootUnitInvTag_Type = SnmpAdminString
_CucsFirmwareBootUnitInvTag_Object = MibTableColumn
cucsFirmwareBootUnitInvTag = _CucsFirmwareBootUnitInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 13),
    _CucsFirmwareBootUnitInvTag_Type()
)
cucsFirmwareBootUnitInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitInvTag.setStatus("current")
_CucsFirmwareBootUnitMode_Type = CucsFirmwareBootUnitMode
_CucsFirmwareBootUnitMode_Object = MibTableColumn
cucsFirmwareBootUnitMode = _CucsFirmwareBootUnitMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 2, 1, 14),
    _CucsFirmwareBootUnitMode_Type()
)
cucsFirmwareBootUnitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBootUnitMode.setStatus("current")
_CucsFirmwareCatalogueTable_Object = MibTable
cucsFirmwareCatalogueTable = _CucsFirmwareCatalogueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 3)
)
if mibBuilder.loadTexts:
    cucsFirmwareCatalogueTable.setStatus("current")
_CucsFirmwareCatalogueEntry_Object = MibTableRow
cucsFirmwareCatalogueEntry = _CucsFirmwareCatalogueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 3, 1)
)
cucsFirmwareCatalogueEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareCatalogueInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareCatalogueEntry.setStatus("current")
_CucsFirmwareCatalogueInstanceId_Type = CucsManagedObjectId
_CucsFirmwareCatalogueInstanceId_Object = MibTableColumn
cucsFirmwareCatalogueInstanceId = _CucsFirmwareCatalogueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 3, 1, 1),
    _CucsFirmwareCatalogueInstanceId_Type()
)
cucsFirmwareCatalogueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogueInstanceId.setStatus("current")
_CucsFirmwareCatalogueDn_Type = CucsManagedObjectDn
_CucsFirmwareCatalogueDn_Object = MibTableColumn
cucsFirmwareCatalogueDn = _CucsFirmwareCatalogueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 3, 1, 2),
    _CucsFirmwareCatalogueDn_Type()
)
cucsFirmwareCatalogueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogueDn.setStatus("current")
_CucsFirmwareCatalogueRn_Type = SnmpAdminString
_CucsFirmwareCatalogueRn_Object = MibTableColumn
cucsFirmwareCatalogueRn = _CucsFirmwareCatalogueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 3, 1, 3),
    _CucsFirmwareCatalogueRn_Type()
)
cucsFirmwareCatalogueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogueRn.setStatus("current")
_CucsFirmwareCatalogueSyncTrigger_Type = TruthValue
_CucsFirmwareCatalogueSyncTrigger_Object = MibTableColumn
cucsFirmwareCatalogueSyncTrigger = _CucsFirmwareCatalogueSyncTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 3, 1, 4),
    _CucsFirmwareCatalogueSyncTrigger_Type()
)
cucsFirmwareCatalogueSyncTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogueSyncTrigger.setStatus("current")
_CucsFirmwareCompSourceTable_Object = MibTable
cucsFirmwareCompSourceTable = _CucsFirmwareCompSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 4)
)
if mibBuilder.loadTexts:
    cucsFirmwareCompSourceTable.setStatus("current")
_CucsFirmwareCompSourceEntry_Object = MibTableRow
cucsFirmwareCompSourceEntry = _CucsFirmwareCompSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 4, 1)
)
cucsFirmwareCompSourceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareCompSourceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareCompSourceEntry.setStatus("current")
_CucsFirmwareCompSourceInstanceId_Type = CucsManagedObjectId
_CucsFirmwareCompSourceInstanceId_Object = MibTableColumn
cucsFirmwareCompSourceInstanceId = _CucsFirmwareCompSourceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 4, 1, 1),
    _CucsFirmwareCompSourceInstanceId_Type()
)
cucsFirmwareCompSourceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareCompSourceInstanceId.setStatus("current")
_CucsFirmwareCompSourceDn_Type = CucsManagedObjectDn
_CucsFirmwareCompSourceDn_Object = MibTableColumn
cucsFirmwareCompSourceDn = _CucsFirmwareCompSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 4, 1, 2),
    _CucsFirmwareCompSourceDn_Type()
)
cucsFirmwareCompSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompSourceDn.setStatus("current")
_CucsFirmwareCompSourceRn_Type = SnmpAdminString
_CucsFirmwareCompSourceRn_Object = MibTableColumn
cucsFirmwareCompSourceRn = _CucsFirmwareCompSourceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 4, 1, 3),
    _CucsFirmwareCompSourceRn_Type()
)
cucsFirmwareCompSourceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompSourceRn.setStatus("current")
_CucsFirmwareCompSourceInvTag_Type = SnmpAdminString
_CucsFirmwareCompSourceInvTag_Object = MibTableColumn
cucsFirmwareCompSourceInvTag = _CucsFirmwareCompSourceInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 4, 1, 4),
    _CucsFirmwareCompSourceInvTag_Type()
)
cucsFirmwareCompSourceInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompSourceInvTag.setStatus("current")
_CucsFirmwareCompSourceVersion_Type = SnmpAdminString
_CucsFirmwareCompSourceVersion_Object = MibTableColumn
cucsFirmwareCompSourceVersion = _CucsFirmwareCompSourceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 4, 1, 5),
    _CucsFirmwareCompSourceVersion_Type()
)
cucsFirmwareCompSourceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompSourceVersion.setStatus("current")
_CucsFirmwareCompSourceDescr_Type = SnmpAdminString
_CucsFirmwareCompSourceDescr_Object = MibTableColumn
cucsFirmwareCompSourceDescr = _CucsFirmwareCompSourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 4, 1, 6),
    _CucsFirmwareCompSourceDescr_Type()
)
cucsFirmwareCompSourceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompSourceDescr.setStatus("current")
_CucsFirmwareCompSourceIntId_Type = SnmpAdminString
_CucsFirmwareCompSourceIntId_Object = MibTableColumn
cucsFirmwareCompSourceIntId = _CucsFirmwareCompSourceIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 4, 1, 7),
    _CucsFirmwareCompSourceIntId_Type()
)
cucsFirmwareCompSourceIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompSourceIntId.setStatus("current")
_CucsFirmwareCompSourceName_Type = SnmpAdminString
_CucsFirmwareCompSourceName_Object = MibTableColumn
cucsFirmwareCompSourceName = _CucsFirmwareCompSourceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 4, 1, 8),
    _CucsFirmwareCompSourceName_Type()
)
cucsFirmwareCompSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompSourceName.setStatus("current")
_CucsFirmwareCompSourcePolicyLevel_Type = Gauge32
_CucsFirmwareCompSourcePolicyLevel_Object = MibTableColumn
cucsFirmwareCompSourcePolicyLevel = _CucsFirmwareCompSourcePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 4, 1, 9),
    _CucsFirmwareCompSourcePolicyLevel_Type()
)
cucsFirmwareCompSourcePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompSourcePolicyLevel.setStatus("current")
_CucsFirmwareCompSourcePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFirmwareCompSourcePolicyOwner_Object = MibTableColumn
cucsFirmwareCompSourcePolicyOwner = _CucsFirmwareCompSourcePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 4, 1, 10),
    _CucsFirmwareCompSourcePolicyOwner_Type()
)
cucsFirmwareCompSourcePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompSourcePolicyOwner.setStatus("current")
_CucsFirmwareCompTargetTable_Object = MibTable
cucsFirmwareCompTargetTable = _CucsFirmwareCompTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 5)
)
if mibBuilder.loadTexts:
    cucsFirmwareCompTargetTable.setStatus("current")
_CucsFirmwareCompTargetEntry_Object = MibTableRow
cucsFirmwareCompTargetEntry = _CucsFirmwareCompTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 5, 1)
)
cucsFirmwareCompTargetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareCompTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareCompTargetEntry.setStatus("current")
_CucsFirmwareCompTargetInstanceId_Type = CucsManagedObjectId
_CucsFirmwareCompTargetInstanceId_Object = MibTableColumn
cucsFirmwareCompTargetInstanceId = _CucsFirmwareCompTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 5, 1, 1),
    _CucsFirmwareCompTargetInstanceId_Type()
)
cucsFirmwareCompTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareCompTargetInstanceId.setStatus("current")
_CucsFirmwareCompTargetDn_Type = CucsManagedObjectDn
_CucsFirmwareCompTargetDn_Object = MibTableColumn
cucsFirmwareCompTargetDn = _CucsFirmwareCompTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 5, 1, 2),
    _CucsFirmwareCompTargetDn_Type()
)
cucsFirmwareCompTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompTargetDn.setStatus("current")
_CucsFirmwareCompTargetRn_Type = SnmpAdminString
_CucsFirmwareCompTargetRn_Object = MibTableColumn
cucsFirmwareCompTargetRn = _CucsFirmwareCompTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 5, 1, 3),
    _CucsFirmwareCompTargetRn_Type()
)
cucsFirmwareCompTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompTargetRn.setStatus("current")
_CucsFirmwareCompTargetInvTag_Type = SnmpAdminString
_CucsFirmwareCompTargetInvTag_Object = MibTableColumn
cucsFirmwareCompTargetInvTag = _CucsFirmwareCompTargetInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 5, 1, 4),
    _CucsFirmwareCompTargetInvTag_Type()
)
cucsFirmwareCompTargetInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompTargetInvTag.setStatus("current")
_CucsFirmwareCompTargetVersion_Type = SnmpAdminString
_CucsFirmwareCompTargetVersion_Object = MibTableColumn
cucsFirmwareCompTargetVersion = _CucsFirmwareCompTargetVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 5, 1, 5),
    _CucsFirmwareCompTargetVersion_Type()
)
cucsFirmwareCompTargetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompTargetVersion.setStatus("current")
_CucsFirmwareCompTargetDescr_Type = SnmpAdminString
_CucsFirmwareCompTargetDescr_Object = MibTableColumn
cucsFirmwareCompTargetDescr = _CucsFirmwareCompTargetDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 5, 1, 6),
    _CucsFirmwareCompTargetDescr_Type()
)
cucsFirmwareCompTargetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompTargetDescr.setStatus("current")
_CucsFirmwareCompTargetIntId_Type = SnmpAdminString
_CucsFirmwareCompTargetIntId_Object = MibTableColumn
cucsFirmwareCompTargetIntId = _CucsFirmwareCompTargetIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 5, 1, 7),
    _CucsFirmwareCompTargetIntId_Type()
)
cucsFirmwareCompTargetIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompTargetIntId.setStatus("current")
_CucsFirmwareCompTargetName_Type = SnmpAdminString
_CucsFirmwareCompTargetName_Object = MibTableColumn
cucsFirmwareCompTargetName = _CucsFirmwareCompTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 5, 1, 8),
    _CucsFirmwareCompTargetName_Type()
)
cucsFirmwareCompTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompTargetName.setStatus("current")
_CucsFirmwareCompTargetPolicyLevel_Type = Gauge32
_CucsFirmwareCompTargetPolicyLevel_Object = MibTableColumn
cucsFirmwareCompTargetPolicyLevel = _CucsFirmwareCompTargetPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 5, 1, 9),
    _CucsFirmwareCompTargetPolicyLevel_Type()
)
cucsFirmwareCompTargetPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompTargetPolicyLevel.setStatus("current")
_CucsFirmwareCompTargetPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFirmwareCompTargetPolicyOwner_Object = MibTableColumn
cucsFirmwareCompTargetPolicyOwner = _CucsFirmwareCompTargetPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 5, 1, 10),
    _CucsFirmwareCompTargetPolicyOwner_Type()
)
cucsFirmwareCompTargetPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCompTargetPolicyOwner.setStatus("current")
_CucsFirmwareComputeHostPackTable_Object = MibTable
cucsFirmwareComputeHostPackTable = _CucsFirmwareComputeHostPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6)
)
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackTable.setStatus("current")
_CucsFirmwareComputeHostPackEntry_Object = MibTableRow
cucsFirmwareComputeHostPackEntry = _CucsFirmwareComputeHostPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1)
)
cucsFirmwareComputeHostPackEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareComputeHostPackInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackEntry.setStatus("current")
_CucsFirmwareComputeHostPackInstanceId_Type = CucsManagedObjectId
_CucsFirmwareComputeHostPackInstanceId_Object = MibTableColumn
cucsFirmwareComputeHostPackInstanceId = _CucsFirmwareComputeHostPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 1),
    _CucsFirmwareComputeHostPackInstanceId_Type()
)
cucsFirmwareComputeHostPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackInstanceId.setStatus("current")
_CucsFirmwareComputeHostPackDn_Type = CucsManagedObjectDn
_CucsFirmwareComputeHostPackDn_Object = MibTableColumn
cucsFirmwareComputeHostPackDn = _CucsFirmwareComputeHostPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 2),
    _CucsFirmwareComputeHostPackDn_Type()
)
cucsFirmwareComputeHostPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackDn.setStatus("current")
_CucsFirmwareComputeHostPackRn_Type = SnmpAdminString
_CucsFirmwareComputeHostPackRn_Object = MibTableColumn
cucsFirmwareComputeHostPackRn = _CucsFirmwareComputeHostPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 3),
    _CucsFirmwareComputeHostPackRn_Type()
)
cucsFirmwareComputeHostPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackRn.setStatus("current")
_CucsFirmwareComputeHostPackDescr_Type = SnmpAdminString
_CucsFirmwareComputeHostPackDescr_Object = MibTableColumn
cucsFirmwareComputeHostPackDescr = _CucsFirmwareComputeHostPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 4),
    _CucsFirmwareComputeHostPackDescr_Type()
)
cucsFirmwareComputeHostPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackDescr.setStatus("current")
_CucsFirmwareComputeHostPackIntId_Type = SnmpAdminString
_CucsFirmwareComputeHostPackIntId_Object = MibTableColumn
cucsFirmwareComputeHostPackIntId = _CucsFirmwareComputeHostPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 5),
    _CucsFirmwareComputeHostPackIntId_Type()
)
cucsFirmwareComputeHostPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackIntId.setStatus("current")
_CucsFirmwareComputeHostPackMode_Type = CucsFirmwarePackMode
_CucsFirmwareComputeHostPackMode_Object = MibTableColumn
cucsFirmwareComputeHostPackMode = _CucsFirmwareComputeHostPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 6),
    _CucsFirmwareComputeHostPackMode_Type()
)
cucsFirmwareComputeHostPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackMode.setStatus("current")
_CucsFirmwareComputeHostPackName_Type = SnmpAdminString
_CucsFirmwareComputeHostPackName_Object = MibTableColumn
cucsFirmwareComputeHostPackName = _CucsFirmwareComputeHostPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 7),
    _CucsFirmwareComputeHostPackName_Type()
)
cucsFirmwareComputeHostPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackName.setStatus("current")
_CucsFirmwareComputeHostPackStageSize_Type = Gauge32
_CucsFirmwareComputeHostPackStageSize_Object = MibTableColumn
cucsFirmwareComputeHostPackStageSize = _CucsFirmwareComputeHostPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 8),
    _CucsFirmwareComputeHostPackStageSize_Type()
)
cucsFirmwareComputeHostPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackStageSize.setStatus("current")
_CucsFirmwareComputeHostPackUpdateTrigger_Type = DateAndTime
_CucsFirmwareComputeHostPackUpdateTrigger_Object = MibTableColumn
cucsFirmwareComputeHostPackUpdateTrigger = _CucsFirmwareComputeHostPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 9),
    _CucsFirmwareComputeHostPackUpdateTrigger_Type()
)
cucsFirmwareComputeHostPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackUpdateTrigger.setStatus("current")
_CucsFirmwareComputeHostPackIgnoreCompCheck_Type = TruthValue
_CucsFirmwareComputeHostPackIgnoreCompCheck_Object = MibTableColumn
cucsFirmwareComputeHostPackIgnoreCompCheck = _CucsFirmwareComputeHostPackIgnoreCompCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 10),
    _CucsFirmwareComputeHostPackIgnoreCompCheck_Type()
)
cucsFirmwareComputeHostPackIgnoreCompCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackIgnoreCompCheck.setStatus("current")
_CucsFirmwareComputeHostPackConfigQualifier_Type = CucsFirmwareHostPackConfigQualifier
_CucsFirmwareComputeHostPackConfigQualifier_Object = MibTableColumn
cucsFirmwareComputeHostPackConfigQualifier = _CucsFirmwareComputeHostPackConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 11),
    _CucsFirmwareComputeHostPackConfigQualifier_Type()
)
cucsFirmwareComputeHostPackConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackConfigQualifier.setStatus("current")
_CucsFirmwareComputeHostPackBladeBundleName_Type = SnmpAdminString
_CucsFirmwareComputeHostPackBladeBundleName_Object = MibTableColumn
cucsFirmwareComputeHostPackBladeBundleName = _CucsFirmwareComputeHostPackBladeBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 12),
    _CucsFirmwareComputeHostPackBladeBundleName_Type()
)
cucsFirmwareComputeHostPackBladeBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackBladeBundleName.setStatus("current")
_CucsFirmwareComputeHostPackBladeBundleVersion_Type = SnmpAdminString
_CucsFirmwareComputeHostPackBladeBundleVersion_Object = MibTableColumn
cucsFirmwareComputeHostPackBladeBundleVersion = _CucsFirmwareComputeHostPackBladeBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 13),
    _CucsFirmwareComputeHostPackBladeBundleVersion_Type()
)
cucsFirmwareComputeHostPackBladeBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackBladeBundleVersion.setStatus("current")
_CucsFirmwareComputeHostPackPolicyLevel_Type = Gauge32
_CucsFirmwareComputeHostPackPolicyLevel_Object = MibTableColumn
cucsFirmwareComputeHostPackPolicyLevel = _CucsFirmwareComputeHostPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 14),
    _CucsFirmwareComputeHostPackPolicyLevel_Type()
)
cucsFirmwareComputeHostPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackPolicyLevel.setStatus("current")
_CucsFirmwareComputeHostPackPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFirmwareComputeHostPackPolicyOwner_Object = MibTableColumn
cucsFirmwareComputeHostPackPolicyOwner = _CucsFirmwareComputeHostPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 15),
    _CucsFirmwareComputeHostPackPolicyOwner_Type()
)
cucsFirmwareComputeHostPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackPolicyOwner.setStatus("current")
_CucsFirmwareComputeHostPackRackBundleName_Type = SnmpAdminString
_CucsFirmwareComputeHostPackRackBundleName_Object = MibTableColumn
cucsFirmwareComputeHostPackRackBundleName = _CucsFirmwareComputeHostPackRackBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 16),
    _CucsFirmwareComputeHostPackRackBundleName_Type()
)
cucsFirmwareComputeHostPackRackBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackRackBundleName.setStatus("current")
_CucsFirmwareComputeHostPackRackBundleVersion_Type = SnmpAdminString
_CucsFirmwareComputeHostPackRackBundleVersion_Object = MibTableColumn
cucsFirmwareComputeHostPackRackBundleVersion = _CucsFirmwareComputeHostPackRackBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 17),
    _CucsFirmwareComputeHostPackRackBundleVersion_Type()
)
cucsFirmwareComputeHostPackRackBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackRackBundleVersion.setStatus("current")
_CucsFirmwareComputeHostPackMSeriesBundleName_Type = SnmpAdminString
_CucsFirmwareComputeHostPackMSeriesBundleName_Object = MibTableColumn
cucsFirmwareComputeHostPackMSeriesBundleName = _CucsFirmwareComputeHostPackMSeriesBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 19),
    _CucsFirmwareComputeHostPackMSeriesBundleName_Type()
)
cucsFirmwareComputeHostPackMSeriesBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackMSeriesBundleName.setStatus("current")
_CucsFirmwareComputeHostPackMSeriesBundleVersion_Type = SnmpAdminString
_CucsFirmwareComputeHostPackMSeriesBundleVersion_Object = MibTableColumn
cucsFirmwareComputeHostPackMSeriesBundleVersion = _CucsFirmwareComputeHostPackMSeriesBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 6, 1, 20),
    _CucsFirmwareComputeHostPackMSeriesBundleVersion_Type()
)
cucsFirmwareComputeHostPackMSeriesBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeHostPackMSeriesBundleVersion.setStatus("current")
_CucsFirmwareComputeMgmtPackTable_Object = MibTable
cucsFirmwareComputeMgmtPackTable = _CucsFirmwareComputeMgmtPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7)
)
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackTable.setStatus("current")
_CucsFirmwareComputeMgmtPackEntry_Object = MibTableRow
cucsFirmwareComputeMgmtPackEntry = _CucsFirmwareComputeMgmtPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1)
)
cucsFirmwareComputeMgmtPackEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareComputeMgmtPackInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackEntry.setStatus("current")
_CucsFirmwareComputeMgmtPackInstanceId_Type = CucsManagedObjectId
_CucsFirmwareComputeMgmtPackInstanceId_Object = MibTableColumn
cucsFirmwareComputeMgmtPackInstanceId = _CucsFirmwareComputeMgmtPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1, 1),
    _CucsFirmwareComputeMgmtPackInstanceId_Type()
)
cucsFirmwareComputeMgmtPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackInstanceId.setStatus("current")
_CucsFirmwareComputeMgmtPackDn_Type = CucsManagedObjectDn
_CucsFirmwareComputeMgmtPackDn_Object = MibTableColumn
cucsFirmwareComputeMgmtPackDn = _CucsFirmwareComputeMgmtPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1, 2),
    _CucsFirmwareComputeMgmtPackDn_Type()
)
cucsFirmwareComputeMgmtPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackDn.setStatus("current")
_CucsFirmwareComputeMgmtPackRn_Type = SnmpAdminString
_CucsFirmwareComputeMgmtPackRn_Object = MibTableColumn
cucsFirmwareComputeMgmtPackRn = _CucsFirmwareComputeMgmtPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1, 3),
    _CucsFirmwareComputeMgmtPackRn_Type()
)
cucsFirmwareComputeMgmtPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackRn.setStatus("current")
_CucsFirmwareComputeMgmtPackDescr_Type = SnmpAdminString
_CucsFirmwareComputeMgmtPackDescr_Object = MibTableColumn
cucsFirmwareComputeMgmtPackDescr = _CucsFirmwareComputeMgmtPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1, 4),
    _CucsFirmwareComputeMgmtPackDescr_Type()
)
cucsFirmwareComputeMgmtPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackDescr.setStatus("current")
_CucsFirmwareComputeMgmtPackIntId_Type = SnmpAdminString
_CucsFirmwareComputeMgmtPackIntId_Object = MibTableColumn
cucsFirmwareComputeMgmtPackIntId = _CucsFirmwareComputeMgmtPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1, 5),
    _CucsFirmwareComputeMgmtPackIntId_Type()
)
cucsFirmwareComputeMgmtPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackIntId.setStatus("current")
_CucsFirmwareComputeMgmtPackMode_Type = CucsFirmwarePackMode
_CucsFirmwareComputeMgmtPackMode_Object = MibTableColumn
cucsFirmwareComputeMgmtPackMode = _CucsFirmwareComputeMgmtPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1, 6),
    _CucsFirmwareComputeMgmtPackMode_Type()
)
cucsFirmwareComputeMgmtPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackMode.setStatus("current")
_CucsFirmwareComputeMgmtPackName_Type = SnmpAdminString
_CucsFirmwareComputeMgmtPackName_Object = MibTableColumn
cucsFirmwareComputeMgmtPackName = _CucsFirmwareComputeMgmtPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1, 7),
    _CucsFirmwareComputeMgmtPackName_Type()
)
cucsFirmwareComputeMgmtPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackName.setStatus("current")
_CucsFirmwareComputeMgmtPackStageSize_Type = Gauge32
_CucsFirmwareComputeMgmtPackStageSize_Object = MibTableColumn
cucsFirmwareComputeMgmtPackStageSize = _CucsFirmwareComputeMgmtPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1, 8),
    _CucsFirmwareComputeMgmtPackStageSize_Type()
)
cucsFirmwareComputeMgmtPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackStageSize.setStatus("current")
_CucsFirmwareComputeMgmtPackUpdateTrigger_Type = DateAndTime
_CucsFirmwareComputeMgmtPackUpdateTrigger_Object = MibTableColumn
cucsFirmwareComputeMgmtPackUpdateTrigger = _CucsFirmwareComputeMgmtPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1, 9),
    _CucsFirmwareComputeMgmtPackUpdateTrigger_Type()
)
cucsFirmwareComputeMgmtPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackUpdateTrigger.setStatus("current")
_CucsFirmwareComputeMgmtPackIgnoreCompCheck_Type = TruthValue
_CucsFirmwareComputeMgmtPackIgnoreCompCheck_Object = MibTableColumn
cucsFirmwareComputeMgmtPackIgnoreCompCheck = _CucsFirmwareComputeMgmtPackIgnoreCompCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1, 10),
    _CucsFirmwareComputeMgmtPackIgnoreCompCheck_Type()
)
cucsFirmwareComputeMgmtPackIgnoreCompCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackIgnoreCompCheck.setStatus("current")
_CucsFirmwareComputeMgmtPackPolicyLevel_Type = Gauge32
_CucsFirmwareComputeMgmtPackPolicyLevel_Object = MibTableColumn
cucsFirmwareComputeMgmtPackPolicyLevel = _CucsFirmwareComputeMgmtPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1, 11),
    _CucsFirmwareComputeMgmtPackPolicyLevel_Type()
)
cucsFirmwareComputeMgmtPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackPolicyLevel.setStatus("current")
_CucsFirmwareComputeMgmtPackPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFirmwareComputeMgmtPackPolicyOwner_Object = MibTableColumn
cucsFirmwareComputeMgmtPackPolicyOwner = _CucsFirmwareComputeMgmtPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 7, 1, 12),
    _CucsFirmwareComputeMgmtPackPolicyOwner_Type()
)
cucsFirmwareComputeMgmtPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareComputeMgmtPackPolicyOwner.setStatus("current")
_CucsFirmwareDependencyTable_Object = MibTable
cucsFirmwareDependencyTable = _CucsFirmwareDependencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8)
)
if mibBuilder.loadTexts:
    cucsFirmwareDependencyTable.setStatus("current")
_CucsFirmwareDependencyEntry_Object = MibTableRow
cucsFirmwareDependencyEntry = _CucsFirmwareDependencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1)
)
cucsFirmwareDependencyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareDependencyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareDependencyEntry.setStatus("current")
_CucsFirmwareDependencyInstanceId_Type = CucsManagedObjectId
_CucsFirmwareDependencyInstanceId_Object = MibTableColumn
cucsFirmwareDependencyInstanceId = _CucsFirmwareDependencyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 1),
    _CucsFirmwareDependencyInstanceId_Type()
)
cucsFirmwareDependencyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareDependencyInstanceId.setStatus("current")
_CucsFirmwareDependencyDn_Type = CucsManagedObjectDn
_CucsFirmwareDependencyDn_Object = MibTableColumn
cucsFirmwareDependencyDn = _CucsFirmwareDependencyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 2),
    _CucsFirmwareDependencyDn_Type()
)
cucsFirmwareDependencyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDependencyDn.setStatus("current")
_CucsFirmwareDependencyRn_Type = SnmpAdminString
_CucsFirmwareDependencyRn_Object = MibTableColumn
cucsFirmwareDependencyRn = _CucsFirmwareDependencyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 3),
    _CucsFirmwareDependencyRn_Type()
)
cucsFirmwareDependencyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDependencyRn.setStatus("current")
_CucsFirmwareDependencyEp_Type = CucsFirmwareType
_CucsFirmwareDependencyEp_Object = MibTableColumn
cucsFirmwareDependencyEp = _CucsFirmwareDependencyEp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 4),
    _CucsFirmwareDependencyEp_Type()
)
cucsFirmwareDependencyEp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDependencyEp.setStatus("current")
_CucsFirmwareDependencyHwModel_Type = SnmpAdminString
_CucsFirmwareDependencyHwModel_Object = MibTableColumn
cucsFirmwareDependencyHwModel = _CucsFirmwareDependencyHwModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 5),
    _CucsFirmwareDependencyHwModel_Type()
)
cucsFirmwareDependencyHwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDependencyHwModel.setStatus("current")
_CucsFirmwareDependencyHwRevision_Type = SnmpAdminString
_CucsFirmwareDependencyHwRevision_Object = MibTableColumn
cucsFirmwareDependencyHwRevision = _CucsFirmwareDependencyHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 6),
    _CucsFirmwareDependencyHwRevision_Type()
)
cucsFirmwareDependencyHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDependencyHwRevision.setStatus("current")
_CucsFirmwareDependencyHwVendor_Type = SnmpAdminString
_CucsFirmwareDependencyHwVendor_Object = MibTableColumn
cucsFirmwareDependencyHwVendor = _CucsFirmwareDependencyHwVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 7),
    _CucsFirmwareDependencyHwVendor_Type()
)
cucsFirmwareDependencyHwVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDependencyHwVendor.setStatus("current")
_CucsFirmwareDependencyInvTag_Type = SnmpAdminString
_CucsFirmwareDependencyInvTag_Object = MibTableColumn
cucsFirmwareDependencyInvTag = _CucsFirmwareDependencyInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 8),
    _CucsFirmwareDependencyInvTag_Type()
)
cucsFirmwareDependencyInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDependencyInvTag.setStatus("current")
_CucsFirmwareDependencyMaxVer_Type = SnmpAdminString
_CucsFirmwareDependencyMaxVer_Object = MibTableColumn
cucsFirmwareDependencyMaxVer = _CucsFirmwareDependencyMaxVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 9),
    _CucsFirmwareDependencyMaxVer_Type()
)
cucsFirmwareDependencyMaxVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDependencyMaxVer.setStatus("current")
_CucsFirmwareDependencyMinVer_Type = SnmpAdminString
_CucsFirmwareDependencyMinVer_Object = MibTableColumn
cucsFirmwareDependencyMinVer = _CucsFirmwareDependencyMinVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 10),
    _CucsFirmwareDependencyMinVer_Type()
)
cucsFirmwareDependencyMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDependencyMinVer.setStatus("current")
_CucsFirmwareDependencyRelationship_Type = CucsFirmwareDependencyRelationship
_CucsFirmwareDependencyRelationship_Object = MibTableColumn
cucsFirmwareDependencyRelationship = _CucsFirmwareDependencyRelationship_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 11),
    _CucsFirmwareDependencyRelationship_Type()
)
cucsFirmwareDependencyRelationship.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDependencyRelationship.setStatus("current")
_CucsFirmwareDependencyScope_Type = CucsFirmwareDependencyScope
_CucsFirmwareDependencyScope_Object = MibTableColumn
cucsFirmwareDependencyScope = _CucsFirmwareDependencyScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 12),
    _CucsFirmwareDependencyScope_Type()
)
cucsFirmwareDependencyScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDependencyScope.setStatus("current")
_CucsFirmwareDependencySensitivity_Type = CucsFirmwareDependencySensitivity
_CucsFirmwareDependencySensitivity_Object = MibTableColumn
cucsFirmwareDependencySensitivity = _CucsFirmwareDependencySensitivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 8, 1, 13),
    _CucsFirmwareDependencySensitivity_Type()
)
cucsFirmwareDependencySensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDependencySensitivity.setStatus("current")
_CucsFirmwareDistImageTable_Object = MibTable
cucsFirmwareDistImageTable = _CucsFirmwareDistImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 9)
)
if mibBuilder.loadTexts:
    cucsFirmwareDistImageTable.setStatus("current")
_CucsFirmwareDistImageEntry_Object = MibTableRow
cucsFirmwareDistImageEntry = _CucsFirmwareDistImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 9, 1)
)
cucsFirmwareDistImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareDistImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareDistImageEntry.setStatus("current")
_CucsFirmwareDistImageInstanceId_Type = CucsManagedObjectId
_CucsFirmwareDistImageInstanceId_Object = MibTableColumn
cucsFirmwareDistImageInstanceId = _CucsFirmwareDistImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 9, 1, 1),
    _CucsFirmwareDistImageInstanceId_Type()
)
cucsFirmwareDistImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareDistImageInstanceId.setStatus("current")
_CucsFirmwareDistImageDn_Type = CucsManagedObjectDn
_CucsFirmwareDistImageDn_Object = MibTableColumn
cucsFirmwareDistImageDn = _CucsFirmwareDistImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 9, 1, 2),
    _CucsFirmwareDistImageDn_Type()
)
cucsFirmwareDistImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistImageDn.setStatus("current")
_CucsFirmwareDistImageRn_Type = SnmpAdminString
_CucsFirmwareDistImageRn_Object = MibTableColumn
cucsFirmwareDistImageRn = _CucsFirmwareDistImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 9, 1, 3),
    _CucsFirmwareDistImageRn_Type()
)
cucsFirmwareDistImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistImageRn.setStatus("current")
_CucsFirmwareDistImageImageDeleted_Type = CucsFirmwareImageDeleted
_CucsFirmwareDistImageImageDeleted_Object = MibTableColumn
cucsFirmwareDistImageImageDeleted = _CucsFirmwareDistImageImageDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 9, 1, 4),
    _CucsFirmwareDistImageImageDeleted_Type()
)
cucsFirmwareDistImageImageDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistImageImageDeleted.setStatus("current")
_CucsFirmwareDistImageName_Type = SnmpAdminString
_CucsFirmwareDistImageName_Object = MibTableColumn
cucsFirmwareDistImageName = _CucsFirmwareDistImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 9, 1, 5),
    _CucsFirmwareDistImageName_Type()
)
cucsFirmwareDistImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistImageName.setStatus("current")
_CucsFirmwareDistImageType_Type = CucsFirmwareType
_CucsFirmwareDistImageType_Object = MibTableColumn
cucsFirmwareDistImageType = _CucsFirmwareDistImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 9, 1, 6),
    _CucsFirmwareDistImageType_Type()
)
cucsFirmwareDistImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistImageType.setStatus("current")
_CucsFirmwareDistributableTable_Object = MibTable
cucsFirmwareDistributableTable = _CucsFirmwareDistributableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10)
)
if mibBuilder.loadTexts:
    cucsFirmwareDistributableTable.setStatus("current")
_CucsFirmwareDistributableEntry_Object = MibTableRow
cucsFirmwareDistributableEntry = _CucsFirmwareDistributableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1)
)
cucsFirmwareDistributableEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareDistributableInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareDistributableEntry.setStatus("current")
_CucsFirmwareDistributableInstanceId_Type = CucsManagedObjectId
_CucsFirmwareDistributableInstanceId_Object = MibTableColumn
cucsFirmwareDistributableInstanceId = _CucsFirmwareDistributableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 1),
    _CucsFirmwareDistributableInstanceId_Type()
)
cucsFirmwareDistributableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableInstanceId.setStatus("current")
_CucsFirmwareDistributableDn_Type = CucsManagedObjectDn
_CucsFirmwareDistributableDn_Object = MibTableColumn
cucsFirmwareDistributableDn = _CucsFirmwareDistributableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 2),
    _CucsFirmwareDistributableDn_Type()
)
cucsFirmwareDistributableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableDn.setStatus("current")
_CucsFirmwareDistributableRn_Type = SnmpAdminString
_CucsFirmwareDistributableRn_Object = MibTableColumn
cucsFirmwareDistributableRn = _CucsFirmwareDistributableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 3),
    _CucsFirmwareDistributableRn_Type()
)
cucsFirmwareDistributableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableRn.setStatus("current")
_CucsFirmwareDistributableAdminState_Type = CucsFirmwareAdminState
_CucsFirmwareDistributableAdminState_Object = MibTableColumn
cucsFirmwareDistributableAdminState = _CucsFirmwareDistributableAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 4),
    _CucsFirmwareDistributableAdminState_Type()
)
cucsFirmwareDistributableAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableAdminState.setStatus("current")
_CucsFirmwareDistributableCompleteness_Type = CucsFirmwareCompleteness
_CucsFirmwareDistributableCompleteness_Object = MibTableColumn
cucsFirmwareDistributableCompleteness = _CucsFirmwareDistributableCompleteness_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 5),
    _CucsFirmwareDistributableCompleteness_Type()
)
cucsFirmwareDistributableCompleteness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableCompleteness.setStatus("current")
_CucsFirmwareDistributableFsmDescr_Type = SnmpAdminString
_CucsFirmwareDistributableFsmDescr_Object = MibTableColumn
cucsFirmwareDistributableFsmDescr = _CucsFirmwareDistributableFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 6),
    _CucsFirmwareDistributableFsmDescr_Type()
)
cucsFirmwareDistributableFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmDescr.setStatus("current")
_CucsFirmwareDistributableFsmPrev_Type = SnmpAdminString
_CucsFirmwareDistributableFsmPrev_Object = MibTableColumn
cucsFirmwareDistributableFsmPrev = _CucsFirmwareDistributableFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 7),
    _CucsFirmwareDistributableFsmPrev_Type()
)
cucsFirmwareDistributableFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmPrev.setStatus("current")
_CucsFirmwareDistributableFsmProgr_Type = Gauge32
_CucsFirmwareDistributableFsmProgr_Object = MibTableColumn
cucsFirmwareDistributableFsmProgr = _CucsFirmwareDistributableFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 8),
    _CucsFirmwareDistributableFsmProgr_Type()
)
cucsFirmwareDistributableFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmProgr.setStatus("current")
_CucsFirmwareDistributableFsmRmtInvErrCode_Type = Gauge32
_CucsFirmwareDistributableFsmRmtInvErrCode_Object = MibTableColumn
cucsFirmwareDistributableFsmRmtInvErrCode = _CucsFirmwareDistributableFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 9),
    _CucsFirmwareDistributableFsmRmtInvErrCode_Type()
)
cucsFirmwareDistributableFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmRmtInvErrCode.setStatus("current")
_CucsFirmwareDistributableFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsFirmwareDistributableFsmRmtInvErrDescr_Object = MibTableColumn
cucsFirmwareDistributableFsmRmtInvErrDescr = _CucsFirmwareDistributableFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 10),
    _CucsFirmwareDistributableFsmRmtInvErrDescr_Type()
)
cucsFirmwareDistributableFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmRmtInvErrDescr.setStatus("current")
_CucsFirmwareDistributableFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsFirmwareDistributableFsmRmtInvRslt_Object = MibTableColumn
cucsFirmwareDistributableFsmRmtInvRslt = _CucsFirmwareDistributableFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 11),
    _CucsFirmwareDistributableFsmRmtInvRslt_Type()
)
cucsFirmwareDistributableFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmRmtInvRslt.setStatus("current")
_CucsFirmwareDistributableFsmStageDescr_Type = SnmpAdminString
_CucsFirmwareDistributableFsmStageDescr_Object = MibTableColumn
cucsFirmwareDistributableFsmStageDescr = _CucsFirmwareDistributableFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 12),
    _CucsFirmwareDistributableFsmStageDescr_Type()
)
cucsFirmwareDistributableFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStageDescr.setStatus("current")
_CucsFirmwareDistributableFsmStamp_Type = DateAndTime
_CucsFirmwareDistributableFsmStamp_Object = MibTableColumn
cucsFirmwareDistributableFsmStamp = _CucsFirmwareDistributableFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 13),
    _CucsFirmwareDistributableFsmStamp_Type()
)
cucsFirmwareDistributableFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStamp.setStatus("current")
_CucsFirmwareDistributableFsmStatus_Type = SnmpAdminString
_CucsFirmwareDistributableFsmStatus_Object = MibTableColumn
cucsFirmwareDistributableFsmStatus = _CucsFirmwareDistributableFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 14),
    _CucsFirmwareDistributableFsmStatus_Type()
)
cucsFirmwareDistributableFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStatus.setStatus("current")
_CucsFirmwareDistributableFsmTry_Type = Gauge32
_CucsFirmwareDistributableFsmTry_Object = MibTableColumn
cucsFirmwareDistributableFsmTry = _CucsFirmwareDistributableFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 15),
    _CucsFirmwareDistributableFsmTry_Type()
)
cucsFirmwareDistributableFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmTry.setStatus("current")
_CucsFirmwareDistributableImagePresence_Type = CucsFirmwareImagePresence
_CucsFirmwareDistributableImagePresence_Object = MibTableColumn
cucsFirmwareDistributableImagePresence = _CucsFirmwareDistributableImagePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 16),
    _CucsFirmwareDistributableImagePresence_Type()
)
cucsFirmwareDistributableImagePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableImagePresence.setStatus("current")
_CucsFirmwareDistributableModel_Type = SnmpAdminString
_CucsFirmwareDistributableModel_Object = MibTableColumn
cucsFirmwareDistributableModel = _CucsFirmwareDistributableModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 17),
    _CucsFirmwareDistributableModel_Type()
)
cucsFirmwareDistributableModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableModel.setStatus("current")
_CucsFirmwareDistributableName_Type = SnmpAdminString
_CucsFirmwareDistributableName_Object = MibTableColumn
cucsFirmwareDistributableName = _CucsFirmwareDistributableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 18),
    _CucsFirmwareDistributableName_Type()
)
cucsFirmwareDistributableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableName.setStatus("current")
_CucsFirmwareDistributableTransferState_Type = CucsFirmwareTransferState
_CucsFirmwareDistributableTransferState_Object = MibTableColumn
cucsFirmwareDistributableTransferState = _CucsFirmwareDistributableTransferState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 19),
    _CucsFirmwareDistributableTransferState_Type()
)
cucsFirmwareDistributableTransferState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableTransferState.setStatus("current")
_CucsFirmwareDistributableType_Type = CucsFirmwareDistributableType
_CucsFirmwareDistributableType_Object = MibTableColumn
cucsFirmwareDistributableType = _CucsFirmwareDistributableType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 20),
    _CucsFirmwareDistributableType_Type()
)
cucsFirmwareDistributableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableType.setStatus("current")
_CucsFirmwareDistributableVendor_Type = SnmpAdminString
_CucsFirmwareDistributableVendor_Object = MibTableColumn
cucsFirmwareDistributableVendor = _CucsFirmwareDistributableVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 21),
    _CucsFirmwareDistributableVendor_Type()
)
cucsFirmwareDistributableVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableVendor.setStatus("current")
_CucsFirmwareDistributableVersion_Type = SnmpAdminString
_CucsFirmwareDistributableVersion_Object = MibTableColumn
cucsFirmwareDistributableVersion = _CucsFirmwareDistributableVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 22),
    _CucsFirmwareDistributableVersion_Type()
)
cucsFirmwareDistributableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableVersion.setStatus("current")
_CucsFirmwareDistributableInvTag_Type = SnmpAdminString
_CucsFirmwareDistributableInvTag_Object = MibTableColumn
cucsFirmwareDistributableInvTag = _CucsFirmwareDistributableInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 23),
    _CucsFirmwareDistributableInvTag_Type()
)
cucsFirmwareDistributableInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableInvTag.setStatus("current")
_CucsFirmwareDistributableDescr_Type = SnmpAdminString
_CucsFirmwareDistributableDescr_Object = MibTableColumn
cucsFirmwareDistributableDescr = _CucsFirmwareDistributableDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 24),
    _CucsFirmwareDistributableDescr_Type()
)
cucsFirmwareDistributableDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableDescr.setStatus("current")
_CucsFirmwareDistributableIntId_Type = SnmpAdminString
_CucsFirmwareDistributableIntId_Object = MibTableColumn
cucsFirmwareDistributableIntId = _CucsFirmwareDistributableIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 25),
    _CucsFirmwareDistributableIntId_Type()
)
cucsFirmwareDistributableIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableIntId.setStatus("current")
_CucsFirmwareDistributablePolicyLevel_Type = Gauge32
_CucsFirmwareDistributablePolicyLevel_Object = MibTableColumn
cucsFirmwareDistributablePolicyLevel = _CucsFirmwareDistributablePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 26),
    _CucsFirmwareDistributablePolicyLevel_Type()
)
cucsFirmwareDistributablePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributablePolicyLevel.setStatus("current")
_CucsFirmwareDistributablePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFirmwareDistributablePolicyOwner_Object = MibTableColumn
cucsFirmwareDistributablePolicyOwner = _CucsFirmwareDistributablePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 10, 1, 27),
    _CucsFirmwareDistributablePolicyOwner_Type()
)
cucsFirmwareDistributablePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributablePolicyOwner.setStatus("current")
_CucsFirmwareDistributableFsmTaskTable_Object = MibTable
cucsFirmwareDistributableFsmTaskTable = _CucsFirmwareDistributableFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 11)
)
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmTaskTable.setStatus("current")
_CucsFirmwareDistributableFsmTaskEntry_Object = MibTableRow
cucsFirmwareDistributableFsmTaskEntry = _CucsFirmwareDistributableFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 11, 1)
)
cucsFirmwareDistributableFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareDistributableFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmTaskEntry.setStatus("current")
_CucsFirmwareDistributableFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsFirmwareDistributableFsmTaskInstanceId_Object = MibTableColumn
cucsFirmwareDistributableFsmTaskInstanceId = _CucsFirmwareDistributableFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 11, 1, 1),
    _CucsFirmwareDistributableFsmTaskInstanceId_Type()
)
cucsFirmwareDistributableFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmTaskInstanceId.setStatus("current")
_CucsFirmwareDistributableFsmTaskDn_Type = CucsManagedObjectDn
_CucsFirmwareDistributableFsmTaskDn_Object = MibTableColumn
cucsFirmwareDistributableFsmTaskDn = _CucsFirmwareDistributableFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 11, 1, 2),
    _CucsFirmwareDistributableFsmTaskDn_Type()
)
cucsFirmwareDistributableFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmTaskDn.setStatus("current")
_CucsFirmwareDistributableFsmTaskRn_Type = SnmpAdminString
_CucsFirmwareDistributableFsmTaskRn_Object = MibTableColumn
cucsFirmwareDistributableFsmTaskRn = _CucsFirmwareDistributableFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 11, 1, 3),
    _CucsFirmwareDistributableFsmTaskRn_Type()
)
cucsFirmwareDistributableFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmTaskRn.setStatus("current")
_CucsFirmwareDistributableFsmTaskCompletion_Type = CucsFsmCompletion
_CucsFirmwareDistributableFsmTaskCompletion_Object = MibTableColumn
cucsFirmwareDistributableFsmTaskCompletion = _CucsFirmwareDistributableFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 11, 1, 4),
    _CucsFirmwareDistributableFsmTaskCompletion_Type()
)
cucsFirmwareDistributableFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmTaskCompletion.setStatus("current")
_CucsFirmwareDistributableFsmTaskFlags_Type = CucsFsmFlags
_CucsFirmwareDistributableFsmTaskFlags_Object = MibTableColumn
cucsFirmwareDistributableFsmTaskFlags = _CucsFirmwareDistributableFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 11, 1, 5),
    _CucsFirmwareDistributableFsmTaskFlags_Type()
)
cucsFirmwareDistributableFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmTaskFlags.setStatus("current")
_CucsFirmwareDistributableFsmTaskItem_Type = CucsFirmwareDistributableFsmTaskItem
_CucsFirmwareDistributableFsmTaskItem_Object = MibTableColumn
cucsFirmwareDistributableFsmTaskItem = _CucsFirmwareDistributableFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 11, 1, 6),
    _CucsFirmwareDistributableFsmTaskItem_Type()
)
cucsFirmwareDistributableFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmTaskItem.setStatus("current")
_CucsFirmwareDistributableFsmTaskSeqId_Type = Gauge32
_CucsFirmwareDistributableFsmTaskSeqId_Object = MibTableColumn
cucsFirmwareDistributableFsmTaskSeqId = _CucsFirmwareDistributableFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 11, 1, 7),
    _CucsFirmwareDistributableFsmTaskSeqId_Type()
)
cucsFirmwareDistributableFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmTaskSeqId.setStatus("current")
_CucsFirmwareDownloaderTable_Object = MibTable
cucsFirmwareDownloaderTable = _CucsFirmwareDownloaderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12)
)
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderTable.setStatus("current")
_CucsFirmwareDownloaderEntry_Object = MibTableRow
cucsFirmwareDownloaderEntry = _CucsFirmwareDownloaderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1)
)
cucsFirmwareDownloaderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareDownloaderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderEntry.setStatus("current")
_CucsFirmwareDownloaderInstanceId_Type = CucsManagedObjectId
_CucsFirmwareDownloaderInstanceId_Object = MibTableColumn
cucsFirmwareDownloaderInstanceId = _CucsFirmwareDownloaderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 1),
    _CucsFirmwareDownloaderInstanceId_Type()
)
cucsFirmwareDownloaderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderInstanceId.setStatus("current")
_CucsFirmwareDownloaderDn_Type = CucsManagedObjectDn
_CucsFirmwareDownloaderDn_Object = MibTableColumn
cucsFirmwareDownloaderDn = _CucsFirmwareDownloaderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 2),
    _CucsFirmwareDownloaderDn_Type()
)
cucsFirmwareDownloaderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderDn.setStatus("current")
_CucsFirmwareDownloaderRn_Type = SnmpAdminString
_CucsFirmwareDownloaderRn_Object = MibTableColumn
cucsFirmwareDownloaderRn = _CucsFirmwareDownloaderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 3),
    _CucsFirmwareDownloaderRn_Type()
)
cucsFirmwareDownloaderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderRn.setStatus("current")
_CucsFirmwareDownloaderAdminState_Type = CucsFirmwareDownloadActivity
_CucsFirmwareDownloaderAdminState_Object = MibTableColumn
cucsFirmwareDownloaderAdminState = _CucsFirmwareDownloaderAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 4),
    _CucsFirmwareDownloaderAdminState_Type()
)
cucsFirmwareDownloaderAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderAdminState.setStatus("current")
_CucsFirmwareDownloaderFileName_Type = SnmpAdminString
_CucsFirmwareDownloaderFileName_Object = MibTableColumn
cucsFirmwareDownloaderFileName = _CucsFirmwareDownloaderFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 5),
    _CucsFirmwareDownloaderFileName_Type()
)
cucsFirmwareDownloaderFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFileName.setStatus("current")
_CucsFirmwareDownloaderFsmDescr_Type = SnmpAdminString
_CucsFirmwareDownloaderFsmDescr_Object = MibTableColumn
cucsFirmwareDownloaderFsmDescr = _CucsFirmwareDownloaderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 6),
    _CucsFirmwareDownloaderFsmDescr_Type()
)
cucsFirmwareDownloaderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmDescr.setStatus("current")
_CucsFirmwareDownloaderFsmPrev_Type = SnmpAdminString
_CucsFirmwareDownloaderFsmPrev_Object = MibTableColumn
cucsFirmwareDownloaderFsmPrev = _CucsFirmwareDownloaderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 7),
    _CucsFirmwareDownloaderFsmPrev_Type()
)
cucsFirmwareDownloaderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmPrev.setStatus("current")
_CucsFirmwareDownloaderFsmProgr_Type = Gauge32
_CucsFirmwareDownloaderFsmProgr_Object = MibTableColumn
cucsFirmwareDownloaderFsmProgr = _CucsFirmwareDownloaderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 8),
    _CucsFirmwareDownloaderFsmProgr_Type()
)
cucsFirmwareDownloaderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmProgr.setStatus("current")
_CucsFirmwareDownloaderFsmRmtInvErrCode_Type = Gauge32
_CucsFirmwareDownloaderFsmRmtInvErrCode_Object = MibTableColumn
cucsFirmwareDownloaderFsmRmtInvErrCode = _CucsFirmwareDownloaderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 9),
    _CucsFirmwareDownloaderFsmRmtInvErrCode_Type()
)
cucsFirmwareDownloaderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmRmtInvErrCode.setStatus("current")
_CucsFirmwareDownloaderFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsFirmwareDownloaderFsmRmtInvErrDescr_Object = MibTableColumn
cucsFirmwareDownloaderFsmRmtInvErrDescr = _CucsFirmwareDownloaderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 10),
    _CucsFirmwareDownloaderFsmRmtInvErrDescr_Type()
)
cucsFirmwareDownloaderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmRmtInvErrDescr.setStatus("current")
_CucsFirmwareDownloaderFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsFirmwareDownloaderFsmRmtInvRslt_Object = MibTableColumn
cucsFirmwareDownloaderFsmRmtInvRslt = _CucsFirmwareDownloaderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 11),
    _CucsFirmwareDownloaderFsmRmtInvRslt_Type()
)
cucsFirmwareDownloaderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmRmtInvRslt.setStatus("current")
_CucsFirmwareDownloaderFsmStageDescr_Type = SnmpAdminString
_CucsFirmwareDownloaderFsmStageDescr_Object = MibTableColumn
cucsFirmwareDownloaderFsmStageDescr = _CucsFirmwareDownloaderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 12),
    _CucsFirmwareDownloaderFsmStageDescr_Type()
)
cucsFirmwareDownloaderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStageDescr.setStatus("current")
_CucsFirmwareDownloaderFsmStamp_Type = DateAndTime
_CucsFirmwareDownloaderFsmStamp_Object = MibTableColumn
cucsFirmwareDownloaderFsmStamp = _CucsFirmwareDownloaderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 13),
    _CucsFirmwareDownloaderFsmStamp_Type()
)
cucsFirmwareDownloaderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStamp.setStatus("current")
_CucsFirmwareDownloaderFsmStatus_Type = SnmpAdminString
_CucsFirmwareDownloaderFsmStatus_Object = MibTableColumn
cucsFirmwareDownloaderFsmStatus = _CucsFirmwareDownloaderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 14),
    _CucsFirmwareDownloaderFsmStatus_Type()
)
cucsFirmwareDownloaderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStatus.setStatus("current")
_CucsFirmwareDownloaderFsmTry_Type = Gauge32
_CucsFirmwareDownloaderFsmTry_Object = MibTableColumn
cucsFirmwareDownloaderFsmTry = _CucsFirmwareDownloaderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 15),
    _CucsFirmwareDownloaderFsmTry_Type()
)
cucsFirmwareDownloaderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmTry.setStatus("current")
_CucsFirmwareDownloaderImageSize_Type = Gauge32
_CucsFirmwareDownloaderImageSize_Object = MibTableColumn
cucsFirmwareDownloaderImageSize = _CucsFirmwareDownloaderImageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 16),
    _CucsFirmwareDownloaderImageSize_Type()
)
cucsFirmwareDownloaderImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderImageSize.setStatus("current")
_CucsFirmwareDownloaderProtocol_Type = CucsFirmwareTransport
_CucsFirmwareDownloaderProtocol_Object = MibTableColumn
cucsFirmwareDownloaderProtocol = _CucsFirmwareDownloaderProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 17),
    _CucsFirmwareDownloaderProtocol_Type()
)
cucsFirmwareDownloaderProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderProtocol.setStatus("current")
_CucsFirmwareDownloaderPwd_Type = SnmpAdminString
_CucsFirmwareDownloaderPwd_Object = MibTableColumn
cucsFirmwareDownloaderPwd = _CucsFirmwareDownloaderPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 18),
    _CucsFirmwareDownloaderPwd_Type()
)
cucsFirmwareDownloaderPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderPwd.setStatus("current")
_CucsFirmwareDownloaderRemotePath_Type = SnmpAdminString
_CucsFirmwareDownloaderRemotePath_Object = MibTableColumn
cucsFirmwareDownloaderRemotePath = _CucsFirmwareDownloaderRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 19),
    _CucsFirmwareDownloaderRemotePath_Type()
)
cucsFirmwareDownloaderRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderRemotePath.setStatus("current")
_CucsFirmwareDownloaderServer_Type = SnmpAdminString
_CucsFirmwareDownloaderServer_Object = MibTableColumn
cucsFirmwareDownloaderServer = _CucsFirmwareDownloaderServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 20),
    _CucsFirmwareDownloaderServer_Type()
)
cucsFirmwareDownloaderServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderServer.setStatus("current")
_CucsFirmwareDownloaderTransferState_Type = CucsFirmwareTransferState
_CucsFirmwareDownloaderTransferState_Object = MibTableColumn
cucsFirmwareDownloaderTransferState = _CucsFirmwareDownloaderTransferState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 21),
    _CucsFirmwareDownloaderTransferState_Type()
)
cucsFirmwareDownloaderTransferState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderTransferState.setStatus("current")
_CucsFirmwareDownloaderUser_Type = SnmpAdminString
_CucsFirmwareDownloaderUser_Object = MibTableColumn
cucsFirmwareDownloaderUser = _CucsFirmwareDownloaderUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 12, 1, 22),
    _CucsFirmwareDownloaderUser_Type()
)
cucsFirmwareDownloaderUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderUser.setStatus("current")
_CucsFirmwareDownloaderFsmTaskTable_Object = MibTable
cucsFirmwareDownloaderFsmTaskTable = _CucsFirmwareDownloaderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 13)
)
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmTaskTable.setStatus("current")
_CucsFirmwareDownloaderFsmTaskEntry_Object = MibTableRow
cucsFirmwareDownloaderFsmTaskEntry = _CucsFirmwareDownloaderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 13, 1)
)
cucsFirmwareDownloaderFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareDownloaderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmTaskEntry.setStatus("current")
_CucsFirmwareDownloaderFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsFirmwareDownloaderFsmTaskInstanceId_Object = MibTableColumn
cucsFirmwareDownloaderFsmTaskInstanceId = _CucsFirmwareDownloaderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 13, 1, 1),
    _CucsFirmwareDownloaderFsmTaskInstanceId_Type()
)
cucsFirmwareDownloaderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmTaskInstanceId.setStatus("current")
_CucsFirmwareDownloaderFsmTaskDn_Type = CucsManagedObjectDn
_CucsFirmwareDownloaderFsmTaskDn_Object = MibTableColumn
cucsFirmwareDownloaderFsmTaskDn = _CucsFirmwareDownloaderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 13, 1, 2),
    _CucsFirmwareDownloaderFsmTaskDn_Type()
)
cucsFirmwareDownloaderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmTaskDn.setStatus("current")
_CucsFirmwareDownloaderFsmTaskRn_Type = SnmpAdminString
_CucsFirmwareDownloaderFsmTaskRn_Object = MibTableColumn
cucsFirmwareDownloaderFsmTaskRn = _CucsFirmwareDownloaderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 13, 1, 3),
    _CucsFirmwareDownloaderFsmTaskRn_Type()
)
cucsFirmwareDownloaderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmTaskRn.setStatus("current")
_CucsFirmwareDownloaderFsmTaskCompletion_Type = CucsFsmCompletion
_CucsFirmwareDownloaderFsmTaskCompletion_Object = MibTableColumn
cucsFirmwareDownloaderFsmTaskCompletion = _CucsFirmwareDownloaderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 13, 1, 4),
    _CucsFirmwareDownloaderFsmTaskCompletion_Type()
)
cucsFirmwareDownloaderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmTaskCompletion.setStatus("current")
_CucsFirmwareDownloaderFsmTaskFlags_Type = CucsFsmFlags
_CucsFirmwareDownloaderFsmTaskFlags_Object = MibTableColumn
cucsFirmwareDownloaderFsmTaskFlags = _CucsFirmwareDownloaderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 13, 1, 5),
    _CucsFirmwareDownloaderFsmTaskFlags_Type()
)
cucsFirmwareDownloaderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmTaskFlags.setStatus("current")
_CucsFirmwareDownloaderFsmTaskItem_Type = CucsFirmwareDownloaderFsmTaskItem
_CucsFirmwareDownloaderFsmTaskItem_Object = MibTableColumn
cucsFirmwareDownloaderFsmTaskItem = _CucsFirmwareDownloaderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 13, 1, 6),
    _CucsFirmwareDownloaderFsmTaskItem_Type()
)
cucsFirmwareDownloaderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmTaskItem.setStatus("current")
_CucsFirmwareDownloaderFsmTaskSeqId_Type = Gauge32
_CucsFirmwareDownloaderFsmTaskSeqId_Object = MibTableColumn
cucsFirmwareDownloaderFsmTaskSeqId = _CucsFirmwareDownloaderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 13, 1, 7),
    _CucsFirmwareDownloaderFsmTaskSeqId_Type()
)
cucsFirmwareDownloaderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmTaskSeqId.setStatus("current")
_CucsFirmwareImageTable_Object = MibTable
cucsFirmwareImageTable = _CucsFirmwareImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14)
)
if mibBuilder.loadTexts:
    cucsFirmwareImageTable.setStatus("current")
_CucsFirmwareImageEntry_Object = MibTableRow
cucsFirmwareImageEntry = _CucsFirmwareImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1)
)
cucsFirmwareImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareImageEntry.setStatus("current")
_CucsFirmwareImageInstanceId_Type = CucsManagedObjectId
_CucsFirmwareImageInstanceId_Object = MibTableColumn
cucsFirmwareImageInstanceId = _CucsFirmwareImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 1),
    _CucsFirmwareImageInstanceId_Type()
)
cucsFirmwareImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareImageInstanceId.setStatus("current")
_CucsFirmwareImageDn_Type = CucsManagedObjectDn
_CucsFirmwareImageDn_Object = MibTableColumn
cucsFirmwareImageDn = _CucsFirmwareImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 2),
    _CucsFirmwareImageDn_Type()
)
cucsFirmwareImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageDn.setStatus("current")
_CucsFirmwareImageRn_Type = SnmpAdminString
_CucsFirmwareImageRn_Object = MibTableColumn
cucsFirmwareImageRn = _CucsFirmwareImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 3),
    _CucsFirmwareImageRn_Type()
)
cucsFirmwareImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageRn.setStatus("current")
_CucsFirmwareImageAdminState_Type = CucsFirmwareAdminState
_CucsFirmwareImageAdminState_Object = MibTableColumn
cucsFirmwareImageAdminState = _CucsFirmwareImageAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 4),
    _CucsFirmwareImageAdminState_Type()
)
cucsFirmwareImageAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageAdminState.setStatus("current")
_CucsFirmwareImageChecksum_Type = SnmpAdminString
_CucsFirmwareImageChecksum_Object = MibTableColumn
cucsFirmwareImageChecksum = _CucsFirmwareImageChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 5),
    _CucsFirmwareImageChecksum_Type()
)
cucsFirmwareImageChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageChecksum.setStatus("current")
_CucsFirmwareImageDownloadDate_Type = DateAndTime
_CucsFirmwareImageDownloadDate_Object = MibTableColumn
cucsFirmwareImageDownloadDate = _CucsFirmwareImageDownloadDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 6),
    _CucsFirmwareImageDownloadDate_Type()
)
cucsFirmwareImageDownloadDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageDownloadDate.setStatus("current")
_CucsFirmwareImageFsmDescr_Type = SnmpAdminString
_CucsFirmwareImageFsmDescr_Object = MibTableColumn
cucsFirmwareImageFsmDescr = _CucsFirmwareImageFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 7),
    _CucsFirmwareImageFsmDescr_Type()
)
cucsFirmwareImageFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmDescr.setStatus("current")
_CucsFirmwareImageFsmPrev_Type = SnmpAdminString
_CucsFirmwareImageFsmPrev_Object = MibTableColumn
cucsFirmwareImageFsmPrev = _CucsFirmwareImageFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 8),
    _CucsFirmwareImageFsmPrev_Type()
)
cucsFirmwareImageFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmPrev.setStatus("current")
_CucsFirmwareImageFsmProgr_Type = Gauge32
_CucsFirmwareImageFsmProgr_Object = MibTableColumn
cucsFirmwareImageFsmProgr = _CucsFirmwareImageFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 9),
    _CucsFirmwareImageFsmProgr_Type()
)
cucsFirmwareImageFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmProgr.setStatus("current")
_CucsFirmwareImageFsmRmtInvErrCode_Type = Gauge32
_CucsFirmwareImageFsmRmtInvErrCode_Object = MibTableColumn
cucsFirmwareImageFsmRmtInvErrCode = _CucsFirmwareImageFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 10),
    _CucsFirmwareImageFsmRmtInvErrCode_Type()
)
cucsFirmwareImageFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmRmtInvErrCode.setStatus("current")
_CucsFirmwareImageFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsFirmwareImageFsmRmtInvErrDescr_Object = MibTableColumn
cucsFirmwareImageFsmRmtInvErrDescr = _CucsFirmwareImageFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 11),
    _CucsFirmwareImageFsmRmtInvErrDescr_Type()
)
cucsFirmwareImageFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmRmtInvErrDescr.setStatus("current")
_CucsFirmwareImageFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsFirmwareImageFsmRmtInvRslt_Object = MibTableColumn
cucsFirmwareImageFsmRmtInvRslt = _CucsFirmwareImageFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 12),
    _CucsFirmwareImageFsmRmtInvRslt_Type()
)
cucsFirmwareImageFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmRmtInvRslt.setStatus("current")
_CucsFirmwareImageFsmStageDescr_Type = SnmpAdminString
_CucsFirmwareImageFsmStageDescr_Object = MibTableColumn
cucsFirmwareImageFsmStageDescr = _CucsFirmwareImageFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 13),
    _CucsFirmwareImageFsmStageDescr_Type()
)
cucsFirmwareImageFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStageDescr.setStatus("current")
_CucsFirmwareImageFsmStamp_Type = DateAndTime
_CucsFirmwareImageFsmStamp_Object = MibTableColumn
cucsFirmwareImageFsmStamp = _CucsFirmwareImageFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 14),
    _CucsFirmwareImageFsmStamp_Type()
)
cucsFirmwareImageFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStamp.setStatus("current")
_CucsFirmwareImageFsmStatus_Type = SnmpAdminString
_CucsFirmwareImageFsmStatus_Object = MibTableColumn
cucsFirmwareImageFsmStatus = _CucsFirmwareImageFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 15),
    _CucsFirmwareImageFsmStatus_Type()
)
cucsFirmwareImageFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStatus.setStatus("current")
_CucsFirmwareImageFsmTry_Type = Gauge32
_CucsFirmwareImageFsmTry_Object = MibTableColumn
cucsFirmwareImageFsmTry = _CucsFirmwareImageFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 16),
    _CucsFirmwareImageFsmTry_Type()
)
cucsFirmwareImageFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmTry.setStatus("current")
_CucsFirmwareImageImagePresence_Type = CucsFirmwareImagePresence
_CucsFirmwareImageImagePresence_Object = MibTableColumn
cucsFirmwareImageImagePresence = _CucsFirmwareImageImagePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 17),
    _CucsFirmwareImageImagePresence_Type()
)
cucsFirmwareImageImagePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageImagePresence.setStatus("current")
_CucsFirmwareImageInvTag_Type = SnmpAdminString
_CucsFirmwareImageInvTag_Object = MibTableColumn
cucsFirmwareImageInvTag = _CucsFirmwareImageInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 18),
    _CucsFirmwareImageInvTag_Type()
)
cucsFirmwareImageInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageInvTag.setStatus("current")
_CucsFirmwareImageIsoname_Type = SnmpAdminString
_CucsFirmwareImageIsoname_Object = MibTableColumn
cucsFirmwareImageIsoname = _CucsFirmwareImageIsoname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 19),
    _CucsFirmwareImageIsoname_Type()
)
cucsFirmwareImageIsoname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageIsoname.setStatus("current")
_CucsFirmwareImageLocation_Type = SnmpAdminString
_CucsFirmwareImageLocation_Object = MibTableColumn
cucsFirmwareImageLocation = _CucsFirmwareImageLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 20),
    _CucsFirmwareImageLocation_Type()
)
cucsFirmwareImageLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageLocation.setStatus("current")
_CucsFirmwareImageName_Type = SnmpAdminString
_CucsFirmwareImageName_Object = MibTableColumn
cucsFirmwareImageName = _CucsFirmwareImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 21),
    _CucsFirmwareImageName_Type()
)
cucsFirmwareImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageName.setStatus("current")
_CucsFirmwareImageSize_Type = Gauge32
_CucsFirmwareImageSize_Object = MibTableColumn
cucsFirmwareImageSize = _CucsFirmwareImageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 22),
    _CucsFirmwareImageSize_Type()
)
cucsFirmwareImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageSize.setStatus("current")
_CucsFirmwareImageType_Type = CucsFirmwareType
_CucsFirmwareImageType_Object = MibTableColumn
cucsFirmwareImageType = _CucsFirmwareImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 23),
    _CucsFirmwareImageType_Type()
)
cucsFirmwareImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageType.setStatus("current")
_CucsFirmwareImageVersion_Type = SnmpAdminString
_CucsFirmwareImageVersion_Object = MibTableColumn
cucsFirmwareImageVersion = _CucsFirmwareImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 24),
    _CucsFirmwareImageVersion_Type()
)
cucsFirmwareImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageVersion.setStatus("current")
_CucsFirmwareImageDescr_Type = SnmpAdminString
_CucsFirmwareImageDescr_Object = MibTableColumn
cucsFirmwareImageDescr = _CucsFirmwareImageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 25),
    _CucsFirmwareImageDescr_Type()
)
cucsFirmwareImageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageDescr.setStatus("current")
_CucsFirmwareImageIntId_Type = SnmpAdminString
_CucsFirmwareImageIntId_Object = MibTableColumn
cucsFirmwareImageIntId = _CucsFirmwareImageIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 26),
    _CucsFirmwareImageIntId_Type()
)
cucsFirmwareImageIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageIntId.setStatus("current")
_CucsFirmwareImagePolicyLevel_Type = Gauge32
_CucsFirmwareImagePolicyLevel_Object = MibTableColumn
cucsFirmwareImagePolicyLevel = _CucsFirmwareImagePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 27),
    _CucsFirmwareImagePolicyLevel_Type()
)
cucsFirmwareImagePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImagePolicyLevel.setStatus("current")
_CucsFirmwareImagePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFirmwareImagePolicyOwner_Object = MibTableColumn
cucsFirmwareImagePolicyOwner = _CucsFirmwareImagePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 14, 1, 28),
    _CucsFirmwareImagePolicyOwner_Type()
)
cucsFirmwareImagePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImagePolicyOwner.setStatus("current")
_CucsFirmwareImageFsmTaskTable_Object = MibTable
cucsFirmwareImageFsmTaskTable = _CucsFirmwareImageFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 15)
)
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmTaskTable.setStatus("current")
_CucsFirmwareImageFsmTaskEntry_Object = MibTableRow
cucsFirmwareImageFsmTaskEntry = _CucsFirmwareImageFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 15, 1)
)
cucsFirmwareImageFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareImageFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmTaskEntry.setStatus("current")
_CucsFirmwareImageFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsFirmwareImageFsmTaskInstanceId_Object = MibTableColumn
cucsFirmwareImageFsmTaskInstanceId = _CucsFirmwareImageFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 15, 1, 1),
    _CucsFirmwareImageFsmTaskInstanceId_Type()
)
cucsFirmwareImageFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmTaskInstanceId.setStatus("current")
_CucsFirmwareImageFsmTaskDn_Type = CucsManagedObjectDn
_CucsFirmwareImageFsmTaskDn_Object = MibTableColumn
cucsFirmwareImageFsmTaskDn = _CucsFirmwareImageFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 15, 1, 2),
    _CucsFirmwareImageFsmTaskDn_Type()
)
cucsFirmwareImageFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmTaskDn.setStatus("current")
_CucsFirmwareImageFsmTaskRn_Type = SnmpAdminString
_CucsFirmwareImageFsmTaskRn_Object = MibTableColumn
cucsFirmwareImageFsmTaskRn = _CucsFirmwareImageFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 15, 1, 3),
    _CucsFirmwareImageFsmTaskRn_Type()
)
cucsFirmwareImageFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmTaskRn.setStatus("current")
_CucsFirmwareImageFsmTaskCompletion_Type = CucsFsmCompletion
_CucsFirmwareImageFsmTaskCompletion_Object = MibTableColumn
cucsFirmwareImageFsmTaskCompletion = _CucsFirmwareImageFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 15, 1, 4),
    _CucsFirmwareImageFsmTaskCompletion_Type()
)
cucsFirmwareImageFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmTaskCompletion.setStatus("current")
_CucsFirmwareImageFsmTaskFlags_Type = CucsFsmFlags
_CucsFirmwareImageFsmTaskFlags_Object = MibTableColumn
cucsFirmwareImageFsmTaskFlags = _CucsFirmwareImageFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 15, 1, 5),
    _CucsFirmwareImageFsmTaskFlags_Type()
)
cucsFirmwareImageFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmTaskFlags.setStatus("current")
_CucsFirmwareImageFsmTaskItem_Type = CucsFirmwareImageFsmTaskItem
_CucsFirmwareImageFsmTaskItem_Object = MibTableColumn
cucsFirmwareImageFsmTaskItem = _CucsFirmwareImageFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 15, 1, 6),
    _CucsFirmwareImageFsmTaskItem_Type()
)
cucsFirmwareImageFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmTaskItem.setStatus("current")
_CucsFirmwareImageFsmTaskSeqId_Type = Gauge32
_CucsFirmwareImageFsmTaskSeqId_Object = MibTableColumn
cucsFirmwareImageFsmTaskSeqId = _CucsFirmwareImageFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 15, 1, 7),
    _CucsFirmwareImageFsmTaskSeqId_Type()
)
cucsFirmwareImageFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmTaskSeqId.setStatus("current")
_CucsFirmwareInstallableTable_Object = MibTable
cucsFirmwareInstallableTable = _CucsFirmwareInstallableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16)
)
if mibBuilder.loadTexts:
    cucsFirmwareInstallableTable.setStatus("current")
_CucsFirmwareInstallableEntry_Object = MibTableRow
cucsFirmwareInstallableEntry = _CucsFirmwareInstallableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1)
)
cucsFirmwareInstallableEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareInstallableInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareInstallableEntry.setStatus("current")
_CucsFirmwareInstallableInstanceId_Type = CucsManagedObjectId
_CucsFirmwareInstallableInstanceId_Object = MibTableColumn
cucsFirmwareInstallableInstanceId = _CucsFirmwareInstallableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 1),
    _CucsFirmwareInstallableInstanceId_Type()
)
cucsFirmwareInstallableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableInstanceId.setStatus("current")
_CucsFirmwareInstallableDn_Type = CucsManagedObjectDn
_CucsFirmwareInstallableDn_Object = MibTableColumn
cucsFirmwareInstallableDn = _CucsFirmwareInstallableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 2),
    _CucsFirmwareInstallableDn_Type()
)
cucsFirmwareInstallableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableDn.setStatus("current")
_CucsFirmwareInstallableRn_Type = SnmpAdminString
_CucsFirmwareInstallableRn_Object = MibTableColumn
cucsFirmwareInstallableRn = _CucsFirmwareInstallableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 3),
    _CucsFirmwareInstallableRn_Type()
)
cucsFirmwareInstallableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableRn.setStatus("current")
_CucsFirmwareInstallableChecksum_Type = SnmpAdminString
_CucsFirmwareInstallableChecksum_Object = MibTableColumn
cucsFirmwareInstallableChecksum = _CucsFirmwareInstallableChecksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 4),
    _CucsFirmwareInstallableChecksum_Type()
)
cucsFirmwareInstallableChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableChecksum.setStatus("current")
_CucsFirmwareInstallableInProgress_Type = Gauge32
_CucsFirmwareInstallableInProgress_Object = MibTableColumn
cucsFirmwareInstallableInProgress = _CucsFirmwareInstallableInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 5),
    _CucsFirmwareInstallableInProgress_Type()
)
cucsFirmwareInstallableInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableInProgress.setStatus("current")
_CucsFirmwareInstallableIsoname_Type = SnmpAdminString
_CucsFirmwareInstallableIsoname_Object = MibTableColumn
cucsFirmwareInstallableIsoname = _CucsFirmwareInstallableIsoname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 6),
    _CucsFirmwareInstallableIsoname_Type()
)
cucsFirmwareInstallableIsoname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableIsoname.setStatus("current")
_CucsFirmwareInstallableLocation_Type = SnmpAdminString
_CucsFirmwareInstallableLocation_Object = MibTableColumn
cucsFirmwareInstallableLocation = _CucsFirmwareInstallableLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 7),
    _CucsFirmwareInstallableLocation_Type()
)
cucsFirmwareInstallableLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableLocation.setStatus("current")
_CucsFirmwareInstallableModel_Type = SnmpAdminString
_CucsFirmwareInstallableModel_Object = MibTableColumn
cucsFirmwareInstallableModel = _CucsFirmwareInstallableModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 8),
    _CucsFirmwareInstallableModel_Type()
)
cucsFirmwareInstallableModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableModel.setStatus("current")
_CucsFirmwareInstallableName_Type = SnmpAdminString
_CucsFirmwareInstallableName_Object = MibTableColumn
cucsFirmwareInstallableName = _CucsFirmwareInstallableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 9),
    _CucsFirmwareInstallableName_Type()
)
cucsFirmwareInstallableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableName.setStatus("current")
_CucsFirmwareInstallableSize_Type = Gauge32
_CucsFirmwareInstallableSize_Object = MibTableColumn
cucsFirmwareInstallableSize = _CucsFirmwareInstallableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 10),
    _CucsFirmwareInstallableSize_Type()
)
cucsFirmwareInstallableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableSize.setStatus("current")
_CucsFirmwareInstallableType_Type = CucsFirmwareType
_CucsFirmwareInstallableType_Object = MibTableColumn
cucsFirmwareInstallableType = _CucsFirmwareInstallableType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 11),
    _CucsFirmwareInstallableType_Type()
)
cucsFirmwareInstallableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableType.setStatus("current")
_CucsFirmwareInstallableVendor_Type = SnmpAdminString
_CucsFirmwareInstallableVendor_Object = MibTableColumn
cucsFirmwareInstallableVendor = _CucsFirmwareInstallableVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 12),
    _CucsFirmwareInstallableVendor_Type()
)
cucsFirmwareInstallableVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableVendor.setStatus("current")
_CucsFirmwareInstallableVersion_Type = SnmpAdminString
_CucsFirmwareInstallableVersion_Object = MibTableColumn
cucsFirmwareInstallableVersion = _CucsFirmwareInstallableVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 16, 1, 13),
    _CucsFirmwareInstallableVersion_Type()
)
cucsFirmwareInstallableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallableVersion.setStatus("current")
_CucsFirmwarePackItemTable_Object = MibTable
cucsFirmwarePackItemTable = _CucsFirmwarePackItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 17)
)
if mibBuilder.loadTexts:
    cucsFirmwarePackItemTable.setStatus("current")
_CucsFirmwarePackItemEntry_Object = MibTableRow
cucsFirmwarePackItemEntry = _CucsFirmwarePackItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 17, 1)
)
cucsFirmwarePackItemEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwarePackItemInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwarePackItemEntry.setStatus("current")
_CucsFirmwarePackItemInstanceId_Type = CucsManagedObjectId
_CucsFirmwarePackItemInstanceId_Object = MibTableColumn
cucsFirmwarePackItemInstanceId = _CucsFirmwarePackItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 17, 1, 1),
    _CucsFirmwarePackItemInstanceId_Type()
)
cucsFirmwarePackItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwarePackItemInstanceId.setStatus("current")
_CucsFirmwarePackItemDn_Type = CucsManagedObjectDn
_CucsFirmwarePackItemDn_Object = MibTableColumn
cucsFirmwarePackItemDn = _CucsFirmwarePackItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 17, 1, 2),
    _CucsFirmwarePackItemDn_Type()
)
cucsFirmwarePackItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePackItemDn.setStatus("current")
_CucsFirmwarePackItemRn_Type = SnmpAdminString
_CucsFirmwarePackItemRn_Object = MibTableColumn
cucsFirmwarePackItemRn = _CucsFirmwarePackItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 17, 1, 3),
    _CucsFirmwarePackItemRn_Type()
)
cucsFirmwarePackItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePackItemRn.setStatus("current")
_CucsFirmwarePackItemHwModel_Type = SnmpAdminString
_CucsFirmwarePackItemHwModel_Object = MibTableColumn
cucsFirmwarePackItemHwModel = _CucsFirmwarePackItemHwModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 17, 1, 4),
    _CucsFirmwarePackItemHwModel_Type()
)
cucsFirmwarePackItemHwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePackItemHwModel.setStatus("current")
_CucsFirmwarePackItemHwVendor_Type = SnmpAdminString
_CucsFirmwarePackItemHwVendor_Object = MibTableColumn
cucsFirmwarePackItemHwVendor = _CucsFirmwarePackItemHwVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 17, 1, 5),
    _CucsFirmwarePackItemHwVendor_Type()
)
cucsFirmwarePackItemHwVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePackItemHwVendor.setStatus("current")
_CucsFirmwarePackItemPresence_Type = CucsFirmwarePackItemPresence
_CucsFirmwarePackItemPresence_Object = MibTableColumn
cucsFirmwarePackItemPresence = _CucsFirmwarePackItemPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 17, 1, 6),
    _CucsFirmwarePackItemPresence_Type()
)
cucsFirmwarePackItemPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePackItemPresence.setStatus("current")
_CucsFirmwarePackItemType_Type = CucsFirmwareItemType
_CucsFirmwarePackItemType_Object = MibTableColumn
cucsFirmwarePackItemType = _CucsFirmwarePackItemType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 17, 1, 7),
    _CucsFirmwarePackItemType_Type()
)
cucsFirmwarePackItemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePackItemType.setStatus("current")
_CucsFirmwarePackItemVersion_Type = SnmpAdminString
_CucsFirmwarePackItemVersion_Object = MibTableColumn
cucsFirmwarePackItemVersion = _CucsFirmwarePackItemVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 17, 1, 8),
    _CucsFirmwarePackItemVersion_Type()
)
cucsFirmwarePackItemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePackItemVersion.setStatus("current")
_CucsFirmwareRunningTable_Object = MibTable
cucsFirmwareRunningTable = _CucsFirmwareRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 18)
)
if mibBuilder.loadTexts:
    cucsFirmwareRunningTable.setStatus("current")
_CucsFirmwareRunningEntry_Object = MibTableRow
cucsFirmwareRunningEntry = _CucsFirmwareRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 18, 1)
)
cucsFirmwareRunningEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareRunningInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareRunningEntry.setStatus("current")
_CucsFirmwareRunningInstanceId_Type = CucsManagedObjectId
_CucsFirmwareRunningInstanceId_Object = MibTableColumn
cucsFirmwareRunningInstanceId = _CucsFirmwareRunningInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 18, 1, 1),
    _CucsFirmwareRunningInstanceId_Type()
)
cucsFirmwareRunningInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareRunningInstanceId.setStatus("current")
_CucsFirmwareRunningDn_Type = CucsManagedObjectDn
_CucsFirmwareRunningDn_Object = MibTableColumn
cucsFirmwareRunningDn = _CucsFirmwareRunningDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 18, 1, 2),
    _CucsFirmwareRunningDn_Type()
)
cucsFirmwareRunningDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareRunningDn.setStatus("current")
_CucsFirmwareRunningRn_Type = SnmpAdminString
_CucsFirmwareRunningRn_Object = MibTableColumn
cucsFirmwareRunningRn = _CucsFirmwareRunningRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 18, 1, 3),
    _CucsFirmwareRunningRn_Type()
)
cucsFirmwareRunningRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareRunningRn.setStatus("current")
_CucsFirmwareRunningDeployment_Type = CucsFirmwareRunningDeployment
_CucsFirmwareRunningDeployment_Object = MibTableColumn
cucsFirmwareRunningDeployment = _CucsFirmwareRunningDeployment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 18, 1, 4),
    _CucsFirmwareRunningDeployment_Type()
)
cucsFirmwareRunningDeployment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareRunningDeployment.setStatus("current")
_CucsFirmwareRunningType_Type = CucsFirmwareType
_CucsFirmwareRunningType_Object = MibTableColumn
cucsFirmwareRunningType = _CucsFirmwareRunningType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 18, 1, 5),
    _CucsFirmwareRunningType_Type()
)
cucsFirmwareRunningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareRunningType.setStatus("current")
_CucsFirmwareRunningVersion_Type = SnmpAdminString
_CucsFirmwareRunningVersion_Object = MibTableColumn
cucsFirmwareRunningVersion = _CucsFirmwareRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 18, 1, 6),
    _CucsFirmwareRunningVersion_Type()
)
cucsFirmwareRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareRunningVersion.setStatus("current")
_CucsFirmwareRunningPackageVersion_Type = SnmpAdminString
_CucsFirmwareRunningPackageVersion_Object = MibTableColumn
cucsFirmwareRunningPackageVersion = _CucsFirmwareRunningPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 18, 1, 7),
    _CucsFirmwareRunningPackageVersion_Type()
)
cucsFirmwareRunningPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareRunningPackageVersion.setStatus("current")
_CucsFirmwareRunningInvTag_Type = SnmpAdminString
_CucsFirmwareRunningInvTag_Object = MibTableColumn
cucsFirmwareRunningInvTag = _CucsFirmwareRunningInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 18, 1, 8),
    _CucsFirmwareRunningInvTag_Type()
)
cucsFirmwareRunningInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareRunningInvTag.setStatus("current")
_CucsFirmwareTypeTable_Object = MibTable
cucsFirmwareTypeTable = _CucsFirmwareTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 19)
)
if mibBuilder.loadTexts:
    cucsFirmwareTypeTable.setStatus("current")
_CucsFirmwareTypeEntry_Object = MibTableRow
cucsFirmwareTypeEntry = _CucsFirmwareTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 19, 1)
)
cucsFirmwareTypeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareTypeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareTypeEntry.setStatus("current")
_CucsFirmwareTypeInstanceId_Type = CucsManagedObjectId
_CucsFirmwareTypeInstanceId_Object = MibTableColumn
cucsFirmwareTypeInstanceId = _CucsFirmwareTypeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 19, 1, 1),
    _CucsFirmwareTypeInstanceId_Type()
)
cucsFirmwareTypeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareTypeInstanceId.setStatus("current")
_CucsFirmwareTypeDn_Type = CucsManagedObjectDn
_CucsFirmwareTypeDn_Object = MibTableColumn
cucsFirmwareTypeDn = _CucsFirmwareTypeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 19, 1, 2),
    _CucsFirmwareTypeDn_Type()
)
cucsFirmwareTypeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareTypeDn.setStatus("current")
_CucsFirmwareTypeRn_Type = SnmpAdminString
_CucsFirmwareTypeRn_Object = MibTableColumn
cucsFirmwareTypeRn = _CucsFirmwareTypeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 19, 1, 3),
    _CucsFirmwareTypeRn_Type()
)
cucsFirmwareTypeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareTypeRn.setStatus("current")
_CucsFirmwareTypeEp_Type = CucsFirmwareType
_CucsFirmwareTypeEp_Object = MibTableColumn
cucsFirmwareTypeEp = _CucsFirmwareTypeEp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 19, 1, 4),
    _CucsFirmwareTypeEp_Type()
)
cucsFirmwareTypeEp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareTypeEp.setStatus("current")
_CucsFirmwareTypeInvTag_Type = SnmpAdminString
_CucsFirmwareTypeInvTag_Object = MibTableColumn
cucsFirmwareTypeInvTag = _CucsFirmwareTypeInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 19, 1, 5),
    _CucsFirmwareTypeInvTag_Type()
)
cucsFirmwareTypeInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareTypeInvTag.setStatus("current")
_CucsFirmwareTypeMaxVer_Type = SnmpAdminString
_CucsFirmwareTypeMaxVer_Object = MibTableColumn
cucsFirmwareTypeMaxVer = _CucsFirmwareTypeMaxVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 19, 1, 6),
    _CucsFirmwareTypeMaxVer_Type()
)
cucsFirmwareTypeMaxVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareTypeMaxVer.setStatus("current")
_CucsFirmwareTypeMinVer_Type = SnmpAdminString
_CucsFirmwareTypeMinVer_Object = MibTableColumn
cucsFirmwareTypeMinVer = _CucsFirmwareTypeMinVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 19, 1, 7),
    _CucsFirmwareTypeMinVer_Type()
)
cucsFirmwareTypeMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareTypeMinVer.setStatus("current")
_CucsFirmwareTypeFwFpgaRevisionSupported_Type = TruthValue
_CucsFirmwareTypeFwFpgaRevisionSupported_Object = MibTableColumn
cucsFirmwareTypeFwFpgaRevisionSupported = _CucsFirmwareTypeFwFpgaRevisionSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 19, 1, 9),
    _CucsFirmwareTypeFwFpgaRevisionSupported_Type()
)
cucsFirmwareTypeFwFpgaRevisionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareTypeFwFpgaRevisionSupported.setStatus("current")
_CucsFirmwareUpdatableTable_Object = MibTable
cucsFirmwareUpdatableTable = _CucsFirmwareUpdatableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 20)
)
if mibBuilder.loadTexts:
    cucsFirmwareUpdatableTable.setStatus("current")
_CucsFirmwareUpdatableEntry_Object = MibTableRow
cucsFirmwareUpdatableEntry = _CucsFirmwareUpdatableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 20, 1)
)
cucsFirmwareUpdatableEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareUpdatableInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareUpdatableEntry.setStatus("current")
_CucsFirmwareUpdatableInstanceId_Type = CucsManagedObjectId
_CucsFirmwareUpdatableInstanceId_Object = MibTableColumn
cucsFirmwareUpdatableInstanceId = _CucsFirmwareUpdatableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 20, 1, 1),
    _CucsFirmwareUpdatableInstanceId_Type()
)
cucsFirmwareUpdatableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareUpdatableInstanceId.setStatus("current")
_CucsFirmwareUpdatableDn_Type = CucsManagedObjectDn
_CucsFirmwareUpdatableDn_Object = MibTableColumn
cucsFirmwareUpdatableDn = _CucsFirmwareUpdatableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 20, 1, 2),
    _CucsFirmwareUpdatableDn_Type()
)
cucsFirmwareUpdatableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpdatableDn.setStatus("current")
_CucsFirmwareUpdatableRn_Type = SnmpAdminString
_CucsFirmwareUpdatableRn_Object = MibTableColumn
cucsFirmwareUpdatableRn = _CucsFirmwareUpdatableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 20, 1, 3),
    _CucsFirmwareUpdatableRn_Type()
)
cucsFirmwareUpdatableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpdatableRn.setStatus("current")
_CucsFirmwareUpdatableAdminState_Type = CucsFirmwareTriggerState
_CucsFirmwareUpdatableAdminState_Object = MibTableColumn
cucsFirmwareUpdatableAdminState = _CucsFirmwareUpdatableAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 20, 1, 4),
    _CucsFirmwareUpdatableAdminState_Type()
)
cucsFirmwareUpdatableAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpdatableAdminState.setStatus("current")
_CucsFirmwareUpdatableDeployment_Type = CucsFirmwareUpdatableDeployment
_CucsFirmwareUpdatableDeployment_Object = MibTableColumn
cucsFirmwareUpdatableDeployment = _CucsFirmwareUpdatableDeployment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 20, 1, 5),
    _CucsFirmwareUpdatableDeployment_Type()
)
cucsFirmwareUpdatableDeployment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpdatableDeployment.setStatus("current")
_CucsFirmwareUpdatableOperState_Type = CucsFirmwareImageState
_CucsFirmwareUpdatableOperState_Object = MibTableColumn
cucsFirmwareUpdatableOperState = _CucsFirmwareUpdatableOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 20, 1, 6),
    _CucsFirmwareUpdatableOperState_Type()
)
cucsFirmwareUpdatableOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpdatableOperState.setStatus("current")
_CucsFirmwareUpdatableOperStateQual_Type = CucsFirmwareImageError
_CucsFirmwareUpdatableOperStateQual_Object = MibTableColumn
cucsFirmwareUpdatableOperStateQual = _CucsFirmwareUpdatableOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 20, 1, 7),
    _CucsFirmwareUpdatableOperStateQual_Type()
)
cucsFirmwareUpdatableOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpdatableOperStateQual.setStatus("current")
_CucsFirmwareUpdatablePrevVersion_Type = SnmpAdminString
_CucsFirmwareUpdatablePrevVersion_Object = MibTableColumn
cucsFirmwareUpdatablePrevVersion = _CucsFirmwareUpdatablePrevVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 20, 1, 8),
    _CucsFirmwareUpdatablePrevVersion_Type()
)
cucsFirmwareUpdatablePrevVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpdatablePrevVersion.setStatus("current")
_CucsFirmwareUpdatableVersion_Type = SnmpAdminString
_CucsFirmwareUpdatableVersion_Object = MibTableColumn
cucsFirmwareUpdatableVersion = _CucsFirmwareUpdatableVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 20, 1, 9),
    _CucsFirmwareUpdatableVersion_Type()
)
cucsFirmwareUpdatableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpdatableVersion.setStatus("current")
_CucsFirmwareBundleTypeTable_Object = MibTable
cucsFirmwareBundleTypeTable = _CucsFirmwareBundleTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 21)
)
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeTable.setStatus("current")
_CucsFirmwareBundleTypeEntry_Object = MibTableRow
cucsFirmwareBundleTypeEntry = _CucsFirmwareBundleTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 21, 1)
)
cucsFirmwareBundleTypeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareBundleTypeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeEntry.setStatus("current")
_CucsFirmwareBundleTypeInstanceId_Type = CucsManagedObjectId
_CucsFirmwareBundleTypeInstanceId_Object = MibTableColumn
cucsFirmwareBundleTypeInstanceId = _CucsFirmwareBundleTypeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 21, 1, 1),
    _CucsFirmwareBundleTypeInstanceId_Type()
)
cucsFirmwareBundleTypeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeInstanceId.setStatus("current")
_CucsFirmwareBundleTypeDn_Type = CucsManagedObjectDn
_CucsFirmwareBundleTypeDn_Object = MibTableColumn
cucsFirmwareBundleTypeDn = _CucsFirmwareBundleTypeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 21, 1, 2),
    _CucsFirmwareBundleTypeDn_Type()
)
cucsFirmwareBundleTypeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeDn.setStatus("current")
_CucsFirmwareBundleTypeRn_Type = SnmpAdminString
_CucsFirmwareBundleTypeRn_Object = MibTableColumn
cucsFirmwareBundleTypeRn = _CucsFirmwareBundleTypeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 21, 1, 3),
    _CucsFirmwareBundleTypeRn_Type()
)
cucsFirmwareBundleTypeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeRn.setStatus("current")
_CucsFirmwareBundleTypeInvTag_Type = SnmpAdminString
_CucsFirmwareBundleTypeInvTag_Object = MibTableColumn
cucsFirmwareBundleTypeInvTag = _CucsFirmwareBundleTypeInvTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 21, 1, 4),
    _CucsFirmwareBundleTypeInvTag_Type()
)
cucsFirmwareBundleTypeInvTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeInvTag.setStatus("current")
_CucsFirmwareBundleTypeType_Type = CucsFirmwareDistributableType
_CucsFirmwareBundleTypeType_Object = MibTableColumn
cucsFirmwareBundleTypeType = _CucsFirmwareBundleTypeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 21, 1, 5),
    _CucsFirmwareBundleTypeType_Type()
)
cucsFirmwareBundleTypeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeType.setStatus("current")
_CucsFirmwareBundleTypeCapProviderTable_Object = MibTable
cucsFirmwareBundleTypeCapProviderTable = _CucsFirmwareBundleTypeCapProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22)
)
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderTable.setStatus("current")
_CucsFirmwareBundleTypeCapProviderEntry_Object = MibTableRow
cucsFirmwareBundleTypeCapProviderEntry = _CucsFirmwareBundleTypeCapProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1)
)
cucsFirmwareBundleTypeCapProviderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareBundleTypeCapProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderEntry.setStatus("current")
_CucsFirmwareBundleTypeCapProviderInstanceId_Type = CucsManagedObjectId
_CucsFirmwareBundleTypeCapProviderInstanceId_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderInstanceId = _CucsFirmwareBundleTypeCapProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 1),
    _CucsFirmwareBundleTypeCapProviderInstanceId_Type()
)
cucsFirmwareBundleTypeCapProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderInstanceId.setStatus("current")
_CucsFirmwareBundleTypeCapProviderDn_Type = CucsManagedObjectDn
_CucsFirmwareBundleTypeCapProviderDn_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderDn = _CucsFirmwareBundleTypeCapProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 2),
    _CucsFirmwareBundleTypeCapProviderDn_Type()
)
cucsFirmwareBundleTypeCapProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderDn.setStatus("current")
_CucsFirmwareBundleTypeCapProviderRn_Type = SnmpAdminString
_CucsFirmwareBundleTypeCapProviderRn_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderRn = _CucsFirmwareBundleTypeCapProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 3),
    _CucsFirmwareBundleTypeCapProviderRn_Type()
)
cucsFirmwareBundleTypeCapProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderRn.setStatus("current")
_CucsFirmwareBundleTypeCapProviderDeleted_Type = TruthValue
_CucsFirmwareBundleTypeCapProviderDeleted_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderDeleted = _CucsFirmwareBundleTypeCapProviderDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 4),
    _CucsFirmwareBundleTypeCapProviderDeleted_Type()
)
cucsFirmwareBundleTypeCapProviderDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderDeleted.setStatus("current")
_CucsFirmwareBundleTypeCapProviderDeprecated_Type = TruthValue
_CucsFirmwareBundleTypeCapProviderDeprecated_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderDeprecated = _CucsFirmwareBundleTypeCapProviderDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 5),
    _CucsFirmwareBundleTypeCapProviderDeprecated_Type()
)
cucsFirmwareBundleTypeCapProviderDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderDeprecated.setStatus("current")
_CucsFirmwareBundleTypeCapProviderGencount_Type = Gauge32
_CucsFirmwareBundleTypeCapProviderGencount_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderGencount = _CucsFirmwareBundleTypeCapProviderGencount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 6),
    _CucsFirmwareBundleTypeCapProviderGencount_Type()
)
cucsFirmwareBundleTypeCapProviderGencount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderGencount.setStatus("current")
_CucsFirmwareBundleTypeCapProviderMgmtPlaneVer_Type = SnmpAdminString
_CucsFirmwareBundleTypeCapProviderMgmtPlaneVer_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderMgmtPlaneVer = _CucsFirmwareBundleTypeCapProviderMgmtPlaneVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 7),
    _CucsFirmwareBundleTypeCapProviderMgmtPlaneVer_Type()
)
cucsFirmwareBundleTypeCapProviderMgmtPlaneVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderMgmtPlaneVer.setStatus("current")
_CucsFirmwareBundleTypeCapProviderModel_Type = SnmpAdminString
_CucsFirmwareBundleTypeCapProviderModel_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderModel = _CucsFirmwareBundleTypeCapProviderModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 8),
    _CucsFirmwareBundleTypeCapProviderModel_Type()
)
cucsFirmwareBundleTypeCapProviderModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderModel.setStatus("current")
_CucsFirmwareBundleTypeCapProviderVendor_Type = SnmpAdminString
_CucsFirmwareBundleTypeCapProviderVendor_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderVendor = _CucsFirmwareBundleTypeCapProviderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 9),
    _CucsFirmwareBundleTypeCapProviderVendor_Type()
)
cucsFirmwareBundleTypeCapProviderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderVendor.setStatus("current")
_CucsFirmwareBundleTypeCapProviderElementLoadFailures_Type = Gauge32
_CucsFirmwareBundleTypeCapProviderElementLoadFailures_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderElementLoadFailures = _CucsFirmwareBundleTypeCapProviderElementLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 10),
    _CucsFirmwareBundleTypeCapProviderElementLoadFailures_Type()
)
cucsFirmwareBundleTypeCapProviderElementLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderElementLoadFailures.setStatus("current")
_CucsFirmwareBundleTypeCapProviderElementsLoaded_Type = Gauge32
_CucsFirmwareBundleTypeCapProviderElementsLoaded_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderElementsLoaded = _CucsFirmwareBundleTypeCapProviderElementsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 11),
    _CucsFirmwareBundleTypeCapProviderElementsLoaded_Type()
)
cucsFirmwareBundleTypeCapProviderElementsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderElementsLoaded.setStatus("current")
_CucsFirmwareBundleTypeCapProviderLoadErrors_Type = Gauge32
_CucsFirmwareBundleTypeCapProviderLoadErrors_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderLoadErrors = _CucsFirmwareBundleTypeCapProviderLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 12),
    _CucsFirmwareBundleTypeCapProviderLoadErrors_Type()
)
cucsFirmwareBundleTypeCapProviderLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderLoadErrors.setStatus("current")
_CucsFirmwareBundleTypeCapProviderLoadWarnings_Type = Gauge32
_CucsFirmwareBundleTypeCapProviderLoadWarnings_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderLoadWarnings = _CucsFirmwareBundleTypeCapProviderLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 13),
    _CucsFirmwareBundleTypeCapProviderLoadWarnings_Type()
)
cucsFirmwareBundleTypeCapProviderLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderLoadWarnings.setStatus("current")
_CucsFirmwareBundleTypeCapProviderPlatformType_Type = CucsFirmwarePlatformType
_CucsFirmwareBundleTypeCapProviderPlatformType_Object = MibTableColumn
cucsFirmwareBundleTypeCapProviderPlatformType = _CucsFirmwareBundleTypeCapProviderPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 22, 1, 14),
    _CucsFirmwareBundleTypeCapProviderPlatformType_Type()
)
cucsFirmwareBundleTypeCapProviderPlatformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleTypeCapProviderPlatformType.setStatus("current")
_CucsFirmwareSpecTable_Object = MibTable
cucsFirmwareSpecTable = _CucsFirmwareSpecTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 23)
)
if mibBuilder.loadTexts:
    cucsFirmwareSpecTable.setStatus("current")
_CucsFirmwareSpecEntry_Object = MibTableRow
cucsFirmwareSpecEntry = _CucsFirmwareSpecEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 23, 1)
)
cucsFirmwareSpecEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareSpecInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareSpecEntry.setStatus("current")
_CucsFirmwareSpecInstanceId_Type = CucsManagedObjectId
_CucsFirmwareSpecInstanceId_Object = MibTableColumn
cucsFirmwareSpecInstanceId = _CucsFirmwareSpecInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 23, 1, 1),
    _CucsFirmwareSpecInstanceId_Type()
)
cucsFirmwareSpecInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareSpecInstanceId.setStatus("current")
_CucsFirmwareSpecDn_Type = CucsManagedObjectDn
_CucsFirmwareSpecDn_Object = MibTableColumn
cucsFirmwareSpecDn = _CucsFirmwareSpecDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 23, 1, 2),
    _CucsFirmwareSpecDn_Type()
)
cucsFirmwareSpecDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSpecDn.setStatus("current")
_CucsFirmwareSpecRn_Type = SnmpAdminString
_CucsFirmwareSpecRn_Object = MibTableColumn
cucsFirmwareSpecRn = _CucsFirmwareSpecRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 23, 1, 3),
    _CucsFirmwareSpecRn_Type()
)
cucsFirmwareSpecRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSpecRn.setStatus("current")
_CucsFirmwareSpecBundleVersion_Type = SnmpAdminString
_CucsFirmwareSpecBundleVersion_Object = MibTableColumn
cucsFirmwareSpecBundleVersion = _CucsFirmwareSpecBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 23, 1, 4),
    _CucsFirmwareSpecBundleVersion_Type()
)
cucsFirmwareSpecBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSpecBundleVersion.setStatus("current")
_CucsFirmwareSpecEthEFIVersion_Type = SnmpAdminString
_CucsFirmwareSpecEthEFIVersion_Object = MibTableColumn
cucsFirmwareSpecEthEFIVersion = _CucsFirmwareSpecEthEFIVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 23, 1, 5),
    _CucsFirmwareSpecEthEFIVersion_Type()
)
cucsFirmwareSpecEthEFIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSpecEthEFIVersion.setStatus("current")
_CucsFirmwareSpecEthOptionRomVersion_Type = SnmpAdminString
_CucsFirmwareSpecEthOptionRomVersion_Object = MibTableColumn
cucsFirmwareSpecEthOptionRomVersion = _CucsFirmwareSpecEthOptionRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 23, 1, 6),
    _CucsFirmwareSpecEthOptionRomVersion_Type()
)
cucsFirmwareSpecEthOptionRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSpecEthOptionRomVersion.setStatus("current")
_CucsFirmwareSpecFcFWVersion_Type = SnmpAdminString
_CucsFirmwareSpecFcFWVersion_Object = MibTableColumn
cucsFirmwareSpecFcFWVersion = _CucsFirmwareSpecFcFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 23, 1, 7),
    _CucsFirmwareSpecFcFWVersion_Type()
)
cucsFirmwareSpecFcFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSpecFcFWVersion.setStatus("current")
_CucsFirmwareSpecFcOptionRomVersion_Type = SnmpAdminString
_CucsFirmwareSpecFcOptionRomVersion_Object = MibTableColumn
cucsFirmwareSpecFcOptionRomVersion = _CucsFirmwareSpecFcOptionRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 23, 1, 8),
    _CucsFirmwareSpecFcOptionRomVersion_Type()
)
cucsFirmwareSpecFcOptionRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSpecFcOptionRomVersion.setStatus("current")
_CucsFirmwareUpgradeConstraintTable_Object = MibTable
cucsFirmwareUpgradeConstraintTable = _CucsFirmwareUpgradeConstraintTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 24)
)
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeConstraintTable.setStatus("current")
_CucsFirmwareUpgradeConstraintEntry_Object = MibTableRow
cucsFirmwareUpgradeConstraintEntry = _CucsFirmwareUpgradeConstraintEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 24, 1)
)
cucsFirmwareUpgradeConstraintEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareUpgradeConstraintInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeConstraintEntry.setStatus("current")
_CucsFirmwareUpgradeConstraintInstanceId_Type = CucsManagedObjectId
_CucsFirmwareUpgradeConstraintInstanceId_Object = MibTableColumn
cucsFirmwareUpgradeConstraintInstanceId = _CucsFirmwareUpgradeConstraintInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 24, 1, 1),
    _CucsFirmwareUpgradeConstraintInstanceId_Type()
)
cucsFirmwareUpgradeConstraintInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeConstraintInstanceId.setStatus("current")
_CucsFirmwareUpgradeConstraintDn_Type = CucsManagedObjectDn
_CucsFirmwareUpgradeConstraintDn_Object = MibTableColumn
cucsFirmwareUpgradeConstraintDn = _CucsFirmwareUpgradeConstraintDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 24, 1, 2),
    _CucsFirmwareUpgradeConstraintDn_Type()
)
cucsFirmwareUpgradeConstraintDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeConstraintDn.setStatus("current")
_CucsFirmwareUpgradeConstraintRn_Type = SnmpAdminString
_CucsFirmwareUpgradeConstraintRn_Object = MibTableColumn
cucsFirmwareUpgradeConstraintRn = _CucsFirmwareUpgradeConstraintRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 24, 1, 3),
    _CucsFirmwareUpgradeConstraintRn_Type()
)
cucsFirmwareUpgradeConstraintRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeConstraintRn.setStatus("current")
_CucsFirmwareUpgradeConstraintMinVer_Type = SnmpAdminString
_CucsFirmwareUpgradeConstraintMinVer_Object = MibTableColumn
cucsFirmwareUpgradeConstraintMinVer = _CucsFirmwareUpgradeConstraintMinVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 24, 1, 4),
    _CucsFirmwareUpgradeConstraintMinVer_Type()
)
cucsFirmwareUpgradeConstraintMinVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeConstraintMinVer.setStatus("current")
_CucsFirmwareAckTable_Object = MibTable
cucsFirmwareAckTable = _CucsFirmwareAckTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25)
)
if mibBuilder.loadTexts:
    cucsFirmwareAckTable.setStatus("current")
_CucsFirmwareAckEntry_Object = MibTableRow
cucsFirmwareAckEntry = _CucsFirmwareAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1)
)
cucsFirmwareAckEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareAckInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareAckEntry.setStatus("current")
_CucsFirmwareAckInstanceId_Type = CucsManagedObjectId
_CucsFirmwareAckInstanceId_Object = MibTableColumn
cucsFirmwareAckInstanceId = _CucsFirmwareAckInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 1),
    _CucsFirmwareAckInstanceId_Type()
)
cucsFirmwareAckInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareAckInstanceId.setStatus("current")
_CucsFirmwareAckDn_Type = CucsManagedObjectDn
_CucsFirmwareAckDn_Object = MibTableColumn
cucsFirmwareAckDn = _CucsFirmwareAckDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 2),
    _CucsFirmwareAckDn_Type()
)
cucsFirmwareAckDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckDn.setStatus("current")
_CucsFirmwareAckRn_Type = SnmpAdminString
_CucsFirmwareAckRn_Object = MibTableColumn
cucsFirmwareAckRn = _CucsFirmwareAckRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 3),
    _CucsFirmwareAckRn_Type()
)
cucsFirmwareAckRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckRn.setStatus("current")
_CucsFirmwareAckAcked_Type = DateAndTime
_CucsFirmwareAckAcked_Object = MibTableColumn
cucsFirmwareAckAcked = _CucsFirmwareAckAcked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 4),
    _CucsFirmwareAckAcked_Type()
)
cucsFirmwareAckAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckAcked.setStatus("current")
_CucsFirmwareAckAckedBy_Type = SnmpAdminString
_CucsFirmwareAckAckedBy_Object = MibTableColumn
cucsFirmwareAckAckedBy = _CucsFirmwareAckAckedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 5),
    _CucsFirmwareAckAckedBy_Type()
)
cucsFirmwareAckAckedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckAckedBy.setStatus("current")
_CucsFirmwareAckAdminState_Type = CucsTrigAdminState
_CucsFirmwareAckAdminState_Object = MibTableColumn
cucsFirmwareAckAdminState = _CucsFirmwareAckAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 6),
    _CucsFirmwareAckAdminState_Type()
)
cucsFirmwareAckAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckAdminState.setStatus("current")
_CucsFirmwareAckAutoDelete_Type = TruthValue
_CucsFirmwareAckAutoDelete_Object = MibTableColumn
cucsFirmwareAckAutoDelete = _CucsFirmwareAckAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 7),
    _CucsFirmwareAckAutoDelete_Type()
)
cucsFirmwareAckAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckAutoDelete.setStatus("current")
_CucsFirmwareAckChangeBy_Type = SnmpAdminString
_CucsFirmwareAckChangeBy_Object = MibTableColumn
cucsFirmwareAckChangeBy = _CucsFirmwareAckChangeBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 8),
    _CucsFirmwareAckChangeBy_Type()
)
cucsFirmwareAckChangeBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckChangeBy.setStatus("current")
_CucsFirmwareAckChangeDetails_Type = CucsTrigAckChangeDetails
_CucsFirmwareAckChangeDetails_Object = MibTableColumn
cucsFirmwareAckChangeDetails = _CucsFirmwareAckChangeDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 9),
    _CucsFirmwareAckChangeDetails_Type()
)
cucsFirmwareAckChangeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckChangeDetails.setStatus("current")
_CucsFirmwareAckChanges_Type = CucsTrigAckChanges
_CucsFirmwareAckChanges_Object = MibTableColumn
cucsFirmwareAckChanges = _CucsFirmwareAckChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 10),
    _CucsFirmwareAckChanges_Type()
)
cucsFirmwareAckChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckChanges.setStatus("current")
_CucsFirmwareAckDescr_Type = SnmpAdminString
_CucsFirmwareAckDescr_Object = MibTableColumn
cucsFirmwareAckDescr = _CucsFirmwareAckDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 11),
    _CucsFirmwareAckDescr_Type()
)
cucsFirmwareAckDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckDescr.setStatus("current")
_CucsFirmwareAckDisr_Type = CucsTrigAckDisr
_CucsFirmwareAckDisr_Object = MibTableColumn
cucsFirmwareAckDisr = _CucsFirmwareAckDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 12),
    _CucsFirmwareAckDisr_Type()
)
cucsFirmwareAckDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckDisr.setStatus("current")
_CucsFirmwareAckIgnoreCap_Type = TruthValue
_CucsFirmwareAckIgnoreCap_Object = MibTableColumn
cucsFirmwareAckIgnoreCap = _CucsFirmwareAckIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 13),
    _CucsFirmwareAckIgnoreCap_Type()
)
cucsFirmwareAckIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckIgnoreCap.setStatus("current")
_CucsFirmwareAckIntId_Type = SnmpAdminString
_CucsFirmwareAckIntId_Object = MibTableColumn
cucsFirmwareAckIntId = _CucsFirmwareAckIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 14),
    _CucsFirmwareAckIntId_Type()
)
cucsFirmwareAckIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckIntId.setStatus("current")
_CucsFirmwareAckModified_Type = DateAndTime
_CucsFirmwareAckModified_Object = MibTableColumn
cucsFirmwareAckModified = _CucsFirmwareAckModified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 15),
    _CucsFirmwareAckModified_Type()
)
cucsFirmwareAckModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckModified.setStatus("current")
_CucsFirmwareAckName_Type = SnmpAdminString
_CucsFirmwareAckName_Object = MibTableColumn
cucsFirmwareAckName = _CucsFirmwareAckName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 16),
    _CucsFirmwareAckName_Type()
)
cucsFirmwareAckName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckName.setStatus("current")
_CucsFirmwareAckOperScheduler_Type = SnmpAdminString
_CucsFirmwareAckOperScheduler_Object = MibTableColumn
cucsFirmwareAckOperScheduler = _CucsFirmwareAckOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 17),
    _CucsFirmwareAckOperScheduler_Type()
)
cucsFirmwareAckOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckOperScheduler.setStatus("current")
_CucsFirmwareAckOperState_Type = CucsTrigAckOperState
_CucsFirmwareAckOperState_Object = MibTableColumn
cucsFirmwareAckOperState = _CucsFirmwareAckOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 18),
    _CucsFirmwareAckOperState_Type()
)
cucsFirmwareAckOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckOperState.setStatus("current")
_CucsFirmwareAckPolicyLevel_Type = Gauge32
_CucsFirmwareAckPolicyLevel_Object = MibTableColumn
cucsFirmwareAckPolicyLevel = _CucsFirmwareAckPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 19),
    _CucsFirmwareAckPolicyLevel_Type()
)
cucsFirmwareAckPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckPolicyLevel.setStatus("current")
_CucsFirmwareAckPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFirmwareAckPolicyOwner_Object = MibTableColumn
cucsFirmwareAckPolicyOwner = _CucsFirmwareAckPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 20),
    _CucsFirmwareAckPolicyOwner_Type()
)
cucsFirmwareAckPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckPolicyOwner.setStatus("current")
_CucsFirmwareAckPrevOperState_Type = CucsTrigAckPrevOperState
_CucsFirmwareAckPrevOperState_Object = MibTableColumn
cucsFirmwareAckPrevOperState = _CucsFirmwareAckPrevOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 21),
    _CucsFirmwareAckPrevOperState_Type()
)
cucsFirmwareAckPrevOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckPrevOperState.setStatus("current")
_CucsFirmwareAckScheduler_Type = SnmpAdminString
_CucsFirmwareAckScheduler_Object = MibTableColumn
cucsFirmwareAckScheduler = _CucsFirmwareAckScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 22),
    _CucsFirmwareAckScheduler_Type()
)
cucsFirmwareAckScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckScheduler.setStatus("current")
_CucsFirmwareAckTriggerConfigState_Type = CucsTrigTrigState
_CucsFirmwareAckTriggerConfigState_Object = MibTableColumn
cucsFirmwareAckTriggerConfigState = _CucsFirmwareAckTriggerConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 25, 1, 23),
    _CucsFirmwareAckTriggerConfigState_Type()
)
cucsFirmwareAckTriggerConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAckTriggerConfigState.setStatus("current")
_CucsFirmwareBladeTable_Object = MibTable
cucsFirmwareBladeTable = _CucsFirmwareBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 26)
)
if mibBuilder.loadTexts:
    cucsFirmwareBladeTable.setStatus("current")
_CucsFirmwareBladeEntry_Object = MibTableRow
cucsFirmwareBladeEntry = _CucsFirmwareBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 26, 1)
)
cucsFirmwareBladeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareBladeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareBladeEntry.setStatus("current")
_CucsFirmwareBladeInstanceId_Type = CucsManagedObjectId
_CucsFirmwareBladeInstanceId_Object = MibTableColumn
cucsFirmwareBladeInstanceId = _CucsFirmwareBladeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 26, 1, 1),
    _CucsFirmwareBladeInstanceId_Type()
)
cucsFirmwareBladeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareBladeInstanceId.setStatus("current")
_CucsFirmwareBladeDn_Type = CucsManagedObjectDn
_CucsFirmwareBladeDn_Object = MibTableColumn
cucsFirmwareBladeDn = _CucsFirmwareBladeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 26, 1, 2),
    _CucsFirmwareBladeDn_Type()
)
cucsFirmwareBladeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBladeDn.setStatus("current")
_CucsFirmwareBladeRn_Type = SnmpAdminString
_CucsFirmwareBladeRn_Object = MibTableColumn
cucsFirmwareBladeRn = _CucsFirmwareBladeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 26, 1, 3),
    _CucsFirmwareBladeRn_Type()
)
cucsFirmwareBladeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBladeRn.setStatus("current")
_CucsFirmwareBladeOperVersion_Type = SnmpAdminString
_CucsFirmwareBladeOperVersion_Object = MibTableColumn
cucsFirmwareBladeOperVersion = _CucsFirmwareBladeOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 26, 1, 4),
    _CucsFirmwareBladeOperVersion_Type()
)
cucsFirmwareBladeOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBladeOperVersion.setStatus("current")
_CucsFirmwareBundleInfoTable_Object = MibTable
cucsFirmwareBundleInfoTable = _CucsFirmwareBundleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 27)
)
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoTable.setStatus("current")
_CucsFirmwareBundleInfoEntry_Object = MibTableRow
cucsFirmwareBundleInfoEntry = _CucsFirmwareBundleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 27, 1)
)
cucsFirmwareBundleInfoEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareBundleInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoEntry.setStatus("current")
_CucsFirmwareBundleInfoInstanceId_Type = CucsManagedObjectId
_CucsFirmwareBundleInfoInstanceId_Object = MibTableColumn
cucsFirmwareBundleInfoInstanceId = _CucsFirmwareBundleInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 27, 1, 1),
    _CucsFirmwareBundleInfoInstanceId_Type()
)
cucsFirmwareBundleInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoInstanceId.setStatus("current")
_CucsFirmwareBundleInfoDn_Type = CucsManagedObjectDn
_CucsFirmwareBundleInfoDn_Object = MibTableColumn
cucsFirmwareBundleInfoDn = _CucsFirmwareBundleInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 27, 1, 2),
    _CucsFirmwareBundleInfoDn_Type()
)
cucsFirmwareBundleInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoDn.setStatus("current")
_CucsFirmwareBundleInfoRn_Type = SnmpAdminString
_CucsFirmwareBundleInfoRn_Object = MibTableColumn
cucsFirmwareBundleInfoRn = _CucsFirmwareBundleInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 27, 1, 3),
    _CucsFirmwareBundleInfoRn_Type()
)
cucsFirmwareBundleInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoRn.setStatus("current")
_CucsFirmwareBundleInfoType_Type = CucsFirmwareDistributableType
_CucsFirmwareBundleInfoType_Object = MibTableColumn
cucsFirmwareBundleInfoType = _CucsFirmwareBundleInfoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 27, 1, 4),
    _CucsFirmwareBundleInfoType_Type()
)
cucsFirmwareBundleInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoType.setStatus("current")
_CucsFirmwareBundleInfoVersion_Type = SnmpAdminString
_CucsFirmwareBundleInfoVersion_Object = MibTableColumn
cucsFirmwareBundleInfoVersion = _CucsFirmwareBundleInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 27, 1, 5),
    _CucsFirmwareBundleInfoVersion_Type()
)
cucsFirmwareBundleInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoVersion.setStatus("current")
_CucsFirmwareBundleInfoDigestTable_Object = MibTable
cucsFirmwareBundleInfoDigestTable = _CucsFirmwareBundleInfoDigestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 28)
)
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoDigestTable.setStatus("current")
_CucsFirmwareBundleInfoDigestEntry_Object = MibTableRow
cucsFirmwareBundleInfoDigestEntry = _CucsFirmwareBundleInfoDigestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 28, 1)
)
cucsFirmwareBundleInfoDigestEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareBundleInfoDigestInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoDigestEntry.setStatus("current")
_CucsFirmwareBundleInfoDigestInstanceId_Type = CucsManagedObjectId
_CucsFirmwareBundleInfoDigestInstanceId_Object = MibTableColumn
cucsFirmwareBundleInfoDigestInstanceId = _CucsFirmwareBundleInfoDigestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 28, 1, 1),
    _CucsFirmwareBundleInfoDigestInstanceId_Type()
)
cucsFirmwareBundleInfoDigestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoDigestInstanceId.setStatus("current")
_CucsFirmwareBundleInfoDigestDn_Type = CucsManagedObjectDn
_CucsFirmwareBundleInfoDigestDn_Object = MibTableColumn
cucsFirmwareBundleInfoDigestDn = _CucsFirmwareBundleInfoDigestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 28, 1, 2),
    _CucsFirmwareBundleInfoDigestDn_Type()
)
cucsFirmwareBundleInfoDigestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoDigestDn.setStatus("current")
_CucsFirmwareBundleInfoDigestRn_Type = SnmpAdminString
_CucsFirmwareBundleInfoDigestRn_Object = MibTableColumn
cucsFirmwareBundleInfoDigestRn = _CucsFirmwareBundleInfoDigestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 28, 1, 3),
    _CucsFirmwareBundleInfoDigestRn_Type()
)
cucsFirmwareBundleInfoDigestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoDigestRn.setStatus("current")
_CucsFirmwareBundleInfoDigestBundleName_Type = SnmpAdminString
_CucsFirmwareBundleInfoDigestBundleName_Object = MibTableColumn
cucsFirmwareBundleInfoDigestBundleName = _CucsFirmwareBundleInfoDigestBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 28, 1, 4),
    _CucsFirmwareBundleInfoDigestBundleName_Type()
)
cucsFirmwareBundleInfoDigestBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoDigestBundleName.setStatus("current")
_CucsFirmwareBundleInfoDigestType_Type = CucsFirmwareDistributableType
_CucsFirmwareBundleInfoDigestType_Object = MibTableColumn
cucsFirmwareBundleInfoDigestType = _CucsFirmwareBundleInfoDigestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 28, 1, 5),
    _CucsFirmwareBundleInfoDigestType_Type()
)
cucsFirmwareBundleInfoDigestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoDigestType.setStatus("current")
_CucsFirmwareBundleInfoDigestVersion_Type = SnmpAdminString
_CucsFirmwareBundleInfoDigestVersion_Object = MibTableColumn
cucsFirmwareBundleInfoDigestVersion = _CucsFirmwareBundleInfoDigestVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 28, 1, 6),
    _CucsFirmwareBundleInfoDigestVersion_Type()
)
cucsFirmwareBundleInfoDigestVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareBundleInfoDigestVersion.setStatus("current")
_CucsFirmwareCatalogPackTable_Object = MibTable
cucsFirmwareCatalogPackTable = _CucsFirmwareCatalogPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29)
)
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackTable.setStatus("current")
_CucsFirmwareCatalogPackEntry_Object = MibTableRow
cucsFirmwareCatalogPackEntry = _CucsFirmwareCatalogPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1)
)
cucsFirmwareCatalogPackEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareCatalogPackInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackEntry.setStatus("current")
_CucsFirmwareCatalogPackInstanceId_Type = CucsManagedObjectId
_CucsFirmwareCatalogPackInstanceId_Object = MibTableColumn
cucsFirmwareCatalogPackInstanceId = _CucsFirmwareCatalogPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 1),
    _CucsFirmwareCatalogPackInstanceId_Type()
)
cucsFirmwareCatalogPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackInstanceId.setStatus("current")
_CucsFirmwareCatalogPackDn_Type = CucsManagedObjectDn
_CucsFirmwareCatalogPackDn_Object = MibTableColumn
cucsFirmwareCatalogPackDn = _CucsFirmwareCatalogPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 2),
    _CucsFirmwareCatalogPackDn_Type()
)
cucsFirmwareCatalogPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackDn.setStatus("current")
_CucsFirmwareCatalogPackRn_Type = SnmpAdminString
_CucsFirmwareCatalogPackRn_Object = MibTableColumn
cucsFirmwareCatalogPackRn = _CucsFirmwareCatalogPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 3),
    _CucsFirmwareCatalogPackRn_Type()
)
cucsFirmwareCatalogPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackRn.setStatus("current")
_CucsFirmwareCatalogPackCatalogName_Type = SnmpAdminString
_CucsFirmwareCatalogPackCatalogName_Object = MibTableColumn
cucsFirmwareCatalogPackCatalogName = _CucsFirmwareCatalogPackCatalogName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 4),
    _CucsFirmwareCatalogPackCatalogName_Type()
)
cucsFirmwareCatalogPackCatalogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackCatalogName.setStatus("current")
_CucsFirmwareCatalogPackCatalogVersion_Type = SnmpAdminString
_CucsFirmwareCatalogPackCatalogVersion_Object = MibTableColumn
cucsFirmwareCatalogPackCatalogVersion = _CucsFirmwareCatalogPackCatalogVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 5),
    _CucsFirmwareCatalogPackCatalogVersion_Type()
)
cucsFirmwareCatalogPackCatalogVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackCatalogVersion.setStatus("current")
_CucsFirmwareCatalogPackConfigState_Type = CucsFirmwareCatalogPackConfigState
_CucsFirmwareCatalogPackConfigState_Object = MibTableColumn
cucsFirmwareCatalogPackConfigState = _CucsFirmwareCatalogPackConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 6),
    _CucsFirmwareCatalogPackConfigState_Type()
)
cucsFirmwareCatalogPackConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackConfigState.setStatus("current")
_CucsFirmwareCatalogPackConfigStatusMessage_Type = SnmpAdminString
_CucsFirmwareCatalogPackConfigStatusMessage_Object = MibTableColumn
cucsFirmwareCatalogPackConfigStatusMessage = _CucsFirmwareCatalogPackConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 7),
    _CucsFirmwareCatalogPackConfigStatusMessage_Type()
)
cucsFirmwareCatalogPackConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackConfigStatusMessage.setStatus("current")
_CucsFirmwareCatalogPackDescr_Type = SnmpAdminString
_CucsFirmwareCatalogPackDescr_Object = MibTableColumn
cucsFirmwareCatalogPackDescr = _CucsFirmwareCatalogPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 8),
    _CucsFirmwareCatalogPackDescr_Type()
)
cucsFirmwareCatalogPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackDescr.setStatus("current")
_CucsFirmwareCatalogPackIntId_Type = SnmpAdminString
_CucsFirmwareCatalogPackIntId_Object = MibTableColumn
cucsFirmwareCatalogPackIntId = _CucsFirmwareCatalogPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 9),
    _CucsFirmwareCatalogPackIntId_Type()
)
cucsFirmwareCatalogPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackIntId.setStatus("current")
_CucsFirmwareCatalogPackMode_Type = CucsFirmwarePackMode
_CucsFirmwareCatalogPackMode_Object = MibTableColumn
cucsFirmwareCatalogPackMode = _CucsFirmwareCatalogPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 10),
    _CucsFirmwareCatalogPackMode_Type()
)
cucsFirmwareCatalogPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackMode.setStatus("current")
_CucsFirmwareCatalogPackName_Type = SnmpAdminString
_CucsFirmwareCatalogPackName_Object = MibTableColumn
cucsFirmwareCatalogPackName = _CucsFirmwareCatalogPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 11),
    _CucsFirmwareCatalogPackName_Type()
)
cucsFirmwareCatalogPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackName.setStatus("current")
_CucsFirmwareCatalogPackPolicyLevel_Type = Gauge32
_CucsFirmwareCatalogPackPolicyLevel_Object = MibTableColumn
cucsFirmwareCatalogPackPolicyLevel = _CucsFirmwareCatalogPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 12),
    _CucsFirmwareCatalogPackPolicyLevel_Type()
)
cucsFirmwareCatalogPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackPolicyLevel.setStatus("current")
_CucsFirmwareCatalogPackPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFirmwareCatalogPackPolicyOwner_Object = MibTableColumn
cucsFirmwareCatalogPackPolicyOwner = _CucsFirmwareCatalogPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 13),
    _CucsFirmwareCatalogPackPolicyOwner_Type()
)
cucsFirmwareCatalogPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackPolicyOwner.setStatus("current")
_CucsFirmwareCatalogPackStageSize_Type = Gauge32
_CucsFirmwareCatalogPackStageSize_Object = MibTableColumn
cucsFirmwareCatalogPackStageSize = _CucsFirmwareCatalogPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 14),
    _CucsFirmwareCatalogPackStageSize_Type()
)
cucsFirmwareCatalogPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackStageSize.setStatus("current")
_CucsFirmwareCatalogPackUpdateTrigger_Type = DateAndTime
_CucsFirmwareCatalogPackUpdateTrigger_Object = MibTableColumn
cucsFirmwareCatalogPackUpdateTrigger = _CucsFirmwareCatalogPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 29, 1, 15),
    _CucsFirmwareCatalogPackUpdateTrigger_Type()
)
cucsFirmwareCatalogPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareCatalogPackUpdateTrigger.setStatus("current")
_CucsFirmwareDistributableFsmTable_Object = MibTable
cucsFirmwareDistributableFsmTable = _CucsFirmwareDistributableFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30)
)
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmTable.setStatus("current")
_CucsFirmwareDistributableFsmEntry_Object = MibTableRow
cucsFirmwareDistributableFsmEntry = _CucsFirmwareDistributableFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30, 1)
)
cucsFirmwareDistributableFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareDistributableFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmEntry.setStatus("current")
_CucsFirmwareDistributableFsmInstanceId_Type = CucsManagedObjectId
_CucsFirmwareDistributableFsmInstanceId_Object = MibTableColumn
cucsFirmwareDistributableFsmInstanceId = _CucsFirmwareDistributableFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30, 1, 1),
    _CucsFirmwareDistributableFsmInstanceId_Type()
)
cucsFirmwareDistributableFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmInstanceId.setStatus("current")
_CucsFirmwareDistributableFsmDn_Type = CucsManagedObjectDn
_CucsFirmwareDistributableFsmDn_Object = MibTableColumn
cucsFirmwareDistributableFsmDn = _CucsFirmwareDistributableFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30, 1, 2),
    _CucsFirmwareDistributableFsmDn_Type()
)
cucsFirmwareDistributableFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmDn.setStatus("current")
_CucsFirmwareDistributableFsmRn_Type = SnmpAdminString
_CucsFirmwareDistributableFsmRn_Object = MibTableColumn
cucsFirmwareDistributableFsmRn = _CucsFirmwareDistributableFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30, 1, 3),
    _CucsFirmwareDistributableFsmRn_Type()
)
cucsFirmwareDistributableFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmRn.setStatus("current")
_CucsFirmwareDistributableFsmCompletionTime_Type = DateAndTime
_CucsFirmwareDistributableFsmCompletionTime_Object = MibTableColumn
cucsFirmwareDistributableFsmCompletionTime = _CucsFirmwareDistributableFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30, 1, 4),
    _CucsFirmwareDistributableFsmCompletionTime_Type()
)
cucsFirmwareDistributableFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmCompletionTime.setStatus("current")
_CucsFirmwareDistributableFsmCurrentFsm_Type = CucsFirmwareDistributableFsmCurrentFsm
_CucsFirmwareDistributableFsmCurrentFsm_Object = MibTableColumn
cucsFirmwareDistributableFsmCurrentFsm = _CucsFirmwareDistributableFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30, 1, 5),
    _CucsFirmwareDistributableFsmCurrentFsm_Type()
)
cucsFirmwareDistributableFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmCurrentFsm.setStatus("current")
_CucsFirmwareDistributableFsmDescrData_Type = SnmpAdminString
_CucsFirmwareDistributableFsmDescrData_Object = MibTableColumn
cucsFirmwareDistributableFsmDescrData = _CucsFirmwareDistributableFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30, 1, 6),
    _CucsFirmwareDistributableFsmDescrData_Type()
)
cucsFirmwareDistributableFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmDescrData.setStatus("current")
_CucsFirmwareDistributableFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsFirmwareDistributableFsmFsmStatus_Object = MibTableColumn
cucsFirmwareDistributableFsmFsmStatus = _CucsFirmwareDistributableFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30, 1, 7),
    _CucsFirmwareDistributableFsmFsmStatus_Type()
)
cucsFirmwareDistributableFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmFsmStatus.setStatus("current")
_CucsFirmwareDistributableFsmProgress_Type = Gauge32
_CucsFirmwareDistributableFsmProgress_Object = MibTableColumn
cucsFirmwareDistributableFsmProgress = _CucsFirmwareDistributableFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30, 1, 8),
    _CucsFirmwareDistributableFsmProgress_Type()
)
cucsFirmwareDistributableFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmProgress.setStatus("current")
_CucsFirmwareDistributableFsmRmtErrCode_Type = Gauge32
_CucsFirmwareDistributableFsmRmtErrCode_Object = MibTableColumn
cucsFirmwareDistributableFsmRmtErrCode = _CucsFirmwareDistributableFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30, 1, 9),
    _CucsFirmwareDistributableFsmRmtErrCode_Type()
)
cucsFirmwareDistributableFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmRmtErrCode.setStatus("current")
_CucsFirmwareDistributableFsmRmtErrDescr_Type = SnmpAdminString
_CucsFirmwareDistributableFsmRmtErrDescr_Object = MibTableColumn
cucsFirmwareDistributableFsmRmtErrDescr = _CucsFirmwareDistributableFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30, 1, 10),
    _CucsFirmwareDistributableFsmRmtErrDescr_Type()
)
cucsFirmwareDistributableFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmRmtErrDescr.setStatus("current")
_CucsFirmwareDistributableFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsFirmwareDistributableFsmRmtRslt_Object = MibTableColumn
cucsFirmwareDistributableFsmRmtRslt = _CucsFirmwareDistributableFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 30, 1, 11),
    _CucsFirmwareDistributableFsmRmtRslt_Type()
)
cucsFirmwareDistributableFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmRmtRslt.setStatus("current")
_CucsFirmwareDistributableFsmStageTable_Object = MibTable
cucsFirmwareDistributableFsmStageTable = _CucsFirmwareDistributableFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 31)
)
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStageTable.setStatus("current")
_CucsFirmwareDistributableFsmStageEntry_Object = MibTableRow
cucsFirmwareDistributableFsmStageEntry = _CucsFirmwareDistributableFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 31, 1)
)
cucsFirmwareDistributableFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareDistributableFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStageEntry.setStatus("current")
_CucsFirmwareDistributableFsmStageInstanceId_Type = CucsManagedObjectId
_CucsFirmwareDistributableFsmStageInstanceId_Object = MibTableColumn
cucsFirmwareDistributableFsmStageInstanceId = _CucsFirmwareDistributableFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 31, 1, 1),
    _CucsFirmwareDistributableFsmStageInstanceId_Type()
)
cucsFirmwareDistributableFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStageInstanceId.setStatus("current")
_CucsFirmwareDistributableFsmStageDn_Type = CucsManagedObjectDn
_CucsFirmwareDistributableFsmStageDn_Object = MibTableColumn
cucsFirmwareDistributableFsmStageDn = _CucsFirmwareDistributableFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 31, 1, 2),
    _CucsFirmwareDistributableFsmStageDn_Type()
)
cucsFirmwareDistributableFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStageDn.setStatus("current")
_CucsFirmwareDistributableFsmStageRn_Type = SnmpAdminString
_CucsFirmwareDistributableFsmStageRn_Object = MibTableColumn
cucsFirmwareDistributableFsmStageRn = _CucsFirmwareDistributableFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 31, 1, 3),
    _CucsFirmwareDistributableFsmStageRn_Type()
)
cucsFirmwareDistributableFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStageRn.setStatus("current")
_CucsFirmwareDistributableFsmStageDescrData_Type = SnmpAdminString
_CucsFirmwareDistributableFsmStageDescrData_Object = MibTableColumn
cucsFirmwareDistributableFsmStageDescrData = _CucsFirmwareDistributableFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 31, 1, 4),
    _CucsFirmwareDistributableFsmStageDescrData_Type()
)
cucsFirmwareDistributableFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStageDescrData.setStatus("current")
_CucsFirmwareDistributableFsmStageLastUpdateTime_Type = DateAndTime
_CucsFirmwareDistributableFsmStageLastUpdateTime_Object = MibTableColumn
cucsFirmwareDistributableFsmStageLastUpdateTime = _CucsFirmwareDistributableFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 31, 1, 5),
    _CucsFirmwareDistributableFsmStageLastUpdateTime_Type()
)
cucsFirmwareDistributableFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStageLastUpdateTime.setStatus("current")
_CucsFirmwareDistributableFsmStageName_Type = CucsFirmwareDistributableFsmStageName
_CucsFirmwareDistributableFsmStageName_Object = MibTableColumn
cucsFirmwareDistributableFsmStageName = _CucsFirmwareDistributableFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 31, 1, 6),
    _CucsFirmwareDistributableFsmStageName_Type()
)
cucsFirmwareDistributableFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStageName.setStatus("current")
_CucsFirmwareDistributableFsmStageOrder_Type = Gauge32
_CucsFirmwareDistributableFsmStageOrder_Object = MibTableColumn
cucsFirmwareDistributableFsmStageOrder = _CucsFirmwareDistributableFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 31, 1, 7),
    _CucsFirmwareDistributableFsmStageOrder_Type()
)
cucsFirmwareDistributableFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStageOrder.setStatus("current")
_CucsFirmwareDistributableFsmStageRetry_Type = Gauge32
_CucsFirmwareDistributableFsmStageRetry_Object = MibTableColumn
cucsFirmwareDistributableFsmStageRetry = _CucsFirmwareDistributableFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 31, 1, 8),
    _CucsFirmwareDistributableFsmStageRetry_Type()
)
cucsFirmwareDistributableFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStageRetry.setStatus("current")
_CucsFirmwareDistributableFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsFirmwareDistributableFsmStageStageStatus_Object = MibTableColumn
cucsFirmwareDistributableFsmStageStageStatus = _CucsFirmwareDistributableFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 31, 1, 9),
    _CucsFirmwareDistributableFsmStageStageStatus_Type()
)
cucsFirmwareDistributableFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDistributableFsmStageStageStatus.setStatus("current")
_CucsFirmwareDownloaderFsmTable_Object = MibTable
cucsFirmwareDownloaderFsmTable = _CucsFirmwareDownloaderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32)
)
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmTable.setStatus("current")
_CucsFirmwareDownloaderFsmEntry_Object = MibTableRow
cucsFirmwareDownloaderFsmEntry = _CucsFirmwareDownloaderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32, 1)
)
cucsFirmwareDownloaderFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareDownloaderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmEntry.setStatus("current")
_CucsFirmwareDownloaderFsmInstanceId_Type = CucsManagedObjectId
_CucsFirmwareDownloaderFsmInstanceId_Object = MibTableColumn
cucsFirmwareDownloaderFsmInstanceId = _CucsFirmwareDownloaderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32, 1, 1),
    _CucsFirmwareDownloaderFsmInstanceId_Type()
)
cucsFirmwareDownloaderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmInstanceId.setStatus("current")
_CucsFirmwareDownloaderFsmDn_Type = CucsManagedObjectDn
_CucsFirmwareDownloaderFsmDn_Object = MibTableColumn
cucsFirmwareDownloaderFsmDn = _CucsFirmwareDownloaderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32, 1, 2),
    _CucsFirmwareDownloaderFsmDn_Type()
)
cucsFirmwareDownloaderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmDn.setStatus("current")
_CucsFirmwareDownloaderFsmRn_Type = SnmpAdminString
_CucsFirmwareDownloaderFsmRn_Object = MibTableColumn
cucsFirmwareDownloaderFsmRn = _CucsFirmwareDownloaderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32, 1, 3),
    _CucsFirmwareDownloaderFsmRn_Type()
)
cucsFirmwareDownloaderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmRn.setStatus("current")
_CucsFirmwareDownloaderFsmCompletionTime_Type = DateAndTime
_CucsFirmwareDownloaderFsmCompletionTime_Object = MibTableColumn
cucsFirmwareDownloaderFsmCompletionTime = _CucsFirmwareDownloaderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32, 1, 4),
    _CucsFirmwareDownloaderFsmCompletionTime_Type()
)
cucsFirmwareDownloaderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmCompletionTime.setStatus("current")
_CucsFirmwareDownloaderFsmCurrentFsm_Type = CucsFirmwareDownloaderFsmCurrentFsm
_CucsFirmwareDownloaderFsmCurrentFsm_Object = MibTableColumn
cucsFirmwareDownloaderFsmCurrentFsm = _CucsFirmwareDownloaderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32, 1, 5),
    _CucsFirmwareDownloaderFsmCurrentFsm_Type()
)
cucsFirmwareDownloaderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmCurrentFsm.setStatus("current")
_CucsFirmwareDownloaderFsmDescrData_Type = SnmpAdminString
_CucsFirmwareDownloaderFsmDescrData_Object = MibTableColumn
cucsFirmwareDownloaderFsmDescrData = _CucsFirmwareDownloaderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32, 1, 6),
    _CucsFirmwareDownloaderFsmDescrData_Type()
)
cucsFirmwareDownloaderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmDescrData.setStatus("current")
_CucsFirmwareDownloaderFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsFirmwareDownloaderFsmFsmStatus_Object = MibTableColumn
cucsFirmwareDownloaderFsmFsmStatus = _CucsFirmwareDownloaderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32, 1, 7),
    _CucsFirmwareDownloaderFsmFsmStatus_Type()
)
cucsFirmwareDownloaderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmFsmStatus.setStatus("current")
_CucsFirmwareDownloaderFsmProgress_Type = Gauge32
_CucsFirmwareDownloaderFsmProgress_Object = MibTableColumn
cucsFirmwareDownloaderFsmProgress = _CucsFirmwareDownloaderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32, 1, 8),
    _CucsFirmwareDownloaderFsmProgress_Type()
)
cucsFirmwareDownloaderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmProgress.setStatus("current")
_CucsFirmwareDownloaderFsmRmtErrCode_Type = Gauge32
_CucsFirmwareDownloaderFsmRmtErrCode_Object = MibTableColumn
cucsFirmwareDownloaderFsmRmtErrCode = _CucsFirmwareDownloaderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32, 1, 9),
    _CucsFirmwareDownloaderFsmRmtErrCode_Type()
)
cucsFirmwareDownloaderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmRmtErrCode.setStatus("current")
_CucsFirmwareDownloaderFsmRmtErrDescr_Type = SnmpAdminString
_CucsFirmwareDownloaderFsmRmtErrDescr_Object = MibTableColumn
cucsFirmwareDownloaderFsmRmtErrDescr = _CucsFirmwareDownloaderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32, 1, 10),
    _CucsFirmwareDownloaderFsmRmtErrDescr_Type()
)
cucsFirmwareDownloaderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmRmtErrDescr.setStatus("current")
_CucsFirmwareDownloaderFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsFirmwareDownloaderFsmRmtRslt_Object = MibTableColumn
cucsFirmwareDownloaderFsmRmtRslt = _CucsFirmwareDownloaderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 32, 1, 11),
    _CucsFirmwareDownloaderFsmRmtRslt_Type()
)
cucsFirmwareDownloaderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmRmtRslt.setStatus("current")
_CucsFirmwareDownloaderFsmStageTable_Object = MibTable
cucsFirmwareDownloaderFsmStageTable = _CucsFirmwareDownloaderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 33)
)
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStageTable.setStatus("current")
_CucsFirmwareDownloaderFsmStageEntry_Object = MibTableRow
cucsFirmwareDownloaderFsmStageEntry = _CucsFirmwareDownloaderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 33, 1)
)
cucsFirmwareDownloaderFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareDownloaderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStageEntry.setStatus("current")
_CucsFirmwareDownloaderFsmStageInstanceId_Type = CucsManagedObjectId
_CucsFirmwareDownloaderFsmStageInstanceId_Object = MibTableColumn
cucsFirmwareDownloaderFsmStageInstanceId = _CucsFirmwareDownloaderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 33, 1, 1),
    _CucsFirmwareDownloaderFsmStageInstanceId_Type()
)
cucsFirmwareDownloaderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStageInstanceId.setStatus("current")
_CucsFirmwareDownloaderFsmStageDn_Type = CucsManagedObjectDn
_CucsFirmwareDownloaderFsmStageDn_Object = MibTableColumn
cucsFirmwareDownloaderFsmStageDn = _CucsFirmwareDownloaderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 33, 1, 2),
    _CucsFirmwareDownloaderFsmStageDn_Type()
)
cucsFirmwareDownloaderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStageDn.setStatus("current")
_CucsFirmwareDownloaderFsmStageRn_Type = SnmpAdminString
_CucsFirmwareDownloaderFsmStageRn_Object = MibTableColumn
cucsFirmwareDownloaderFsmStageRn = _CucsFirmwareDownloaderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 33, 1, 3),
    _CucsFirmwareDownloaderFsmStageRn_Type()
)
cucsFirmwareDownloaderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStageRn.setStatus("current")
_CucsFirmwareDownloaderFsmStageDescrData_Type = SnmpAdminString
_CucsFirmwareDownloaderFsmStageDescrData_Object = MibTableColumn
cucsFirmwareDownloaderFsmStageDescrData = _CucsFirmwareDownloaderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 33, 1, 4),
    _CucsFirmwareDownloaderFsmStageDescrData_Type()
)
cucsFirmwareDownloaderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStageDescrData.setStatus("current")
_CucsFirmwareDownloaderFsmStageLastUpdateTime_Type = DateAndTime
_CucsFirmwareDownloaderFsmStageLastUpdateTime_Object = MibTableColumn
cucsFirmwareDownloaderFsmStageLastUpdateTime = _CucsFirmwareDownloaderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 33, 1, 5),
    _CucsFirmwareDownloaderFsmStageLastUpdateTime_Type()
)
cucsFirmwareDownloaderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStageLastUpdateTime.setStatus("current")
_CucsFirmwareDownloaderFsmStageName_Type = CucsFirmwareDownloaderFsmStageName
_CucsFirmwareDownloaderFsmStageName_Object = MibTableColumn
cucsFirmwareDownloaderFsmStageName = _CucsFirmwareDownloaderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 33, 1, 6),
    _CucsFirmwareDownloaderFsmStageName_Type()
)
cucsFirmwareDownloaderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStageName.setStatus("current")
_CucsFirmwareDownloaderFsmStageOrder_Type = Gauge32
_CucsFirmwareDownloaderFsmStageOrder_Object = MibTableColumn
cucsFirmwareDownloaderFsmStageOrder = _CucsFirmwareDownloaderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 33, 1, 7),
    _CucsFirmwareDownloaderFsmStageOrder_Type()
)
cucsFirmwareDownloaderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStageOrder.setStatus("current")
_CucsFirmwareDownloaderFsmStageRetry_Type = Gauge32
_CucsFirmwareDownloaderFsmStageRetry_Object = MibTableColumn
cucsFirmwareDownloaderFsmStageRetry = _CucsFirmwareDownloaderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 33, 1, 8),
    _CucsFirmwareDownloaderFsmStageRetry_Type()
)
cucsFirmwareDownloaderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStageRetry.setStatus("current")
_CucsFirmwareDownloaderFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsFirmwareDownloaderFsmStageStageStatus_Object = MibTableColumn
cucsFirmwareDownloaderFsmStageStageStatus = _CucsFirmwareDownloaderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 33, 1, 9),
    _CucsFirmwareDownloaderFsmStageStageStatus_Type()
)
cucsFirmwareDownloaderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareDownloaderFsmStageStageStatus.setStatus("current")
_CucsFirmwareHostTable_Object = MibTable
cucsFirmwareHostTable = _CucsFirmwareHostTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 34)
)
if mibBuilder.loadTexts:
    cucsFirmwareHostTable.setStatus("current")
_CucsFirmwareHostEntry_Object = MibTableRow
cucsFirmwareHostEntry = _CucsFirmwareHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 34, 1)
)
cucsFirmwareHostEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareHostInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareHostEntry.setStatus("current")
_CucsFirmwareHostInstanceId_Type = CucsManagedObjectId
_CucsFirmwareHostInstanceId_Object = MibTableColumn
cucsFirmwareHostInstanceId = _CucsFirmwareHostInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 34, 1, 1),
    _CucsFirmwareHostInstanceId_Type()
)
cucsFirmwareHostInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareHostInstanceId.setStatus("current")
_CucsFirmwareHostDn_Type = CucsManagedObjectDn
_CucsFirmwareHostDn_Object = MibTableColumn
cucsFirmwareHostDn = _CucsFirmwareHostDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 34, 1, 2),
    _CucsFirmwareHostDn_Type()
)
cucsFirmwareHostDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareHostDn.setStatus("current")
_CucsFirmwareHostRn_Type = SnmpAdminString
_CucsFirmwareHostRn_Object = MibTableColumn
cucsFirmwareHostRn = _CucsFirmwareHostRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 34, 1, 3),
    _CucsFirmwareHostRn_Type()
)
cucsFirmwareHostRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareHostRn.setStatus("current")
_CucsFirmwareHostPackModImpactTable_Object = MibTable
cucsFirmwareHostPackModImpactTable = _CucsFirmwareHostPackModImpactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 35)
)
if mibBuilder.loadTexts:
    cucsFirmwareHostPackModImpactTable.setStatus("current")
_CucsFirmwareHostPackModImpactEntry_Object = MibTableRow
cucsFirmwareHostPackModImpactEntry = _CucsFirmwareHostPackModImpactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 35, 1)
)
cucsFirmwareHostPackModImpactEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareHostPackModImpactInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareHostPackModImpactEntry.setStatus("current")
_CucsFirmwareHostPackModImpactInstanceId_Type = CucsManagedObjectId
_CucsFirmwareHostPackModImpactInstanceId_Object = MibTableColumn
cucsFirmwareHostPackModImpactInstanceId = _CucsFirmwareHostPackModImpactInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 35, 1, 1),
    _CucsFirmwareHostPackModImpactInstanceId_Type()
)
cucsFirmwareHostPackModImpactInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareHostPackModImpactInstanceId.setStatus("current")
_CucsFirmwareHostPackModImpactDn_Type = CucsManagedObjectDn
_CucsFirmwareHostPackModImpactDn_Object = MibTableColumn
cucsFirmwareHostPackModImpactDn = _CucsFirmwareHostPackModImpactDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 35, 1, 2),
    _CucsFirmwareHostPackModImpactDn_Type()
)
cucsFirmwareHostPackModImpactDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareHostPackModImpactDn.setStatus("current")
_CucsFirmwareHostPackModImpactRn_Type = SnmpAdminString
_CucsFirmwareHostPackModImpactRn_Object = MibTableColumn
cucsFirmwareHostPackModImpactRn = _CucsFirmwareHostPackModImpactRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 35, 1, 3),
    _CucsFirmwareHostPackModImpactRn_Type()
)
cucsFirmwareHostPackModImpactRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareHostPackModImpactRn.setStatus("current")
_CucsFirmwareHostPackModImpactKeyDn_Type = SnmpAdminString
_CucsFirmwareHostPackModImpactKeyDn_Object = MibTableColumn
cucsFirmwareHostPackModImpactKeyDn = _CucsFirmwareHostPackModImpactKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 35, 1, 4),
    _CucsFirmwareHostPackModImpactKeyDn_Type()
)
cucsFirmwareHostPackModImpactKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareHostPackModImpactKeyDn.setStatus("current")
_CucsFirmwareHostPackModImpactMaintPolicyDn_Type = SnmpAdminString
_CucsFirmwareHostPackModImpactMaintPolicyDn_Object = MibTableColumn
cucsFirmwareHostPackModImpactMaintPolicyDn = _CucsFirmwareHostPackModImpactMaintPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 35, 1, 5),
    _CucsFirmwareHostPackModImpactMaintPolicyDn_Type()
)
cucsFirmwareHostPackModImpactMaintPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareHostPackModImpactMaintPolicyDn.setStatus("current")
_CucsFirmwareHostPackModImpactPnDn_Type = SnmpAdminString
_CucsFirmwareHostPackModImpactPnDn_Object = MibTableColumn
cucsFirmwareHostPackModImpactPnDn = _CucsFirmwareHostPackModImpactPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 35, 1, 6),
    _CucsFirmwareHostPackModImpactPnDn_Type()
)
cucsFirmwareHostPackModImpactPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareHostPackModImpactPnDn.setStatus("current")
_CucsFirmwareHostPackModImpactRebootPolicy_Type = SnmpAdminString
_CucsFirmwareHostPackModImpactRebootPolicy_Object = MibTableColumn
cucsFirmwareHostPackModImpactRebootPolicy = _CucsFirmwareHostPackModImpactRebootPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 35, 1, 7),
    _CucsFirmwareHostPackModImpactRebootPolicy_Type()
)
cucsFirmwareHostPackModImpactRebootPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareHostPackModImpactRebootPolicy.setStatus("current")
_CucsFirmwareHostPackModImpactServiceProfileDn_Type = SnmpAdminString
_CucsFirmwareHostPackModImpactServiceProfileDn_Object = MibTableColumn
cucsFirmwareHostPackModImpactServiceProfileDn = _CucsFirmwareHostPackModImpactServiceProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 35, 1, 8),
    _CucsFirmwareHostPackModImpactServiceProfileDn_Type()
)
cucsFirmwareHostPackModImpactServiceProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareHostPackModImpactServiceProfileDn.setStatus("current")
_CucsFirmwareImageFsmTable_Object = MibTable
cucsFirmwareImageFsmTable = _CucsFirmwareImageFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36)
)
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmTable.setStatus("current")
_CucsFirmwareImageFsmEntry_Object = MibTableRow
cucsFirmwareImageFsmEntry = _CucsFirmwareImageFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36, 1)
)
cucsFirmwareImageFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareImageFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmEntry.setStatus("current")
_CucsFirmwareImageFsmInstanceId_Type = CucsManagedObjectId
_CucsFirmwareImageFsmInstanceId_Object = MibTableColumn
cucsFirmwareImageFsmInstanceId = _CucsFirmwareImageFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36, 1, 1),
    _CucsFirmwareImageFsmInstanceId_Type()
)
cucsFirmwareImageFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmInstanceId.setStatus("current")
_CucsFirmwareImageFsmDn_Type = CucsManagedObjectDn
_CucsFirmwareImageFsmDn_Object = MibTableColumn
cucsFirmwareImageFsmDn = _CucsFirmwareImageFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36, 1, 2),
    _CucsFirmwareImageFsmDn_Type()
)
cucsFirmwareImageFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmDn.setStatus("current")
_CucsFirmwareImageFsmRn_Type = SnmpAdminString
_CucsFirmwareImageFsmRn_Object = MibTableColumn
cucsFirmwareImageFsmRn = _CucsFirmwareImageFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36, 1, 3),
    _CucsFirmwareImageFsmRn_Type()
)
cucsFirmwareImageFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmRn.setStatus("current")
_CucsFirmwareImageFsmCompletionTime_Type = DateAndTime
_CucsFirmwareImageFsmCompletionTime_Object = MibTableColumn
cucsFirmwareImageFsmCompletionTime = _CucsFirmwareImageFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36, 1, 4),
    _CucsFirmwareImageFsmCompletionTime_Type()
)
cucsFirmwareImageFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmCompletionTime.setStatus("current")
_CucsFirmwareImageFsmCurrentFsm_Type = CucsFirmwareImageFsmCurrentFsm
_CucsFirmwareImageFsmCurrentFsm_Object = MibTableColumn
cucsFirmwareImageFsmCurrentFsm = _CucsFirmwareImageFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36, 1, 5),
    _CucsFirmwareImageFsmCurrentFsm_Type()
)
cucsFirmwareImageFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmCurrentFsm.setStatus("current")
_CucsFirmwareImageFsmDescrData_Type = SnmpAdminString
_CucsFirmwareImageFsmDescrData_Object = MibTableColumn
cucsFirmwareImageFsmDescrData = _CucsFirmwareImageFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36, 1, 6),
    _CucsFirmwareImageFsmDescrData_Type()
)
cucsFirmwareImageFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmDescrData.setStatus("current")
_CucsFirmwareImageFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsFirmwareImageFsmFsmStatus_Object = MibTableColumn
cucsFirmwareImageFsmFsmStatus = _CucsFirmwareImageFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36, 1, 7),
    _CucsFirmwareImageFsmFsmStatus_Type()
)
cucsFirmwareImageFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmFsmStatus.setStatus("current")
_CucsFirmwareImageFsmProgress_Type = Gauge32
_CucsFirmwareImageFsmProgress_Object = MibTableColumn
cucsFirmwareImageFsmProgress = _CucsFirmwareImageFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36, 1, 8),
    _CucsFirmwareImageFsmProgress_Type()
)
cucsFirmwareImageFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmProgress.setStatus("current")
_CucsFirmwareImageFsmRmtErrCode_Type = Gauge32
_CucsFirmwareImageFsmRmtErrCode_Object = MibTableColumn
cucsFirmwareImageFsmRmtErrCode = _CucsFirmwareImageFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36, 1, 9),
    _CucsFirmwareImageFsmRmtErrCode_Type()
)
cucsFirmwareImageFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmRmtErrCode.setStatus("current")
_CucsFirmwareImageFsmRmtErrDescr_Type = SnmpAdminString
_CucsFirmwareImageFsmRmtErrDescr_Object = MibTableColumn
cucsFirmwareImageFsmRmtErrDescr = _CucsFirmwareImageFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36, 1, 10),
    _CucsFirmwareImageFsmRmtErrDescr_Type()
)
cucsFirmwareImageFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmRmtErrDescr.setStatus("current")
_CucsFirmwareImageFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsFirmwareImageFsmRmtRslt_Object = MibTableColumn
cucsFirmwareImageFsmRmtRslt = _CucsFirmwareImageFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 36, 1, 11),
    _CucsFirmwareImageFsmRmtRslt_Type()
)
cucsFirmwareImageFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmRmtRslt.setStatus("current")
_CucsFirmwareImageFsmStageTable_Object = MibTable
cucsFirmwareImageFsmStageTable = _CucsFirmwareImageFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 37)
)
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStageTable.setStatus("current")
_CucsFirmwareImageFsmStageEntry_Object = MibTableRow
cucsFirmwareImageFsmStageEntry = _CucsFirmwareImageFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 37, 1)
)
cucsFirmwareImageFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareImageFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStageEntry.setStatus("current")
_CucsFirmwareImageFsmStageInstanceId_Type = CucsManagedObjectId
_CucsFirmwareImageFsmStageInstanceId_Object = MibTableColumn
cucsFirmwareImageFsmStageInstanceId = _CucsFirmwareImageFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 37, 1, 1),
    _CucsFirmwareImageFsmStageInstanceId_Type()
)
cucsFirmwareImageFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStageInstanceId.setStatus("current")
_CucsFirmwareImageFsmStageDn_Type = CucsManagedObjectDn
_CucsFirmwareImageFsmStageDn_Object = MibTableColumn
cucsFirmwareImageFsmStageDn = _CucsFirmwareImageFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 37, 1, 2),
    _CucsFirmwareImageFsmStageDn_Type()
)
cucsFirmwareImageFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStageDn.setStatus("current")
_CucsFirmwareImageFsmStageRn_Type = SnmpAdminString
_CucsFirmwareImageFsmStageRn_Object = MibTableColumn
cucsFirmwareImageFsmStageRn = _CucsFirmwareImageFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 37, 1, 3),
    _CucsFirmwareImageFsmStageRn_Type()
)
cucsFirmwareImageFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStageRn.setStatus("current")
_CucsFirmwareImageFsmStageDescrData_Type = SnmpAdminString
_CucsFirmwareImageFsmStageDescrData_Object = MibTableColumn
cucsFirmwareImageFsmStageDescrData = _CucsFirmwareImageFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 37, 1, 4),
    _CucsFirmwareImageFsmStageDescrData_Type()
)
cucsFirmwareImageFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStageDescrData.setStatus("current")
_CucsFirmwareImageFsmStageLastUpdateTime_Type = DateAndTime
_CucsFirmwareImageFsmStageLastUpdateTime_Object = MibTableColumn
cucsFirmwareImageFsmStageLastUpdateTime = _CucsFirmwareImageFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 37, 1, 5),
    _CucsFirmwareImageFsmStageLastUpdateTime_Type()
)
cucsFirmwareImageFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStageLastUpdateTime.setStatus("current")
_CucsFirmwareImageFsmStageName_Type = CucsFirmwareImageFsmStageName
_CucsFirmwareImageFsmStageName_Object = MibTableColumn
cucsFirmwareImageFsmStageName = _CucsFirmwareImageFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 37, 1, 6),
    _CucsFirmwareImageFsmStageName_Type()
)
cucsFirmwareImageFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStageName.setStatus("current")
_CucsFirmwareImageFsmStageOrder_Type = Gauge32
_CucsFirmwareImageFsmStageOrder_Object = MibTableColumn
cucsFirmwareImageFsmStageOrder = _CucsFirmwareImageFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 37, 1, 7),
    _CucsFirmwareImageFsmStageOrder_Type()
)
cucsFirmwareImageFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStageOrder.setStatus("current")
_CucsFirmwareImageFsmStageRetry_Type = Gauge32
_CucsFirmwareImageFsmStageRetry_Object = MibTableColumn
cucsFirmwareImageFsmStageRetry = _CucsFirmwareImageFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 37, 1, 8),
    _CucsFirmwareImageFsmStageRetry_Type()
)
cucsFirmwareImageFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStageRetry.setStatus("current")
_CucsFirmwareImageFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsFirmwareImageFsmStageStageStatus_Object = MibTableColumn
cucsFirmwareImageFsmStageStageStatus = _CucsFirmwareImageFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 37, 1, 9),
    _CucsFirmwareImageFsmStageStageStatus_Type()
)
cucsFirmwareImageFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageFsmStageStageStatus.setStatus("current")
_CucsFirmwareInfraTable_Object = MibTable
cucsFirmwareInfraTable = _CucsFirmwareInfraTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38)
)
if mibBuilder.loadTexts:
    cucsFirmwareInfraTable.setStatus("current")
_CucsFirmwareInfraEntry_Object = MibTableRow
cucsFirmwareInfraEntry = _CucsFirmwareInfraEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1)
)
cucsFirmwareInfraEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareInfraInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareInfraEntry.setStatus("current")
_CucsFirmwareInfraInstanceId_Type = CucsManagedObjectId
_CucsFirmwareInfraInstanceId_Object = MibTableColumn
cucsFirmwareInfraInstanceId = _CucsFirmwareInfraInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 1),
    _CucsFirmwareInfraInstanceId_Type()
)
cucsFirmwareInfraInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareInfraInstanceId.setStatus("current")
_CucsFirmwareInfraDn_Type = CucsManagedObjectDn
_CucsFirmwareInfraDn_Object = MibTableColumn
cucsFirmwareInfraDn = _CucsFirmwareInfraDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 2),
    _CucsFirmwareInfraDn_Type()
)
cucsFirmwareInfraDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraDn.setStatus("current")
_CucsFirmwareInfraRn_Type = SnmpAdminString
_CucsFirmwareInfraRn_Object = MibTableColumn
cucsFirmwareInfraRn = _CucsFirmwareInfraRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 3),
    _CucsFirmwareInfraRn_Type()
)
cucsFirmwareInfraRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraRn.setStatus("current")
_CucsFirmwareInfraAdminState_Type = CucsTrigAdminState
_CucsFirmwareInfraAdminState_Object = MibTableColumn
cucsFirmwareInfraAdminState = _CucsFirmwareInfraAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 4),
    _CucsFirmwareInfraAdminState_Type()
)
cucsFirmwareInfraAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraAdminState.setStatus("current")
_CucsFirmwareInfraAutoDelete_Type = TruthValue
_CucsFirmwareInfraAutoDelete_Object = MibTableColumn
cucsFirmwareInfraAutoDelete = _CucsFirmwareInfraAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 5),
    _CucsFirmwareInfraAutoDelete_Type()
)
cucsFirmwareInfraAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraAutoDelete.setStatus("current")
_CucsFirmwareInfraDescr_Type = SnmpAdminString
_CucsFirmwareInfraDescr_Object = MibTableColumn
cucsFirmwareInfraDescr = _CucsFirmwareInfraDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 6),
    _CucsFirmwareInfraDescr_Type()
)
cucsFirmwareInfraDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraDescr.setStatus("current")
_CucsFirmwareInfraIgnoreCap_Type = TruthValue
_CucsFirmwareInfraIgnoreCap_Object = MibTableColumn
cucsFirmwareInfraIgnoreCap = _CucsFirmwareInfraIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 7),
    _CucsFirmwareInfraIgnoreCap_Type()
)
cucsFirmwareInfraIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraIgnoreCap.setStatus("current")
_CucsFirmwareInfraIntId_Type = SnmpAdminString
_CucsFirmwareInfraIntId_Object = MibTableColumn
cucsFirmwareInfraIntId = _CucsFirmwareInfraIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 8),
    _CucsFirmwareInfraIntId_Type()
)
cucsFirmwareInfraIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraIntId.setStatus("current")
_CucsFirmwareInfraName_Type = SnmpAdminString
_CucsFirmwareInfraName_Object = MibTableColumn
cucsFirmwareInfraName = _CucsFirmwareInfraName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 9),
    _CucsFirmwareInfraName_Type()
)
cucsFirmwareInfraName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraName.setStatus("current")
_CucsFirmwareInfraOperScheduler_Type = SnmpAdminString
_CucsFirmwareInfraOperScheduler_Object = MibTableColumn
cucsFirmwareInfraOperScheduler = _CucsFirmwareInfraOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 10),
    _CucsFirmwareInfraOperScheduler_Type()
)
cucsFirmwareInfraOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraOperScheduler.setStatus("current")
_CucsFirmwareInfraOperState_Type = CucsTrigTrigOperState
_CucsFirmwareInfraOperState_Object = MibTableColumn
cucsFirmwareInfraOperState = _CucsFirmwareInfraOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 11),
    _CucsFirmwareInfraOperState_Type()
)
cucsFirmwareInfraOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraOperState.setStatus("current")
_CucsFirmwareInfraOperVersion_Type = SnmpAdminString
_CucsFirmwareInfraOperVersion_Object = MibTableColumn
cucsFirmwareInfraOperVersion = _CucsFirmwareInfraOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 12),
    _CucsFirmwareInfraOperVersion_Type()
)
cucsFirmwareInfraOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraOperVersion.setStatus("current")
_CucsFirmwareInfraPolicyLevel_Type = Gauge32
_CucsFirmwareInfraPolicyLevel_Object = MibTableColumn
cucsFirmwareInfraPolicyLevel = _CucsFirmwareInfraPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 13),
    _CucsFirmwareInfraPolicyLevel_Type()
)
cucsFirmwareInfraPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPolicyLevel.setStatus("current")
_CucsFirmwareInfraPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFirmwareInfraPolicyOwner_Object = MibTableColumn
cucsFirmwareInfraPolicyOwner = _CucsFirmwareInfraPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 14),
    _CucsFirmwareInfraPolicyOwner_Type()
)
cucsFirmwareInfraPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPolicyOwner.setStatus("current")
_CucsFirmwareInfraScheduler_Type = SnmpAdminString
_CucsFirmwareInfraScheduler_Object = MibTableColumn
cucsFirmwareInfraScheduler = _CucsFirmwareInfraScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 38, 1, 15),
    _CucsFirmwareInfraScheduler_Type()
)
cucsFirmwareInfraScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraScheduler.setStatus("current")
_CucsFirmwareInfraPackTable_Object = MibTable
cucsFirmwareInfraPackTable = _CucsFirmwareInfraPackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39)
)
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackTable.setStatus("current")
_CucsFirmwareInfraPackEntry_Object = MibTableRow
cucsFirmwareInfraPackEntry = _CucsFirmwareInfraPackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1)
)
cucsFirmwareInfraPackEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareInfraPackInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackEntry.setStatus("current")
_CucsFirmwareInfraPackInstanceId_Type = CucsManagedObjectId
_CucsFirmwareInfraPackInstanceId_Object = MibTableColumn
cucsFirmwareInfraPackInstanceId = _CucsFirmwareInfraPackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 1),
    _CucsFirmwareInfraPackInstanceId_Type()
)
cucsFirmwareInfraPackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackInstanceId.setStatus("current")
_CucsFirmwareInfraPackDn_Type = CucsManagedObjectDn
_CucsFirmwareInfraPackDn_Object = MibTableColumn
cucsFirmwareInfraPackDn = _CucsFirmwareInfraPackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 2),
    _CucsFirmwareInfraPackDn_Type()
)
cucsFirmwareInfraPackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackDn.setStatus("current")
_CucsFirmwareInfraPackRn_Type = SnmpAdminString
_CucsFirmwareInfraPackRn_Object = MibTableColumn
cucsFirmwareInfraPackRn = _CucsFirmwareInfraPackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 3),
    _CucsFirmwareInfraPackRn_Type()
)
cucsFirmwareInfraPackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackRn.setStatus("current")
_CucsFirmwareInfraPackDescr_Type = SnmpAdminString
_CucsFirmwareInfraPackDescr_Object = MibTableColumn
cucsFirmwareInfraPackDescr = _CucsFirmwareInfraPackDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 4),
    _CucsFirmwareInfraPackDescr_Type()
)
cucsFirmwareInfraPackDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackDescr.setStatus("current")
_CucsFirmwareInfraPackForceDeploy_Type = TruthValue
_CucsFirmwareInfraPackForceDeploy_Object = MibTableColumn
cucsFirmwareInfraPackForceDeploy = _CucsFirmwareInfraPackForceDeploy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 5),
    _CucsFirmwareInfraPackForceDeploy_Type()
)
cucsFirmwareInfraPackForceDeploy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackForceDeploy.setStatus("current")
_CucsFirmwareInfraPackInfraBundleName_Type = SnmpAdminString
_CucsFirmwareInfraPackInfraBundleName_Object = MibTableColumn
cucsFirmwareInfraPackInfraBundleName = _CucsFirmwareInfraPackInfraBundleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 6),
    _CucsFirmwareInfraPackInfraBundleName_Type()
)
cucsFirmwareInfraPackInfraBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackInfraBundleName.setStatus("current")
_CucsFirmwareInfraPackInfraBundleVersion_Type = SnmpAdminString
_CucsFirmwareInfraPackInfraBundleVersion_Object = MibTableColumn
cucsFirmwareInfraPackInfraBundleVersion = _CucsFirmwareInfraPackInfraBundleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 7),
    _CucsFirmwareInfraPackInfraBundleVersion_Type()
)
cucsFirmwareInfraPackInfraBundleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackInfraBundleVersion.setStatus("current")
_CucsFirmwareInfraPackIntId_Type = SnmpAdminString
_CucsFirmwareInfraPackIntId_Object = MibTableColumn
cucsFirmwareInfraPackIntId = _CucsFirmwareInfraPackIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 8),
    _CucsFirmwareInfraPackIntId_Type()
)
cucsFirmwareInfraPackIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackIntId.setStatus("current")
_CucsFirmwareInfraPackMode_Type = CucsFirmwarePackMode
_CucsFirmwareInfraPackMode_Object = MibTableColumn
cucsFirmwareInfraPackMode = _CucsFirmwareInfraPackMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 9),
    _CucsFirmwareInfraPackMode_Type()
)
cucsFirmwareInfraPackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackMode.setStatus("current")
_CucsFirmwareInfraPackName_Type = SnmpAdminString
_CucsFirmwareInfraPackName_Object = MibTableColumn
cucsFirmwareInfraPackName = _CucsFirmwareInfraPackName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 10),
    _CucsFirmwareInfraPackName_Type()
)
cucsFirmwareInfraPackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackName.setStatus("current")
_CucsFirmwareInfraPackPolicyLevel_Type = Gauge32
_CucsFirmwareInfraPackPolicyLevel_Object = MibTableColumn
cucsFirmwareInfraPackPolicyLevel = _CucsFirmwareInfraPackPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 11),
    _CucsFirmwareInfraPackPolicyLevel_Type()
)
cucsFirmwareInfraPackPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackPolicyLevel.setStatus("current")
_CucsFirmwareInfraPackPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFirmwareInfraPackPolicyOwner_Object = MibTableColumn
cucsFirmwareInfraPackPolicyOwner = _CucsFirmwareInfraPackPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 12),
    _CucsFirmwareInfraPackPolicyOwner_Type()
)
cucsFirmwareInfraPackPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackPolicyOwner.setStatus("current")
_CucsFirmwareInfraPackStageSize_Type = Gauge32
_CucsFirmwareInfraPackStageSize_Object = MibTableColumn
cucsFirmwareInfraPackStageSize = _CucsFirmwareInfraPackStageSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 13),
    _CucsFirmwareInfraPackStageSize_Type()
)
cucsFirmwareInfraPackStageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackStageSize.setStatus("current")
_CucsFirmwareInfraPackUpdateTrigger_Type = DateAndTime
_CucsFirmwareInfraPackUpdateTrigger_Object = MibTableColumn
cucsFirmwareInfraPackUpdateTrigger = _CucsFirmwareInfraPackUpdateTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 14),
    _CucsFirmwareInfraPackUpdateTrigger_Type()
)
cucsFirmwareInfraPackUpdateTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackUpdateTrigger.setStatus("current")
_CucsFirmwareInfraPackSkipValidation_Type = TruthValue
_CucsFirmwareInfraPackSkipValidation_Object = MibTableColumn
cucsFirmwareInfraPackSkipValidation = _CucsFirmwareInfraPackSkipValidation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 39, 1, 15),
    _CucsFirmwareInfraPackSkipValidation_Type()
)
cucsFirmwareInfraPackSkipValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInfraPackSkipValidation.setStatus("current")
_CucsFirmwareInstallImpactTable_Object = MibTable
cucsFirmwareInstallImpactTable = _CucsFirmwareInstallImpactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 40)
)
if mibBuilder.loadTexts:
    cucsFirmwareInstallImpactTable.setStatus("current")
_CucsFirmwareInstallImpactEntry_Object = MibTableRow
cucsFirmwareInstallImpactEntry = _CucsFirmwareInstallImpactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 40, 1)
)
cucsFirmwareInstallImpactEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareInstallImpactInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareInstallImpactEntry.setStatus("current")
_CucsFirmwareInstallImpactInstanceId_Type = CucsManagedObjectId
_CucsFirmwareInstallImpactInstanceId_Object = MibTableColumn
cucsFirmwareInstallImpactInstanceId = _CucsFirmwareInstallImpactInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 40, 1, 1),
    _CucsFirmwareInstallImpactInstanceId_Type()
)
cucsFirmwareInstallImpactInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareInstallImpactInstanceId.setStatus("current")
_CucsFirmwareInstallImpactDn_Type = CucsManagedObjectDn
_CucsFirmwareInstallImpactDn_Object = MibTableColumn
cucsFirmwareInstallImpactDn = _CucsFirmwareInstallImpactDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 40, 1, 2),
    _CucsFirmwareInstallImpactDn_Type()
)
cucsFirmwareInstallImpactDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallImpactDn.setStatus("current")
_CucsFirmwareInstallImpactRn_Type = SnmpAdminString
_CucsFirmwareInstallImpactRn_Object = MibTableColumn
cucsFirmwareInstallImpactRn = _CucsFirmwareInstallImpactRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 40, 1, 3),
    _CucsFirmwareInstallImpactRn_Type()
)
cucsFirmwareInstallImpactRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallImpactRn.setStatus("current")
_CucsFirmwareInstallImpactDescr_Type = SnmpAdminString
_CucsFirmwareInstallImpactDescr_Object = MibTableColumn
cucsFirmwareInstallImpactDescr = _CucsFirmwareInstallImpactDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 40, 1, 4),
    _CucsFirmwareInstallImpactDescr_Type()
)
cucsFirmwareInstallImpactDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallImpactDescr.setStatus("current")
_CucsFirmwareInstallImpactKeyDn_Type = SnmpAdminString
_CucsFirmwareInstallImpactKeyDn_Object = MibTableColumn
cucsFirmwareInstallImpactKeyDn = _CucsFirmwareInstallImpactKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 40, 1, 5),
    _CucsFirmwareInstallImpactKeyDn_Type()
)
cucsFirmwareInstallImpactKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallImpactKeyDn.setStatus("current")
_CucsFirmwareInstallImpactMaintPolicyDn_Type = SnmpAdminString
_CucsFirmwareInstallImpactMaintPolicyDn_Object = MibTableColumn
cucsFirmwareInstallImpactMaintPolicyDn = _CucsFirmwareInstallImpactMaintPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 40, 1, 6),
    _CucsFirmwareInstallImpactMaintPolicyDn_Type()
)
cucsFirmwareInstallImpactMaintPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallImpactMaintPolicyDn.setStatus("current")
_CucsFirmwareInstallImpactRebootPolicy_Type = SnmpAdminString
_CucsFirmwareInstallImpactRebootPolicy_Object = MibTableColumn
cucsFirmwareInstallImpactRebootPolicy = _CucsFirmwareInstallImpactRebootPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 40, 1, 7),
    _CucsFirmwareInstallImpactRebootPolicy_Type()
)
cucsFirmwareInstallImpactRebootPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallImpactRebootPolicy.setStatus("current")
_CucsFirmwareInstallImpactSubject_Type = CucsFirmwareEquipmentType
_CucsFirmwareInstallImpactSubject_Object = MibTableColumn
cucsFirmwareInstallImpactSubject = _CucsFirmwareInstallImpactSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 40, 1, 8),
    _CucsFirmwareInstallImpactSubject_Type()
)
cucsFirmwareInstallImpactSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallImpactSubject.setStatus("current")
_CucsFirmwareInstallImpactType_Type = CucsFirmwareImpactType
_CucsFirmwareInstallImpactType_Object = MibTableColumn
cucsFirmwareInstallImpactType = _CucsFirmwareInstallImpactType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 40, 1, 9),
    _CucsFirmwareInstallImpactType_Type()
)
cucsFirmwareInstallImpactType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareInstallImpactType.setStatus("current")
_CucsFirmwareRackTable_Object = MibTable
cucsFirmwareRackTable = _CucsFirmwareRackTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 41)
)
if mibBuilder.loadTexts:
    cucsFirmwareRackTable.setStatus("current")
_CucsFirmwareRackEntry_Object = MibTableRow
cucsFirmwareRackEntry = _CucsFirmwareRackEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 41, 1)
)
cucsFirmwareRackEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareRackInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareRackEntry.setStatus("current")
_CucsFirmwareRackInstanceId_Type = CucsManagedObjectId
_CucsFirmwareRackInstanceId_Object = MibTableColumn
cucsFirmwareRackInstanceId = _CucsFirmwareRackInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 41, 1, 1),
    _CucsFirmwareRackInstanceId_Type()
)
cucsFirmwareRackInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareRackInstanceId.setStatus("current")
_CucsFirmwareRackDn_Type = CucsManagedObjectDn
_CucsFirmwareRackDn_Object = MibTableColumn
cucsFirmwareRackDn = _CucsFirmwareRackDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 41, 1, 2),
    _CucsFirmwareRackDn_Type()
)
cucsFirmwareRackDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareRackDn.setStatus("current")
_CucsFirmwareRackRn_Type = SnmpAdminString
_CucsFirmwareRackRn_Object = MibTableColumn
cucsFirmwareRackRn = _CucsFirmwareRackRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 41, 1, 3),
    _CucsFirmwareRackRn_Type()
)
cucsFirmwareRackRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareRackRn.setStatus("current")
_CucsFirmwareRackOperVersion_Type = SnmpAdminString
_CucsFirmwareRackOperVersion_Object = MibTableColumn
cucsFirmwareRackOperVersion = _CucsFirmwareRackOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 41, 1, 4),
    _CucsFirmwareRackOperVersion_Type()
)
cucsFirmwareRackOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareRackOperVersion.setStatus("current")
_CucsFirmwareStatusTable_Object = MibTable
cucsFirmwareStatusTable = _CucsFirmwareStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 42)
)
if mibBuilder.loadTexts:
    cucsFirmwareStatusTable.setStatus("current")
_CucsFirmwareStatusEntry_Object = MibTableRow
cucsFirmwareStatusEntry = _CucsFirmwareStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 42, 1)
)
cucsFirmwareStatusEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareStatusEntry.setStatus("current")
_CucsFirmwareStatusInstanceId_Type = CucsManagedObjectId
_CucsFirmwareStatusInstanceId_Object = MibTableColumn
cucsFirmwareStatusInstanceId = _CucsFirmwareStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 42, 1, 1),
    _CucsFirmwareStatusInstanceId_Type()
)
cucsFirmwareStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareStatusInstanceId.setStatus("current")
_CucsFirmwareStatusDn_Type = CucsManagedObjectDn
_CucsFirmwareStatusDn_Object = MibTableColumn
cucsFirmwareStatusDn = _CucsFirmwareStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 42, 1, 2),
    _CucsFirmwareStatusDn_Type()
)
cucsFirmwareStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareStatusDn.setStatus("current")
_CucsFirmwareStatusRn_Type = SnmpAdminString
_CucsFirmwareStatusRn_Object = MibTableColumn
cucsFirmwareStatusRn = _CucsFirmwareStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 42, 1, 3),
    _CucsFirmwareStatusRn_Type()
)
cucsFirmwareStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareStatusRn.setStatus("current")
_CucsFirmwareStatusOperState_Type = CucsFirmwareImageState
_CucsFirmwareStatusOperState_Object = MibTableColumn
cucsFirmwareStatusOperState = _CucsFirmwareStatusOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 42, 1, 4),
    _CucsFirmwareStatusOperState_Type()
)
cucsFirmwareStatusOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareStatusOperState.setStatus("current")
_CucsFirmwareStatusPackageVersion_Type = SnmpAdminString
_CucsFirmwareStatusPackageVersion_Object = MibTableColumn
cucsFirmwareStatusPackageVersion = _CucsFirmwareStatusPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 42, 1, 5),
    _CucsFirmwareStatusPackageVersion_Type()
)
cucsFirmwareStatusPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareStatusPackageVersion.setStatus("current")
_CucsFirmwareStatusCimcVersion_Type = SnmpAdminString
_CucsFirmwareStatusCimcVersion_Object = MibTableColumn
cucsFirmwareStatusCimcVersion = _CucsFirmwareStatusCimcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 42, 1, 6),
    _CucsFirmwareStatusCimcVersion_Type()
)
cucsFirmwareStatusCimcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareStatusCimcVersion.setStatus("current")
_CucsFirmwareStatusFirmwareState_Type = CucsFirmwareFirmwareState
_CucsFirmwareStatusFirmwareState_Object = MibTableColumn
cucsFirmwareStatusFirmwareState = _CucsFirmwareStatusFirmwareState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 42, 1, 7),
    _CucsFirmwareStatusFirmwareState_Type()
)
cucsFirmwareStatusFirmwareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareStatusFirmwareState.setStatus("current")
_CucsFirmwareStatusPldVersion_Type = SnmpAdminString
_CucsFirmwareStatusPldVersion_Object = MibTableColumn
cucsFirmwareStatusPldVersion = _CucsFirmwareStatusPldVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 42, 1, 8),
    _CucsFirmwareStatusPldVersion_Type()
)
cucsFirmwareStatusPldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareStatusPldVersion.setStatus("current")
_CucsFirmwareSystemTable_Object = MibTable
cucsFirmwareSystemTable = _CucsFirmwareSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43)
)
if mibBuilder.loadTexts:
    cucsFirmwareSystemTable.setStatus("current")
_CucsFirmwareSystemEntry_Object = MibTableRow
cucsFirmwareSystemEntry = _CucsFirmwareSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1)
)
cucsFirmwareSystemEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareSystemEntry.setStatus("current")
_CucsFirmwareSystemInstanceId_Type = CucsManagedObjectId
_CucsFirmwareSystemInstanceId_Object = MibTableColumn
cucsFirmwareSystemInstanceId = _CucsFirmwareSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 1),
    _CucsFirmwareSystemInstanceId_Type()
)
cucsFirmwareSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareSystemInstanceId.setStatus("current")
_CucsFirmwareSystemDn_Type = CucsManagedObjectDn
_CucsFirmwareSystemDn_Object = MibTableColumn
cucsFirmwareSystemDn = _CucsFirmwareSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 2),
    _CucsFirmwareSystemDn_Type()
)
cucsFirmwareSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemDn.setStatus("current")
_CucsFirmwareSystemRn_Type = SnmpAdminString
_CucsFirmwareSystemRn_Object = MibTableColumn
cucsFirmwareSystemRn = _CucsFirmwareSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 3),
    _CucsFirmwareSystemRn_Type()
)
cucsFirmwareSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemRn.setStatus("current")
_CucsFirmwareSystemFsmDescr_Type = SnmpAdminString
_CucsFirmwareSystemFsmDescr_Object = MibTableColumn
cucsFirmwareSystemFsmDescr = _CucsFirmwareSystemFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 4),
    _CucsFirmwareSystemFsmDescr_Type()
)
cucsFirmwareSystemFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmDescr.setStatus("current")
_CucsFirmwareSystemFsmFlags_Type = SnmpAdminString
_CucsFirmwareSystemFsmFlags_Object = MibTableColumn
cucsFirmwareSystemFsmFlags = _CucsFirmwareSystemFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 5),
    _CucsFirmwareSystemFsmFlags_Type()
)
cucsFirmwareSystemFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmFlags.setStatus("current")
_CucsFirmwareSystemFsmPrev_Type = SnmpAdminString
_CucsFirmwareSystemFsmPrev_Object = MibTableColumn
cucsFirmwareSystemFsmPrev = _CucsFirmwareSystemFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 6),
    _CucsFirmwareSystemFsmPrev_Type()
)
cucsFirmwareSystemFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmPrev.setStatus("current")
_CucsFirmwareSystemFsmProgr_Type = Gauge32
_CucsFirmwareSystemFsmProgr_Object = MibTableColumn
cucsFirmwareSystemFsmProgr = _CucsFirmwareSystemFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 7),
    _CucsFirmwareSystemFsmProgr_Type()
)
cucsFirmwareSystemFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmProgr.setStatus("current")
_CucsFirmwareSystemFsmRmtInvErrCode_Type = Gauge32
_CucsFirmwareSystemFsmRmtInvErrCode_Object = MibTableColumn
cucsFirmwareSystemFsmRmtInvErrCode = _CucsFirmwareSystemFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 8),
    _CucsFirmwareSystemFsmRmtInvErrCode_Type()
)
cucsFirmwareSystemFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmRmtInvErrCode.setStatus("current")
_CucsFirmwareSystemFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsFirmwareSystemFsmRmtInvErrDescr_Object = MibTableColumn
cucsFirmwareSystemFsmRmtInvErrDescr = _CucsFirmwareSystemFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 9),
    _CucsFirmwareSystemFsmRmtInvErrDescr_Type()
)
cucsFirmwareSystemFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmRmtInvErrDescr.setStatus("current")
_CucsFirmwareSystemFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsFirmwareSystemFsmRmtInvRslt_Object = MibTableColumn
cucsFirmwareSystemFsmRmtInvRslt = _CucsFirmwareSystemFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 10),
    _CucsFirmwareSystemFsmRmtInvRslt_Type()
)
cucsFirmwareSystemFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmRmtInvRslt.setStatus("current")
_CucsFirmwareSystemFsmStageDescr_Type = SnmpAdminString
_CucsFirmwareSystemFsmStageDescr_Object = MibTableColumn
cucsFirmwareSystemFsmStageDescr = _CucsFirmwareSystemFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 11),
    _CucsFirmwareSystemFsmStageDescr_Type()
)
cucsFirmwareSystemFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStageDescr.setStatus("current")
_CucsFirmwareSystemFsmStamp_Type = DateAndTime
_CucsFirmwareSystemFsmStamp_Object = MibTableColumn
cucsFirmwareSystemFsmStamp = _CucsFirmwareSystemFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 12),
    _CucsFirmwareSystemFsmStamp_Type()
)
cucsFirmwareSystemFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStamp.setStatus("current")
_CucsFirmwareSystemFsmStatus_Type = SnmpAdminString
_CucsFirmwareSystemFsmStatus_Object = MibTableColumn
cucsFirmwareSystemFsmStatus = _CucsFirmwareSystemFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 13),
    _CucsFirmwareSystemFsmStatus_Type()
)
cucsFirmwareSystemFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStatus.setStatus("current")
_CucsFirmwareSystemFsmTry_Type = Gauge32
_CucsFirmwareSystemFsmTry_Object = MibTableColumn
cucsFirmwareSystemFsmTry = _CucsFirmwareSystemFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 14),
    _CucsFirmwareSystemFsmTry_Type()
)
cucsFirmwareSystemFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmTry.setStatus("current")
_CucsFirmwareSystemOperState_Type = CucsFirmwareInstallState
_CucsFirmwareSystemOperState_Object = MibTableColumn
cucsFirmwareSystemOperState = _CucsFirmwareSystemOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 15),
    _CucsFirmwareSystemOperState_Type()
)
cucsFirmwareSystemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemOperState.setStatus("current")
_CucsFirmwareSystemState_Type = CucsFirmwareFwState
_CucsFirmwareSystemState_Object = MibTableColumn
cucsFirmwareSystemState = _CucsFirmwareSystemState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 43, 1, 16),
    _CucsFirmwareSystemState_Type()
)
cucsFirmwareSystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemState.setStatus("current")
_CucsFirmwareSystemCompCheckResultTable_Object = MibTable
cucsFirmwareSystemCompCheckResultTable = _CucsFirmwareSystemCompCheckResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 44)
)
if mibBuilder.loadTexts:
    cucsFirmwareSystemCompCheckResultTable.setStatus("current")
_CucsFirmwareSystemCompCheckResultEntry_Object = MibTableRow
cucsFirmwareSystemCompCheckResultEntry = _CucsFirmwareSystemCompCheckResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 44, 1)
)
cucsFirmwareSystemCompCheckResultEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareSystemCompCheckResultInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareSystemCompCheckResultEntry.setStatus("current")
_CucsFirmwareSystemCompCheckResultInstanceId_Type = CucsManagedObjectId
_CucsFirmwareSystemCompCheckResultInstanceId_Object = MibTableColumn
cucsFirmwareSystemCompCheckResultInstanceId = _CucsFirmwareSystemCompCheckResultInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 44, 1, 1),
    _CucsFirmwareSystemCompCheckResultInstanceId_Type()
)
cucsFirmwareSystemCompCheckResultInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareSystemCompCheckResultInstanceId.setStatus("current")
_CucsFirmwareSystemCompCheckResultDn_Type = CucsManagedObjectDn
_CucsFirmwareSystemCompCheckResultDn_Object = MibTableColumn
cucsFirmwareSystemCompCheckResultDn = _CucsFirmwareSystemCompCheckResultDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 44, 1, 2),
    _CucsFirmwareSystemCompCheckResultDn_Type()
)
cucsFirmwareSystemCompCheckResultDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemCompCheckResultDn.setStatus("current")
_CucsFirmwareSystemCompCheckResultRn_Type = SnmpAdminString
_CucsFirmwareSystemCompCheckResultRn_Object = MibTableColumn
cucsFirmwareSystemCompCheckResultRn = _CucsFirmwareSystemCompCheckResultRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 44, 1, 3),
    _CucsFirmwareSystemCompCheckResultRn_Type()
)
cucsFirmwareSystemCompCheckResultRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemCompCheckResultRn.setStatus("current")
_CucsFirmwareSystemCompCheckResultKeyDescr_Type = SnmpAdminString
_CucsFirmwareSystemCompCheckResultKeyDescr_Object = MibTableColumn
cucsFirmwareSystemCompCheckResultKeyDescr = _CucsFirmwareSystemCompCheckResultKeyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 44, 1, 4),
    _CucsFirmwareSystemCompCheckResultKeyDescr_Type()
)
cucsFirmwareSystemCompCheckResultKeyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemCompCheckResultKeyDescr.setStatus("current")
_CucsFirmwareSystemCompCheckResultKeyDn_Type = SnmpAdminString
_CucsFirmwareSystemCompCheckResultKeyDn_Object = MibTableColumn
cucsFirmwareSystemCompCheckResultKeyDn = _CucsFirmwareSystemCompCheckResultKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 44, 1, 5),
    _CucsFirmwareSystemCompCheckResultKeyDn_Type()
)
cucsFirmwareSystemCompCheckResultKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemCompCheckResultKeyDn.setStatus("current")
_CucsFirmwareSystemCompCheckResultNonCompDescr_Type = SnmpAdminString
_CucsFirmwareSystemCompCheckResultNonCompDescr_Object = MibTableColumn
cucsFirmwareSystemCompCheckResultNonCompDescr = _CucsFirmwareSystemCompCheckResultNonCompDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 44, 1, 6),
    _CucsFirmwareSystemCompCheckResultNonCompDescr_Type()
)
cucsFirmwareSystemCompCheckResultNonCompDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemCompCheckResultNonCompDescr.setStatus("current")
_CucsFirmwareSystemCompCheckResultNonCompDns_Type = SnmpAdminString
_CucsFirmwareSystemCompCheckResultNonCompDns_Object = MibTableColumn
cucsFirmwareSystemCompCheckResultNonCompDns = _CucsFirmwareSystemCompCheckResultNonCompDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 44, 1, 7),
    _CucsFirmwareSystemCompCheckResultNonCompDns_Type()
)
cucsFirmwareSystemCompCheckResultNonCompDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemCompCheckResultNonCompDns.setStatus("current")
_CucsFirmwareSystemCompCheckResultSubject_Type = CucsFirmwareEquipmentType
_CucsFirmwareSystemCompCheckResultSubject_Object = MibTableColumn
cucsFirmwareSystemCompCheckResultSubject = _CucsFirmwareSystemCompCheckResultSubject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 44, 1, 8),
    _CucsFirmwareSystemCompCheckResultSubject_Type()
)
cucsFirmwareSystemCompCheckResultSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemCompCheckResultSubject.setStatus("current")
_CucsFirmwareSystemFsmTable_Object = MibTable
cucsFirmwareSystemFsmTable = _CucsFirmwareSystemFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45)
)
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmTable.setStatus("current")
_CucsFirmwareSystemFsmEntry_Object = MibTableRow
cucsFirmwareSystemFsmEntry = _CucsFirmwareSystemFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45, 1)
)
cucsFirmwareSystemFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareSystemFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmEntry.setStatus("current")
_CucsFirmwareSystemFsmInstanceId_Type = CucsManagedObjectId
_CucsFirmwareSystemFsmInstanceId_Object = MibTableColumn
cucsFirmwareSystemFsmInstanceId = _CucsFirmwareSystemFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45, 1, 1),
    _CucsFirmwareSystemFsmInstanceId_Type()
)
cucsFirmwareSystemFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmInstanceId.setStatus("current")
_CucsFirmwareSystemFsmDn_Type = CucsManagedObjectDn
_CucsFirmwareSystemFsmDn_Object = MibTableColumn
cucsFirmwareSystemFsmDn = _CucsFirmwareSystemFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45, 1, 2),
    _CucsFirmwareSystemFsmDn_Type()
)
cucsFirmwareSystemFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmDn.setStatus("current")
_CucsFirmwareSystemFsmRn_Type = SnmpAdminString
_CucsFirmwareSystemFsmRn_Object = MibTableColumn
cucsFirmwareSystemFsmRn = _CucsFirmwareSystemFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45, 1, 3),
    _CucsFirmwareSystemFsmRn_Type()
)
cucsFirmwareSystemFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmRn.setStatus("current")
_CucsFirmwareSystemFsmCompletionTime_Type = DateAndTime
_CucsFirmwareSystemFsmCompletionTime_Object = MibTableColumn
cucsFirmwareSystemFsmCompletionTime = _CucsFirmwareSystemFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45, 1, 4),
    _CucsFirmwareSystemFsmCompletionTime_Type()
)
cucsFirmwareSystemFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmCompletionTime.setStatus("current")
_CucsFirmwareSystemFsmCurrentFsm_Type = CucsFirmwareSystemFsmCurrentFsm
_CucsFirmwareSystemFsmCurrentFsm_Object = MibTableColumn
cucsFirmwareSystemFsmCurrentFsm = _CucsFirmwareSystemFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45, 1, 5),
    _CucsFirmwareSystemFsmCurrentFsm_Type()
)
cucsFirmwareSystemFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmCurrentFsm.setStatus("current")
_CucsFirmwareSystemFsmDescrData_Type = SnmpAdminString
_CucsFirmwareSystemFsmDescrData_Object = MibTableColumn
cucsFirmwareSystemFsmDescrData = _CucsFirmwareSystemFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45, 1, 6),
    _CucsFirmwareSystemFsmDescrData_Type()
)
cucsFirmwareSystemFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmDescrData.setStatus("current")
_CucsFirmwareSystemFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsFirmwareSystemFsmFsmStatus_Object = MibTableColumn
cucsFirmwareSystemFsmFsmStatus = _CucsFirmwareSystemFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45, 1, 7),
    _CucsFirmwareSystemFsmFsmStatus_Type()
)
cucsFirmwareSystemFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmFsmStatus.setStatus("current")
_CucsFirmwareSystemFsmProgress_Type = Gauge32
_CucsFirmwareSystemFsmProgress_Object = MibTableColumn
cucsFirmwareSystemFsmProgress = _CucsFirmwareSystemFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45, 1, 8),
    _CucsFirmwareSystemFsmProgress_Type()
)
cucsFirmwareSystemFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmProgress.setStatus("current")
_CucsFirmwareSystemFsmRmtErrCode_Type = Gauge32
_CucsFirmwareSystemFsmRmtErrCode_Object = MibTableColumn
cucsFirmwareSystemFsmRmtErrCode = _CucsFirmwareSystemFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45, 1, 9),
    _CucsFirmwareSystemFsmRmtErrCode_Type()
)
cucsFirmwareSystemFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmRmtErrCode.setStatus("current")
_CucsFirmwareSystemFsmRmtErrDescr_Type = SnmpAdminString
_CucsFirmwareSystemFsmRmtErrDescr_Object = MibTableColumn
cucsFirmwareSystemFsmRmtErrDescr = _CucsFirmwareSystemFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45, 1, 10),
    _CucsFirmwareSystemFsmRmtErrDescr_Type()
)
cucsFirmwareSystemFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmRmtErrDescr.setStatus("current")
_CucsFirmwareSystemFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsFirmwareSystemFsmRmtRslt_Object = MibTableColumn
cucsFirmwareSystemFsmRmtRslt = _CucsFirmwareSystemFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 45, 1, 11),
    _CucsFirmwareSystemFsmRmtRslt_Type()
)
cucsFirmwareSystemFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmRmtRslt.setStatus("current")
_CucsFirmwareSystemFsmStageTable_Object = MibTable
cucsFirmwareSystemFsmStageTable = _CucsFirmwareSystemFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 46)
)
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStageTable.setStatus("current")
_CucsFirmwareSystemFsmStageEntry_Object = MibTableRow
cucsFirmwareSystemFsmStageEntry = _CucsFirmwareSystemFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 46, 1)
)
cucsFirmwareSystemFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareSystemFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStageEntry.setStatus("current")
_CucsFirmwareSystemFsmStageInstanceId_Type = CucsManagedObjectId
_CucsFirmwareSystemFsmStageInstanceId_Object = MibTableColumn
cucsFirmwareSystemFsmStageInstanceId = _CucsFirmwareSystemFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 46, 1, 1),
    _CucsFirmwareSystemFsmStageInstanceId_Type()
)
cucsFirmwareSystemFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStageInstanceId.setStatus("current")
_CucsFirmwareSystemFsmStageDn_Type = CucsManagedObjectDn
_CucsFirmwareSystemFsmStageDn_Object = MibTableColumn
cucsFirmwareSystemFsmStageDn = _CucsFirmwareSystemFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 46, 1, 2),
    _CucsFirmwareSystemFsmStageDn_Type()
)
cucsFirmwareSystemFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStageDn.setStatus("current")
_CucsFirmwareSystemFsmStageRn_Type = SnmpAdminString
_CucsFirmwareSystemFsmStageRn_Object = MibTableColumn
cucsFirmwareSystemFsmStageRn = _CucsFirmwareSystemFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 46, 1, 3),
    _CucsFirmwareSystemFsmStageRn_Type()
)
cucsFirmwareSystemFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStageRn.setStatus("current")
_CucsFirmwareSystemFsmStageDescrData_Type = SnmpAdminString
_CucsFirmwareSystemFsmStageDescrData_Object = MibTableColumn
cucsFirmwareSystemFsmStageDescrData = _CucsFirmwareSystemFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 46, 1, 4),
    _CucsFirmwareSystemFsmStageDescrData_Type()
)
cucsFirmwareSystemFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStageDescrData.setStatus("current")
_CucsFirmwareSystemFsmStageLastUpdateTime_Type = DateAndTime
_CucsFirmwareSystemFsmStageLastUpdateTime_Object = MibTableColumn
cucsFirmwareSystemFsmStageLastUpdateTime = _CucsFirmwareSystemFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 46, 1, 5),
    _CucsFirmwareSystemFsmStageLastUpdateTime_Type()
)
cucsFirmwareSystemFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStageLastUpdateTime.setStatus("current")
_CucsFirmwareSystemFsmStageName_Type = CucsFirmwareSystemFsmStageName
_CucsFirmwareSystemFsmStageName_Object = MibTableColumn
cucsFirmwareSystemFsmStageName = _CucsFirmwareSystemFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 46, 1, 6),
    _CucsFirmwareSystemFsmStageName_Type()
)
cucsFirmwareSystemFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStageName.setStatus("current")
_CucsFirmwareSystemFsmStageOrder_Type = Gauge32
_CucsFirmwareSystemFsmStageOrder_Object = MibTableColumn
cucsFirmwareSystemFsmStageOrder = _CucsFirmwareSystemFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 46, 1, 7),
    _CucsFirmwareSystemFsmStageOrder_Type()
)
cucsFirmwareSystemFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStageOrder.setStatus("current")
_CucsFirmwareSystemFsmStageRetry_Type = Gauge32
_CucsFirmwareSystemFsmStageRetry_Object = MibTableColumn
cucsFirmwareSystemFsmStageRetry = _CucsFirmwareSystemFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 46, 1, 8),
    _CucsFirmwareSystemFsmStageRetry_Type()
)
cucsFirmwareSystemFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStageRetry.setStatus("current")
_CucsFirmwareSystemFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsFirmwareSystemFsmStageStageStatus_Object = MibTableColumn
cucsFirmwareSystemFsmStageStageStatus = _CucsFirmwareSystemFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 46, 1, 9),
    _CucsFirmwareSystemFsmStageStageStatus_Type()
)
cucsFirmwareSystemFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmStageStageStatus.setStatus("current")
_CucsFirmwareSystemFsmTaskTable_Object = MibTable
cucsFirmwareSystemFsmTaskTable = _CucsFirmwareSystemFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 47)
)
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmTaskTable.setStatus("current")
_CucsFirmwareSystemFsmTaskEntry_Object = MibTableRow
cucsFirmwareSystemFsmTaskEntry = _CucsFirmwareSystemFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 47, 1)
)
cucsFirmwareSystemFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareSystemFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmTaskEntry.setStatus("current")
_CucsFirmwareSystemFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsFirmwareSystemFsmTaskInstanceId_Object = MibTableColumn
cucsFirmwareSystemFsmTaskInstanceId = _CucsFirmwareSystemFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 47, 1, 1),
    _CucsFirmwareSystemFsmTaskInstanceId_Type()
)
cucsFirmwareSystemFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmTaskInstanceId.setStatus("current")
_CucsFirmwareSystemFsmTaskDn_Type = CucsManagedObjectDn
_CucsFirmwareSystemFsmTaskDn_Object = MibTableColumn
cucsFirmwareSystemFsmTaskDn = _CucsFirmwareSystemFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 47, 1, 2),
    _CucsFirmwareSystemFsmTaskDn_Type()
)
cucsFirmwareSystemFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmTaskDn.setStatus("current")
_CucsFirmwareSystemFsmTaskRn_Type = SnmpAdminString
_CucsFirmwareSystemFsmTaskRn_Object = MibTableColumn
cucsFirmwareSystemFsmTaskRn = _CucsFirmwareSystemFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 47, 1, 3),
    _CucsFirmwareSystemFsmTaskRn_Type()
)
cucsFirmwareSystemFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmTaskRn.setStatus("current")
_CucsFirmwareSystemFsmTaskCompletion_Type = CucsFsmCompletion
_CucsFirmwareSystemFsmTaskCompletion_Object = MibTableColumn
cucsFirmwareSystemFsmTaskCompletion = _CucsFirmwareSystemFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 47, 1, 4),
    _CucsFirmwareSystemFsmTaskCompletion_Type()
)
cucsFirmwareSystemFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmTaskCompletion.setStatus("current")
_CucsFirmwareSystemFsmTaskFlags_Type = CucsFirmwareSystemFsmTaskFlags
_CucsFirmwareSystemFsmTaskFlags_Object = MibTableColumn
cucsFirmwareSystemFsmTaskFlags = _CucsFirmwareSystemFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 47, 1, 5),
    _CucsFirmwareSystemFsmTaskFlags_Type()
)
cucsFirmwareSystemFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmTaskFlags.setStatus("current")
_CucsFirmwareSystemFsmTaskItem_Type = CucsFirmwareSystemFsmTaskItem
_CucsFirmwareSystemFsmTaskItem_Object = MibTableColumn
cucsFirmwareSystemFsmTaskItem = _CucsFirmwareSystemFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 47, 1, 6),
    _CucsFirmwareSystemFsmTaskItem_Type()
)
cucsFirmwareSystemFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmTaskItem.setStatus("current")
_CucsFirmwareSystemFsmTaskSeqId_Type = Gauge32
_CucsFirmwareSystemFsmTaskSeqId_Object = MibTableColumn
cucsFirmwareSystemFsmTaskSeqId = _CucsFirmwareSystemFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 47, 1, 7),
    _CucsFirmwareSystemFsmTaskSeqId_Type()
)
cucsFirmwareSystemFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareSystemFsmTaskSeqId.setStatus("current")
_CucsFirmwareUpgradeDetailTable_Object = MibTable
cucsFirmwareUpgradeDetailTable = _CucsFirmwareUpgradeDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 48)
)
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeDetailTable.setStatus("current")
_CucsFirmwareUpgradeDetailEntry_Object = MibTableRow
cucsFirmwareUpgradeDetailEntry = _CucsFirmwareUpgradeDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 48, 1)
)
cucsFirmwareUpgradeDetailEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareUpgradeDetailInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeDetailEntry.setStatus("current")
_CucsFirmwareUpgradeDetailInstanceId_Type = CucsManagedObjectId
_CucsFirmwareUpgradeDetailInstanceId_Object = MibTableColumn
cucsFirmwareUpgradeDetailInstanceId = _CucsFirmwareUpgradeDetailInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 48, 1, 1),
    _CucsFirmwareUpgradeDetailInstanceId_Type()
)
cucsFirmwareUpgradeDetailInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeDetailInstanceId.setStatus("current")
_CucsFirmwareUpgradeDetailDn_Type = CucsManagedObjectDn
_CucsFirmwareUpgradeDetailDn_Object = MibTableColumn
cucsFirmwareUpgradeDetailDn = _CucsFirmwareUpgradeDetailDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 48, 1, 2),
    _CucsFirmwareUpgradeDetailDn_Type()
)
cucsFirmwareUpgradeDetailDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeDetailDn.setStatus("current")
_CucsFirmwareUpgradeDetailRn_Type = SnmpAdminString
_CucsFirmwareUpgradeDetailRn_Object = MibTableColumn
cucsFirmwareUpgradeDetailRn = _CucsFirmwareUpgradeDetailRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 48, 1, 3),
    _CucsFirmwareUpgradeDetailRn_Type()
)
cucsFirmwareUpgradeDetailRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeDetailRn.setStatus("current")
_CucsFirmwareUpgradeDetailCategory_Type = CucsFirmwareUpgradeCategory
_CucsFirmwareUpgradeDetailCategory_Object = MibTableColumn
cucsFirmwareUpgradeDetailCategory = _CucsFirmwareUpgradeDetailCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 48, 1, 4),
    _CucsFirmwareUpgradeDetailCategory_Type()
)
cucsFirmwareUpgradeDetailCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeDetailCategory.setStatus("current")
_CucsFirmwareUpgradeDetailDescription_Type = SnmpAdminString
_CucsFirmwareUpgradeDetailDescription_Object = MibTableColumn
cucsFirmwareUpgradeDetailDescription = _CucsFirmwareUpgradeDetailDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 48, 1, 5),
    _CucsFirmwareUpgradeDetailDescription_Type()
)
cucsFirmwareUpgradeDetailDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeDetailDescription.setStatus("current")
_CucsFirmwareUpgradeDetailId_Type = Gauge32
_CucsFirmwareUpgradeDetailId_Object = MibTableColumn
cucsFirmwareUpgradeDetailId = _CucsFirmwareUpgradeDetailId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 48, 1, 6),
    _CucsFirmwareUpgradeDetailId_Type()
)
cucsFirmwareUpgradeDetailId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeDetailId.setStatus("current")
_CucsFirmwareUpgradeDetailSeverity_Type = CucsFirmwareUpgradeSeverity
_CucsFirmwareUpgradeDetailSeverity_Object = MibTableColumn
cucsFirmwareUpgradeDetailSeverity = _CucsFirmwareUpgradeDetailSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 48, 1, 7),
    _CucsFirmwareUpgradeDetailSeverity_Type()
)
cucsFirmwareUpgradeDetailSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeDetailSeverity.setStatus("current")
_CucsFirmwareUpgradeInfoTable_Object = MibTable
cucsFirmwareUpgradeInfoTable = _CucsFirmwareUpgradeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 49)
)
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeInfoTable.setStatus("current")
_CucsFirmwareUpgradeInfoEntry_Object = MibTableRow
cucsFirmwareUpgradeInfoEntry = _CucsFirmwareUpgradeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 49, 1)
)
cucsFirmwareUpgradeInfoEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareUpgradeInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeInfoEntry.setStatus("current")
_CucsFirmwareUpgradeInfoInstanceId_Type = CucsManagedObjectId
_CucsFirmwareUpgradeInfoInstanceId_Object = MibTableColumn
cucsFirmwareUpgradeInfoInstanceId = _CucsFirmwareUpgradeInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 49, 1, 1),
    _CucsFirmwareUpgradeInfoInstanceId_Type()
)
cucsFirmwareUpgradeInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeInfoInstanceId.setStatus("current")
_CucsFirmwareUpgradeInfoDn_Type = CucsManagedObjectDn
_CucsFirmwareUpgradeInfoDn_Object = MibTableColumn
cucsFirmwareUpgradeInfoDn = _CucsFirmwareUpgradeInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 49, 1, 2),
    _CucsFirmwareUpgradeInfoDn_Type()
)
cucsFirmwareUpgradeInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeInfoDn.setStatus("current")
_CucsFirmwareUpgradeInfoRn_Type = SnmpAdminString
_CucsFirmwareUpgradeInfoRn_Object = MibTableColumn
cucsFirmwareUpgradeInfoRn = _CucsFirmwareUpgradeInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 49, 1, 3),
    _CucsFirmwareUpgradeInfoRn_Type()
)
cucsFirmwareUpgradeInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeInfoRn.setStatus("current")
_CucsFirmwareUpgradeInfoMessage_Type = SnmpAdminString
_CucsFirmwareUpgradeInfoMessage_Object = MibTableColumn
cucsFirmwareUpgradeInfoMessage = _CucsFirmwareUpgradeInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 49, 1, 4),
    _CucsFirmwareUpgradeInfoMessage_Type()
)
cucsFirmwareUpgradeInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeInfoMessage.setStatus("current")
_CucsFirmwareUpgradeInfoTimeStamp_Type = DateAndTime
_CucsFirmwareUpgradeInfoTimeStamp_Object = MibTableColumn
cucsFirmwareUpgradeInfoTimeStamp = _CucsFirmwareUpgradeInfoTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 49, 1, 5),
    _CucsFirmwareUpgradeInfoTimeStamp_Type()
)
cucsFirmwareUpgradeInfoTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeInfoTimeStamp.setStatus("current")
_CucsFirmwareUpgradeInfoValidateStatus_Type = CucsFirmwareUpgradeStatus
_CucsFirmwareUpgradeInfoValidateStatus_Object = MibTableColumn
cucsFirmwareUpgradeInfoValidateStatus = _CucsFirmwareUpgradeInfoValidateStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 49, 1, 6),
    _CucsFirmwareUpgradeInfoValidateStatus_Type()
)
cucsFirmwareUpgradeInfoValidateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeInfoValidateStatus.setStatus("current")
_CucsFirmwareUpgradeInfoVersion_Type = SnmpAdminString
_CucsFirmwareUpgradeInfoVersion_Object = MibTableColumn
cucsFirmwareUpgradeInfoVersion = _CucsFirmwareUpgradeInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 49, 1, 7),
    _CucsFirmwareUpgradeInfoVersion_Type()
)
cucsFirmwareUpgradeInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUpgradeInfoVersion.setStatus("current")
_CucsFirmwareAutoSyncPolicyTable_Object = MibTable
cucsFirmwareAutoSyncPolicyTable = _CucsFirmwareAutoSyncPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 50)
)
if mibBuilder.loadTexts:
    cucsFirmwareAutoSyncPolicyTable.setStatus("current")
_CucsFirmwareAutoSyncPolicyEntry_Object = MibTableRow
cucsFirmwareAutoSyncPolicyEntry = _CucsFirmwareAutoSyncPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 50, 1)
)
cucsFirmwareAutoSyncPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareAutoSyncPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareAutoSyncPolicyEntry.setStatus("current")
_CucsFirmwareAutoSyncPolicyInstanceId_Type = CucsManagedObjectId
_CucsFirmwareAutoSyncPolicyInstanceId_Object = MibTableColumn
cucsFirmwareAutoSyncPolicyInstanceId = _CucsFirmwareAutoSyncPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 50, 1, 1),
    _CucsFirmwareAutoSyncPolicyInstanceId_Type()
)
cucsFirmwareAutoSyncPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareAutoSyncPolicyInstanceId.setStatus("current")
_CucsFirmwareAutoSyncPolicyDn_Type = CucsManagedObjectDn
_CucsFirmwareAutoSyncPolicyDn_Object = MibTableColumn
cucsFirmwareAutoSyncPolicyDn = _CucsFirmwareAutoSyncPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 50, 1, 2),
    _CucsFirmwareAutoSyncPolicyDn_Type()
)
cucsFirmwareAutoSyncPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAutoSyncPolicyDn.setStatus("current")
_CucsFirmwareAutoSyncPolicyRn_Type = SnmpAdminString
_CucsFirmwareAutoSyncPolicyRn_Object = MibTableColumn
cucsFirmwareAutoSyncPolicyRn = _CucsFirmwareAutoSyncPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 50, 1, 3),
    _CucsFirmwareAutoSyncPolicyRn_Type()
)
cucsFirmwareAutoSyncPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAutoSyncPolicyRn.setStatus("current")
_CucsFirmwareAutoSyncPolicyConfigIssue_Type = CucsFirmwareAutoSyncConfigIssue
_CucsFirmwareAutoSyncPolicyConfigIssue_Object = MibTableColumn
cucsFirmwareAutoSyncPolicyConfigIssue = _CucsFirmwareAutoSyncPolicyConfigIssue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 50, 1, 4),
    _CucsFirmwareAutoSyncPolicyConfigIssue_Type()
)
cucsFirmwareAutoSyncPolicyConfigIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAutoSyncPolicyConfigIssue.setStatus("current")
_CucsFirmwareAutoSyncPolicyDescr_Type = SnmpAdminString
_CucsFirmwareAutoSyncPolicyDescr_Object = MibTableColumn
cucsFirmwareAutoSyncPolicyDescr = _CucsFirmwareAutoSyncPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 50, 1, 5),
    _CucsFirmwareAutoSyncPolicyDescr_Type()
)
cucsFirmwareAutoSyncPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAutoSyncPolicyDescr.setStatus("current")
_CucsFirmwareAutoSyncPolicyIntId_Type = SnmpAdminString
_CucsFirmwareAutoSyncPolicyIntId_Object = MibTableColumn
cucsFirmwareAutoSyncPolicyIntId = _CucsFirmwareAutoSyncPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 50, 1, 6),
    _CucsFirmwareAutoSyncPolicyIntId_Type()
)
cucsFirmwareAutoSyncPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAutoSyncPolicyIntId.setStatus("current")
_CucsFirmwareAutoSyncPolicyName_Type = SnmpAdminString
_CucsFirmwareAutoSyncPolicyName_Object = MibTableColumn
cucsFirmwareAutoSyncPolicyName = _CucsFirmwareAutoSyncPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 50, 1, 7),
    _CucsFirmwareAutoSyncPolicyName_Type()
)
cucsFirmwareAutoSyncPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAutoSyncPolicyName.setStatus("current")
_CucsFirmwareAutoSyncPolicyPolicyLevel_Type = Gauge32
_CucsFirmwareAutoSyncPolicyPolicyLevel_Object = MibTableColumn
cucsFirmwareAutoSyncPolicyPolicyLevel = _CucsFirmwareAutoSyncPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 50, 1, 8),
    _CucsFirmwareAutoSyncPolicyPolicyLevel_Type()
)
cucsFirmwareAutoSyncPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAutoSyncPolicyPolicyLevel.setStatus("current")
_CucsFirmwareAutoSyncPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFirmwareAutoSyncPolicyPolicyOwner_Object = MibTableColumn
cucsFirmwareAutoSyncPolicyPolicyOwner = _CucsFirmwareAutoSyncPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 50, 1, 9),
    _CucsFirmwareAutoSyncPolicyPolicyOwner_Type()
)
cucsFirmwareAutoSyncPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAutoSyncPolicyPolicyOwner.setStatus("current")
_CucsFirmwareAutoSyncPolicySyncState_Type = CucsFirmwareAutoSyncState
_CucsFirmwareAutoSyncPolicySyncState_Object = MibTableColumn
cucsFirmwareAutoSyncPolicySyncState = _CucsFirmwareAutoSyncPolicySyncState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 50, 1, 10),
    _CucsFirmwareAutoSyncPolicySyncState_Type()
)
cucsFirmwareAutoSyncPolicySyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareAutoSyncPolicySyncState.setStatus("current")
_CucsFirmwareImageLockTable_Object = MibTable
cucsFirmwareImageLockTable = _CucsFirmwareImageLockTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 51)
)
if mibBuilder.loadTexts:
    cucsFirmwareImageLockTable.setStatus("current")
_CucsFirmwareImageLockEntry_Object = MibTableRow
cucsFirmwareImageLockEntry = _CucsFirmwareImageLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 51, 1)
)
cucsFirmwareImageLockEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareImageLockInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareImageLockEntry.setStatus("current")
_CucsFirmwareImageLockInstanceId_Type = CucsManagedObjectId
_CucsFirmwareImageLockInstanceId_Object = MibTableColumn
cucsFirmwareImageLockInstanceId = _CucsFirmwareImageLockInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 51, 1, 1),
    _CucsFirmwareImageLockInstanceId_Type()
)
cucsFirmwareImageLockInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareImageLockInstanceId.setStatus("current")
_CucsFirmwareImageLockDn_Type = CucsManagedObjectDn
_CucsFirmwareImageLockDn_Object = MibTableColumn
cucsFirmwareImageLockDn = _CucsFirmwareImageLockDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 51, 1, 2),
    _CucsFirmwareImageLockDn_Type()
)
cucsFirmwareImageLockDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageLockDn.setStatus("current")
_CucsFirmwareImageLockRn_Type = SnmpAdminString
_CucsFirmwareImageLockRn_Object = MibTableColumn
cucsFirmwareImageLockRn = _CucsFirmwareImageLockRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 51, 1, 3),
    _CucsFirmwareImageLockRn_Type()
)
cucsFirmwareImageLockRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageLockRn.setStatus("current")
_CucsFirmwareImageLockImageNameDn_Type = SnmpAdminString
_CucsFirmwareImageLockImageNameDn_Object = MibTableColumn
cucsFirmwareImageLockImageNameDn = _CucsFirmwareImageLockImageNameDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 51, 1, 4),
    _CucsFirmwareImageLockImageNameDn_Type()
)
cucsFirmwareImageLockImageNameDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageLockImageNameDn.setStatus("current")
_CucsFirmwareImageLockName_Type = SnmpAdminString
_CucsFirmwareImageLockName_Object = MibTableColumn
cucsFirmwareImageLockName = _CucsFirmwareImageLockName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 51, 1, 5),
    _CucsFirmwareImageLockName_Type()
)
cucsFirmwareImageLockName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareImageLockName.setStatus("current")
_CucsFirmwareUcscInfoTable_Object = MibTable
cucsFirmwareUcscInfoTable = _CucsFirmwareUcscInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 52)
)
if mibBuilder.loadTexts:
    cucsFirmwareUcscInfoTable.setStatus("current")
_CucsFirmwareUcscInfoEntry_Object = MibTableRow
cucsFirmwareUcscInfoEntry = _CucsFirmwareUcscInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 52, 1)
)
cucsFirmwareUcscInfoEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareUcscInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareUcscInfoEntry.setStatus("current")
_CucsFirmwareUcscInfoInstanceId_Type = CucsManagedObjectId
_CucsFirmwareUcscInfoInstanceId_Object = MibTableColumn
cucsFirmwareUcscInfoInstanceId = _CucsFirmwareUcscInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 52, 1, 1),
    _CucsFirmwareUcscInfoInstanceId_Type()
)
cucsFirmwareUcscInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareUcscInfoInstanceId.setStatus("current")
_CucsFirmwareUcscInfoDn_Type = CucsManagedObjectDn
_CucsFirmwareUcscInfoDn_Object = MibTableColumn
cucsFirmwareUcscInfoDn = _CucsFirmwareUcscInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 52, 1, 2),
    _CucsFirmwareUcscInfoDn_Type()
)
cucsFirmwareUcscInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUcscInfoDn.setStatus("current")
_CucsFirmwareUcscInfoRn_Type = SnmpAdminString
_CucsFirmwareUcscInfoRn_Object = MibTableColumn
cucsFirmwareUcscInfoRn = _CucsFirmwareUcscInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 52, 1, 3),
    _CucsFirmwareUcscInfoRn_Type()
)
cucsFirmwareUcscInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUcscInfoRn.setStatus("current")
_CucsFirmwareUcscInfoConnProtocol_Type = CucsExtpolConnProtocol
_CucsFirmwareUcscInfoConnProtocol_Object = MibTableColumn
cucsFirmwareUcscInfoConnProtocol = _CucsFirmwareUcscInfoConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 52, 1, 4),
    _CucsFirmwareUcscInfoConnProtocol_Type()
)
cucsFirmwareUcscInfoConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUcscInfoConnProtocol.setStatus("current")
_CucsFirmwareUcscInfoHost_Type = SnmpAdminString
_CucsFirmwareUcscInfoHost_Object = MibTableColumn
cucsFirmwareUcscInfoHost = _CucsFirmwareUcscInfoHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 52, 1, 5),
    _CucsFirmwareUcscInfoHost_Type()
)
cucsFirmwareUcscInfoHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUcscInfoHost.setStatus("current")
_CucsFirmwareUcscInfoVersion_Type = SnmpAdminString
_CucsFirmwareUcscInfoVersion_Object = MibTableColumn
cucsFirmwareUcscInfoVersion = _CucsFirmwareUcscInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 52, 1, 6),
    _CucsFirmwareUcscInfoVersion_Type()
)
cucsFirmwareUcscInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareUcscInfoVersion.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderTable_Object = MibTable
cucsFirmwarePlatformBundleTypeCapProviderTable = _CucsFirmwarePlatformBundleTypeCapProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53)
)
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderTable.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderEntry_Object = MibTableRow
cucsFirmwarePlatformBundleTypeCapProviderEntry = _CucsFirmwarePlatformBundleTypeCapProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1)
)
cucsFirmwarePlatformBundleTypeCapProviderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwarePlatformBundleTypeCapProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderEntry.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderInstanceId_Type = CucsManagedObjectId
_CucsFirmwarePlatformBundleTypeCapProviderInstanceId_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderInstanceId = _CucsFirmwarePlatformBundleTypeCapProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 1),
    _CucsFirmwarePlatformBundleTypeCapProviderInstanceId_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderInstanceId.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderDn_Type = CucsManagedObjectDn
_CucsFirmwarePlatformBundleTypeCapProviderDn_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderDn = _CucsFirmwarePlatformBundleTypeCapProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 2),
    _CucsFirmwarePlatformBundleTypeCapProviderDn_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderDn.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderRn_Type = SnmpAdminString
_CucsFirmwarePlatformBundleTypeCapProviderRn_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderRn = _CucsFirmwarePlatformBundleTypeCapProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 3),
    _CucsFirmwarePlatformBundleTypeCapProviderRn_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderRn.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderDeleted_Type = TruthValue
_CucsFirmwarePlatformBundleTypeCapProviderDeleted_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderDeleted = _CucsFirmwarePlatformBundleTypeCapProviderDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 4),
    _CucsFirmwarePlatformBundleTypeCapProviderDeleted_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderDeleted.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderDeprecated_Type = TruthValue
_CucsFirmwarePlatformBundleTypeCapProviderDeprecated_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderDeprecated = _CucsFirmwarePlatformBundleTypeCapProviderDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 5),
    _CucsFirmwarePlatformBundleTypeCapProviderDeprecated_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderDeprecated.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderElementLoadFailures_Type = Gauge32
_CucsFirmwarePlatformBundleTypeCapProviderElementLoadFailures_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderElementLoadFailures = _CucsFirmwarePlatformBundleTypeCapProviderElementLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 6),
    _CucsFirmwarePlatformBundleTypeCapProviderElementLoadFailures_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderElementLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderElementLoadFailures.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderElementsLoaded_Type = Gauge32
_CucsFirmwarePlatformBundleTypeCapProviderElementsLoaded_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderElementsLoaded = _CucsFirmwarePlatformBundleTypeCapProviderElementsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 7),
    _CucsFirmwarePlatformBundleTypeCapProviderElementsLoaded_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderElementsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderElementsLoaded.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderGencount_Type = Gauge32
_CucsFirmwarePlatformBundleTypeCapProviderGencount_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderGencount = _CucsFirmwarePlatformBundleTypeCapProviderGencount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 8),
    _CucsFirmwarePlatformBundleTypeCapProviderGencount_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderGencount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderGencount.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderLoadErrors_Type = Gauge32
_CucsFirmwarePlatformBundleTypeCapProviderLoadErrors_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderLoadErrors = _CucsFirmwarePlatformBundleTypeCapProviderLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 9),
    _CucsFirmwarePlatformBundleTypeCapProviderLoadErrors_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderLoadErrors.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderLoadWarnings_Type = Gauge32
_CucsFirmwarePlatformBundleTypeCapProviderLoadWarnings_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderLoadWarnings = _CucsFirmwarePlatformBundleTypeCapProviderLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 10),
    _CucsFirmwarePlatformBundleTypeCapProviderLoadWarnings_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderLoadWarnings.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer_Type = SnmpAdminString
_CucsFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer = _CucsFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 11),
    _CucsFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderModel_Type = SnmpAdminString
_CucsFirmwarePlatformBundleTypeCapProviderModel_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderModel = _CucsFirmwarePlatformBundleTypeCapProviderModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 12),
    _CucsFirmwarePlatformBundleTypeCapProviderModel_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderModel.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderPlatformType_Type = CucsFirmwarePlatformType
_CucsFirmwarePlatformBundleTypeCapProviderPlatformType_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderPlatformType = _CucsFirmwarePlatformBundleTypeCapProviderPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 13),
    _CucsFirmwarePlatformBundleTypeCapProviderPlatformType_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderPlatformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderPlatformType.setStatus("current")
_CucsFirmwarePlatformBundleTypeCapProviderVendor_Type = SnmpAdminString
_CucsFirmwarePlatformBundleTypeCapProviderVendor_Object = MibTableColumn
cucsFirmwarePlatformBundleTypeCapProviderVendor = _CucsFirmwarePlatformBundleTypeCapProviderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 53, 1, 14),
    _CucsFirmwarePlatformBundleTypeCapProviderVendor_Type()
)
cucsFirmwarePlatformBundleTypeCapProviderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePlatformBundleTypeCapProviderVendor.setStatus("current")
_CucsFirmwareConstraintsTable_Object = MibTable
cucsFirmwareConstraintsTable = _CucsFirmwareConstraintsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 55)
)
if mibBuilder.loadTexts:
    cucsFirmwareConstraintsTable.setStatus("current")
_CucsFirmwareConstraintsEntry_Object = MibTableRow
cucsFirmwareConstraintsEntry = _CucsFirmwareConstraintsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 55, 1)
)
cucsFirmwareConstraintsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareConstraintsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareConstraintsEntry.setStatus("current")
_CucsFirmwareConstraintsInstanceId_Type = CucsManagedObjectId
_CucsFirmwareConstraintsInstanceId_Object = MibTableColumn
cucsFirmwareConstraintsInstanceId = _CucsFirmwareConstraintsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 55, 1, 1),
    _CucsFirmwareConstraintsInstanceId_Type()
)
cucsFirmwareConstraintsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareConstraintsInstanceId.setStatus("current")
_CucsFirmwareConstraintsDn_Type = CucsManagedObjectDn
_CucsFirmwareConstraintsDn_Object = MibTableColumn
cucsFirmwareConstraintsDn = _CucsFirmwareConstraintsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 55, 1, 2),
    _CucsFirmwareConstraintsDn_Type()
)
cucsFirmwareConstraintsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareConstraintsDn.setStatus("current")
_CucsFirmwareConstraintsRn_Type = SnmpAdminString
_CucsFirmwareConstraintsRn_Object = MibTableColumn
cucsFirmwareConstraintsRn = _CucsFirmwareConstraintsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 55, 1, 3),
    _CucsFirmwareConstraintsRn_Type()
)
cucsFirmwareConstraintsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareConstraintsRn.setStatus("current")
_CucsFirmwareFileUnitTable_Object = MibTable
cucsFirmwareFileUnitTable = _CucsFirmwareFileUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 57)
)
if mibBuilder.loadTexts:
    cucsFirmwareFileUnitTable.setStatus("current")
_CucsFirmwareFileUnitEntry_Object = MibTableRow
cucsFirmwareFileUnitEntry = _CucsFirmwareFileUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 57, 1)
)
cucsFirmwareFileUnitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareFileUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareFileUnitEntry.setStatus("current")
_CucsFirmwareFileUnitInstanceId_Type = CucsManagedObjectId
_CucsFirmwareFileUnitInstanceId_Object = MibTableColumn
cucsFirmwareFileUnitInstanceId = _CucsFirmwareFileUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 57, 1, 1),
    _CucsFirmwareFileUnitInstanceId_Type()
)
cucsFirmwareFileUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareFileUnitInstanceId.setStatus("current")
_CucsFirmwareFileUnitDn_Type = CucsManagedObjectDn
_CucsFirmwareFileUnitDn_Object = MibTableColumn
cucsFirmwareFileUnitDn = _CucsFirmwareFileUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 57, 1, 2),
    _CucsFirmwareFileUnitDn_Type()
)
cucsFirmwareFileUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareFileUnitDn.setStatus("current")
_CucsFirmwareFileUnitRn_Type = SnmpAdminString
_CucsFirmwareFileUnitRn_Object = MibTableColumn
cucsFirmwareFileUnitRn = _CucsFirmwareFileUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 57, 1, 3),
    _CucsFirmwareFileUnitRn_Type()
)
cucsFirmwareFileUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareFileUnitRn.setStatus("current")
_CucsFirmwareFileUnitPathName_Type = SnmpAdminString
_CucsFirmwareFileUnitPathName_Object = MibTableColumn
cucsFirmwareFileUnitPathName = _CucsFirmwareFileUnitPathName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 57, 1, 4),
    _CucsFirmwareFileUnitPathName_Type()
)
cucsFirmwareFileUnitPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareFileUnitPathName.setStatus("current")
_CucsFirmwareFileUnitType_Type = CucsFirmwareFileType
_CucsFirmwareFileUnitType_Object = MibTableColumn
cucsFirmwareFileUnitType = _CucsFirmwareFileUnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 57, 1, 5),
    _CucsFirmwareFileUnitType_Type()
)
cucsFirmwareFileUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareFileUnitType.setStatus("current")
_CucsFirmwareFileUnitVersion_Type = SnmpAdminString
_CucsFirmwareFileUnitVersion_Object = MibTableColumn
cucsFirmwareFileUnitVersion = _CucsFirmwareFileUnitVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 57, 1, 6),
    _CucsFirmwareFileUnitVersion_Type()
)
cucsFirmwareFileUnitVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareFileUnitVersion.setStatus("current")
_CucsFirmwareActivityTable_Object = MibTable
cucsFirmwareActivityTable = _CucsFirmwareActivityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 59)
)
if mibBuilder.loadTexts:
    cucsFirmwareActivityTable.setStatus("current")
_CucsFirmwareActivityEntry_Object = MibTableRow
cucsFirmwareActivityEntry = _CucsFirmwareActivityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 59, 1)
)
cucsFirmwareActivityEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareActivityInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareActivityEntry.setStatus("current")
_CucsFirmwareActivityInstanceId_Type = CucsManagedObjectId
_CucsFirmwareActivityInstanceId_Object = MibTableColumn
cucsFirmwareActivityInstanceId = _CucsFirmwareActivityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 59, 1, 1),
    _CucsFirmwareActivityInstanceId_Type()
)
cucsFirmwareActivityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareActivityInstanceId.setStatus("current")
_CucsFirmwareActivityDn_Type = CucsManagedObjectDn
_CucsFirmwareActivityDn_Object = MibTableColumn
cucsFirmwareActivityDn = _CucsFirmwareActivityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 59, 1, 2),
    _CucsFirmwareActivityDn_Type()
)
cucsFirmwareActivityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareActivityDn.setStatus("current")
_CucsFirmwareActivityRn_Type = SnmpAdminString
_CucsFirmwareActivityRn_Object = MibTableColumn
cucsFirmwareActivityRn = _CucsFirmwareActivityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 59, 1, 3),
    _CucsFirmwareActivityRn_Type()
)
cucsFirmwareActivityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareActivityRn.setStatus("current")
_CucsFirmwareActivityChassisCompInActivationDn_Type = SnmpAdminString
_CucsFirmwareActivityChassisCompInActivationDn_Object = MibTableColumn
cucsFirmwareActivityChassisCompInActivationDn = _CucsFirmwareActivityChassisCompInActivationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 59, 1, 4),
    _CucsFirmwareActivityChassisCompInActivationDn_Type()
)
cucsFirmwareActivityChassisCompInActivationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareActivityChassisCompInActivationDn.setStatus("current")
_CucsFirmwareActivityServerCompInActivationDn_Type = SnmpAdminString
_CucsFirmwareActivityServerCompInActivationDn_Object = MibTableColumn
cucsFirmwareActivityServerCompInActivationDn = _CucsFirmwareActivityServerCompInActivationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 59, 1, 5),
    _CucsFirmwareActivityServerCompInActivationDn_Type()
)
cucsFirmwareActivityServerCompInActivationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareActivityServerCompInActivationDn.setStatus("current")
_CucsFirmwareActivityServersPowerState_Type = CucsFirmwareActivityServersPowerState
_CucsFirmwareActivityServersPowerState_Object = MibTableColumn
cucsFirmwareActivityServersPowerState = _CucsFirmwareActivityServersPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 59, 1, 6),
    _CucsFirmwareActivityServersPowerState_Type()
)
cucsFirmwareActivityServersPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareActivityServersPowerState.setStatus("current")
_CucsFirmwareActivityUpgradePriorityInfo_Type = CucsFirmwareActivityUpgradePriorityInfo
_CucsFirmwareActivityUpgradePriorityInfo_Object = MibTableColumn
cucsFirmwareActivityUpgradePriorityInfo = _CucsFirmwareActivityUpgradePriorityInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 59, 1, 7),
    _CucsFirmwareActivityUpgradePriorityInfo_Type()
)
cucsFirmwareActivityUpgradePriorityInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareActivityUpgradePriorityInfo.setStatus("current")
_CucsFirmwareProcessorTypeConstraintTable_Object = MibTable
cucsFirmwareProcessorTypeConstraintTable = _CucsFirmwareProcessorTypeConstraintTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 60)
)
if mibBuilder.loadTexts:
    cucsFirmwareProcessorTypeConstraintTable.setStatus("current")
_CucsFirmwareProcessorTypeConstraintEntry_Object = MibTableRow
cucsFirmwareProcessorTypeConstraintEntry = _CucsFirmwareProcessorTypeConstraintEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 60, 1)
)
cucsFirmwareProcessorTypeConstraintEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareProcessorTypeConstraintInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareProcessorTypeConstraintEntry.setStatus("current")
_CucsFirmwareProcessorTypeConstraintInstanceId_Type = CucsManagedObjectId
_CucsFirmwareProcessorTypeConstraintInstanceId_Object = MibTableColumn
cucsFirmwareProcessorTypeConstraintInstanceId = _CucsFirmwareProcessorTypeConstraintInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 60, 1, 1),
    _CucsFirmwareProcessorTypeConstraintInstanceId_Type()
)
cucsFirmwareProcessorTypeConstraintInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareProcessorTypeConstraintInstanceId.setStatus("current")
_CucsFirmwareProcessorTypeConstraintDn_Type = CucsManagedObjectDn
_CucsFirmwareProcessorTypeConstraintDn_Object = MibTableColumn
cucsFirmwareProcessorTypeConstraintDn = _CucsFirmwareProcessorTypeConstraintDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 60, 1, 2),
    _CucsFirmwareProcessorTypeConstraintDn_Type()
)
cucsFirmwareProcessorTypeConstraintDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareProcessorTypeConstraintDn.setStatus("current")
_CucsFirmwareProcessorTypeConstraintRn_Type = SnmpAdminString
_CucsFirmwareProcessorTypeConstraintRn_Object = MibTableColumn
cucsFirmwareProcessorTypeConstraintRn = _CucsFirmwareProcessorTypeConstraintRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 60, 1, 3),
    _CucsFirmwareProcessorTypeConstraintRn_Type()
)
cucsFirmwareProcessorTypeConstraintRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareProcessorTypeConstraintRn.setStatus("current")
_CucsFirmwareProcessorTypeConstraintMinBiosVersion_Type = SnmpAdminString
_CucsFirmwareProcessorTypeConstraintMinBiosVersion_Object = MibTableColumn
cucsFirmwareProcessorTypeConstraintMinBiosVersion = _CucsFirmwareProcessorTypeConstraintMinBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 60, 1, 4),
    _CucsFirmwareProcessorTypeConstraintMinBiosVersion_Type()
)
cucsFirmwareProcessorTypeConstraintMinBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareProcessorTypeConstraintMinBiosVersion.setStatus("current")
_CucsFirmwareProcessorTypeConstraintMinCimcVersion_Type = SnmpAdminString
_CucsFirmwareProcessorTypeConstraintMinCimcVersion_Object = MibTableColumn
cucsFirmwareProcessorTypeConstraintMinCimcVersion = _CucsFirmwareProcessorTypeConstraintMinCimcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 60, 1, 5),
    _CucsFirmwareProcessorTypeConstraintMinCimcVersion_Type()
)
cucsFirmwareProcessorTypeConstraintMinCimcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareProcessorTypeConstraintMinCimcVersion.setStatus("current")
_CucsFirmwareProcessorTypeConstraintType_Type = SnmpAdminString
_CucsFirmwareProcessorTypeConstraintType_Object = MibTableColumn
cucsFirmwareProcessorTypeConstraintType = _CucsFirmwareProcessorTypeConstraintType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 60, 1, 6),
    _CucsFirmwareProcessorTypeConstraintType_Type()
)
cucsFirmwareProcessorTypeConstraintType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareProcessorTypeConstraintType.setStatus("current")
_CucsFirmwareVnicCdnConstraintTable_Object = MibTable
cucsFirmwareVnicCdnConstraintTable = _CucsFirmwareVnicCdnConstraintTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 61)
)
if mibBuilder.loadTexts:
    cucsFirmwareVnicCdnConstraintTable.setStatus("current")
_CucsFirmwareVnicCdnConstraintEntry_Object = MibTableRow
cucsFirmwareVnicCdnConstraintEntry = _CucsFirmwareVnicCdnConstraintEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 61, 1)
)
cucsFirmwareVnicCdnConstraintEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareVnicCdnConstraintInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareVnicCdnConstraintEntry.setStatus("current")
_CucsFirmwareVnicCdnConstraintInstanceId_Type = CucsManagedObjectId
_CucsFirmwareVnicCdnConstraintInstanceId_Object = MibTableColumn
cucsFirmwareVnicCdnConstraintInstanceId = _CucsFirmwareVnicCdnConstraintInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 61, 1, 1),
    _CucsFirmwareVnicCdnConstraintInstanceId_Type()
)
cucsFirmwareVnicCdnConstraintInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareVnicCdnConstraintInstanceId.setStatus("current")
_CucsFirmwareVnicCdnConstraintDn_Type = CucsManagedObjectDn
_CucsFirmwareVnicCdnConstraintDn_Object = MibTableColumn
cucsFirmwareVnicCdnConstraintDn = _CucsFirmwareVnicCdnConstraintDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 61, 1, 2),
    _CucsFirmwareVnicCdnConstraintDn_Type()
)
cucsFirmwareVnicCdnConstraintDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareVnicCdnConstraintDn.setStatus("current")
_CucsFirmwareVnicCdnConstraintRn_Type = SnmpAdminString
_CucsFirmwareVnicCdnConstraintRn_Object = MibTableColumn
cucsFirmwareVnicCdnConstraintRn = _CucsFirmwareVnicCdnConstraintRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 61, 1, 3),
    _CucsFirmwareVnicCdnConstraintRn_Type()
)
cucsFirmwareVnicCdnConstraintRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareVnicCdnConstraintRn.setStatus("current")
_CucsFirmwareVnicCdnConstraintMinBiosVersion_Type = SnmpAdminString
_CucsFirmwareVnicCdnConstraintMinBiosVersion_Object = MibTableColumn
cucsFirmwareVnicCdnConstraintMinBiosVersion = _CucsFirmwareVnicCdnConstraintMinBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 61, 1, 4),
    _CucsFirmwareVnicCdnConstraintMinBiosVersion_Type()
)
cucsFirmwareVnicCdnConstraintMinBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareVnicCdnConstraintMinBiosVersion.setStatus("current")
_CucsFirmwareVnicCdnConstraintMinCimcVersion_Type = SnmpAdminString
_CucsFirmwareVnicCdnConstraintMinCimcVersion_Object = MibTableColumn
cucsFirmwareVnicCdnConstraintMinCimcVersion = _CucsFirmwareVnicCdnConstraintMinCimcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 61, 1, 5),
    _CucsFirmwareVnicCdnConstraintMinCimcVersion_Type()
)
cucsFirmwareVnicCdnConstraintMinCimcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareVnicCdnConstraintMinCimcVersion.setStatus("current")
_CucsFirmwareVnicCdnConstraintType_Type = SnmpAdminString
_CucsFirmwareVnicCdnConstraintType_Object = MibTableColumn
cucsFirmwareVnicCdnConstraintType = _CucsFirmwareVnicCdnConstraintType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 61, 1, 6),
    _CucsFirmwareVnicCdnConstraintType_Type()
)
cucsFirmwareVnicCdnConstraintType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareVnicCdnConstraintType.setStatus("current")
_CucsFirmwareExcludeServerComponentTable_Object = MibTable
cucsFirmwareExcludeServerComponentTable = _CucsFirmwareExcludeServerComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 64)
)
if mibBuilder.loadTexts:
    cucsFirmwareExcludeServerComponentTable.setStatus("current")
_CucsFirmwareExcludeServerComponentEntry_Object = MibTableRow
cucsFirmwareExcludeServerComponentEntry = _CucsFirmwareExcludeServerComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 64, 1)
)
cucsFirmwareExcludeServerComponentEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareExcludeServerComponentInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareExcludeServerComponentEntry.setStatus("current")
_CucsFirmwareExcludeServerComponentInstanceId_Type = CucsManagedObjectId
_CucsFirmwareExcludeServerComponentInstanceId_Object = MibTableColumn
cucsFirmwareExcludeServerComponentInstanceId = _CucsFirmwareExcludeServerComponentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 64, 1, 1),
    _CucsFirmwareExcludeServerComponentInstanceId_Type()
)
cucsFirmwareExcludeServerComponentInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareExcludeServerComponentInstanceId.setStatus("current")
_CucsFirmwareExcludeServerComponentDn_Type = CucsManagedObjectDn
_CucsFirmwareExcludeServerComponentDn_Object = MibTableColumn
cucsFirmwareExcludeServerComponentDn = _CucsFirmwareExcludeServerComponentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 64, 1, 2),
    _CucsFirmwareExcludeServerComponentDn_Type()
)
cucsFirmwareExcludeServerComponentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareExcludeServerComponentDn.setStatus("current")
_CucsFirmwareExcludeServerComponentRn_Type = SnmpAdminString
_CucsFirmwareExcludeServerComponentRn_Object = MibTableColumn
cucsFirmwareExcludeServerComponentRn = _CucsFirmwareExcludeServerComponentRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 64, 1, 3),
    _CucsFirmwareExcludeServerComponentRn_Type()
)
cucsFirmwareExcludeServerComponentRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareExcludeServerComponentRn.setStatus("current")
_CucsFirmwareExcludeServerComponentServerComponent_Type = CucsFirmwareBladeType
_CucsFirmwareExcludeServerComponentServerComponent_Object = MibTableColumn
cucsFirmwareExcludeServerComponentServerComponent = _CucsFirmwareExcludeServerComponentServerComponent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 64, 1, 4),
    _CucsFirmwareExcludeServerComponentServerComponent_Type()
)
cucsFirmwareExcludeServerComponentServerComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareExcludeServerComponentServerComponent.setStatus("current")
_CucsFirmwareExcludeServerComponentPropAcl_Type = Unsigned64
_CucsFirmwareExcludeServerComponentPropAcl_Object = MibTableColumn
cucsFirmwareExcludeServerComponentPropAcl = _CucsFirmwareExcludeServerComponentPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 64, 1, 5),
    _CucsFirmwareExcludeServerComponentPropAcl_Type()
)
cucsFirmwareExcludeServerComponentPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareExcludeServerComponentPropAcl.setStatus("current")
_CucsFirmwarePCHStorageConfigConstraintTable_Object = MibTable
cucsFirmwarePCHStorageConfigConstraintTable = _CucsFirmwarePCHStorageConfigConstraintTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 71)
)
if mibBuilder.loadTexts:
    cucsFirmwarePCHStorageConfigConstraintTable.setStatus("current")
_CucsFirmwarePCHStorageConfigConstraintEntry_Object = MibTableRow
cucsFirmwarePCHStorageConfigConstraintEntry = _CucsFirmwarePCHStorageConfigConstraintEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 71, 1)
)
cucsFirmwarePCHStorageConfigConstraintEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwarePCHStorageConfigConstraintInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwarePCHStorageConfigConstraintEntry.setStatus("current")
_CucsFirmwarePCHStorageConfigConstraintInstanceId_Type = CucsManagedObjectId
_CucsFirmwarePCHStorageConfigConstraintInstanceId_Object = MibTableColumn
cucsFirmwarePCHStorageConfigConstraintInstanceId = _CucsFirmwarePCHStorageConfigConstraintInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 71, 1, 1),
    _CucsFirmwarePCHStorageConfigConstraintInstanceId_Type()
)
cucsFirmwarePCHStorageConfigConstraintInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwarePCHStorageConfigConstraintInstanceId.setStatus("current")
_CucsFirmwarePCHStorageConfigConstraintDn_Type = CucsManagedObjectDn
_CucsFirmwarePCHStorageConfigConstraintDn_Object = MibTableColumn
cucsFirmwarePCHStorageConfigConstraintDn = _CucsFirmwarePCHStorageConfigConstraintDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 71, 1, 2),
    _CucsFirmwarePCHStorageConfigConstraintDn_Type()
)
cucsFirmwarePCHStorageConfigConstraintDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePCHStorageConfigConstraintDn.setStatus("current")
_CucsFirmwarePCHStorageConfigConstraintRn_Type = SnmpAdminString
_CucsFirmwarePCHStorageConfigConstraintRn_Object = MibTableColumn
cucsFirmwarePCHStorageConfigConstraintRn = _CucsFirmwarePCHStorageConfigConstraintRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 71, 1, 3),
    _CucsFirmwarePCHStorageConfigConstraintRn_Type()
)
cucsFirmwarePCHStorageConfigConstraintRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePCHStorageConfigConstraintRn.setStatus("current")
_CucsFirmwarePCHStorageConfigConstraintMinBiosVersion_Type = SnmpAdminString
_CucsFirmwarePCHStorageConfigConstraintMinBiosVersion_Object = MibTableColumn
cucsFirmwarePCHStorageConfigConstraintMinBiosVersion = _CucsFirmwarePCHStorageConfigConstraintMinBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 71, 1, 4),
    _CucsFirmwarePCHStorageConfigConstraintMinBiosVersion_Type()
)
cucsFirmwarePCHStorageConfigConstraintMinBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePCHStorageConfigConstraintMinBiosVersion.setStatus("current")
_CucsFirmwarePCHStorageConfigConstraintMinCimcVersion_Type = SnmpAdminString
_CucsFirmwarePCHStorageConfigConstraintMinCimcVersion_Object = MibTableColumn
cucsFirmwarePCHStorageConfigConstraintMinCimcVersion = _CucsFirmwarePCHStorageConfigConstraintMinCimcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 71, 1, 5),
    _CucsFirmwarePCHStorageConfigConstraintMinCimcVersion_Type()
)
cucsFirmwarePCHStorageConfigConstraintMinCimcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwarePCHStorageConfigConstraintMinCimcVersion.setStatus("current")
_CucsFirmwareServerTypeConstraintTable_Object = MibTable
cucsFirmwareServerTypeConstraintTable = _CucsFirmwareServerTypeConstraintTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 72)
)
if mibBuilder.loadTexts:
    cucsFirmwareServerTypeConstraintTable.setStatus("current")
_CucsFirmwareServerTypeConstraintEntry_Object = MibTableRow
cucsFirmwareServerTypeConstraintEntry = _CucsFirmwareServerTypeConstraintEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 72, 1)
)
cucsFirmwareServerTypeConstraintEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareServerTypeConstraintInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareServerTypeConstraintEntry.setStatus("current")
_CucsFirmwareServerTypeConstraintInstanceId_Type = CucsManagedObjectId
_CucsFirmwareServerTypeConstraintInstanceId_Object = MibTableColumn
cucsFirmwareServerTypeConstraintInstanceId = _CucsFirmwareServerTypeConstraintInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 72, 1, 1),
    _CucsFirmwareServerTypeConstraintInstanceId_Type()
)
cucsFirmwareServerTypeConstraintInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareServerTypeConstraintInstanceId.setStatus("current")
_CucsFirmwareServerTypeConstraintDn_Type = CucsManagedObjectDn
_CucsFirmwareServerTypeConstraintDn_Object = MibTableColumn
cucsFirmwareServerTypeConstraintDn = _CucsFirmwareServerTypeConstraintDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 72, 1, 2),
    _CucsFirmwareServerTypeConstraintDn_Type()
)
cucsFirmwareServerTypeConstraintDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareServerTypeConstraintDn.setStatus("current")
_CucsFirmwareServerTypeConstraintRn_Type = SnmpAdminString
_CucsFirmwareServerTypeConstraintRn_Object = MibTableColumn
cucsFirmwareServerTypeConstraintRn = _CucsFirmwareServerTypeConstraintRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 72, 1, 3),
    _CucsFirmwareServerTypeConstraintRn_Type()
)
cucsFirmwareServerTypeConstraintRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareServerTypeConstraintRn.setStatus("current")
_CucsFirmwareServerTypeConstraintMinBiosVersion_Type = SnmpAdminString
_CucsFirmwareServerTypeConstraintMinBiosVersion_Object = MibTableColumn
cucsFirmwareServerTypeConstraintMinBiosVersion = _CucsFirmwareServerTypeConstraintMinBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 72, 1, 4),
    _CucsFirmwareServerTypeConstraintMinBiosVersion_Type()
)
cucsFirmwareServerTypeConstraintMinBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareServerTypeConstraintMinBiosVersion.setStatus("current")
_CucsFirmwareServerTypeConstraintMinCimcVersion_Type = SnmpAdminString
_CucsFirmwareServerTypeConstraintMinCimcVersion_Object = MibTableColumn
cucsFirmwareServerTypeConstraintMinCimcVersion = _CucsFirmwareServerTypeConstraintMinCimcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 72, 1, 5),
    _CucsFirmwareServerTypeConstraintMinCimcVersion_Type()
)
cucsFirmwareServerTypeConstraintMinCimcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareServerTypeConstraintMinCimcVersion.setStatus("current")
_CucsFirmwareVicSlotConstraintTable_Object = MibTable
cucsFirmwareVicSlotConstraintTable = _CucsFirmwareVicSlotConstraintTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 73)
)
if mibBuilder.loadTexts:
    cucsFirmwareVicSlotConstraintTable.setStatus("current")
_CucsFirmwareVicSlotConstraintEntry_Object = MibTableRow
cucsFirmwareVicSlotConstraintEntry = _CucsFirmwareVicSlotConstraintEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 73, 1)
)
cucsFirmwareVicSlotConstraintEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB", "cucsFirmwareVicSlotConstraintInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFirmwareVicSlotConstraintEntry.setStatus("current")
_CucsFirmwareVicSlotConstraintInstanceId_Type = CucsManagedObjectId
_CucsFirmwareVicSlotConstraintInstanceId_Object = MibTableColumn
cucsFirmwareVicSlotConstraintInstanceId = _CucsFirmwareVicSlotConstraintInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 73, 1, 1),
    _CucsFirmwareVicSlotConstraintInstanceId_Type()
)
cucsFirmwareVicSlotConstraintInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFirmwareVicSlotConstraintInstanceId.setStatus("current")
_CucsFirmwareVicSlotConstraintDn_Type = CucsManagedObjectDn
_CucsFirmwareVicSlotConstraintDn_Object = MibTableColumn
cucsFirmwareVicSlotConstraintDn = _CucsFirmwareVicSlotConstraintDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 73, 1, 2),
    _CucsFirmwareVicSlotConstraintDn_Type()
)
cucsFirmwareVicSlotConstraintDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareVicSlotConstraintDn.setStatus("current")
_CucsFirmwareVicSlotConstraintRn_Type = SnmpAdminString
_CucsFirmwareVicSlotConstraintRn_Object = MibTableColumn
cucsFirmwareVicSlotConstraintRn = _CucsFirmwareVicSlotConstraintRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 73, 1, 3),
    _CucsFirmwareVicSlotConstraintRn_Type()
)
cucsFirmwareVicSlotConstraintRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareVicSlotConstraintRn.setStatus("current")
_CucsFirmwareVicSlotConstraintMinBiosVersion_Type = SnmpAdminString
_CucsFirmwareVicSlotConstraintMinBiosVersion_Object = MibTableColumn
cucsFirmwareVicSlotConstraintMinBiosVersion = _CucsFirmwareVicSlotConstraintMinBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 73, 1, 4),
    _CucsFirmwareVicSlotConstraintMinBiosVersion_Type()
)
cucsFirmwareVicSlotConstraintMinBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareVicSlotConstraintMinBiosVersion.setStatus("current")
_CucsFirmwareVicSlotConstraintMinCimcVersion_Type = SnmpAdminString
_CucsFirmwareVicSlotConstraintMinCimcVersion_Object = MibTableColumn
cucsFirmwareVicSlotConstraintMinCimcVersion = _CucsFirmwareVicSlotConstraintMinCimcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 73, 1, 5),
    _CucsFirmwareVicSlotConstraintMinCimcVersion_Type()
)
cucsFirmwareVicSlotConstraintMinCimcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareVicSlotConstraintMinCimcVersion.setStatus("current")
_CucsFirmwareVicSlotConstraintVicSlot_Type = SnmpAdminString
_CucsFirmwareVicSlotConstraintVicSlot_Object = MibTableColumn
cucsFirmwareVicSlotConstraintVicSlot = _CucsFirmwareVicSlotConstraintVicSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 22, 73, 1, 6),
    _CucsFirmwareVicSlotConstraintVicSlot_Type()
)
cucsFirmwareVicSlotConstraintVicSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFirmwareVicSlotConstraintVicSlot.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-FIRMWARE-MIB",
    **{"cucsFirmwareObjects": cucsFirmwareObjects,
       "cucsFirmwareBootDefinitionTable": cucsFirmwareBootDefinitionTable,
       "cucsFirmwareBootDefinitionEntry": cucsFirmwareBootDefinitionEntry,
       "cucsFirmwareBootDefinitionInstanceId": cucsFirmwareBootDefinitionInstanceId,
       "cucsFirmwareBootDefinitionDn": cucsFirmwareBootDefinitionDn,
       "cucsFirmwareBootDefinitionRn": cucsFirmwareBootDefinitionRn,
       "cucsFirmwareBootDefinitionType": cucsFirmwareBootDefinitionType,
       "cucsFirmwareBootUnitTable": cucsFirmwareBootUnitTable,
       "cucsFirmwareBootUnitEntry": cucsFirmwareBootUnitEntry,
       "cucsFirmwareBootUnitInstanceId": cucsFirmwareBootUnitInstanceId,
       "cucsFirmwareBootUnitDn": cucsFirmwareBootUnitDn,
       "cucsFirmwareBootUnitRn": cucsFirmwareBootUnitRn,
       "cucsFirmwareBootUnitAdminState": cucsFirmwareBootUnitAdminState,
       "cucsFirmwareBootUnitIgnoreCompCheck": cucsFirmwareBootUnitIgnoreCompCheck,
       "cucsFirmwareBootUnitImage": cucsFirmwareBootUnitImage,
       "cucsFirmwareBootUnitOperState": cucsFirmwareBootUnitOperState,
       "cucsFirmwareBootUnitPrevVersion": cucsFirmwareBootUnitPrevVersion,
       "cucsFirmwareBootUnitResetOnActivate": cucsFirmwareBootUnitResetOnActivate,
       "cucsFirmwareBootUnitType": cucsFirmwareBootUnitType,
       "cucsFirmwareBootUnitVersion": cucsFirmwareBootUnitVersion,
       "cucsFirmwareBootUnitSkipValidation": cucsFirmwareBootUnitSkipValidation,
       "cucsFirmwareBootUnitInvTag": cucsFirmwareBootUnitInvTag,
       "cucsFirmwareBootUnitMode": cucsFirmwareBootUnitMode,
       "cucsFirmwareCatalogueTable": cucsFirmwareCatalogueTable,
       "cucsFirmwareCatalogueEntry": cucsFirmwareCatalogueEntry,
       "cucsFirmwareCatalogueInstanceId": cucsFirmwareCatalogueInstanceId,
       "cucsFirmwareCatalogueDn": cucsFirmwareCatalogueDn,
       "cucsFirmwareCatalogueRn": cucsFirmwareCatalogueRn,
       "cucsFirmwareCatalogueSyncTrigger": cucsFirmwareCatalogueSyncTrigger,
       "cucsFirmwareCompSourceTable": cucsFirmwareCompSourceTable,
       "cucsFirmwareCompSourceEntry": cucsFirmwareCompSourceEntry,
       "cucsFirmwareCompSourceInstanceId": cucsFirmwareCompSourceInstanceId,
       "cucsFirmwareCompSourceDn": cucsFirmwareCompSourceDn,
       "cucsFirmwareCompSourceRn": cucsFirmwareCompSourceRn,
       "cucsFirmwareCompSourceInvTag": cucsFirmwareCompSourceInvTag,
       "cucsFirmwareCompSourceVersion": cucsFirmwareCompSourceVersion,
       "cucsFirmwareCompSourceDescr": cucsFirmwareCompSourceDescr,
       "cucsFirmwareCompSourceIntId": cucsFirmwareCompSourceIntId,
       "cucsFirmwareCompSourceName": cucsFirmwareCompSourceName,
       "cucsFirmwareCompSourcePolicyLevel": cucsFirmwareCompSourcePolicyLevel,
       "cucsFirmwareCompSourcePolicyOwner": cucsFirmwareCompSourcePolicyOwner,
       "cucsFirmwareCompTargetTable": cucsFirmwareCompTargetTable,
       "cucsFirmwareCompTargetEntry": cucsFirmwareCompTargetEntry,
       "cucsFirmwareCompTargetInstanceId": cucsFirmwareCompTargetInstanceId,
       "cucsFirmwareCompTargetDn": cucsFirmwareCompTargetDn,
       "cucsFirmwareCompTargetRn": cucsFirmwareCompTargetRn,
       "cucsFirmwareCompTargetInvTag": cucsFirmwareCompTargetInvTag,
       "cucsFirmwareCompTargetVersion": cucsFirmwareCompTargetVersion,
       "cucsFirmwareCompTargetDescr": cucsFirmwareCompTargetDescr,
       "cucsFirmwareCompTargetIntId": cucsFirmwareCompTargetIntId,
       "cucsFirmwareCompTargetName": cucsFirmwareCompTargetName,
       "cucsFirmwareCompTargetPolicyLevel": cucsFirmwareCompTargetPolicyLevel,
       "cucsFirmwareCompTargetPolicyOwner": cucsFirmwareCompTargetPolicyOwner,
       "cucsFirmwareComputeHostPackTable": cucsFirmwareComputeHostPackTable,
       "cucsFirmwareComputeHostPackEntry": cucsFirmwareComputeHostPackEntry,
       "cucsFirmwareComputeHostPackInstanceId": cucsFirmwareComputeHostPackInstanceId,
       "cucsFirmwareComputeHostPackDn": cucsFirmwareComputeHostPackDn,
       "cucsFirmwareComputeHostPackRn": cucsFirmwareComputeHostPackRn,
       "cucsFirmwareComputeHostPackDescr": cucsFirmwareComputeHostPackDescr,
       "cucsFirmwareComputeHostPackIntId": cucsFirmwareComputeHostPackIntId,
       "cucsFirmwareComputeHostPackMode": cucsFirmwareComputeHostPackMode,
       "cucsFirmwareComputeHostPackName": cucsFirmwareComputeHostPackName,
       "cucsFirmwareComputeHostPackStageSize": cucsFirmwareComputeHostPackStageSize,
       "cucsFirmwareComputeHostPackUpdateTrigger": cucsFirmwareComputeHostPackUpdateTrigger,
       "cucsFirmwareComputeHostPackIgnoreCompCheck": cucsFirmwareComputeHostPackIgnoreCompCheck,
       "cucsFirmwareComputeHostPackConfigQualifier": cucsFirmwareComputeHostPackConfigQualifier,
       "cucsFirmwareComputeHostPackBladeBundleName": cucsFirmwareComputeHostPackBladeBundleName,
       "cucsFirmwareComputeHostPackBladeBundleVersion": cucsFirmwareComputeHostPackBladeBundleVersion,
       "cucsFirmwareComputeHostPackPolicyLevel": cucsFirmwareComputeHostPackPolicyLevel,
       "cucsFirmwareComputeHostPackPolicyOwner": cucsFirmwareComputeHostPackPolicyOwner,
       "cucsFirmwareComputeHostPackRackBundleName": cucsFirmwareComputeHostPackRackBundleName,
       "cucsFirmwareComputeHostPackRackBundleVersion": cucsFirmwareComputeHostPackRackBundleVersion,
       "cucsFirmwareComputeHostPackMSeriesBundleName": cucsFirmwareComputeHostPackMSeriesBundleName,
       "cucsFirmwareComputeHostPackMSeriesBundleVersion": cucsFirmwareComputeHostPackMSeriesBundleVersion,
       "cucsFirmwareComputeMgmtPackTable": cucsFirmwareComputeMgmtPackTable,
       "cucsFirmwareComputeMgmtPackEntry": cucsFirmwareComputeMgmtPackEntry,
       "cucsFirmwareComputeMgmtPackInstanceId": cucsFirmwareComputeMgmtPackInstanceId,
       "cucsFirmwareComputeMgmtPackDn": cucsFirmwareComputeMgmtPackDn,
       "cucsFirmwareComputeMgmtPackRn": cucsFirmwareComputeMgmtPackRn,
       "cucsFirmwareComputeMgmtPackDescr": cucsFirmwareComputeMgmtPackDescr,
       "cucsFirmwareComputeMgmtPackIntId": cucsFirmwareComputeMgmtPackIntId,
       "cucsFirmwareComputeMgmtPackMode": cucsFirmwareComputeMgmtPackMode,
       "cucsFirmwareComputeMgmtPackName": cucsFirmwareComputeMgmtPackName,
       "cucsFirmwareComputeMgmtPackStageSize": cucsFirmwareComputeMgmtPackStageSize,
       "cucsFirmwareComputeMgmtPackUpdateTrigger": cucsFirmwareComputeMgmtPackUpdateTrigger,
       "cucsFirmwareComputeMgmtPackIgnoreCompCheck": cucsFirmwareComputeMgmtPackIgnoreCompCheck,
       "cucsFirmwareComputeMgmtPackPolicyLevel": cucsFirmwareComputeMgmtPackPolicyLevel,
       "cucsFirmwareComputeMgmtPackPolicyOwner": cucsFirmwareComputeMgmtPackPolicyOwner,
       "cucsFirmwareDependencyTable": cucsFirmwareDependencyTable,
       "cucsFirmwareDependencyEntry": cucsFirmwareDependencyEntry,
       "cucsFirmwareDependencyInstanceId": cucsFirmwareDependencyInstanceId,
       "cucsFirmwareDependencyDn": cucsFirmwareDependencyDn,
       "cucsFirmwareDependencyRn": cucsFirmwareDependencyRn,
       "cucsFirmwareDependencyEp": cucsFirmwareDependencyEp,
       "cucsFirmwareDependencyHwModel": cucsFirmwareDependencyHwModel,
       "cucsFirmwareDependencyHwRevision": cucsFirmwareDependencyHwRevision,
       "cucsFirmwareDependencyHwVendor": cucsFirmwareDependencyHwVendor,
       "cucsFirmwareDependencyInvTag": cucsFirmwareDependencyInvTag,
       "cucsFirmwareDependencyMaxVer": cucsFirmwareDependencyMaxVer,
       "cucsFirmwareDependencyMinVer": cucsFirmwareDependencyMinVer,
       "cucsFirmwareDependencyRelationship": cucsFirmwareDependencyRelationship,
       "cucsFirmwareDependencyScope": cucsFirmwareDependencyScope,
       "cucsFirmwareDependencySensitivity": cucsFirmwareDependencySensitivity,
       "cucsFirmwareDistImageTable": cucsFirmwareDistImageTable,
       "cucsFirmwareDistImageEntry": cucsFirmwareDistImageEntry,
       "cucsFirmwareDistImageInstanceId": cucsFirmwareDistImageInstanceId,
       "cucsFirmwareDistImageDn": cucsFirmwareDistImageDn,
       "cucsFirmwareDistImageRn": cucsFirmwareDistImageRn,
       "cucsFirmwareDistImageImageDeleted": cucsFirmwareDistImageImageDeleted,
       "cucsFirmwareDistImageName": cucsFirmwareDistImageName,
       "cucsFirmwareDistImageType": cucsFirmwareDistImageType,
       "cucsFirmwareDistributableTable": cucsFirmwareDistributableTable,
       "cucsFirmwareDistributableEntry": cucsFirmwareDistributableEntry,
       "cucsFirmwareDistributableInstanceId": cucsFirmwareDistributableInstanceId,
       "cucsFirmwareDistributableDn": cucsFirmwareDistributableDn,
       "cucsFirmwareDistributableRn": cucsFirmwareDistributableRn,
       "cucsFirmwareDistributableAdminState": cucsFirmwareDistributableAdminState,
       "cucsFirmwareDistributableCompleteness": cucsFirmwareDistributableCompleteness,
       "cucsFirmwareDistributableFsmDescr": cucsFirmwareDistributableFsmDescr,
       "cucsFirmwareDistributableFsmPrev": cucsFirmwareDistributableFsmPrev,
       "cucsFirmwareDistributableFsmProgr": cucsFirmwareDistributableFsmProgr,
       "cucsFirmwareDistributableFsmRmtInvErrCode": cucsFirmwareDistributableFsmRmtInvErrCode,
       "cucsFirmwareDistributableFsmRmtInvErrDescr": cucsFirmwareDistributableFsmRmtInvErrDescr,
       "cucsFirmwareDistributableFsmRmtInvRslt": cucsFirmwareDistributableFsmRmtInvRslt,
       "cucsFirmwareDistributableFsmStageDescr": cucsFirmwareDistributableFsmStageDescr,
       "cucsFirmwareDistributableFsmStamp": cucsFirmwareDistributableFsmStamp,
       "cucsFirmwareDistributableFsmStatus": cucsFirmwareDistributableFsmStatus,
       "cucsFirmwareDistributableFsmTry": cucsFirmwareDistributableFsmTry,
       "cucsFirmwareDistributableImagePresence": cucsFirmwareDistributableImagePresence,
       "cucsFirmwareDistributableModel": cucsFirmwareDistributableModel,
       "cucsFirmwareDistributableName": cucsFirmwareDistributableName,
       "cucsFirmwareDistributableTransferState": cucsFirmwareDistributableTransferState,
       "cucsFirmwareDistributableType": cucsFirmwareDistributableType,
       "cucsFirmwareDistributableVendor": cucsFirmwareDistributableVendor,
       "cucsFirmwareDistributableVersion": cucsFirmwareDistributableVersion,
       "cucsFirmwareDistributableInvTag": cucsFirmwareDistributableInvTag,
       "cucsFirmwareDistributableDescr": cucsFirmwareDistributableDescr,
       "cucsFirmwareDistributableIntId": cucsFirmwareDistributableIntId,
       "cucsFirmwareDistributablePolicyLevel": cucsFirmwareDistributablePolicyLevel,
       "cucsFirmwareDistributablePolicyOwner": cucsFirmwareDistributablePolicyOwner,
       "cucsFirmwareDistributableFsmTaskTable": cucsFirmwareDistributableFsmTaskTable,
       "cucsFirmwareDistributableFsmTaskEntry": cucsFirmwareDistributableFsmTaskEntry,
       "cucsFirmwareDistributableFsmTaskInstanceId": cucsFirmwareDistributableFsmTaskInstanceId,
       "cucsFirmwareDistributableFsmTaskDn": cucsFirmwareDistributableFsmTaskDn,
       "cucsFirmwareDistributableFsmTaskRn": cucsFirmwareDistributableFsmTaskRn,
       "cucsFirmwareDistributableFsmTaskCompletion": cucsFirmwareDistributableFsmTaskCompletion,
       "cucsFirmwareDistributableFsmTaskFlags": cucsFirmwareDistributableFsmTaskFlags,
       "cucsFirmwareDistributableFsmTaskItem": cucsFirmwareDistributableFsmTaskItem,
       "cucsFirmwareDistributableFsmTaskSeqId": cucsFirmwareDistributableFsmTaskSeqId,
       "cucsFirmwareDownloaderTable": cucsFirmwareDownloaderTable,
       "cucsFirmwareDownloaderEntry": cucsFirmwareDownloaderEntry,
       "cucsFirmwareDownloaderInstanceId": cucsFirmwareDownloaderInstanceId,
       "cucsFirmwareDownloaderDn": cucsFirmwareDownloaderDn,
       "cucsFirmwareDownloaderRn": cucsFirmwareDownloaderRn,
       "cucsFirmwareDownloaderAdminState": cucsFirmwareDownloaderAdminState,
       "cucsFirmwareDownloaderFileName": cucsFirmwareDownloaderFileName,
       "cucsFirmwareDownloaderFsmDescr": cucsFirmwareDownloaderFsmDescr,
       "cucsFirmwareDownloaderFsmPrev": cucsFirmwareDownloaderFsmPrev,
       "cucsFirmwareDownloaderFsmProgr": cucsFirmwareDownloaderFsmProgr,
       "cucsFirmwareDownloaderFsmRmtInvErrCode": cucsFirmwareDownloaderFsmRmtInvErrCode,
       "cucsFirmwareDownloaderFsmRmtInvErrDescr": cucsFirmwareDownloaderFsmRmtInvErrDescr,
       "cucsFirmwareDownloaderFsmRmtInvRslt": cucsFirmwareDownloaderFsmRmtInvRslt,
       "cucsFirmwareDownloaderFsmStageDescr": cucsFirmwareDownloaderFsmStageDescr,
       "cucsFirmwareDownloaderFsmStamp": cucsFirmwareDownloaderFsmStamp,
       "cucsFirmwareDownloaderFsmStatus": cucsFirmwareDownloaderFsmStatus,
       "cucsFirmwareDownloaderFsmTry": cucsFirmwareDownloaderFsmTry,
       "cucsFirmwareDownloaderImageSize": cucsFirmwareDownloaderImageSize,
       "cucsFirmwareDownloaderProtocol": cucsFirmwareDownloaderProtocol,
       "cucsFirmwareDownloaderPwd": cucsFirmwareDownloaderPwd,
       "cucsFirmwareDownloaderRemotePath": cucsFirmwareDownloaderRemotePath,
       "cucsFirmwareDownloaderServer": cucsFirmwareDownloaderServer,
       "cucsFirmwareDownloaderTransferState": cucsFirmwareDownloaderTransferState,
       "cucsFirmwareDownloaderUser": cucsFirmwareDownloaderUser,
       "cucsFirmwareDownloaderFsmTaskTable": cucsFirmwareDownloaderFsmTaskTable,
       "cucsFirmwareDownloaderFsmTaskEntry": cucsFirmwareDownloaderFsmTaskEntry,
       "cucsFirmwareDownloaderFsmTaskInstanceId": cucsFirmwareDownloaderFsmTaskInstanceId,
       "cucsFirmwareDownloaderFsmTaskDn": cucsFirmwareDownloaderFsmTaskDn,
       "cucsFirmwareDownloaderFsmTaskRn": cucsFirmwareDownloaderFsmTaskRn,
       "cucsFirmwareDownloaderFsmTaskCompletion": cucsFirmwareDownloaderFsmTaskCompletion,
       "cucsFirmwareDownloaderFsmTaskFlags": cucsFirmwareDownloaderFsmTaskFlags,
       "cucsFirmwareDownloaderFsmTaskItem": cucsFirmwareDownloaderFsmTaskItem,
       "cucsFirmwareDownloaderFsmTaskSeqId": cucsFirmwareDownloaderFsmTaskSeqId,
       "cucsFirmwareImageTable": cucsFirmwareImageTable,
       "cucsFirmwareImageEntry": cucsFirmwareImageEntry,
       "cucsFirmwareImageInstanceId": cucsFirmwareImageInstanceId,
       "cucsFirmwareImageDn": cucsFirmwareImageDn,
       "cucsFirmwareImageRn": cucsFirmwareImageRn,
       "cucsFirmwareImageAdminState": cucsFirmwareImageAdminState,
       "cucsFirmwareImageChecksum": cucsFirmwareImageChecksum,
       "cucsFirmwareImageDownloadDate": cucsFirmwareImageDownloadDate,
       "cucsFirmwareImageFsmDescr": cucsFirmwareImageFsmDescr,
       "cucsFirmwareImageFsmPrev": cucsFirmwareImageFsmPrev,
       "cucsFirmwareImageFsmProgr": cucsFirmwareImageFsmProgr,
       "cucsFirmwareImageFsmRmtInvErrCode": cucsFirmwareImageFsmRmtInvErrCode,
       "cucsFirmwareImageFsmRmtInvErrDescr": cucsFirmwareImageFsmRmtInvErrDescr,
       "cucsFirmwareImageFsmRmtInvRslt": cucsFirmwareImageFsmRmtInvRslt,
       "cucsFirmwareImageFsmStageDescr": cucsFirmwareImageFsmStageDescr,
       "cucsFirmwareImageFsmStamp": cucsFirmwareImageFsmStamp,
       "cucsFirmwareImageFsmStatus": cucsFirmwareImageFsmStatus,
       "cucsFirmwareImageFsmTry": cucsFirmwareImageFsmTry,
       "cucsFirmwareImageImagePresence": cucsFirmwareImageImagePresence,
       "cucsFirmwareImageInvTag": cucsFirmwareImageInvTag,
       "cucsFirmwareImageIsoname": cucsFirmwareImageIsoname,
       "cucsFirmwareImageLocation": cucsFirmwareImageLocation,
       "cucsFirmwareImageName": cucsFirmwareImageName,
       "cucsFirmwareImageSize": cucsFirmwareImageSize,
       "cucsFirmwareImageType": cucsFirmwareImageType,
       "cucsFirmwareImageVersion": cucsFirmwareImageVersion,
       "cucsFirmwareImageDescr": cucsFirmwareImageDescr,
       "cucsFirmwareImageIntId": cucsFirmwareImageIntId,
       "cucsFirmwareImagePolicyLevel": cucsFirmwareImagePolicyLevel,
       "cucsFirmwareImagePolicyOwner": cucsFirmwareImagePolicyOwner,
       "cucsFirmwareImageFsmTaskTable": cucsFirmwareImageFsmTaskTable,
       "cucsFirmwareImageFsmTaskEntry": cucsFirmwareImageFsmTaskEntry,
       "cucsFirmwareImageFsmTaskInstanceId": cucsFirmwareImageFsmTaskInstanceId,
       "cucsFirmwareImageFsmTaskDn": cucsFirmwareImageFsmTaskDn,
       "cucsFirmwareImageFsmTaskRn": cucsFirmwareImageFsmTaskRn,
       "cucsFirmwareImageFsmTaskCompletion": cucsFirmwareImageFsmTaskCompletion,
       "cucsFirmwareImageFsmTaskFlags": cucsFirmwareImageFsmTaskFlags,
       "cucsFirmwareImageFsmTaskItem": cucsFirmwareImageFsmTaskItem,
       "cucsFirmwareImageFsmTaskSeqId": cucsFirmwareImageFsmTaskSeqId,
       "cucsFirmwareInstallableTable": cucsFirmwareInstallableTable,
       "cucsFirmwareInstallableEntry": cucsFirmwareInstallableEntry,
       "cucsFirmwareInstallableInstanceId": cucsFirmwareInstallableInstanceId,
       "cucsFirmwareInstallableDn": cucsFirmwareInstallableDn,
       "cucsFirmwareInstallableRn": cucsFirmwareInstallableRn,
       "cucsFirmwareInstallableChecksum": cucsFirmwareInstallableChecksum,
       "cucsFirmwareInstallableInProgress": cucsFirmwareInstallableInProgress,
       "cucsFirmwareInstallableIsoname": cucsFirmwareInstallableIsoname,
       "cucsFirmwareInstallableLocation": cucsFirmwareInstallableLocation,
       "cucsFirmwareInstallableModel": cucsFirmwareInstallableModel,
       "cucsFirmwareInstallableName": cucsFirmwareInstallableName,
       "cucsFirmwareInstallableSize": cucsFirmwareInstallableSize,
       "cucsFirmwareInstallableType": cucsFirmwareInstallableType,
       "cucsFirmwareInstallableVendor": cucsFirmwareInstallableVendor,
       "cucsFirmwareInstallableVersion": cucsFirmwareInstallableVersion,
       "cucsFirmwarePackItemTable": cucsFirmwarePackItemTable,
       "cucsFirmwarePackItemEntry": cucsFirmwarePackItemEntry,
       "cucsFirmwarePackItemInstanceId": cucsFirmwarePackItemInstanceId,
       "cucsFirmwarePackItemDn": cucsFirmwarePackItemDn,
       "cucsFirmwarePackItemRn": cucsFirmwarePackItemRn,
       "cucsFirmwarePackItemHwModel": cucsFirmwarePackItemHwModel,
       "cucsFirmwarePackItemHwVendor": cucsFirmwarePackItemHwVendor,
       "cucsFirmwarePackItemPresence": cucsFirmwarePackItemPresence,
       "cucsFirmwarePackItemType": cucsFirmwarePackItemType,
       "cucsFirmwarePackItemVersion": cucsFirmwarePackItemVersion,
       "cucsFirmwareRunningTable": cucsFirmwareRunningTable,
       "cucsFirmwareRunningEntry": cucsFirmwareRunningEntry,
       "cucsFirmwareRunningInstanceId": cucsFirmwareRunningInstanceId,
       "cucsFirmwareRunningDn": cucsFirmwareRunningDn,
       "cucsFirmwareRunningRn": cucsFirmwareRunningRn,
       "cucsFirmwareRunningDeployment": cucsFirmwareRunningDeployment,
       "cucsFirmwareRunningType": cucsFirmwareRunningType,
       "cucsFirmwareRunningVersion": cucsFirmwareRunningVersion,
       "cucsFirmwareRunningPackageVersion": cucsFirmwareRunningPackageVersion,
       "cucsFirmwareRunningInvTag": cucsFirmwareRunningInvTag,
       "cucsFirmwareTypeTable": cucsFirmwareTypeTable,
       "cucsFirmwareTypeEntry": cucsFirmwareTypeEntry,
       "cucsFirmwareTypeInstanceId": cucsFirmwareTypeInstanceId,
       "cucsFirmwareTypeDn": cucsFirmwareTypeDn,
       "cucsFirmwareTypeRn": cucsFirmwareTypeRn,
       "cucsFirmwareTypeEp": cucsFirmwareTypeEp,
       "cucsFirmwareTypeInvTag": cucsFirmwareTypeInvTag,
       "cucsFirmwareTypeMaxVer": cucsFirmwareTypeMaxVer,
       "cucsFirmwareTypeMinVer": cucsFirmwareTypeMinVer,
       "cucsFirmwareTypeFwFpgaRevisionSupported": cucsFirmwareTypeFwFpgaRevisionSupported,
       "cucsFirmwareUpdatableTable": cucsFirmwareUpdatableTable,
       "cucsFirmwareUpdatableEntry": cucsFirmwareUpdatableEntry,
       "cucsFirmwareUpdatableInstanceId": cucsFirmwareUpdatableInstanceId,
       "cucsFirmwareUpdatableDn": cucsFirmwareUpdatableDn,
       "cucsFirmwareUpdatableRn": cucsFirmwareUpdatableRn,
       "cucsFirmwareUpdatableAdminState": cucsFirmwareUpdatableAdminState,
       "cucsFirmwareUpdatableDeployment": cucsFirmwareUpdatableDeployment,
       "cucsFirmwareUpdatableOperState": cucsFirmwareUpdatableOperState,
       "cucsFirmwareUpdatableOperStateQual": cucsFirmwareUpdatableOperStateQual,
       "cucsFirmwareUpdatablePrevVersion": cucsFirmwareUpdatablePrevVersion,
       "cucsFirmwareUpdatableVersion": cucsFirmwareUpdatableVersion,
       "cucsFirmwareBundleTypeTable": cucsFirmwareBundleTypeTable,
       "cucsFirmwareBundleTypeEntry": cucsFirmwareBundleTypeEntry,
       "cucsFirmwareBundleTypeInstanceId": cucsFirmwareBundleTypeInstanceId,
       "cucsFirmwareBundleTypeDn": cucsFirmwareBundleTypeDn,
       "cucsFirmwareBundleTypeRn": cucsFirmwareBundleTypeRn,
       "cucsFirmwareBundleTypeInvTag": cucsFirmwareBundleTypeInvTag,
       "cucsFirmwareBundleTypeType": cucsFirmwareBundleTypeType,
       "cucsFirmwareBundleTypeCapProviderTable": cucsFirmwareBundleTypeCapProviderTable,
       "cucsFirmwareBundleTypeCapProviderEntry": cucsFirmwareBundleTypeCapProviderEntry,
       "cucsFirmwareBundleTypeCapProviderInstanceId": cucsFirmwareBundleTypeCapProviderInstanceId,
       "cucsFirmwareBundleTypeCapProviderDn": cucsFirmwareBundleTypeCapProviderDn,
       "cucsFirmwareBundleTypeCapProviderRn": cucsFirmwareBundleTypeCapProviderRn,
       "cucsFirmwareBundleTypeCapProviderDeleted": cucsFirmwareBundleTypeCapProviderDeleted,
       "cucsFirmwareBundleTypeCapProviderDeprecated": cucsFirmwareBundleTypeCapProviderDeprecated,
       "cucsFirmwareBundleTypeCapProviderGencount": cucsFirmwareBundleTypeCapProviderGencount,
       "cucsFirmwareBundleTypeCapProviderMgmtPlaneVer": cucsFirmwareBundleTypeCapProviderMgmtPlaneVer,
       "cucsFirmwareBundleTypeCapProviderModel": cucsFirmwareBundleTypeCapProviderModel,
       "cucsFirmwareBundleTypeCapProviderVendor": cucsFirmwareBundleTypeCapProviderVendor,
       "cucsFirmwareBundleTypeCapProviderElementLoadFailures": cucsFirmwareBundleTypeCapProviderElementLoadFailures,
       "cucsFirmwareBundleTypeCapProviderElementsLoaded": cucsFirmwareBundleTypeCapProviderElementsLoaded,
       "cucsFirmwareBundleTypeCapProviderLoadErrors": cucsFirmwareBundleTypeCapProviderLoadErrors,
       "cucsFirmwareBundleTypeCapProviderLoadWarnings": cucsFirmwareBundleTypeCapProviderLoadWarnings,
       "cucsFirmwareBundleTypeCapProviderPlatformType": cucsFirmwareBundleTypeCapProviderPlatformType,
       "cucsFirmwareSpecTable": cucsFirmwareSpecTable,
       "cucsFirmwareSpecEntry": cucsFirmwareSpecEntry,
       "cucsFirmwareSpecInstanceId": cucsFirmwareSpecInstanceId,
       "cucsFirmwareSpecDn": cucsFirmwareSpecDn,
       "cucsFirmwareSpecRn": cucsFirmwareSpecRn,
       "cucsFirmwareSpecBundleVersion": cucsFirmwareSpecBundleVersion,
       "cucsFirmwareSpecEthEFIVersion": cucsFirmwareSpecEthEFIVersion,
       "cucsFirmwareSpecEthOptionRomVersion": cucsFirmwareSpecEthOptionRomVersion,
       "cucsFirmwareSpecFcFWVersion": cucsFirmwareSpecFcFWVersion,
       "cucsFirmwareSpecFcOptionRomVersion": cucsFirmwareSpecFcOptionRomVersion,
       "cucsFirmwareUpgradeConstraintTable": cucsFirmwareUpgradeConstraintTable,
       "cucsFirmwareUpgradeConstraintEntry": cucsFirmwareUpgradeConstraintEntry,
       "cucsFirmwareUpgradeConstraintInstanceId": cucsFirmwareUpgradeConstraintInstanceId,
       "cucsFirmwareUpgradeConstraintDn": cucsFirmwareUpgradeConstraintDn,
       "cucsFirmwareUpgradeConstraintRn": cucsFirmwareUpgradeConstraintRn,
       "cucsFirmwareUpgradeConstraintMinVer": cucsFirmwareUpgradeConstraintMinVer,
       "cucsFirmwareAckTable": cucsFirmwareAckTable,
       "cucsFirmwareAckEntry": cucsFirmwareAckEntry,
       "cucsFirmwareAckInstanceId": cucsFirmwareAckInstanceId,
       "cucsFirmwareAckDn": cucsFirmwareAckDn,
       "cucsFirmwareAckRn": cucsFirmwareAckRn,
       "cucsFirmwareAckAcked": cucsFirmwareAckAcked,
       "cucsFirmwareAckAckedBy": cucsFirmwareAckAckedBy,
       "cucsFirmwareAckAdminState": cucsFirmwareAckAdminState,
       "cucsFirmwareAckAutoDelete": cucsFirmwareAckAutoDelete,
       "cucsFirmwareAckChangeBy": cucsFirmwareAckChangeBy,
       "cucsFirmwareAckChangeDetails": cucsFirmwareAckChangeDetails,
       "cucsFirmwareAckChanges": cucsFirmwareAckChanges,
       "cucsFirmwareAckDescr": cucsFirmwareAckDescr,
       "cucsFirmwareAckDisr": cucsFirmwareAckDisr,
       "cucsFirmwareAckIgnoreCap": cucsFirmwareAckIgnoreCap,
       "cucsFirmwareAckIntId": cucsFirmwareAckIntId,
       "cucsFirmwareAckModified": cucsFirmwareAckModified,
       "cucsFirmwareAckName": cucsFirmwareAckName,
       "cucsFirmwareAckOperScheduler": cucsFirmwareAckOperScheduler,
       "cucsFirmwareAckOperState": cucsFirmwareAckOperState,
       "cucsFirmwareAckPolicyLevel": cucsFirmwareAckPolicyLevel,
       "cucsFirmwareAckPolicyOwner": cucsFirmwareAckPolicyOwner,
       "cucsFirmwareAckPrevOperState": cucsFirmwareAckPrevOperState,
       "cucsFirmwareAckScheduler": cucsFirmwareAckScheduler,
       "cucsFirmwareAckTriggerConfigState": cucsFirmwareAckTriggerConfigState,
       "cucsFirmwareBladeTable": cucsFirmwareBladeTable,
       "cucsFirmwareBladeEntry": cucsFirmwareBladeEntry,
       "cucsFirmwareBladeInstanceId": cucsFirmwareBladeInstanceId,
       "cucsFirmwareBladeDn": cucsFirmwareBladeDn,
       "cucsFirmwareBladeRn": cucsFirmwareBladeRn,
       "cucsFirmwareBladeOperVersion": cucsFirmwareBladeOperVersion,
       "cucsFirmwareBundleInfoTable": cucsFirmwareBundleInfoTable,
       "cucsFirmwareBundleInfoEntry": cucsFirmwareBundleInfoEntry,
       "cucsFirmwareBundleInfoInstanceId": cucsFirmwareBundleInfoInstanceId,
       "cucsFirmwareBundleInfoDn": cucsFirmwareBundleInfoDn,
       "cucsFirmwareBundleInfoRn": cucsFirmwareBundleInfoRn,
       "cucsFirmwareBundleInfoType": cucsFirmwareBundleInfoType,
       "cucsFirmwareBundleInfoVersion": cucsFirmwareBundleInfoVersion,
       "cucsFirmwareBundleInfoDigestTable": cucsFirmwareBundleInfoDigestTable,
       "cucsFirmwareBundleInfoDigestEntry": cucsFirmwareBundleInfoDigestEntry,
       "cucsFirmwareBundleInfoDigestInstanceId": cucsFirmwareBundleInfoDigestInstanceId,
       "cucsFirmwareBundleInfoDigestDn": cucsFirmwareBundleInfoDigestDn,
       "cucsFirmwareBundleInfoDigestRn": cucsFirmwareBundleInfoDigestRn,
       "cucsFirmwareBundleInfoDigestBundleName": cucsFirmwareBundleInfoDigestBundleName,
       "cucsFirmwareBundleInfoDigestType": cucsFirmwareBundleInfoDigestType,
       "cucsFirmwareBundleInfoDigestVersion": cucsFirmwareBundleInfoDigestVersion,
       "cucsFirmwareCatalogPackTable": cucsFirmwareCatalogPackTable,
       "cucsFirmwareCatalogPackEntry": cucsFirmwareCatalogPackEntry,
       "cucsFirmwareCatalogPackInstanceId": cucsFirmwareCatalogPackInstanceId,
       "cucsFirmwareCatalogPackDn": cucsFirmwareCatalogPackDn,
       "cucsFirmwareCatalogPackRn": cucsFirmwareCatalogPackRn,
       "cucsFirmwareCatalogPackCatalogName": cucsFirmwareCatalogPackCatalogName,
       "cucsFirmwareCatalogPackCatalogVersion": cucsFirmwareCatalogPackCatalogVersion,
       "cucsFirmwareCatalogPackConfigState": cucsFirmwareCatalogPackConfigState,
       "cucsFirmwareCatalogPackConfigStatusMessage": cucsFirmwareCatalogPackConfigStatusMessage,
       "cucsFirmwareCatalogPackDescr": cucsFirmwareCatalogPackDescr,
       "cucsFirmwareCatalogPackIntId": cucsFirmwareCatalogPackIntId,
       "cucsFirmwareCatalogPackMode": cucsFirmwareCatalogPackMode,
       "cucsFirmwareCatalogPackName": cucsFirmwareCatalogPackName,
       "cucsFirmwareCatalogPackPolicyLevel": cucsFirmwareCatalogPackPolicyLevel,
       "cucsFirmwareCatalogPackPolicyOwner": cucsFirmwareCatalogPackPolicyOwner,
       "cucsFirmwareCatalogPackStageSize": cucsFirmwareCatalogPackStageSize,
       "cucsFirmwareCatalogPackUpdateTrigger": cucsFirmwareCatalogPackUpdateTrigger,
       "cucsFirmwareDistributableFsmTable": cucsFirmwareDistributableFsmTable,
       "cucsFirmwareDistributableFsmEntry": cucsFirmwareDistributableFsmEntry,
       "cucsFirmwareDistributableFsmInstanceId": cucsFirmwareDistributableFsmInstanceId,
       "cucsFirmwareDistributableFsmDn": cucsFirmwareDistributableFsmDn,
       "cucsFirmwareDistributableFsmRn": cucsFirmwareDistributableFsmRn,
       "cucsFirmwareDistributableFsmCompletionTime": cucsFirmwareDistributableFsmCompletionTime,
       "cucsFirmwareDistributableFsmCurrentFsm": cucsFirmwareDistributableFsmCurrentFsm,
       "cucsFirmwareDistributableFsmDescrData": cucsFirmwareDistributableFsmDescrData,
       "cucsFirmwareDistributableFsmFsmStatus": cucsFirmwareDistributableFsmFsmStatus,
       "cucsFirmwareDistributableFsmProgress": cucsFirmwareDistributableFsmProgress,
       "cucsFirmwareDistributableFsmRmtErrCode": cucsFirmwareDistributableFsmRmtErrCode,
       "cucsFirmwareDistributableFsmRmtErrDescr": cucsFirmwareDistributableFsmRmtErrDescr,
       "cucsFirmwareDistributableFsmRmtRslt": cucsFirmwareDistributableFsmRmtRslt,
       "cucsFirmwareDistributableFsmStageTable": cucsFirmwareDistributableFsmStageTable,
       "cucsFirmwareDistributableFsmStageEntry": cucsFirmwareDistributableFsmStageEntry,
       "cucsFirmwareDistributableFsmStageInstanceId": cucsFirmwareDistributableFsmStageInstanceId,
       "cucsFirmwareDistributableFsmStageDn": cucsFirmwareDistributableFsmStageDn,
       "cucsFirmwareDistributableFsmStageRn": cucsFirmwareDistributableFsmStageRn,
       "cucsFirmwareDistributableFsmStageDescrData": cucsFirmwareDistributableFsmStageDescrData,
       "cucsFirmwareDistributableFsmStageLastUpdateTime": cucsFirmwareDistributableFsmStageLastUpdateTime,
       "cucsFirmwareDistributableFsmStageName": cucsFirmwareDistributableFsmStageName,
       "cucsFirmwareDistributableFsmStageOrder": cucsFirmwareDistributableFsmStageOrder,
       "cucsFirmwareDistributableFsmStageRetry": cucsFirmwareDistributableFsmStageRetry,
       "cucsFirmwareDistributableFsmStageStageStatus": cucsFirmwareDistributableFsmStageStageStatus,
       "cucsFirmwareDownloaderFsmTable": cucsFirmwareDownloaderFsmTable,
       "cucsFirmwareDownloaderFsmEntry": cucsFirmwareDownloaderFsmEntry,
       "cucsFirmwareDownloaderFsmInstanceId": cucsFirmwareDownloaderFsmInstanceId,
       "cucsFirmwareDownloaderFsmDn": cucsFirmwareDownloaderFsmDn,
       "cucsFirmwareDownloaderFsmRn": cucsFirmwareDownloaderFsmRn,
       "cucsFirmwareDownloaderFsmCompletionTime": cucsFirmwareDownloaderFsmCompletionTime,
       "cucsFirmwareDownloaderFsmCurrentFsm": cucsFirmwareDownloaderFsmCurrentFsm,
       "cucsFirmwareDownloaderFsmDescrData": cucsFirmwareDownloaderFsmDescrData,
       "cucsFirmwareDownloaderFsmFsmStatus": cucsFirmwareDownloaderFsmFsmStatus,
       "cucsFirmwareDownloaderFsmProgress": cucsFirmwareDownloaderFsmProgress,
       "cucsFirmwareDownloaderFsmRmtErrCode": cucsFirmwareDownloaderFsmRmtErrCode,
       "cucsFirmwareDownloaderFsmRmtErrDescr": cucsFirmwareDownloaderFsmRmtErrDescr,
       "cucsFirmwareDownloaderFsmRmtRslt": cucsFirmwareDownloaderFsmRmtRslt,
       "cucsFirmwareDownloaderFsmStageTable": cucsFirmwareDownloaderFsmStageTable,
       "cucsFirmwareDownloaderFsmStageEntry": cucsFirmwareDownloaderFsmStageEntry,
       "cucsFirmwareDownloaderFsmStageInstanceId": cucsFirmwareDownloaderFsmStageInstanceId,
       "cucsFirmwareDownloaderFsmStageDn": cucsFirmwareDownloaderFsmStageDn,
       "cucsFirmwareDownloaderFsmStageRn": cucsFirmwareDownloaderFsmStageRn,
       "cucsFirmwareDownloaderFsmStageDescrData": cucsFirmwareDownloaderFsmStageDescrData,
       "cucsFirmwareDownloaderFsmStageLastUpdateTime": cucsFirmwareDownloaderFsmStageLastUpdateTime,
       "cucsFirmwareDownloaderFsmStageName": cucsFirmwareDownloaderFsmStageName,
       "cucsFirmwareDownloaderFsmStageOrder": cucsFirmwareDownloaderFsmStageOrder,
       "cucsFirmwareDownloaderFsmStageRetry": cucsFirmwareDownloaderFsmStageRetry,
       "cucsFirmwareDownloaderFsmStageStageStatus": cucsFirmwareDownloaderFsmStageStageStatus,
       "cucsFirmwareHostTable": cucsFirmwareHostTable,
       "cucsFirmwareHostEntry": cucsFirmwareHostEntry,
       "cucsFirmwareHostInstanceId": cucsFirmwareHostInstanceId,
       "cucsFirmwareHostDn": cucsFirmwareHostDn,
       "cucsFirmwareHostRn": cucsFirmwareHostRn,
       "cucsFirmwareHostPackModImpactTable": cucsFirmwareHostPackModImpactTable,
       "cucsFirmwareHostPackModImpactEntry": cucsFirmwareHostPackModImpactEntry,
       "cucsFirmwareHostPackModImpactInstanceId": cucsFirmwareHostPackModImpactInstanceId,
       "cucsFirmwareHostPackModImpactDn": cucsFirmwareHostPackModImpactDn,
       "cucsFirmwareHostPackModImpactRn": cucsFirmwareHostPackModImpactRn,
       "cucsFirmwareHostPackModImpactKeyDn": cucsFirmwareHostPackModImpactKeyDn,
       "cucsFirmwareHostPackModImpactMaintPolicyDn": cucsFirmwareHostPackModImpactMaintPolicyDn,
       "cucsFirmwareHostPackModImpactPnDn": cucsFirmwareHostPackModImpactPnDn,
       "cucsFirmwareHostPackModImpactRebootPolicy": cucsFirmwareHostPackModImpactRebootPolicy,
       "cucsFirmwareHostPackModImpactServiceProfileDn": cucsFirmwareHostPackModImpactServiceProfileDn,
       "cucsFirmwareImageFsmTable": cucsFirmwareImageFsmTable,
       "cucsFirmwareImageFsmEntry": cucsFirmwareImageFsmEntry,
       "cucsFirmwareImageFsmInstanceId": cucsFirmwareImageFsmInstanceId,
       "cucsFirmwareImageFsmDn": cucsFirmwareImageFsmDn,
       "cucsFirmwareImageFsmRn": cucsFirmwareImageFsmRn,
       "cucsFirmwareImageFsmCompletionTime": cucsFirmwareImageFsmCompletionTime,
       "cucsFirmwareImageFsmCurrentFsm": cucsFirmwareImageFsmCurrentFsm,
       "cucsFirmwareImageFsmDescrData": cucsFirmwareImageFsmDescrData,
       "cucsFirmwareImageFsmFsmStatus": cucsFirmwareImageFsmFsmStatus,
       "cucsFirmwareImageFsmProgress": cucsFirmwareImageFsmProgress,
       "cucsFirmwareImageFsmRmtErrCode": cucsFirmwareImageFsmRmtErrCode,
       "cucsFirmwareImageFsmRmtErrDescr": cucsFirmwareImageFsmRmtErrDescr,
       "cucsFirmwareImageFsmRmtRslt": cucsFirmwareImageFsmRmtRslt,
       "cucsFirmwareImageFsmStageTable": cucsFirmwareImageFsmStageTable,
       "cucsFirmwareImageFsmStageEntry": cucsFirmwareImageFsmStageEntry,
       "cucsFirmwareImageFsmStageInstanceId": cucsFirmwareImageFsmStageInstanceId,
       "cucsFirmwareImageFsmStageDn": cucsFirmwareImageFsmStageDn,
       "cucsFirmwareImageFsmStageRn": cucsFirmwareImageFsmStageRn,
       "cucsFirmwareImageFsmStageDescrData": cucsFirmwareImageFsmStageDescrData,
       "cucsFirmwareImageFsmStageLastUpdateTime": cucsFirmwareImageFsmStageLastUpdateTime,
       "cucsFirmwareImageFsmStageName": cucsFirmwareImageFsmStageName,
       "cucsFirmwareImageFsmStageOrder": cucsFirmwareImageFsmStageOrder,
       "cucsFirmwareImageFsmStageRetry": cucsFirmwareImageFsmStageRetry,
       "cucsFirmwareImageFsmStageStageStatus": cucsFirmwareImageFsmStageStageStatus,
       "cucsFirmwareInfraTable": cucsFirmwareInfraTable,
       "cucsFirmwareInfraEntry": cucsFirmwareInfraEntry,
       "cucsFirmwareInfraInstanceId": cucsFirmwareInfraInstanceId,
       "cucsFirmwareInfraDn": cucsFirmwareInfraDn,
       "cucsFirmwareInfraRn": cucsFirmwareInfraRn,
       "cucsFirmwareInfraAdminState": cucsFirmwareInfraAdminState,
       "cucsFirmwareInfraAutoDelete": cucsFirmwareInfraAutoDelete,
       "cucsFirmwareInfraDescr": cucsFirmwareInfraDescr,
       "cucsFirmwareInfraIgnoreCap": cucsFirmwareInfraIgnoreCap,
       "cucsFirmwareInfraIntId": cucsFirmwareInfraIntId,
       "cucsFirmwareInfraName": cucsFirmwareInfraName,
       "cucsFirmwareInfraOperScheduler": cucsFirmwareInfraOperScheduler,
       "cucsFirmwareInfraOperState": cucsFirmwareInfraOperState,
       "cucsFirmwareInfraOperVersion": cucsFirmwareInfraOperVersion,
       "cucsFirmwareInfraPolicyLevel": cucsFirmwareInfraPolicyLevel,
       "cucsFirmwareInfraPolicyOwner": cucsFirmwareInfraPolicyOwner,
       "cucsFirmwareInfraScheduler": cucsFirmwareInfraScheduler,
       "cucsFirmwareInfraPackTable": cucsFirmwareInfraPackTable,
       "cucsFirmwareInfraPackEntry": cucsFirmwareInfraPackEntry,
       "cucsFirmwareInfraPackInstanceId": cucsFirmwareInfraPackInstanceId,
       "cucsFirmwareInfraPackDn": cucsFirmwareInfraPackDn,
       "cucsFirmwareInfraPackRn": cucsFirmwareInfraPackRn,
       "cucsFirmwareInfraPackDescr": cucsFirmwareInfraPackDescr,
       "cucsFirmwareInfraPackForceDeploy": cucsFirmwareInfraPackForceDeploy,
       "cucsFirmwareInfraPackInfraBundleName": cucsFirmwareInfraPackInfraBundleName,
       "cucsFirmwareInfraPackInfraBundleVersion": cucsFirmwareInfraPackInfraBundleVersion,
       "cucsFirmwareInfraPackIntId": cucsFirmwareInfraPackIntId,
       "cucsFirmwareInfraPackMode": cucsFirmwareInfraPackMode,
       "cucsFirmwareInfraPackName": cucsFirmwareInfraPackName,
       "cucsFirmwareInfraPackPolicyLevel": cucsFirmwareInfraPackPolicyLevel,
       "cucsFirmwareInfraPackPolicyOwner": cucsFirmwareInfraPackPolicyOwner,
       "cucsFirmwareInfraPackStageSize": cucsFirmwareInfraPackStageSize,
       "cucsFirmwareInfraPackUpdateTrigger": cucsFirmwareInfraPackUpdateTrigger,
       "cucsFirmwareInfraPackSkipValidation": cucsFirmwareInfraPackSkipValidation,
       "cucsFirmwareInstallImpactTable": cucsFirmwareInstallImpactTable,
       "cucsFirmwareInstallImpactEntry": cucsFirmwareInstallImpactEntry,
       "cucsFirmwareInstallImpactInstanceId": cucsFirmwareInstallImpactInstanceId,
       "cucsFirmwareInstallImpactDn": cucsFirmwareInstallImpactDn,
       "cucsFirmwareInstallImpactRn": cucsFirmwareInstallImpactRn,
       "cucsFirmwareInstallImpactDescr": cucsFirmwareInstallImpactDescr,
       "cucsFirmwareInstallImpactKeyDn": cucsFirmwareInstallImpactKeyDn,
       "cucsFirmwareInstallImpactMaintPolicyDn": cucsFirmwareInstallImpactMaintPolicyDn,
       "cucsFirmwareInstallImpactRebootPolicy": cucsFirmwareInstallImpactRebootPolicy,
       "cucsFirmwareInstallImpactSubject": cucsFirmwareInstallImpactSubject,
       "cucsFirmwareInstallImpactType": cucsFirmwareInstallImpactType,
       "cucsFirmwareRackTable": cucsFirmwareRackTable,
       "cucsFirmwareRackEntry": cucsFirmwareRackEntry,
       "cucsFirmwareRackInstanceId": cucsFirmwareRackInstanceId,
       "cucsFirmwareRackDn": cucsFirmwareRackDn,
       "cucsFirmwareRackRn": cucsFirmwareRackRn,
       "cucsFirmwareRackOperVersion": cucsFirmwareRackOperVersion,
       "cucsFirmwareStatusTable": cucsFirmwareStatusTable,
       "cucsFirmwareStatusEntry": cucsFirmwareStatusEntry,
       "cucsFirmwareStatusInstanceId": cucsFirmwareStatusInstanceId,
       "cucsFirmwareStatusDn": cucsFirmwareStatusDn,
       "cucsFirmwareStatusRn": cucsFirmwareStatusRn,
       "cucsFirmwareStatusOperState": cucsFirmwareStatusOperState,
       "cucsFirmwareStatusPackageVersion": cucsFirmwareStatusPackageVersion,
       "cucsFirmwareStatusCimcVersion": cucsFirmwareStatusCimcVersion,
       "cucsFirmwareStatusFirmwareState": cucsFirmwareStatusFirmwareState,
       "cucsFirmwareStatusPldVersion": cucsFirmwareStatusPldVersion,
       "cucsFirmwareSystemTable": cucsFirmwareSystemTable,
       "cucsFirmwareSystemEntry": cucsFirmwareSystemEntry,
       "cucsFirmwareSystemInstanceId": cucsFirmwareSystemInstanceId,
       "cucsFirmwareSystemDn": cucsFirmwareSystemDn,
       "cucsFirmwareSystemRn": cucsFirmwareSystemRn,
       "cucsFirmwareSystemFsmDescr": cucsFirmwareSystemFsmDescr,
       "cucsFirmwareSystemFsmFlags": cucsFirmwareSystemFsmFlags,
       "cucsFirmwareSystemFsmPrev": cucsFirmwareSystemFsmPrev,
       "cucsFirmwareSystemFsmProgr": cucsFirmwareSystemFsmProgr,
       "cucsFirmwareSystemFsmRmtInvErrCode": cucsFirmwareSystemFsmRmtInvErrCode,
       "cucsFirmwareSystemFsmRmtInvErrDescr": cucsFirmwareSystemFsmRmtInvErrDescr,
       "cucsFirmwareSystemFsmRmtInvRslt": cucsFirmwareSystemFsmRmtInvRslt,
       "cucsFirmwareSystemFsmStageDescr": cucsFirmwareSystemFsmStageDescr,
       "cucsFirmwareSystemFsmStamp": cucsFirmwareSystemFsmStamp,
       "cucsFirmwareSystemFsmStatus": cucsFirmwareSystemFsmStatus,
       "cucsFirmwareSystemFsmTry": cucsFirmwareSystemFsmTry,
       "cucsFirmwareSystemOperState": cucsFirmwareSystemOperState,
       "cucsFirmwareSystemState": cucsFirmwareSystemState,
       "cucsFirmwareSystemCompCheckResultTable": cucsFirmwareSystemCompCheckResultTable,
       "cucsFirmwareSystemCompCheckResultEntry": cucsFirmwareSystemCompCheckResultEntry,
       "cucsFirmwareSystemCompCheckResultInstanceId": cucsFirmwareSystemCompCheckResultInstanceId,
       "cucsFirmwareSystemCompCheckResultDn": cucsFirmwareSystemCompCheckResultDn,
       "cucsFirmwareSystemCompCheckResultRn": cucsFirmwareSystemCompCheckResultRn,
       "cucsFirmwareSystemCompCheckResultKeyDescr": cucsFirmwareSystemCompCheckResultKeyDescr,
       "cucsFirmwareSystemCompCheckResultKeyDn": cucsFirmwareSystemCompCheckResultKeyDn,
       "cucsFirmwareSystemCompCheckResultNonCompDescr": cucsFirmwareSystemCompCheckResultNonCompDescr,
       "cucsFirmwareSystemCompCheckResultNonCompDns": cucsFirmwareSystemCompCheckResultNonCompDns,
       "cucsFirmwareSystemCompCheckResultSubject": cucsFirmwareSystemCompCheckResultSubject,
       "cucsFirmwareSystemFsmTable": cucsFirmwareSystemFsmTable,
       "cucsFirmwareSystemFsmEntry": cucsFirmwareSystemFsmEntry,
       "cucsFirmwareSystemFsmInstanceId": cucsFirmwareSystemFsmInstanceId,
       "cucsFirmwareSystemFsmDn": cucsFirmwareSystemFsmDn,
       "cucsFirmwareSystemFsmRn": cucsFirmwareSystemFsmRn,
       "cucsFirmwareSystemFsmCompletionTime": cucsFirmwareSystemFsmCompletionTime,
       "cucsFirmwareSystemFsmCurrentFsm": cucsFirmwareSystemFsmCurrentFsm,
       "cucsFirmwareSystemFsmDescrData": cucsFirmwareSystemFsmDescrData,
       "cucsFirmwareSystemFsmFsmStatus": cucsFirmwareSystemFsmFsmStatus,
       "cucsFirmwareSystemFsmProgress": cucsFirmwareSystemFsmProgress,
       "cucsFirmwareSystemFsmRmtErrCode": cucsFirmwareSystemFsmRmtErrCode,
       "cucsFirmwareSystemFsmRmtErrDescr": cucsFirmwareSystemFsmRmtErrDescr,
       "cucsFirmwareSystemFsmRmtRslt": cucsFirmwareSystemFsmRmtRslt,
       "cucsFirmwareSystemFsmStageTable": cucsFirmwareSystemFsmStageTable,
       "cucsFirmwareSystemFsmStageEntry": cucsFirmwareSystemFsmStageEntry,
       "cucsFirmwareSystemFsmStageInstanceId": cucsFirmwareSystemFsmStageInstanceId,
       "cucsFirmwareSystemFsmStageDn": cucsFirmwareSystemFsmStageDn,
       "cucsFirmwareSystemFsmStageRn": cucsFirmwareSystemFsmStageRn,
       "cucsFirmwareSystemFsmStageDescrData": cucsFirmwareSystemFsmStageDescrData,
       "cucsFirmwareSystemFsmStageLastUpdateTime": cucsFirmwareSystemFsmStageLastUpdateTime,
       "cucsFirmwareSystemFsmStageName": cucsFirmwareSystemFsmStageName,
       "cucsFirmwareSystemFsmStageOrder": cucsFirmwareSystemFsmStageOrder,
       "cucsFirmwareSystemFsmStageRetry": cucsFirmwareSystemFsmStageRetry,
       "cucsFirmwareSystemFsmStageStageStatus": cucsFirmwareSystemFsmStageStageStatus,
       "cucsFirmwareSystemFsmTaskTable": cucsFirmwareSystemFsmTaskTable,
       "cucsFirmwareSystemFsmTaskEntry": cucsFirmwareSystemFsmTaskEntry,
       "cucsFirmwareSystemFsmTaskInstanceId": cucsFirmwareSystemFsmTaskInstanceId,
       "cucsFirmwareSystemFsmTaskDn": cucsFirmwareSystemFsmTaskDn,
       "cucsFirmwareSystemFsmTaskRn": cucsFirmwareSystemFsmTaskRn,
       "cucsFirmwareSystemFsmTaskCompletion": cucsFirmwareSystemFsmTaskCompletion,
       "cucsFirmwareSystemFsmTaskFlags": cucsFirmwareSystemFsmTaskFlags,
       "cucsFirmwareSystemFsmTaskItem": cucsFirmwareSystemFsmTaskItem,
       "cucsFirmwareSystemFsmTaskSeqId": cucsFirmwareSystemFsmTaskSeqId,
       "cucsFirmwareUpgradeDetailTable": cucsFirmwareUpgradeDetailTable,
       "cucsFirmwareUpgradeDetailEntry": cucsFirmwareUpgradeDetailEntry,
       "cucsFirmwareUpgradeDetailInstanceId": cucsFirmwareUpgradeDetailInstanceId,
       "cucsFirmwareUpgradeDetailDn": cucsFirmwareUpgradeDetailDn,
       "cucsFirmwareUpgradeDetailRn": cucsFirmwareUpgradeDetailRn,
       "cucsFirmwareUpgradeDetailCategory": cucsFirmwareUpgradeDetailCategory,
       "cucsFirmwareUpgradeDetailDescription": cucsFirmwareUpgradeDetailDescription,
       "cucsFirmwareUpgradeDetailId": cucsFirmwareUpgradeDetailId,
       "cucsFirmwareUpgradeDetailSeverity": cucsFirmwareUpgradeDetailSeverity,
       "cucsFirmwareUpgradeInfoTable": cucsFirmwareUpgradeInfoTable,
       "cucsFirmwareUpgradeInfoEntry": cucsFirmwareUpgradeInfoEntry,
       "cucsFirmwareUpgradeInfoInstanceId": cucsFirmwareUpgradeInfoInstanceId,
       "cucsFirmwareUpgradeInfoDn": cucsFirmwareUpgradeInfoDn,
       "cucsFirmwareUpgradeInfoRn": cucsFirmwareUpgradeInfoRn,
       "cucsFirmwareUpgradeInfoMessage": cucsFirmwareUpgradeInfoMessage,
       "cucsFirmwareUpgradeInfoTimeStamp": cucsFirmwareUpgradeInfoTimeStamp,
       "cucsFirmwareUpgradeInfoValidateStatus": cucsFirmwareUpgradeInfoValidateStatus,
       "cucsFirmwareUpgradeInfoVersion": cucsFirmwareUpgradeInfoVersion,
       "cucsFirmwareAutoSyncPolicyTable": cucsFirmwareAutoSyncPolicyTable,
       "cucsFirmwareAutoSyncPolicyEntry": cucsFirmwareAutoSyncPolicyEntry,
       "cucsFirmwareAutoSyncPolicyInstanceId": cucsFirmwareAutoSyncPolicyInstanceId,
       "cucsFirmwareAutoSyncPolicyDn": cucsFirmwareAutoSyncPolicyDn,
       "cucsFirmwareAutoSyncPolicyRn": cucsFirmwareAutoSyncPolicyRn,
       "cucsFirmwareAutoSyncPolicyConfigIssue": cucsFirmwareAutoSyncPolicyConfigIssue,
       "cucsFirmwareAutoSyncPolicyDescr": cucsFirmwareAutoSyncPolicyDescr,
       "cucsFirmwareAutoSyncPolicyIntId": cucsFirmwareAutoSyncPolicyIntId,
       "cucsFirmwareAutoSyncPolicyName": cucsFirmwareAutoSyncPolicyName,
       "cucsFirmwareAutoSyncPolicyPolicyLevel": cucsFirmwareAutoSyncPolicyPolicyLevel,
       "cucsFirmwareAutoSyncPolicyPolicyOwner": cucsFirmwareAutoSyncPolicyPolicyOwner,
       "cucsFirmwareAutoSyncPolicySyncState": cucsFirmwareAutoSyncPolicySyncState,
       "cucsFirmwareImageLockTable": cucsFirmwareImageLockTable,
       "cucsFirmwareImageLockEntry": cucsFirmwareImageLockEntry,
       "cucsFirmwareImageLockInstanceId": cucsFirmwareImageLockInstanceId,
       "cucsFirmwareImageLockDn": cucsFirmwareImageLockDn,
       "cucsFirmwareImageLockRn": cucsFirmwareImageLockRn,
       "cucsFirmwareImageLockImageNameDn": cucsFirmwareImageLockImageNameDn,
       "cucsFirmwareImageLockName": cucsFirmwareImageLockName,
       "cucsFirmwareUcscInfoTable": cucsFirmwareUcscInfoTable,
       "cucsFirmwareUcscInfoEntry": cucsFirmwareUcscInfoEntry,
       "cucsFirmwareUcscInfoInstanceId": cucsFirmwareUcscInfoInstanceId,
       "cucsFirmwareUcscInfoDn": cucsFirmwareUcscInfoDn,
       "cucsFirmwareUcscInfoRn": cucsFirmwareUcscInfoRn,
       "cucsFirmwareUcscInfoConnProtocol": cucsFirmwareUcscInfoConnProtocol,
       "cucsFirmwareUcscInfoHost": cucsFirmwareUcscInfoHost,
       "cucsFirmwareUcscInfoVersion": cucsFirmwareUcscInfoVersion,
       "cucsFirmwarePlatformBundleTypeCapProviderTable": cucsFirmwarePlatformBundleTypeCapProviderTable,
       "cucsFirmwarePlatformBundleTypeCapProviderEntry": cucsFirmwarePlatformBundleTypeCapProviderEntry,
       "cucsFirmwarePlatformBundleTypeCapProviderInstanceId": cucsFirmwarePlatformBundleTypeCapProviderInstanceId,
       "cucsFirmwarePlatformBundleTypeCapProviderDn": cucsFirmwarePlatformBundleTypeCapProviderDn,
       "cucsFirmwarePlatformBundleTypeCapProviderRn": cucsFirmwarePlatformBundleTypeCapProviderRn,
       "cucsFirmwarePlatformBundleTypeCapProviderDeleted": cucsFirmwarePlatformBundleTypeCapProviderDeleted,
       "cucsFirmwarePlatformBundleTypeCapProviderDeprecated": cucsFirmwarePlatformBundleTypeCapProviderDeprecated,
       "cucsFirmwarePlatformBundleTypeCapProviderElementLoadFailures": cucsFirmwarePlatformBundleTypeCapProviderElementLoadFailures,
       "cucsFirmwarePlatformBundleTypeCapProviderElementsLoaded": cucsFirmwarePlatformBundleTypeCapProviderElementsLoaded,
       "cucsFirmwarePlatformBundleTypeCapProviderGencount": cucsFirmwarePlatformBundleTypeCapProviderGencount,
       "cucsFirmwarePlatformBundleTypeCapProviderLoadErrors": cucsFirmwarePlatformBundleTypeCapProviderLoadErrors,
       "cucsFirmwarePlatformBundleTypeCapProviderLoadWarnings": cucsFirmwarePlatformBundleTypeCapProviderLoadWarnings,
       "cucsFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer": cucsFirmwarePlatformBundleTypeCapProviderMgmtPlaneVer,
       "cucsFirmwarePlatformBundleTypeCapProviderModel": cucsFirmwarePlatformBundleTypeCapProviderModel,
       "cucsFirmwarePlatformBundleTypeCapProviderPlatformType": cucsFirmwarePlatformBundleTypeCapProviderPlatformType,
       "cucsFirmwarePlatformBundleTypeCapProviderVendor": cucsFirmwarePlatformBundleTypeCapProviderVendor,
       "cucsFirmwareConstraintsTable": cucsFirmwareConstraintsTable,
       "cucsFirmwareConstraintsEntry": cucsFirmwareConstraintsEntry,
       "cucsFirmwareConstraintsInstanceId": cucsFirmwareConstraintsInstanceId,
       "cucsFirmwareConstraintsDn": cucsFirmwareConstraintsDn,
       "cucsFirmwareConstraintsRn": cucsFirmwareConstraintsRn,
       "cucsFirmwareFileUnitTable": cucsFirmwareFileUnitTable,
       "cucsFirmwareFileUnitEntry": cucsFirmwareFileUnitEntry,
       "cucsFirmwareFileUnitInstanceId": cucsFirmwareFileUnitInstanceId,
       "cucsFirmwareFileUnitDn": cucsFirmwareFileUnitDn,
       "cucsFirmwareFileUnitRn": cucsFirmwareFileUnitRn,
       "cucsFirmwareFileUnitPathName": cucsFirmwareFileUnitPathName,
       "cucsFirmwareFileUnitType": cucsFirmwareFileUnitType,
       "cucsFirmwareFileUnitVersion": cucsFirmwareFileUnitVersion,
       "cucsFirmwareActivityTable": cucsFirmwareActivityTable,
       "cucsFirmwareActivityEntry": cucsFirmwareActivityEntry,
       "cucsFirmwareActivityInstanceId": cucsFirmwareActivityInstanceId,
       "cucsFirmwareActivityDn": cucsFirmwareActivityDn,
       "cucsFirmwareActivityRn": cucsFirmwareActivityRn,
       "cucsFirmwareActivityChassisCompInActivationDn": cucsFirmwareActivityChassisCompInActivationDn,
       "cucsFirmwareActivityServerCompInActivationDn": cucsFirmwareActivityServerCompInActivationDn,
       "cucsFirmwareActivityServersPowerState": cucsFirmwareActivityServersPowerState,
       "cucsFirmwareActivityUpgradePriorityInfo": cucsFirmwareActivityUpgradePriorityInfo,
       "cucsFirmwareProcessorTypeConstraintTable": cucsFirmwareProcessorTypeConstraintTable,
       "cucsFirmwareProcessorTypeConstraintEntry": cucsFirmwareProcessorTypeConstraintEntry,
       "cucsFirmwareProcessorTypeConstraintInstanceId": cucsFirmwareProcessorTypeConstraintInstanceId,
       "cucsFirmwareProcessorTypeConstraintDn": cucsFirmwareProcessorTypeConstraintDn,
       "cucsFirmwareProcessorTypeConstraintRn": cucsFirmwareProcessorTypeConstraintRn,
       "cucsFirmwareProcessorTypeConstraintMinBiosVersion": cucsFirmwareProcessorTypeConstraintMinBiosVersion,
       "cucsFirmwareProcessorTypeConstraintMinCimcVersion": cucsFirmwareProcessorTypeConstraintMinCimcVersion,
       "cucsFirmwareProcessorTypeConstraintType": cucsFirmwareProcessorTypeConstraintType,
       "cucsFirmwareVnicCdnConstraintTable": cucsFirmwareVnicCdnConstraintTable,
       "cucsFirmwareVnicCdnConstraintEntry": cucsFirmwareVnicCdnConstraintEntry,
       "cucsFirmwareVnicCdnConstraintInstanceId": cucsFirmwareVnicCdnConstraintInstanceId,
       "cucsFirmwareVnicCdnConstraintDn": cucsFirmwareVnicCdnConstraintDn,
       "cucsFirmwareVnicCdnConstraintRn": cucsFirmwareVnicCdnConstraintRn,
       "cucsFirmwareVnicCdnConstraintMinBiosVersion": cucsFirmwareVnicCdnConstraintMinBiosVersion,
       "cucsFirmwareVnicCdnConstraintMinCimcVersion": cucsFirmwareVnicCdnConstraintMinCimcVersion,
       "cucsFirmwareVnicCdnConstraintType": cucsFirmwareVnicCdnConstraintType,
       "cucsFirmwareExcludeServerComponentTable": cucsFirmwareExcludeServerComponentTable,
       "cucsFirmwareExcludeServerComponentEntry": cucsFirmwareExcludeServerComponentEntry,
       "cucsFirmwareExcludeServerComponentInstanceId": cucsFirmwareExcludeServerComponentInstanceId,
       "cucsFirmwareExcludeServerComponentDn": cucsFirmwareExcludeServerComponentDn,
       "cucsFirmwareExcludeServerComponentRn": cucsFirmwareExcludeServerComponentRn,
       "cucsFirmwareExcludeServerComponentServerComponent": cucsFirmwareExcludeServerComponentServerComponent,
       "cucsFirmwareExcludeServerComponentPropAcl": cucsFirmwareExcludeServerComponentPropAcl,
       "cucsFirmwarePCHStorageConfigConstraintTable": cucsFirmwarePCHStorageConfigConstraintTable,
       "cucsFirmwarePCHStorageConfigConstraintEntry": cucsFirmwarePCHStorageConfigConstraintEntry,
       "cucsFirmwarePCHStorageConfigConstraintInstanceId": cucsFirmwarePCHStorageConfigConstraintInstanceId,
       "cucsFirmwarePCHStorageConfigConstraintDn": cucsFirmwarePCHStorageConfigConstraintDn,
       "cucsFirmwarePCHStorageConfigConstraintRn": cucsFirmwarePCHStorageConfigConstraintRn,
       "cucsFirmwarePCHStorageConfigConstraintMinBiosVersion": cucsFirmwarePCHStorageConfigConstraintMinBiosVersion,
       "cucsFirmwarePCHStorageConfigConstraintMinCimcVersion": cucsFirmwarePCHStorageConfigConstraintMinCimcVersion,
       "cucsFirmwareServerTypeConstraintTable": cucsFirmwareServerTypeConstraintTable,
       "cucsFirmwareServerTypeConstraintEntry": cucsFirmwareServerTypeConstraintEntry,
       "cucsFirmwareServerTypeConstraintInstanceId": cucsFirmwareServerTypeConstraintInstanceId,
       "cucsFirmwareServerTypeConstraintDn": cucsFirmwareServerTypeConstraintDn,
       "cucsFirmwareServerTypeConstraintRn": cucsFirmwareServerTypeConstraintRn,
       "cucsFirmwareServerTypeConstraintMinBiosVersion": cucsFirmwareServerTypeConstraintMinBiosVersion,
       "cucsFirmwareServerTypeConstraintMinCimcVersion": cucsFirmwareServerTypeConstraintMinCimcVersion,
       "cucsFirmwareVicSlotConstraintTable": cucsFirmwareVicSlotConstraintTable,
       "cucsFirmwareVicSlotConstraintEntry": cucsFirmwareVicSlotConstraintEntry,
       "cucsFirmwareVicSlotConstraintInstanceId": cucsFirmwareVicSlotConstraintInstanceId,
       "cucsFirmwareVicSlotConstraintDn": cucsFirmwareVicSlotConstraintDn,
       "cucsFirmwareVicSlotConstraintRn": cucsFirmwareVicSlotConstraintRn,
       "cucsFirmwareVicSlotConstraintMinBiosVersion": cucsFirmwareVicSlotConstraintMinBiosVersion,
       "cucsFirmwareVicSlotConstraintMinCimcVersion": cucsFirmwareVicSlotConstraintMinCimcVersion,
       "cucsFirmwareVicSlotConstraintVicSlot": cucsFirmwareVicSlotConstraintVicSlot}
)
