# SNMP MIB module (CISCO-UNIFIED-COMPUTING-CALLHOME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-CALLHOME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:05 2024
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

(CucsCallhomeAdminState,
 CucsCallhomeAlertGroup,
 CucsCallhomeAlertGroups,
 CucsCallhomeAlertLevel,
 CucsCallhomeAlertMessageSubtype,
 CucsCallhomeAlertMessageType,
 CucsCallhomeAlertThrottlingAdminState,
 CucsCallhomeAnonymousReportingAdminState,
 CucsCallhomeEpConfigState,
 CucsCallhomeEpFsmCurrentFsm,
 CucsCallhomeEpFsmStageName,
 CucsCallhomeEpFsmTaskItem,
 CucsCallhomeFormat,
 CucsCallhomeLevel,
 CucsCallhomePolicyAdminState,
 CucsCallhomeUrgency,
 CucsConditionCallHomeCause,
 CucsConditionRemoteInvRslt,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsCallhomeAdminState",
    "CucsCallhomeAlertGroup",
    "CucsCallhomeAlertGroups",
    "CucsCallhomeAlertLevel",
    "CucsCallhomeAlertMessageSubtype",
    "CucsCallhomeAlertMessageType",
    "CucsCallhomeAlertThrottlingAdminState",
    "CucsCallhomeAnonymousReportingAdminState",
    "CucsCallhomeEpConfigState",
    "CucsCallhomeEpFsmCurrentFsm",
    "CucsCallhomeEpFsmStageName",
    "CucsCallhomeEpFsmTaskItem",
    "CucsCallhomeFormat",
    "CucsCallhomeLevel",
    "CucsCallhomePolicyAdminState",
    "CucsCallhomeUrgency",
    "CucsConditionCallHomeCause",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsPolicyPolicyOwner")

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

cucsCallhomeObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsCallhomeDestTable_Object = MibTable
cucsCallhomeDestTable = _CucsCallhomeDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cucsCallhomeDestTable.setStatus("current")
_CucsCallhomeDestEntry_Object = MibTableRow
cucsCallhomeDestEntry = _CucsCallhomeDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 1, 1)
)
cucsCallhomeDestEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB", "cucsCallhomeDestInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCallhomeDestEntry.setStatus("current")
_CucsCallhomeDestInstanceId_Type = CucsManagedObjectId
_CucsCallhomeDestInstanceId_Object = MibTableColumn
cucsCallhomeDestInstanceId = _CucsCallhomeDestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 1, 1, 1),
    _CucsCallhomeDestInstanceId_Type()
)
cucsCallhomeDestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCallhomeDestInstanceId.setStatus("current")
_CucsCallhomeDestDn_Type = CucsManagedObjectDn
_CucsCallhomeDestDn_Object = MibTableColumn
cucsCallhomeDestDn = _CucsCallhomeDestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 1, 1, 2),
    _CucsCallhomeDestDn_Type()
)
cucsCallhomeDestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeDestDn.setStatus("current")
_CucsCallhomeDestRn_Type = SnmpAdminString
_CucsCallhomeDestRn_Object = MibTableColumn
cucsCallhomeDestRn = _CucsCallhomeDestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 1, 1, 3),
    _CucsCallhomeDestRn_Type()
)
cucsCallhomeDestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeDestRn.setStatus("current")
_CucsCallhomeDestEmail_Type = SnmpAdminString
_CucsCallhomeDestEmail_Object = MibTableColumn
cucsCallhomeDestEmail = _CucsCallhomeDestEmail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 1, 1, 4),
    _CucsCallhomeDestEmail_Type()
)
cucsCallhomeDestEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeDestEmail.setStatus("current")
_CucsCallhomeEpTable_Object = MibTable
cucsCallhomeEpTable = _CucsCallhomeEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cucsCallhomeEpTable.setStatus("current")
_CucsCallhomeEpEntry_Object = MibTableRow
cucsCallhomeEpEntry = _CucsCallhomeEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1)
)
cucsCallhomeEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB", "cucsCallhomeEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCallhomeEpEntry.setStatus("current")
_CucsCallhomeEpInstanceId_Type = CucsManagedObjectId
_CucsCallhomeEpInstanceId_Object = MibTableColumn
cucsCallhomeEpInstanceId = _CucsCallhomeEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 1),
    _CucsCallhomeEpInstanceId_Type()
)
cucsCallhomeEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCallhomeEpInstanceId.setStatus("current")
_CucsCallhomeEpDn_Type = CucsManagedObjectDn
_CucsCallhomeEpDn_Object = MibTableColumn
cucsCallhomeEpDn = _CucsCallhomeEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 2),
    _CucsCallhomeEpDn_Type()
)
cucsCallhomeEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpDn.setStatus("current")
_CucsCallhomeEpRn_Type = SnmpAdminString
_CucsCallhomeEpRn_Object = MibTableColumn
cucsCallhomeEpRn = _CucsCallhomeEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 3),
    _CucsCallhomeEpRn_Type()
)
cucsCallhomeEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpRn.setStatus("current")
_CucsCallhomeEpAdminState_Type = CucsCallhomeAdminState
_CucsCallhomeEpAdminState_Object = MibTableColumn
cucsCallhomeEpAdminState = _CucsCallhomeEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 4),
    _CucsCallhomeEpAdminState_Type()
)
cucsCallhomeEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpAdminState.setStatus("current")
_CucsCallhomeEpAlertThrottlingAdminState_Type = CucsCallhomeAlertThrottlingAdminState
_CucsCallhomeEpAlertThrottlingAdminState_Object = MibTableColumn
cucsCallhomeEpAlertThrottlingAdminState = _CucsCallhomeEpAlertThrottlingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 5),
    _CucsCallhomeEpAlertThrottlingAdminState_Type()
)
cucsCallhomeEpAlertThrottlingAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpAlertThrottlingAdminState.setStatus("current")
_CucsCallhomeEpFsmDescr_Type = SnmpAdminString
_CucsCallhomeEpFsmDescr_Object = MibTableColumn
cucsCallhomeEpFsmDescr = _CucsCallhomeEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 6),
    _CucsCallhomeEpFsmDescr_Type()
)
cucsCallhomeEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmDescr.setStatus("current")
_CucsCallhomeEpFsmPrev_Type = SnmpAdminString
_CucsCallhomeEpFsmPrev_Object = MibTableColumn
cucsCallhomeEpFsmPrev = _CucsCallhomeEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 7),
    _CucsCallhomeEpFsmPrev_Type()
)
cucsCallhomeEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmPrev.setStatus("current")
_CucsCallhomeEpFsmProgr_Type = Gauge32
_CucsCallhomeEpFsmProgr_Object = MibTableColumn
cucsCallhomeEpFsmProgr = _CucsCallhomeEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 8),
    _CucsCallhomeEpFsmProgr_Type()
)
cucsCallhomeEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmProgr.setStatus("current")
_CucsCallhomeEpFsmRmtInvErrCode_Type = Gauge32
_CucsCallhomeEpFsmRmtInvErrCode_Object = MibTableColumn
cucsCallhomeEpFsmRmtInvErrCode = _CucsCallhomeEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 9),
    _CucsCallhomeEpFsmRmtInvErrCode_Type()
)
cucsCallhomeEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmRmtInvErrCode.setStatus("current")
_CucsCallhomeEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsCallhomeEpFsmRmtInvErrDescr_Object = MibTableColumn
cucsCallhomeEpFsmRmtInvErrDescr = _CucsCallhomeEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 10),
    _CucsCallhomeEpFsmRmtInvErrDescr_Type()
)
cucsCallhomeEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmRmtInvErrDescr.setStatus("current")
_CucsCallhomeEpFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsCallhomeEpFsmRmtInvRslt_Object = MibTableColumn
cucsCallhomeEpFsmRmtInvRslt = _CucsCallhomeEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 11),
    _CucsCallhomeEpFsmRmtInvRslt_Type()
)
cucsCallhomeEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmRmtInvRslt.setStatus("current")
_CucsCallhomeEpFsmStageDescr_Type = SnmpAdminString
_CucsCallhomeEpFsmStageDescr_Object = MibTableColumn
cucsCallhomeEpFsmStageDescr = _CucsCallhomeEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 12),
    _CucsCallhomeEpFsmStageDescr_Type()
)
cucsCallhomeEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStageDescr.setStatus("current")
_CucsCallhomeEpFsmStamp_Type = DateAndTime
_CucsCallhomeEpFsmStamp_Object = MibTableColumn
cucsCallhomeEpFsmStamp = _CucsCallhomeEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 13),
    _CucsCallhomeEpFsmStamp_Type()
)
cucsCallhomeEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStamp.setStatus("current")
_CucsCallhomeEpFsmStatus_Type = SnmpAdminString
_CucsCallhomeEpFsmStatus_Object = MibTableColumn
cucsCallhomeEpFsmStatus = _CucsCallhomeEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 14),
    _CucsCallhomeEpFsmStatus_Type()
)
cucsCallhomeEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStatus.setStatus("current")
_CucsCallhomeEpFsmTry_Type = Gauge32
_CucsCallhomeEpFsmTry_Object = MibTableColumn
cucsCallhomeEpFsmTry = _CucsCallhomeEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 15),
    _CucsCallhomeEpFsmTry_Type()
)
cucsCallhomeEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmTry.setStatus("current")
_CucsCallhomeEpConfigState_Type = CucsCallhomeEpConfigState
_CucsCallhomeEpConfigState_Object = MibTableColumn
cucsCallhomeEpConfigState = _CucsCallhomeEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 16),
    _CucsCallhomeEpConfigState_Type()
)
cucsCallhomeEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpConfigState.setStatus("current")
_CucsCallhomeEpDescr_Type = SnmpAdminString
_CucsCallhomeEpDescr_Object = MibTableColumn
cucsCallhomeEpDescr = _CucsCallhomeEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 17),
    _CucsCallhomeEpDescr_Type()
)
cucsCallhomeEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpDescr.setStatus("current")
_CucsCallhomeEpIntId_Type = SnmpAdminString
_CucsCallhomeEpIntId_Object = MibTableColumn
cucsCallhomeEpIntId = _CucsCallhomeEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 18),
    _CucsCallhomeEpIntId_Type()
)
cucsCallhomeEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpIntId.setStatus("current")
_CucsCallhomeEpName_Type = SnmpAdminString
_CucsCallhomeEpName_Object = MibTableColumn
cucsCallhomeEpName = _CucsCallhomeEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 19),
    _CucsCallhomeEpName_Type()
)
cucsCallhomeEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpName.setStatus("current")
_CucsCallhomeEpPolicyLevel_Type = Gauge32
_CucsCallhomeEpPolicyLevel_Object = MibTableColumn
cucsCallhomeEpPolicyLevel = _CucsCallhomeEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 20),
    _CucsCallhomeEpPolicyLevel_Type()
)
cucsCallhomeEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpPolicyLevel.setStatus("current")
_CucsCallhomeEpPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCallhomeEpPolicyOwner_Object = MibTableColumn
cucsCallhomeEpPolicyOwner = _CucsCallhomeEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 2, 1, 21),
    _CucsCallhomeEpPolicyOwner_Type()
)
cucsCallhomeEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpPolicyOwner.setStatus("current")
_CucsCallhomeEpFsmTaskTable_Object = MibTable
cucsCallhomeEpFsmTaskTable = _CucsCallhomeEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmTaskTable.setStatus("current")
_CucsCallhomeEpFsmTaskEntry_Object = MibTableRow
cucsCallhomeEpFsmTaskEntry = _CucsCallhomeEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 3, 1)
)
cucsCallhomeEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB", "cucsCallhomeEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmTaskEntry.setStatus("current")
_CucsCallhomeEpFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsCallhomeEpFsmTaskInstanceId_Object = MibTableColumn
cucsCallhomeEpFsmTaskInstanceId = _CucsCallhomeEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 3, 1, 1),
    _CucsCallhomeEpFsmTaskInstanceId_Type()
)
cucsCallhomeEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmTaskInstanceId.setStatus("current")
_CucsCallhomeEpFsmTaskDn_Type = CucsManagedObjectDn
_CucsCallhomeEpFsmTaskDn_Object = MibTableColumn
cucsCallhomeEpFsmTaskDn = _CucsCallhomeEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 3, 1, 2),
    _CucsCallhomeEpFsmTaskDn_Type()
)
cucsCallhomeEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmTaskDn.setStatus("current")
_CucsCallhomeEpFsmTaskRn_Type = SnmpAdminString
_CucsCallhomeEpFsmTaskRn_Object = MibTableColumn
cucsCallhomeEpFsmTaskRn = _CucsCallhomeEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 3, 1, 3),
    _CucsCallhomeEpFsmTaskRn_Type()
)
cucsCallhomeEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmTaskRn.setStatus("current")
_CucsCallhomeEpFsmTaskCompletion_Type = CucsFsmCompletion
_CucsCallhomeEpFsmTaskCompletion_Object = MibTableColumn
cucsCallhomeEpFsmTaskCompletion = _CucsCallhomeEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 3, 1, 4),
    _CucsCallhomeEpFsmTaskCompletion_Type()
)
cucsCallhomeEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmTaskCompletion.setStatus("current")
_CucsCallhomeEpFsmTaskFlags_Type = CucsFsmFlags
_CucsCallhomeEpFsmTaskFlags_Object = MibTableColumn
cucsCallhomeEpFsmTaskFlags = _CucsCallhomeEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 3, 1, 5),
    _CucsCallhomeEpFsmTaskFlags_Type()
)
cucsCallhomeEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmTaskFlags.setStatus("current")
_CucsCallhomeEpFsmTaskItem_Type = CucsCallhomeEpFsmTaskItem
_CucsCallhomeEpFsmTaskItem_Object = MibTableColumn
cucsCallhomeEpFsmTaskItem = _CucsCallhomeEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 3, 1, 6),
    _CucsCallhomeEpFsmTaskItem_Type()
)
cucsCallhomeEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmTaskItem.setStatus("current")
_CucsCallhomeEpFsmTaskSeqId_Type = Gauge32
_CucsCallhomeEpFsmTaskSeqId_Object = MibTableColumn
cucsCallhomeEpFsmTaskSeqId = _CucsCallhomeEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 3, 1, 7),
    _CucsCallhomeEpFsmTaskSeqId_Type()
)
cucsCallhomeEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmTaskSeqId.setStatus("current")
_CucsCallhomePeriodicSystemInventoryTable_Object = MibTable
cucsCallhomePeriodicSystemInventoryTable = _CucsCallhomePeriodicSystemInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4)
)
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryTable.setStatus("current")
_CucsCallhomePeriodicSystemInventoryEntry_Object = MibTableRow
cucsCallhomePeriodicSystemInventoryEntry = _CucsCallhomePeriodicSystemInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1)
)
cucsCallhomePeriodicSystemInventoryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB", "cucsCallhomePeriodicSystemInventoryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryEntry.setStatus("current")
_CucsCallhomePeriodicSystemInventoryInstanceId_Type = CucsManagedObjectId
_CucsCallhomePeriodicSystemInventoryInstanceId_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryInstanceId = _CucsCallhomePeriodicSystemInventoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 1),
    _CucsCallhomePeriodicSystemInventoryInstanceId_Type()
)
cucsCallhomePeriodicSystemInventoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryInstanceId.setStatus("current")
_CucsCallhomePeriodicSystemInventoryDn_Type = CucsManagedObjectDn
_CucsCallhomePeriodicSystemInventoryDn_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryDn = _CucsCallhomePeriodicSystemInventoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 2),
    _CucsCallhomePeriodicSystemInventoryDn_Type()
)
cucsCallhomePeriodicSystemInventoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryDn.setStatus("current")
_CucsCallhomePeriodicSystemInventoryRn_Type = SnmpAdminString
_CucsCallhomePeriodicSystemInventoryRn_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryRn = _CucsCallhomePeriodicSystemInventoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 3),
    _CucsCallhomePeriodicSystemInventoryRn_Type()
)
cucsCallhomePeriodicSystemInventoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryRn.setStatus("current")
_CucsCallhomePeriodicSystemInventoryAdminState_Type = CucsCallhomeAdminState
_CucsCallhomePeriodicSystemInventoryAdminState_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryAdminState = _CucsCallhomePeriodicSystemInventoryAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 4),
    _CucsCallhomePeriodicSystemInventoryAdminState_Type()
)
cucsCallhomePeriodicSystemInventoryAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryAdminState.setStatus("current")
_CucsCallhomePeriodicSystemInventoryIntervalDays_Type = Gauge32
_CucsCallhomePeriodicSystemInventoryIntervalDays_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryIntervalDays = _CucsCallhomePeriodicSystemInventoryIntervalDays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 5),
    _CucsCallhomePeriodicSystemInventoryIntervalDays_Type()
)
cucsCallhomePeriodicSystemInventoryIntervalDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryIntervalDays.setStatus("current")
_CucsCallhomePeriodicSystemInventoryLastDeadline_Type = DateAndTime
_CucsCallhomePeriodicSystemInventoryLastDeadline_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryLastDeadline = _CucsCallhomePeriodicSystemInventoryLastDeadline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 6),
    _CucsCallhomePeriodicSystemInventoryLastDeadline_Type()
)
cucsCallhomePeriodicSystemInventoryLastDeadline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryLastDeadline.setStatus("current")
_CucsCallhomePeriodicSystemInventoryMaximumRetryCount_Type = Gauge32
_CucsCallhomePeriodicSystemInventoryMaximumRetryCount_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryMaximumRetryCount = _CucsCallhomePeriodicSystemInventoryMaximumRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 7),
    _CucsCallhomePeriodicSystemInventoryMaximumRetryCount_Type()
)
cucsCallhomePeriodicSystemInventoryMaximumRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryMaximumRetryCount.setStatus("current")
_CucsCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds_Type = Gauge32
_CucsCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds = _CucsCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 8),
    _CucsCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds_Type()
)
cucsCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds.setStatus("current")
_CucsCallhomePeriodicSystemInventoryNextDeadline_Type = DateAndTime
_CucsCallhomePeriodicSystemInventoryNextDeadline_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryNextDeadline = _CucsCallhomePeriodicSystemInventoryNextDeadline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 9),
    _CucsCallhomePeriodicSystemInventoryNextDeadline_Type()
)
cucsCallhomePeriodicSystemInventoryNextDeadline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryNextDeadline.setStatus("current")
_CucsCallhomePeriodicSystemInventoryPollIntervalSeconds_Type = Gauge32
_CucsCallhomePeriodicSystemInventoryPollIntervalSeconds_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryPollIntervalSeconds = _CucsCallhomePeriodicSystemInventoryPollIntervalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 10),
    _CucsCallhomePeriodicSystemInventoryPollIntervalSeconds_Type()
)
cucsCallhomePeriodicSystemInventoryPollIntervalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryPollIntervalSeconds.setStatus("current")
_CucsCallhomePeriodicSystemInventoryRetryCount_Type = Gauge32
_CucsCallhomePeriodicSystemInventoryRetryCount_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryRetryCount = _CucsCallhomePeriodicSystemInventoryRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 11),
    _CucsCallhomePeriodicSystemInventoryRetryCount_Type()
)
cucsCallhomePeriodicSystemInventoryRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryRetryCount.setStatus("current")
_CucsCallhomePeriodicSystemInventoryRetryDelayMinutes_Type = Gauge32
_CucsCallhomePeriodicSystemInventoryRetryDelayMinutes_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryRetryDelayMinutes = _CucsCallhomePeriodicSystemInventoryRetryDelayMinutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 12),
    _CucsCallhomePeriodicSystemInventoryRetryDelayMinutes_Type()
)
cucsCallhomePeriodicSystemInventoryRetryDelayMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryRetryDelayMinutes.setStatus("current")
_CucsCallhomePeriodicSystemInventorySendNow_Type = TruthValue
_CucsCallhomePeriodicSystemInventorySendNow_Object = MibTableColumn
cucsCallhomePeriodicSystemInventorySendNow = _CucsCallhomePeriodicSystemInventorySendNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 13),
    _CucsCallhomePeriodicSystemInventorySendNow_Type()
)
cucsCallhomePeriodicSystemInventorySendNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventorySendNow.setStatus("current")
_CucsCallhomePeriodicSystemInventoryTimeOfDayHour_Type = Gauge32
_CucsCallhomePeriodicSystemInventoryTimeOfDayHour_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryTimeOfDayHour = _CucsCallhomePeriodicSystemInventoryTimeOfDayHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 14),
    _CucsCallhomePeriodicSystemInventoryTimeOfDayHour_Type()
)
cucsCallhomePeriodicSystemInventoryTimeOfDayHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryTimeOfDayHour.setStatus("current")
_CucsCallhomePeriodicSystemInventoryTimeOfDayMinute_Type = Gauge32
_CucsCallhomePeriodicSystemInventoryTimeOfDayMinute_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryTimeOfDayMinute = _CucsCallhomePeriodicSystemInventoryTimeOfDayMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 15),
    _CucsCallhomePeriodicSystemInventoryTimeOfDayMinute_Type()
)
cucsCallhomePeriodicSystemInventoryTimeOfDayMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryTimeOfDayMinute.setStatus("current")
_CucsCallhomePeriodicSystemInventoryTimeOfLastAttempt_Type = DateAndTime
_CucsCallhomePeriodicSystemInventoryTimeOfLastAttempt_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryTimeOfLastAttempt = _CucsCallhomePeriodicSystemInventoryTimeOfLastAttempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 16),
    _CucsCallhomePeriodicSystemInventoryTimeOfLastAttempt_Type()
)
cucsCallhomePeriodicSystemInventoryTimeOfLastAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryTimeOfLastAttempt.setStatus("current")
_CucsCallhomePeriodicSystemInventoryTimeOfLastSuccess_Type = DateAndTime
_CucsCallhomePeriodicSystemInventoryTimeOfLastSuccess_Object = MibTableColumn
cucsCallhomePeriodicSystemInventoryTimeOfLastSuccess = _CucsCallhomePeriodicSystemInventoryTimeOfLastSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 4, 1, 17),
    _CucsCallhomePeriodicSystemInventoryTimeOfLastSuccess_Type()
)
cucsCallhomePeriodicSystemInventoryTimeOfLastSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePeriodicSystemInventoryTimeOfLastSuccess.setStatus("current")
_CucsCallhomePolicyTable_Object = MibTable
cucsCallhomePolicyTable = _CucsCallhomePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 5)
)
if mibBuilder.loadTexts:
    cucsCallhomePolicyTable.setStatus("current")
