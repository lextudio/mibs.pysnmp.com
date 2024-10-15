# SNMP MIB module (CISCO-UNIFIED-COMPUTING-COMPUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-COMPUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:10 2024
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

(CucsComputeABoardPower,
 CucsComputeAdminLinkAggregation,
 CucsComputeAdminMemoryState,
 CucsComputeAdminPowerState,
 CucsComputeAdminState,
 CucsComputeAdminTrigger,
 CucsComputeAlarmSeverity,
 CucsComputeAssociation,
 CucsComputeAvailability,
 CucsComputeBlackListing,
 CucsComputeBladeEpId,
 CucsComputeBladeEpSlotId,
 CucsComputeBladeFsmCurrentFsm,
 CucsComputeBladeFsmStageName,
 CucsComputeBladeFsmTaskFlags,
 CucsComputeBladeFsmTaskItem,
 CucsComputeBladeSlotId,
 CucsComputeCartridgeDiscovery,
 CucsComputeCartridgeSlotId,
 CucsComputeChassisConnPolicyChassisId,
 CucsComputeChassisDiscAction,
 CucsComputeChassisDiscPolicyMulticastHwHash,
 CucsComputeChassisQualMaxId,
 CucsComputeChassisQualMinId,
 CucsComputeCheckPoint,
 CucsComputeConnectivityRebalancing,
 CucsComputeDiscovery,
 CucsComputeEquipmentConstraintType,
 CucsComputeIOHubEnvStatsHistThresholded,
 CucsComputeIOHubEnvStatsThresholded,
 CucsComputeInstanceIdQualMaxId,
 CucsComputeInstanceIdQualMinId,
 CucsComputeIssues,
 CucsComputeKvmMgmtPolicyVmediaEncryption,
 CucsComputeLinkAggregation,
 CucsComputeMbPowerStatsHistThresholded,
 CucsComputeMbPowerStatsThresholded,
 CucsComputeMbTempStatsHistThresholded,
 CucsComputeMbTempStatsThresholded,
 CucsComputeMemoryUnitConstraintType,
 CucsComputeMode,
 CucsComputeOwner,
 CucsComputePCIeFatalCompletionStatsThresholded,
 CucsComputePCIeFatalProtocolStatsThresholded,
 CucsComputePCIeFatalReceiveStatsThresholded,
 CucsComputePCIeFatalStatsThresholded,
 CucsComputePciCapOrder,
 CucsComputePhysicalFsmCurrentFsm,
 CucsComputePhysicalFsmStageName,
 CucsComputePhysicalFsmTaskFlags,
 CucsComputePhysicalFsmTaskItem,
 CucsComputePhysicalLowVoltageMemory,
 CucsComputePooledEnclosureComputeSlotServerInstanceId,
 CucsComputePooledEnclosureComputeSlotSlotId,
 CucsComputePooledRackUnitId,
 CucsComputePooledSlotSlotId,
 CucsComputePowerTransitionSrc,
 CucsComputePsuClusterState,
 CucsComputePsuControlRedundancy,
 CucsComputePsuRedundancy,
 CucsComputePsuRedundancyOperQualifier,
 CucsComputePsuRedundancyOperState,
 CucsComputeRackQualMaxId,
 CucsComputeRackQualMinId,
 CucsComputeRackUnitFsmCurrentFsm,
 CucsComputeRackUnitFsmStageName,
 CucsComputeRackUnitFsmTaskFlags,
 CucsComputeRackUnitFsmTaskItem,
 CucsComputeRackUnitId,
 CucsComputeRackUnitMbTempStatsHistThresholded,
 CucsComputeRackUnitMbTempStatsThresholded,
 CucsComputeScrubAction,
 CucsComputeServerDiscPolicyFsmCurrentFsm,
 CucsComputeServerDiscPolicyFsmStageName,
 CucsComputeServerDiscPolicyFsmTaskItem,
 CucsComputeServerMgmtDiscAction,
 CucsComputeServerTypeCapType,
 CucsComputeServerUnitChassisId,
 CucsComputeServerUnitFsmCurrentFsm,
 CucsComputeServerUnitFsmStageName,
 CucsComputeServerUnitFsmTaskFlags,
 CucsComputeServerUnitFsmTaskItem,
 CucsComputeServerUnitServerInstanceId,
 CucsComputeServerUnitSlotId,
 CucsComputeSlotQualMaxId,
 CucsComputeSlotQualMinId,
 CucsComputeUpgradeStatus,
 CucsConditionRemoteInvRslt,
 CucsEquipmentBoardAggregationRole,
 CucsEquipmentBoardConnectorType,
 CucsEquipmentConnectionStatus,
 CucsEquipmentFanSpeedPolicyFault,
 CucsEquipmentOperability,
 CucsEquipmentPowerState,
 CucsEquipmentPresence,
 CucsEquipmentSensorThresholdStatus,
 CucsEquipmentSlotStatus,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsLsOperState,
 CucsNetworkSwitchId,
 CucsPolicyPolicyOwner,
 CucsPoolPoolAssignmentOrder,
 CucsTrigAckChangeDetails,
 CucsTrigAckChanges,
 CucsTrigAckDisr,
 CucsTrigAckOperState,
 CucsTrigAckPrevOperState,
 CucsTrigAdminState,
 CucsTrigTrigState) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsComputeABoardPower",
    "CucsComputeAdminLinkAggregation",
    "CucsComputeAdminMemoryState",
    "CucsComputeAdminPowerState",
    "CucsComputeAdminState",
    "CucsComputeAdminTrigger",
    "CucsComputeAlarmSeverity",
    "CucsComputeAssociation",
    "CucsComputeAvailability",
    "CucsComputeBlackListing",
    "CucsComputeBladeEpId",
    "CucsComputeBladeEpSlotId",
    "CucsComputeBladeFsmCurrentFsm",
    "CucsComputeBladeFsmStageName",
    "CucsComputeBladeFsmTaskFlags",
    "CucsComputeBladeFsmTaskItem",
    "CucsComputeBladeSlotId",
    "CucsComputeCartridgeDiscovery",
    "CucsComputeCartridgeSlotId",
    "CucsComputeChassisConnPolicyChassisId",
    "CucsComputeChassisDiscAction",
    "CucsComputeChassisDiscPolicyMulticastHwHash",
    "CucsComputeChassisQualMaxId",
    "CucsComputeChassisQualMinId",
    "CucsComputeCheckPoint",
    "CucsComputeConnectivityRebalancing",
    "CucsComputeDiscovery",
    "CucsComputeEquipmentConstraintType",
    "CucsComputeIOHubEnvStatsHistThresholded",
    "CucsComputeIOHubEnvStatsThresholded",
    "CucsComputeInstanceIdQualMaxId",
    "CucsComputeInstanceIdQualMinId",
    "CucsComputeIssues",
    "CucsComputeKvmMgmtPolicyVmediaEncryption",
    "CucsComputeLinkAggregation",
    "CucsComputeMbPowerStatsHistThresholded",
    "CucsComputeMbPowerStatsThresholded",
    "CucsComputeMbTempStatsHistThresholded",
    "CucsComputeMbTempStatsThresholded",
    "CucsComputeMemoryUnitConstraintType",
    "CucsComputeMode",
    "CucsComputeOwner",
    "CucsComputePCIeFatalCompletionStatsThresholded",
    "CucsComputePCIeFatalProtocolStatsThresholded",
    "CucsComputePCIeFatalReceiveStatsThresholded",
    "CucsComputePCIeFatalStatsThresholded",
    "CucsComputePciCapOrder",
    "CucsComputePhysicalFsmCurrentFsm",
    "CucsComputePhysicalFsmStageName",
    "CucsComputePhysicalFsmTaskFlags",
    "CucsComputePhysicalFsmTaskItem",
    "CucsComputePhysicalLowVoltageMemory",
    "CucsComputePooledEnclosureComputeSlotServerInstanceId",
    "CucsComputePooledEnclosureComputeSlotSlotId",
    "CucsComputePooledRackUnitId",
    "CucsComputePooledSlotSlotId",
    "CucsComputePowerTransitionSrc",
    "CucsComputePsuClusterState",
    "CucsComputePsuControlRedundancy",
    "CucsComputePsuRedundancy",
    "CucsComputePsuRedundancyOperQualifier",
    "CucsComputePsuRedundancyOperState",
    "CucsComputeRackQualMaxId",
    "CucsComputeRackQualMinId",
    "CucsComputeRackUnitFsmCurrentFsm",
    "CucsComputeRackUnitFsmStageName",
    "CucsComputeRackUnitFsmTaskFlags",
    "CucsComputeRackUnitFsmTaskItem",
    "CucsComputeRackUnitId",
    "CucsComputeRackUnitMbTempStatsHistThresholded",
    "CucsComputeRackUnitMbTempStatsThresholded",
    "CucsComputeScrubAction",
    "CucsComputeServerDiscPolicyFsmCurrentFsm",
    "CucsComputeServerDiscPolicyFsmStageName",
    "CucsComputeServerDiscPolicyFsmTaskItem",
    "CucsComputeServerMgmtDiscAction",
    "CucsComputeServerTypeCapType",
    "CucsComputeServerUnitChassisId",
    "CucsComputeServerUnitFsmCurrentFsm",
    "CucsComputeServerUnitFsmStageName",
    "CucsComputeServerUnitFsmTaskFlags",
    "CucsComputeServerUnitFsmTaskItem",
    "CucsComputeServerUnitServerInstanceId",
    "CucsComputeServerUnitSlotId",
    "CucsComputeSlotQualMaxId",
    "CucsComputeSlotQualMinId",
    "CucsComputeUpgradeStatus",
    "CucsConditionRemoteInvRslt",
    "CucsEquipmentBoardAggregationRole",
    "CucsEquipmentBoardConnectorType",
    "CucsEquipmentConnectionStatus",
    "CucsEquipmentFanSpeedPolicyFault",
    "CucsEquipmentOperability",
    "CucsEquipmentPowerState",
    "CucsEquipmentPresence",
    "CucsEquipmentSensorThresholdStatus",
    "CucsEquipmentSlotStatus",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsLsOperState",
    "CucsNetworkSwitchId",
    "CucsPolicyPolicyOwner",
    "CucsPoolPoolAssignmentOrder",
    "CucsTrigAckChangeDetails",
    "CucsTrigAckChanges",
    "CucsTrigAckDisr",
    "CucsTrigAckOperState",
    "CucsTrigAckPrevOperState",
    "CucsTrigAdminState",
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

cucsComputeObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsComputeAutoconfigPolicyTable_Object = MibTable
cucsComputeAutoconfigPolicyTable = _CucsComputeAutoconfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyTable.setStatus("current")
_CucsComputeAutoconfigPolicyEntry_Object = MibTableRow
cucsComputeAutoconfigPolicyEntry = _CucsComputeAutoconfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1)
)
cucsComputeAutoconfigPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeAutoconfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyEntry.setStatus("current")
_CucsComputeAutoconfigPolicyInstanceId_Type = CucsManagedObjectId
_CucsComputeAutoconfigPolicyInstanceId_Object = MibTableColumn
cucsComputeAutoconfigPolicyInstanceId = _CucsComputeAutoconfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1, 1),
    _CucsComputeAutoconfigPolicyInstanceId_Type()
)
cucsComputeAutoconfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyInstanceId.setStatus("current")
_CucsComputeAutoconfigPolicyDn_Type = CucsManagedObjectDn
_CucsComputeAutoconfigPolicyDn_Object = MibTableColumn
cucsComputeAutoconfigPolicyDn = _CucsComputeAutoconfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1, 2),
    _CucsComputeAutoconfigPolicyDn_Type()
)
cucsComputeAutoconfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyDn.setStatus("current")
_CucsComputeAutoconfigPolicyRn_Type = SnmpAdminString
_CucsComputeAutoconfigPolicyRn_Object = MibTableColumn
cucsComputeAutoconfigPolicyRn = _CucsComputeAutoconfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1, 3),
    _CucsComputeAutoconfigPolicyRn_Type()
)
cucsComputeAutoconfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyRn.setStatus("current")
_CucsComputeAutoconfigPolicyDescr_Type = SnmpAdminString
_CucsComputeAutoconfigPolicyDescr_Object = MibTableColumn
cucsComputeAutoconfigPolicyDescr = _CucsComputeAutoconfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1, 4),
    _CucsComputeAutoconfigPolicyDescr_Type()
)
cucsComputeAutoconfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyDescr.setStatus("current")
_CucsComputeAutoconfigPolicyDstDn_Type = SnmpAdminString
_CucsComputeAutoconfigPolicyDstDn_Object = MibTableColumn
cucsComputeAutoconfigPolicyDstDn = _CucsComputeAutoconfigPolicyDstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1, 5),
    _CucsComputeAutoconfigPolicyDstDn_Type()
)
cucsComputeAutoconfigPolicyDstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyDstDn.setStatus("current")
_CucsComputeAutoconfigPolicyIntId_Type = SnmpAdminString
_CucsComputeAutoconfigPolicyIntId_Object = MibTableColumn
cucsComputeAutoconfigPolicyIntId = _CucsComputeAutoconfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1, 6),
    _CucsComputeAutoconfigPolicyIntId_Type()
)
cucsComputeAutoconfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyIntId.setStatus("current")
_CucsComputeAutoconfigPolicyName_Type = SnmpAdminString
_CucsComputeAutoconfigPolicyName_Object = MibTableColumn
cucsComputeAutoconfigPolicyName = _CucsComputeAutoconfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1, 7),
    _CucsComputeAutoconfigPolicyName_Type()
)
cucsComputeAutoconfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyName.setStatus("current")
_CucsComputeAutoconfigPolicyQualifier_Type = SnmpAdminString
_CucsComputeAutoconfigPolicyQualifier_Object = MibTableColumn
cucsComputeAutoconfigPolicyQualifier = _CucsComputeAutoconfigPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1, 8),
    _CucsComputeAutoconfigPolicyQualifier_Type()
)
cucsComputeAutoconfigPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyQualifier.setStatus("current")
_CucsComputeAutoconfigPolicySrcTemplName_Type = SnmpAdminString
_CucsComputeAutoconfigPolicySrcTemplName_Object = MibTableColumn
cucsComputeAutoconfigPolicySrcTemplName = _CucsComputeAutoconfigPolicySrcTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1, 9),
    _CucsComputeAutoconfigPolicySrcTemplName_Type()
)
cucsComputeAutoconfigPolicySrcTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicySrcTemplName.setStatus("current")
_CucsComputeAutoconfigPolicyPolicyLevel_Type = Gauge32
_CucsComputeAutoconfigPolicyPolicyLevel_Object = MibTableColumn
cucsComputeAutoconfigPolicyPolicyLevel = _CucsComputeAutoconfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1, 10),
    _CucsComputeAutoconfigPolicyPolicyLevel_Type()
)
cucsComputeAutoconfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyPolicyLevel.setStatus("current")
_CucsComputeAutoconfigPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeAutoconfigPolicyPolicyOwner_Object = MibTableColumn
cucsComputeAutoconfigPolicyPolicyOwner = _CucsComputeAutoconfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1, 11),
    _CucsComputeAutoconfigPolicyPolicyOwner_Type()
)
cucsComputeAutoconfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyPolicyOwner.setStatus("current")
_CucsComputeAutoconfigPolicyOperQualifier_Type = SnmpAdminString
_CucsComputeAutoconfigPolicyOperQualifier_Object = MibTableColumn
cucsComputeAutoconfigPolicyOperQualifier = _CucsComputeAutoconfigPolicyOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 1, 1, 12),
    _CucsComputeAutoconfigPolicyOperQualifier_Type()
)
cucsComputeAutoconfigPolicyOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeAutoconfigPolicyOperQualifier.setStatus("current")
_CucsComputeBladeTable_Object = MibTable
cucsComputeBladeTable = _CucsComputeBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2)
)
if mibBuilder.loadTexts:
    cucsComputeBladeTable.setStatus("current")
_CucsComputeBladeEntry_Object = MibTableRow
cucsComputeBladeEntry = _CucsComputeBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1)
)
cucsComputeBladeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeBladeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeBladeEntry.setStatus("current")
_CucsComputeBladeInstanceId_Type = CucsManagedObjectId
_CucsComputeBladeInstanceId_Object = MibTableColumn
cucsComputeBladeInstanceId = _CucsComputeBladeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 1),
    _CucsComputeBladeInstanceId_Type()
)
cucsComputeBladeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeBladeInstanceId.setStatus("current")
_CucsComputeBladeDn_Type = CucsManagedObjectDn
_CucsComputeBladeDn_Object = MibTableColumn
cucsComputeBladeDn = _CucsComputeBladeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 2),
    _CucsComputeBladeDn_Type()
)
cucsComputeBladeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDn.setStatus("current")
_CucsComputeBladeRn_Type = SnmpAdminString
_CucsComputeBladeRn_Object = MibTableColumn
cucsComputeBladeRn = _CucsComputeBladeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 3),
    _CucsComputeBladeRn_Type()
)
cucsComputeBladeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeRn.setStatus("current")
_CucsComputeBladeAdminPower_Type = CucsComputeAdminPowerState
_CucsComputeBladeAdminPower_Object = MibTableColumn
cucsComputeBladeAdminPower = _CucsComputeBladeAdminPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 4),
    _CucsComputeBladeAdminPower_Type()
)
cucsComputeBladeAdminPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeAdminPower.setStatus("current")
_CucsComputeBladeAdminState_Type = CucsComputeAdminState
_CucsComputeBladeAdminState_Object = MibTableColumn
cucsComputeBladeAdminState = _CucsComputeBladeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 5),
    _CucsComputeBladeAdminState_Type()
)
cucsComputeBladeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeAdminState.setStatus("current")
_CucsComputeBladeAssignedToDn_Type = SnmpAdminString
_CucsComputeBladeAssignedToDn_Object = MibTableColumn
cucsComputeBladeAssignedToDn = _CucsComputeBladeAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 6),
    _CucsComputeBladeAssignedToDn_Type()
)
cucsComputeBladeAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeAssignedToDn.setStatus("current")
_CucsComputeBladeAssociation_Type = CucsComputeAssociation
_CucsComputeBladeAssociation_Object = MibTableColumn
cucsComputeBladeAssociation = _CucsComputeBladeAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 7),
    _CucsComputeBladeAssociation_Type()
)
cucsComputeBladeAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeAssociation.setStatus("current")
_CucsComputeBladeAvailability_Type = CucsComputeAvailability
_CucsComputeBladeAvailability_Object = MibTableColumn
cucsComputeBladeAvailability = _CucsComputeBladeAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 8),
    _CucsComputeBladeAvailability_Type()
)
cucsComputeBladeAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeAvailability.setStatus("current")
_CucsComputeBladeAvailableMemory_Type = Gauge32
_CucsComputeBladeAvailableMemory_Object = MibTableColumn
cucsComputeBladeAvailableMemory = _CucsComputeBladeAvailableMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 9),
    _CucsComputeBladeAvailableMemory_Type()
)
cucsComputeBladeAvailableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeAvailableMemory.setStatus("current")
_CucsComputeBladeChassisId_Type = Gauge32
_CucsComputeBladeChassisId_Object = MibTableColumn
cucsComputeBladeChassisId = _CucsComputeBladeChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 10),
    _CucsComputeBladeChassisId_Type()
)
cucsComputeBladeChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeChassisId.setStatus("current")
_CucsComputeBladeCheckPoint_Type = CucsComputeCheckPoint
_CucsComputeBladeCheckPoint_Object = MibTableColumn
cucsComputeBladeCheckPoint = _CucsComputeBladeCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 11),
    _CucsComputeBladeCheckPoint_Type()
)
cucsComputeBladeCheckPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeCheckPoint.setStatus("current")
_CucsComputeBladeConnPath_Type = CucsEquipmentConnectionStatus
_CucsComputeBladeConnPath_Object = MibTableColumn
cucsComputeBladeConnPath = _CucsComputeBladeConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 12),
    _CucsComputeBladeConnPath_Type()
)
cucsComputeBladeConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeConnPath.setStatus("current")
_CucsComputeBladeConnStatus_Type = CucsEquipmentConnectionStatus
_CucsComputeBladeConnStatus_Object = MibTableColumn
cucsComputeBladeConnStatus = _CucsComputeBladeConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 13),
    _CucsComputeBladeConnStatus_Type()
)
cucsComputeBladeConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeConnStatus.setStatus("current")
_CucsComputeBladeDescr_Type = SnmpAdminString
_CucsComputeBladeDescr_Object = MibTableColumn
cucsComputeBladeDescr = _CucsComputeBladeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 14),
    _CucsComputeBladeDescr_Type()
)
cucsComputeBladeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDescr.setStatus("current")
_CucsComputeBladeDiscovery_Type = CucsComputeDiscovery
_CucsComputeBladeDiscovery_Object = MibTableColumn
cucsComputeBladeDiscovery = _CucsComputeBladeDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 15),
    _CucsComputeBladeDiscovery_Type()
)
cucsComputeBladeDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscovery.setStatus("current")
_CucsComputeBladeFltAggr_Type = Unsigned64
_CucsComputeBladeFltAggr_Object = MibTableColumn
cucsComputeBladeFltAggr = _CucsComputeBladeFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 16),
    _CucsComputeBladeFltAggr_Type()
)
cucsComputeBladeFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFltAggr.setStatus("current")
_CucsComputeBladeFsmDescr_Type = SnmpAdminString
_CucsComputeBladeFsmDescr_Object = MibTableColumn
cucsComputeBladeFsmDescr = _CucsComputeBladeFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 17),
    _CucsComputeBladeFsmDescr_Type()
)
cucsComputeBladeFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmDescr.setStatus("current")
_CucsComputeBladeFsmFlags_Type = SnmpAdminString
_CucsComputeBladeFsmFlags_Object = MibTableColumn
cucsComputeBladeFsmFlags = _CucsComputeBladeFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 18),
    _CucsComputeBladeFsmFlags_Type()
)
cucsComputeBladeFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmFlags.setStatus("current")
_CucsComputeBladeFsmPrev_Type = SnmpAdminString
_CucsComputeBladeFsmPrev_Object = MibTableColumn
cucsComputeBladeFsmPrev = _CucsComputeBladeFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 19),
    _CucsComputeBladeFsmPrev_Type()
)
cucsComputeBladeFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmPrev.setStatus("current")
_CucsComputeBladeFsmProgr_Type = Gauge32
_CucsComputeBladeFsmProgr_Object = MibTableColumn
cucsComputeBladeFsmProgr = _CucsComputeBladeFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 20),
    _CucsComputeBladeFsmProgr_Type()
)
cucsComputeBladeFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmProgr.setStatus("current")
_CucsComputeBladeFsmRmtInvErrCode_Type = Gauge32
_CucsComputeBladeFsmRmtInvErrCode_Object = MibTableColumn
cucsComputeBladeFsmRmtInvErrCode = _CucsComputeBladeFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 21),
    _CucsComputeBladeFsmRmtInvErrCode_Type()
)
cucsComputeBladeFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmRmtInvErrCode.setStatus("current")
_CucsComputeBladeFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsComputeBladeFsmRmtInvErrDescr_Object = MibTableColumn
cucsComputeBladeFsmRmtInvErrDescr = _CucsComputeBladeFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 22),
    _CucsComputeBladeFsmRmtInvErrDescr_Type()
)
cucsComputeBladeFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmRmtInvErrDescr.setStatus("current")
_CucsComputeBladeFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsComputeBladeFsmRmtInvRslt_Object = MibTableColumn
cucsComputeBladeFsmRmtInvRslt = _CucsComputeBladeFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 23),
    _CucsComputeBladeFsmRmtInvRslt_Type()
)
cucsComputeBladeFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmRmtInvRslt.setStatus("current")
_CucsComputeBladeFsmStageDescr_Type = SnmpAdminString
_CucsComputeBladeFsmStageDescr_Object = MibTableColumn
cucsComputeBladeFsmStageDescr = _CucsComputeBladeFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 24),
    _CucsComputeBladeFsmStageDescr_Type()
)
cucsComputeBladeFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStageDescr.setStatus("current")
_CucsComputeBladeFsmStamp_Type = DateAndTime
_CucsComputeBladeFsmStamp_Object = MibTableColumn
cucsComputeBladeFsmStamp = _CucsComputeBladeFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 25),
    _CucsComputeBladeFsmStamp_Type()
)
cucsComputeBladeFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStamp.setStatus("current")
_CucsComputeBladeFsmStatus_Type = SnmpAdminString
_CucsComputeBladeFsmStatus_Object = MibTableColumn
cucsComputeBladeFsmStatus = _CucsComputeBladeFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 26),
    _CucsComputeBladeFsmStatus_Type()
)
cucsComputeBladeFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStatus.setStatus("current")
_CucsComputeBladeFsmTry_Type = Gauge32
_CucsComputeBladeFsmTry_Object = MibTableColumn
cucsComputeBladeFsmTry = _CucsComputeBladeFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 27),
    _CucsComputeBladeFsmTry_Type()
)
cucsComputeBladeFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmTry.setStatus("current")
_CucsComputeBladeIntId_Type = SnmpAdminString
_CucsComputeBladeIntId_Object = MibTableColumn
cucsComputeBladeIntId = _CucsComputeBladeIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 28),
    _CucsComputeBladeIntId_Type()
)
cucsComputeBladeIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeIntId.setStatus("current")
_CucsComputeBladeLc_Type = CucsComputeAdminTrigger
_CucsComputeBladeLc_Object = MibTableColumn
cucsComputeBladeLc = _CucsComputeBladeLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 29),
    _CucsComputeBladeLc_Type()
)
cucsComputeBladeLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeLc.setStatus("current")
_CucsComputeBladeLcTs_Type = DateAndTime
_CucsComputeBladeLcTs_Object = MibTableColumn
cucsComputeBladeLcTs = _CucsComputeBladeLcTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 30),
    _CucsComputeBladeLcTs_Type()
)
cucsComputeBladeLcTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeLcTs.setStatus("current")
_CucsComputeBladeManagingInst_Type = CucsNetworkSwitchId
_CucsComputeBladeManagingInst_Object = MibTableColumn
cucsComputeBladeManagingInst = _CucsComputeBladeManagingInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 31),
    _CucsComputeBladeManagingInst_Type()
)
cucsComputeBladeManagingInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeManagingInst.setStatus("current")
_CucsComputeBladeModel_Type = SnmpAdminString
_CucsComputeBladeModel_Object = MibTableColumn
cucsComputeBladeModel = _CucsComputeBladeModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 32),
    _CucsComputeBladeModel_Type()
)
cucsComputeBladeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeModel.setStatus("current")
_CucsComputeBladeName_Type = SnmpAdminString
_CucsComputeBladeName_Object = MibTableColumn
cucsComputeBladeName = _CucsComputeBladeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 33),
    _CucsComputeBladeName_Type()
)
cucsComputeBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeName.setStatus("current")
_CucsComputeBladeNumOfAdaptors_Type = Gauge32
_CucsComputeBladeNumOfAdaptors_Object = MibTableColumn
cucsComputeBladeNumOfAdaptors = _CucsComputeBladeNumOfAdaptors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 34),
    _CucsComputeBladeNumOfAdaptors_Type()
)
cucsComputeBladeNumOfAdaptors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeNumOfAdaptors.setStatus("current")
_CucsComputeBladeNumOfCores_Type = Gauge32
_CucsComputeBladeNumOfCores_Object = MibTableColumn
cucsComputeBladeNumOfCores = _CucsComputeBladeNumOfCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 35),
    _CucsComputeBladeNumOfCores_Type()
)
cucsComputeBladeNumOfCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeNumOfCores.setStatus("current")
_CucsComputeBladeNumOfCpus_Type = Gauge32
_CucsComputeBladeNumOfCpus_Object = MibTableColumn
cucsComputeBladeNumOfCpus = _CucsComputeBladeNumOfCpus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 36),
    _CucsComputeBladeNumOfCpus_Type()
)
cucsComputeBladeNumOfCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeNumOfCpus.setStatus("current")
_CucsComputeBladeNumOfEthHostIfs_Type = Gauge32
_CucsComputeBladeNumOfEthHostIfs_Object = MibTableColumn
cucsComputeBladeNumOfEthHostIfs = _CucsComputeBladeNumOfEthHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 37),
    _CucsComputeBladeNumOfEthHostIfs_Type()
)
cucsComputeBladeNumOfEthHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeNumOfEthHostIfs.setStatus("current")
_CucsComputeBladeNumOfFcHostIfs_Type = Gauge32
_CucsComputeBladeNumOfFcHostIfs_Object = MibTableColumn
cucsComputeBladeNumOfFcHostIfs = _CucsComputeBladeNumOfFcHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 38),
    _CucsComputeBladeNumOfFcHostIfs_Type()
)
cucsComputeBladeNumOfFcHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeNumOfFcHostIfs.setStatus("current")
_CucsComputeBladeNumOfThreads_Type = Gauge32
_CucsComputeBladeNumOfThreads_Object = MibTableColumn
cucsComputeBladeNumOfThreads = _CucsComputeBladeNumOfThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 39),
    _CucsComputeBladeNumOfThreads_Type()
)
cucsComputeBladeNumOfThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeNumOfThreads.setStatus("current")
_CucsComputeBladeOperPower_Type = CucsEquipmentPowerState
_CucsComputeBladeOperPower_Object = MibTableColumn
cucsComputeBladeOperPower = _CucsComputeBladeOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 40),
    _CucsComputeBladeOperPower_Type()
)
cucsComputeBladeOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeOperPower.setStatus("current")
_CucsComputeBladeOperQualifier_Type = CucsComputeIssues
_CucsComputeBladeOperQualifier_Object = MibTableColumn
cucsComputeBladeOperQualifier = _CucsComputeBladeOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 41),
    _CucsComputeBladeOperQualifier_Type()
)
cucsComputeBladeOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeOperQualifier.setStatus("current")
_CucsComputeBladeOperState_Type = CucsLsOperState
_CucsComputeBladeOperState_Object = MibTableColumn
cucsComputeBladeOperState = _CucsComputeBladeOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 42),
    _CucsComputeBladeOperState_Type()
)
cucsComputeBladeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeOperState.setStatus("current")
_CucsComputeBladeOperability_Type = CucsEquipmentOperability
_CucsComputeBladeOperability_Object = MibTableColumn
cucsComputeBladeOperability = _CucsComputeBladeOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 43),
    _CucsComputeBladeOperability_Type()
)
cucsComputeBladeOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeOperability.setStatus("current")
_CucsComputeBladeOriginalUuid_Type = SnmpAdminString
_CucsComputeBladeOriginalUuid_Object = MibTableColumn
cucsComputeBladeOriginalUuid = _CucsComputeBladeOriginalUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 44),
    _CucsComputeBladeOriginalUuid_Type()
)
cucsComputeBladeOriginalUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeOriginalUuid.setStatus("current")
_CucsComputeBladePresence_Type = CucsEquipmentSlotStatus
_CucsComputeBladePresence_Object = MibTableColumn
cucsComputeBladePresence = _CucsComputeBladePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 45),
    _CucsComputeBladePresence_Type()
)
cucsComputeBladePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladePresence.setStatus("current")
_CucsComputeBladeRevision_Type = SnmpAdminString
_CucsComputeBladeRevision_Object = MibTableColumn
cucsComputeBladeRevision = _CucsComputeBladeRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 46),
    _CucsComputeBladeRevision_Type()
)
cucsComputeBladeRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeRevision.setStatus("current")
_CucsComputeBladeSerial_Type = SnmpAdminString
_CucsComputeBladeSerial_Object = MibTableColumn
cucsComputeBladeSerial = _CucsComputeBladeSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 47),
    _CucsComputeBladeSerial_Type()
)
cucsComputeBladeSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeSerial.setStatus("current")
_CucsComputeBladeServerId_Type = SnmpAdminString
_CucsComputeBladeServerId_Object = MibTableColumn
cucsComputeBladeServerId = _CucsComputeBladeServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 48),
    _CucsComputeBladeServerId_Type()
)
cucsComputeBladeServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeServerId.setStatus("current")
_CucsComputeBladeSlotId_Type = CucsComputeBladeSlotId
_CucsComputeBladeSlotId_Object = MibTableColumn
cucsComputeBladeSlotId = _CucsComputeBladeSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 49),
    _CucsComputeBladeSlotId_Type()
)
cucsComputeBladeSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeSlotId.setStatus("current")
_CucsComputeBladeTotalMemory_Type = Gauge32
_CucsComputeBladeTotalMemory_Object = MibTableColumn
cucsComputeBladeTotalMemory = _CucsComputeBladeTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 50),
    _CucsComputeBladeTotalMemory_Type()
)
cucsComputeBladeTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeTotalMemory.setStatus("current")
_CucsComputeBladeUsrLbl_Type = SnmpAdminString
_CucsComputeBladeUsrLbl_Object = MibTableColumn
cucsComputeBladeUsrLbl = _CucsComputeBladeUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 51),
    _CucsComputeBladeUsrLbl_Type()
)
cucsComputeBladeUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeUsrLbl.setStatus("current")
_CucsComputeBladeUuid_Type = SnmpAdminString
_CucsComputeBladeUuid_Object = MibTableColumn
cucsComputeBladeUuid = _CucsComputeBladeUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 52),
    _CucsComputeBladeUuid_Type()
)
cucsComputeBladeUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeUuid.setStatus("current")
_CucsComputeBladeVendor_Type = SnmpAdminString
_CucsComputeBladeVendor_Object = MibTableColumn
cucsComputeBladeVendor = _CucsComputeBladeVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 53),
    _CucsComputeBladeVendor_Type()
)
cucsComputeBladeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeVendor.setStatus("current")
_CucsComputeBladeNumOfCoresEnabled_Type = Gauge32
_CucsComputeBladeNumOfCoresEnabled_Object = MibTableColumn
cucsComputeBladeNumOfCoresEnabled = _CucsComputeBladeNumOfCoresEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 54),
    _CucsComputeBladeNumOfCoresEnabled_Type()
)
cucsComputeBladeNumOfCoresEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeNumOfCoresEnabled.setStatus("current")
_CucsComputeBladeLowVoltageMemory_Type = CucsComputePhysicalLowVoltageMemory
_CucsComputeBladeLowVoltageMemory_Object = MibTableColumn
cucsComputeBladeLowVoltageMemory = _CucsComputeBladeLowVoltageMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 55),
    _CucsComputeBladeLowVoltageMemory_Type()
)
cucsComputeBladeLowVoltageMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeLowVoltageMemory.setStatus("current")
_CucsComputeBladeMemorySpeed_Type = Gauge32
_CucsComputeBladeMemorySpeed_Object = MibTableColumn
cucsComputeBladeMemorySpeed = _CucsComputeBladeMemorySpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 56),
    _CucsComputeBladeMemorySpeed_Type()
)
cucsComputeBladeMemorySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeMemorySpeed.setStatus("current")
_CucsComputeBladeMfgTime_Type = DateAndTime
_CucsComputeBladeMfgTime_Object = MibTableColumn
cucsComputeBladeMfgTime = _CucsComputeBladeMfgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 57),
    _CucsComputeBladeMfgTime_Type()
)
cucsComputeBladeMfgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeMfgTime.setStatus("current")
_CucsComputeBladePartNumber_Type = SnmpAdminString
_CucsComputeBladePartNumber_Object = MibTableColumn
cucsComputeBladePartNumber = _CucsComputeBladePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 58),
    _CucsComputeBladePartNumber_Type()
)
cucsComputeBladePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladePartNumber.setStatus("current")
_CucsComputeBladeVid_Type = SnmpAdminString
_CucsComputeBladeVid_Object = MibTableColumn
cucsComputeBladeVid = _CucsComputeBladeVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 59),
    _CucsComputeBladeVid_Type()
)
cucsComputeBladeVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeVid.setStatus("current")
_CucsComputeBladePolicyLevel_Type = Gauge32
_CucsComputeBladePolicyLevel_Object = MibTableColumn
cucsComputeBladePolicyLevel = _CucsComputeBladePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 60),
    _CucsComputeBladePolicyLevel_Type()
)
cucsComputeBladePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladePolicyLevel.setStatus("current")
_CucsComputeBladePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeBladePolicyOwner_Object = MibTableColumn
cucsComputeBladePolicyOwner = _CucsComputeBladePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 61),
    _CucsComputeBladePolicyOwner_Type()
)
cucsComputeBladePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladePolicyOwner.setStatus("current")
_CucsComputeBladeLocalId_Type = SnmpAdminString
_CucsComputeBladeLocalId_Object = MibTableColumn
cucsComputeBladeLocalId = _CucsComputeBladeLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 62),
    _CucsComputeBladeLocalId_Type()
)
cucsComputeBladeLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeLocalId.setStatus("current")
_CucsComputeBladeScaledMode_Type = CucsComputeMode
_CucsComputeBladeScaledMode_Object = MibTableColumn
cucsComputeBladeScaledMode = _CucsComputeBladeScaledMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 63),
    _CucsComputeBladeScaledMode_Type()
)
cucsComputeBladeScaledMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeScaledMode.setStatus("current")
_CucsComputeBladeUpgradeScenario_Type = CucsComputeUpgradeStatus
_CucsComputeBladeUpgradeScenario_Object = MibTableColumn
cucsComputeBladeUpgradeScenario = _CucsComputeBladeUpgradeScenario_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 64),
    _CucsComputeBladeUpgradeScenario_Type()
)
cucsComputeBladeUpgradeScenario.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeUpgradeScenario.setStatus("current")
_CucsComputeBladeOperPwrTransSrc_Type = CucsComputePowerTransitionSrc
_CucsComputeBladeOperPwrTransSrc_Object = MibTableColumn
cucsComputeBladeOperPwrTransSrc = _CucsComputeBladeOperPwrTransSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 65),
    _CucsComputeBladeOperPwrTransSrc_Type()
)
cucsComputeBladeOperPwrTransSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeOperPwrTransSrc.setStatus("current")
_CucsComputeBladeDiscoveryStatus_Type = CucsEquipmentConnectionStatus
_CucsComputeBladeDiscoveryStatus_Object = MibTableColumn
cucsComputeBladeDiscoveryStatus = _CucsComputeBladeDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 66),
    _CucsComputeBladeDiscoveryStatus_Type()
)
cucsComputeBladeDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscoveryStatus.setStatus("current")
_CucsComputeBladeNumOf40GAdaptorsWithOldFw_Type = Gauge32
_CucsComputeBladeNumOf40GAdaptorsWithOldFw_Object = MibTableColumn
cucsComputeBladeNumOf40GAdaptorsWithOldFw = _CucsComputeBladeNumOf40GAdaptorsWithOldFw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 68),
    _CucsComputeBladeNumOf40GAdaptorsWithOldFw_Type()
)
cucsComputeBladeNumOf40GAdaptorsWithOldFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeNumOf40GAdaptorsWithOldFw.setStatus("current")
_CucsComputeBladeNumOf40GAdaptorsWithUnknownFw_Type = Gauge32
_CucsComputeBladeNumOf40GAdaptorsWithUnknownFw_Object = MibTableColumn
cucsComputeBladeNumOf40GAdaptorsWithUnknownFw = _CucsComputeBladeNumOf40GAdaptorsWithUnknownFw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 2, 1, 69),
    _CucsComputeBladeNumOf40GAdaptorsWithUnknownFw_Type()
)
cucsComputeBladeNumOf40GAdaptorsWithUnknownFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeNumOf40GAdaptorsWithUnknownFw.setStatus("current")
_CucsComputeBladeDiscPolicyTable_Object = MibTable
cucsComputeBladeDiscPolicyTable = _CucsComputeBladeDiscPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3)
)
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyTable.setStatus("current")
_CucsComputeBladeDiscPolicyEntry_Object = MibTableRow
cucsComputeBladeDiscPolicyEntry = _CucsComputeBladeDiscPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3, 1)
)
cucsComputeBladeDiscPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeBladeDiscPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyEntry.setStatus("current")
_CucsComputeBladeDiscPolicyInstanceId_Type = CucsManagedObjectId
_CucsComputeBladeDiscPolicyInstanceId_Object = MibTableColumn
cucsComputeBladeDiscPolicyInstanceId = _CucsComputeBladeDiscPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3, 1, 1),
    _CucsComputeBladeDiscPolicyInstanceId_Type()
)
cucsComputeBladeDiscPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyInstanceId.setStatus("current")
_CucsComputeBladeDiscPolicyDn_Type = CucsManagedObjectDn
_CucsComputeBladeDiscPolicyDn_Object = MibTableColumn
cucsComputeBladeDiscPolicyDn = _CucsComputeBladeDiscPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3, 1, 2),
    _CucsComputeBladeDiscPolicyDn_Type()
)
cucsComputeBladeDiscPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyDn.setStatus("current")
_CucsComputeBladeDiscPolicyRn_Type = SnmpAdminString
_CucsComputeBladeDiscPolicyRn_Object = MibTableColumn
cucsComputeBladeDiscPolicyRn = _CucsComputeBladeDiscPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3, 1, 3),
    _CucsComputeBladeDiscPolicyRn_Type()
)
cucsComputeBladeDiscPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyRn.setStatus("current")
_CucsComputeBladeDiscPolicyAction_Type = SnmpAdminString
_CucsComputeBladeDiscPolicyAction_Object = MibTableColumn
cucsComputeBladeDiscPolicyAction = _CucsComputeBladeDiscPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3, 1, 4),
    _CucsComputeBladeDiscPolicyAction_Type()
)
cucsComputeBladeDiscPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyAction.setStatus("current")
_CucsComputeBladeDiscPolicyDescr_Type = SnmpAdminString
_CucsComputeBladeDiscPolicyDescr_Object = MibTableColumn
cucsComputeBladeDiscPolicyDescr = _CucsComputeBladeDiscPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3, 1, 5),
    _CucsComputeBladeDiscPolicyDescr_Type()
)
cucsComputeBladeDiscPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyDescr.setStatus("current")
_CucsComputeBladeDiscPolicyIntId_Type = SnmpAdminString
_CucsComputeBladeDiscPolicyIntId_Object = MibTableColumn
cucsComputeBladeDiscPolicyIntId = _CucsComputeBladeDiscPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3, 1, 6),
    _CucsComputeBladeDiscPolicyIntId_Type()
)
cucsComputeBladeDiscPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyIntId.setStatus("current")
_CucsComputeBladeDiscPolicyName_Type = SnmpAdminString
_CucsComputeBladeDiscPolicyName_Object = MibTableColumn
cucsComputeBladeDiscPolicyName = _CucsComputeBladeDiscPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3, 1, 7),
    _CucsComputeBladeDiscPolicyName_Type()
)
cucsComputeBladeDiscPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyName.setStatus("current")
_CucsComputeBladeDiscPolicyQualifier_Type = SnmpAdminString
_CucsComputeBladeDiscPolicyQualifier_Object = MibTableColumn
cucsComputeBladeDiscPolicyQualifier = _CucsComputeBladeDiscPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3, 1, 8),
    _CucsComputeBladeDiscPolicyQualifier_Type()
)
cucsComputeBladeDiscPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyQualifier.setStatus("current")
_CucsComputeBladeDiscPolicyScrubPolicyName_Type = SnmpAdminString
_CucsComputeBladeDiscPolicyScrubPolicyName_Object = MibTableColumn
cucsComputeBladeDiscPolicyScrubPolicyName = _CucsComputeBladeDiscPolicyScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3, 1, 9),
    _CucsComputeBladeDiscPolicyScrubPolicyName_Type()
)
cucsComputeBladeDiscPolicyScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyScrubPolicyName.setStatus("current")
_CucsComputeBladeDiscPolicyPolicyLevel_Type = Gauge32
_CucsComputeBladeDiscPolicyPolicyLevel_Object = MibTableColumn
cucsComputeBladeDiscPolicyPolicyLevel = _CucsComputeBladeDiscPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3, 1, 10),
    _CucsComputeBladeDiscPolicyPolicyLevel_Type()
)
cucsComputeBladeDiscPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyPolicyLevel.setStatus("current")
_CucsComputeBladeDiscPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeBladeDiscPolicyPolicyOwner_Object = MibTableColumn
cucsComputeBladeDiscPolicyPolicyOwner = _CucsComputeBladeDiscPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 3, 1, 11),
    _CucsComputeBladeDiscPolicyPolicyOwner_Type()
)
cucsComputeBladeDiscPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeDiscPolicyPolicyOwner.setStatus("current")
_CucsComputeBladeFsmTaskTable_Object = MibTable
cucsComputeBladeFsmTaskTable = _CucsComputeBladeFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 4)
)
if mibBuilder.loadTexts:
    cucsComputeBladeFsmTaskTable.setStatus("current")
_CucsComputeBladeFsmTaskEntry_Object = MibTableRow
cucsComputeBladeFsmTaskEntry = _CucsComputeBladeFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 4, 1)
)
cucsComputeBladeFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeBladeFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeBladeFsmTaskEntry.setStatus("current")
_CucsComputeBladeFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsComputeBladeFsmTaskInstanceId_Object = MibTableColumn
cucsComputeBladeFsmTaskInstanceId = _CucsComputeBladeFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 4, 1, 1),
    _CucsComputeBladeFsmTaskInstanceId_Type()
)
cucsComputeBladeFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmTaskInstanceId.setStatus("current")
_CucsComputeBladeFsmTaskDn_Type = CucsManagedObjectDn
_CucsComputeBladeFsmTaskDn_Object = MibTableColumn
cucsComputeBladeFsmTaskDn = _CucsComputeBladeFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 4, 1, 2),
    _CucsComputeBladeFsmTaskDn_Type()
)
cucsComputeBladeFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmTaskDn.setStatus("current")
_CucsComputeBladeFsmTaskRn_Type = SnmpAdminString
_CucsComputeBladeFsmTaskRn_Object = MibTableColumn
cucsComputeBladeFsmTaskRn = _CucsComputeBladeFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 4, 1, 3),
    _CucsComputeBladeFsmTaskRn_Type()
)
cucsComputeBladeFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmTaskRn.setStatus("current")
_CucsComputeBladeFsmTaskCompletion_Type = CucsFsmCompletion
_CucsComputeBladeFsmTaskCompletion_Object = MibTableColumn
cucsComputeBladeFsmTaskCompletion = _CucsComputeBladeFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 4, 1, 4),
    _CucsComputeBladeFsmTaskCompletion_Type()
)
cucsComputeBladeFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmTaskCompletion.setStatus("current")
_CucsComputeBladeFsmTaskFlags_Type = CucsComputeBladeFsmTaskFlags
_CucsComputeBladeFsmTaskFlags_Object = MibTableColumn
cucsComputeBladeFsmTaskFlags = _CucsComputeBladeFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 4, 1, 5),
    _CucsComputeBladeFsmTaskFlags_Type()
)
cucsComputeBladeFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmTaskFlags.setStatus("current")
_CucsComputeBladeFsmTaskItem_Type = CucsComputeBladeFsmTaskItem
_CucsComputeBladeFsmTaskItem_Object = MibTableColumn
cucsComputeBladeFsmTaskItem = _CucsComputeBladeFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 4, 1, 6),
    _CucsComputeBladeFsmTaskItem_Type()
)
cucsComputeBladeFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmTaskItem.setStatus("current")
_CucsComputeBladeFsmTaskSeqId_Type = Gauge32
_CucsComputeBladeFsmTaskSeqId_Object = MibTableColumn
cucsComputeBladeFsmTaskSeqId = _CucsComputeBladeFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 4, 1, 7),
    _CucsComputeBladeFsmTaskSeqId_Type()
)
cucsComputeBladeFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmTaskSeqId.setStatus("current")
_CucsComputeBladeInheritPolicyTable_Object = MibTable
cucsComputeBladeInheritPolicyTable = _CucsComputeBladeInheritPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5)
)
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyTable.setStatus("current")
_CucsComputeBladeInheritPolicyEntry_Object = MibTableRow
cucsComputeBladeInheritPolicyEntry = _CucsComputeBladeInheritPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5, 1)
)
cucsComputeBladeInheritPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeBladeInheritPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyEntry.setStatus("current")
_CucsComputeBladeInheritPolicyInstanceId_Type = CucsManagedObjectId
_CucsComputeBladeInheritPolicyInstanceId_Object = MibTableColumn
cucsComputeBladeInheritPolicyInstanceId = _CucsComputeBladeInheritPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5, 1, 1),
    _CucsComputeBladeInheritPolicyInstanceId_Type()
)
cucsComputeBladeInheritPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyInstanceId.setStatus("current")
_CucsComputeBladeInheritPolicyDn_Type = CucsManagedObjectDn
_CucsComputeBladeInheritPolicyDn_Object = MibTableColumn
cucsComputeBladeInheritPolicyDn = _CucsComputeBladeInheritPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5, 1, 2),
    _CucsComputeBladeInheritPolicyDn_Type()
)
cucsComputeBladeInheritPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyDn.setStatus("current")
_CucsComputeBladeInheritPolicyRn_Type = SnmpAdminString
_CucsComputeBladeInheritPolicyRn_Object = MibTableColumn
cucsComputeBladeInheritPolicyRn = _CucsComputeBladeInheritPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5, 1, 3),
    _CucsComputeBladeInheritPolicyRn_Type()
)
cucsComputeBladeInheritPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyRn.setStatus("current")
_CucsComputeBladeInheritPolicyDescr_Type = SnmpAdminString
_CucsComputeBladeInheritPolicyDescr_Object = MibTableColumn
cucsComputeBladeInheritPolicyDescr = _CucsComputeBladeInheritPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5, 1, 4),
    _CucsComputeBladeInheritPolicyDescr_Type()
)
cucsComputeBladeInheritPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyDescr.setStatus("current")
_CucsComputeBladeInheritPolicyDstDn_Type = SnmpAdminString
_CucsComputeBladeInheritPolicyDstDn_Object = MibTableColumn
cucsComputeBladeInheritPolicyDstDn = _CucsComputeBladeInheritPolicyDstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5, 1, 5),
    _CucsComputeBladeInheritPolicyDstDn_Type()
)
cucsComputeBladeInheritPolicyDstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyDstDn.setStatus("current")
_CucsComputeBladeInheritPolicyIntId_Type = SnmpAdminString
_CucsComputeBladeInheritPolicyIntId_Object = MibTableColumn
cucsComputeBladeInheritPolicyIntId = _CucsComputeBladeInheritPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5, 1, 6),
    _CucsComputeBladeInheritPolicyIntId_Type()
)
cucsComputeBladeInheritPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyIntId.setStatus("current")
_CucsComputeBladeInheritPolicyName_Type = SnmpAdminString
_CucsComputeBladeInheritPolicyName_Object = MibTableColumn
cucsComputeBladeInheritPolicyName = _CucsComputeBladeInheritPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5, 1, 7),
    _CucsComputeBladeInheritPolicyName_Type()
)
cucsComputeBladeInheritPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyName.setStatus("current")
_CucsComputeBladeInheritPolicyQualifier_Type = SnmpAdminString
_CucsComputeBladeInheritPolicyQualifier_Object = MibTableColumn
cucsComputeBladeInheritPolicyQualifier = _CucsComputeBladeInheritPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5, 1, 8),
    _CucsComputeBladeInheritPolicyQualifier_Type()
)
cucsComputeBladeInheritPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyQualifier.setStatus("current")
_CucsComputeBladeInheritPolicyPolicyLevel_Type = Gauge32
_CucsComputeBladeInheritPolicyPolicyLevel_Object = MibTableColumn
cucsComputeBladeInheritPolicyPolicyLevel = _CucsComputeBladeInheritPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5, 1, 9),
    _CucsComputeBladeInheritPolicyPolicyLevel_Type()
)
cucsComputeBladeInheritPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyPolicyLevel.setStatus("current")
_CucsComputeBladeInheritPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeBladeInheritPolicyPolicyOwner_Object = MibTableColumn
cucsComputeBladeInheritPolicyPolicyOwner = _CucsComputeBladeInheritPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5, 1, 10),
    _CucsComputeBladeInheritPolicyPolicyOwner_Type()
)
cucsComputeBladeInheritPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyPolicyOwner.setStatus("current")
_CucsComputeBladeInheritPolicyOperQualifier_Type = SnmpAdminString
_CucsComputeBladeInheritPolicyOperQualifier_Object = MibTableColumn
cucsComputeBladeInheritPolicyOperQualifier = _CucsComputeBladeInheritPolicyOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 5, 1, 11),
    _CucsComputeBladeInheritPolicyOperQualifier_Type()
)
cucsComputeBladeInheritPolicyOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeInheritPolicyOperQualifier.setStatus("current")
_CucsComputeBoardTable_Object = MibTable
cucsComputeBoardTable = _CucsComputeBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6)
)
if mibBuilder.loadTexts:
    cucsComputeBoardTable.setStatus("current")
_CucsComputeBoardEntry_Object = MibTableRow
cucsComputeBoardEntry = _CucsComputeBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1)
)
cucsComputeBoardEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeBoardInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeBoardEntry.setStatus("current")
_CucsComputeBoardInstanceId_Type = CucsManagedObjectId
_CucsComputeBoardInstanceId_Object = MibTableColumn
cucsComputeBoardInstanceId = _CucsComputeBoardInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 1),
    _CucsComputeBoardInstanceId_Type()
)
cucsComputeBoardInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeBoardInstanceId.setStatus("current")
_CucsComputeBoardDn_Type = CucsManagedObjectDn
_CucsComputeBoardDn_Object = MibTableColumn
cucsComputeBoardDn = _CucsComputeBoardDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 2),
    _CucsComputeBoardDn_Type()
)
cucsComputeBoardDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardDn.setStatus("current")
_CucsComputeBoardRn_Type = SnmpAdminString
_CucsComputeBoardRn_Object = MibTableColumn
cucsComputeBoardRn = _CucsComputeBoardRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 3),
    _CucsComputeBoardRn_Type()
)
cucsComputeBoardRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardRn.setStatus("current")
_CucsComputeBoardCmosVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeBoardCmosVoltage_Object = MibTableColumn
cucsComputeBoardCmosVoltage = _CucsComputeBoardCmosVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 4),
    _CucsComputeBoardCmosVoltage_Type()
)
cucsComputeBoardCmosVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardCmosVoltage.setStatus("current")
_CucsComputeBoardId_Type = Gauge32
_CucsComputeBoardId_Object = MibTableColumn
cucsComputeBoardId = _CucsComputeBoardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 5),
    _CucsComputeBoardId_Type()
)
cucsComputeBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardId.setStatus("current")
_CucsComputeBoardModel_Type = SnmpAdminString
_CucsComputeBoardModel_Object = MibTableColumn
cucsComputeBoardModel = _CucsComputeBoardModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 6),
    _CucsComputeBoardModel_Type()
)
cucsComputeBoardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardModel.setStatus("current")
_CucsComputeBoardOperPower_Type = CucsEquipmentPowerState
_CucsComputeBoardOperPower_Object = MibTableColumn
cucsComputeBoardOperPower = _CucsComputeBoardOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 7),
    _CucsComputeBoardOperPower_Type()
)
cucsComputeBoardOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardOperPower.setStatus("current")
_CucsComputeBoardOperState_Type = CucsEquipmentOperability
_CucsComputeBoardOperState_Object = MibTableColumn
cucsComputeBoardOperState = _CucsComputeBoardOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 8),
    _CucsComputeBoardOperState_Type()
)
cucsComputeBoardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardOperState.setStatus("current")
_CucsComputeBoardOperability_Type = CucsEquipmentOperability
_CucsComputeBoardOperability_Object = MibTableColumn
cucsComputeBoardOperability = _CucsComputeBoardOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 9),
    _CucsComputeBoardOperability_Type()
)
cucsComputeBoardOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardOperability.setStatus("current")
_CucsComputeBoardPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeBoardPerf_Object = MibTableColumn
cucsComputeBoardPerf = _CucsComputeBoardPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 10),
    _CucsComputeBoardPerf_Type()
)
cucsComputeBoardPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardPerf.setStatus("current")
_CucsComputeBoardPower_Type = CucsComputeABoardPower
_CucsComputeBoardPower_Object = MibTableColumn
cucsComputeBoardPower = _CucsComputeBoardPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 11),
    _CucsComputeBoardPower_Type()
)
cucsComputeBoardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardPower.setStatus("current")
_CucsComputeBoardPresence_Type = CucsEquipmentPresence
_CucsComputeBoardPresence_Object = MibTableColumn
cucsComputeBoardPresence = _CucsComputeBoardPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 12),
    _CucsComputeBoardPresence_Type()
)
cucsComputeBoardPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardPresence.setStatus("current")
_CucsComputeBoardRevision_Type = SnmpAdminString
_CucsComputeBoardRevision_Object = MibTableColumn
cucsComputeBoardRevision = _CucsComputeBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 13),
    _CucsComputeBoardRevision_Type()
)
cucsComputeBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardRevision.setStatus("current")
_CucsComputeBoardSerial_Type = SnmpAdminString
_CucsComputeBoardSerial_Object = MibTableColumn
cucsComputeBoardSerial = _CucsComputeBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 14),
    _CucsComputeBoardSerial_Type()
)
cucsComputeBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardSerial.setStatus("current")
_CucsComputeBoardThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeBoardThermal_Object = MibTableColumn
cucsComputeBoardThermal = _CucsComputeBoardThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 15),
    _CucsComputeBoardThermal_Type()
)
cucsComputeBoardThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardThermal.setStatus("current")
_CucsComputeBoardVendor_Type = SnmpAdminString
_CucsComputeBoardVendor_Object = MibTableColumn
cucsComputeBoardVendor = _CucsComputeBoardVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 16),
    _CucsComputeBoardVendor_Type()
)
cucsComputeBoardVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardVendor.setStatus("current")
_CucsComputeBoardVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeBoardVoltage_Object = MibTableColumn
cucsComputeBoardVoltage = _CucsComputeBoardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 17),
    _CucsComputeBoardVoltage_Type()
)
cucsComputeBoardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardVoltage.setStatus("current")
_CucsComputeBoardOperQualifierReason_Type = SnmpAdminString
_CucsComputeBoardOperQualifierReason_Object = MibTableColumn
cucsComputeBoardOperQualifierReason = _CucsComputeBoardOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 18),
    _CucsComputeBoardOperQualifierReason_Type()
)
cucsComputeBoardOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardOperQualifierReason.setStatus("current")
_CucsComputeBoardPowerUsage_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeBoardPowerUsage_Object = MibTableColumn
cucsComputeBoardPowerUsage = _CucsComputeBoardPowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 19),
    _CucsComputeBoardPowerUsage_Type()
)
cucsComputeBoardPowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardPowerUsage.setStatus("current")
_CucsComputeBoardFaultQualifier_Type = SnmpAdminString
_CucsComputeBoardFaultQualifier_Object = MibTableColumn
cucsComputeBoardFaultQualifier = _CucsComputeBoardFaultQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 20),
    _CucsComputeBoardFaultQualifier_Type()
)
cucsComputeBoardFaultQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardFaultQualifier.setStatus("current")
_CucsComputeBoardLocationDn_Type = SnmpAdminString
_CucsComputeBoardLocationDn_Object = MibTableColumn
cucsComputeBoardLocationDn = _CucsComputeBoardLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 21),
    _CucsComputeBoardLocationDn_Type()
)
cucsComputeBoardLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardLocationDn.setStatus("current")
_CucsComputeBoardCpuTypeDescription_Type = SnmpAdminString
_CucsComputeBoardCpuTypeDescription_Object = MibTableColumn
cucsComputeBoardCpuTypeDescription = _CucsComputeBoardCpuTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 6, 1, 23),
    _CucsComputeBoardCpuTypeDescription_Type()
)
cucsComputeBoardCpuTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardCpuTypeDescription.setStatus("current")
_CucsComputeBoardControllerTable_Object = MibTable
cucsComputeBoardControllerTable = _CucsComputeBoardControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7)
)
if mibBuilder.loadTexts:
    cucsComputeBoardControllerTable.setStatus("current")
_CucsComputeBoardControllerEntry_Object = MibTableRow
cucsComputeBoardControllerEntry = _CucsComputeBoardControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1)
)
cucsComputeBoardControllerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeBoardControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeBoardControllerEntry.setStatus("current")
_CucsComputeBoardControllerInstanceId_Type = CucsManagedObjectId
_CucsComputeBoardControllerInstanceId_Object = MibTableColumn
cucsComputeBoardControllerInstanceId = _CucsComputeBoardControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 1),
    _CucsComputeBoardControllerInstanceId_Type()
)
cucsComputeBoardControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerInstanceId.setStatus("current")
_CucsComputeBoardControllerDn_Type = CucsManagedObjectDn
_CucsComputeBoardControllerDn_Object = MibTableColumn
cucsComputeBoardControllerDn = _CucsComputeBoardControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 2),
    _CucsComputeBoardControllerDn_Type()
)
cucsComputeBoardControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerDn.setStatus("current")
_CucsComputeBoardControllerRn_Type = SnmpAdminString
_CucsComputeBoardControllerRn_Object = MibTableColumn
cucsComputeBoardControllerRn = _CucsComputeBoardControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 3),
    _CucsComputeBoardControllerRn_Type()
)
cucsComputeBoardControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerRn.setStatus("current")
_CucsComputeBoardControllerId_Type = Gauge32
_CucsComputeBoardControllerId_Object = MibTableColumn
cucsComputeBoardControllerId = _CucsComputeBoardControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 4),
    _CucsComputeBoardControllerId_Type()
)
cucsComputeBoardControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerId.setStatus("current")
_CucsComputeBoardControllerModel_Type = SnmpAdminString
_CucsComputeBoardControllerModel_Object = MibTableColumn
cucsComputeBoardControllerModel = _CucsComputeBoardControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 5),
    _CucsComputeBoardControllerModel_Type()
)
cucsComputeBoardControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerModel.setStatus("current")
_CucsComputeBoardControllerOperState_Type = CucsEquipmentOperability
_CucsComputeBoardControllerOperState_Object = MibTableColumn
cucsComputeBoardControllerOperState = _CucsComputeBoardControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 6),
    _CucsComputeBoardControllerOperState_Type()
)
cucsComputeBoardControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerOperState.setStatus("current")
_CucsComputeBoardControllerOperability_Type = CucsEquipmentOperability
_CucsComputeBoardControllerOperability_Object = MibTableColumn
cucsComputeBoardControllerOperability = _CucsComputeBoardControllerOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 7),
    _CucsComputeBoardControllerOperability_Type()
)
cucsComputeBoardControllerOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerOperability.setStatus("current")
_CucsComputeBoardControllerPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeBoardControllerPerf_Object = MibTableColumn
cucsComputeBoardControllerPerf = _CucsComputeBoardControllerPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 8),
    _CucsComputeBoardControllerPerf_Type()
)
cucsComputeBoardControllerPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerPerf.setStatus("current")
_CucsComputeBoardControllerPower_Type = CucsEquipmentPowerState
_CucsComputeBoardControllerPower_Object = MibTableColumn
cucsComputeBoardControllerPower = _CucsComputeBoardControllerPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 9),
    _CucsComputeBoardControllerPower_Type()
)
cucsComputeBoardControllerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerPower.setStatus("current")
_CucsComputeBoardControllerPresence_Type = CucsEquipmentPresence
_CucsComputeBoardControllerPresence_Object = MibTableColumn
cucsComputeBoardControllerPresence = _CucsComputeBoardControllerPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 10),
    _CucsComputeBoardControllerPresence_Type()
)
cucsComputeBoardControllerPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerPresence.setStatus("current")
_CucsComputeBoardControllerRevision_Type = SnmpAdminString
_CucsComputeBoardControllerRevision_Object = MibTableColumn
cucsComputeBoardControllerRevision = _CucsComputeBoardControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 11),
    _CucsComputeBoardControllerRevision_Type()
)
cucsComputeBoardControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerRevision.setStatus("current")
_CucsComputeBoardControllerSerial_Type = SnmpAdminString
_CucsComputeBoardControllerSerial_Object = MibTableColumn
cucsComputeBoardControllerSerial = _CucsComputeBoardControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 12),
    _CucsComputeBoardControllerSerial_Type()
)
cucsComputeBoardControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerSerial.setStatus("current")
_CucsComputeBoardControllerThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeBoardControllerThermal_Object = MibTableColumn
cucsComputeBoardControllerThermal = _CucsComputeBoardControllerThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 13),
    _CucsComputeBoardControllerThermal_Type()
)
cucsComputeBoardControllerThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerThermal.setStatus("current")
_CucsComputeBoardControllerVendor_Type = SnmpAdminString
_CucsComputeBoardControllerVendor_Object = MibTableColumn
cucsComputeBoardControllerVendor = _CucsComputeBoardControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 14),
    _CucsComputeBoardControllerVendor_Type()
)
cucsComputeBoardControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerVendor.setStatus("current")
_CucsComputeBoardControllerVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeBoardControllerVoltage_Object = MibTableColumn
cucsComputeBoardControllerVoltage = _CucsComputeBoardControllerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 15),
    _CucsComputeBoardControllerVoltage_Type()
)
cucsComputeBoardControllerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerVoltage.setStatus("current")
_CucsComputeBoardControllerOperQualifierReason_Type = SnmpAdminString
_CucsComputeBoardControllerOperQualifierReason_Object = MibTableColumn
cucsComputeBoardControllerOperQualifierReason = _CucsComputeBoardControllerOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 16),
    _CucsComputeBoardControllerOperQualifierReason_Type()
)
cucsComputeBoardControllerOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerOperQualifierReason.setStatus("current")
_CucsComputeBoardControllerLocationDn_Type = SnmpAdminString
_CucsComputeBoardControllerLocationDn_Object = MibTableColumn
cucsComputeBoardControllerLocationDn = _CucsComputeBoardControllerLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 7, 1, 17),
    _CucsComputeBoardControllerLocationDn_Type()
)
cucsComputeBoardControllerLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardControllerLocationDn.setStatus("current")
_CucsComputeChassisDiscPolicyTable_Object = MibTable
cucsComputeChassisDiscPolicyTable = _CucsComputeChassisDiscPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8)
)
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyTable.setStatus("current")
_CucsComputeChassisDiscPolicyEntry_Object = MibTableRow
cucsComputeChassisDiscPolicyEntry = _CucsComputeChassisDiscPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1)
)
cucsComputeChassisDiscPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeChassisDiscPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyEntry.setStatus("current")
_CucsComputeChassisDiscPolicyInstanceId_Type = CucsManagedObjectId
_CucsComputeChassisDiscPolicyInstanceId_Object = MibTableColumn
cucsComputeChassisDiscPolicyInstanceId = _CucsComputeChassisDiscPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 1),
    _CucsComputeChassisDiscPolicyInstanceId_Type()
)
cucsComputeChassisDiscPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyInstanceId.setStatus("current")
_CucsComputeChassisDiscPolicyDn_Type = CucsManagedObjectDn
_CucsComputeChassisDiscPolicyDn_Object = MibTableColumn
cucsComputeChassisDiscPolicyDn = _CucsComputeChassisDiscPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 2),
    _CucsComputeChassisDiscPolicyDn_Type()
)
cucsComputeChassisDiscPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyDn.setStatus("current")
_CucsComputeChassisDiscPolicyRn_Type = SnmpAdminString
_CucsComputeChassisDiscPolicyRn_Object = MibTableColumn
cucsComputeChassisDiscPolicyRn = _CucsComputeChassisDiscPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 3),
    _CucsComputeChassisDiscPolicyRn_Type()
)
cucsComputeChassisDiscPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyRn.setStatus("current")
_CucsComputeChassisDiscPolicyAction_Type = CucsComputeChassisDiscAction
_CucsComputeChassisDiscPolicyAction_Object = MibTableColumn
cucsComputeChassisDiscPolicyAction = _CucsComputeChassisDiscPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 4),
    _CucsComputeChassisDiscPolicyAction_Type()
)
cucsComputeChassisDiscPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyAction.setStatus("current")
_CucsComputeChassisDiscPolicyDescr_Type = SnmpAdminString
_CucsComputeChassisDiscPolicyDescr_Object = MibTableColumn
cucsComputeChassisDiscPolicyDescr = _CucsComputeChassisDiscPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 5),
    _CucsComputeChassisDiscPolicyDescr_Type()
)
cucsComputeChassisDiscPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyDescr.setStatus("current")
_CucsComputeChassisDiscPolicyIntId_Type = SnmpAdminString
_CucsComputeChassisDiscPolicyIntId_Object = MibTableColumn
cucsComputeChassisDiscPolicyIntId = _CucsComputeChassisDiscPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 6),
    _CucsComputeChassisDiscPolicyIntId_Type()
)
cucsComputeChassisDiscPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyIntId.setStatus("current")
_CucsComputeChassisDiscPolicyName_Type = SnmpAdminString
_CucsComputeChassisDiscPolicyName_Object = MibTableColumn
cucsComputeChassisDiscPolicyName = _CucsComputeChassisDiscPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 7),
    _CucsComputeChassisDiscPolicyName_Type()
)
cucsComputeChassisDiscPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyName.setStatus("current")
_CucsComputeChassisDiscPolicyQualifier_Type = SnmpAdminString
_CucsComputeChassisDiscPolicyQualifier_Object = MibTableColumn
cucsComputeChassisDiscPolicyQualifier = _CucsComputeChassisDiscPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 8),
    _CucsComputeChassisDiscPolicyQualifier_Type()
)
cucsComputeChassisDiscPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyQualifier.setStatus("current")
_CucsComputeChassisDiscPolicyRebalance_Type = CucsComputeConnectivityRebalancing
_CucsComputeChassisDiscPolicyRebalance_Object = MibTableColumn
cucsComputeChassisDiscPolicyRebalance = _CucsComputeChassisDiscPolicyRebalance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 9),
    _CucsComputeChassisDiscPolicyRebalance_Type()
)
cucsComputeChassisDiscPolicyRebalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyRebalance.setStatus("current")
_CucsComputeChassisDiscPolicyLinkAggregationPref_Type = CucsComputeLinkAggregation
_CucsComputeChassisDiscPolicyLinkAggregationPref_Object = MibTableColumn
cucsComputeChassisDiscPolicyLinkAggregationPref = _CucsComputeChassisDiscPolicyLinkAggregationPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 10),
    _CucsComputeChassisDiscPolicyLinkAggregationPref_Type()
)
cucsComputeChassisDiscPolicyLinkAggregationPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyLinkAggregationPref.setStatus("current")
_CucsComputeChassisDiscPolicyPolicyLevel_Type = Gauge32
_CucsComputeChassisDiscPolicyPolicyLevel_Object = MibTableColumn
cucsComputeChassisDiscPolicyPolicyLevel = _CucsComputeChassisDiscPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 11),
    _CucsComputeChassisDiscPolicyPolicyLevel_Type()
)
cucsComputeChassisDiscPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyPolicyLevel.setStatus("current")
_CucsComputeChassisDiscPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeChassisDiscPolicyPolicyOwner_Object = MibTableColumn
cucsComputeChassisDiscPolicyPolicyOwner = _CucsComputeChassisDiscPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 12),
    _CucsComputeChassisDiscPolicyPolicyOwner_Type()
)
cucsComputeChassisDiscPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyPolicyOwner.setStatus("current")
_CucsComputeChassisDiscPolicyMulticastHwHash_Type = CucsComputeChassisDiscPolicyMulticastHwHash
_CucsComputeChassisDiscPolicyMulticastHwHash_Object = MibTableColumn
cucsComputeChassisDiscPolicyMulticastHwHash = _CucsComputeChassisDiscPolicyMulticastHwHash_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 8, 1, 13),
    _CucsComputeChassisDiscPolicyMulticastHwHash_Type()
)
cucsComputeChassisDiscPolicyMulticastHwHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisDiscPolicyMulticastHwHash.setStatus("current")
_CucsComputeChassisQualTable_Object = MibTable
cucsComputeChassisQualTable = _CucsComputeChassisQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 9)
)
if mibBuilder.loadTexts:
    cucsComputeChassisQualTable.setStatus("current")
_CucsComputeChassisQualEntry_Object = MibTableRow
cucsComputeChassisQualEntry = _CucsComputeChassisQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 9, 1)
)
cucsComputeChassisQualEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeChassisQualInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeChassisQualEntry.setStatus("current")
_CucsComputeChassisQualInstanceId_Type = CucsManagedObjectId
_CucsComputeChassisQualInstanceId_Object = MibTableColumn
cucsComputeChassisQualInstanceId = _CucsComputeChassisQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 9, 1, 1),
    _CucsComputeChassisQualInstanceId_Type()
)
cucsComputeChassisQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeChassisQualInstanceId.setStatus("current")
_CucsComputeChassisQualDn_Type = CucsManagedObjectDn
_CucsComputeChassisQualDn_Object = MibTableColumn
cucsComputeChassisQualDn = _CucsComputeChassisQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 9, 1, 2),
    _CucsComputeChassisQualDn_Type()
)
cucsComputeChassisQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisQualDn.setStatus("current")
_CucsComputeChassisQualRn_Type = SnmpAdminString
_CucsComputeChassisQualRn_Object = MibTableColumn
cucsComputeChassisQualRn = _CucsComputeChassisQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 9, 1, 3),
    _CucsComputeChassisQualRn_Type()
)
cucsComputeChassisQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisQualRn.setStatus("current")
_CucsComputeChassisQualMaxId_Type = CucsComputeChassisQualMaxId
_CucsComputeChassisQualMaxId_Object = MibTableColumn
cucsComputeChassisQualMaxId = _CucsComputeChassisQualMaxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 9, 1, 4),
    _CucsComputeChassisQualMaxId_Type()
)
cucsComputeChassisQualMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisQualMaxId.setStatus("current")
_CucsComputeChassisQualMinId_Type = CucsComputeChassisQualMinId
_CucsComputeChassisQualMinId_Object = MibTableColumn
cucsComputeChassisQualMinId = _CucsComputeChassisQualMinId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 9, 1, 5),
    _CucsComputeChassisQualMinId_Type()
)
cucsComputeChassisQualMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisQualMinId.setStatus("current")
_CucsComputeDefaultsTable_Object = MibTable
cucsComputeDefaultsTable = _CucsComputeDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 10)
)
if mibBuilder.loadTexts:
    cucsComputeDefaultsTable.setStatus("current")
_CucsComputeDefaultsEntry_Object = MibTableRow
cucsComputeDefaultsEntry = _CucsComputeDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 10, 1)
)
cucsComputeDefaultsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeDefaultsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeDefaultsEntry.setStatus("current")
_CucsComputeDefaultsInstanceId_Type = CucsManagedObjectId
_CucsComputeDefaultsInstanceId_Object = MibTableColumn
cucsComputeDefaultsInstanceId = _CucsComputeDefaultsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 10, 1, 1),
    _CucsComputeDefaultsInstanceId_Type()
)
cucsComputeDefaultsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeDefaultsInstanceId.setStatus("current")
_CucsComputeDefaultsDn_Type = CucsManagedObjectDn
_CucsComputeDefaultsDn_Object = MibTableColumn
cucsComputeDefaultsDn = _CucsComputeDefaultsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 10, 1, 2),
    _CucsComputeDefaultsDn_Type()
)
cucsComputeDefaultsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeDefaultsDn.setStatus("current")
_CucsComputeDefaultsRn_Type = SnmpAdminString
_CucsComputeDefaultsRn_Object = MibTableColumn
cucsComputeDefaultsRn = _CucsComputeDefaultsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 10, 1, 3),
    _CucsComputeDefaultsRn_Type()
)
cucsComputeDefaultsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeDefaultsRn.setStatus("current")
_CucsComputeIOHubTable_Object = MibTable
cucsComputeIOHubTable = _CucsComputeIOHubTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11)
)
if mibBuilder.loadTexts:
    cucsComputeIOHubTable.setStatus("current")
_CucsComputeIOHubEntry_Object = MibTableRow
cucsComputeIOHubEntry = _CucsComputeIOHubEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1)
)
cucsComputeIOHubEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeIOHubInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeIOHubEntry.setStatus("current")
_CucsComputeIOHubInstanceId_Type = CucsManagedObjectId
_CucsComputeIOHubInstanceId_Object = MibTableColumn
cucsComputeIOHubInstanceId = _CucsComputeIOHubInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 1),
    _CucsComputeIOHubInstanceId_Type()
)
cucsComputeIOHubInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeIOHubInstanceId.setStatus("current")
_CucsComputeIOHubDn_Type = CucsManagedObjectDn
_CucsComputeIOHubDn_Object = MibTableColumn
cucsComputeIOHubDn = _CucsComputeIOHubDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 2),
    _CucsComputeIOHubDn_Type()
)
cucsComputeIOHubDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubDn.setStatus("current")
_CucsComputeIOHubRn_Type = SnmpAdminString
_CucsComputeIOHubRn_Object = MibTableColumn
cucsComputeIOHubRn = _CucsComputeIOHubRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 3),
    _CucsComputeIOHubRn_Type()
)
cucsComputeIOHubRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubRn.setStatus("current")
_CucsComputeIOHubId_Type = Gauge32
_CucsComputeIOHubId_Object = MibTableColumn
cucsComputeIOHubId = _CucsComputeIOHubId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 4),
    _CucsComputeIOHubId_Type()
)
cucsComputeIOHubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubId.setStatus("current")
_CucsComputeIOHubModel_Type = SnmpAdminString
_CucsComputeIOHubModel_Object = MibTableColumn
cucsComputeIOHubModel = _CucsComputeIOHubModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 5),
    _CucsComputeIOHubModel_Type()
)
cucsComputeIOHubModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubModel.setStatus("current")
_CucsComputeIOHubOperState_Type = CucsEquipmentOperability
_CucsComputeIOHubOperState_Object = MibTableColumn
cucsComputeIOHubOperState = _CucsComputeIOHubOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 6),
    _CucsComputeIOHubOperState_Type()
)
cucsComputeIOHubOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubOperState.setStatus("current")
_CucsComputeIOHubOperability_Type = CucsEquipmentOperability
_CucsComputeIOHubOperability_Object = MibTableColumn
cucsComputeIOHubOperability = _CucsComputeIOHubOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 7),
    _CucsComputeIOHubOperability_Type()
)
cucsComputeIOHubOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubOperability.setStatus("current")
_CucsComputeIOHubPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeIOHubPerf_Object = MibTableColumn
cucsComputeIOHubPerf = _CucsComputeIOHubPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 8),
    _CucsComputeIOHubPerf_Type()
)
cucsComputeIOHubPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubPerf.setStatus("current")
_CucsComputeIOHubPower_Type = CucsEquipmentPowerState
_CucsComputeIOHubPower_Object = MibTableColumn
cucsComputeIOHubPower = _CucsComputeIOHubPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 9),
    _CucsComputeIOHubPower_Type()
)
cucsComputeIOHubPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubPower.setStatus("current")
_CucsComputeIOHubPresence_Type = CucsEquipmentPresence
_CucsComputeIOHubPresence_Object = MibTableColumn
cucsComputeIOHubPresence = _CucsComputeIOHubPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 10),
    _CucsComputeIOHubPresence_Type()
)
cucsComputeIOHubPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubPresence.setStatus("current")
_CucsComputeIOHubRevision_Type = SnmpAdminString
_CucsComputeIOHubRevision_Object = MibTableColumn
cucsComputeIOHubRevision = _CucsComputeIOHubRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 11),
    _CucsComputeIOHubRevision_Type()
)
cucsComputeIOHubRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubRevision.setStatus("current")
_CucsComputeIOHubSerial_Type = SnmpAdminString
_CucsComputeIOHubSerial_Object = MibTableColumn
cucsComputeIOHubSerial = _CucsComputeIOHubSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 12),
    _CucsComputeIOHubSerial_Type()
)
cucsComputeIOHubSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubSerial.setStatus("current")
_CucsComputeIOHubThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeIOHubThermal_Object = MibTableColumn
cucsComputeIOHubThermal = _CucsComputeIOHubThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 13),
    _CucsComputeIOHubThermal_Type()
)
cucsComputeIOHubThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubThermal.setStatus("current")
_CucsComputeIOHubVendor_Type = SnmpAdminString
_CucsComputeIOHubVendor_Object = MibTableColumn
cucsComputeIOHubVendor = _CucsComputeIOHubVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 14),
    _CucsComputeIOHubVendor_Type()
)
cucsComputeIOHubVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubVendor.setStatus("current")
_CucsComputeIOHubVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeIOHubVoltage_Object = MibTableColumn
cucsComputeIOHubVoltage = _CucsComputeIOHubVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 15),
    _CucsComputeIOHubVoltage_Type()
)
cucsComputeIOHubVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubVoltage.setStatus("current")
_CucsComputeIOHubOperQualifierReason_Type = SnmpAdminString
_CucsComputeIOHubOperQualifierReason_Object = MibTableColumn
cucsComputeIOHubOperQualifierReason = _CucsComputeIOHubOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 16),
    _CucsComputeIOHubOperQualifierReason_Type()
)
cucsComputeIOHubOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubOperQualifierReason.setStatus("current")
_CucsComputeIOHubLocationDn_Type = SnmpAdminString
_CucsComputeIOHubLocationDn_Object = MibTableColumn
cucsComputeIOHubLocationDn = _CucsComputeIOHubLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 11, 1, 17),
    _CucsComputeIOHubLocationDn_Type()
)
cucsComputeIOHubLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubLocationDn.setStatus("current")
_CucsComputeIOHubEnvStatsTable_Object = MibTable
cucsComputeIOHubEnvStatsTable = _CucsComputeIOHubEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12)
)
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsTable.setStatus("current")
_CucsComputeIOHubEnvStatsEntry_Object = MibTableRow
cucsComputeIOHubEnvStatsEntry = _CucsComputeIOHubEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1)
)
cucsComputeIOHubEnvStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeIOHubEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsEntry.setStatus("current")
_CucsComputeIOHubEnvStatsInstanceId_Type = CucsManagedObjectId
_CucsComputeIOHubEnvStatsInstanceId_Object = MibTableColumn
cucsComputeIOHubEnvStatsInstanceId = _CucsComputeIOHubEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1, 1),
    _CucsComputeIOHubEnvStatsInstanceId_Type()
)
cucsComputeIOHubEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsInstanceId.setStatus("current")
_CucsComputeIOHubEnvStatsDn_Type = CucsManagedObjectDn
_CucsComputeIOHubEnvStatsDn_Object = MibTableColumn
cucsComputeIOHubEnvStatsDn = _CucsComputeIOHubEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1, 2),
    _CucsComputeIOHubEnvStatsDn_Type()
)
cucsComputeIOHubEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsDn.setStatus("current")
_CucsComputeIOHubEnvStatsRn_Type = SnmpAdminString
_CucsComputeIOHubEnvStatsRn_Object = MibTableColumn
cucsComputeIOHubEnvStatsRn = _CucsComputeIOHubEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1, 3),
    _CucsComputeIOHubEnvStatsRn_Type()
)
cucsComputeIOHubEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsRn.setStatus("current")
_CucsComputeIOHubEnvStatsIntervals_Type = Gauge32
_CucsComputeIOHubEnvStatsIntervals_Object = MibTableColumn
cucsComputeIOHubEnvStatsIntervals = _CucsComputeIOHubEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1, 4),
    _CucsComputeIOHubEnvStatsIntervals_Type()
)
cucsComputeIOHubEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsIntervals.setStatus("current")
_CucsComputeIOHubEnvStatsSuspect_Type = TruthValue
_CucsComputeIOHubEnvStatsSuspect_Object = MibTableColumn
cucsComputeIOHubEnvStatsSuspect = _CucsComputeIOHubEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1, 5),
    _CucsComputeIOHubEnvStatsSuspect_Type()
)
cucsComputeIOHubEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsSuspect.setStatus("current")
_CucsComputeIOHubEnvStatsTemperature_Type = Integer32
_CucsComputeIOHubEnvStatsTemperature_Object = MibTableColumn
cucsComputeIOHubEnvStatsTemperature = _CucsComputeIOHubEnvStatsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1, 6),
    _CucsComputeIOHubEnvStatsTemperature_Type()
)
cucsComputeIOHubEnvStatsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsTemperature.setStatus("current")
_CucsComputeIOHubEnvStatsTemperatureAvg_Type = Integer32
_CucsComputeIOHubEnvStatsTemperatureAvg_Object = MibTableColumn
cucsComputeIOHubEnvStatsTemperatureAvg = _CucsComputeIOHubEnvStatsTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1, 7),
    _CucsComputeIOHubEnvStatsTemperatureAvg_Type()
)
cucsComputeIOHubEnvStatsTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsTemperatureAvg.setStatus("current")
_CucsComputeIOHubEnvStatsTemperatureMax_Type = Integer32
_CucsComputeIOHubEnvStatsTemperatureMax_Object = MibTableColumn
cucsComputeIOHubEnvStatsTemperatureMax = _CucsComputeIOHubEnvStatsTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1, 8),
    _CucsComputeIOHubEnvStatsTemperatureMax_Type()
)
cucsComputeIOHubEnvStatsTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsTemperatureMax.setStatus("current")
_CucsComputeIOHubEnvStatsTemperatureMin_Type = Integer32
_CucsComputeIOHubEnvStatsTemperatureMin_Object = MibTableColumn
cucsComputeIOHubEnvStatsTemperatureMin = _CucsComputeIOHubEnvStatsTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1, 9),
    _CucsComputeIOHubEnvStatsTemperatureMin_Type()
)
cucsComputeIOHubEnvStatsTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsTemperatureMin.setStatus("current")
_CucsComputeIOHubEnvStatsThresholded_Type = CucsComputeIOHubEnvStatsThresholded
_CucsComputeIOHubEnvStatsThresholded_Object = MibTableColumn
cucsComputeIOHubEnvStatsThresholded = _CucsComputeIOHubEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1, 10),
    _CucsComputeIOHubEnvStatsThresholded_Type()
)
cucsComputeIOHubEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsThresholded.setStatus("current")
_CucsComputeIOHubEnvStatsTimeCollected_Type = DateAndTime
_CucsComputeIOHubEnvStatsTimeCollected_Object = MibTableColumn
cucsComputeIOHubEnvStatsTimeCollected = _CucsComputeIOHubEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1, 11),
    _CucsComputeIOHubEnvStatsTimeCollected_Type()
)
cucsComputeIOHubEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsTimeCollected.setStatus("current")
_CucsComputeIOHubEnvStatsUpdate_Type = Gauge32
_CucsComputeIOHubEnvStatsUpdate_Object = MibTableColumn
cucsComputeIOHubEnvStatsUpdate = _CucsComputeIOHubEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 12, 1, 12),
    _CucsComputeIOHubEnvStatsUpdate_Type()
)
cucsComputeIOHubEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsUpdate.setStatus("current")
_CucsComputeIOHubEnvStatsHistTable_Object = MibTable
cucsComputeIOHubEnvStatsHistTable = _CucsComputeIOHubEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13)
)
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistTable.setStatus("current")
_CucsComputeIOHubEnvStatsHistEntry_Object = MibTableRow
cucsComputeIOHubEnvStatsHistEntry = _CucsComputeIOHubEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1)
)
cucsComputeIOHubEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeIOHubEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistEntry.setStatus("current")
_CucsComputeIOHubEnvStatsHistInstanceId_Type = CucsManagedObjectId
_CucsComputeIOHubEnvStatsHistInstanceId_Object = MibTableColumn
cucsComputeIOHubEnvStatsHistInstanceId = _CucsComputeIOHubEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1, 1),
    _CucsComputeIOHubEnvStatsHistInstanceId_Type()
)
cucsComputeIOHubEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistInstanceId.setStatus("current")
_CucsComputeIOHubEnvStatsHistDn_Type = CucsManagedObjectDn
_CucsComputeIOHubEnvStatsHistDn_Object = MibTableColumn
cucsComputeIOHubEnvStatsHistDn = _CucsComputeIOHubEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1, 2),
    _CucsComputeIOHubEnvStatsHistDn_Type()
)
cucsComputeIOHubEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistDn.setStatus("current")
_CucsComputeIOHubEnvStatsHistRn_Type = SnmpAdminString
_CucsComputeIOHubEnvStatsHistRn_Object = MibTableColumn
cucsComputeIOHubEnvStatsHistRn = _CucsComputeIOHubEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1, 3),
    _CucsComputeIOHubEnvStatsHistRn_Type()
)
cucsComputeIOHubEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistRn.setStatus("current")
_CucsComputeIOHubEnvStatsHistId_Type = Unsigned64
_CucsComputeIOHubEnvStatsHistId_Object = MibTableColumn
cucsComputeIOHubEnvStatsHistId = _CucsComputeIOHubEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1, 4),
    _CucsComputeIOHubEnvStatsHistId_Type()
)
cucsComputeIOHubEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistId.setStatus("current")
_CucsComputeIOHubEnvStatsHistMostRecent_Type = TruthValue
_CucsComputeIOHubEnvStatsHistMostRecent_Object = MibTableColumn
cucsComputeIOHubEnvStatsHistMostRecent = _CucsComputeIOHubEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1, 5),
    _CucsComputeIOHubEnvStatsHistMostRecent_Type()
)
cucsComputeIOHubEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistMostRecent.setStatus("current")
_CucsComputeIOHubEnvStatsHistSuspect_Type = TruthValue
_CucsComputeIOHubEnvStatsHistSuspect_Object = MibTableColumn
cucsComputeIOHubEnvStatsHistSuspect = _CucsComputeIOHubEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1, 6),
    _CucsComputeIOHubEnvStatsHistSuspect_Type()
)
cucsComputeIOHubEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistSuspect.setStatus("current")
_CucsComputeIOHubEnvStatsHistTemperature_Type = Integer32
_CucsComputeIOHubEnvStatsHistTemperature_Object = MibTableColumn
cucsComputeIOHubEnvStatsHistTemperature = _CucsComputeIOHubEnvStatsHistTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1, 7),
    _CucsComputeIOHubEnvStatsHistTemperature_Type()
)
cucsComputeIOHubEnvStatsHistTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistTemperature.setStatus("current")
_CucsComputeIOHubEnvStatsHistTemperatureAvg_Type = Integer32
_CucsComputeIOHubEnvStatsHistTemperatureAvg_Object = MibTableColumn
cucsComputeIOHubEnvStatsHistTemperatureAvg = _CucsComputeIOHubEnvStatsHistTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1, 8),
    _CucsComputeIOHubEnvStatsHistTemperatureAvg_Type()
)
cucsComputeIOHubEnvStatsHistTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistTemperatureAvg.setStatus("current")
_CucsComputeIOHubEnvStatsHistTemperatureMax_Type = Integer32
_CucsComputeIOHubEnvStatsHistTemperatureMax_Object = MibTableColumn
cucsComputeIOHubEnvStatsHistTemperatureMax = _CucsComputeIOHubEnvStatsHistTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1, 9),
    _CucsComputeIOHubEnvStatsHistTemperatureMax_Type()
)
cucsComputeIOHubEnvStatsHistTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistTemperatureMax.setStatus("current")
_CucsComputeIOHubEnvStatsHistTemperatureMin_Type = Integer32
_CucsComputeIOHubEnvStatsHistTemperatureMin_Object = MibTableColumn
cucsComputeIOHubEnvStatsHistTemperatureMin = _CucsComputeIOHubEnvStatsHistTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1, 10),
    _CucsComputeIOHubEnvStatsHistTemperatureMin_Type()
)
cucsComputeIOHubEnvStatsHistTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistTemperatureMin.setStatus("current")
_CucsComputeIOHubEnvStatsHistThresholded_Type = CucsComputeIOHubEnvStatsHistThresholded
_CucsComputeIOHubEnvStatsHistThresholded_Object = MibTableColumn
cucsComputeIOHubEnvStatsHistThresholded = _CucsComputeIOHubEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1, 11),
    _CucsComputeIOHubEnvStatsHistThresholded_Type()
)
cucsComputeIOHubEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistThresholded.setStatus("current")
_CucsComputeIOHubEnvStatsHistTimeCollected_Type = DateAndTime
_CucsComputeIOHubEnvStatsHistTimeCollected_Object = MibTableColumn
cucsComputeIOHubEnvStatsHistTimeCollected = _CucsComputeIOHubEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 13, 1, 12),
    _CucsComputeIOHubEnvStatsHistTimeCollected_Type()
)
cucsComputeIOHubEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeIOHubEnvStatsHistTimeCollected.setStatus("current")
_CucsComputeMbPowerStatsTable_Object = MibTable
cucsComputeMbPowerStatsTable = _CucsComputeMbPowerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14)
)
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsTable.setStatus("current")
_CucsComputeMbPowerStatsEntry_Object = MibTableRow
cucsComputeMbPowerStatsEntry = _CucsComputeMbPowerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1)
)
cucsComputeMbPowerStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeMbPowerStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsEntry.setStatus("current")
_CucsComputeMbPowerStatsInstanceId_Type = CucsManagedObjectId
_CucsComputeMbPowerStatsInstanceId_Object = MibTableColumn
cucsComputeMbPowerStatsInstanceId = _CucsComputeMbPowerStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 1),
    _CucsComputeMbPowerStatsInstanceId_Type()
)
cucsComputeMbPowerStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsInstanceId.setStatus("current")
_CucsComputeMbPowerStatsDn_Type = CucsManagedObjectDn
_CucsComputeMbPowerStatsDn_Object = MibTableColumn
cucsComputeMbPowerStatsDn = _CucsComputeMbPowerStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 2),
    _CucsComputeMbPowerStatsDn_Type()
)
cucsComputeMbPowerStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsDn.setStatus("current")
_CucsComputeMbPowerStatsRn_Type = SnmpAdminString
_CucsComputeMbPowerStatsRn_Object = MibTableColumn
cucsComputeMbPowerStatsRn = _CucsComputeMbPowerStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 3),
    _CucsComputeMbPowerStatsRn_Type()
)
cucsComputeMbPowerStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsRn.setStatus("current")
_CucsComputeMbPowerStatsConsumedPower_Type = Integer32
_CucsComputeMbPowerStatsConsumedPower_Object = MibTableColumn
cucsComputeMbPowerStatsConsumedPower = _CucsComputeMbPowerStatsConsumedPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 4),
    _CucsComputeMbPowerStatsConsumedPower_Type()
)
cucsComputeMbPowerStatsConsumedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsConsumedPower.setStatus("current")
_CucsComputeMbPowerStatsConsumedPowerAvg_Type = Integer32
_CucsComputeMbPowerStatsConsumedPowerAvg_Object = MibTableColumn
cucsComputeMbPowerStatsConsumedPowerAvg = _CucsComputeMbPowerStatsConsumedPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 5),
    _CucsComputeMbPowerStatsConsumedPowerAvg_Type()
)
cucsComputeMbPowerStatsConsumedPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsConsumedPowerAvg.setStatus("current")
_CucsComputeMbPowerStatsConsumedPowerMax_Type = Integer32
_CucsComputeMbPowerStatsConsumedPowerMax_Object = MibTableColumn
cucsComputeMbPowerStatsConsumedPowerMax = _CucsComputeMbPowerStatsConsumedPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 6),
    _CucsComputeMbPowerStatsConsumedPowerMax_Type()
)
cucsComputeMbPowerStatsConsumedPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsConsumedPowerMax.setStatus("current")
_CucsComputeMbPowerStatsConsumedPowerMin_Type = Integer32
_CucsComputeMbPowerStatsConsumedPowerMin_Object = MibTableColumn
cucsComputeMbPowerStatsConsumedPowerMin = _CucsComputeMbPowerStatsConsumedPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 7),
    _CucsComputeMbPowerStatsConsumedPowerMin_Type()
)
cucsComputeMbPowerStatsConsumedPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsConsumedPowerMin.setStatus("current")
_CucsComputeMbPowerStatsInputCurrent_Type = Integer32
_CucsComputeMbPowerStatsInputCurrent_Object = MibTableColumn
cucsComputeMbPowerStatsInputCurrent = _CucsComputeMbPowerStatsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 8),
    _CucsComputeMbPowerStatsInputCurrent_Type()
)
cucsComputeMbPowerStatsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsInputCurrent.setStatus("current")
_CucsComputeMbPowerStatsInputCurrentAvg_Type = Integer32
_CucsComputeMbPowerStatsInputCurrentAvg_Object = MibTableColumn
cucsComputeMbPowerStatsInputCurrentAvg = _CucsComputeMbPowerStatsInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 9),
    _CucsComputeMbPowerStatsInputCurrentAvg_Type()
)
cucsComputeMbPowerStatsInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsInputCurrentAvg.setStatus("current")
_CucsComputeMbPowerStatsInputCurrentMax_Type = Integer32
_CucsComputeMbPowerStatsInputCurrentMax_Object = MibTableColumn
cucsComputeMbPowerStatsInputCurrentMax = _CucsComputeMbPowerStatsInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 10),
    _CucsComputeMbPowerStatsInputCurrentMax_Type()
)
cucsComputeMbPowerStatsInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsInputCurrentMax.setStatus("current")
_CucsComputeMbPowerStatsInputCurrentMin_Type = Integer32
_CucsComputeMbPowerStatsInputCurrentMin_Object = MibTableColumn
cucsComputeMbPowerStatsInputCurrentMin = _CucsComputeMbPowerStatsInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 11),
    _CucsComputeMbPowerStatsInputCurrentMin_Type()
)
cucsComputeMbPowerStatsInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsInputCurrentMin.setStatus("current")
_CucsComputeMbPowerStatsInputVoltage_Type = Integer32
_CucsComputeMbPowerStatsInputVoltage_Object = MibTableColumn
cucsComputeMbPowerStatsInputVoltage = _CucsComputeMbPowerStatsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 12),
    _CucsComputeMbPowerStatsInputVoltage_Type()
)
cucsComputeMbPowerStatsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsInputVoltage.setStatus("current")
_CucsComputeMbPowerStatsInputVoltageAvg_Type = Integer32
_CucsComputeMbPowerStatsInputVoltageAvg_Object = MibTableColumn
cucsComputeMbPowerStatsInputVoltageAvg = _CucsComputeMbPowerStatsInputVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 13),
    _CucsComputeMbPowerStatsInputVoltageAvg_Type()
)
cucsComputeMbPowerStatsInputVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsInputVoltageAvg.setStatus("current")
_CucsComputeMbPowerStatsInputVoltageMax_Type = Integer32
_CucsComputeMbPowerStatsInputVoltageMax_Object = MibTableColumn
cucsComputeMbPowerStatsInputVoltageMax = _CucsComputeMbPowerStatsInputVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 14),
    _CucsComputeMbPowerStatsInputVoltageMax_Type()
)
cucsComputeMbPowerStatsInputVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsInputVoltageMax.setStatus("current")
_CucsComputeMbPowerStatsInputVoltageMin_Type = Integer32
_CucsComputeMbPowerStatsInputVoltageMin_Object = MibTableColumn
cucsComputeMbPowerStatsInputVoltageMin = _CucsComputeMbPowerStatsInputVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 15),
    _CucsComputeMbPowerStatsInputVoltageMin_Type()
)
cucsComputeMbPowerStatsInputVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsInputVoltageMin.setStatus("current")
_CucsComputeMbPowerStatsIntervals_Type = Gauge32
_CucsComputeMbPowerStatsIntervals_Object = MibTableColumn
cucsComputeMbPowerStatsIntervals = _CucsComputeMbPowerStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 16),
    _CucsComputeMbPowerStatsIntervals_Type()
)
cucsComputeMbPowerStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsIntervals.setStatus("current")
_CucsComputeMbPowerStatsSuspect_Type = TruthValue
_CucsComputeMbPowerStatsSuspect_Object = MibTableColumn
cucsComputeMbPowerStatsSuspect = _CucsComputeMbPowerStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 17),
    _CucsComputeMbPowerStatsSuspect_Type()
)
cucsComputeMbPowerStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsSuspect.setStatus("current")
_CucsComputeMbPowerStatsThresholded_Type = CucsComputeMbPowerStatsThresholded
_CucsComputeMbPowerStatsThresholded_Object = MibTableColumn
cucsComputeMbPowerStatsThresholded = _CucsComputeMbPowerStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 18),
    _CucsComputeMbPowerStatsThresholded_Type()
)
cucsComputeMbPowerStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsThresholded.setStatus("current")
_CucsComputeMbPowerStatsTimeCollected_Type = DateAndTime
_CucsComputeMbPowerStatsTimeCollected_Object = MibTableColumn
cucsComputeMbPowerStatsTimeCollected = _CucsComputeMbPowerStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 19),
    _CucsComputeMbPowerStatsTimeCollected_Type()
)
cucsComputeMbPowerStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsTimeCollected.setStatus("current")
_CucsComputeMbPowerStatsUpdate_Type = Gauge32
_CucsComputeMbPowerStatsUpdate_Object = MibTableColumn
cucsComputeMbPowerStatsUpdate = _CucsComputeMbPowerStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 14, 1, 20),
    _CucsComputeMbPowerStatsUpdate_Type()
)
cucsComputeMbPowerStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsUpdate.setStatus("current")
_CucsComputeMbPowerStatsHistTable_Object = MibTable
cucsComputeMbPowerStatsHistTable = _CucsComputeMbPowerStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15)
)
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistTable.setStatus("current")
_CucsComputeMbPowerStatsHistEntry_Object = MibTableRow
cucsComputeMbPowerStatsHistEntry = _CucsComputeMbPowerStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1)
)
cucsComputeMbPowerStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeMbPowerStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistEntry.setStatus("current")
_CucsComputeMbPowerStatsHistInstanceId_Type = CucsManagedObjectId
_CucsComputeMbPowerStatsHistInstanceId_Object = MibTableColumn
cucsComputeMbPowerStatsHistInstanceId = _CucsComputeMbPowerStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 1),
    _CucsComputeMbPowerStatsHistInstanceId_Type()
)
cucsComputeMbPowerStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistInstanceId.setStatus("current")
_CucsComputeMbPowerStatsHistDn_Type = CucsManagedObjectDn
_CucsComputeMbPowerStatsHistDn_Object = MibTableColumn
cucsComputeMbPowerStatsHistDn = _CucsComputeMbPowerStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 2),
    _CucsComputeMbPowerStatsHistDn_Type()
)
cucsComputeMbPowerStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistDn.setStatus("current")
_CucsComputeMbPowerStatsHistRn_Type = SnmpAdminString
_CucsComputeMbPowerStatsHistRn_Object = MibTableColumn
cucsComputeMbPowerStatsHistRn = _CucsComputeMbPowerStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 3),
    _CucsComputeMbPowerStatsHistRn_Type()
)
cucsComputeMbPowerStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistRn.setStatus("current")
_CucsComputeMbPowerStatsHistConsumedPower_Type = Integer32
_CucsComputeMbPowerStatsHistConsumedPower_Object = MibTableColumn
cucsComputeMbPowerStatsHistConsumedPower = _CucsComputeMbPowerStatsHistConsumedPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 4),
    _CucsComputeMbPowerStatsHistConsumedPower_Type()
)
cucsComputeMbPowerStatsHistConsumedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistConsumedPower.setStatus("current")
_CucsComputeMbPowerStatsHistConsumedPowerAvg_Type = Integer32
_CucsComputeMbPowerStatsHistConsumedPowerAvg_Object = MibTableColumn
cucsComputeMbPowerStatsHistConsumedPowerAvg = _CucsComputeMbPowerStatsHistConsumedPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 5),
    _CucsComputeMbPowerStatsHistConsumedPowerAvg_Type()
)
cucsComputeMbPowerStatsHistConsumedPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistConsumedPowerAvg.setStatus("current")
_CucsComputeMbPowerStatsHistConsumedPowerMax_Type = Integer32
_CucsComputeMbPowerStatsHistConsumedPowerMax_Object = MibTableColumn
cucsComputeMbPowerStatsHistConsumedPowerMax = _CucsComputeMbPowerStatsHistConsumedPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 6),
    _CucsComputeMbPowerStatsHistConsumedPowerMax_Type()
)
cucsComputeMbPowerStatsHistConsumedPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistConsumedPowerMax.setStatus("current")
_CucsComputeMbPowerStatsHistConsumedPowerMin_Type = Integer32
_CucsComputeMbPowerStatsHistConsumedPowerMin_Object = MibTableColumn
cucsComputeMbPowerStatsHistConsumedPowerMin = _CucsComputeMbPowerStatsHistConsumedPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 7),
    _CucsComputeMbPowerStatsHistConsumedPowerMin_Type()
)
cucsComputeMbPowerStatsHistConsumedPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistConsumedPowerMin.setStatus("current")
_CucsComputeMbPowerStatsHistId_Type = Unsigned64
_CucsComputeMbPowerStatsHistId_Object = MibTableColumn
cucsComputeMbPowerStatsHistId = _CucsComputeMbPowerStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 8),
    _CucsComputeMbPowerStatsHistId_Type()
)
cucsComputeMbPowerStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistId.setStatus("current")
_CucsComputeMbPowerStatsHistInputCurrent_Type = Integer32
_CucsComputeMbPowerStatsHistInputCurrent_Object = MibTableColumn
cucsComputeMbPowerStatsHistInputCurrent = _CucsComputeMbPowerStatsHistInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 9),
    _CucsComputeMbPowerStatsHistInputCurrent_Type()
)
cucsComputeMbPowerStatsHistInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistInputCurrent.setStatus("current")
_CucsComputeMbPowerStatsHistInputCurrentAvg_Type = Integer32
_CucsComputeMbPowerStatsHistInputCurrentAvg_Object = MibTableColumn
cucsComputeMbPowerStatsHistInputCurrentAvg = _CucsComputeMbPowerStatsHistInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 10),
    _CucsComputeMbPowerStatsHistInputCurrentAvg_Type()
)
cucsComputeMbPowerStatsHistInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistInputCurrentAvg.setStatus("current")
_CucsComputeMbPowerStatsHistInputCurrentMax_Type = Integer32
_CucsComputeMbPowerStatsHistInputCurrentMax_Object = MibTableColumn
cucsComputeMbPowerStatsHistInputCurrentMax = _CucsComputeMbPowerStatsHistInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 11),
    _CucsComputeMbPowerStatsHistInputCurrentMax_Type()
)
cucsComputeMbPowerStatsHistInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistInputCurrentMax.setStatus("current")
_CucsComputeMbPowerStatsHistInputCurrentMin_Type = Integer32
_CucsComputeMbPowerStatsHistInputCurrentMin_Object = MibTableColumn
cucsComputeMbPowerStatsHistInputCurrentMin = _CucsComputeMbPowerStatsHistInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 12),
    _CucsComputeMbPowerStatsHistInputCurrentMin_Type()
)
cucsComputeMbPowerStatsHistInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistInputCurrentMin.setStatus("current")
_CucsComputeMbPowerStatsHistInputVoltage_Type = Integer32
_CucsComputeMbPowerStatsHistInputVoltage_Object = MibTableColumn
cucsComputeMbPowerStatsHistInputVoltage = _CucsComputeMbPowerStatsHistInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 13),
    _CucsComputeMbPowerStatsHistInputVoltage_Type()
)
cucsComputeMbPowerStatsHistInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistInputVoltage.setStatus("current")
_CucsComputeMbPowerStatsHistInputVoltageAvg_Type = Integer32
_CucsComputeMbPowerStatsHistInputVoltageAvg_Object = MibTableColumn
cucsComputeMbPowerStatsHistInputVoltageAvg = _CucsComputeMbPowerStatsHistInputVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 14),
    _CucsComputeMbPowerStatsHistInputVoltageAvg_Type()
)
cucsComputeMbPowerStatsHistInputVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistInputVoltageAvg.setStatus("current")
_CucsComputeMbPowerStatsHistInputVoltageMax_Type = Integer32
_CucsComputeMbPowerStatsHistInputVoltageMax_Object = MibTableColumn
cucsComputeMbPowerStatsHistInputVoltageMax = _CucsComputeMbPowerStatsHistInputVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 15),
    _CucsComputeMbPowerStatsHistInputVoltageMax_Type()
)
cucsComputeMbPowerStatsHistInputVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistInputVoltageMax.setStatus("current")
_CucsComputeMbPowerStatsHistInputVoltageMin_Type = Integer32
_CucsComputeMbPowerStatsHistInputVoltageMin_Object = MibTableColumn
cucsComputeMbPowerStatsHistInputVoltageMin = _CucsComputeMbPowerStatsHistInputVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 16),
    _CucsComputeMbPowerStatsHistInputVoltageMin_Type()
)
cucsComputeMbPowerStatsHistInputVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistInputVoltageMin.setStatus("current")
_CucsComputeMbPowerStatsHistMostRecent_Type = TruthValue
_CucsComputeMbPowerStatsHistMostRecent_Object = MibTableColumn
cucsComputeMbPowerStatsHistMostRecent = _CucsComputeMbPowerStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 17),
    _CucsComputeMbPowerStatsHistMostRecent_Type()
)
cucsComputeMbPowerStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistMostRecent.setStatus("current")
_CucsComputeMbPowerStatsHistSuspect_Type = TruthValue
_CucsComputeMbPowerStatsHistSuspect_Object = MibTableColumn
cucsComputeMbPowerStatsHistSuspect = _CucsComputeMbPowerStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 18),
    _CucsComputeMbPowerStatsHistSuspect_Type()
)
cucsComputeMbPowerStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistSuspect.setStatus("current")
_CucsComputeMbPowerStatsHistThresholded_Type = CucsComputeMbPowerStatsHistThresholded
_CucsComputeMbPowerStatsHistThresholded_Object = MibTableColumn
cucsComputeMbPowerStatsHistThresholded = _CucsComputeMbPowerStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 19),
    _CucsComputeMbPowerStatsHistThresholded_Type()
)
cucsComputeMbPowerStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistThresholded.setStatus("current")
_CucsComputeMbPowerStatsHistTimeCollected_Type = DateAndTime
_CucsComputeMbPowerStatsHistTimeCollected_Object = MibTableColumn
cucsComputeMbPowerStatsHistTimeCollected = _CucsComputeMbPowerStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 15, 1, 20),
    _CucsComputeMbPowerStatsHistTimeCollected_Type()
)
cucsComputeMbPowerStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbPowerStatsHistTimeCollected.setStatus("current")
_CucsComputeMbTempStatsTable_Object = MibTable
cucsComputeMbTempStatsTable = _CucsComputeMbTempStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16)
)
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsTable.setStatus("current")
_CucsComputeMbTempStatsEntry_Object = MibTableRow
cucsComputeMbTempStatsEntry = _CucsComputeMbTempStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1)
)
cucsComputeMbTempStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeMbTempStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsEntry.setStatus("current")
_CucsComputeMbTempStatsInstanceId_Type = CucsManagedObjectId
_CucsComputeMbTempStatsInstanceId_Object = MibTableColumn
cucsComputeMbTempStatsInstanceId = _CucsComputeMbTempStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 1),
    _CucsComputeMbTempStatsInstanceId_Type()
)
cucsComputeMbTempStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsInstanceId.setStatus("current")
_CucsComputeMbTempStatsDn_Type = CucsManagedObjectDn
_CucsComputeMbTempStatsDn_Object = MibTableColumn
cucsComputeMbTempStatsDn = _CucsComputeMbTempStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 2),
    _CucsComputeMbTempStatsDn_Type()
)
cucsComputeMbTempStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsDn.setStatus("current")
_CucsComputeMbTempStatsRn_Type = SnmpAdminString
_CucsComputeMbTempStatsRn_Object = MibTableColumn
cucsComputeMbTempStatsRn = _CucsComputeMbTempStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 3),
    _CucsComputeMbTempStatsRn_Type()
)
cucsComputeMbTempStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsRn.setStatus("current")
_CucsComputeMbTempStatsFmTempSenIo_Type = Integer32
_CucsComputeMbTempStatsFmTempSenIo_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenIo = _CucsComputeMbTempStatsFmTempSenIo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 4),
    _CucsComputeMbTempStatsFmTempSenIo_Type()
)
cucsComputeMbTempStatsFmTempSenIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenIo.setStatus("current")
_CucsComputeMbTempStatsFmTempSenIoAvg_Type = Integer32
_CucsComputeMbTempStatsFmTempSenIoAvg_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenIoAvg = _CucsComputeMbTempStatsFmTempSenIoAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 5),
    _CucsComputeMbTempStatsFmTempSenIoAvg_Type()
)
cucsComputeMbTempStatsFmTempSenIoAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenIoAvg.setStatus("current")
_CucsComputeMbTempStatsFmTempSenIoMax_Type = Integer32
_CucsComputeMbTempStatsFmTempSenIoMax_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenIoMax = _CucsComputeMbTempStatsFmTempSenIoMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 6),
    _CucsComputeMbTempStatsFmTempSenIoMax_Type()
)
cucsComputeMbTempStatsFmTempSenIoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenIoMax.setStatus("current")
_CucsComputeMbTempStatsFmTempSenIoMin_Type = Integer32
_CucsComputeMbTempStatsFmTempSenIoMin_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenIoMin = _CucsComputeMbTempStatsFmTempSenIoMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 7),
    _CucsComputeMbTempStatsFmTempSenIoMin_Type()
)
cucsComputeMbTempStatsFmTempSenIoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenIoMin.setStatus("current")
_CucsComputeMbTempStatsFmTempSenRear_Type = Integer32
_CucsComputeMbTempStatsFmTempSenRear_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenRear = _CucsComputeMbTempStatsFmTempSenRear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 8),
    _CucsComputeMbTempStatsFmTempSenRear_Type()
)
cucsComputeMbTempStatsFmTempSenRear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenRear.setStatus("current")
_CucsComputeMbTempStatsFmTempSenRearAvg_Type = Integer32
_CucsComputeMbTempStatsFmTempSenRearAvg_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenRearAvg = _CucsComputeMbTempStatsFmTempSenRearAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 9),
    _CucsComputeMbTempStatsFmTempSenRearAvg_Type()
)
cucsComputeMbTempStatsFmTempSenRearAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenRearAvg.setStatus("current")
_CucsComputeMbTempStatsFmTempSenRearL_Type = Integer32
_CucsComputeMbTempStatsFmTempSenRearL_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenRearL = _CucsComputeMbTempStatsFmTempSenRearL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 10),
    _CucsComputeMbTempStatsFmTempSenRearL_Type()
)
cucsComputeMbTempStatsFmTempSenRearL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenRearL.setStatus("current")
_CucsComputeMbTempStatsFmTempSenRearLAvg_Type = Integer32
_CucsComputeMbTempStatsFmTempSenRearLAvg_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenRearLAvg = _CucsComputeMbTempStatsFmTempSenRearLAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 11),
    _CucsComputeMbTempStatsFmTempSenRearLAvg_Type()
)
cucsComputeMbTempStatsFmTempSenRearLAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenRearLAvg.setStatus("current")
_CucsComputeMbTempStatsFmTempSenRearLMax_Type = Integer32
_CucsComputeMbTempStatsFmTempSenRearLMax_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenRearLMax = _CucsComputeMbTempStatsFmTempSenRearLMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 12),
    _CucsComputeMbTempStatsFmTempSenRearLMax_Type()
)
cucsComputeMbTempStatsFmTempSenRearLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenRearLMax.setStatus("current")
_CucsComputeMbTempStatsFmTempSenRearLMin_Type = Integer32
_CucsComputeMbTempStatsFmTempSenRearLMin_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenRearLMin = _CucsComputeMbTempStatsFmTempSenRearLMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 13),
    _CucsComputeMbTempStatsFmTempSenRearLMin_Type()
)
cucsComputeMbTempStatsFmTempSenRearLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenRearLMin.setStatus("current")
_CucsComputeMbTempStatsFmTempSenRearMax_Type = Integer32
_CucsComputeMbTempStatsFmTempSenRearMax_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenRearMax = _CucsComputeMbTempStatsFmTempSenRearMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 14),
    _CucsComputeMbTempStatsFmTempSenRearMax_Type()
)
cucsComputeMbTempStatsFmTempSenRearMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenRearMax.setStatus("current")
_CucsComputeMbTempStatsFmTempSenRearMin_Type = Integer32
_CucsComputeMbTempStatsFmTempSenRearMin_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenRearMin = _CucsComputeMbTempStatsFmTempSenRearMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 15),
    _CucsComputeMbTempStatsFmTempSenRearMin_Type()
)
cucsComputeMbTempStatsFmTempSenRearMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenRearMin.setStatus("current")
_CucsComputeMbTempStatsFmTempSenRearR_Type = Integer32
_CucsComputeMbTempStatsFmTempSenRearR_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenRearR = _CucsComputeMbTempStatsFmTempSenRearR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 16),
    _CucsComputeMbTempStatsFmTempSenRearR_Type()
)
cucsComputeMbTempStatsFmTempSenRearR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenRearR.setStatus("current")
_CucsComputeMbTempStatsFmTempSenRearRAvg_Type = Integer32
_CucsComputeMbTempStatsFmTempSenRearRAvg_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenRearRAvg = _CucsComputeMbTempStatsFmTempSenRearRAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 17),
    _CucsComputeMbTempStatsFmTempSenRearRAvg_Type()
)
cucsComputeMbTempStatsFmTempSenRearRAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenRearRAvg.setStatus("current")
_CucsComputeMbTempStatsFmTempSenRearRMax_Type = Integer32
_CucsComputeMbTempStatsFmTempSenRearRMax_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenRearRMax = _CucsComputeMbTempStatsFmTempSenRearRMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 18),
    _CucsComputeMbTempStatsFmTempSenRearRMax_Type()
)
cucsComputeMbTempStatsFmTempSenRearRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenRearRMax.setStatus("current")
_CucsComputeMbTempStatsFmTempSenRearRMin_Type = Integer32
_CucsComputeMbTempStatsFmTempSenRearRMin_Object = MibTableColumn
cucsComputeMbTempStatsFmTempSenRearRMin = _CucsComputeMbTempStatsFmTempSenRearRMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 19),
    _CucsComputeMbTempStatsFmTempSenRearRMin_Type()
)
cucsComputeMbTempStatsFmTempSenRearRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsFmTempSenRearRMin.setStatus("current")
_CucsComputeMbTempStatsIntervals_Type = Gauge32
_CucsComputeMbTempStatsIntervals_Object = MibTableColumn
cucsComputeMbTempStatsIntervals = _CucsComputeMbTempStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 20),
    _CucsComputeMbTempStatsIntervals_Type()
)
cucsComputeMbTempStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsIntervals.setStatus("current")
_CucsComputeMbTempStatsSuspect_Type = TruthValue
_CucsComputeMbTempStatsSuspect_Object = MibTableColumn
cucsComputeMbTempStatsSuspect = _CucsComputeMbTempStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 21),
    _CucsComputeMbTempStatsSuspect_Type()
)
cucsComputeMbTempStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsSuspect.setStatus("current")
_CucsComputeMbTempStatsThresholded_Type = CucsComputeMbTempStatsThresholded
_CucsComputeMbTempStatsThresholded_Object = MibTableColumn
cucsComputeMbTempStatsThresholded = _CucsComputeMbTempStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 22),
    _CucsComputeMbTempStatsThresholded_Type()
)
cucsComputeMbTempStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsThresholded.setStatus("current")
_CucsComputeMbTempStatsTimeCollected_Type = DateAndTime
_CucsComputeMbTempStatsTimeCollected_Object = MibTableColumn
cucsComputeMbTempStatsTimeCollected = _CucsComputeMbTempStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 23),
    _CucsComputeMbTempStatsTimeCollected_Type()
)
cucsComputeMbTempStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsTimeCollected.setStatus("current")
_CucsComputeMbTempStatsUpdate_Type = Gauge32
_CucsComputeMbTempStatsUpdate_Object = MibTableColumn
cucsComputeMbTempStatsUpdate = _CucsComputeMbTempStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 16, 1, 24),
    _CucsComputeMbTempStatsUpdate_Type()
)
cucsComputeMbTempStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsUpdate.setStatus("current")
_CucsComputeMbTempStatsHistTable_Object = MibTable
cucsComputeMbTempStatsHistTable = _CucsComputeMbTempStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17)
)
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistTable.setStatus("current")
_CucsComputeMbTempStatsHistEntry_Object = MibTableRow
cucsComputeMbTempStatsHistEntry = _CucsComputeMbTempStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1)
)
cucsComputeMbTempStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeMbTempStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistEntry.setStatus("current")
_CucsComputeMbTempStatsHistInstanceId_Type = CucsManagedObjectId
_CucsComputeMbTempStatsHistInstanceId_Object = MibTableColumn
cucsComputeMbTempStatsHistInstanceId = _CucsComputeMbTempStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 1),
    _CucsComputeMbTempStatsHistInstanceId_Type()
)
cucsComputeMbTempStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistInstanceId.setStatus("current")
_CucsComputeMbTempStatsHistDn_Type = CucsManagedObjectDn
_CucsComputeMbTempStatsHistDn_Object = MibTableColumn
cucsComputeMbTempStatsHistDn = _CucsComputeMbTempStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 2),
    _CucsComputeMbTempStatsHistDn_Type()
)
cucsComputeMbTempStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistDn.setStatus("current")
_CucsComputeMbTempStatsHistRn_Type = SnmpAdminString
_CucsComputeMbTempStatsHistRn_Object = MibTableColumn
cucsComputeMbTempStatsHistRn = _CucsComputeMbTempStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 3),
    _CucsComputeMbTempStatsHistRn_Type()
)
cucsComputeMbTempStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistRn.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenIo_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenIo_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenIo = _CucsComputeMbTempStatsHistFmTempSenIo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 4),
    _CucsComputeMbTempStatsHistFmTempSenIo_Type()
)
cucsComputeMbTempStatsHistFmTempSenIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenIo.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenIoAvg_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenIoAvg_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenIoAvg = _CucsComputeMbTempStatsHistFmTempSenIoAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 5),
    _CucsComputeMbTempStatsHistFmTempSenIoAvg_Type()
)
cucsComputeMbTempStatsHistFmTempSenIoAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenIoAvg.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenIoMax_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenIoMax_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenIoMax = _CucsComputeMbTempStatsHistFmTempSenIoMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 6),
    _CucsComputeMbTempStatsHistFmTempSenIoMax_Type()
)
cucsComputeMbTempStatsHistFmTempSenIoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenIoMax.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenIoMin_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenIoMin_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenIoMin = _CucsComputeMbTempStatsHistFmTempSenIoMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 7),
    _CucsComputeMbTempStatsHistFmTempSenIoMin_Type()
)
cucsComputeMbTempStatsHistFmTempSenIoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenIoMin.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenRear_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenRear_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenRear = _CucsComputeMbTempStatsHistFmTempSenRear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 8),
    _CucsComputeMbTempStatsHistFmTempSenRear_Type()
)
cucsComputeMbTempStatsHistFmTempSenRear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenRear.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenRearAvg_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenRearAvg_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenRearAvg = _CucsComputeMbTempStatsHistFmTempSenRearAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 9),
    _CucsComputeMbTempStatsHistFmTempSenRearAvg_Type()
)
cucsComputeMbTempStatsHistFmTempSenRearAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenRearAvg.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenRearL_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenRearL_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenRearL = _CucsComputeMbTempStatsHistFmTempSenRearL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 10),
    _CucsComputeMbTempStatsHistFmTempSenRearL_Type()
)
cucsComputeMbTempStatsHistFmTempSenRearL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenRearL.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenRearLAvg_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenRearLAvg_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenRearLAvg = _CucsComputeMbTempStatsHistFmTempSenRearLAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 11),
    _CucsComputeMbTempStatsHistFmTempSenRearLAvg_Type()
)
cucsComputeMbTempStatsHistFmTempSenRearLAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenRearLAvg.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenRearLMax_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenRearLMax_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenRearLMax = _CucsComputeMbTempStatsHistFmTempSenRearLMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 12),
    _CucsComputeMbTempStatsHistFmTempSenRearLMax_Type()
)
cucsComputeMbTempStatsHistFmTempSenRearLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenRearLMax.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenRearLMin_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenRearLMin_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenRearLMin = _CucsComputeMbTempStatsHistFmTempSenRearLMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 13),
    _CucsComputeMbTempStatsHistFmTempSenRearLMin_Type()
)
cucsComputeMbTempStatsHistFmTempSenRearLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenRearLMin.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenRearMax_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenRearMax_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenRearMax = _CucsComputeMbTempStatsHistFmTempSenRearMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 14),
    _CucsComputeMbTempStatsHistFmTempSenRearMax_Type()
)
cucsComputeMbTempStatsHistFmTempSenRearMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenRearMax.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenRearMin_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenRearMin_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenRearMin = _CucsComputeMbTempStatsHistFmTempSenRearMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 15),
    _CucsComputeMbTempStatsHistFmTempSenRearMin_Type()
)
cucsComputeMbTempStatsHistFmTempSenRearMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenRearMin.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenRearR_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenRearR_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenRearR = _CucsComputeMbTempStatsHistFmTempSenRearR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 16),
    _CucsComputeMbTempStatsHistFmTempSenRearR_Type()
)
cucsComputeMbTempStatsHistFmTempSenRearR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenRearR.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenRearRAvg_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenRearRAvg_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenRearRAvg = _CucsComputeMbTempStatsHistFmTempSenRearRAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 17),
    _CucsComputeMbTempStatsHistFmTempSenRearRAvg_Type()
)
cucsComputeMbTempStatsHistFmTempSenRearRAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenRearRAvg.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenRearRMax_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenRearRMax_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenRearRMax = _CucsComputeMbTempStatsHistFmTempSenRearRMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 18),
    _CucsComputeMbTempStatsHistFmTempSenRearRMax_Type()
)
cucsComputeMbTempStatsHistFmTempSenRearRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenRearRMax.setStatus("current")
_CucsComputeMbTempStatsHistFmTempSenRearRMin_Type = Integer32
_CucsComputeMbTempStatsHistFmTempSenRearRMin_Object = MibTableColumn
cucsComputeMbTempStatsHistFmTempSenRearRMin = _CucsComputeMbTempStatsHistFmTempSenRearRMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 19),
    _CucsComputeMbTempStatsHistFmTempSenRearRMin_Type()
)
cucsComputeMbTempStatsHistFmTempSenRearRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistFmTempSenRearRMin.setStatus("current")
_CucsComputeMbTempStatsHistId_Type = Unsigned64
_CucsComputeMbTempStatsHistId_Object = MibTableColumn
cucsComputeMbTempStatsHistId = _CucsComputeMbTempStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 20),
    _CucsComputeMbTempStatsHistId_Type()
)
cucsComputeMbTempStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistId.setStatus("current")
_CucsComputeMbTempStatsHistMostRecent_Type = TruthValue
_CucsComputeMbTempStatsHistMostRecent_Object = MibTableColumn
cucsComputeMbTempStatsHistMostRecent = _CucsComputeMbTempStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 21),
    _CucsComputeMbTempStatsHistMostRecent_Type()
)
cucsComputeMbTempStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistMostRecent.setStatus("current")
_CucsComputeMbTempStatsHistSuspect_Type = TruthValue
_CucsComputeMbTempStatsHistSuspect_Object = MibTableColumn
cucsComputeMbTempStatsHistSuspect = _CucsComputeMbTempStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 22),
    _CucsComputeMbTempStatsHistSuspect_Type()
)
cucsComputeMbTempStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistSuspect.setStatus("current")
_CucsComputeMbTempStatsHistThresholded_Type = CucsComputeMbTempStatsHistThresholded
_CucsComputeMbTempStatsHistThresholded_Object = MibTableColumn
cucsComputeMbTempStatsHistThresholded = _CucsComputeMbTempStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 23),
    _CucsComputeMbTempStatsHistThresholded_Type()
)
cucsComputeMbTempStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistThresholded.setStatus("current")
_CucsComputeMbTempStatsHistTimeCollected_Type = DateAndTime
_CucsComputeMbTempStatsHistTimeCollected_Object = MibTableColumn
cucsComputeMbTempStatsHistTimeCollected = _CucsComputeMbTempStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 17, 1, 24),
    _CucsComputeMbTempStatsHistTimeCollected_Type()
)
cucsComputeMbTempStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMbTempStatsHistTimeCollected.setStatus("current")
_CucsComputeMemoryUnitConstraintDefTable_Object = MibTable
cucsComputeMemoryUnitConstraintDefTable = _CucsComputeMemoryUnitConstraintDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 18)
)
if mibBuilder.loadTexts:
    cucsComputeMemoryUnitConstraintDefTable.setStatus("current")
_CucsComputeMemoryUnitConstraintDefEntry_Object = MibTableRow
cucsComputeMemoryUnitConstraintDefEntry = _CucsComputeMemoryUnitConstraintDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 18, 1)
)
cucsComputeMemoryUnitConstraintDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeMemoryUnitConstraintDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeMemoryUnitConstraintDefEntry.setStatus("current")
_CucsComputeMemoryUnitConstraintDefInstanceId_Type = CucsManagedObjectId
_CucsComputeMemoryUnitConstraintDefInstanceId_Object = MibTableColumn
cucsComputeMemoryUnitConstraintDefInstanceId = _CucsComputeMemoryUnitConstraintDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 18, 1, 1),
    _CucsComputeMemoryUnitConstraintDefInstanceId_Type()
)
cucsComputeMemoryUnitConstraintDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeMemoryUnitConstraintDefInstanceId.setStatus("current")
_CucsComputeMemoryUnitConstraintDefDn_Type = CucsManagedObjectDn
_CucsComputeMemoryUnitConstraintDefDn_Object = MibTableColumn
cucsComputeMemoryUnitConstraintDefDn = _CucsComputeMemoryUnitConstraintDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 18, 1, 2),
    _CucsComputeMemoryUnitConstraintDefDn_Type()
)
cucsComputeMemoryUnitConstraintDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryUnitConstraintDefDn.setStatus("current")
_CucsComputeMemoryUnitConstraintDefRn_Type = SnmpAdminString
_CucsComputeMemoryUnitConstraintDefRn_Object = MibTableColumn
cucsComputeMemoryUnitConstraintDefRn = _CucsComputeMemoryUnitConstraintDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 18, 1, 3),
    _CucsComputeMemoryUnitConstraintDefRn_Type()
)
cucsComputeMemoryUnitConstraintDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryUnitConstraintDefRn.setStatus("current")
_CucsComputeMemoryUnitConstraintDefDescr_Type = SnmpAdminString
_CucsComputeMemoryUnitConstraintDefDescr_Object = MibTableColumn
cucsComputeMemoryUnitConstraintDefDescr = _CucsComputeMemoryUnitConstraintDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 18, 1, 4),
    _CucsComputeMemoryUnitConstraintDefDescr_Type()
)
cucsComputeMemoryUnitConstraintDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryUnitConstraintDefDescr.setStatus("current")
_CucsComputeMemoryUnitConstraintDefIntId_Type = SnmpAdminString
_CucsComputeMemoryUnitConstraintDefIntId_Object = MibTableColumn
cucsComputeMemoryUnitConstraintDefIntId = _CucsComputeMemoryUnitConstraintDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 18, 1, 5),
    _CucsComputeMemoryUnitConstraintDefIntId_Type()
)
cucsComputeMemoryUnitConstraintDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryUnitConstraintDefIntId.setStatus("current")
_CucsComputeMemoryUnitConstraintDefName_Type = SnmpAdminString
_CucsComputeMemoryUnitConstraintDefName_Object = MibTableColumn
cucsComputeMemoryUnitConstraintDefName = _CucsComputeMemoryUnitConstraintDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 18, 1, 6),
    _CucsComputeMemoryUnitConstraintDefName_Type()
)
cucsComputeMemoryUnitConstraintDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryUnitConstraintDefName.setStatus("current")
_CucsComputeMemoryUnitConstraintDefType_Type = CucsComputeMemoryUnitConstraintType
_CucsComputeMemoryUnitConstraintDefType_Object = MibTableColumn
cucsComputeMemoryUnitConstraintDefType = _CucsComputeMemoryUnitConstraintDefType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 18, 1, 7),
    _CucsComputeMemoryUnitConstraintDefType_Type()
)
cucsComputeMemoryUnitConstraintDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryUnitConstraintDefType.setStatus("current")
_CucsComputeMemoryUnitConstraintDefRevisionModifier_Type = SnmpAdminString
_CucsComputeMemoryUnitConstraintDefRevisionModifier_Object = MibTableColumn
cucsComputeMemoryUnitConstraintDefRevisionModifier = _CucsComputeMemoryUnitConstraintDefRevisionModifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 18, 1, 8),
    _CucsComputeMemoryUnitConstraintDefRevisionModifier_Type()
)
cucsComputeMemoryUnitConstraintDefRevisionModifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryUnitConstraintDefRevisionModifier.setStatus("current")
_CucsComputeMemoryUnitConstraintDefPolicyLevel_Type = Gauge32
_CucsComputeMemoryUnitConstraintDefPolicyLevel_Object = MibTableColumn
cucsComputeMemoryUnitConstraintDefPolicyLevel = _CucsComputeMemoryUnitConstraintDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 18, 1, 9),
    _CucsComputeMemoryUnitConstraintDefPolicyLevel_Type()
)
cucsComputeMemoryUnitConstraintDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryUnitConstraintDefPolicyLevel.setStatus("current")
_CucsComputeMemoryUnitConstraintDefPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeMemoryUnitConstraintDefPolicyOwner_Object = MibTableColumn
cucsComputeMemoryUnitConstraintDefPolicyOwner = _CucsComputeMemoryUnitConstraintDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 18, 1, 10),
    _CucsComputeMemoryUnitConstraintDefPolicyOwner_Type()
)
cucsComputeMemoryUnitConstraintDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryUnitConstraintDefPolicyOwner.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTable_Object = MibTable
cucsComputePCIeFatalCompletionStatsTable = _CucsComputePCIeFatalCompletionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19)
)
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTable.setStatus("current")
_CucsComputePCIeFatalCompletionStatsEntry_Object = MibTableRow
cucsComputePCIeFatalCompletionStatsEntry = _CucsComputePCIeFatalCompletionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1)
)
cucsComputePCIeFatalCompletionStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePCIeFatalCompletionStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsEntry.setStatus("current")
_CucsComputePCIeFatalCompletionStatsInstanceId_Type = CucsManagedObjectId
_CucsComputePCIeFatalCompletionStatsInstanceId_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsInstanceId = _CucsComputePCIeFatalCompletionStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 1),
    _CucsComputePCIeFatalCompletionStatsInstanceId_Type()
)
cucsComputePCIeFatalCompletionStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsInstanceId.setStatus("current")
_CucsComputePCIeFatalCompletionStatsDn_Type = CucsManagedObjectDn
_CucsComputePCIeFatalCompletionStatsDn_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsDn = _CucsComputePCIeFatalCompletionStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 2),
    _CucsComputePCIeFatalCompletionStatsDn_Type()
)
cucsComputePCIeFatalCompletionStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsDn.setStatus("current")
_CucsComputePCIeFatalCompletionStatsRn_Type = SnmpAdminString
_CucsComputePCIeFatalCompletionStatsRn_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsRn = _CucsComputePCIeFatalCompletionStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 3),
    _CucsComputePCIeFatalCompletionStatsRn_Type()
)
cucsComputePCIeFatalCompletionStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsRn.setStatus("current")
_CucsComputePCIeFatalCompletionStatsAbortErrors_Type = Counter32
_CucsComputePCIeFatalCompletionStatsAbortErrors_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsAbortErrors = _CucsComputePCIeFatalCompletionStatsAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 4),
    _CucsComputePCIeFatalCompletionStatsAbortErrors_Type()
)
cucsComputePCIeFatalCompletionStatsAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsAbortErrors.setStatus("current")
_CucsComputePCIeFatalCompletionStatsAbortErrors15Min_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsAbortErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsAbortErrors15Min = _CucsComputePCIeFatalCompletionStatsAbortErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 5),
    _CucsComputePCIeFatalCompletionStatsAbortErrors15Min_Type()
)
cucsComputePCIeFatalCompletionStatsAbortErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsAbortErrors15Min.setStatus("current")
_CucsComputePCIeFatalCompletionStatsAbortErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsAbortErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsAbortErrors15MinH = _CucsComputePCIeFatalCompletionStatsAbortErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 6),
    _CucsComputePCIeFatalCompletionStatsAbortErrors15MinH_Type()
)
cucsComputePCIeFatalCompletionStatsAbortErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsAbortErrors15MinH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsAbortErrors1Day_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsAbortErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsAbortErrors1Day = _CucsComputePCIeFatalCompletionStatsAbortErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 7),
    _CucsComputePCIeFatalCompletionStatsAbortErrors1Day_Type()
)
cucsComputePCIeFatalCompletionStatsAbortErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsAbortErrors1Day.setStatus("current")
_CucsComputePCIeFatalCompletionStatsAbortErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsAbortErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsAbortErrors1DayH = _CucsComputePCIeFatalCompletionStatsAbortErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 8),
    _CucsComputePCIeFatalCompletionStatsAbortErrors1DayH_Type()
)
cucsComputePCIeFatalCompletionStatsAbortErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsAbortErrors1DayH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsAbortErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsAbortErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsAbortErrors1Hour = _CucsComputePCIeFatalCompletionStatsAbortErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 9),
    _CucsComputePCIeFatalCompletionStatsAbortErrors1Hour_Type()
)
cucsComputePCIeFatalCompletionStatsAbortErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsAbortErrors1Hour.setStatus("current")
_CucsComputePCIeFatalCompletionStatsAbortErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsAbortErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsAbortErrors1HourH = _CucsComputePCIeFatalCompletionStatsAbortErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 10),
    _CucsComputePCIeFatalCompletionStatsAbortErrors1HourH_Type()
)
cucsComputePCIeFatalCompletionStatsAbortErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsAbortErrors1HourH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsAbortErrors1Week_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsAbortErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsAbortErrors1Week = _CucsComputePCIeFatalCompletionStatsAbortErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 11),
    _CucsComputePCIeFatalCompletionStatsAbortErrors1Week_Type()
)
cucsComputePCIeFatalCompletionStatsAbortErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsAbortErrors1Week.setStatus("current")
_CucsComputePCIeFatalCompletionStatsAbortErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsAbortErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsAbortErrors1WeekH = _CucsComputePCIeFatalCompletionStatsAbortErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 12),
    _CucsComputePCIeFatalCompletionStatsAbortErrors1WeekH_Type()
)
cucsComputePCIeFatalCompletionStatsAbortErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsAbortErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTimeoutErrors_Type = Counter32
_CucsComputePCIeFatalCompletionStatsTimeoutErrors_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsTimeoutErrors = _CucsComputePCIeFatalCompletionStatsTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 13),
    _CucsComputePCIeFatalCompletionStatsTimeoutErrors_Type()
)
cucsComputePCIeFatalCompletionStatsTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTimeoutErrors.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTimeoutErrors15Min_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsTimeoutErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsTimeoutErrors15Min = _CucsComputePCIeFatalCompletionStatsTimeoutErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 14),
    _CucsComputePCIeFatalCompletionStatsTimeoutErrors15Min_Type()
)
cucsComputePCIeFatalCompletionStatsTimeoutErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTimeoutErrors15Min.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTimeoutErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsTimeoutErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsTimeoutErrors15MinH = _CucsComputePCIeFatalCompletionStatsTimeoutErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 15),
    _CucsComputePCIeFatalCompletionStatsTimeoutErrors15MinH_Type()
)
cucsComputePCIeFatalCompletionStatsTimeoutErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTimeoutErrors15MinH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTimeoutErrors1Day_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsTimeoutErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsTimeoutErrors1Day = _CucsComputePCIeFatalCompletionStatsTimeoutErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 16),
    _CucsComputePCIeFatalCompletionStatsTimeoutErrors1Day_Type()
)
cucsComputePCIeFatalCompletionStatsTimeoutErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTimeoutErrors1Day.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTimeoutErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsTimeoutErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsTimeoutErrors1DayH = _CucsComputePCIeFatalCompletionStatsTimeoutErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 17),
    _CucsComputePCIeFatalCompletionStatsTimeoutErrors1DayH_Type()
)
cucsComputePCIeFatalCompletionStatsTimeoutErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTimeoutErrors1DayH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTimeoutErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsTimeoutErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsTimeoutErrors1Hour = _CucsComputePCIeFatalCompletionStatsTimeoutErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 18),
    _CucsComputePCIeFatalCompletionStatsTimeoutErrors1Hour_Type()
)
cucsComputePCIeFatalCompletionStatsTimeoutErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTimeoutErrors1Hour.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTimeoutErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsTimeoutErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsTimeoutErrors1HourH = _CucsComputePCIeFatalCompletionStatsTimeoutErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 19),
    _CucsComputePCIeFatalCompletionStatsTimeoutErrors1HourH_Type()
)
cucsComputePCIeFatalCompletionStatsTimeoutErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTimeoutErrors1HourH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTimeoutErrors1Week_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsTimeoutErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsTimeoutErrors1Week = _CucsComputePCIeFatalCompletionStatsTimeoutErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 20),
    _CucsComputePCIeFatalCompletionStatsTimeoutErrors1Week_Type()
)
cucsComputePCIeFatalCompletionStatsTimeoutErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTimeoutErrors1Week.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTimeoutErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsTimeoutErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsTimeoutErrors1WeekH = _CucsComputePCIeFatalCompletionStatsTimeoutErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 21),
    _CucsComputePCIeFatalCompletionStatsTimeoutErrors1WeekH_Type()
)
cucsComputePCIeFatalCompletionStatsTimeoutErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTimeoutErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsIntervals_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsIntervals_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsIntervals = _CucsComputePCIeFatalCompletionStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 22),
    _CucsComputePCIeFatalCompletionStatsIntervals_Type()
)
cucsComputePCIeFatalCompletionStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsIntervals.setStatus("current")
_CucsComputePCIeFatalCompletionStatsSuspect_Type = TruthValue
_CucsComputePCIeFatalCompletionStatsSuspect_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsSuspect = _CucsComputePCIeFatalCompletionStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 23),
    _CucsComputePCIeFatalCompletionStatsSuspect_Type()
)
cucsComputePCIeFatalCompletionStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsSuspect.setStatus("current")
_CucsComputePCIeFatalCompletionStatsThresholded_Type = CucsComputePCIeFatalCompletionStatsThresholded
_CucsComputePCIeFatalCompletionStatsThresholded_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsThresholded = _CucsComputePCIeFatalCompletionStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 24),
    _CucsComputePCIeFatalCompletionStatsThresholded_Type()
)
cucsComputePCIeFatalCompletionStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsThresholded.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTimeCollected_Type = DateAndTime
_CucsComputePCIeFatalCompletionStatsTimeCollected_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsTimeCollected = _CucsComputePCIeFatalCompletionStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 25),
    _CucsComputePCIeFatalCompletionStatsTimeCollected_Type()
)
cucsComputePCIeFatalCompletionStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTimeCollected.setStatus("current")
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors_Type = Counter32
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsUnexpectedErrors = _CucsComputePCIeFatalCompletionStatsUnexpectedErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 26),
    _CucsComputePCIeFatalCompletionStatsUnexpectedErrors_Type()
)
cucsComputePCIeFatalCompletionStatsUnexpectedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsUnexpectedErrors.setStatus("current")
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors15Min_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsUnexpectedErrors15Min = _CucsComputePCIeFatalCompletionStatsUnexpectedErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 27),
    _CucsComputePCIeFatalCompletionStatsUnexpectedErrors15Min_Type()
)
cucsComputePCIeFatalCompletionStatsUnexpectedErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsUnexpectedErrors15Min.setStatus("current")
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsUnexpectedErrors15MinH = _CucsComputePCIeFatalCompletionStatsUnexpectedErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 28),
    _CucsComputePCIeFatalCompletionStatsUnexpectedErrors15MinH_Type()
)
cucsComputePCIeFatalCompletionStatsUnexpectedErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsUnexpectedErrors15MinH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors1Day_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Day = _CucsComputePCIeFatalCompletionStatsUnexpectedErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 29),
    _CucsComputePCIeFatalCompletionStatsUnexpectedErrors1Day_Type()
)
cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Day.setStatus("current")
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsUnexpectedErrors1DayH = _CucsComputePCIeFatalCompletionStatsUnexpectedErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 30),
    _CucsComputePCIeFatalCompletionStatsUnexpectedErrors1DayH_Type()
)
cucsComputePCIeFatalCompletionStatsUnexpectedErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsUnexpectedErrors1DayH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Hour = _CucsComputePCIeFatalCompletionStatsUnexpectedErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 31),
    _CucsComputePCIeFatalCompletionStatsUnexpectedErrors1Hour_Type()
)
cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Hour.setStatus("current")
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsUnexpectedErrors1HourH = _CucsComputePCIeFatalCompletionStatsUnexpectedErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 32),
    _CucsComputePCIeFatalCompletionStatsUnexpectedErrors1HourH_Type()
)
cucsComputePCIeFatalCompletionStatsUnexpectedErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsUnexpectedErrors1HourH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors1Week_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Week = _CucsComputePCIeFatalCompletionStatsUnexpectedErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 33),
    _CucsComputePCIeFatalCompletionStatsUnexpectedErrors1Week_Type()
)
cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Week.setStatus("current")
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH = _CucsComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 34),
    _CucsComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH_Type()
)
cucsComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsUpdate_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsUpdate_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsUpdate = _CucsComputePCIeFatalCompletionStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 35),
    _CucsComputePCIeFatalCompletionStatsUpdate_Type()
)
cucsComputePCIeFatalCompletionStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsUpdate.setStatus("current")
_CucsComputePCIeFatalCompletionStatsAbortErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsAbortErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsAbortErrors2Weeks = _CucsComputePCIeFatalCompletionStatsAbortErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 36),
    _CucsComputePCIeFatalCompletionStatsAbortErrors2Weeks_Type()
)
cucsComputePCIeFatalCompletionStatsAbortErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsAbortErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalCompletionStatsAbortErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsAbortErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsAbortErrors2WeeksH = _CucsComputePCIeFatalCompletionStatsAbortErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 37),
    _CucsComputePCIeFatalCompletionStatsAbortErrors2WeeksH_Type()
)
cucsComputePCIeFatalCompletionStatsAbortErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsAbortErrors2WeeksH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTimeoutErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsTimeoutErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsTimeoutErrors2Weeks = _CucsComputePCIeFatalCompletionStatsTimeoutErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 38),
    _CucsComputePCIeFatalCompletionStatsTimeoutErrors2Weeks_Type()
)
cucsComputePCIeFatalCompletionStatsTimeoutErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTimeoutErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH = _CucsComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 39),
    _CucsComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH_Type()
)
cucsComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH.setStatus("current")
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks = _CucsComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 40),
    _CucsComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks_Type()
)
cucsComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH = _CucsComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 19, 1, 41),
    _CucsComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH_Type()
)
cucsComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH.setStatus("current")
_CucsComputePCIeFatalProtocolStatsTable_Object = MibTable
cucsComputePCIeFatalProtocolStatsTable = _CucsComputePCIeFatalProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20)
)
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsTable.setStatus("current")
_CucsComputePCIeFatalProtocolStatsEntry_Object = MibTableRow
cucsComputePCIeFatalProtocolStatsEntry = _CucsComputePCIeFatalProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1)
)
cucsComputePCIeFatalProtocolStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePCIeFatalProtocolStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsEntry.setStatus("current")
_CucsComputePCIeFatalProtocolStatsInstanceId_Type = CucsManagedObjectId
_CucsComputePCIeFatalProtocolStatsInstanceId_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsInstanceId = _CucsComputePCIeFatalProtocolStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 1),
    _CucsComputePCIeFatalProtocolStatsInstanceId_Type()
)
cucsComputePCIeFatalProtocolStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsInstanceId.setStatus("current")
_CucsComputePCIeFatalProtocolStatsDn_Type = CucsManagedObjectDn
_CucsComputePCIeFatalProtocolStatsDn_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsDn = _CucsComputePCIeFatalProtocolStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 2),
    _CucsComputePCIeFatalProtocolStatsDn_Type()
)
cucsComputePCIeFatalProtocolStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsDn.setStatus("current")
_CucsComputePCIeFatalProtocolStatsRn_Type = SnmpAdminString
_CucsComputePCIeFatalProtocolStatsRn_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsRn = _CucsComputePCIeFatalProtocolStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 3),
    _CucsComputePCIeFatalProtocolStatsRn_Type()
)
cucsComputePCIeFatalProtocolStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsRn.setStatus("current")
_CucsComputePCIeFatalProtocolStatsDllpErrors_Type = Counter32
_CucsComputePCIeFatalProtocolStatsDllpErrors_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsDllpErrors = _CucsComputePCIeFatalProtocolStatsDllpErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 4),
    _CucsComputePCIeFatalProtocolStatsDllpErrors_Type()
)
cucsComputePCIeFatalProtocolStatsDllpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsDllpErrors.setStatus("current")
_CucsComputePCIeFatalProtocolStatsDllpErrors15Min_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsDllpErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsDllpErrors15Min = _CucsComputePCIeFatalProtocolStatsDllpErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 5),
    _CucsComputePCIeFatalProtocolStatsDllpErrors15Min_Type()
)
cucsComputePCIeFatalProtocolStatsDllpErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsDllpErrors15Min.setStatus("current")
_CucsComputePCIeFatalProtocolStatsDllpErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsDllpErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsDllpErrors15MinH = _CucsComputePCIeFatalProtocolStatsDllpErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 6),
    _CucsComputePCIeFatalProtocolStatsDllpErrors15MinH_Type()
)
cucsComputePCIeFatalProtocolStatsDllpErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsDllpErrors15MinH.setStatus("current")
_CucsComputePCIeFatalProtocolStatsDllpErrors1Day_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsDllpErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsDllpErrors1Day = _CucsComputePCIeFatalProtocolStatsDllpErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 7),
    _CucsComputePCIeFatalProtocolStatsDllpErrors1Day_Type()
)
cucsComputePCIeFatalProtocolStatsDllpErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsDllpErrors1Day.setStatus("current")
_CucsComputePCIeFatalProtocolStatsDllpErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsDllpErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsDllpErrors1DayH = _CucsComputePCIeFatalProtocolStatsDllpErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 8),
    _CucsComputePCIeFatalProtocolStatsDllpErrors1DayH_Type()
)
cucsComputePCIeFatalProtocolStatsDllpErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsDllpErrors1DayH.setStatus("current")
_CucsComputePCIeFatalProtocolStatsDllpErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsDllpErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsDllpErrors1Hour = _CucsComputePCIeFatalProtocolStatsDllpErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 9),
    _CucsComputePCIeFatalProtocolStatsDllpErrors1Hour_Type()
)
cucsComputePCIeFatalProtocolStatsDllpErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsDllpErrors1Hour.setStatus("current")
_CucsComputePCIeFatalProtocolStatsDllpErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsDllpErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsDllpErrors1HourH = _CucsComputePCIeFatalProtocolStatsDllpErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 10),
    _CucsComputePCIeFatalProtocolStatsDllpErrors1HourH_Type()
)
cucsComputePCIeFatalProtocolStatsDllpErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsDllpErrors1HourH.setStatus("current")
_CucsComputePCIeFatalProtocolStatsDllpErrors1Week_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsDllpErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsDllpErrors1Week = _CucsComputePCIeFatalProtocolStatsDllpErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 11),
    _CucsComputePCIeFatalProtocolStatsDllpErrors1Week_Type()
)
cucsComputePCIeFatalProtocolStatsDllpErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsDllpErrors1Week.setStatus("current")
_CucsComputePCIeFatalProtocolStatsDllpErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsDllpErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsDllpErrors1WeekH = _CucsComputePCIeFatalProtocolStatsDllpErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 12),
    _CucsComputePCIeFatalProtocolStatsDllpErrors1WeekH_Type()
)
cucsComputePCIeFatalProtocolStatsDllpErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsDllpErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalProtocolStatsFlowControlErrors_Type = Counter32
_CucsComputePCIeFatalProtocolStatsFlowControlErrors_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsFlowControlErrors = _CucsComputePCIeFatalProtocolStatsFlowControlErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 13),
    _CucsComputePCIeFatalProtocolStatsFlowControlErrors_Type()
)
cucsComputePCIeFatalProtocolStatsFlowControlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsFlowControlErrors.setStatus("current")
_CucsComputePCIeFatalProtocolStatsFlowControlErrors15Min_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsFlowControlErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsFlowControlErrors15Min = _CucsComputePCIeFatalProtocolStatsFlowControlErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 14),
    _CucsComputePCIeFatalProtocolStatsFlowControlErrors15Min_Type()
)
cucsComputePCIeFatalProtocolStatsFlowControlErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsFlowControlErrors15Min.setStatus("current")
_CucsComputePCIeFatalProtocolStatsFlowControlErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsFlowControlErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsFlowControlErrors15MinH = _CucsComputePCIeFatalProtocolStatsFlowControlErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 15),
    _CucsComputePCIeFatalProtocolStatsFlowControlErrors15MinH_Type()
)
cucsComputePCIeFatalProtocolStatsFlowControlErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsFlowControlErrors15MinH.setStatus("current")
_CucsComputePCIeFatalProtocolStatsFlowControlErrors1Day_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsFlowControlErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsFlowControlErrors1Day = _CucsComputePCIeFatalProtocolStatsFlowControlErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 16),
    _CucsComputePCIeFatalProtocolStatsFlowControlErrors1Day_Type()
)
cucsComputePCIeFatalProtocolStatsFlowControlErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsFlowControlErrors1Day.setStatus("current")
_CucsComputePCIeFatalProtocolStatsFlowControlErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsFlowControlErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsFlowControlErrors1DayH = _CucsComputePCIeFatalProtocolStatsFlowControlErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 17),
    _CucsComputePCIeFatalProtocolStatsFlowControlErrors1DayH_Type()
)
cucsComputePCIeFatalProtocolStatsFlowControlErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsFlowControlErrors1DayH.setStatus("current")
_CucsComputePCIeFatalProtocolStatsFlowControlErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsFlowControlErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsFlowControlErrors1Hour = _CucsComputePCIeFatalProtocolStatsFlowControlErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 18),
    _CucsComputePCIeFatalProtocolStatsFlowControlErrors1Hour_Type()
)
cucsComputePCIeFatalProtocolStatsFlowControlErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsFlowControlErrors1Hour.setStatus("current")
_CucsComputePCIeFatalProtocolStatsFlowControlErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsFlowControlErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsFlowControlErrors1HourH = _CucsComputePCIeFatalProtocolStatsFlowControlErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 19),
    _CucsComputePCIeFatalProtocolStatsFlowControlErrors1HourH_Type()
)
cucsComputePCIeFatalProtocolStatsFlowControlErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsFlowControlErrors1HourH.setStatus("current")
_CucsComputePCIeFatalProtocolStatsFlowControlErrors1Week_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsFlowControlErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsFlowControlErrors1Week = _CucsComputePCIeFatalProtocolStatsFlowControlErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 20),
    _CucsComputePCIeFatalProtocolStatsFlowControlErrors1Week_Type()
)
cucsComputePCIeFatalProtocolStatsFlowControlErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsFlowControlErrors1Week.setStatus("current")
_CucsComputePCIeFatalProtocolStatsFlowControlErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsFlowControlErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsFlowControlErrors1WeekH = _CucsComputePCIeFatalProtocolStatsFlowControlErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 21),
    _CucsComputePCIeFatalProtocolStatsFlowControlErrors1WeekH_Type()
)
cucsComputePCIeFatalProtocolStatsFlowControlErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsFlowControlErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalProtocolStatsIntervals_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsIntervals_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsIntervals = _CucsComputePCIeFatalProtocolStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 22),
    _CucsComputePCIeFatalProtocolStatsIntervals_Type()
)
cucsComputePCIeFatalProtocolStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsIntervals.setStatus("current")
_CucsComputePCIeFatalProtocolStatsSuspect_Type = TruthValue
_CucsComputePCIeFatalProtocolStatsSuspect_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsSuspect = _CucsComputePCIeFatalProtocolStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 23),
    _CucsComputePCIeFatalProtocolStatsSuspect_Type()
)
cucsComputePCIeFatalProtocolStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsSuspect.setStatus("current")
_CucsComputePCIeFatalProtocolStatsThresholded_Type = CucsComputePCIeFatalProtocolStatsThresholded
_CucsComputePCIeFatalProtocolStatsThresholded_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsThresholded = _CucsComputePCIeFatalProtocolStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 24),
    _CucsComputePCIeFatalProtocolStatsThresholded_Type()
)
cucsComputePCIeFatalProtocolStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsThresholded.setStatus("current")
_CucsComputePCIeFatalProtocolStatsTimeCollected_Type = DateAndTime
_CucsComputePCIeFatalProtocolStatsTimeCollected_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsTimeCollected = _CucsComputePCIeFatalProtocolStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 25),
    _CucsComputePCIeFatalProtocolStatsTimeCollected_Type()
)
cucsComputePCIeFatalProtocolStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsTimeCollected.setStatus("current")
_CucsComputePCIeFatalProtocolStatsUpdate_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsUpdate_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsUpdate = _CucsComputePCIeFatalProtocolStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 26),
    _CucsComputePCIeFatalProtocolStatsUpdate_Type()
)
cucsComputePCIeFatalProtocolStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsUpdate.setStatus("current")
_CucsComputePCIeFatalProtocolStatsDllpErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsDllpErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsDllpErrors2Weeks = _CucsComputePCIeFatalProtocolStatsDllpErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 27),
    _CucsComputePCIeFatalProtocolStatsDllpErrors2Weeks_Type()
)
cucsComputePCIeFatalProtocolStatsDllpErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsDllpErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalProtocolStatsDllpErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsDllpErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsDllpErrors2WeeksH = _CucsComputePCIeFatalProtocolStatsDllpErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 28),
    _CucsComputePCIeFatalProtocolStatsDllpErrors2WeeksH_Type()
)
cucsComputePCIeFatalProtocolStatsDllpErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsDllpErrors2WeeksH.setStatus("current")
_CucsComputePCIeFatalProtocolStatsFlowControlErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsFlowControlErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsFlowControlErrors2Weeks = _CucsComputePCIeFatalProtocolStatsFlowControlErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 29),
    _CucsComputePCIeFatalProtocolStatsFlowControlErrors2Weeks_Type()
)
cucsComputePCIeFatalProtocolStatsFlowControlErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsFlowControlErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH = _CucsComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 20, 1, 30),
    _CucsComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH_Type()
)
cucsComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsTable_Object = MibTable
cucsComputePCIeFatalReceiveStatsTable = _CucsComputePCIeFatalReceiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21)
)
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsTable.setStatus("current")
_CucsComputePCIeFatalReceiveStatsEntry_Object = MibTableRow
cucsComputePCIeFatalReceiveStatsEntry = _CucsComputePCIeFatalReceiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1)
)
cucsComputePCIeFatalReceiveStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePCIeFatalReceiveStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsEntry.setStatus("current")
_CucsComputePCIeFatalReceiveStatsInstanceId_Type = CucsManagedObjectId
_CucsComputePCIeFatalReceiveStatsInstanceId_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsInstanceId = _CucsComputePCIeFatalReceiveStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 1),
    _CucsComputePCIeFatalReceiveStatsInstanceId_Type()
)
cucsComputePCIeFatalReceiveStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsInstanceId.setStatus("current")
_CucsComputePCIeFatalReceiveStatsDn_Type = CucsManagedObjectDn
_CucsComputePCIeFatalReceiveStatsDn_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsDn = _CucsComputePCIeFatalReceiveStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 2),
    _CucsComputePCIeFatalReceiveStatsDn_Type()
)
cucsComputePCIeFatalReceiveStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsDn.setStatus("current")
_CucsComputePCIeFatalReceiveStatsRn_Type = SnmpAdminString
_CucsComputePCIeFatalReceiveStatsRn_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsRn = _CucsComputePCIeFatalReceiveStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 3),
    _CucsComputePCIeFatalReceiveStatsRn_Type()
)
cucsComputePCIeFatalReceiveStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsRn.setStatus("current")
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors_Type = Counter32
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors = _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 4),
    _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors_Type()
)
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsBufferOverflowErrors.setStatus("current")
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors15Min_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors15Min = _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 5),
    _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors15Min_Type()
)
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsBufferOverflowErrors15Min.setStatus("current")
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH = _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 6),
    _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH_Type()
)
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Day_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Day = _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 7),
    _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Day_Type()
)
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Day.setStatus("current")
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH = _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 8),
    _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH_Type()
)
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour = _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 9),
    _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour_Type()
)
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour.setStatus("current")
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH = _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 10),
    _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH_Type()
)
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Week_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Week = _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 11),
    _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Week_Type()
)
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Week.setStatus("current")
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH = _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 12),
    _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH_Type()
)
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrFatalErrors_Type = Counter32
_CucsComputePCIeFatalReceiveStatsErrFatalErrors_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrFatalErrors = _CucsComputePCIeFatalReceiveStatsErrFatalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 13),
    _CucsComputePCIeFatalReceiveStatsErrFatalErrors_Type()
)
cucsComputePCIeFatalReceiveStatsErrFatalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrFatalErrors.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrFatalErrors15Min_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrFatalErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrFatalErrors15Min = _CucsComputePCIeFatalReceiveStatsErrFatalErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 14),
    _CucsComputePCIeFatalReceiveStatsErrFatalErrors15Min_Type()
)
cucsComputePCIeFatalReceiveStatsErrFatalErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrFatalErrors15Min.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrFatalErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrFatalErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrFatalErrors15MinH = _CucsComputePCIeFatalReceiveStatsErrFatalErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 15),
    _CucsComputePCIeFatalReceiveStatsErrFatalErrors15MinH_Type()
)
cucsComputePCIeFatalReceiveStatsErrFatalErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrFatalErrors15MinH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrFatalErrors1Day_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrFatalErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrFatalErrors1Day = _CucsComputePCIeFatalReceiveStatsErrFatalErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 16),
    _CucsComputePCIeFatalReceiveStatsErrFatalErrors1Day_Type()
)
cucsComputePCIeFatalReceiveStatsErrFatalErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrFatalErrors1Day.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrFatalErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrFatalErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrFatalErrors1DayH = _CucsComputePCIeFatalReceiveStatsErrFatalErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 17),
    _CucsComputePCIeFatalReceiveStatsErrFatalErrors1DayH_Type()
)
cucsComputePCIeFatalReceiveStatsErrFatalErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrFatalErrors1DayH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrFatalErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrFatalErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrFatalErrors1Hour = _CucsComputePCIeFatalReceiveStatsErrFatalErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 18),
    _CucsComputePCIeFatalReceiveStatsErrFatalErrors1Hour_Type()
)
cucsComputePCIeFatalReceiveStatsErrFatalErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrFatalErrors1Hour.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrFatalErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrFatalErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrFatalErrors1HourH = _CucsComputePCIeFatalReceiveStatsErrFatalErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 19),
    _CucsComputePCIeFatalReceiveStatsErrFatalErrors1HourH_Type()
)
cucsComputePCIeFatalReceiveStatsErrFatalErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrFatalErrors1HourH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrFatalErrors1Week_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrFatalErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrFatalErrors1Week = _CucsComputePCIeFatalReceiveStatsErrFatalErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 20),
    _CucsComputePCIeFatalReceiveStatsErrFatalErrors1Week_Type()
)
cucsComputePCIeFatalReceiveStatsErrFatalErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrFatalErrors1Week.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrFatalErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrFatalErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrFatalErrors1WeekH = _CucsComputePCIeFatalReceiveStatsErrFatalErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 21),
    _CucsComputePCIeFatalReceiveStatsErrFatalErrors1WeekH_Type()
)
cucsComputePCIeFatalReceiveStatsErrFatalErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrFatalErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors_Type = Counter32
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors = _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 22),
    _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors_Type()
)
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrNonFatalErrors.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors15Min_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors15Min = _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 23),
    _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors15Min_Type()
)
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrNonFatalErrors15Min.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH = _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 24),
    _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH_Type()
)
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Day_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Day = _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 25),
    _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Day_Type()
)
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Day.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH = _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 26),
    _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH_Type()
)
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour = _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 27),
    _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour_Type()
)
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH = _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 28),
    _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH_Type()
)
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Week_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Week = _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 29),
    _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Week_Type()
)
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Week.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH = _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 30),
    _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH_Type()
)
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsIntervals_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsIntervals_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsIntervals = _CucsComputePCIeFatalReceiveStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 31),
    _CucsComputePCIeFatalReceiveStatsIntervals_Type()
)
cucsComputePCIeFatalReceiveStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsIntervals.setStatus("current")
_CucsComputePCIeFatalReceiveStatsSuspect_Type = TruthValue
_CucsComputePCIeFatalReceiveStatsSuspect_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsSuspect = _CucsComputePCIeFatalReceiveStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 32),
    _CucsComputePCIeFatalReceiveStatsSuspect_Type()
)
cucsComputePCIeFatalReceiveStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsSuspect.setStatus("current")
_CucsComputePCIeFatalReceiveStatsThresholded_Type = CucsComputePCIeFatalReceiveStatsThresholded
_CucsComputePCIeFatalReceiveStatsThresholded_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsThresholded = _CucsComputePCIeFatalReceiveStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 33),
    _CucsComputePCIeFatalReceiveStatsThresholded_Type()
)
cucsComputePCIeFatalReceiveStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsThresholded.setStatus("current")
_CucsComputePCIeFatalReceiveStatsTimeCollected_Type = DateAndTime
_CucsComputePCIeFatalReceiveStatsTimeCollected_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsTimeCollected = _CucsComputePCIeFatalReceiveStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 34),
    _CucsComputePCIeFatalReceiveStatsTimeCollected_Type()
)
cucsComputePCIeFatalReceiveStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsTimeCollected.setStatus("current")
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors_Type = Counter32
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors = _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 35),
    _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors_Type()
)
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors.setStatus("current")
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min = _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 36),
    _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min_Type()
)
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min.setStatus("current")
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH = _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 37),
    _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH_Type()
)
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day = _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 38),
    _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day_Type()
)
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day.setStatus("current")
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH = _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 39),
    _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH_Type()
)
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour = _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 40),
    _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour_Type()
)
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour.setStatus("current")
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH = _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 41),
    _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH_Type()
)
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week = _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 42),
    _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week_Type()
)
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week.setStatus("current")
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH = _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 43),
    _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH_Type()
)
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsUpdate_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsUpdate_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsUpdate = _CucsComputePCIeFatalReceiveStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 44),
    _CucsComputePCIeFatalReceiveStatsUpdate_Type()
)
cucsComputePCIeFatalReceiveStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsUpdate.setStatus("current")
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks = _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 45),
    _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks_Type()
)
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH = _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 46),
    _CucsComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH_Type()
)
cucsComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrFatalErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrFatalErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrFatalErrors2Weeks = _CucsComputePCIeFatalReceiveStatsErrFatalErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 47),
    _CucsComputePCIeFatalReceiveStatsErrFatalErrors2Weeks_Type()
)
cucsComputePCIeFatalReceiveStatsErrFatalErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrFatalErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH = _CucsComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 48),
    _CucsComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH_Type()
)
cucsComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks = _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 49),
    _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks_Type()
)
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH = _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 50),
    _CucsComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH_Type()
)
cucsComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH.setStatus("current")
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks = _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 51),
    _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks_Type()
)
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH = _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 21, 1, 52),
    _CucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH_Type()
)
cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH.setStatus("current")
_CucsComputePCIeFatalStatsTable_Object = MibTable
cucsComputePCIeFatalStatsTable = _CucsComputePCIeFatalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22)
)
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsTable.setStatus("current")
_CucsComputePCIeFatalStatsEntry_Object = MibTableRow
cucsComputePCIeFatalStatsEntry = _CucsComputePCIeFatalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1)
)
cucsComputePCIeFatalStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePCIeFatalStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsEntry.setStatus("current")
_CucsComputePCIeFatalStatsInstanceId_Type = CucsManagedObjectId
_CucsComputePCIeFatalStatsInstanceId_Object = MibTableColumn
cucsComputePCIeFatalStatsInstanceId = _CucsComputePCIeFatalStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 1),
    _CucsComputePCIeFatalStatsInstanceId_Type()
)
cucsComputePCIeFatalStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsInstanceId.setStatus("current")
_CucsComputePCIeFatalStatsDn_Type = CucsManagedObjectDn
_CucsComputePCIeFatalStatsDn_Object = MibTableColumn
cucsComputePCIeFatalStatsDn = _CucsComputePCIeFatalStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 2),
    _CucsComputePCIeFatalStatsDn_Type()
)
cucsComputePCIeFatalStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsDn.setStatus("current")
_CucsComputePCIeFatalStatsRn_Type = SnmpAdminString
_CucsComputePCIeFatalStatsRn_Object = MibTableColumn
cucsComputePCIeFatalStatsRn = _CucsComputePCIeFatalStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 3),
    _CucsComputePCIeFatalStatsRn_Type()
)
cucsComputePCIeFatalStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsRn.setStatus("current")
_CucsComputePCIeFatalStatsAcsViolationErrors_Type = Counter32
_CucsComputePCIeFatalStatsAcsViolationErrors_Object = MibTableColumn
cucsComputePCIeFatalStatsAcsViolationErrors = _CucsComputePCIeFatalStatsAcsViolationErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 4),
    _CucsComputePCIeFatalStatsAcsViolationErrors_Type()
)
cucsComputePCIeFatalStatsAcsViolationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsAcsViolationErrors.setStatus("current")
_CucsComputePCIeFatalStatsAcsViolationErrors15Min_Type = Gauge32
_CucsComputePCIeFatalStatsAcsViolationErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalStatsAcsViolationErrors15Min = _CucsComputePCIeFatalStatsAcsViolationErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 5),
    _CucsComputePCIeFatalStatsAcsViolationErrors15Min_Type()
)
cucsComputePCIeFatalStatsAcsViolationErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsAcsViolationErrors15Min.setStatus("current")
_CucsComputePCIeFatalStatsAcsViolationErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalStatsAcsViolationErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalStatsAcsViolationErrors15MinH = _CucsComputePCIeFatalStatsAcsViolationErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 6),
    _CucsComputePCIeFatalStatsAcsViolationErrors15MinH_Type()
)
cucsComputePCIeFatalStatsAcsViolationErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsAcsViolationErrors15MinH.setStatus("current")
_CucsComputePCIeFatalStatsAcsViolationErrors1Day_Type = Gauge32
_CucsComputePCIeFatalStatsAcsViolationErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalStatsAcsViolationErrors1Day = _CucsComputePCIeFatalStatsAcsViolationErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 7),
    _CucsComputePCIeFatalStatsAcsViolationErrors1Day_Type()
)
cucsComputePCIeFatalStatsAcsViolationErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsAcsViolationErrors1Day.setStatus("current")
_CucsComputePCIeFatalStatsAcsViolationErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalStatsAcsViolationErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalStatsAcsViolationErrors1DayH = _CucsComputePCIeFatalStatsAcsViolationErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 8),
    _CucsComputePCIeFatalStatsAcsViolationErrors1DayH_Type()
)
cucsComputePCIeFatalStatsAcsViolationErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsAcsViolationErrors1DayH.setStatus("current")
_CucsComputePCIeFatalStatsAcsViolationErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalStatsAcsViolationErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalStatsAcsViolationErrors1Hour = _CucsComputePCIeFatalStatsAcsViolationErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 9),
    _CucsComputePCIeFatalStatsAcsViolationErrors1Hour_Type()
)
cucsComputePCIeFatalStatsAcsViolationErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsAcsViolationErrors1Hour.setStatus("current")
_CucsComputePCIeFatalStatsAcsViolationErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalStatsAcsViolationErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalStatsAcsViolationErrors1HourH = _CucsComputePCIeFatalStatsAcsViolationErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 10),
    _CucsComputePCIeFatalStatsAcsViolationErrors1HourH_Type()
)
cucsComputePCIeFatalStatsAcsViolationErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsAcsViolationErrors1HourH.setStatus("current")
_CucsComputePCIeFatalStatsAcsViolationErrors1Week_Type = Gauge32
_CucsComputePCIeFatalStatsAcsViolationErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalStatsAcsViolationErrors1Week = _CucsComputePCIeFatalStatsAcsViolationErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 11),
    _CucsComputePCIeFatalStatsAcsViolationErrors1Week_Type()
)
cucsComputePCIeFatalStatsAcsViolationErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsAcsViolationErrors1Week.setStatus("current")
_CucsComputePCIeFatalStatsAcsViolationErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalStatsAcsViolationErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalStatsAcsViolationErrors1WeekH = _CucsComputePCIeFatalStatsAcsViolationErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 12),
    _CucsComputePCIeFatalStatsAcsViolationErrors1WeekH_Type()
)
cucsComputePCIeFatalStatsAcsViolationErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsAcsViolationErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalStatsIntervals_Type = Gauge32
_CucsComputePCIeFatalStatsIntervals_Object = MibTableColumn
cucsComputePCIeFatalStatsIntervals = _CucsComputePCIeFatalStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 13),
    _CucsComputePCIeFatalStatsIntervals_Type()
)
cucsComputePCIeFatalStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsIntervals.setStatus("current")
_CucsComputePCIeFatalStatsMalformedTLPErrors_Type = Counter32
_CucsComputePCIeFatalStatsMalformedTLPErrors_Object = MibTableColumn
cucsComputePCIeFatalStatsMalformedTLPErrors = _CucsComputePCIeFatalStatsMalformedTLPErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 14),
    _CucsComputePCIeFatalStatsMalformedTLPErrors_Type()
)
cucsComputePCIeFatalStatsMalformedTLPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsMalformedTLPErrors.setStatus("current")
_CucsComputePCIeFatalStatsMalformedTLPErrors15Min_Type = Gauge32
_CucsComputePCIeFatalStatsMalformedTLPErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalStatsMalformedTLPErrors15Min = _CucsComputePCIeFatalStatsMalformedTLPErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 15),
    _CucsComputePCIeFatalStatsMalformedTLPErrors15Min_Type()
)
cucsComputePCIeFatalStatsMalformedTLPErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsMalformedTLPErrors15Min.setStatus("current")
_CucsComputePCIeFatalStatsMalformedTLPErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalStatsMalformedTLPErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalStatsMalformedTLPErrors15MinH = _CucsComputePCIeFatalStatsMalformedTLPErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 16),
    _CucsComputePCIeFatalStatsMalformedTLPErrors15MinH_Type()
)
cucsComputePCIeFatalStatsMalformedTLPErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsMalformedTLPErrors15MinH.setStatus("current")
_CucsComputePCIeFatalStatsMalformedTLPErrors1Day_Type = Gauge32
_CucsComputePCIeFatalStatsMalformedTLPErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalStatsMalformedTLPErrors1Day = _CucsComputePCIeFatalStatsMalformedTLPErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 17),
    _CucsComputePCIeFatalStatsMalformedTLPErrors1Day_Type()
)
cucsComputePCIeFatalStatsMalformedTLPErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsMalformedTLPErrors1Day.setStatus("current")
_CucsComputePCIeFatalStatsMalformedTLPErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalStatsMalformedTLPErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalStatsMalformedTLPErrors1DayH = _CucsComputePCIeFatalStatsMalformedTLPErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 18),
    _CucsComputePCIeFatalStatsMalformedTLPErrors1DayH_Type()
)
cucsComputePCIeFatalStatsMalformedTLPErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsMalformedTLPErrors1DayH.setStatus("current")
_CucsComputePCIeFatalStatsMalformedTLPErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalStatsMalformedTLPErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalStatsMalformedTLPErrors1Hour = _CucsComputePCIeFatalStatsMalformedTLPErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 19),
    _CucsComputePCIeFatalStatsMalformedTLPErrors1Hour_Type()
)
cucsComputePCIeFatalStatsMalformedTLPErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsMalformedTLPErrors1Hour.setStatus("current")
_CucsComputePCIeFatalStatsMalformedTLPErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalStatsMalformedTLPErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalStatsMalformedTLPErrors1HourH = _CucsComputePCIeFatalStatsMalformedTLPErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 20),
    _CucsComputePCIeFatalStatsMalformedTLPErrors1HourH_Type()
)
cucsComputePCIeFatalStatsMalformedTLPErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsMalformedTLPErrors1HourH.setStatus("current")
_CucsComputePCIeFatalStatsMalformedTLPErrors1Week_Type = Gauge32
_CucsComputePCIeFatalStatsMalformedTLPErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalStatsMalformedTLPErrors1Week = _CucsComputePCIeFatalStatsMalformedTLPErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 21),
    _CucsComputePCIeFatalStatsMalformedTLPErrors1Week_Type()
)
cucsComputePCIeFatalStatsMalformedTLPErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsMalformedTLPErrors1Week.setStatus("current")
_CucsComputePCIeFatalStatsMalformedTLPErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalStatsMalformedTLPErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalStatsMalformedTLPErrors1WeekH = _CucsComputePCIeFatalStatsMalformedTLPErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 22),
    _CucsComputePCIeFatalStatsMalformedTLPErrors1WeekH_Type()
)
cucsComputePCIeFatalStatsMalformedTLPErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsMalformedTLPErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalStatsPoisonedTLPErrors_Type = Counter32
_CucsComputePCIeFatalStatsPoisonedTLPErrors_Object = MibTableColumn
cucsComputePCIeFatalStatsPoisonedTLPErrors = _CucsComputePCIeFatalStatsPoisonedTLPErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 23),
    _CucsComputePCIeFatalStatsPoisonedTLPErrors_Type()
)
cucsComputePCIeFatalStatsPoisonedTLPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsPoisonedTLPErrors.setStatus("current")
_CucsComputePCIeFatalStatsPoisonedTLPErrors15Min_Type = Gauge32
_CucsComputePCIeFatalStatsPoisonedTLPErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalStatsPoisonedTLPErrors15Min = _CucsComputePCIeFatalStatsPoisonedTLPErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 24),
    _CucsComputePCIeFatalStatsPoisonedTLPErrors15Min_Type()
)
cucsComputePCIeFatalStatsPoisonedTLPErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsPoisonedTLPErrors15Min.setStatus("current")
_CucsComputePCIeFatalStatsPoisonedTLPErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalStatsPoisonedTLPErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalStatsPoisonedTLPErrors15MinH = _CucsComputePCIeFatalStatsPoisonedTLPErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 25),
    _CucsComputePCIeFatalStatsPoisonedTLPErrors15MinH_Type()
)
cucsComputePCIeFatalStatsPoisonedTLPErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsPoisonedTLPErrors15MinH.setStatus("current")
_CucsComputePCIeFatalStatsPoisonedTLPErrors1Day_Type = Gauge32
_CucsComputePCIeFatalStatsPoisonedTLPErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalStatsPoisonedTLPErrors1Day = _CucsComputePCIeFatalStatsPoisonedTLPErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 26),
    _CucsComputePCIeFatalStatsPoisonedTLPErrors1Day_Type()
)
cucsComputePCIeFatalStatsPoisonedTLPErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsPoisonedTLPErrors1Day.setStatus("current")
_CucsComputePCIeFatalStatsPoisonedTLPErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalStatsPoisonedTLPErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalStatsPoisonedTLPErrors1DayH = _CucsComputePCIeFatalStatsPoisonedTLPErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 27),
    _CucsComputePCIeFatalStatsPoisonedTLPErrors1DayH_Type()
)
cucsComputePCIeFatalStatsPoisonedTLPErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsPoisonedTLPErrors1DayH.setStatus("current")
_CucsComputePCIeFatalStatsPoisonedTLPErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalStatsPoisonedTLPErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalStatsPoisonedTLPErrors1Hour = _CucsComputePCIeFatalStatsPoisonedTLPErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 28),
    _CucsComputePCIeFatalStatsPoisonedTLPErrors1Hour_Type()
)
cucsComputePCIeFatalStatsPoisonedTLPErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsPoisonedTLPErrors1Hour.setStatus("current")
_CucsComputePCIeFatalStatsPoisonedTLPErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalStatsPoisonedTLPErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalStatsPoisonedTLPErrors1HourH = _CucsComputePCIeFatalStatsPoisonedTLPErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 29),
    _CucsComputePCIeFatalStatsPoisonedTLPErrors1HourH_Type()
)
cucsComputePCIeFatalStatsPoisonedTLPErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsPoisonedTLPErrors1HourH.setStatus("current")
_CucsComputePCIeFatalStatsPoisonedTLPErrors1Week_Type = Gauge32
_CucsComputePCIeFatalStatsPoisonedTLPErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalStatsPoisonedTLPErrors1Week = _CucsComputePCIeFatalStatsPoisonedTLPErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 30),
    _CucsComputePCIeFatalStatsPoisonedTLPErrors1Week_Type()
)
cucsComputePCIeFatalStatsPoisonedTLPErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsPoisonedTLPErrors1Week.setStatus("current")
_CucsComputePCIeFatalStatsPoisonedTLPErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalStatsPoisonedTLPErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalStatsPoisonedTLPErrors1WeekH = _CucsComputePCIeFatalStatsPoisonedTLPErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 31),
    _CucsComputePCIeFatalStatsPoisonedTLPErrors1WeekH_Type()
)
cucsComputePCIeFatalStatsPoisonedTLPErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsPoisonedTLPErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors_Type = Counter32
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors_Object = MibTableColumn
cucsComputePCIeFatalStatsSurpriseLinkDownErrors = _CucsComputePCIeFatalStatsSurpriseLinkDownErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 32),
    _CucsComputePCIeFatalStatsSurpriseLinkDownErrors_Type()
)
cucsComputePCIeFatalStatsSurpriseLinkDownErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsSurpriseLinkDownErrors.setStatus("current")
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors15Min_Type = Gauge32
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors15Min_Object = MibTableColumn
cucsComputePCIeFatalStatsSurpriseLinkDownErrors15Min = _CucsComputePCIeFatalStatsSurpriseLinkDownErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 33),
    _CucsComputePCIeFatalStatsSurpriseLinkDownErrors15Min_Type()
)
cucsComputePCIeFatalStatsSurpriseLinkDownErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsSurpriseLinkDownErrors15Min.setStatus("current")
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors15MinH_Type = Gauge32
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors15MinH_Object = MibTableColumn
cucsComputePCIeFatalStatsSurpriseLinkDownErrors15MinH = _CucsComputePCIeFatalStatsSurpriseLinkDownErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 34),
    _CucsComputePCIeFatalStatsSurpriseLinkDownErrors15MinH_Type()
)
cucsComputePCIeFatalStatsSurpriseLinkDownErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsSurpriseLinkDownErrors15MinH.setStatus("current")
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors1Day_Type = Gauge32
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors1Day_Object = MibTableColumn
cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Day = _CucsComputePCIeFatalStatsSurpriseLinkDownErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 35),
    _CucsComputePCIeFatalStatsSurpriseLinkDownErrors1Day_Type()
)
cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Day.setStatus("current")
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors1DayH_Type = Gauge32
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors1DayH_Object = MibTableColumn
cucsComputePCIeFatalStatsSurpriseLinkDownErrors1DayH = _CucsComputePCIeFatalStatsSurpriseLinkDownErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 36),
    _CucsComputePCIeFatalStatsSurpriseLinkDownErrors1DayH_Type()
)
cucsComputePCIeFatalStatsSurpriseLinkDownErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsSurpriseLinkDownErrors1DayH.setStatus("current")
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors1Hour_Type = Gauge32
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors1Hour_Object = MibTableColumn
cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Hour = _CucsComputePCIeFatalStatsSurpriseLinkDownErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 37),
    _CucsComputePCIeFatalStatsSurpriseLinkDownErrors1Hour_Type()
)
cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Hour.setStatus("current")
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors1HourH_Type = Gauge32
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors1HourH_Object = MibTableColumn
cucsComputePCIeFatalStatsSurpriseLinkDownErrors1HourH = _CucsComputePCIeFatalStatsSurpriseLinkDownErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 38),
    _CucsComputePCIeFatalStatsSurpriseLinkDownErrors1HourH_Type()
)
cucsComputePCIeFatalStatsSurpriseLinkDownErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsSurpriseLinkDownErrors1HourH.setStatus("current")
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors1Week_Type = Gauge32
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors1Week_Object = MibTableColumn
cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Week = _CucsComputePCIeFatalStatsSurpriseLinkDownErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 39),
    _CucsComputePCIeFatalStatsSurpriseLinkDownErrors1Week_Type()
)
cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Week.setStatus("current")
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH_Type = Gauge32
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH_Object = MibTableColumn
cucsComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH = _CucsComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 40),
    _CucsComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH_Type()
)
cucsComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH.setStatus("current")
_CucsComputePCIeFatalStatsSuspect_Type = TruthValue
_CucsComputePCIeFatalStatsSuspect_Object = MibTableColumn
cucsComputePCIeFatalStatsSuspect = _CucsComputePCIeFatalStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 41),
    _CucsComputePCIeFatalStatsSuspect_Type()
)
cucsComputePCIeFatalStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsSuspect.setStatus("current")
_CucsComputePCIeFatalStatsThresholded_Type = CucsComputePCIeFatalStatsThresholded
_CucsComputePCIeFatalStatsThresholded_Object = MibTableColumn
cucsComputePCIeFatalStatsThresholded = _CucsComputePCIeFatalStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 42),
    _CucsComputePCIeFatalStatsThresholded_Type()
)
cucsComputePCIeFatalStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsThresholded.setStatus("current")
_CucsComputePCIeFatalStatsTimeCollected_Type = DateAndTime
_CucsComputePCIeFatalStatsTimeCollected_Object = MibTableColumn
cucsComputePCIeFatalStatsTimeCollected = _CucsComputePCIeFatalStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 43),
    _CucsComputePCIeFatalStatsTimeCollected_Type()
)
cucsComputePCIeFatalStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsTimeCollected.setStatus("current")
_CucsComputePCIeFatalStatsUpdate_Type = Gauge32
_CucsComputePCIeFatalStatsUpdate_Object = MibTableColumn
cucsComputePCIeFatalStatsUpdate = _CucsComputePCIeFatalStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 44),
    _CucsComputePCIeFatalStatsUpdate_Type()
)
cucsComputePCIeFatalStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsUpdate.setStatus("current")
_CucsComputePCIeFatalStatsAcsViolationErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalStatsAcsViolationErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalStatsAcsViolationErrors2Weeks = _CucsComputePCIeFatalStatsAcsViolationErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 45),
    _CucsComputePCIeFatalStatsAcsViolationErrors2Weeks_Type()
)
cucsComputePCIeFatalStatsAcsViolationErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsAcsViolationErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalStatsAcsViolationErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalStatsAcsViolationErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalStatsAcsViolationErrors2WeeksH = _CucsComputePCIeFatalStatsAcsViolationErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 46),
    _CucsComputePCIeFatalStatsAcsViolationErrors2WeeksH_Type()
)
cucsComputePCIeFatalStatsAcsViolationErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsAcsViolationErrors2WeeksH.setStatus("current")
_CucsComputePCIeFatalStatsMalformedTLPErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalStatsMalformedTLPErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalStatsMalformedTLPErrors2Weeks = _CucsComputePCIeFatalStatsMalformedTLPErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 47),
    _CucsComputePCIeFatalStatsMalformedTLPErrors2Weeks_Type()
)
cucsComputePCIeFatalStatsMalformedTLPErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsMalformedTLPErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalStatsMalformedTLPErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalStatsMalformedTLPErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalStatsMalformedTLPErrors2WeeksH = _CucsComputePCIeFatalStatsMalformedTLPErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 48),
    _CucsComputePCIeFatalStatsMalformedTLPErrors2WeeksH_Type()
)
cucsComputePCIeFatalStatsMalformedTLPErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsMalformedTLPErrors2WeeksH.setStatus("current")
_CucsComputePCIeFatalStatsPoisonedTLPErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalStatsPoisonedTLPErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalStatsPoisonedTLPErrors2Weeks = _CucsComputePCIeFatalStatsPoisonedTLPErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 49),
    _CucsComputePCIeFatalStatsPoisonedTLPErrors2Weeks_Type()
)
cucsComputePCIeFatalStatsPoisonedTLPErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsPoisonedTLPErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalStatsPoisonedTLPErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalStatsPoisonedTLPErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalStatsPoisonedTLPErrors2WeeksH = _CucsComputePCIeFatalStatsPoisonedTLPErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 50),
    _CucsComputePCIeFatalStatsPoisonedTLPErrors2WeeksH_Type()
)
cucsComputePCIeFatalStatsPoisonedTLPErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsPoisonedTLPErrors2WeeksH.setStatus("current")
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks_Type = Gauge32
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks_Object = MibTableColumn
cucsComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks = _CucsComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 51),
    _CucsComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks_Type()
)
cucsComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks.setStatus("current")
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH_Type = Gauge32
_CucsComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH_Object = MibTableColumn
cucsComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH = _CucsComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 22, 1, 52),
    _CucsComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH_Type()
)
cucsComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH.setStatus("current")
_CucsComputePciCapTable_Object = MibTable
cucsComputePciCapTable = _CucsComputePciCapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 23)
)
if mibBuilder.loadTexts:
    cucsComputePciCapTable.setStatus("current")
_CucsComputePciCapEntry_Object = MibTableRow
cucsComputePciCapEntry = _CucsComputePciCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 23, 1)
)
cucsComputePciCapEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePciCapInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePciCapEntry.setStatus("current")
_CucsComputePciCapInstanceId_Type = CucsManagedObjectId
_CucsComputePciCapInstanceId_Object = MibTableColumn
cucsComputePciCapInstanceId = _CucsComputePciCapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 23, 1, 1),
    _CucsComputePciCapInstanceId_Type()
)
cucsComputePciCapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePciCapInstanceId.setStatus("current")
_CucsComputePciCapDn_Type = CucsManagedObjectDn
_CucsComputePciCapDn_Object = MibTableColumn
cucsComputePciCapDn = _CucsComputePciCapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 23, 1, 2),
    _CucsComputePciCapDn_Type()
)
cucsComputePciCapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciCapDn.setStatus("current")
_CucsComputePciCapRn_Type = SnmpAdminString
_CucsComputePciCapRn_Object = MibTableColumn
cucsComputePciCapRn = _CucsComputePciCapRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 23, 1, 3),
    _CucsComputePciCapRn_Type()
)
cucsComputePciCapRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciCapRn.setStatus("current")
_CucsComputePciCapNumOfPhysSlots_Type = Gauge32
_CucsComputePciCapNumOfPhysSlots_Object = MibTableColumn
cucsComputePciCapNumOfPhysSlots = _CucsComputePciCapNumOfPhysSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 23, 1, 4),
    _CucsComputePciCapNumOfPhysSlots_Type()
)
cucsComputePciCapNumOfPhysSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciCapNumOfPhysSlots.setStatus("current")
_CucsComputePciCapOrder_Type = CucsComputePciCapOrder
_CucsComputePciCapOrder_Object = MibTableColumn
cucsComputePciCapOrder = _CucsComputePciCapOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 23, 1, 5),
    _CucsComputePciCapOrder_Type()
)
cucsComputePciCapOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciCapOrder.setStatus("current")
_CucsComputePciCapStartsWith_Type = Gauge32
_CucsComputePciCapStartsWith_Object = MibTableColumn
cucsComputePciCapStartsWith = _CucsComputePciCapStartsWith_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 23, 1, 6),
    _CucsComputePciCapStartsWith_Type()
)
cucsComputePciCapStartsWith.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciCapStartsWith.setStatus("current")
_CucsComputePciCapMaxBusIdPerSlot_Type = Gauge32
_CucsComputePciCapMaxBusIdPerSlot_Object = MibTableColumn
cucsComputePciCapMaxBusIdPerSlot = _CucsComputePciCapMaxBusIdPerSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 23, 1, 7),
    _CucsComputePciCapMaxBusIdPerSlot_Type()
)
cucsComputePciCapMaxBusIdPerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciCapMaxBusIdPerSlot.setStatus("current")
_CucsComputePhysicalFsmTaskTable_Object = MibTable
cucsComputePhysicalFsmTaskTable = _CucsComputePhysicalFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 24)
)
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmTaskTable.setStatus("current")
_CucsComputePhysicalFsmTaskEntry_Object = MibTableRow
cucsComputePhysicalFsmTaskEntry = _CucsComputePhysicalFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 24, 1)
)
cucsComputePhysicalFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePhysicalFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmTaskEntry.setStatus("current")
_CucsComputePhysicalFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsComputePhysicalFsmTaskInstanceId_Object = MibTableColumn
cucsComputePhysicalFsmTaskInstanceId = _CucsComputePhysicalFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 24, 1, 1),
    _CucsComputePhysicalFsmTaskInstanceId_Type()
)
cucsComputePhysicalFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmTaskInstanceId.setStatus("current")
_CucsComputePhysicalFsmTaskDn_Type = CucsManagedObjectDn
_CucsComputePhysicalFsmTaskDn_Object = MibTableColumn
cucsComputePhysicalFsmTaskDn = _CucsComputePhysicalFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 24, 1, 2),
    _CucsComputePhysicalFsmTaskDn_Type()
)
cucsComputePhysicalFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmTaskDn.setStatus("current")
_CucsComputePhysicalFsmTaskRn_Type = SnmpAdminString
_CucsComputePhysicalFsmTaskRn_Object = MibTableColumn
cucsComputePhysicalFsmTaskRn = _CucsComputePhysicalFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 24, 1, 3),
    _CucsComputePhysicalFsmTaskRn_Type()
)
cucsComputePhysicalFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmTaskRn.setStatus("current")
_CucsComputePhysicalFsmTaskCompletion_Type = CucsFsmCompletion
_CucsComputePhysicalFsmTaskCompletion_Object = MibTableColumn
cucsComputePhysicalFsmTaskCompletion = _CucsComputePhysicalFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 24, 1, 4),
    _CucsComputePhysicalFsmTaskCompletion_Type()
)
cucsComputePhysicalFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmTaskCompletion.setStatus("current")
_CucsComputePhysicalFsmTaskFlags_Type = CucsComputePhysicalFsmTaskFlags
_CucsComputePhysicalFsmTaskFlags_Object = MibTableColumn
cucsComputePhysicalFsmTaskFlags = _CucsComputePhysicalFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 24, 1, 5),
    _CucsComputePhysicalFsmTaskFlags_Type()
)
cucsComputePhysicalFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmTaskFlags.setStatus("current")
_CucsComputePhysicalFsmTaskItem_Type = CucsComputePhysicalFsmTaskItem
_CucsComputePhysicalFsmTaskItem_Object = MibTableColumn
cucsComputePhysicalFsmTaskItem = _CucsComputePhysicalFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 24, 1, 6),
    _CucsComputePhysicalFsmTaskItem_Type()
)
cucsComputePhysicalFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmTaskItem.setStatus("current")
_CucsComputePhysicalFsmTaskSeqId_Type = Gauge32
_CucsComputePhysicalFsmTaskSeqId_Object = MibTableColumn
cucsComputePhysicalFsmTaskSeqId = _CucsComputePhysicalFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 24, 1, 7),
    _CucsComputePhysicalFsmTaskSeqId_Type()
)
cucsComputePhysicalFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmTaskSeqId.setStatus("current")
_CucsComputePhysicalQualTable_Object = MibTable
cucsComputePhysicalQualTable = _CucsComputePhysicalQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 25)
)
if mibBuilder.loadTexts:
    cucsComputePhysicalQualTable.setStatus("current")
_CucsComputePhysicalQualEntry_Object = MibTableRow
cucsComputePhysicalQualEntry = _CucsComputePhysicalQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 25, 1)
)
cucsComputePhysicalQualEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePhysicalQualInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePhysicalQualEntry.setStatus("current")
_CucsComputePhysicalQualInstanceId_Type = CucsManagedObjectId
_CucsComputePhysicalQualInstanceId_Object = MibTableColumn
cucsComputePhysicalQualInstanceId = _CucsComputePhysicalQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 25, 1, 1),
    _CucsComputePhysicalQualInstanceId_Type()
)
cucsComputePhysicalQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePhysicalQualInstanceId.setStatus("current")
_CucsComputePhysicalQualDn_Type = CucsManagedObjectDn
_CucsComputePhysicalQualDn_Object = MibTableColumn
cucsComputePhysicalQualDn = _CucsComputePhysicalQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 25, 1, 2),
    _CucsComputePhysicalQualDn_Type()
)
cucsComputePhysicalQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalQualDn.setStatus("current")
_CucsComputePhysicalQualRn_Type = SnmpAdminString
_CucsComputePhysicalQualRn_Object = MibTableColumn
cucsComputePhysicalQualRn = _CucsComputePhysicalQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 25, 1, 3),
    _CucsComputePhysicalQualRn_Type()
)
cucsComputePhysicalQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalQualRn.setStatus("current")
_CucsComputePhysicalQualModel_Type = SnmpAdminString
_CucsComputePhysicalQualModel_Object = MibTableColumn
cucsComputePhysicalQualModel = _CucsComputePhysicalQualModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 25, 1, 4),
    _CucsComputePhysicalQualModel_Type()
)
cucsComputePhysicalQualModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalQualModel.setStatus("current")
_CucsComputePhysicalQualPropAcl_Type = Unsigned64
_CucsComputePhysicalQualPropAcl_Object = MibTableColumn
cucsComputePhysicalQualPropAcl = _CucsComputePhysicalQualPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 25, 1, 5),
    _CucsComputePhysicalQualPropAcl_Type()
)
cucsComputePhysicalQualPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalQualPropAcl.setStatus("current")
_CucsComputePlatformTable_Object = MibTable
cucsComputePlatformTable = _CucsComputePlatformTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 26)
)
if mibBuilder.loadTexts:
    cucsComputePlatformTable.setStatus("current")
_CucsComputePlatformEntry_Object = MibTableRow
cucsComputePlatformEntry = _CucsComputePlatformEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 26, 1)
)
cucsComputePlatformEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePlatformInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePlatformEntry.setStatus("current")
_CucsComputePlatformInstanceId_Type = CucsManagedObjectId
_CucsComputePlatformInstanceId_Object = MibTableColumn
cucsComputePlatformInstanceId = _CucsComputePlatformInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 26, 1, 1),
    _CucsComputePlatformInstanceId_Type()
)
cucsComputePlatformInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePlatformInstanceId.setStatus("current")
_CucsComputePlatformDn_Type = CucsManagedObjectDn
_CucsComputePlatformDn_Object = MibTableColumn
cucsComputePlatformDn = _CucsComputePlatformDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 26, 1, 2),
    _CucsComputePlatformDn_Type()
)
cucsComputePlatformDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePlatformDn.setStatus("current")
_CucsComputePlatformRn_Type = SnmpAdminString
_CucsComputePlatformRn_Object = MibTableColumn
cucsComputePlatformRn = _CucsComputePlatformRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 26, 1, 3),
    _CucsComputePlatformRn_Type()
)
cucsComputePlatformRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePlatformRn.setStatus("current")
_CucsComputePlatformModel_Type = SnmpAdminString
_CucsComputePlatformModel_Object = MibTableColumn
cucsComputePlatformModel = _CucsComputePlatformModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 26, 1, 4),
    _CucsComputePlatformModel_Type()
)
cucsComputePlatformModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePlatformModel.setStatus("current")
_CucsComputePlatformRevision_Type = SnmpAdminString
_CucsComputePlatformRevision_Object = MibTableColumn
cucsComputePlatformRevision = _CucsComputePlatformRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 26, 1, 5),
    _CucsComputePlatformRevision_Type()
)
cucsComputePlatformRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePlatformRevision.setStatus("current")
_CucsComputePlatformVendor_Type = SnmpAdminString
_CucsComputePlatformVendor_Object = MibTableColumn
cucsComputePlatformVendor = _CucsComputePlatformVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 26, 1, 6),
    _CucsComputePlatformVendor_Type()
)
cucsComputePlatformVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePlatformVendor.setStatus("current")
_CucsComputePlatformProductName_Type = SnmpAdminString
_CucsComputePlatformProductName_Object = MibTableColumn
cucsComputePlatformProductName = _CucsComputePlatformProductName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 26, 1, 7),
    _CucsComputePlatformProductName_Type()
)
cucsComputePlatformProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePlatformProductName.setStatus("current")
_CucsComputePlatformPropAcl_Type = Unsigned64
_CucsComputePlatformPropAcl_Object = MibTableColumn
cucsComputePlatformPropAcl = _CucsComputePlatformPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 26, 1, 8),
    _CucsComputePlatformPropAcl_Type()
)
cucsComputePlatformPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePlatformPropAcl.setStatus("current")
_CucsComputePoolTable_Object = MibTable
cucsComputePoolTable = _CucsComputePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27)
)
if mibBuilder.loadTexts:
    cucsComputePoolTable.setStatus("current")
_CucsComputePoolEntry_Object = MibTableRow
cucsComputePoolEntry = _CucsComputePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27, 1)
)
cucsComputePoolEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePoolInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePoolEntry.setStatus("current")
_CucsComputePoolInstanceId_Type = CucsManagedObjectId
_CucsComputePoolInstanceId_Object = MibTableColumn
cucsComputePoolInstanceId = _CucsComputePoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27, 1, 1),
    _CucsComputePoolInstanceId_Type()
)
cucsComputePoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePoolInstanceId.setStatus("current")
_CucsComputePoolDn_Type = CucsManagedObjectDn
_CucsComputePoolDn_Object = MibTableColumn
cucsComputePoolDn = _CucsComputePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27, 1, 2),
    _CucsComputePoolDn_Type()
)
cucsComputePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolDn.setStatus("current")
_CucsComputePoolRn_Type = SnmpAdminString
_CucsComputePoolRn_Object = MibTableColumn
cucsComputePoolRn = _CucsComputePoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27, 1, 3),
    _CucsComputePoolRn_Type()
)
cucsComputePoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolRn.setStatus("current")
_CucsComputePoolAssigned_Type = Gauge32
_CucsComputePoolAssigned_Object = MibTableColumn
cucsComputePoolAssigned = _CucsComputePoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27, 1, 4),
    _CucsComputePoolAssigned_Type()
)
cucsComputePoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolAssigned.setStatus("current")
_CucsComputePoolDescr_Type = SnmpAdminString
_CucsComputePoolDescr_Object = MibTableColumn
cucsComputePoolDescr = _CucsComputePoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27, 1, 5),
    _CucsComputePoolDescr_Type()
)
cucsComputePoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolDescr.setStatus("current")
_CucsComputePoolIntId_Type = SnmpAdminString
_CucsComputePoolIntId_Object = MibTableColumn
cucsComputePoolIntId = _CucsComputePoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27, 1, 6),
    _CucsComputePoolIntId_Type()
)
cucsComputePoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolIntId.setStatus("current")
_CucsComputePoolName_Type = SnmpAdminString
_CucsComputePoolName_Object = MibTableColumn
cucsComputePoolName = _CucsComputePoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27, 1, 7),
    _CucsComputePoolName_Type()
)
cucsComputePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolName.setStatus("current")
_CucsComputePoolSize_Type = Gauge32
_CucsComputePoolSize_Object = MibTableColumn
cucsComputePoolSize = _CucsComputePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27, 1, 8),
    _CucsComputePoolSize_Type()
)
cucsComputePoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolSize.setStatus("current")
_CucsComputePoolAssignmentOrder_Type = CucsPoolPoolAssignmentOrder
_CucsComputePoolAssignmentOrder_Object = MibTableColumn
cucsComputePoolAssignmentOrder = _CucsComputePoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27, 1, 9),
    _CucsComputePoolAssignmentOrder_Type()
)
cucsComputePoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolAssignmentOrder.setStatus("current")
_CucsComputePoolPolicyLevel_Type = Gauge32
_CucsComputePoolPolicyLevel_Object = MibTableColumn
cucsComputePoolPolicyLevel = _CucsComputePoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27, 1, 10),
    _CucsComputePoolPolicyLevel_Type()
)
cucsComputePoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolPolicyLevel.setStatus("current")
_CucsComputePoolPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputePoolPolicyOwner_Object = MibTableColumn
cucsComputePoolPolicyOwner = _CucsComputePoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 27, 1, 11),
    _CucsComputePoolPolicyOwner_Type()
)
cucsComputePoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolPolicyOwner.setStatus("current")
_CucsComputePoolableTable_Object = MibTable
cucsComputePoolableTable = _CucsComputePoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 28)
)
if mibBuilder.loadTexts:
    cucsComputePoolableTable.setStatus("current")
_CucsComputePoolableEntry_Object = MibTableRow
cucsComputePoolableEntry = _CucsComputePoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 28, 1)
)
cucsComputePoolableEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePoolableEntry.setStatus("current")
_CucsComputePoolableInstanceId_Type = CucsManagedObjectId
_CucsComputePoolableInstanceId_Object = MibTableColumn
cucsComputePoolableInstanceId = _CucsComputePoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 28, 1, 1),
    _CucsComputePoolableInstanceId_Type()
)
cucsComputePoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePoolableInstanceId.setStatus("current")
_CucsComputePoolableDn_Type = CucsManagedObjectDn
_CucsComputePoolableDn_Object = MibTableColumn
cucsComputePoolableDn = _CucsComputePoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 28, 1, 2),
    _CucsComputePoolableDn_Type()
)
cucsComputePoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolableDn.setStatus("current")
_CucsComputePoolableRn_Type = SnmpAdminString
_CucsComputePoolableRn_Object = MibTableColumn
cucsComputePoolableRn = _CucsComputePoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 28, 1, 3),
    _CucsComputePoolableRn_Type()
)
cucsComputePoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolableRn.setStatus("current")
_CucsComputePoolableId_Type = Unsigned64
_CucsComputePoolableId_Object = MibTableColumn
cucsComputePoolableId = _CucsComputePoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 28, 1, 4),
    _CucsComputePoolableId_Type()
)
cucsComputePoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolableId.setStatus("current")
_CucsComputePoolablePoolDn_Type = SnmpAdminString
_CucsComputePoolablePoolDn_Object = MibTableColumn
cucsComputePoolablePoolDn = _CucsComputePoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 28, 1, 5),
    _CucsComputePoolablePoolDn_Type()
)
cucsComputePoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolablePoolDn.setStatus("current")
_CucsComputePooledRackUnitTable_Object = MibTable
cucsComputePooledRackUnitTable = _CucsComputePooledRackUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 29)
)
if mibBuilder.loadTexts:
    cucsComputePooledRackUnitTable.setStatus("current")
_CucsComputePooledRackUnitEntry_Object = MibTableRow
cucsComputePooledRackUnitEntry = _CucsComputePooledRackUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 29, 1)
)
cucsComputePooledRackUnitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePooledRackUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePooledRackUnitEntry.setStatus("current")
_CucsComputePooledRackUnitInstanceId_Type = CucsManagedObjectId
_CucsComputePooledRackUnitInstanceId_Object = MibTableColumn
cucsComputePooledRackUnitInstanceId = _CucsComputePooledRackUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 29, 1, 1),
    _CucsComputePooledRackUnitInstanceId_Type()
)
cucsComputePooledRackUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePooledRackUnitInstanceId.setStatus("current")
_CucsComputePooledRackUnitDn_Type = CucsManagedObjectDn
_CucsComputePooledRackUnitDn_Object = MibTableColumn
cucsComputePooledRackUnitDn = _CucsComputePooledRackUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 29, 1, 2),
    _CucsComputePooledRackUnitDn_Type()
)
cucsComputePooledRackUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledRackUnitDn.setStatus("current")
_CucsComputePooledRackUnitRn_Type = SnmpAdminString
_CucsComputePooledRackUnitRn_Object = MibTableColumn
cucsComputePooledRackUnitRn = _CucsComputePooledRackUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 29, 1, 3),
    _CucsComputePooledRackUnitRn_Type()
)
cucsComputePooledRackUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledRackUnitRn.setStatus("current")
_CucsComputePooledRackUnitAssigned_Type = TruthValue
_CucsComputePooledRackUnitAssigned_Object = MibTableColumn
cucsComputePooledRackUnitAssigned = _CucsComputePooledRackUnitAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 29, 1, 4),
    _CucsComputePooledRackUnitAssigned_Type()
)
cucsComputePooledRackUnitAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledRackUnitAssigned.setStatus("current")
_CucsComputePooledRackUnitAssignedToDn_Type = SnmpAdminString
_CucsComputePooledRackUnitAssignedToDn_Object = MibTableColumn
cucsComputePooledRackUnitAssignedToDn = _CucsComputePooledRackUnitAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 29, 1, 5),
    _CucsComputePooledRackUnitAssignedToDn_Type()
)
cucsComputePooledRackUnitAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledRackUnitAssignedToDn.setStatus("current")
_CucsComputePooledRackUnitId_Type = CucsComputePooledRackUnitId
_CucsComputePooledRackUnitId_Object = MibTableColumn
cucsComputePooledRackUnitId = _CucsComputePooledRackUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 29, 1, 6),
    _CucsComputePooledRackUnitId_Type()
)
cucsComputePooledRackUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledRackUnitId.setStatus("current")
_CucsComputePooledRackUnitOwner_Type = CucsComputeOwner
_CucsComputePooledRackUnitOwner_Object = MibTableColumn
cucsComputePooledRackUnitOwner = _CucsComputePooledRackUnitOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 29, 1, 7),
    _CucsComputePooledRackUnitOwner_Type()
)
cucsComputePooledRackUnitOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledRackUnitOwner.setStatus("current")
_CucsComputePooledRackUnitPoolableDn_Type = SnmpAdminString
_CucsComputePooledRackUnitPoolableDn_Object = MibTableColumn
cucsComputePooledRackUnitPoolableDn = _CucsComputePooledRackUnitPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 29, 1, 8),
    _CucsComputePooledRackUnitPoolableDn_Type()
)
cucsComputePooledRackUnitPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledRackUnitPoolableDn.setStatus("current")
_CucsComputePooledRackUnitPrevAssignedToDn_Type = SnmpAdminString
_CucsComputePooledRackUnitPrevAssignedToDn_Object = MibTableColumn
cucsComputePooledRackUnitPrevAssignedToDn = _CucsComputePooledRackUnitPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 29, 1, 9),
    _CucsComputePooledRackUnitPrevAssignedToDn_Type()
)
cucsComputePooledRackUnitPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledRackUnitPrevAssignedToDn.setStatus("current")
_CucsComputePooledSlotTable_Object = MibTable
cucsComputePooledSlotTable = _CucsComputePooledSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 30)
)
if mibBuilder.loadTexts:
    cucsComputePooledSlotTable.setStatus("current")
_CucsComputePooledSlotEntry_Object = MibTableRow
cucsComputePooledSlotEntry = _CucsComputePooledSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 30, 1)
)
cucsComputePooledSlotEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePooledSlotInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePooledSlotEntry.setStatus("current")
_CucsComputePooledSlotInstanceId_Type = CucsManagedObjectId
_CucsComputePooledSlotInstanceId_Object = MibTableColumn
cucsComputePooledSlotInstanceId = _CucsComputePooledSlotInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 30, 1, 1),
    _CucsComputePooledSlotInstanceId_Type()
)
cucsComputePooledSlotInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePooledSlotInstanceId.setStatus("current")
_CucsComputePooledSlotDn_Type = CucsManagedObjectDn
_CucsComputePooledSlotDn_Object = MibTableColumn
cucsComputePooledSlotDn = _CucsComputePooledSlotDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 30, 1, 2),
    _CucsComputePooledSlotDn_Type()
)
cucsComputePooledSlotDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledSlotDn.setStatus("current")
_CucsComputePooledSlotRn_Type = SnmpAdminString
_CucsComputePooledSlotRn_Object = MibTableColumn
cucsComputePooledSlotRn = _CucsComputePooledSlotRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 30, 1, 3),
    _CucsComputePooledSlotRn_Type()
)
cucsComputePooledSlotRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledSlotRn.setStatus("current")
_CucsComputePooledSlotAssigned_Type = TruthValue
_CucsComputePooledSlotAssigned_Object = MibTableColumn
cucsComputePooledSlotAssigned = _CucsComputePooledSlotAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 30, 1, 4),
    _CucsComputePooledSlotAssigned_Type()
)
cucsComputePooledSlotAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledSlotAssigned.setStatus("current")
_CucsComputePooledSlotAssignedToDn_Type = SnmpAdminString
_CucsComputePooledSlotAssignedToDn_Object = MibTableColumn
cucsComputePooledSlotAssignedToDn = _CucsComputePooledSlotAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 30, 1, 5),
    _CucsComputePooledSlotAssignedToDn_Type()
)
cucsComputePooledSlotAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledSlotAssignedToDn.setStatus("current")
_CucsComputePooledSlotChassisId_Type = Gauge32
_CucsComputePooledSlotChassisId_Object = MibTableColumn
cucsComputePooledSlotChassisId = _CucsComputePooledSlotChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 30, 1, 6),
    _CucsComputePooledSlotChassisId_Type()
)
cucsComputePooledSlotChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledSlotChassisId.setStatus("current")
_CucsComputePooledSlotOwner_Type = CucsComputeOwner
_CucsComputePooledSlotOwner_Object = MibTableColumn
cucsComputePooledSlotOwner = _CucsComputePooledSlotOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 30, 1, 7),
    _CucsComputePooledSlotOwner_Type()
)
cucsComputePooledSlotOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledSlotOwner.setStatus("current")
_CucsComputePooledSlotPoolableDn_Type = SnmpAdminString
_CucsComputePooledSlotPoolableDn_Object = MibTableColumn
cucsComputePooledSlotPoolableDn = _CucsComputePooledSlotPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 30, 1, 8),
    _CucsComputePooledSlotPoolableDn_Type()
)
cucsComputePooledSlotPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledSlotPoolableDn.setStatus("current")
_CucsComputePooledSlotPrevAssignedToDn_Type = SnmpAdminString
_CucsComputePooledSlotPrevAssignedToDn_Object = MibTableColumn
cucsComputePooledSlotPrevAssignedToDn = _CucsComputePooledSlotPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 30, 1, 9),
    _CucsComputePooledSlotPrevAssignedToDn_Type()
)
cucsComputePooledSlotPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledSlotPrevAssignedToDn.setStatus("current")
_CucsComputePooledSlotSlotId_Type = CucsComputePooledSlotSlotId
_CucsComputePooledSlotSlotId_Object = MibTableColumn
cucsComputePooledSlotSlotId = _CucsComputePooledSlotSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 30, 1, 10),
    _CucsComputePooledSlotSlotId_Type()
)
cucsComputePooledSlotSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledSlotSlotId.setStatus("current")
_CucsComputePoolingPolicyTable_Object = MibTable
cucsComputePoolingPolicyTable = _CucsComputePoolingPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 31)
)
if mibBuilder.loadTexts:
    cucsComputePoolingPolicyTable.setStatus("current")
_CucsComputePoolingPolicyEntry_Object = MibTableRow
cucsComputePoolingPolicyEntry = _CucsComputePoolingPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 31, 1)
)
cucsComputePoolingPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePoolingPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePoolingPolicyEntry.setStatus("current")
_CucsComputePoolingPolicyInstanceId_Type = CucsManagedObjectId
_CucsComputePoolingPolicyInstanceId_Object = MibTableColumn
cucsComputePoolingPolicyInstanceId = _CucsComputePoolingPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 31, 1, 1),
    _CucsComputePoolingPolicyInstanceId_Type()
)
cucsComputePoolingPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePoolingPolicyInstanceId.setStatus("current")
_CucsComputePoolingPolicyDn_Type = CucsManagedObjectDn
_CucsComputePoolingPolicyDn_Object = MibTableColumn
cucsComputePoolingPolicyDn = _CucsComputePoolingPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 31, 1, 2),
    _CucsComputePoolingPolicyDn_Type()
)
cucsComputePoolingPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolingPolicyDn.setStatus("current")
_CucsComputePoolingPolicyRn_Type = SnmpAdminString
_CucsComputePoolingPolicyRn_Object = MibTableColumn
cucsComputePoolingPolicyRn = _CucsComputePoolingPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 31, 1, 3),
    _CucsComputePoolingPolicyRn_Type()
)
cucsComputePoolingPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolingPolicyRn.setStatus("current")
_CucsComputePoolingPolicyDescr_Type = SnmpAdminString
_CucsComputePoolingPolicyDescr_Object = MibTableColumn
cucsComputePoolingPolicyDescr = _CucsComputePoolingPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 31, 1, 4),
    _CucsComputePoolingPolicyDescr_Type()
)
cucsComputePoolingPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolingPolicyDescr.setStatus("current")
_CucsComputePoolingPolicyIntId_Type = SnmpAdminString
_CucsComputePoolingPolicyIntId_Object = MibTableColumn
cucsComputePoolingPolicyIntId = _CucsComputePoolingPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 31, 1, 5),
    _CucsComputePoolingPolicyIntId_Type()
)
cucsComputePoolingPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolingPolicyIntId.setStatus("current")
_CucsComputePoolingPolicyName_Type = SnmpAdminString
_CucsComputePoolingPolicyName_Object = MibTableColumn
cucsComputePoolingPolicyName = _CucsComputePoolingPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 31, 1, 6),
    _CucsComputePoolingPolicyName_Type()
)
cucsComputePoolingPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolingPolicyName.setStatus("current")
_CucsComputePoolingPolicyPoolDn_Type = SnmpAdminString
_CucsComputePoolingPolicyPoolDn_Object = MibTableColumn
cucsComputePoolingPolicyPoolDn = _CucsComputePoolingPolicyPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 31, 1, 7),
    _CucsComputePoolingPolicyPoolDn_Type()
)
cucsComputePoolingPolicyPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolingPolicyPoolDn.setStatus("current")
_CucsComputePoolingPolicyQualifier_Type = SnmpAdminString
_CucsComputePoolingPolicyQualifier_Object = MibTableColumn
cucsComputePoolingPolicyQualifier = _CucsComputePoolingPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 31, 1, 8),
    _CucsComputePoolingPolicyQualifier_Type()
)
cucsComputePoolingPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolingPolicyQualifier.setStatus("current")
_CucsComputePoolingPolicyPolicyLevel_Type = Gauge32
_CucsComputePoolingPolicyPolicyLevel_Object = MibTableColumn
cucsComputePoolingPolicyPolicyLevel = _CucsComputePoolingPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 31, 1, 9),
    _CucsComputePoolingPolicyPolicyLevel_Type()
)
cucsComputePoolingPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolingPolicyPolicyLevel.setStatus("current")
_CucsComputePoolingPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputePoolingPolicyPolicyOwner_Object = MibTableColumn
cucsComputePoolingPolicyPolicyOwner = _CucsComputePoolingPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 31, 1, 10),
    _CucsComputePoolingPolicyPolicyOwner_Type()
)
cucsComputePoolingPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolingPolicyPolicyOwner.setStatus("current")
_CucsComputePsuControlTable_Object = MibTable
cucsComputePsuControlTable = _CucsComputePsuControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32)
)
if mibBuilder.loadTexts:
    cucsComputePsuControlTable.setStatus("current")
_CucsComputePsuControlEntry_Object = MibTableRow
cucsComputePsuControlEntry = _CucsComputePsuControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1)
)
cucsComputePsuControlEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePsuControlInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePsuControlEntry.setStatus("current")
_CucsComputePsuControlInstanceId_Type = CucsManagedObjectId
_CucsComputePsuControlInstanceId_Object = MibTableColumn
cucsComputePsuControlInstanceId = _CucsComputePsuControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 1),
    _CucsComputePsuControlInstanceId_Type()
)
cucsComputePsuControlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePsuControlInstanceId.setStatus("current")
_CucsComputePsuControlDn_Type = CucsManagedObjectDn
_CucsComputePsuControlDn_Object = MibTableColumn
cucsComputePsuControlDn = _CucsComputePsuControlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 2),
    _CucsComputePsuControlDn_Type()
)
cucsComputePsuControlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlDn.setStatus("current")
_CucsComputePsuControlRn_Type = SnmpAdminString
_CucsComputePsuControlRn_Object = MibTableColumn
cucsComputePsuControlRn = _CucsComputePsuControlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 3),
    _CucsComputePsuControlRn_Type()
)
cucsComputePsuControlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlRn.setStatus("current")
_CucsComputePsuControlClusterState_Type = CucsComputePsuClusterState
_CucsComputePsuControlClusterState_Object = MibTableColumn
cucsComputePsuControlClusterState = _CucsComputePsuControlClusterState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 4),
    _CucsComputePsuControlClusterState_Type()
)
cucsComputePsuControlClusterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlClusterState.setStatus("current")
_CucsComputePsuControlDescr_Type = SnmpAdminString
_CucsComputePsuControlDescr_Object = MibTableColumn
cucsComputePsuControlDescr = _CucsComputePsuControlDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 5),
    _CucsComputePsuControlDescr_Type()
)
cucsComputePsuControlDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlDescr.setStatus("current")
_CucsComputePsuControlInputPowerState_Type = CucsEquipmentSensorThresholdStatus
_CucsComputePsuControlInputPowerState_Object = MibTableColumn
cucsComputePsuControlInputPowerState = _CucsComputePsuControlInputPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 6),
    _CucsComputePsuControlInputPowerState_Type()
)
cucsComputePsuControlInputPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlInputPowerState.setStatus("current")
_CucsComputePsuControlIntId_Type = SnmpAdminString
_CucsComputePsuControlIntId_Object = MibTableColumn
cucsComputePsuControlIntId = _CucsComputePsuControlIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 7),
    _CucsComputePsuControlIntId_Type()
)
cucsComputePsuControlIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlIntId.setStatus("current")
_CucsComputePsuControlName_Type = SnmpAdminString
_CucsComputePsuControlName_Object = MibTableColumn
cucsComputePsuControlName = _CucsComputePsuControlName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 8),
    _CucsComputePsuControlName_Type()
)
cucsComputePsuControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlName.setStatus("current")
_CucsComputePsuControlOperQualifier_Type = CucsComputePsuRedundancyOperQualifier
_CucsComputePsuControlOperQualifier_Object = MibTableColumn
cucsComputePsuControlOperQualifier = _CucsComputePsuControlOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 9),
    _CucsComputePsuControlOperQualifier_Type()
)
cucsComputePsuControlOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlOperQualifier.setStatus("current")
_CucsComputePsuControlOperState_Type = CucsComputePsuRedundancyOperState
_CucsComputePsuControlOperState_Object = MibTableColumn
cucsComputePsuControlOperState = _CucsComputePsuControlOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 10),
    _CucsComputePsuControlOperState_Type()
)
cucsComputePsuControlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlOperState.setStatus("current")
_CucsComputePsuControlOutputPowerState_Type = CucsEquipmentSensorThresholdStatus
_CucsComputePsuControlOutputPowerState_Object = MibTableColumn
cucsComputePsuControlOutputPowerState = _CucsComputePsuControlOutputPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 11),
    _CucsComputePsuControlOutputPowerState_Type()
)
cucsComputePsuControlOutputPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlOutputPowerState.setStatus("current")
_CucsComputePsuControlRedundancy_Type = CucsComputePsuControlRedundancy
_CucsComputePsuControlRedundancy_Object = MibTableColumn
cucsComputePsuControlRedundancy = _CucsComputePsuControlRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 12),
    _CucsComputePsuControlRedundancy_Type()
)
cucsComputePsuControlRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlRedundancy.setStatus("current")
_CucsComputePsuControlPolicyLevel_Type = Gauge32
_CucsComputePsuControlPolicyLevel_Object = MibTableColumn
cucsComputePsuControlPolicyLevel = _CucsComputePsuControlPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 13),
    _CucsComputePsuControlPolicyLevel_Type()
)
cucsComputePsuControlPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlPolicyLevel.setStatus("current")
_CucsComputePsuControlPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputePsuControlPolicyOwner_Object = MibTableColumn
cucsComputePsuControlPolicyOwner = _CucsComputePsuControlPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 32, 1, 14),
    _CucsComputePsuControlPolicyOwner_Type()
)
cucsComputePsuControlPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuControlPolicyOwner.setStatus("current")
_CucsComputePsuPolicyTable_Object = MibTable
cucsComputePsuPolicyTable = _CucsComputePsuPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 33)
)
if mibBuilder.loadTexts:
    cucsComputePsuPolicyTable.setStatus("current")
_CucsComputePsuPolicyEntry_Object = MibTableRow
cucsComputePsuPolicyEntry = _CucsComputePsuPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 33, 1)
)
cucsComputePsuPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePsuPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePsuPolicyEntry.setStatus("current")
_CucsComputePsuPolicyInstanceId_Type = CucsManagedObjectId
_CucsComputePsuPolicyInstanceId_Object = MibTableColumn
cucsComputePsuPolicyInstanceId = _CucsComputePsuPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 33, 1, 1),
    _CucsComputePsuPolicyInstanceId_Type()
)
cucsComputePsuPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePsuPolicyInstanceId.setStatus("current")
_CucsComputePsuPolicyDn_Type = CucsManagedObjectDn
_CucsComputePsuPolicyDn_Object = MibTableColumn
cucsComputePsuPolicyDn = _CucsComputePsuPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 33, 1, 2),
    _CucsComputePsuPolicyDn_Type()
)
cucsComputePsuPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuPolicyDn.setStatus("current")
_CucsComputePsuPolicyRn_Type = SnmpAdminString
_CucsComputePsuPolicyRn_Object = MibTableColumn
cucsComputePsuPolicyRn = _CucsComputePsuPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 33, 1, 3),
    _CucsComputePsuPolicyRn_Type()
)
cucsComputePsuPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuPolicyRn.setStatus("current")
_CucsComputePsuPolicyDescr_Type = SnmpAdminString
_CucsComputePsuPolicyDescr_Object = MibTableColumn
cucsComputePsuPolicyDescr = _CucsComputePsuPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 33, 1, 4),
    _CucsComputePsuPolicyDescr_Type()
)
cucsComputePsuPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuPolicyDescr.setStatus("current")
_CucsComputePsuPolicyIntId_Type = SnmpAdminString
_CucsComputePsuPolicyIntId_Object = MibTableColumn
cucsComputePsuPolicyIntId = _CucsComputePsuPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 33, 1, 5),
    _CucsComputePsuPolicyIntId_Type()
)
cucsComputePsuPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuPolicyIntId.setStatus("current")
_CucsComputePsuPolicyName_Type = SnmpAdminString
_CucsComputePsuPolicyName_Object = MibTableColumn
cucsComputePsuPolicyName = _CucsComputePsuPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 33, 1, 6),
    _CucsComputePsuPolicyName_Type()
)
cucsComputePsuPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuPolicyName.setStatus("current")
_CucsComputePsuPolicyRedundancy_Type = CucsComputePsuRedundancy
_CucsComputePsuPolicyRedundancy_Object = MibTableColumn
cucsComputePsuPolicyRedundancy = _CucsComputePsuPolicyRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 33, 1, 7),
    _CucsComputePsuPolicyRedundancy_Type()
)
cucsComputePsuPolicyRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuPolicyRedundancy.setStatus("current")
_CucsComputePsuPolicyPolicyLevel_Type = Gauge32
_CucsComputePsuPolicyPolicyLevel_Object = MibTableColumn
cucsComputePsuPolicyPolicyLevel = _CucsComputePsuPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 33, 1, 8),
    _CucsComputePsuPolicyPolicyLevel_Type()
)
cucsComputePsuPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuPolicyPolicyLevel.setStatus("current")
_CucsComputePsuPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputePsuPolicyPolicyOwner_Object = MibTableColumn
cucsComputePsuPolicyPolicyOwner = _CucsComputePsuPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 33, 1, 9),
    _CucsComputePsuPolicyPolicyOwner_Type()
)
cucsComputePsuPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePsuPolicyPolicyOwner.setStatus("current")
_CucsComputeQualTable_Object = MibTable
cucsComputeQualTable = _CucsComputeQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 34)
)
if mibBuilder.loadTexts:
    cucsComputeQualTable.setStatus("current")
_CucsComputeQualEntry_Object = MibTableRow
cucsComputeQualEntry = _CucsComputeQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 34, 1)
)
cucsComputeQualEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeQualInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeQualEntry.setStatus("current")
_CucsComputeQualInstanceId_Type = CucsManagedObjectId
_CucsComputeQualInstanceId_Object = MibTableColumn
cucsComputeQualInstanceId = _CucsComputeQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 34, 1, 1),
    _CucsComputeQualInstanceId_Type()
)
cucsComputeQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeQualInstanceId.setStatus("current")
_CucsComputeQualDn_Type = CucsManagedObjectDn
_CucsComputeQualDn_Object = MibTableColumn
cucsComputeQualDn = _CucsComputeQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 34, 1, 2),
    _CucsComputeQualDn_Type()
)
cucsComputeQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeQualDn.setStatus("current")
_CucsComputeQualRn_Type = SnmpAdminString
_CucsComputeQualRn_Object = MibTableColumn
cucsComputeQualRn = _CucsComputeQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 34, 1, 3),
    _CucsComputeQualRn_Type()
)
cucsComputeQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeQualRn.setStatus("current")
_CucsComputeQualDescr_Type = SnmpAdminString
_CucsComputeQualDescr_Object = MibTableColumn
cucsComputeQualDescr = _CucsComputeQualDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 34, 1, 4),
    _CucsComputeQualDescr_Type()
)
cucsComputeQualDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeQualDescr.setStatus("current")
_CucsComputeQualIntId_Type = SnmpAdminString
_CucsComputeQualIntId_Object = MibTableColumn
cucsComputeQualIntId = _CucsComputeQualIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 34, 1, 5),
    _CucsComputeQualIntId_Type()
)
cucsComputeQualIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeQualIntId.setStatus("current")
_CucsComputeQualName_Type = SnmpAdminString
_CucsComputeQualName_Object = MibTableColumn
cucsComputeQualName = _CucsComputeQualName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 34, 1, 6),
    _CucsComputeQualName_Type()
)
cucsComputeQualName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeQualName.setStatus("current")
_CucsComputeQualPolicyLevel_Type = Gauge32
_CucsComputeQualPolicyLevel_Object = MibTableColumn
cucsComputeQualPolicyLevel = _CucsComputeQualPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 34, 1, 7),
    _CucsComputeQualPolicyLevel_Type()
)
cucsComputeQualPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeQualPolicyLevel.setStatus("current")
_CucsComputeQualPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeQualPolicyOwner_Object = MibTableColumn
cucsComputeQualPolicyOwner = _CucsComputeQualPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 34, 1, 8),
    _CucsComputeQualPolicyOwner_Type()
)
cucsComputeQualPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeQualPolicyOwner.setStatus("current")
_CucsComputeRackUnitTable_Object = MibTable
cucsComputeRackUnitTable = _CucsComputeRackUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35)
)
if mibBuilder.loadTexts:
    cucsComputeRackUnitTable.setStatus("current")
_CucsComputeRackUnitEntry_Object = MibTableRow
cucsComputeRackUnitEntry = _CucsComputeRackUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1)
)
cucsComputeRackUnitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeRackUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeRackUnitEntry.setStatus("current")
_CucsComputeRackUnitInstanceId_Type = CucsManagedObjectId
_CucsComputeRackUnitInstanceId_Object = MibTableColumn
cucsComputeRackUnitInstanceId = _CucsComputeRackUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 1),
    _CucsComputeRackUnitInstanceId_Type()
)
cucsComputeRackUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeRackUnitInstanceId.setStatus("current")
_CucsComputeRackUnitDn_Type = CucsManagedObjectDn
_CucsComputeRackUnitDn_Object = MibTableColumn
cucsComputeRackUnitDn = _CucsComputeRackUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 2),
    _CucsComputeRackUnitDn_Type()
)
cucsComputeRackUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitDn.setStatus("current")
_CucsComputeRackUnitRn_Type = SnmpAdminString
_CucsComputeRackUnitRn_Object = MibTableColumn
cucsComputeRackUnitRn = _CucsComputeRackUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 3),
    _CucsComputeRackUnitRn_Type()
)
cucsComputeRackUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitRn.setStatus("current")
_CucsComputeRackUnitAdminPower_Type = CucsComputeAdminPowerState
_CucsComputeRackUnitAdminPower_Object = MibTableColumn
cucsComputeRackUnitAdminPower = _CucsComputeRackUnitAdminPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 4),
    _CucsComputeRackUnitAdminPower_Type()
)
cucsComputeRackUnitAdminPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitAdminPower.setStatus("current")
_CucsComputeRackUnitAdminState_Type = CucsComputeAdminState
_CucsComputeRackUnitAdminState_Object = MibTableColumn
cucsComputeRackUnitAdminState = _CucsComputeRackUnitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 5),
    _CucsComputeRackUnitAdminState_Type()
)
cucsComputeRackUnitAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitAdminState.setStatus("current")
_CucsComputeRackUnitAssignedToDn_Type = SnmpAdminString
_CucsComputeRackUnitAssignedToDn_Object = MibTableColumn
cucsComputeRackUnitAssignedToDn = _CucsComputeRackUnitAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 6),
    _CucsComputeRackUnitAssignedToDn_Type()
)
cucsComputeRackUnitAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitAssignedToDn.setStatus("current")
_CucsComputeRackUnitAssociation_Type = CucsComputeAssociation
_CucsComputeRackUnitAssociation_Object = MibTableColumn
cucsComputeRackUnitAssociation = _CucsComputeRackUnitAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 7),
    _CucsComputeRackUnitAssociation_Type()
)
cucsComputeRackUnitAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitAssociation.setStatus("current")
_CucsComputeRackUnitAvailability_Type = CucsComputeAvailability
_CucsComputeRackUnitAvailability_Object = MibTableColumn
cucsComputeRackUnitAvailability = _CucsComputeRackUnitAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 8),
    _CucsComputeRackUnitAvailability_Type()
)
cucsComputeRackUnitAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitAvailability.setStatus("current")
_CucsComputeRackUnitAvailableMemory_Type = Gauge32
_CucsComputeRackUnitAvailableMemory_Object = MibTableColumn
cucsComputeRackUnitAvailableMemory = _CucsComputeRackUnitAvailableMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 9),
    _CucsComputeRackUnitAvailableMemory_Type()
)
cucsComputeRackUnitAvailableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitAvailableMemory.setStatus("current")
_CucsComputeRackUnitCheckPoint_Type = CucsComputeCheckPoint
_CucsComputeRackUnitCheckPoint_Object = MibTableColumn
cucsComputeRackUnitCheckPoint = _CucsComputeRackUnitCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 10),
    _CucsComputeRackUnitCheckPoint_Type()
)
cucsComputeRackUnitCheckPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitCheckPoint.setStatus("current")
_CucsComputeRackUnitConnPath_Type = CucsEquipmentConnectionStatus
_CucsComputeRackUnitConnPath_Object = MibTableColumn
cucsComputeRackUnitConnPath = _CucsComputeRackUnitConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 11),
    _CucsComputeRackUnitConnPath_Type()
)
cucsComputeRackUnitConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitConnPath.setStatus("current")
_CucsComputeRackUnitConnStatus_Type = CucsEquipmentConnectionStatus
_CucsComputeRackUnitConnStatus_Object = MibTableColumn
cucsComputeRackUnitConnStatus = _CucsComputeRackUnitConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 12),
    _CucsComputeRackUnitConnStatus_Type()
)
cucsComputeRackUnitConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitConnStatus.setStatus("current")
_CucsComputeRackUnitDescr_Type = SnmpAdminString
_CucsComputeRackUnitDescr_Object = MibTableColumn
cucsComputeRackUnitDescr = _CucsComputeRackUnitDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 13),
    _CucsComputeRackUnitDescr_Type()
)
cucsComputeRackUnitDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitDescr.setStatus("current")
_CucsComputeRackUnitDiscovery_Type = CucsComputeDiscovery
_CucsComputeRackUnitDiscovery_Object = MibTableColumn
cucsComputeRackUnitDiscovery = _CucsComputeRackUnitDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 14),
    _CucsComputeRackUnitDiscovery_Type()
)
cucsComputeRackUnitDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitDiscovery.setStatus("current")
_CucsComputeRackUnitFltAggr_Type = Unsigned64
_CucsComputeRackUnitFltAggr_Object = MibTableColumn
cucsComputeRackUnitFltAggr = _CucsComputeRackUnitFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 15),
    _CucsComputeRackUnitFltAggr_Type()
)
cucsComputeRackUnitFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFltAggr.setStatus("current")
_CucsComputeRackUnitFsmDescr_Type = SnmpAdminString
_CucsComputeRackUnitFsmDescr_Object = MibTableColumn
cucsComputeRackUnitFsmDescr = _CucsComputeRackUnitFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 16),
    _CucsComputeRackUnitFsmDescr_Type()
)
cucsComputeRackUnitFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmDescr.setStatus("current")
_CucsComputeRackUnitFsmFlags_Type = SnmpAdminString
_CucsComputeRackUnitFsmFlags_Object = MibTableColumn
cucsComputeRackUnitFsmFlags = _CucsComputeRackUnitFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 17),
    _CucsComputeRackUnitFsmFlags_Type()
)
cucsComputeRackUnitFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmFlags.setStatus("current")
_CucsComputeRackUnitFsmPrev_Type = SnmpAdminString
_CucsComputeRackUnitFsmPrev_Object = MibTableColumn
cucsComputeRackUnitFsmPrev = _CucsComputeRackUnitFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 18),
    _CucsComputeRackUnitFsmPrev_Type()
)
cucsComputeRackUnitFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmPrev.setStatus("current")
_CucsComputeRackUnitFsmProgr_Type = Gauge32
_CucsComputeRackUnitFsmProgr_Object = MibTableColumn
cucsComputeRackUnitFsmProgr = _CucsComputeRackUnitFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 19),
    _CucsComputeRackUnitFsmProgr_Type()
)
cucsComputeRackUnitFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmProgr.setStatus("current")
_CucsComputeRackUnitFsmRmtInvErrCode_Type = Gauge32
_CucsComputeRackUnitFsmRmtInvErrCode_Object = MibTableColumn
cucsComputeRackUnitFsmRmtInvErrCode = _CucsComputeRackUnitFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 20),
    _CucsComputeRackUnitFsmRmtInvErrCode_Type()
)
cucsComputeRackUnitFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmRmtInvErrCode.setStatus("current")
_CucsComputeRackUnitFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsComputeRackUnitFsmRmtInvErrDescr_Object = MibTableColumn
cucsComputeRackUnitFsmRmtInvErrDescr = _CucsComputeRackUnitFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 21),
    _CucsComputeRackUnitFsmRmtInvErrDescr_Type()
)
cucsComputeRackUnitFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmRmtInvErrDescr.setStatus("current")
_CucsComputeRackUnitFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsComputeRackUnitFsmRmtInvRslt_Object = MibTableColumn
cucsComputeRackUnitFsmRmtInvRslt = _CucsComputeRackUnitFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 22),
    _CucsComputeRackUnitFsmRmtInvRslt_Type()
)
cucsComputeRackUnitFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmRmtInvRslt.setStatus("current")
_CucsComputeRackUnitFsmStageDescr_Type = SnmpAdminString
_CucsComputeRackUnitFsmStageDescr_Object = MibTableColumn
cucsComputeRackUnitFsmStageDescr = _CucsComputeRackUnitFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 23),
    _CucsComputeRackUnitFsmStageDescr_Type()
)
cucsComputeRackUnitFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStageDescr.setStatus("current")
_CucsComputeRackUnitFsmStamp_Type = DateAndTime
_CucsComputeRackUnitFsmStamp_Object = MibTableColumn
cucsComputeRackUnitFsmStamp = _CucsComputeRackUnitFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 24),
    _CucsComputeRackUnitFsmStamp_Type()
)
cucsComputeRackUnitFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStamp.setStatus("current")
_CucsComputeRackUnitFsmStatus_Type = SnmpAdminString
_CucsComputeRackUnitFsmStatus_Object = MibTableColumn
cucsComputeRackUnitFsmStatus = _CucsComputeRackUnitFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 25),
    _CucsComputeRackUnitFsmStatus_Type()
)
cucsComputeRackUnitFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStatus.setStatus("current")
_CucsComputeRackUnitFsmTry_Type = Gauge32
_CucsComputeRackUnitFsmTry_Object = MibTableColumn
cucsComputeRackUnitFsmTry = _CucsComputeRackUnitFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 26),
    _CucsComputeRackUnitFsmTry_Type()
)
cucsComputeRackUnitFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmTry.setStatus("current")
_CucsComputeRackUnitId_Type = CucsComputeRackUnitId
_CucsComputeRackUnitId_Object = MibTableColumn
cucsComputeRackUnitId = _CucsComputeRackUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 27),
    _CucsComputeRackUnitId_Type()
)
cucsComputeRackUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitId.setStatus("current")
_CucsComputeRackUnitIntId_Type = SnmpAdminString
_CucsComputeRackUnitIntId_Object = MibTableColumn
cucsComputeRackUnitIntId = _CucsComputeRackUnitIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 28),
    _CucsComputeRackUnitIntId_Type()
)
cucsComputeRackUnitIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitIntId.setStatus("current")
_CucsComputeRackUnitLc_Type = CucsComputeAdminTrigger
_CucsComputeRackUnitLc_Object = MibTableColumn
cucsComputeRackUnitLc = _CucsComputeRackUnitLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 29),
    _CucsComputeRackUnitLc_Type()
)
cucsComputeRackUnitLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitLc.setStatus("current")
_CucsComputeRackUnitLcTs_Type = DateAndTime
_CucsComputeRackUnitLcTs_Object = MibTableColumn
cucsComputeRackUnitLcTs = _CucsComputeRackUnitLcTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 30),
    _CucsComputeRackUnitLcTs_Type()
)
cucsComputeRackUnitLcTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitLcTs.setStatus("current")
_CucsComputeRackUnitManagingInst_Type = CucsNetworkSwitchId
_CucsComputeRackUnitManagingInst_Object = MibTableColumn
cucsComputeRackUnitManagingInst = _CucsComputeRackUnitManagingInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 31),
    _CucsComputeRackUnitManagingInst_Type()
)
cucsComputeRackUnitManagingInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitManagingInst.setStatus("current")
_CucsComputeRackUnitModel_Type = SnmpAdminString
_CucsComputeRackUnitModel_Object = MibTableColumn
cucsComputeRackUnitModel = _CucsComputeRackUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 32),
    _CucsComputeRackUnitModel_Type()
)
cucsComputeRackUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitModel.setStatus("current")
_CucsComputeRackUnitName_Type = SnmpAdminString
_CucsComputeRackUnitName_Object = MibTableColumn
cucsComputeRackUnitName = _CucsComputeRackUnitName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 33),
    _CucsComputeRackUnitName_Type()
)
cucsComputeRackUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitName.setStatus("current")
_CucsComputeRackUnitNumOfAdaptors_Type = Gauge32
_CucsComputeRackUnitNumOfAdaptors_Object = MibTableColumn
cucsComputeRackUnitNumOfAdaptors = _CucsComputeRackUnitNumOfAdaptors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 34),
    _CucsComputeRackUnitNumOfAdaptors_Type()
)
cucsComputeRackUnitNumOfAdaptors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitNumOfAdaptors.setStatus("current")
_CucsComputeRackUnitNumOfCores_Type = Gauge32
_CucsComputeRackUnitNumOfCores_Object = MibTableColumn
cucsComputeRackUnitNumOfCores = _CucsComputeRackUnitNumOfCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 35),
    _CucsComputeRackUnitNumOfCores_Type()
)
cucsComputeRackUnitNumOfCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitNumOfCores.setStatus("current")
_CucsComputeRackUnitNumOfCpus_Type = Gauge32
_CucsComputeRackUnitNumOfCpus_Object = MibTableColumn
cucsComputeRackUnitNumOfCpus = _CucsComputeRackUnitNumOfCpus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 36),
    _CucsComputeRackUnitNumOfCpus_Type()
)
cucsComputeRackUnitNumOfCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitNumOfCpus.setStatus("current")
_CucsComputeRackUnitNumOfEthHostIfs_Type = Gauge32
_CucsComputeRackUnitNumOfEthHostIfs_Object = MibTableColumn
cucsComputeRackUnitNumOfEthHostIfs = _CucsComputeRackUnitNumOfEthHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 37),
    _CucsComputeRackUnitNumOfEthHostIfs_Type()
)
cucsComputeRackUnitNumOfEthHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitNumOfEthHostIfs.setStatus("current")
_CucsComputeRackUnitNumOfFcHostIfs_Type = Gauge32
_CucsComputeRackUnitNumOfFcHostIfs_Object = MibTableColumn
cucsComputeRackUnitNumOfFcHostIfs = _CucsComputeRackUnitNumOfFcHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 38),
    _CucsComputeRackUnitNumOfFcHostIfs_Type()
)
cucsComputeRackUnitNumOfFcHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitNumOfFcHostIfs.setStatus("current")
_CucsComputeRackUnitNumOfThreads_Type = Gauge32
_CucsComputeRackUnitNumOfThreads_Object = MibTableColumn
cucsComputeRackUnitNumOfThreads = _CucsComputeRackUnitNumOfThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 39),
    _CucsComputeRackUnitNumOfThreads_Type()
)
cucsComputeRackUnitNumOfThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitNumOfThreads.setStatus("current")
_CucsComputeRackUnitOperPower_Type = CucsEquipmentPowerState
_CucsComputeRackUnitOperPower_Object = MibTableColumn
cucsComputeRackUnitOperPower = _CucsComputeRackUnitOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 40),
    _CucsComputeRackUnitOperPower_Type()
)
cucsComputeRackUnitOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitOperPower.setStatus("current")
_CucsComputeRackUnitOperQualifier_Type = CucsComputeIssues
_CucsComputeRackUnitOperQualifier_Object = MibTableColumn
cucsComputeRackUnitOperQualifier = _CucsComputeRackUnitOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 41),
    _CucsComputeRackUnitOperQualifier_Type()
)
cucsComputeRackUnitOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitOperQualifier.setStatus("current")
_CucsComputeRackUnitOperState_Type = CucsLsOperState
_CucsComputeRackUnitOperState_Object = MibTableColumn
cucsComputeRackUnitOperState = _CucsComputeRackUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 42),
    _CucsComputeRackUnitOperState_Type()
)
cucsComputeRackUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitOperState.setStatus("current")
_CucsComputeRackUnitOperability_Type = CucsEquipmentOperability
_CucsComputeRackUnitOperability_Object = MibTableColumn
cucsComputeRackUnitOperability = _CucsComputeRackUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 43),
    _CucsComputeRackUnitOperability_Type()
)
cucsComputeRackUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitOperability.setStatus("current")
_CucsComputeRackUnitOriginalUuid_Type = SnmpAdminString
_CucsComputeRackUnitOriginalUuid_Object = MibTableColumn
cucsComputeRackUnitOriginalUuid = _CucsComputeRackUnitOriginalUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 44),
    _CucsComputeRackUnitOriginalUuid_Type()
)
cucsComputeRackUnitOriginalUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitOriginalUuid.setStatus("current")
_CucsComputeRackUnitPresence_Type = CucsEquipmentSlotStatus
_CucsComputeRackUnitPresence_Object = MibTableColumn
cucsComputeRackUnitPresence = _CucsComputeRackUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 45),
    _CucsComputeRackUnitPresence_Type()
)
cucsComputeRackUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitPresence.setStatus("current")
_CucsComputeRackUnitRevision_Type = SnmpAdminString
_CucsComputeRackUnitRevision_Object = MibTableColumn
cucsComputeRackUnitRevision = _CucsComputeRackUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 46),
    _CucsComputeRackUnitRevision_Type()
)
cucsComputeRackUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitRevision.setStatus("current")
_CucsComputeRackUnitSerial_Type = SnmpAdminString
_CucsComputeRackUnitSerial_Object = MibTableColumn
cucsComputeRackUnitSerial = _CucsComputeRackUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 47),
    _CucsComputeRackUnitSerial_Type()
)
cucsComputeRackUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitSerial.setStatus("current")
_CucsComputeRackUnitServerId_Type = SnmpAdminString
_CucsComputeRackUnitServerId_Object = MibTableColumn
cucsComputeRackUnitServerId = _CucsComputeRackUnitServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 48),
    _CucsComputeRackUnitServerId_Type()
)
cucsComputeRackUnitServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitServerId.setStatus("current")
_CucsComputeRackUnitTotalMemory_Type = Gauge32
_CucsComputeRackUnitTotalMemory_Object = MibTableColumn
cucsComputeRackUnitTotalMemory = _CucsComputeRackUnitTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 49),
    _CucsComputeRackUnitTotalMemory_Type()
)
cucsComputeRackUnitTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitTotalMemory.setStatus("current")
_CucsComputeRackUnitUuid_Type = SnmpAdminString
_CucsComputeRackUnitUuid_Object = MibTableColumn
cucsComputeRackUnitUuid = _CucsComputeRackUnitUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 50),
    _CucsComputeRackUnitUuid_Type()
)
cucsComputeRackUnitUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitUuid.setStatus("current")
_CucsComputeRackUnitVendor_Type = SnmpAdminString
_CucsComputeRackUnitVendor_Object = MibTableColumn
cucsComputeRackUnitVendor = _CucsComputeRackUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 51),
    _CucsComputeRackUnitVendor_Type()
)
cucsComputeRackUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitVendor.setStatus("current")
_CucsComputeRackUnitVersionHolder_Type = TruthValue
_CucsComputeRackUnitVersionHolder_Object = MibTableColumn
cucsComputeRackUnitVersionHolder = _CucsComputeRackUnitVersionHolder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 52),
    _CucsComputeRackUnitVersionHolder_Type()
)
cucsComputeRackUnitVersionHolder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitVersionHolder.setStatus("current")
_CucsComputeRackUnitNumOfCoresEnabled_Type = Gauge32
_CucsComputeRackUnitNumOfCoresEnabled_Object = MibTableColumn
cucsComputeRackUnitNumOfCoresEnabled = _CucsComputeRackUnitNumOfCoresEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 53),
    _CucsComputeRackUnitNumOfCoresEnabled_Type()
)
cucsComputeRackUnitNumOfCoresEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitNumOfCoresEnabled.setStatus("current")
_CucsComputeRackUnitLowVoltageMemory_Type = CucsComputePhysicalLowVoltageMemory
_CucsComputeRackUnitLowVoltageMemory_Object = MibTableColumn
cucsComputeRackUnitLowVoltageMemory = _CucsComputeRackUnitLowVoltageMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 54),
    _CucsComputeRackUnitLowVoltageMemory_Type()
)
cucsComputeRackUnitLowVoltageMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitLowVoltageMemory.setStatus("current")
_CucsComputeRackUnitMemorySpeed_Type = Gauge32
_CucsComputeRackUnitMemorySpeed_Object = MibTableColumn
cucsComputeRackUnitMemorySpeed = _CucsComputeRackUnitMemorySpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 55),
    _CucsComputeRackUnitMemorySpeed_Type()
)
cucsComputeRackUnitMemorySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMemorySpeed.setStatus("current")
_CucsComputeRackUnitUsrLbl_Type = SnmpAdminString
_CucsComputeRackUnitUsrLbl_Object = MibTableColumn
cucsComputeRackUnitUsrLbl = _CucsComputeRackUnitUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 56),
    _CucsComputeRackUnitUsrLbl_Type()
)
cucsComputeRackUnitUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitUsrLbl.setStatus("current")
_CucsComputeRackUnitMfgTime_Type = DateAndTime
_CucsComputeRackUnitMfgTime_Object = MibTableColumn
cucsComputeRackUnitMfgTime = _CucsComputeRackUnitMfgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 57),
    _CucsComputeRackUnitMfgTime_Type()
)
cucsComputeRackUnitMfgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMfgTime.setStatus("current")
_CucsComputeRackUnitPartNumber_Type = SnmpAdminString
_CucsComputeRackUnitPartNumber_Object = MibTableColumn
cucsComputeRackUnitPartNumber = _CucsComputeRackUnitPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 58),
    _CucsComputeRackUnitPartNumber_Type()
)
cucsComputeRackUnitPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitPartNumber.setStatus("current")
_CucsComputeRackUnitVid_Type = SnmpAdminString
_CucsComputeRackUnitVid_Object = MibTableColumn
cucsComputeRackUnitVid = _CucsComputeRackUnitVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 59),
    _CucsComputeRackUnitVid_Type()
)
cucsComputeRackUnitVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitVid.setStatus("current")
_CucsComputeRackUnitPolicyLevel_Type = Gauge32
_CucsComputeRackUnitPolicyLevel_Object = MibTableColumn
cucsComputeRackUnitPolicyLevel = _CucsComputeRackUnitPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 60),
    _CucsComputeRackUnitPolicyLevel_Type()
)
cucsComputeRackUnitPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitPolicyLevel.setStatus("current")
_CucsComputeRackUnitPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeRackUnitPolicyOwner_Object = MibTableColumn
cucsComputeRackUnitPolicyOwner = _CucsComputeRackUnitPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 61),
    _CucsComputeRackUnitPolicyOwner_Type()
)
cucsComputeRackUnitPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitPolicyOwner.setStatus("current")
_CucsComputeRackUnitLocalId_Type = SnmpAdminString
_CucsComputeRackUnitLocalId_Object = MibTableColumn
cucsComputeRackUnitLocalId = _CucsComputeRackUnitLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 62),
    _CucsComputeRackUnitLocalId_Type()
)
cucsComputeRackUnitLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitLocalId.setStatus("current")
_CucsComputeRackUnitOperPwrTransSrc_Type = CucsComputePowerTransitionSrc
_CucsComputeRackUnitOperPwrTransSrc_Object = MibTableColumn
cucsComputeRackUnitOperPwrTransSrc = _CucsComputeRackUnitOperPwrTransSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 63),
    _CucsComputeRackUnitOperPwrTransSrc_Type()
)
cucsComputeRackUnitOperPwrTransSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitOperPwrTransSrc.setStatus("current")
_CucsComputeRackUnitDiscoveryStatus_Type = CucsEquipmentConnectionStatus
_CucsComputeRackUnitDiscoveryStatus_Object = MibTableColumn
cucsComputeRackUnitDiscoveryStatus = _CucsComputeRackUnitDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 64),
    _CucsComputeRackUnitDiscoveryStatus_Type()
)
cucsComputeRackUnitDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitDiscoveryStatus.setStatus("current")
_CucsComputeRackUnitNumOf40GAdaptorsWithOldFw_Type = Gauge32
_CucsComputeRackUnitNumOf40GAdaptorsWithOldFw_Object = MibTableColumn
cucsComputeRackUnitNumOf40GAdaptorsWithOldFw = _CucsComputeRackUnitNumOf40GAdaptorsWithOldFw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 66),
    _CucsComputeRackUnitNumOf40GAdaptorsWithOldFw_Type()
)
cucsComputeRackUnitNumOf40GAdaptorsWithOldFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitNumOf40GAdaptorsWithOldFw.setStatus("current")
_CucsComputeRackUnitNumOf40GAdaptorsWithUnknownFw_Type = Gauge32
_CucsComputeRackUnitNumOf40GAdaptorsWithUnknownFw_Object = MibTableColumn
cucsComputeRackUnitNumOf40GAdaptorsWithUnknownFw = _CucsComputeRackUnitNumOf40GAdaptorsWithUnknownFw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 67),
    _CucsComputeRackUnitNumOf40GAdaptorsWithUnknownFw_Type()
)
cucsComputeRackUnitNumOf40GAdaptorsWithUnknownFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitNumOf40GAdaptorsWithUnknownFw.setStatus("current")
_CucsComputeRackUnitFanSpeedConfigStatus_Type = SnmpAdminString
_CucsComputeRackUnitFanSpeedConfigStatus_Object = MibTableColumn
cucsComputeRackUnitFanSpeedConfigStatus = _CucsComputeRackUnitFanSpeedConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 68),
    _CucsComputeRackUnitFanSpeedConfigStatus_Type()
)
cucsComputeRackUnitFanSpeedConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFanSpeedConfigStatus.setStatus("current")
_CucsComputeRackUnitFanSpeedPolicyFault_Type = CucsEquipmentFanSpeedPolicyFault
_CucsComputeRackUnitFanSpeedPolicyFault_Object = MibTableColumn
cucsComputeRackUnitFanSpeedPolicyFault = _CucsComputeRackUnitFanSpeedPolicyFault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 35, 1, 69),
    _CucsComputeRackUnitFanSpeedPolicyFault_Type()
)
cucsComputeRackUnitFanSpeedPolicyFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFanSpeedPolicyFault.setStatus("current")
_CucsComputeRackUnitFsmTaskTable_Object = MibTable
cucsComputeRackUnitFsmTaskTable = _CucsComputeRackUnitFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 36)
)
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmTaskTable.setStatus("current")
_CucsComputeRackUnitFsmTaskEntry_Object = MibTableRow
cucsComputeRackUnitFsmTaskEntry = _CucsComputeRackUnitFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 36, 1)
)
cucsComputeRackUnitFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeRackUnitFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmTaskEntry.setStatus("current")
_CucsComputeRackUnitFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsComputeRackUnitFsmTaskInstanceId_Object = MibTableColumn
cucsComputeRackUnitFsmTaskInstanceId = _CucsComputeRackUnitFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 36, 1, 1),
    _CucsComputeRackUnitFsmTaskInstanceId_Type()
)
cucsComputeRackUnitFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmTaskInstanceId.setStatus("current")
_CucsComputeRackUnitFsmTaskDn_Type = CucsManagedObjectDn
_CucsComputeRackUnitFsmTaskDn_Object = MibTableColumn
cucsComputeRackUnitFsmTaskDn = _CucsComputeRackUnitFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 36, 1, 2),
    _CucsComputeRackUnitFsmTaskDn_Type()
)
cucsComputeRackUnitFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmTaskDn.setStatus("current")
_CucsComputeRackUnitFsmTaskRn_Type = SnmpAdminString
_CucsComputeRackUnitFsmTaskRn_Object = MibTableColumn
cucsComputeRackUnitFsmTaskRn = _CucsComputeRackUnitFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 36, 1, 3),
    _CucsComputeRackUnitFsmTaskRn_Type()
)
cucsComputeRackUnitFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmTaskRn.setStatus("current")
_CucsComputeRackUnitFsmTaskCompletion_Type = CucsFsmCompletion
_CucsComputeRackUnitFsmTaskCompletion_Object = MibTableColumn
cucsComputeRackUnitFsmTaskCompletion = _CucsComputeRackUnitFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 36, 1, 4),
    _CucsComputeRackUnitFsmTaskCompletion_Type()
)
cucsComputeRackUnitFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmTaskCompletion.setStatus("current")
_CucsComputeRackUnitFsmTaskFlags_Type = CucsComputeRackUnitFsmTaskFlags
_CucsComputeRackUnitFsmTaskFlags_Object = MibTableColumn
cucsComputeRackUnitFsmTaskFlags = _CucsComputeRackUnitFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 36, 1, 5),
    _CucsComputeRackUnitFsmTaskFlags_Type()
)
cucsComputeRackUnitFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmTaskFlags.setStatus("current")
_CucsComputeRackUnitFsmTaskItem_Type = CucsComputeRackUnitFsmTaskItem
_CucsComputeRackUnitFsmTaskItem_Object = MibTableColumn
cucsComputeRackUnitFsmTaskItem = _CucsComputeRackUnitFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 36, 1, 6),
    _CucsComputeRackUnitFsmTaskItem_Type()
)
cucsComputeRackUnitFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmTaskItem.setStatus("current")
_CucsComputeRackUnitFsmTaskSeqId_Type = Gauge32
_CucsComputeRackUnitFsmTaskSeqId_Object = MibTableColumn
cucsComputeRackUnitFsmTaskSeqId = _CucsComputeRackUnitFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 36, 1, 7),
    _CucsComputeRackUnitFsmTaskSeqId_Type()
)
cucsComputeRackUnitFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmTaskSeqId.setStatus("current")
_CucsComputeRtcBatteryTable_Object = MibTable
cucsComputeRtcBatteryTable = _CucsComputeRtcBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37)
)
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryTable.setStatus("current")
_CucsComputeRtcBatteryEntry_Object = MibTableRow
cucsComputeRtcBatteryEntry = _CucsComputeRtcBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1)
)
cucsComputeRtcBatteryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeRtcBatteryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryEntry.setStatus("current")
_CucsComputeRtcBatteryInstanceId_Type = CucsManagedObjectId
_CucsComputeRtcBatteryInstanceId_Object = MibTableColumn
cucsComputeRtcBatteryInstanceId = _CucsComputeRtcBatteryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 1),
    _CucsComputeRtcBatteryInstanceId_Type()
)
cucsComputeRtcBatteryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryInstanceId.setStatus("current")
_CucsComputeRtcBatteryDn_Type = CucsManagedObjectDn
_CucsComputeRtcBatteryDn_Object = MibTableColumn
cucsComputeRtcBatteryDn = _CucsComputeRtcBatteryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 2),
    _CucsComputeRtcBatteryDn_Type()
)
cucsComputeRtcBatteryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryDn.setStatus("current")
_CucsComputeRtcBatteryRn_Type = SnmpAdminString
_CucsComputeRtcBatteryRn_Object = MibTableColumn
cucsComputeRtcBatteryRn = _CucsComputeRtcBatteryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 3),
    _CucsComputeRtcBatteryRn_Type()
)
cucsComputeRtcBatteryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryRn.setStatus("current")
_CucsComputeRtcBatteryId_Type = Gauge32
_CucsComputeRtcBatteryId_Object = MibTableColumn
cucsComputeRtcBatteryId = _CucsComputeRtcBatteryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 4),
    _CucsComputeRtcBatteryId_Type()
)
cucsComputeRtcBatteryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryId.setStatus("current")
_CucsComputeRtcBatteryModel_Type = SnmpAdminString
_CucsComputeRtcBatteryModel_Object = MibTableColumn
cucsComputeRtcBatteryModel = _CucsComputeRtcBatteryModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 5),
    _CucsComputeRtcBatteryModel_Type()
)
cucsComputeRtcBatteryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryModel.setStatus("current")
_CucsComputeRtcBatteryOperState_Type = CucsEquipmentOperability
_CucsComputeRtcBatteryOperState_Object = MibTableColumn
cucsComputeRtcBatteryOperState = _CucsComputeRtcBatteryOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 6),
    _CucsComputeRtcBatteryOperState_Type()
)
cucsComputeRtcBatteryOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryOperState.setStatus("current")
_CucsComputeRtcBatteryOperability_Type = CucsEquipmentOperability
_CucsComputeRtcBatteryOperability_Object = MibTableColumn
cucsComputeRtcBatteryOperability = _CucsComputeRtcBatteryOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 7),
    _CucsComputeRtcBatteryOperability_Type()
)
cucsComputeRtcBatteryOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryOperability.setStatus("current")
_CucsComputeRtcBatteryPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeRtcBatteryPerf_Object = MibTableColumn
cucsComputeRtcBatteryPerf = _CucsComputeRtcBatteryPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 8),
    _CucsComputeRtcBatteryPerf_Type()
)
cucsComputeRtcBatteryPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryPerf.setStatus("current")
_CucsComputeRtcBatteryPower_Type = CucsEquipmentPowerState
_CucsComputeRtcBatteryPower_Object = MibTableColumn
cucsComputeRtcBatteryPower = _CucsComputeRtcBatteryPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 9),
    _CucsComputeRtcBatteryPower_Type()
)
cucsComputeRtcBatteryPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryPower.setStatus("current")
_CucsComputeRtcBatteryPresence_Type = CucsEquipmentPresence
_CucsComputeRtcBatteryPresence_Object = MibTableColumn
cucsComputeRtcBatteryPresence = _CucsComputeRtcBatteryPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 10),
    _CucsComputeRtcBatteryPresence_Type()
)
cucsComputeRtcBatteryPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryPresence.setStatus("current")
_CucsComputeRtcBatteryRevision_Type = SnmpAdminString
_CucsComputeRtcBatteryRevision_Object = MibTableColumn
cucsComputeRtcBatteryRevision = _CucsComputeRtcBatteryRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 11),
    _CucsComputeRtcBatteryRevision_Type()
)
cucsComputeRtcBatteryRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryRevision.setStatus("current")
_CucsComputeRtcBatterySerial_Type = SnmpAdminString
_CucsComputeRtcBatterySerial_Object = MibTableColumn
cucsComputeRtcBatterySerial = _CucsComputeRtcBatterySerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 12),
    _CucsComputeRtcBatterySerial_Type()
)
cucsComputeRtcBatterySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatterySerial.setStatus("current")
_CucsComputeRtcBatteryThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeRtcBatteryThermal_Object = MibTableColumn
cucsComputeRtcBatteryThermal = _CucsComputeRtcBatteryThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 13),
    _CucsComputeRtcBatteryThermal_Type()
)
cucsComputeRtcBatteryThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryThermal.setStatus("current")
_CucsComputeRtcBatteryVendor_Type = SnmpAdminString
_CucsComputeRtcBatteryVendor_Object = MibTableColumn
cucsComputeRtcBatteryVendor = _CucsComputeRtcBatteryVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 14),
    _CucsComputeRtcBatteryVendor_Type()
)
cucsComputeRtcBatteryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryVendor.setStatus("current")
_CucsComputeRtcBatteryVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeRtcBatteryVoltage_Object = MibTableColumn
cucsComputeRtcBatteryVoltage = _CucsComputeRtcBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 15),
    _CucsComputeRtcBatteryVoltage_Type()
)
cucsComputeRtcBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryVoltage.setStatus("current")
_CucsComputeRtcBatteryOperQualifierReason_Type = SnmpAdminString
_CucsComputeRtcBatteryOperQualifierReason_Object = MibTableColumn
cucsComputeRtcBatteryOperQualifierReason = _CucsComputeRtcBatteryOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 16),
    _CucsComputeRtcBatteryOperQualifierReason_Type()
)
cucsComputeRtcBatteryOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryOperQualifierReason.setStatus("current")
_CucsComputeRtcBatteryLocationDn_Type = SnmpAdminString
_CucsComputeRtcBatteryLocationDn_Object = MibTableColumn
cucsComputeRtcBatteryLocationDn = _CucsComputeRtcBatteryLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 37, 1, 17),
    _CucsComputeRtcBatteryLocationDn_Type()
)
cucsComputeRtcBatteryLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRtcBatteryLocationDn.setStatus("current")
_CucsComputeScrubPolicyTable_Object = MibTable
cucsComputeScrubPolicyTable = _CucsComputeScrubPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38)
)
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyTable.setStatus("current")
_CucsComputeScrubPolicyEntry_Object = MibTableRow
cucsComputeScrubPolicyEntry = _CucsComputeScrubPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38, 1)
)
cucsComputeScrubPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeScrubPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyEntry.setStatus("current")
_CucsComputeScrubPolicyInstanceId_Type = CucsManagedObjectId
_CucsComputeScrubPolicyInstanceId_Object = MibTableColumn
cucsComputeScrubPolicyInstanceId = _CucsComputeScrubPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38, 1, 1),
    _CucsComputeScrubPolicyInstanceId_Type()
)
cucsComputeScrubPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyInstanceId.setStatus("current")
_CucsComputeScrubPolicyDn_Type = CucsManagedObjectDn
_CucsComputeScrubPolicyDn_Object = MibTableColumn
cucsComputeScrubPolicyDn = _CucsComputeScrubPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38, 1, 2),
    _CucsComputeScrubPolicyDn_Type()
)
cucsComputeScrubPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyDn.setStatus("current")
_CucsComputeScrubPolicyRn_Type = SnmpAdminString
_CucsComputeScrubPolicyRn_Object = MibTableColumn
cucsComputeScrubPolicyRn = _CucsComputeScrubPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38, 1, 3),
    _CucsComputeScrubPolicyRn_Type()
)
cucsComputeScrubPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyRn.setStatus("current")
_CucsComputeScrubPolicyBiosSettingsScrub_Type = CucsComputeScrubAction
_CucsComputeScrubPolicyBiosSettingsScrub_Object = MibTableColumn
cucsComputeScrubPolicyBiosSettingsScrub = _CucsComputeScrubPolicyBiosSettingsScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38, 1, 4),
    _CucsComputeScrubPolicyBiosSettingsScrub_Type()
)
cucsComputeScrubPolicyBiosSettingsScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyBiosSettingsScrub.setStatus("current")
_CucsComputeScrubPolicyDescr_Type = SnmpAdminString
_CucsComputeScrubPolicyDescr_Object = MibTableColumn
cucsComputeScrubPolicyDescr = _CucsComputeScrubPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38, 1, 5),
    _CucsComputeScrubPolicyDescr_Type()
)
cucsComputeScrubPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyDescr.setStatus("current")
_CucsComputeScrubPolicyDiskScrub_Type = CucsComputeScrubAction
_CucsComputeScrubPolicyDiskScrub_Object = MibTableColumn
cucsComputeScrubPolicyDiskScrub = _CucsComputeScrubPolicyDiskScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38, 1, 6),
    _CucsComputeScrubPolicyDiskScrub_Type()
)
cucsComputeScrubPolicyDiskScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyDiskScrub.setStatus("current")
_CucsComputeScrubPolicyIntId_Type = SnmpAdminString
_CucsComputeScrubPolicyIntId_Object = MibTableColumn
cucsComputeScrubPolicyIntId = _CucsComputeScrubPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38, 1, 7),
    _CucsComputeScrubPolicyIntId_Type()
)
cucsComputeScrubPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyIntId.setStatus("current")
_CucsComputeScrubPolicyName_Type = SnmpAdminString
_CucsComputeScrubPolicyName_Object = MibTableColumn
cucsComputeScrubPolicyName = _CucsComputeScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38, 1, 8),
    _CucsComputeScrubPolicyName_Type()
)
cucsComputeScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyName.setStatus("current")
_CucsComputeScrubPolicyPolicyLevel_Type = Gauge32
_CucsComputeScrubPolicyPolicyLevel_Object = MibTableColumn
cucsComputeScrubPolicyPolicyLevel = _CucsComputeScrubPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38, 1, 9),
    _CucsComputeScrubPolicyPolicyLevel_Type()
)
cucsComputeScrubPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyPolicyLevel.setStatus("current")
_CucsComputeScrubPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeScrubPolicyPolicyOwner_Object = MibTableColumn
cucsComputeScrubPolicyPolicyOwner = _CucsComputeScrubPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38, 1, 10),
    _CucsComputeScrubPolicyPolicyOwner_Type()
)
cucsComputeScrubPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyPolicyOwner.setStatus("current")
_CucsComputeScrubPolicyFlexFlashScrub_Type = CucsComputeScrubAction
_CucsComputeScrubPolicyFlexFlashScrub_Object = MibTableColumn
cucsComputeScrubPolicyFlexFlashScrub = _CucsComputeScrubPolicyFlexFlashScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 38, 1, 11),
    _CucsComputeScrubPolicyFlexFlashScrub_Type()
)
cucsComputeScrubPolicyFlexFlashScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeScrubPolicyFlexFlashScrub.setStatus("current")
_CucsComputeServerDiscPolicyTable_Object = MibTable
cucsComputeServerDiscPolicyTable = _CucsComputeServerDiscPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39)
)
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyTable.setStatus("current")
_CucsComputeServerDiscPolicyEntry_Object = MibTableRow
cucsComputeServerDiscPolicyEntry = _CucsComputeServerDiscPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1)
)
cucsComputeServerDiscPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeServerDiscPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyEntry.setStatus("current")
_CucsComputeServerDiscPolicyInstanceId_Type = CucsManagedObjectId
_CucsComputeServerDiscPolicyInstanceId_Object = MibTableColumn
cucsComputeServerDiscPolicyInstanceId = _CucsComputeServerDiscPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 1),
    _CucsComputeServerDiscPolicyInstanceId_Type()
)
cucsComputeServerDiscPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyInstanceId.setStatus("current")
_CucsComputeServerDiscPolicyDn_Type = CucsManagedObjectDn
_CucsComputeServerDiscPolicyDn_Object = MibTableColumn
cucsComputeServerDiscPolicyDn = _CucsComputeServerDiscPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 2),
    _CucsComputeServerDiscPolicyDn_Type()
)
cucsComputeServerDiscPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyDn.setStatus("current")
_CucsComputeServerDiscPolicyRn_Type = SnmpAdminString
_CucsComputeServerDiscPolicyRn_Object = MibTableColumn
cucsComputeServerDiscPolicyRn = _CucsComputeServerDiscPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 3),
    _CucsComputeServerDiscPolicyRn_Type()
)
cucsComputeServerDiscPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyRn.setStatus("current")
_CucsComputeServerDiscPolicyAction_Type = SnmpAdminString
_CucsComputeServerDiscPolicyAction_Object = MibTableColumn
cucsComputeServerDiscPolicyAction = _CucsComputeServerDiscPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 4),
    _CucsComputeServerDiscPolicyAction_Type()
)
cucsComputeServerDiscPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyAction.setStatus("current")
_CucsComputeServerDiscPolicyDescr_Type = SnmpAdminString
_CucsComputeServerDiscPolicyDescr_Object = MibTableColumn
cucsComputeServerDiscPolicyDescr = _CucsComputeServerDiscPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 5),
    _CucsComputeServerDiscPolicyDescr_Type()
)
cucsComputeServerDiscPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyDescr.setStatus("current")
_CucsComputeServerDiscPolicyIntId_Type = SnmpAdminString
_CucsComputeServerDiscPolicyIntId_Object = MibTableColumn
cucsComputeServerDiscPolicyIntId = _CucsComputeServerDiscPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 6),
    _CucsComputeServerDiscPolicyIntId_Type()
)
cucsComputeServerDiscPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyIntId.setStatus("current")
_CucsComputeServerDiscPolicyName_Type = SnmpAdminString
_CucsComputeServerDiscPolicyName_Object = MibTableColumn
cucsComputeServerDiscPolicyName = _CucsComputeServerDiscPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 7),
    _CucsComputeServerDiscPolicyName_Type()
)
cucsComputeServerDiscPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyName.setStatus("current")
_CucsComputeServerDiscPolicyQualifier_Type = SnmpAdminString
_CucsComputeServerDiscPolicyQualifier_Object = MibTableColumn
cucsComputeServerDiscPolicyQualifier = _CucsComputeServerDiscPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 8),
    _CucsComputeServerDiscPolicyQualifier_Type()
)
cucsComputeServerDiscPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyQualifier.setStatus("current")
_CucsComputeServerDiscPolicyScrubPolicyName_Type = SnmpAdminString
_CucsComputeServerDiscPolicyScrubPolicyName_Object = MibTableColumn
cucsComputeServerDiscPolicyScrubPolicyName = _CucsComputeServerDiscPolicyScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 9),
    _CucsComputeServerDiscPolicyScrubPolicyName_Type()
)
cucsComputeServerDiscPolicyScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyScrubPolicyName.setStatus("current")
_CucsComputeServerDiscPolicyFsmDescr_Type = SnmpAdminString
_CucsComputeServerDiscPolicyFsmDescr_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmDescr = _CucsComputeServerDiscPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 10),
    _CucsComputeServerDiscPolicyFsmDescr_Type()
)
cucsComputeServerDiscPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmDescr.setStatus("current")
_CucsComputeServerDiscPolicyFsmPrev_Type = SnmpAdminString
_CucsComputeServerDiscPolicyFsmPrev_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmPrev = _CucsComputeServerDiscPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 11),
    _CucsComputeServerDiscPolicyFsmPrev_Type()
)
cucsComputeServerDiscPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmPrev.setStatus("current")
_CucsComputeServerDiscPolicyFsmProgr_Type = Gauge32
_CucsComputeServerDiscPolicyFsmProgr_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmProgr = _CucsComputeServerDiscPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 12),
    _CucsComputeServerDiscPolicyFsmProgr_Type()
)
cucsComputeServerDiscPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmProgr.setStatus("current")
_CucsComputeServerDiscPolicyFsmRmtInvErrCode_Type = Gauge32
_CucsComputeServerDiscPolicyFsmRmtInvErrCode_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmRmtInvErrCode = _CucsComputeServerDiscPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 13),
    _CucsComputeServerDiscPolicyFsmRmtInvErrCode_Type()
)
cucsComputeServerDiscPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmRmtInvErrCode.setStatus("current")
_CucsComputeServerDiscPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsComputeServerDiscPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmRmtInvErrDescr = _CucsComputeServerDiscPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 14),
    _CucsComputeServerDiscPolicyFsmRmtInvErrDescr_Type()
)
cucsComputeServerDiscPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmRmtInvErrDescr.setStatus("current")
_CucsComputeServerDiscPolicyFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsComputeServerDiscPolicyFsmRmtInvRslt_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmRmtInvRslt = _CucsComputeServerDiscPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 15),
    _CucsComputeServerDiscPolicyFsmRmtInvRslt_Type()
)
cucsComputeServerDiscPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmRmtInvRslt.setStatus("current")
_CucsComputeServerDiscPolicyFsmStageDescr_Type = SnmpAdminString
_CucsComputeServerDiscPolicyFsmStageDescr_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmStageDescr = _CucsComputeServerDiscPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 16),
    _CucsComputeServerDiscPolicyFsmStageDescr_Type()
)
cucsComputeServerDiscPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStageDescr.setStatus("current")
_CucsComputeServerDiscPolicyFsmStamp_Type = DateAndTime
_CucsComputeServerDiscPolicyFsmStamp_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmStamp = _CucsComputeServerDiscPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 17),
    _CucsComputeServerDiscPolicyFsmStamp_Type()
)
cucsComputeServerDiscPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStamp.setStatus("current")
_CucsComputeServerDiscPolicyFsmStatus_Type = SnmpAdminString
_CucsComputeServerDiscPolicyFsmStatus_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmStatus = _CucsComputeServerDiscPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 18),
    _CucsComputeServerDiscPolicyFsmStatus_Type()
)
cucsComputeServerDiscPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStatus.setStatus("current")
_CucsComputeServerDiscPolicyFsmTry_Type = Gauge32
_CucsComputeServerDiscPolicyFsmTry_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmTry = _CucsComputeServerDiscPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 19),
    _CucsComputeServerDiscPolicyFsmTry_Type()
)
cucsComputeServerDiscPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmTry.setStatus("current")
_CucsComputeServerDiscPolicyPolicyLevel_Type = Gauge32
_CucsComputeServerDiscPolicyPolicyLevel_Object = MibTableColumn
cucsComputeServerDiscPolicyPolicyLevel = _CucsComputeServerDiscPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 20),
    _CucsComputeServerDiscPolicyPolicyLevel_Type()
)
cucsComputeServerDiscPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyPolicyLevel.setStatus("current")
_CucsComputeServerDiscPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeServerDiscPolicyPolicyOwner_Object = MibTableColumn
cucsComputeServerDiscPolicyPolicyOwner = _CucsComputeServerDiscPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 39, 1, 21),
    _CucsComputeServerDiscPolicyPolicyOwner_Type()
)
cucsComputeServerDiscPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyPolicyOwner.setStatus("current")
_CucsComputeSlotQualTable_Object = MibTable
cucsComputeSlotQualTable = _CucsComputeSlotQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 40)
)
if mibBuilder.loadTexts:
    cucsComputeSlotQualTable.setStatus("current")
_CucsComputeSlotQualEntry_Object = MibTableRow
cucsComputeSlotQualEntry = _CucsComputeSlotQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 40, 1)
)
cucsComputeSlotQualEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeSlotQualInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeSlotQualEntry.setStatus("current")
_CucsComputeSlotQualInstanceId_Type = CucsManagedObjectId
_CucsComputeSlotQualInstanceId_Object = MibTableColumn
cucsComputeSlotQualInstanceId = _CucsComputeSlotQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 40, 1, 1),
    _CucsComputeSlotQualInstanceId_Type()
)
cucsComputeSlotQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeSlotQualInstanceId.setStatus("current")
_CucsComputeSlotQualDn_Type = CucsManagedObjectDn
_CucsComputeSlotQualDn_Object = MibTableColumn
cucsComputeSlotQualDn = _CucsComputeSlotQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 40, 1, 2),
    _CucsComputeSlotQualDn_Type()
)
cucsComputeSlotQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeSlotQualDn.setStatus("current")
_CucsComputeSlotQualRn_Type = SnmpAdminString
_CucsComputeSlotQualRn_Object = MibTableColumn
cucsComputeSlotQualRn = _CucsComputeSlotQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 40, 1, 3),
    _CucsComputeSlotQualRn_Type()
)
cucsComputeSlotQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeSlotQualRn.setStatus("current")
_CucsComputeSlotQualMaxId_Type = CucsComputeSlotQualMaxId
_CucsComputeSlotQualMaxId_Object = MibTableColumn
cucsComputeSlotQualMaxId = _CucsComputeSlotQualMaxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 40, 1, 4),
    _CucsComputeSlotQualMaxId_Type()
)
cucsComputeSlotQualMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeSlotQualMaxId.setStatus("current")
_CucsComputeSlotQualMinId_Type = CucsComputeSlotQualMinId
_CucsComputeSlotQualMinId_Object = MibTableColumn
cucsComputeSlotQualMinId = _CucsComputeSlotQualMinId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 40, 1, 5),
    _CucsComputeSlotQualMinId_Type()
)
cucsComputeSlotQualMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeSlotQualMinId.setStatus("current")
_CucsComputePhysicalAssocCtxTable_Object = MibTable
cucsComputePhysicalAssocCtxTable = _CucsComputePhysicalAssocCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 41)
)
if mibBuilder.loadTexts:
    cucsComputePhysicalAssocCtxTable.setStatus("current")
_CucsComputePhysicalAssocCtxEntry_Object = MibTableRow
cucsComputePhysicalAssocCtxEntry = _CucsComputePhysicalAssocCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 41, 1)
)
cucsComputePhysicalAssocCtxEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePhysicalAssocCtxInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePhysicalAssocCtxEntry.setStatus("current")
_CucsComputePhysicalAssocCtxInstanceId_Type = CucsManagedObjectId
_CucsComputePhysicalAssocCtxInstanceId_Object = MibTableColumn
cucsComputePhysicalAssocCtxInstanceId = _CucsComputePhysicalAssocCtxInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 41, 1, 1),
    _CucsComputePhysicalAssocCtxInstanceId_Type()
)
cucsComputePhysicalAssocCtxInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePhysicalAssocCtxInstanceId.setStatus("current")
_CucsComputePhysicalAssocCtxDn_Type = CucsManagedObjectDn
_CucsComputePhysicalAssocCtxDn_Object = MibTableColumn
cucsComputePhysicalAssocCtxDn = _CucsComputePhysicalAssocCtxDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 41, 1, 2),
    _CucsComputePhysicalAssocCtxDn_Type()
)
cucsComputePhysicalAssocCtxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalAssocCtxDn.setStatus("current")
_CucsComputePhysicalAssocCtxRn_Type = SnmpAdminString
_CucsComputePhysicalAssocCtxRn_Object = MibTableColumn
cucsComputePhysicalAssocCtxRn = _CucsComputePhysicalAssocCtxRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 41, 1, 3),
    _CucsComputePhysicalAssocCtxRn_Type()
)
cucsComputePhysicalAssocCtxRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalAssocCtxRn.setStatus("current")
_CucsComputePhysicalAssocCtxFruCapDn_Type = SnmpAdminString
_CucsComputePhysicalAssocCtxFruCapDn_Object = MibTableColumn
cucsComputePhysicalAssocCtxFruCapDn = _CucsComputePhysicalAssocCtxFruCapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 41, 1, 4),
    _CucsComputePhysicalAssocCtxFruCapDn_Type()
)
cucsComputePhysicalAssocCtxFruCapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalAssocCtxFruCapDn.setStatus("current")
_CucsComputePoolPolicyRefTable_Object = MibTable
cucsComputePoolPolicyRefTable = _CucsComputePoolPolicyRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 42)
)
if mibBuilder.loadTexts:
    cucsComputePoolPolicyRefTable.setStatus("current")
_CucsComputePoolPolicyRefEntry_Object = MibTableRow
cucsComputePoolPolicyRefEntry = _CucsComputePoolPolicyRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 42, 1)
)
cucsComputePoolPolicyRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePoolPolicyRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePoolPolicyRefEntry.setStatus("current")
_CucsComputePoolPolicyRefInstanceId_Type = CucsManagedObjectId
_CucsComputePoolPolicyRefInstanceId_Object = MibTableColumn
cucsComputePoolPolicyRefInstanceId = _CucsComputePoolPolicyRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 42, 1, 1),
    _CucsComputePoolPolicyRefInstanceId_Type()
)
cucsComputePoolPolicyRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePoolPolicyRefInstanceId.setStatus("current")
_CucsComputePoolPolicyRefDn_Type = CucsManagedObjectDn
_CucsComputePoolPolicyRefDn_Object = MibTableColumn
cucsComputePoolPolicyRefDn = _CucsComputePoolPolicyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 42, 1, 2),
    _CucsComputePoolPolicyRefDn_Type()
)
cucsComputePoolPolicyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolPolicyRefDn.setStatus("current")
_CucsComputePoolPolicyRefRn_Type = SnmpAdminString
_CucsComputePoolPolicyRefRn_Object = MibTableColumn
cucsComputePoolPolicyRefRn = _CucsComputePoolPolicyRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 42, 1, 3),
    _CucsComputePoolPolicyRefRn_Type()
)
cucsComputePoolPolicyRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolPolicyRefRn.setStatus("current")
_CucsComputePoolPolicyRefId_Type = Unsigned64
_CucsComputePoolPolicyRefId_Object = MibTableColumn
cucsComputePoolPolicyRefId = _CucsComputePoolPolicyRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 42, 1, 4),
    _CucsComputePoolPolicyRefId_Type()
)
cucsComputePoolPolicyRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolPolicyRefId.setStatus("current")
_CucsComputePoolPolicyRefPolicyDn_Type = SnmpAdminString
_CucsComputePoolPolicyRefPolicyDn_Object = MibTableColumn
cucsComputePoolPolicyRefPolicyDn = _CucsComputePoolPolicyRefPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 42, 1, 5),
    _CucsComputePoolPolicyRefPolicyDn_Type()
)
cucsComputePoolPolicyRefPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePoolPolicyRefPolicyDn.setStatus("current")
_CucsComputeRackQualTable_Object = MibTable
cucsComputeRackQualTable = _CucsComputeRackQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 43)
)
if mibBuilder.loadTexts:
    cucsComputeRackQualTable.setStatus("current")
_CucsComputeRackQualEntry_Object = MibTableRow
cucsComputeRackQualEntry = _CucsComputeRackQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 43, 1)
)
cucsComputeRackQualEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeRackQualInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeRackQualEntry.setStatus("current")
_CucsComputeRackQualInstanceId_Type = CucsManagedObjectId
_CucsComputeRackQualInstanceId_Object = MibTableColumn
cucsComputeRackQualInstanceId = _CucsComputeRackQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 43, 1, 1),
    _CucsComputeRackQualInstanceId_Type()
)
cucsComputeRackQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeRackQualInstanceId.setStatus("current")
_CucsComputeRackQualDn_Type = CucsManagedObjectDn
_CucsComputeRackQualDn_Object = MibTableColumn
cucsComputeRackQualDn = _CucsComputeRackQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 43, 1, 2),
    _CucsComputeRackQualDn_Type()
)
cucsComputeRackQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackQualDn.setStatus("current")
_CucsComputeRackQualRn_Type = SnmpAdminString
_CucsComputeRackQualRn_Object = MibTableColumn
cucsComputeRackQualRn = _CucsComputeRackQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 43, 1, 3),
    _CucsComputeRackQualRn_Type()
)
cucsComputeRackQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackQualRn.setStatus("current")
_CucsComputeRackQualMaxId_Type = CucsComputeRackQualMaxId
_CucsComputeRackQualMaxId_Object = MibTableColumn
cucsComputeRackQualMaxId = _CucsComputeRackQualMaxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 43, 1, 4),
    _CucsComputeRackQualMaxId_Type()
)
cucsComputeRackQualMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackQualMaxId.setStatus("current")
_CucsComputeRackQualMinId_Type = CucsComputeRackQualMinId
_CucsComputeRackQualMinId_Object = MibTableColumn
cucsComputeRackQualMinId = _CucsComputeRackQualMinId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 43, 1, 5),
    _CucsComputeRackQualMinId_Type()
)
cucsComputeRackQualMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackQualMinId.setStatus("current")
_CucsComputeRackUnitMbTempStatsTable_Object = MibTable
cucsComputeRackUnitMbTempStatsTable = _CucsComputeRackUnitMbTempStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44)
)
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsTable.setStatus("current")
_CucsComputeRackUnitMbTempStatsEntry_Object = MibTableRow
cucsComputeRackUnitMbTempStatsEntry = _CucsComputeRackUnitMbTempStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1)
)
cucsComputeRackUnitMbTempStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeRackUnitMbTempStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsEntry.setStatus("current")
_CucsComputeRackUnitMbTempStatsInstanceId_Type = CucsManagedObjectId
_CucsComputeRackUnitMbTempStatsInstanceId_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsInstanceId = _CucsComputeRackUnitMbTempStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 1),
    _CucsComputeRackUnitMbTempStatsInstanceId_Type()
)
cucsComputeRackUnitMbTempStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsInstanceId.setStatus("current")
_CucsComputeRackUnitMbTempStatsDn_Type = CucsManagedObjectDn
_CucsComputeRackUnitMbTempStatsDn_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsDn = _CucsComputeRackUnitMbTempStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 2),
    _CucsComputeRackUnitMbTempStatsDn_Type()
)
cucsComputeRackUnitMbTempStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsDn.setStatus("current")
_CucsComputeRackUnitMbTempStatsRn_Type = SnmpAdminString
_CucsComputeRackUnitMbTempStatsRn_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsRn = _CucsComputeRackUnitMbTempStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 3),
    _CucsComputeRackUnitMbTempStatsRn_Type()
)
cucsComputeRackUnitMbTempStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsRn.setStatus("current")
_CucsComputeRackUnitMbTempStatsAmbientTemp_Type = Integer32
_CucsComputeRackUnitMbTempStatsAmbientTemp_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsAmbientTemp = _CucsComputeRackUnitMbTempStatsAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 4),
    _CucsComputeRackUnitMbTempStatsAmbientTemp_Type()
)
cucsComputeRackUnitMbTempStatsAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsAmbientTemp.setStatus("current")
_CucsComputeRackUnitMbTempStatsAmbientTempAvg_Type = Integer32
_CucsComputeRackUnitMbTempStatsAmbientTempAvg_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsAmbientTempAvg = _CucsComputeRackUnitMbTempStatsAmbientTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 5),
    _CucsComputeRackUnitMbTempStatsAmbientTempAvg_Type()
)
cucsComputeRackUnitMbTempStatsAmbientTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsAmbientTempAvg.setStatus("current")
_CucsComputeRackUnitMbTempStatsAmbientTempMax_Type = Integer32
_CucsComputeRackUnitMbTempStatsAmbientTempMax_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsAmbientTempMax = _CucsComputeRackUnitMbTempStatsAmbientTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 6),
    _CucsComputeRackUnitMbTempStatsAmbientTempMax_Type()
)
cucsComputeRackUnitMbTempStatsAmbientTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsAmbientTempMax.setStatus("current")
_CucsComputeRackUnitMbTempStatsAmbientTempMin_Type = Integer32
_CucsComputeRackUnitMbTempStatsAmbientTempMin_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsAmbientTempMin = _CucsComputeRackUnitMbTempStatsAmbientTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 7),
    _CucsComputeRackUnitMbTempStatsAmbientTempMin_Type()
)
cucsComputeRackUnitMbTempStatsAmbientTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsAmbientTempMin.setStatus("current")
_CucsComputeRackUnitMbTempStatsFrontTemp_Type = Integer32
_CucsComputeRackUnitMbTempStatsFrontTemp_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsFrontTemp = _CucsComputeRackUnitMbTempStatsFrontTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 8),
    _CucsComputeRackUnitMbTempStatsFrontTemp_Type()
)
cucsComputeRackUnitMbTempStatsFrontTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsFrontTemp.setStatus("current")
_CucsComputeRackUnitMbTempStatsFrontTempAvg_Type = Integer32
_CucsComputeRackUnitMbTempStatsFrontTempAvg_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsFrontTempAvg = _CucsComputeRackUnitMbTempStatsFrontTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 9),
    _CucsComputeRackUnitMbTempStatsFrontTempAvg_Type()
)
cucsComputeRackUnitMbTempStatsFrontTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsFrontTempAvg.setStatus("current")
_CucsComputeRackUnitMbTempStatsFrontTempMax_Type = Integer32
_CucsComputeRackUnitMbTempStatsFrontTempMax_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsFrontTempMax = _CucsComputeRackUnitMbTempStatsFrontTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 10),
    _CucsComputeRackUnitMbTempStatsFrontTempMax_Type()
)
cucsComputeRackUnitMbTempStatsFrontTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsFrontTempMax.setStatus("current")
_CucsComputeRackUnitMbTempStatsFrontTempMin_Type = Integer32
_CucsComputeRackUnitMbTempStatsFrontTempMin_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsFrontTempMin = _CucsComputeRackUnitMbTempStatsFrontTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 11),
    _CucsComputeRackUnitMbTempStatsFrontTempMin_Type()
)
cucsComputeRackUnitMbTempStatsFrontTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsFrontTempMin.setStatus("current")
_CucsComputeRackUnitMbTempStatsIntervals_Type = Gauge32
_CucsComputeRackUnitMbTempStatsIntervals_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsIntervals = _CucsComputeRackUnitMbTempStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 12),
    _CucsComputeRackUnitMbTempStatsIntervals_Type()
)
cucsComputeRackUnitMbTempStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsIntervals.setStatus("current")
_CucsComputeRackUnitMbTempStatsIoh1Temp_Type = Integer32
_CucsComputeRackUnitMbTempStatsIoh1Temp_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsIoh1Temp = _CucsComputeRackUnitMbTempStatsIoh1Temp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 13),
    _CucsComputeRackUnitMbTempStatsIoh1Temp_Type()
)
cucsComputeRackUnitMbTempStatsIoh1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsIoh1Temp.setStatus("current")
_CucsComputeRackUnitMbTempStatsIoh1TempAvg_Type = Integer32
_CucsComputeRackUnitMbTempStatsIoh1TempAvg_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsIoh1TempAvg = _CucsComputeRackUnitMbTempStatsIoh1TempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 14),
    _CucsComputeRackUnitMbTempStatsIoh1TempAvg_Type()
)
cucsComputeRackUnitMbTempStatsIoh1TempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsIoh1TempAvg.setStatus("current")
_CucsComputeRackUnitMbTempStatsIoh1TempMax_Type = Integer32
_CucsComputeRackUnitMbTempStatsIoh1TempMax_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsIoh1TempMax = _CucsComputeRackUnitMbTempStatsIoh1TempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 15),
    _CucsComputeRackUnitMbTempStatsIoh1TempMax_Type()
)
cucsComputeRackUnitMbTempStatsIoh1TempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsIoh1TempMax.setStatus("current")
_CucsComputeRackUnitMbTempStatsIoh1TempMin_Type = Integer32
_CucsComputeRackUnitMbTempStatsIoh1TempMin_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsIoh1TempMin = _CucsComputeRackUnitMbTempStatsIoh1TempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 16),
    _CucsComputeRackUnitMbTempStatsIoh1TempMin_Type()
)
cucsComputeRackUnitMbTempStatsIoh1TempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsIoh1TempMin.setStatus("current")
_CucsComputeRackUnitMbTempStatsIoh2Temp_Type = Integer32
_CucsComputeRackUnitMbTempStatsIoh2Temp_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsIoh2Temp = _CucsComputeRackUnitMbTempStatsIoh2Temp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 17),
    _CucsComputeRackUnitMbTempStatsIoh2Temp_Type()
)
cucsComputeRackUnitMbTempStatsIoh2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsIoh2Temp.setStatus("current")
_CucsComputeRackUnitMbTempStatsIoh2TempAvg_Type = Integer32
_CucsComputeRackUnitMbTempStatsIoh2TempAvg_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsIoh2TempAvg = _CucsComputeRackUnitMbTempStatsIoh2TempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 18),
    _CucsComputeRackUnitMbTempStatsIoh2TempAvg_Type()
)
cucsComputeRackUnitMbTempStatsIoh2TempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsIoh2TempAvg.setStatus("current")
_CucsComputeRackUnitMbTempStatsIoh2TempMax_Type = Integer32
_CucsComputeRackUnitMbTempStatsIoh2TempMax_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsIoh2TempMax = _CucsComputeRackUnitMbTempStatsIoh2TempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 19),
    _CucsComputeRackUnitMbTempStatsIoh2TempMax_Type()
)
cucsComputeRackUnitMbTempStatsIoh2TempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsIoh2TempMax.setStatus("current")
_CucsComputeRackUnitMbTempStatsIoh2TempMin_Type = Integer32
_CucsComputeRackUnitMbTempStatsIoh2TempMin_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsIoh2TempMin = _CucsComputeRackUnitMbTempStatsIoh2TempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 20),
    _CucsComputeRackUnitMbTempStatsIoh2TempMin_Type()
)
cucsComputeRackUnitMbTempStatsIoh2TempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsIoh2TempMin.setStatus("current")
_CucsComputeRackUnitMbTempStatsRearTemp_Type = Integer32
_CucsComputeRackUnitMbTempStatsRearTemp_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsRearTemp = _CucsComputeRackUnitMbTempStatsRearTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 21),
    _CucsComputeRackUnitMbTempStatsRearTemp_Type()
)
cucsComputeRackUnitMbTempStatsRearTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsRearTemp.setStatus("current")
_CucsComputeRackUnitMbTempStatsRearTempAvg_Type = Integer32
_CucsComputeRackUnitMbTempStatsRearTempAvg_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsRearTempAvg = _CucsComputeRackUnitMbTempStatsRearTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 22),
    _CucsComputeRackUnitMbTempStatsRearTempAvg_Type()
)
cucsComputeRackUnitMbTempStatsRearTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsRearTempAvg.setStatus("current")
_CucsComputeRackUnitMbTempStatsRearTempMax_Type = Integer32
_CucsComputeRackUnitMbTempStatsRearTempMax_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsRearTempMax = _CucsComputeRackUnitMbTempStatsRearTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 23),
    _CucsComputeRackUnitMbTempStatsRearTempMax_Type()
)
cucsComputeRackUnitMbTempStatsRearTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsRearTempMax.setStatus("current")
_CucsComputeRackUnitMbTempStatsRearTempMin_Type = Integer32
_CucsComputeRackUnitMbTempStatsRearTempMin_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsRearTempMin = _CucsComputeRackUnitMbTempStatsRearTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 24),
    _CucsComputeRackUnitMbTempStatsRearTempMin_Type()
)
cucsComputeRackUnitMbTempStatsRearTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsRearTempMin.setStatus("current")
_CucsComputeRackUnitMbTempStatsSuspect_Type = TruthValue
_CucsComputeRackUnitMbTempStatsSuspect_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsSuspect = _CucsComputeRackUnitMbTempStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 25),
    _CucsComputeRackUnitMbTempStatsSuspect_Type()
)
cucsComputeRackUnitMbTempStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsSuspect.setStatus("current")
_CucsComputeRackUnitMbTempStatsThresholded_Type = CucsComputeRackUnitMbTempStatsThresholded
_CucsComputeRackUnitMbTempStatsThresholded_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsThresholded = _CucsComputeRackUnitMbTempStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 26),
    _CucsComputeRackUnitMbTempStatsThresholded_Type()
)
cucsComputeRackUnitMbTempStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsThresholded.setStatus("current")
_CucsComputeRackUnitMbTempStatsTimeCollected_Type = DateAndTime
_CucsComputeRackUnitMbTempStatsTimeCollected_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsTimeCollected = _CucsComputeRackUnitMbTempStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 27),
    _CucsComputeRackUnitMbTempStatsTimeCollected_Type()
)
cucsComputeRackUnitMbTempStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsTimeCollected.setStatus("current")
_CucsComputeRackUnitMbTempStatsUpdate_Type = Gauge32
_CucsComputeRackUnitMbTempStatsUpdate_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsUpdate = _CucsComputeRackUnitMbTempStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 44, 1, 28),
    _CucsComputeRackUnitMbTempStatsUpdate_Type()
)
cucsComputeRackUnitMbTempStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsUpdate.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistTable_Object = MibTable
cucsComputeRackUnitMbTempStatsHistTable = _CucsComputeRackUnitMbTempStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45)
)
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistTable.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistEntry_Object = MibTableRow
cucsComputeRackUnitMbTempStatsHistEntry = _CucsComputeRackUnitMbTempStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1)
)
cucsComputeRackUnitMbTempStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeRackUnitMbTempStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistEntry.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistInstanceId_Type = CucsManagedObjectId
_CucsComputeRackUnitMbTempStatsHistInstanceId_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistInstanceId = _CucsComputeRackUnitMbTempStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 1),
    _CucsComputeRackUnitMbTempStatsHistInstanceId_Type()
)
cucsComputeRackUnitMbTempStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistInstanceId.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistDn_Type = CucsManagedObjectDn
_CucsComputeRackUnitMbTempStatsHistDn_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistDn = _CucsComputeRackUnitMbTempStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 2),
    _CucsComputeRackUnitMbTempStatsHistDn_Type()
)
cucsComputeRackUnitMbTempStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistDn.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistRn_Type = SnmpAdminString
_CucsComputeRackUnitMbTempStatsHistRn_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistRn = _CucsComputeRackUnitMbTempStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 3),
    _CucsComputeRackUnitMbTempStatsHistRn_Type()
)
cucsComputeRackUnitMbTempStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistRn.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistAmbientTemp_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistAmbientTemp_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistAmbientTemp = _CucsComputeRackUnitMbTempStatsHistAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 4),
    _CucsComputeRackUnitMbTempStatsHistAmbientTemp_Type()
)
cucsComputeRackUnitMbTempStatsHistAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistAmbientTemp.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistAmbientTempAvg_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistAmbientTempAvg_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistAmbientTempAvg = _CucsComputeRackUnitMbTempStatsHistAmbientTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 5),
    _CucsComputeRackUnitMbTempStatsHistAmbientTempAvg_Type()
)
cucsComputeRackUnitMbTempStatsHistAmbientTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistAmbientTempAvg.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistAmbientTempMax_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistAmbientTempMax_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistAmbientTempMax = _CucsComputeRackUnitMbTempStatsHistAmbientTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 6),
    _CucsComputeRackUnitMbTempStatsHistAmbientTempMax_Type()
)
cucsComputeRackUnitMbTempStatsHistAmbientTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistAmbientTempMax.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistAmbientTempMin_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistAmbientTempMin_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistAmbientTempMin = _CucsComputeRackUnitMbTempStatsHistAmbientTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 7),
    _CucsComputeRackUnitMbTempStatsHistAmbientTempMin_Type()
)
cucsComputeRackUnitMbTempStatsHistAmbientTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistAmbientTempMin.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistFrontTemp_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistFrontTemp_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistFrontTemp = _CucsComputeRackUnitMbTempStatsHistFrontTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 8),
    _CucsComputeRackUnitMbTempStatsHistFrontTemp_Type()
)
cucsComputeRackUnitMbTempStatsHistFrontTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistFrontTemp.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistFrontTempAvg_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistFrontTempAvg_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistFrontTempAvg = _CucsComputeRackUnitMbTempStatsHistFrontTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 9),
    _CucsComputeRackUnitMbTempStatsHistFrontTempAvg_Type()
)
cucsComputeRackUnitMbTempStatsHistFrontTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistFrontTempAvg.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistFrontTempMax_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistFrontTempMax_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistFrontTempMax = _CucsComputeRackUnitMbTempStatsHistFrontTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 10),
    _CucsComputeRackUnitMbTempStatsHistFrontTempMax_Type()
)
cucsComputeRackUnitMbTempStatsHistFrontTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistFrontTempMax.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistFrontTempMin_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistFrontTempMin_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistFrontTempMin = _CucsComputeRackUnitMbTempStatsHistFrontTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 11),
    _CucsComputeRackUnitMbTempStatsHistFrontTempMin_Type()
)
cucsComputeRackUnitMbTempStatsHistFrontTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistFrontTempMin.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistId_Type = Unsigned64
_CucsComputeRackUnitMbTempStatsHistId_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistId = _CucsComputeRackUnitMbTempStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 12),
    _CucsComputeRackUnitMbTempStatsHistId_Type()
)
cucsComputeRackUnitMbTempStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistId.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistIoh1Temp_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistIoh1Temp_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistIoh1Temp = _CucsComputeRackUnitMbTempStatsHistIoh1Temp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 13),
    _CucsComputeRackUnitMbTempStatsHistIoh1Temp_Type()
)
cucsComputeRackUnitMbTempStatsHistIoh1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistIoh1Temp.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistIoh1TempAvg_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistIoh1TempAvg_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistIoh1TempAvg = _CucsComputeRackUnitMbTempStatsHistIoh1TempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 14),
    _CucsComputeRackUnitMbTempStatsHistIoh1TempAvg_Type()
)
cucsComputeRackUnitMbTempStatsHistIoh1TempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistIoh1TempAvg.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistIoh1TempMax_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistIoh1TempMax_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistIoh1TempMax = _CucsComputeRackUnitMbTempStatsHistIoh1TempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 15),
    _CucsComputeRackUnitMbTempStatsHistIoh1TempMax_Type()
)
cucsComputeRackUnitMbTempStatsHistIoh1TempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistIoh1TempMax.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistIoh1TempMin_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistIoh1TempMin_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistIoh1TempMin = _CucsComputeRackUnitMbTempStatsHistIoh1TempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 16),
    _CucsComputeRackUnitMbTempStatsHistIoh1TempMin_Type()
)
cucsComputeRackUnitMbTempStatsHistIoh1TempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistIoh1TempMin.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistIoh2Temp_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistIoh2Temp_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistIoh2Temp = _CucsComputeRackUnitMbTempStatsHistIoh2Temp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 17),
    _CucsComputeRackUnitMbTempStatsHistIoh2Temp_Type()
)
cucsComputeRackUnitMbTempStatsHistIoh2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistIoh2Temp.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistIoh2TempAvg_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistIoh2TempAvg_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistIoh2TempAvg = _CucsComputeRackUnitMbTempStatsHistIoh2TempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 18),
    _CucsComputeRackUnitMbTempStatsHistIoh2TempAvg_Type()
)
cucsComputeRackUnitMbTempStatsHistIoh2TempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistIoh2TempAvg.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistIoh2TempMax_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistIoh2TempMax_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistIoh2TempMax = _CucsComputeRackUnitMbTempStatsHistIoh2TempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 19),
    _CucsComputeRackUnitMbTempStatsHistIoh2TempMax_Type()
)
cucsComputeRackUnitMbTempStatsHistIoh2TempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistIoh2TempMax.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistIoh2TempMin_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistIoh2TempMin_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistIoh2TempMin = _CucsComputeRackUnitMbTempStatsHistIoh2TempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 20),
    _CucsComputeRackUnitMbTempStatsHistIoh2TempMin_Type()
)
cucsComputeRackUnitMbTempStatsHistIoh2TempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistIoh2TempMin.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistMostRecent_Type = TruthValue
_CucsComputeRackUnitMbTempStatsHistMostRecent_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistMostRecent = _CucsComputeRackUnitMbTempStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 21),
    _CucsComputeRackUnitMbTempStatsHistMostRecent_Type()
)
cucsComputeRackUnitMbTempStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistMostRecent.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistRearTemp_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistRearTemp_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistRearTemp = _CucsComputeRackUnitMbTempStatsHistRearTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 22),
    _CucsComputeRackUnitMbTempStatsHistRearTemp_Type()
)
cucsComputeRackUnitMbTempStatsHistRearTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistRearTemp.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistRearTempAvg_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistRearTempAvg_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistRearTempAvg = _CucsComputeRackUnitMbTempStatsHistRearTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 23),
    _CucsComputeRackUnitMbTempStatsHistRearTempAvg_Type()
)
cucsComputeRackUnitMbTempStatsHistRearTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistRearTempAvg.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistRearTempMax_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistRearTempMax_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistRearTempMax = _CucsComputeRackUnitMbTempStatsHistRearTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 24),
    _CucsComputeRackUnitMbTempStatsHistRearTempMax_Type()
)
cucsComputeRackUnitMbTempStatsHistRearTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistRearTempMax.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistRearTempMin_Type = Integer32
_CucsComputeRackUnitMbTempStatsHistRearTempMin_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistRearTempMin = _CucsComputeRackUnitMbTempStatsHistRearTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 25),
    _CucsComputeRackUnitMbTempStatsHistRearTempMin_Type()
)
cucsComputeRackUnitMbTempStatsHistRearTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistRearTempMin.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistSuspect_Type = TruthValue
_CucsComputeRackUnitMbTempStatsHistSuspect_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistSuspect = _CucsComputeRackUnitMbTempStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 26),
    _CucsComputeRackUnitMbTempStatsHistSuspect_Type()
)
cucsComputeRackUnitMbTempStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistSuspect.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistThresholded_Type = CucsComputeRackUnitMbTempStatsHistThresholded
_CucsComputeRackUnitMbTempStatsHistThresholded_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistThresholded = _CucsComputeRackUnitMbTempStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 27),
    _CucsComputeRackUnitMbTempStatsHistThresholded_Type()
)
cucsComputeRackUnitMbTempStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistThresholded.setStatus("current")
_CucsComputeRackUnitMbTempStatsHistTimeCollected_Type = DateAndTime
_CucsComputeRackUnitMbTempStatsHistTimeCollected_Object = MibTableColumn
cucsComputeRackUnitMbTempStatsHistTimeCollected = _CucsComputeRackUnitMbTempStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 45, 1, 28),
    _CucsComputeRackUnitMbTempStatsHistTimeCollected_Type()
)
cucsComputeRackUnitMbTempStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitMbTempStatsHistTimeCollected.setStatus("current")
_CucsComputeChassisConnPolicyTable_Object = MibTable
cucsComputeChassisConnPolicyTable = _CucsComputeChassisConnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46)
)
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyTable.setStatus("current")
_CucsComputeChassisConnPolicyEntry_Object = MibTableRow
cucsComputeChassisConnPolicyEntry = _CucsComputeChassisConnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1)
)
cucsComputeChassisConnPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeChassisConnPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyEntry.setStatus("current")
_CucsComputeChassisConnPolicyInstanceId_Type = CucsManagedObjectId
_CucsComputeChassisConnPolicyInstanceId_Object = MibTableColumn
cucsComputeChassisConnPolicyInstanceId = _CucsComputeChassisConnPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1, 1),
    _CucsComputeChassisConnPolicyInstanceId_Type()
)
cucsComputeChassisConnPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyInstanceId.setStatus("current")
_CucsComputeChassisConnPolicyDn_Type = CucsManagedObjectDn
_CucsComputeChassisConnPolicyDn_Object = MibTableColumn
cucsComputeChassisConnPolicyDn = _CucsComputeChassisConnPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1, 2),
    _CucsComputeChassisConnPolicyDn_Type()
)
cucsComputeChassisConnPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyDn.setStatus("current")
_CucsComputeChassisConnPolicyRn_Type = SnmpAdminString
_CucsComputeChassisConnPolicyRn_Object = MibTableColumn
cucsComputeChassisConnPolicyRn = _CucsComputeChassisConnPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1, 3),
    _CucsComputeChassisConnPolicyRn_Type()
)
cucsComputeChassisConnPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyRn.setStatus("current")
_CucsComputeChassisConnPolicyAdminState_Type = CucsComputeAdminLinkAggregation
_CucsComputeChassisConnPolicyAdminState_Object = MibTableColumn
cucsComputeChassisConnPolicyAdminState = _CucsComputeChassisConnPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1, 4),
    _CucsComputeChassisConnPolicyAdminState_Type()
)
cucsComputeChassisConnPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyAdminState.setStatus("current")
_CucsComputeChassisConnPolicyChassisId_Type = CucsComputeChassisConnPolicyChassisId
_CucsComputeChassisConnPolicyChassisId_Object = MibTableColumn
cucsComputeChassisConnPolicyChassisId = _CucsComputeChassisConnPolicyChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1, 5),
    _CucsComputeChassisConnPolicyChassisId_Type()
)
cucsComputeChassisConnPolicyChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyChassisId.setStatus("current")
_CucsComputeChassisConnPolicyDescr_Type = SnmpAdminString
_CucsComputeChassisConnPolicyDescr_Object = MibTableColumn
cucsComputeChassisConnPolicyDescr = _CucsComputeChassisConnPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1, 6),
    _CucsComputeChassisConnPolicyDescr_Type()
)
cucsComputeChassisConnPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyDescr.setStatus("current")
_CucsComputeChassisConnPolicyIntId_Type = SnmpAdminString
_CucsComputeChassisConnPolicyIntId_Object = MibTableColumn
cucsComputeChassisConnPolicyIntId = _CucsComputeChassisConnPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1, 7),
    _CucsComputeChassisConnPolicyIntId_Type()
)
cucsComputeChassisConnPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyIntId.setStatus("current")
_CucsComputeChassisConnPolicyName_Type = SnmpAdminString
_CucsComputeChassisConnPolicyName_Object = MibTableColumn
cucsComputeChassisConnPolicyName = _CucsComputeChassisConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1, 8),
    _CucsComputeChassisConnPolicyName_Type()
)
cucsComputeChassisConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyName.setStatus("current")
_CucsComputeChassisConnPolicyQualifier_Type = SnmpAdminString
_CucsComputeChassisConnPolicyQualifier_Object = MibTableColumn
cucsComputeChassisConnPolicyQualifier = _CucsComputeChassisConnPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1, 9),
    _CucsComputeChassisConnPolicyQualifier_Type()
)
cucsComputeChassisConnPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyQualifier.setStatus("current")
_CucsComputeChassisConnPolicySwitchId_Type = CucsNetworkSwitchId
_CucsComputeChassisConnPolicySwitchId_Object = MibTableColumn
cucsComputeChassisConnPolicySwitchId = _CucsComputeChassisConnPolicySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1, 10),
    _CucsComputeChassisConnPolicySwitchId_Type()
)
cucsComputeChassisConnPolicySwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicySwitchId.setStatus("current")
_CucsComputeChassisConnPolicyPolicyLevel_Type = Gauge32
_CucsComputeChassisConnPolicyPolicyLevel_Object = MibTableColumn
cucsComputeChassisConnPolicyPolicyLevel = _CucsComputeChassisConnPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1, 11),
    _CucsComputeChassisConnPolicyPolicyLevel_Type()
)
cucsComputeChassisConnPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyPolicyLevel.setStatus("current")
_CucsComputeChassisConnPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeChassisConnPolicyPolicyOwner_Object = MibTableColumn
cucsComputeChassisConnPolicyPolicyOwner = _CucsComputeChassisConnPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 46, 1, 12),
    _CucsComputeChassisConnPolicyPolicyOwner_Type()
)
cucsComputeChassisConnPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeChassisConnPolicyPolicyOwner.setStatus("current")
_CucsComputePnuOSImageTable_Object = MibTable
cucsComputePnuOSImageTable = _CucsComputePnuOSImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 47)
)
if mibBuilder.loadTexts:
    cucsComputePnuOSImageTable.setStatus("current")
_CucsComputePnuOSImageEntry_Object = MibTableRow
cucsComputePnuOSImageEntry = _CucsComputePnuOSImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 47, 1)
)
cucsComputePnuOSImageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePnuOSImageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePnuOSImageEntry.setStatus("current")
_CucsComputePnuOSImageInstanceId_Type = CucsManagedObjectId
_CucsComputePnuOSImageInstanceId_Object = MibTableColumn
cucsComputePnuOSImageInstanceId = _CucsComputePnuOSImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 47, 1, 1),
    _CucsComputePnuOSImageInstanceId_Type()
)
cucsComputePnuOSImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePnuOSImageInstanceId.setStatus("current")
_CucsComputePnuOSImageDn_Type = CucsManagedObjectDn
_CucsComputePnuOSImageDn_Object = MibTableColumn
cucsComputePnuOSImageDn = _CucsComputePnuOSImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 47, 1, 2),
    _CucsComputePnuOSImageDn_Type()
)
cucsComputePnuOSImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePnuOSImageDn.setStatus("current")
_CucsComputePnuOSImageRn_Type = SnmpAdminString
_CucsComputePnuOSImageRn_Object = MibTableColumn
cucsComputePnuOSImageRn = _CucsComputePnuOSImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 47, 1, 3),
    _CucsComputePnuOSImageRn_Type()
)
cucsComputePnuOSImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePnuOSImageRn.setStatus("current")
_CucsComputePnuOSImageImgLoc_Type = SnmpAdminString
_CucsComputePnuOSImageImgLoc_Object = MibTableColumn
cucsComputePnuOSImageImgLoc = _CucsComputePnuOSImageImgLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 47, 1, 4),
    _CucsComputePnuOSImageImgLoc_Type()
)
cucsComputePnuOSImageImgLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePnuOSImageImgLoc.setStatus("current")
_CucsComputePnuOSImageImgName_Type = SnmpAdminString
_CucsComputePnuOSImageImgName_Object = MibTableColumn
cucsComputePnuOSImageImgName = _CucsComputePnuOSImageImgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 47, 1, 5),
    _CucsComputePnuOSImageImgName_Type()
)
cucsComputePnuOSImageImgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePnuOSImageImgName.setStatus("current")
_CucsComputeBladeFsmTable_Object = MibTable
cucsComputeBladeFsmTable = _CucsComputeBladeFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48)
)
if mibBuilder.loadTexts:
    cucsComputeBladeFsmTable.setStatus("current")
_CucsComputeBladeFsmEntry_Object = MibTableRow
cucsComputeBladeFsmEntry = _CucsComputeBladeFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48, 1)
)
cucsComputeBladeFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeBladeFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeBladeFsmEntry.setStatus("current")
_CucsComputeBladeFsmInstanceId_Type = CucsManagedObjectId
_CucsComputeBladeFsmInstanceId_Object = MibTableColumn
cucsComputeBladeFsmInstanceId = _CucsComputeBladeFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48, 1, 1),
    _CucsComputeBladeFsmInstanceId_Type()
)
cucsComputeBladeFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmInstanceId.setStatus("current")
_CucsComputeBladeFsmDn_Type = CucsManagedObjectDn
_CucsComputeBladeFsmDn_Object = MibTableColumn
cucsComputeBladeFsmDn = _CucsComputeBladeFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48, 1, 2),
    _CucsComputeBladeFsmDn_Type()
)
cucsComputeBladeFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmDn.setStatus("current")
_CucsComputeBladeFsmRn_Type = SnmpAdminString
_CucsComputeBladeFsmRn_Object = MibTableColumn
cucsComputeBladeFsmRn = _CucsComputeBladeFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48, 1, 3),
    _CucsComputeBladeFsmRn_Type()
)
cucsComputeBladeFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmRn.setStatus("current")
_CucsComputeBladeFsmCompletionTime_Type = DateAndTime
_CucsComputeBladeFsmCompletionTime_Object = MibTableColumn
cucsComputeBladeFsmCompletionTime = _CucsComputeBladeFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48, 1, 4),
    _CucsComputeBladeFsmCompletionTime_Type()
)
cucsComputeBladeFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmCompletionTime.setStatus("current")
_CucsComputeBladeFsmCurrentFsm_Type = CucsComputeBladeFsmCurrentFsm
_CucsComputeBladeFsmCurrentFsm_Object = MibTableColumn
cucsComputeBladeFsmCurrentFsm = _CucsComputeBladeFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48, 1, 5),
    _CucsComputeBladeFsmCurrentFsm_Type()
)
cucsComputeBladeFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmCurrentFsm.setStatus("current")
_CucsComputeBladeFsmDescrData_Type = SnmpAdminString
_CucsComputeBladeFsmDescrData_Object = MibTableColumn
cucsComputeBladeFsmDescrData = _CucsComputeBladeFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48, 1, 6),
    _CucsComputeBladeFsmDescrData_Type()
)
cucsComputeBladeFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmDescrData.setStatus("current")
_CucsComputeBladeFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsComputeBladeFsmFsmStatus_Object = MibTableColumn
cucsComputeBladeFsmFsmStatus = _CucsComputeBladeFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48, 1, 7),
    _CucsComputeBladeFsmFsmStatus_Type()
)
cucsComputeBladeFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmFsmStatus.setStatus("current")
_CucsComputeBladeFsmProgress_Type = Gauge32
_CucsComputeBladeFsmProgress_Object = MibTableColumn
cucsComputeBladeFsmProgress = _CucsComputeBladeFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48, 1, 8),
    _CucsComputeBladeFsmProgress_Type()
)
cucsComputeBladeFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmProgress.setStatus("current")
_CucsComputeBladeFsmRmtErrCode_Type = Gauge32
_CucsComputeBladeFsmRmtErrCode_Object = MibTableColumn
cucsComputeBladeFsmRmtErrCode = _CucsComputeBladeFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48, 1, 9),
    _CucsComputeBladeFsmRmtErrCode_Type()
)
cucsComputeBladeFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmRmtErrCode.setStatus("current")
_CucsComputeBladeFsmRmtErrDescr_Type = SnmpAdminString
_CucsComputeBladeFsmRmtErrDescr_Object = MibTableColumn
cucsComputeBladeFsmRmtErrDescr = _CucsComputeBladeFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48, 1, 10),
    _CucsComputeBladeFsmRmtErrDescr_Type()
)
cucsComputeBladeFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmRmtErrDescr.setStatus("current")
_CucsComputeBladeFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsComputeBladeFsmRmtRslt_Object = MibTableColumn
cucsComputeBladeFsmRmtRslt = _CucsComputeBladeFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 48, 1, 11),
    _CucsComputeBladeFsmRmtRslt_Type()
)
cucsComputeBladeFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmRmtRslt.setStatus("current")
_CucsComputeBladeFsmStageTable_Object = MibTable
cucsComputeBladeFsmStageTable = _CucsComputeBladeFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 49)
)
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStageTable.setStatus("current")
_CucsComputeBladeFsmStageEntry_Object = MibTableRow
cucsComputeBladeFsmStageEntry = _CucsComputeBladeFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 49, 1)
)
cucsComputeBladeFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeBladeFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStageEntry.setStatus("current")
_CucsComputeBladeFsmStageInstanceId_Type = CucsManagedObjectId
_CucsComputeBladeFsmStageInstanceId_Object = MibTableColumn
cucsComputeBladeFsmStageInstanceId = _CucsComputeBladeFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 49, 1, 1),
    _CucsComputeBladeFsmStageInstanceId_Type()
)
cucsComputeBladeFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStageInstanceId.setStatus("current")
_CucsComputeBladeFsmStageDn_Type = CucsManagedObjectDn
_CucsComputeBladeFsmStageDn_Object = MibTableColumn
cucsComputeBladeFsmStageDn = _CucsComputeBladeFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 49, 1, 2),
    _CucsComputeBladeFsmStageDn_Type()
)
cucsComputeBladeFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStageDn.setStatus("current")
_CucsComputeBladeFsmStageRn_Type = SnmpAdminString
_CucsComputeBladeFsmStageRn_Object = MibTableColumn
cucsComputeBladeFsmStageRn = _CucsComputeBladeFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 49, 1, 3),
    _CucsComputeBladeFsmStageRn_Type()
)
cucsComputeBladeFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStageRn.setStatus("current")
_CucsComputeBladeFsmStageDescrData_Type = SnmpAdminString
_CucsComputeBladeFsmStageDescrData_Object = MibTableColumn
cucsComputeBladeFsmStageDescrData = _CucsComputeBladeFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 49, 1, 4),
    _CucsComputeBladeFsmStageDescrData_Type()
)
cucsComputeBladeFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStageDescrData.setStatus("current")
_CucsComputeBladeFsmStageLastUpdateTime_Type = DateAndTime
_CucsComputeBladeFsmStageLastUpdateTime_Object = MibTableColumn
cucsComputeBladeFsmStageLastUpdateTime = _CucsComputeBladeFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 49, 1, 5),
    _CucsComputeBladeFsmStageLastUpdateTime_Type()
)
cucsComputeBladeFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStageLastUpdateTime.setStatus("current")
_CucsComputeBladeFsmStageName_Type = CucsComputeBladeFsmStageName
_CucsComputeBladeFsmStageName_Object = MibTableColumn
cucsComputeBladeFsmStageName = _CucsComputeBladeFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 49, 1, 6),
    _CucsComputeBladeFsmStageName_Type()
)
cucsComputeBladeFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStageName.setStatus("current")
_CucsComputeBladeFsmStageOrder_Type = Gauge32
_CucsComputeBladeFsmStageOrder_Object = MibTableColumn
cucsComputeBladeFsmStageOrder = _CucsComputeBladeFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 49, 1, 7),
    _CucsComputeBladeFsmStageOrder_Type()
)
cucsComputeBladeFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStageOrder.setStatus("current")
_CucsComputeBladeFsmStageRetry_Type = Gauge32
_CucsComputeBladeFsmStageRetry_Object = MibTableColumn
cucsComputeBladeFsmStageRetry = _CucsComputeBladeFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 49, 1, 8),
    _CucsComputeBladeFsmStageRetry_Type()
)
cucsComputeBladeFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStageRetry.setStatus("current")
_CucsComputeBladeFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsComputeBladeFsmStageStageStatus_Object = MibTableColumn
cucsComputeBladeFsmStageStageStatus = _CucsComputeBladeFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 49, 1, 9),
    _CucsComputeBladeFsmStageStageStatus_Type()
)
cucsComputeBladeFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeFsmStageStageStatus.setStatus("current")
_CucsComputePhysicalFsmTable_Object = MibTable
cucsComputePhysicalFsmTable = _CucsComputePhysicalFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50)
)
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmTable.setStatus("current")
_CucsComputePhysicalFsmEntry_Object = MibTableRow
cucsComputePhysicalFsmEntry = _CucsComputePhysicalFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50, 1)
)
cucsComputePhysicalFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePhysicalFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmEntry.setStatus("current")
_CucsComputePhysicalFsmInstanceId_Type = CucsManagedObjectId
_CucsComputePhysicalFsmInstanceId_Object = MibTableColumn
cucsComputePhysicalFsmInstanceId = _CucsComputePhysicalFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50, 1, 1),
    _CucsComputePhysicalFsmInstanceId_Type()
)
cucsComputePhysicalFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmInstanceId.setStatus("current")
_CucsComputePhysicalFsmDn_Type = CucsManagedObjectDn
_CucsComputePhysicalFsmDn_Object = MibTableColumn
cucsComputePhysicalFsmDn = _CucsComputePhysicalFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50, 1, 2),
    _CucsComputePhysicalFsmDn_Type()
)
cucsComputePhysicalFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmDn.setStatus("current")
_CucsComputePhysicalFsmRn_Type = SnmpAdminString
_CucsComputePhysicalFsmRn_Object = MibTableColumn
cucsComputePhysicalFsmRn = _CucsComputePhysicalFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50, 1, 3),
    _CucsComputePhysicalFsmRn_Type()
)
cucsComputePhysicalFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmRn.setStatus("current")
_CucsComputePhysicalFsmCompletionTime_Type = DateAndTime
_CucsComputePhysicalFsmCompletionTime_Object = MibTableColumn
cucsComputePhysicalFsmCompletionTime = _CucsComputePhysicalFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50, 1, 4),
    _CucsComputePhysicalFsmCompletionTime_Type()
)
cucsComputePhysicalFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmCompletionTime.setStatus("current")
_CucsComputePhysicalFsmCurrentFsm_Type = CucsComputePhysicalFsmCurrentFsm
_CucsComputePhysicalFsmCurrentFsm_Object = MibTableColumn
cucsComputePhysicalFsmCurrentFsm = _CucsComputePhysicalFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50, 1, 5),
    _CucsComputePhysicalFsmCurrentFsm_Type()
)
cucsComputePhysicalFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmCurrentFsm.setStatus("current")
_CucsComputePhysicalFsmDescr_Type = SnmpAdminString
_CucsComputePhysicalFsmDescr_Object = MibTableColumn
cucsComputePhysicalFsmDescr = _CucsComputePhysicalFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50, 1, 6),
    _CucsComputePhysicalFsmDescr_Type()
)
cucsComputePhysicalFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmDescr.setStatus("current")
_CucsComputePhysicalFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsComputePhysicalFsmFsmStatus_Object = MibTableColumn
cucsComputePhysicalFsmFsmStatus = _CucsComputePhysicalFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50, 1, 7),
    _CucsComputePhysicalFsmFsmStatus_Type()
)
cucsComputePhysicalFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmFsmStatus.setStatus("current")
_CucsComputePhysicalFsmProgress_Type = Gauge32
_CucsComputePhysicalFsmProgress_Object = MibTableColumn
cucsComputePhysicalFsmProgress = _CucsComputePhysicalFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50, 1, 8),
    _CucsComputePhysicalFsmProgress_Type()
)
cucsComputePhysicalFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmProgress.setStatus("current")
_CucsComputePhysicalFsmRmtErrCode_Type = Gauge32
_CucsComputePhysicalFsmRmtErrCode_Object = MibTableColumn
cucsComputePhysicalFsmRmtErrCode = _CucsComputePhysicalFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50, 1, 9),
    _CucsComputePhysicalFsmRmtErrCode_Type()
)
cucsComputePhysicalFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmRmtErrCode.setStatus("current")
_CucsComputePhysicalFsmRmtErrDescr_Type = SnmpAdminString
_CucsComputePhysicalFsmRmtErrDescr_Object = MibTableColumn
cucsComputePhysicalFsmRmtErrDescr = _CucsComputePhysicalFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50, 1, 10),
    _CucsComputePhysicalFsmRmtErrDescr_Type()
)
cucsComputePhysicalFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmRmtErrDescr.setStatus("current")
_CucsComputePhysicalFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsComputePhysicalFsmRmtRslt_Object = MibTableColumn
cucsComputePhysicalFsmRmtRslt = _CucsComputePhysicalFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 50, 1, 11),
    _CucsComputePhysicalFsmRmtRslt_Type()
)
cucsComputePhysicalFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmRmtRslt.setStatus("current")
_CucsComputePhysicalFsmStageTable_Object = MibTable
cucsComputePhysicalFsmStageTable = _CucsComputePhysicalFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 51)
)
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmStageTable.setStatus("current")
_CucsComputePhysicalFsmStageEntry_Object = MibTableRow
cucsComputePhysicalFsmStageEntry = _CucsComputePhysicalFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 51, 1)
)
cucsComputePhysicalFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePhysicalFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmStageEntry.setStatus("current")
_CucsComputePhysicalFsmStageInstanceId_Type = CucsManagedObjectId
_CucsComputePhysicalFsmStageInstanceId_Object = MibTableColumn
cucsComputePhysicalFsmStageInstanceId = _CucsComputePhysicalFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 51, 1, 1),
    _CucsComputePhysicalFsmStageInstanceId_Type()
)
cucsComputePhysicalFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmStageInstanceId.setStatus("current")
_CucsComputePhysicalFsmStageDn_Type = CucsManagedObjectDn
_CucsComputePhysicalFsmStageDn_Object = MibTableColumn
cucsComputePhysicalFsmStageDn = _CucsComputePhysicalFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 51, 1, 2),
    _CucsComputePhysicalFsmStageDn_Type()
)
cucsComputePhysicalFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmStageDn.setStatus("current")
_CucsComputePhysicalFsmStageRn_Type = SnmpAdminString
_CucsComputePhysicalFsmStageRn_Object = MibTableColumn
cucsComputePhysicalFsmStageRn = _CucsComputePhysicalFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 51, 1, 3),
    _CucsComputePhysicalFsmStageRn_Type()
)
cucsComputePhysicalFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmStageRn.setStatus("current")
_CucsComputePhysicalFsmStageDescr_Type = SnmpAdminString
_CucsComputePhysicalFsmStageDescr_Object = MibTableColumn
cucsComputePhysicalFsmStageDescr = _CucsComputePhysicalFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 51, 1, 4),
    _CucsComputePhysicalFsmStageDescr_Type()
)
cucsComputePhysicalFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmStageDescr.setStatus("current")
_CucsComputePhysicalFsmStageLastUpdateTime_Type = DateAndTime
_CucsComputePhysicalFsmStageLastUpdateTime_Object = MibTableColumn
cucsComputePhysicalFsmStageLastUpdateTime = _CucsComputePhysicalFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 51, 1, 5),
    _CucsComputePhysicalFsmStageLastUpdateTime_Type()
)
cucsComputePhysicalFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmStageLastUpdateTime.setStatus("current")
_CucsComputePhysicalFsmStageName_Type = CucsComputePhysicalFsmStageName
_CucsComputePhysicalFsmStageName_Object = MibTableColumn
cucsComputePhysicalFsmStageName = _CucsComputePhysicalFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 51, 1, 6),
    _CucsComputePhysicalFsmStageName_Type()
)
cucsComputePhysicalFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmStageName.setStatus("current")
_CucsComputePhysicalFsmStageOrder_Type = Gauge32
_CucsComputePhysicalFsmStageOrder_Object = MibTableColumn
cucsComputePhysicalFsmStageOrder = _CucsComputePhysicalFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 51, 1, 7),
    _CucsComputePhysicalFsmStageOrder_Type()
)
cucsComputePhysicalFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmStageOrder.setStatus("current")
_CucsComputePhysicalFsmStageRetry_Type = Gauge32
_CucsComputePhysicalFsmStageRetry_Object = MibTableColumn
cucsComputePhysicalFsmStageRetry = _CucsComputePhysicalFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 51, 1, 8),
    _CucsComputePhysicalFsmStageRetry_Type()
)
cucsComputePhysicalFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmStageRetry.setStatus("current")
_CucsComputePhysicalFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsComputePhysicalFsmStageStageStatus_Object = MibTableColumn
cucsComputePhysicalFsmStageStageStatus = _CucsComputePhysicalFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 51, 1, 9),
    _CucsComputePhysicalFsmStageStageStatus_Type()
)
cucsComputePhysicalFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePhysicalFsmStageStageStatus.setStatus("current")
_CucsComputeRackUnitFsmTable_Object = MibTable
cucsComputeRackUnitFsmTable = _CucsComputeRackUnitFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52)
)
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmTable.setStatus("current")
_CucsComputeRackUnitFsmEntry_Object = MibTableRow
cucsComputeRackUnitFsmEntry = _CucsComputeRackUnitFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52, 1)
)
cucsComputeRackUnitFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeRackUnitFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmEntry.setStatus("current")
_CucsComputeRackUnitFsmInstanceId_Type = CucsManagedObjectId
_CucsComputeRackUnitFsmInstanceId_Object = MibTableColumn
cucsComputeRackUnitFsmInstanceId = _CucsComputeRackUnitFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52, 1, 1),
    _CucsComputeRackUnitFsmInstanceId_Type()
)
cucsComputeRackUnitFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmInstanceId.setStatus("current")
_CucsComputeRackUnitFsmDn_Type = CucsManagedObjectDn
_CucsComputeRackUnitFsmDn_Object = MibTableColumn
cucsComputeRackUnitFsmDn = _CucsComputeRackUnitFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52, 1, 2),
    _CucsComputeRackUnitFsmDn_Type()
)
cucsComputeRackUnitFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmDn.setStatus("current")
_CucsComputeRackUnitFsmRn_Type = SnmpAdminString
_CucsComputeRackUnitFsmRn_Object = MibTableColumn
cucsComputeRackUnitFsmRn = _CucsComputeRackUnitFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52, 1, 3),
    _CucsComputeRackUnitFsmRn_Type()
)
cucsComputeRackUnitFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmRn.setStatus("current")
_CucsComputeRackUnitFsmCompletionTime_Type = DateAndTime
_CucsComputeRackUnitFsmCompletionTime_Object = MibTableColumn
cucsComputeRackUnitFsmCompletionTime = _CucsComputeRackUnitFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52, 1, 4),
    _CucsComputeRackUnitFsmCompletionTime_Type()
)
cucsComputeRackUnitFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmCompletionTime.setStatus("current")
_CucsComputeRackUnitFsmCurrentFsm_Type = CucsComputeRackUnitFsmCurrentFsm
_CucsComputeRackUnitFsmCurrentFsm_Object = MibTableColumn
cucsComputeRackUnitFsmCurrentFsm = _CucsComputeRackUnitFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52, 1, 5),
    _CucsComputeRackUnitFsmCurrentFsm_Type()
)
cucsComputeRackUnitFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmCurrentFsm.setStatus("current")
_CucsComputeRackUnitFsmDescrData_Type = SnmpAdminString
_CucsComputeRackUnitFsmDescrData_Object = MibTableColumn
cucsComputeRackUnitFsmDescrData = _CucsComputeRackUnitFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52, 1, 6),
    _CucsComputeRackUnitFsmDescrData_Type()
)
cucsComputeRackUnitFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmDescrData.setStatus("current")
_CucsComputeRackUnitFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsComputeRackUnitFsmFsmStatus_Object = MibTableColumn
cucsComputeRackUnitFsmFsmStatus = _CucsComputeRackUnitFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52, 1, 7),
    _CucsComputeRackUnitFsmFsmStatus_Type()
)
cucsComputeRackUnitFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmFsmStatus.setStatus("current")
_CucsComputeRackUnitFsmProgress_Type = Gauge32
_CucsComputeRackUnitFsmProgress_Object = MibTableColumn
cucsComputeRackUnitFsmProgress = _CucsComputeRackUnitFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52, 1, 8),
    _CucsComputeRackUnitFsmProgress_Type()
)
cucsComputeRackUnitFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmProgress.setStatus("current")
_CucsComputeRackUnitFsmRmtErrCode_Type = Gauge32
_CucsComputeRackUnitFsmRmtErrCode_Object = MibTableColumn
cucsComputeRackUnitFsmRmtErrCode = _CucsComputeRackUnitFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52, 1, 9),
    _CucsComputeRackUnitFsmRmtErrCode_Type()
)
cucsComputeRackUnitFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmRmtErrCode.setStatus("current")
_CucsComputeRackUnitFsmRmtErrDescr_Type = SnmpAdminString
_CucsComputeRackUnitFsmRmtErrDescr_Object = MibTableColumn
cucsComputeRackUnitFsmRmtErrDescr = _CucsComputeRackUnitFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52, 1, 10),
    _CucsComputeRackUnitFsmRmtErrDescr_Type()
)
cucsComputeRackUnitFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmRmtErrDescr.setStatus("current")
_CucsComputeRackUnitFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsComputeRackUnitFsmRmtRslt_Object = MibTableColumn
cucsComputeRackUnitFsmRmtRslt = _CucsComputeRackUnitFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 52, 1, 11),
    _CucsComputeRackUnitFsmRmtRslt_Type()
)
cucsComputeRackUnitFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmRmtRslt.setStatus("current")
_CucsComputeRackUnitFsmStageTable_Object = MibTable
cucsComputeRackUnitFsmStageTable = _CucsComputeRackUnitFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 53)
)
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStageTable.setStatus("current")
_CucsComputeRackUnitFsmStageEntry_Object = MibTableRow
cucsComputeRackUnitFsmStageEntry = _CucsComputeRackUnitFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 53, 1)
)
cucsComputeRackUnitFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeRackUnitFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStageEntry.setStatus("current")
_CucsComputeRackUnitFsmStageInstanceId_Type = CucsManagedObjectId
_CucsComputeRackUnitFsmStageInstanceId_Object = MibTableColumn
cucsComputeRackUnitFsmStageInstanceId = _CucsComputeRackUnitFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 53, 1, 1),
    _CucsComputeRackUnitFsmStageInstanceId_Type()
)
cucsComputeRackUnitFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStageInstanceId.setStatus("current")
_CucsComputeRackUnitFsmStageDn_Type = CucsManagedObjectDn
_CucsComputeRackUnitFsmStageDn_Object = MibTableColumn
cucsComputeRackUnitFsmStageDn = _CucsComputeRackUnitFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 53, 1, 2),
    _CucsComputeRackUnitFsmStageDn_Type()
)
cucsComputeRackUnitFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStageDn.setStatus("current")
_CucsComputeRackUnitFsmStageRn_Type = SnmpAdminString
_CucsComputeRackUnitFsmStageRn_Object = MibTableColumn
cucsComputeRackUnitFsmStageRn = _CucsComputeRackUnitFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 53, 1, 3),
    _CucsComputeRackUnitFsmStageRn_Type()
)
cucsComputeRackUnitFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStageRn.setStatus("current")
_CucsComputeRackUnitFsmStageDescrData_Type = SnmpAdminString
_CucsComputeRackUnitFsmStageDescrData_Object = MibTableColumn
cucsComputeRackUnitFsmStageDescrData = _CucsComputeRackUnitFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 53, 1, 4),
    _CucsComputeRackUnitFsmStageDescrData_Type()
)
cucsComputeRackUnitFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStageDescrData.setStatus("current")
_CucsComputeRackUnitFsmStageLastUpdateTime_Type = DateAndTime
_CucsComputeRackUnitFsmStageLastUpdateTime_Object = MibTableColumn
cucsComputeRackUnitFsmStageLastUpdateTime = _CucsComputeRackUnitFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 53, 1, 5),
    _CucsComputeRackUnitFsmStageLastUpdateTime_Type()
)
cucsComputeRackUnitFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStageLastUpdateTime.setStatus("current")
_CucsComputeRackUnitFsmStageName_Type = CucsComputeRackUnitFsmStageName
_CucsComputeRackUnitFsmStageName_Object = MibTableColumn
cucsComputeRackUnitFsmStageName = _CucsComputeRackUnitFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 53, 1, 6),
    _CucsComputeRackUnitFsmStageName_Type()
)
cucsComputeRackUnitFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStageName.setStatus("current")
_CucsComputeRackUnitFsmStageOrder_Type = Gauge32
_CucsComputeRackUnitFsmStageOrder_Object = MibTableColumn
cucsComputeRackUnitFsmStageOrder = _CucsComputeRackUnitFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 53, 1, 7),
    _CucsComputeRackUnitFsmStageOrder_Type()
)
cucsComputeRackUnitFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStageOrder.setStatus("current")
_CucsComputeRackUnitFsmStageRetry_Type = Gauge32
_CucsComputeRackUnitFsmStageRetry_Object = MibTableColumn
cucsComputeRackUnitFsmStageRetry = _CucsComputeRackUnitFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 53, 1, 8),
    _CucsComputeRackUnitFsmStageRetry_Type()
)
cucsComputeRackUnitFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStageRetry.setStatus("current")
_CucsComputeRackUnitFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsComputeRackUnitFsmStageStageStatus_Object = MibTableColumn
cucsComputeRackUnitFsmStageStageStatus = _CucsComputeRackUnitFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 53, 1, 9),
    _CucsComputeRackUnitFsmStageStageStatus_Type()
)
cucsComputeRackUnitFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeRackUnitFsmStageStageStatus.setStatus("current")
_CucsComputeServerDiscPolicyFsmTable_Object = MibTable
cucsComputeServerDiscPolicyFsmTable = _CucsComputeServerDiscPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54)
)
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmTable.setStatus("current")
_CucsComputeServerDiscPolicyFsmEntry_Object = MibTableRow
cucsComputeServerDiscPolicyFsmEntry = _CucsComputeServerDiscPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54, 1)
)
cucsComputeServerDiscPolicyFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeServerDiscPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmEntry.setStatus("current")
_CucsComputeServerDiscPolicyFsmInstanceId_Type = CucsManagedObjectId
_CucsComputeServerDiscPolicyFsmInstanceId_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmInstanceId = _CucsComputeServerDiscPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54, 1, 1),
    _CucsComputeServerDiscPolicyFsmInstanceId_Type()
)
cucsComputeServerDiscPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmInstanceId.setStatus("current")
_CucsComputeServerDiscPolicyFsmDn_Type = CucsManagedObjectDn
_CucsComputeServerDiscPolicyFsmDn_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmDn = _CucsComputeServerDiscPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54, 1, 2),
    _CucsComputeServerDiscPolicyFsmDn_Type()
)
cucsComputeServerDiscPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmDn.setStatus("current")
_CucsComputeServerDiscPolicyFsmRn_Type = SnmpAdminString
_CucsComputeServerDiscPolicyFsmRn_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmRn = _CucsComputeServerDiscPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54, 1, 3),
    _CucsComputeServerDiscPolicyFsmRn_Type()
)
cucsComputeServerDiscPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmRn.setStatus("current")
_CucsComputeServerDiscPolicyFsmCompletionTime_Type = DateAndTime
_CucsComputeServerDiscPolicyFsmCompletionTime_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmCompletionTime = _CucsComputeServerDiscPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54, 1, 4),
    _CucsComputeServerDiscPolicyFsmCompletionTime_Type()
)
cucsComputeServerDiscPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmCompletionTime.setStatus("current")
_CucsComputeServerDiscPolicyFsmCurrentFsm_Type = CucsComputeServerDiscPolicyFsmCurrentFsm
_CucsComputeServerDiscPolicyFsmCurrentFsm_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmCurrentFsm = _CucsComputeServerDiscPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54, 1, 5),
    _CucsComputeServerDiscPolicyFsmCurrentFsm_Type()
)
cucsComputeServerDiscPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmCurrentFsm.setStatus("current")
_CucsComputeServerDiscPolicyFsmDescrData_Type = SnmpAdminString
_CucsComputeServerDiscPolicyFsmDescrData_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmDescrData = _CucsComputeServerDiscPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54, 1, 6),
    _CucsComputeServerDiscPolicyFsmDescrData_Type()
)
cucsComputeServerDiscPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmDescrData.setStatus("current")
_CucsComputeServerDiscPolicyFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsComputeServerDiscPolicyFsmFsmStatus_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmFsmStatus = _CucsComputeServerDiscPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54, 1, 7),
    _CucsComputeServerDiscPolicyFsmFsmStatus_Type()
)
cucsComputeServerDiscPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmFsmStatus.setStatus("current")
_CucsComputeServerDiscPolicyFsmProgress_Type = Gauge32
_CucsComputeServerDiscPolicyFsmProgress_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmProgress = _CucsComputeServerDiscPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54, 1, 8),
    _CucsComputeServerDiscPolicyFsmProgress_Type()
)
cucsComputeServerDiscPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmProgress.setStatus("current")
_CucsComputeServerDiscPolicyFsmRmtErrCode_Type = Gauge32
_CucsComputeServerDiscPolicyFsmRmtErrCode_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmRmtErrCode = _CucsComputeServerDiscPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54, 1, 9),
    _CucsComputeServerDiscPolicyFsmRmtErrCode_Type()
)
cucsComputeServerDiscPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmRmtErrCode.setStatus("current")
_CucsComputeServerDiscPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CucsComputeServerDiscPolicyFsmRmtErrDescr_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmRmtErrDescr = _CucsComputeServerDiscPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54, 1, 10),
    _CucsComputeServerDiscPolicyFsmRmtErrDescr_Type()
)
cucsComputeServerDiscPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmRmtErrDescr.setStatus("current")
_CucsComputeServerDiscPolicyFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsComputeServerDiscPolicyFsmRmtRslt_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmRmtRslt = _CucsComputeServerDiscPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 54, 1, 11),
    _CucsComputeServerDiscPolicyFsmRmtRslt_Type()
)
cucsComputeServerDiscPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmRmtRslt.setStatus("current")
_CucsComputeServerDiscPolicyFsmStageTable_Object = MibTable
cucsComputeServerDiscPolicyFsmStageTable = _CucsComputeServerDiscPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 55)
)
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStageTable.setStatus("current")
_CucsComputeServerDiscPolicyFsmStageEntry_Object = MibTableRow
cucsComputeServerDiscPolicyFsmStageEntry = _CucsComputeServerDiscPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 55, 1)
)
cucsComputeServerDiscPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeServerDiscPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStageEntry.setStatus("current")
_CucsComputeServerDiscPolicyFsmStageInstanceId_Type = CucsManagedObjectId
_CucsComputeServerDiscPolicyFsmStageInstanceId_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmStageInstanceId = _CucsComputeServerDiscPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 55, 1, 1),
    _CucsComputeServerDiscPolicyFsmStageInstanceId_Type()
)
cucsComputeServerDiscPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStageInstanceId.setStatus("current")
_CucsComputeServerDiscPolicyFsmStageDn_Type = CucsManagedObjectDn
_CucsComputeServerDiscPolicyFsmStageDn_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmStageDn = _CucsComputeServerDiscPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 55, 1, 2),
    _CucsComputeServerDiscPolicyFsmStageDn_Type()
)
cucsComputeServerDiscPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStageDn.setStatus("current")
_CucsComputeServerDiscPolicyFsmStageRn_Type = SnmpAdminString
_CucsComputeServerDiscPolicyFsmStageRn_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmStageRn = _CucsComputeServerDiscPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 55, 1, 3),
    _CucsComputeServerDiscPolicyFsmStageRn_Type()
)
cucsComputeServerDiscPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStageRn.setStatus("current")
_CucsComputeServerDiscPolicyFsmStageDescrData_Type = SnmpAdminString
_CucsComputeServerDiscPolicyFsmStageDescrData_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmStageDescrData = _CucsComputeServerDiscPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 55, 1, 4),
    _CucsComputeServerDiscPolicyFsmStageDescrData_Type()
)
cucsComputeServerDiscPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStageDescrData.setStatus("current")
_CucsComputeServerDiscPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CucsComputeServerDiscPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmStageLastUpdateTime = _CucsComputeServerDiscPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 55, 1, 5),
    _CucsComputeServerDiscPolicyFsmStageLastUpdateTime_Type()
)
cucsComputeServerDiscPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStageLastUpdateTime.setStatus("current")
_CucsComputeServerDiscPolicyFsmStageName_Type = CucsComputeServerDiscPolicyFsmStageName
_CucsComputeServerDiscPolicyFsmStageName_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmStageName = _CucsComputeServerDiscPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 55, 1, 6),
    _CucsComputeServerDiscPolicyFsmStageName_Type()
)
cucsComputeServerDiscPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStageName.setStatus("current")
_CucsComputeServerDiscPolicyFsmStageOrder_Type = Gauge32
_CucsComputeServerDiscPolicyFsmStageOrder_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmStageOrder = _CucsComputeServerDiscPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 55, 1, 7),
    _CucsComputeServerDiscPolicyFsmStageOrder_Type()
)
cucsComputeServerDiscPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStageOrder.setStatus("current")
_CucsComputeServerDiscPolicyFsmStageRetry_Type = Gauge32
_CucsComputeServerDiscPolicyFsmStageRetry_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmStageRetry = _CucsComputeServerDiscPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 55, 1, 8),
    _CucsComputeServerDiscPolicyFsmStageRetry_Type()
)
cucsComputeServerDiscPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStageRetry.setStatus("current")
_CucsComputeServerDiscPolicyFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsComputeServerDiscPolicyFsmStageStageStatus_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmStageStageStatus = _CucsComputeServerDiscPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 55, 1, 9),
    _CucsComputeServerDiscPolicyFsmStageStageStatus_Type()
)
cucsComputeServerDiscPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmStageStageStatus.setStatus("current")
_CucsComputeServerDiscPolicyFsmTaskTable_Object = MibTable
cucsComputeServerDiscPolicyFsmTaskTable = _CucsComputeServerDiscPolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 56)
)
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmTaskTable.setStatus("current")
_CucsComputeServerDiscPolicyFsmTaskEntry_Object = MibTableRow
cucsComputeServerDiscPolicyFsmTaskEntry = _CucsComputeServerDiscPolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 56, 1)
)
cucsComputeServerDiscPolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeServerDiscPolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmTaskEntry.setStatus("current")
_CucsComputeServerDiscPolicyFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsComputeServerDiscPolicyFsmTaskInstanceId_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmTaskInstanceId = _CucsComputeServerDiscPolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 56, 1, 1),
    _CucsComputeServerDiscPolicyFsmTaskInstanceId_Type()
)
cucsComputeServerDiscPolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmTaskInstanceId.setStatus("current")
_CucsComputeServerDiscPolicyFsmTaskDn_Type = CucsManagedObjectDn
_CucsComputeServerDiscPolicyFsmTaskDn_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmTaskDn = _CucsComputeServerDiscPolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 56, 1, 2),
    _CucsComputeServerDiscPolicyFsmTaskDn_Type()
)
cucsComputeServerDiscPolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmTaskDn.setStatus("current")
_CucsComputeServerDiscPolicyFsmTaskRn_Type = SnmpAdminString
_CucsComputeServerDiscPolicyFsmTaskRn_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmTaskRn = _CucsComputeServerDiscPolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 56, 1, 3),
    _CucsComputeServerDiscPolicyFsmTaskRn_Type()
)
cucsComputeServerDiscPolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmTaskRn.setStatus("current")
_CucsComputeServerDiscPolicyFsmTaskCompletion_Type = CucsFsmCompletion
_CucsComputeServerDiscPolicyFsmTaskCompletion_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmTaskCompletion = _CucsComputeServerDiscPolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 56, 1, 4),
    _CucsComputeServerDiscPolicyFsmTaskCompletion_Type()
)
cucsComputeServerDiscPolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmTaskCompletion.setStatus("current")
_CucsComputeServerDiscPolicyFsmTaskFlags_Type = CucsFsmFlags
_CucsComputeServerDiscPolicyFsmTaskFlags_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmTaskFlags = _CucsComputeServerDiscPolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 56, 1, 5),
    _CucsComputeServerDiscPolicyFsmTaskFlags_Type()
)
cucsComputeServerDiscPolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmTaskFlags.setStatus("current")
_CucsComputeServerDiscPolicyFsmTaskItem_Type = CucsComputeServerDiscPolicyFsmTaskItem
_CucsComputeServerDiscPolicyFsmTaskItem_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmTaskItem = _CucsComputeServerDiscPolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 56, 1, 6),
    _CucsComputeServerDiscPolicyFsmTaskItem_Type()
)
cucsComputeServerDiscPolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmTaskItem.setStatus("current")
_CucsComputeServerDiscPolicyFsmTaskSeqId_Type = Gauge32
_CucsComputeServerDiscPolicyFsmTaskSeqId_Object = MibTableColumn
cucsComputeServerDiscPolicyFsmTaskSeqId = _CucsComputeServerDiscPolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 56, 1, 7),
    _CucsComputeServerDiscPolicyFsmTaskSeqId_Type()
)
cucsComputeServerDiscPolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerDiscPolicyFsmTaskSeqId.setStatus("current")
_CucsComputeServerMgmtPolicyTable_Object = MibTable
cucsComputeServerMgmtPolicyTable = _CucsComputeServerMgmtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 57)
)
if mibBuilder.loadTexts:
    cucsComputeServerMgmtPolicyTable.setStatus("current")
_CucsComputeServerMgmtPolicyEntry_Object = MibTableRow
cucsComputeServerMgmtPolicyEntry = _CucsComputeServerMgmtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 57, 1)
)
cucsComputeServerMgmtPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeServerMgmtPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeServerMgmtPolicyEntry.setStatus("current")
_CucsComputeServerMgmtPolicyInstanceId_Type = CucsManagedObjectId
_CucsComputeServerMgmtPolicyInstanceId_Object = MibTableColumn
cucsComputeServerMgmtPolicyInstanceId = _CucsComputeServerMgmtPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 57, 1, 1),
    _CucsComputeServerMgmtPolicyInstanceId_Type()
)
cucsComputeServerMgmtPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeServerMgmtPolicyInstanceId.setStatus("current")
_CucsComputeServerMgmtPolicyDn_Type = CucsManagedObjectDn
_CucsComputeServerMgmtPolicyDn_Object = MibTableColumn
cucsComputeServerMgmtPolicyDn = _CucsComputeServerMgmtPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 57, 1, 2),
    _CucsComputeServerMgmtPolicyDn_Type()
)
cucsComputeServerMgmtPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerMgmtPolicyDn.setStatus("current")
_CucsComputeServerMgmtPolicyRn_Type = SnmpAdminString
_CucsComputeServerMgmtPolicyRn_Object = MibTableColumn
cucsComputeServerMgmtPolicyRn = _CucsComputeServerMgmtPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 57, 1, 3),
    _CucsComputeServerMgmtPolicyRn_Type()
)
cucsComputeServerMgmtPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerMgmtPolicyRn.setStatus("current")
_CucsComputeServerMgmtPolicyAction_Type = CucsComputeServerMgmtDiscAction
_CucsComputeServerMgmtPolicyAction_Object = MibTableColumn
cucsComputeServerMgmtPolicyAction = _CucsComputeServerMgmtPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 57, 1, 4),
    _CucsComputeServerMgmtPolicyAction_Type()
)
cucsComputeServerMgmtPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerMgmtPolicyAction.setStatus("current")
_CucsComputeServerMgmtPolicyDescr_Type = SnmpAdminString
_CucsComputeServerMgmtPolicyDescr_Object = MibTableColumn
cucsComputeServerMgmtPolicyDescr = _CucsComputeServerMgmtPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 57, 1, 5),
    _CucsComputeServerMgmtPolicyDescr_Type()
)
cucsComputeServerMgmtPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerMgmtPolicyDescr.setStatus("current")
_CucsComputeServerMgmtPolicyIntId_Type = SnmpAdminString
_CucsComputeServerMgmtPolicyIntId_Object = MibTableColumn
cucsComputeServerMgmtPolicyIntId = _CucsComputeServerMgmtPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 57, 1, 6),
    _CucsComputeServerMgmtPolicyIntId_Type()
)
cucsComputeServerMgmtPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerMgmtPolicyIntId.setStatus("current")
_CucsComputeServerMgmtPolicyName_Type = SnmpAdminString
_CucsComputeServerMgmtPolicyName_Object = MibTableColumn
cucsComputeServerMgmtPolicyName = _CucsComputeServerMgmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 57, 1, 7),
    _CucsComputeServerMgmtPolicyName_Type()
)
cucsComputeServerMgmtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerMgmtPolicyName.setStatus("current")
_CucsComputeServerMgmtPolicyPolicyLevel_Type = Gauge32
_CucsComputeServerMgmtPolicyPolicyLevel_Object = MibTableColumn
cucsComputeServerMgmtPolicyPolicyLevel = _CucsComputeServerMgmtPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 57, 1, 8),
    _CucsComputeServerMgmtPolicyPolicyLevel_Type()
)
cucsComputeServerMgmtPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerMgmtPolicyPolicyLevel.setStatus("current")
_CucsComputeServerMgmtPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeServerMgmtPolicyPolicyOwner_Object = MibTableColumn
cucsComputeServerMgmtPolicyPolicyOwner = _CucsComputeServerMgmtPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 57, 1, 9),
    _CucsComputeServerMgmtPolicyPolicyOwner_Type()
)
cucsComputeServerMgmtPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerMgmtPolicyPolicyOwner.setStatus("current")
_CucsComputeServerMgmtPolicyQualifier_Type = SnmpAdminString
_CucsComputeServerMgmtPolicyQualifier_Object = MibTableColumn
cucsComputeServerMgmtPolicyQualifier = _CucsComputeServerMgmtPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 57, 1, 10),
    _CucsComputeServerMgmtPolicyQualifier_Type()
)
cucsComputeServerMgmtPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerMgmtPolicyQualifier.setStatus("current")
_CucsComputePciSlotScanDefTable_Object = MibTable
cucsComputePciSlotScanDefTable = _CucsComputePciSlotScanDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 58)
)
if mibBuilder.loadTexts:
    cucsComputePciSlotScanDefTable.setStatus("current")
_CucsComputePciSlotScanDefEntry_Object = MibTableRow
cucsComputePciSlotScanDefEntry = _CucsComputePciSlotScanDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 58, 1)
)
cucsComputePciSlotScanDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePciSlotScanDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePciSlotScanDefEntry.setStatus("current")
_CucsComputePciSlotScanDefInstanceId_Type = CucsManagedObjectId
_CucsComputePciSlotScanDefInstanceId_Object = MibTableColumn
cucsComputePciSlotScanDefInstanceId = _CucsComputePciSlotScanDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 58, 1, 1),
    _CucsComputePciSlotScanDefInstanceId_Type()
)
cucsComputePciSlotScanDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePciSlotScanDefInstanceId.setStatus("current")
_CucsComputePciSlotScanDefDn_Type = CucsManagedObjectDn
_CucsComputePciSlotScanDefDn_Object = MibTableColumn
cucsComputePciSlotScanDefDn = _CucsComputePciSlotScanDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 58, 1, 2),
    _CucsComputePciSlotScanDefDn_Type()
)
cucsComputePciSlotScanDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciSlotScanDefDn.setStatus("current")
_CucsComputePciSlotScanDefRn_Type = SnmpAdminString
_CucsComputePciSlotScanDefRn_Object = MibTableColumn
cucsComputePciSlotScanDefRn = _CucsComputePciSlotScanDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 58, 1, 3),
    _CucsComputePciSlotScanDefRn_Type()
)
cucsComputePciSlotScanDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciSlotScanDefRn.setStatus("current")
_CucsComputePciSlotScanDefDescr_Type = SnmpAdminString
_CucsComputePciSlotScanDefDescr_Object = MibTableColumn
cucsComputePciSlotScanDefDescr = _CucsComputePciSlotScanDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 58, 1, 4),
    _CucsComputePciSlotScanDefDescr_Type()
)
cucsComputePciSlotScanDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciSlotScanDefDescr.setStatus("current")
_CucsComputePciSlotScanDefIntId_Type = SnmpAdminString
_CucsComputePciSlotScanDefIntId_Object = MibTableColumn
cucsComputePciSlotScanDefIntId = _CucsComputePciSlotScanDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 58, 1, 5),
    _CucsComputePciSlotScanDefIntId_Type()
)
cucsComputePciSlotScanDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciSlotScanDefIntId.setStatus("current")
_CucsComputePciSlotScanDefName_Type = SnmpAdminString
_CucsComputePciSlotScanDefName_Object = MibTableColumn
cucsComputePciSlotScanDefName = _CucsComputePciSlotScanDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 58, 1, 6),
    _CucsComputePciSlotScanDefName_Type()
)
cucsComputePciSlotScanDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciSlotScanDefName.setStatus("current")
_CucsComputePciSlotScanDefPolicyLevel_Type = Gauge32
_CucsComputePciSlotScanDefPolicyLevel_Object = MibTableColumn
cucsComputePciSlotScanDefPolicyLevel = _CucsComputePciSlotScanDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 58, 1, 7),
    _CucsComputePciSlotScanDefPolicyLevel_Type()
)
cucsComputePciSlotScanDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciSlotScanDefPolicyLevel.setStatus("current")
_CucsComputePciSlotScanDefPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputePciSlotScanDefPolicyOwner_Object = MibTableColumn
cucsComputePciSlotScanDefPolicyOwner = _CucsComputePciSlotScanDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 58, 1, 8),
    _CucsComputePciSlotScanDefPolicyOwner_Type()
)
cucsComputePciSlotScanDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciSlotScanDefPolicyOwner.setStatus("current")
_CucsComputePciSlotScanDefScanOrder_Type = Gauge32
_CucsComputePciSlotScanDefScanOrder_Object = MibTableColumn
cucsComputePciSlotScanDefScanOrder = _CucsComputePciSlotScanDefScanOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 58, 1, 9),
    _CucsComputePciSlotScanDefScanOrder_Type()
)
cucsComputePciSlotScanDefScanOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciSlotScanDefScanOrder.setStatus("current")
_CucsComputePciSlotScanDefSlotId_Type = Gauge32
_CucsComputePciSlotScanDefSlotId_Object = MibTableColumn
cucsComputePciSlotScanDefSlotId = _CucsComputePciSlotScanDefSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 58, 1, 10),
    _CucsComputePciSlotScanDefSlotId_Type()
)
cucsComputePciSlotScanDefSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePciSlotScanDefSlotId.setStatus("current")
_CucsComputeHealthLedSensorAlarmTable_Object = MibTable
cucsComputeHealthLedSensorAlarmTable = _CucsComputeHealthLedSensorAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 59)
)
if mibBuilder.loadTexts:
    cucsComputeHealthLedSensorAlarmTable.setStatus("current")
_CucsComputeHealthLedSensorAlarmEntry_Object = MibTableRow
cucsComputeHealthLedSensorAlarmEntry = _CucsComputeHealthLedSensorAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 59, 1)
)
cucsComputeHealthLedSensorAlarmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeHealthLedSensorAlarmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeHealthLedSensorAlarmEntry.setStatus("current")
_CucsComputeHealthLedSensorAlarmInstanceId_Type = CucsManagedObjectId
_CucsComputeHealthLedSensorAlarmInstanceId_Object = MibTableColumn
cucsComputeHealthLedSensorAlarmInstanceId = _CucsComputeHealthLedSensorAlarmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 59, 1, 1),
    _CucsComputeHealthLedSensorAlarmInstanceId_Type()
)
cucsComputeHealthLedSensorAlarmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeHealthLedSensorAlarmInstanceId.setStatus("current")
_CucsComputeHealthLedSensorAlarmDn_Type = CucsManagedObjectDn
_CucsComputeHealthLedSensorAlarmDn_Object = MibTableColumn
cucsComputeHealthLedSensorAlarmDn = _CucsComputeHealthLedSensorAlarmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 59, 1, 2),
    _CucsComputeHealthLedSensorAlarmDn_Type()
)
cucsComputeHealthLedSensorAlarmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeHealthLedSensorAlarmDn.setStatus("current")
_CucsComputeHealthLedSensorAlarmRn_Type = SnmpAdminString
_CucsComputeHealthLedSensorAlarmRn_Object = MibTableColumn
cucsComputeHealthLedSensorAlarmRn = _CucsComputeHealthLedSensorAlarmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 59, 1, 3),
    _CucsComputeHealthLedSensorAlarmRn_Type()
)
cucsComputeHealthLedSensorAlarmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeHealthLedSensorAlarmRn.setStatus("current")
_CucsComputeHealthLedSensorAlarmAlarmDesc_Type = SnmpAdminString
_CucsComputeHealthLedSensorAlarmAlarmDesc_Object = MibTableColumn
cucsComputeHealthLedSensorAlarmAlarmDesc = _CucsComputeHealthLedSensorAlarmAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 59, 1, 4),
    _CucsComputeHealthLedSensorAlarmAlarmDesc_Type()
)
cucsComputeHealthLedSensorAlarmAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeHealthLedSensorAlarmAlarmDesc.setStatus("current")
_CucsComputeHealthLedSensorAlarmAlarmSeverity_Type = CucsComputeAlarmSeverity
_CucsComputeHealthLedSensorAlarmAlarmSeverity_Object = MibTableColumn
cucsComputeHealthLedSensorAlarmAlarmSeverity = _CucsComputeHealthLedSensorAlarmAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 59, 1, 5),
    _CucsComputeHealthLedSensorAlarmAlarmSeverity_Type()
)
cucsComputeHealthLedSensorAlarmAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeHealthLedSensorAlarmAlarmSeverity.setStatus("current")
_CucsComputeHealthLedSensorAlarmSensorId_Type = Gauge32
_CucsComputeHealthLedSensorAlarmSensorId_Object = MibTableColumn
cucsComputeHealthLedSensorAlarmSensorId = _CucsComputeHealthLedSensorAlarmSensorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 59, 1, 6),
    _CucsComputeHealthLedSensorAlarmSensorId_Type()
)
cucsComputeHealthLedSensorAlarmSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeHealthLedSensorAlarmSensorId.setStatus("current")
_CucsComputeHealthLedSensorAlarmSensorName_Type = SnmpAdminString
_CucsComputeHealthLedSensorAlarmSensorName_Object = MibTableColumn
cucsComputeHealthLedSensorAlarmSensorName = _CucsComputeHealthLedSensorAlarmSensorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 59, 1, 7),
    _CucsComputeHealthLedSensorAlarmSensorName_Type()
)
cucsComputeHealthLedSensorAlarmSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeHealthLedSensorAlarmSensorName.setStatus("current")
_CucsComputeFwSyncAckTable_Object = MibTable
cucsComputeFwSyncAckTable = _CucsComputeFwSyncAckTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60)
)
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckTable.setStatus("current")
_CucsComputeFwSyncAckEntry_Object = MibTableRow
cucsComputeFwSyncAckEntry = _CucsComputeFwSyncAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1)
)
cucsComputeFwSyncAckEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeFwSyncAckInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckEntry.setStatus("current")
_CucsComputeFwSyncAckInstanceId_Type = CucsManagedObjectId
_CucsComputeFwSyncAckInstanceId_Object = MibTableColumn
cucsComputeFwSyncAckInstanceId = _CucsComputeFwSyncAckInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 1),
    _CucsComputeFwSyncAckInstanceId_Type()
)
cucsComputeFwSyncAckInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckInstanceId.setStatus("current")
_CucsComputeFwSyncAckDn_Type = CucsManagedObjectDn
_CucsComputeFwSyncAckDn_Object = MibTableColumn
cucsComputeFwSyncAckDn = _CucsComputeFwSyncAckDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 2),
    _CucsComputeFwSyncAckDn_Type()
)
cucsComputeFwSyncAckDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckDn.setStatus("current")
_CucsComputeFwSyncAckRn_Type = SnmpAdminString
_CucsComputeFwSyncAckRn_Object = MibTableColumn
cucsComputeFwSyncAckRn = _CucsComputeFwSyncAckRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 3),
    _CucsComputeFwSyncAckRn_Type()
)
cucsComputeFwSyncAckRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckRn.setStatus("current")
_CucsComputeFwSyncAckAcked_Type = DateAndTime
_CucsComputeFwSyncAckAcked_Object = MibTableColumn
cucsComputeFwSyncAckAcked = _CucsComputeFwSyncAckAcked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 4),
    _CucsComputeFwSyncAckAcked_Type()
)
cucsComputeFwSyncAckAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckAcked.setStatus("current")
_CucsComputeFwSyncAckAckedBy_Type = SnmpAdminString
_CucsComputeFwSyncAckAckedBy_Object = MibTableColumn
cucsComputeFwSyncAckAckedBy = _CucsComputeFwSyncAckAckedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 5),
    _CucsComputeFwSyncAckAckedBy_Type()
)
cucsComputeFwSyncAckAckedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckAckedBy.setStatus("current")
_CucsComputeFwSyncAckAdminState_Type = CucsTrigAdminState
_CucsComputeFwSyncAckAdminState_Object = MibTableColumn
cucsComputeFwSyncAckAdminState = _CucsComputeFwSyncAckAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 6),
    _CucsComputeFwSyncAckAdminState_Type()
)
cucsComputeFwSyncAckAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckAdminState.setStatus("current")
_CucsComputeFwSyncAckAutoDelete_Type = TruthValue
_CucsComputeFwSyncAckAutoDelete_Object = MibTableColumn
cucsComputeFwSyncAckAutoDelete = _CucsComputeFwSyncAckAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 7),
    _CucsComputeFwSyncAckAutoDelete_Type()
)
cucsComputeFwSyncAckAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckAutoDelete.setStatus("current")
_CucsComputeFwSyncAckChangeBy_Type = SnmpAdminString
_CucsComputeFwSyncAckChangeBy_Object = MibTableColumn
cucsComputeFwSyncAckChangeBy = _CucsComputeFwSyncAckChangeBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 8),
    _CucsComputeFwSyncAckChangeBy_Type()
)
cucsComputeFwSyncAckChangeBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckChangeBy.setStatus("current")
_CucsComputeFwSyncAckChangeDetails_Type = CucsTrigAckChangeDetails
_CucsComputeFwSyncAckChangeDetails_Object = MibTableColumn
cucsComputeFwSyncAckChangeDetails = _CucsComputeFwSyncAckChangeDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 9),
    _CucsComputeFwSyncAckChangeDetails_Type()
)
cucsComputeFwSyncAckChangeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckChangeDetails.setStatus("current")
_CucsComputeFwSyncAckChanges_Type = CucsTrigAckChanges
_CucsComputeFwSyncAckChanges_Object = MibTableColumn
cucsComputeFwSyncAckChanges = _CucsComputeFwSyncAckChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 10),
    _CucsComputeFwSyncAckChanges_Type()
)
cucsComputeFwSyncAckChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckChanges.setStatus("current")
_CucsComputeFwSyncAckDescr_Type = SnmpAdminString
_CucsComputeFwSyncAckDescr_Object = MibTableColumn
cucsComputeFwSyncAckDescr = _CucsComputeFwSyncAckDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 11),
    _CucsComputeFwSyncAckDescr_Type()
)
cucsComputeFwSyncAckDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckDescr.setStatus("current")
_CucsComputeFwSyncAckDisr_Type = CucsTrigAckDisr
_CucsComputeFwSyncAckDisr_Object = MibTableColumn
cucsComputeFwSyncAckDisr = _CucsComputeFwSyncAckDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 12),
    _CucsComputeFwSyncAckDisr_Type()
)
cucsComputeFwSyncAckDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckDisr.setStatus("current")
_CucsComputeFwSyncAckIgnoreCap_Type = TruthValue
_CucsComputeFwSyncAckIgnoreCap_Object = MibTableColumn
cucsComputeFwSyncAckIgnoreCap = _CucsComputeFwSyncAckIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 13),
    _CucsComputeFwSyncAckIgnoreCap_Type()
)
cucsComputeFwSyncAckIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckIgnoreCap.setStatus("current")
_CucsComputeFwSyncAckIntId_Type = SnmpAdminString
_CucsComputeFwSyncAckIntId_Object = MibTableColumn
cucsComputeFwSyncAckIntId = _CucsComputeFwSyncAckIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 14),
    _CucsComputeFwSyncAckIntId_Type()
)
cucsComputeFwSyncAckIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckIntId.setStatus("current")
_CucsComputeFwSyncAckModified_Type = DateAndTime
_CucsComputeFwSyncAckModified_Object = MibTableColumn
cucsComputeFwSyncAckModified = _CucsComputeFwSyncAckModified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 15),
    _CucsComputeFwSyncAckModified_Type()
)
cucsComputeFwSyncAckModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckModified.setStatus("current")
_CucsComputeFwSyncAckName_Type = SnmpAdminString
_CucsComputeFwSyncAckName_Object = MibTableColumn
cucsComputeFwSyncAckName = _CucsComputeFwSyncAckName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 16),
    _CucsComputeFwSyncAckName_Type()
)
cucsComputeFwSyncAckName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckName.setStatus("current")
_CucsComputeFwSyncAckOperScheduler_Type = SnmpAdminString
_CucsComputeFwSyncAckOperScheduler_Object = MibTableColumn
cucsComputeFwSyncAckOperScheduler = _CucsComputeFwSyncAckOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 17),
    _CucsComputeFwSyncAckOperScheduler_Type()
)
cucsComputeFwSyncAckOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckOperScheduler.setStatus("current")
_CucsComputeFwSyncAckOperState_Type = CucsTrigAckOperState
_CucsComputeFwSyncAckOperState_Object = MibTableColumn
cucsComputeFwSyncAckOperState = _CucsComputeFwSyncAckOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 18),
    _CucsComputeFwSyncAckOperState_Type()
)
cucsComputeFwSyncAckOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckOperState.setStatus("current")
_CucsComputeFwSyncAckPolicyLevel_Type = Gauge32
_CucsComputeFwSyncAckPolicyLevel_Object = MibTableColumn
cucsComputeFwSyncAckPolicyLevel = _CucsComputeFwSyncAckPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 19),
    _CucsComputeFwSyncAckPolicyLevel_Type()
)
cucsComputeFwSyncAckPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckPolicyLevel.setStatus("current")
_CucsComputeFwSyncAckPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeFwSyncAckPolicyOwner_Object = MibTableColumn
cucsComputeFwSyncAckPolicyOwner = _CucsComputeFwSyncAckPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 20),
    _CucsComputeFwSyncAckPolicyOwner_Type()
)
cucsComputeFwSyncAckPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckPolicyOwner.setStatus("current")
_CucsComputeFwSyncAckPrevOperState_Type = CucsTrigAckPrevOperState
_CucsComputeFwSyncAckPrevOperState_Object = MibTableColumn
cucsComputeFwSyncAckPrevOperState = _CucsComputeFwSyncAckPrevOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 21),
    _CucsComputeFwSyncAckPrevOperState_Type()
)
cucsComputeFwSyncAckPrevOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckPrevOperState.setStatus("current")
_CucsComputeFwSyncAckScheduler_Type = SnmpAdminString
_CucsComputeFwSyncAckScheduler_Object = MibTableColumn
cucsComputeFwSyncAckScheduler = _CucsComputeFwSyncAckScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 22),
    _CucsComputeFwSyncAckScheduler_Type()
)
cucsComputeFwSyncAckScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckScheduler.setStatus("current")
_CucsComputeFwSyncAckTriggerConfigState_Type = CucsTrigTrigState
_CucsComputeFwSyncAckTriggerConfigState_Object = MibTableColumn
cucsComputeFwSyncAckTriggerConfigState = _CucsComputeFwSyncAckTriggerConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 60, 1, 23),
    _CucsComputeFwSyncAckTriggerConfigState_Type()
)
cucsComputeFwSyncAckTriggerConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeFwSyncAckTriggerConfigState.setStatus("current")
_CucsComputeMemoryConfigPolicyTable_Object = MibTable
cucsComputeMemoryConfigPolicyTable = _CucsComputeMemoryConfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 61)
)
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigPolicyTable.setStatus("current")
_CucsComputeMemoryConfigPolicyEntry_Object = MibTableRow
cucsComputeMemoryConfigPolicyEntry = _CucsComputeMemoryConfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 61, 1)
)
cucsComputeMemoryConfigPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeMemoryConfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigPolicyEntry.setStatus("current")
_CucsComputeMemoryConfigPolicyInstanceId_Type = CucsManagedObjectId
_CucsComputeMemoryConfigPolicyInstanceId_Object = MibTableColumn
cucsComputeMemoryConfigPolicyInstanceId = _CucsComputeMemoryConfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 61, 1, 1),
    _CucsComputeMemoryConfigPolicyInstanceId_Type()
)
cucsComputeMemoryConfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigPolicyInstanceId.setStatus("current")
_CucsComputeMemoryConfigPolicyDn_Type = CucsManagedObjectDn
_CucsComputeMemoryConfigPolicyDn_Object = MibTableColumn
cucsComputeMemoryConfigPolicyDn = _CucsComputeMemoryConfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 61, 1, 2),
    _CucsComputeMemoryConfigPolicyDn_Type()
)
cucsComputeMemoryConfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigPolicyDn.setStatus("current")
_CucsComputeMemoryConfigPolicyRn_Type = SnmpAdminString
_CucsComputeMemoryConfigPolicyRn_Object = MibTableColumn
cucsComputeMemoryConfigPolicyRn = _CucsComputeMemoryConfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 61, 1, 3),
    _CucsComputeMemoryConfigPolicyRn_Type()
)
cucsComputeMemoryConfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigPolicyRn.setStatus("current")
_CucsComputeMemoryConfigPolicyBlackListing_Type = CucsComputeBlackListing
_CucsComputeMemoryConfigPolicyBlackListing_Object = MibTableColumn
cucsComputeMemoryConfigPolicyBlackListing = _CucsComputeMemoryConfigPolicyBlackListing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 61, 1, 4),
    _CucsComputeMemoryConfigPolicyBlackListing_Type()
)
cucsComputeMemoryConfigPolicyBlackListing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigPolicyBlackListing.setStatus("current")
_CucsComputeMemoryConfigPolicyDescr_Type = SnmpAdminString
_CucsComputeMemoryConfigPolicyDescr_Object = MibTableColumn
cucsComputeMemoryConfigPolicyDescr = _CucsComputeMemoryConfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 61, 1, 5),
    _CucsComputeMemoryConfigPolicyDescr_Type()
)
cucsComputeMemoryConfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigPolicyDescr.setStatus("current")
_CucsComputeMemoryConfigPolicyIntId_Type = SnmpAdminString
_CucsComputeMemoryConfigPolicyIntId_Object = MibTableColumn
cucsComputeMemoryConfigPolicyIntId = _CucsComputeMemoryConfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 61, 1, 6),
    _CucsComputeMemoryConfigPolicyIntId_Type()
)
cucsComputeMemoryConfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigPolicyIntId.setStatus("current")
_CucsComputeMemoryConfigPolicyName_Type = SnmpAdminString
_CucsComputeMemoryConfigPolicyName_Object = MibTableColumn
cucsComputeMemoryConfigPolicyName = _CucsComputeMemoryConfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 61, 1, 7),
    _CucsComputeMemoryConfigPolicyName_Type()
)
cucsComputeMemoryConfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigPolicyName.setStatus("current")
_CucsComputeMemoryConfigPolicyPolicyLevel_Type = Gauge32
_CucsComputeMemoryConfigPolicyPolicyLevel_Object = MibTableColumn
cucsComputeMemoryConfigPolicyPolicyLevel = _CucsComputeMemoryConfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 61, 1, 8),
    _CucsComputeMemoryConfigPolicyPolicyLevel_Type()
)
cucsComputeMemoryConfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigPolicyPolicyLevel.setStatus("current")
_CucsComputeMemoryConfigPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeMemoryConfigPolicyPolicyOwner_Object = MibTableColumn
cucsComputeMemoryConfigPolicyPolicyOwner = _CucsComputeMemoryConfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 61, 1, 9),
    _CucsComputeMemoryConfigPolicyPolicyOwner_Type()
)
cucsComputeMemoryConfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigPolicyPolicyOwner.setStatus("current")
_CucsComputeMemoryConfigurationTable_Object = MibTable
cucsComputeMemoryConfigurationTable = _CucsComputeMemoryConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 62)
)
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigurationTable.setStatus("current")
_CucsComputeMemoryConfigurationEntry_Object = MibTableRow
cucsComputeMemoryConfigurationEntry = _CucsComputeMemoryConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 62, 1)
)
cucsComputeMemoryConfigurationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeMemoryConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigurationEntry.setStatus("current")
_CucsComputeMemoryConfigurationInstanceId_Type = CucsManagedObjectId
_CucsComputeMemoryConfigurationInstanceId_Object = MibTableColumn
cucsComputeMemoryConfigurationInstanceId = _CucsComputeMemoryConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 62, 1, 1),
    _CucsComputeMemoryConfigurationInstanceId_Type()
)
cucsComputeMemoryConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigurationInstanceId.setStatus("current")
_CucsComputeMemoryConfigurationDn_Type = CucsManagedObjectDn
_CucsComputeMemoryConfigurationDn_Object = MibTableColumn
cucsComputeMemoryConfigurationDn = _CucsComputeMemoryConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 62, 1, 2),
    _CucsComputeMemoryConfigurationDn_Type()
)
cucsComputeMemoryConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigurationDn.setStatus("current")
_CucsComputeMemoryConfigurationRn_Type = SnmpAdminString
_CucsComputeMemoryConfigurationRn_Object = MibTableColumn
cucsComputeMemoryConfigurationRn = _CucsComputeMemoryConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 62, 1, 3),
    _CucsComputeMemoryConfigurationRn_Type()
)
cucsComputeMemoryConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigurationRn.setStatus("current")
_CucsComputeMemoryConfigurationAdminMemoryState_Type = CucsComputeAdminMemoryState
_CucsComputeMemoryConfigurationAdminMemoryState_Object = MibTableColumn
cucsComputeMemoryConfigurationAdminMemoryState = _CucsComputeMemoryConfigurationAdminMemoryState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 62, 1, 4),
    _CucsComputeMemoryConfigurationAdminMemoryState_Type()
)
cucsComputeMemoryConfigurationAdminMemoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigurationAdminMemoryState.setStatus("current")
_CucsComputeMemoryConfigurationBlackListing_Type = CucsComputeBlackListing
_CucsComputeMemoryConfigurationBlackListing_Object = MibTableColumn
cucsComputeMemoryConfigurationBlackListing = _CucsComputeMemoryConfigurationBlackListing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 62, 1, 5),
    _CucsComputeMemoryConfigurationBlackListing_Type()
)
cucsComputeMemoryConfigurationBlackListing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeMemoryConfigurationBlackListing.setStatus("current")
_CucsComputeBoardConnectorTable_Object = MibTable
cucsComputeBoardConnectorTable = _CucsComputeBoardConnectorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 63)
)
if mibBuilder.loadTexts:
    cucsComputeBoardConnectorTable.setStatus("current")
_CucsComputeBoardConnectorEntry_Object = MibTableRow
cucsComputeBoardConnectorEntry = _CucsComputeBoardConnectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 63, 1)
)
cucsComputeBoardConnectorEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeBoardConnectorInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeBoardConnectorEntry.setStatus("current")
_CucsComputeBoardConnectorInstanceId_Type = CucsManagedObjectId
_CucsComputeBoardConnectorInstanceId_Object = MibTableColumn
cucsComputeBoardConnectorInstanceId = _CucsComputeBoardConnectorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 63, 1, 1),
    _CucsComputeBoardConnectorInstanceId_Type()
)
cucsComputeBoardConnectorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeBoardConnectorInstanceId.setStatus("current")
_CucsComputeBoardConnectorDn_Type = CucsManagedObjectDn
_CucsComputeBoardConnectorDn_Object = MibTableColumn
cucsComputeBoardConnectorDn = _CucsComputeBoardConnectorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 63, 1, 2),
    _CucsComputeBoardConnectorDn_Type()
)
cucsComputeBoardConnectorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardConnectorDn.setStatus("current")
_CucsComputeBoardConnectorRn_Type = SnmpAdminString
_CucsComputeBoardConnectorRn_Object = MibTableColumn
cucsComputeBoardConnectorRn = _CucsComputeBoardConnectorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 63, 1, 3),
    _CucsComputeBoardConnectorRn_Type()
)
cucsComputeBoardConnectorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardConnectorRn.setStatus("current")
_CucsComputeBoardConnectorBoardConnectorType_Type = CucsEquipmentBoardConnectorType
_CucsComputeBoardConnectorBoardConnectorType_Object = MibTableColumn
cucsComputeBoardConnectorBoardConnectorType = _CucsComputeBoardConnectorBoardConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 63, 1, 4),
    _CucsComputeBoardConnectorBoardConnectorType_Type()
)
cucsComputeBoardConnectorBoardConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardConnectorBoardConnectorType.setStatus("current")
_CucsComputeBoardConnectorMasterSlotId_Type = Gauge32
_CucsComputeBoardConnectorMasterSlotId_Object = MibTableColumn
cucsComputeBoardConnectorMasterSlotId = _CucsComputeBoardConnectorMasterSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 63, 1, 5),
    _CucsComputeBoardConnectorMasterSlotId_Type()
)
cucsComputeBoardConnectorMasterSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardConnectorMasterSlotId.setStatus("current")
_CucsComputeBoardConnectorSlaveSlotId_Type = Gauge32
_CucsComputeBoardConnectorSlaveSlotId_Object = MibTableColumn
cucsComputeBoardConnectorSlaveSlotId = _CucsComputeBoardConnectorSlaveSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 63, 1, 6),
    _CucsComputeBoardConnectorSlaveSlotId_Type()
)
cucsComputeBoardConnectorSlaveSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBoardConnectorSlaveSlotId.setStatus("current")
_CucsComputeExtBoardTable_Object = MibTable
cucsComputeExtBoardTable = _CucsComputeExtBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64)
)
if mibBuilder.loadTexts:
    cucsComputeExtBoardTable.setStatus("current")
_CucsComputeExtBoardEntry_Object = MibTableRow
cucsComputeExtBoardEntry = _CucsComputeExtBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1)
)
cucsComputeExtBoardEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeExtBoardInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeExtBoardEntry.setStatus("current")
_CucsComputeExtBoardInstanceId_Type = CucsManagedObjectId
_CucsComputeExtBoardInstanceId_Object = MibTableColumn
cucsComputeExtBoardInstanceId = _CucsComputeExtBoardInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 1),
    _CucsComputeExtBoardInstanceId_Type()
)
cucsComputeExtBoardInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeExtBoardInstanceId.setStatus("current")
_CucsComputeExtBoardDn_Type = CucsManagedObjectDn
_CucsComputeExtBoardDn_Object = MibTableColumn
cucsComputeExtBoardDn = _CucsComputeExtBoardDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 2),
    _CucsComputeExtBoardDn_Type()
)
cucsComputeExtBoardDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardDn.setStatus("current")
_CucsComputeExtBoardRn_Type = SnmpAdminString
_CucsComputeExtBoardRn_Object = MibTableColumn
cucsComputeExtBoardRn = _CucsComputeExtBoardRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 3),
    _CucsComputeExtBoardRn_Type()
)
cucsComputeExtBoardRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardRn.setStatus("current")
_CucsComputeExtBoardBoardAggregationRole_Type = CucsEquipmentBoardAggregationRole
_CucsComputeExtBoardBoardAggregationRole_Object = MibTableColumn
cucsComputeExtBoardBoardAggregationRole = _CucsComputeExtBoardBoardAggregationRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 4),
    _CucsComputeExtBoardBoardAggregationRole_Type()
)
cucsComputeExtBoardBoardAggregationRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardBoardAggregationRole.setStatus("current")
_CucsComputeExtBoardChassisId_Type = Gauge32
_CucsComputeExtBoardChassisId_Object = MibTableColumn
cucsComputeExtBoardChassisId = _CucsComputeExtBoardChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 5),
    _CucsComputeExtBoardChassisId_Type()
)
cucsComputeExtBoardChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardChassisId.setStatus("current")
_CucsComputeExtBoardCmosVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeExtBoardCmosVoltage_Object = MibTableColumn
cucsComputeExtBoardCmosVoltage = _CucsComputeExtBoardCmosVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 6),
    _CucsComputeExtBoardCmosVoltage_Type()
)
cucsComputeExtBoardCmosVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardCmosVoltage.setStatus("current")
_CucsComputeExtBoardConnPath_Type = CucsEquipmentConnectionStatus
_CucsComputeExtBoardConnPath_Object = MibTableColumn
cucsComputeExtBoardConnPath = _CucsComputeExtBoardConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 7),
    _CucsComputeExtBoardConnPath_Type()
)
cucsComputeExtBoardConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardConnPath.setStatus("current")
_CucsComputeExtBoardConnStatus_Type = CucsEquipmentConnectionStatus
_CucsComputeExtBoardConnStatus_Object = MibTableColumn
cucsComputeExtBoardConnStatus = _CucsComputeExtBoardConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 8),
    _CucsComputeExtBoardConnStatus_Type()
)
cucsComputeExtBoardConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardConnStatus.setStatus("current")
_CucsComputeExtBoardFaultQualifier_Type = SnmpAdminString
_CucsComputeExtBoardFaultQualifier_Object = MibTableColumn
cucsComputeExtBoardFaultQualifier = _CucsComputeExtBoardFaultQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 9),
    _CucsComputeExtBoardFaultQualifier_Type()
)
cucsComputeExtBoardFaultQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardFaultQualifier.setStatus("current")
_CucsComputeExtBoardId_Type = Gauge32
_CucsComputeExtBoardId_Object = MibTableColumn
cucsComputeExtBoardId = _CucsComputeExtBoardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 10),
    _CucsComputeExtBoardId_Type()
)
cucsComputeExtBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardId.setStatus("current")
_CucsComputeExtBoardLocationDn_Type = SnmpAdminString
_CucsComputeExtBoardLocationDn_Object = MibTableColumn
cucsComputeExtBoardLocationDn = _CucsComputeExtBoardLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 11),
    _CucsComputeExtBoardLocationDn_Type()
)
cucsComputeExtBoardLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardLocationDn.setStatus("current")
_CucsComputeExtBoardManagingInst_Type = CucsNetworkSwitchId
_CucsComputeExtBoardManagingInst_Object = MibTableColumn
cucsComputeExtBoardManagingInst = _CucsComputeExtBoardManagingInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 12),
    _CucsComputeExtBoardManagingInst_Type()
)
cucsComputeExtBoardManagingInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardManagingInst.setStatus("current")
_CucsComputeExtBoardModel_Type = SnmpAdminString
_CucsComputeExtBoardModel_Object = MibTableColumn
cucsComputeExtBoardModel = _CucsComputeExtBoardModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 13),
    _CucsComputeExtBoardModel_Type()
)
cucsComputeExtBoardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardModel.setStatus("current")
_CucsComputeExtBoardOperPower_Type = CucsEquipmentPowerState
_CucsComputeExtBoardOperPower_Object = MibTableColumn
cucsComputeExtBoardOperPower = _CucsComputeExtBoardOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 14),
    _CucsComputeExtBoardOperPower_Type()
)
cucsComputeExtBoardOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardOperPower.setStatus("current")
_CucsComputeExtBoardOperQualifierReason_Type = SnmpAdminString
_CucsComputeExtBoardOperQualifierReason_Object = MibTableColumn
cucsComputeExtBoardOperQualifierReason = _CucsComputeExtBoardOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 15),
    _CucsComputeExtBoardOperQualifierReason_Type()
)
cucsComputeExtBoardOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardOperQualifierReason.setStatus("current")
_CucsComputeExtBoardOperState_Type = CucsEquipmentOperability
_CucsComputeExtBoardOperState_Object = MibTableColumn
cucsComputeExtBoardOperState = _CucsComputeExtBoardOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 16),
    _CucsComputeExtBoardOperState_Type()
)
cucsComputeExtBoardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardOperState.setStatus("current")
_CucsComputeExtBoardOperability_Type = CucsEquipmentOperability
_CucsComputeExtBoardOperability_Object = MibTableColumn
cucsComputeExtBoardOperability = _CucsComputeExtBoardOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 17),
    _CucsComputeExtBoardOperability_Type()
)
cucsComputeExtBoardOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardOperability.setStatus("current")
_CucsComputeExtBoardPerf_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeExtBoardPerf_Object = MibTableColumn
cucsComputeExtBoardPerf = _CucsComputeExtBoardPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 18),
    _CucsComputeExtBoardPerf_Type()
)
cucsComputeExtBoardPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardPerf.setStatus("current")
_CucsComputeExtBoardPower_Type = CucsComputeABoardPower
_CucsComputeExtBoardPower_Object = MibTableColumn
cucsComputeExtBoardPower = _CucsComputeExtBoardPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 19),
    _CucsComputeExtBoardPower_Type()
)
cucsComputeExtBoardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardPower.setStatus("current")
_CucsComputeExtBoardPowerUsage_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeExtBoardPowerUsage_Object = MibTableColumn
cucsComputeExtBoardPowerUsage = _CucsComputeExtBoardPowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 20),
    _CucsComputeExtBoardPowerUsage_Type()
)
cucsComputeExtBoardPowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardPowerUsage.setStatus("current")
_CucsComputeExtBoardPresence_Type = CucsEquipmentPresence
_CucsComputeExtBoardPresence_Object = MibTableColumn
cucsComputeExtBoardPresence = _CucsComputeExtBoardPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 21),
    _CucsComputeExtBoardPresence_Type()
)
cucsComputeExtBoardPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardPresence.setStatus("current")
_CucsComputeExtBoardRevision_Type = SnmpAdminString
_CucsComputeExtBoardRevision_Object = MibTableColumn
cucsComputeExtBoardRevision = _CucsComputeExtBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 22),
    _CucsComputeExtBoardRevision_Type()
)
cucsComputeExtBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardRevision.setStatus("current")
_CucsComputeExtBoardSerial_Type = SnmpAdminString
_CucsComputeExtBoardSerial_Object = MibTableColumn
cucsComputeExtBoardSerial = _CucsComputeExtBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 23),
    _CucsComputeExtBoardSerial_Type()
)
cucsComputeExtBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardSerial.setStatus("current")
_CucsComputeExtBoardSlotId_Type = Gauge32
_CucsComputeExtBoardSlotId_Object = MibTableColumn
cucsComputeExtBoardSlotId = _CucsComputeExtBoardSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 24),
    _CucsComputeExtBoardSlotId_Type()
)
cucsComputeExtBoardSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardSlotId.setStatus("current")
_CucsComputeExtBoardThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeExtBoardThermal_Object = MibTableColumn
cucsComputeExtBoardThermal = _CucsComputeExtBoardThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 25),
    _CucsComputeExtBoardThermal_Type()
)
cucsComputeExtBoardThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardThermal.setStatus("current")
_CucsComputeExtBoardVendor_Type = SnmpAdminString
_CucsComputeExtBoardVendor_Object = MibTableColumn
cucsComputeExtBoardVendor = _CucsComputeExtBoardVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 26),
    _CucsComputeExtBoardVendor_Type()
)
cucsComputeExtBoardVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardVendor.setStatus("current")
_CucsComputeExtBoardVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeExtBoardVoltage_Object = MibTableColumn
cucsComputeExtBoardVoltage = _CucsComputeExtBoardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 27),
    _CucsComputeExtBoardVoltage_Type()
)
cucsComputeExtBoardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardVoltage.setStatus("current")
_CucsComputeExtBoardDiscoveryStatus_Type = CucsEquipmentConnectionStatus
_CucsComputeExtBoardDiscoveryStatus_Object = MibTableColumn
cucsComputeExtBoardDiscoveryStatus = _CucsComputeExtBoardDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 64, 1, 28),
    _CucsComputeExtBoardDiscoveryStatus_Type()
)
cucsComputeExtBoardDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeExtBoardDiscoveryStatus.setStatus("current")
_CucsComputeKvmMgmtPolicyTable_Object = MibTable
cucsComputeKvmMgmtPolicyTable = _CucsComputeKvmMgmtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 65)
)
if mibBuilder.loadTexts:
    cucsComputeKvmMgmtPolicyTable.setStatus("current")
_CucsComputeKvmMgmtPolicyEntry_Object = MibTableRow
cucsComputeKvmMgmtPolicyEntry = _CucsComputeKvmMgmtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 65, 1)
)
cucsComputeKvmMgmtPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeKvmMgmtPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeKvmMgmtPolicyEntry.setStatus("current")
_CucsComputeKvmMgmtPolicyInstanceId_Type = CucsManagedObjectId
_CucsComputeKvmMgmtPolicyInstanceId_Object = MibTableColumn
cucsComputeKvmMgmtPolicyInstanceId = _CucsComputeKvmMgmtPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 65, 1, 1),
    _CucsComputeKvmMgmtPolicyInstanceId_Type()
)
cucsComputeKvmMgmtPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeKvmMgmtPolicyInstanceId.setStatus("current")
_CucsComputeKvmMgmtPolicyDn_Type = CucsManagedObjectDn
_CucsComputeKvmMgmtPolicyDn_Object = MibTableColumn
cucsComputeKvmMgmtPolicyDn = _CucsComputeKvmMgmtPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 65, 1, 2),
    _CucsComputeKvmMgmtPolicyDn_Type()
)
cucsComputeKvmMgmtPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeKvmMgmtPolicyDn.setStatus("current")
_CucsComputeKvmMgmtPolicyRn_Type = SnmpAdminString
_CucsComputeKvmMgmtPolicyRn_Object = MibTableColumn
cucsComputeKvmMgmtPolicyRn = _CucsComputeKvmMgmtPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 65, 1, 3),
    _CucsComputeKvmMgmtPolicyRn_Type()
)
cucsComputeKvmMgmtPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeKvmMgmtPolicyRn.setStatus("current")
_CucsComputeKvmMgmtPolicyDescr_Type = SnmpAdminString
_CucsComputeKvmMgmtPolicyDescr_Object = MibTableColumn
cucsComputeKvmMgmtPolicyDescr = _CucsComputeKvmMgmtPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 65, 1, 4),
    _CucsComputeKvmMgmtPolicyDescr_Type()
)
cucsComputeKvmMgmtPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeKvmMgmtPolicyDescr.setStatus("current")
_CucsComputeKvmMgmtPolicyIntId_Type = SnmpAdminString
_CucsComputeKvmMgmtPolicyIntId_Object = MibTableColumn
cucsComputeKvmMgmtPolicyIntId = _CucsComputeKvmMgmtPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 65, 1, 5),
    _CucsComputeKvmMgmtPolicyIntId_Type()
)
cucsComputeKvmMgmtPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeKvmMgmtPolicyIntId.setStatus("current")
_CucsComputeKvmMgmtPolicyName_Type = SnmpAdminString
_CucsComputeKvmMgmtPolicyName_Object = MibTableColumn
cucsComputeKvmMgmtPolicyName = _CucsComputeKvmMgmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 65, 1, 6),
    _CucsComputeKvmMgmtPolicyName_Type()
)
cucsComputeKvmMgmtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeKvmMgmtPolicyName.setStatus("current")
_CucsComputeKvmMgmtPolicyPolicyLevel_Type = Gauge32
_CucsComputeKvmMgmtPolicyPolicyLevel_Object = MibTableColumn
cucsComputeKvmMgmtPolicyPolicyLevel = _CucsComputeKvmMgmtPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 65, 1, 7),
    _CucsComputeKvmMgmtPolicyPolicyLevel_Type()
)
cucsComputeKvmMgmtPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeKvmMgmtPolicyPolicyLevel.setStatus("current")
_CucsComputeKvmMgmtPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeKvmMgmtPolicyPolicyOwner_Object = MibTableColumn
cucsComputeKvmMgmtPolicyPolicyOwner = _CucsComputeKvmMgmtPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 65, 1, 8),
    _CucsComputeKvmMgmtPolicyPolicyOwner_Type()
)
cucsComputeKvmMgmtPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeKvmMgmtPolicyPolicyOwner.setStatus("current")
_CucsComputeKvmMgmtPolicyVmediaEncryption_Type = CucsComputeKvmMgmtPolicyVmediaEncryption
_CucsComputeKvmMgmtPolicyVmediaEncryption_Object = MibTableColumn
cucsComputeKvmMgmtPolicyVmediaEncryption = _CucsComputeKvmMgmtPolicyVmediaEncryption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 65, 1, 9),
    _CucsComputeKvmMgmtPolicyVmediaEncryption_Type()
)
cucsComputeKvmMgmtPolicyVmediaEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeKvmMgmtPolicyVmediaEncryption.setStatus("current")
_CucsComputeBladeEpTable_Object = MibTable
cucsComputeBladeEpTable = _CucsComputeBladeEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66)
)
if mibBuilder.loadTexts:
    cucsComputeBladeEpTable.setStatus("current")
_CucsComputeBladeEpEntry_Object = MibTableRow
cucsComputeBladeEpEntry = _CucsComputeBladeEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1)
)
cucsComputeBladeEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeBladeEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeBladeEpEntry.setStatus("current")
_CucsComputeBladeEpInstanceId_Type = CucsManagedObjectId
_CucsComputeBladeEpInstanceId_Object = MibTableColumn
cucsComputeBladeEpInstanceId = _CucsComputeBladeEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1, 1),
    _CucsComputeBladeEpInstanceId_Type()
)
cucsComputeBladeEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeBladeEpInstanceId.setStatus("current")
_CucsComputeBladeEpDn_Type = CucsManagedObjectDn
_CucsComputeBladeEpDn_Object = MibTableColumn
cucsComputeBladeEpDn = _CucsComputeBladeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1, 2),
    _CucsComputeBladeEpDn_Type()
)
cucsComputeBladeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeEpDn.setStatus("current")
_CucsComputeBladeEpRn_Type = SnmpAdminString
_CucsComputeBladeEpRn_Object = MibTableColumn
cucsComputeBladeEpRn = _CucsComputeBladeEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1, 3),
    _CucsComputeBladeEpRn_Type()
)
cucsComputeBladeEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeEpRn.setStatus("current")
_CucsComputeBladeEpAdminState_Type = CucsComputeAdminState
_CucsComputeBladeEpAdminState_Object = MibTableColumn
cucsComputeBladeEpAdminState = _CucsComputeBladeEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1, 4),
    _CucsComputeBladeEpAdminState_Type()
)
cucsComputeBladeEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeEpAdminState.setStatus("current")
_CucsComputeBladeEpChassisId_Type = Gauge32
_CucsComputeBladeEpChassisId_Object = MibTableColumn
cucsComputeBladeEpChassisId = _CucsComputeBladeEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1, 5),
    _CucsComputeBladeEpChassisId_Type()
)
cucsComputeBladeEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeEpChassisId.setStatus("current")
_CucsComputeBladeEpEpDn_Type = SnmpAdminString
_CucsComputeBladeEpEpDn_Object = MibTableColumn
cucsComputeBladeEpEpDn = _CucsComputeBladeEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1, 6),
    _CucsComputeBladeEpEpDn_Type()
)
cucsComputeBladeEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeEpEpDn.setStatus("current")
_CucsComputeBladeEpId_Type = CucsComputeBladeEpId
_CucsComputeBladeEpId_Object = MibTableColumn
cucsComputeBladeEpId = _CucsComputeBladeEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1, 7),
    _CucsComputeBladeEpId_Type()
)
cucsComputeBladeEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeEpId.setStatus("current")
_CucsComputeBladeEpOperQualifierReason_Type = SnmpAdminString
_CucsComputeBladeEpOperQualifierReason_Object = MibTableColumn
cucsComputeBladeEpOperQualifierReason = _CucsComputeBladeEpOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1, 8),
    _CucsComputeBladeEpOperQualifierReason_Type()
)
cucsComputeBladeEpOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeEpOperQualifierReason.setStatus("current")
_CucsComputeBladeEpOperState_Type = CucsLsOperState
_CucsComputeBladeEpOperState_Object = MibTableColumn
cucsComputeBladeEpOperState = _CucsComputeBladeEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1, 9),
    _CucsComputeBladeEpOperState_Type()
)
cucsComputeBladeEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeEpOperState.setStatus("current")
_CucsComputeBladeEpPeerPresence_Type = CucsEquipmentSlotStatus
_CucsComputeBladeEpPeerPresence_Object = MibTableColumn
cucsComputeBladeEpPeerPresence = _CucsComputeBladeEpPeerPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1, 10),
    _CucsComputeBladeEpPeerPresence_Type()
)
cucsComputeBladeEpPeerPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeEpPeerPresence.setStatus("current")
_CucsComputeBladeEpPresence_Type = CucsEquipmentSlotStatus
_CucsComputeBladeEpPresence_Object = MibTableColumn
cucsComputeBladeEpPresence = _CucsComputeBladeEpPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1, 11),
    _CucsComputeBladeEpPresence_Type()
)
cucsComputeBladeEpPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeEpPresence.setStatus("current")
_CucsComputeBladeEpSlotId_Type = CucsComputeBladeEpSlotId
_CucsComputeBladeEpSlotId_Object = MibTableColumn
cucsComputeBladeEpSlotId = _CucsComputeBladeEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 66, 1, 12),
    _CucsComputeBladeEpSlotId_Type()
)
cucsComputeBladeEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeBladeEpSlotId.setStatus("current")
_CucsComputeConstraintDefTable_Object = MibTable
cucsComputeConstraintDefTable = _CucsComputeConstraintDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67)
)
if mibBuilder.loadTexts:
    cucsComputeConstraintDefTable.setStatus("current")
_CucsComputeConstraintDefEntry_Object = MibTableRow
cucsComputeConstraintDefEntry = _CucsComputeConstraintDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1)
)
cucsComputeConstraintDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeConstraintDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeConstraintDefEntry.setStatus("current")
_CucsComputeConstraintDefInstanceId_Type = CucsManagedObjectId
_CucsComputeConstraintDefInstanceId_Object = MibTableColumn
cucsComputeConstraintDefInstanceId = _CucsComputeConstraintDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1, 1),
    _CucsComputeConstraintDefInstanceId_Type()
)
cucsComputeConstraintDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeConstraintDefInstanceId.setStatus("current")
_CucsComputeConstraintDefDn_Type = CucsManagedObjectDn
_CucsComputeConstraintDefDn_Object = MibTableColumn
cucsComputeConstraintDefDn = _CucsComputeConstraintDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1, 2),
    _CucsComputeConstraintDefDn_Type()
)
cucsComputeConstraintDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeConstraintDefDn.setStatus("current")
_CucsComputeConstraintDefRn_Type = SnmpAdminString
_CucsComputeConstraintDefRn_Object = MibTableColumn
cucsComputeConstraintDefRn = _CucsComputeConstraintDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1, 3),
    _CucsComputeConstraintDefRn_Type()
)
cucsComputeConstraintDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeConstraintDefRn.setStatus("current")
_CucsComputeConstraintDefConstraintType_Type = CucsComputeEquipmentConstraintType
_CucsComputeConstraintDefConstraintType_Object = MibTableColumn
cucsComputeConstraintDefConstraintType = _CucsComputeConstraintDefConstraintType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1, 4),
    _CucsComputeConstraintDefConstraintType_Type()
)
cucsComputeConstraintDefConstraintType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeConstraintDefConstraintType.setStatus("current")
_CucsComputeConstraintDefDescr_Type = SnmpAdminString
_CucsComputeConstraintDefDescr_Object = MibTableColumn
cucsComputeConstraintDefDescr = _CucsComputeConstraintDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1, 5),
    _CucsComputeConstraintDefDescr_Type()
)
cucsComputeConstraintDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeConstraintDefDescr.setStatus("current")
_CucsComputeConstraintDefHwModel_Type = SnmpAdminString
_CucsComputeConstraintDefHwModel_Object = MibTableColumn
cucsComputeConstraintDefHwModel = _CucsComputeConstraintDefHwModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1, 6),
    _CucsComputeConstraintDefHwModel_Type()
)
cucsComputeConstraintDefHwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeConstraintDefHwModel.setStatus("current")
_CucsComputeConstraintDefHwRevision_Type = SnmpAdminString
_CucsComputeConstraintDefHwRevision_Object = MibTableColumn
cucsComputeConstraintDefHwRevision = _CucsComputeConstraintDefHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1, 7),
    _CucsComputeConstraintDefHwRevision_Type()
)
cucsComputeConstraintDefHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeConstraintDefHwRevision.setStatus("current")
_CucsComputeConstraintDefHwVendor_Type = SnmpAdminString
_CucsComputeConstraintDefHwVendor_Object = MibTableColumn
cucsComputeConstraintDefHwVendor = _CucsComputeConstraintDefHwVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1, 8),
    _CucsComputeConstraintDefHwVendor_Type()
)
cucsComputeConstraintDefHwVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeConstraintDefHwVendor.setStatus("current")
_CucsComputeConstraintDefIntId_Type = SnmpAdminString
_CucsComputeConstraintDefIntId_Object = MibTableColumn
cucsComputeConstraintDefIntId = _CucsComputeConstraintDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1, 9),
    _CucsComputeConstraintDefIntId_Type()
)
cucsComputeConstraintDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeConstraintDefIntId.setStatus("current")
_CucsComputeConstraintDefName_Type = SnmpAdminString
_CucsComputeConstraintDefName_Object = MibTableColumn
cucsComputeConstraintDefName = _CucsComputeConstraintDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1, 10),
    _CucsComputeConstraintDefName_Type()
)
cucsComputeConstraintDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeConstraintDefName.setStatus("current")
_CucsComputeConstraintDefPolicyLevel_Type = Gauge32
_CucsComputeConstraintDefPolicyLevel_Object = MibTableColumn
cucsComputeConstraintDefPolicyLevel = _CucsComputeConstraintDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1, 11),
    _CucsComputeConstraintDefPolicyLevel_Type()
)
cucsComputeConstraintDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeConstraintDefPolicyLevel.setStatus("current")
_CucsComputeConstraintDefPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeConstraintDefPolicyOwner_Object = MibTableColumn
cucsComputeConstraintDefPolicyOwner = _CucsComputeConstraintDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 67, 1, 12),
    _CucsComputeConstraintDefPolicyOwner_Type()
)
cucsComputeConstraintDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeConstraintDefPolicyOwner.setStatus("current")
_CucsComputeServerTypeCapTable_Object = MibTable
cucsComputeServerTypeCapTable = _CucsComputeServerTypeCapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 68)
)
if mibBuilder.loadTexts:
    cucsComputeServerTypeCapTable.setStatus("current")
_CucsComputeServerTypeCapEntry_Object = MibTableRow
cucsComputeServerTypeCapEntry = _CucsComputeServerTypeCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 68, 1)
)
cucsComputeServerTypeCapEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeServerTypeCapInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeServerTypeCapEntry.setStatus("current")
_CucsComputeServerTypeCapInstanceId_Type = CucsManagedObjectId
_CucsComputeServerTypeCapInstanceId_Object = MibTableColumn
cucsComputeServerTypeCapInstanceId = _CucsComputeServerTypeCapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 68, 1, 1),
    _CucsComputeServerTypeCapInstanceId_Type()
)
cucsComputeServerTypeCapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeServerTypeCapInstanceId.setStatus("current")
_CucsComputeServerTypeCapDn_Type = CucsManagedObjectDn
_CucsComputeServerTypeCapDn_Object = MibTableColumn
cucsComputeServerTypeCapDn = _CucsComputeServerTypeCapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 68, 1, 2),
    _CucsComputeServerTypeCapDn_Type()
)
cucsComputeServerTypeCapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerTypeCapDn.setStatus("current")
_CucsComputeServerTypeCapRn_Type = SnmpAdminString
_CucsComputeServerTypeCapRn_Object = MibTableColumn
cucsComputeServerTypeCapRn = _CucsComputeServerTypeCapRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 68, 1, 3),
    _CucsComputeServerTypeCapRn_Type()
)
cucsComputeServerTypeCapRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerTypeCapRn.setStatus("current")
_CucsComputeServerTypeCapType_Type = CucsComputeServerTypeCapType
_CucsComputeServerTypeCapType_Object = MibTableColumn
cucsComputeServerTypeCapType = _CucsComputeServerTypeCapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 68, 1, 4),
    _CucsComputeServerTypeCapType_Type()
)
cucsComputeServerTypeCapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerTypeCapType.setStatus("current")
_CucsComputeCartridgeTable_Object = MibTable
cucsComputeCartridgeTable = _CucsComputeCartridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71)
)
if mibBuilder.loadTexts:
    cucsComputeCartridgeTable.setStatus("current")
_CucsComputeCartridgeEntry_Object = MibTableRow
cucsComputeCartridgeEntry = _CucsComputeCartridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1)
)
cucsComputeCartridgeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeCartridgeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeCartridgeEntry.setStatus("current")
_CucsComputeCartridgeInstanceId_Type = CucsManagedObjectId
_CucsComputeCartridgeInstanceId_Object = MibTableColumn
cucsComputeCartridgeInstanceId = _CucsComputeCartridgeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 1),
    _CucsComputeCartridgeInstanceId_Type()
)
cucsComputeCartridgeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeCartridgeInstanceId.setStatus("current")
_CucsComputeCartridgeDn_Type = CucsManagedObjectDn
_CucsComputeCartridgeDn_Object = MibTableColumn
cucsComputeCartridgeDn = _CucsComputeCartridgeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 2),
    _CucsComputeCartridgeDn_Type()
)
cucsComputeCartridgeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeDn.setStatus("current")
_CucsComputeCartridgeRn_Type = SnmpAdminString
_CucsComputeCartridgeRn_Object = MibTableColumn
cucsComputeCartridgeRn = _CucsComputeCartridgeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 3),
    _CucsComputeCartridgeRn_Type()
)
cucsComputeCartridgeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeRn.setStatus("current")
_CucsComputeCartridgeChassisId_Type = Gauge32
_CucsComputeCartridgeChassisId_Object = MibTableColumn
cucsComputeCartridgeChassisId = _CucsComputeCartridgeChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 4),
    _CucsComputeCartridgeChassisId_Type()
)
cucsComputeCartridgeChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeChassisId.setStatus("current")
_CucsComputeCartridgeDiscovery_Type = CucsComputeCartridgeDiscovery
_CucsComputeCartridgeDiscovery_Object = MibTableColumn
cucsComputeCartridgeDiscovery = _CucsComputeCartridgeDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 5),
    _CucsComputeCartridgeDiscovery_Type()
)
cucsComputeCartridgeDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeDiscovery.setStatus("current")
_CucsComputeCartridgeFltAggr_Type = Unsigned64
_CucsComputeCartridgeFltAggr_Object = MibTableColumn
cucsComputeCartridgeFltAggr = _CucsComputeCartridgeFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 6),
    _CucsComputeCartridgeFltAggr_Type()
)
cucsComputeCartridgeFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeFltAggr.setStatus("current")
_CucsComputeCartridgeId_Type = Gauge32
_CucsComputeCartridgeId_Object = MibTableColumn
cucsComputeCartridgeId = _CucsComputeCartridgeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 7),
    _CucsComputeCartridgeId_Type()
)
cucsComputeCartridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeId.setStatus("current")
_CucsComputeCartridgeLc_Type = CucsComputeAdminTrigger
_CucsComputeCartridgeLc_Object = MibTableColumn
cucsComputeCartridgeLc = _CucsComputeCartridgeLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 8),
    _CucsComputeCartridgeLc_Type()
)
cucsComputeCartridgeLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeLc.setStatus("current")
_CucsComputeCartridgeLcTs_Type = DateAndTime
_CucsComputeCartridgeLcTs_Object = MibTableColumn
cucsComputeCartridgeLcTs = _CucsComputeCartridgeLcTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 9),
    _CucsComputeCartridgeLcTs_Type()
)
cucsComputeCartridgeLcTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeLcTs.setStatus("current")
_CucsComputeCartridgeModel_Type = SnmpAdminString
_CucsComputeCartridgeModel_Object = MibTableColumn
cucsComputeCartridgeModel = _CucsComputeCartridgeModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 10),
    _CucsComputeCartridgeModel_Type()
)
cucsComputeCartridgeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeModel.setStatus("current")
_CucsComputeCartridgeOperQualifierReason_Type = SnmpAdminString
_CucsComputeCartridgeOperQualifierReason_Object = MibTableColumn
cucsComputeCartridgeOperQualifierReason = _CucsComputeCartridgeOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 11),
    _CucsComputeCartridgeOperQualifierReason_Type()
)
cucsComputeCartridgeOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeOperQualifierReason.setStatus("current")
_CucsComputeCartridgeOperState_Type = CucsEquipmentOperability
_CucsComputeCartridgeOperState_Object = MibTableColumn
cucsComputeCartridgeOperState = _CucsComputeCartridgeOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 12),
    _CucsComputeCartridgeOperState_Type()
)
cucsComputeCartridgeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeOperState.setStatus("current")
_CucsComputeCartridgeOperability_Type = CucsEquipmentOperability
_CucsComputeCartridgeOperability_Object = MibTableColumn
cucsComputeCartridgeOperability = _CucsComputeCartridgeOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 13),
    _CucsComputeCartridgeOperability_Type()
)
cucsComputeCartridgeOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeOperability.setStatus("current")
_CucsComputeCartridgePerf_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeCartridgePerf_Object = MibTableColumn
cucsComputeCartridgePerf = _CucsComputeCartridgePerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 14),
    _CucsComputeCartridgePerf_Type()
)
cucsComputeCartridgePerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgePerf.setStatus("current")
_CucsComputeCartridgePower_Type = CucsEquipmentPowerState
_CucsComputeCartridgePower_Object = MibTableColumn
cucsComputeCartridgePower = _CucsComputeCartridgePower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 15),
    _CucsComputeCartridgePower_Type()
)
cucsComputeCartridgePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgePower.setStatus("current")
_CucsComputeCartridgePresence_Type = CucsEquipmentPresence
_CucsComputeCartridgePresence_Object = MibTableColumn
cucsComputeCartridgePresence = _CucsComputeCartridgePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 16),
    _CucsComputeCartridgePresence_Type()
)
cucsComputeCartridgePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgePresence.setStatus("current")
_CucsComputeCartridgeRevision_Type = SnmpAdminString
_CucsComputeCartridgeRevision_Object = MibTableColumn
cucsComputeCartridgeRevision = _CucsComputeCartridgeRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 17),
    _CucsComputeCartridgeRevision_Type()
)
cucsComputeCartridgeRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeRevision.setStatus("current")
_CucsComputeCartridgeSerial_Type = SnmpAdminString
_CucsComputeCartridgeSerial_Object = MibTableColumn
cucsComputeCartridgeSerial = _CucsComputeCartridgeSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 18),
    _CucsComputeCartridgeSerial_Type()
)
cucsComputeCartridgeSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeSerial.setStatus("current")
_CucsComputeCartridgeSlotId_Type = CucsComputeCartridgeSlotId
_CucsComputeCartridgeSlotId_Object = MibTableColumn
cucsComputeCartridgeSlotId = _CucsComputeCartridgeSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 19),
    _CucsComputeCartridgeSlotId_Type()
)
cucsComputeCartridgeSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeSlotId.setStatus("current")
_CucsComputeCartridgeThermal_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeCartridgeThermal_Object = MibTableColumn
cucsComputeCartridgeThermal = _CucsComputeCartridgeThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 20),
    _CucsComputeCartridgeThermal_Type()
)
cucsComputeCartridgeThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeThermal.setStatus("current")
_CucsComputeCartridgeVendor_Type = SnmpAdminString
_CucsComputeCartridgeVendor_Object = MibTableColumn
cucsComputeCartridgeVendor = _CucsComputeCartridgeVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 21),
    _CucsComputeCartridgeVendor_Type()
)
cucsComputeCartridgeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeVendor.setStatus("current")
_CucsComputeCartridgeVoltage_Type = CucsEquipmentSensorThresholdStatus
_CucsComputeCartridgeVoltage_Object = MibTableColumn
cucsComputeCartridgeVoltage = _CucsComputeCartridgeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 71, 1, 22),
    _CucsComputeCartridgeVoltage_Type()
)
cucsComputeCartridgeVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeCartridgeVoltage.setStatus("current")
_CucsComputeInstanceIdQualTable_Object = MibTable
cucsComputeInstanceIdQualTable = _CucsComputeInstanceIdQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 72)
)
if mibBuilder.loadTexts:
    cucsComputeInstanceIdQualTable.setStatus("current")
_CucsComputeInstanceIdQualEntry_Object = MibTableRow
cucsComputeInstanceIdQualEntry = _CucsComputeInstanceIdQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 72, 1)
)
cucsComputeInstanceIdQualEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeInstanceIdQualInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeInstanceIdQualEntry.setStatus("current")
_CucsComputeInstanceIdQualInstanceId_Type = CucsManagedObjectId
_CucsComputeInstanceIdQualInstanceId_Object = MibTableColumn
cucsComputeInstanceIdQualInstanceId = _CucsComputeInstanceIdQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 72, 1, 1),
    _CucsComputeInstanceIdQualInstanceId_Type()
)
cucsComputeInstanceIdQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeInstanceIdQualInstanceId.setStatus("current")
_CucsComputeInstanceIdQualDn_Type = CucsManagedObjectDn
_CucsComputeInstanceIdQualDn_Object = MibTableColumn
cucsComputeInstanceIdQualDn = _CucsComputeInstanceIdQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 72, 1, 2),
    _CucsComputeInstanceIdQualDn_Type()
)
cucsComputeInstanceIdQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeInstanceIdQualDn.setStatus("current")
_CucsComputeInstanceIdQualRn_Type = SnmpAdminString
_CucsComputeInstanceIdQualRn_Object = MibTableColumn
cucsComputeInstanceIdQualRn = _CucsComputeInstanceIdQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 72, 1, 3),
    _CucsComputeInstanceIdQualRn_Type()
)
cucsComputeInstanceIdQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeInstanceIdQualRn.setStatus("current")
_CucsComputeInstanceIdQualMaxId_Type = CucsComputeInstanceIdQualMaxId
_CucsComputeInstanceIdQualMaxId_Object = MibTableColumn
cucsComputeInstanceIdQualMaxId = _CucsComputeInstanceIdQualMaxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 72, 1, 4),
    _CucsComputeInstanceIdQualMaxId_Type()
)
cucsComputeInstanceIdQualMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeInstanceIdQualMaxId.setStatus("current")
_CucsComputeInstanceIdQualMinId_Type = CucsComputeInstanceIdQualMinId
_CucsComputeInstanceIdQualMinId_Object = MibTableColumn
cucsComputeInstanceIdQualMinId = _CucsComputeInstanceIdQualMinId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 72, 1, 5),
    _CucsComputeInstanceIdQualMinId_Type()
)
cucsComputeInstanceIdQualMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeInstanceIdQualMinId.setStatus("current")
_CucsComputePooledEnclosureComputeSlotTable_Object = MibTable
cucsComputePooledEnclosureComputeSlotTable = _CucsComputePooledEnclosureComputeSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73)
)
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotTable.setStatus("current")
_CucsComputePooledEnclosureComputeSlotEntry_Object = MibTableRow
cucsComputePooledEnclosureComputeSlotEntry = _CucsComputePooledEnclosureComputeSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73, 1)
)
cucsComputePooledEnclosureComputeSlotEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputePooledEnclosureComputeSlotInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotEntry.setStatus("current")
_CucsComputePooledEnclosureComputeSlotInstanceId_Type = CucsManagedObjectId
_CucsComputePooledEnclosureComputeSlotInstanceId_Object = MibTableColumn
cucsComputePooledEnclosureComputeSlotInstanceId = _CucsComputePooledEnclosureComputeSlotInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73, 1, 1),
    _CucsComputePooledEnclosureComputeSlotInstanceId_Type()
)
cucsComputePooledEnclosureComputeSlotInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotInstanceId.setStatus("current")
_CucsComputePooledEnclosureComputeSlotDn_Type = CucsManagedObjectDn
_CucsComputePooledEnclosureComputeSlotDn_Object = MibTableColumn
cucsComputePooledEnclosureComputeSlotDn = _CucsComputePooledEnclosureComputeSlotDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73, 1, 2),
    _CucsComputePooledEnclosureComputeSlotDn_Type()
)
cucsComputePooledEnclosureComputeSlotDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotDn.setStatus("current")
_CucsComputePooledEnclosureComputeSlotRn_Type = SnmpAdminString
_CucsComputePooledEnclosureComputeSlotRn_Object = MibTableColumn
cucsComputePooledEnclosureComputeSlotRn = _CucsComputePooledEnclosureComputeSlotRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73, 1, 3),
    _CucsComputePooledEnclosureComputeSlotRn_Type()
)
cucsComputePooledEnclosureComputeSlotRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotRn.setStatus("current")
_CucsComputePooledEnclosureComputeSlotAssigned_Type = TruthValue
_CucsComputePooledEnclosureComputeSlotAssigned_Object = MibTableColumn
cucsComputePooledEnclosureComputeSlotAssigned = _CucsComputePooledEnclosureComputeSlotAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73, 1, 4),
    _CucsComputePooledEnclosureComputeSlotAssigned_Type()
)
cucsComputePooledEnclosureComputeSlotAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotAssigned.setStatus("current")
_CucsComputePooledEnclosureComputeSlotAssignedToDn_Type = SnmpAdminString
_CucsComputePooledEnclosureComputeSlotAssignedToDn_Object = MibTableColumn
cucsComputePooledEnclosureComputeSlotAssignedToDn = _CucsComputePooledEnclosureComputeSlotAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73, 1, 5),
    _CucsComputePooledEnclosureComputeSlotAssignedToDn_Type()
)
cucsComputePooledEnclosureComputeSlotAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotAssignedToDn.setStatus("current")
_CucsComputePooledEnclosureComputeSlotChassisId_Type = Gauge32
_CucsComputePooledEnclosureComputeSlotChassisId_Object = MibTableColumn
cucsComputePooledEnclosureComputeSlotChassisId = _CucsComputePooledEnclosureComputeSlotChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73, 1, 6),
    _CucsComputePooledEnclosureComputeSlotChassisId_Type()
)
cucsComputePooledEnclosureComputeSlotChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotChassisId.setStatus("current")
_CucsComputePooledEnclosureComputeSlotOwner_Type = CucsComputeOwner
_CucsComputePooledEnclosureComputeSlotOwner_Object = MibTableColumn
cucsComputePooledEnclosureComputeSlotOwner = _CucsComputePooledEnclosureComputeSlotOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73, 1, 7),
    _CucsComputePooledEnclosureComputeSlotOwner_Type()
)
cucsComputePooledEnclosureComputeSlotOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotOwner.setStatus("current")
_CucsComputePooledEnclosureComputeSlotPoolableDn_Type = SnmpAdminString
_CucsComputePooledEnclosureComputeSlotPoolableDn_Object = MibTableColumn
cucsComputePooledEnclosureComputeSlotPoolableDn = _CucsComputePooledEnclosureComputeSlotPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73, 1, 8),
    _CucsComputePooledEnclosureComputeSlotPoolableDn_Type()
)
cucsComputePooledEnclosureComputeSlotPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotPoolableDn.setStatus("current")
_CucsComputePooledEnclosureComputeSlotPrevAssignedToDn_Type = SnmpAdminString
_CucsComputePooledEnclosureComputeSlotPrevAssignedToDn_Object = MibTableColumn
cucsComputePooledEnclosureComputeSlotPrevAssignedToDn = _CucsComputePooledEnclosureComputeSlotPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73, 1, 9),
    _CucsComputePooledEnclosureComputeSlotPrevAssignedToDn_Type()
)
cucsComputePooledEnclosureComputeSlotPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotPrevAssignedToDn.setStatus("current")
_CucsComputePooledEnclosureComputeSlotServerInstanceId_Type = CucsComputePooledEnclosureComputeSlotServerInstanceId
_CucsComputePooledEnclosureComputeSlotServerInstanceId_Object = MibTableColumn
cucsComputePooledEnclosureComputeSlotServerInstanceId = _CucsComputePooledEnclosureComputeSlotServerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73, 1, 10),
    _CucsComputePooledEnclosureComputeSlotServerInstanceId_Type()
)
cucsComputePooledEnclosureComputeSlotServerInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotServerInstanceId.setStatus("current")
_CucsComputePooledEnclosureComputeSlotSlotId_Type = CucsComputePooledEnclosureComputeSlotSlotId
_CucsComputePooledEnclosureComputeSlotSlotId_Object = MibTableColumn
cucsComputePooledEnclosureComputeSlotSlotId = _CucsComputePooledEnclosureComputeSlotSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 73, 1, 11),
    _CucsComputePooledEnclosureComputeSlotSlotId_Type()
)
cucsComputePooledEnclosureComputeSlotSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputePooledEnclosureComputeSlotSlotId.setStatus("current")
_CucsComputeServerUnitTable_Object = MibTable
cucsComputeServerUnitTable = _CucsComputeServerUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74)
)
if mibBuilder.loadTexts:
    cucsComputeServerUnitTable.setStatus("current")
_CucsComputeServerUnitEntry_Object = MibTableRow
cucsComputeServerUnitEntry = _CucsComputeServerUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1)
)
cucsComputeServerUnitEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeServerUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeServerUnitEntry.setStatus("current")
_CucsComputeServerUnitInstanceId_Type = CucsManagedObjectId
_CucsComputeServerUnitInstanceId_Object = MibTableColumn
cucsComputeServerUnitInstanceId = _CucsComputeServerUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 1),
    _CucsComputeServerUnitInstanceId_Type()
)
cucsComputeServerUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeServerUnitInstanceId.setStatus("current")
_CucsComputeServerUnitDn_Type = CucsManagedObjectDn
_CucsComputeServerUnitDn_Object = MibTableColumn
cucsComputeServerUnitDn = _CucsComputeServerUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 2),
    _CucsComputeServerUnitDn_Type()
)
cucsComputeServerUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitDn.setStatus("current")
_CucsComputeServerUnitRn_Type = SnmpAdminString
_CucsComputeServerUnitRn_Object = MibTableColumn
cucsComputeServerUnitRn = _CucsComputeServerUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 3),
    _CucsComputeServerUnitRn_Type()
)
cucsComputeServerUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitRn.setStatus("current")
_CucsComputeServerUnitAdminPower_Type = CucsComputeAdminPowerState
_CucsComputeServerUnitAdminPower_Object = MibTableColumn
cucsComputeServerUnitAdminPower = _CucsComputeServerUnitAdminPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 4),
    _CucsComputeServerUnitAdminPower_Type()
)
cucsComputeServerUnitAdminPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitAdminPower.setStatus("current")
_CucsComputeServerUnitAdminState_Type = CucsComputeAdminState
_CucsComputeServerUnitAdminState_Object = MibTableColumn
cucsComputeServerUnitAdminState = _CucsComputeServerUnitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 5),
    _CucsComputeServerUnitAdminState_Type()
)
cucsComputeServerUnitAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitAdminState.setStatus("current")
_CucsComputeServerUnitAssignedToDn_Type = SnmpAdminString
_CucsComputeServerUnitAssignedToDn_Object = MibTableColumn
cucsComputeServerUnitAssignedToDn = _CucsComputeServerUnitAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 6),
    _CucsComputeServerUnitAssignedToDn_Type()
)
cucsComputeServerUnitAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitAssignedToDn.setStatus("current")
_CucsComputeServerUnitAssociation_Type = CucsComputeAssociation
_CucsComputeServerUnitAssociation_Object = MibTableColumn
cucsComputeServerUnitAssociation = _CucsComputeServerUnitAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 7),
    _CucsComputeServerUnitAssociation_Type()
)
cucsComputeServerUnitAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitAssociation.setStatus("current")
_CucsComputeServerUnitAvailability_Type = CucsComputeAvailability
_CucsComputeServerUnitAvailability_Object = MibTableColumn
cucsComputeServerUnitAvailability = _CucsComputeServerUnitAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 8),
    _CucsComputeServerUnitAvailability_Type()
)
cucsComputeServerUnitAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitAvailability.setStatus("current")
_CucsComputeServerUnitAvailableMemory_Type = Gauge32
_CucsComputeServerUnitAvailableMemory_Object = MibTableColumn
cucsComputeServerUnitAvailableMemory = _CucsComputeServerUnitAvailableMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 9),
    _CucsComputeServerUnitAvailableMemory_Type()
)
cucsComputeServerUnitAvailableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitAvailableMemory.setStatus("current")
_CucsComputeServerUnitChassisId_Type = CucsComputeServerUnitChassisId
_CucsComputeServerUnitChassisId_Object = MibTableColumn
cucsComputeServerUnitChassisId = _CucsComputeServerUnitChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 10),
    _CucsComputeServerUnitChassisId_Type()
)
cucsComputeServerUnitChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitChassisId.setStatus("current")
_CucsComputeServerUnitCheckPoint_Type = CucsComputeCheckPoint
_CucsComputeServerUnitCheckPoint_Object = MibTableColumn
cucsComputeServerUnitCheckPoint = _CucsComputeServerUnitCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 11),
    _CucsComputeServerUnitCheckPoint_Type()
)
cucsComputeServerUnitCheckPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitCheckPoint.setStatus("current")
_CucsComputeServerUnitConnPath_Type = CucsEquipmentConnectionStatus
_CucsComputeServerUnitConnPath_Object = MibTableColumn
cucsComputeServerUnitConnPath = _CucsComputeServerUnitConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 12),
    _CucsComputeServerUnitConnPath_Type()
)
cucsComputeServerUnitConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitConnPath.setStatus("current")
_CucsComputeServerUnitConnStatus_Type = CucsEquipmentConnectionStatus
_CucsComputeServerUnitConnStatus_Object = MibTableColumn
cucsComputeServerUnitConnStatus = _CucsComputeServerUnitConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 13),
    _CucsComputeServerUnitConnStatus_Type()
)
cucsComputeServerUnitConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitConnStatus.setStatus("current")
_CucsComputeServerUnitDescr_Type = SnmpAdminString
_CucsComputeServerUnitDescr_Object = MibTableColumn
cucsComputeServerUnitDescr = _CucsComputeServerUnitDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 14),
    _CucsComputeServerUnitDescr_Type()
)
cucsComputeServerUnitDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitDescr.setStatus("current")
_CucsComputeServerUnitDiscovery_Type = CucsComputeDiscovery
_CucsComputeServerUnitDiscovery_Object = MibTableColumn
cucsComputeServerUnitDiscovery = _CucsComputeServerUnitDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 15),
    _CucsComputeServerUnitDiscovery_Type()
)
cucsComputeServerUnitDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitDiscovery.setStatus("current")
_CucsComputeServerUnitDiscoveryStatus_Type = CucsEquipmentConnectionStatus
_CucsComputeServerUnitDiscoveryStatus_Object = MibTableColumn
cucsComputeServerUnitDiscoveryStatus = _CucsComputeServerUnitDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 16),
    _CucsComputeServerUnitDiscoveryStatus_Type()
)
cucsComputeServerUnitDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitDiscoveryStatus.setStatus("current")
_CucsComputeServerUnitFltAggr_Type = Unsigned64
_CucsComputeServerUnitFltAggr_Object = MibTableColumn
cucsComputeServerUnitFltAggr = _CucsComputeServerUnitFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 17),
    _CucsComputeServerUnitFltAggr_Type()
)
cucsComputeServerUnitFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFltAggr.setStatus("current")
_CucsComputeServerUnitFsmDescr_Type = SnmpAdminString
_CucsComputeServerUnitFsmDescr_Object = MibTableColumn
cucsComputeServerUnitFsmDescr = _CucsComputeServerUnitFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 18),
    _CucsComputeServerUnitFsmDescr_Type()
)
cucsComputeServerUnitFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmDescr.setStatus("current")
_CucsComputeServerUnitFsmFlags_Type = SnmpAdminString
_CucsComputeServerUnitFsmFlags_Object = MibTableColumn
cucsComputeServerUnitFsmFlags = _CucsComputeServerUnitFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 19),
    _CucsComputeServerUnitFsmFlags_Type()
)
cucsComputeServerUnitFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmFlags.setStatus("current")
_CucsComputeServerUnitFsmPrev_Type = SnmpAdminString
_CucsComputeServerUnitFsmPrev_Object = MibTableColumn
cucsComputeServerUnitFsmPrev = _CucsComputeServerUnitFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 20),
    _CucsComputeServerUnitFsmPrev_Type()
)
cucsComputeServerUnitFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmPrev.setStatus("current")
_CucsComputeServerUnitFsmProgr_Type = Gauge32
_CucsComputeServerUnitFsmProgr_Object = MibTableColumn
cucsComputeServerUnitFsmProgr = _CucsComputeServerUnitFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 21),
    _CucsComputeServerUnitFsmProgr_Type()
)
cucsComputeServerUnitFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmProgr.setStatus("current")
_CucsComputeServerUnitFsmRmtInvErrCode_Type = Gauge32
_CucsComputeServerUnitFsmRmtInvErrCode_Object = MibTableColumn
cucsComputeServerUnitFsmRmtInvErrCode = _CucsComputeServerUnitFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 22),
    _CucsComputeServerUnitFsmRmtInvErrCode_Type()
)
cucsComputeServerUnitFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmRmtInvErrCode.setStatus("current")
_CucsComputeServerUnitFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsComputeServerUnitFsmRmtInvErrDescr_Object = MibTableColumn
cucsComputeServerUnitFsmRmtInvErrDescr = _CucsComputeServerUnitFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 23),
    _CucsComputeServerUnitFsmRmtInvErrDescr_Type()
)
cucsComputeServerUnitFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmRmtInvErrDescr.setStatus("current")
_CucsComputeServerUnitFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsComputeServerUnitFsmRmtInvRslt_Object = MibTableColumn
cucsComputeServerUnitFsmRmtInvRslt = _CucsComputeServerUnitFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 24),
    _CucsComputeServerUnitFsmRmtInvRslt_Type()
)
cucsComputeServerUnitFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmRmtInvRslt.setStatus("current")
_CucsComputeServerUnitFsmStageDescr_Type = SnmpAdminString
_CucsComputeServerUnitFsmStageDescr_Object = MibTableColumn
cucsComputeServerUnitFsmStageDescr = _CucsComputeServerUnitFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 25),
    _CucsComputeServerUnitFsmStageDescr_Type()
)
cucsComputeServerUnitFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStageDescr.setStatus("current")
_CucsComputeServerUnitFsmStamp_Type = DateAndTime
_CucsComputeServerUnitFsmStamp_Object = MibTableColumn
cucsComputeServerUnitFsmStamp = _CucsComputeServerUnitFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 26),
    _CucsComputeServerUnitFsmStamp_Type()
)
cucsComputeServerUnitFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStamp.setStatus("current")
_CucsComputeServerUnitFsmStatus_Type = SnmpAdminString
_CucsComputeServerUnitFsmStatus_Object = MibTableColumn
cucsComputeServerUnitFsmStatus = _CucsComputeServerUnitFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 27),
    _CucsComputeServerUnitFsmStatus_Type()
)
cucsComputeServerUnitFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStatus.setStatus("current")
_CucsComputeServerUnitFsmTry_Type = Gauge32
_CucsComputeServerUnitFsmTry_Object = MibTableColumn
cucsComputeServerUnitFsmTry = _CucsComputeServerUnitFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 28),
    _CucsComputeServerUnitFsmTry_Type()
)
cucsComputeServerUnitFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmTry.setStatus("current")
_CucsComputeServerUnitIntId_Type = SnmpAdminString
_CucsComputeServerUnitIntId_Object = MibTableColumn
cucsComputeServerUnitIntId = _CucsComputeServerUnitIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 29),
    _CucsComputeServerUnitIntId_Type()
)
cucsComputeServerUnitIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitIntId.setStatus("current")
_CucsComputeServerUnitLc_Type = CucsComputeAdminTrigger
_CucsComputeServerUnitLc_Object = MibTableColumn
cucsComputeServerUnitLc = _CucsComputeServerUnitLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 30),
    _CucsComputeServerUnitLc_Type()
)
cucsComputeServerUnitLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitLc.setStatus("current")
_CucsComputeServerUnitLcTs_Type = DateAndTime
_CucsComputeServerUnitLcTs_Object = MibTableColumn
cucsComputeServerUnitLcTs = _CucsComputeServerUnitLcTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 31),
    _CucsComputeServerUnitLcTs_Type()
)
cucsComputeServerUnitLcTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitLcTs.setStatus("current")
_CucsComputeServerUnitLocalId_Type = SnmpAdminString
_CucsComputeServerUnitLocalId_Object = MibTableColumn
cucsComputeServerUnitLocalId = _CucsComputeServerUnitLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 32),
    _CucsComputeServerUnitLocalId_Type()
)
cucsComputeServerUnitLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitLocalId.setStatus("current")
_CucsComputeServerUnitLowVoltageMemory_Type = CucsComputePhysicalLowVoltageMemory
_CucsComputeServerUnitLowVoltageMemory_Object = MibTableColumn
cucsComputeServerUnitLowVoltageMemory = _CucsComputeServerUnitLowVoltageMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 33),
    _CucsComputeServerUnitLowVoltageMemory_Type()
)
cucsComputeServerUnitLowVoltageMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitLowVoltageMemory.setStatus("current")
_CucsComputeServerUnitManagingInst_Type = CucsNetworkSwitchId
_CucsComputeServerUnitManagingInst_Object = MibTableColumn
cucsComputeServerUnitManagingInst = _CucsComputeServerUnitManagingInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 34),
    _CucsComputeServerUnitManagingInst_Type()
)
cucsComputeServerUnitManagingInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitManagingInst.setStatus("current")
_CucsComputeServerUnitMemorySpeed_Type = Gauge32
_CucsComputeServerUnitMemorySpeed_Object = MibTableColumn
cucsComputeServerUnitMemorySpeed = _CucsComputeServerUnitMemorySpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 35),
    _CucsComputeServerUnitMemorySpeed_Type()
)
cucsComputeServerUnitMemorySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitMemorySpeed.setStatus("current")
_CucsComputeServerUnitMfgTime_Type = DateAndTime
_CucsComputeServerUnitMfgTime_Object = MibTableColumn
cucsComputeServerUnitMfgTime = _CucsComputeServerUnitMfgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 36),
    _CucsComputeServerUnitMfgTime_Type()
)
cucsComputeServerUnitMfgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitMfgTime.setStatus("current")
_CucsComputeServerUnitModel_Type = SnmpAdminString
_CucsComputeServerUnitModel_Object = MibTableColumn
cucsComputeServerUnitModel = _CucsComputeServerUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 37),
    _CucsComputeServerUnitModel_Type()
)
cucsComputeServerUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitModel.setStatus("current")
_CucsComputeServerUnitName_Type = SnmpAdminString
_CucsComputeServerUnitName_Object = MibTableColumn
cucsComputeServerUnitName = _CucsComputeServerUnitName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 38),
    _CucsComputeServerUnitName_Type()
)
cucsComputeServerUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitName.setStatus("current")
_CucsComputeServerUnitNumOfAdaptors_Type = Gauge32
_CucsComputeServerUnitNumOfAdaptors_Object = MibTableColumn
cucsComputeServerUnitNumOfAdaptors = _CucsComputeServerUnitNumOfAdaptors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 39),
    _CucsComputeServerUnitNumOfAdaptors_Type()
)
cucsComputeServerUnitNumOfAdaptors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitNumOfAdaptors.setStatus("current")
_CucsComputeServerUnitNumOfCores_Type = Gauge32
_CucsComputeServerUnitNumOfCores_Object = MibTableColumn
cucsComputeServerUnitNumOfCores = _CucsComputeServerUnitNumOfCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 40),
    _CucsComputeServerUnitNumOfCores_Type()
)
cucsComputeServerUnitNumOfCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitNumOfCores.setStatus("current")
_CucsComputeServerUnitNumOfCoresEnabled_Type = Gauge32
_CucsComputeServerUnitNumOfCoresEnabled_Object = MibTableColumn
cucsComputeServerUnitNumOfCoresEnabled = _CucsComputeServerUnitNumOfCoresEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 41),
    _CucsComputeServerUnitNumOfCoresEnabled_Type()
)
cucsComputeServerUnitNumOfCoresEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitNumOfCoresEnabled.setStatus("current")
_CucsComputeServerUnitNumOfCpus_Type = Gauge32
_CucsComputeServerUnitNumOfCpus_Object = MibTableColumn
cucsComputeServerUnitNumOfCpus = _CucsComputeServerUnitNumOfCpus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 42),
    _CucsComputeServerUnitNumOfCpus_Type()
)
cucsComputeServerUnitNumOfCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitNumOfCpus.setStatus("current")
_CucsComputeServerUnitNumOfEthHostIfs_Type = Gauge32
_CucsComputeServerUnitNumOfEthHostIfs_Object = MibTableColumn
cucsComputeServerUnitNumOfEthHostIfs = _CucsComputeServerUnitNumOfEthHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 43),
    _CucsComputeServerUnitNumOfEthHostIfs_Type()
)
cucsComputeServerUnitNumOfEthHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitNumOfEthHostIfs.setStatus("current")
_CucsComputeServerUnitNumOfFcHostIfs_Type = Gauge32
_CucsComputeServerUnitNumOfFcHostIfs_Object = MibTableColumn
cucsComputeServerUnitNumOfFcHostIfs = _CucsComputeServerUnitNumOfFcHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 44),
    _CucsComputeServerUnitNumOfFcHostIfs_Type()
)
cucsComputeServerUnitNumOfFcHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitNumOfFcHostIfs.setStatus("current")
_CucsComputeServerUnitNumOfThreads_Type = Gauge32
_CucsComputeServerUnitNumOfThreads_Object = MibTableColumn
cucsComputeServerUnitNumOfThreads = _CucsComputeServerUnitNumOfThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 45),
    _CucsComputeServerUnitNumOfThreads_Type()
)
cucsComputeServerUnitNumOfThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitNumOfThreads.setStatus("current")
_CucsComputeServerUnitOperPower_Type = CucsEquipmentPowerState
_CucsComputeServerUnitOperPower_Object = MibTableColumn
cucsComputeServerUnitOperPower = _CucsComputeServerUnitOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 46),
    _CucsComputeServerUnitOperPower_Type()
)
cucsComputeServerUnitOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitOperPower.setStatus("current")
_CucsComputeServerUnitOperQualifier_Type = CucsComputeIssues
_CucsComputeServerUnitOperQualifier_Object = MibTableColumn
cucsComputeServerUnitOperQualifier = _CucsComputeServerUnitOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 47),
    _CucsComputeServerUnitOperQualifier_Type()
)
cucsComputeServerUnitOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitOperQualifier.setStatus("current")
_CucsComputeServerUnitOperState_Type = CucsLsOperState
_CucsComputeServerUnitOperState_Object = MibTableColumn
cucsComputeServerUnitOperState = _CucsComputeServerUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 48),
    _CucsComputeServerUnitOperState_Type()
)
cucsComputeServerUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitOperState.setStatus("current")
_CucsComputeServerUnitOperability_Type = CucsEquipmentOperability
_CucsComputeServerUnitOperability_Object = MibTableColumn
cucsComputeServerUnitOperability = _CucsComputeServerUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 49),
    _CucsComputeServerUnitOperability_Type()
)
cucsComputeServerUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitOperability.setStatus("current")
_CucsComputeServerUnitOriginalUuid_Type = SnmpAdminString
_CucsComputeServerUnitOriginalUuid_Object = MibTableColumn
cucsComputeServerUnitOriginalUuid = _CucsComputeServerUnitOriginalUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 50),
    _CucsComputeServerUnitOriginalUuid_Type()
)
cucsComputeServerUnitOriginalUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitOriginalUuid.setStatus("current")
_CucsComputeServerUnitPartNumber_Type = SnmpAdminString
_CucsComputeServerUnitPartNumber_Object = MibTableColumn
cucsComputeServerUnitPartNumber = _CucsComputeServerUnitPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 51),
    _CucsComputeServerUnitPartNumber_Type()
)
cucsComputeServerUnitPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitPartNumber.setStatus("current")
_CucsComputeServerUnitPolicyLevel_Type = Gauge32
_CucsComputeServerUnitPolicyLevel_Object = MibTableColumn
cucsComputeServerUnitPolicyLevel = _CucsComputeServerUnitPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 52),
    _CucsComputeServerUnitPolicyLevel_Type()
)
cucsComputeServerUnitPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitPolicyLevel.setStatus("current")
_CucsComputeServerUnitPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsComputeServerUnitPolicyOwner_Object = MibTableColumn
cucsComputeServerUnitPolicyOwner = _CucsComputeServerUnitPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 53),
    _CucsComputeServerUnitPolicyOwner_Type()
)
cucsComputeServerUnitPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitPolicyOwner.setStatus("current")
_CucsComputeServerUnitPresence_Type = CucsEquipmentSlotStatus
_CucsComputeServerUnitPresence_Object = MibTableColumn
cucsComputeServerUnitPresence = _CucsComputeServerUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 54),
    _CucsComputeServerUnitPresence_Type()
)
cucsComputeServerUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitPresence.setStatus("current")
_CucsComputeServerUnitRevision_Type = SnmpAdminString
_CucsComputeServerUnitRevision_Object = MibTableColumn
cucsComputeServerUnitRevision = _CucsComputeServerUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 55),
    _CucsComputeServerUnitRevision_Type()
)
cucsComputeServerUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitRevision.setStatus("current")
_CucsComputeServerUnitSerial_Type = SnmpAdminString
_CucsComputeServerUnitSerial_Object = MibTableColumn
cucsComputeServerUnitSerial = _CucsComputeServerUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 56),
    _CucsComputeServerUnitSerial_Type()
)
cucsComputeServerUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitSerial.setStatus("current")
_CucsComputeServerUnitServerId_Type = SnmpAdminString
_CucsComputeServerUnitServerId_Object = MibTableColumn
cucsComputeServerUnitServerId = _CucsComputeServerUnitServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 57),
    _CucsComputeServerUnitServerId_Type()
)
cucsComputeServerUnitServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitServerId.setStatus("current")
_CucsComputeServerUnitServerInstanceId_Type = CucsComputeServerUnitServerInstanceId
_CucsComputeServerUnitServerInstanceId_Object = MibTableColumn
cucsComputeServerUnitServerInstanceId = _CucsComputeServerUnitServerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 58),
    _CucsComputeServerUnitServerInstanceId_Type()
)
cucsComputeServerUnitServerInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitServerInstanceId.setStatus("current")
_CucsComputeServerUnitSlotId_Type = CucsComputeServerUnitSlotId
_CucsComputeServerUnitSlotId_Object = MibTableColumn
cucsComputeServerUnitSlotId = _CucsComputeServerUnitSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 59),
    _CucsComputeServerUnitSlotId_Type()
)
cucsComputeServerUnitSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitSlotId.setStatus("current")
_CucsComputeServerUnitTotalMemory_Type = Gauge32
_CucsComputeServerUnitTotalMemory_Object = MibTableColumn
cucsComputeServerUnitTotalMemory = _CucsComputeServerUnitTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 60),
    _CucsComputeServerUnitTotalMemory_Type()
)
cucsComputeServerUnitTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitTotalMemory.setStatus("current")
_CucsComputeServerUnitUsrLbl_Type = SnmpAdminString
_CucsComputeServerUnitUsrLbl_Object = MibTableColumn
cucsComputeServerUnitUsrLbl = _CucsComputeServerUnitUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 61),
    _CucsComputeServerUnitUsrLbl_Type()
)
cucsComputeServerUnitUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitUsrLbl.setStatus("current")
_CucsComputeServerUnitUuid_Type = SnmpAdminString
_CucsComputeServerUnitUuid_Object = MibTableColumn
cucsComputeServerUnitUuid = _CucsComputeServerUnitUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 62),
    _CucsComputeServerUnitUuid_Type()
)
cucsComputeServerUnitUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitUuid.setStatus("current")
_CucsComputeServerUnitVendor_Type = SnmpAdminString
_CucsComputeServerUnitVendor_Object = MibTableColumn
cucsComputeServerUnitVendor = _CucsComputeServerUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 63),
    _CucsComputeServerUnitVendor_Type()
)
cucsComputeServerUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitVendor.setStatus("current")
_CucsComputeServerUnitVid_Type = SnmpAdminString
_CucsComputeServerUnitVid_Object = MibTableColumn
cucsComputeServerUnitVid = _CucsComputeServerUnitVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 64),
    _CucsComputeServerUnitVid_Type()
)
cucsComputeServerUnitVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitVid.setStatus("current")
_CucsComputeServerUnitNumOf40GAdaptorsWithOldFw_Type = Gauge32
_CucsComputeServerUnitNumOf40GAdaptorsWithOldFw_Object = MibTableColumn
cucsComputeServerUnitNumOf40GAdaptorsWithOldFw = _CucsComputeServerUnitNumOf40GAdaptorsWithOldFw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 66),
    _CucsComputeServerUnitNumOf40GAdaptorsWithOldFw_Type()
)
cucsComputeServerUnitNumOf40GAdaptorsWithOldFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitNumOf40GAdaptorsWithOldFw.setStatus("current")
_CucsComputeServerUnitNumOf40GAdaptorsWithUnknownFw_Type = Gauge32
_CucsComputeServerUnitNumOf40GAdaptorsWithUnknownFw_Object = MibTableColumn
cucsComputeServerUnitNumOf40GAdaptorsWithUnknownFw = _CucsComputeServerUnitNumOf40GAdaptorsWithUnknownFw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 67),
    _CucsComputeServerUnitNumOf40GAdaptorsWithUnknownFw_Type()
)
cucsComputeServerUnitNumOf40GAdaptorsWithUnknownFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitNumOf40GAdaptorsWithUnknownFw.setStatus("current")
_CucsComputeServerUnitOperPwrTransSrc_Type = CucsComputePowerTransitionSrc
_CucsComputeServerUnitOperPwrTransSrc_Object = MibTableColumn
cucsComputeServerUnitOperPwrTransSrc = _CucsComputeServerUnitOperPwrTransSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 74, 1, 68),
    _CucsComputeServerUnitOperPwrTransSrc_Type()
)
cucsComputeServerUnitOperPwrTransSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitOperPwrTransSrc.setStatus("current")
_CucsComputeServerUnitFsmTable_Object = MibTable
cucsComputeServerUnitFsmTable = _CucsComputeServerUnitFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75)
)
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmTable.setStatus("current")
_CucsComputeServerUnitFsmEntry_Object = MibTableRow
cucsComputeServerUnitFsmEntry = _CucsComputeServerUnitFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75, 1)
)
cucsComputeServerUnitFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeServerUnitFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmEntry.setStatus("current")
_CucsComputeServerUnitFsmInstanceId_Type = CucsManagedObjectId
_CucsComputeServerUnitFsmInstanceId_Object = MibTableColumn
cucsComputeServerUnitFsmInstanceId = _CucsComputeServerUnitFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75, 1, 1),
    _CucsComputeServerUnitFsmInstanceId_Type()
)
cucsComputeServerUnitFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmInstanceId.setStatus("current")
_CucsComputeServerUnitFsmDn_Type = CucsManagedObjectDn
_CucsComputeServerUnitFsmDn_Object = MibTableColumn
cucsComputeServerUnitFsmDn = _CucsComputeServerUnitFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75, 1, 2),
    _CucsComputeServerUnitFsmDn_Type()
)
cucsComputeServerUnitFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmDn.setStatus("current")
_CucsComputeServerUnitFsmRn_Type = SnmpAdminString
_CucsComputeServerUnitFsmRn_Object = MibTableColumn
cucsComputeServerUnitFsmRn = _CucsComputeServerUnitFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75, 1, 3),
    _CucsComputeServerUnitFsmRn_Type()
)
cucsComputeServerUnitFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmRn.setStatus("current")
_CucsComputeServerUnitFsmCompletionTime_Type = DateAndTime
_CucsComputeServerUnitFsmCompletionTime_Object = MibTableColumn
cucsComputeServerUnitFsmCompletionTime = _CucsComputeServerUnitFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75, 1, 4),
    _CucsComputeServerUnitFsmCompletionTime_Type()
)
cucsComputeServerUnitFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmCompletionTime.setStatus("current")
_CucsComputeServerUnitFsmCurrentFsm_Type = CucsComputeServerUnitFsmCurrentFsm
_CucsComputeServerUnitFsmCurrentFsm_Object = MibTableColumn
cucsComputeServerUnitFsmCurrentFsm = _CucsComputeServerUnitFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75, 1, 5),
    _CucsComputeServerUnitFsmCurrentFsm_Type()
)
cucsComputeServerUnitFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmCurrentFsm.setStatus("current")
_CucsComputeServerUnitFsmDescrData_Type = SnmpAdminString
_CucsComputeServerUnitFsmDescrData_Object = MibTableColumn
cucsComputeServerUnitFsmDescrData = _CucsComputeServerUnitFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75, 1, 6),
    _CucsComputeServerUnitFsmDescrData_Type()
)
cucsComputeServerUnitFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmDescrData.setStatus("current")
_CucsComputeServerUnitFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsComputeServerUnitFsmFsmStatus_Object = MibTableColumn
cucsComputeServerUnitFsmFsmStatus = _CucsComputeServerUnitFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75, 1, 7),
    _CucsComputeServerUnitFsmFsmStatus_Type()
)
cucsComputeServerUnitFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmFsmStatus.setStatus("current")
_CucsComputeServerUnitFsmProgress_Type = Gauge32
_CucsComputeServerUnitFsmProgress_Object = MibTableColumn
cucsComputeServerUnitFsmProgress = _CucsComputeServerUnitFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75, 1, 8),
    _CucsComputeServerUnitFsmProgress_Type()
)
cucsComputeServerUnitFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmProgress.setStatus("current")
_CucsComputeServerUnitFsmRmtErrCode_Type = Gauge32
_CucsComputeServerUnitFsmRmtErrCode_Object = MibTableColumn
cucsComputeServerUnitFsmRmtErrCode = _CucsComputeServerUnitFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75, 1, 9),
    _CucsComputeServerUnitFsmRmtErrCode_Type()
)
cucsComputeServerUnitFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmRmtErrCode.setStatus("current")
_CucsComputeServerUnitFsmRmtErrDescr_Type = SnmpAdminString
_CucsComputeServerUnitFsmRmtErrDescr_Object = MibTableColumn
cucsComputeServerUnitFsmRmtErrDescr = _CucsComputeServerUnitFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75, 1, 10),
    _CucsComputeServerUnitFsmRmtErrDescr_Type()
)
cucsComputeServerUnitFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmRmtErrDescr.setStatus("current")
_CucsComputeServerUnitFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsComputeServerUnitFsmRmtRslt_Object = MibTableColumn
cucsComputeServerUnitFsmRmtRslt = _CucsComputeServerUnitFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 75, 1, 11),
    _CucsComputeServerUnitFsmRmtRslt_Type()
)
cucsComputeServerUnitFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmRmtRslt.setStatus("current")
_CucsComputeServerUnitFsmStageTable_Object = MibTable
cucsComputeServerUnitFsmStageTable = _CucsComputeServerUnitFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 76)
)
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStageTable.setStatus("current")
_CucsComputeServerUnitFsmStageEntry_Object = MibTableRow
cucsComputeServerUnitFsmStageEntry = _CucsComputeServerUnitFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 76, 1)
)
cucsComputeServerUnitFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeServerUnitFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStageEntry.setStatus("current")
_CucsComputeServerUnitFsmStageInstanceId_Type = CucsManagedObjectId
_CucsComputeServerUnitFsmStageInstanceId_Object = MibTableColumn
cucsComputeServerUnitFsmStageInstanceId = _CucsComputeServerUnitFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 76, 1, 1),
    _CucsComputeServerUnitFsmStageInstanceId_Type()
)
cucsComputeServerUnitFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStageInstanceId.setStatus("current")
_CucsComputeServerUnitFsmStageDn_Type = CucsManagedObjectDn
_CucsComputeServerUnitFsmStageDn_Object = MibTableColumn
cucsComputeServerUnitFsmStageDn = _CucsComputeServerUnitFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 76, 1, 2),
    _CucsComputeServerUnitFsmStageDn_Type()
)
cucsComputeServerUnitFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStageDn.setStatus("current")
_CucsComputeServerUnitFsmStageRn_Type = SnmpAdminString
_CucsComputeServerUnitFsmStageRn_Object = MibTableColumn
cucsComputeServerUnitFsmStageRn = _CucsComputeServerUnitFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 76, 1, 3),
    _CucsComputeServerUnitFsmStageRn_Type()
)
cucsComputeServerUnitFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStageRn.setStatus("current")
_CucsComputeServerUnitFsmStageDescrData_Type = SnmpAdminString
_CucsComputeServerUnitFsmStageDescrData_Object = MibTableColumn
cucsComputeServerUnitFsmStageDescrData = _CucsComputeServerUnitFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 76, 1, 4),
    _CucsComputeServerUnitFsmStageDescrData_Type()
)
cucsComputeServerUnitFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStageDescrData.setStatus("current")
_CucsComputeServerUnitFsmStageLastUpdateTime_Type = DateAndTime
_CucsComputeServerUnitFsmStageLastUpdateTime_Object = MibTableColumn
cucsComputeServerUnitFsmStageLastUpdateTime = _CucsComputeServerUnitFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 76, 1, 5),
    _CucsComputeServerUnitFsmStageLastUpdateTime_Type()
)
cucsComputeServerUnitFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStageLastUpdateTime.setStatus("current")
_CucsComputeServerUnitFsmStageName_Type = CucsComputeServerUnitFsmStageName
_CucsComputeServerUnitFsmStageName_Object = MibTableColumn
cucsComputeServerUnitFsmStageName = _CucsComputeServerUnitFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 76, 1, 6),
    _CucsComputeServerUnitFsmStageName_Type()
)
cucsComputeServerUnitFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStageName.setStatus("current")
_CucsComputeServerUnitFsmStageOrder_Type = Gauge32
_CucsComputeServerUnitFsmStageOrder_Object = MibTableColumn
cucsComputeServerUnitFsmStageOrder = _CucsComputeServerUnitFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 76, 1, 7),
    _CucsComputeServerUnitFsmStageOrder_Type()
)
cucsComputeServerUnitFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStageOrder.setStatus("current")
_CucsComputeServerUnitFsmStageRetry_Type = Gauge32
_CucsComputeServerUnitFsmStageRetry_Object = MibTableColumn
cucsComputeServerUnitFsmStageRetry = _CucsComputeServerUnitFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 76, 1, 8),
    _CucsComputeServerUnitFsmStageRetry_Type()
)
cucsComputeServerUnitFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStageRetry.setStatus("current")
_CucsComputeServerUnitFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsComputeServerUnitFsmStageStageStatus_Object = MibTableColumn
cucsComputeServerUnitFsmStageStageStatus = _CucsComputeServerUnitFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 76, 1, 9),
    _CucsComputeServerUnitFsmStageStageStatus_Type()
)
cucsComputeServerUnitFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmStageStageStatus.setStatus("current")
_CucsComputeServerUnitFsmTaskTable_Object = MibTable
cucsComputeServerUnitFsmTaskTable = _CucsComputeServerUnitFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 77)
)
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmTaskTable.setStatus("current")
_CucsComputeServerUnitFsmTaskEntry_Object = MibTableRow
cucsComputeServerUnitFsmTaskEntry = _CucsComputeServerUnitFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 77, 1)
)
cucsComputeServerUnitFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB", "cucsComputeServerUnitFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmTaskEntry.setStatus("current")
_CucsComputeServerUnitFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsComputeServerUnitFsmTaskInstanceId_Object = MibTableColumn
cucsComputeServerUnitFsmTaskInstanceId = _CucsComputeServerUnitFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 77, 1, 1),
    _CucsComputeServerUnitFsmTaskInstanceId_Type()
)
cucsComputeServerUnitFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmTaskInstanceId.setStatus("current")
_CucsComputeServerUnitFsmTaskDn_Type = CucsManagedObjectDn
_CucsComputeServerUnitFsmTaskDn_Object = MibTableColumn
cucsComputeServerUnitFsmTaskDn = _CucsComputeServerUnitFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 77, 1, 2),
    _CucsComputeServerUnitFsmTaskDn_Type()
)
cucsComputeServerUnitFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmTaskDn.setStatus("current")
_CucsComputeServerUnitFsmTaskRn_Type = SnmpAdminString
_CucsComputeServerUnitFsmTaskRn_Object = MibTableColumn
cucsComputeServerUnitFsmTaskRn = _CucsComputeServerUnitFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 77, 1, 3),
    _CucsComputeServerUnitFsmTaskRn_Type()
)
cucsComputeServerUnitFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmTaskRn.setStatus("current")
_CucsComputeServerUnitFsmTaskCompletion_Type = CucsFsmCompletion
_CucsComputeServerUnitFsmTaskCompletion_Object = MibTableColumn
cucsComputeServerUnitFsmTaskCompletion = _CucsComputeServerUnitFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 77, 1, 4),
    _CucsComputeServerUnitFsmTaskCompletion_Type()
)
cucsComputeServerUnitFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmTaskCompletion.setStatus("current")
_CucsComputeServerUnitFsmTaskFlags_Type = CucsComputeServerUnitFsmTaskFlags
_CucsComputeServerUnitFsmTaskFlags_Object = MibTableColumn
cucsComputeServerUnitFsmTaskFlags = _CucsComputeServerUnitFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 77, 1, 5),
    _CucsComputeServerUnitFsmTaskFlags_Type()
)
cucsComputeServerUnitFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmTaskFlags.setStatus("current")
_CucsComputeServerUnitFsmTaskItem_Type = CucsComputeServerUnitFsmTaskItem
_CucsComputeServerUnitFsmTaskItem_Object = MibTableColumn
cucsComputeServerUnitFsmTaskItem = _CucsComputeServerUnitFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 77, 1, 6),
    _CucsComputeServerUnitFsmTaskItem_Type()
)
cucsComputeServerUnitFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmTaskItem.setStatus("current")
_CucsComputeServerUnitFsmTaskSeqId_Type = Gauge32
_CucsComputeServerUnitFsmTaskSeqId_Object = MibTableColumn
cucsComputeServerUnitFsmTaskSeqId = _CucsComputeServerUnitFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 9, 77, 1, 7),
    _CucsComputeServerUnitFsmTaskSeqId_Type()
)
cucsComputeServerUnitFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsComputeServerUnitFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-COMPUTE-MIB",
    **{"cucsComputeObjects": cucsComputeObjects,
       "cucsComputeAutoconfigPolicyTable": cucsComputeAutoconfigPolicyTable,
       "cucsComputeAutoconfigPolicyEntry": cucsComputeAutoconfigPolicyEntry,
       "cucsComputeAutoconfigPolicyInstanceId": cucsComputeAutoconfigPolicyInstanceId,
       "cucsComputeAutoconfigPolicyDn": cucsComputeAutoconfigPolicyDn,
       "cucsComputeAutoconfigPolicyRn": cucsComputeAutoconfigPolicyRn,
       "cucsComputeAutoconfigPolicyDescr": cucsComputeAutoconfigPolicyDescr,
       "cucsComputeAutoconfigPolicyDstDn": cucsComputeAutoconfigPolicyDstDn,
       "cucsComputeAutoconfigPolicyIntId": cucsComputeAutoconfigPolicyIntId,
       "cucsComputeAutoconfigPolicyName": cucsComputeAutoconfigPolicyName,
       "cucsComputeAutoconfigPolicyQualifier": cucsComputeAutoconfigPolicyQualifier,
       "cucsComputeAutoconfigPolicySrcTemplName": cucsComputeAutoconfigPolicySrcTemplName,
       "cucsComputeAutoconfigPolicyPolicyLevel": cucsComputeAutoconfigPolicyPolicyLevel,
       "cucsComputeAutoconfigPolicyPolicyOwner": cucsComputeAutoconfigPolicyPolicyOwner,
       "cucsComputeAutoconfigPolicyOperQualifier": cucsComputeAutoconfigPolicyOperQualifier,
       "cucsComputeBladeTable": cucsComputeBladeTable,
       "cucsComputeBladeEntry": cucsComputeBladeEntry,
       "cucsComputeBladeInstanceId": cucsComputeBladeInstanceId,
       "cucsComputeBladeDn": cucsComputeBladeDn,
       "cucsComputeBladeRn": cucsComputeBladeRn,
       "cucsComputeBladeAdminPower": cucsComputeBladeAdminPower,
       "cucsComputeBladeAdminState": cucsComputeBladeAdminState,
       "cucsComputeBladeAssignedToDn": cucsComputeBladeAssignedToDn,
       "cucsComputeBladeAssociation": cucsComputeBladeAssociation,
       "cucsComputeBladeAvailability": cucsComputeBladeAvailability,
       "cucsComputeBladeAvailableMemory": cucsComputeBladeAvailableMemory,
       "cucsComputeBladeChassisId": cucsComputeBladeChassisId,
       "cucsComputeBladeCheckPoint": cucsComputeBladeCheckPoint,
       "cucsComputeBladeConnPath": cucsComputeBladeConnPath,
       "cucsComputeBladeConnStatus": cucsComputeBladeConnStatus,
       "cucsComputeBladeDescr": cucsComputeBladeDescr,
       "cucsComputeBladeDiscovery": cucsComputeBladeDiscovery,
       "cucsComputeBladeFltAggr": cucsComputeBladeFltAggr,
       "cucsComputeBladeFsmDescr": cucsComputeBladeFsmDescr,
       "cucsComputeBladeFsmFlags": cucsComputeBladeFsmFlags,
       "cucsComputeBladeFsmPrev": cucsComputeBladeFsmPrev,
       "cucsComputeBladeFsmProgr": cucsComputeBladeFsmProgr,
       "cucsComputeBladeFsmRmtInvErrCode": cucsComputeBladeFsmRmtInvErrCode,
       "cucsComputeBladeFsmRmtInvErrDescr": cucsComputeBladeFsmRmtInvErrDescr,
       "cucsComputeBladeFsmRmtInvRslt": cucsComputeBladeFsmRmtInvRslt,
       "cucsComputeBladeFsmStageDescr": cucsComputeBladeFsmStageDescr,
       "cucsComputeBladeFsmStamp": cucsComputeBladeFsmStamp,
       "cucsComputeBladeFsmStatus": cucsComputeBladeFsmStatus,
       "cucsComputeBladeFsmTry": cucsComputeBladeFsmTry,
       "cucsComputeBladeIntId": cucsComputeBladeIntId,
       "cucsComputeBladeLc": cucsComputeBladeLc,
       "cucsComputeBladeLcTs": cucsComputeBladeLcTs,
       "cucsComputeBladeManagingInst": cucsComputeBladeManagingInst,
       "cucsComputeBladeModel": cucsComputeBladeModel,
       "cucsComputeBladeName": cucsComputeBladeName,
       "cucsComputeBladeNumOfAdaptors": cucsComputeBladeNumOfAdaptors,
       "cucsComputeBladeNumOfCores": cucsComputeBladeNumOfCores,
       "cucsComputeBladeNumOfCpus": cucsComputeBladeNumOfCpus,
       "cucsComputeBladeNumOfEthHostIfs": cucsComputeBladeNumOfEthHostIfs,
       "cucsComputeBladeNumOfFcHostIfs": cucsComputeBladeNumOfFcHostIfs,
       "cucsComputeBladeNumOfThreads": cucsComputeBladeNumOfThreads,
       "cucsComputeBladeOperPower": cucsComputeBladeOperPower,
       "cucsComputeBladeOperQualifier": cucsComputeBladeOperQualifier,
       "cucsComputeBladeOperState": cucsComputeBladeOperState,
       "cucsComputeBladeOperability": cucsComputeBladeOperability,
       "cucsComputeBladeOriginalUuid": cucsComputeBladeOriginalUuid,
       "cucsComputeBladePresence": cucsComputeBladePresence,
       "cucsComputeBladeRevision": cucsComputeBladeRevision,
       "cucsComputeBladeSerial": cucsComputeBladeSerial,
       "cucsComputeBladeServerId": cucsComputeBladeServerId,
       "cucsComputeBladeSlotId": cucsComputeBladeSlotId,
       "cucsComputeBladeTotalMemory": cucsComputeBladeTotalMemory,
       "cucsComputeBladeUsrLbl": cucsComputeBladeUsrLbl,
       "cucsComputeBladeUuid": cucsComputeBladeUuid,
       "cucsComputeBladeVendor": cucsComputeBladeVendor,
       "cucsComputeBladeNumOfCoresEnabled": cucsComputeBladeNumOfCoresEnabled,
       "cucsComputeBladeLowVoltageMemory": cucsComputeBladeLowVoltageMemory,
       "cucsComputeBladeMemorySpeed": cucsComputeBladeMemorySpeed,
       "cucsComputeBladeMfgTime": cucsComputeBladeMfgTime,
       "cucsComputeBladePartNumber": cucsComputeBladePartNumber,
       "cucsComputeBladeVid": cucsComputeBladeVid,
       "cucsComputeBladePolicyLevel": cucsComputeBladePolicyLevel,
       "cucsComputeBladePolicyOwner": cucsComputeBladePolicyOwner,
       "cucsComputeBladeLocalId": cucsComputeBladeLocalId,
       "cucsComputeBladeScaledMode": cucsComputeBladeScaledMode,
       "cucsComputeBladeUpgradeScenario": cucsComputeBladeUpgradeScenario,
       "cucsComputeBladeOperPwrTransSrc": cucsComputeBladeOperPwrTransSrc,
       "cucsComputeBladeDiscoveryStatus": cucsComputeBladeDiscoveryStatus,
       "cucsComputeBladeNumOf40GAdaptorsWithOldFw": cucsComputeBladeNumOf40GAdaptorsWithOldFw,
       "cucsComputeBladeNumOf40GAdaptorsWithUnknownFw": cucsComputeBladeNumOf40GAdaptorsWithUnknownFw,
       "cucsComputeBladeDiscPolicyTable": cucsComputeBladeDiscPolicyTable,
       "cucsComputeBladeDiscPolicyEntry": cucsComputeBladeDiscPolicyEntry,
       "cucsComputeBladeDiscPolicyInstanceId": cucsComputeBladeDiscPolicyInstanceId,
       "cucsComputeBladeDiscPolicyDn": cucsComputeBladeDiscPolicyDn,
       "cucsComputeBladeDiscPolicyRn": cucsComputeBladeDiscPolicyRn,
       "cucsComputeBladeDiscPolicyAction": cucsComputeBladeDiscPolicyAction,
       "cucsComputeBladeDiscPolicyDescr": cucsComputeBladeDiscPolicyDescr,
       "cucsComputeBladeDiscPolicyIntId": cucsComputeBladeDiscPolicyIntId,
       "cucsComputeBladeDiscPolicyName": cucsComputeBladeDiscPolicyName,
       "cucsComputeBladeDiscPolicyQualifier": cucsComputeBladeDiscPolicyQualifier,
       "cucsComputeBladeDiscPolicyScrubPolicyName": cucsComputeBladeDiscPolicyScrubPolicyName,
       "cucsComputeBladeDiscPolicyPolicyLevel": cucsComputeBladeDiscPolicyPolicyLevel,
       "cucsComputeBladeDiscPolicyPolicyOwner": cucsComputeBladeDiscPolicyPolicyOwner,
       "cucsComputeBladeFsmTaskTable": cucsComputeBladeFsmTaskTable,
       "cucsComputeBladeFsmTaskEntry": cucsComputeBladeFsmTaskEntry,
       "cucsComputeBladeFsmTaskInstanceId": cucsComputeBladeFsmTaskInstanceId,
       "cucsComputeBladeFsmTaskDn": cucsComputeBladeFsmTaskDn,
       "cucsComputeBladeFsmTaskRn": cucsComputeBladeFsmTaskRn,
       "cucsComputeBladeFsmTaskCompletion": cucsComputeBladeFsmTaskCompletion,
       "cucsComputeBladeFsmTaskFlags": cucsComputeBladeFsmTaskFlags,
       "cucsComputeBladeFsmTaskItem": cucsComputeBladeFsmTaskItem,
       "cucsComputeBladeFsmTaskSeqId": cucsComputeBladeFsmTaskSeqId,
       "cucsComputeBladeInheritPolicyTable": cucsComputeBladeInheritPolicyTable,
       "cucsComputeBladeInheritPolicyEntry": cucsComputeBladeInheritPolicyEntry,
       "cucsComputeBladeInheritPolicyInstanceId": cucsComputeBladeInheritPolicyInstanceId,
       "cucsComputeBladeInheritPolicyDn": cucsComputeBladeInheritPolicyDn,
       "cucsComputeBladeInheritPolicyRn": cucsComputeBladeInheritPolicyRn,
       "cucsComputeBladeInheritPolicyDescr": cucsComputeBladeInheritPolicyDescr,
       "cucsComputeBladeInheritPolicyDstDn": cucsComputeBladeInheritPolicyDstDn,
       "cucsComputeBladeInheritPolicyIntId": cucsComputeBladeInheritPolicyIntId,
       "cucsComputeBladeInheritPolicyName": cucsComputeBladeInheritPolicyName,
       "cucsComputeBladeInheritPolicyQualifier": cucsComputeBladeInheritPolicyQualifier,
       "cucsComputeBladeInheritPolicyPolicyLevel": cucsComputeBladeInheritPolicyPolicyLevel,
       "cucsComputeBladeInheritPolicyPolicyOwner": cucsComputeBladeInheritPolicyPolicyOwner,
       "cucsComputeBladeInheritPolicyOperQualifier": cucsComputeBladeInheritPolicyOperQualifier,
       "cucsComputeBoardTable": cucsComputeBoardTable,
       "cucsComputeBoardEntry": cucsComputeBoardEntry,
       "cucsComputeBoardInstanceId": cucsComputeBoardInstanceId,
       "cucsComputeBoardDn": cucsComputeBoardDn,
       "cucsComputeBoardRn": cucsComputeBoardRn,
       "cucsComputeBoardCmosVoltage": cucsComputeBoardCmosVoltage,
       "cucsComputeBoardId": cucsComputeBoardId,
       "cucsComputeBoardModel": cucsComputeBoardModel,
       "cucsComputeBoardOperPower": cucsComputeBoardOperPower,
       "cucsComputeBoardOperState": cucsComputeBoardOperState,
       "cucsComputeBoardOperability": cucsComputeBoardOperability,
       "cucsComputeBoardPerf": cucsComputeBoardPerf,
       "cucsComputeBoardPower": cucsComputeBoardPower,
       "cucsComputeBoardPresence": cucsComputeBoardPresence,
       "cucsComputeBoardRevision": cucsComputeBoardRevision,
       "cucsComputeBoardSerial": cucsComputeBoardSerial,
       "cucsComputeBoardThermal": cucsComputeBoardThermal,
       "cucsComputeBoardVendor": cucsComputeBoardVendor,
       "cucsComputeBoardVoltage": cucsComputeBoardVoltage,
       "cucsComputeBoardOperQualifierReason": cucsComputeBoardOperQualifierReason,
       "cucsComputeBoardPowerUsage": cucsComputeBoardPowerUsage,
       "cucsComputeBoardFaultQualifier": cucsComputeBoardFaultQualifier,
       "cucsComputeBoardLocationDn": cucsComputeBoardLocationDn,
       "cucsComputeBoardCpuTypeDescription": cucsComputeBoardCpuTypeDescription,
       "cucsComputeBoardControllerTable": cucsComputeBoardControllerTable,
       "cucsComputeBoardControllerEntry": cucsComputeBoardControllerEntry,
       "cucsComputeBoardControllerInstanceId": cucsComputeBoardControllerInstanceId,
       "cucsComputeBoardControllerDn": cucsComputeBoardControllerDn,
       "cucsComputeBoardControllerRn": cucsComputeBoardControllerRn,
       "cucsComputeBoardControllerId": cucsComputeBoardControllerId,
       "cucsComputeBoardControllerModel": cucsComputeBoardControllerModel,
       "cucsComputeBoardControllerOperState": cucsComputeBoardControllerOperState,
       "cucsComputeBoardControllerOperability": cucsComputeBoardControllerOperability,
       "cucsComputeBoardControllerPerf": cucsComputeBoardControllerPerf,
       "cucsComputeBoardControllerPower": cucsComputeBoardControllerPower,
       "cucsComputeBoardControllerPresence": cucsComputeBoardControllerPresence,
       "cucsComputeBoardControllerRevision": cucsComputeBoardControllerRevision,
       "cucsComputeBoardControllerSerial": cucsComputeBoardControllerSerial,
       "cucsComputeBoardControllerThermal": cucsComputeBoardControllerThermal,
       "cucsComputeBoardControllerVendor": cucsComputeBoardControllerVendor,
       "cucsComputeBoardControllerVoltage": cucsComputeBoardControllerVoltage,
       "cucsComputeBoardControllerOperQualifierReason": cucsComputeBoardControllerOperQualifierReason,
       "cucsComputeBoardControllerLocationDn": cucsComputeBoardControllerLocationDn,
       "cucsComputeChassisDiscPolicyTable": cucsComputeChassisDiscPolicyTable,
       "cucsComputeChassisDiscPolicyEntry": cucsComputeChassisDiscPolicyEntry,
       "cucsComputeChassisDiscPolicyInstanceId": cucsComputeChassisDiscPolicyInstanceId,
       "cucsComputeChassisDiscPolicyDn": cucsComputeChassisDiscPolicyDn,
       "cucsComputeChassisDiscPolicyRn": cucsComputeChassisDiscPolicyRn,
       "cucsComputeChassisDiscPolicyAction": cucsComputeChassisDiscPolicyAction,
       "cucsComputeChassisDiscPolicyDescr": cucsComputeChassisDiscPolicyDescr,
       "cucsComputeChassisDiscPolicyIntId": cucsComputeChassisDiscPolicyIntId,
       "cucsComputeChassisDiscPolicyName": cucsComputeChassisDiscPolicyName,
       "cucsComputeChassisDiscPolicyQualifier": cucsComputeChassisDiscPolicyQualifier,
       "cucsComputeChassisDiscPolicyRebalance": cucsComputeChassisDiscPolicyRebalance,
       "cucsComputeChassisDiscPolicyLinkAggregationPref": cucsComputeChassisDiscPolicyLinkAggregationPref,
       "cucsComputeChassisDiscPolicyPolicyLevel": cucsComputeChassisDiscPolicyPolicyLevel,
       "cucsComputeChassisDiscPolicyPolicyOwner": cucsComputeChassisDiscPolicyPolicyOwner,
       "cucsComputeChassisDiscPolicyMulticastHwHash": cucsComputeChassisDiscPolicyMulticastHwHash,
       "cucsComputeChassisQualTable": cucsComputeChassisQualTable,
       "cucsComputeChassisQualEntry": cucsComputeChassisQualEntry,
       "cucsComputeChassisQualInstanceId": cucsComputeChassisQualInstanceId,
       "cucsComputeChassisQualDn": cucsComputeChassisQualDn,
       "cucsComputeChassisQualRn": cucsComputeChassisQualRn,
       "cucsComputeChassisQualMaxId": cucsComputeChassisQualMaxId,
       "cucsComputeChassisQualMinId": cucsComputeChassisQualMinId,
       "cucsComputeDefaultsTable": cucsComputeDefaultsTable,
       "cucsComputeDefaultsEntry": cucsComputeDefaultsEntry,
       "cucsComputeDefaultsInstanceId": cucsComputeDefaultsInstanceId,
       "cucsComputeDefaultsDn": cucsComputeDefaultsDn,
       "cucsComputeDefaultsRn": cucsComputeDefaultsRn,
       "cucsComputeIOHubTable": cucsComputeIOHubTable,
       "cucsComputeIOHubEntry": cucsComputeIOHubEntry,
       "cucsComputeIOHubInstanceId": cucsComputeIOHubInstanceId,
       "cucsComputeIOHubDn": cucsComputeIOHubDn,
       "cucsComputeIOHubRn": cucsComputeIOHubRn,
       "cucsComputeIOHubId": cucsComputeIOHubId,
       "cucsComputeIOHubModel": cucsComputeIOHubModel,
       "cucsComputeIOHubOperState": cucsComputeIOHubOperState,
       "cucsComputeIOHubOperability": cucsComputeIOHubOperability,
       "cucsComputeIOHubPerf": cucsComputeIOHubPerf,
       "cucsComputeIOHubPower": cucsComputeIOHubPower,
       "cucsComputeIOHubPresence": cucsComputeIOHubPresence,
       "cucsComputeIOHubRevision": cucsComputeIOHubRevision,
       "cucsComputeIOHubSerial": cucsComputeIOHubSerial,
       "cucsComputeIOHubThermal": cucsComputeIOHubThermal,
       "cucsComputeIOHubVendor": cucsComputeIOHubVendor,
       "cucsComputeIOHubVoltage": cucsComputeIOHubVoltage,
       "cucsComputeIOHubOperQualifierReason": cucsComputeIOHubOperQualifierReason,
       "cucsComputeIOHubLocationDn": cucsComputeIOHubLocationDn,
       "cucsComputeIOHubEnvStatsTable": cucsComputeIOHubEnvStatsTable,
       "cucsComputeIOHubEnvStatsEntry": cucsComputeIOHubEnvStatsEntry,
       "cucsComputeIOHubEnvStatsInstanceId": cucsComputeIOHubEnvStatsInstanceId,
       "cucsComputeIOHubEnvStatsDn": cucsComputeIOHubEnvStatsDn,
       "cucsComputeIOHubEnvStatsRn": cucsComputeIOHubEnvStatsRn,
       "cucsComputeIOHubEnvStatsIntervals": cucsComputeIOHubEnvStatsIntervals,
       "cucsComputeIOHubEnvStatsSuspect": cucsComputeIOHubEnvStatsSuspect,
       "cucsComputeIOHubEnvStatsTemperature": cucsComputeIOHubEnvStatsTemperature,
       "cucsComputeIOHubEnvStatsTemperatureAvg": cucsComputeIOHubEnvStatsTemperatureAvg,
       "cucsComputeIOHubEnvStatsTemperatureMax": cucsComputeIOHubEnvStatsTemperatureMax,
       "cucsComputeIOHubEnvStatsTemperatureMin": cucsComputeIOHubEnvStatsTemperatureMin,
       "cucsComputeIOHubEnvStatsThresholded": cucsComputeIOHubEnvStatsThresholded,
       "cucsComputeIOHubEnvStatsTimeCollected": cucsComputeIOHubEnvStatsTimeCollected,
       "cucsComputeIOHubEnvStatsUpdate": cucsComputeIOHubEnvStatsUpdate,
       "cucsComputeIOHubEnvStatsHistTable": cucsComputeIOHubEnvStatsHistTable,
       "cucsComputeIOHubEnvStatsHistEntry": cucsComputeIOHubEnvStatsHistEntry,
       "cucsComputeIOHubEnvStatsHistInstanceId": cucsComputeIOHubEnvStatsHistInstanceId,
       "cucsComputeIOHubEnvStatsHistDn": cucsComputeIOHubEnvStatsHistDn,
       "cucsComputeIOHubEnvStatsHistRn": cucsComputeIOHubEnvStatsHistRn,
       "cucsComputeIOHubEnvStatsHistId": cucsComputeIOHubEnvStatsHistId,
       "cucsComputeIOHubEnvStatsHistMostRecent": cucsComputeIOHubEnvStatsHistMostRecent,
       "cucsComputeIOHubEnvStatsHistSuspect": cucsComputeIOHubEnvStatsHistSuspect,
       "cucsComputeIOHubEnvStatsHistTemperature": cucsComputeIOHubEnvStatsHistTemperature,
       "cucsComputeIOHubEnvStatsHistTemperatureAvg": cucsComputeIOHubEnvStatsHistTemperatureAvg,
       "cucsComputeIOHubEnvStatsHistTemperatureMax": cucsComputeIOHubEnvStatsHistTemperatureMax,
       "cucsComputeIOHubEnvStatsHistTemperatureMin": cucsComputeIOHubEnvStatsHistTemperatureMin,
       "cucsComputeIOHubEnvStatsHistThresholded": cucsComputeIOHubEnvStatsHistThresholded,
       "cucsComputeIOHubEnvStatsHistTimeCollected": cucsComputeIOHubEnvStatsHistTimeCollected,
       "cucsComputeMbPowerStatsTable": cucsComputeMbPowerStatsTable,
       "cucsComputeMbPowerStatsEntry": cucsComputeMbPowerStatsEntry,
       "cucsComputeMbPowerStatsInstanceId": cucsComputeMbPowerStatsInstanceId,
       "cucsComputeMbPowerStatsDn": cucsComputeMbPowerStatsDn,
       "cucsComputeMbPowerStatsRn": cucsComputeMbPowerStatsRn,
       "cucsComputeMbPowerStatsConsumedPower": cucsComputeMbPowerStatsConsumedPower,
       "cucsComputeMbPowerStatsConsumedPowerAvg": cucsComputeMbPowerStatsConsumedPowerAvg,
       "cucsComputeMbPowerStatsConsumedPowerMax": cucsComputeMbPowerStatsConsumedPowerMax,
       "cucsComputeMbPowerStatsConsumedPowerMin": cucsComputeMbPowerStatsConsumedPowerMin,
       "cucsComputeMbPowerStatsInputCurrent": cucsComputeMbPowerStatsInputCurrent,
       "cucsComputeMbPowerStatsInputCurrentAvg": cucsComputeMbPowerStatsInputCurrentAvg,
       "cucsComputeMbPowerStatsInputCurrentMax": cucsComputeMbPowerStatsInputCurrentMax,
       "cucsComputeMbPowerStatsInputCurrentMin": cucsComputeMbPowerStatsInputCurrentMin,
       "cucsComputeMbPowerStatsInputVoltage": cucsComputeMbPowerStatsInputVoltage,
       "cucsComputeMbPowerStatsInputVoltageAvg": cucsComputeMbPowerStatsInputVoltageAvg,
       "cucsComputeMbPowerStatsInputVoltageMax": cucsComputeMbPowerStatsInputVoltageMax,
       "cucsComputeMbPowerStatsInputVoltageMin": cucsComputeMbPowerStatsInputVoltageMin,
       "cucsComputeMbPowerStatsIntervals": cucsComputeMbPowerStatsIntervals,
       "cucsComputeMbPowerStatsSuspect": cucsComputeMbPowerStatsSuspect,
       "cucsComputeMbPowerStatsThresholded": cucsComputeMbPowerStatsThresholded,
       "cucsComputeMbPowerStatsTimeCollected": cucsComputeMbPowerStatsTimeCollected,
       "cucsComputeMbPowerStatsUpdate": cucsComputeMbPowerStatsUpdate,
       "cucsComputeMbPowerStatsHistTable": cucsComputeMbPowerStatsHistTable,
       "cucsComputeMbPowerStatsHistEntry": cucsComputeMbPowerStatsHistEntry,
       "cucsComputeMbPowerStatsHistInstanceId": cucsComputeMbPowerStatsHistInstanceId,
       "cucsComputeMbPowerStatsHistDn": cucsComputeMbPowerStatsHistDn,
       "cucsComputeMbPowerStatsHistRn": cucsComputeMbPowerStatsHistRn,
       "cucsComputeMbPowerStatsHistConsumedPower": cucsComputeMbPowerStatsHistConsumedPower,
       "cucsComputeMbPowerStatsHistConsumedPowerAvg": cucsComputeMbPowerStatsHistConsumedPowerAvg,
       "cucsComputeMbPowerStatsHistConsumedPowerMax": cucsComputeMbPowerStatsHistConsumedPowerMax,
       "cucsComputeMbPowerStatsHistConsumedPowerMin": cucsComputeMbPowerStatsHistConsumedPowerMin,
       "cucsComputeMbPowerStatsHistId": cucsComputeMbPowerStatsHistId,
       "cucsComputeMbPowerStatsHistInputCurrent": cucsComputeMbPowerStatsHistInputCurrent,
       "cucsComputeMbPowerStatsHistInputCurrentAvg": cucsComputeMbPowerStatsHistInputCurrentAvg,
       "cucsComputeMbPowerStatsHistInputCurrentMax": cucsComputeMbPowerStatsHistInputCurrentMax,
       "cucsComputeMbPowerStatsHistInputCurrentMin": cucsComputeMbPowerStatsHistInputCurrentMin,
       "cucsComputeMbPowerStatsHistInputVoltage": cucsComputeMbPowerStatsHistInputVoltage,
       "cucsComputeMbPowerStatsHistInputVoltageAvg": cucsComputeMbPowerStatsHistInputVoltageAvg,
       "cucsComputeMbPowerStatsHistInputVoltageMax": cucsComputeMbPowerStatsHistInputVoltageMax,
       "cucsComputeMbPowerStatsHistInputVoltageMin": cucsComputeMbPowerStatsHistInputVoltageMin,
       "cucsComputeMbPowerStatsHistMostRecent": cucsComputeMbPowerStatsHistMostRecent,
       "cucsComputeMbPowerStatsHistSuspect": cucsComputeMbPowerStatsHistSuspect,
       "cucsComputeMbPowerStatsHistThresholded": cucsComputeMbPowerStatsHistThresholded,
       "cucsComputeMbPowerStatsHistTimeCollected": cucsComputeMbPowerStatsHistTimeCollected,
       "cucsComputeMbTempStatsTable": cucsComputeMbTempStatsTable,
       "cucsComputeMbTempStatsEntry": cucsComputeMbTempStatsEntry,
       "cucsComputeMbTempStatsInstanceId": cucsComputeMbTempStatsInstanceId,
       "cucsComputeMbTempStatsDn": cucsComputeMbTempStatsDn,
       "cucsComputeMbTempStatsRn": cucsComputeMbTempStatsRn,
       "cucsComputeMbTempStatsFmTempSenIo": cucsComputeMbTempStatsFmTempSenIo,
       "cucsComputeMbTempStatsFmTempSenIoAvg": cucsComputeMbTempStatsFmTempSenIoAvg,
       "cucsComputeMbTempStatsFmTempSenIoMax": cucsComputeMbTempStatsFmTempSenIoMax,
       "cucsComputeMbTempStatsFmTempSenIoMin": cucsComputeMbTempStatsFmTempSenIoMin,
       "cucsComputeMbTempStatsFmTempSenRear": cucsComputeMbTempStatsFmTempSenRear,
       "cucsComputeMbTempStatsFmTempSenRearAvg": cucsComputeMbTempStatsFmTempSenRearAvg,
       "cucsComputeMbTempStatsFmTempSenRearL": cucsComputeMbTempStatsFmTempSenRearL,
       "cucsComputeMbTempStatsFmTempSenRearLAvg": cucsComputeMbTempStatsFmTempSenRearLAvg,
       "cucsComputeMbTempStatsFmTempSenRearLMax": cucsComputeMbTempStatsFmTempSenRearLMax,
       "cucsComputeMbTempStatsFmTempSenRearLMin": cucsComputeMbTempStatsFmTempSenRearLMin,
       "cucsComputeMbTempStatsFmTempSenRearMax": cucsComputeMbTempStatsFmTempSenRearMax,
       "cucsComputeMbTempStatsFmTempSenRearMin": cucsComputeMbTempStatsFmTempSenRearMin,
       "cucsComputeMbTempStatsFmTempSenRearR": cucsComputeMbTempStatsFmTempSenRearR,
       "cucsComputeMbTempStatsFmTempSenRearRAvg": cucsComputeMbTempStatsFmTempSenRearRAvg,
       "cucsComputeMbTempStatsFmTempSenRearRMax": cucsComputeMbTempStatsFmTempSenRearRMax,
       "cucsComputeMbTempStatsFmTempSenRearRMin": cucsComputeMbTempStatsFmTempSenRearRMin,
       "cucsComputeMbTempStatsIntervals": cucsComputeMbTempStatsIntervals,
       "cucsComputeMbTempStatsSuspect": cucsComputeMbTempStatsSuspect,
       "cucsComputeMbTempStatsThresholded": cucsComputeMbTempStatsThresholded,
       "cucsComputeMbTempStatsTimeCollected": cucsComputeMbTempStatsTimeCollected,
       "cucsComputeMbTempStatsUpdate": cucsComputeMbTempStatsUpdate,
       "cucsComputeMbTempStatsHistTable": cucsComputeMbTempStatsHistTable,
       "cucsComputeMbTempStatsHistEntry": cucsComputeMbTempStatsHistEntry,
       "cucsComputeMbTempStatsHistInstanceId": cucsComputeMbTempStatsHistInstanceId,
       "cucsComputeMbTempStatsHistDn": cucsComputeMbTempStatsHistDn,
       "cucsComputeMbTempStatsHistRn": cucsComputeMbTempStatsHistRn,
       "cucsComputeMbTempStatsHistFmTempSenIo": cucsComputeMbTempStatsHistFmTempSenIo,
       "cucsComputeMbTempStatsHistFmTempSenIoAvg": cucsComputeMbTempStatsHistFmTempSenIoAvg,
       "cucsComputeMbTempStatsHistFmTempSenIoMax": cucsComputeMbTempStatsHistFmTempSenIoMax,
       "cucsComputeMbTempStatsHistFmTempSenIoMin": cucsComputeMbTempStatsHistFmTempSenIoMin,
       "cucsComputeMbTempStatsHistFmTempSenRear": cucsComputeMbTempStatsHistFmTempSenRear,
       "cucsComputeMbTempStatsHistFmTempSenRearAvg": cucsComputeMbTempStatsHistFmTempSenRearAvg,
       "cucsComputeMbTempStatsHistFmTempSenRearL": cucsComputeMbTempStatsHistFmTempSenRearL,
       "cucsComputeMbTempStatsHistFmTempSenRearLAvg": cucsComputeMbTempStatsHistFmTempSenRearLAvg,
       "cucsComputeMbTempStatsHistFmTempSenRearLMax": cucsComputeMbTempStatsHistFmTempSenRearLMax,
       "cucsComputeMbTempStatsHistFmTempSenRearLMin": cucsComputeMbTempStatsHistFmTempSenRearLMin,
       "cucsComputeMbTempStatsHistFmTempSenRearMax": cucsComputeMbTempStatsHistFmTempSenRearMax,
       "cucsComputeMbTempStatsHistFmTempSenRearMin": cucsComputeMbTempStatsHistFmTempSenRearMin,
       "cucsComputeMbTempStatsHistFmTempSenRearR": cucsComputeMbTempStatsHistFmTempSenRearR,
       "cucsComputeMbTempStatsHistFmTempSenRearRAvg": cucsComputeMbTempStatsHistFmTempSenRearRAvg,
       "cucsComputeMbTempStatsHistFmTempSenRearRMax": cucsComputeMbTempStatsHistFmTempSenRearRMax,
       "cucsComputeMbTempStatsHistFmTempSenRearRMin": cucsComputeMbTempStatsHistFmTempSenRearRMin,
       "cucsComputeMbTempStatsHistId": cucsComputeMbTempStatsHistId,
       "cucsComputeMbTempStatsHistMostRecent": cucsComputeMbTempStatsHistMostRecent,
       "cucsComputeMbTempStatsHistSuspect": cucsComputeMbTempStatsHistSuspect,
       "cucsComputeMbTempStatsHistThresholded": cucsComputeMbTempStatsHistThresholded,
       "cucsComputeMbTempStatsHistTimeCollected": cucsComputeMbTempStatsHistTimeCollected,
       "cucsComputeMemoryUnitConstraintDefTable": cucsComputeMemoryUnitConstraintDefTable,
       "cucsComputeMemoryUnitConstraintDefEntry": cucsComputeMemoryUnitConstraintDefEntry,
       "cucsComputeMemoryUnitConstraintDefInstanceId": cucsComputeMemoryUnitConstraintDefInstanceId,
       "cucsComputeMemoryUnitConstraintDefDn": cucsComputeMemoryUnitConstraintDefDn,
       "cucsComputeMemoryUnitConstraintDefRn": cucsComputeMemoryUnitConstraintDefRn,
       "cucsComputeMemoryUnitConstraintDefDescr": cucsComputeMemoryUnitConstraintDefDescr,
       "cucsComputeMemoryUnitConstraintDefIntId": cucsComputeMemoryUnitConstraintDefIntId,
       "cucsComputeMemoryUnitConstraintDefName": cucsComputeMemoryUnitConstraintDefName,
       "cucsComputeMemoryUnitConstraintDefType": cucsComputeMemoryUnitConstraintDefType,
       "cucsComputeMemoryUnitConstraintDefRevisionModifier": cucsComputeMemoryUnitConstraintDefRevisionModifier,
       "cucsComputeMemoryUnitConstraintDefPolicyLevel": cucsComputeMemoryUnitConstraintDefPolicyLevel,
       "cucsComputeMemoryUnitConstraintDefPolicyOwner": cucsComputeMemoryUnitConstraintDefPolicyOwner,
       "cucsComputePCIeFatalCompletionStatsTable": cucsComputePCIeFatalCompletionStatsTable,
       "cucsComputePCIeFatalCompletionStatsEntry": cucsComputePCIeFatalCompletionStatsEntry,
       "cucsComputePCIeFatalCompletionStatsInstanceId": cucsComputePCIeFatalCompletionStatsInstanceId,
       "cucsComputePCIeFatalCompletionStatsDn": cucsComputePCIeFatalCompletionStatsDn,
       "cucsComputePCIeFatalCompletionStatsRn": cucsComputePCIeFatalCompletionStatsRn,
       "cucsComputePCIeFatalCompletionStatsAbortErrors": cucsComputePCIeFatalCompletionStatsAbortErrors,
       "cucsComputePCIeFatalCompletionStatsAbortErrors15Min": cucsComputePCIeFatalCompletionStatsAbortErrors15Min,
       "cucsComputePCIeFatalCompletionStatsAbortErrors15MinH": cucsComputePCIeFatalCompletionStatsAbortErrors15MinH,
       "cucsComputePCIeFatalCompletionStatsAbortErrors1Day": cucsComputePCIeFatalCompletionStatsAbortErrors1Day,
       "cucsComputePCIeFatalCompletionStatsAbortErrors1DayH": cucsComputePCIeFatalCompletionStatsAbortErrors1DayH,
       "cucsComputePCIeFatalCompletionStatsAbortErrors1Hour": cucsComputePCIeFatalCompletionStatsAbortErrors1Hour,
       "cucsComputePCIeFatalCompletionStatsAbortErrors1HourH": cucsComputePCIeFatalCompletionStatsAbortErrors1HourH,
       "cucsComputePCIeFatalCompletionStatsAbortErrors1Week": cucsComputePCIeFatalCompletionStatsAbortErrors1Week,
       "cucsComputePCIeFatalCompletionStatsAbortErrors1WeekH": cucsComputePCIeFatalCompletionStatsAbortErrors1WeekH,
       "cucsComputePCIeFatalCompletionStatsTimeoutErrors": cucsComputePCIeFatalCompletionStatsTimeoutErrors,
       "cucsComputePCIeFatalCompletionStatsTimeoutErrors15Min": cucsComputePCIeFatalCompletionStatsTimeoutErrors15Min,
       "cucsComputePCIeFatalCompletionStatsTimeoutErrors15MinH": cucsComputePCIeFatalCompletionStatsTimeoutErrors15MinH,
       "cucsComputePCIeFatalCompletionStatsTimeoutErrors1Day": cucsComputePCIeFatalCompletionStatsTimeoutErrors1Day,
       "cucsComputePCIeFatalCompletionStatsTimeoutErrors1DayH": cucsComputePCIeFatalCompletionStatsTimeoutErrors1DayH,
       "cucsComputePCIeFatalCompletionStatsTimeoutErrors1Hour": cucsComputePCIeFatalCompletionStatsTimeoutErrors1Hour,
       "cucsComputePCIeFatalCompletionStatsTimeoutErrors1HourH": cucsComputePCIeFatalCompletionStatsTimeoutErrors1HourH,
       "cucsComputePCIeFatalCompletionStatsTimeoutErrors1Week": cucsComputePCIeFatalCompletionStatsTimeoutErrors1Week,
       "cucsComputePCIeFatalCompletionStatsTimeoutErrors1WeekH": cucsComputePCIeFatalCompletionStatsTimeoutErrors1WeekH,
       "cucsComputePCIeFatalCompletionStatsIntervals": cucsComputePCIeFatalCompletionStatsIntervals,
       "cucsComputePCIeFatalCompletionStatsSuspect": cucsComputePCIeFatalCompletionStatsSuspect,
       "cucsComputePCIeFatalCompletionStatsThresholded": cucsComputePCIeFatalCompletionStatsThresholded,
       "cucsComputePCIeFatalCompletionStatsTimeCollected": cucsComputePCIeFatalCompletionStatsTimeCollected,
       "cucsComputePCIeFatalCompletionStatsUnexpectedErrors": cucsComputePCIeFatalCompletionStatsUnexpectedErrors,
       "cucsComputePCIeFatalCompletionStatsUnexpectedErrors15Min": cucsComputePCIeFatalCompletionStatsUnexpectedErrors15Min,
       "cucsComputePCIeFatalCompletionStatsUnexpectedErrors15MinH": cucsComputePCIeFatalCompletionStatsUnexpectedErrors15MinH,
       "cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Day": cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Day,
       "cucsComputePCIeFatalCompletionStatsUnexpectedErrors1DayH": cucsComputePCIeFatalCompletionStatsUnexpectedErrors1DayH,
       "cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Hour": cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Hour,
       "cucsComputePCIeFatalCompletionStatsUnexpectedErrors1HourH": cucsComputePCIeFatalCompletionStatsUnexpectedErrors1HourH,
       "cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Week": cucsComputePCIeFatalCompletionStatsUnexpectedErrors1Week,
       "cucsComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH": cucsComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH,
       "cucsComputePCIeFatalCompletionStatsUpdate": cucsComputePCIeFatalCompletionStatsUpdate,
       "cucsComputePCIeFatalCompletionStatsAbortErrors2Weeks": cucsComputePCIeFatalCompletionStatsAbortErrors2Weeks,
       "cucsComputePCIeFatalCompletionStatsAbortErrors2WeeksH": cucsComputePCIeFatalCompletionStatsAbortErrors2WeeksH,
       "cucsComputePCIeFatalCompletionStatsTimeoutErrors2Weeks": cucsComputePCIeFatalCompletionStatsTimeoutErrors2Weeks,
       "cucsComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH": cucsComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH,
       "cucsComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks": cucsComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks,
       "cucsComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH": cucsComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH,
       "cucsComputePCIeFatalProtocolStatsTable": cucsComputePCIeFatalProtocolStatsTable,
       "cucsComputePCIeFatalProtocolStatsEntry": cucsComputePCIeFatalProtocolStatsEntry,
       "cucsComputePCIeFatalProtocolStatsInstanceId": cucsComputePCIeFatalProtocolStatsInstanceId,
       "cucsComputePCIeFatalProtocolStatsDn": cucsComputePCIeFatalProtocolStatsDn,
       "cucsComputePCIeFatalProtocolStatsRn": cucsComputePCIeFatalProtocolStatsRn,
       "cucsComputePCIeFatalProtocolStatsDllpErrors": cucsComputePCIeFatalProtocolStatsDllpErrors,
       "cucsComputePCIeFatalProtocolStatsDllpErrors15Min": cucsComputePCIeFatalProtocolStatsDllpErrors15Min,
       "cucsComputePCIeFatalProtocolStatsDllpErrors15MinH": cucsComputePCIeFatalProtocolStatsDllpErrors15MinH,
       "cucsComputePCIeFatalProtocolStatsDllpErrors1Day": cucsComputePCIeFatalProtocolStatsDllpErrors1Day,
       "cucsComputePCIeFatalProtocolStatsDllpErrors1DayH": cucsComputePCIeFatalProtocolStatsDllpErrors1DayH,
       "cucsComputePCIeFatalProtocolStatsDllpErrors1Hour": cucsComputePCIeFatalProtocolStatsDllpErrors1Hour,
       "cucsComputePCIeFatalProtocolStatsDllpErrors1HourH": cucsComputePCIeFatalProtocolStatsDllpErrors1HourH,
       "cucsComputePCIeFatalProtocolStatsDllpErrors1Week": cucsComputePCIeFatalProtocolStatsDllpErrors1Week,
       "cucsComputePCIeFatalProtocolStatsDllpErrors1WeekH": cucsComputePCIeFatalProtocolStatsDllpErrors1WeekH,
       "cucsComputePCIeFatalProtocolStatsFlowControlErrors": cucsComputePCIeFatalProtocolStatsFlowControlErrors,
       "cucsComputePCIeFatalProtocolStatsFlowControlErrors15Min": cucsComputePCIeFatalProtocolStatsFlowControlErrors15Min,
       "cucsComputePCIeFatalProtocolStatsFlowControlErrors15MinH": cucsComputePCIeFatalProtocolStatsFlowControlErrors15MinH,
       "cucsComputePCIeFatalProtocolStatsFlowControlErrors1Day": cucsComputePCIeFatalProtocolStatsFlowControlErrors1Day,
       "cucsComputePCIeFatalProtocolStatsFlowControlErrors1DayH": cucsComputePCIeFatalProtocolStatsFlowControlErrors1DayH,
       "cucsComputePCIeFatalProtocolStatsFlowControlErrors1Hour": cucsComputePCIeFatalProtocolStatsFlowControlErrors1Hour,
       "cucsComputePCIeFatalProtocolStatsFlowControlErrors1HourH": cucsComputePCIeFatalProtocolStatsFlowControlErrors1HourH,
       "cucsComputePCIeFatalProtocolStatsFlowControlErrors1Week": cucsComputePCIeFatalProtocolStatsFlowControlErrors1Week,
       "cucsComputePCIeFatalProtocolStatsFlowControlErrors1WeekH": cucsComputePCIeFatalProtocolStatsFlowControlErrors1WeekH,
       "cucsComputePCIeFatalProtocolStatsIntervals": cucsComputePCIeFatalProtocolStatsIntervals,
       "cucsComputePCIeFatalProtocolStatsSuspect": cucsComputePCIeFatalProtocolStatsSuspect,
       "cucsComputePCIeFatalProtocolStatsThresholded": cucsComputePCIeFatalProtocolStatsThresholded,
       "cucsComputePCIeFatalProtocolStatsTimeCollected": cucsComputePCIeFatalProtocolStatsTimeCollected,
       "cucsComputePCIeFatalProtocolStatsUpdate": cucsComputePCIeFatalProtocolStatsUpdate,
       "cucsComputePCIeFatalProtocolStatsDllpErrors2Weeks": cucsComputePCIeFatalProtocolStatsDllpErrors2Weeks,
       "cucsComputePCIeFatalProtocolStatsDllpErrors2WeeksH": cucsComputePCIeFatalProtocolStatsDllpErrors2WeeksH,
       "cucsComputePCIeFatalProtocolStatsFlowControlErrors2Weeks": cucsComputePCIeFatalProtocolStatsFlowControlErrors2Weeks,
       "cucsComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH": cucsComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH,
       "cucsComputePCIeFatalReceiveStatsTable": cucsComputePCIeFatalReceiveStatsTable,
       "cucsComputePCIeFatalReceiveStatsEntry": cucsComputePCIeFatalReceiveStatsEntry,
       "cucsComputePCIeFatalReceiveStatsInstanceId": cucsComputePCIeFatalReceiveStatsInstanceId,
       "cucsComputePCIeFatalReceiveStatsDn": cucsComputePCIeFatalReceiveStatsDn,
       "cucsComputePCIeFatalReceiveStatsRn": cucsComputePCIeFatalReceiveStatsRn,
       "cucsComputePCIeFatalReceiveStatsBufferOverflowErrors": cucsComputePCIeFatalReceiveStatsBufferOverflowErrors,
       "cucsComputePCIeFatalReceiveStatsBufferOverflowErrors15Min": cucsComputePCIeFatalReceiveStatsBufferOverflowErrors15Min,
       "cucsComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH": cucsComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH,
       "cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Day": cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Day,
       "cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH": cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH,
       "cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour": cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour,
       "cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH": cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH,
       "cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Week": cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1Week,
       "cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH": cucsComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH,
       "cucsComputePCIeFatalReceiveStatsErrFatalErrors": cucsComputePCIeFatalReceiveStatsErrFatalErrors,
       "cucsComputePCIeFatalReceiveStatsErrFatalErrors15Min": cucsComputePCIeFatalReceiveStatsErrFatalErrors15Min,
       "cucsComputePCIeFatalReceiveStatsErrFatalErrors15MinH": cucsComputePCIeFatalReceiveStatsErrFatalErrors15MinH,
       "cucsComputePCIeFatalReceiveStatsErrFatalErrors1Day": cucsComputePCIeFatalReceiveStatsErrFatalErrors1Day,
       "cucsComputePCIeFatalReceiveStatsErrFatalErrors1DayH": cucsComputePCIeFatalReceiveStatsErrFatalErrors1DayH,
       "cucsComputePCIeFatalReceiveStatsErrFatalErrors1Hour": cucsComputePCIeFatalReceiveStatsErrFatalErrors1Hour,
       "cucsComputePCIeFatalReceiveStatsErrFatalErrors1HourH": cucsComputePCIeFatalReceiveStatsErrFatalErrors1HourH,
       "cucsComputePCIeFatalReceiveStatsErrFatalErrors1Week": cucsComputePCIeFatalReceiveStatsErrFatalErrors1Week,
       "cucsComputePCIeFatalReceiveStatsErrFatalErrors1WeekH": cucsComputePCIeFatalReceiveStatsErrFatalErrors1WeekH,
       "cucsComputePCIeFatalReceiveStatsErrNonFatalErrors": cucsComputePCIeFatalReceiveStatsErrNonFatalErrors,
       "cucsComputePCIeFatalReceiveStatsErrNonFatalErrors15Min": cucsComputePCIeFatalReceiveStatsErrNonFatalErrors15Min,
       "cucsComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH": cucsComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH,
       "cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Day": cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Day,
       "cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH": cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH,
       "cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour": cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour,
       "cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH": cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH,
       "cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Week": cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1Week,
       "cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH": cucsComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH,
       "cucsComputePCIeFatalReceiveStatsIntervals": cucsComputePCIeFatalReceiveStatsIntervals,
       "cucsComputePCIeFatalReceiveStatsSuspect": cucsComputePCIeFatalReceiveStatsSuspect,
       "cucsComputePCIeFatalReceiveStatsThresholded": cucsComputePCIeFatalReceiveStatsThresholded,
       "cucsComputePCIeFatalReceiveStatsTimeCollected": cucsComputePCIeFatalReceiveStatsTimeCollected,
       "cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors": cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors,
       "cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min": cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min,
       "cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH": cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH,
       "cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day": cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day,
       "cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH": cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH,
       "cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour": cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour,
       "cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH": cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH,
       "cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week": cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week,
       "cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH": cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH,
       "cucsComputePCIeFatalReceiveStatsUpdate": cucsComputePCIeFatalReceiveStatsUpdate,
       "cucsComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks": cucsComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks,
       "cucsComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH": cucsComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH,
       "cucsComputePCIeFatalReceiveStatsErrFatalErrors2Weeks": cucsComputePCIeFatalReceiveStatsErrFatalErrors2Weeks,
       "cucsComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH": cucsComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH,
       "cucsComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks": cucsComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks,
       "cucsComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH": cucsComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH,
       "cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks": cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks,
       "cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH": cucsComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH,
       "cucsComputePCIeFatalStatsTable": cucsComputePCIeFatalStatsTable,
       "cucsComputePCIeFatalStatsEntry": cucsComputePCIeFatalStatsEntry,
       "cucsComputePCIeFatalStatsInstanceId": cucsComputePCIeFatalStatsInstanceId,
       "cucsComputePCIeFatalStatsDn": cucsComputePCIeFatalStatsDn,
       "cucsComputePCIeFatalStatsRn": cucsComputePCIeFatalStatsRn,
       "cucsComputePCIeFatalStatsAcsViolationErrors": cucsComputePCIeFatalStatsAcsViolationErrors,
       "cucsComputePCIeFatalStatsAcsViolationErrors15Min": cucsComputePCIeFatalStatsAcsViolationErrors15Min,
       "cucsComputePCIeFatalStatsAcsViolationErrors15MinH": cucsComputePCIeFatalStatsAcsViolationErrors15MinH,
       "cucsComputePCIeFatalStatsAcsViolationErrors1Day": cucsComputePCIeFatalStatsAcsViolationErrors1Day,
       "cucsComputePCIeFatalStatsAcsViolationErrors1DayH": cucsComputePCIeFatalStatsAcsViolationErrors1DayH,
       "cucsComputePCIeFatalStatsAcsViolationErrors1Hour": cucsComputePCIeFatalStatsAcsViolationErrors1Hour,
       "cucsComputePCIeFatalStatsAcsViolationErrors1HourH": cucsComputePCIeFatalStatsAcsViolationErrors1HourH,
       "cucsComputePCIeFatalStatsAcsViolationErrors1Week": cucsComputePCIeFatalStatsAcsViolationErrors1Week,
       "cucsComputePCIeFatalStatsAcsViolationErrors1WeekH": cucsComputePCIeFatalStatsAcsViolationErrors1WeekH,
       "cucsComputePCIeFatalStatsIntervals": cucsComputePCIeFatalStatsIntervals,
       "cucsComputePCIeFatalStatsMalformedTLPErrors": cucsComputePCIeFatalStatsMalformedTLPErrors,
       "cucsComputePCIeFatalStatsMalformedTLPErrors15Min": cucsComputePCIeFatalStatsMalformedTLPErrors15Min,
       "cucsComputePCIeFatalStatsMalformedTLPErrors15MinH": cucsComputePCIeFatalStatsMalformedTLPErrors15MinH,
       "cucsComputePCIeFatalStatsMalformedTLPErrors1Day": cucsComputePCIeFatalStatsMalformedTLPErrors1Day,
       "cucsComputePCIeFatalStatsMalformedTLPErrors1DayH": cucsComputePCIeFatalStatsMalformedTLPErrors1DayH,
       "cucsComputePCIeFatalStatsMalformedTLPErrors1Hour": cucsComputePCIeFatalStatsMalformedTLPErrors1Hour,
       "cucsComputePCIeFatalStatsMalformedTLPErrors1HourH": cucsComputePCIeFatalStatsMalformedTLPErrors1HourH,
       "cucsComputePCIeFatalStatsMalformedTLPErrors1Week": cucsComputePCIeFatalStatsMalformedTLPErrors1Week,
       "cucsComputePCIeFatalStatsMalformedTLPErrors1WeekH": cucsComputePCIeFatalStatsMalformedTLPErrors1WeekH,
       "cucsComputePCIeFatalStatsPoisonedTLPErrors": cucsComputePCIeFatalStatsPoisonedTLPErrors,
       "cucsComputePCIeFatalStatsPoisonedTLPErrors15Min": cucsComputePCIeFatalStatsPoisonedTLPErrors15Min,
       "cucsComputePCIeFatalStatsPoisonedTLPErrors15MinH": cucsComputePCIeFatalStatsPoisonedTLPErrors15MinH,
       "cucsComputePCIeFatalStatsPoisonedTLPErrors1Day": cucsComputePCIeFatalStatsPoisonedTLPErrors1Day,
       "cucsComputePCIeFatalStatsPoisonedTLPErrors1DayH": cucsComputePCIeFatalStatsPoisonedTLPErrors1DayH,
       "cucsComputePCIeFatalStatsPoisonedTLPErrors1Hour": cucsComputePCIeFatalStatsPoisonedTLPErrors1Hour,
       "cucsComputePCIeFatalStatsPoisonedTLPErrors1HourH": cucsComputePCIeFatalStatsPoisonedTLPErrors1HourH,
       "cucsComputePCIeFatalStatsPoisonedTLPErrors1Week": cucsComputePCIeFatalStatsPoisonedTLPErrors1Week,
       "cucsComputePCIeFatalStatsPoisonedTLPErrors1WeekH": cucsComputePCIeFatalStatsPoisonedTLPErrors1WeekH,
       "cucsComputePCIeFatalStatsSurpriseLinkDownErrors": cucsComputePCIeFatalStatsSurpriseLinkDownErrors,
       "cucsComputePCIeFatalStatsSurpriseLinkDownErrors15Min": cucsComputePCIeFatalStatsSurpriseLinkDownErrors15Min,
       "cucsComputePCIeFatalStatsSurpriseLinkDownErrors15MinH": cucsComputePCIeFatalStatsSurpriseLinkDownErrors15MinH,
       "cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Day": cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Day,
       "cucsComputePCIeFatalStatsSurpriseLinkDownErrors1DayH": cucsComputePCIeFatalStatsSurpriseLinkDownErrors1DayH,
       "cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Hour": cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Hour,
       "cucsComputePCIeFatalStatsSurpriseLinkDownErrors1HourH": cucsComputePCIeFatalStatsSurpriseLinkDownErrors1HourH,
       "cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Week": cucsComputePCIeFatalStatsSurpriseLinkDownErrors1Week,
       "cucsComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH": cucsComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH,
       "cucsComputePCIeFatalStatsSuspect": cucsComputePCIeFatalStatsSuspect,
       "cucsComputePCIeFatalStatsThresholded": cucsComputePCIeFatalStatsThresholded,
       "cucsComputePCIeFatalStatsTimeCollected": cucsComputePCIeFatalStatsTimeCollected,
       "cucsComputePCIeFatalStatsUpdate": cucsComputePCIeFatalStatsUpdate,
       "cucsComputePCIeFatalStatsAcsViolationErrors2Weeks": cucsComputePCIeFatalStatsAcsViolationErrors2Weeks,
       "cucsComputePCIeFatalStatsAcsViolationErrors2WeeksH": cucsComputePCIeFatalStatsAcsViolationErrors2WeeksH,
       "cucsComputePCIeFatalStatsMalformedTLPErrors2Weeks": cucsComputePCIeFatalStatsMalformedTLPErrors2Weeks,
       "cucsComputePCIeFatalStatsMalformedTLPErrors2WeeksH": cucsComputePCIeFatalStatsMalformedTLPErrors2WeeksH,
       "cucsComputePCIeFatalStatsPoisonedTLPErrors2Weeks": cucsComputePCIeFatalStatsPoisonedTLPErrors2Weeks,
       "cucsComputePCIeFatalStatsPoisonedTLPErrors2WeeksH": cucsComputePCIeFatalStatsPoisonedTLPErrors2WeeksH,
       "cucsComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks": cucsComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks,
       "cucsComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH": cucsComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH,
       "cucsComputePciCapTable": cucsComputePciCapTable,
       "cucsComputePciCapEntry": cucsComputePciCapEntry,
       "cucsComputePciCapInstanceId": cucsComputePciCapInstanceId,
       "cucsComputePciCapDn": cucsComputePciCapDn,
       "cucsComputePciCapRn": cucsComputePciCapRn,
       "cucsComputePciCapNumOfPhysSlots": cucsComputePciCapNumOfPhysSlots,
       "cucsComputePciCapOrder": cucsComputePciCapOrder,
       "cucsComputePciCapStartsWith": cucsComputePciCapStartsWith,
       "cucsComputePciCapMaxBusIdPerSlot": cucsComputePciCapMaxBusIdPerSlot,
       "cucsComputePhysicalFsmTaskTable": cucsComputePhysicalFsmTaskTable,
       "cucsComputePhysicalFsmTaskEntry": cucsComputePhysicalFsmTaskEntry,
       "cucsComputePhysicalFsmTaskInstanceId": cucsComputePhysicalFsmTaskInstanceId,
       "cucsComputePhysicalFsmTaskDn": cucsComputePhysicalFsmTaskDn,
       "cucsComputePhysicalFsmTaskRn": cucsComputePhysicalFsmTaskRn,
       "cucsComputePhysicalFsmTaskCompletion": cucsComputePhysicalFsmTaskCompletion,
       "cucsComputePhysicalFsmTaskFlags": cucsComputePhysicalFsmTaskFlags,
       "cucsComputePhysicalFsmTaskItem": cucsComputePhysicalFsmTaskItem,
       "cucsComputePhysicalFsmTaskSeqId": cucsComputePhysicalFsmTaskSeqId,
       "cucsComputePhysicalQualTable": cucsComputePhysicalQualTable,
       "cucsComputePhysicalQualEntry": cucsComputePhysicalQualEntry,
       "cucsComputePhysicalQualInstanceId": cucsComputePhysicalQualInstanceId,
       "cucsComputePhysicalQualDn": cucsComputePhysicalQualDn,
       "cucsComputePhysicalQualRn": cucsComputePhysicalQualRn,
       "cucsComputePhysicalQualModel": cucsComputePhysicalQualModel,
       "cucsComputePhysicalQualPropAcl": cucsComputePhysicalQualPropAcl,
       "cucsComputePlatformTable": cucsComputePlatformTable,
       "cucsComputePlatformEntry": cucsComputePlatformEntry,
       "cucsComputePlatformInstanceId": cucsComputePlatformInstanceId,
       "cucsComputePlatformDn": cucsComputePlatformDn,
       "cucsComputePlatformRn": cucsComputePlatformRn,
       "cucsComputePlatformModel": cucsComputePlatformModel,
       "cucsComputePlatformRevision": cucsComputePlatformRevision,
       "cucsComputePlatformVendor": cucsComputePlatformVendor,
       "cucsComputePlatformProductName": cucsComputePlatformProductName,
       "cucsComputePlatformPropAcl": cucsComputePlatformPropAcl,
       "cucsComputePoolTable": cucsComputePoolTable,
       "cucsComputePoolEntry": cucsComputePoolEntry,
       "cucsComputePoolInstanceId": cucsComputePoolInstanceId,
       "cucsComputePoolDn": cucsComputePoolDn,
       "cucsComputePoolRn": cucsComputePoolRn,
       "cucsComputePoolAssigned": cucsComputePoolAssigned,
       "cucsComputePoolDescr": cucsComputePoolDescr,
       "cucsComputePoolIntId": cucsComputePoolIntId,
       "cucsComputePoolName": cucsComputePoolName,
       "cucsComputePoolSize": cucsComputePoolSize,
       "cucsComputePoolAssignmentOrder": cucsComputePoolAssignmentOrder,
       "cucsComputePoolPolicyLevel": cucsComputePoolPolicyLevel,
       "cucsComputePoolPolicyOwner": cucsComputePoolPolicyOwner,
       "cucsComputePoolableTable": cucsComputePoolableTable,
       "cucsComputePoolableEntry": cucsComputePoolableEntry,
       "cucsComputePoolableInstanceId": cucsComputePoolableInstanceId,
       "cucsComputePoolableDn": cucsComputePoolableDn,
       "cucsComputePoolableRn": cucsComputePoolableRn,
       "cucsComputePoolableId": cucsComputePoolableId,
       "cucsComputePoolablePoolDn": cucsComputePoolablePoolDn,
       "cucsComputePooledRackUnitTable": cucsComputePooledRackUnitTable,
       "cucsComputePooledRackUnitEntry": cucsComputePooledRackUnitEntry,
       "cucsComputePooledRackUnitInstanceId": cucsComputePooledRackUnitInstanceId,
       "cucsComputePooledRackUnitDn": cucsComputePooledRackUnitDn,
       "cucsComputePooledRackUnitRn": cucsComputePooledRackUnitRn,
       "cucsComputePooledRackUnitAssigned": cucsComputePooledRackUnitAssigned,
       "cucsComputePooledRackUnitAssignedToDn": cucsComputePooledRackUnitAssignedToDn,
       "cucsComputePooledRackUnitId": cucsComputePooledRackUnitId,
       "cucsComputePooledRackUnitOwner": cucsComputePooledRackUnitOwner,
       "cucsComputePooledRackUnitPoolableDn": cucsComputePooledRackUnitPoolableDn,
       "cucsComputePooledRackUnitPrevAssignedToDn": cucsComputePooledRackUnitPrevAssignedToDn,
       "cucsComputePooledSlotTable": cucsComputePooledSlotTable,
       "cucsComputePooledSlotEntry": cucsComputePooledSlotEntry,
       "cucsComputePooledSlotInstanceId": cucsComputePooledSlotInstanceId,
       "cucsComputePooledSlotDn": cucsComputePooledSlotDn,
       "cucsComputePooledSlotRn": cucsComputePooledSlotRn,
       "cucsComputePooledSlotAssigned": cucsComputePooledSlotAssigned,
       "cucsComputePooledSlotAssignedToDn": cucsComputePooledSlotAssignedToDn,
       "cucsComputePooledSlotChassisId": cucsComputePooledSlotChassisId,
       "cucsComputePooledSlotOwner": cucsComputePooledSlotOwner,
       "cucsComputePooledSlotPoolableDn": cucsComputePooledSlotPoolableDn,
       "cucsComputePooledSlotPrevAssignedToDn": cucsComputePooledSlotPrevAssignedToDn,
       "cucsComputePooledSlotSlotId": cucsComputePooledSlotSlotId,
       "cucsComputePoolingPolicyTable": cucsComputePoolingPolicyTable,
       "cucsComputePoolingPolicyEntry": cucsComputePoolingPolicyEntry,
       "cucsComputePoolingPolicyInstanceId": cucsComputePoolingPolicyInstanceId,
       "cucsComputePoolingPolicyDn": cucsComputePoolingPolicyDn,
       "cucsComputePoolingPolicyRn": cucsComputePoolingPolicyRn,
       "cucsComputePoolingPolicyDescr": cucsComputePoolingPolicyDescr,
       "cucsComputePoolingPolicyIntId": cucsComputePoolingPolicyIntId,
       "cucsComputePoolingPolicyName": cucsComputePoolingPolicyName,
       "cucsComputePoolingPolicyPoolDn": cucsComputePoolingPolicyPoolDn,
       "cucsComputePoolingPolicyQualifier": cucsComputePoolingPolicyQualifier,
       "cucsComputePoolingPolicyPolicyLevel": cucsComputePoolingPolicyPolicyLevel,
       "cucsComputePoolingPolicyPolicyOwner": cucsComputePoolingPolicyPolicyOwner,
       "cucsComputePsuControlTable": cucsComputePsuControlTable,
       "cucsComputePsuControlEntry": cucsComputePsuControlEntry,
       "cucsComputePsuControlInstanceId": cucsComputePsuControlInstanceId,
       "cucsComputePsuControlDn": cucsComputePsuControlDn,
       "cucsComputePsuControlRn": cucsComputePsuControlRn,
       "cucsComputePsuControlClusterState": cucsComputePsuControlClusterState,
       "cucsComputePsuControlDescr": cucsComputePsuControlDescr,
       "cucsComputePsuControlInputPowerState": cucsComputePsuControlInputPowerState,
       "cucsComputePsuControlIntId": cucsComputePsuControlIntId,
       "cucsComputePsuControlName": cucsComputePsuControlName,
       "cucsComputePsuControlOperQualifier": cucsComputePsuControlOperQualifier,
       "cucsComputePsuControlOperState": cucsComputePsuControlOperState,
       "cucsComputePsuControlOutputPowerState": cucsComputePsuControlOutputPowerState,
       "cucsComputePsuControlRedundancy": cucsComputePsuControlRedundancy,
       "cucsComputePsuControlPolicyLevel": cucsComputePsuControlPolicyLevel,
       "cucsComputePsuControlPolicyOwner": cucsComputePsuControlPolicyOwner,
       "cucsComputePsuPolicyTable": cucsComputePsuPolicyTable,
       "cucsComputePsuPolicyEntry": cucsComputePsuPolicyEntry,
       "cucsComputePsuPolicyInstanceId": cucsComputePsuPolicyInstanceId,
       "cucsComputePsuPolicyDn": cucsComputePsuPolicyDn,
       "cucsComputePsuPolicyRn": cucsComputePsuPolicyRn,
       "cucsComputePsuPolicyDescr": cucsComputePsuPolicyDescr,
       "cucsComputePsuPolicyIntId": cucsComputePsuPolicyIntId,
       "cucsComputePsuPolicyName": cucsComputePsuPolicyName,
       "cucsComputePsuPolicyRedundancy": cucsComputePsuPolicyRedundancy,
       "cucsComputePsuPolicyPolicyLevel": cucsComputePsuPolicyPolicyLevel,
       "cucsComputePsuPolicyPolicyOwner": cucsComputePsuPolicyPolicyOwner,
       "cucsComputeQualTable": cucsComputeQualTable,
       "cucsComputeQualEntry": cucsComputeQualEntry,
       "cucsComputeQualInstanceId": cucsComputeQualInstanceId,
       "cucsComputeQualDn": cucsComputeQualDn,
       "cucsComputeQualRn": cucsComputeQualRn,
       "cucsComputeQualDescr": cucsComputeQualDescr,
       "cucsComputeQualIntId": cucsComputeQualIntId,
       "cucsComputeQualName": cucsComputeQualName,
       "cucsComputeQualPolicyLevel": cucsComputeQualPolicyLevel,
       "cucsComputeQualPolicyOwner": cucsComputeQualPolicyOwner,
       "cucsComputeRackUnitTable": cucsComputeRackUnitTable,
       "cucsComputeRackUnitEntry": cucsComputeRackUnitEntry,
       "cucsComputeRackUnitInstanceId": cucsComputeRackUnitInstanceId,
       "cucsComputeRackUnitDn": cucsComputeRackUnitDn,
       "cucsComputeRackUnitRn": cucsComputeRackUnitRn,
       "cucsComputeRackUnitAdminPower": cucsComputeRackUnitAdminPower,
       "cucsComputeRackUnitAdminState": cucsComputeRackUnitAdminState,
       "cucsComputeRackUnitAssignedToDn": cucsComputeRackUnitAssignedToDn,
       "cucsComputeRackUnitAssociation": cucsComputeRackUnitAssociation,
       "cucsComputeRackUnitAvailability": cucsComputeRackUnitAvailability,
       "cucsComputeRackUnitAvailableMemory": cucsComputeRackUnitAvailableMemory,
       "cucsComputeRackUnitCheckPoint": cucsComputeRackUnitCheckPoint,
       "cucsComputeRackUnitConnPath": cucsComputeRackUnitConnPath,
       "cucsComputeRackUnitConnStatus": cucsComputeRackUnitConnStatus,
       "cucsComputeRackUnitDescr": cucsComputeRackUnitDescr,
       "cucsComputeRackUnitDiscovery": cucsComputeRackUnitDiscovery,
       "cucsComputeRackUnitFltAggr": cucsComputeRackUnitFltAggr,
       "cucsComputeRackUnitFsmDescr": cucsComputeRackUnitFsmDescr,
       "cucsComputeRackUnitFsmFlags": cucsComputeRackUnitFsmFlags,
       "cucsComputeRackUnitFsmPrev": cucsComputeRackUnitFsmPrev,
       "cucsComputeRackUnitFsmProgr": cucsComputeRackUnitFsmProgr,
       "cucsComputeRackUnitFsmRmtInvErrCode": cucsComputeRackUnitFsmRmtInvErrCode,
       "cucsComputeRackUnitFsmRmtInvErrDescr": cucsComputeRackUnitFsmRmtInvErrDescr,
       "cucsComputeRackUnitFsmRmtInvRslt": cucsComputeRackUnitFsmRmtInvRslt,
       "cucsComputeRackUnitFsmStageDescr": cucsComputeRackUnitFsmStageDescr,
       "cucsComputeRackUnitFsmStamp": cucsComputeRackUnitFsmStamp,
       "cucsComputeRackUnitFsmStatus": cucsComputeRackUnitFsmStatus,
       "cucsComputeRackUnitFsmTry": cucsComputeRackUnitFsmTry,
       "cucsComputeRackUnitId": cucsComputeRackUnitId,
       "cucsComputeRackUnitIntId": cucsComputeRackUnitIntId,
       "cucsComputeRackUnitLc": cucsComputeRackUnitLc,
       "cucsComputeRackUnitLcTs": cucsComputeRackUnitLcTs,
       "cucsComputeRackUnitManagingInst": cucsComputeRackUnitManagingInst,
       "cucsComputeRackUnitModel": cucsComputeRackUnitModel,
       "cucsComputeRackUnitName": cucsComputeRackUnitName,
       "cucsComputeRackUnitNumOfAdaptors": cucsComputeRackUnitNumOfAdaptors,
       "cucsComputeRackUnitNumOfCores": cucsComputeRackUnitNumOfCores,
       "cucsComputeRackUnitNumOfCpus": cucsComputeRackUnitNumOfCpus,
       "cucsComputeRackUnitNumOfEthHostIfs": cucsComputeRackUnitNumOfEthHostIfs,
       "cucsComputeRackUnitNumOfFcHostIfs": cucsComputeRackUnitNumOfFcHostIfs,
       "cucsComputeRackUnitNumOfThreads": cucsComputeRackUnitNumOfThreads,
       "cucsComputeRackUnitOperPower": cucsComputeRackUnitOperPower,
       "cucsComputeRackUnitOperQualifier": cucsComputeRackUnitOperQualifier,
       "cucsComputeRackUnitOperState": cucsComputeRackUnitOperState,
       "cucsComputeRackUnitOperability": cucsComputeRackUnitOperability,
       "cucsComputeRackUnitOriginalUuid": cucsComputeRackUnitOriginalUuid,
       "cucsComputeRackUnitPresence": cucsComputeRackUnitPresence,
       "cucsComputeRackUnitRevision": cucsComputeRackUnitRevision,
       "cucsComputeRackUnitSerial": cucsComputeRackUnitSerial,
       "cucsComputeRackUnitServerId": cucsComputeRackUnitServerId,
       "cucsComputeRackUnitTotalMemory": cucsComputeRackUnitTotalMemory,
       "cucsComputeRackUnitUuid": cucsComputeRackUnitUuid,
       "cucsComputeRackUnitVendor": cucsComputeRackUnitVendor,
       "cucsComputeRackUnitVersionHolder": cucsComputeRackUnitVersionHolder,
       "cucsComputeRackUnitNumOfCoresEnabled": cucsComputeRackUnitNumOfCoresEnabled,
       "cucsComputeRackUnitLowVoltageMemory": cucsComputeRackUnitLowVoltageMemory,
       "cucsComputeRackUnitMemorySpeed": cucsComputeRackUnitMemorySpeed,
       "cucsComputeRackUnitUsrLbl": cucsComputeRackUnitUsrLbl,
       "cucsComputeRackUnitMfgTime": cucsComputeRackUnitMfgTime,
       "cucsComputeRackUnitPartNumber": cucsComputeRackUnitPartNumber,
       "cucsComputeRackUnitVid": cucsComputeRackUnitVid,
       "cucsComputeRackUnitPolicyLevel": cucsComputeRackUnitPolicyLevel,
       "cucsComputeRackUnitPolicyOwner": cucsComputeRackUnitPolicyOwner,
       "cucsComputeRackUnitLocalId": cucsComputeRackUnitLocalId,
       "cucsComputeRackUnitOperPwrTransSrc": cucsComputeRackUnitOperPwrTransSrc,
       "cucsComputeRackUnitDiscoveryStatus": cucsComputeRackUnitDiscoveryStatus,
       "cucsComputeRackUnitNumOf40GAdaptorsWithOldFw": cucsComputeRackUnitNumOf40GAdaptorsWithOldFw,
       "cucsComputeRackUnitNumOf40GAdaptorsWithUnknownFw": cucsComputeRackUnitNumOf40GAdaptorsWithUnknownFw,
       "cucsComputeRackUnitFanSpeedConfigStatus": cucsComputeRackUnitFanSpeedConfigStatus,
       "cucsComputeRackUnitFanSpeedPolicyFault": cucsComputeRackUnitFanSpeedPolicyFault,
       "cucsComputeRackUnitFsmTaskTable": cucsComputeRackUnitFsmTaskTable,
       "cucsComputeRackUnitFsmTaskEntry": cucsComputeRackUnitFsmTaskEntry,
       "cucsComputeRackUnitFsmTaskInstanceId": cucsComputeRackUnitFsmTaskInstanceId,
       "cucsComputeRackUnitFsmTaskDn": cucsComputeRackUnitFsmTaskDn,
       "cucsComputeRackUnitFsmTaskRn": cucsComputeRackUnitFsmTaskRn,
       "cucsComputeRackUnitFsmTaskCompletion": cucsComputeRackUnitFsmTaskCompletion,
       "cucsComputeRackUnitFsmTaskFlags": cucsComputeRackUnitFsmTaskFlags,
       "cucsComputeRackUnitFsmTaskItem": cucsComputeRackUnitFsmTaskItem,
       "cucsComputeRackUnitFsmTaskSeqId": cucsComputeRackUnitFsmTaskSeqId,
       "cucsComputeRtcBatteryTable": cucsComputeRtcBatteryTable,
       "cucsComputeRtcBatteryEntry": cucsComputeRtcBatteryEntry,
       "cucsComputeRtcBatteryInstanceId": cucsComputeRtcBatteryInstanceId,
       "cucsComputeRtcBatteryDn": cucsComputeRtcBatteryDn,
       "cucsComputeRtcBatteryRn": cucsComputeRtcBatteryRn,
       "cucsComputeRtcBatteryId": cucsComputeRtcBatteryId,
       "cucsComputeRtcBatteryModel": cucsComputeRtcBatteryModel,
       "cucsComputeRtcBatteryOperState": cucsComputeRtcBatteryOperState,
       "cucsComputeRtcBatteryOperability": cucsComputeRtcBatteryOperability,
       "cucsComputeRtcBatteryPerf": cucsComputeRtcBatteryPerf,
       "cucsComputeRtcBatteryPower": cucsComputeRtcBatteryPower,
       "cucsComputeRtcBatteryPresence": cucsComputeRtcBatteryPresence,
       "cucsComputeRtcBatteryRevision": cucsComputeRtcBatteryRevision,
       "cucsComputeRtcBatterySerial": cucsComputeRtcBatterySerial,
       "cucsComputeRtcBatteryThermal": cucsComputeRtcBatteryThermal,
       "cucsComputeRtcBatteryVendor": cucsComputeRtcBatteryVendor,
       "cucsComputeRtcBatteryVoltage": cucsComputeRtcBatteryVoltage,
       "cucsComputeRtcBatteryOperQualifierReason": cucsComputeRtcBatteryOperQualifierReason,
       "cucsComputeRtcBatteryLocationDn": cucsComputeRtcBatteryLocationDn,
       "cucsComputeScrubPolicyTable": cucsComputeScrubPolicyTable,
       "cucsComputeScrubPolicyEntry": cucsComputeScrubPolicyEntry,
       "cucsComputeScrubPolicyInstanceId": cucsComputeScrubPolicyInstanceId,
       "cucsComputeScrubPolicyDn": cucsComputeScrubPolicyDn,
       "cucsComputeScrubPolicyRn": cucsComputeScrubPolicyRn,
       "cucsComputeScrubPolicyBiosSettingsScrub": cucsComputeScrubPolicyBiosSettingsScrub,
       "cucsComputeScrubPolicyDescr": cucsComputeScrubPolicyDescr,
       "cucsComputeScrubPolicyDiskScrub": cucsComputeScrubPolicyDiskScrub,
       "cucsComputeScrubPolicyIntId": cucsComputeScrubPolicyIntId,
       "cucsComputeScrubPolicyName": cucsComputeScrubPolicyName,
       "cucsComputeScrubPolicyPolicyLevel": cucsComputeScrubPolicyPolicyLevel,
       "cucsComputeScrubPolicyPolicyOwner": cucsComputeScrubPolicyPolicyOwner,
       "cucsComputeScrubPolicyFlexFlashScrub": cucsComputeScrubPolicyFlexFlashScrub,
       "cucsComputeServerDiscPolicyTable": cucsComputeServerDiscPolicyTable,
       "cucsComputeServerDiscPolicyEntry": cucsComputeServerDiscPolicyEntry,
       "cucsComputeServerDiscPolicyInstanceId": cucsComputeServerDiscPolicyInstanceId,
       "cucsComputeServerDiscPolicyDn": cucsComputeServerDiscPolicyDn,
       "cucsComputeServerDiscPolicyRn": cucsComputeServerDiscPolicyRn,
       "cucsComputeServerDiscPolicyAction": cucsComputeServerDiscPolicyAction,
       "cucsComputeServerDiscPolicyDescr": cucsComputeServerDiscPolicyDescr,
       "cucsComputeServerDiscPolicyIntId": cucsComputeServerDiscPolicyIntId,
       "cucsComputeServerDiscPolicyName": cucsComputeServerDiscPolicyName,
       "cucsComputeServerDiscPolicyQualifier": cucsComputeServerDiscPolicyQualifier,
       "cucsComputeServerDiscPolicyScrubPolicyName": cucsComputeServerDiscPolicyScrubPolicyName,
       "cucsComputeServerDiscPolicyFsmDescr": cucsComputeServerDiscPolicyFsmDescr,
       "cucsComputeServerDiscPolicyFsmPrev": cucsComputeServerDiscPolicyFsmPrev,
       "cucsComputeServerDiscPolicyFsmProgr": cucsComputeServerDiscPolicyFsmProgr,
       "cucsComputeServerDiscPolicyFsmRmtInvErrCode": cucsComputeServerDiscPolicyFsmRmtInvErrCode,
       "cucsComputeServerDiscPolicyFsmRmtInvErrDescr": cucsComputeServerDiscPolicyFsmRmtInvErrDescr,
       "cucsComputeServerDiscPolicyFsmRmtInvRslt": cucsComputeServerDiscPolicyFsmRmtInvRslt,
       "cucsComputeServerDiscPolicyFsmStageDescr": cucsComputeServerDiscPolicyFsmStageDescr,
       "cucsComputeServerDiscPolicyFsmStamp": cucsComputeServerDiscPolicyFsmStamp,
       "cucsComputeServerDiscPolicyFsmStatus": cucsComputeServerDiscPolicyFsmStatus,
       "cucsComputeServerDiscPolicyFsmTry": cucsComputeServerDiscPolicyFsmTry,
       "cucsComputeServerDiscPolicyPolicyLevel": cucsComputeServerDiscPolicyPolicyLevel,
       "cucsComputeServerDiscPolicyPolicyOwner": cucsComputeServerDiscPolicyPolicyOwner,
       "cucsComputeSlotQualTable": cucsComputeSlotQualTable,
       "cucsComputeSlotQualEntry": cucsComputeSlotQualEntry,
       "cucsComputeSlotQualInstanceId": cucsComputeSlotQualInstanceId,
       "cucsComputeSlotQualDn": cucsComputeSlotQualDn,
       "cucsComputeSlotQualRn": cucsComputeSlotQualRn,
       "cucsComputeSlotQualMaxId": cucsComputeSlotQualMaxId,
       "cucsComputeSlotQualMinId": cucsComputeSlotQualMinId,
       "cucsComputePhysicalAssocCtxTable": cucsComputePhysicalAssocCtxTable,
       "cucsComputePhysicalAssocCtxEntry": cucsComputePhysicalAssocCtxEntry,
       "cucsComputePhysicalAssocCtxInstanceId": cucsComputePhysicalAssocCtxInstanceId,
       "cucsComputePhysicalAssocCtxDn": cucsComputePhysicalAssocCtxDn,
       "cucsComputePhysicalAssocCtxRn": cucsComputePhysicalAssocCtxRn,
       "cucsComputePhysicalAssocCtxFruCapDn": cucsComputePhysicalAssocCtxFruCapDn,
       "cucsComputePoolPolicyRefTable": cucsComputePoolPolicyRefTable,
       "cucsComputePoolPolicyRefEntry": cucsComputePoolPolicyRefEntry,
       "cucsComputePoolPolicyRefInstanceId": cucsComputePoolPolicyRefInstanceId,
       "cucsComputePoolPolicyRefDn": cucsComputePoolPolicyRefDn,
       "cucsComputePoolPolicyRefRn": cucsComputePoolPolicyRefRn,
       "cucsComputePoolPolicyRefId": cucsComputePoolPolicyRefId,
       "cucsComputePoolPolicyRefPolicyDn": cucsComputePoolPolicyRefPolicyDn,
       "cucsComputeRackQualTable": cucsComputeRackQualTable,
       "cucsComputeRackQualEntry": cucsComputeRackQualEntry,
       "cucsComputeRackQualInstanceId": cucsComputeRackQualInstanceId,
       "cucsComputeRackQualDn": cucsComputeRackQualDn,
       "cucsComputeRackQualRn": cucsComputeRackQualRn,
       "cucsComputeRackQualMaxId": cucsComputeRackQualMaxId,
       "cucsComputeRackQualMinId": cucsComputeRackQualMinId,
       "cucsComputeRackUnitMbTempStatsTable": cucsComputeRackUnitMbTempStatsTable,
       "cucsComputeRackUnitMbTempStatsEntry": cucsComputeRackUnitMbTempStatsEntry,
       "cucsComputeRackUnitMbTempStatsInstanceId": cucsComputeRackUnitMbTempStatsInstanceId,
       "cucsComputeRackUnitMbTempStatsDn": cucsComputeRackUnitMbTempStatsDn,
       "cucsComputeRackUnitMbTempStatsRn": cucsComputeRackUnitMbTempStatsRn,
       "cucsComputeRackUnitMbTempStatsAmbientTemp": cucsComputeRackUnitMbTempStatsAmbientTemp,
       "cucsComputeRackUnitMbTempStatsAmbientTempAvg": cucsComputeRackUnitMbTempStatsAmbientTempAvg,
       "cucsComputeRackUnitMbTempStatsAmbientTempMax": cucsComputeRackUnitMbTempStatsAmbientTempMax,
       "cucsComputeRackUnitMbTempStatsAmbientTempMin": cucsComputeRackUnitMbTempStatsAmbientTempMin,
       "cucsComputeRackUnitMbTempStatsFrontTemp": cucsComputeRackUnitMbTempStatsFrontTemp,
       "cucsComputeRackUnitMbTempStatsFrontTempAvg": cucsComputeRackUnitMbTempStatsFrontTempAvg,
       "cucsComputeRackUnitMbTempStatsFrontTempMax": cucsComputeRackUnitMbTempStatsFrontTempMax,
       "cucsComputeRackUnitMbTempStatsFrontTempMin": cucsComputeRackUnitMbTempStatsFrontTempMin,
       "cucsComputeRackUnitMbTempStatsIntervals": cucsComputeRackUnitMbTempStatsIntervals,
       "cucsComputeRackUnitMbTempStatsIoh1Temp": cucsComputeRackUnitMbTempStatsIoh1Temp,
       "cucsComputeRackUnitMbTempStatsIoh1TempAvg": cucsComputeRackUnitMbTempStatsIoh1TempAvg,
       "cucsComputeRackUnitMbTempStatsIoh1TempMax": cucsComputeRackUnitMbTempStatsIoh1TempMax,
       "cucsComputeRackUnitMbTempStatsIoh1TempMin": cucsComputeRackUnitMbTempStatsIoh1TempMin,
       "cucsComputeRackUnitMbTempStatsIoh2Temp": cucsComputeRackUnitMbTempStatsIoh2Temp,
       "cucsComputeRackUnitMbTempStatsIoh2TempAvg": cucsComputeRackUnitMbTempStatsIoh2TempAvg,
       "cucsComputeRackUnitMbTempStatsIoh2TempMax": cucsComputeRackUnitMbTempStatsIoh2TempMax,
       "cucsComputeRackUnitMbTempStatsIoh2TempMin": cucsComputeRackUnitMbTempStatsIoh2TempMin,
       "cucsComputeRackUnitMbTempStatsRearTemp": cucsComputeRackUnitMbTempStatsRearTemp,
       "cucsComputeRackUnitMbTempStatsRearTempAvg": cucsComputeRackUnitMbTempStatsRearTempAvg,
       "cucsComputeRackUnitMbTempStatsRearTempMax": cucsComputeRackUnitMbTempStatsRearTempMax,
       "cucsComputeRackUnitMbTempStatsRearTempMin": cucsComputeRackUnitMbTempStatsRearTempMin,
       "cucsComputeRackUnitMbTempStatsSuspect": cucsComputeRackUnitMbTempStatsSuspect,
       "cucsComputeRackUnitMbTempStatsThresholded": cucsComputeRackUnitMbTempStatsThresholded,
       "cucsComputeRackUnitMbTempStatsTimeCollected": cucsComputeRackUnitMbTempStatsTimeCollected,
       "cucsComputeRackUnitMbTempStatsUpdate": cucsComputeRackUnitMbTempStatsUpdate,
       "cucsComputeRackUnitMbTempStatsHistTable": cucsComputeRackUnitMbTempStatsHistTable,
       "cucsComputeRackUnitMbTempStatsHistEntry": cucsComputeRackUnitMbTempStatsHistEntry,
       "cucsComputeRackUnitMbTempStatsHistInstanceId": cucsComputeRackUnitMbTempStatsHistInstanceId,
       "cucsComputeRackUnitMbTempStatsHistDn": cucsComputeRackUnitMbTempStatsHistDn,
       "cucsComputeRackUnitMbTempStatsHistRn": cucsComputeRackUnitMbTempStatsHistRn,
       "cucsComputeRackUnitMbTempStatsHistAmbientTemp": cucsComputeRackUnitMbTempStatsHistAmbientTemp,
       "cucsComputeRackUnitMbTempStatsHistAmbientTempAvg": cucsComputeRackUnitMbTempStatsHistAmbientTempAvg,
       "cucsComputeRackUnitMbTempStatsHistAmbientTempMax": cucsComputeRackUnitMbTempStatsHistAmbientTempMax,
       "cucsComputeRackUnitMbTempStatsHistAmbientTempMin": cucsComputeRackUnitMbTempStatsHistAmbientTempMin,
       "cucsComputeRackUnitMbTempStatsHistFrontTemp": cucsComputeRackUnitMbTempStatsHistFrontTemp,
       "cucsComputeRackUnitMbTempStatsHistFrontTempAvg": cucsComputeRackUnitMbTempStatsHistFrontTempAvg,
       "cucsComputeRackUnitMbTempStatsHistFrontTempMax": cucsComputeRackUnitMbTempStatsHistFrontTempMax,
       "cucsComputeRackUnitMbTempStatsHistFrontTempMin": cucsComputeRackUnitMbTempStatsHistFrontTempMin,
       "cucsComputeRackUnitMbTempStatsHistId": cucsComputeRackUnitMbTempStatsHistId,
       "cucsComputeRackUnitMbTempStatsHistIoh1Temp": cucsComputeRackUnitMbTempStatsHistIoh1Temp,
       "cucsComputeRackUnitMbTempStatsHistIoh1TempAvg": cucsComputeRackUnitMbTempStatsHistIoh1TempAvg,
       "cucsComputeRackUnitMbTempStatsHistIoh1TempMax": cucsComputeRackUnitMbTempStatsHistIoh1TempMax,
       "cucsComputeRackUnitMbTempStatsHistIoh1TempMin": cucsComputeRackUnitMbTempStatsHistIoh1TempMin,
       "cucsComputeRackUnitMbTempStatsHistIoh2Temp": cucsComputeRackUnitMbTempStatsHistIoh2Temp,
       "cucsComputeRackUnitMbTempStatsHistIoh2TempAvg": cucsComputeRackUnitMbTempStatsHistIoh2TempAvg,
       "cucsComputeRackUnitMbTempStatsHistIoh2TempMax": cucsComputeRackUnitMbTempStatsHistIoh2TempMax,
       "cucsComputeRackUnitMbTempStatsHistIoh2TempMin": cucsComputeRackUnitMbTempStatsHistIoh2TempMin,
       "cucsComputeRackUnitMbTempStatsHistMostRecent": cucsComputeRackUnitMbTempStatsHistMostRecent,
       "cucsComputeRackUnitMbTempStatsHistRearTemp": cucsComputeRackUnitMbTempStatsHistRearTemp,
       "cucsComputeRackUnitMbTempStatsHistRearTempAvg": cucsComputeRackUnitMbTempStatsHistRearTempAvg,
       "cucsComputeRackUnitMbTempStatsHistRearTempMax": cucsComputeRackUnitMbTempStatsHistRearTempMax,
       "cucsComputeRackUnitMbTempStatsHistRearTempMin": cucsComputeRackUnitMbTempStatsHistRearTempMin,
       "cucsComputeRackUnitMbTempStatsHistSuspect": cucsComputeRackUnitMbTempStatsHistSuspect,
       "cucsComputeRackUnitMbTempStatsHistThresholded": cucsComputeRackUnitMbTempStatsHistThresholded,
       "cucsComputeRackUnitMbTempStatsHistTimeCollected": cucsComputeRackUnitMbTempStatsHistTimeCollected,
       "cucsComputeChassisConnPolicyTable": cucsComputeChassisConnPolicyTable,
       "cucsComputeChassisConnPolicyEntry": cucsComputeChassisConnPolicyEntry,
       "cucsComputeChassisConnPolicyInstanceId": cucsComputeChassisConnPolicyInstanceId,
       "cucsComputeChassisConnPolicyDn": cucsComputeChassisConnPolicyDn,
       "cucsComputeChassisConnPolicyRn": cucsComputeChassisConnPolicyRn,
       "cucsComputeChassisConnPolicyAdminState": cucsComputeChassisConnPolicyAdminState,
       "cucsComputeChassisConnPolicyChassisId": cucsComputeChassisConnPolicyChassisId,
       "cucsComputeChassisConnPolicyDescr": cucsComputeChassisConnPolicyDescr,
       "cucsComputeChassisConnPolicyIntId": cucsComputeChassisConnPolicyIntId,
       "cucsComputeChassisConnPolicyName": cucsComputeChassisConnPolicyName,
       "cucsComputeChassisConnPolicyQualifier": cucsComputeChassisConnPolicyQualifier,
       "cucsComputeChassisConnPolicySwitchId": cucsComputeChassisConnPolicySwitchId,
       "cucsComputeChassisConnPolicyPolicyLevel": cucsComputeChassisConnPolicyPolicyLevel,
       "cucsComputeChassisConnPolicyPolicyOwner": cucsComputeChassisConnPolicyPolicyOwner,
       "cucsComputePnuOSImageTable": cucsComputePnuOSImageTable,
       "cucsComputePnuOSImageEntry": cucsComputePnuOSImageEntry,
       "cucsComputePnuOSImageInstanceId": cucsComputePnuOSImageInstanceId,
       "cucsComputePnuOSImageDn": cucsComputePnuOSImageDn,
       "cucsComputePnuOSImageRn": cucsComputePnuOSImageRn,
       "cucsComputePnuOSImageImgLoc": cucsComputePnuOSImageImgLoc,
       "cucsComputePnuOSImageImgName": cucsComputePnuOSImageImgName,
       "cucsComputeBladeFsmTable": cucsComputeBladeFsmTable,
       "cucsComputeBladeFsmEntry": cucsComputeBladeFsmEntry,
       "cucsComputeBladeFsmInstanceId": cucsComputeBladeFsmInstanceId,
       "cucsComputeBladeFsmDn": cucsComputeBladeFsmDn,
       "cucsComputeBladeFsmRn": cucsComputeBladeFsmRn,
       "cucsComputeBladeFsmCompletionTime": cucsComputeBladeFsmCompletionTime,
       "cucsComputeBladeFsmCurrentFsm": cucsComputeBladeFsmCurrentFsm,
       "cucsComputeBladeFsmDescrData": cucsComputeBladeFsmDescrData,
       "cucsComputeBladeFsmFsmStatus": cucsComputeBladeFsmFsmStatus,
       "cucsComputeBladeFsmProgress": cucsComputeBladeFsmProgress,
       "cucsComputeBladeFsmRmtErrCode": cucsComputeBladeFsmRmtErrCode,
       "cucsComputeBladeFsmRmtErrDescr": cucsComputeBladeFsmRmtErrDescr,
       "cucsComputeBladeFsmRmtRslt": cucsComputeBladeFsmRmtRslt,
       "cucsComputeBladeFsmStageTable": cucsComputeBladeFsmStageTable,
       "cucsComputeBladeFsmStageEntry": cucsComputeBladeFsmStageEntry,
       "cucsComputeBladeFsmStageInstanceId": cucsComputeBladeFsmStageInstanceId,
       "cucsComputeBladeFsmStageDn": cucsComputeBladeFsmStageDn,
       "cucsComputeBladeFsmStageRn": cucsComputeBladeFsmStageRn,
       "cucsComputeBladeFsmStageDescrData": cucsComputeBladeFsmStageDescrData,
       "cucsComputeBladeFsmStageLastUpdateTime": cucsComputeBladeFsmStageLastUpdateTime,
       "cucsComputeBladeFsmStageName": cucsComputeBladeFsmStageName,
       "cucsComputeBladeFsmStageOrder": cucsComputeBladeFsmStageOrder,
       "cucsComputeBladeFsmStageRetry": cucsComputeBladeFsmStageRetry,
       "cucsComputeBladeFsmStageStageStatus": cucsComputeBladeFsmStageStageStatus,
       "cucsComputePhysicalFsmTable": cucsComputePhysicalFsmTable,
       "cucsComputePhysicalFsmEntry": cucsComputePhysicalFsmEntry,
       "cucsComputePhysicalFsmInstanceId": cucsComputePhysicalFsmInstanceId,
       "cucsComputePhysicalFsmDn": cucsComputePhysicalFsmDn,
       "cucsComputePhysicalFsmRn": cucsComputePhysicalFsmRn,
       "cucsComputePhysicalFsmCompletionTime": cucsComputePhysicalFsmCompletionTime,
       "cucsComputePhysicalFsmCurrentFsm": cucsComputePhysicalFsmCurrentFsm,
       "cucsComputePhysicalFsmDescr": cucsComputePhysicalFsmDescr,
       "cucsComputePhysicalFsmFsmStatus": cucsComputePhysicalFsmFsmStatus,
       "cucsComputePhysicalFsmProgress": cucsComputePhysicalFsmProgress,
       "cucsComputePhysicalFsmRmtErrCode": cucsComputePhysicalFsmRmtErrCode,
       "cucsComputePhysicalFsmRmtErrDescr": cucsComputePhysicalFsmRmtErrDescr,
       "cucsComputePhysicalFsmRmtRslt": cucsComputePhysicalFsmRmtRslt,
       "cucsComputePhysicalFsmStageTable": cucsComputePhysicalFsmStageTable,
       "cucsComputePhysicalFsmStageEntry": cucsComputePhysicalFsmStageEntry,
       "cucsComputePhysicalFsmStageInstanceId": cucsComputePhysicalFsmStageInstanceId,
       "cucsComputePhysicalFsmStageDn": cucsComputePhysicalFsmStageDn,
       "cucsComputePhysicalFsmStageRn": cucsComputePhysicalFsmStageRn,
       "cucsComputePhysicalFsmStageDescr": cucsComputePhysicalFsmStageDescr,
       "cucsComputePhysicalFsmStageLastUpdateTime": cucsComputePhysicalFsmStageLastUpdateTime,
       "cucsComputePhysicalFsmStageName": cucsComputePhysicalFsmStageName,
       "cucsComputePhysicalFsmStageOrder": cucsComputePhysicalFsmStageOrder,
       "cucsComputePhysicalFsmStageRetry": cucsComputePhysicalFsmStageRetry,
       "cucsComputePhysicalFsmStageStageStatus": cucsComputePhysicalFsmStageStageStatus,
       "cucsComputeRackUnitFsmTable": cucsComputeRackUnitFsmTable,
       "cucsComputeRackUnitFsmEntry": cucsComputeRackUnitFsmEntry,
       "cucsComputeRackUnitFsmInstanceId": cucsComputeRackUnitFsmInstanceId,
       "cucsComputeRackUnitFsmDn": cucsComputeRackUnitFsmDn,
       "cucsComputeRackUnitFsmRn": cucsComputeRackUnitFsmRn,
       "cucsComputeRackUnitFsmCompletionTime": cucsComputeRackUnitFsmCompletionTime,
       "cucsComputeRackUnitFsmCurrentFsm": cucsComputeRackUnitFsmCurrentFsm,
       "cucsComputeRackUnitFsmDescrData": cucsComputeRackUnitFsmDescrData,
       "cucsComputeRackUnitFsmFsmStatus": cucsComputeRackUnitFsmFsmStatus,
       "cucsComputeRackUnitFsmProgress": cucsComputeRackUnitFsmProgress,
       "cucsComputeRackUnitFsmRmtErrCode": cucsComputeRackUnitFsmRmtErrCode,
       "cucsComputeRackUnitFsmRmtErrDescr": cucsComputeRackUnitFsmRmtErrDescr,
       "cucsComputeRackUnitFsmRmtRslt": cucsComputeRackUnitFsmRmtRslt,
       "cucsComputeRackUnitFsmStageTable": cucsComputeRackUnitFsmStageTable,
       "cucsComputeRackUnitFsmStageEntry": cucsComputeRackUnitFsmStageEntry,
       "cucsComputeRackUnitFsmStageInstanceId": cucsComputeRackUnitFsmStageInstanceId,
       "cucsComputeRackUnitFsmStageDn": cucsComputeRackUnitFsmStageDn,
       "cucsComputeRackUnitFsmStageRn": cucsComputeRackUnitFsmStageRn,
       "cucsComputeRackUnitFsmStageDescrData": cucsComputeRackUnitFsmStageDescrData,
       "cucsComputeRackUnitFsmStageLastUpdateTime": cucsComputeRackUnitFsmStageLastUpdateTime,
       "cucsComputeRackUnitFsmStageName": cucsComputeRackUnitFsmStageName,
       "cucsComputeRackUnitFsmStageOrder": cucsComputeRackUnitFsmStageOrder,
       "cucsComputeRackUnitFsmStageRetry": cucsComputeRackUnitFsmStageRetry,
       "cucsComputeRackUnitFsmStageStageStatus": cucsComputeRackUnitFsmStageStageStatus,
       "cucsComputeServerDiscPolicyFsmTable": cucsComputeServerDiscPolicyFsmTable,
       "cucsComputeServerDiscPolicyFsmEntry": cucsComputeServerDiscPolicyFsmEntry,
       "cucsComputeServerDiscPolicyFsmInstanceId": cucsComputeServerDiscPolicyFsmInstanceId,
       "cucsComputeServerDiscPolicyFsmDn": cucsComputeServerDiscPolicyFsmDn,
       "cucsComputeServerDiscPolicyFsmRn": cucsComputeServerDiscPolicyFsmRn,
       "cucsComputeServerDiscPolicyFsmCompletionTime": cucsComputeServerDiscPolicyFsmCompletionTime,
       "cucsComputeServerDiscPolicyFsmCurrentFsm": cucsComputeServerDiscPolicyFsmCurrentFsm,
       "cucsComputeServerDiscPolicyFsmDescrData": cucsComputeServerDiscPolicyFsmDescrData,
       "cucsComputeServerDiscPolicyFsmFsmStatus": cucsComputeServerDiscPolicyFsmFsmStatus,
       "cucsComputeServerDiscPolicyFsmProgress": cucsComputeServerDiscPolicyFsmProgress,
       "cucsComputeServerDiscPolicyFsmRmtErrCode": cucsComputeServerDiscPolicyFsmRmtErrCode,
       "cucsComputeServerDiscPolicyFsmRmtErrDescr": cucsComputeServerDiscPolicyFsmRmtErrDescr,
       "cucsComputeServerDiscPolicyFsmRmtRslt": cucsComputeServerDiscPolicyFsmRmtRslt,
       "cucsComputeServerDiscPolicyFsmStageTable": cucsComputeServerDiscPolicyFsmStageTable,
       "cucsComputeServerDiscPolicyFsmStageEntry": cucsComputeServerDiscPolicyFsmStageEntry,
       "cucsComputeServerDiscPolicyFsmStageInstanceId": cucsComputeServerDiscPolicyFsmStageInstanceId,
       "cucsComputeServerDiscPolicyFsmStageDn": cucsComputeServerDiscPolicyFsmStageDn,
       "cucsComputeServerDiscPolicyFsmStageRn": cucsComputeServerDiscPolicyFsmStageRn,
       "cucsComputeServerDiscPolicyFsmStageDescrData": cucsComputeServerDiscPolicyFsmStageDescrData,
       "cucsComputeServerDiscPolicyFsmStageLastUpdateTime": cucsComputeServerDiscPolicyFsmStageLastUpdateTime,
       "cucsComputeServerDiscPolicyFsmStageName": cucsComputeServerDiscPolicyFsmStageName,
       "cucsComputeServerDiscPolicyFsmStageOrder": cucsComputeServerDiscPolicyFsmStageOrder,
       "cucsComputeServerDiscPolicyFsmStageRetry": cucsComputeServerDiscPolicyFsmStageRetry,
       "cucsComputeServerDiscPolicyFsmStageStageStatus": cucsComputeServerDiscPolicyFsmStageStageStatus,
       "cucsComputeServerDiscPolicyFsmTaskTable": cucsComputeServerDiscPolicyFsmTaskTable,
       "cucsComputeServerDiscPolicyFsmTaskEntry": cucsComputeServerDiscPolicyFsmTaskEntry,
       "cucsComputeServerDiscPolicyFsmTaskInstanceId": cucsComputeServerDiscPolicyFsmTaskInstanceId,
       "cucsComputeServerDiscPolicyFsmTaskDn": cucsComputeServerDiscPolicyFsmTaskDn,
       "cucsComputeServerDiscPolicyFsmTaskRn": cucsComputeServerDiscPolicyFsmTaskRn,
       "cucsComputeServerDiscPolicyFsmTaskCompletion": cucsComputeServerDiscPolicyFsmTaskCompletion,
       "cucsComputeServerDiscPolicyFsmTaskFlags": cucsComputeServerDiscPolicyFsmTaskFlags,
       "cucsComputeServerDiscPolicyFsmTaskItem": cucsComputeServerDiscPolicyFsmTaskItem,
       "cucsComputeServerDiscPolicyFsmTaskSeqId": cucsComputeServerDiscPolicyFsmTaskSeqId,
       "cucsComputeServerMgmtPolicyTable": cucsComputeServerMgmtPolicyTable,
       "cucsComputeServerMgmtPolicyEntry": cucsComputeServerMgmtPolicyEntry,
       "cucsComputeServerMgmtPolicyInstanceId": cucsComputeServerMgmtPolicyInstanceId,
       "cucsComputeServerMgmtPolicyDn": cucsComputeServerMgmtPolicyDn,
       "cucsComputeServerMgmtPolicyRn": cucsComputeServerMgmtPolicyRn,
       "cucsComputeServerMgmtPolicyAction": cucsComputeServerMgmtPolicyAction,
       "cucsComputeServerMgmtPolicyDescr": cucsComputeServerMgmtPolicyDescr,
       "cucsComputeServerMgmtPolicyIntId": cucsComputeServerMgmtPolicyIntId,
       "cucsComputeServerMgmtPolicyName": cucsComputeServerMgmtPolicyName,
       "cucsComputeServerMgmtPolicyPolicyLevel": cucsComputeServerMgmtPolicyPolicyLevel,
       "cucsComputeServerMgmtPolicyPolicyOwner": cucsComputeServerMgmtPolicyPolicyOwner,
       "cucsComputeServerMgmtPolicyQualifier": cucsComputeServerMgmtPolicyQualifier,
       "cucsComputePciSlotScanDefTable": cucsComputePciSlotScanDefTable,
       "cucsComputePciSlotScanDefEntry": cucsComputePciSlotScanDefEntry,
       "cucsComputePciSlotScanDefInstanceId": cucsComputePciSlotScanDefInstanceId,
       "cucsComputePciSlotScanDefDn": cucsComputePciSlotScanDefDn,
       "cucsComputePciSlotScanDefRn": cucsComputePciSlotScanDefRn,
       "cucsComputePciSlotScanDefDescr": cucsComputePciSlotScanDefDescr,
       "cucsComputePciSlotScanDefIntId": cucsComputePciSlotScanDefIntId,
       "cucsComputePciSlotScanDefName": cucsComputePciSlotScanDefName,
       "cucsComputePciSlotScanDefPolicyLevel": cucsComputePciSlotScanDefPolicyLevel,
       "cucsComputePciSlotScanDefPolicyOwner": cucsComputePciSlotScanDefPolicyOwner,
       "cucsComputePciSlotScanDefScanOrder": cucsComputePciSlotScanDefScanOrder,
       "cucsComputePciSlotScanDefSlotId": cucsComputePciSlotScanDefSlotId,
       "cucsComputeHealthLedSensorAlarmTable": cucsComputeHealthLedSensorAlarmTable,
       "cucsComputeHealthLedSensorAlarmEntry": cucsComputeHealthLedSensorAlarmEntry,
       "cucsComputeHealthLedSensorAlarmInstanceId": cucsComputeHealthLedSensorAlarmInstanceId,
       "cucsComputeHealthLedSensorAlarmDn": cucsComputeHealthLedSensorAlarmDn,
       "cucsComputeHealthLedSensorAlarmRn": cucsComputeHealthLedSensorAlarmRn,
       "cucsComputeHealthLedSensorAlarmAlarmDesc": cucsComputeHealthLedSensorAlarmAlarmDesc,
       "cucsComputeHealthLedSensorAlarmAlarmSeverity": cucsComputeHealthLedSensorAlarmAlarmSeverity,
       "cucsComputeHealthLedSensorAlarmSensorId": cucsComputeHealthLedSensorAlarmSensorId,
       "cucsComputeHealthLedSensorAlarmSensorName": cucsComputeHealthLedSensorAlarmSensorName,
       "cucsComputeFwSyncAckTable": cucsComputeFwSyncAckTable,
       "cucsComputeFwSyncAckEntry": cucsComputeFwSyncAckEntry,
       "cucsComputeFwSyncAckInstanceId": cucsComputeFwSyncAckInstanceId,
       "cucsComputeFwSyncAckDn": cucsComputeFwSyncAckDn,
       "cucsComputeFwSyncAckRn": cucsComputeFwSyncAckRn,
       "cucsComputeFwSyncAckAcked": cucsComputeFwSyncAckAcked,
       "cucsComputeFwSyncAckAckedBy": cucsComputeFwSyncAckAckedBy,
       "cucsComputeFwSyncAckAdminState": cucsComputeFwSyncAckAdminState,
       "cucsComputeFwSyncAckAutoDelete": cucsComputeFwSyncAckAutoDelete,
       "cucsComputeFwSyncAckChangeBy": cucsComputeFwSyncAckChangeBy,
       "cucsComputeFwSyncAckChangeDetails": cucsComputeFwSyncAckChangeDetails,
       "cucsComputeFwSyncAckChanges": cucsComputeFwSyncAckChanges,
       "cucsComputeFwSyncAckDescr": cucsComputeFwSyncAckDescr,
       "cucsComputeFwSyncAckDisr": cucsComputeFwSyncAckDisr,
       "cucsComputeFwSyncAckIgnoreCap": cucsComputeFwSyncAckIgnoreCap,
       "cucsComputeFwSyncAckIntId": cucsComputeFwSyncAckIntId,
       "cucsComputeFwSyncAckModified": cucsComputeFwSyncAckModified,
       "cucsComputeFwSyncAckName": cucsComputeFwSyncAckName,
       "cucsComputeFwSyncAckOperScheduler": cucsComputeFwSyncAckOperScheduler,
       "cucsComputeFwSyncAckOperState": cucsComputeFwSyncAckOperState,
       "cucsComputeFwSyncAckPolicyLevel": cucsComputeFwSyncAckPolicyLevel,
       "cucsComputeFwSyncAckPolicyOwner": cucsComputeFwSyncAckPolicyOwner,
       "cucsComputeFwSyncAckPrevOperState": cucsComputeFwSyncAckPrevOperState,
       "cucsComputeFwSyncAckScheduler": cucsComputeFwSyncAckScheduler,
       "cucsComputeFwSyncAckTriggerConfigState": cucsComputeFwSyncAckTriggerConfigState,
       "cucsComputeMemoryConfigPolicyTable": cucsComputeMemoryConfigPolicyTable,
       "cucsComputeMemoryConfigPolicyEntry": cucsComputeMemoryConfigPolicyEntry,
       "cucsComputeMemoryConfigPolicyInstanceId": cucsComputeMemoryConfigPolicyInstanceId,
       "cucsComputeMemoryConfigPolicyDn": cucsComputeMemoryConfigPolicyDn,
       "cucsComputeMemoryConfigPolicyRn": cucsComputeMemoryConfigPolicyRn,
       "cucsComputeMemoryConfigPolicyBlackListing": cucsComputeMemoryConfigPolicyBlackListing,
       "cucsComputeMemoryConfigPolicyDescr": cucsComputeMemoryConfigPolicyDescr,
       "cucsComputeMemoryConfigPolicyIntId": cucsComputeMemoryConfigPolicyIntId,
       "cucsComputeMemoryConfigPolicyName": cucsComputeMemoryConfigPolicyName,
       "cucsComputeMemoryConfigPolicyPolicyLevel": cucsComputeMemoryConfigPolicyPolicyLevel,
       "cucsComputeMemoryConfigPolicyPolicyOwner": cucsComputeMemoryConfigPolicyPolicyOwner,
       "cucsComputeMemoryConfigurationTable": cucsComputeMemoryConfigurationTable,
       "cucsComputeMemoryConfigurationEntry": cucsComputeMemoryConfigurationEntry,
       "cucsComputeMemoryConfigurationInstanceId": cucsComputeMemoryConfigurationInstanceId,
       "cucsComputeMemoryConfigurationDn": cucsComputeMemoryConfigurationDn,
       "cucsComputeMemoryConfigurationRn": cucsComputeMemoryConfigurationRn,
       "cucsComputeMemoryConfigurationAdminMemoryState": cucsComputeMemoryConfigurationAdminMemoryState,
       "cucsComputeMemoryConfigurationBlackListing": cucsComputeMemoryConfigurationBlackListing,
       "cucsComputeBoardConnectorTable": cucsComputeBoardConnectorTable,
       "cucsComputeBoardConnectorEntry": cucsComputeBoardConnectorEntry,
       "cucsComputeBoardConnectorInstanceId": cucsComputeBoardConnectorInstanceId,
       "cucsComputeBoardConnectorDn": cucsComputeBoardConnectorDn,
       "cucsComputeBoardConnectorRn": cucsComputeBoardConnectorRn,
       "cucsComputeBoardConnectorBoardConnectorType": cucsComputeBoardConnectorBoardConnectorType,
       "cucsComputeBoardConnectorMasterSlotId": cucsComputeBoardConnectorMasterSlotId,
       "cucsComputeBoardConnectorSlaveSlotId": cucsComputeBoardConnectorSlaveSlotId,
       "cucsComputeExtBoardTable": cucsComputeExtBoardTable,
       "cucsComputeExtBoardEntry": cucsComputeExtBoardEntry,
       "cucsComputeExtBoardInstanceId": cucsComputeExtBoardInstanceId,
       "cucsComputeExtBoardDn": cucsComputeExtBoardDn,
       "cucsComputeExtBoardRn": cucsComputeExtBoardRn,
       "cucsComputeExtBoardBoardAggregationRole": cucsComputeExtBoardBoardAggregationRole,
       "cucsComputeExtBoardChassisId": cucsComputeExtBoardChassisId,
       "cucsComputeExtBoardCmosVoltage": cucsComputeExtBoardCmosVoltage,
       "cucsComputeExtBoardConnPath": cucsComputeExtBoardConnPath,
       "cucsComputeExtBoardConnStatus": cucsComputeExtBoardConnStatus,
       "cucsComputeExtBoardFaultQualifier": cucsComputeExtBoardFaultQualifier,
       "cucsComputeExtBoardId": cucsComputeExtBoardId,
       "cucsComputeExtBoardLocationDn": cucsComputeExtBoardLocationDn,
       "cucsComputeExtBoardManagingInst": cucsComputeExtBoardManagingInst,
       "cucsComputeExtBoardModel": cucsComputeExtBoardModel,
       "cucsComputeExtBoardOperPower": cucsComputeExtBoardOperPower,
       "cucsComputeExtBoardOperQualifierReason": cucsComputeExtBoardOperQualifierReason,
       "cucsComputeExtBoardOperState": cucsComputeExtBoardOperState,
       "cucsComputeExtBoardOperability": cucsComputeExtBoardOperability,
       "cucsComputeExtBoardPerf": cucsComputeExtBoardPerf,
       "cucsComputeExtBoardPower": cucsComputeExtBoardPower,
       "cucsComputeExtBoardPowerUsage": cucsComputeExtBoardPowerUsage,
       "cucsComputeExtBoardPresence": cucsComputeExtBoardPresence,
       "cucsComputeExtBoardRevision": cucsComputeExtBoardRevision,
       "cucsComputeExtBoardSerial": cucsComputeExtBoardSerial,
       "cucsComputeExtBoardSlotId": cucsComputeExtBoardSlotId,
       "cucsComputeExtBoardThermal": cucsComputeExtBoardThermal,
       "cucsComputeExtBoardVendor": cucsComputeExtBoardVendor,
       "cucsComputeExtBoardVoltage": cucsComputeExtBoardVoltage,
       "cucsComputeExtBoardDiscoveryStatus": cucsComputeExtBoardDiscoveryStatus,
       "cucsComputeKvmMgmtPolicyTable": cucsComputeKvmMgmtPolicyTable,
       "cucsComputeKvmMgmtPolicyEntry": cucsComputeKvmMgmtPolicyEntry,
       "cucsComputeKvmMgmtPolicyInstanceId": cucsComputeKvmMgmtPolicyInstanceId,
       "cucsComputeKvmMgmtPolicyDn": cucsComputeKvmMgmtPolicyDn,
       "cucsComputeKvmMgmtPolicyRn": cucsComputeKvmMgmtPolicyRn,
       "cucsComputeKvmMgmtPolicyDescr": cucsComputeKvmMgmtPolicyDescr,
       "cucsComputeKvmMgmtPolicyIntId": cucsComputeKvmMgmtPolicyIntId,
       "cucsComputeKvmMgmtPolicyName": cucsComputeKvmMgmtPolicyName,
       "cucsComputeKvmMgmtPolicyPolicyLevel": cucsComputeKvmMgmtPolicyPolicyLevel,
       "cucsComputeKvmMgmtPolicyPolicyOwner": cucsComputeKvmMgmtPolicyPolicyOwner,
       "cucsComputeKvmMgmtPolicyVmediaEncryption": cucsComputeKvmMgmtPolicyVmediaEncryption,
       "cucsComputeBladeEpTable": cucsComputeBladeEpTable,
       "cucsComputeBladeEpEntry": cucsComputeBladeEpEntry,
       "cucsComputeBladeEpInstanceId": cucsComputeBladeEpInstanceId,
       "cucsComputeBladeEpDn": cucsComputeBladeEpDn,
       "cucsComputeBladeEpRn": cucsComputeBladeEpRn,
       "cucsComputeBladeEpAdminState": cucsComputeBladeEpAdminState,
       "cucsComputeBladeEpChassisId": cucsComputeBladeEpChassisId,
       "cucsComputeBladeEpEpDn": cucsComputeBladeEpEpDn,
       "cucsComputeBladeEpId": cucsComputeBladeEpId,
       "cucsComputeBladeEpOperQualifierReason": cucsComputeBladeEpOperQualifierReason,
       "cucsComputeBladeEpOperState": cucsComputeBladeEpOperState,
       "cucsComputeBladeEpPeerPresence": cucsComputeBladeEpPeerPresence,
       "cucsComputeBladeEpPresence": cucsComputeBladeEpPresence,
       "cucsComputeBladeEpSlotId": cucsComputeBladeEpSlotId,
       "cucsComputeConstraintDefTable": cucsComputeConstraintDefTable,
       "cucsComputeConstraintDefEntry": cucsComputeConstraintDefEntry,
       "cucsComputeConstraintDefInstanceId": cucsComputeConstraintDefInstanceId,
       "cucsComputeConstraintDefDn": cucsComputeConstraintDefDn,
       "cucsComputeConstraintDefRn": cucsComputeConstraintDefRn,
       "cucsComputeConstraintDefConstraintType": cucsComputeConstraintDefConstraintType,
       "cucsComputeConstraintDefDescr": cucsComputeConstraintDefDescr,
       "cucsComputeConstraintDefHwModel": cucsComputeConstraintDefHwModel,
       "cucsComputeConstraintDefHwRevision": cucsComputeConstraintDefHwRevision,
       "cucsComputeConstraintDefHwVendor": cucsComputeConstraintDefHwVendor,
       "cucsComputeConstraintDefIntId": cucsComputeConstraintDefIntId,
       "cucsComputeConstraintDefName": cucsComputeConstraintDefName,
       "cucsComputeConstraintDefPolicyLevel": cucsComputeConstraintDefPolicyLevel,
       "cucsComputeConstraintDefPolicyOwner": cucsComputeConstraintDefPolicyOwner,
       "cucsComputeServerTypeCapTable": cucsComputeServerTypeCapTable,
       "cucsComputeServerTypeCapEntry": cucsComputeServerTypeCapEntry,
       "cucsComputeServerTypeCapInstanceId": cucsComputeServerTypeCapInstanceId,
       "cucsComputeServerTypeCapDn": cucsComputeServerTypeCapDn,
       "cucsComputeServerTypeCapRn": cucsComputeServerTypeCapRn,
       "cucsComputeServerTypeCapType": cucsComputeServerTypeCapType,
       "cucsComputeCartridgeTable": cucsComputeCartridgeTable,
       "cucsComputeCartridgeEntry": cucsComputeCartridgeEntry,
       "cucsComputeCartridgeInstanceId": cucsComputeCartridgeInstanceId,
       "cucsComputeCartridgeDn": cucsComputeCartridgeDn,
       "cucsComputeCartridgeRn": cucsComputeCartridgeRn,
       "cucsComputeCartridgeChassisId": cucsComputeCartridgeChassisId,
       "cucsComputeCartridgeDiscovery": cucsComputeCartridgeDiscovery,
       "cucsComputeCartridgeFltAggr": cucsComputeCartridgeFltAggr,
       "cucsComputeCartridgeId": cucsComputeCartridgeId,
       "cucsComputeCartridgeLc": cucsComputeCartridgeLc,
       "cucsComputeCartridgeLcTs": cucsComputeCartridgeLcTs,
       "cucsComputeCartridgeModel": cucsComputeCartridgeModel,
       "cucsComputeCartridgeOperQualifierReason": cucsComputeCartridgeOperQualifierReason,
       "cucsComputeCartridgeOperState": cucsComputeCartridgeOperState,
       "cucsComputeCartridgeOperability": cucsComputeCartridgeOperability,
       "cucsComputeCartridgePerf": cucsComputeCartridgePerf,
       "cucsComputeCartridgePower": cucsComputeCartridgePower,
       "cucsComputeCartridgePresence": cucsComputeCartridgePresence,
       "cucsComputeCartridgeRevision": cucsComputeCartridgeRevision,
       "cucsComputeCartridgeSerial": cucsComputeCartridgeSerial,
       "cucsComputeCartridgeSlotId": cucsComputeCartridgeSlotId,
       "cucsComputeCartridgeThermal": cucsComputeCartridgeThermal,
       "cucsComputeCartridgeVendor": cucsComputeCartridgeVendor,
       "cucsComputeCartridgeVoltage": cucsComputeCartridgeVoltage,
       "cucsComputeInstanceIdQualTable": cucsComputeInstanceIdQualTable,
       "cucsComputeInstanceIdQualEntry": cucsComputeInstanceIdQualEntry,
       "cucsComputeInstanceIdQualInstanceId": cucsComputeInstanceIdQualInstanceId,
       "cucsComputeInstanceIdQualDn": cucsComputeInstanceIdQualDn,
       "cucsComputeInstanceIdQualRn": cucsComputeInstanceIdQualRn,
       "cucsComputeInstanceIdQualMaxId": cucsComputeInstanceIdQualMaxId,
       "cucsComputeInstanceIdQualMinId": cucsComputeInstanceIdQualMinId,
       "cucsComputePooledEnclosureComputeSlotTable": cucsComputePooledEnclosureComputeSlotTable,
       "cucsComputePooledEnclosureComputeSlotEntry": cucsComputePooledEnclosureComputeSlotEntry,
       "cucsComputePooledEnclosureComputeSlotInstanceId": cucsComputePooledEnclosureComputeSlotInstanceId,
       "cucsComputePooledEnclosureComputeSlotDn": cucsComputePooledEnclosureComputeSlotDn,
       "cucsComputePooledEnclosureComputeSlotRn": cucsComputePooledEnclosureComputeSlotRn,
       "cucsComputePooledEnclosureComputeSlotAssigned": cucsComputePooledEnclosureComputeSlotAssigned,
       "cucsComputePooledEnclosureComputeSlotAssignedToDn": cucsComputePooledEnclosureComputeSlotAssignedToDn,
       "cucsComputePooledEnclosureComputeSlotChassisId": cucsComputePooledEnclosureComputeSlotChassisId,
       "cucsComputePooledEnclosureComputeSlotOwner": cucsComputePooledEnclosureComputeSlotOwner,
       "cucsComputePooledEnclosureComputeSlotPoolableDn": cucsComputePooledEnclosureComputeSlotPoolableDn,
       "cucsComputePooledEnclosureComputeSlotPrevAssignedToDn": cucsComputePooledEnclosureComputeSlotPrevAssignedToDn,
       "cucsComputePooledEnclosureComputeSlotServerInstanceId": cucsComputePooledEnclosureComputeSlotServerInstanceId,
       "cucsComputePooledEnclosureComputeSlotSlotId": cucsComputePooledEnclosureComputeSlotSlotId,
       "cucsComputeServerUnitTable": cucsComputeServerUnitTable,
       "cucsComputeServerUnitEntry": cucsComputeServerUnitEntry,
       "cucsComputeServerUnitInstanceId": cucsComputeServerUnitInstanceId,
       "cucsComputeServerUnitDn": cucsComputeServerUnitDn,
       "cucsComputeServerUnitRn": cucsComputeServerUnitRn,
       "cucsComputeServerUnitAdminPower": cucsComputeServerUnitAdminPower,
       "cucsComputeServerUnitAdminState": cucsComputeServerUnitAdminState,
       "cucsComputeServerUnitAssignedToDn": cucsComputeServerUnitAssignedToDn,
       "cucsComputeServerUnitAssociation": cucsComputeServerUnitAssociation,
       "cucsComputeServerUnitAvailability": cucsComputeServerUnitAvailability,
       "cucsComputeServerUnitAvailableMemory": cucsComputeServerUnitAvailableMemory,
       "cucsComputeServerUnitChassisId": cucsComputeServerUnitChassisId,
       "cucsComputeServerUnitCheckPoint": cucsComputeServerUnitCheckPoint,
       "cucsComputeServerUnitConnPath": cucsComputeServerUnitConnPath,
       "cucsComputeServerUnitConnStatus": cucsComputeServerUnitConnStatus,
       "cucsComputeServerUnitDescr": cucsComputeServerUnitDescr,
       "cucsComputeServerUnitDiscovery": cucsComputeServerUnitDiscovery,
       "cucsComputeServerUnitDiscoveryStatus": cucsComputeServerUnitDiscoveryStatus,
       "cucsComputeServerUnitFltAggr": cucsComputeServerUnitFltAggr,
       "cucsComputeServerUnitFsmDescr": cucsComputeServerUnitFsmDescr,
       "cucsComputeServerUnitFsmFlags": cucsComputeServerUnitFsmFlags,
       "cucsComputeServerUnitFsmPrev": cucsComputeServerUnitFsmPrev,
       "cucsComputeServerUnitFsmProgr": cucsComputeServerUnitFsmProgr,
       "cucsComputeServerUnitFsmRmtInvErrCode": cucsComputeServerUnitFsmRmtInvErrCode,
       "cucsComputeServerUnitFsmRmtInvErrDescr": cucsComputeServerUnitFsmRmtInvErrDescr,
       "cucsComputeServerUnitFsmRmtInvRslt": cucsComputeServerUnitFsmRmtInvRslt,
       "cucsComputeServerUnitFsmStageDescr": cucsComputeServerUnitFsmStageDescr,
       "cucsComputeServerUnitFsmStamp": cucsComputeServerUnitFsmStamp,
       "cucsComputeServerUnitFsmStatus": cucsComputeServerUnitFsmStatus,
       "cucsComputeServerUnitFsmTry": cucsComputeServerUnitFsmTry,
       "cucsComputeServerUnitIntId": cucsComputeServerUnitIntId,
       "cucsComputeServerUnitLc": cucsComputeServerUnitLc,
       "cucsComputeServerUnitLcTs": cucsComputeServerUnitLcTs,
       "cucsComputeServerUnitLocalId": cucsComputeServerUnitLocalId,
       "cucsComputeServerUnitLowVoltageMemory": cucsComputeServerUnitLowVoltageMemory,
       "cucsComputeServerUnitManagingInst": cucsComputeServerUnitManagingInst,
       "cucsComputeServerUnitMemorySpeed": cucsComputeServerUnitMemorySpeed,
       "cucsComputeServerUnitMfgTime": cucsComputeServerUnitMfgTime,
       "cucsComputeServerUnitModel": cucsComputeServerUnitModel,
       "cucsComputeServerUnitName": cucsComputeServerUnitName,
       "cucsComputeServerUnitNumOfAdaptors": cucsComputeServerUnitNumOfAdaptors,
       "cucsComputeServerUnitNumOfCores": cucsComputeServerUnitNumOfCores,
       "cucsComputeServerUnitNumOfCoresEnabled": cucsComputeServerUnitNumOfCoresEnabled,
       "cucsComputeServerUnitNumOfCpus": cucsComputeServerUnitNumOfCpus,
       "cucsComputeServerUnitNumOfEthHostIfs": cucsComputeServerUnitNumOfEthHostIfs,
       "cucsComputeServerUnitNumOfFcHostIfs": cucsComputeServerUnitNumOfFcHostIfs,
       "cucsComputeServerUnitNumOfThreads": cucsComputeServerUnitNumOfThreads,
       "cucsComputeServerUnitOperPower": cucsComputeServerUnitOperPower,
       "cucsComputeServerUnitOperQualifier": cucsComputeServerUnitOperQualifier,
       "cucsComputeServerUnitOperState": cucsComputeServerUnitOperState,
       "cucsComputeServerUnitOperability": cucsComputeServerUnitOperability,
       "cucsComputeServerUnitOriginalUuid": cucsComputeServerUnitOriginalUuid,
       "cucsComputeServerUnitPartNumber": cucsComputeServerUnitPartNumber,
       "cucsComputeServerUnitPolicyLevel": cucsComputeServerUnitPolicyLevel,
       "cucsComputeServerUnitPolicyOwner": cucsComputeServerUnitPolicyOwner,
       "cucsComputeServerUnitPresence": cucsComputeServerUnitPresence,
       "cucsComputeServerUnitRevision": cucsComputeServerUnitRevision,
       "cucsComputeServerUnitSerial": cucsComputeServerUnitSerial,
       "cucsComputeServerUnitServerId": cucsComputeServerUnitServerId,
       "cucsComputeServerUnitServerInstanceId": cucsComputeServerUnitServerInstanceId,
       "cucsComputeServerUnitSlotId": cucsComputeServerUnitSlotId,
       "cucsComputeServerUnitTotalMemory": cucsComputeServerUnitTotalMemory,
       "cucsComputeServerUnitUsrLbl": cucsComputeServerUnitUsrLbl,
       "cucsComputeServerUnitUuid": cucsComputeServerUnitUuid,
       "cucsComputeServerUnitVendor": cucsComputeServerUnitVendor,
       "cucsComputeServerUnitVid": cucsComputeServerUnitVid,
       "cucsComputeServerUnitNumOf40GAdaptorsWithOldFw": cucsComputeServerUnitNumOf40GAdaptorsWithOldFw,
       "cucsComputeServerUnitNumOf40GAdaptorsWithUnknownFw": cucsComputeServerUnitNumOf40GAdaptorsWithUnknownFw,
       "cucsComputeServerUnitOperPwrTransSrc": cucsComputeServerUnitOperPwrTransSrc,
       "cucsComputeServerUnitFsmTable": cucsComputeServerUnitFsmTable,
       "cucsComputeServerUnitFsmEntry": cucsComputeServerUnitFsmEntry,
       "cucsComputeServerUnitFsmInstanceId": cucsComputeServerUnitFsmInstanceId,
       "cucsComputeServerUnitFsmDn": cucsComputeServerUnitFsmDn,
       "cucsComputeServerUnitFsmRn": cucsComputeServerUnitFsmRn,
       "cucsComputeServerUnitFsmCompletionTime": cucsComputeServerUnitFsmCompletionTime,
       "cucsComputeServerUnitFsmCurrentFsm": cucsComputeServerUnitFsmCurrentFsm,
       "cucsComputeServerUnitFsmDescrData": cucsComputeServerUnitFsmDescrData,
       "cucsComputeServerUnitFsmFsmStatus": cucsComputeServerUnitFsmFsmStatus,
       "cucsComputeServerUnitFsmProgress": cucsComputeServerUnitFsmProgress,
       "cucsComputeServerUnitFsmRmtErrCode": cucsComputeServerUnitFsmRmtErrCode,
       "cucsComputeServerUnitFsmRmtErrDescr": cucsComputeServerUnitFsmRmtErrDescr,
       "cucsComputeServerUnitFsmRmtRslt": cucsComputeServerUnitFsmRmtRslt,
       "cucsComputeServerUnitFsmStageTable": cucsComputeServerUnitFsmStageTable,
       "cucsComputeServerUnitFsmStageEntry": cucsComputeServerUnitFsmStageEntry,
       "cucsComputeServerUnitFsmStageInstanceId": cucsComputeServerUnitFsmStageInstanceId,
       "cucsComputeServerUnitFsmStageDn": cucsComputeServerUnitFsmStageDn,
       "cucsComputeServerUnitFsmStageRn": cucsComputeServerUnitFsmStageRn,
       "cucsComputeServerUnitFsmStageDescrData": cucsComputeServerUnitFsmStageDescrData,
       "cucsComputeServerUnitFsmStageLastUpdateTime": cucsComputeServerUnitFsmStageLastUpdateTime,
       "cucsComputeServerUnitFsmStageName": cucsComputeServerUnitFsmStageName,
       "cucsComputeServerUnitFsmStageOrder": cucsComputeServerUnitFsmStageOrder,
       "cucsComputeServerUnitFsmStageRetry": cucsComputeServerUnitFsmStageRetry,
       "cucsComputeServerUnitFsmStageStageStatus": cucsComputeServerUnitFsmStageStageStatus,
       "cucsComputeServerUnitFsmTaskTable": cucsComputeServerUnitFsmTaskTable,
       "cucsComputeServerUnitFsmTaskEntry": cucsComputeServerUnitFsmTaskEntry,
       "cucsComputeServerUnitFsmTaskInstanceId": cucsComputeServerUnitFsmTaskInstanceId,
       "cucsComputeServerUnitFsmTaskDn": cucsComputeServerUnitFsmTaskDn,
       "cucsComputeServerUnitFsmTaskRn": cucsComputeServerUnitFsmTaskRn,
       "cucsComputeServerUnitFsmTaskCompletion": cucsComputeServerUnitFsmTaskCompletion,
       "cucsComputeServerUnitFsmTaskFlags": cucsComputeServerUnitFsmTaskFlags,
       "cucsComputeServerUnitFsmTaskItem": cucsComputeServerUnitFsmTaskItem,
       "cucsComputeServerUnitFsmTaskSeqId": cucsComputeServerUnitFsmTaskSeqId}
)
