# SNMP MIB module (CISCO-UNIFIED-COMPUTING-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:09 2024
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
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsPolicyCleanupMode,
 CucsPolicyControlEpFsmCurrentFsm,
 CucsPolicyControlEpFsmStageName,
 CucsPolicyControlEpFsmTaskItem,
 CucsPolicyControlEpType,
 CucsPolicyControlSource,
 CucsPolicyControlledTypeFsmCurrentFsm,
 CucsPolicyControlledTypeFsmStageName,
 CucsPolicyControlledTypeFsmTaskItem,
 CucsPolicyIdResolvePolicyType,
 CucsPolicyPolicyOperStatus,
 CucsPolicyPolicyOwner,
 CucsPolicyPolicyResolveType,
 CucsPolicyPolicyScopeFsmCurrentFsm,
 CucsPolicyPolicyScopeFsmStageName,
 CucsPolicyPolicyScopeFsmTaskItem,
 CucsPolicyRegistrationStateType,
 CucsPolicyRepairStateType,
 CucsPolicyResumeAckState,
 CucsPolicyState,
 CucsPolicySuspendState) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsPolicyCleanupMode",
    "CucsPolicyControlEpFsmCurrentFsm",
    "CucsPolicyControlEpFsmStageName",
    "CucsPolicyControlEpFsmTaskItem",
    "CucsPolicyControlEpType",
    "CucsPolicyControlSource",
    "CucsPolicyControlledTypeFsmCurrentFsm",
    "CucsPolicyControlledTypeFsmStageName",
    "CucsPolicyControlledTypeFsmTaskItem",
    "CucsPolicyIdResolvePolicyType",
    "CucsPolicyPolicyOperStatus",
    "CucsPolicyPolicyOwner",
    "CucsPolicyPolicyResolveType",
    "CucsPolicyPolicyScopeFsmCurrentFsm",
    "CucsPolicyPolicyScopeFsmStageName",
    "CucsPolicyPolicyScopeFsmTaskItem",
    "CucsPolicyRegistrationStateType",
    "CucsPolicyRepairStateType",
    "CucsPolicyResumeAckState",
    "CucsPolicyState",
    "CucsPolicySuspendState")

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

cucsPolicyObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsPolicyCommunicationTable_Object = MibTable
cucsPolicyCommunicationTable = _CucsPolicyCommunicationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 1)
)
if mibBuilder.loadTexts:
    cucsPolicyCommunicationTable.setStatus("current")
_CucsPolicyCommunicationEntry_Object = MibTableRow
cucsPolicyCommunicationEntry = _CucsPolicyCommunicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 1, 1)
)
cucsPolicyCommunicationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyCommunicationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyCommunicationEntry.setStatus("current")
_CucsPolicyCommunicationInstanceId_Type = CucsManagedObjectId
_CucsPolicyCommunicationInstanceId_Object = MibTableColumn
cucsPolicyCommunicationInstanceId = _CucsPolicyCommunicationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 1, 1, 1),
    _CucsPolicyCommunicationInstanceId_Type()
)
cucsPolicyCommunicationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyCommunicationInstanceId.setStatus("current")
_CucsPolicyCommunicationDn_Type = CucsManagedObjectDn
_CucsPolicyCommunicationDn_Object = MibTableColumn
cucsPolicyCommunicationDn = _CucsPolicyCommunicationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 1, 1, 2),
    _CucsPolicyCommunicationDn_Type()
)
cucsPolicyCommunicationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyCommunicationDn.setStatus("current")
_CucsPolicyCommunicationRn_Type = SnmpAdminString
_CucsPolicyCommunicationRn_Object = MibTableColumn
cucsPolicyCommunicationRn = _CucsPolicyCommunicationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 1, 1, 3),
    _CucsPolicyCommunicationRn_Type()
)
cucsPolicyCommunicationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyCommunicationRn.setStatus("current")
_CucsPolicyCommunicationSource_Type = CucsPolicyControlSource
_CucsPolicyCommunicationSource_Object = MibTableColumn
cucsPolicyCommunicationSource = _CucsPolicyCommunicationSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 1, 1, 4),
    _CucsPolicyCommunicationSource_Type()
)
cucsPolicyCommunicationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyCommunicationSource.setStatus("current")
_CucsPolicyConfigBackupTable_Object = MibTable
cucsPolicyConfigBackupTable = _CucsPolicyConfigBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 2)
)
if mibBuilder.loadTexts:
    cucsPolicyConfigBackupTable.setStatus("current")
_CucsPolicyConfigBackupEntry_Object = MibTableRow
cucsPolicyConfigBackupEntry = _CucsPolicyConfigBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 2, 1)
)
cucsPolicyConfigBackupEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyConfigBackupInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyConfigBackupEntry.setStatus("current")
_CucsPolicyConfigBackupInstanceId_Type = CucsManagedObjectId
_CucsPolicyConfigBackupInstanceId_Object = MibTableColumn
cucsPolicyConfigBackupInstanceId = _CucsPolicyConfigBackupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 2, 1, 1),
    _CucsPolicyConfigBackupInstanceId_Type()
)
cucsPolicyConfigBackupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyConfigBackupInstanceId.setStatus("current")
_CucsPolicyConfigBackupDn_Type = CucsManagedObjectDn
_CucsPolicyConfigBackupDn_Object = MibTableColumn
cucsPolicyConfigBackupDn = _CucsPolicyConfigBackupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 2, 1, 2),
    _CucsPolicyConfigBackupDn_Type()
)
cucsPolicyConfigBackupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyConfigBackupDn.setStatus("current")
_CucsPolicyConfigBackupRn_Type = SnmpAdminString
_CucsPolicyConfigBackupRn_Object = MibTableColumn
cucsPolicyConfigBackupRn = _CucsPolicyConfigBackupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 2, 1, 3),
    _CucsPolicyConfigBackupRn_Type()
)
cucsPolicyConfigBackupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyConfigBackupRn.setStatus("current")
_CucsPolicyConfigBackupSource_Type = CucsPolicyControlSource
_CucsPolicyConfigBackupSource_Object = MibTableColumn
cucsPolicyConfigBackupSource = _CucsPolicyConfigBackupSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 2, 1, 4),
    _CucsPolicyConfigBackupSource_Type()
)
cucsPolicyConfigBackupSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyConfigBackupSource.setStatus("current")
_CucsPolicyControlEpTable_Object = MibTable
cucsPolicyControlEpTable = _CucsPolicyControlEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3)
)
if mibBuilder.loadTexts:
    cucsPolicyControlEpTable.setStatus("current")
_CucsPolicyControlEpEntry_Object = MibTableRow
cucsPolicyControlEpEntry = _CucsPolicyControlEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1)
)
cucsPolicyControlEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyControlEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyControlEpEntry.setStatus("current")
_CucsPolicyControlEpInstanceId_Type = CucsManagedObjectId
_CucsPolicyControlEpInstanceId_Object = MibTableColumn
cucsPolicyControlEpInstanceId = _CucsPolicyControlEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 1),
    _CucsPolicyControlEpInstanceId_Type()
)
cucsPolicyControlEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyControlEpInstanceId.setStatus("current")
_CucsPolicyControlEpDn_Type = CucsManagedObjectDn
_CucsPolicyControlEpDn_Object = MibTableColumn
cucsPolicyControlEpDn = _CucsPolicyControlEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 2),
    _CucsPolicyControlEpDn_Type()
)
cucsPolicyControlEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpDn.setStatus("current")
_CucsPolicyControlEpRn_Type = SnmpAdminString
_CucsPolicyControlEpRn_Object = MibTableColumn
cucsPolicyControlEpRn = _CucsPolicyControlEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 3),
    _CucsPolicyControlEpRn_Type()
)
cucsPolicyControlEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpRn.setStatus("current")
_CucsPolicyControlEpAckState_Type = CucsPolicyResumeAckState
_CucsPolicyControlEpAckState_Object = MibTableColumn
cucsPolicyControlEpAckState = _CucsPolicyControlEpAckState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 4),
    _CucsPolicyControlEpAckState_Type()
)
cucsPolicyControlEpAckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpAckState.setStatus("current")
_CucsPolicyControlEpEncSecret_Type = SnmpAdminString
_CucsPolicyControlEpEncSecret_Object = MibTableColumn
cucsPolicyControlEpEncSecret = _CucsPolicyControlEpEncSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 5),
    _CucsPolicyControlEpEncSecret_Type()
)
cucsPolicyControlEpEncSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpEncSecret.setStatus("current")
_CucsPolicyControlEpFsmDescr_Type = SnmpAdminString
_CucsPolicyControlEpFsmDescr_Object = MibTableColumn
cucsPolicyControlEpFsmDescr = _CucsPolicyControlEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 6),
    _CucsPolicyControlEpFsmDescr_Type()
)
cucsPolicyControlEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmDescr.setStatus("current")
_CucsPolicyControlEpFsmPrev_Type = SnmpAdminString
_CucsPolicyControlEpFsmPrev_Object = MibTableColumn
cucsPolicyControlEpFsmPrev = _CucsPolicyControlEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 7),
    _CucsPolicyControlEpFsmPrev_Type()
)
cucsPolicyControlEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmPrev.setStatus("current")
_CucsPolicyControlEpFsmProgr_Type = Gauge32
_CucsPolicyControlEpFsmProgr_Object = MibTableColumn
cucsPolicyControlEpFsmProgr = _CucsPolicyControlEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 8),
    _CucsPolicyControlEpFsmProgr_Type()
)
cucsPolicyControlEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmProgr.setStatus("current")
_CucsPolicyControlEpFsmRmtInvErrCode_Type = Gauge32
_CucsPolicyControlEpFsmRmtInvErrCode_Object = MibTableColumn
cucsPolicyControlEpFsmRmtInvErrCode = _CucsPolicyControlEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 9),
    _CucsPolicyControlEpFsmRmtInvErrCode_Type()
)
cucsPolicyControlEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmRmtInvErrCode.setStatus("current")
_CucsPolicyControlEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsPolicyControlEpFsmRmtInvErrDescr_Object = MibTableColumn
cucsPolicyControlEpFsmRmtInvErrDescr = _CucsPolicyControlEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 10),
    _CucsPolicyControlEpFsmRmtInvErrDescr_Type()
)
cucsPolicyControlEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmRmtInvErrDescr.setStatus("current")
_CucsPolicyControlEpFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsPolicyControlEpFsmRmtInvRslt_Object = MibTableColumn
cucsPolicyControlEpFsmRmtInvRslt = _CucsPolicyControlEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 11),
    _CucsPolicyControlEpFsmRmtInvRslt_Type()
)
cucsPolicyControlEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmRmtInvRslt.setStatus("current")
_CucsPolicyControlEpFsmStageDescr_Type = SnmpAdminString
_CucsPolicyControlEpFsmStageDescr_Object = MibTableColumn
cucsPolicyControlEpFsmStageDescr = _CucsPolicyControlEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 12),
    _CucsPolicyControlEpFsmStageDescr_Type()
)
cucsPolicyControlEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStageDescr.setStatus("current")
_CucsPolicyControlEpFsmStamp_Type = DateAndTime
_CucsPolicyControlEpFsmStamp_Object = MibTableColumn
cucsPolicyControlEpFsmStamp = _CucsPolicyControlEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 13),
    _CucsPolicyControlEpFsmStamp_Type()
)
cucsPolicyControlEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStamp.setStatus("current")
_CucsPolicyControlEpFsmStatus_Type = SnmpAdminString
_CucsPolicyControlEpFsmStatus_Object = MibTableColumn
cucsPolicyControlEpFsmStatus = _CucsPolicyControlEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 14),
    _CucsPolicyControlEpFsmStatus_Type()
)
cucsPolicyControlEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStatus.setStatus("current")
_CucsPolicyControlEpFsmTry_Type = Gauge32
_CucsPolicyControlEpFsmTry_Object = MibTableColumn
cucsPolicyControlEpFsmTry = _CucsPolicyControlEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 15),
    _CucsPolicyControlEpFsmTry_Type()
)
cucsPolicyControlEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmTry.setStatus("current")
_CucsPolicyControlEpName_Type = SnmpAdminString
_CucsPolicyControlEpName_Object = MibTableColumn
cucsPolicyControlEpName = _CucsPolicyControlEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 16),
    _CucsPolicyControlEpName_Type()
)
cucsPolicyControlEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpName.setStatus("current")
_CucsPolicyControlEpRegistrationState_Type = CucsPolicyRegistrationStateType
_CucsPolicyControlEpRegistrationState_Object = MibTableColumn
cucsPolicyControlEpRegistrationState = _CucsPolicyControlEpRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 17),
    _CucsPolicyControlEpRegistrationState_Type()
)
cucsPolicyControlEpRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpRegistrationState.setStatus("current")
_CucsPolicyControlEpRepairState_Type = CucsPolicyRepairStateType
_CucsPolicyControlEpRepairState_Object = MibTableColumn
cucsPolicyControlEpRepairState = _CucsPolicyControlEpRepairState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 18),
    _CucsPolicyControlEpRepairState_Type()
)
cucsPolicyControlEpRepairState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpRepairState.setStatus("current")
_CucsPolicyControlEpSecret_Type = SnmpAdminString
_CucsPolicyControlEpSecret_Object = MibTableColumn
cucsPolicyControlEpSecret = _CucsPolicyControlEpSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 19),
    _CucsPolicyControlEpSecret_Type()
)
cucsPolicyControlEpSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpSecret.setStatus("current")
_CucsPolicyControlEpState_Type = CucsPolicyState
_CucsPolicyControlEpState_Object = MibTableColumn
cucsPolicyControlEpState = _CucsPolicyControlEpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 20),
    _CucsPolicyControlEpState_Type()
)
cucsPolicyControlEpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpState.setStatus("current")
_CucsPolicyControlEpSuspendState_Type = CucsPolicySuspendState
_CucsPolicyControlEpSuspendState_Object = MibTableColumn
cucsPolicyControlEpSuspendState = _CucsPolicyControlEpSuspendState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 21),
    _CucsPolicyControlEpSuspendState_Type()
)
cucsPolicyControlEpSuspendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpSuspendState.setStatus("current")
_CucsPolicyControlEpSvcRegIP_Type = InetAddressIPv4
_CucsPolicyControlEpSvcRegIP_Object = MibTableColumn
cucsPolicyControlEpSvcRegIP = _CucsPolicyControlEpSvcRegIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 22),
    _CucsPolicyControlEpSvcRegIP_Type()
)
cucsPolicyControlEpSvcRegIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpSvcRegIP.setStatus("current")
_CucsPolicyControlEpSvcRegName_Type = SnmpAdminString
_CucsPolicyControlEpSvcRegName_Object = MibTableColumn
cucsPolicyControlEpSvcRegName = _CucsPolicyControlEpSvcRegName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 23),
    _CucsPolicyControlEpSvcRegName_Type()
)
cucsPolicyControlEpSvcRegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpSvcRegName.setStatus("current")
_CucsPolicyControlEpType_Type = CucsPolicyControlEpType
_CucsPolicyControlEpType_Object = MibTableColumn
cucsPolicyControlEpType = _CucsPolicyControlEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 24),
    _CucsPolicyControlEpType_Type()
)
cucsPolicyControlEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpType.setStatus("current")
_CucsPolicyControlEpCleanupMode_Type = CucsPolicyCleanupMode
_CucsPolicyControlEpCleanupMode_Object = MibTableColumn
cucsPolicyControlEpCleanupMode = _CucsPolicyControlEpCleanupMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 3, 1, 25),
    _CucsPolicyControlEpCleanupMode_Type()
)
cucsPolicyControlEpCleanupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpCleanupMode.setStatus("current")
_CucsPolicyControlEpFsmTable_Object = MibTable
cucsPolicyControlEpFsmTable = _CucsPolicyControlEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4)
)
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmTable.setStatus("current")
_CucsPolicyControlEpFsmEntry_Object = MibTableRow
cucsPolicyControlEpFsmEntry = _CucsPolicyControlEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4, 1)
)
cucsPolicyControlEpFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyControlEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmEntry.setStatus("current")
_CucsPolicyControlEpFsmInstanceId_Type = CucsManagedObjectId
_CucsPolicyControlEpFsmInstanceId_Object = MibTableColumn
cucsPolicyControlEpFsmInstanceId = _CucsPolicyControlEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4, 1, 1),
    _CucsPolicyControlEpFsmInstanceId_Type()
)
cucsPolicyControlEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmInstanceId.setStatus("current")
_CucsPolicyControlEpFsmDn_Type = CucsManagedObjectDn
_CucsPolicyControlEpFsmDn_Object = MibTableColumn
cucsPolicyControlEpFsmDn = _CucsPolicyControlEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4, 1, 2),
    _CucsPolicyControlEpFsmDn_Type()
)
cucsPolicyControlEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmDn.setStatus("current")
_CucsPolicyControlEpFsmRn_Type = SnmpAdminString
_CucsPolicyControlEpFsmRn_Object = MibTableColumn
cucsPolicyControlEpFsmRn = _CucsPolicyControlEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4, 1, 3),
    _CucsPolicyControlEpFsmRn_Type()
)
cucsPolicyControlEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmRn.setStatus("current")
_CucsPolicyControlEpFsmCompletionTime_Type = DateAndTime
_CucsPolicyControlEpFsmCompletionTime_Object = MibTableColumn
cucsPolicyControlEpFsmCompletionTime = _CucsPolicyControlEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4, 1, 4),
    _CucsPolicyControlEpFsmCompletionTime_Type()
)
cucsPolicyControlEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmCompletionTime.setStatus("current")
_CucsPolicyControlEpFsmCurrentFsm_Type = CucsPolicyControlEpFsmCurrentFsm
_CucsPolicyControlEpFsmCurrentFsm_Object = MibTableColumn
cucsPolicyControlEpFsmCurrentFsm = _CucsPolicyControlEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4, 1, 5),
    _CucsPolicyControlEpFsmCurrentFsm_Type()
)
cucsPolicyControlEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmCurrentFsm.setStatus("current")
_CucsPolicyControlEpFsmDescrData_Type = SnmpAdminString
_CucsPolicyControlEpFsmDescrData_Object = MibTableColumn
cucsPolicyControlEpFsmDescrData = _CucsPolicyControlEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4, 1, 6),
    _CucsPolicyControlEpFsmDescrData_Type()
)
cucsPolicyControlEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmDescrData.setStatus("current")
_CucsPolicyControlEpFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsPolicyControlEpFsmFsmStatus_Object = MibTableColumn
cucsPolicyControlEpFsmFsmStatus = _CucsPolicyControlEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4, 1, 7),
    _CucsPolicyControlEpFsmFsmStatus_Type()
)
cucsPolicyControlEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmFsmStatus.setStatus("current")
_CucsPolicyControlEpFsmProgress_Type = Gauge32
_CucsPolicyControlEpFsmProgress_Object = MibTableColumn
cucsPolicyControlEpFsmProgress = _CucsPolicyControlEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4, 1, 8),
    _CucsPolicyControlEpFsmProgress_Type()
)
cucsPolicyControlEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmProgress.setStatus("current")
_CucsPolicyControlEpFsmRmtErrCode_Type = Gauge32
_CucsPolicyControlEpFsmRmtErrCode_Object = MibTableColumn
cucsPolicyControlEpFsmRmtErrCode = _CucsPolicyControlEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4, 1, 9),
    _CucsPolicyControlEpFsmRmtErrCode_Type()
)
cucsPolicyControlEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmRmtErrCode.setStatus("current")
_CucsPolicyControlEpFsmRmtErrDescr_Type = SnmpAdminString
_CucsPolicyControlEpFsmRmtErrDescr_Object = MibTableColumn
cucsPolicyControlEpFsmRmtErrDescr = _CucsPolicyControlEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4, 1, 10),
    _CucsPolicyControlEpFsmRmtErrDescr_Type()
)
cucsPolicyControlEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmRmtErrDescr.setStatus("current")
_CucsPolicyControlEpFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsPolicyControlEpFsmRmtRslt_Object = MibTableColumn
cucsPolicyControlEpFsmRmtRslt = _CucsPolicyControlEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 4, 1, 11),
    _CucsPolicyControlEpFsmRmtRslt_Type()
)
cucsPolicyControlEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmRmtRslt.setStatus("current")
_CucsPolicyControlEpFsmStageTable_Object = MibTable
cucsPolicyControlEpFsmStageTable = _CucsPolicyControlEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 5)
)
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStageTable.setStatus("current")
_CucsPolicyControlEpFsmStageEntry_Object = MibTableRow
cucsPolicyControlEpFsmStageEntry = _CucsPolicyControlEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 5, 1)
)
cucsPolicyControlEpFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyControlEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStageEntry.setStatus("current")
_CucsPolicyControlEpFsmStageInstanceId_Type = CucsManagedObjectId
_CucsPolicyControlEpFsmStageInstanceId_Object = MibTableColumn
cucsPolicyControlEpFsmStageInstanceId = _CucsPolicyControlEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 5, 1, 1),
    _CucsPolicyControlEpFsmStageInstanceId_Type()
)
cucsPolicyControlEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStageInstanceId.setStatus("current")
_CucsPolicyControlEpFsmStageDn_Type = CucsManagedObjectDn
_CucsPolicyControlEpFsmStageDn_Object = MibTableColumn
cucsPolicyControlEpFsmStageDn = _CucsPolicyControlEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 5, 1, 2),
    _CucsPolicyControlEpFsmStageDn_Type()
)
cucsPolicyControlEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStageDn.setStatus("current")
_CucsPolicyControlEpFsmStageRn_Type = SnmpAdminString
_CucsPolicyControlEpFsmStageRn_Object = MibTableColumn
cucsPolicyControlEpFsmStageRn = _CucsPolicyControlEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 5, 1, 3),
    _CucsPolicyControlEpFsmStageRn_Type()
)
cucsPolicyControlEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStageRn.setStatus("current")
_CucsPolicyControlEpFsmStageDescrData_Type = SnmpAdminString
_CucsPolicyControlEpFsmStageDescrData_Object = MibTableColumn
cucsPolicyControlEpFsmStageDescrData = _CucsPolicyControlEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 5, 1, 4),
    _CucsPolicyControlEpFsmStageDescrData_Type()
)
cucsPolicyControlEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStageDescrData.setStatus("current")
_CucsPolicyControlEpFsmStageLastUpdateTime_Type = DateAndTime
_CucsPolicyControlEpFsmStageLastUpdateTime_Object = MibTableColumn
cucsPolicyControlEpFsmStageLastUpdateTime = _CucsPolicyControlEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 5, 1, 5),
    _CucsPolicyControlEpFsmStageLastUpdateTime_Type()
)
cucsPolicyControlEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStageLastUpdateTime.setStatus("current")
_CucsPolicyControlEpFsmStageName_Type = CucsPolicyControlEpFsmStageName
_CucsPolicyControlEpFsmStageName_Object = MibTableColumn
cucsPolicyControlEpFsmStageName = _CucsPolicyControlEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 5, 1, 6),
    _CucsPolicyControlEpFsmStageName_Type()
)
cucsPolicyControlEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStageName.setStatus("current")
_CucsPolicyControlEpFsmStageOrder_Type = Gauge32
_CucsPolicyControlEpFsmStageOrder_Object = MibTableColumn
cucsPolicyControlEpFsmStageOrder = _CucsPolicyControlEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 5, 1, 7),
    _CucsPolicyControlEpFsmStageOrder_Type()
)
cucsPolicyControlEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStageOrder.setStatus("current")
_CucsPolicyControlEpFsmStageRetry_Type = Gauge32
_CucsPolicyControlEpFsmStageRetry_Object = MibTableColumn
cucsPolicyControlEpFsmStageRetry = _CucsPolicyControlEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 5, 1, 8),
    _CucsPolicyControlEpFsmStageRetry_Type()
)
cucsPolicyControlEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStageRetry.setStatus("current")
_CucsPolicyControlEpFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsPolicyControlEpFsmStageStageStatus_Object = MibTableColumn
cucsPolicyControlEpFsmStageStageStatus = _CucsPolicyControlEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 5, 1, 9),
    _CucsPolicyControlEpFsmStageStageStatus_Type()
)
cucsPolicyControlEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmStageStageStatus.setStatus("current")
_CucsPolicyControlEpFsmTaskTable_Object = MibTable
cucsPolicyControlEpFsmTaskTable = _CucsPolicyControlEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 6)
)
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmTaskTable.setStatus("current")
_CucsPolicyControlEpFsmTaskEntry_Object = MibTableRow
cucsPolicyControlEpFsmTaskEntry = _CucsPolicyControlEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 6, 1)
)
cucsPolicyControlEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyControlEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmTaskEntry.setStatus("current")
_CucsPolicyControlEpFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsPolicyControlEpFsmTaskInstanceId_Object = MibTableColumn
cucsPolicyControlEpFsmTaskInstanceId = _CucsPolicyControlEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 6, 1, 1),
    _CucsPolicyControlEpFsmTaskInstanceId_Type()
)
cucsPolicyControlEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmTaskInstanceId.setStatus("current")
_CucsPolicyControlEpFsmTaskDn_Type = CucsManagedObjectDn
_CucsPolicyControlEpFsmTaskDn_Object = MibTableColumn
cucsPolicyControlEpFsmTaskDn = _CucsPolicyControlEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 6, 1, 2),
    _CucsPolicyControlEpFsmTaskDn_Type()
)
cucsPolicyControlEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmTaskDn.setStatus("current")
_CucsPolicyControlEpFsmTaskRn_Type = SnmpAdminString
_CucsPolicyControlEpFsmTaskRn_Object = MibTableColumn
cucsPolicyControlEpFsmTaskRn = _CucsPolicyControlEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 6, 1, 3),
    _CucsPolicyControlEpFsmTaskRn_Type()
)
cucsPolicyControlEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmTaskRn.setStatus("current")
_CucsPolicyControlEpFsmTaskCompletion_Type = CucsFsmCompletion
_CucsPolicyControlEpFsmTaskCompletion_Object = MibTableColumn
cucsPolicyControlEpFsmTaskCompletion = _CucsPolicyControlEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 6, 1, 4),
    _CucsPolicyControlEpFsmTaskCompletion_Type()
)
cucsPolicyControlEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmTaskCompletion.setStatus("current")
_CucsPolicyControlEpFsmTaskFlags_Type = CucsFsmFlags
_CucsPolicyControlEpFsmTaskFlags_Object = MibTableColumn
cucsPolicyControlEpFsmTaskFlags = _CucsPolicyControlEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 6, 1, 5),
    _CucsPolicyControlEpFsmTaskFlags_Type()
)
cucsPolicyControlEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmTaskFlags.setStatus("current")
_CucsPolicyControlEpFsmTaskItem_Type = CucsPolicyControlEpFsmTaskItem
_CucsPolicyControlEpFsmTaskItem_Object = MibTableColumn
cucsPolicyControlEpFsmTaskItem = _CucsPolicyControlEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 6, 1, 6),
    _CucsPolicyControlEpFsmTaskItem_Type()
)
cucsPolicyControlEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmTaskItem.setStatus("current")
_CucsPolicyControlEpFsmTaskSeqId_Type = Gauge32
_CucsPolicyControlEpFsmTaskSeqId_Object = MibTableColumn
cucsPolicyControlEpFsmTaskSeqId = _CucsPolicyControlEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 6, 1, 7),
    _CucsPolicyControlEpFsmTaskSeqId_Type()
)
cucsPolicyControlEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlEpFsmTaskSeqId.setStatus("current")
_CucsPolicyControlledInstanceTable_Object = MibTable
cucsPolicyControlledInstanceTable = _CucsPolicyControlledInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 7)
)
if mibBuilder.loadTexts:
    cucsPolicyControlledInstanceTable.setStatus("current")