_CucsCallhomePolicyEntry_Object = MibTableRow
cucsCallhomePolicyEntry = _CucsCallhomePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 5, 1)
)
cucsCallhomePolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB", "cucsCallhomePolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCallhomePolicyEntry.setStatus("current")
_CucsCallhomePolicyInstanceId_Type = CucsManagedObjectId
_CucsCallhomePolicyInstanceId_Object = MibTableColumn
cucsCallhomePolicyInstanceId = _CucsCallhomePolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 5, 1, 1),
    _CucsCallhomePolicyInstanceId_Type()
)
cucsCallhomePolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCallhomePolicyInstanceId.setStatus("current")
_CucsCallhomePolicyDn_Type = CucsManagedObjectDn
_CucsCallhomePolicyDn_Object = MibTableColumn
cucsCallhomePolicyDn = _CucsCallhomePolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 5, 1, 2),
    _CucsCallhomePolicyDn_Type()
)
cucsCallhomePolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePolicyDn.setStatus("current")
_CucsCallhomePolicyRn_Type = SnmpAdminString
_CucsCallhomePolicyRn_Object = MibTableColumn
cucsCallhomePolicyRn = _CucsCallhomePolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 5, 1, 3),
    _CucsCallhomePolicyRn_Type()
)
cucsCallhomePolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePolicyRn.setStatus("current")
_CucsCallhomePolicyAdminState_Type = CucsCallhomePolicyAdminState
_CucsCallhomePolicyAdminState_Object = MibTableColumn
cucsCallhomePolicyAdminState = _CucsCallhomePolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 5, 1, 4),
    _CucsCallhomePolicyAdminState_Type()
)
cucsCallhomePolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePolicyAdminState.setStatus("current")
_CucsCallhomePolicyCause_Type = CucsConditionCallHomeCause
_CucsCallhomePolicyCause_Object = MibTableColumn
cucsCallhomePolicyCause = _CucsCallhomePolicyCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 5, 1, 5),
    _CucsCallhomePolicyCause_Type()
)
cucsCallhomePolicyCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePolicyCause.setStatus("current")
_CucsCallhomePolicyDescr_Type = SnmpAdminString
_CucsCallhomePolicyDescr_Object = MibTableColumn
cucsCallhomePolicyDescr = _CucsCallhomePolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 5, 1, 6),
    _CucsCallhomePolicyDescr_Type()
)
cucsCallhomePolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePolicyDescr.setStatus("current")
_CucsCallhomePolicyName_Type = SnmpAdminString
_CucsCallhomePolicyName_Object = MibTableColumn
cucsCallhomePolicyName = _CucsCallhomePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 5, 1, 8),
    _CucsCallhomePolicyName_Type()
)
cucsCallhomePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomePolicyName.setStatus("current")
_CucsCallhomeProfileTable_Object = MibTable
cucsCallhomeProfileTable = _CucsCallhomeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 6)
)
if mibBuilder.loadTexts:
    cucsCallhomeProfileTable.setStatus("current")
