# SNMP MIB module (CISCO-UNIFIED-COMPUTING-LS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-LS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:51 2024
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
 CucsFabricHostPortId,
 CucsFabricVConMappingScheme,
 CucsFabricVConTransportPref,
 CucsFsmCompletion,
 CucsFsmFsmStageStatus,
 CucsLsAgentCapability,
 CucsLsAgentMode,
 CucsLsApply,
 CucsLsAssignment,
 CucsLsAssocState,
 CucsLsComputeBindingOperState,
 CucsLsConfigIssues,
 CucsLsConfigState,
 CucsLsConfigWarnings,
 CucsLsFcZoneGroupSwitchId,
 CucsLsFcZoneState,
 CucsLsOperState,
 CucsLsOwner,
 CucsLsPowerState,
 CucsLsResolveFromRemoteServer,
 CucsLsServerFsmCurrentFsm,
 CucsLsServerFsmStageName,
 CucsLsServerFsmTaskFlags,
 CucsLsServerFsmTaskItem,
 CucsLsType,
 CucsLsUUIDIdentityState,
 CucsNetworkConfigIssues,
 CucsNetworkSwitchId,
 CucsPolicyPolicyOwner,
 CucsServerConfigIssues,
 CucsStorageConfigIssues,
 CucsStorageFcZoningType,
 CucsVnicConfigIssues,
 CucsVnicExternalMgmtIPMode,
 CucsVnicIScsiConfigIssues,
 CucsVnicMezzMappingScheme,
 CucsVnicOrderScheme,
 CucsVnicPlacement) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsFabricHostPortId",
    "CucsFabricVConMappingScheme",
    "CucsFabricVConTransportPref",
    "CucsFsmCompletion",
    "CucsFsmFsmStageStatus",
    "CucsLsAgentCapability",
    "CucsLsAgentMode",
    "CucsLsApply",
    "CucsLsAssignment",
    "CucsLsAssocState",
    "CucsLsComputeBindingOperState",
    "CucsLsConfigIssues",
    "CucsLsConfigState",
    "CucsLsConfigWarnings",
    "CucsLsFcZoneGroupSwitchId",
    "CucsLsFcZoneState",
    "CucsLsOperState",
    "CucsLsOwner",
    "CucsLsPowerState",
    "CucsLsResolveFromRemoteServer",
    "CucsLsServerFsmCurrentFsm",
    "CucsLsServerFsmStageName",
    "CucsLsServerFsmTaskFlags",
    "CucsLsServerFsmTaskItem",
    "CucsLsType",
    "CucsLsUUIDIdentityState",
    "CucsNetworkConfigIssues",
    "CucsNetworkSwitchId",
    "CucsPolicyPolicyOwner",
    "CucsServerConfigIssues",
    "CucsStorageConfigIssues",
    "CucsStorageFcZoningType",
    "CucsVnicConfigIssues",
    "CucsVnicExternalMgmtIPMode",
    "CucsVnicIScsiConfigIssues",
    "CucsVnicMezzMappingScheme",
    "CucsVnicOrderScheme",
    "CucsVnicPlacement")

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

cucsLsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsLsAgentPolicyTable_Object = MibTable
cucsLsAgentPolicyTable = _CucsLsAgentPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 1)
)
if mibBuilder.loadTexts:
    cucsLsAgentPolicyTable.setStatus("current")
_CucsLsAgentPolicyEntry_Object = MibTableRow
cucsLsAgentPolicyEntry = _CucsLsAgentPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 1, 1)
)
cucsLsAgentPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsAgentPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsAgentPolicyEntry.setStatus("current")
_CucsLsAgentPolicyInstanceId_Type = CucsManagedObjectId
_CucsLsAgentPolicyInstanceId_Object = MibTableColumn
cucsLsAgentPolicyInstanceId = _CucsLsAgentPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 1, 1, 1),
    _CucsLsAgentPolicyInstanceId_Type()
)
cucsLsAgentPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsAgentPolicyInstanceId.setStatus("current")
_CucsLsAgentPolicyDn_Type = CucsManagedObjectDn
_CucsLsAgentPolicyDn_Object = MibTableColumn
cucsLsAgentPolicyDn = _CucsLsAgentPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 1, 1, 2),
    _CucsLsAgentPolicyDn_Type()
)
cucsLsAgentPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsAgentPolicyDn.setStatus("current")
_CucsLsAgentPolicyRn_Type = SnmpAdminString
_CucsLsAgentPolicyRn_Object = MibTableColumn
cucsLsAgentPolicyRn = _CucsLsAgentPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 1, 1, 3),
    _CucsLsAgentPolicyRn_Type()
)
cucsLsAgentPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsAgentPolicyRn.setStatus("current")
_CucsLsAgentPolicyCapability_Type = CucsLsAgentCapability
_CucsLsAgentPolicyCapability_Object = MibTableColumn
cucsLsAgentPolicyCapability = _CucsLsAgentPolicyCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 1, 1, 4),
    _CucsLsAgentPolicyCapability_Type()
)
cucsLsAgentPolicyCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsAgentPolicyCapability.setStatus("current")
_CucsLsAgentPolicyDescr_Type = SnmpAdminString
_CucsLsAgentPolicyDescr_Object = MibTableColumn
cucsLsAgentPolicyDescr = _CucsLsAgentPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 1, 1, 5),
    _CucsLsAgentPolicyDescr_Type()
)
cucsLsAgentPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsAgentPolicyDescr.setStatus("current")
_CucsLsAgentPolicyIntId_Type = SnmpAdminString
_CucsLsAgentPolicyIntId_Object = MibTableColumn
cucsLsAgentPolicyIntId = _CucsLsAgentPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 1, 1, 6),
    _CucsLsAgentPolicyIntId_Type()
)
cucsLsAgentPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsAgentPolicyIntId.setStatus("current")
_CucsLsAgentPolicyMode_Type = CucsLsAgentMode
_CucsLsAgentPolicyMode_Object = MibTableColumn
cucsLsAgentPolicyMode = _CucsLsAgentPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 1, 1, 7),
    _CucsLsAgentPolicyMode_Type()
)
cucsLsAgentPolicyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsAgentPolicyMode.setStatus("current")
_CucsLsAgentPolicyName_Type = SnmpAdminString
_CucsLsAgentPolicyName_Object = MibTableColumn
cucsLsAgentPolicyName = _CucsLsAgentPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 1, 1, 8),
    _CucsLsAgentPolicyName_Type()
)
cucsLsAgentPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsAgentPolicyName.setStatus("current")
_CucsLsAgentPolicyPolicyLevel_Type = Gauge32
_CucsLsAgentPolicyPolicyLevel_Object = MibTableColumn
cucsLsAgentPolicyPolicyLevel = _CucsLsAgentPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 1, 1, 9),
    _CucsLsAgentPolicyPolicyLevel_Type()
)
cucsLsAgentPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsAgentPolicyPolicyLevel.setStatus("current")
_CucsLsAgentPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsLsAgentPolicyPolicyOwner_Object = MibTableColumn
cucsLsAgentPolicyPolicyOwner = _CucsLsAgentPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 1, 1, 10),
    _CucsLsAgentPolicyPolicyOwner_Type()
)
cucsLsAgentPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsAgentPolicyPolicyOwner.setStatus("current")
_CucsLsBindingTable_Object = MibTable
cucsLsBindingTable = _CucsLsBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2)
)
if mibBuilder.loadTexts:
    cucsLsBindingTable.setStatus("current")
_CucsLsBindingEntry_Object = MibTableRow
cucsLsBindingEntry = _CucsLsBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2, 1)
)
cucsLsBindingEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsBindingInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsBindingEntry.setStatus("current")
_CucsLsBindingInstanceId_Type = CucsManagedObjectId
_CucsLsBindingInstanceId_Object = MibTableColumn
cucsLsBindingInstanceId = _CucsLsBindingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2, 1, 1),
    _CucsLsBindingInstanceId_Type()
)
cucsLsBindingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsBindingInstanceId.setStatus("current")
_CucsLsBindingDn_Type = CucsManagedObjectDn
_CucsLsBindingDn_Object = MibTableColumn
cucsLsBindingDn = _CucsLsBindingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2, 1, 2),
    _CucsLsBindingDn_Type()
)
cucsLsBindingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsBindingDn.setStatus("current")
_CucsLsBindingRn_Type = SnmpAdminString
_CucsLsBindingRn_Object = MibTableColumn
cucsLsBindingRn = _CucsLsBindingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2, 1, 3),
    _CucsLsBindingRn_Type()
)
cucsLsBindingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsBindingRn.setStatus("current")
_CucsLsBindingComputeEpDn_Type = SnmpAdminString
_CucsLsBindingComputeEpDn_Object = MibTableColumn
cucsLsBindingComputeEpDn = _CucsLsBindingComputeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2, 1, 4),
    _CucsLsBindingComputeEpDn_Type()
)
cucsLsBindingComputeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsBindingComputeEpDn.setStatus("current")
_CucsLsBindingName_Type = SnmpAdminString
_CucsLsBindingName_Object = MibTableColumn
cucsLsBindingName = _CucsLsBindingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2, 1, 5),
    _CucsLsBindingName_Type()
)
cucsLsBindingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsBindingName.setStatus("current")
_CucsLsBindingPnDn_Type = SnmpAdminString
_CucsLsBindingPnDn_Object = MibTableColumn
cucsLsBindingPnDn = _CucsLsBindingPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2, 1, 6),
    _CucsLsBindingPnDn_Type()
)
cucsLsBindingPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsBindingPnDn.setStatus("current")
_CucsLsBindingRestrictMigration_Type = TruthValue
_CucsLsBindingRestrictMigration_Object = MibTableColumn
cucsLsBindingRestrictMigration = _CucsLsBindingRestrictMigration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2, 1, 7),
    _CucsLsBindingRestrictMigration_Type()
)
cucsLsBindingRestrictMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsBindingRestrictMigration.setStatus("current")
_CucsLsBindingAssignedToDn_Type = SnmpAdminString
_CucsLsBindingAssignedToDn_Object = MibTableColumn
cucsLsBindingAssignedToDn = _CucsLsBindingAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2, 1, 8),
    _CucsLsBindingAssignedToDn_Type()
)
cucsLsBindingAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsBindingAssignedToDn.setStatus("current")
_CucsLsBindingIssues_Type = CucsLsConfigIssues
_CucsLsBindingIssues_Object = MibTableColumn
cucsLsBindingIssues = _CucsLsBindingIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2, 1, 9),
    _CucsLsBindingIssues_Type()
)
cucsLsBindingIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsBindingIssues.setStatus("current")
_CucsLsBindingOperState_Type = CucsLsComputeBindingOperState
_CucsLsBindingOperState_Object = MibTableColumn
cucsLsBindingOperState = _CucsLsBindingOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2, 1, 10),
    _CucsLsBindingOperState_Type()
)
cucsLsBindingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsBindingOperState.setStatus("current")
_CucsLsBindingPropAcl_Type = Unsigned64
_CucsLsBindingPropAcl_Object = MibTableColumn
cucsLsBindingPropAcl = _CucsLsBindingPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 2, 1, 11),
    _CucsLsBindingPropAcl_Type()
)
cucsLsBindingPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsBindingPropAcl.setStatus("current")
_CucsLsPowerTable_Object = MibTable
cucsLsPowerTable = _CucsLsPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 3)
)
if mibBuilder.loadTexts:
    cucsLsPowerTable.setStatus("current")
_CucsLsPowerEntry_Object = MibTableRow
cucsLsPowerEntry = _CucsLsPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 3, 1)
)
cucsLsPowerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsPowerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsPowerEntry.setStatus("current")
_CucsLsPowerInstanceId_Type = CucsManagedObjectId
_CucsLsPowerInstanceId_Object = MibTableColumn
cucsLsPowerInstanceId = _CucsLsPowerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 3, 1, 1),
    _CucsLsPowerInstanceId_Type()
)
cucsLsPowerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsPowerInstanceId.setStatus("current")
_CucsLsPowerDn_Type = CucsManagedObjectDn
_CucsLsPowerDn_Object = MibTableColumn
cucsLsPowerDn = _CucsLsPowerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 3, 1, 2),
    _CucsLsPowerDn_Type()
)
cucsLsPowerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsPowerDn.setStatus("current")
_CucsLsPowerRn_Type = SnmpAdminString
_CucsLsPowerRn_Object = MibTableColumn
cucsLsPowerRn = _CucsLsPowerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 3, 1, 3),
    _CucsLsPowerRn_Type()
)
cucsLsPowerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsPowerRn.setStatus("current")
_CucsLsPowerState_Type = CucsLsPowerState
_CucsLsPowerState_Object = MibTableColumn
cucsLsPowerState = _CucsLsPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 3, 1, 4),
    _CucsLsPowerState_Type()
)
cucsLsPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsPowerState.setStatus("current")
_CucsLsPowerPropAcl_Type = Unsigned64
_CucsLsPowerPropAcl_Object = MibTableColumn
cucsLsPowerPropAcl = _CucsLsPowerPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 3, 1, 5),
    _CucsLsPowerPropAcl_Type()
)
cucsLsPowerPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsPowerPropAcl.setStatus("current")
_CucsLsRequirementTable_Object = MibTable
cucsLsRequirementTable = _CucsLsRequirementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4)
)
if mibBuilder.loadTexts:
    cucsLsRequirementTable.setStatus("current")