_CucsPolicyControlledInstanceEntry_Object = MibTableRow
cucsPolicyControlledInstanceEntry = _CucsPolicyControlledInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 7, 1)
)
cucsPolicyControlledInstanceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyControlledInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyControlledInstanceEntry.setStatus("current")
_CucsPolicyControlledInstanceInstanceId_Type = CucsManagedObjectId
_CucsPolicyControlledInstanceInstanceId_Object = MibTableColumn
cucsPolicyControlledInstanceInstanceId = _CucsPolicyControlledInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 7, 1, 1),
    _CucsPolicyControlledInstanceInstanceId_Type()
)
cucsPolicyControlledInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyControlledInstanceInstanceId.setStatus("current")
_CucsPolicyControlledInstanceDn_Type = CucsManagedObjectDn
_CucsPolicyControlledInstanceDn_Object = MibTableColumn
cucsPolicyControlledInstanceDn = _CucsPolicyControlledInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 7, 1, 2),
    _CucsPolicyControlledInstanceDn_Type()
)
cucsPolicyControlledInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledInstanceDn.setStatus("current")
_CucsPolicyControlledInstanceRn_Type = SnmpAdminString
_CucsPolicyControlledInstanceRn_Object = MibTableColumn
cucsPolicyControlledInstanceRn = _CucsPolicyControlledInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 7, 1, 3),
    _CucsPolicyControlledInstanceRn_Type()
)
cucsPolicyControlledInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledInstanceRn.setStatus("current")
_CucsPolicyControlledInstanceDefDn_Type = SnmpAdminString
_CucsPolicyControlledInstanceDefDn_Object = MibTableColumn
cucsPolicyControlledInstanceDefDn = _CucsPolicyControlledInstanceDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 7, 1, 4),
    _CucsPolicyControlledInstanceDefDn_Type()
)
cucsPolicyControlledInstanceDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledInstanceDefDn.setStatus("current")
_CucsPolicyControlledInstanceExternalResolveName_Type = SnmpAdminString
_CucsPolicyControlledInstanceExternalResolveName_Object = MibTableColumn
cucsPolicyControlledInstanceExternalResolveName = _CucsPolicyControlledInstanceExternalResolveName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 7, 1, 5),
    _CucsPolicyControlledInstanceExternalResolveName_Type()
)
cucsPolicyControlledInstanceExternalResolveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledInstanceExternalResolveName.setStatus("current")
_CucsPolicyControlledInstanceName_Type = SnmpAdminString
_CucsPolicyControlledInstanceName_Object = MibTableColumn
cucsPolicyControlledInstanceName = _CucsPolicyControlledInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 7, 1, 6),
    _CucsPolicyControlledInstanceName_Type()
)
cucsPolicyControlledInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledInstanceName.setStatus("current")
_CucsPolicyControlledInstanceResolveType_Type = CucsPolicyPolicyResolveType
_CucsPolicyControlledInstanceResolveType_Object = MibTableColumn
cucsPolicyControlledInstanceResolveType = _CucsPolicyControlledInstanceResolveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 7, 1, 7),
    _CucsPolicyControlledInstanceResolveType_Type()
)
cucsPolicyControlledInstanceResolveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledInstanceResolveType.setStatus("current")
_CucsPolicyControlledInstanceType_Type = SnmpAdminString
_CucsPolicyControlledInstanceType_Object = MibTableColumn
cucsPolicyControlledInstanceType = _CucsPolicyControlledInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 7, 1, 8),
    _CucsPolicyControlledInstanceType_Type()
)
cucsPolicyControlledInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledInstanceType.setStatus("current")
_CucsPolicyControlledTypeTable_Object = MibTable
cucsPolicyControlledTypeTable = _CucsPolicyControlledTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8)
)
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeTable.setStatus("current")
_CucsPolicyControlledTypeEntry_Object = MibTableRow
cucsPolicyControlledTypeEntry = _CucsPolicyControlledTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1)
)
cucsPolicyControlledTypeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyControlledTypeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeEntry.setStatus("current")
_CucsPolicyControlledTypeInstanceId_Type = CucsManagedObjectId
_CucsPolicyControlledTypeInstanceId_Object = MibTableColumn
cucsPolicyControlledTypeInstanceId = _CucsPolicyControlledTypeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 1),
    _CucsPolicyControlledTypeInstanceId_Type()
)
cucsPolicyControlledTypeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeInstanceId.setStatus("current")
_CucsPolicyControlledTypeDn_Type = CucsManagedObjectDn
_CucsPolicyControlledTypeDn_Object = MibTableColumn
cucsPolicyControlledTypeDn = _CucsPolicyControlledTypeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 2),
    _CucsPolicyControlledTypeDn_Type()
)
cucsPolicyControlledTypeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeDn.setStatus("current")
_CucsPolicyControlledTypeRn_Type = SnmpAdminString
_CucsPolicyControlledTypeRn_Object = MibTableColumn
cucsPolicyControlledTypeRn = _CucsPolicyControlledTypeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 3),
    _CucsPolicyControlledTypeRn_Type()
)
cucsPolicyControlledTypeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeRn.setStatus("current")
_CucsPolicyControlledTypeParentContext_Type = SnmpAdminString
_CucsPolicyControlledTypeParentContext_Object = MibTableColumn
cucsPolicyControlledTypeParentContext = _CucsPolicyControlledTypeParentContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 4),
    _CucsPolicyControlledTypeParentContext_Type()
)
cucsPolicyControlledTypeParentContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeParentContext.setStatus("current")
_CucsPolicyControlledTypeType_Type = SnmpAdminString
_CucsPolicyControlledTypeType_Object = MibTableColumn
cucsPolicyControlledTypeType = _CucsPolicyControlledTypeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 5),
    _CucsPolicyControlledTypeType_Type()
)
cucsPolicyControlledTypeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeType.setStatus("current")
_CucsPolicyControlledTypeFsmDescr_Type = SnmpAdminString
_CucsPolicyControlledTypeFsmDescr_Object = MibTableColumn
cucsPolicyControlledTypeFsmDescr = _CucsPolicyControlledTypeFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 6),
    _CucsPolicyControlledTypeFsmDescr_Type()
)
cucsPolicyControlledTypeFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmDescr.setStatus("current")
_CucsPolicyControlledTypeFsmPrev_Type = SnmpAdminString
_CucsPolicyControlledTypeFsmPrev_Object = MibTableColumn
cucsPolicyControlledTypeFsmPrev = _CucsPolicyControlledTypeFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 7),
    _CucsPolicyControlledTypeFsmPrev_Type()
)
cucsPolicyControlledTypeFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmPrev.setStatus("current")
_CucsPolicyControlledTypeFsmProgr_Type = Gauge32
_CucsPolicyControlledTypeFsmProgr_Object = MibTableColumn
cucsPolicyControlledTypeFsmProgr = _CucsPolicyControlledTypeFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 8),
    _CucsPolicyControlledTypeFsmProgr_Type()
)
cucsPolicyControlledTypeFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmProgr.setStatus("current")
_CucsPolicyControlledTypeFsmRmtInvErrCode_Type = Gauge32
_CucsPolicyControlledTypeFsmRmtInvErrCode_Object = MibTableColumn
cucsPolicyControlledTypeFsmRmtInvErrCode = _CucsPolicyControlledTypeFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 9),
    _CucsPolicyControlledTypeFsmRmtInvErrCode_Type()
)
cucsPolicyControlledTypeFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmRmtInvErrCode.setStatus("current")
_CucsPolicyControlledTypeFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsPolicyControlledTypeFsmRmtInvErrDescr_Object = MibTableColumn
cucsPolicyControlledTypeFsmRmtInvErrDescr = _CucsPolicyControlledTypeFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 10),
    _CucsPolicyControlledTypeFsmRmtInvErrDescr_Type()
)
cucsPolicyControlledTypeFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmRmtInvErrDescr.setStatus("current")
_CucsPolicyControlledTypeFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsPolicyControlledTypeFsmRmtInvRslt_Object = MibTableColumn
cucsPolicyControlledTypeFsmRmtInvRslt = _CucsPolicyControlledTypeFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 11),
    _CucsPolicyControlledTypeFsmRmtInvRslt_Type()
)
cucsPolicyControlledTypeFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmRmtInvRslt.setStatus("current")
_CucsPolicyControlledTypeFsmStageDescr_Type = SnmpAdminString
_CucsPolicyControlledTypeFsmStageDescr_Object = MibTableColumn
cucsPolicyControlledTypeFsmStageDescr = _CucsPolicyControlledTypeFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 12),
    _CucsPolicyControlledTypeFsmStageDescr_Type()
)
cucsPolicyControlledTypeFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStageDescr.setStatus("current")
_CucsPolicyControlledTypeFsmStamp_Type = DateAndTime
_CucsPolicyControlledTypeFsmStamp_Object = MibTableColumn
cucsPolicyControlledTypeFsmStamp = _CucsPolicyControlledTypeFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 13),
    _CucsPolicyControlledTypeFsmStamp_Type()
)
cucsPolicyControlledTypeFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStamp.setStatus("current")
_CucsPolicyControlledTypeFsmStatus_Type = SnmpAdminString
_CucsPolicyControlledTypeFsmStatus_Object = MibTableColumn
cucsPolicyControlledTypeFsmStatus = _CucsPolicyControlledTypeFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 14),
    _CucsPolicyControlledTypeFsmStatus_Type()
)
cucsPolicyControlledTypeFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStatus.setStatus("current")
_CucsPolicyControlledTypeFsmTry_Type = Gauge32
_CucsPolicyControlledTypeFsmTry_Object = MibTableColumn
cucsPolicyControlledTypeFsmTry = _CucsPolicyControlledTypeFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 8, 1, 15),
    _CucsPolicyControlledTypeFsmTry_Type()
)
cucsPolicyControlledTypeFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmTry.setStatus("current")
_CucsPolicyDateTimeTable_Object = MibTable
cucsPolicyDateTimeTable = _CucsPolicyDateTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 9)
)
if mibBuilder.loadTexts:
    cucsPolicyDateTimeTable.setStatus("current")
_CucsPolicyDateTimeEntry_Object = MibTableRow
cucsPolicyDateTimeEntry = _CucsPolicyDateTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 9, 1)
)
cucsPolicyDateTimeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyDateTimeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyDateTimeEntry.setStatus("current")
_CucsPolicyDateTimeInstanceId_Type = CucsManagedObjectId
_CucsPolicyDateTimeInstanceId_Object = MibTableColumn
cucsPolicyDateTimeInstanceId = _CucsPolicyDateTimeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 9, 1, 1),
    _CucsPolicyDateTimeInstanceId_Type()
)
cucsPolicyDateTimeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyDateTimeInstanceId.setStatus("current")
_CucsPolicyDateTimeDn_Type = CucsManagedObjectDn
_CucsPolicyDateTimeDn_Object = MibTableColumn
cucsPolicyDateTimeDn = _CucsPolicyDateTimeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 9, 1, 2),
    _CucsPolicyDateTimeDn_Type()
)
cucsPolicyDateTimeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDateTimeDn.setStatus("current")
_CucsPolicyDateTimeRn_Type = SnmpAdminString
_CucsPolicyDateTimeRn_Object = MibTableColumn
cucsPolicyDateTimeRn = _CucsPolicyDateTimeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 9, 1, 3),
    _CucsPolicyDateTimeRn_Type()
)
cucsPolicyDateTimeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDateTimeRn.setStatus("current")
_CucsPolicyDateTimeSource_Type = CucsPolicyControlSource
_CucsPolicyDateTimeSource_Object = MibTableColumn
cucsPolicyDateTimeSource = _CucsPolicyDateTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 9, 1, 4),
    _CucsPolicyDateTimeSource_Type()
)
cucsPolicyDateTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDateTimeSource.setStatus("current")
_CucsPolicyDigestTable_Object = MibTable
cucsPolicyDigestTable = _CucsPolicyDigestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10)
)
if mibBuilder.loadTexts:
    cucsPolicyDigestTable.setStatus("current")