_CucsCallhomeProfileEntry_Object = MibTableRow
cucsCallhomeProfileEntry = _CucsCallhomeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 6, 1)
)
cucsCallhomeProfileEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB", "cucsCallhomeProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCallhomeProfileEntry.setStatus("current")
_CucsCallhomeProfileInstanceId_Type = CucsManagedObjectId
_CucsCallhomeProfileInstanceId_Object = MibTableColumn
cucsCallhomeProfileInstanceId = _CucsCallhomeProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 6, 1, 1),
    _CucsCallhomeProfileInstanceId_Type()
)
cucsCallhomeProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCallhomeProfileInstanceId.setStatus("current")
_CucsCallhomeProfileDn_Type = CucsManagedObjectDn
_CucsCallhomeProfileDn_Object = MibTableColumn
cucsCallhomeProfileDn = _CucsCallhomeProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 6, 1, 2),
    _CucsCallhomeProfileDn_Type()
)
cucsCallhomeProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeProfileDn.setStatus("current")
_CucsCallhomeProfileRn_Type = SnmpAdminString
_CucsCallhomeProfileRn_Object = MibTableColumn
cucsCallhomeProfileRn = _CucsCallhomeProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 6, 1, 3),
    _CucsCallhomeProfileRn_Type()
)
cucsCallhomeProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeProfileRn.setStatus("current")
_CucsCallhomeProfileAlertGroups_Type = CucsCallhomeAlertGroups
_CucsCallhomeProfileAlertGroups_Object = MibTableColumn
cucsCallhomeProfileAlertGroups = _CucsCallhomeProfileAlertGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 6, 1, 4),
    _CucsCallhomeProfileAlertGroups_Type()
)
cucsCallhomeProfileAlertGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeProfileAlertGroups.setStatus("current")
_CucsCallhomeProfileDescr_Type = SnmpAdminString
_CucsCallhomeProfileDescr_Object = MibTableColumn
cucsCallhomeProfileDescr = _CucsCallhomeProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 6, 1, 5),
    _CucsCallhomeProfileDescr_Type()
)
cucsCallhomeProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeProfileDescr.setStatus("current")
_CucsCallhomeProfileFormat_Type = CucsCallhomeFormat
_CucsCallhomeProfileFormat_Object = MibTableColumn
cucsCallhomeProfileFormat = _CucsCallhomeProfileFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 6, 1, 6),
    _CucsCallhomeProfileFormat_Type()
)
cucsCallhomeProfileFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeProfileFormat.setStatus("current")
_CucsCallhomeProfileLevel_Type = CucsCallhomeLevel
_CucsCallhomeProfileLevel_Object = MibTableColumn
cucsCallhomeProfileLevel = _CucsCallhomeProfileLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 6, 1, 8),
    _CucsCallhomeProfileLevel_Type()
)
cucsCallhomeProfileLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeProfileLevel.setStatus("current")
_CucsCallhomeProfileMaxSize_Type = Gauge32
_CucsCallhomeProfileMaxSize_Object = MibTableColumn
cucsCallhomeProfileMaxSize = _CucsCallhomeProfileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 6, 1, 9),
    _CucsCallhomeProfileMaxSize_Type()
)
cucsCallhomeProfileMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeProfileMaxSize.setStatus("current")
_CucsCallhomeProfileName_Type = SnmpAdminString
_CucsCallhomeProfileName_Object = MibTableColumn
cucsCallhomeProfileName = _CucsCallhomeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 6, 1, 10),
    _CucsCallhomeProfileName_Type()
)
cucsCallhomeProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeProfileName.setStatus("current")
_CucsCallhomeSmtpTable_Object = MibTable
cucsCallhomeSmtpTable = _CucsCallhomeSmtpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 7)
)
if mibBuilder.loadTexts:
    cucsCallhomeSmtpTable.setStatus("current")