_CucsLsRequirementEntry_Object = MibTableRow
cucsLsRequirementEntry = _CucsLsRequirementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1)
)
cucsLsRequirementEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsRequirementInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsRequirementEntry.setStatus("current")
_CucsLsRequirementInstanceId_Type = CucsManagedObjectId
_CucsLsRequirementInstanceId_Object = MibTableColumn
cucsLsRequirementInstanceId = _CucsLsRequirementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 1),
    _CucsLsRequirementInstanceId_Type()
)
cucsLsRequirementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsRequirementInstanceId.setStatus("current")
_CucsLsRequirementDn_Type = CucsManagedObjectDn
_CucsLsRequirementDn_Object = MibTableColumn
cucsLsRequirementDn = _CucsLsRequirementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 2),
    _CucsLsRequirementDn_Type()
)
cucsLsRequirementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsRequirementDn.setStatus("current")
_CucsLsRequirementRn_Type = SnmpAdminString
_CucsLsRequirementRn_Object = MibTableColumn
cucsLsRequirementRn = _CucsLsRequirementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 3),
    _CucsLsRequirementRn_Type()
)
cucsLsRequirementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsRequirementRn.setStatus("current")
_CucsLsRequirementComputeEpDn_Type = SnmpAdminString
_CucsLsRequirementComputeEpDn_Object = MibTableColumn
cucsLsRequirementComputeEpDn = _CucsLsRequirementComputeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 4),
    _CucsLsRequirementComputeEpDn_Type()
)
cucsLsRequirementComputeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsRequirementComputeEpDn.setStatus("current")
_CucsLsRequirementName_Type = SnmpAdminString
_CucsLsRequirementName_Object = MibTableColumn
cucsLsRequirementName = _CucsLsRequirementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 5),
    _CucsLsRequirementName_Type()
)
cucsLsRequirementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsRequirementName.setStatus("current")
_CucsLsRequirementPnPoolDn_Type = SnmpAdminString
_CucsLsRequirementPnPoolDn_Object = MibTableColumn
cucsLsRequirementPnPoolDn = _CucsLsRequirementPnPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 6),
    _CucsLsRequirementPnPoolDn_Type()
)
cucsLsRequirementPnPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsRequirementPnPoolDn.setStatus("current")
_CucsLsRequirementQualifier_Type = SnmpAdminString
_CucsLsRequirementQualifier_Object = MibTableColumn
cucsLsRequirementQualifier = _CucsLsRequirementQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 7),
    _CucsLsRequirementQualifier_Type()
)
cucsLsRequirementQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsRequirementQualifier.setStatus("current")
_CucsLsRequirementRestrictMigration_Type = TruthValue
_CucsLsRequirementRestrictMigration_Object = MibTableColumn
cucsLsRequirementRestrictMigration = _CucsLsRequirementRestrictMigration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 8),
    _CucsLsRequirementRestrictMigration_Type()
)
cucsLsRequirementRestrictMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsRequirementRestrictMigration.setStatus("current")
_CucsLsRequirementAssignedToDn_Type = SnmpAdminString
_CucsLsRequirementAssignedToDn_Object = MibTableColumn
cucsLsRequirementAssignedToDn = _CucsLsRequirementAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 9),
    _CucsLsRequirementAssignedToDn_Type()
)
cucsLsRequirementAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsRequirementAssignedToDn.setStatus("current")
_CucsLsRequirementIssues_Type = CucsLsConfigIssues
_CucsLsRequirementIssues_Object = MibTableColumn
cucsLsRequirementIssues = _CucsLsRequirementIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 10),
    _CucsLsRequirementIssues_Type()
)
cucsLsRequirementIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsRequirementIssues.setStatus("current")
_CucsLsRequirementOperState_Type = CucsLsComputeBindingOperState
_CucsLsRequirementOperState_Object = MibTableColumn
cucsLsRequirementOperState = _CucsLsRequirementOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 11),
    _CucsLsRequirementOperState_Type()
)
cucsLsRequirementOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsRequirementOperState.setStatus("current")
_CucsLsRequirementPnDn_Type = SnmpAdminString
_CucsLsRequirementPnDn_Object = MibTableColumn
cucsLsRequirementPnDn = _CucsLsRequirementPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 12),
    _CucsLsRequirementPnDn_Type()
)
cucsLsRequirementPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsRequirementPnDn.setStatus("current")
_CucsLsRequirementOperName_Type = SnmpAdminString
_CucsLsRequirementOperName_Object = MibTableColumn
cucsLsRequirementOperName = _CucsLsRequirementOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 4, 1, 13),
    _CucsLsRequirementOperName_Type()
)
cucsLsRequirementOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsRequirementOperName.setStatus("current")
_CucsLsServerTable_Object = MibTable
cucsLsServerTable = _CucsLsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5)
)
if mibBuilder.loadTexts:
    cucsLsServerTable.setStatus("current")