_CucsPolicyDigestEntry_Object = MibTableRow
cucsPolicyDigestEntry = _CucsPolicyDigestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1)
)
cucsPolicyDigestEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyDigestInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyDigestEntry.setStatus("current")
_CucsPolicyDigestInstanceId_Type = CucsManagedObjectId
_CucsPolicyDigestInstanceId_Object = MibTableColumn
cucsPolicyDigestInstanceId = _CucsPolicyDigestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 1),
    _CucsPolicyDigestInstanceId_Type()
)
cucsPolicyDigestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyDigestInstanceId.setStatus("current")
_CucsPolicyDigestDn_Type = CucsManagedObjectDn
_CucsPolicyDigestDn_Object = MibTableColumn
cucsPolicyDigestDn = _CucsPolicyDigestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 2),
    _CucsPolicyDigestDn_Type()
)
cucsPolicyDigestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDigestDn.setStatus("current")
_CucsPolicyDigestRn_Type = SnmpAdminString
_CucsPolicyDigestRn_Object = MibTableColumn
cucsPolicyDigestRn = _CucsPolicyDigestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 3),
    _CucsPolicyDigestRn_Type()
)
cucsPolicyDigestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDigestRn.setStatus("current")
_CucsPolicyDigestContext_Type = SnmpAdminString
_CucsPolicyDigestContext_Object = MibTableColumn
cucsPolicyDigestContext = _CucsPolicyDigestContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 4),
    _CucsPolicyDigestContext_Type()
)
cucsPolicyDigestContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDigestContext.setStatus("current")
_CucsPolicyDigestDescr_Type = SnmpAdminString
_CucsPolicyDigestDescr_Object = MibTableColumn
cucsPolicyDigestDescr = _CucsPolicyDigestDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 5),
    _CucsPolicyDigestDescr_Type()
)
cucsPolicyDigestDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDigestDescr.setStatus("current")
_CucsPolicyDigestLabel_Type = SnmpAdminString
_CucsPolicyDigestLabel_Object = MibTableColumn
cucsPolicyDigestLabel = _CucsPolicyDigestLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 6),
    _CucsPolicyDigestLabel_Type()
)
cucsPolicyDigestLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDigestLabel.setStatus("current")
_CucsPolicyDigestName_Type = SnmpAdminString
_CucsPolicyDigestName_Object = MibTableColumn
cucsPolicyDigestName = _CucsPolicyDigestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 7),
    _CucsPolicyDigestName_Type()
)
cucsPolicyDigestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDigestName.setStatus("current")
_CucsPolicyDigestResolveType_Type = CucsPolicyPolicyResolveType
_CucsPolicyDigestResolveType_Object = MibTableColumn
cucsPolicyDigestResolveType = _CucsPolicyDigestResolveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 8),
    _CucsPolicyDigestResolveType_Type()
)
cucsPolicyDigestResolveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDigestResolveType.setStatus("current")
_CucsPolicyDigestType_Type = SnmpAdminString
_CucsPolicyDigestType_Object = MibTableColumn
cucsPolicyDigestType = _CucsPolicyDigestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 9),
    _CucsPolicyDigestType_Type()
)
cucsPolicyDigestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDigestType.setStatus("current")
_CucsPolicyDigestUsage_Type = SnmpAdminString
_CucsPolicyDigestUsage_Object = MibTableColumn
cucsPolicyDigestUsage = _CucsPolicyDigestUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 10),
    _CucsPolicyDigestUsage_Type()
)
cucsPolicyDigestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDigestUsage.setStatus("current")
_CucsPolicyDigestOnBehalfOfIdent_Type = SnmpAdminString
_CucsPolicyDigestOnBehalfOfIdent_Object = MibTableColumn
cucsPolicyDigestOnBehalfOfIdent = _CucsPolicyDigestOnBehalfOfIdent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 11),
    _CucsPolicyDigestOnBehalfOfIdent_Type()
)
cucsPolicyDigestOnBehalfOfIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDigestOnBehalfOfIdent.setStatus("current")
_CucsPolicyDigestOnBehalfOfType_Type = SnmpAdminString
_CucsPolicyDigestOnBehalfOfType_Object = MibTableColumn
cucsPolicyDigestOnBehalfOfType = _CucsPolicyDigestOnBehalfOfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 12),
    _CucsPolicyDigestOnBehalfOfType_Type()
)
cucsPolicyDigestOnBehalfOfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDigestOnBehalfOfType.setStatus("current")
_CucsPolicyDigestRequestorOwnership_Type = CucsPolicyPolicyOwner
_CucsPolicyDigestRequestorOwnership_Object = MibTableColumn
cucsPolicyDigestRequestorOwnership = _CucsPolicyDigestRequestorOwnership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 10, 1, 13),
    _CucsPolicyDigestRequestorOwnership_Type()
)
cucsPolicyDigestRequestorOwnership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDigestRequestorOwnership.setStatus("current")
_CucsPolicyDiscoveryTable_Object = MibTable
cucsPolicyDiscoveryTable = _CucsPolicyDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 11)
)
if mibBuilder.loadTexts:
    cucsPolicyDiscoveryTable.setStatus("current")
_CucsPolicyDiscoveryEntry_Object = MibTableRow
cucsPolicyDiscoveryEntry = _CucsPolicyDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 11, 1)
)
cucsPolicyDiscoveryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyDiscoveryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyDiscoveryEntry.setStatus("current")
_CucsPolicyDiscoveryInstanceId_Type = CucsManagedObjectId
_CucsPolicyDiscoveryInstanceId_Object = MibTableColumn
cucsPolicyDiscoveryInstanceId = _CucsPolicyDiscoveryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 11, 1, 1),
    _CucsPolicyDiscoveryInstanceId_Type()
)
cucsPolicyDiscoveryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyDiscoveryInstanceId.setStatus("current")
_CucsPolicyDiscoveryDn_Type = CucsManagedObjectDn
_CucsPolicyDiscoveryDn_Object = MibTableColumn
cucsPolicyDiscoveryDn = _CucsPolicyDiscoveryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 11, 1, 2),
    _CucsPolicyDiscoveryDn_Type()
)
cucsPolicyDiscoveryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDiscoveryDn.setStatus("current")
_CucsPolicyDiscoveryRn_Type = SnmpAdminString
_CucsPolicyDiscoveryRn_Object = MibTableColumn
cucsPolicyDiscoveryRn = _CucsPolicyDiscoveryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 11, 1, 3),
    _CucsPolicyDiscoveryRn_Type()
)
cucsPolicyDiscoveryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDiscoveryRn.setStatus("current")
_CucsPolicyDiscoverySource_Type = CucsPolicyControlSource
_CucsPolicyDiscoverySource_Object = MibTableColumn
cucsPolicyDiscoverySource = _CucsPolicyDiscoverySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 11, 1, 4),
    _CucsPolicyDiscoverySource_Type()
)
cucsPolicyDiscoverySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDiscoverySource.setStatus("current")
_CucsPolicyDnsTable_Object = MibTable
cucsPolicyDnsTable = _CucsPolicyDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 12)
)
if mibBuilder.loadTexts:
    cucsPolicyDnsTable.setStatus("current")
_CucsPolicyDnsEntry_Object = MibTableRow
cucsPolicyDnsEntry = _CucsPolicyDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 12, 1)
)
cucsPolicyDnsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyDnsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyDnsEntry.setStatus("current")
_CucsPolicyDnsInstanceId_Type = CucsManagedObjectId
_CucsPolicyDnsInstanceId_Object = MibTableColumn
cucsPolicyDnsInstanceId = _CucsPolicyDnsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 12, 1, 1),
    _CucsPolicyDnsInstanceId_Type()
)
cucsPolicyDnsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyDnsInstanceId.setStatus("current")
_CucsPolicyDnsDn_Type = CucsManagedObjectDn
_CucsPolicyDnsDn_Object = MibTableColumn
cucsPolicyDnsDn = _CucsPolicyDnsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 12, 1, 2),
    _CucsPolicyDnsDn_Type()
)
cucsPolicyDnsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDnsDn.setStatus("current")
_CucsPolicyDnsRn_Type = SnmpAdminString
_CucsPolicyDnsRn_Object = MibTableColumn
cucsPolicyDnsRn = _CucsPolicyDnsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 12, 1, 3),
    _CucsPolicyDnsRn_Type()
)
cucsPolicyDnsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDnsRn.setStatus("current")
_CucsPolicyDnsSource_Type = CucsPolicyControlSource
_CucsPolicyDnsSource_Object = MibTableColumn
cucsPolicyDnsSource = _CucsPolicyDnsSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 12, 1, 4),
    _CucsPolicyDnsSource_Type()
)
cucsPolicyDnsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyDnsSource.setStatus("current")
_CucsPolicyFaultTable_Object = MibTable
cucsPolicyFaultTable = _CucsPolicyFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 13)
)
if mibBuilder.loadTexts:
    cucsPolicyFaultTable.setStatus("current")
_CucsPolicyFaultEntry_Object = MibTableRow
cucsPolicyFaultEntry = _CucsPolicyFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 13, 1)
)
cucsPolicyFaultEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyFaultInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyFaultEntry.setStatus("current")
_CucsPolicyFaultInstanceId_Type = CucsManagedObjectId
_CucsPolicyFaultInstanceId_Object = MibTableColumn
cucsPolicyFaultInstanceId = _CucsPolicyFaultInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 13, 1, 1),
    _CucsPolicyFaultInstanceId_Type()
)
cucsPolicyFaultInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyFaultInstanceId.setStatus("current")
_CucsPolicyFaultDn_Type = CucsManagedObjectDn
_CucsPolicyFaultDn_Object = MibTableColumn
cucsPolicyFaultDn = _CucsPolicyFaultDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 13, 1, 2),
    _CucsPolicyFaultDn_Type()
)
cucsPolicyFaultDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyFaultDn.setStatus("current")
_CucsPolicyFaultRn_Type = SnmpAdminString
_CucsPolicyFaultRn_Object = MibTableColumn
cucsPolicyFaultRn = _CucsPolicyFaultRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 13, 1, 3),
    _CucsPolicyFaultRn_Type()
)
cucsPolicyFaultRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyFaultRn.setStatus("current")
_CucsPolicyFaultSource_Type = CucsPolicyControlSource
_CucsPolicyFaultSource_Object = MibTableColumn
cucsPolicyFaultSource = _CucsPolicyFaultSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 13, 1, 4),
    _CucsPolicyFaultSource_Type()
)
cucsPolicyFaultSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyFaultSource.setStatus("current")
_CucsPolicyInfraFirmwareTable_Object = MibTable
cucsPolicyInfraFirmwareTable = _CucsPolicyInfraFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 14)
)
if mibBuilder.loadTexts:
    cucsPolicyInfraFirmwareTable.setStatus("current")
_CucsPolicyInfraFirmwareEntry_Object = MibTableRow
cucsPolicyInfraFirmwareEntry = _CucsPolicyInfraFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 14, 1)
)
cucsPolicyInfraFirmwareEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyInfraFirmwareInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyInfraFirmwareEntry.setStatus("current")
_CucsPolicyInfraFirmwareInstanceId_Type = CucsManagedObjectId
_CucsPolicyInfraFirmwareInstanceId_Object = MibTableColumn
cucsPolicyInfraFirmwareInstanceId = _CucsPolicyInfraFirmwareInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 14, 1, 1),
    _CucsPolicyInfraFirmwareInstanceId_Type()
)
cucsPolicyInfraFirmwareInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyInfraFirmwareInstanceId.setStatus("current")
_CucsPolicyInfraFirmwareDn_Type = CucsManagedObjectDn
_CucsPolicyInfraFirmwareDn_Object = MibTableColumn
cucsPolicyInfraFirmwareDn = _CucsPolicyInfraFirmwareDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 14, 1, 2),
    _CucsPolicyInfraFirmwareDn_Type()
)
cucsPolicyInfraFirmwareDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyInfraFirmwareDn.setStatus("current")
_CucsPolicyInfraFirmwareRn_Type = SnmpAdminString
_CucsPolicyInfraFirmwareRn_Object = MibTableColumn
cucsPolicyInfraFirmwareRn = _CucsPolicyInfraFirmwareRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 14, 1, 3),
    _CucsPolicyInfraFirmwareRn_Type()
)
cucsPolicyInfraFirmwareRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyInfraFirmwareRn.setStatus("current")
_CucsPolicyInfraFirmwareSource_Type = CucsPolicyControlSource
_CucsPolicyInfraFirmwareSource_Object = MibTableColumn
cucsPolicyInfraFirmwareSource = _CucsPolicyInfraFirmwareSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 14, 1, 4),
    _CucsPolicyInfraFirmwareSource_Type()
)
cucsPolicyInfraFirmwareSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyInfraFirmwareSource.setStatus("current")
_CucsPolicyMEpTable_Object = MibTable
cucsPolicyMEpTable = _CucsPolicyMEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 15)
)
if mibBuilder.loadTexts:
    cucsPolicyMEpTable.setStatus("current")
_CucsPolicyMEpEntry_Object = MibTableRow
cucsPolicyMEpEntry = _CucsPolicyMEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 15, 1)
)
cucsPolicyMEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyMEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyMEpEntry.setStatus("current")
_CucsPolicyMEpInstanceId_Type = CucsManagedObjectId
_CucsPolicyMEpInstanceId_Object = MibTableColumn
cucsPolicyMEpInstanceId = _CucsPolicyMEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 15, 1, 1),
    _CucsPolicyMEpInstanceId_Type()
)
cucsPolicyMEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyMEpInstanceId.setStatus("current")
_CucsPolicyMEpDn_Type = CucsManagedObjectDn
_CucsPolicyMEpDn_Object = MibTableColumn
cucsPolicyMEpDn = _CucsPolicyMEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 15, 1, 2),
    _CucsPolicyMEpDn_Type()
)
cucsPolicyMEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyMEpDn.setStatus("current")
_CucsPolicyMEpRn_Type = SnmpAdminString
_CucsPolicyMEpRn_Object = MibTableColumn
cucsPolicyMEpRn = _CucsPolicyMEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 15, 1, 3),
    _CucsPolicyMEpRn_Type()
)
cucsPolicyMEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyMEpRn.setStatus("current")
_CucsPolicyMEpSource_Type = CucsPolicyControlSource
_CucsPolicyMEpSource_Object = MibTableColumn
cucsPolicyMEpSource = _CucsPolicyMEpSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 15, 1, 4),
    _CucsPolicyMEpSource_Type()
)
cucsPolicyMEpSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyMEpSource.setStatus("current")
_CucsPolicyMonitoringTable_Object = MibTable
cucsPolicyMonitoringTable = _CucsPolicyMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 16)
)
if mibBuilder.loadTexts:
    cucsPolicyMonitoringTable.setStatus("current")