_CucsCallhomeSmtpEntry_Object = MibTableRow
cucsCallhomeSmtpEntry = _CucsCallhomeSmtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 7, 1)
)
cucsCallhomeSmtpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB", "cucsCallhomeSmtpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCallhomeSmtpEntry.setStatus("current")
_CucsCallhomeSmtpInstanceId_Type = CucsManagedObjectId
_CucsCallhomeSmtpInstanceId_Object = MibTableColumn
cucsCallhomeSmtpInstanceId = _CucsCallhomeSmtpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 7, 1, 1),
    _CucsCallhomeSmtpInstanceId_Type()
)
cucsCallhomeSmtpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCallhomeSmtpInstanceId.setStatus("current")
_CucsCallhomeSmtpDn_Type = CucsManagedObjectDn
_CucsCallhomeSmtpDn_Object = MibTableColumn
cucsCallhomeSmtpDn = _CucsCallhomeSmtpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 7, 1, 2),
    _CucsCallhomeSmtpDn_Type()
)
cucsCallhomeSmtpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSmtpDn.setStatus("current")
_CucsCallhomeSmtpRn_Type = SnmpAdminString
_CucsCallhomeSmtpRn_Object = MibTableColumn
cucsCallhomeSmtpRn = _CucsCallhomeSmtpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 7, 1, 3),
    _CucsCallhomeSmtpRn_Type()
)
cucsCallhomeSmtpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSmtpRn.setStatus("current")
_CucsCallhomeSmtpHost_Type = SnmpAdminString
_CucsCallhomeSmtpHost_Object = MibTableColumn
cucsCallhomeSmtpHost = _CucsCallhomeSmtpHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 7, 1, 4),
    _CucsCallhomeSmtpHost_Type()
)
cucsCallhomeSmtpHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSmtpHost.setStatus("current")
_CucsCallhomeSmtpPort_Type = Gauge32
_CucsCallhomeSmtpPort_Object = MibTableColumn
cucsCallhomeSmtpPort = _CucsCallhomeSmtpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 7, 1, 5),
    _CucsCallhomeSmtpPort_Type()
)
cucsCallhomeSmtpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSmtpPort.setStatus("current")
_CucsCallhomeSourceTable_Object = MibTable
cucsCallhomeSourceTable = _CucsCallhomeSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8)
)
if mibBuilder.loadTexts:
    cucsCallhomeSourceTable.setStatus("current")