_CucsLsServerEntry_Object = MibTableRow
cucsLsServerEntry = _CucsLsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1)
)
cucsLsServerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsServerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsServerEntry.setStatus("current")
_CucsLsServerInstanceId_Type = CucsManagedObjectId
_CucsLsServerInstanceId_Object = MibTableColumn
cucsLsServerInstanceId = _CucsLsServerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 1),
    _CucsLsServerInstanceId_Type()
)
cucsLsServerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsServerInstanceId.setStatus("current")
_CucsLsServerDn_Type = CucsManagedObjectDn
_CucsLsServerDn_Object = MibTableColumn
cucsLsServerDn = _CucsLsServerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 2),
    _CucsLsServerDn_Type()
)
cucsLsServerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerDn.setStatus("current")
_CucsLsServerRn_Type = SnmpAdminString
_CucsLsServerRn_Object = MibTableColumn
cucsLsServerRn = _CucsLsServerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 3),
    _CucsLsServerRn_Type()
)
cucsLsServerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerRn.setStatus("current")
_CucsLsServerAgentPolicyName_Type = SnmpAdminString
_CucsLsServerAgentPolicyName_Object = MibTableColumn
cucsLsServerAgentPolicyName = _CucsLsServerAgentPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 4),
    _CucsLsServerAgentPolicyName_Type()
)
cucsLsServerAgentPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerAgentPolicyName.setStatus("current")
_CucsLsServerAssignState_Type = CucsLsAssignment
_CucsLsServerAssignState_Object = MibTableColumn
cucsLsServerAssignState = _CucsLsServerAssignState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 5),
    _CucsLsServerAssignState_Type()
)
cucsLsServerAssignState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerAssignState.setStatus("current")
_CucsLsServerAssocState_Type = CucsLsAssocState
_CucsLsServerAssocState_Object = MibTableColumn
cucsLsServerAssocState = _CucsLsServerAssocState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 6),
    _CucsLsServerAssocState_Type()
)
cucsLsServerAssocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerAssocState.setStatus("current")
_CucsLsServerBiosProfileName_Type = SnmpAdminString
_CucsLsServerBiosProfileName_Object = MibTableColumn
cucsLsServerBiosProfileName = _CucsLsServerBiosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 7),
    _CucsLsServerBiosProfileName_Type()
)
cucsLsServerBiosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerBiosProfileName.setStatus("current")
_CucsLsServerBootPolicyName_Type = SnmpAdminString
_CucsLsServerBootPolicyName_Object = MibTableColumn
cucsLsServerBootPolicyName = _CucsLsServerBootPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 8),
    _CucsLsServerBootPolicyName_Type()
)
cucsLsServerBootPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerBootPolicyName.setStatus("current")
_CucsLsServerConfigQualifier_Type = CucsLsConfigIssues
_CucsLsServerConfigQualifier_Object = MibTableColumn
cucsLsServerConfigQualifier = _CucsLsServerConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 9),
    _CucsLsServerConfigQualifier_Type()
)
cucsLsServerConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerConfigQualifier.setStatus("current")
_CucsLsServerConfigState_Type = CucsLsConfigState
_CucsLsServerConfigState_Object = MibTableColumn
cucsLsServerConfigState = _CucsLsServerConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 10),
    _CucsLsServerConfigState_Type()
)
cucsLsServerConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerConfigState.setStatus("current")
_CucsLsServerDescr_Type = SnmpAdminString
_CucsLsServerDescr_Object = MibTableColumn
cucsLsServerDescr = _CucsLsServerDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 11),
    _CucsLsServerDescr_Type()
)
cucsLsServerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerDescr.setStatus("current")
_CucsLsServerDynamicConPolicyName_Type = SnmpAdminString
_CucsLsServerDynamicConPolicyName_Object = MibTableColumn
cucsLsServerDynamicConPolicyName = _CucsLsServerDynamicConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 12),
    _CucsLsServerDynamicConPolicyName_Type()
)
cucsLsServerDynamicConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerDynamicConPolicyName.setStatus("current")
_CucsLsServerExtIPState_Type = CucsVnicExternalMgmtIPMode
_CucsLsServerExtIPState_Object = MibTableColumn
cucsLsServerExtIPState = _CucsLsServerExtIPState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 13),
    _CucsLsServerExtIPState_Type()
)
cucsLsServerExtIPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerExtIPState.setStatus("current")
_CucsLsServerFltAggr_Type = Unsigned64
_CucsLsServerFltAggr_Object = MibTableColumn
cucsLsServerFltAggr = _CucsLsServerFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 14),
    _CucsLsServerFltAggr_Type()
)
cucsLsServerFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFltAggr.setStatus("current")
_CucsLsServerHostFwPolicyName_Type = SnmpAdminString
_CucsLsServerHostFwPolicyName_Object = MibTableColumn
cucsLsServerHostFwPolicyName = _CucsLsServerHostFwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 15),
    _CucsLsServerHostFwPolicyName_Type()
)
cucsLsServerHostFwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerHostFwPolicyName.setStatus("current")
_CucsLsServerIdentPoolName_Type = SnmpAdminString
_CucsLsServerIdentPoolName_Object = MibTableColumn
cucsLsServerIdentPoolName = _CucsLsServerIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 16),
    _CucsLsServerIdentPoolName_Type()
)
cucsLsServerIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerIdentPoolName.setStatus("current")
_CucsLsServerIntId_Type = SnmpAdminString
_CucsLsServerIntId_Object = MibTableColumn
cucsLsServerIntId = _CucsLsServerIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 17),
    _CucsLsServerIntId_Type()
)
cucsLsServerIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerIntId.setStatus("current")
_CucsLsServerLocalDiskPolicyName_Type = SnmpAdminString
_CucsLsServerLocalDiskPolicyName_Object = MibTableColumn
cucsLsServerLocalDiskPolicyName = _CucsLsServerLocalDiskPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 18),
    _CucsLsServerLocalDiskPolicyName_Type()
)
cucsLsServerLocalDiskPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerLocalDiskPolicyName.setStatus("current")
_CucsLsServerMaintPolicyName_Type = SnmpAdminString
_CucsLsServerMaintPolicyName_Object = MibTableColumn
cucsLsServerMaintPolicyName = _CucsLsServerMaintPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 19),
    _CucsLsServerMaintPolicyName_Type()
)
cucsLsServerMaintPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerMaintPolicyName.setStatus("current")
_CucsLsServerMgmtAccessPolicyName_Type = SnmpAdminString
_CucsLsServerMgmtAccessPolicyName_Object = MibTableColumn
cucsLsServerMgmtAccessPolicyName = _CucsLsServerMgmtAccessPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 20),
    _CucsLsServerMgmtAccessPolicyName_Type()
)
cucsLsServerMgmtAccessPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerMgmtAccessPolicyName.setStatus("current")
_CucsLsServerMgmtFwPolicyName_Type = SnmpAdminString
_CucsLsServerMgmtFwPolicyName_Object = MibTableColumn
cucsLsServerMgmtFwPolicyName = _CucsLsServerMgmtFwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 21),
    _CucsLsServerMgmtFwPolicyName_Type()
)
cucsLsServerMgmtFwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerMgmtFwPolicyName.setStatus("current")
_CucsLsServerName_Type = SnmpAdminString
_CucsLsServerName_Object = MibTableColumn
cucsLsServerName = _CucsLsServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 22),
    _CucsLsServerName_Type()
)
cucsLsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerName.setStatus("current")
_CucsLsServerOperBiosProfileName_Type = SnmpAdminString
_CucsLsServerOperBiosProfileName_Object = MibTableColumn
cucsLsServerOperBiosProfileName = _CucsLsServerOperBiosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 23),
    _CucsLsServerOperBiosProfileName_Type()
)
cucsLsServerOperBiosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperBiosProfileName.setStatus("current")
_CucsLsServerOperBootPolicyName_Type = SnmpAdminString
_CucsLsServerOperBootPolicyName_Object = MibTableColumn
cucsLsServerOperBootPolicyName = _CucsLsServerOperBootPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 24),
    _CucsLsServerOperBootPolicyName_Type()
)
cucsLsServerOperBootPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperBootPolicyName.setStatus("current")
_CucsLsServerOperDynamicConPolicyName_Type = SnmpAdminString
_CucsLsServerOperDynamicConPolicyName_Object = MibTableColumn
cucsLsServerOperDynamicConPolicyName = _CucsLsServerOperDynamicConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 25),
    _CucsLsServerOperDynamicConPolicyName_Type()
)
cucsLsServerOperDynamicConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperDynamicConPolicyName.setStatus("current")
_CucsLsServerOperHostFwPolicyName_Type = SnmpAdminString
_CucsLsServerOperHostFwPolicyName_Object = MibTableColumn
cucsLsServerOperHostFwPolicyName = _CucsLsServerOperHostFwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 26),
    _CucsLsServerOperHostFwPolicyName_Type()
)
cucsLsServerOperHostFwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperHostFwPolicyName.setStatus("current")
_CucsLsServerOperIdentPoolName_Type = SnmpAdminString
_CucsLsServerOperIdentPoolName_Object = MibTableColumn
cucsLsServerOperIdentPoolName = _CucsLsServerOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 27),
    _CucsLsServerOperIdentPoolName_Type()
)
cucsLsServerOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperIdentPoolName.setStatus("current")
_CucsLsServerOperLocalDiskPolicyName_Type = SnmpAdminString
_CucsLsServerOperLocalDiskPolicyName_Object = MibTableColumn
cucsLsServerOperLocalDiskPolicyName = _CucsLsServerOperLocalDiskPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 28),
    _CucsLsServerOperLocalDiskPolicyName_Type()
)
cucsLsServerOperLocalDiskPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperLocalDiskPolicyName.setStatus("current")
_CucsLsServerOperMgmtAccessPolicyName_Type = SnmpAdminString
_CucsLsServerOperMgmtAccessPolicyName_Object = MibTableColumn
cucsLsServerOperMgmtAccessPolicyName = _CucsLsServerOperMgmtAccessPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 29),
    _CucsLsServerOperMgmtAccessPolicyName_Type()
)
cucsLsServerOperMgmtAccessPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperMgmtAccessPolicyName.setStatus("current")
_CucsLsServerOperMgmtFwPolicyName_Type = SnmpAdminString
_CucsLsServerOperMgmtFwPolicyName_Object = MibTableColumn
cucsLsServerOperMgmtFwPolicyName = _CucsLsServerOperMgmtFwPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 30),
    _CucsLsServerOperMgmtFwPolicyName_Type()
)
cucsLsServerOperMgmtFwPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperMgmtFwPolicyName.setStatus("current")
_CucsLsServerOperScrubPolicyName_Type = SnmpAdminString
_CucsLsServerOperScrubPolicyName_Object = MibTableColumn
cucsLsServerOperScrubPolicyName = _CucsLsServerOperScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 31),
    _CucsLsServerOperScrubPolicyName_Type()
)
cucsLsServerOperScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperScrubPolicyName.setStatus("current")
_CucsLsServerOperSolPolicyName_Type = SnmpAdminString
_CucsLsServerOperSolPolicyName_Object = MibTableColumn
cucsLsServerOperSolPolicyName = _CucsLsServerOperSolPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 32),
    _CucsLsServerOperSolPolicyName_Type()
)
cucsLsServerOperSolPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperSolPolicyName.setStatus("current")
_CucsLsServerOperSrcTemplName_Type = SnmpAdminString
_CucsLsServerOperSrcTemplName_Object = MibTableColumn
cucsLsServerOperSrcTemplName = _CucsLsServerOperSrcTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 33),
    _CucsLsServerOperSrcTemplName_Type()
)
cucsLsServerOperSrcTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperSrcTemplName.setStatus("current")
_CucsLsServerOperState_Type = CucsLsOperState
_CucsLsServerOperState_Object = MibTableColumn
cucsLsServerOperState = _CucsLsServerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 34),
    _CucsLsServerOperState_Type()
)
cucsLsServerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperState.setStatus("current")
_CucsLsServerOperStatsPolicyName_Type = SnmpAdminString
_CucsLsServerOperStatsPolicyName_Object = MibTableColumn
cucsLsServerOperStatsPolicyName = _CucsLsServerOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 35),
    _CucsLsServerOperStatsPolicyName_Type()
)
cucsLsServerOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperStatsPolicyName.setStatus("current")
_CucsLsServerOperVconProfileName_Type = SnmpAdminString
_CucsLsServerOperVconProfileName_Object = MibTableColumn
cucsLsServerOperVconProfileName = _CucsLsServerOperVconProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 36),
    _CucsLsServerOperVconProfileName_Type()
)
cucsLsServerOperVconProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperVconProfileName.setStatus("current")
_CucsLsServerOwner_Type = CucsLsOwner
_CucsLsServerOwner_Object = MibTableColumn
cucsLsServerOwner = _CucsLsServerOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 37),
    _CucsLsServerOwner_Type()
)
cucsLsServerOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOwner.setStatus("current")
_CucsLsServerFsmFlags_Type = SnmpAdminString
_CucsLsServerFsmFlags_Object = MibTableColumn
cucsLsServerFsmFlags = _CucsLsServerFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 38),
    _CucsLsServerFsmFlags_Type()
)
cucsLsServerFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmFlags.setStatus("current")
_CucsLsServerPnDn_Type = SnmpAdminString
_CucsLsServerPnDn_Object = MibTableColumn
cucsLsServerPnDn = _CucsLsServerPnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 39),
    _CucsLsServerPnDn_Type()
)
cucsLsServerPnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerPnDn.setStatus("current")
_CucsLsServerPowerPolicyName_Type = SnmpAdminString
_CucsLsServerPowerPolicyName_Object = MibTableColumn
cucsLsServerPowerPolicyName = _CucsLsServerPowerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 40),
    _CucsLsServerPowerPolicyName_Type()
)
cucsLsServerPowerPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerPowerPolicyName.setStatus("current")
_CucsLsServerScrubPolicyName_Type = SnmpAdminString
_CucsLsServerScrubPolicyName_Object = MibTableColumn
cucsLsServerScrubPolicyName = _CucsLsServerScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 41),
    _CucsLsServerScrubPolicyName_Type()
)
cucsLsServerScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerScrubPolicyName.setStatus("current")
_CucsLsServerSolPolicyName_Type = SnmpAdminString
_CucsLsServerSolPolicyName_Object = MibTableColumn
cucsLsServerSolPolicyName = _CucsLsServerSolPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 42),
    _CucsLsServerSolPolicyName_Type()
)
cucsLsServerSolPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerSolPolicyName.setStatus("current")
_CucsLsServerSrcTemplName_Type = SnmpAdminString
_CucsLsServerSrcTemplName_Object = MibTableColumn
cucsLsServerSrcTemplName = _CucsLsServerSrcTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 43),
    _CucsLsServerSrcTemplName_Type()
)
cucsLsServerSrcTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerSrcTemplName.setStatus("current")
_CucsLsServerStatsPolicyName_Type = SnmpAdminString
_CucsLsServerStatsPolicyName_Object = MibTableColumn
cucsLsServerStatsPolicyName = _CucsLsServerStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 44),
    _CucsLsServerStatsPolicyName_Type()
)
cucsLsServerStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerStatsPolicyName.setStatus("current")
_CucsLsServerType_Type = CucsLsType
_CucsLsServerType_Object = MibTableColumn
cucsLsServerType = _CucsLsServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 45),
    _CucsLsServerType_Type()
)
cucsLsServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerType.setStatus("current")
_CucsLsServerUsrLbl_Type = SnmpAdminString
_CucsLsServerUsrLbl_Object = MibTableColumn
cucsLsServerUsrLbl = _CucsLsServerUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 46),
    _CucsLsServerUsrLbl_Type()
)
cucsLsServerUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerUsrLbl.setStatus("current")
_CucsLsServerUuid_Type = SnmpAdminString
_CucsLsServerUuid_Object = MibTableColumn
cucsLsServerUuid = _CucsLsServerUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 47),
    _CucsLsServerUuid_Type()
)
cucsLsServerUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerUuid.setStatus("current")
_CucsLsServerUuidSuffix_Type = Unsigned64
_CucsLsServerUuidSuffix_Object = MibTableColumn
cucsLsServerUuidSuffix = _CucsLsServerUuidSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 48),
    _CucsLsServerUuidSuffix_Type()
)
cucsLsServerUuidSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerUuidSuffix.setStatus("current")
_CucsLsServerVconProfileName_Type = SnmpAdminString
_CucsLsServerVconProfileName_Object = MibTableColumn
cucsLsServerVconProfileName = _CucsLsServerVconProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 49),
    _CucsLsServerVconProfileName_Type()
)
cucsLsServerVconProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerVconProfileName.setStatus("current")
_CucsLsServerFsmDescr_Type = SnmpAdminString
_CucsLsServerFsmDescr_Object = MibTableColumn
cucsLsServerFsmDescr = _CucsLsServerFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 50),
    _CucsLsServerFsmDescr_Type()
)
cucsLsServerFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmDescr.setStatus("current")
_CucsLsServerFsmPrev_Type = SnmpAdminString
_CucsLsServerFsmPrev_Object = MibTableColumn
cucsLsServerFsmPrev = _CucsLsServerFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 51),
    _CucsLsServerFsmPrev_Type()
)
cucsLsServerFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmPrev.setStatus("current")
_CucsLsServerFsmProgr_Type = Gauge32
_CucsLsServerFsmProgr_Object = MibTableColumn
cucsLsServerFsmProgr = _CucsLsServerFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 52),
    _CucsLsServerFsmProgr_Type()
)
cucsLsServerFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmProgr.setStatus("current")
_CucsLsServerFsmRmtInvErrCode_Type = Gauge32
_CucsLsServerFsmRmtInvErrCode_Object = MibTableColumn
cucsLsServerFsmRmtInvErrCode = _CucsLsServerFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 53),
    _CucsLsServerFsmRmtInvErrCode_Type()
)
cucsLsServerFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmRmtInvErrCode.setStatus("current")
_CucsLsServerFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsLsServerFsmRmtInvErrDescr_Object = MibTableColumn
cucsLsServerFsmRmtInvErrDescr = _CucsLsServerFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 54),
    _CucsLsServerFsmRmtInvErrDescr_Type()
)
cucsLsServerFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmRmtInvErrDescr.setStatus("current")
_CucsLsServerFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsLsServerFsmRmtInvRslt_Object = MibTableColumn
cucsLsServerFsmRmtInvRslt = _CucsLsServerFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 55),
    _CucsLsServerFsmRmtInvRslt_Type()
)
cucsLsServerFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmRmtInvRslt.setStatus("current")
_CucsLsServerFsmStageDescr_Type = SnmpAdminString
_CucsLsServerFsmStageDescr_Object = MibTableColumn
cucsLsServerFsmStageDescr = _CucsLsServerFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 56),
    _CucsLsServerFsmStageDescr_Type()
)
cucsLsServerFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmStageDescr.setStatus("current")
_CucsLsServerFsmStamp_Type = DateAndTime
_CucsLsServerFsmStamp_Object = MibTableColumn
cucsLsServerFsmStamp = _CucsLsServerFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 57),
    _CucsLsServerFsmStamp_Type()
)
cucsLsServerFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmStamp.setStatus("current")
_CucsLsServerFsmStatus_Type = SnmpAdminString
_CucsLsServerFsmStatus_Object = MibTableColumn
cucsLsServerFsmStatus = _CucsLsServerFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 58),
    _CucsLsServerFsmStatus_Type()
)
cucsLsServerFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmStatus.setStatus("current")
_CucsLsServerFsmTry_Type = Gauge32
_CucsLsServerFsmTry_Object = MibTableColumn
cucsLsServerFsmTry = _CucsLsServerFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 59),
    _CucsLsServerFsmTry_Type()
)
cucsLsServerFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmTry.setStatus("current")
_CucsLsServerOperMaintPolicyName_Type = SnmpAdminString
_CucsLsServerOperMaintPolicyName_Object = MibTableColumn
cucsLsServerOperMaintPolicyName = _CucsLsServerOperMaintPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 60),
    _CucsLsServerOperMaintPolicyName_Type()
)
cucsLsServerOperMaintPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperMaintPolicyName.setStatus("current")
_CucsLsServerOperPowerPolicyName_Type = SnmpAdminString
_CucsLsServerOperPowerPolicyName_Object = MibTableColumn
cucsLsServerOperPowerPolicyName = _CucsLsServerOperPowerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 61),
    _CucsLsServerOperPowerPolicyName_Type()
)
cucsLsServerOperPowerPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperPowerPolicyName.setStatus("current")
_CucsLsServerExtIPPoolName_Type = SnmpAdminString
_CucsLsServerExtIPPoolName_Object = MibTableColumn
cucsLsServerExtIPPoolName = _CucsLsServerExtIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 62),
    _CucsLsServerExtIPPoolName_Type()
)
cucsLsServerExtIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerExtIPPoolName.setStatus("current")
_CucsLsServerOperExtIPPoolName_Type = SnmpAdminString
_CucsLsServerOperExtIPPoolName_Object = MibTableColumn
cucsLsServerOperExtIPPoolName = _CucsLsServerOperExtIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 63),
    _CucsLsServerOperExtIPPoolName_Type()
)
cucsLsServerOperExtIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperExtIPPoolName.setStatus("current")
_CucsLsServerPolicyLevel_Type = Gauge32
_CucsLsServerPolicyLevel_Object = MibTableColumn
cucsLsServerPolicyLevel = _CucsLsServerPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 64),
    _CucsLsServerPolicyLevel_Type()
)
cucsLsServerPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerPolicyLevel.setStatus("current")
_CucsLsServerPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsLsServerPolicyOwner_Object = MibTableColumn
cucsLsServerPolicyOwner = _CucsLsServerPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 65),
    _CucsLsServerPolicyOwner_Type()
)
cucsLsServerPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerPolicyOwner.setStatus("current")
_CucsLsServerResolveRemote_Type = CucsLsResolveFromRemoteServer
_CucsLsServerResolveRemote_Object = MibTableColumn
cucsLsServerResolveRemote = _CucsLsServerResolveRemote_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 66),
    _CucsLsServerResolveRemote_Type()
)
cucsLsServerResolveRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerResolveRemote.setStatus("current")
_CucsLsServerKvmMgmtPolicyName_Type = SnmpAdminString
_CucsLsServerKvmMgmtPolicyName_Object = MibTableColumn
cucsLsServerKvmMgmtPolicyName = _CucsLsServerKvmMgmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 67),
    _CucsLsServerKvmMgmtPolicyName_Type()
)
cucsLsServerKvmMgmtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerKvmMgmtPolicyName.setStatus("current")
_CucsLsServerOperKvmMgmtPolicyName_Type = SnmpAdminString
_CucsLsServerOperKvmMgmtPolicyName_Object = MibTableColumn
cucsLsServerOperKvmMgmtPolicyName = _CucsLsServerOperKvmMgmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 68),
    _CucsLsServerOperKvmMgmtPolicyName_Type()
)
cucsLsServerOperKvmMgmtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperKvmMgmtPolicyName.setStatus("current")
_CucsLsServerOperVmediaPolicyName_Type = SnmpAdminString
_CucsLsServerOperVmediaPolicyName_Object = MibTableColumn
cucsLsServerOperVmediaPolicyName = _CucsLsServerOperVmediaPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 69),
    _CucsLsServerOperVmediaPolicyName_Type()
)
cucsLsServerOperVmediaPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerOperVmediaPolicyName.setStatus("current")
_CucsLsServerSvnicConfig_Type = TruthValue
_CucsLsServerSvnicConfig_Object = MibTableColumn
cucsLsServerSvnicConfig = _CucsLsServerSvnicConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 70),
    _CucsLsServerSvnicConfig_Type()
)
cucsLsServerSvnicConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerSvnicConfig.setStatus("current")
_CucsLsServerVmediaPolicyName_Type = SnmpAdminString
_CucsLsServerVmediaPolicyName_Object = MibTableColumn
cucsLsServerVmediaPolicyName = _CucsLsServerVmediaPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 71),
    _CucsLsServerVmediaPolicyName_Type()
)
cucsLsServerVmediaPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerVmediaPolicyName.setStatus("current")
_CucsLsServerPropAcl_Type = Unsigned64
_CucsLsServerPropAcl_Object = MibTableColumn
cucsLsServerPropAcl = _CucsLsServerPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 5, 1, 72),
    _CucsLsServerPropAcl_Type()
)
cucsLsServerPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerPropAcl.setStatus("current")
_CucsLsTierTable_Object = MibTable
cucsLsTierTable = _CucsLsTierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 6)
)
if mibBuilder.loadTexts:
    cucsLsTierTable.setStatus("current")