_CucsPolicyMonitoringEntry_Object = MibTableRow
cucsPolicyMonitoringEntry = _CucsPolicyMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 16, 1)
)
cucsPolicyMonitoringEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyMonitoringInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyMonitoringEntry.setStatus("current")
_CucsPolicyMonitoringInstanceId_Type = CucsManagedObjectId
_CucsPolicyMonitoringInstanceId_Object = MibTableColumn
cucsPolicyMonitoringInstanceId = _CucsPolicyMonitoringInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 16, 1, 1),
    _CucsPolicyMonitoringInstanceId_Type()
)
cucsPolicyMonitoringInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyMonitoringInstanceId.setStatus("current")
_CucsPolicyMonitoringDn_Type = CucsManagedObjectDn
_CucsPolicyMonitoringDn_Object = MibTableColumn
cucsPolicyMonitoringDn = _CucsPolicyMonitoringDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 16, 1, 2),
    _CucsPolicyMonitoringDn_Type()
)
cucsPolicyMonitoringDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyMonitoringDn.setStatus("current")
_CucsPolicyMonitoringRn_Type = SnmpAdminString
_CucsPolicyMonitoringRn_Object = MibTableColumn
cucsPolicyMonitoringRn = _CucsPolicyMonitoringRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 16, 1, 3),
    _CucsPolicyMonitoringRn_Type()
)
cucsPolicyMonitoringRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyMonitoringRn.setStatus("current")
_CucsPolicyMonitoringSource_Type = CucsPolicyControlSource
_CucsPolicyMonitoringSource_Object = MibTableColumn
cucsPolicyMonitoringSource = _CucsPolicyMonitoringSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 16, 1, 4),
    _CucsPolicyMonitoringSource_Type()
)
cucsPolicyMonitoringSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyMonitoringSource.setStatus("current")
_CucsPolicyPolicyEpTable_Object = MibTable
cucsPolicyPolicyEpTable = _CucsPolicyPolicyEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 17)
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyEpTable.setStatus("current")
_CucsPolicyPolicyEpEntry_Object = MibTableRow
cucsPolicyPolicyEpEntry = _CucsPolicyPolicyEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 17, 1)
)
cucsPolicyPolicyEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyPolicyEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyEpEntry.setStatus("current")
_CucsPolicyPolicyEpInstanceId_Type = CucsManagedObjectId
_CucsPolicyPolicyEpInstanceId_Object = MibTableColumn
cucsPolicyPolicyEpInstanceId = _CucsPolicyPolicyEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 17, 1, 1),
    _CucsPolicyPolicyEpInstanceId_Type()
)
cucsPolicyPolicyEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyPolicyEpInstanceId.setStatus("current")
_CucsPolicyPolicyEpDn_Type = CucsManagedObjectDn
_CucsPolicyPolicyEpDn_Object = MibTableColumn
cucsPolicyPolicyEpDn = _CucsPolicyPolicyEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 17, 1, 2),
    _CucsPolicyPolicyEpDn_Type()
)
cucsPolicyPolicyEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyEpDn.setStatus("current")
_CucsPolicyPolicyEpRn_Type = SnmpAdminString
_CucsPolicyPolicyEpRn_Object = MibTableColumn
cucsPolicyPolicyEpRn = _CucsPolicyPolicyEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 17, 1, 3),
    _CucsPolicyPolicyEpRn_Type()
)
cucsPolicyPolicyEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyEpRn.setStatus("current")
_CucsPolicyPolicyRequestorTable_Object = MibTable
cucsPolicyPolicyRequestorTable = _CucsPolicyPolicyRequestorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 18)
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyRequestorTable.setStatus("current")
_CucsPolicyPolicyRequestorEntry_Object = MibTableRow
cucsPolicyPolicyRequestorEntry = _CucsPolicyPolicyRequestorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 18, 1)
)
cucsPolicyPolicyRequestorEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyPolicyRequestorInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyRequestorEntry.setStatus("current")
_CucsPolicyPolicyRequestorInstanceId_Type = CucsManagedObjectId
_CucsPolicyPolicyRequestorInstanceId_Object = MibTableColumn
cucsPolicyPolicyRequestorInstanceId = _CucsPolicyPolicyRequestorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 18, 1, 1),
    _CucsPolicyPolicyRequestorInstanceId_Type()
)
cucsPolicyPolicyRequestorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyPolicyRequestorInstanceId.setStatus("current")
_CucsPolicyPolicyRequestorDn_Type = CucsManagedObjectDn
_CucsPolicyPolicyRequestorDn_Object = MibTableColumn
cucsPolicyPolicyRequestorDn = _CucsPolicyPolicyRequestorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 18, 1, 2),
    _CucsPolicyPolicyRequestorDn_Type()
)
cucsPolicyPolicyRequestorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyRequestorDn.setStatus("current")
_CucsPolicyPolicyRequestorRn_Type = SnmpAdminString
_CucsPolicyPolicyRequestorRn_Object = MibTableColumn
cucsPolicyPolicyRequestorRn = _CucsPolicyPolicyRequestorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 18, 1, 3),
    _CucsPolicyPolicyRequestorRn_Type()
)
cucsPolicyPolicyRequestorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyRequestorRn.setStatus("current")
_CucsPolicyPolicyRequestorName_Type = SnmpAdminString
_CucsPolicyPolicyRequestorName_Object = MibTableColumn
cucsPolicyPolicyRequestorName = _CucsPolicyPolicyRequestorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 18, 1, 4),
    _CucsPolicyPolicyRequestorName_Type()
)
cucsPolicyPolicyRequestorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyRequestorName.setStatus("current")
_CucsPolicyPolicyRequestorOnBehalfOfIdent_Type = SnmpAdminString
_CucsPolicyPolicyRequestorOnBehalfOfIdent_Object = MibTableColumn
cucsPolicyPolicyRequestorOnBehalfOfIdent = _CucsPolicyPolicyRequestorOnBehalfOfIdent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 18, 1, 5),
    _CucsPolicyPolicyRequestorOnBehalfOfIdent_Type()
)
cucsPolicyPolicyRequestorOnBehalfOfIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyRequestorOnBehalfOfIdent.setStatus("current")
_CucsPolicyPolicyRequestorOnBehalfOfType_Type = SnmpAdminString
_CucsPolicyPolicyRequestorOnBehalfOfType_Object = MibTableColumn
cucsPolicyPolicyRequestorOnBehalfOfType = _CucsPolicyPolicyRequestorOnBehalfOfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 18, 1, 6),
    _CucsPolicyPolicyRequestorOnBehalfOfType_Type()
)
cucsPolicyPolicyRequestorOnBehalfOfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyRequestorOnBehalfOfType.setStatus("current")
_CucsPolicyPolicyRequestorResolvedClassType_Type = SnmpAdminString
_CucsPolicyPolicyRequestorResolvedClassType_Object = MibTableColumn
cucsPolicyPolicyRequestorResolvedClassType = _CucsPolicyPolicyRequestorResolvedClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 18, 1, 7),
    _CucsPolicyPolicyRequestorResolvedClassType_Type()
)
cucsPolicyPolicyRequestorResolvedClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyRequestorResolvedClassType.setStatus("current")
_CucsPolicyPolicyScopeTable_Object = MibTable
cucsPolicyPolicyScopeTable = _CucsPolicyPolicyScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19)
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeTable.setStatus("current")
_CucsPolicyPolicyScopeEntry_Object = MibTableRow
cucsPolicyPolicyScopeEntry = _CucsPolicyPolicyScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1)
)
cucsPolicyPolicyScopeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyPolicyScopeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeEntry.setStatus("current")
_CucsPolicyPolicyScopeInstanceId_Type = CucsManagedObjectId
_CucsPolicyPolicyScopeInstanceId_Object = MibTableColumn
cucsPolicyPolicyScopeInstanceId = _CucsPolicyPolicyScopeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 1),
    _CucsPolicyPolicyScopeInstanceId_Type()
)
cucsPolicyPolicyScopeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeInstanceId.setStatus("current")
_CucsPolicyPolicyScopeDn_Type = CucsManagedObjectDn
_CucsPolicyPolicyScopeDn_Object = MibTableColumn
cucsPolicyPolicyScopeDn = _CucsPolicyPolicyScopeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 2),
    _CucsPolicyPolicyScopeDn_Type()
)
cucsPolicyPolicyScopeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeDn.setStatus("current")
_CucsPolicyPolicyScopeRn_Type = SnmpAdminString
_CucsPolicyPolicyScopeRn_Object = MibTableColumn
cucsPolicyPolicyScopeRn = _CucsPolicyPolicyScopeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 3),
    _CucsPolicyPolicyScopeRn_Type()
)
cucsPolicyPolicyScopeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeRn.setStatus("current")
_CucsPolicyPolicyScopeAppType_Type = SnmpAdminString
_CucsPolicyPolicyScopeAppType_Object = MibTableColumn
cucsPolicyPolicyScopeAppType = _CucsPolicyPolicyScopeAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 4),
    _CucsPolicyPolicyScopeAppType_Type()
)
cucsPolicyPolicyScopeAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeAppType.setStatus("current")
_CucsPolicyPolicyScopeDefaultPolicyName_Type = SnmpAdminString
_CucsPolicyPolicyScopeDefaultPolicyName_Object = MibTableColumn
cucsPolicyPolicyScopeDefaultPolicyName = _CucsPolicyPolicyScopeDefaultPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 5),
    _CucsPolicyPolicyScopeDefaultPolicyName_Type()
)
cucsPolicyPolicyScopeDefaultPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeDefaultPolicyName.setStatus("current")
_CucsPolicyPolicyScopeFsmDescr_Type = SnmpAdminString
_CucsPolicyPolicyScopeFsmDescr_Object = MibTableColumn
cucsPolicyPolicyScopeFsmDescr = _CucsPolicyPolicyScopeFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 6),
    _CucsPolicyPolicyScopeFsmDescr_Type()
)
cucsPolicyPolicyScopeFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmDescr.setStatus("current")
_CucsPolicyPolicyScopeFsmPrev_Type = SnmpAdminString
_CucsPolicyPolicyScopeFsmPrev_Object = MibTableColumn
cucsPolicyPolicyScopeFsmPrev = _CucsPolicyPolicyScopeFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 7),
    _CucsPolicyPolicyScopeFsmPrev_Type()
)
cucsPolicyPolicyScopeFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmPrev.setStatus("current")
_CucsPolicyPolicyScopeFsmProgr_Type = Gauge32
_CucsPolicyPolicyScopeFsmProgr_Object = MibTableColumn
cucsPolicyPolicyScopeFsmProgr = _CucsPolicyPolicyScopeFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 8),
    _CucsPolicyPolicyScopeFsmProgr_Type()
)
cucsPolicyPolicyScopeFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmProgr.setStatus("current")
_CucsPolicyPolicyScopeFsmRmtInvErrCode_Type = Gauge32
_CucsPolicyPolicyScopeFsmRmtInvErrCode_Object = MibTableColumn
cucsPolicyPolicyScopeFsmRmtInvErrCode = _CucsPolicyPolicyScopeFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 9),
    _CucsPolicyPolicyScopeFsmRmtInvErrCode_Type()
)
cucsPolicyPolicyScopeFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmRmtInvErrCode.setStatus("current")
_CucsPolicyPolicyScopeFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsPolicyPolicyScopeFsmRmtInvErrDescr_Object = MibTableColumn
cucsPolicyPolicyScopeFsmRmtInvErrDescr = _CucsPolicyPolicyScopeFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 10),
    _CucsPolicyPolicyScopeFsmRmtInvErrDescr_Type()
)
cucsPolicyPolicyScopeFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmRmtInvErrDescr.setStatus("current")
_CucsPolicyPolicyScopeFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsPolicyPolicyScopeFsmRmtInvRslt_Object = MibTableColumn
cucsPolicyPolicyScopeFsmRmtInvRslt = _CucsPolicyPolicyScopeFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 11),
    _CucsPolicyPolicyScopeFsmRmtInvRslt_Type()
)
cucsPolicyPolicyScopeFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmRmtInvRslt.setStatus("current")
_CucsPolicyPolicyScopeFsmStageDescr_Type = SnmpAdminString
_CucsPolicyPolicyScopeFsmStageDescr_Object = MibTableColumn
cucsPolicyPolicyScopeFsmStageDescr = _CucsPolicyPolicyScopeFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 12),
    _CucsPolicyPolicyScopeFsmStageDescr_Type()
)
cucsPolicyPolicyScopeFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStageDescr.setStatus("current")
_CucsPolicyPolicyScopeFsmStamp_Type = DateAndTime
_CucsPolicyPolicyScopeFsmStamp_Object = MibTableColumn
cucsPolicyPolicyScopeFsmStamp = _CucsPolicyPolicyScopeFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 13),
    _CucsPolicyPolicyScopeFsmStamp_Type()
)
cucsPolicyPolicyScopeFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStamp.setStatus("current")
_CucsPolicyPolicyScopeFsmStatus_Type = SnmpAdminString
_CucsPolicyPolicyScopeFsmStatus_Object = MibTableColumn
cucsPolicyPolicyScopeFsmStatus = _CucsPolicyPolicyScopeFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 14),
    _CucsPolicyPolicyScopeFsmStatus_Type()
)
cucsPolicyPolicyScopeFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStatus.setStatus("current")
_CucsPolicyPolicyScopeFsmTry_Type = Gauge32
_CucsPolicyPolicyScopeFsmTry_Object = MibTableColumn
cucsPolicyPolicyScopeFsmTry = _CucsPolicyPolicyScopeFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 15),
    _CucsPolicyPolicyScopeFsmTry_Type()
)
cucsPolicyPolicyScopeFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmTry.setStatus("current")
_CucsPolicyPolicyScopeOperStatus_Type = CucsPolicyPolicyOperStatus
_CucsPolicyPolicyScopeOperStatus_Object = MibTableColumn
cucsPolicyPolicyScopeOperStatus = _CucsPolicyPolicyScopeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 16),
    _CucsPolicyPolicyScopeOperStatus_Type()
)
cucsPolicyPolicyScopeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeOperStatus.setStatus("current")
_CucsPolicyPolicyScopeOwner_Type = CucsPolicyPolicyOwner
_CucsPolicyPolicyScopeOwner_Object = MibTableColumn
cucsPolicyPolicyScopeOwner = _CucsPolicyPolicyScopeOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 17),
    _CucsPolicyPolicyScopeOwner_Type()
)
cucsPolicyPolicyScopeOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeOwner.setStatus("current")
_CucsPolicyPolicyScopePolicyName_Type = SnmpAdminString
_CucsPolicyPolicyScopePolicyName_Object = MibTableColumn
cucsPolicyPolicyScopePolicyName = _CucsPolicyPolicyScopePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 18),
    _CucsPolicyPolicyScopePolicyName_Type()
)
cucsPolicyPolicyScopePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopePolicyName.setStatus("current")
_CucsPolicyPolicyScopePolicyType_Type = SnmpAdminString
_CucsPolicyPolicyScopePolicyType_Object = MibTableColumn
cucsPolicyPolicyScopePolicyType = _CucsPolicyPolicyScopePolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 19),
    _CucsPolicyPolicyScopePolicyType_Type()
)
cucsPolicyPolicyScopePolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopePolicyType.setStatus("current")
_CucsPolicyPolicyScopeRecursive_Type = TruthValue
_CucsPolicyPolicyScopeRecursive_Object = MibTableColumn
cucsPolicyPolicyScopeRecursive = _CucsPolicyPolicyScopeRecursive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 20),
    _CucsPolicyPolicyScopeRecursive_Type()
)
cucsPolicyPolicyScopeRecursive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeRecursive.setStatus("current")
_CucsPolicyPolicyScopeResolveType_Type = CucsPolicyPolicyResolveType
_CucsPolicyPolicyScopeResolveType_Object = MibTableColumn
cucsPolicyPolicyScopeResolveType = _CucsPolicyPolicyScopeResolveType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 19, 1, 21),
    _CucsPolicyPolicyScopeResolveType_Type()
)
cucsPolicyPolicyScopeResolveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeResolveType.setStatus("current")
_CucsPolicyPolicyScopeContTable_Object = MibTable
cucsPolicyPolicyScopeContTable = _CucsPolicyPolicyScopeContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 20)
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContTable.setStatus("current")
_CucsPolicyPolicyScopeContEntry_Object = MibTableRow
cucsPolicyPolicyScopeContEntry = _CucsPolicyPolicyScopeContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 20, 1)
)
cucsPolicyPolicyScopeContEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyPolicyScopeContInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContEntry.setStatus("current")
_CucsPolicyPolicyScopeContInstanceId_Type = CucsManagedObjectId
_CucsPolicyPolicyScopeContInstanceId_Object = MibTableColumn
cucsPolicyPolicyScopeContInstanceId = _CucsPolicyPolicyScopeContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 20, 1, 1),
    _CucsPolicyPolicyScopeContInstanceId_Type()
)
cucsPolicyPolicyScopeContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContInstanceId.setStatus("current")
_CucsPolicyPolicyScopeContDn_Type = CucsManagedObjectDn
_CucsPolicyPolicyScopeContDn_Object = MibTableColumn
cucsPolicyPolicyScopeContDn = _CucsPolicyPolicyScopeContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 20, 1, 2),
    _CucsPolicyPolicyScopeContDn_Type()
)
cucsPolicyPolicyScopeContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContDn.setStatus("current")
_CucsPolicyPolicyScopeContRn_Type = SnmpAdminString
_CucsPolicyPolicyScopeContRn_Object = MibTableColumn
cucsPolicyPolicyScopeContRn = _CucsPolicyPolicyScopeContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 20, 1, 3),
    _CucsPolicyPolicyScopeContRn_Type()
)
cucsPolicyPolicyScopeContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContRn.setStatus("current")
_CucsPolicyPolicyScopeContAppType_Type = SnmpAdminString
_CucsPolicyPolicyScopeContAppType_Object = MibTableColumn
cucsPolicyPolicyScopeContAppType = _CucsPolicyPolicyScopeContAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 20, 1, 4),
    _CucsPolicyPolicyScopeContAppType_Type()
)
cucsPolicyPolicyScopeContAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContAppType.setStatus("current")
_CucsPolicyPolicyScopeContGenNum_Type = Gauge32
_CucsPolicyPolicyScopeContGenNum_Object = MibTableColumn
cucsPolicyPolicyScopeContGenNum = _CucsPolicyPolicyScopeContGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 20, 1, 5),
    _CucsPolicyPolicyScopeContGenNum_Type()
)
cucsPolicyPolicyScopeContGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContGenNum.setStatus("current")
_CucsPolicyPolicyScopeContNeedRecovery_Type = TruthValue
_CucsPolicyPolicyScopeContNeedRecovery_Object = MibTableColumn
cucsPolicyPolicyScopeContNeedRecovery = _CucsPolicyPolicyScopeContNeedRecovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 20, 1, 6),
    _CucsPolicyPolicyScopeContNeedRecovery_Type()
)
cucsPolicyPolicyScopeContNeedRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContNeedRecovery.setStatus("current")
_CucsPolicyPolicyScopeContextTable_Object = MibTable
cucsPolicyPolicyScopeContextTable = _CucsPolicyPolicyScopeContextTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 21)
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContextTable.setStatus("current")
_CucsPolicyPolicyScopeContextEntry_Object = MibTableRow
cucsPolicyPolicyScopeContextEntry = _CucsPolicyPolicyScopeContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 21, 1)
)
cucsPolicyPolicyScopeContextEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyPolicyScopeContextInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContextEntry.setStatus("current")
_CucsPolicyPolicyScopeContextInstanceId_Type = CucsManagedObjectId
_CucsPolicyPolicyScopeContextInstanceId_Object = MibTableColumn
cucsPolicyPolicyScopeContextInstanceId = _CucsPolicyPolicyScopeContextInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 21, 1, 1),
    _CucsPolicyPolicyScopeContextInstanceId_Type()
)
cucsPolicyPolicyScopeContextInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContextInstanceId.setStatus("current")
_CucsPolicyPolicyScopeContextDn_Type = CucsManagedObjectDn
_CucsPolicyPolicyScopeContextDn_Object = MibTableColumn
cucsPolicyPolicyScopeContextDn = _CucsPolicyPolicyScopeContextDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 21, 1, 2),
    _CucsPolicyPolicyScopeContextDn_Type()
)
cucsPolicyPolicyScopeContextDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContextDn.setStatus("current")
_CucsPolicyPolicyScopeContextRn_Type = SnmpAdminString
_CucsPolicyPolicyScopeContextRn_Object = MibTableColumn
cucsPolicyPolicyScopeContextRn = _CucsPolicyPolicyScopeContextRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 21, 1, 3),
    _CucsPolicyPolicyScopeContextRn_Type()
)
cucsPolicyPolicyScopeContextRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContextRn.setStatus("current")
_CucsPolicyPolicyScopeContextContext_Type = SnmpAdminString
_CucsPolicyPolicyScopeContextContext_Object = MibTableColumn
cucsPolicyPolicyScopeContextContext = _CucsPolicyPolicyScopeContextContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 21, 1, 4),
    _CucsPolicyPolicyScopeContextContext_Type()
)
cucsPolicyPolicyScopeContextContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContextContext.setStatus("current")
_CucsPolicyPolicyScopeContextName_Type = SnmpAdminString
_CucsPolicyPolicyScopeContextName_Object = MibTableColumn
cucsPolicyPolicyScopeContextName = _CucsPolicyPolicyScopeContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 21, 1, 5),
    _CucsPolicyPolicyScopeContextName_Type()
)
cucsPolicyPolicyScopeContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeContextName.setStatus("current")
_CucsPolicyPolicyScopeFsmTable_Object = MibTable
cucsPolicyPolicyScopeFsmTable = _CucsPolicyPolicyScopeFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22)
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmTable.setStatus("current")
_CucsPolicyPolicyScopeFsmEntry_Object = MibTableRow
cucsPolicyPolicyScopeFsmEntry = _CucsPolicyPolicyScopeFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22, 1)
)
cucsPolicyPolicyScopeFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyPolicyScopeFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmEntry.setStatus("current")
_CucsPolicyPolicyScopeFsmInstanceId_Type = CucsManagedObjectId
_CucsPolicyPolicyScopeFsmInstanceId_Object = MibTableColumn
cucsPolicyPolicyScopeFsmInstanceId = _CucsPolicyPolicyScopeFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22, 1, 1),
    _CucsPolicyPolicyScopeFsmInstanceId_Type()
)
cucsPolicyPolicyScopeFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmInstanceId.setStatus("current")
_CucsPolicyPolicyScopeFsmDn_Type = CucsManagedObjectDn
_CucsPolicyPolicyScopeFsmDn_Object = MibTableColumn
cucsPolicyPolicyScopeFsmDn = _CucsPolicyPolicyScopeFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22, 1, 2),
    _CucsPolicyPolicyScopeFsmDn_Type()
)
cucsPolicyPolicyScopeFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmDn.setStatus("current")
_CucsPolicyPolicyScopeFsmRn_Type = SnmpAdminString
_CucsPolicyPolicyScopeFsmRn_Object = MibTableColumn
cucsPolicyPolicyScopeFsmRn = _CucsPolicyPolicyScopeFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22, 1, 3),
    _CucsPolicyPolicyScopeFsmRn_Type()
)
cucsPolicyPolicyScopeFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmRn.setStatus("current")
_CucsPolicyPolicyScopeFsmCompletionTime_Type = DateAndTime
_CucsPolicyPolicyScopeFsmCompletionTime_Object = MibTableColumn
cucsPolicyPolicyScopeFsmCompletionTime = _CucsPolicyPolicyScopeFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22, 1, 4),
    _CucsPolicyPolicyScopeFsmCompletionTime_Type()
)
cucsPolicyPolicyScopeFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmCompletionTime.setStatus("current")
_CucsPolicyPolicyScopeFsmCurrentFsm_Type = CucsPolicyPolicyScopeFsmCurrentFsm
_CucsPolicyPolicyScopeFsmCurrentFsm_Object = MibTableColumn
cucsPolicyPolicyScopeFsmCurrentFsm = _CucsPolicyPolicyScopeFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22, 1, 5),
    _CucsPolicyPolicyScopeFsmCurrentFsm_Type()
)
cucsPolicyPolicyScopeFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmCurrentFsm.setStatus("current")
_CucsPolicyPolicyScopeFsmDescrData_Type = SnmpAdminString
_CucsPolicyPolicyScopeFsmDescrData_Object = MibTableColumn
cucsPolicyPolicyScopeFsmDescrData = _CucsPolicyPolicyScopeFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22, 1, 6),
    _CucsPolicyPolicyScopeFsmDescrData_Type()
)
cucsPolicyPolicyScopeFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmDescrData.setStatus("current")
_CucsPolicyPolicyScopeFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsPolicyPolicyScopeFsmFsmStatus_Object = MibTableColumn
cucsPolicyPolicyScopeFsmFsmStatus = _CucsPolicyPolicyScopeFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22, 1, 7),
    _CucsPolicyPolicyScopeFsmFsmStatus_Type()
)
cucsPolicyPolicyScopeFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmFsmStatus.setStatus("current")
_CucsPolicyPolicyScopeFsmProgress_Type = Gauge32
_CucsPolicyPolicyScopeFsmProgress_Object = MibTableColumn
cucsPolicyPolicyScopeFsmProgress = _CucsPolicyPolicyScopeFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22, 1, 8),
    _CucsPolicyPolicyScopeFsmProgress_Type()
)
cucsPolicyPolicyScopeFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmProgress.setStatus("current")
_CucsPolicyPolicyScopeFsmRmtErrCode_Type = Gauge32
_CucsPolicyPolicyScopeFsmRmtErrCode_Object = MibTableColumn
cucsPolicyPolicyScopeFsmRmtErrCode = _CucsPolicyPolicyScopeFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22, 1, 9),
    _CucsPolicyPolicyScopeFsmRmtErrCode_Type()
)
cucsPolicyPolicyScopeFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmRmtErrCode.setStatus("current")
_CucsPolicyPolicyScopeFsmRmtErrDescr_Type = SnmpAdminString
_CucsPolicyPolicyScopeFsmRmtErrDescr_Object = MibTableColumn
cucsPolicyPolicyScopeFsmRmtErrDescr = _CucsPolicyPolicyScopeFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22, 1, 10),
    _CucsPolicyPolicyScopeFsmRmtErrDescr_Type()
)
cucsPolicyPolicyScopeFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmRmtErrDescr.setStatus("current")
_CucsPolicyPolicyScopeFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsPolicyPolicyScopeFsmRmtRslt_Object = MibTableColumn
cucsPolicyPolicyScopeFsmRmtRslt = _CucsPolicyPolicyScopeFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 22, 1, 11),
    _CucsPolicyPolicyScopeFsmRmtRslt_Type()
)
cucsPolicyPolicyScopeFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmRmtRslt.setStatus("current")
_CucsPolicyPolicyScopeFsmStageTable_Object = MibTable
cucsPolicyPolicyScopeFsmStageTable = _CucsPolicyPolicyScopeFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 23)
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStageTable.setStatus("current")
_CucsPolicyPolicyScopeFsmStageEntry_Object = MibTableRow
cucsPolicyPolicyScopeFsmStageEntry = _CucsPolicyPolicyScopeFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 23, 1)
)
cucsPolicyPolicyScopeFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyPolicyScopeFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStageEntry.setStatus("current")
_CucsPolicyPolicyScopeFsmStageInstanceId_Type = CucsManagedObjectId
_CucsPolicyPolicyScopeFsmStageInstanceId_Object = MibTableColumn
cucsPolicyPolicyScopeFsmStageInstanceId = _CucsPolicyPolicyScopeFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 23, 1, 1),
    _CucsPolicyPolicyScopeFsmStageInstanceId_Type()
)
cucsPolicyPolicyScopeFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStageInstanceId.setStatus("current")
_CucsPolicyPolicyScopeFsmStageDn_Type = CucsManagedObjectDn
_CucsPolicyPolicyScopeFsmStageDn_Object = MibTableColumn
cucsPolicyPolicyScopeFsmStageDn = _CucsPolicyPolicyScopeFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 23, 1, 2),
    _CucsPolicyPolicyScopeFsmStageDn_Type()
)
cucsPolicyPolicyScopeFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStageDn.setStatus("current")
_CucsPolicyPolicyScopeFsmStageRn_Type = SnmpAdminString
_CucsPolicyPolicyScopeFsmStageRn_Object = MibTableColumn
cucsPolicyPolicyScopeFsmStageRn = _CucsPolicyPolicyScopeFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 23, 1, 3),
    _CucsPolicyPolicyScopeFsmStageRn_Type()
)
cucsPolicyPolicyScopeFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStageRn.setStatus("current")
_CucsPolicyPolicyScopeFsmStageDescrData_Type = SnmpAdminString
_CucsPolicyPolicyScopeFsmStageDescrData_Object = MibTableColumn
cucsPolicyPolicyScopeFsmStageDescrData = _CucsPolicyPolicyScopeFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 23, 1, 4),
    _CucsPolicyPolicyScopeFsmStageDescrData_Type()
)
cucsPolicyPolicyScopeFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStageDescrData.setStatus("current")
_CucsPolicyPolicyScopeFsmStageLastUpdateTime_Type = DateAndTime
_CucsPolicyPolicyScopeFsmStageLastUpdateTime_Object = MibTableColumn
cucsPolicyPolicyScopeFsmStageLastUpdateTime = _CucsPolicyPolicyScopeFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 23, 1, 5),
    _CucsPolicyPolicyScopeFsmStageLastUpdateTime_Type()
)
cucsPolicyPolicyScopeFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStageLastUpdateTime.setStatus("current")
_CucsPolicyPolicyScopeFsmStageName_Type = CucsPolicyPolicyScopeFsmStageName
_CucsPolicyPolicyScopeFsmStageName_Object = MibTableColumn
cucsPolicyPolicyScopeFsmStageName = _CucsPolicyPolicyScopeFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 23, 1, 6),
    _CucsPolicyPolicyScopeFsmStageName_Type()
)
cucsPolicyPolicyScopeFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStageName.setStatus("current")
_CucsPolicyPolicyScopeFsmStageOrder_Type = Gauge32
_CucsPolicyPolicyScopeFsmStageOrder_Object = MibTableColumn
cucsPolicyPolicyScopeFsmStageOrder = _CucsPolicyPolicyScopeFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 23, 1, 7),
    _CucsPolicyPolicyScopeFsmStageOrder_Type()
)
cucsPolicyPolicyScopeFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStageOrder.setStatus("current")
_CucsPolicyPolicyScopeFsmStageRetry_Type = Gauge32
_CucsPolicyPolicyScopeFsmStageRetry_Object = MibTableColumn
cucsPolicyPolicyScopeFsmStageRetry = _CucsPolicyPolicyScopeFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 23, 1, 8),
    _CucsPolicyPolicyScopeFsmStageRetry_Type()
)
cucsPolicyPolicyScopeFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStageRetry.setStatus("current")
_CucsPolicyPolicyScopeFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsPolicyPolicyScopeFsmStageStageStatus_Object = MibTableColumn
cucsPolicyPolicyScopeFsmStageStageStatus = _CucsPolicyPolicyScopeFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 23, 1, 9),
    _CucsPolicyPolicyScopeFsmStageStageStatus_Type()
)
cucsPolicyPolicyScopeFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmStageStageStatus.setStatus("current")
_CucsPolicyPolicyScopeFsmTaskTable_Object = MibTable
cucsPolicyPolicyScopeFsmTaskTable = _CucsPolicyPolicyScopeFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 24)
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmTaskTable.setStatus("current")
_CucsPolicyPolicyScopeFsmTaskEntry_Object = MibTableRow
cucsPolicyPolicyScopeFsmTaskEntry = _CucsPolicyPolicyScopeFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 24, 1)
)
cucsPolicyPolicyScopeFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyPolicyScopeFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmTaskEntry.setStatus("current")
_CucsPolicyPolicyScopeFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsPolicyPolicyScopeFsmTaskInstanceId_Object = MibTableColumn
cucsPolicyPolicyScopeFsmTaskInstanceId = _CucsPolicyPolicyScopeFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 24, 1, 1),
    _CucsPolicyPolicyScopeFsmTaskInstanceId_Type()
)
cucsPolicyPolicyScopeFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmTaskInstanceId.setStatus("current")
_CucsPolicyPolicyScopeFsmTaskDn_Type = CucsManagedObjectDn
_CucsPolicyPolicyScopeFsmTaskDn_Object = MibTableColumn
cucsPolicyPolicyScopeFsmTaskDn = _CucsPolicyPolicyScopeFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 24, 1, 2),
    _CucsPolicyPolicyScopeFsmTaskDn_Type()
)
cucsPolicyPolicyScopeFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmTaskDn.setStatus("current")
_CucsPolicyPolicyScopeFsmTaskRn_Type = SnmpAdminString
_CucsPolicyPolicyScopeFsmTaskRn_Object = MibTableColumn
cucsPolicyPolicyScopeFsmTaskRn = _CucsPolicyPolicyScopeFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 24, 1, 3),
    _CucsPolicyPolicyScopeFsmTaskRn_Type()
)
cucsPolicyPolicyScopeFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmTaskRn.setStatus("current")
_CucsPolicyPolicyScopeFsmTaskCompletion_Type = CucsFsmCompletion
_CucsPolicyPolicyScopeFsmTaskCompletion_Object = MibTableColumn
cucsPolicyPolicyScopeFsmTaskCompletion = _CucsPolicyPolicyScopeFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 24, 1, 4),
    _CucsPolicyPolicyScopeFsmTaskCompletion_Type()
)
cucsPolicyPolicyScopeFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmTaskCompletion.setStatus("current")
_CucsPolicyPolicyScopeFsmTaskFlags_Type = CucsFsmFlags
_CucsPolicyPolicyScopeFsmTaskFlags_Object = MibTableColumn
cucsPolicyPolicyScopeFsmTaskFlags = _CucsPolicyPolicyScopeFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 24, 1, 5),
    _CucsPolicyPolicyScopeFsmTaskFlags_Type()
)
cucsPolicyPolicyScopeFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmTaskFlags.setStatus("current")
_CucsPolicyPolicyScopeFsmTaskItem_Type = CucsPolicyPolicyScopeFsmTaskItem
_CucsPolicyPolicyScopeFsmTaskItem_Object = MibTableColumn
cucsPolicyPolicyScopeFsmTaskItem = _CucsPolicyPolicyScopeFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 24, 1, 6),
    _CucsPolicyPolicyScopeFsmTaskItem_Type()
)
cucsPolicyPolicyScopeFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmTaskItem.setStatus("current")
_CucsPolicyPolicyScopeFsmTaskSeqId_Type = Gauge32
_CucsPolicyPolicyScopeFsmTaskSeqId_Object = MibTableColumn
cucsPolicyPolicyScopeFsmTaskSeqId = _CucsPolicyPolicyScopeFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 24, 1, 7),
    _CucsPolicyPolicyScopeFsmTaskSeqId_Type()
)
cucsPolicyPolicyScopeFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPolicyScopeFsmTaskSeqId.setStatus("current")
_CucsPolicyPowerMgmtTable_Object = MibTable
cucsPolicyPowerMgmtTable = _CucsPolicyPowerMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 25)
)
if mibBuilder.loadTexts:
    cucsPolicyPowerMgmtTable.setStatus("current")