_CucsCallhomeSourceEntry_Object = MibTableRow
cucsCallhomeSourceEntry = _CucsCallhomeSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1)
)
cucsCallhomeSourceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB", "cucsCallhomeSourceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCallhomeSourceEntry.setStatus("current")
_CucsCallhomeSourceInstanceId_Type = CucsManagedObjectId
_CucsCallhomeSourceInstanceId_Object = MibTableColumn
cucsCallhomeSourceInstanceId = _CucsCallhomeSourceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 1),
    _CucsCallhomeSourceInstanceId_Type()
)
cucsCallhomeSourceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCallhomeSourceInstanceId.setStatus("current")
_CucsCallhomeSourceDn_Type = CucsManagedObjectDn
_CucsCallhomeSourceDn_Object = MibTableColumn
cucsCallhomeSourceDn = _CucsCallhomeSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 2),
    _CucsCallhomeSourceDn_Type()
)
cucsCallhomeSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSourceDn.setStatus("current")
_CucsCallhomeSourceRn_Type = SnmpAdminString
_CucsCallhomeSourceRn_Object = MibTableColumn
cucsCallhomeSourceRn = _CucsCallhomeSourceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 3),
    _CucsCallhomeSourceRn_Type()
)
cucsCallhomeSourceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSourceRn.setStatus("current")
_CucsCallhomeSourceAddr_Type = SnmpAdminString
_CucsCallhomeSourceAddr_Object = MibTableColumn
cucsCallhomeSourceAddr = _CucsCallhomeSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 4),
    _CucsCallhomeSourceAddr_Type()
)
cucsCallhomeSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSourceAddr.setStatus("current")
_CucsCallhomeSourceContact_Type = SnmpAdminString
_CucsCallhomeSourceContact_Object = MibTableColumn
cucsCallhomeSourceContact = _CucsCallhomeSourceContact_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 5),
    _CucsCallhomeSourceContact_Type()
)
cucsCallhomeSourceContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSourceContact.setStatus("current")
_CucsCallhomeSourceContract_Type = SnmpAdminString
_CucsCallhomeSourceContract_Object = MibTableColumn
cucsCallhomeSourceContract = _CucsCallhomeSourceContract_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 6),
    _CucsCallhomeSourceContract_Type()
)
cucsCallhomeSourceContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSourceContract.setStatus("current")
_CucsCallhomeSourceCustomer_Type = SnmpAdminString
_CucsCallhomeSourceCustomer_Object = MibTableColumn
cucsCallhomeSourceCustomer = _CucsCallhomeSourceCustomer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 7),
    _CucsCallhomeSourceCustomer_Type()
)
cucsCallhomeSourceCustomer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSourceCustomer.setStatus("current")
_CucsCallhomeSourceEmail_Type = SnmpAdminString
_CucsCallhomeSourceEmail_Object = MibTableColumn
cucsCallhomeSourceEmail = _CucsCallhomeSourceEmail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 8),
    _CucsCallhomeSourceEmail_Type()
)
cucsCallhomeSourceEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSourceEmail.setStatus("current")
_CucsCallhomeSourceFrom_Type = SnmpAdminString
_CucsCallhomeSourceFrom_Object = MibTableColumn
cucsCallhomeSourceFrom = _CucsCallhomeSourceFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 9),
    _CucsCallhomeSourceFrom_Type()
)
cucsCallhomeSourceFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSourceFrom.setStatus("current")
_CucsCallhomeSourcePhone_Type = SnmpAdminString
_CucsCallhomeSourcePhone_Object = MibTableColumn
cucsCallhomeSourcePhone = _CucsCallhomeSourcePhone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 10),
    _CucsCallhomeSourcePhone_Type()
)
cucsCallhomeSourcePhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSourcePhone.setStatus("current")
_CucsCallhomeSourceReplyTo_Type = SnmpAdminString
_CucsCallhomeSourceReplyTo_Object = MibTableColumn
cucsCallhomeSourceReplyTo = _CucsCallhomeSourceReplyTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 11),
    _CucsCallhomeSourceReplyTo_Type()
)
cucsCallhomeSourceReplyTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSourceReplyTo.setStatus("current")
_CucsCallhomeSourceSite_Type = SnmpAdminString
_CucsCallhomeSourceSite_Object = MibTableColumn
cucsCallhomeSourceSite = _CucsCallhomeSourceSite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 12),
    _CucsCallhomeSourceSite_Type()
)
cucsCallhomeSourceSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSourceSite.setStatus("current")
_CucsCallhomeSourceUrgency_Type = CucsCallhomeUrgency
_CucsCallhomeSourceUrgency_Object = MibTableColumn
cucsCallhomeSourceUrgency = _CucsCallhomeSourceUrgency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 8, 1, 13),
    _CucsCallhomeSourceUrgency_Type()
)
cucsCallhomeSourceUrgency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeSourceUrgency.setStatus("current")
_CucsCallhomeTestAlertTable_Object = MibTable
cucsCallhomeTestAlertTable = _CucsCallhomeTestAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 9)
)
if mibBuilder.loadTexts:
    cucsCallhomeTestAlertTable.setStatus("current")