_CucsLsTierEntry_Object = MibTableRow
cucsLsTierEntry = _CucsLsTierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 6, 1)
)
cucsLsTierEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsTierInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsTierEntry.setStatus("current")
_CucsLsTierInstanceId_Type = CucsManagedObjectId
_CucsLsTierInstanceId_Object = MibTableColumn
cucsLsTierInstanceId = _CucsLsTierInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 6, 1, 1),
    _CucsLsTierInstanceId_Type()
)
cucsLsTierInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsTierInstanceId.setStatus("current")
_CucsLsTierDn_Type = CucsManagedObjectDn
_CucsLsTierDn_Object = MibTableColumn
cucsLsTierDn = _CucsLsTierDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 6, 1, 2),
    _CucsLsTierDn_Type()
)
cucsLsTierDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsTierDn.setStatus("current")
_CucsLsTierRn_Type = SnmpAdminString
_CucsLsTierRn_Object = MibTableColumn
cucsLsTierRn = _CucsLsTierRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 6, 1, 3),
    _CucsLsTierRn_Type()
)
cucsLsTierRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsTierRn.setStatus("current")
_CucsLsTierApply_Type = CucsLsApply
_CucsLsTierApply_Object = MibTableColumn
cucsLsTierApply = _CucsLsTierApply_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 6, 1, 4),
    _CucsLsTierApply_Type()
)
cucsLsTierApply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsTierApply.setStatus("current")
_CucsLsTierDescr_Type = SnmpAdminString
_CucsLsTierDescr_Object = MibTableColumn
cucsLsTierDescr = _CucsLsTierDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 6, 1, 5),
    _CucsLsTierDescr_Type()
)
cucsLsTierDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsTierDescr.setStatus("current")
_CucsLsTierIntId_Type = SnmpAdminString
_CucsLsTierIntId_Object = MibTableColumn
cucsLsTierIntId = _CucsLsTierIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 6, 1, 6),
    _CucsLsTierIntId_Type()
)
cucsLsTierIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsTierIntId.setStatus("current")
_CucsLsTierName_Type = SnmpAdminString
_CucsLsTierName_Object = MibTableColumn
cucsLsTierName = _CucsLsTierName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 6, 1, 7),
    _CucsLsTierName_Type()
)
cucsLsTierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsTierName.setStatus("current")
_CucsLsTierSrcTemplName_Type = SnmpAdminString
_CucsLsTierSrcTemplName_Object = MibTableColumn
cucsLsTierSrcTemplName = _CucsLsTierSrcTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 6, 1, 8),
    _CucsLsTierSrcTemplName_Type()
)
cucsLsTierSrcTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsTierSrcTemplName.setStatus("current")
_CucsLsTierPolicyLevel_Type = Gauge32
_CucsLsTierPolicyLevel_Object = MibTableColumn
cucsLsTierPolicyLevel = _CucsLsTierPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 6, 1, 9),
    _CucsLsTierPolicyLevel_Type()
)
cucsLsTierPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsTierPolicyLevel.setStatus("current")
_CucsLsTierPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsLsTierPolicyOwner_Object = MibTableColumn
cucsLsTierPolicyOwner = _CucsLsTierPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 6, 1, 10),
    _CucsLsTierPolicyOwner_Type()
)
cucsLsTierPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsTierPolicyOwner.setStatus("current")
_CucsLsServerFsmTaskTable_Object = MibTable
cucsLsServerFsmTaskTable = _CucsLsServerFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 7)
)
if mibBuilder.loadTexts:
    cucsLsServerFsmTaskTable.setStatus("current")
_CucsLsServerFsmTaskEntry_Object = MibTableRow
cucsLsServerFsmTaskEntry = _CucsLsServerFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 7, 1)
)
cucsLsServerFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsServerFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsServerFsmTaskEntry.setStatus("current")
_CucsLsServerFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsLsServerFsmTaskInstanceId_Object = MibTableColumn
cucsLsServerFsmTaskInstanceId = _CucsLsServerFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 7, 1, 1),
    _CucsLsServerFsmTaskInstanceId_Type()
)
cucsLsServerFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsServerFsmTaskInstanceId.setStatus("current")
_CucsLsServerFsmTaskDn_Type = CucsManagedObjectDn
_CucsLsServerFsmTaskDn_Object = MibTableColumn
cucsLsServerFsmTaskDn = _CucsLsServerFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 7, 1, 2),
    _CucsLsServerFsmTaskDn_Type()
)
cucsLsServerFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmTaskDn.setStatus("current")
_CucsLsServerFsmTaskRn_Type = SnmpAdminString
_CucsLsServerFsmTaskRn_Object = MibTableColumn
cucsLsServerFsmTaskRn = _CucsLsServerFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 7, 1, 3),
    _CucsLsServerFsmTaskRn_Type()
)
cucsLsServerFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmTaskRn.setStatus("current")
_CucsLsServerFsmTaskCompletion_Type = CucsFsmCompletion
_CucsLsServerFsmTaskCompletion_Object = MibTableColumn
cucsLsServerFsmTaskCompletion = _CucsLsServerFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 7, 1, 4),
    _CucsLsServerFsmTaskCompletion_Type()
)
cucsLsServerFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmTaskCompletion.setStatus("current")
_CucsLsServerFsmTaskFlags_Type = CucsLsServerFsmTaskFlags
_CucsLsServerFsmTaskFlags_Object = MibTableColumn
cucsLsServerFsmTaskFlags = _CucsLsServerFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 7, 1, 5),
    _CucsLsServerFsmTaskFlags_Type()
)
cucsLsServerFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmTaskFlags.setStatus("current")
_CucsLsServerFsmTaskItem_Type = CucsLsServerFsmTaskItem
_CucsLsServerFsmTaskItem_Object = MibTableColumn
cucsLsServerFsmTaskItem = _CucsLsServerFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 7, 1, 6),
    _CucsLsServerFsmTaskItem_Type()
)
cucsLsServerFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmTaskItem.setStatus("current")
_CucsLsServerFsmTaskSeqId_Type = Gauge32
_CucsLsServerFsmTaskSeqId_Object = MibTableColumn
cucsLsServerFsmTaskSeqId = _CucsLsServerFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 7, 1, 7),
    _CucsLsServerFsmTaskSeqId_Type()
)
cucsLsServerFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmTaskSeqId.setStatus("current")
_CucsLsServerAssocCtxTable_Object = MibTable
cucsLsServerAssocCtxTable = _CucsLsServerAssocCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 8)
)
if mibBuilder.loadTexts:
    cucsLsServerAssocCtxTable.setStatus("current")
_CucsLsServerAssocCtxEntry_Object = MibTableRow
cucsLsServerAssocCtxEntry = _CucsLsServerAssocCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 8, 1)
)
cucsLsServerAssocCtxEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsServerAssocCtxInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsServerAssocCtxEntry.setStatus("current")
_CucsLsServerAssocCtxInstanceId_Type = CucsManagedObjectId
_CucsLsServerAssocCtxInstanceId_Object = MibTableColumn
cucsLsServerAssocCtxInstanceId = _CucsLsServerAssocCtxInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 8, 1, 1),
    _CucsLsServerAssocCtxInstanceId_Type()
)
cucsLsServerAssocCtxInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsServerAssocCtxInstanceId.setStatus("current")
_CucsLsServerAssocCtxDn_Type = CucsManagedObjectDn
_CucsLsServerAssocCtxDn_Object = MibTableColumn
cucsLsServerAssocCtxDn = _CucsLsServerAssocCtxDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 8, 1, 2),
    _CucsLsServerAssocCtxDn_Type()
)
cucsLsServerAssocCtxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerAssocCtxDn.setStatus("current")
_CucsLsServerAssocCtxRn_Type = SnmpAdminString
_CucsLsServerAssocCtxRn_Object = MibTableColumn
cucsLsServerAssocCtxRn = _CucsLsServerAssocCtxRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 8, 1, 3),
    _CucsLsServerAssocCtxRn_Type()
)
cucsLsServerAssocCtxRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerAssocCtxRn.setStatus("current")
_CucsLsServerAssocCtxPropAcl_Type = Unsigned64
_CucsLsServerAssocCtxPropAcl_Object = MibTableColumn
cucsLsServerAssocCtxPropAcl = _CucsLsServerAssocCtxPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 8, 1, 4),
    _CucsLsServerAssocCtxPropAcl_Type()
)
cucsLsServerAssocCtxPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerAssocCtxPropAcl.setStatus("current")
_CucsLsVersionBehTable_Object = MibTable
cucsLsVersionBehTable = _CucsLsVersionBehTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 9)
)
if mibBuilder.loadTexts:
    cucsLsVersionBehTable.setStatus("current")
_CucsLsVersionBehEntry_Object = MibTableRow
cucsLsVersionBehEntry = _CucsLsVersionBehEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 9, 1)
)
cucsLsVersionBehEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsVersionBehInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsVersionBehEntry.setStatus("current")
_CucsLsVersionBehInstanceId_Type = CucsManagedObjectId
_CucsLsVersionBehInstanceId_Object = MibTableColumn
cucsLsVersionBehInstanceId = _CucsLsVersionBehInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 9, 1, 1),
    _CucsLsVersionBehInstanceId_Type()
)
cucsLsVersionBehInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsVersionBehInstanceId.setStatus("current")
_CucsLsVersionBehDn_Type = CucsManagedObjectDn
_CucsLsVersionBehDn_Object = MibTableColumn
cucsLsVersionBehDn = _CucsLsVersionBehDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 9, 1, 2),
    _CucsLsVersionBehDn_Type()
)
cucsLsVersionBehDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVersionBehDn.setStatus("current")
_CucsLsVersionBehRn_Type = SnmpAdminString
_CucsLsVersionBehRn_Object = MibTableColumn
cucsLsVersionBehRn = _CucsLsVersionBehRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 9, 1, 3),
    _CucsLsVersionBehRn_Type()
)
cucsLsVersionBehRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVersionBehRn.setStatus("current")
_CucsLsVersionBehPciEnum_Type = CucsVnicOrderScheme
_CucsLsVersionBehPciEnum_Object = MibTableColumn
cucsLsVersionBehPciEnum = _CucsLsVersionBehPciEnum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 9, 1, 4),
    _CucsLsVersionBehPciEnum_Type()
)
cucsLsVersionBehPciEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVersionBehPciEnum.setStatus("current")
_CucsLsVersionBehVnicOrder_Type = CucsVnicPlacement
_CucsLsVersionBehVnicOrder_Object = MibTableColumn
cucsLsVersionBehVnicOrder = _CucsLsVersionBehVnicOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 9, 1, 5),
    _CucsLsVersionBehVnicOrder_Type()
)
cucsLsVersionBehVnicOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVersionBehVnicOrder.setStatus("current")
_CucsLsVersionBehVconMap_Type = CucsFabricVConMappingScheme
_CucsLsVersionBehVconMap_Object = MibTableColumn
cucsLsVersionBehVconMap = _CucsLsVersionBehVconMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 9, 1, 6),
    _CucsLsVersionBehVconMap_Type()
)
cucsLsVersionBehVconMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVersionBehVconMap.setStatus("current")
_CucsLsVersionBehVnicMap_Type = CucsVnicMezzMappingScheme
_CucsLsVersionBehVnicMap_Object = MibTableColumn
cucsLsVersionBehVnicMap = _CucsLsVersionBehVnicMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 9, 1, 7),
    _CucsLsVersionBehVnicMap_Type()
)
cucsLsVersionBehVnicMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVersionBehVnicMap.setStatus("current")
_CucsLsVersionBehPropAcl_Type = Unsigned64
_CucsLsVersionBehPropAcl_Object = MibTableColumn
cucsLsVersionBehPropAcl = _CucsLsVersionBehPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 9, 1, 8),
    _CucsLsVersionBehPropAcl_Type()
)
cucsLsVersionBehPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVersionBehPropAcl.setStatus("current")
_CucsLsFcLocaleTable_Object = MibTable
cucsLsFcLocaleTable = _CucsLsFcLocaleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 10)
)
if mibBuilder.loadTexts:
    cucsLsFcLocaleTable.setStatus("current")
_CucsLsFcLocaleEntry_Object = MibTableRow
cucsLsFcLocaleEntry = _CucsLsFcLocaleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 10, 1)
)
cucsLsFcLocaleEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsFcLocaleInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsFcLocaleEntry.setStatus("current")
_CucsLsFcLocaleInstanceId_Type = CucsManagedObjectId
_CucsLsFcLocaleInstanceId_Object = MibTableColumn
cucsLsFcLocaleInstanceId = _CucsLsFcLocaleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 10, 1, 1),
    _CucsLsFcLocaleInstanceId_Type()
)
cucsLsFcLocaleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsFcLocaleInstanceId.setStatus("current")
_CucsLsFcLocaleDn_Type = CucsManagedObjectDn
_CucsLsFcLocaleDn_Object = MibTableColumn
cucsLsFcLocaleDn = _CucsLsFcLocaleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 10, 1, 2),
    _CucsLsFcLocaleDn_Type()
)
cucsLsFcLocaleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcLocaleDn.setStatus("current")
_CucsLsFcLocaleRn_Type = SnmpAdminString
_CucsLsFcLocaleRn_Object = MibTableColumn
cucsLsFcLocaleRn = _CucsLsFcLocaleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 10, 1, 3),
    _CucsLsFcLocaleRn_Type()
)
cucsLsFcLocaleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcLocaleRn.setStatus("current")
_CucsLsFcLocaleSwitchId_Type = CucsNetworkSwitchId
_CucsLsFcLocaleSwitchId_Object = MibTableColumn
cucsLsFcLocaleSwitchId = _CucsLsFcLocaleSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 10, 1, 4),
    _CucsLsFcLocaleSwitchId_Type()
)
cucsLsFcLocaleSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcLocaleSwitchId.setStatus("current")
_CucsLsFcZoneTable_Object = MibTable
cucsLsFcZoneTable = _CucsLsFcZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11)
)
if mibBuilder.loadTexts:
    cucsLsFcZoneTable.setStatus("current")