_CucsPolicyPowerMgmtEntry_Object = MibTableRow
cucsPolicyPowerMgmtEntry = _CucsPolicyPowerMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 25, 1)
)
cucsPolicyPowerMgmtEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyPowerMgmtInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyPowerMgmtEntry.setStatus("current")
_CucsPolicyPowerMgmtInstanceId_Type = CucsManagedObjectId
_CucsPolicyPowerMgmtInstanceId_Object = MibTableColumn
cucsPolicyPowerMgmtInstanceId = _CucsPolicyPowerMgmtInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 25, 1, 1),
    _CucsPolicyPowerMgmtInstanceId_Type()
)
cucsPolicyPowerMgmtInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyPowerMgmtInstanceId.setStatus("current")
_CucsPolicyPowerMgmtDn_Type = CucsManagedObjectDn
_CucsPolicyPowerMgmtDn_Object = MibTableColumn
cucsPolicyPowerMgmtDn = _CucsPolicyPowerMgmtDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 25, 1, 2),
    _CucsPolicyPowerMgmtDn_Type()
)
cucsPolicyPowerMgmtDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPowerMgmtDn.setStatus("current")
_CucsPolicyPowerMgmtRn_Type = SnmpAdminString
_CucsPolicyPowerMgmtRn_Object = MibTableColumn
cucsPolicyPowerMgmtRn = _CucsPolicyPowerMgmtRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 25, 1, 3),
    _CucsPolicyPowerMgmtRn_Type()
)
cucsPolicyPowerMgmtRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPowerMgmtRn.setStatus("current")
_CucsPolicyPowerMgmtSource_Type = CucsPolicyControlSource
_CucsPolicyPowerMgmtSource_Object = MibTableColumn
cucsPolicyPowerMgmtSource = _CucsPolicyPowerMgmtSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 25, 1, 4),
    _CucsPolicyPowerMgmtSource_Type()
)
cucsPolicyPowerMgmtSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPowerMgmtSource.setStatus("current")
_CucsPolicyPsuTable_Object = MibTable
cucsPolicyPsuTable = _CucsPolicyPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 26)
)
if mibBuilder.loadTexts:
    cucsPolicyPsuTable.setStatus("current")
_CucsPolicyPsuEntry_Object = MibTableRow
cucsPolicyPsuEntry = _CucsPolicyPsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 26, 1)
)
cucsPolicyPsuEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyPsuInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyPsuEntry.setStatus("current")
_CucsPolicyPsuInstanceId_Type = CucsManagedObjectId
_CucsPolicyPsuInstanceId_Object = MibTableColumn
cucsPolicyPsuInstanceId = _CucsPolicyPsuInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 26, 1, 1),
    _CucsPolicyPsuInstanceId_Type()
)
cucsPolicyPsuInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyPsuInstanceId.setStatus("current")
_CucsPolicyPsuDn_Type = CucsManagedObjectDn
_CucsPolicyPsuDn_Object = MibTableColumn
cucsPolicyPsuDn = _CucsPolicyPsuDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 26, 1, 2),
    _CucsPolicyPsuDn_Type()
)
cucsPolicyPsuDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPsuDn.setStatus("current")
_CucsPolicyPsuRn_Type = SnmpAdminString
_CucsPolicyPsuRn_Object = MibTableColumn
cucsPolicyPsuRn = _CucsPolicyPsuRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 26, 1, 3),
    _CucsPolicyPsuRn_Type()
)
cucsPolicyPsuRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPsuRn.setStatus("current")
_CucsPolicyPsuSource_Type = CucsPolicyControlSource
_CucsPolicyPsuSource_Object = MibTableColumn
cucsPolicyPsuSource = _CucsPolicyPsuSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 26, 1, 4),
    _CucsPolicyPsuSource_Type()
)
cucsPolicyPsuSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPsuSource.setStatus("current")
_CucsPolicySecurityTable_Object = MibTable
cucsPolicySecurityTable = _CucsPolicySecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 27)
)
if mibBuilder.loadTexts:
    cucsPolicySecurityTable.setStatus("current")
_CucsPolicySecurityEntry_Object = MibTableRow
cucsPolicySecurityEntry = _CucsPolicySecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 27, 1)
)
cucsPolicySecurityEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicySecurityInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicySecurityEntry.setStatus("current")
_CucsPolicySecurityInstanceId_Type = CucsManagedObjectId
_CucsPolicySecurityInstanceId_Object = MibTableColumn
cucsPolicySecurityInstanceId = _CucsPolicySecurityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 27, 1, 1),
    _CucsPolicySecurityInstanceId_Type()
)
cucsPolicySecurityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicySecurityInstanceId.setStatus("current")
_CucsPolicySecurityDn_Type = CucsManagedObjectDn
_CucsPolicySecurityDn_Object = MibTableColumn
cucsPolicySecurityDn = _CucsPolicySecurityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 27, 1, 2),
    _CucsPolicySecurityDn_Type()
)
cucsPolicySecurityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicySecurityDn.setStatus("current")
_CucsPolicySecurityRn_Type = SnmpAdminString
_CucsPolicySecurityRn_Object = MibTableColumn
cucsPolicySecurityRn = _CucsPolicySecurityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 27, 1, 3),
    _CucsPolicySecurityRn_Type()
)
cucsPolicySecurityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicySecurityRn.setStatus("current")
_CucsPolicySecuritySource_Type = CucsPolicyControlSource
_CucsPolicySecuritySource_Object = MibTableColumn
cucsPolicySecuritySource = _CucsPolicySecuritySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 27, 1, 4),
    _CucsPolicySecuritySource_Type()
)
cucsPolicySecuritySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicySecuritySource.setStatus("current")
_CucsPolicyCentraleSyncTable_Object = MibTable
cucsPolicyCentraleSyncTable = _CucsPolicyCentraleSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 28)
)
if mibBuilder.loadTexts:
    cucsPolicyCentraleSyncTable.setStatus("current")
_CucsPolicyCentraleSyncEntry_Object = MibTableRow
cucsPolicyCentraleSyncEntry = _CucsPolicyCentraleSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 28, 1)
)
cucsPolicyCentraleSyncEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyCentraleSyncInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyCentraleSyncEntry.setStatus("current")
_CucsPolicyCentraleSyncInstanceId_Type = CucsManagedObjectId
_CucsPolicyCentraleSyncInstanceId_Object = MibTableColumn
cucsPolicyCentraleSyncInstanceId = _CucsPolicyCentraleSyncInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 28, 1, 1),
    _CucsPolicyCentraleSyncInstanceId_Type()
)
cucsPolicyCentraleSyncInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyCentraleSyncInstanceId.setStatus("current")
_CucsPolicyCentraleSyncDn_Type = CucsManagedObjectDn
_CucsPolicyCentraleSyncDn_Object = MibTableColumn
cucsPolicyCentraleSyncDn = _CucsPolicyCentraleSyncDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 28, 1, 2),
    _CucsPolicyCentraleSyncDn_Type()
)
cucsPolicyCentraleSyncDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyCentraleSyncDn.setStatus("current")
_CucsPolicyCentraleSyncRn_Type = SnmpAdminString
_CucsPolicyCentraleSyncRn_Object = MibTableColumn
cucsPolicyCentraleSyncRn = _CucsPolicyCentraleSyncRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 28, 1, 3),
    _CucsPolicyCentraleSyncRn_Type()
)
cucsPolicyCentraleSyncRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyCentraleSyncRn.setStatus("current")
_CucsPolicyCentraleSyncLeftData_Type = SnmpAdminString
_CucsPolicyCentraleSyncLeftData_Object = MibTableColumn
cucsPolicyCentraleSyncLeftData = _CucsPolicyCentraleSyncLeftData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 28, 1, 4),
    _CucsPolicyCentraleSyncLeftData_Type()
)
cucsPolicyCentraleSyncLeftData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyCentraleSyncLeftData.setStatus("current")
_CucsPolicyCentraleSyncRightData_Type = SnmpAdminString
_CucsPolicyCentraleSyncRightData_Object = MibTableColumn
cucsPolicyCentraleSyncRightData = _CucsPolicyCentraleSyncRightData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 28, 1, 5),
    _CucsPolicyCentraleSyncRightData_Type()
)
cucsPolicyCentraleSyncRightData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyCentraleSyncRightData.setStatus("current")
_CucsPolicyElementTable_Object = MibTable
cucsPolicyElementTable = _CucsPolicyElementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 29)
)
if mibBuilder.loadTexts:
    cucsPolicyElementTable.setStatus("current")
_CucsPolicyElementEntry_Object = MibTableRow
cucsPolicyElementEntry = _CucsPolicyElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 29, 1)
)
cucsPolicyElementEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyElementInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyElementEntry.setStatus("current")
_CucsPolicyElementInstanceId_Type = CucsManagedObjectId
_CucsPolicyElementInstanceId_Object = MibTableColumn
cucsPolicyElementInstanceId = _CucsPolicyElementInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 29, 1, 1),
    _CucsPolicyElementInstanceId_Type()
)
cucsPolicyElementInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyElementInstanceId.setStatus("current")
_CucsPolicyElementDn_Type = CucsManagedObjectDn
_CucsPolicyElementDn_Object = MibTableColumn
cucsPolicyElementDn = _CucsPolicyElementDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 29, 1, 2),
    _CucsPolicyElementDn_Type()
)
cucsPolicyElementDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyElementDn.setStatus("current")
_CucsPolicyElementRn_Type = SnmpAdminString
_CucsPolicyElementRn_Object = MibTableColumn
cucsPolicyElementRn = _CucsPolicyElementRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 29, 1, 3),
    _CucsPolicyElementRn_Type()
)
cucsPolicyElementRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyElementRn.setStatus("current")
_CucsPolicyElementClassType_Type = SnmpAdminString
_CucsPolicyElementClassType_Object = MibTableColumn
cucsPolicyElementClassType = _CucsPolicyElementClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 29, 1, 4),
    _CucsPolicyElementClassType_Type()
)
cucsPolicyElementClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyElementClassType.setStatus("current")
_CucsPolicyElementConvertedDn_Type = SnmpAdminString
_CucsPolicyElementConvertedDn_Object = MibTableColumn
cucsPolicyElementConvertedDn = _CucsPolicyElementConvertedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 29, 1, 5),
    _CucsPolicyElementConvertedDn_Type()
)
cucsPolicyElementConvertedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyElementConvertedDn.setStatus("current")
_CucsPolicyElementOwnership_Type = CucsPolicyPolicyOwner
_CucsPolicyElementOwnership_Object = MibTableColumn
cucsPolicyElementOwnership = _CucsPolicyElementOwnership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 29, 1, 6),
    _CucsPolicyElementOwnership_Type()
)
cucsPolicyElementOwnership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyElementOwnership.setStatus("current")
_CucsPolicyElementPolicyDn_Type = SnmpAdminString
_CucsPolicyElementPolicyDn_Object = MibTableColumn
cucsPolicyElementPolicyDn = _CucsPolicyElementPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 29, 1, 7),
    _CucsPolicyElementPolicyDn_Type()
)
cucsPolicyElementPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyElementPolicyDn.setStatus("current")
_CucsPolicyLocalMapTable_Object = MibTable
cucsPolicyLocalMapTable = _CucsPolicyLocalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 30)
)
if mibBuilder.loadTexts:
    cucsPolicyLocalMapTable.setStatus("current")