_CucsCallhomeTestAlertEntry_Object = MibTableRow
cucsCallhomeTestAlertEntry = _CucsCallhomeTestAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 9, 1)
)
cucsCallhomeTestAlertEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB", "cucsCallhomeTestAlertInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCallhomeTestAlertEntry.setStatus("current")
_CucsCallhomeTestAlertInstanceId_Type = CucsManagedObjectId
_CucsCallhomeTestAlertInstanceId_Object = MibTableColumn
cucsCallhomeTestAlertInstanceId = _CucsCallhomeTestAlertInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 9, 1, 1),
    _CucsCallhomeTestAlertInstanceId_Type()
)
cucsCallhomeTestAlertInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCallhomeTestAlertInstanceId.setStatus("current")
_CucsCallhomeTestAlertDn_Type = CucsManagedObjectDn
_CucsCallhomeTestAlertDn_Object = MibTableColumn
cucsCallhomeTestAlertDn = _CucsCallhomeTestAlertDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 9, 1, 2),
    _CucsCallhomeTestAlertDn_Type()
)
cucsCallhomeTestAlertDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeTestAlertDn.setStatus("current")
_CucsCallhomeTestAlertRn_Type = SnmpAdminString
_CucsCallhomeTestAlertRn_Object = MibTableColumn
cucsCallhomeTestAlertRn = _CucsCallhomeTestAlertRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 9, 1, 3),
    _CucsCallhomeTestAlertRn_Type()
)
cucsCallhomeTestAlertRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeTestAlertRn.setStatus("current")
_CucsCallhomeTestAlertDescription_Type = SnmpAdminString
_CucsCallhomeTestAlertDescription_Object = MibTableColumn
cucsCallhomeTestAlertDescription = _CucsCallhomeTestAlertDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 9, 1, 4),
    _CucsCallhomeTestAlertDescription_Type()
)
cucsCallhomeTestAlertDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeTestAlertDescription.setStatus("current")
_CucsCallhomeTestAlertGroup_Type = CucsCallhomeAlertGroup
_CucsCallhomeTestAlertGroup_Object = MibTableColumn
cucsCallhomeTestAlertGroup = _CucsCallhomeTestAlertGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 9, 1, 5),
    _CucsCallhomeTestAlertGroup_Type()
)
cucsCallhomeTestAlertGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeTestAlertGroup.setStatus("current")
_CucsCallhomeTestAlertLevel_Type = CucsCallhomeAlertLevel
_CucsCallhomeTestAlertLevel_Object = MibTableColumn
cucsCallhomeTestAlertLevel = _CucsCallhomeTestAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 9, 1, 6),
    _CucsCallhomeTestAlertLevel_Type()
)
cucsCallhomeTestAlertLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeTestAlertLevel.setStatus("current")
_CucsCallhomeTestAlertMessageSubtype_Type = CucsCallhomeAlertMessageSubtype
_CucsCallhomeTestAlertMessageSubtype_Object = MibTableColumn
cucsCallhomeTestAlertMessageSubtype = _CucsCallhomeTestAlertMessageSubtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 9, 1, 7),
    _CucsCallhomeTestAlertMessageSubtype_Type()
)
cucsCallhomeTestAlertMessageSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeTestAlertMessageSubtype.setStatus("current")
_CucsCallhomeTestAlertMessageType_Type = CucsCallhomeAlertMessageType
_CucsCallhomeTestAlertMessageType_Object = MibTableColumn
cucsCallhomeTestAlertMessageType = _CucsCallhomeTestAlertMessageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 9, 1, 8),
    _CucsCallhomeTestAlertMessageType_Type()
)
cucsCallhomeTestAlertMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeTestAlertMessageType.setStatus("current")
_CucsCallhomeTestAlertSendNow_Type = TruthValue
_CucsCallhomeTestAlertSendNow_Object = MibTableColumn
cucsCallhomeTestAlertSendNow = _CucsCallhomeTestAlertSendNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 9, 1, 9),
    _CucsCallhomeTestAlertSendNow_Type()
)
cucsCallhomeTestAlertSendNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeTestAlertSendNow.setStatus("current")
_CucsCallhomeEpFsmTable_Object = MibTable
cucsCallhomeEpFsmTable = _CucsCallhomeEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10)
)
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmTable.setStatus("current")
_CucsCallhomeEpFsmEntry_Object = MibTableRow
cucsCallhomeEpFsmEntry = _CucsCallhomeEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10, 1)
)
cucsCallhomeEpFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB", "cucsCallhomeEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmEntry.setStatus("current")
_CucsCallhomeEpFsmInstanceId_Type = CucsManagedObjectId
_CucsCallhomeEpFsmInstanceId_Object = MibTableColumn
cucsCallhomeEpFsmInstanceId = _CucsCallhomeEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10, 1, 1),
    _CucsCallhomeEpFsmInstanceId_Type()
)
cucsCallhomeEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmInstanceId.setStatus("current")
_CucsCallhomeEpFsmDn_Type = CucsManagedObjectDn
_CucsCallhomeEpFsmDn_Object = MibTableColumn
cucsCallhomeEpFsmDn = _CucsCallhomeEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10, 1, 2),
    _CucsCallhomeEpFsmDn_Type()
)
cucsCallhomeEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmDn.setStatus("current")
_CucsCallhomeEpFsmRn_Type = SnmpAdminString
_CucsCallhomeEpFsmRn_Object = MibTableColumn
cucsCallhomeEpFsmRn = _CucsCallhomeEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10, 1, 3),
    _CucsCallhomeEpFsmRn_Type()
)
cucsCallhomeEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmRn.setStatus("current")
_CucsCallhomeEpFsmCompletionTime_Type = DateAndTime
_CucsCallhomeEpFsmCompletionTime_Object = MibTableColumn
cucsCallhomeEpFsmCompletionTime = _CucsCallhomeEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10, 1, 4),
    _CucsCallhomeEpFsmCompletionTime_Type()
)
cucsCallhomeEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmCompletionTime.setStatus("current")
_CucsCallhomeEpFsmCurrentFsm_Type = CucsCallhomeEpFsmCurrentFsm
_CucsCallhomeEpFsmCurrentFsm_Object = MibTableColumn
cucsCallhomeEpFsmCurrentFsm = _CucsCallhomeEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10, 1, 5),
    _CucsCallhomeEpFsmCurrentFsm_Type()
)
cucsCallhomeEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmCurrentFsm.setStatus("current")
_CucsCallhomeEpFsmDescrData_Type = SnmpAdminString
_CucsCallhomeEpFsmDescrData_Object = MibTableColumn
cucsCallhomeEpFsmDescrData = _CucsCallhomeEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10, 1, 6),
    _CucsCallhomeEpFsmDescrData_Type()
)
cucsCallhomeEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmDescrData.setStatus("current")
_CucsCallhomeEpFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsCallhomeEpFsmFsmStatus_Object = MibTableColumn
cucsCallhomeEpFsmFsmStatus = _CucsCallhomeEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10, 1, 7),
    _CucsCallhomeEpFsmFsmStatus_Type()
)
cucsCallhomeEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmFsmStatus.setStatus("current")
_CucsCallhomeEpFsmProgress_Type = Gauge32
_CucsCallhomeEpFsmProgress_Object = MibTableColumn
cucsCallhomeEpFsmProgress = _CucsCallhomeEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10, 1, 8),
    _CucsCallhomeEpFsmProgress_Type()
)
cucsCallhomeEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmProgress.setStatus("current")
_CucsCallhomeEpFsmRmtErrCode_Type = Gauge32
_CucsCallhomeEpFsmRmtErrCode_Object = MibTableColumn
cucsCallhomeEpFsmRmtErrCode = _CucsCallhomeEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10, 1, 9),
    _CucsCallhomeEpFsmRmtErrCode_Type()
)
cucsCallhomeEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmRmtErrCode.setStatus("current")
_CucsCallhomeEpFsmRmtErrDescr_Type = SnmpAdminString
_CucsCallhomeEpFsmRmtErrDescr_Object = MibTableColumn
cucsCallhomeEpFsmRmtErrDescr = _CucsCallhomeEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10, 1, 10),
    _CucsCallhomeEpFsmRmtErrDescr_Type()
)
cucsCallhomeEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmRmtErrDescr.setStatus("current")
_CucsCallhomeEpFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsCallhomeEpFsmRmtRslt_Object = MibTableColumn
cucsCallhomeEpFsmRmtRslt = _CucsCallhomeEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 10, 1, 11),
    _CucsCallhomeEpFsmRmtRslt_Type()
)
cucsCallhomeEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmRmtRslt.setStatus("current")
_CucsCallhomeEpFsmStageTable_Object = MibTable
cucsCallhomeEpFsmStageTable = _CucsCallhomeEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 11)
)
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStageTable.setStatus("current")
_CucsCallhomeEpFsmStageEntry_Object = MibTableRow
cucsCallhomeEpFsmStageEntry = _CucsCallhomeEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 11, 1)
)
cucsCallhomeEpFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB", "cucsCallhomeEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStageEntry.setStatus("current")
_CucsCallhomeEpFsmStageInstanceId_Type = CucsManagedObjectId
_CucsCallhomeEpFsmStageInstanceId_Object = MibTableColumn
cucsCallhomeEpFsmStageInstanceId = _CucsCallhomeEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 11, 1, 1),
    _CucsCallhomeEpFsmStageInstanceId_Type()
)
cucsCallhomeEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStageInstanceId.setStatus("current")
_CucsCallhomeEpFsmStageDn_Type = CucsManagedObjectDn
_CucsCallhomeEpFsmStageDn_Object = MibTableColumn
cucsCallhomeEpFsmStageDn = _CucsCallhomeEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 11, 1, 2),
    _CucsCallhomeEpFsmStageDn_Type()
)
cucsCallhomeEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStageDn.setStatus("current")
_CucsCallhomeEpFsmStageRn_Type = SnmpAdminString
_CucsCallhomeEpFsmStageRn_Object = MibTableColumn
cucsCallhomeEpFsmStageRn = _CucsCallhomeEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 11, 1, 3),
    _CucsCallhomeEpFsmStageRn_Type()
)
cucsCallhomeEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStageRn.setStatus("current")
_CucsCallhomeEpFsmStageDescrData_Type = SnmpAdminString
_CucsCallhomeEpFsmStageDescrData_Object = MibTableColumn
cucsCallhomeEpFsmStageDescrData = _CucsCallhomeEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 11, 1, 4),
    _CucsCallhomeEpFsmStageDescrData_Type()
)
cucsCallhomeEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStageDescrData.setStatus("current")
_CucsCallhomeEpFsmStageLastUpdateTime_Type = DateAndTime
_CucsCallhomeEpFsmStageLastUpdateTime_Object = MibTableColumn
cucsCallhomeEpFsmStageLastUpdateTime = _CucsCallhomeEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 11, 1, 5),
    _CucsCallhomeEpFsmStageLastUpdateTime_Type()
)
cucsCallhomeEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStageLastUpdateTime.setStatus("current")
_CucsCallhomeEpFsmStageName_Type = CucsCallhomeEpFsmStageName
_CucsCallhomeEpFsmStageName_Object = MibTableColumn
cucsCallhomeEpFsmStageName = _CucsCallhomeEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 11, 1, 6),
    _CucsCallhomeEpFsmStageName_Type()
)
cucsCallhomeEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStageName.setStatus("current")
_CucsCallhomeEpFsmStageOrder_Type = Gauge32
_CucsCallhomeEpFsmStageOrder_Object = MibTableColumn
cucsCallhomeEpFsmStageOrder = _CucsCallhomeEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 11, 1, 7),
    _CucsCallhomeEpFsmStageOrder_Type()
)
cucsCallhomeEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStageOrder.setStatus("current")
_CucsCallhomeEpFsmStageRetry_Type = Gauge32
_CucsCallhomeEpFsmStageRetry_Object = MibTableColumn
cucsCallhomeEpFsmStageRetry = _CucsCallhomeEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 11, 1, 8),
    _CucsCallhomeEpFsmStageRetry_Type()
)
cucsCallhomeEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStageRetry.setStatus("current")
_CucsCallhomeEpFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsCallhomeEpFsmStageStageStatus_Object = MibTableColumn
cucsCallhomeEpFsmStageStageStatus = _CucsCallhomeEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 11, 1, 9),
    _CucsCallhomeEpFsmStageStageStatus_Type()
)
cucsCallhomeEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeEpFsmStageStageStatus.setStatus("current")
_CucsCallhomeAnonymousReportingTable_Object = MibTable
cucsCallhomeAnonymousReportingTable = _CucsCallhomeAnonymousReportingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 12)
)
if mibBuilder.loadTexts:
    cucsCallhomeAnonymousReportingTable.setStatus("current")