_CucsLsFcZoneEntry_Object = MibTableRow
cucsLsFcZoneEntry = _CucsLsFcZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1)
)
cucsLsFcZoneEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsFcZoneInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsFcZoneEntry.setStatus("current")
_CucsLsFcZoneInstanceId_Type = CucsManagedObjectId
_CucsLsFcZoneInstanceId_Object = MibTableColumn
cucsLsFcZoneInstanceId = _CucsLsFcZoneInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 1),
    _CucsLsFcZoneInstanceId_Type()
)
cucsLsFcZoneInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsFcZoneInstanceId.setStatus("current")
_CucsLsFcZoneDn_Type = CucsManagedObjectDn
_CucsLsFcZoneDn_Object = MibTableColumn
cucsLsFcZoneDn = _CucsLsFcZoneDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 2),
    _CucsLsFcZoneDn_Type()
)
cucsLsFcZoneDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneDn.setStatus("current")
_CucsLsFcZoneRn_Type = SnmpAdminString
_CucsLsFcZoneRn_Object = MibTableColumn
cucsLsFcZoneRn = _CucsLsFcZoneRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 3),
    _CucsLsFcZoneRn_Type()
)
cucsLsFcZoneRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneRn.setStatus("current")
_CucsLsFcZoneAdminState_Type = CucsLsFcZoneState
_CucsLsFcZoneAdminState_Object = MibTableColumn
cucsLsFcZoneAdminState = _CucsLsFcZoneAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 4),
    _CucsLsFcZoneAdminState_Type()
)
cucsLsFcZoneAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneAdminState.setStatus("current")
_CucsLsFcZoneId_Type = Gauge32
_CucsLsFcZoneId_Object = MibTableColumn
cucsLsFcZoneId = _CucsLsFcZoneId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 5),
    _CucsLsFcZoneId_Type()
)
cucsLsFcZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneId.setStatus("current")
_CucsLsFcZoneIdentity_Type = SnmpAdminString
_CucsLsFcZoneIdentity_Object = MibTableColumn
cucsLsFcZoneIdentity = _CucsLsFcZoneIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 6),
    _CucsLsFcZoneIdentity_Type()
)
cucsLsFcZoneIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneIdentity.setStatus("current")
_CucsLsFcZoneIniName_Type = SnmpAdminString
_CucsLsFcZoneIniName_Object = MibTableColumn
cucsLsFcZoneIniName = _CucsLsFcZoneIniName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 7),
    _CucsLsFcZoneIniName_Type()
)
cucsLsFcZoneIniName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneIniName.setStatus("current")
_CucsLsFcZoneName_Type = SnmpAdminString
_CucsLsFcZoneName_Object = MibTableColumn
cucsLsFcZoneName = _CucsLsFcZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 8),
    _CucsLsFcZoneName_Type()
)
cucsLsFcZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneName.setStatus("current")
_CucsLsFcZoneOperState_Type = CucsLsFcZoneState
_CucsLsFcZoneOperState_Object = MibTableColumn
cucsLsFcZoneOperState = _CucsLsFcZoneOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 9),
    _CucsLsFcZoneOperState_Type()
)
cucsLsFcZoneOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneOperState.setStatus("current")
_CucsLsFcZonePeerDn_Type = SnmpAdminString
_CucsLsFcZonePeerDn_Object = MibTableColumn
cucsLsFcZonePeerDn = _CucsLsFcZonePeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 10),
    _CucsLsFcZonePeerDn_Type()
)
cucsLsFcZonePeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZonePeerDn.setStatus("current")
_CucsLsFcZoneSwitchId_Type = CucsNetworkSwitchId
_CucsLsFcZoneSwitchId_Object = MibTableColumn
cucsLsFcZoneSwitchId = _CucsLsFcZoneSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 11),
    _CucsLsFcZoneSwitchId_Type()
)
cucsLsFcZoneSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneSwitchId.setStatus("current")
_CucsLsFcZoneUsrLbl_Type = SnmpAdminString
_CucsLsFcZoneUsrLbl_Object = MibTableColumn
cucsLsFcZoneUsrLbl = _CucsLsFcZoneUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 12),
    _CucsLsFcZoneUsrLbl_Type()
)
cucsLsFcZoneUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneUsrLbl.setStatus("current")
_CucsLsFcZoneVnetId_Type = Gauge32
_CucsLsFcZoneVnetId_Object = MibTableColumn
cucsLsFcZoneVnetId = _CucsLsFcZoneVnetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 13),
    _CucsLsFcZoneVnetId_Type()
)
cucsLsFcZoneVnetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneVnetId.setStatus("current")
_CucsLsFcZoneZoningType_Type = CucsStorageFcZoningType
_CucsLsFcZoneZoningType_Object = MibTableColumn
cucsLsFcZoneZoningType = _CucsLsFcZoneZoningType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 11, 1, 14),
    _CucsLsFcZoneZoningType_Type()
)
cucsLsFcZoneZoningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneZoningType.setStatus("current")
_CucsLsFcZoneGroupTable_Object = MibTable
cucsLsFcZoneGroupTable = _CucsLsFcZoneGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 12)
)
if mibBuilder.loadTexts:
    cucsLsFcZoneGroupTable.setStatus("current")
_CucsLsFcZoneGroupEntry_Object = MibTableRow
cucsLsFcZoneGroupEntry = _CucsLsFcZoneGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 12, 1)
)
cucsLsFcZoneGroupEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsFcZoneGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsFcZoneGroupEntry.setStatus("current")
_CucsLsFcZoneGroupInstanceId_Type = CucsManagedObjectId
_CucsLsFcZoneGroupInstanceId_Object = MibTableColumn
cucsLsFcZoneGroupInstanceId = _CucsLsFcZoneGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 12, 1, 1),
    _CucsLsFcZoneGroupInstanceId_Type()
)
cucsLsFcZoneGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsFcZoneGroupInstanceId.setStatus("current")
_CucsLsFcZoneGroupDn_Type = CucsManagedObjectDn
_CucsLsFcZoneGroupDn_Object = MibTableColumn
cucsLsFcZoneGroupDn = _CucsLsFcZoneGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 12, 1, 2),
    _CucsLsFcZoneGroupDn_Type()
)
cucsLsFcZoneGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneGroupDn.setStatus("current")
_CucsLsFcZoneGroupRn_Type = SnmpAdminString
_CucsLsFcZoneGroupRn_Object = MibTableColumn
cucsLsFcZoneGroupRn = _CucsLsFcZoneGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 12, 1, 3),
    _CucsLsFcZoneGroupRn_Type()
)
cucsLsFcZoneGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneGroupRn.setStatus("current")
_CucsLsFcZoneGroupId_Type = Gauge32
_CucsLsFcZoneGroupId_Object = MibTableColumn
cucsLsFcZoneGroupId = _CucsLsFcZoneGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 12, 1, 4),
    _CucsLsFcZoneGroupId_Type()
)
cucsLsFcZoneGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneGroupId.setStatus("current")
_CucsLsFcZoneGroupName_Type = SnmpAdminString
_CucsLsFcZoneGroupName_Object = MibTableColumn
cucsLsFcZoneGroupName = _CucsLsFcZoneGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 12, 1, 5),
    _CucsLsFcZoneGroupName_Type()
)
cucsLsFcZoneGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneGroupName.setStatus("current")
_CucsLsFcZoneGroupSwitchId_Type = CucsLsFcZoneGroupSwitchId
_CucsLsFcZoneGroupSwitchId_Object = MibTableColumn
cucsLsFcZoneGroupSwitchId = _CucsLsFcZoneGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 12, 1, 6),
    _CucsLsFcZoneGroupSwitchId_Type()
)
cucsLsFcZoneGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsFcZoneGroupSwitchId.setStatus("current")
_CucsLsServerFsmTable_Object = MibTable
cucsLsServerFsmTable = _CucsLsServerFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13)
)
if mibBuilder.loadTexts:
    cucsLsServerFsmTable.setStatus("current")
_CucsLsServerFsmEntry_Object = MibTableRow
cucsLsServerFsmEntry = _CucsLsServerFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13, 1)
)
cucsLsServerFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsServerFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsServerFsmEntry.setStatus("current")
_CucsLsServerFsmInstanceId_Type = CucsManagedObjectId
_CucsLsServerFsmInstanceId_Object = MibTableColumn
cucsLsServerFsmInstanceId = _CucsLsServerFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13, 1, 1),
    _CucsLsServerFsmInstanceId_Type()
)
cucsLsServerFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsServerFsmInstanceId.setStatus("current")
_CucsLsServerFsmDn_Type = CucsManagedObjectDn
_CucsLsServerFsmDn_Object = MibTableColumn
cucsLsServerFsmDn = _CucsLsServerFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13, 1, 2),
    _CucsLsServerFsmDn_Type()
)
cucsLsServerFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmDn.setStatus("current")
_CucsLsServerFsmRn_Type = SnmpAdminString
_CucsLsServerFsmRn_Object = MibTableColumn
cucsLsServerFsmRn = _CucsLsServerFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13, 1, 3),
    _CucsLsServerFsmRn_Type()
)
cucsLsServerFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmRn.setStatus("current")
_CucsLsServerFsmCompletionTime_Type = DateAndTime
_CucsLsServerFsmCompletionTime_Object = MibTableColumn
cucsLsServerFsmCompletionTime = _CucsLsServerFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13, 1, 4),
    _CucsLsServerFsmCompletionTime_Type()
)
cucsLsServerFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmCompletionTime.setStatus("current")
_CucsLsServerFsmCurrentFsm_Type = CucsLsServerFsmCurrentFsm
_CucsLsServerFsmCurrentFsm_Object = MibTableColumn
cucsLsServerFsmCurrentFsm = _CucsLsServerFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13, 1, 5),
    _CucsLsServerFsmCurrentFsm_Type()
)
cucsLsServerFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmCurrentFsm.setStatus("current")
_CucsLsServerFsmDescrData_Type = SnmpAdminString
_CucsLsServerFsmDescrData_Object = MibTableColumn
cucsLsServerFsmDescrData = _CucsLsServerFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13, 1, 6),
    _CucsLsServerFsmDescrData_Type()
)
cucsLsServerFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmDescrData.setStatus("current")
_CucsLsServerFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsLsServerFsmFsmStatus_Object = MibTableColumn
cucsLsServerFsmFsmStatus = _CucsLsServerFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13, 1, 7),
    _CucsLsServerFsmFsmStatus_Type()
)
cucsLsServerFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmFsmStatus.setStatus("current")
_CucsLsServerFsmProgress_Type = Gauge32
_CucsLsServerFsmProgress_Object = MibTableColumn
cucsLsServerFsmProgress = _CucsLsServerFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13, 1, 8),
    _CucsLsServerFsmProgress_Type()
)
cucsLsServerFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmProgress.setStatus("current")
_CucsLsServerFsmRmtErrCode_Type = Gauge32
_CucsLsServerFsmRmtErrCode_Object = MibTableColumn
cucsLsServerFsmRmtErrCode = _CucsLsServerFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13, 1, 9),
    _CucsLsServerFsmRmtErrCode_Type()
)
cucsLsServerFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmRmtErrCode.setStatus("current")
_CucsLsServerFsmRmtErrDescr_Type = SnmpAdminString
_CucsLsServerFsmRmtErrDescr_Object = MibTableColumn
cucsLsServerFsmRmtErrDescr = _CucsLsServerFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13, 1, 10),
    _CucsLsServerFsmRmtErrDescr_Type()
)
cucsLsServerFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmRmtErrDescr.setStatus("current")
_CucsLsServerFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsLsServerFsmRmtRslt_Object = MibTableColumn
cucsLsServerFsmRmtRslt = _CucsLsServerFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 13, 1, 11),
    _CucsLsServerFsmRmtRslt_Type()
)
cucsLsServerFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmRmtRslt.setStatus("current")
_CucsLsServerFsmStageTable_Object = MibTable
cucsLsServerFsmStageTable = _CucsLsServerFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 14)
)
if mibBuilder.loadTexts:
    cucsLsServerFsmStageTable.setStatus("current")
_CucsLsServerFsmStageEntry_Object = MibTableRow
cucsLsServerFsmStageEntry = _CucsLsServerFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 14, 1)
)
cucsLsServerFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsServerFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsServerFsmStageEntry.setStatus("current")
_CucsLsServerFsmStageInstanceId_Type = CucsManagedObjectId
_CucsLsServerFsmStageInstanceId_Object = MibTableColumn
cucsLsServerFsmStageInstanceId = _CucsLsServerFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 14, 1, 1),
    _CucsLsServerFsmStageInstanceId_Type()
)
cucsLsServerFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsServerFsmStageInstanceId.setStatus("current")
_CucsLsServerFsmStageDn_Type = CucsManagedObjectDn
_CucsLsServerFsmStageDn_Object = MibTableColumn
cucsLsServerFsmStageDn = _CucsLsServerFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 14, 1, 2),
    _CucsLsServerFsmStageDn_Type()
)
cucsLsServerFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmStageDn.setStatus("current")
_CucsLsServerFsmStageRn_Type = SnmpAdminString
_CucsLsServerFsmStageRn_Object = MibTableColumn
cucsLsServerFsmStageRn = _CucsLsServerFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 14, 1, 3),
    _CucsLsServerFsmStageRn_Type()
)
cucsLsServerFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmStageRn.setStatus("current")
_CucsLsServerFsmStageDescrData_Type = SnmpAdminString
_CucsLsServerFsmStageDescrData_Object = MibTableColumn
cucsLsServerFsmStageDescrData = _CucsLsServerFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 14, 1, 4),
    _CucsLsServerFsmStageDescrData_Type()
)
cucsLsServerFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmStageDescrData.setStatus("current")
_CucsLsServerFsmStageLastUpdateTime_Type = DateAndTime
_CucsLsServerFsmStageLastUpdateTime_Object = MibTableColumn
cucsLsServerFsmStageLastUpdateTime = _CucsLsServerFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 14, 1, 5),
    _CucsLsServerFsmStageLastUpdateTime_Type()
)
cucsLsServerFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmStageLastUpdateTime.setStatus("current")
_CucsLsServerFsmStageName_Type = CucsLsServerFsmStageName
_CucsLsServerFsmStageName_Object = MibTableColumn
cucsLsServerFsmStageName = _CucsLsServerFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 14, 1, 6),
    _CucsLsServerFsmStageName_Type()
)
cucsLsServerFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmStageName.setStatus("current")
_CucsLsServerFsmStageOrder_Type = Gauge32
_CucsLsServerFsmStageOrder_Object = MibTableColumn
cucsLsServerFsmStageOrder = _CucsLsServerFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 14, 1, 7),
    _CucsLsServerFsmStageOrder_Type()
)
cucsLsServerFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmStageOrder.setStatus("current")
_CucsLsServerFsmStageRetry_Type = Gauge32
_CucsLsServerFsmStageRetry_Object = MibTableColumn
cucsLsServerFsmStageRetry = _CucsLsServerFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 14, 1, 8),
    _CucsLsServerFsmStageRetry_Type()
)
cucsLsServerFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmStageRetry.setStatus("current")
_CucsLsServerFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsLsServerFsmStageStageStatus_Object = MibTableColumn
cucsLsServerFsmStageStageStatus = _CucsLsServerFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 14, 1, 9),
    _CucsLsServerFsmStageStageStatus_Type()
)
cucsLsServerFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerFsmStageStageStatus.setStatus("current")
_CucsLsVConAssignTable_Object = MibTable
cucsLsVConAssignTable = _CucsLsVConAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 15)
)
if mibBuilder.loadTexts:
    cucsLsVConAssignTable.setStatus("current")