_CucsPolicyLocalMapEntry_Object = MibTableRow
cucsPolicyLocalMapEntry = _CucsPolicyLocalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 30, 1)
)
cucsPolicyLocalMapEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyLocalMapInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyLocalMapEntry.setStatus("current")
_CucsPolicyLocalMapInstanceId_Type = CucsManagedObjectId
_CucsPolicyLocalMapInstanceId_Object = MibTableColumn
cucsPolicyLocalMapInstanceId = _CucsPolicyLocalMapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 30, 1, 1),
    _CucsPolicyLocalMapInstanceId_Type()
)
cucsPolicyLocalMapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyLocalMapInstanceId.setStatus("current")
_CucsPolicyLocalMapDn_Type = CucsManagedObjectDn
_CucsPolicyLocalMapDn_Object = MibTableColumn
cucsPolicyLocalMapDn = _CucsPolicyLocalMapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 30, 1, 2),
    _CucsPolicyLocalMapDn_Type()
)
cucsPolicyLocalMapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyLocalMapDn.setStatus("current")
_CucsPolicyLocalMapRn_Type = SnmpAdminString
_CucsPolicyLocalMapRn_Object = MibTableColumn
cucsPolicyLocalMapRn = _CucsPolicyLocalMapRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 30, 1, 3),
    _CucsPolicyLocalMapRn_Type()
)
cucsPolicyLocalMapRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyLocalMapRn.setStatus("current")
_CucsPolicyControlledTypeFsmTable_Object = MibTable
cucsPolicyControlledTypeFsmTable = _CucsPolicyControlledTypeFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31)
)
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmTable.setStatus("current")
_CucsPolicyControlledTypeFsmEntry_Object = MibTableRow
cucsPolicyControlledTypeFsmEntry = _CucsPolicyControlledTypeFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31, 1)
)
cucsPolicyControlledTypeFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyControlledTypeFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmEntry.setStatus("current")
_CucsPolicyControlledTypeFsmInstanceId_Type = CucsManagedObjectId
_CucsPolicyControlledTypeFsmInstanceId_Object = MibTableColumn
cucsPolicyControlledTypeFsmInstanceId = _CucsPolicyControlledTypeFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31, 1, 1),
    _CucsPolicyControlledTypeFsmInstanceId_Type()
)
cucsPolicyControlledTypeFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmInstanceId.setStatus("current")
_CucsPolicyControlledTypeFsmDn_Type = CucsManagedObjectDn
_CucsPolicyControlledTypeFsmDn_Object = MibTableColumn
cucsPolicyControlledTypeFsmDn = _CucsPolicyControlledTypeFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31, 1, 2),
    _CucsPolicyControlledTypeFsmDn_Type()
)
cucsPolicyControlledTypeFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmDn.setStatus("current")
_CucsPolicyControlledTypeFsmRn_Type = SnmpAdminString
_CucsPolicyControlledTypeFsmRn_Object = MibTableColumn
cucsPolicyControlledTypeFsmRn = _CucsPolicyControlledTypeFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31, 1, 3),
    _CucsPolicyControlledTypeFsmRn_Type()
)
cucsPolicyControlledTypeFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmRn.setStatus("current")
_CucsPolicyControlledTypeFsmCompletionTime_Type = DateAndTime
_CucsPolicyControlledTypeFsmCompletionTime_Object = MibTableColumn
cucsPolicyControlledTypeFsmCompletionTime = _CucsPolicyControlledTypeFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31, 1, 4),
    _CucsPolicyControlledTypeFsmCompletionTime_Type()
)
cucsPolicyControlledTypeFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmCompletionTime.setStatus("current")
_CucsPolicyControlledTypeFsmCurrentFsm_Type = CucsPolicyControlledTypeFsmCurrentFsm
_CucsPolicyControlledTypeFsmCurrentFsm_Object = MibTableColumn
cucsPolicyControlledTypeFsmCurrentFsm = _CucsPolicyControlledTypeFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31, 1, 5),
    _CucsPolicyControlledTypeFsmCurrentFsm_Type()
)
cucsPolicyControlledTypeFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmCurrentFsm.setStatus("current")
_CucsPolicyControlledTypeFsmDescrData_Type = SnmpAdminString
_CucsPolicyControlledTypeFsmDescrData_Object = MibTableColumn
cucsPolicyControlledTypeFsmDescrData = _CucsPolicyControlledTypeFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31, 1, 6),
    _CucsPolicyControlledTypeFsmDescrData_Type()
)
cucsPolicyControlledTypeFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmDescrData.setStatus("current")
_CucsPolicyControlledTypeFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsPolicyControlledTypeFsmFsmStatus_Object = MibTableColumn
cucsPolicyControlledTypeFsmFsmStatus = _CucsPolicyControlledTypeFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31, 1, 7),
    _CucsPolicyControlledTypeFsmFsmStatus_Type()
)
cucsPolicyControlledTypeFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmFsmStatus.setStatus("current")
_CucsPolicyControlledTypeFsmProgress_Type = Gauge32
_CucsPolicyControlledTypeFsmProgress_Object = MibTableColumn
cucsPolicyControlledTypeFsmProgress = _CucsPolicyControlledTypeFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31, 1, 8),
    _CucsPolicyControlledTypeFsmProgress_Type()
)
cucsPolicyControlledTypeFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmProgress.setStatus("current")
_CucsPolicyControlledTypeFsmRmtErrCode_Type = Gauge32
_CucsPolicyControlledTypeFsmRmtErrCode_Object = MibTableColumn
cucsPolicyControlledTypeFsmRmtErrCode = _CucsPolicyControlledTypeFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31, 1, 9),
    _CucsPolicyControlledTypeFsmRmtErrCode_Type()
)
cucsPolicyControlledTypeFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmRmtErrCode.setStatus("current")
_CucsPolicyControlledTypeFsmRmtErrDescr_Type = SnmpAdminString
_CucsPolicyControlledTypeFsmRmtErrDescr_Object = MibTableColumn
cucsPolicyControlledTypeFsmRmtErrDescr = _CucsPolicyControlledTypeFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31, 1, 10),
    _CucsPolicyControlledTypeFsmRmtErrDescr_Type()
)
cucsPolicyControlledTypeFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmRmtErrDescr.setStatus("current")
_CucsPolicyControlledTypeFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsPolicyControlledTypeFsmRmtRslt_Object = MibTableColumn
cucsPolicyControlledTypeFsmRmtRslt = _CucsPolicyControlledTypeFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 31, 1, 11),
    _CucsPolicyControlledTypeFsmRmtRslt_Type()
)
cucsPolicyControlledTypeFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmRmtRslt.setStatus("current")
_CucsPolicyControlledTypeFsmStageTable_Object = MibTable
cucsPolicyControlledTypeFsmStageTable = _CucsPolicyControlledTypeFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 32)
)
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStageTable.setStatus("current")
_CucsPolicyControlledTypeFsmStageEntry_Object = MibTableRow
cucsPolicyControlledTypeFsmStageEntry = _CucsPolicyControlledTypeFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 32, 1)
)
cucsPolicyControlledTypeFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyControlledTypeFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStageEntry.setStatus("current")
_CucsPolicyControlledTypeFsmStageInstanceId_Type = CucsManagedObjectId
_CucsPolicyControlledTypeFsmStageInstanceId_Object = MibTableColumn
cucsPolicyControlledTypeFsmStageInstanceId = _CucsPolicyControlledTypeFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 32, 1, 1),
    _CucsPolicyControlledTypeFsmStageInstanceId_Type()
)
cucsPolicyControlledTypeFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStageInstanceId.setStatus("current")
_CucsPolicyControlledTypeFsmStageDn_Type = CucsManagedObjectDn
_CucsPolicyControlledTypeFsmStageDn_Object = MibTableColumn
cucsPolicyControlledTypeFsmStageDn = _CucsPolicyControlledTypeFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 32, 1, 2),
    _CucsPolicyControlledTypeFsmStageDn_Type()
)
cucsPolicyControlledTypeFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStageDn.setStatus("current")
_CucsPolicyControlledTypeFsmStageRn_Type = SnmpAdminString
_CucsPolicyControlledTypeFsmStageRn_Object = MibTableColumn
cucsPolicyControlledTypeFsmStageRn = _CucsPolicyControlledTypeFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 32, 1, 3),
    _CucsPolicyControlledTypeFsmStageRn_Type()
)
cucsPolicyControlledTypeFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStageRn.setStatus("current")
_CucsPolicyControlledTypeFsmStageDescrData_Type = SnmpAdminString
_CucsPolicyControlledTypeFsmStageDescrData_Object = MibTableColumn
cucsPolicyControlledTypeFsmStageDescrData = _CucsPolicyControlledTypeFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 32, 1, 4),
    _CucsPolicyControlledTypeFsmStageDescrData_Type()
)
cucsPolicyControlledTypeFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStageDescrData.setStatus("current")
_CucsPolicyControlledTypeFsmStageLastUpdateTime_Type = DateAndTime
_CucsPolicyControlledTypeFsmStageLastUpdateTime_Object = MibTableColumn
cucsPolicyControlledTypeFsmStageLastUpdateTime = _CucsPolicyControlledTypeFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 32, 1, 5),
    _CucsPolicyControlledTypeFsmStageLastUpdateTime_Type()
)
cucsPolicyControlledTypeFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStageLastUpdateTime.setStatus("current")
_CucsPolicyControlledTypeFsmStageName_Type = CucsPolicyControlledTypeFsmStageName
_CucsPolicyControlledTypeFsmStageName_Object = MibTableColumn
cucsPolicyControlledTypeFsmStageName = _CucsPolicyControlledTypeFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 32, 1, 6),
    _CucsPolicyControlledTypeFsmStageName_Type()
)
cucsPolicyControlledTypeFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStageName.setStatus("current")
_CucsPolicyControlledTypeFsmStageOrder_Type = Gauge32
_CucsPolicyControlledTypeFsmStageOrder_Object = MibTableColumn
cucsPolicyControlledTypeFsmStageOrder = _CucsPolicyControlledTypeFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 32, 1, 7),
    _CucsPolicyControlledTypeFsmStageOrder_Type()
)
cucsPolicyControlledTypeFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStageOrder.setStatus("current")
_CucsPolicyControlledTypeFsmStageRetry_Type = Gauge32
_CucsPolicyControlledTypeFsmStageRetry_Object = MibTableColumn
cucsPolicyControlledTypeFsmStageRetry = _CucsPolicyControlledTypeFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 32, 1, 8),
    _CucsPolicyControlledTypeFsmStageRetry_Type()
)
cucsPolicyControlledTypeFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStageRetry.setStatus("current")
_CucsPolicyControlledTypeFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsPolicyControlledTypeFsmStageStageStatus_Object = MibTableColumn
cucsPolicyControlledTypeFsmStageStageStatus = _CucsPolicyControlledTypeFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 32, 1, 9),
    _CucsPolicyControlledTypeFsmStageStageStatus_Type()
)
cucsPolicyControlledTypeFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmStageStageStatus.setStatus("current")
_CucsPolicyControlledTypeFsmTaskTable_Object = MibTable
cucsPolicyControlledTypeFsmTaskTable = _CucsPolicyControlledTypeFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 33)
)
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmTaskTable.setStatus("current")
_CucsPolicyControlledTypeFsmTaskEntry_Object = MibTableRow
cucsPolicyControlledTypeFsmTaskEntry = _CucsPolicyControlledTypeFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 33, 1)
)
cucsPolicyControlledTypeFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyControlledTypeFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmTaskEntry.setStatus("current")
_CucsPolicyControlledTypeFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsPolicyControlledTypeFsmTaskInstanceId_Object = MibTableColumn
cucsPolicyControlledTypeFsmTaskInstanceId = _CucsPolicyControlledTypeFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 33, 1, 1),
    _CucsPolicyControlledTypeFsmTaskInstanceId_Type()
)
cucsPolicyControlledTypeFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmTaskInstanceId.setStatus("current")
_CucsPolicyControlledTypeFsmTaskDn_Type = CucsManagedObjectDn
_CucsPolicyControlledTypeFsmTaskDn_Object = MibTableColumn
cucsPolicyControlledTypeFsmTaskDn = _CucsPolicyControlledTypeFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 33, 1, 2),
    _CucsPolicyControlledTypeFsmTaskDn_Type()
)
cucsPolicyControlledTypeFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmTaskDn.setStatus("current")
_CucsPolicyControlledTypeFsmTaskRn_Type = SnmpAdminString
_CucsPolicyControlledTypeFsmTaskRn_Object = MibTableColumn
cucsPolicyControlledTypeFsmTaskRn = _CucsPolicyControlledTypeFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 33, 1, 3),
    _CucsPolicyControlledTypeFsmTaskRn_Type()
)
cucsPolicyControlledTypeFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmTaskRn.setStatus("current")
_CucsPolicyControlledTypeFsmTaskCompletion_Type = CucsFsmCompletion
_CucsPolicyControlledTypeFsmTaskCompletion_Object = MibTableColumn
cucsPolicyControlledTypeFsmTaskCompletion = _CucsPolicyControlledTypeFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 33, 1, 4),
    _CucsPolicyControlledTypeFsmTaskCompletion_Type()
)
cucsPolicyControlledTypeFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmTaskCompletion.setStatus("current")
_CucsPolicyControlledTypeFsmTaskFlags_Type = CucsFsmFlags
_CucsPolicyControlledTypeFsmTaskFlags_Object = MibTableColumn
cucsPolicyControlledTypeFsmTaskFlags = _CucsPolicyControlledTypeFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 33, 1, 5),
    _CucsPolicyControlledTypeFsmTaskFlags_Type()
)
cucsPolicyControlledTypeFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmTaskFlags.setStatus("current")
_CucsPolicyControlledTypeFsmTaskItem_Type = CucsPolicyControlledTypeFsmTaskItem
_CucsPolicyControlledTypeFsmTaskItem_Object = MibTableColumn
cucsPolicyControlledTypeFsmTaskItem = _CucsPolicyControlledTypeFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 33, 1, 6),
    _CucsPolicyControlledTypeFsmTaskItem_Type()
)
cucsPolicyControlledTypeFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmTaskItem.setStatus("current")
_CucsPolicyControlledTypeFsmTaskSeqId_Type = Gauge32
_CucsPolicyControlledTypeFsmTaskSeqId_Object = MibTableColumn
cucsPolicyControlledTypeFsmTaskSeqId = _CucsPolicyControlledTypeFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 33, 1, 7),
    _CucsPolicyControlledTypeFsmTaskSeqId_Type()
)
cucsPolicyControlledTypeFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyControlledTypeFsmTaskSeqId.setStatus("current")
_CucsPolicyRefReqTable_Object = MibTable
cucsPolicyRefReqTable = _CucsPolicyRefReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 34)
)
if mibBuilder.loadTexts:
    cucsPolicyRefReqTable.setStatus("current")
_CucsPolicyRefReqEntry_Object = MibTableRow
cucsPolicyRefReqEntry = _CucsPolicyRefReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 34, 1)
)
cucsPolicyRefReqEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyRefReqInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyRefReqEntry.setStatus("current")
_CucsPolicyRefReqInstanceId_Type = CucsManagedObjectId
_CucsPolicyRefReqInstanceId_Object = MibTableColumn
cucsPolicyRefReqInstanceId = _CucsPolicyRefReqInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 34, 1, 1),
    _CucsPolicyRefReqInstanceId_Type()
)
cucsPolicyRefReqInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyRefReqInstanceId.setStatus("current")
_CucsPolicyRefReqDn_Type = CucsManagedObjectDn
_CucsPolicyRefReqDn_Object = MibTableColumn
cucsPolicyRefReqDn = _CucsPolicyRefReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 34, 1, 2),
    _CucsPolicyRefReqDn_Type()
)
cucsPolicyRefReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyRefReqDn.setStatus("current")
_CucsPolicyRefReqRn_Type = SnmpAdminString
_CucsPolicyRefReqRn_Object = MibTableColumn
cucsPolicyRefReqRn = _CucsPolicyRefReqRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 34, 1, 3),
    _CucsPolicyRefReqRn_Type()
)
cucsPolicyRefReqRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyRefReqRn.setStatus("current")
_CucsPolicyRefReqPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsPolicyRefReqPolicyOwner_Object = MibTableColumn
cucsPolicyRefReqPolicyOwner = _CucsPolicyRefReqPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 34, 1, 4),
    _CucsPolicyRefReqPolicyOwner_Type()
)
cucsPolicyRefReqPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyRefReqPolicyOwner.setStatus("current")
_CucsPolicyRefReqRefConvertedDn_Type = SnmpAdminString
_CucsPolicyRefReqRefConvertedDn_Object = MibTableColumn
cucsPolicyRefReqRefConvertedDn = _CucsPolicyRefReqRefConvertedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 34, 1, 5),
    _CucsPolicyRefReqRefConvertedDn_Type()
)
cucsPolicyRefReqRefConvertedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyRefReqRefConvertedDn.setStatus("current")
_CucsPolicyRefReqRefPolicyDn_Type = SnmpAdminString
_CucsPolicyRefReqRefPolicyDn_Object = MibTableColumn
cucsPolicyRefReqRefPolicyDn = _CucsPolicyRefReqRefPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 34, 1, 6),
    _CucsPolicyRefReqRefPolicyDn_Type()
)
cucsPolicyRefReqRefPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyRefReqRefPolicyDn.setStatus("current")
_CucsPolicyIdResolvePolicyTable_Object = MibTable
cucsPolicyIdResolvePolicyTable = _CucsPolicyIdResolvePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 35)
)
if mibBuilder.loadTexts:
    cucsPolicyIdResolvePolicyTable.setStatus("current")
_CucsPolicyIdResolvePolicyEntry_Object = MibTableRow
cucsPolicyIdResolvePolicyEntry = _CucsPolicyIdResolvePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 35, 1)
)
cucsPolicyIdResolvePolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyIdResolvePolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyIdResolvePolicyEntry.setStatus("current")
_CucsPolicyIdResolvePolicyInstanceId_Type = CucsManagedObjectId
_CucsPolicyIdResolvePolicyInstanceId_Object = MibTableColumn
cucsPolicyIdResolvePolicyInstanceId = _CucsPolicyIdResolvePolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 35, 1, 1),
    _CucsPolicyIdResolvePolicyInstanceId_Type()
)
cucsPolicyIdResolvePolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyIdResolvePolicyInstanceId.setStatus("current")
_CucsPolicyIdResolvePolicyDn_Type = CucsManagedObjectDn
_CucsPolicyIdResolvePolicyDn_Object = MibTableColumn
cucsPolicyIdResolvePolicyDn = _CucsPolicyIdResolvePolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 35, 1, 2),
    _CucsPolicyIdResolvePolicyDn_Type()
)
cucsPolicyIdResolvePolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyIdResolvePolicyDn.setStatus("current")
_CucsPolicyIdResolvePolicyRn_Type = SnmpAdminString
_CucsPolicyIdResolvePolicyRn_Object = MibTableColumn
cucsPolicyIdResolvePolicyRn = _CucsPolicyIdResolvePolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 35, 1, 3),
    _CucsPolicyIdResolvePolicyRn_Type()
)
cucsPolicyIdResolvePolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyIdResolvePolicyRn.setStatus("current")
_CucsPolicyIdResolvePolicyIdAssignmentMode_Type = CucsPolicyIdResolvePolicyType
_CucsPolicyIdResolvePolicyIdAssignmentMode_Object = MibTableColumn
cucsPolicyIdResolvePolicyIdAssignmentMode = _CucsPolicyIdResolvePolicyIdAssignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 35, 1, 4),
    _CucsPolicyIdResolvePolicyIdAssignmentMode_Type()
)
cucsPolicyIdResolvePolicyIdAssignmentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyIdResolvePolicyIdAssignmentMode.setStatus("current")
_CucsPolicyStorageAutoConfigTable_Object = MibTable
cucsPolicyStorageAutoConfigTable = _CucsPolicyStorageAutoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 36)
)
if mibBuilder.loadTexts:
    cucsPolicyStorageAutoConfigTable.setStatus("current")
_CucsPolicyStorageAutoConfigEntry_Object = MibTableRow
cucsPolicyStorageAutoConfigEntry = _CucsPolicyStorageAutoConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 36, 1)
)
cucsPolicyStorageAutoConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyStorageAutoConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyStorageAutoConfigEntry.setStatus("current")
_CucsPolicyStorageAutoConfigInstanceId_Type = CucsManagedObjectId
_CucsPolicyStorageAutoConfigInstanceId_Object = MibTableColumn
cucsPolicyStorageAutoConfigInstanceId = _CucsPolicyStorageAutoConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 36, 1, 1),
    _CucsPolicyStorageAutoConfigInstanceId_Type()
)
cucsPolicyStorageAutoConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyStorageAutoConfigInstanceId.setStatus("current")
_CucsPolicyStorageAutoConfigDn_Type = CucsManagedObjectDn
_CucsPolicyStorageAutoConfigDn_Object = MibTableColumn
cucsPolicyStorageAutoConfigDn = _CucsPolicyStorageAutoConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 36, 1, 2),
    _CucsPolicyStorageAutoConfigDn_Type()
)
cucsPolicyStorageAutoConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyStorageAutoConfigDn.setStatus("current")
_CucsPolicyStorageAutoConfigRn_Type = SnmpAdminString
_CucsPolicyStorageAutoConfigRn_Object = MibTableColumn
cucsPolicyStorageAutoConfigRn = _CucsPolicyStorageAutoConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 36, 1, 3),
    _CucsPolicyStorageAutoConfigRn_Type()
)
cucsPolicyStorageAutoConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyStorageAutoConfigRn.setStatus("current")
_CucsPolicyStorageAutoConfigSource_Type = CucsPolicyControlSource
_CucsPolicyStorageAutoConfigSource_Object = MibTableColumn
cucsPolicyStorageAutoConfigSource = _CucsPolicyStorageAutoConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 36, 1, 4),
    _CucsPolicyStorageAutoConfigSource_Type()
)
cucsPolicyStorageAutoConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyStorageAutoConfigSource.setStatus("current")
_CucsPolicySystemEpTable_Object = MibTable
cucsPolicySystemEpTable = _CucsPolicySystemEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 37)
)
if mibBuilder.loadTexts:
    cucsPolicySystemEpTable.setStatus("current")