_CucsCallhomeAnonymousReportingEntry_Object = MibTableRow
cucsCallhomeAnonymousReportingEntry = _CucsCallhomeAnonymousReportingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 12, 1)
)
cucsCallhomeAnonymousReportingEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB", "cucsCallhomeAnonymousReportingInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCallhomeAnonymousReportingEntry.setStatus("current")
_CucsCallhomeAnonymousReportingInstanceId_Type = CucsManagedObjectId
_CucsCallhomeAnonymousReportingInstanceId_Object = MibTableColumn
cucsCallhomeAnonymousReportingInstanceId = _CucsCallhomeAnonymousReportingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 12, 1, 1),
    _CucsCallhomeAnonymousReportingInstanceId_Type()
)
cucsCallhomeAnonymousReportingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCallhomeAnonymousReportingInstanceId.setStatus("current")
_CucsCallhomeAnonymousReportingDn_Type = CucsManagedObjectDn
_CucsCallhomeAnonymousReportingDn_Object = MibTableColumn
cucsCallhomeAnonymousReportingDn = _CucsCallhomeAnonymousReportingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 12, 1, 2),
    _CucsCallhomeAnonymousReportingDn_Type()
)
cucsCallhomeAnonymousReportingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeAnonymousReportingDn.setStatus("current")
_CucsCallhomeAnonymousReportingRn_Type = SnmpAdminString
_CucsCallhomeAnonymousReportingRn_Object = MibTableColumn
cucsCallhomeAnonymousReportingRn = _CucsCallhomeAnonymousReportingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 12, 1, 3),
    _CucsCallhomeAnonymousReportingRn_Type()
)
cucsCallhomeAnonymousReportingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeAnonymousReportingRn.setStatus("current")
_CucsCallhomeAnonymousReportingAdminState_Type = CucsCallhomeAnonymousReportingAdminState
_CucsCallhomeAnonymousReportingAdminState_Object = MibTableColumn
cucsCallhomeAnonymousReportingAdminState = _CucsCallhomeAnonymousReportingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 12, 1, 4),
    _CucsCallhomeAnonymousReportingAdminState_Type()
)
cucsCallhomeAnonymousReportingAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeAnonymousReportingAdminState.setStatus("current")
_CucsCallhomeAnonymousReportingCount_Type = Gauge32
_CucsCallhomeAnonymousReportingCount_Object = MibTableColumn
cucsCallhomeAnonymousReportingCount = _CucsCallhomeAnonymousReportingCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 12, 1, 5),
    _CucsCallhomeAnonymousReportingCount_Type()
)
cucsCallhomeAnonymousReportingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeAnonymousReportingCount.setStatus("current")
_CucsCallhomeAnonymousReportingSleepInterval_Type = Gauge32
_CucsCallhomeAnonymousReportingSleepInterval_Object = MibTableColumn
cucsCallhomeAnonymousReportingSleepInterval = _CucsCallhomeAnonymousReportingSleepInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 12, 1, 6),
    _CucsCallhomeAnonymousReportingSleepInterval_Type()
)
cucsCallhomeAnonymousReportingSleepInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeAnonymousReportingSleepInterval.setStatus("current")
_CucsCallhomeAnonymousReportingUserAcknowledged_Type = TruthValue
_CucsCallhomeAnonymousReportingUserAcknowledged_Object = MibTableColumn
cucsCallhomeAnonymousReportingUserAcknowledged = _CucsCallhomeAnonymousReportingUserAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 6, 12, 1, 7),
    _CucsCallhomeAnonymousReportingUserAcknowledged_Type()
)
cucsCallhomeAnonymousReportingUserAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCallhomeAnonymousReportingUserAcknowledged.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-CALLHOME-MIB",
    **{"cucsCallhomeObjects": cucsCallhomeObjects,
       "cucsCallhomeDestTable": cucsCallhomeDestTable,
       "cucsCallhomeDestEntry": cucsCallhomeDestEntry,
       "cucsCallhomeDestInstanceId": cucsCallhomeDestInstanceId,
       "cucsCallhomeDestDn": cucsCallhomeDestDn,
       "cucsCallhomeDestRn": cucsCallhomeDestRn,
       "cucsCallhomeDestEmail": cucsCallhomeDestEmail,
       "cucsCallhomeEpTable": cucsCallhomeEpTable,
       "cucsCallhomeEpEntry": cucsCallhomeEpEntry,
       "cucsCallhomeEpInstanceId": cucsCallhomeEpInstanceId,
       "cucsCallhomeEpDn": cucsCallhomeEpDn,
       "cucsCallhomeEpRn": cucsCallhomeEpRn,
       "cucsCallhomeEpAdminState": cucsCallhomeEpAdminState,
       "cucsCallhomeEpAlertThrottlingAdminState": cucsCallhomeEpAlertThrottlingAdminState,
       "cucsCallhomeEpFsmDescr": cucsCallhomeEpFsmDescr,
       "cucsCallhomeEpFsmPrev": cucsCallhomeEpFsmPrev,
       "cucsCallhomeEpFsmProgr": cucsCallhomeEpFsmProgr,
       "cucsCallhomeEpFsmRmtInvErrCode": cucsCallhomeEpFsmRmtInvErrCode,
       "cucsCallhomeEpFsmRmtInvErrDescr": cucsCallhomeEpFsmRmtInvErrDescr,
       "cucsCallhomeEpFsmRmtInvRslt": cucsCallhomeEpFsmRmtInvRslt,
       "cucsCallhomeEpFsmStageDescr": cucsCallhomeEpFsmStageDescr,
       "cucsCallhomeEpFsmStamp": cucsCallhomeEpFsmStamp,
       "cucsCallhomeEpFsmStatus": cucsCallhomeEpFsmStatus,
       "cucsCallhomeEpFsmTry": cucsCallhomeEpFsmTry,
       "cucsCallhomeEpConfigState": cucsCallhomeEpConfigState,
       "cucsCallhomeEpDescr": cucsCallhomeEpDescr,
       "cucsCallhomeEpIntId": cucsCallhomeEpIntId,
       "cucsCallhomeEpName": cucsCallhomeEpName,
       "cucsCallhomeEpPolicyLevel": cucsCallhomeEpPolicyLevel,
       "cucsCallhomeEpPolicyOwner": cucsCallhomeEpPolicyOwner,
       "cucsCallhomeEpFsmTaskTable": cucsCallhomeEpFsmTaskTable,
       "cucsCallhomeEpFsmTaskEntry": cucsCallhomeEpFsmTaskEntry,
       "cucsCallhomeEpFsmTaskInstanceId": cucsCallhomeEpFsmTaskInstanceId,
       "cucsCallhomeEpFsmTaskDn": cucsCallhomeEpFsmTaskDn,
       "cucsCallhomeEpFsmTaskRn": cucsCallhomeEpFsmTaskRn,
       "cucsCallhomeEpFsmTaskCompletion": cucsCallhomeEpFsmTaskCompletion,
       "cucsCallhomeEpFsmTaskFlags": cucsCallhomeEpFsmTaskFlags,
       "cucsCallhomeEpFsmTaskItem": cucsCallhomeEpFsmTaskItem,
       "cucsCallhomeEpFsmTaskSeqId": cucsCallhomeEpFsmTaskSeqId,
       "cucsCallhomePeriodicSystemInventoryTable": cucsCallhomePeriodicSystemInventoryTable,
       "cucsCallhomePeriodicSystemInventoryEntry": cucsCallhomePeriodicSystemInventoryEntry,
       "cucsCallhomePeriodicSystemInventoryInstanceId": cucsCallhomePeriodicSystemInventoryInstanceId,
       "cucsCallhomePeriodicSystemInventoryDn": cucsCallhomePeriodicSystemInventoryDn,
       "cucsCallhomePeriodicSystemInventoryRn": cucsCallhomePeriodicSystemInventoryRn,
       "cucsCallhomePeriodicSystemInventoryAdminState": cucsCallhomePeriodicSystemInventoryAdminState,
       "cucsCallhomePeriodicSystemInventoryIntervalDays": cucsCallhomePeriodicSystemInventoryIntervalDays,
       "cucsCallhomePeriodicSystemInventoryLastDeadline": cucsCallhomePeriodicSystemInventoryLastDeadline,
       "cucsCallhomePeriodicSystemInventoryMaximumRetryCount": cucsCallhomePeriodicSystemInventoryMaximumRetryCount,
       "cucsCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds": cucsCallhomePeriodicSystemInventoryMinimumSendNowIntervalSeconds,
       "cucsCallhomePeriodicSystemInventoryNextDeadline": cucsCallhomePeriodicSystemInventoryNextDeadline,
       "cucsCallhomePeriodicSystemInventoryPollIntervalSeconds": cucsCallhomePeriodicSystemInventoryPollIntervalSeconds,
       "cucsCallhomePeriodicSystemInventoryRetryCount": cucsCallhomePeriodicSystemInventoryRetryCount,
       "cucsCallhomePeriodicSystemInventoryRetryDelayMinutes": cucsCallhomePeriodicSystemInventoryRetryDelayMinutes,
       "cucsCallhomePeriodicSystemInventorySendNow": cucsCallhomePeriodicSystemInventorySendNow,
       "cucsCallhomePeriodicSystemInventoryTimeOfDayHour": cucsCallhomePeriodicSystemInventoryTimeOfDayHour,
       "cucsCallhomePeriodicSystemInventoryTimeOfDayMinute": cucsCallhomePeriodicSystemInventoryTimeOfDayMinute,
       "cucsCallhomePeriodicSystemInventoryTimeOfLastAttempt": cucsCallhomePeriodicSystemInventoryTimeOfLastAttempt,
       "cucsCallhomePeriodicSystemInventoryTimeOfLastSuccess": cucsCallhomePeriodicSystemInventoryTimeOfLastSuccess,
       "cucsCallhomePolicyTable": cucsCallhomePolicyTable,
       "cucsCallhomePolicyEntry": cucsCallhomePolicyEntry,
       "cucsCallhomePolicyInstanceId": cucsCallhomePolicyInstanceId,
       "cucsCallhomePolicyDn": cucsCallhomePolicyDn,
       "cucsCallhomePolicyRn": cucsCallhomePolicyRn,
       "cucsCallhomePolicyAdminState": cucsCallhomePolicyAdminState,
       "cucsCallhomePolicyCause": cucsCallhomePolicyCause,
       "cucsCallhomePolicyDescr": cucsCallhomePolicyDescr,
       "cucsCallhomePolicyName": cucsCallhomePolicyName,
       "cucsCallhomeProfileTable": cucsCallhomeProfileTable,
       "cucsCallhomeProfileEntry": cucsCallhomeProfileEntry,
       "cucsCallhomeProfileInstanceId": cucsCallhomeProfileInstanceId,
       "cucsCallhomeProfileDn": cucsCallhomeProfileDn,
       "cucsCallhomeProfileRn": cucsCallhomeProfileRn,
       "cucsCallhomeProfileAlertGroups": cucsCallhomeProfileAlertGroups,
       "cucsCallhomeProfileDescr": cucsCallhomeProfileDescr,
       "cucsCallhomeProfileFormat": cucsCallhomeProfileFormat,
       "cucsCallhomeProfileLevel": cucsCallhomeProfileLevel,
       "cucsCallhomeProfileMaxSize": cucsCallhomeProfileMaxSize,
       "cucsCallhomeProfileName": cucsCallhomeProfileName,
       "cucsCallhomeSmtpTable": cucsCallhomeSmtpTable,
       "cucsCallhomeSmtpEntry": cucsCallhomeSmtpEntry,
       "cucsCallhomeSmtpInstanceId": cucsCallhomeSmtpInstanceId,
       "cucsCallhomeSmtpDn": cucsCallhomeSmtpDn,
       "cucsCallhomeSmtpRn": cucsCallhomeSmtpRn,
       "cucsCallhomeSmtpHost": cucsCallhomeSmtpHost,
       "cucsCallhomeSmtpPort": cucsCallhomeSmtpPort,
       "cucsCallhomeSourceTable": cucsCallhomeSourceTable,
       "cucsCallhomeSourceEntry": cucsCallhomeSourceEntry,
       "cucsCallhomeSourceInstanceId": cucsCallhomeSourceInstanceId,
       "cucsCallhomeSourceDn": cucsCallhomeSourceDn,
       "cucsCallhomeSourceRn": cucsCallhomeSourceRn,
       "cucsCallhomeSourceAddr": cucsCallhomeSourceAddr,
       "cucsCallhomeSourceContact": cucsCallhomeSourceContact,
       "cucsCallhomeSourceContract": cucsCallhomeSourceContract,
       "cucsCallhomeSourceCustomer": cucsCallhomeSourceCustomer,
       "cucsCallhomeSourceEmail": cucsCallhomeSourceEmail,
       "cucsCallhomeSourceFrom": cucsCallhomeSourceFrom,
       "cucsCallhomeSourcePhone": cucsCallhomeSourcePhone,
       "cucsCallhomeSourceReplyTo": cucsCallhomeSourceReplyTo,
       "cucsCallhomeSourceSite": cucsCallhomeSourceSite,
       "cucsCallhomeSourceUrgency": cucsCallhomeSourceUrgency,
       "cucsCallhomeTestAlertTable": cucsCallhomeTestAlertTable,
       "cucsCallhomeTestAlertEntry": cucsCallhomeTestAlertEntry,
       "cucsCallhomeTestAlertInstanceId": cucsCallhomeTestAlertInstanceId,
       "cucsCallhomeTestAlertDn": cucsCallhomeTestAlertDn,
       "cucsCallhomeTestAlertRn": cucsCallhomeTestAlertRn,
       "cucsCallhomeTestAlertDescription": cucsCallhomeTestAlertDescription,
       "cucsCallhomeTestAlertGroup": cucsCallhomeTestAlertGroup,
       "cucsCallhomeTestAlertLevel": cucsCallhomeTestAlertLevel,
       "cucsCallhomeTestAlertMessageSubtype": cucsCallhomeTestAlertMessageSubtype,
       "cucsCallhomeTestAlertMessageType": cucsCallhomeTestAlertMessageType,
       "cucsCallhomeTestAlertSendNow": cucsCallhomeTestAlertSendNow,
       "cucsCallhomeEpFsmTable": cucsCallhomeEpFsmTable,
       "cucsCallhomeEpFsmEntry": cucsCallhomeEpFsmEntry,
       "cucsCallhomeEpFsmInstanceId": cucsCallhomeEpFsmInstanceId,
       "cucsCallhomeEpFsmDn": cucsCallhomeEpFsmDn,
       "cucsCallhomeEpFsmRn": cucsCallhomeEpFsmRn,
       "cucsCallhomeEpFsmCompletionTime": cucsCallhomeEpFsmCompletionTime,
       "cucsCallhomeEpFsmCurrentFsm": cucsCallhomeEpFsmCurrentFsm,
       "cucsCallhomeEpFsmDescrData": cucsCallhomeEpFsmDescrData,
       "cucsCallhomeEpFsmFsmStatus": cucsCallhomeEpFsmFsmStatus,
       "cucsCallhomeEpFsmProgress": cucsCallhomeEpFsmProgress,
       "cucsCallhomeEpFsmRmtErrCode": cucsCallhomeEpFsmRmtErrCode,
       "cucsCallhomeEpFsmRmtErrDescr": cucsCallhomeEpFsmRmtErrDescr,
       "cucsCallhomeEpFsmRmtRslt": cucsCallhomeEpFsmRmtRslt,
       "cucsCallhomeEpFsmStageTable": cucsCallhomeEpFsmStageTable,
       "cucsCallhomeEpFsmStageEntry": cucsCallhomeEpFsmStageEntry,
       "cucsCallhomeEpFsmStageInstanceId": cucsCallhomeEpFsmStageInstanceId,
       "cucsCallhomeEpFsmStageDn": cucsCallhomeEpFsmStageDn,
       "cucsCallhomeEpFsmStageRn": cucsCallhomeEpFsmStageRn,
       "cucsCallhomeEpFsmStageDescrData": cucsCallhomeEpFsmStageDescrData,
       "cucsCallhomeEpFsmStageLastUpdateTime": cucsCallhomeEpFsmStageLastUpdateTime,
       "cucsCallhomeEpFsmStageName": cucsCallhomeEpFsmStageName,
       "cucsCallhomeEpFsmStageOrder": cucsCallhomeEpFsmStageOrder,
       "cucsCallhomeEpFsmStageRetry": cucsCallhomeEpFsmStageRetry,
       "cucsCallhomeEpFsmStageStageStatus": cucsCallhomeEpFsmStageStageStatus,
       "cucsCallhomeAnonymousReportingTable": cucsCallhomeAnonymousReportingTable,
       "cucsCallhomeAnonymousReportingEntry": cucsCallhomeAnonymousReportingEntry,
       "cucsCallhomeAnonymousReportingInstanceId": cucsCallhomeAnonymousReportingInstanceId,
       "cucsCallhomeAnonymousReportingDn": cucsCallhomeAnonymousReportingDn,
       "cucsCallhomeAnonymousReportingRn": cucsCallhomeAnonymousReportingRn,
       "cucsCallhomeAnonymousReportingAdminState": cucsCallhomeAnonymousReportingAdminState,
       "cucsCallhomeAnonymousReportingCount": cucsCallhomeAnonymousReportingCount,
       "cucsCallhomeAnonymousReportingSleepInterval": cucsCallhomeAnonymousReportingSleepInterval,
       "cucsCallhomeAnonymousReportingUserAcknowledged": cucsCallhomeAnonymousReportingUserAcknowledged}
)