_CucsLsVConAssignEntry_Object = MibTableRow
cucsLsVConAssignEntry = _CucsLsVConAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 15, 1)
)
cucsLsVConAssignEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsVConAssignInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsVConAssignEntry.setStatus("current")
_CucsLsVConAssignInstanceId_Type = CucsManagedObjectId
_CucsLsVConAssignInstanceId_Object = MibTableColumn
cucsLsVConAssignInstanceId = _CucsLsVConAssignInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 15, 1, 1),
    _CucsLsVConAssignInstanceId_Type()
)
cucsLsVConAssignInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsVConAssignInstanceId.setStatus("current")
_CucsLsVConAssignDn_Type = CucsManagedObjectDn
_CucsLsVConAssignDn_Object = MibTableColumn
cucsLsVConAssignDn = _CucsLsVConAssignDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 15, 1, 2),
    _CucsLsVConAssignDn_Type()
)
cucsLsVConAssignDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVConAssignDn.setStatus("current")
_CucsLsVConAssignRn_Type = SnmpAdminString
_CucsLsVConAssignRn_Object = MibTableColumn
cucsLsVConAssignRn = _CucsLsVConAssignRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 15, 1, 3),
    _CucsLsVConAssignRn_Type()
)
cucsLsVConAssignRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVConAssignRn.setStatus("current")
_CucsLsVConAssignAdminVcon_Type = SnmpAdminString
_CucsLsVConAssignAdminVcon_Object = MibTableColumn
cucsLsVConAssignAdminVcon = _CucsLsVConAssignAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 15, 1, 4),
    _CucsLsVConAssignAdminVcon_Type()
)
cucsLsVConAssignAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVConAssignAdminVcon.setStatus("current")
_CucsLsVConAssignOrder_Type = Gauge32
_CucsLsVConAssignOrder_Object = MibTableColumn
cucsLsVConAssignOrder = _CucsLsVConAssignOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 15, 1, 5),
    _CucsLsVConAssignOrder_Type()
)
cucsLsVConAssignOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVConAssignOrder.setStatus("current")
_CucsLsVConAssignTransport_Type = CucsFabricVConTransportPref
_CucsLsVConAssignTransport_Object = MibTableColumn
cucsLsVConAssignTransport = _CucsLsVConAssignTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 15, 1, 6),
    _CucsLsVConAssignTransport_Type()
)
cucsLsVConAssignTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVConAssignTransport.setStatus("current")
_CucsLsVConAssignVnicName_Type = SnmpAdminString
_CucsLsVConAssignVnicName_Object = MibTableColumn
cucsLsVConAssignVnicName = _CucsLsVConAssignVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 15, 1, 7),
    _CucsLsVConAssignVnicName_Type()
)
cucsLsVConAssignVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVConAssignVnicName.setStatus("current")
_CucsLsVConAssignPropAcl_Type = Unsigned64
_CucsLsVConAssignPropAcl_Object = MibTableColumn
cucsLsVConAssignPropAcl = _CucsLsVConAssignPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 15, 1, 8),
    _CucsLsVConAssignPropAcl_Type()
)
cucsLsVConAssignPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVConAssignPropAcl.setStatus("current")
_CucsLsVConAssignAdminHostPort_Type = CucsFabricHostPortId
_CucsLsVConAssignAdminHostPort_Object = MibTableColumn
cucsLsVConAssignAdminHostPort = _CucsLsVConAssignAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 15, 1, 9),
    _CucsLsVConAssignAdminHostPort_Type()
)
cucsLsVConAssignAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsVConAssignAdminHostPort.setStatus("current")
_CucsLsZoneInitiatorMemberTable_Object = MibTable
cucsLsZoneInitiatorMemberTable = _CucsLsZoneInitiatorMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 16)
)
if mibBuilder.loadTexts:
    cucsLsZoneInitiatorMemberTable.setStatus("current")
_CucsLsZoneInitiatorMemberEntry_Object = MibTableRow
cucsLsZoneInitiatorMemberEntry = _CucsLsZoneInitiatorMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 16, 1)
)
cucsLsZoneInitiatorMemberEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsZoneInitiatorMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsZoneInitiatorMemberEntry.setStatus("current")
_CucsLsZoneInitiatorMemberInstanceId_Type = CucsManagedObjectId
_CucsLsZoneInitiatorMemberInstanceId_Object = MibTableColumn
cucsLsZoneInitiatorMemberInstanceId = _CucsLsZoneInitiatorMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 16, 1, 1),
    _CucsLsZoneInitiatorMemberInstanceId_Type()
)
cucsLsZoneInitiatorMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsZoneInitiatorMemberInstanceId.setStatus("current")
_CucsLsZoneInitiatorMemberDn_Type = CucsManagedObjectDn
_CucsLsZoneInitiatorMemberDn_Object = MibTableColumn
cucsLsZoneInitiatorMemberDn = _CucsLsZoneInitiatorMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 16, 1, 2),
    _CucsLsZoneInitiatorMemberDn_Type()
)
cucsLsZoneInitiatorMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsZoneInitiatorMemberDn.setStatus("current")
_CucsLsZoneInitiatorMemberRn_Type = SnmpAdminString
_CucsLsZoneInitiatorMemberRn_Object = MibTableColumn
cucsLsZoneInitiatorMemberRn = _CucsLsZoneInitiatorMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 16, 1, 3),
    _CucsLsZoneInitiatorMemberRn_Type()
)
cucsLsZoneInitiatorMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsZoneInitiatorMemberRn.setStatus("current")
_CucsLsZoneInitiatorMemberEpDn_Type = SnmpAdminString
_CucsLsZoneInitiatorMemberEpDn_Object = MibTableColumn
cucsLsZoneInitiatorMemberEpDn = _CucsLsZoneInitiatorMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 16, 1, 4),
    _CucsLsZoneInitiatorMemberEpDn_Type()
)
cucsLsZoneInitiatorMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsZoneInitiatorMemberEpDn.setStatus("current")
_CucsLsZoneInitiatorMemberName_Type = SnmpAdminString
_CucsLsZoneInitiatorMemberName_Object = MibTableColumn
cucsLsZoneInitiatorMemberName = _CucsLsZoneInitiatorMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 16, 1, 5),
    _CucsLsZoneInitiatorMemberName_Type()
)
cucsLsZoneInitiatorMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsZoneInitiatorMemberName.setStatus("current")
_CucsLsZoneInitiatorMemberUsrLbl_Type = SnmpAdminString
_CucsLsZoneInitiatorMemberUsrLbl_Object = MibTableColumn
cucsLsZoneInitiatorMemberUsrLbl = _CucsLsZoneInitiatorMemberUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 16, 1, 6),
    _CucsLsZoneInitiatorMemberUsrLbl_Type()
)
cucsLsZoneInitiatorMemberUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsZoneInitiatorMemberUsrLbl.setStatus("current")
_CucsLsZoneInitiatorMemberWwpn_Type = Unsigned64
_CucsLsZoneInitiatorMemberWwpn_Object = MibTableColumn
cucsLsZoneInitiatorMemberWwpn = _CucsLsZoneInitiatorMemberWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 16, 1, 7),
    _CucsLsZoneInitiatorMemberWwpn_Type()
)
cucsLsZoneInitiatorMemberWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsZoneInitiatorMemberWwpn.setStatus("current")
_CucsLsZoneTargetMemberTable_Object = MibTable
cucsLsZoneTargetMemberTable = _CucsLsZoneTargetMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 17)
)
if mibBuilder.loadTexts:
    cucsLsZoneTargetMemberTable.setStatus("current")
_CucsLsZoneTargetMemberEntry_Object = MibTableRow
cucsLsZoneTargetMemberEntry = _CucsLsZoneTargetMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 17, 1)
)
cucsLsZoneTargetMemberEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsZoneTargetMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsZoneTargetMemberEntry.setStatus("current")
_CucsLsZoneTargetMemberInstanceId_Type = CucsManagedObjectId
_CucsLsZoneTargetMemberInstanceId_Object = MibTableColumn
cucsLsZoneTargetMemberInstanceId = _CucsLsZoneTargetMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 17, 1, 1),
    _CucsLsZoneTargetMemberInstanceId_Type()
)
cucsLsZoneTargetMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsZoneTargetMemberInstanceId.setStatus("current")
_CucsLsZoneTargetMemberDn_Type = CucsManagedObjectDn
_CucsLsZoneTargetMemberDn_Object = MibTableColumn
cucsLsZoneTargetMemberDn = _CucsLsZoneTargetMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 17, 1, 2),
    _CucsLsZoneTargetMemberDn_Type()
)
cucsLsZoneTargetMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsZoneTargetMemberDn.setStatus("current")
_CucsLsZoneTargetMemberRn_Type = SnmpAdminString
_CucsLsZoneTargetMemberRn_Object = MibTableColumn
cucsLsZoneTargetMemberRn = _CucsLsZoneTargetMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 17, 1, 3),
    _CucsLsZoneTargetMemberRn_Type()
)
cucsLsZoneTargetMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsZoneTargetMemberRn.setStatus("current")
_CucsLsZoneTargetMemberEpDn_Type = SnmpAdminString
_CucsLsZoneTargetMemberEpDn_Object = MibTableColumn
cucsLsZoneTargetMemberEpDn = _CucsLsZoneTargetMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 17, 1, 4),
    _CucsLsZoneTargetMemberEpDn_Type()
)
cucsLsZoneTargetMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsZoneTargetMemberEpDn.setStatus("current")
_CucsLsZoneTargetMemberName_Type = SnmpAdminString
_CucsLsZoneTargetMemberName_Object = MibTableColumn
cucsLsZoneTargetMemberName = _CucsLsZoneTargetMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 17, 1, 5),
    _CucsLsZoneTargetMemberName_Type()
)
cucsLsZoneTargetMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsZoneTargetMemberName.setStatus("current")
_CucsLsZoneTargetMemberUsrLbl_Type = SnmpAdminString
_CucsLsZoneTargetMemberUsrLbl_Object = MibTableColumn
cucsLsZoneTargetMemberUsrLbl = _CucsLsZoneTargetMemberUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 17, 1, 6),
    _CucsLsZoneTargetMemberUsrLbl_Type()
)
cucsLsZoneTargetMemberUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsZoneTargetMemberUsrLbl.setStatus("current")
_CucsLsZoneTargetMemberWwpn_Type = Unsigned64
_CucsLsZoneTargetMemberWwpn_Object = MibTableColumn
cucsLsZoneTargetMemberWwpn = _CucsLsZoneTargetMemberWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 17, 1, 7),
    _CucsLsZoneTargetMemberWwpn_Type()
)
cucsLsZoneTargetMemberWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsZoneTargetMemberWwpn.setStatus("current")
_CucsLsServerExtensionTable_Object = MibTable
cucsLsServerExtensionTable = _CucsLsServerExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 18)
)
if mibBuilder.loadTexts:
    cucsLsServerExtensionTable.setStatus("current")
_CucsLsServerExtensionEntry_Object = MibTableRow
cucsLsServerExtensionEntry = _CucsLsServerExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 18, 1)
)
cucsLsServerExtensionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsServerExtensionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsServerExtensionEntry.setStatus("current")
_CucsLsServerExtensionInstanceId_Type = CucsManagedObjectId
_CucsLsServerExtensionInstanceId_Object = MibTableColumn
cucsLsServerExtensionInstanceId = _CucsLsServerExtensionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 18, 1, 1),
    _CucsLsServerExtensionInstanceId_Type()
)
cucsLsServerExtensionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsServerExtensionInstanceId.setStatus("current")
_CucsLsServerExtensionDn_Type = CucsManagedObjectDn
_CucsLsServerExtensionDn_Object = MibTableColumn
cucsLsServerExtensionDn = _CucsLsServerExtensionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 18, 1, 2),
    _CucsLsServerExtensionDn_Type()
)
cucsLsServerExtensionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerExtensionDn.setStatus("current")
_CucsLsServerExtensionRn_Type = SnmpAdminString
_CucsLsServerExtensionRn_Object = MibTableColumn
cucsLsServerExtensionRn = _CucsLsServerExtensionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 18, 1, 3),
    _CucsLsServerExtensionRn_Type()
)
cucsLsServerExtensionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerExtensionRn.setStatus("current")
_CucsLsServerExtensionGuid_Type = SnmpAdminString
_CucsLsServerExtensionGuid_Object = MibTableColumn
cucsLsServerExtensionGuid = _CucsLsServerExtensionGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 18, 1, 4),
    _CucsLsServerExtensionGuid_Type()
)
cucsLsServerExtensionGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerExtensionGuid.setStatus("current")
_CucsLsServerExtensionVersion_Type = Gauge32
_CucsLsServerExtensionVersion_Object = MibTableColumn
cucsLsServerExtensionVersion = _CucsLsServerExtensionVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 18, 1, 5),
    _CucsLsServerExtensionVersion_Type()
)
cucsLsServerExtensionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerExtensionVersion.setStatus("current")
_CucsLsServerExtensionPropAcl_Type = Unsigned64
_CucsLsServerExtensionPropAcl_Object = MibTableColumn
cucsLsServerExtensionPropAcl = _CucsLsServerExtensionPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 18, 1, 6),
    _CucsLsServerExtensionPropAcl_Type()
)
cucsLsServerExtensionPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerExtensionPropAcl.setStatus("current")
_CucsLsServerExtensionVlanGrpRequestComputeTime_Type = DateAndTime
_CucsLsServerExtensionVlanGrpRequestComputeTime_Object = MibTableColumn
cucsLsServerExtensionVlanGrpRequestComputeTime = _CucsLsServerExtensionVlanGrpRequestComputeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 18, 1, 7),
    _CucsLsServerExtensionVlanGrpRequestComputeTime_Type()
)
cucsLsServerExtensionVlanGrpRequestComputeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsServerExtensionVlanGrpRequestComputeTime.setStatus("current")
_CucsLsUuidHistoryTable_Object = MibTable
cucsLsUuidHistoryTable = _CucsLsUuidHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 19)
)
if mibBuilder.loadTexts:
    cucsLsUuidHistoryTable.setStatus("current")
_CucsLsUuidHistoryEntry_Object = MibTableRow
cucsLsUuidHistoryEntry = _CucsLsUuidHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 19, 1)
)
cucsLsUuidHistoryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsUuidHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsUuidHistoryEntry.setStatus("current")
_CucsLsUuidHistoryInstanceId_Type = CucsManagedObjectId
_CucsLsUuidHistoryInstanceId_Object = MibTableColumn
cucsLsUuidHistoryInstanceId = _CucsLsUuidHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 19, 1, 1),
    _CucsLsUuidHistoryInstanceId_Type()
)
cucsLsUuidHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsUuidHistoryInstanceId.setStatus("current")
_CucsLsUuidHistoryDn_Type = CucsManagedObjectDn
_CucsLsUuidHistoryDn_Object = MibTableColumn
cucsLsUuidHistoryDn = _CucsLsUuidHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 19, 1, 2),
    _CucsLsUuidHistoryDn_Type()
)
cucsLsUuidHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsUuidHistoryDn.setStatus("current")
_CucsLsUuidHistoryRn_Type = SnmpAdminString
_CucsLsUuidHistoryRn_Object = MibTableColumn
cucsLsUuidHistoryRn = _CucsLsUuidHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 19, 1, 3),
    _CucsLsUuidHistoryRn_Type()
)
cucsLsUuidHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsUuidHistoryRn.setStatus("current")
_CucsLsUuidHistoryOlduuid_Type = SnmpAdminString
_CucsLsUuidHistoryOlduuid_Object = MibTableColumn
cucsLsUuidHistoryOlduuid = _CucsLsUuidHistoryOlduuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 19, 1, 4),
    _CucsLsUuidHistoryOlduuid_Type()
)
cucsLsUuidHistoryOlduuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsUuidHistoryOlduuid.setStatus("current")
_CucsLsIssuesTable_Object = MibTable
cucsLsIssuesTable = _CucsLsIssuesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 20)
)
if mibBuilder.loadTexts:
    cucsLsIssuesTable.setStatus("current")