_CucsPolicySystemEpEntry_Object = MibTableRow
cucsPolicySystemEpEntry = _CucsPolicySystemEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 37, 1)
)
cucsPolicySystemEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicySystemEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicySystemEpEntry.setStatus("current")
_CucsPolicySystemEpInstanceId_Type = CucsManagedObjectId
_CucsPolicySystemEpInstanceId_Object = MibTableColumn
cucsPolicySystemEpInstanceId = _CucsPolicySystemEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 37, 1, 1),
    _CucsPolicySystemEpInstanceId_Type()
)
cucsPolicySystemEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicySystemEpInstanceId.setStatus("current")
_CucsPolicySystemEpDn_Type = CucsManagedObjectDn
_CucsPolicySystemEpDn_Object = MibTableColumn
cucsPolicySystemEpDn = _CucsPolicySystemEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 37, 1, 2),
    _CucsPolicySystemEpDn_Type()
)
cucsPolicySystemEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicySystemEpDn.setStatus("current")
_CucsPolicySystemEpRn_Type = SnmpAdminString
_CucsPolicySystemEpRn_Object = MibTableColumn
cucsPolicySystemEpRn = _CucsPolicySystemEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 37, 1, 3),
    _CucsPolicySystemEpRn_Type()
)
cucsPolicySystemEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicySystemEpRn.setStatus("current")
_CucsPolicySystemEpPropAcl_Type = Unsigned64
_CucsPolicySystemEpPropAcl_Object = MibTableColumn
cucsPolicySystemEpPropAcl = _CucsPolicySystemEpPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 37, 1, 4),
    _CucsPolicySystemEpPropAcl_Type()
)
cucsPolicySystemEpPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicySystemEpPropAcl.setStatus("current")
_CucsPolicyEquipmentTable_Object = MibTable
cucsPolicyEquipmentTable = _CucsPolicyEquipmentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 41)
)
if mibBuilder.loadTexts:
    cucsPolicyEquipmentTable.setStatus("current")
_CucsPolicyEquipmentEntry_Object = MibTableRow
cucsPolicyEquipmentEntry = _CucsPolicyEquipmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 41, 1)
)
cucsPolicyEquipmentEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyEquipmentInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyEquipmentEntry.setStatus("current")
_CucsPolicyEquipmentInstanceId_Type = CucsManagedObjectId
_CucsPolicyEquipmentInstanceId_Object = MibTableColumn
cucsPolicyEquipmentInstanceId = _CucsPolicyEquipmentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 41, 1, 1),
    _CucsPolicyEquipmentInstanceId_Type()
)
cucsPolicyEquipmentInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyEquipmentInstanceId.setStatus("current")
_CucsPolicyEquipmentDn_Type = CucsManagedObjectDn
_CucsPolicyEquipmentDn_Object = MibTableColumn
cucsPolicyEquipmentDn = _CucsPolicyEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 41, 1, 2),
    _CucsPolicyEquipmentDn_Type()
)
cucsPolicyEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyEquipmentDn.setStatus("current")
_CucsPolicyEquipmentRn_Type = SnmpAdminString
_CucsPolicyEquipmentRn_Object = MibTableColumn
cucsPolicyEquipmentRn = _CucsPolicyEquipmentRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 41, 1, 3),
    _CucsPolicyEquipmentRn_Type()
)
cucsPolicyEquipmentRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyEquipmentRn.setStatus("current")
_CucsPolicyEquipmentSource_Type = CucsPolicyControlSource
_CucsPolicyEquipmentSource_Object = MibTableColumn
cucsPolicyEquipmentSource = _CucsPolicyEquipmentSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 41, 1, 4),
    _CucsPolicyEquipmentSource_Type()
)
cucsPolicyEquipmentSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyEquipmentSource.setStatus("current")
_CucsPolicyPortConfigTable_Object = MibTable
cucsPolicyPortConfigTable = _CucsPolicyPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 44)
)
if mibBuilder.loadTexts:
    cucsPolicyPortConfigTable.setStatus("current")
_CucsPolicyPortConfigEntry_Object = MibTableRow
cucsPolicyPortConfigEntry = _CucsPolicyPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 44, 1)
)
cucsPolicyPortConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-POLICY-MIB", "cucsPolicyPortConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPolicyPortConfigEntry.setStatus("current")
_CucsPolicyPortConfigInstanceId_Type = CucsManagedObjectId
_CucsPolicyPortConfigInstanceId_Object = MibTableColumn
cucsPolicyPortConfigInstanceId = _CucsPolicyPortConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 44, 1, 1),
    _CucsPolicyPortConfigInstanceId_Type()
)
cucsPolicyPortConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPolicyPortConfigInstanceId.setStatus("current")
_CucsPolicyPortConfigDn_Type = CucsManagedObjectDn
_CucsPolicyPortConfigDn_Object = MibTableColumn
cucsPolicyPortConfigDn = _CucsPolicyPortConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 44, 1, 2),
    _CucsPolicyPortConfigDn_Type()
)
cucsPolicyPortConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPortConfigDn.setStatus("current")
_CucsPolicyPortConfigRn_Type = SnmpAdminString
_CucsPolicyPortConfigRn_Object = MibTableColumn
cucsPolicyPortConfigRn = _CucsPolicyPortConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 44, 1, 3),
    _CucsPolicyPortConfigRn_Type()
)
cucsPolicyPortConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPortConfigRn.setStatus("current")
_CucsPolicyPortConfigSource_Type = CucsPolicyControlSource
_CucsPolicyPortConfigSource_Object = MibTableColumn
cucsPolicyPortConfigSource = _CucsPolicyPortConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 69, 44, 1, 4),
    _CucsPolicyPortConfigSource_Type()
)
cucsPolicyPortConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPolicyPortConfigSource.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-POLICY-MIB",
    **{"cucsPolicyObjects": cucsPolicyObjects,
       "cucsPolicyCommunicationTable": cucsPolicyCommunicationTable,
       "cucsPolicyCommunicationEntry": cucsPolicyCommunicationEntry,
       "cucsPolicyCommunicationInstanceId": cucsPolicyCommunicationInstanceId,
       "cucsPolicyCommunicationDn": cucsPolicyCommunicationDn,
       "cucsPolicyCommunicationRn": cucsPolicyCommunicationRn,
       "cucsPolicyCommunicationSource": cucsPolicyCommunicationSource,
       "cucsPolicyConfigBackupTable": cucsPolicyConfigBackupTable,
       "cucsPolicyConfigBackupEntry": cucsPolicyConfigBackupEntry,
       "cucsPolicyConfigBackupInstanceId": cucsPolicyConfigBackupInstanceId,
       "cucsPolicyConfigBackupDn": cucsPolicyConfigBackupDn,
       "cucsPolicyConfigBackupRn": cucsPolicyConfigBackupRn,
       "cucsPolicyConfigBackupSource": cucsPolicyConfigBackupSource,
       "cucsPolicyControlEpTable": cucsPolicyControlEpTable,
       "cucsPolicyControlEpEntry": cucsPolicyControlEpEntry,
       "cucsPolicyControlEpInstanceId": cucsPolicyControlEpInstanceId,
       "cucsPolicyControlEpDn": cucsPolicyControlEpDn,
       "cucsPolicyControlEpRn": cucsPolicyControlEpRn,
       "cucsPolicyControlEpAckState": cucsPolicyControlEpAckState,
       "cucsPolicyControlEpEncSecret": cucsPolicyControlEpEncSecret,
       "cucsPolicyControlEpFsmDescr": cucsPolicyControlEpFsmDescr,
       "cucsPolicyControlEpFsmPrev": cucsPolicyControlEpFsmPrev,
       "cucsPolicyControlEpFsmProgr": cucsPolicyControlEpFsmProgr,
       "cucsPolicyControlEpFsmRmtInvErrCode": cucsPolicyControlEpFsmRmtInvErrCode,
       "cucsPolicyControlEpFsmRmtInvErrDescr": cucsPolicyControlEpFsmRmtInvErrDescr,
       "cucsPolicyControlEpFsmRmtInvRslt": cucsPolicyControlEpFsmRmtInvRslt,
       "cucsPolicyControlEpFsmStageDescr": cucsPolicyControlEpFsmStageDescr,
       "cucsPolicyControlEpFsmStamp": cucsPolicyControlEpFsmStamp,
       "cucsPolicyControlEpFsmStatus": cucsPolicyControlEpFsmStatus,
       "cucsPolicyControlEpFsmTry": cucsPolicyControlEpFsmTry,
       "cucsPolicyControlEpName": cucsPolicyControlEpName,
       "cucsPolicyControlEpRegistrationState": cucsPolicyControlEpRegistrationState,
       "cucsPolicyControlEpRepairState": cucsPolicyControlEpRepairState,
       "cucsPolicyControlEpSecret": cucsPolicyControlEpSecret,
       "cucsPolicyControlEpState": cucsPolicyControlEpState,
       "cucsPolicyControlEpSuspendState": cucsPolicyControlEpSuspendState,
       "cucsPolicyControlEpSvcRegIP": cucsPolicyControlEpSvcRegIP,
       "cucsPolicyControlEpSvcRegName": cucsPolicyControlEpSvcRegName,
       "cucsPolicyControlEpType": cucsPolicyControlEpType,
       "cucsPolicyControlEpCleanupMode": cucsPolicyControlEpCleanupMode,
       "cucsPolicyControlEpFsmTable": cucsPolicyControlEpFsmTable,
       "cucsPolicyControlEpFsmEntry": cucsPolicyControlEpFsmEntry,
       "cucsPolicyControlEpFsmInstanceId": cucsPolicyControlEpFsmInstanceId,
       "cucsPolicyControlEpFsmDn": cucsPolicyControlEpFsmDn,
       "cucsPolicyControlEpFsmRn": cucsPolicyControlEpFsmRn,
       "cucsPolicyControlEpFsmCompletionTime": cucsPolicyControlEpFsmCompletionTime,
       "cucsPolicyControlEpFsmCurrentFsm": cucsPolicyControlEpFsmCurrentFsm,
       "cucsPolicyControlEpFsmDescrData": cucsPolicyControlEpFsmDescrData,
       "cucsPolicyControlEpFsmFsmStatus": cucsPolicyControlEpFsmFsmStatus,
       "cucsPolicyControlEpFsmProgress": cucsPolicyControlEpFsmProgress,
       "cucsPolicyControlEpFsmRmtErrCode": cucsPolicyControlEpFsmRmtErrCode,
       "cucsPolicyControlEpFsmRmtErrDescr": cucsPolicyControlEpFsmRmtErrDescr,
       "cucsPolicyControlEpFsmRmtRslt": cucsPolicyControlEpFsmRmtRslt,
       "cucsPolicyControlEpFsmStageTable": cucsPolicyControlEpFsmStageTable,
       "cucsPolicyControlEpFsmStageEntry": cucsPolicyControlEpFsmStageEntry,
       "cucsPolicyControlEpFsmStageInstanceId": cucsPolicyControlEpFsmStageInstanceId,
       "cucsPolicyControlEpFsmStageDn": cucsPolicyControlEpFsmStageDn,
       "cucsPolicyControlEpFsmStageRn": cucsPolicyControlEpFsmStageRn,
       "cucsPolicyControlEpFsmStageDescrData": cucsPolicyControlEpFsmStageDescrData,
       "cucsPolicyControlEpFsmStageLastUpdateTime": cucsPolicyControlEpFsmStageLastUpdateTime,
       "cucsPolicyControlEpFsmStageName": cucsPolicyControlEpFsmStageName,
       "cucsPolicyControlEpFsmStageOrder": cucsPolicyControlEpFsmStageOrder,
       "cucsPolicyControlEpFsmStageRetry": cucsPolicyControlEpFsmStageRetry,
       "cucsPolicyControlEpFsmStageStageStatus": cucsPolicyControlEpFsmStageStageStatus,
       "cucsPolicyControlEpFsmTaskTable": cucsPolicyControlEpFsmTaskTable,
       "cucsPolicyControlEpFsmTaskEntry": cucsPolicyControlEpFsmTaskEntry,
       "cucsPolicyControlEpFsmTaskInstanceId": cucsPolicyControlEpFsmTaskInstanceId,
       "cucsPolicyControlEpFsmTaskDn": cucsPolicyControlEpFsmTaskDn,
       "cucsPolicyControlEpFsmTaskRn": cucsPolicyControlEpFsmTaskRn,
       "cucsPolicyControlEpFsmTaskCompletion": cucsPolicyControlEpFsmTaskCompletion,
       "cucsPolicyControlEpFsmTaskFlags": cucsPolicyControlEpFsmTaskFlags,
       "cucsPolicyControlEpFsmTaskItem": cucsPolicyControlEpFsmTaskItem,
       "cucsPolicyControlEpFsmTaskSeqId": cucsPolicyControlEpFsmTaskSeqId,
       "cucsPolicyControlledInstanceTable": cucsPolicyControlledInstanceTable,
       "cucsPolicyControlledInstanceEntry": cucsPolicyControlledInstanceEntry,
       "cucsPolicyControlledInstanceInstanceId": cucsPolicyControlledInstanceInstanceId,
       "cucsPolicyControlledInstanceDn": cucsPolicyControlledInstanceDn,
       "cucsPolicyControlledInstanceRn": cucsPolicyControlledInstanceRn,
       "cucsPolicyControlledInstanceDefDn": cucsPolicyControlledInstanceDefDn,
       "cucsPolicyControlledInstanceExternalResolveName": cucsPolicyControlledInstanceExternalResolveName,
       "cucsPolicyControlledInstanceName": cucsPolicyControlledInstanceName,
       "cucsPolicyControlledInstanceResolveType": cucsPolicyControlledInstanceResolveType,
       "cucsPolicyControlledInstanceType": cucsPolicyControlledInstanceType,
       "cucsPolicyControlledTypeTable": cucsPolicyControlledTypeTable,
       "cucsPolicyControlledTypeEntry": cucsPolicyControlledTypeEntry,
       "cucsPolicyControlledTypeInstanceId": cucsPolicyControlledTypeInstanceId,
       "cucsPolicyControlledTypeDn": cucsPolicyControlledTypeDn,
       "cucsPolicyControlledTypeRn": cucsPolicyControlledTypeRn,
       "cucsPolicyControlledTypeParentContext": cucsPolicyControlledTypeParentContext,
       "cucsPolicyControlledTypeType": cucsPolicyControlledTypeType,
       "cucsPolicyControlledTypeFsmDescr": cucsPolicyControlledTypeFsmDescr,
       "cucsPolicyControlledTypeFsmPrev": cucsPolicyControlledTypeFsmPrev,
       "cucsPolicyControlledTypeFsmProgr": cucsPolicyControlledTypeFsmProgr,
       "cucsPolicyControlledTypeFsmRmtInvErrCode": cucsPolicyControlledTypeFsmRmtInvErrCode,
       "cucsPolicyControlledTypeFsmRmtInvErrDescr": cucsPolicyControlledTypeFsmRmtInvErrDescr,
       "cucsPolicyControlledTypeFsmRmtInvRslt": cucsPolicyControlledTypeFsmRmtInvRslt,
       "cucsPolicyControlledTypeFsmStageDescr": cucsPolicyControlledTypeFsmStageDescr,
       "cucsPolicyControlledTypeFsmStamp": cucsPolicyControlledTypeFsmStamp,
       "cucsPolicyControlledTypeFsmStatus": cucsPolicyControlledTypeFsmStatus,
       "cucsPolicyControlledTypeFsmTry": cucsPolicyControlledTypeFsmTry,
       "cucsPolicyDateTimeTable": cucsPolicyDateTimeTable,
       "cucsPolicyDateTimeEntry": cucsPolicyDateTimeEntry,
       "cucsPolicyDateTimeInstanceId": cucsPolicyDateTimeInstanceId,
       "cucsPolicyDateTimeDn": cucsPolicyDateTimeDn,
       "cucsPolicyDateTimeRn": cucsPolicyDateTimeRn,
       "cucsPolicyDateTimeSource": cucsPolicyDateTimeSource,
       "cucsPolicyDigestTable": cucsPolicyDigestTable,
       "cucsPolicyDigestEntry": cucsPolicyDigestEntry,
       "cucsPolicyDigestInstanceId": cucsPolicyDigestInstanceId,
       "cucsPolicyDigestDn": cucsPolicyDigestDn,
       "cucsPolicyDigestRn": cucsPolicyDigestRn,
       "cucsPolicyDigestContext": cucsPolicyDigestContext,
       "cucsPolicyDigestDescr": cucsPolicyDigestDescr,
       "cucsPolicyDigestLabel": cucsPolicyDigestLabel,
       "cucsPolicyDigestName": cucsPolicyDigestName,
       "cucsPolicyDigestResolveType": cucsPolicyDigestResolveType,
       "cucsPolicyDigestType": cucsPolicyDigestType,
       "cucsPolicyDigestUsage": cucsPolicyDigestUsage,
       "cucsPolicyDigestOnBehalfOfIdent": cucsPolicyDigestOnBehalfOfIdent,
       "cucsPolicyDigestOnBehalfOfType": cucsPolicyDigestOnBehalfOfType,
       "cucsPolicyDigestRequestorOwnership": cucsPolicyDigestRequestorOwnership,
       "cucsPolicyDiscoveryTable": cucsPolicyDiscoveryTable,
       "cucsPolicyDiscoveryEntry": cucsPolicyDiscoveryEntry,
       "cucsPolicyDiscoveryInstanceId": cucsPolicyDiscoveryInstanceId,
       "cucsPolicyDiscoveryDn": cucsPolicyDiscoveryDn,
       "cucsPolicyDiscoveryRn": cucsPolicyDiscoveryRn,
       "cucsPolicyDiscoverySource": cucsPolicyDiscoverySource,
       "cucsPolicyDnsTable": cucsPolicyDnsTable,
       "cucsPolicyDnsEntry": cucsPolicyDnsEntry,
       "cucsPolicyDnsInstanceId": cucsPolicyDnsInstanceId,
       "cucsPolicyDnsDn": cucsPolicyDnsDn,
       "cucsPolicyDnsRn": cucsPolicyDnsRn,
       "cucsPolicyDnsSource": cucsPolicyDnsSource,
       "cucsPolicyFaultTable": cucsPolicyFaultTable,
       "cucsPolicyFaultEntry": cucsPolicyFaultEntry,
       "cucsPolicyFaultInstanceId": cucsPolicyFaultInstanceId,
       "cucsPolicyFaultDn": cucsPolicyFaultDn,
       "cucsPolicyFaultRn": cucsPolicyFaultRn,
       "cucsPolicyFaultSource": cucsPolicyFaultSource,
       "cucsPolicyInfraFirmwareTable": cucsPolicyInfraFirmwareTable,
       "cucsPolicyInfraFirmwareEntry": cucsPolicyInfraFirmwareEntry,
       "cucsPolicyInfraFirmwareInstanceId": cucsPolicyInfraFirmwareInstanceId,
       "cucsPolicyInfraFirmwareDn": cucsPolicyInfraFirmwareDn,
       "cucsPolicyInfraFirmwareRn": cucsPolicyInfraFirmwareRn,
       "cucsPolicyInfraFirmwareSource": cucsPolicyInfraFirmwareSource,
       "cucsPolicyMEpTable": cucsPolicyMEpTable,
       "cucsPolicyMEpEntry": cucsPolicyMEpEntry,
       "cucsPolicyMEpInstanceId": cucsPolicyMEpInstanceId,
       "cucsPolicyMEpDn": cucsPolicyMEpDn,
       "cucsPolicyMEpRn": cucsPolicyMEpRn,
       "cucsPolicyMEpSource": cucsPolicyMEpSource,
       "cucsPolicyMonitoringTable": cucsPolicyMonitoringTable,
       "cucsPolicyMonitoringEntry": cucsPolicyMonitoringEntry,
       "cucsPolicyMonitoringInstanceId": cucsPolicyMonitoringInstanceId,
       "cucsPolicyMonitoringDn": cucsPolicyMonitoringDn,
       "cucsPolicyMonitoringRn": cucsPolicyMonitoringRn,
       "cucsPolicyMonitoringSource": cucsPolicyMonitoringSource,
       "cucsPolicyPolicyEpTable": cucsPolicyPolicyEpTable,
       "cucsPolicyPolicyEpEntry": cucsPolicyPolicyEpEntry,
       "cucsPolicyPolicyEpInstanceId": cucsPolicyPolicyEpInstanceId,
       "cucsPolicyPolicyEpDn": cucsPolicyPolicyEpDn,
       "cucsPolicyPolicyEpRn": cucsPolicyPolicyEpRn,
       "cucsPolicyPolicyRequestorTable": cucsPolicyPolicyRequestorTable,
       "cucsPolicyPolicyRequestorEntry": cucsPolicyPolicyRequestorEntry,
       "cucsPolicyPolicyRequestorInstanceId": cucsPolicyPolicyRequestorInstanceId,
       "cucsPolicyPolicyRequestorDn": cucsPolicyPolicyRequestorDn,
       "cucsPolicyPolicyRequestorRn": cucsPolicyPolicyRequestorRn,
       "cucsPolicyPolicyRequestorName": cucsPolicyPolicyRequestorName,
       "cucsPolicyPolicyRequestorOnBehalfOfIdent": cucsPolicyPolicyRequestorOnBehalfOfIdent,
       "cucsPolicyPolicyRequestorOnBehalfOfType": cucsPolicyPolicyRequestorOnBehalfOfType,
       "cucsPolicyPolicyRequestorResolvedClassType": cucsPolicyPolicyRequestorResolvedClassType,
       "cucsPolicyPolicyScopeTable": cucsPolicyPolicyScopeTable,
       "cucsPolicyPolicyScopeEntry": cucsPolicyPolicyScopeEntry,
       "cucsPolicyPolicyScopeInstanceId": cucsPolicyPolicyScopeInstanceId,
       "cucsPolicyPolicyScopeDn": cucsPolicyPolicyScopeDn,
       "cucsPolicyPolicyScopeRn": cucsPolicyPolicyScopeRn,
       "cucsPolicyPolicyScopeAppType": cucsPolicyPolicyScopeAppType,
       "cucsPolicyPolicyScopeDefaultPolicyName": cucsPolicyPolicyScopeDefaultPolicyName,
       "cucsPolicyPolicyScopeFsmDescr": cucsPolicyPolicyScopeFsmDescr,
       "cucsPolicyPolicyScopeFsmPrev": cucsPolicyPolicyScopeFsmPrev,
       "cucsPolicyPolicyScopeFsmProgr": cucsPolicyPolicyScopeFsmProgr,
       "cucsPolicyPolicyScopeFsmRmtInvErrCode": cucsPolicyPolicyScopeFsmRmtInvErrCode,
       "cucsPolicyPolicyScopeFsmRmtInvErrDescr": cucsPolicyPolicyScopeFsmRmtInvErrDescr,
       "cucsPolicyPolicyScopeFsmRmtInvRslt": cucsPolicyPolicyScopeFsmRmtInvRslt,
       "cucsPolicyPolicyScopeFsmStageDescr": cucsPolicyPolicyScopeFsmStageDescr,
       "cucsPolicyPolicyScopeFsmStamp": cucsPolicyPolicyScopeFsmStamp,
       "cucsPolicyPolicyScopeFsmStatus": cucsPolicyPolicyScopeFsmStatus,
       "cucsPolicyPolicyScopeFsmTry": cucsPolicyPolicyScopeFsmTry,
       "cucsPolicyPolicyScopeOperStatus": cucsPolicyPolicyScopeOperStatus,
       "cucsPolicyPolicyScopeOwner": cucsPolicyPolicyScopeOwner,
       "cucsPolicyPolicyScopePolicyName": cucsPolicyPolicyScopePolicyName,
       "cucsPolicyPolicyScopePolicyType": cucsPolicyPolicyScopePolicyType,
       "cucsPolicyPolicyScopeRecursive": cucsPolicyPolicyScopeRecursive,
       "cucsPolicyPolicyScopeResolveType": cucsPolicyPolicyScopeResolveType,
       "cucsPolicyPolicyScopeContTable": cucsPolicyPolicyScopeContTable,
       "cucsPolicyPolicyScopeContEntry": cucsPolicyPolicyScopeContEntry,
       "cucsPolicyPolicyScopeContInstanceId": cucsPolicyPolicyScopeContInstanceId,
       "cucsPolicyPolicyScopeContDn": cucsPolicyPolicyScopeContDn,
       "cucsPolicyPolicyScopeContRn": cucsPolicyPolicyScopeContRn,
       "cucsPolicyPolicyScopeContAppType": cucsPolicyPolicyScopeContAppType,
       "cucsPolicyPolicyScopeContGenNum": cucsPolicyPolicyScopeContGenNum,
       "cucsPolicyPolicyScopeContNeedRecovery": cucsPolicyPolicyScopeContNeedRecovery,
       "cucsPolicyPolicyScopeContextTable": cucsPolicyPolicyScopeContextTable,
       "cucsPolicyPolicyScopeContextEntry": cucsPolicyPolicyScopeContextEntry,
       "cucsPolicyPolicyScopeContextInstanceId": cucsPolicyPolicyScopeContextInstanceId,
       "cucsPolicyPolicyScopeContextDn": cucsPolicyPolicyScopeContextDn,
       "cucsPolicyPolicyScopeContextRn": cucsPolicyPolicyScopeContextRn,
       "cucsPolicyPolicyScopeContextContext": cucsPolicyPolicyScopeContextContext,
       "cucsPolicyPolicyScopeContextName": cucsPolicyPolicyScopeContextName,
       "cucsPolicyPolicyScopeFsmTable": cucsPolicyPolicyScopeFsmTable,
       "cucsPolicyPolicyScopeFsmEntry": cucsPolicyPolicyScopeFsmEntry,
       "cucsPolicyPolicyScopeFsmInstanceId": cucsPolicyPolicyScopeFsmInstanceId,
       "cucsPolicyPolicyScopeFsmDn": cucsPolicyPolicyScopeFsmDn,
       "cucsPolicyPolicyScopeFsmRn": cucsPolicyPolicyScopeFsmRn,
       "cucsPolicyPolicyScopeFsmCompletionTime": cucsPolicyPolicyScopeFsmCompletionTime,
       "cucsPolicyPolicyScopeFsmCurrentFsm": cucsPolicyPolicyScopeFsmCurrentFsm,
       "cucsPolicyPolicyScopeFsmDescrData": cucsPolicyPolicyScopeFsmDescrData,
       "cucsPolicyPolicyScopeFsmFsmStatus": cucsPolicyPolicyScopeFsmFsmStatus,
       "cucsPolicyPolicyScopeFsmProgress": cucsPolicyPolicyScopeFsmProgress,
       "cucsPolicyPolicyScopeFsmRmtErrCode": cucsPolicyPolicyScopeFsmRmtErrCode,
       "cucsPolicyPolicyScopeFsmRmtErrDescr": cucsPolicyPolicyScopeFsmRmtErrDescr,
       "cucsPolicyPolicyScopeFsmRmtRslt": cucsPolicyPolicyScopeFsmRmtRslt,
       "cucsPolicyPolicyScopeFsmStageTable": cucsPolicyPolicyScopeFsmStageTable,
       "cucsPolicyPolicyScopeFsmStageEntry": cucsPolicyPolicyScopeFsmStageEntry,
       "cucsPolicyPolicyScopeFsmStageInstanceId": cucsPolicyPolicyScopeFsmStageInstanceId,
       "cucsPolicyPolicyScopeFsmStageDn": cucsPolicyPolicyScopeFsmStageDn,
       "cucsPolicyPolicyScopeFsmStageRn": cucsPolicyPolicyScopeFsmStageRn,
       "cucsPolicyPolicyScopeFsmStageDescrData": cucsPolicyPolicyScopeFsmStageDescrData,
       "cucsPolicyPolicyScopeFsmStageLastUpdateTime": cucsPolicyPolicyScopeFsmStageLastUpdateTime,
       "cucsPolicyPolicyScopeFsmStageName": cucsPolicyPolicyScopeFsmStageName,
       "cucsPolicyPolicyScopeFsmStageOrder": cucsPolicyPolicyScopeFsmStageOrder,
       "cucsPolicyPolicyScopeFsmStageRetry": cucsPolicyPolicyScopeFsmStageRetry,
       "cucsPolicyPolicyScopeFsmStageStageStatus": cucsPolicyPolicyScopeFsmStageStageStatus,
       "cucsPolicyPolicyScopeFsmTaskTable": cucsPolicyPolicyScopeFsmTaskTable,
       "cucsPolicyPolicyScopeFsmTaskEntry": cucsPolicyPolicyScopeFsmTaskEntry,
       "cucsPolicyPolicyScopeFsmTaskInstanceId": cucsPolicyPolicyScopeFsmTaskInstanceId,
       "cucsPolicyPolicyScopeFsmTaskDn": cucsPolicyPolicyScopeFsmTaskDn,
       "cucsPolicyPolicyScopeFsmTaskRn": cucsPolicyPolicyScopeFsmTaskRn,
       "cucsPolicyPolicyScopeFsmTaskCompletion": cucsPolicyPolicyScopeFsmTaskCompletion,
       "cucsPolicyPolicyScopeFsmTaskFlags": cucsPolicyPolicyScopeFsmTaskFlags,
       "cucsPolicyPolicyScopeFsmTaskItem": cucsPolicyPolicyScopeFsmTaskItem,
       "cucsPolicyPolicyScopeFsmTaskSeqId": cucsPolicyPolicyScopeFsmTaskSeqId,
       "cucsPolicyPowerMgmtTable": cucsPolicyPowerMgmtTable,
       "cucsPolicyPowerMgmtEntry": cucsPolicyPowerMgmtEntry,
       "cucsPolicyPowerMgmtInstanceId": cucsPolicyPowerMgmtInstanceId,
       "cucsPolicyPowerMgmtDn": cucsPolicyPowerMgmtDn,
       "cucsPolicyPowerMgmtRn": cucsPolicyPowerMgmtRn,
       "cucsPolicyPowerMgmtSource": cucsPolicyPowerMgmtSource,
       "cucsPolicyPsuTable": cucsPolicyPsuTable,
       "cucsPolicyPsuEntry": cucsPolicyPsuEntry,
       "cucsPolicyPsuInstanceId": cucsPolicyPsuInstanceId,
       "cucsPolicyPsuDn": cucsPolicyPsuDn,
       "cucsPolicyPsuRn": cucsPolicyPsuRn,
       "cucsPolicyPsuSource": cucsPolicyPsuSource,
       "cucsPolicySecurityTable": cucsPolicySecurityTable,
       "cucsPolicySecurityEntry": cucsPolicySecurityEntry,
       "cucsPolicySecurityInstanceId": cucsPolicySecurityInstanceId,
       "cucsPolicySecurityDn": cucsPolicySecurityDn,
       "cucsPolicySecurityRn": cucsPolicySecurityRn,
       "cucsPolicySecuritySource": cucsPolicySecuritySource,
       "cucsPolicyCentraleSyncTable": cucsPolicyCentraleSyncTable,
       "cucsPolicyCentraleSyncEntry": cucsPolicyCentraleSyncEntry,
       "cucsPolicyCentraleSyncInstanceId": cucsPolicyCentraleSyncInstanceId,
       "cucsPolicyCentraleSyncDn": cucsPolicyCentraleSyncDn,
       "cucsPolicyCentraleSyncRn": cucsPolicyCentraleSyncRn,
       "cucsPolicyCentraleSyncLeftData": cucsPolicyCentraleSyncLeftData,
       "cucsPolicyCentraleSyncRightData": cucsPolicyCentraleSyncRightData,
       "cucsPolicyElementTable": cucsPolicyElementTable,
       "cucsPolicyElementEntry": cucsPolicyElementEntry,
       "cucsPolicyElementInstanceId": cucsPolicyElementInstanceId,
       "cucsPolicyElementDn": cucsPolicyElementDn,
       "cucsPolicyElementRn": cucsPolicyElementRn,
       "cucsPolicyElementClassType": cucsPolicyElementClassType,
       "cucsPolicyElementConvertedDn": cucsPolicyElementConvertedDn,
       "cucsPolicyElementOwnership": cucsPolicyElementOwnership,
       "cucsPolicyElementPolicyDn": cucsPolicyElementPolicyDn,
       "cucsPolicyLocalMapTable": cucsPolicyLocalMapTable,
       "cucsPolicyLocalMapEntry": cucsPolicyLocalMapEntry,
       "cucsPolicyLocalMapInstanceId": cucsPolicyLocalMapInstanceId,
       "cucsPolicyLocalMapDn": cucsPolicyLocalMapDn,
       "cucsPolicyLocalMapRn": cucsPolicyLocalMapRn,
       "cucsPolicyControlledTypeFsmTable": cucsPolicyControlledTypeFsmTable,
       "cucsPolicyControlledTypeFsmEntry": cucsPolicyControlledTypeFsmEntry,
       "cucsPolicyControlledTypeFsmInstanceId": cucsPolicyControlledTypeFsmInstanceId,
       "cucsPolicyControlledTypeFsmDn": cucsPolicyControlledTypeFsmDn,
       "cucsPolicyControlledTypeFsmRn": cucsPolicyControlledTypeFsmRn,
       "cucsPolicyControlledTypeFsmCompletionTime": cucsPolicyControlledTypeFsmCompletionTime,
       "cucsPolicyControlledTypeFsmCurrentFsm": cucsPolicyControlledTypeFsmCurrentFsm,
       "cucsPolicyControlledTypeFsmDescrData": cucsPolicyControlledTypeFsmDescrData,
       "cucsPolicyControlledTypeFsmFsmStatus": cucsPolicyControlledTypeFsmFsmStatus,
       "cucsPolicyControlledTypeFsmProgress": cucsPolicyControlledTypeFsmProgress,
       "cucsPolicyControlledTypeFsmRmtErrCode": cucsPolicyControlledTypeFsmRmtErrCode,
       "cucsPolicyControlledTypeFsmRmtErrDescr": cucsPolicyControlledTypeFsmRmtErrDescr,
       "cucsPolicyControlledTypeFsmRmtRslt": cucsPolicyControlledTypeFsmRmtRslt,
       "cucsPolicyControlledTypeFsmStageTable": cucsPolicyControlledTypeFsmStageTable,
       "cucsPolicyControlledTypeFsmStageEntry": cucsPolicyControlledTypeFsmStageEntry,
       "cucsPolicyControlledTypeFsmStageInstanceId": cucsPolicyControlledTypeFsmStageInstanceId,
       "cucsPolicyControlledTypeFsmStageDn": cucsPolicyControlledTypeFsmStageDn,
       "cucsPolicyControlledTypeFsmStageRn": cucsPolicyControlledTypeFsmStageRn,
       "cucsPolicyControlledTypeFsmStageDescrData": cucsPolicyControlledTypeFsmStageDescrData,
       "cucsPolicyControlledTypeFsmStageLastUpdateTime": cucsPolicyControlledTypeFsmStageLastUpdateTime,
       "cucsPolicyControlledTypeFsmStageName": cucsPolicyControlledTypeFsmStageName,
       "cucsPolicyControlledTypeFsmStageOrder": cucsPolicyControlledTypeFsmStageOrder,
       "cucsPolicyControlledTypeFsmStageRetry": cucsPolicyControlledTypeFsmStageRetry,
       "cucsPolicyControlledTypeFsmStageStageStatus": cucsPolicyControlledTypeFsmStageStageStatus,
       "cucsPolicyControlledTypeFsmTaskTable": cucsPolicyControlledTypeFsmTaskTable,
       "cucsPolicyControlledTypeFsmTaskEntry": cucsPolicyControlledTypeFsmTaskEntry,
       "cucsPolicyControlledTypeFsmTaskInstanceId": cucsPolicyControlledTypeFsmTaskInstanceId,
       "cucsPolicyControlledTypeFsmTaskDn": cucsPolicyControlledTypeFsmTaskDn,
       "cucsPolicyControlledTypeFsmTaskRn": cucsPolicyControlledTypeFsmTaskRn,
       "cucsPolicyControlledTypeFsmTaskCompletion": cucsPolicyControlledTypeFsmTaskCompletion,
       "cucsPolicyControlledTypeFsmTaskFlags": cucsPolicyControlledTypeFsmTaskFlags,
       "cucsPolicyControlledTypeFsmTaskItem": cucsPolicyControlledTypeFsmTaskItem,
       "cucsPolicyControlledTypeFsmTaskSeqId": cucsPolicyControlledTypeFsmTaskSeqId,
       "cucsPolicyRefReqTable": cucsPolicyRefReqTable,
       "cucsPolicyRefReqEntry": cucsPolicyRefReqEntry,
       "cucsPolicyRefReqInstanceId": cucsPolicyRefReqInstanceId,
       "cucsPolicyRefReqDn": cucsPolicyRefReqDn,
       "cucsPolicyRefReqRn": cucsPolicyRefReqRn,
       "cucsPolicyRefReqPolicyOwner": cucsPolicyRefReqPolicyOwner,
       "cucsPolicyRefReqRefConvertedDn": cucsPolicyRefReqRefConvertedDn,
       "cucsPolicyRefReqRefPolicyDn": cucsPolicyRefReqRefPolicyDn,
       "cucsPolicyIdResolvePolicyTable": cucsPolicyIdResolvePolicyTable,
       "cucsPolicyIdResolvePolicyEntry": cucsPolicyIdResolvePolicyEntry,
       "cucsPolicyIdResolvePolicyInstanceId": cucsPolicyIdResolvePolicyInstanceId,
       "cucsPolicyIdResolvePolicyDn": cucsPolicyIdResolvePolicyDn,
       "cucsPolicyIdResolvePolicyRn": cucsPolicyIdResolvePolicyRn,
       "cucsPolicyIdResolvePolicyIdAssignmentMode": cucsPolicyIdResolvePolicyIdAssignmentMode,
       "cucsPolicyStorageAutoConfigTable": cucsPolicyStorageAutoConfigTable,
       "cucsPolicyStorageAutoConfigEntry": cucsPolicyStorageAutoConfigEntry,
       "cucsPolicyStorageAutoConfigInstanceId": cucsPolicyStorageAutoConfigInstanceId,
       "cucsPolicyStorageAutoConfigDn": cucsPolicyStorageAutoConfigDn,
       "cucsPolicyStorageAutoConfigRn": cucsPolicyStorageAutoConfigRn,
       "cucsPolicyStorageAutoConfigSource": cucsPolicyStorageAutoConfigSource,
       "cucsPolicySystemEpTable": cucsPolicySystemEpTable,
       "cucsPolicySystemEpEntry": cucsPolicySystemEpEntry,
       "cucsPolicySystemEpInstanceId": cucsPolicySystemEpInstanceId,
       "cucsPolicySystemEpDn": cucsPolicySystemEpDn,
       "cucsPolicySystemEpRn": cucsPolicySystemEpRn,
       "cucsPolicySystemEpPropAcl": cucsPolicySystemEpPropAcl,
       "cucsPolicyEquipmentTable": cucsPolicyEquipmentTable,
       "cucsPolicyEquipmentEntry": cucsPolicyEquipmentEntry,
       "cucsPolicyEquipmentInstanceId": cucsPolicyEquipmentInstanceId,
       "cucsPolicyEquipmentDn": cucsPolicyEquipmentDn,
       "cucsPolicyEquipmentRn": cucsPolicyEquipmentRn,
       "cucsPolicyEquipmentSource": cucsPolicyEquipmentSource,
       "cucsPolicyPortConfigTable": cucsPolicyPortConfigTable,
       "cucsPolicyPortConfigEntry": cucsPolicyPortConfigEntry,
       "cucsPolicyPortConfigInstanceId": cucsPolicyPortConfigInstanceId,
       "cucsPolicyPortConfigDn": cucsPolicyPortConfigDn,
       "cucsPolicyPortConfigRn": cucsPolicyPortConfigRn,
       "cucsPolicyPortConfigSource": cucsPolicyPortConfigSource}
)