_CucsLsIssuesEntry_Object = MibTableRow
cucsLsIssuesEntry = _CucsLsIssuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 20, 1)
)
cucsLsIssuesEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsIssuesInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsIssuesEntry.setStatus("current")
_CucsLsIssuesInstanceId_Type = CucsManagedObjectId
_CucsLsIssuesInstanceId_Object = MibTableColumn
cucsLsIssuesInstanceId = _CucsLsIssuesInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 20, 1, 1),
    _CucsLsIssuesInstanceId_Type()
)
cucsLsIssuesInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsIssuesInstanceId.setStatus("current")
_CucsLsIssuesDn_Type = CucsManagedObjectDn
_CucsLsIssuesDn_Object = MibTableColumn
cucsLsIssuesDn = _CucsLsIssuesDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 20, 1, 2),
    _CucsLsIssuesDn_Type()
)
cucsLsIssuesDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsIssuesDn.setStatus("current")
_CucsLsIssuesRn_Type = SnmpAdminString
_CucsLsIssuesRn_Object = MibTableColumn
cucsLsIssuesRn = _CucsLsIssuesRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 20, 1, 3),
    _CucsLsIssuesRn_Type()
)
cucsLsIssuesRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsIssuesRn.setStatus("current")
_CucsLsIssuesIscsiConfigIssues_Type = CucsVnicIScsiConfigIssues
_CucsLsIssuesIscsiConfigIssues_Object = MibTableColumn
cucsLsIssuesIscsiConfigIssues = _CucsLsIssuesIscsiConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 20, 1, 4),
    _CucsLsIssuesIscsiConfigIssues_Type()
)
cucsLsIssuesIscsiConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsIssuesIscsiConfigIssues.setStatus("current")
_CucsLsIssuesNetworkConfigIssues_Type = CucsNetworkConfigIssues
_CucsLsIssuesNetworkConfigIssues_Object = MibTableColumn
cucsLsIssuesNetworkConfigIssues = _CucsLsIssuesNetworkConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 20, 1, 5),
    _CucsLsIssuesNetworkConfigIssues_Type()
)
cucsLsIssuesNetworkConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsIssuesNetworkConfigIssues.setStatus("current")
_CucsLsIssuesServerConfigIssues_Type = CucsServerConfigIssues
_CucsLsIssuesServerConfigIssues_Object = MibTableColumn
cucsLsIssuesServerConfigIssues = _CucsLsIssuesServerConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 20, 1, 6),
    _CucsLsIssuesServerConfigIssues_Type()
)
cucsLsIssuesServerConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsIssuesServerConfigIssues.setStatus("current")
_CucsLsIssuesStorageConfigIssues_Type = CucsStorageConfigIssues
_CucsLsIssuesStorageConfigIssues_Object = MibTableColumn
cucsLsIssuesStorageConfigIssues = _CucsLsIssuesStorageConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 20, 1, 7),
    _CucsLsIssuesStorageConfigIssues_Type()
)
cucsLsIssuesStorageConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsIssuesStorageConfigIssues.setStatus("current")
_CucsLsIssuesVnicConfigIssues_Type = CucsVnicConfigIssues
_CucsLsIssuesVnicConfigIssues_Object = MibTableColumn
cucsLsIssuesVnicConfigIssues = _CucsLsIssuesVnicConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 20, 1, 8),
    _CucsLsIssuesVnicConfigIssues_Type()
)
cucsLsIssuesVnicConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsIssuesVnicConfigIssues.setStatus("current")
_CucsLsIssuesConfigWarnings_Type = CucsLsConfigWarnings
_CucsLsIssuesConfigWarnings_Object = MibTableColumn
cucsLsIssuesConfigWarnings = _CucsLsIssuesConfigWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 20, 1, 9),
    _CucsLsIssuesConfigWarnings_Type()
)
cucsLsIssuesConfigWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsIssuesConfigWarnings.setStatus("current")
_CucsLsIssuesPropAcl_Type = Unsigned64
_CucsLsIssuesPropAcl_Object = MibTableColumn
cucsLsIssuesPropAcl = _CucsLsIssuesPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 20, 1, 10),
    _CucsLsIssuesPropAcl_Type()
)
cucsLsIssuesPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsIssuesPropAcl.setStatus("current")
_CucsLsIdentityInfoTable_Object = MibTable
cucsLsIdentityInfoTable = _CucsLsIdentityInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 21)
)
if mibBuilder.loadTexts:
    cucsLsIdentityInfoTable.setStatus("current")
_CucsLsIdentityInfoEntry_Object = MibTableRow
cucsLsIdentityInfoEntry = _CucsLsIdentityInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 21, 1)
)
cucsLsIdentityInfoEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LS-MIB", "cucsLsIdentityInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLsIdentityInfoEntry.setStatus("current")
_CucsLsIdentityInfoInstanceId_Type = CucsManagedObjectId
_CucsLsIdentityInfoInstanceId_Object = MibTableColumn
cucsLsIdentityInfoInstanceId = _CucsLsIdentityInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 21, 1, 1),
    _CucsLsIdentityInfoInstanceId_Type()
)
cucsLsIdentityInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLsIdentityInfoInstanceId.setStatus("current")
_CucsLsIdentityInfoDn_Type = CucsManagedObjectDn
_CucsLsIdentityInfoDn_Object = MibTableColumn
cucsLsIdentityInfoDn = _CucsLsIdentityInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 21, 1, 2),
    _CucsLsIdentityInfoDn_Type()
)
cucsLsIdentityInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsIdentityInfoDn.setStatus("current")
_CucsLsIdentityInfoRn_Type = SnmpAdminString
_CucsLsIdentityInfoRn_Object = MibTableColumn
cucsLsIdentityInfoRn = _CucsLsIdentityInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 21, 1, 3),
    _CucsLsIdentityInfoRn_Type()
)
cucsLsIdentityInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsIdentityInfoRn.setStatus("current")
_CucsLsIdentityInfoUuidIdentityState_Type = CucsLsUUIDIdentityState
_CucsLsIdentityInfoUuidIdentityState_Object = MibTableColumn
cucsLsIdentityInfoUuidIdentityState = _CucsLsIdentityInfoUuidIdentityState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 26, 21, 1, 4),
    _CucsLsIdentityInfoUuidIdentityState_Type()
)
cucsLsIdentityInfoUuidIdentityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLsIdentityInfoUuidIdentityState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-LS-MIB",
    **{"cucsLsObjects": cucsLsObjects,
       "cucsLsAgentPolicyTable": cucsLsAgentPolicyTable,
       "cucsLsAgentPolicyEntry": cucsLsAgentPolicyEntry,
       "cucsLsAgentPolicyInstanceId": cucsLsAgentPolicyInstanceId,
       "cucsLsAgentPolicyDn": cucsLsAgentPolicyDn,
       "cucsLsAgentPolicyRn": cucsLsAgentPolicyRn,
       "cucsLsAgentPolicyCapability": cucsLsAgentPolicyCapability,
       "cucsLsAgentPolicyDescr": cucsLsAgentPolicyDescr,
       "cucsLsAgentPolicyIntId": cucsLsAgentPolicyIntId,
       "cucsLsAgentPolicyMode": cucsLsAgentPolicyMode,
       "cucsLsAgentPolicyName": cucsLsAgentPolicyName,
       "cucsLsAgentPolicyPolicyLevel": cucsLsAgentPolicyPolicyLevel,
       "cucsLsAgentPolicyPolicyOwner": cucsLsAgentPolicyPolicyOwner,
       "cucsLsBindingTable": cucsLsBindingTable,
       "cucsLsBindingEntry": cucsLsBindingEntry,
       "cucsLsBindingInstanceId": cucsLsBindingInstanceId,
       "cucsLsBindingDn": cucsLsBindingDn,
       "cucsLsBindingRn": cucsLsBindingRn,
       "cucsLsBindingComputeEpDn": cucsLsBindingComputeEpDn,
       "cucsLsBindingName": cucsLsBindingName,
       "cucsLsBindingPnDn": cucsLsBindingPnDn,
       "cucsLsBindingRestrictMigration": cucsLsBindingRestrictMigration,
       "cucsLsBindingAssignedToDn": cucsLsBindingAssignedToDn,
       "cucsLsBindingIssues": cucsLsBindingIssues,
       "cucsLsBindingOperState": cucsLsBindingOperState,
       "cucsLsBindingPropAcl": cucsLsBindingPropAcl,
       "cucsLsPowerTable": cucsLsPowerTable,
       "cucsLsPowerEntry": cucsLsPowerEntry,
       "cucsLsPowerInstanceId": cucsLsPowerInstanceId,
       "cucsLsPowerDn": cucsLsPowerDn,
       "cucsLsPowerRn": cucsLsPowerRn,
       "cucsLsPowerState": cucsLsPowerState,
       "cucsLsPowerPropAcl": cucsLsPowerPropAcl,
       "cucsLsRequirementTable": cucsLsRequirementTable,
       "cucsLsRequirementEntry": cucsLsRequirementEntry,
       "cucsLsRequirementInstanceId": cucsLsRequirementInstanceId,
       "cucsLsRequirementDn": cucsLsRequirementDn,
       "cucsLsRequirementRn": cucsLsRequirementRn,
       "cucsLsRequirementComputeEpDn": cucsLsRequirementComputeEpDn,
       "cucsLsRequirementName": cucsLsRequirementName,
       "cucsLsRequirementPnPoolDn": cucsLsRequirementPnPoolDn,
       "cucsLsRequirementQualifier": cucsLsRequirementQualifier,
       "cucsLsRequirementRestrictMigration": cucsLsRequirementRestrictMigration,
       "cucsLsRequirementAssignedToDn": cucsLsRequirementAssignedToDn,
       "cucsLsRequirementIssues": cucsLsRequirementIssues,
       "cucsLsRequirementOperState": cucsLsRequirementOperState,
       "cucsLsRequirementPnDn": cucsLsRequirementPnDn,
       "cucsLsRequirementOperName": cucsLsRequirementOperName,
       "cucsLsServerTable": cucsLsServerTable,
       "cucsLsServerEntry": cucsLsServerEntry,
       "cucsLsServerInstanceId": cucsLsServerInstanceId,
       "cucsLsServerDn": cucsLsServerDn,
       "cucsLsServerRn": cucsLsServerRn,
       "cucsLsServerAgentPolicyName": cucsLsServerAgentPolicyName,
       "cucsLsServerAssignState": cucsLsServerAssignState,
       "cucsLsServerAssocState": cucsLsServerAssocState,
       "cucsLsServerBiosProfileName": cucsLsServerBiosProfileName,
       "cucsLsServerBootPolicyName": cucsLsServerBootPolicyName,
       "cucsLsServerConfigQualifier": cucsLsServerConfigQualifier,
       "cucsLsServerConfigState": cucsLsServerConfigState,
       "cucsLsServerDescr": cucsLsServerDescr,
       "cucsLsServerDynamicConPolicyName": cucsLsServerDynamicConPolicyName,
       "cucsLsServerExtIPState": cucsLsServerExtIPState,
       "cucsLsServerFltAggr": cucsLsServerFltAggr,
       "cucsLsServerHostFwPolicyName": cucsLsServerHostFwPolicyName,
       "cucsLsServerIdentPoolName": cucsLsServerIdentPoolName,
       "cucsLsServerIntId": cucsLsServerIntId,
       "cucsLsServerLocalDiskPolicyName": cucsLsServerLocalDiskPolicyName,
       "cucsLsServerMaintPolicyName": cucsLsServerMaintPolicyName,
       "cucsLsServerMgmtAccessPolicyName": cucsLsServerMgmtAccessPolicyName,
       "cucsLsServerMgmtFwPolicyName": cucsLsServerMgmtFwPolicyName,
       "cucsLsServerName": cucsLsServerName,
       "cucsLsServerOperBiosProfileName": cucsLsServerOperBiosProfileName,
       "cucsLsServerOperBootPolicyName": cucsLsServerOperBootPolicyName,
       "cucsLsServerOperDynamicConPolicyName": cucsLsServerOperDynamicConPolicyName,
       "cucsLsServerOperHostFwPolicyName": cucsLsServerOperHostFwPolicyName,
       "cucsLsServerOperIdentPoolName": cucsLsServerOperIdentPoolName,
       "cucsLsServerOperLocalDiskPolicyName": cucsLsServerOperLocalDiskPolicyName,
       "cucsLsServerOperMgmtAccessPolicyName": cucsLsServerOperMgmtAccessPolicyName,
       "cucsLsServerOperMgmtFwPolicyName": cucsLsServerOperMgmtFwPolicyName,
       "cucsLsServerOperScrubPolicyName": cucsLsServerOperScrubPolicyName,
       "cucsLsServerOperSolPolicyName": cucsLsServerOperSolPolicyName,
       "cucsLsServerOperSrcTemplName": cucsLsServerOperSrcTemplName,
       "cucsLsServerOperState": cucsLsServerOperState,
       "cucsLsServerOperStatsPolicyName": cucsLsServerOperStatsPolicyName,
       "cucsLsServerOperVconProfileName": cucsLsServerOperVconProfileName,
       "cucsLsServerOwner": cucsLsServerOwner,
       "cucsLsServerFsmFlags": cucsLsServerFsmFlags,
       "cucsLsServerPnDn": cucsLsServerPnDn,
       "cucsLsServerPowerPolicyName": cucsLsServerPowerPolicyName,
       "cucsLsServerScrubPolicyName": cucsLsServerScrubPolicyName,
       "cucsLsServerSolPolicyName": cucsLsServerSolPolicyName,
       "cucsLsServerSrcTemplName": cucsLsServerSrcTemplName,
       "cucsLsServerStatsPolicyName": cucsLsServerStatsPolicyName,
       "cucsLsServerType": cucsLsServerType,
       "cucsLsServerUsrLbl": cucsLsServerUsrLbl,
       "cucsLsServerUuid": cucsLsServerUuid,
       "cucsLsServerUuidSuffix": cucsLsServerUuidSuffix,
       "cucsLsServerVconProfileName": cucsLsServerVconProfileName,
       "cucsLsServerFsmDescr": cucsLsServerFsmDescr,
       "cucsLsServerFsmPrev": cucsLsServerFsmPrev,
       "cucsLsServerFsmProgr": cucsLsServerFsmProgr,
       "cucsLsServerFsmRmtInvErrCode": cucsLsServerFsmRmtInvErrCode,
       "cucsLsServerFsmRmtInvErrDescr": cucsLsServerFsmRmtInvErrDescr,
       "cucsLsServerFsmRmtInvRslt": cucsLsServerFsmRmtInvRslt,
       "cucsLsServerFsmStageDescr": cucsLsServerFsmStageDescr,
       "cucsLsServerFsmStamp": cucsLsServerFsmStamp,
       "cucsLsServerFsmStatus": cucsLsServerFsmStatus,
       "cucsLsServerFsmTry": cucsLsServerFsmTry,
       "cucsLsServerOperMaintPolicyName": cucsLsServerOperMaintPolicyName,
       "cucsLsServerOperPowerPolicyName": cucsLsServerOperPowerPolicyName,
       "cucsLsServerExtIPPoolName": cucsLsServerExtIPPoolName,
       "cucsLsServerOperExtIPPoolName": cucsLsServerOperExtIPPoolName,
       "cucsLsServerPolicyLevel": cucsLsServerPolicyLevel,
       "cucsLsServerPolicyOwner": cucsLsServerPolicyOwner,
       "cucsLsServerResolveRemote": cucsLsServerResolveRemote,
       "cucsLsServerKvmMgmtPolicyName": cucsLsServerKvmMgmtPolicyName,
       "cucsLsServerOperKvmMgmtPolicyName": cucsLsServerOperKvmMgmtPolicyName,
       "cucsLsServerOperVmediaPolicyName": cucsLsServerOperVmediaPolicyName,
       "cucsLsServerSvnicConfig": cucsLsServerSvnicConfig,
       "cucsLsServerVmediaPolicyName": cucsLsServerVmediaPolicyName,
       "cucsLsServerPropAcl": cucsLsServerPropAcl,
       "cucsLsTierTable": cucsLsTierTable,
       "cucsLsTierEntry": cucsLsTierEntry,
       "cucsLsTierInstanceId": cucsLsTierInstanceId,
       "cucsLsTierDn": cucsLsTierDn,
       "cucsLsTierRn": cucsLsTierRn,
       "cucsLsTierApply": cucsLsTierApply,
       "cucsLsTierDescr": cucsLsTierDescr,
       "cucsLsTierIntId": cucsLsTierIntId,
       "cucsLsTierName": cucsLsTierName,
       "cucsLsTierSrcTemplName": cucsLsTierSrcTemplName,
       "cucsLsTierPolicyLevel": cucsLsTierPolicyLevel,
       "cucsLsTierPolicyOwner": cucsLsTierPolicyOwner,
       "cucsLsServerFsmTaskTable": cucsLsServerFsmTaskTable,
       "cucsLsServerFsmTaskEntry": cucsLsServerFsmTaskEntry,
       "cucsLsServerFsmTaskInstanceId": cucsLsServerFsmTaskInstanceId,
       "cucsLsServerFsmTaskDn": cucsLsServerFsmTaskDn,
       "cucsLsServerFsmTaskRn": cucsLsServerFsmTaskRn,
       "cucsLsServerFsmTaskCompletion": cucsLsServerFsmTaskCompletion,
       "cucsLsServerFsmTaskFlags": cucsLsServerFsmTaskFlags,
       "cucsLsServerFsmTaskItem": cucsLsServerFsmTaskItem,
       "cucsLsServerFsmTaskSeqId": cucsLsServerFsmTaskSeqId,
       "cucsLsServerAssocCtxTable": cucsLsServerAssocCtxTable,
       "cucsLsServerAssocCtxEntry": cucsLsServerAssocCtxEntry,
       "cucsLsServerAssocCtxInstanceId": cucsLsServerAssocCtxInstanceId,
       "cucsLsServerAssocCtxDn": cucsLsServerAssocCtxDn,
       "cucsLsServerAssocCtxRn": cucsLsServerAssocCtxRn,
       "cucsLsServerAssocCtxPropAcl": cucsLsServerAssocCtxPropAcl,
       "cucsLsVersionBehTable": cucsLsVersionBehTable,
       "cucsLsVersionBehEntry": cucsLsVersionBehEntry,
       "cucsLsVersionBehInstanceId": cucsLsVersionBehInstanceId,
       "cucsLsVersionBehDn": cucsLsVersionBehDn,
       "cucsLsVersionBehRn": cucsLsVersionBehRn,
       "cucsLsVersionBehPciEnum": cucsLsVersionBehPciEnum,
       "cucsLsVersionBehVnicOrder": cucsLsVersionBehVnicOrder,
       "cucsLsVersionBehVconMap": cucsLsVersionBehVconMap,
       "cucsLsVersionBehVnicMap": cucsLsVersionBehVnicMap,
       "cucsLsVersionBehPropAcl": cucsLsVersionBehPropAcl,
       "cucsLsFcLocaleTable": cucsLsFcLocaleTable,
       "cucsLsFcLocaleEntry": cucsLsFcLocaleEntry,
       "cucsLsFcLocaleInstanceId": cucsLsFcLocaleInstanceId,
       "cucsLsFcLocaleDn": cucsLsFcLocaleDn,
       "cucsLsFcLocaleRn": cucsLsFcLocaleRn,
       "cucsLsFcLocaleSwitchId": cucsLsFcLocaleSwitchId,
       "cucsLsFcZoneTable": cucsLsFcZoneTable,
       "cucsLsFcZoneEntry": cucsLsFcZoneEntry,
       "cucsLsFcZoneInstanceId": cucsLsFcZoneInstanceId,
       "cucsLsFcZoneDn": cucsLsFcZoneDn,
       "cucsLsFcZoneRn": cucsLsFcZoneRn,
       "cucsLsFcZoneAdminState": cucsLsFcZoneAdminState,
       "cucsLsFcZoneId": cucsLsFcZoneId,
       "cucsLsFcZoneIdentity": cucsLsFcZoneIdentity,
       "cucsLsFcZoneIniName": cucsLsFcZoneIniName,
       "cucsLsFcZoneName": cucsLsFcZoneName,
       "cucsLsFcZoneOperState": cucsLsFcZoneOperState,
       "cucsLsFcZonePeerDn": cucsLsFcZonePeerDn,
       "cucsLsFcZoneSwitchId": cucsLsFcZoneSwitchId,
       "cucsLsFcZoneUsrLbl": cucsLsFcZoneUsrLbl,
       "cucsLsFcZoneVnetId": cucsLsFcZoneVnetId,
       "cucsLsFcZoneZoningType": cucsLsFcZoneZoningType,
       "cucsLsFcZoneGroupTable": cucsLsFcZoneGroupTable,
       "cucsLsFcZoneGroupEntry": cucsLsFcZoneGroupEntry,
       "cucsLsFcZoneGroupInstanceId": cucsLsFcZoneGroupInstanceId,
       "cucsLsFcZoneGroupDn": cucsLsFcZoneGroupDn,
       "cucsLsFcZoneGroupRn": cucsLsFcZoneGroupRn,
       "cucsLsFcZoneGroupId": cucsLsFcZoneGroupId,
       "cucsLsFcZoneGroupName": cucsLsFcZoneGroupName,
       "cucsLsFcZoneGroupSwitchId": cucsLsFcZoneGroupSwitchId,
       "cucsLsServerFsmTable": cucsLsServerFsmTable,
       "cucsLsServerFsmEntry": cucsLsServerFsmEntry,
       "cucsLsServerFsmInstanceId": cucsLsServerFsmInstanceId,
       "cucsLsServerFsmDn": cucsLsServerFsmDn,
       "cucsLsServerFsmRn": cucsLsServerFsmRn,
       "cucsLsServerFsmCompletionTime": cucsLsServerFsmCompletionTime,
       "cucsLsServerFsmCurrentFsm": cucsLsServerFsmCurrentFsm,
       "cucsLsServerFsmDescrData": cucsLsServerFsmDescrData,
       "cucsLsServerFsmFsmStatus": cucsLsServerFsmFsmStatus,
       "cucsLsServerFsmProgress": cucsLsServerFsmProgress,
       "cucsLsServerFsmRmtErrCode": cucsLsServerFsmRmtErrCode,
       "cucsLsServerFsmRmtErrDescr": cucsLsServerFsmRmtErrDescr,
       "cucsLsServerFsmRmtRslt": cucsLsServerFsmRmtRslt,
       "cucsLsServerFsmStageTable": cucsLsServerFsmStageTable,
       "cucsLsServerFsmStageEntry": cucsLsServerFsmStageEntry,
       "cucsLsServerFsmStageInstanceId": cucsLsServerFsmStageInstanceId,
       "cucsLsServerFsmStageDn": cucsLsServerFsmStageDn,
       "cucsLsServerFsmStageRn": cucsLsServerFsmStageRn,
       "cucsLsServerFsmStageDescrData": cucsLsServerFsmStageDescrData,
       "cucsLsServerFsmStageLastUpdateTime": cucsLsServerFsmStageLastUpdateTime,
       "cucsLsServerFsmStageName": cucsLsServerFsmStageName,
       "cucsLsServerFsmStageOrder": cucsLsServerFsmStageOrder,
       "cucsLsServerFsmStageRetry": cucsLsServerFsmStageRetry,
       "cucsLsServerFsmStageStageStatus": cucsLsServerFsmStageStageStatus,
       "cucsLsVConAssignTable": cucsLsVConAssignTable,
       "cucsLsVConAssignEntry": cucsLsVConAssignEntry,
       "cucsLsVConAssignInstanceId": cucsLsVConAssignInstanceId,
       "cucsLsVConAssignDn": cucsLsVConAssignDn,
       "cucsLsVConAssignRn": cucsLsVConAssignRn,
       "cucsLsVConAssignAdminVcon": cucsLsVConAssignAdminVcon,
       "cucsLsVConAssignOrder": cucsLsVConAssignOrder,
       "cucsLsVConAssignTransport": cucsLsVConAssignTransport,
       "cucsLsVConAssignVnicName": cucsLsVConAssignVnicName,
       "cucsLsVConAssignPropAcl": cucsLsVConAssignPropAcl,
       "cucsLsVConAssignAdminHostPort": cucsLsVConAssignAdminHostPort,
       "cucsLsZoneInitiatorMemberTable": cucsLsZoneInitiatorMemberTable,
       "cucsLsZoneInitiatorMemberEntry": cucsLsZoneInitiatorMemberEntry,
       "cucsLsZoneInitiatorMemberInstanceId": cucsLsZoneInitiatorMemberInstanceId,
       "cucsLsZoneInitiatorMemberDn": cucsLsZoneInitiatorMemberDn,
       "cucsLsZoneInitiatorMemberRn": cucsLsZoneInitiatorMemberRn,
       "cucsLsZoneInitiatorMemberEpDn": cucsLsZoneInitiatorMemberEpDn,
       "cucsLsZoneInitiatorMemberName": cucsLsZoneInitiatorMemberName,
       "cucsLsZoneInitiatorMemberUsrLbl": cucsLsZoneInitiatorMemberUsrLbl,
       "cucsLsZoneInitiatorMemberWwpn": cucsLsZoneInitiatorMemberWwpn,
       "cucsLsZoneTargetMemberTable": cucsLsZoneTargetMemberTable,
       "cucsLsZoneTargetMemberEntry": cucsLsZoneTargetMemberEntry,
       "cucsLsZoneTargetMemberInstanceId": cucsLsZoneTargetMemberInstanceId,
       "cucsLsZoneTargetMemberDn": cucsLsZoneTargetMemberDn,
       "cucsLsZoneTargetMemberRn": cucsLsZoneTargetMemberRn,
       "cucsLsZoneTargetMemberEpDn": cucsLsZoneTargetMemberEpDn,
       "cucsLsZoneTargetMemberName": cucsLsZoneTargetMemberName,
       "cucsLsZoneTargetMemberUsrLbl": cucsLsZoneTargetMemberUsrLbl,
       "cucsLsZoneTargetMemberWwpn": cucsLsZoneTargetMemberWwpn,
       "cucsLsServerExtensionTable": cucsLsServerExtensionTable,
       "cucsLsServerExtensionEntry": cucsLsServerExtensionEntry,
       "cucsLsServerExtensionInstanceId": cucsLsServerExtensionInstanceId,
       "cucsLsServerExtensionDn": cucsLsServerExtensionDn,
       "cucsLsServerExtensionRn": cucsLsServerExtensionRn,
       "cucsLsServerExtensionGuid": cucsLsServerExtensionGuid,
       "cucsLsServerExtensionVersion": cucsLsServerExtensionVersion,
       "cucsLsServerExtensionPropAcl": cucsLsServerExtensionPropAcl,
       "cucsLsServerExtensionVlanGrpRequestComputeTime": cucsLsServerExtensionVlanGrpRequestComputeTime,
       "cucsLsUuidHistoryTable": cucsLsUuidHistoryTable,
       "cucsLsUuidHistoryEntry": cucsLsUuidHistoryEntry,
       "cucsLsUuidHistoryInstanceId": cucsLsUuidHistoryInstanceId,
       "cucsLsUuidHistoryDn": cucsLsUuidHistoryDn,
       "cucsLsUuidHistoryRn": cucsLsUuidHistoryRn,
       "cucsLsUuidHistoryOlduuid": cucsLsUuidHistoryOlduuid,
       "cucsLsIssuesTable": cucsLsIssuesTable,
       "cucsLsIssuesEntry": cucsLsIssuesEntry,
       "cucsLsIssuesInstanceId": cucsLsIssuesInstanceId,
       "cucsLsIssuesDn": cucsLsIssuesDn,
       "cucsLsIssuesRn": cucsLsIssuesRn,
       "cucsLsIssuesIscsiConfigIssues": cucsLsIssuesIscsiConfigIssues,
       "cucsLsIssuesNetworkConfigIssues": cucsLsIssuesNetworkConfigIssues,
       "cucsLsIssuesServerConfigIssues": cucsLsIssuesServerConfigIssues,
       "cucsLsIssuesStorageConfigIssues": cucsLsIssuesStorageConfigIssues,
       "cucsLsIssuesVnicConfigIssues": cucsLsIssuesVnicConfigIssues,
       "cucsLsIssuesConfigWarnings": cucsLsIssuesConfigWarnings,
       "cucsLsIssuesPropAcl": cucsLsIssuesPropAcl,
       "cucsLsIdentityInfoTable": cucsLsIdentityInfoTable,
       "cucsLsIdentityInfoEntry": cucsLsIdentityInfoEntry,
       "cucsLsIdentityInfoInstanceId": cucsLsIdentityInfoInstanceId,
       "cucsLsIdentityInfoDn": cucsLsIdentityInfoDn,
       "cucsLsIdentityInfoRn": cucsLsIdentityInfoRn,
       "cucsLsIdentityInfoUuidIdentityState": cucsLsIdentityInfoUuidIdentityState}
)
