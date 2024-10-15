# SNMP MIB module (CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:23 2024
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

(CucsCommClientAdminState,
 CucsConditionRemoteInvRslt,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsNetworkSwitchId,
 CucsPolicyPolicyOwner,
 CucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm,
 CucsSysdebugAutoCoreFileExportTargetFsmStageName,
 CucsSysdebugAutoCoreFileExportTargetFsmTaskItem,
 CucsSysdebugAutoCoreFileExportTargetProto,
 CucsSysdebugBackupBehaviorInterval,
 CucsSysdebugBackupBehaviorProto,
 CucsSysdebugBackupFormat,
 CucsSysdebugCoreExportStatus,
 CucsSysdebugCoreFileAdminState,
 CucsSysdebugCoreFileOperState,
 CucsSysdebugCoreFsmCurrentFsm,
 CucsSysdebugCoreFsmStageName,
 CucsSysdebugCoreFsmTaskItem,
 CucsSysdebugEpLogAdminState,
 CucsSysdebugEpLogBackupAction,
 CucsSysdebugEpLogCapacity,
 CucsSysdebugEpLogType,
 CucsSysdebugExportStatus,
 CucsSysdebugLogControlDomainEnum,
 CucsSysdebugLogControlEpFsmCurrentFsm,
 CucsSysdebugLogControlEpFsmStageName,
 CucsSysdebugLogControlEpFsmTaskItem,
 CucsSysdebugLogControlLevel,
 CucsSysdebugLogExportPolicyFsmCurrentFsm,
 CucsSysdebugLogExportPolicyFsmStageName,
 CucsSysdebugLogExportPolicyFsmTaskItem,
 CucsSysdebugLogExportPolicyProto,
 CucsSysdebugMEpLogOperState,
 CucsSysdebugManualCoreFileExportTargetAdminState,
 CucsSysdebugManualCoreFileExportTargetFsmCurrentFsm,
 CucsSysdebugManualCoreFileExportTargetFsmStageName,
 CucsSysdebugManualCoreFileExportTargetFsmTaskItem,
 CucsSysdebugManualCoreFileExportTargetProto,
 CucsSysdebugTSCmdOptCmdOptions,
 CucsSysdebugTSCmdOptMajorType,
 CucsSysdebugTechSupportAdminState,
 CucsSysdebugTechSupportFsmCurrentFsm,
 CucsSysdebugTechSupportFsmStageName,
 CucsSysdebugTechSupportFsmTaskItem,
 CucsSysdebugTechSupportOperState,
 CucsSysfileExporterPostAction) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsCommClientAdminState",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsNetworkSwitchId",
    "CucsPolicyPolicyOwner",
    "CucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm",
    "CucsSysdebugAutoCoreFileExportTargetFsmStageName",
    "CucsSysdebugAutoCoreFileExportTargetFsmTaskItem",
    "CucsSysdebugAutoCoreFileExportTargetProto",
    "CucsSysdebugBackupBehaviorInterval",
    "CucsSysdebugBackupBehaviorProto",
    "CucsSysdebugBackupFormat",
    "CucsSysdebugCoreExportStatus",
    "CucsSysdebugCoreFileAdminState",
    "CucsSysdebugCoreFileOperState",
    "CucsSysdebugCoreFsmCurrentFsm",
    "CucsSysdebugCoreFsmStageName",
    "CucsSysdebugCoreFsmTaskItem",
    "CucsSysdebugEpLogAdminState",
    "CucsSysdebugEpLogBackupAction",
    "CucsSysdebugEpLogCapacity",
    "CucsSysdebugEpLogType",
    "CucsSysdebugExportStatus",
    "CucsSysdebugLogControlDomainEnum",
    "CucsSysdebugLogControlEpFsmCurrentFsm",
    "CucsSysdebugLogControlEpFsmStageName",
    "CucsSysdebugLogControlEpFsmTaskItem",
    "CucsSysdebugLogControlLevel",
    "CucsSysdebugLogExportPolicyFsmCurrentFsm",
    "CucsSysdebugLogExportPolicyFsmStageName",
    "CucsSysdebugLogExportPolicyFsmTaskItem",
    "CucsSysdebugLogExportPolicyProto",
    "CucsSysdebugMEpLogOperState",
    "CucsSysdebugManualCoreFileExportTargetAdminState",
    "CucsSysdebugManualCoreFileExportTargetFsmCurrentFsm",
    "CucsSysdebugManualCoreFileExportTargetFsmStageName",
    "CucsSysdebugManualCoreFileExportTargetFsmTaskItem",
    "CucsSysdebugManualCoreFileExportTargetProto",
    "CucsSysdebugTSCmdOptCmdOptions",
    "CucsSysdebugTSCmdOptMajorType",
    "CucsSysdebugTechSupportAdminState",
    "CucsSysdebugTechSupportFsmCurrentFsm",
    "CucsSysdebugTechSupportFsmStageName",
    "CucsSysdebugTechSupportFsmTaskItem",
    "CucsSysdebugTechSupportOperState",
    "CucsSysfileExporterPostAction")

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

cucsSysdebugObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsSysdebugAutoCoreFileExportTargetTable_Object = MibTable
cucsSysdebugAutoCoreFileExportTargetTable = _CucsSysdebugAutoCoreFileExportTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1)
)
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetTable.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetEntry_Object = MibTableRow
cucsSysdebugAutoCoreFileExportTargetEntry = _CucsSysdebugAutoCoreFileExportTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1)
)
cucsSysdebugAutoCoreFileExportTargetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugAutoCoreFileExportTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetEntry.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetInstanceId_Type = CucsManagedObjectId
_CucsSysdebugAutoCoreFileExportTargetInstanceId_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetInstanceId = _CucsSysdebugAutoCoreFileExportTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 1),
    _CucsSysdebugAutoCoreFileExportTargetInstanceId_Type()
)
cucsSysdebugAutoCoreFileExportTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetInstanceId.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetDn_Type = CucsManagedObjectDn
_CucsSysdebugAutoCoreFileExportTargetDn_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetDn = _CucsSysdebugAutoCoreFileExportTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 2),
    _CucsSysdebugAutoCoreFileExportTargetDn_Type()
)
cucsSysdebugAutoCoreFileExportTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetDn.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetRn_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetRn_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetRn = _CucsSysdebugAutoCoreFileExportTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 3),
    _CucsSysdebugAutoCoreFileExportTargetRn_Type()
)
cucsSysdebugAutoCoreFileExportTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetRn.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetAdminState_Type = CucsCommClientAdminState
_CucsSysdebugAutoCoreFileExportTargetAdminState_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetAdminState = _CucsSysdebugAutoCoreFileExportTargetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 4),
    _CucsSysdebugAutoCoreFileExportTargetAdminState_Type()
)
cucsSysdebugAutoCoreFileExportTargetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetAdminState.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetDescr_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetDescr_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetDescr = _CucsSysdebugAutoCoreFileExportTargetDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 5),
    _CucsSysdebugAutoCoreFileExportTargetDescr_Type()
)
cucsSysdebugAutoCoreFileExportTargetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetDescr.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmDescr_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetFsmDescr_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmDescr = _CucsSysdebugAutoCoreFileExportTargetFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 6),
    _CucsSysdebugAutoCoreFileExportTargetFsmDescr_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmDescr.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmPrev_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetFsmPrev_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmPrev = _CucsSysdebugAutoCoreFileExportTargetFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 7),
    _CucsSysdebugAutoCoreFileExportTargetFsmPrev_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmPrev.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmProgr_Type = Gauge32
_CucsSysdebugAutoCoreFileExportTargetFsmProgr_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmProgr = _CucsSysdebugAutoCoreFileExportTargetFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 8),
    _CucsSysdebugAutoCoreFileExportTargetFsmProgr_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmProgr.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode_Type = Gauge32
_CucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode = _CucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 9),
    _CucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr = _CucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 10),
    _CucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSysdebugAutoCoreFileExportTargetFsmRmtInvRslt_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmRmtInvRslt = _CucsSysdebugAutoCoreFileExportTargetFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 11),
    _CucsSysdebugAutoCoreFileExportTargetFsmRmtInvRslt_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmRmtInvRslt.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStageDescr_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetFsmStageDescr_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmStageDescr = _CucsSysdebugAutoCoreFileExportTargetFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 12),
    _CucsSysdebugAutoCoreFileExportTargetFsmStageDescr_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStageDescr.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStamp_Type = DateAndTime
_CucsSysdebugAutoCoreFileExportTargetFsmStamp_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmStamp = _CucsSysdebugAutoCoreFileExportTargetFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 13),
    _CucsSysdebugAutoCoreFileExportTargetFsmStamp_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStamp.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStatus_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetFsmStatus_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmStatus = _CucsSysdebugAutoCoreFileExportTargetFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 14),
    _CucsSysdebugAutoCoreFileExportTargetFsmStatus_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStatus.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmTry_Type = Gauge32
_CucsSysdebugAutoCoreFileExportTargetFsmTry_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmTry = _CucsSysdebugAutoCoreFileExportTargetFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 15),
    _CucsSysdebugAutoCoreFileExportTargetFsmTry_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmTry.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetHostname_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetHostname_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetHostname = _CucsSysdebugAutoCoreFileExportTargetHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 16),
    _CucsSysdebugAutoCoreFileExportTargetHostname_Type()
)
cucsSysdebugAutoCoreFileExportTargetHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetHostname.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetIntId_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetIntId_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetIntId = _CucsSysdebugAutoCoreFileExportTargetIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 17),
    _CucsSysdebugAutoCoreFileExportTargetIntId_Type()
)
cucsSysdebugAutoCoreFileExportTargetIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetIntId.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetName_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetName_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetName = _CucsSysdebugAutoCoreFileExportTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 18),
    _CucsSysdebugAutoCoreFileExportTargetName_Type()
)
cucsSysdebugAutoCoreFileExportTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetName.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetPath_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetPath_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetPath = _CucsSysdebugAutoCoreFileExportTargetPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 19),
    _CucsSysdebugAutoCoreFileExportTargetPath_Type()
)
cucsSysdebugAutoCoreFileExportTargetPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetPath.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetPort_Type = Gauge32
_CucsSysdebugAutoCoreFileExportTargetPort_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetPort = _CucsSysdebugAutoCoreFileExportTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 20),
    _CucsSysdebugAutoCoreFileExportTargetPort_Type()
)
cucsSysdebugAutoCoreFileExportTargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetPort.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetPostAction_Type = CucsSysfileExporterPostAction
_CucsSysdebugAutoCoreFileExportTargetPostAction_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetPostAction = _CucsSysdebugAutoCoreFileExportTargetPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 21),
    _CucsSysdebugAutoCoreFileExportTargetPostAction_Type()
)
cucsSysdebugAutoCoreFileExportTargetPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetPostAction.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetProto_Type = CucsSysdebugAutoCoreFileExportTargetProto
_CucsSysdebugAutoCoreFileExportTargetProto_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetProto = _CucsSysdebugAutoCoreFileExportTargetProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 22),
    _CucsSysdebugAutoCoreFileExportTargetProto_Type()
)
cucsSysdebugAutoCoreFileExportTargetProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetProto.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetExportFailureReason_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetExportFailureReason_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetExportFailureReason = _CucsSysdebugAutoCoreFileExportTargetExportFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 23),
    _CucsSysdebugAutoCoreFileExportTargetExportFailureReason_Type()
)
cucsSysdebugAutoCoreFileExportTargetExportFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetExportFailureReason.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetExportStatus_Type = CucsSysdebugCoreExportStatus
_CucsSysdebugAutoCoreFileExportTargetExportStatus_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetExportStatus = _CucsSysdebugAutoCoreFileExportTargetExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 24),
    _CucsSysdebugAutoCoreFileExportTargetExportStatus_Type()
)
cucsSysdebugAutoCoreFileExportTargetExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetExportStatus.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetPolicyLevel_Type = Gauge32
_CucsSysdebugAutoCoreFileExportTargetPolicyLevel_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetPolicyLevel = _CucsSysdebugAutoCoreFileExportTargetPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 25),
    _CucsSysdebugAutoCoreFileExportTargetPolicyLevel_Type()
)
cucsSysdebugAutoCoreFileExportTargetPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetPolicyLevel.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsSysdebugAutoCoreFileExportTargetPolicyOwner_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetPolicyOwner = _CucsSysdebugAutoCoreFileExportTargetPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 1, 1, 26),
    _CucsSysdebugAutoCoreFileExportTargetPolicyOwner_Type()
)
cucsSysdebugAutoCoreFileExportTargetPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetPolicyOwner.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmTaskTable_Object = MibTable
cucsSysdebugAutoCoreFileExportTargetFsmTaskTable = _CucsSysdebugAutoCoreFileExportTargetFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 2)
)
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmTaskTable.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmTaskEntry_Object = MibTableRow
cucsSysdebugAutoCoreFileExportTargetFsmTaskEntry = _CucsSysdebugAutoCoreFileExportTargetFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 2, 1)
)
cucsSysdebugAutoCoreFileExportTargetFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugAutoCoreFileExportTargetFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmTaskEntry.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSysdebugAutoCoreFileExportTargetFsmTaskInstanceId_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmTaskInstanceId = _CucsSysdebugAutoCoreFileExportTargetFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 2, 1, 1),
    _CucsSysdebugAutoCoreFileExportTargetFsmTaskInstanceId_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmTaskInstanceId.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmTaskDn_Type = CucsManagedObjectDn
_CucsSysdebugAutoCoreFileExportTargetFsmTaskDn_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmTaskDn = _CucsSysdebugAutoCoreFileExportTargetFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 2, 1, 2),
    _CucsSysdebugAutoCoreFileExportTargetFsmTaskDn_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmTaskDn.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmTaskRn_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetFsmTaskRn_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmTaskRn = _CucsSysdebugAutoCoreFileExportTargetFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 2, 1, 3),
    _CucsSysdebugAutoCoreFileExportTargetFsmTaskRn_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmTaskRn.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSysdebugAutoCoreFileExportTargetFsmTaskCompletion_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmTaskCompletion = _CucsSysdebugAutoCoreFileExportTargetFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 2, 1, 4),
    _CucsSysdebugAutoCoreFileExportTargetFsmTaskCompletion_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmTaskCompletion.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmTaskFlags_Type = CucsFsmFlags
_CucsSysdebugAutoCoreFileExportTargetFsmTaskFlags_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmTaskFlags = _CucsSysdebugAutoCoreFileExportTargetFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 2, 1, 5),
    _CucsSysdebugAutoCoreFileExportTargetFsmTaskFlags_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmTaskFlags.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmTaskItem_Type = CucsSysdebugAutoCoreFileExportTargetFsmTaskItem
_CucsSysdebugAutoCoreFileExportTargetFsmTaskItem_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmTaskItem = _CucsSysdebugAutoCoreFileExportTargetFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 2, 1, 6),
    _CucsSysdebugAutoCoreFileExportTargetFsmTaskItem_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmTaskItem.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmTaskSeqId_Type = Gauge32
_CucsSysdebugAutoCoreFileExportTargetFsmTaskSeqId_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmTaskSeqId = _CucsSysdebugAutoCoreFileExportTargetFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 2, 1, 7),
    _CucsSysdebugAutoCoreFileExportTargetFsmTaskSeqId_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmTaskSeqId.setStatus("current")
_CucsSysdebugBackupBehaviorTable_Object = MibTable
cucsSysdebugBackupBehaviorTable = _CucsSysdebugBackupBehaviorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3)
)
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorTable.setStatus("current")
_CucsSysdebugBackupBehaviorEntry_Object = MibTableRow
cucsSysdebugBackupBehaviorEntry = _CucsSysdebugBackupBehaviorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1)
)
cucsSysdebugBackupBehaviorEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugBackupBehaviorInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorEntry.setStatus("current")
_CucsSysdebugBackupBehaviorInstanceId_Type = CucsManagedObjectId
_CucsSysdebugBackupBehaviorInstanceId_Object = MibTableColumn
cucsSysdebugBackupBehaviorInstanceId = _CucsSysdebugBackupBehaviorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1, 1),
    _CucsSysdebugBackupBehaviorInstanceId_Type()
)
cucsSysdebugBackupBehaviorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorInstanceId.setStatus("current")
_CucsSysdebugBackupBehaviorDn_Type = CucsManagedObjectDn
_CucsSysdebugBackupBehaviorDn_Object = MibTableColumn
cucsSysdebugBackupBehaviorDn = _CucsSysdebugBackupBehaviorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1, 2),
    _CucsSysdebugBackupBehaviorDn_Type()
)
cucsSysdebugBackupBehaviorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorDn.setStatus("current")
_CucsSysdebugBackupBehaviorRn_Type = SnmpAdminString
_CucsSysdebugBackupBehaviorRn_Object = MibTableColumn
cucsSysdebugBackupBehaviorRn = _CucsSysdebugBackupBehaviorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1, 3),
    _CucsSysdebugBackupBehaviorRn_Type()
)
cucsSysdebugBackupBehaviorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorRn.setStatus("current")
_CucsSysdebugBackupBehaviorAction_Type = CucsSysdebugEpLogBackupAction
_CucsSysdebugBackupBehaviorAction_Object = MibTableColumn
cucsSysdebugBackupBehaviorAction = _CucsSysdebugBackupBehaviorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1, 4),
    _CucsSysdebugBackupBehaviorAction_Type()
)
cucsSysdebugBackupBehaviorAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorAction.setStatus("current")
_CucsSysdebugBackupBehaviorClearOnBackup_Type = TruthValue
_CucsSysdebugBackupBehaviorClearOnBackup_Object = MibTableColumn
cucsSysdebugBackupBehaviorClearOnBackup = _CucsSysdebugBackupBehaviorClearOnBackup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1, 5),
    _CucsSysdebugBackupBehaviorClearOnBackup_Type()
)
cucsSysdebugBackupBehaviorClearOnBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorClearOnBackup.setStatus("current")
_CucsSysdebugBackupBehaviorFormat_Type = CucsSysdebugBackupFormat
_CucsSysdebugBackupBehaviorFormat_Object = MibTableColumn
cucsSysdebugBackupBehaviorFormat = _CucsSysdebugBackupBehaviorFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1, 6),
    _CucsSysdebugBackupBehaviorFormat_Type()
)
cucsSysdebugBackupBehaviorFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorFormat.setStatus("current")
_CucsSysdebugBackupBehaviorHostname_Type = SnmpAdminString
_CucsSysdebugBackupBehaviorHostname_Object = MibTableColumn
cucsSysdebugBackupBehaviorHostname = _CucsSysdebugBackupBehaviorHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1, 7),
    _CucsSysdebugBackupBehaviorHostname_Type()
)
cucsSysdebugBackupBehaviorHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorHostname.setStatus("current")
_CucsSysdebugBackupBehaviorInterval_Type = CucsSysdebugBackupBehaviorInterval
_CucsSysdebugBackupBehaviorInterval_Object = MibTableColumn
cucsSysdebugBackupBehaviorInterval = _CucsSysdebugBackupBehaviorInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1, 8),
    _CucsSysdebugBackupBehaviorInterval_Type()
)
cucsSysdebugBackupBehaviorInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorInterval.setStatus("current")
_CucsSysdebugBackupBehaviorProto_Type = CucsSysdebugBackupBehaviorProto
_CucsSysdebugBackupBehaviorProto_Object = MibTableColumn
cucsSysdebugBackupBehaviorProto = _CucsSysdebugBackupBehaviorProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1, 9),
    _CucsSysdebugBackupBehaviorProto_Type()
)
cucsSysdebugBackupBehaviorProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorProto.setStatus("current")
_CucsSysdebugBackupBehaviorPwd_Type = SnmpAdminString
_CucsSysdebugBackupBehaviorPwd_Object = MibTableColumn
cucsSysdebugBackupBehaviorPwd = _CucsSysdebugBackupBehaviorPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1, 10),
    _CucsSysdebugBackupBehaviorPwd_Type()
)
cucsSysdebugBackupBehaviorPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorPwd.setStatus("current")
_CucsSysdebugBackupBehaviorRemotePath_Type = SnmpAdminString
_CucsSysdebugBackupBehaviorRemotePath_Object = MibTableColumn
cucsSysdebugBackupBehaviorRemotePath = _CucsSysdebugBackupBehaviorRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1, 11),
    _CucsSysdebugBackupBehaviorRemotePath_Type()
)
cucsSysdebugBackupBehaviorRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorRemotePath.setStatus("current")
_CucsSysdebugBackupBehaviorUser_Type = SnmpAdminString
_CucsSysdebugBackupBehaviorUser_Object = MibTableColumn
cucsSysdebugBackupBehaviorUser = _CucsSysdebugBackupBehaviorUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 3, 1, 12),
    _CucsSysdebugBackupBehaviorUser_Type()
)
cucsSysdebugBackupBehaviorUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugBackupBehaviorUser.setStatus("current")
_CucsSysdebugCoreTable_Object = MibTable
cucsSysdebugCoreTable = _CucsSysdebugCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4)
)
if mibBuilder.loadTexts:
    cucsSysdebugCoreTable.setStatus("current")
_CucsSysdebugCoreEntry_Object = MibTableRow
cucsSysdebugCoreEntry = _CucsSysdebugCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1)
)
cucsSysdebugCoreEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugCoreInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugCoreEntry.setStatus("current")
_CucsSysdebugCoreInstanceId_Type = CucsManagedObjectId
_CucsSysdebugCoreInstanceId_Object = MibTableColumn
cucsSysdebugCoreInstanceId = _CucsSysdebugCoreInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 1),
    _CucsSysdebugCoreInstanceId_Type()
)
cucsSysdebugCoreInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugCoreInstanceId.setStatus("current")
_CucsSysdebugCoreDn_Type = CucsManagedObjectDn
_CucsSysdebugCoreDn_Object = MibTableColumn
cucsSysdebugCoreDn = _CucsSysdebugCoreDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 2),
    _CucsSysdebugCoreDn_Type()
)
cucsSysdebugCoreDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreDn.setStatus("current")
_CucsSysdebugCoreRn_Type = SnmpAdminString
_CucsSysdebugCoreRn_Object = MibTableColumn
cucsSysdebugCoreRn = _CucsSysdebugCoreRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 3),
    _CucsSysdebugCoreRn_Type()
)
cucsSysdebugCoreRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreRn.setStatus("current")
_CucsSysdebugCoreDescr_Type = SnmpAdminString
_CucsSysdebugCoreDescr_Object = MibTableColumn
cucsSysdebugCoreDescr = _CucsSysdebugCoreDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 4),
    _CucsSysdebugCoreDescr_Type()
)
cucsSysdebugCoreDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreDescr.setStatus("current")
_CucsSysdebugCoreName_Type = SnmpAdminString
_CucsSysdebugCoreName_Object = MibTableColumn
cucsSysdebugCoreName = _CucsSysdebugCoreName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 5),
    _CucsSysdebugCoreName_Type()
)
cucsSysdebugCoreName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreName.setStatus("current")
_CucsSysdebugCoreSize_Type = Gauge32
_CucsSysdebugCoreSize_Object = MibTableColumn
cucsSysdebugCoreSize = _CucsSysdebugCoreSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 6),
    _CucsSysdebugCoreSize_Type()
)
cucsSysdebugCoreSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreSize.setStatus("current")
_CucsSysdebugCoreSwitchId_Type = CucsNetworkSwitchId
_CucsSysdebugCoreSwitchId_Object = MibTableColumn
cucsSysdebugCoreSwitchId = _CucsSysdebugCoreSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 7),
    _CucsSysdebugCoreSwitchId_Type()
)
cucsSysdebugCoreSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreSwitchId.setStatus("current")
_CucsSysdebugCoreTs_Type = DateAndTime
_CucsSysdebugCoreTs_Object = MibTableColumn
cucsSysdebugCoreTs = _CucsSysdebugCoreTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 8),
    _CucsSysdebugCoreTs_Type()
)
cucsSysdebugCoreTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreTs.setStatus("current")
_CucsSysdebugCoreUri_Type = SnmpAdminString
_CucsSysdebugCoreUri_Object = MibTableColumn
cucsSysdebugCoreUri = _CucsSysdebugCoreUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 9),
    _CucsSysdebugCoreUri_Type()
)
cucsSysdebugCoreUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreUri.setStatus("current")
_CucsSysdebugCoreAdminState_Type = CucsSysdebugCoreFileAdminState
_CucsSysdebugCoreAdminState_Object = MibTableColumn
cucsSysdebugCoreAdminState = _CucsSysdebugCoreAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 10),
    _CucsSysdebugCoreAdminState_Type()
)
cucsSysdebugCoreAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreAdminState.setStatus("current")
_CucsSysdebugCoreFsmDescr_Type = SnmpAdminString
_CucsSysdebugCoreFsmDescr_Object = MibTableColumn
cucsSysdebugCoreFsmDescr = _CucsSysdebugCoreFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 11),
    _CucsSysdebugCoreFsmDescr_Type()
)
cucsSysdebugCoreFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmDescr.setStatus("current")
_CucsSysdebugCoreFsmPrev_Type = SnmpAdminString
_CucsSysdebugCoreFsmPrev_Object = MibTableColumn
cucsSysdebugCoreFsmPrev = _CucsSysdebugCoreFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 12),
    _CucsSysdebugCoreFsmPrev_Type()
)
cucsSysdebugCoreFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmPrev.setStatus("current")
_CucsSysdebugCoreFsmProgr_Type = Gauge32
_CucsSysdebugCoreFsmProgr_Object = MibTableColumn
cucsSysdebugCoreFsmProgr = _CucsSysdebugCoreFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 13),
    _CucsSysdebugCoreFsmProgr_Type()
)
cucsSysdebugCoreFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmProgr.setStatus("current")
_CucsSysdebugCoreFsmRmtInvErrCode_Type = Gauge32
_CucsSysdebugCoreFsmRmtInvErrCode_Object = MibTableColumn
cucsSysdebugCoreFsmRmtInvErrCode = _CucsSysdebugCoreFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 14),
    _CucsSysdebugCoreFsmRmtInvErrCode_Type()
)
cucsSysdebugCoreFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmRmtInvErrCode.setStatus("current")
_CucsSysdebugCoreFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSysdebugCoreFsmRmtInvErrDescr_Object = MibTableColumn
cucsSysdebugCoreFsmRmtInvErrDescr = _CucsSysdebugCoreFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 15),
    _CucsSysdebugCoreFsmRmtInvErrDescr_Type()
)
cucsSysdebugCoreFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmRmtInvErrDescr.setStatus("current")
_CucsSysdebugCoreFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSysdebugCoreFsmRmtInvRslt_Object = MibTableColumn
cucsSysdebugCoreFsmRmtInvRslt = _CucsSysdebugCoreFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 16),
    _CucsSysdebugCoreFsmRmtInvRslt_Type()
)
cucsSysdebugCoreFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmRmtInvRslt.setStatus("current")
_CucsSysdebugCoreFsmStageDescr_Type = SnmpAdminString
_CucsSysdebugCoreFsmStageDescr_Object = MibTableColumn
cucsSysdebugCoreFsmStageDescr = _CucsSysdebugCoreFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 17),
    _CucsSysdebugCoreFsmStageDescr_Type()
)
cucsSysdebugCoreFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStageDescr.setStatus("current")
_CucsSysdebugCoreFsmStamp_Type = DateAndTime
_CucsSysdebugCoreFsmStamp_Object = MibTableColumn
cucsSysdebugCoreFsmStamp = _CucsSysdebugCoreFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 18),
    _CucsSysdebugCoreFsmStamp_Type()
)
cucsSysdebugCoreFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStamp.setStatus("current")
_CucsSysdebugCoreFsmStatus_Type = SnmpAdminString
_CucsSysdebugCoreFsmStatus_Object = MibTableColumn
cucsSysdebugCoreFsmStatus = _CucsSysdebugCoreFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 19),
    _CucsSysdebugCoreFsmStatus_Type()
)
cucsSysdebugCoreFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStatus.setStatus("current")
_CucsSysdebugCoreFsmTry_Type = Gauge32
_CucsSysdebugCoreFsmTry_Object = MibTableColumn
cucsSysdebugCoreFsmTry = _CucsSysdebugCoreFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 20),
    _CucsSysdebugCoreFsmTry_Type()
)
cucsSysdebugCoreFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmTry.setStatus("current")
_CucsSysdebugCoreOperState_Type = CucsSysdebugCoreFileOperState
_CucsSysdebugCoreOperState_Object = MibTableColumn
cucsSysdebugCoreOperState = _CucsSysdebugCoreOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 4, 1, 21),
    _CucsSysdebugCoreOperState_Type()
)
cucsSysdebugCoreOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreOperState.setStatus("current")
_CucsSysdebugCoreFileRepositoryTable_Object = MibTable
cucsSysdebugCoreFileRepositoryTable = _CucsSysdebugCoreFileRepositoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 5)
)
if mibBuilder.loadTexts:
    cucsSysdebugCoreFileRepositoryTable.setStatus("current")
_CucsSysdebugCoreFileRepositoryEntry_Object = MibTableRow
cucsSysdebugCoreFileRepositoryEntry = _CucsSysdebugCoreFileRepositoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 5, 1)
)
cucsSysdebugCoreFileRepositoryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugCoreFileRepositoryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugCoreFileRepositoryEntry.setStatus("current")
_CucsSysdebugCoreFileRepositoryInstanceId_Type = CucsManagedObjectId
_CucsSysdebugCoreFileRepositoryInstanceId_Object = MibTableColumn
cucsSysdebugCoreFileRepositoryInstanceId = _CucsSysdebugCoreFileRepositoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 5, 1, 1),
    _CucsSysdebugCoreFileRepositoryInstanceId_Type()
)
cucsSysdebugCoreFileRepositoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFileRepositoryInstanceId.setStatus("current")
_CucsSysdebugCoreFileRepositoryDn_Type = CucsManagedObjectDn
_CucsSysdebugCoreFileRepositoryDn_Object = MibTableColumn
cucsSysdebugCoreFileRepositoryDn = _CucsSysdebugCoreFileRepositoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 5, 1, 2),
    _CucsSysdebugCoreFileRepositoryDn_Type()
)
cucsSysdebugCoreFileRepositoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFileRepositoryDn.setStatus("current")
_CucsSysdebugCoreFileRepositoryRn_Type = SnmpAdminString
_CucsSysdebugCoreFileRepositoryRn_Object = MibTableColumn
cucsSysdebugCoreFileRepositoryRn = _CucsSysdebugCoreFileRepositoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 5, 1, 3),
    _CucsSysdebugCoreFileRepositoryRn_Type()
)
cucsSysdebugCoreFileRepositoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFileRepositoryRn.setStatus("current")
_CucsSysdebugEpTable_Object = MibTable
cucsSysdebugEpTable = _CucsSysdebugEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 6)
)
if mibBuilder.loadTexts:
    cucsSysdebugEpTable.setStatus("current")
_CucsSysdebugEpEntry_Object = MibTableRow
cucsSysdebugEpEntry = _CucsSysdebugEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 6, 1)
)
cucsSysdebugEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugEpEntry.setStatus("current")
_CucsSysdebugEpInstanceId_Type = CucsManagedObjectId
_CucsSysdebugEpInstanceId_Object = MibTableColumn
cucsSysdebugEpInstanceId = _CucsSysdebugEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 6, 1, 1),
    _CucsSysdebugEpInstanceId_Type()
)
cucsSysdebugEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugEpInstanceId.setStatus("current")
_CucsSysdebugEpDn_Type = CucsManagedObjectDn
_CucsSysdebugEpDn_Object = MibTableColumn
cucsSysdebugEpDn = _CucsSysdebugEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 6, 1, 2),
    _CucsSysdebugEpDn_Type()
)
cucsSysdebugEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugEpDn.setStatus("current")
_CucsSysdebugEpRn_Type = SnmpAdminString
_CucsSysdebugEpRn_Object = MibTableColumn
cucsSysdebugEpRn = _CucsSysdebugEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 6, 1, 3),
    _CucsSysdebugEpRn_Type()
)
cucsSysdebugEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugEpRn.setStatus("current")
_CucsSysdebugLogControlDestinationFileTable_Object = MibTable
cucsSysdebugLogControlDestinationFileTable = _CucsSysdebugLogControlDestinationFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 7)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationFileTable.setStatus("current")
_CucsSysdebugLogControlDestinationFileEntry_Object = MibTableRow
cucsSysdebugLogControlDestinationFileEntry = _CucsSysdebugLogControlDestinationFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 7, 1)
)
cucsSysdebugLogControlDestinationFileEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogControlDestinationFileInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationFileEntry.setStatus("current")
_CucsSysdebugLogControlDestinationFileInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogControlDestinationFileInstanceId_Object = MibTableColumn
cucsSysdebugLogControlDestinationFileInstanceId = _CucsSysdebugLogControlDestinationFileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 7, 1, 1),
    _CucsSysdebugLogControlDestinationFileInstanceId_Type()
)
cucsSysdebugLogControlDestinationFileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationFileInstanceId.setStatus("current")
_CucsSysdebugLogControlDestinationFileDn_Type = CucsManagedObjectDn
_CucsSysdebugLogControlDestinationFileDn_Object = MibTableColumn
cucsSysdebugLogControlDestinationFileDn = _CucsSysdebugLogControlDestinationFileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 7, 1, 2),
    _CucsSysdebugLogControlDestinationFileDn_Type()
)
cucsSysdebugLogControlDestinationFileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationFileDn.setStatus("current")
_CucsSysdebugLogControlDestinationFileRn_Type = SnmpAdminString
_CucsSysdebugLogControlDestinationFileRn_Object = MibTableColumn
cucsSysdebugLogControlDestinationFileRn = _CucsSysdebugLogControlDestinationFileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 7, 1, 3),
    _CucsSysdebugLogControlDestinationFileRn_Type()
)
cucsSysdebugLogControlDestinationFileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationFileRn.setStatus("current")
_CucsSysdebugLogControlDestinationFileBackupCount_Type = Gauge32
_CucsSysdebugLogControlDestinationFileBackupCount_Object = MibTableColumn
cucsSysdebugLogControlDestinationFileBackupCount = _CucsSysdebugLogControlDestinationFileBackupCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 7, 1, 4),
    _CucsSysdebugLogControlDestinationFileBackupCount_Type()
)
cucsSysdebugLogControlDestinationFileBackupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationFileBackupCount.setStatus("current")
_CucsSysdebugLogControlDestinationFileDefaultLevel_Type = CucsSysdebugLogControlLevel
_CucsSysdebugLogControlDestinationFileDefaultLevel_Object = MibTableColumn
cucsSysdebugLogControlDestinationFileDefaultLevel = _CucsSysdebugLogControlDestinationFileDefaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 7, 1, 5),
    _CucsSysdebugLogControlDestinationFileDefaultLevel_Type()
)
cucsSysdebugLogControlDestinationFileDefaultLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationFileDefaultLevel.setStatus("current")
_CucsSysdebugLogControlDestinationFileDefaultSize_Type = Gauge32
_CucsSysdebugLogControlDestinationFileDefaultSize_Object = MibTableColumn
cucsSysdebugLogControlDestinationFileDefaultSize = _CucsSysdebugLogControlDestinationFileDefaultSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 7, 1, 6),
    _CucsSysdebugLogControlDestinationFileDefaultSize_Type()
)
cucsSysdebugLogControlDestinationFileDefaultSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationFileDefaultSize.setStatus("current")
_CucsSysdebugLogControlDestinationFileLevel_Type = CucsSysdebugLogControlLevel
_CucsSysdebugLogControlDestinationFileLevel_Object = MibTableColumn
cucsSysdebugLogControlDestinationFileLevel = _CucsSysdebugLogControlDestinationFileLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 7, 1, 7),
    _CucsSysdebugLogControlDestinationFileLevel_Type()
)
cucsSysdebugLogControlDestinationFileLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationFileLevel.setStatus("current")
_CucsSysdebugLogControlDestinationFileSize_Type = Gauge32
_CucsSysdebugLogControlDestinationFileSize_Object = MibTableColumn
cucsSysdebugLogControlDestinationFileSize = _CucsSysdebugLogControlDestinationFileSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 7, 1, 8),
    _CucsSysdebugLogControlDestinationFileSize_Type()
)
cucsSysdebugLogControlDestinationFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationFileSize.setStatus("current")
_CucsSysdebugLogControlDestinationSyslogTable_Object = MibTable
cucsSysdebugLogControlDestinationSyslogTable = _CucsSysdebugLogControlDestinationSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 8)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationSyslogTable.setStatus("current")
_CucsSysdebugLogControlDestinationSyslogEntry_Object = MibTableRow
cucsSysdebugLogControlDestinationSyslogEntry = _CucsSysdebugLogControlDestinationSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 8, 1)
)
cucsSysdebugLogControlDestinationSyslogEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogControlDestinationSyslogInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationSyslogEntry.setStatus("current")
_CucsSysdebugLogControlDestinationSyslogInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogControlDestinationSyslogInstanceId_Object = MibTableColumn
cucsSysdebugLogControlDestinationSyslogInstanceId = _CucsSysdebugLogControlDestinationSyslogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 8, 1, 1),
    _CucsSysdebugLogControlDestinationSyslogInstanceId_Type()
)
cucsSysdebugLogControlDestinationSyslogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationSyslogInstanceId.setStatus("current")
_CucsSysdebugLogControlDestinationSyslogDn_Type = CucsManagedObjectDn
_CucsSysdebugLogControlDestinationSyslogDn_Object = MibTableColumn
cucsSysdebugLogControlDestinationSyslogDn = _CucsSysdebugLogControlDestinationSyslogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 8, 1, 2),
    _CucsSysdebugLogControlDestinationSyslogDn_Type()
)
cucsSysdebugLogControlDestinationSyslogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationSyslogDn.setStatus("current")
_CucsSysdebugLogControlDestinationSyslogRn_Type = SnmpAdminString
_CucsSysdebugLogControlDestinationSyslogRn_Object = MibTableColumn
cucsSysdebugLogControlDestinationSyslogRn = _CucsSysdebugLogControlDestinationSyslogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 8, 1, 3),
    _CucsSysdebugLogControlDestinationSyslogRn_Type()
)
cucsSysdebugLogControlDestinationSyslogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationSyslogRn.setStatus("current")
_CucsSysdebugLogControlDestinationSyslogDefaultLevel_Type = CucsSysdebugLogControlLevel
_CucsSysdebugLogControlDestinationSyslogDefaultLevel_Object = MibTableColumn
cucsSysdebugLogControlDestinationSyslogDefaultLevel = _CucsSysdebugLogControlDestinationSyslogDefaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 8, 1, 4),
    _CucsSysdebugLogControlDestinationSyslogDefaultLevel_Type()
)
cucsSysdebugLogControlDestinationSyslogDefaultLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationSyslogDefaultLevel.setStatus("current")
_CucsSysdebugLogControlDestinationSyslogLevel_Type = CucsSysdebugLogControlLevel
_CucsSysdebugLogControlDestinationSyslogLevel_Object = MibTableColumn
cucsSysdebugLogControlDestinationSyslogLevel = _CucsSysdebugLogControlDestinationSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 8, 1, 5),
    _CucsSysdebugLogControlDestinationSyslogLevel_Type()
)
cucsSysdebugLogControlDestinationSyslogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDestinationSyslogLevel.setStatus("current")
_CucsSysdebugLogControlDomainTable_Object = MibTable
cucsSysdebugLogControlDomainTable = _CucsSysdebugLogControlDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 9)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDomainTable.setStatus("current")
_CucsSysdebugLogControlDomainEntry_Object = MibTableRow
cucsSysdebugLogControlDomainEntry = _CucsSysdebugLogControlDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 9, 1)
)
cucsSysdebugLogControlDomainEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogControlDomainInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDomainEntry.setStatus("current")
_CucsSysdebugLogControlDomainInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogControlDomainInstanceId_Object = MibTableColumn
cucsSysdebugLogControlDomainInstanceId = _CucsSysdebugLogControlDomainInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 9, 1, 1),
    _CucsSysdebugLogControlDomainInstanceId_Type()
)
cucsSysdebugLogControlDomainInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDomainInstanceId.setStatus("current")
_CucsSysdebugLogControlDomainDn_Type = CucsManagedObjectDn
_CucsSysdebugLogControlDomainDn_Object = MibTableColumn
cucsSysdebugLogControlDomainDn = _CucsSysdebugLogControlDomainDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 9, 1, 2),
    _CucsSysdebugLogControlDomainDn_Type()
)
cucsSysdebugLogControlDomainDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDomainDn.setStatus("current")
_CucsSysdebugLogControlDomainRn_Type = SnmpAdminString
_CucsSysdebugLogControlDomainRn_Object = MibTableColumn
cucsSysdebugLogControlDomainRn = _CucsSysdebugLogControlDomainRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 9, 1, 3),
    _CucsSysdebugLogControlDomainRn_Type()
)
cucsSysdebugLogControlDomainRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDomainRn.setStatus("current")
_CucsSysdebugLogControlDomainLevel_Type = CucsSysdebugLogControlLevel
_CucsSysdebugLogControlDomainLevel_Object = MibTableColumn
cucsSysdebugLogControlDomainLevel = _CucsSysdebugLogControlDomainLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 9, 1, 4),
    _CucsSysdebugLogControlDomainLevel_Type()
)
cucsSysdebugLogControlDomainLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDomainLevel.setStatus("current")
_CucsSysdebugLogControlDomainLevelFlag_Type = TruthValue
_CucsSysdebugLogControlDomainLevelFlag_Object = MibTableColumn
cucsSysdebugLogControlDomainLevelFlag = _CucsSysdebugLogControlDomainLevelFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 9, 1, 5),
    _CucsSysdebugLogControlDomainLevelFlag_Type()
)
cucsSysdebugLogControlDomainLevelFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDomainLevelFlag.setStatus("current")
_CucsSysdebugLogControlDomainName_Type = CucsSysdebugLogControlDomainEnum
_CucsSysdebugLogControlDomainName_Object = MibTableColumn
cucsSysdebugLogControlDomainName = _CucsSysdebugLogControlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 9, 1, 6),
    _CucsSysdebugLogControlDomainName_Type()
)
cucsSysdebugLogControlDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDomainName.setStatus("current")
_CucsSysdebugLogControlDomainPersist_Type = TruthValue
_CucsSysdebugLogControlDomainPersist_Object = MibTableColumn
cucsSysdebugLogControlDomainPersist = _CucsSysdebugLogControlDomainPersist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 9, 1, 7),
    _CucsSysdebugLogControlDomainPersist_Type()
)
cucsSysdebugLogControlDomainPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDomainPersist.setStatus("current")
_CucsSysdebugLogControlDomainReset_Type = TruthValue
_CucsSysdebugLogControlDomainReset_Object = MibTableColumn
cucsSysdebugLogControlDomainReset = _CucsSysdebugLogControlDomainReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 9, 1, 8),
    _CucsSysdebugLogControlDomainReset_Type()
)
cucsSysdebugLogControlDomainReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlDomainReset.setStatus("current")
_CucsSysdebugLogControlEpTable_Object = MibTable
cucsSysdebugLogControlEpTable = _CucsSysdebugLogControlEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpTable.setStatus("current")
_CucsSysdebugLogControlEpEntry_Object = MibTableRow
cucsSysdebugLogControlEpEntry = _CucsSysdebugLogControlEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1)
)
cucsSysdebugLogControlEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogControlEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpEntry.setStatus("current")
_CucsSysdebugLogControlEpInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogControlEpInstanceId_Object = MibTableColumn
cucsSysdebugLogControlEpInstanceId = _CucsSysdebugLogControlEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 1),
    _CucsSysdebugLogControlEpInstanceId_Type()
)
cucsSysdebugLogControlEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpInstanceId.setStatus("current")
_CucsSysdebugLogControlEpDn_Type = CucsManagedObjectDn
_CucsSysdebugLogControlEpDn_Object = MibTableColumn
cucsSysdebugLogControlEpDn = _CucsSysdebugLogControlEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 2),
    _CucsSysdebugLogControlEpDn_Type()
)
cucsSysdebugLogControlEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpDn.setStatus("current")
_CucsSysdebugLogControlEpRn_Type = SnmpAdminString
_CucsSysdebugLogControlEpRn_Object = MibTableColumn
cucsSysdebugLogControlEpRn = _CucsSysdebugLogControlEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 3),
    _CucsSysdebugLogControlEpRn_Type()
)
cucsSysdebugLogControlEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpRn.setStatus("current")
_CucsSysdebugLogControlEpFsmDescr_Type = SnmpAdminString
_CucsSysdebugLogControlEpFsmDescr_Object = MibTableColumn
cucsSysdebugLogControlEpFsmDescr = _CucsSysdebugLogControlEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 4),
    _CucsSysdebugLogControlEpFsmDescr_Type()
)
cucsSysdebugLogControlEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmDescr.setStatus("current")
_CucsSysdebugLogControlEpFsmPrev_Type = SnmpAdminString
_CucsSysdebugLogControlEpFsmPrev_Object = MibTableColumn
cucsSysdebugLogControlEpFsmPrev = _CucsSysdebugLogControlEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 5),
    _CucsSysdebugLogControlEpFsmPrev_Type()
)
cucsSysdebugLogControlEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmPrev.setStatus("current")
_CucsSysdebugLogControlEpFsmProgr_Type = Gauge32
_CucsSysdebugLogControlEpFsmProgr_Object = MibTableColumn
cucsSysdebugLogControlEpFsmProgr = _CucsSysdebugLogControlEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 6),
    _CucsSysdebugLogControlEpFsmProgr_Type()
)
cucsSysdebugLogControlEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmProgr.setStatus("current")
_CucsSysdebugLogControlEpFsmRmtInvErrCode_Type = Gauge32
_CucsSysdebugLogControlEpFsmRmtInvErrCode_Object = MibTableColumn
cucsSysdebugLogControlEpFsmRmtInvErrCode = _CucsSysdebugLogControlEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 7),
    _CucsSysdebugLogControlEpFsmRmtInvErrCode_Type()
)
cucsSysdebugLogControlEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmRmtInvErrCode.setStatus("current")
_CucsSysdebugLogControlEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSysdebugLogControlEpFsmRmtInvErrDescr_Object = MibTableColumn
cucsSysdebugLogControlEpFsmRmtInvErrDescr = _CucsSysdebugLogControlEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 8),
    _CucsSysdebugLogControlEpFsmRmtInvErrDescr_Type()
)
cucsSysdebugLogControlEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmRmtInvErrDescr.setStatus("current")
_CucsSysdebugLogControlEpFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSysdebugLogControlEpFsmRmtInvRslt_Object = MibTableColumn
cucsSysdebugLogControlEpFsmRmtInvRslt = _CucsSysdebugLogControlEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 9),
    _CucsSysdebugLogControlEpFsmRmtInvRslt_Type()
)
cucsSysdebugLogControlEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmRmtInvRslt.setStatus("current")
_CucsSysdebugLogControlEpFsmStageDescr_Type = SnmpAdminString
_CucsSysdebugLogControlEpFsmStageDescr_Object = MibTableColumn
cucsSysdebugLogControlEpFsmStageDescr = _CucsSysdebugLogControlEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 10),
    _CucsSysdebugLogControlEpFsmStageDescr_Type()
)
cucsSysdebugLogControlEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStageDescr.setStatus("current")
_CucsSysdebugLogControlEpFsmStamp_Type = DateAndTime
_CucsSysdebugLogControlEpFsmStamp_Object = MibTableColumn
cucsSysdebugLogControlEpFsmStamp = _CucsSysdebugLogControlEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 11),
    _CucsSysdebugLogControlEpFsmStamp_Type()
)
cucsSysdebugLogControlEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStamp.setStatus("current")
_CucsSysdebugLogControlEpFsmStatus_Type = SnmpAdminString
_CucsSysdebugLogControlEpFsmStatus_Object = MibTableColumn
cucsSysdebugLogControlEpFsmStatus = _CucsSysdebugLogControlEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 12),
    _CucsSysdebugLogControlEpFsmStatus_Type()
)
cucsSysdebugLogControlEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStatus.setStatus("current")
_CucsSysdebugLogControlEpFsmTry_Type = Gauge32
_CucsSysdebugLogControlEpFsmTry_Object = MibTableColumn
cucsSysdebugLogControlEpFsmTry = _CucsSysdebugLogControlEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 13),
    _CucsSysdebugLogControlEpFsmTry_Type()
)
cucsSysdebugLogControlEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmTry.setStatus("current")
_CucsSysdebugLogControlEpLevel_Type = CucsSysdebugLogControlLevel
_CucsSysdebugLogControlEpLevel_Object = MibTableColumn
cucsSysdebugLogControlEpLevel = _CucsSysdebugLogControlEpLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 14),
    _CucsSysdebugLogControlEpLevel_Type()
)
cucsSysdebugLogControlEpLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpLevel.setStatus("current")
_CucsSysdebugLogControlEpLevelFlag_Type = TruthValue
_CucsSysdebugLogControlEpLevelFlag_Object = MibTableColumn
cucsSysdebugLogControlEpLevelFlag = _CucsSysdebugLogControlEpLevelFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 15),
    _CucsSysdebugLogControlEpLevelFlag_Type()
)
cucsSysdebugLogControlEpLevelFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpLevelFlag.setStatus("current")
_CucsSysdebugLogControlEpPersist_Type = TruthValue
_CucsSysdebugLogControlEpPersist_Object = MibTableColumn
cucsSysdebugLogControlEpPersist = _CucsSysdebugLogControlEpPersist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 16),
    _CucsSysdebugLogControlEpPersist_Type()
)
cucsSysdebugLogControlEpPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpPersist.setStatus("current")
_CucsSysdebugLogControlEpReset_Type = TruthValue
_CucsSysdebugLogControlEpReset_Object = MibTableColumn
cucsSysdebugLogControlEpReset = _CucsSysdebugLogControlEpReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 10, 1, 17),
    _CucsSysdebugLogControlEpReset_Type()
)
cucsSysdebugLogControlEpReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpReset.setStatus("current")
_CucsSysdebugLogControlEpFsmTaskTable_Object = MibTable
cucsSysdebugLogControlEpFsmTaskTable = _CucsSysdebugLogControlEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 11)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmTaskTable.setStatus("current")
_CucsSysdebugLogControlEpFsmTaskEntry_Object = MibTableRow
cucsSysdebugLogControlEpFsmTaskEntry = _CucsSysdebugLogControlEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 11, 1)
)
cucsSysdebugLogControlEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogControlEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmTaskEntry.setStatus("current")
_CucsSysdebugLogControlEpFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogControlEpFsmTaskInstanceId_Object = MibTableColumn
cucsSysdebugLogControlEpFsmTaskInstanceId = _CucsSysdebugLogControlEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 11, 1, 1),
    _CucsSysdebugLogControlEpFsmTaskInstanceId_Type()
)
cucsSysdebugLogControlEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmTaskInstanceId.setStatus("current")
_CucsSysdebugLogControlEpFsmTaskDn_Type = CucsManagedObjectDn
_CucsSysdebugLogControlEpFsmTaskDn_Object = MibTableColumn
cucsSysdebugLogControlEpFsmTaskDn = _CucsSysdebugLogControlEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 11, 1, 2),
    _CucsSysdebugLogControlEpFsmTaskDn_Type()
)
cucsSysdebugLogControlEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmTaskDn.setStatus("current")
_CucsSysdebugLogControlEpFsmTaskRn_Type = SnmpAdminString
_CucsSysdebugLogControlEpFsmTaskRn_Object = MibTableColumn
cucsSysdebugLogControlEpFsmTaskRn = _CucsSysdebugLogControlEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 11, 1, 3),
    _CucsSysdebugLogControlEpFsmTaskRn_Type()
)
cucsSysdebugLogControlEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmTaskRn.setStatus("current")
_CucsSysdebugLogControlEpFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSysdebugLogControlEpFsmTaskCompletion_Object = MibTableColumn
cucsSysdebugLogControlEpFsmTaskCompletion = _CucsSysdebugLogControlEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 11, 1, 4),
    _CucsSysdebugLogControlEpFsmTaskCompletion_Type()
)
cucsSysdebugLogControlEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmTaskCompletion.setStatus("current")
_CucsSysdebugLogControlEpFsmTaskFlags_Type = CucsFsmFlags
_CucsSysdebugLogControlEpFsmTaskFlags_Object = MibTableColumn
cucsSysdebugLogControlEpFsmTaskFlags = _CucsSysdebugLogControlEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 11, 1, 5),
    _CucsSysdebugLogControlEpFsmTaskFlags_Type()
)
cucsSysdebugLogControlEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmTaskFlags.setStatus("current")
_CucsSysdebugLogControlEpFsmTaskItem_Type = CucsSysdebugLogControlEpFsmTaskItem
_CucsSysdebugLogControlEpFsmTaskItem_Object = MibTableColumn
cucsSysdebugLogControlEpFsmTaskItem = _CucsSysdebugLogControlEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 11, 1, 6),
    _CucsSysdebugLogControlEpFsmTaskItem_Type()
)
cucsSysdebugLogControlEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmTaskItem.setStatus("current")
_CucsSysdebugLogControlEpFsmTaskSeqId_Type = Gauge32
_CucsSysdebugLogControlEpFsmTaskSeqId_Object = MibTableColumn
cucsSysdebugLogControlEpFsmTaskSeqId = _CucsSysdebugLogControlEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 11, 1, 7),
    _CucsSysdebugLogControlEpFsmTaskSeqId_Type()
)
cucsSysdebugLogControlEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmTaskSeqId.setStatus("current")
_CucsSysdebugLogControlModuleTable_Object = MibTable
cucsSysdebugLogControlModuleTable = _CucsSysdebugLogControlModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 12)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlModuleTable.setStatus("current")
_CucsSysdebugLogControlModuleEntry_Object = MibTableRow
cucsSysdebugLogControlModuleEntry = _CucsSysdebugLogControlModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 12, 1)
)
cucsSysdebugLogControlModuleEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogControlModuleInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlModuleEntry.setStatus("current")
_CucsSysdebugLogControlModuleInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogControlModuleInstanceId_Object = MibTableColumn
cucsSysdebugLogControlModuleInstanceId = _CucsSysdebugLogControlModuleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 12, 1, 1),
    _CucsSysdebugLogControlModuleInstanceId_Type()
)
cucsSysdebugLogControlModuleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlModuleInstanceId.setStatus("current")
_CucsSysdebugLogControlModuleDn_Type = CucsManagedObjectDn
_CucsSysdebugLogControlModuleDn_Object = MibTableColumn
cucsSysdebugLogControlModuleDn = _CucsSysdebugLogControlModuleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 12, 1, 2),
    _CucsSysdebugLogControlModuleDn_Type()
)
cucsSysdebugLogControlModuleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlModuleDn.setStatus("current")
_CucsSysdebugLogControlModuleRn_Type = SnmpAdminString
_CucsSysdebugLogControlModuleRn_Object = MibTableColumn
cucsSysdebugLogControlModuleRn = _CucsSysdebugLogControlModuleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 12, 1, 3),
    _CucsSysdebugLogControlModuleRn_Type()
)
cucsSysdebugLogControlModuleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlModuleRn.setStatus("current")
_CucsSysdebugLogControlModuleDefaultLevel_Type = CucsSysdebugLogControlLevel
_CucsSysdebugLogControlModuleDefaultLevel_Object = MibTableColumn
cucsSysdebugLogControlModuleDefaultLevel = _CucsSysdebugLogControlModuleDefaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 12, 1, 4),
    _CucsSysdebugLogControlModuleDefaultLevel_Type()
)
cucsSysdebugLogControlModuleDefaultLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlModuleDefaultLevel.setStatus("current")
_CucsSysdebugLogControlModuleLevel_Type = CucsSysdebugLogControlLevel
_CucsSysdebugLogControlModuleLevel_Object = MibTableColumn
cucsSysdebugLogControlModuleLevel = _CucsSysdebugLogControlModuleLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 12, 1, 5),
    _CucsSysdebugLogControlModuleLevel_Type()
)
cucsSysdebugLogControlModuleLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlModuleLevel.setStatus("current")
_CucsSysdebugLogControlModuleName_Type = SnmpAdminString
_CucsSysdebugLogControlModuleName_Object = MibTableColumn
cucsSysdebugLogControlModuleName = _CucsSysdebugLogControlModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 12, 1, 6),
    _CucsSysdebugLogControlModuleName_Type()
)
cucsSysdebugLogControlModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlModuleName.setStatus("current")
_CucsSysdebugLogControlModuleReset_Type = TruthValue
_CucsSysdebugLogControlModuleReset_Object = MibTableColumn
cucsSysdebugLogControlModuleReset = _CucsSysdebugLogControlModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 12, 1, 7),
    _CucsSysdebugLogControlModuleReset_Type()
)
cucsSysdebugLogControlModuleReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlModuleReset.setStatus("current")
_CucsSysdebugMEpLogTable_Object = MibTable
cucsSysdebugMEpLogTable = _CucsSysdebugMEpLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 13)
)
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogTable.setStatus("current")
_CucsSysdebugMEpLogEntry_Object = MibTableRow
cucsSysdebugMEpLogEntry = _CucsSysdebugMEpLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 13, 1)
)
cucsSysdebugMEpLogEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugMEpLogInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogEntry.setStatus("current")
_CucsSysdebugMEpLogInstanceId_Type = CucsManagedObjectId
_CucsSysdebugMEpLogInstanceId_Object = MibTableColumn
cucsSysdebugMEpLogInstanceId = _CucsSysdebugMEpLogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 13, 1, 1),
    _CucsSysdebugMEpLogInstanceId_Type()
)
cucsSysdebugMEpLogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogInstanceId.setStatus("current")
_CucsSysdebugMEpLogDn_Type = CucsManagedObjectDn
_CucsSysdebugMEpLogDn_Object = MibTableColumn
cucsSysdebugMEpLogDn = _CucsSysdebugMEpLogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 13, 1, 2),
    _CucsSysdebugMEpLogDn_Type()
)
cucsSysdebugMEpLogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogDn.setStatus("current")
_CucsSysdebugMEpLogRn_Type = SnmpAdminString
_CucsSysdebugMEpLogRn_Object = MibTableColumn
cucsSysdebugMEpLogRn = _CucsSysdebugMEpLogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 13, 1, 3),
    _CucsSysdebugMEpLogRn_Type()
)
cucsSysdebugMEpLogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogRn.setStatus("current")
_CucsSysdebugMEpLogAdminState_Type = CucsSysdebugEpLogAdminState
_CucsSysdebugMEpLogAdminState_Object = MibTableColumn
cucsSysdebugMEpLogAdminState = _CucsSysdebugMEpLogAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 13, 1, 4),
    _CucsSysdebugMEpLogAdminState_Type()
)
cucsSysdebugMEpLogAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogAdminState.setStatus("current")
_CucsSysdebugMEpLogCapacity_Type = CucsSysdebugEpLogCapacity
_CucsSysdebugMEpLogCapacity_Object = MibTableColumn
cucsSysdebugMEpLogCapacity = _CucsSysdebugMEpLogCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 13, 1, 5),
    _CucsSysdebugMEpLogCapacity_Type()
)
cucsSysdebugMEpLogCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogCapacity.setStatus("current")
_CucsSysdebugMEpLogId_Type = Gauge32
_CucsSysdebugMEpLogId_Object = MibTableColumn
cucsSysdebugMEpLogId = _CucsSysdebugMEpLogId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 13, 1, 6),
    _CucsSysdebugMEpLogId_Type()
)
cucsSysdebugMEpLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogId.setStatus("current")
_CucsSysdebugMEpLogLastUpdate_Type = DateAndTime
_CucsSysdebugMEpLogLastUpdate_Object = MibTableColumn
cucsSysdebugMEpLogLastUpdate = _CucsSysdebugMEpLogLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 13, 1, 7),
    _CucsSysdebugMEpLogLastUpdate_Type()
)
cucsSysdebugMEpLogLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogLastUpdate.setStatus("current")
_CucsSysdebugMEpLogOperState_Type = CucsSysdebugMEpLogOperState
_CucsSysdebugMEpLogOperState_Object = MibTableColumn
cucsSysdebugMEpLogOperState = _CucsSysdebugMEpLogOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 13, 1, 8),
    _CucsSysdebugMEpLogOperState_Type()
)
cucsSysdebugMEpLogOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogOperState.setStatus("current")
_CucsSysdebugMEpLogType_Type = CucsSysdebugEpLogType
_CucsSysdebugMEpLogType_Object = MibTableColumn
cucsSysdebugMEpLogType = _CucsSysdebugMEpLogType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 13, 1, 9),
    _CucsSysdebugMEpLogType_Type()
)
cucsSysdebugMEpLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogType.setStatus("current")
_CucsSysdebugMEpLogPolicyTable_Object = MibTable
cucsSysdebugMEpLogPolicyTable = _CucsSysdebugMEpLogPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 14)
)
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogPolicyTable.setStatus("current")
_CucsSysdebugMEpLogPolicyEntry_Object = MibTableRow
cucsSysdebugMEpLogPolicyEntry = _CucsSysdebugMEpLogPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 14, 1)
)
cucsSysdebugMEpLogPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugMEpLogPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogPolicyEntry.setStatus("current")
_CucsSysdebugMEpLogPolicyInstanceId_Type = CucsManagedObjectId
_CucsSysdebugMEpLogPolicyInstanceId_Object = MibTableColumn
cucsSysdebugMEpLogPolicyInstanceId = _CucsSysdebugMEpLogPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 14, 1, 1),
    _CucsSysdebugMEpLogPolicyInstanceId_Type()
)
cucsSysdebugMEpLogPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogPolicyInstanceId.setStatus("current")
_CucsSysdebugMEpLogPolicyDn_Type = CucsManagedObjectDn
_CucsSysdebugMEpLogPolicyDn_Object = MibTableColumn
cucsSysdebugMEpLogPolicyDn = _CucsSysdebugMEpLogPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 14, 1, 2),
    _CucsSysdebugMEpLogPolicyDn_Type()
)
cucsSysdebugMEpLogPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogPolicyDn.setStatus("current")
_CucsSysdebugMEpLogPolicyRn_Type = SnmpAdminString
_CucsSysdebugMEpLogPolicyRn_Object = MibTableColumn
cucsSysdebugMEpLogPolicyRn = _CucsSysdebugMEpLogPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 14, 1, 3),
    _CucsSysdebugMEpLogPolicyRn_Type()
)
cucsSysdebugMEpLogPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogPolicyRn.setStatus("current")
_CucsSysdebugMEpLogPolicyDescr_Type = SnmpAdminString
_CucsSysdebugMEpLogPolicyDescr_Object = MibTableColumn
cucsSysdebugMEpLogPolicyDescr = _CucsSysdebugMEpLogPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 14, 1, 4),
    _CucsSysdebugMEpLogPolicyDescr_Type()
)
cucsSysdebugMEpLogPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogPolicyDescr.setStatus("current")
_CucsSysdebugMEpLogPolicyIntId_Type = SnmpAdminString
_CucsSysdebugMEpLogPolicyIntId_Object = MibTableColumn
cucsSysdebugMEpLogPolicyIntId = _CucsSysdebugMEpLogPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 14, 1, 5),
    _CucsSysdebugMEpLogPolicyIntId_Type()
)
cucsSysdebugMEpLogPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogPolicyIntId.setStatus("current")
_CucsSysdebugMEpLogPolicyName_Type = SnmpAdminString
_CucsSysdebugMEpLogPolicyName_Object = MibTableColumn
cucsSysdebugMEpLogPolicyName = _CucsSysdebugMEpLogPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 14, 1, 6),
    _CucsSysdebugMEpLogPolicyName_Type()
)
cucsSysdebugMEpLogPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogPolicyName.setStatus("current")
_CucsSysdebugMEpLogPolicyType_Type = CucsSysdebugEpLogType
_CucsSysdebugMEpLogPolicyType_Object = MibTableColumn
cucsSysdebugMEpLogPolicyType = _CucsSysdebugMEpLogPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 14, 1, 7),
    _CucsSysdebugMEpLogPolicyType_Type()
)
cucsSysdebugMEpLogPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogPolicyType.setStatus("current")
_CucsSysdebugMEpLogPolicyPolicyLevel_Type = Gauge32
_CucsSysdebugMEpLogPolicyPolicyLevel_Object = MibTableColumn
cucsSysdebugMEpLogPolicyPolicyLevel = _CucsSysdebugMEpLogPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 14, 1, 8),
    _CucsSysdebugMEpLogPolicyPolicyLevel_Type()
)
cucsSysdebugMEpLogPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogPolicyPolicyLevel.setStatus("current")
_CucsSysdebugMEpLogPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsSysdebugMEpLogPolicyPolicyOwner_Object = MibTableColumn
cucsSysdebugMEpLogPolicyPolicyOwner = _CucsSysdebugMEpLogPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 14, 1, 9),
    _CucsSysdebugMEpLogPolicyPolicyOwner_Type()
)
cucsSysdebugMEpLogPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugMEpLogPolicyPolicyOwner.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetTable_Object = MibTable
cucsSysdebugManualCoreFileExportTargetTable = _CucsSysdebugManualCoreFileExportTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15)
)
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetTable.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetEntry_Object = MibTableRow
cucsSysdebugManualCoreFileExportTargetEntry = _CucsSysdebugManualCoreFileExportTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1)
)
cucsSysdebugManualCoreFileExportTargetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugManualCoreFileExportTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetEntry.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetInstanceId_Type = CucsManagedObjectId
_CucsSysdebugManualCoreFileExportTargetInstanceId_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetInstanceId = _CucsSysdebugManualCoreFileExportTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 1),
    _CucsSysdebugManualCoreFileExportTargetInstanceId_Type()
)
cucsSysdebugManualCoreFileExportTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetInstanceId.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetDn_Type = CucsManagedObjectDn
_CucsSysdebugManualCoreFileExportTargetDn_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetDn = _CucsSysdebugManualCoreFileExportTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 2),
    _CucsSysdebugManualCoreFileExportTargetDn_Type()
)
cucsSysdebugManualCoreFileExportTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetDn.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetRn_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetRn_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetRn = _CucsSysdebugManualCoreFileExportTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 3),
    _CucsSysdebugManualCoreFileExportTargetRn_Type()
)
cucsSysdebugManualCoreFileExportTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetRn.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetAdminState_Type = CucsSysdebugManualCoreFileExportTargetAdminState
_CucsSysdebugManualCoreFileExportTargetAdminState_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetAdminState = _CucsSysdebugManualCoreFileExportTargetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 4),
    _CucsSysdebugManualCoreFileExportTargetAdminState_Type()
)
cucsSysdebugManualCoreFileExportTargetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetAdminState.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetDescr_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetDescr_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetDescr = _CucsSysdebugManualCoreFileExportTargetDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 5),
    _CucsSysdebugManualCoreFileExportTargetDescr_Type()
)
cucsSysdebugManualCoreFileExportTargetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetDescr.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmDescr_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetFsmDescr_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmDescr = _CucsSysdebugManualCoreFileExportTargetFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 6),
    _CucsSysdebugManualCoreFileExportTargetFsmDescr_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmDescr.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmPrev_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetFsmPrev_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmPrev = _CucsSysdebugManualCoreFileExportTargetFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 7),
    _CucsSysdebugManualCoreFileExportTargetFsmPrev_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmPrev.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmProgr_Type = Gauge32
_CucsSysdebugManualCoreFileExportTargetFsmProgr_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmProgr = _CucsSysdebugManualCoreFileExportTargetFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 8),
    _CucsSysdebugManualCoreFileExportTargetFsmProgr_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmProgr.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmRmtInvErrCode_Type = Gauge32
_CucsSysdebugManualCoreFileExportTargetFsmRmtInvErrCode_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmRmtInvErrCode = _CucsSysdebugManualCoreFileExportTargetFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 9),
    _CucsSysdebugManualCoreFileExportTargetFsmRmtInvErrCode_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmRmtInvErrCode.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr = _CucsSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 10),
    _CucsSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSysdebugManualCoreFileExportTargetFsmRmtInvRslt_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmRmtInvRslt = _CucsSysdebugManualCoreFileExportTargetFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 11),
    _CucsSysdebugManualCoreFileExportTargetFsmRmtInvRslt_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmRmtInvRslt.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStageDescr_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetFsmStageDescr_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmStageDescr = _CucsSysdebugManualCoreFileExportTargetFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 12),
    _CucsSysdebugManualCoreFileExportTargetFsmStageDescr_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStageDescr.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStamp_Type = DateAndTime
_CucsSysdebugManualCoreFileExportTargetFsmStamp_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmStamp = _CucsSysdebugManualCoreFileExportTargetFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 13),
    _CucsSysdebugManualCoreFileExportTargetFsmStamp_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStamp.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStatus_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetFsmStatus_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmStatus = _CucsSysdebugManualCoreFileExportTargetFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 14),
    _CucsSysdebugManualCoreFileExportTargetFsmStatus_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStatus.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmTry_Type = Gauge32
_CucsSysdebugManualCoreFileExportTargetFsmTry_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmTry = _CucsSysdebugManualCoreFileExportTargetFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 15),
    _CucsSysdebugManualCoreFileExportTargetFsmTry_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmTry.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetHostname_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetHostname_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetHostname = _CucsSysdebugManualCoreFileExportTargetHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 16),
    _CucsSysdebugManualCoreFileExportTargetHostname_Type()
)
cucsSysdebugManualCoreFileExportTargetHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetHostname.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetIntId_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetIntId_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetIntId = _CucsSysdebugManualCoreFileExportTargetIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 17),
    _CucsSysdebugManualCoreFileExportTargetIntId_Type()
)
cucsSysdebugManualCoreFileExportTargetIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetIntId.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetName_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetName_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetName = _CucsSysdebugManualCoreFileExportTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 18),
    _CucsSysdebugManualCoreFileExportTargetName_Type()
)
cucsSysdebugManualCoreFileExportTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetName.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetPath_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetPath_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetPath = _CucsSysdebugManualCoreFileExportTargetPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 19),
    _CucsSysdebugManualCoreFileExportTargetPath_Type()
)
cucsSysdebugManualCoreFileExportTargetPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetPath.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetPort_Type = Gauge32
_CucsSysdebugManualCoreFileExportTargetPort_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetPort = _CucsSysdebugManualCoreFileExportTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 20),
    _CucsSysdebugManualCoreFileExportTargetPort_Type()
)
cucsSysdebugManualCoreFileExportTargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetPort.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetPostAction_Type = CucsSysfileExporterPostAction
_CucsSysdebugManualCoreFileExportTargetPostAction_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetPostAction = _CucsSysdebugManualCoreFileExportTargetPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 21),
    _CucsSysdebugManualCoreFileExportTargetPostAction_Type()
)
cucsSysdebugManualCoreFileExportTargetPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetPostAction.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetProto_Type = CucsSysdebugManualCoreFileExportTargetProto
_CucsSysdebugManualCoreFileExportTargetProto_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetProto = _CucsSysdebugManualCoreFileExportTargetProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 22),
    _CucsSysdebugManualCoreFileExportTargetProto_Type()
)
cucsSysdebugManualCoreFileExportTargetProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetProto.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetExportFailureReason_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetExportFailureReason_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetExportFailureReason = _CucsSysdebugManualCoreFileExportTargetExportFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 23),
    _CucsSysdebugManualCoreFileExportTargetExportFailureReason_Type()
)
cucsSysdebugManualCoreFileExportTargetExportFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetExportFailureReason.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetExportStatus_Type = CucsSysdebugCoreExportStatus
_CucsSysdebugManualCoreFileExportTargetExportStatus_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetExportStatus = _CucsSysdebugManualCoreFileExportTargetExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 24),
    _CucsSysdebugManualCoreFileExportTargetExportStatus_Type()
)
cucsSysdebugManualCoreFileExportTargetExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetExportStatus.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetPolicyLevel_Type = Gauge32
_CucsSysdebugManualCoreFileExportTargetPolicyLevel_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetPolicyLevel = _CucsSysdebugManualCoreFileExportTargetPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 25),
    _CucsSysdebugManualCoreFileExportTargetPolicyLevel_Type()
)
cucsSysdebugManualCoreFileExportTargetPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetPolicyLevel.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsSysdebugManualCoreFileExportTargetPolicyOwner_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetPolicyOwner = _CucsSysdebugManualCoreFileExportTargetPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 15, 1, 26),
    _CucsSysdebugManualCoreFileExportTargetPolicyOwner_Type()
)
cucsSysdebugManualCoreFileExportTargetPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetPolicyOwner.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmTaskTable_Object = MibTable
cucsSysdebugManualCoreFileExportTargetFsmTaskTable = _CucsSysdebugManualCoreFileExportTargetFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 16)
)
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmTaskTable.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmTaskEntry_Object = MibTableRow
cucsSysdebugManualCoreFileExportTargetFsmTaskEntry = _CucsSysdebugManualCoreFileExportTargetFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 16, 1)
)
cucsSysdebugManualCoreFileExportTargetFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugManualCoreFileExportTargetFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmTaskEntry.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSysdebugManualCoreFileExportTargetFsmTaskInstanceId_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmTaskInstanceId = _CucsSysdebugManualCoreFileExportTargetFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 16, 1, 1),
    _CucsSysdebugManualCoreFileExportTargetFsmTaskInstanceId_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmTaskInstanceId.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmTaskDn_Type = CucsManagedObjectDn
_CucsSysdebugManualCoreFileExportTargetFsmTaskDn_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmTaskDn = _CucsSysdebugManualCoreFileExportTargetFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 16, 1, 2),
    _CucsSysdebugManualCoreFileExportTargetFsmTaskDn_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmTaskDn.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmTaskRn_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetFsmTaskRn_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmTaskRn = _CucsSysdebugManualCoreFileExportTargetFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 16, 1, 3),
    _CucsSysdebugManualCoreFileExportTargetFsmTaskRn_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmTaskRn.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSysdebugManualCoreFileExportTargetFsmTaskCompletion_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmTaskCompletion = _CucsSysdebugManualCoreFileExportTargetFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 16, 1, 4),
    _CucsSysdebugManualCoreFileExportTargetFsmTaskCompletion_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmTaskCompletion.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmTaskFlags_Type = CucsFsmFlags
_CucsSysdebugManualCoreFileExportTargetFsmTaskFlags_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmTaskFlags = _CucsSysdebugManualCoreFileExportTargetFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 16, 1, 5),
    _CucsSysdebugManualCoreFileExportTargetFsmTaskFlags_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmTaskFlags.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmTaskItem_Type = CucsSysdebugManualCoreFileExportTargetFsmTaskItem
_CucsSysdebugManualCoreFileExportTargetFsmTaskItem_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmTaskItem = _CucsSysdebugManualCoreFileExportTargetFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 16, 1, 6),
    _CucsSysdebugManualCoreFileExportTargetFsmTaskItem_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmTaskItem.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmTaskSeqId_Type = Gauge32
_CucsSysdebugManualCoreFileExportTargetFsmTaskSeqId_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmTaskSeqId = _CucsSysdebugManualCoreFileExportTargetFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 16, 1, 7),
    _CucsSysdebugManualCoreFileExportTargetFsmTaskSeqId_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmTaskSeqId.setStatus("current")
_CucsSysdebugTechSupFileRepositoryTable_Object = MibTable
cucsSysdebugTechSupFileRepositoryTable = _CucsSysdebugTechSupFileRepositoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 17)
)
if mibBuilder.loadTexts:
    cucsSysdebugTechSupFileRepositoryTable.setStatus("current")
_CucsSysdebugTechSupFileRepositoryEntry_Object = MibTableRow
cucsSysdebugTechSupFileRepositoryEntry = _CucsSysdebugTechSupFileRepositoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 17, 1)
)
cucsSysdebugTechSupFileRepositoryEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugTechSupFileRepositoryInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugTechSupFileRepositoryEntry.setStatus("current")
_CucsSysdebugTechSupFileRepositoryInstanceId_Type = CucsManagedObjectId
_CucsSysdebugTechSupFileRepositoryInstanceId_Object = MibTableColumn
cucsSysdebugTechSupFileRepositoryInstanceId = _CucsSysdebugTechSupFileRepositoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 17, 1, 1),
    _CucsSysdebugTechSupFileRepositoryInstanceId_Type()
)
cucsSysdebugTechSupFileRepositoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupFileRepositoryInstanceId.setStatus("current")
_CucsSysdebugTechSupFileRepositoryDn_Type = CucsManagedObjectDn
_CucsSysdebugTechSupFileRepositoryDn_Object = MibTableColumn
cucsSysdebugTechSupFileRepositoryDn = _CucsSysdebugTechSupFileRepositoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 17, 1, 2),
    _CucsSysdebugTechSupFileRepositoryDn_Type()
)
cucsSysdebugTechSupFileRepositoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupFileRepositoryDn.setStatus("current")
_CucsSysdebugTechSupFileRepositoryRn_Type = SnmpAdminString
_CucsSysdebugTechSupFileRepositoryRn_Object = MibTableColumn
cucsSysdebugTechSupFileRepositoryRn = _CucsSysdebugTechSupFileRepositoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 17, 1, 3),
    _CucsSysdebugTechSupFileRepositoryRn_Type()
)
cucsSysdebugTechSupFileRepositoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupFileRepositoryRn.setStatus("current")
_CucsSysdebugTechSupportTable_Object = MibTable
cucsSysdebugTechSupportTable = _CucsSysdebugTechSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18)
)
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportTable.setStatus("current")
_CucsSysdebugTechSupportEntry_Object = MibTableRow
cucsSysdebugTechSupportEntry = _CucsSysdebugTechSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1)
)
cucsSysdebugTechSupportEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugTechSupportInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportEntry.setStatus("current")
_CucsSysdebugTechSupportInstanceId_Type = CucsManagedObjectId
_CucsSysdebugTechSupportInstanceId_Object = MibTableColumn
cucsSysdebugTechSupportInstanceId = _CucsSysdebugTechSupportInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 1),
    _CucsSysdebugTechSupportInstanceId_Type()
)
cucsSysdebugTechSupportInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportInstanceId.setStatus("current")
_CucsSysdebugTechSupportDn_Type = CucsManagedObjectDn
_CucsSysdebugTechSupportDn_Object = MibTableColumn
cucsSysdebugTechSupportDn = _CucsSysdebugTechSupportDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 2),
    _CucsSysdebugTechSupportDn_Type()
)
cucsSysdebugTechSupportDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportDn.setStatus("current")
_CucsSysdebugTechSupportRn_Type = SnmpAdminString
_CucsSysdebugTechSupportRn_Object = MibTableColumn
cucsSysdebugTechSupportRn = _CucsSysdebugTechSupportRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 3),
    _CucsSysdebugTechSupportRn_Type()
)
cucsSysdebugTechSupportRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportRn.setStatus("current")
_CucsSysdebugTechSupportAdminState_Type = CucsSysdebugTechSupportAdminState
_CucsSysdebugTechSupportAdminState_Object = MibTableColumn
cucsSysdebugTechSupportAdminState = _CucsSysdebugTechSupportAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 4),
    _CucsSysdebugTechSupportAdminState_Type()
)
cucsSysdebugTechSupportAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportAdminState.setStatus("current")
_CucsSysdebugTechSupportDescr_Type = SnmpAdminString
_CucsSysdebugTechSupportDescr_Object = MibTableColumn
cucsSysdebugTechSupportDescr = _CucsSysdebugTechSupportDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 5),
    _CucsSysdebugTechSupportDescr_Type()
)
cucsSysdebugTechSupportDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportDescr.setStatus("current")
_CucsSysdebugTechSupportFsmDescr_Type = SnmpAdminString
_CucsSysdebugTechSupportFsmDescr_Object = MibTableColumn
cucsSysdebugTechSupportFsmDescr = _CucsSysdebugTechSupportFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 6),
    _CucsSysdebugTechSupportFsmDescr_Type()
)
cucsSysdebugTechSupportFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmDescr.setStatus("current")
_CucsSysdebugTechSupportFsmPrev_Type = SnmpAdminString
_CucsSysdebugTechSupportFsmPrev_Object = MibTableColumn
cucsSysdebugTechSupportFsmPrev = _CucsSysdebugTechSupportFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 7),
    _CucsSysdebugTechSupportFsmPrev_Type()
)
cucsSysdebugTechSupportFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmPrev.setStatus("current")
_CucsSysdebugTechSupportFsmProgr_Type = Gauge32
_CucsSysdebugTechSupportFsmProgr_Object = MibTableColumn
cucsSysdebugTechSupportFsmProgr = _CucsSysdebugTechSupportFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 8),
    _CucsSysdebugTechSupportFsmProgr_Type()
)
cucsSysdebugTechSupportFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmProgr.setStatus("current")
_CucsSysdebugTechSupportFsmRmtInvErrCode_Type = Gauge32
_CucsSysdebugTechSupportFsmRmtInvErrCode_Object = MibTableColumn
cucsSysdebugTechSupportFsmRmtInvErrCode = _CucsSysdebugTechSupportFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 9),
    _CucsSysdebugTechSupportFsmRmtInvErrCode_Type()
)
cucsSysdebugTechSupportFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmRmtInvErrCode.setStatus("current")
_CucsSysdebugTechSupportFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSysdebugTechSupportFsmRmtInvErrDescr_Object = MibTableColumn
cucsSysdebugTechSupportFsmRmtInvErrDescr = _CucsSysdebugTechSupportFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 10),
    _CucsSysdebugTechSupportFsmRmtInvErrDescr_Type()
)
cucsSysdebugTechSupportFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmRmtInvErrDescr.setStatus("current")
_CucsSysdebugTechSupportFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSysdebugTechSupportFsmRmtInvRslt_Object = MibTableColumn
cucsSysdebugTechSupportFsmRmtInvRslt = _CucsSysdebugTechSupportFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 11),
    _CucsSysdebugTechSupportFsmRmtInvRslt_Type()
)
cucsSysdebugTechSupportFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmRmtInvRslt.setStatus("current")
_CucsSysdebugTechSupportFsmStageDescr_Type = SnmpAdminString
_CucsSysdebugTechSupportFsmStageDescr_Object = MibTableColumn
cucsSysdebugTechSupportFsmStageDescr = _CucsSysdebugTechSupportFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 12),
    _CucsSysdebugTechSupportFsmStageDescr_Type()
)
cucsSysdebugTechSupportFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStageDescr.setStatus("current")
_CucsSysdebugTechSupportFsmStamp_Type = DateAndTime
_CucsSysdebugTechSupportFsmStamp_Object = MibTableColumn
cucsSysdebugTechSupportFsmStamp = _CucsSysdebugTechSupportFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 13),
    _CucsSysdebugTechSupportFsmStamp_Type()
)
cucsSysdebugTechSupportFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStamp.setStatus("current")
_CucsSysdebugTechSupportFsmStatus_Type = SnmpAdminString
_CucsSysdebugTechSupportFsmStatus_Object = MibTableColumn
cucsSysdebugTechSupportFsmStatus = _CucsSysdebugTechSupportFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 14),
    _CucsSysdebugTechSupportFsmStatus_Type()
)
cucsSysdebugTechSupportFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStatus.setStatus("current")
_CucsSysdebugTechSupportFsmTry_Type = Gauge32
_CucsSysdebugTechSupportFsmTry_Object = MibTableColumn
cucsSysdebugTechSupportFsmTry = _CucsSysdebugTechSupportFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 15),
    _CucsSysdebugTechSupportFsmTry_Type()
)
cucsSysdebugTechSupportFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmTry.setStatus("current")
_CucsSysdebugTechSupportName_Type = SnmpAdminString
_CucsSysdebugTechSupportName_Object = MibTableColumn
cucsSysdebugTechSupportName = _CucsSysdebugTechSupportName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 16),
    _CucsSysdebugTechSupportName_Type()
)
cucsSysdebugTechSupportName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportName.setStatus("current")
_CucsSysdebugTechSupportOperState_Type = CucsSysdebugTechSupportOperState
_CucsSysdebugTechSupportOperState_Object = MibTableColumn
cucsSysdebugTechSupportOperState = _CucsSysdebugTechSupportOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 17),
    _CucsSysdebugTechSupportOperState_Type()
)
cucsSysdebugTechSupportOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportOperState.setStatus("current")
_CucsSysdebugTechSupportSize_Type = Gauge32
_CucsSysdebugTechSupportSize_Object = MibTableColumn
cucsSysdebugTechSupportSize = _CucsSysdebugTechSupportSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 18),
    _CucsSysdebugTechSupportSize_Type()
)
cucsSysdebugTechSupportSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportSize.setStatus("current")
_CucsSysdebugTechSupportSwitchId_Type = CucsNetworkSwitchId
_CucsSysdebugTechSupportSwitchId_Object = MibTableColumn
cucsSysdebugTechSupportSwitchId = _CucsSysdebugTechSupportSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 19),
    _CucsSysdebugTechSupportSwitchId_Type()
)
cucsSysdebugTechSupportSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportSwitchId.setStatus("current")
_CucsSysdebugTechSupportTs_Type = DateAndTime
_CucsSysdebugTechSupportTs_Object = MibTableColumn
cucsSysdebugTechSupportTs = _CucsSysdebugTechSupportTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 20),
    _CucsSysdebugTechSupportTs_Type()
)
cucsSysdebugTechSupportTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportTs.setStatus("current")
_CucsSysdebugTechSupportUri_Type = SnmpAdminString
_CucsSysdebugTechSupportUri_Object = MibTableColumn
cucsSysdebugTechSupportUri = _CucsSysdebugTechSupportUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 21),
    _CucsSysdebugTechSupportUri_Type()
)
cucsSysdebugTechSupportUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportUri.setStatus("current")
_CucsSysdebugTechSupportCreationTS_Type = Unsigned64
_CucsSysdebugTechSupportCreationTS_Object = MibTableColumn
cucsSysdebugTechSupportCreationTS = _CucsSysdebugTechSupportCreationTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 18, 1, 22),
    _CucsSysdebugTechSupportCreationTS_Type()
)
cucsSysdebugTechSupportCreationTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCreationTS.setStatus("current")
_CucsSysdebugTechSupportCmdOptTable_Object = MibTable
cucsSysdebugTechSupportCmdOptTable = _CucsSysdebugTechSupportCmdOptTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19)
)
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptTable.setStatus("current")
_CucsSysdebugTechSupportCmdOptEntry_Object = MibTableRow
cucsSysdebugTechSupportCmdOptEntry = _CucsSysdebugTechSupportCmdOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1)
)
cucsSysdebugTechSupportCmdOptEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugTechSupportCmdOptInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptEntry.setStatus("current")
_CucsSysdebugTechSupportCmdOptInstanceId_Type = CucsManagedObjectId
_CucsSysdebugTechSupportCmdOptInstanceId_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptInstanceId = _CucsSysdebugTechSupportCmdOptInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 1),
    _CucsSysdebugTechSupportCmdOptInstanceId_Type()
)
cucsSysdebugTechSupportCmdOptInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptInstanceId.setStatus("current")
_CucsSysdebugTechSupportCmdOptDn_Type = CucsManagedObjectDn
_CucsSysdebugTechSupportCmdOptDn_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptDn = _CucsSysdebugTechSupportCmdOptDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 2),
    _CucsSysdebugTechSupportCmdOptDn_Type()
)
cucsSysdebugTechSupportCmdOptDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptDn.setStatus("current")
_CucsSysdebugTechSupportCmdOptRn_Type = SnmpAdminString
_CucsSysdebugTechSupportCmdOptRn_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptRn = _CucsSysdebugTechSupportCmdOptRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 3),
    _CucsSysdebugTechSupportCmdOptRn_Type()
)
cucsSysdebugTechSupportCmdOptRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptRn.setStatus("current")
_CucsSysdebugTechSupportCmdOptChassisCimcId_Type = Gauge32
_CucsSysdebugTechSupportCmdOptChassisCimcId_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptChassisCimcId = _CucsSysdebugTechSupportCmdOptChassisCimcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 4),
    _CucsSysdebugTechSupportCmdOptChassisCimcId_Type()
)
cucsSysdebugTechSupportCmdOptChassisCimcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptChassisCimcId.setStatus("current")
_CucsSysdebugTechSupportCmdOptChassisId_Type = Gauge32
_CucsSysdebugTechSupportCmdOptChassisId_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptChassisId = _CucsSysdebugTechSupportCmdOptChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 5),
    _CucsSysdebugTechSupportCmdOptChassisId_Type()
)
cucsSysdebugTechSupportCmdOptChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptChassisId.setStatus("current")
_CucsSysdebugTechSupportCmdOptChassisIomId_Type = Gauge32
_CucsSysdebugTechSupportCmdOptChassisIomId_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptChassisIomId = _CucsSysdebugTechSupportCmdOptChassisIomId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 6),
    _CucsSysdebugTechSupportCmdOptChassisIomId_Type()
)
cucsSysdebugTechSupportCmdOptChassisIomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptChassisIomId.setStatus("current")
_CucsSysdebugTechSupportCmdOptCimcAdapterId_Type = Gauge32
_CucsSysdebugTechSupportCmdOptCimcAdapterId_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptCimcAdapterId = _CucsSysdebugTechSupportCmdOptCimcAdapterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 7),
    _CucsSysdebugTechSupportCmdOptCimcAdapterId_Type()
)
cucsSysdebugTechSupportCmdOptCimcAdapterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptCimcAdapterId.setStatus("current")
_CucsSysdebugTechSupportCmdOptFabExtId_Type = Gauge32
_CucsSysdebugTechSupportCmdOptFabExtId_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptFabExtId = _CucsSysdebugTechSupportCmdOptFabExtId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 8),
    _CucsSysdebugTechSupportCmdOptFabExtId_Type()
)
cucsSysdebugTechSupportCmdOptFabExtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptFabExtId.setStatus("current")
_CucsSysdebugTechSupportCmdOptMajorOptType_Type = CucsSysdebugTSCmdOptMajorType
_CucsSysdebugTechSupportCmdOptMajorOptType_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptMajorOptType = _CucsSysdebugTechSupportCmdOptMajorOptType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 9),
    _CucsSysdebugTechSupportCmdOptMajorOptType_Type()
)
cucsSysdebugTechSupportCmdOptMajorOptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptMajorOptType.setStatus("current")
_CucsSysdebugTechSupportCmdOptRackServerAdapterId_Type = Gauge32
_CucsSysdebugTechSupportCmdOptRackServerAdapterId_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptRackServerAdapterId = _CucsSysdebugTechSupportCmdOptRackServerAdapterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 10),
    _CucsSysdebugTechSupportCmdOptRackServerAdapterId_Type()
)
cucsSysdebugTechSupportCmdOptRackServerAdapterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptRackServerAdapterId.setStatus("current")
_CucsSysdebugTechSupportCmdOptRackServerId_Type = Gauge32
_CucsSysdebugTechSupportCmdOptRackServerId_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptRackServerId = _CucsSysdebugTechSupportCmdOptRackServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 11),
    _CucsSysdebugTechSupportCmdOptRackServerId_Type()
)
cucsSysdebugTechSupportCmdOptRackServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptRackServerId.setStatus("current")
_CucsSysdebugTechSupportCmdOptCartridgeCIMCId_Type = Gauge32
_CucsSysdebugTechSupportCmdOptCartridgeCIMCId_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptCartridgeCIMCId = _CucsSysdebugTechSupportCmdOptCartridgeCIMCId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 13),
    _CucsSysdebugTechSupportCmdOptCartridgeCIMCId_Type()
)
cucsSysdebugTechSupportCmdOptCartridgeCIMCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptCartridgeCIMCId.setStatus("current")
_CucsSysdebugTechSupportCmdOptChassisCartridgeId_Type = Gauge32
_CucsSysdebugTechSupportCmdOptChassisCartridgeId_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptChassisCartridgeId = _CucsSysdebugTechSupportCmdOptChassisCartridgeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 14),
    _CucsSysdebugTechSupportCmdOptChassisCartridgeId_Type()
)
cucsSysdebugTechSupportCmdOptChassisCartridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptChassisCartridgeId.setStatus("current")
_CucsSysdebugTechSupportCmdOptServerIdList_Type = SnmpAdminString
_CucsSysdebugTechSupportCmdOptServerIdList_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptServerIdList = _CucsSysdebugTechSupportCmdOptServerIdList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 15),
    _CucsSysdebugTechSupportCmdOptServerIdList_Type()
)
cucsSysdebugTechSupportCmdOptServerIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptServerIdList.setStatus("current")
_CucsSysdebugTechSupportCmdOptCommandOptions_Type = CucsSysdebugTSCmdOptCmdOptions
_CucsSysdebugTechSupportCmdOptCommandOptions_Object = MibTableColumn
cucsSysdebugTechSupportCmdOptCommandOptions = _CucsSysdebugTechSupportCmdOptCommandOptions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 19, 1, 18),
    _CucsSysdebugTechSupportCmdOptCommandOptions_Type()
)
cucsSysdebugTechSupportCmdOptCommandOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportCmdOptCommandOptions.setStatus("current")
_CucsSysdebugTechSupportFsmTaskTable_Object = MibTable
cucsSysdebugTechSupportFsmTaskTable = _CucsSysdebugTechSupportFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 20)
)
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmTaskTable.setStatus("current")
_CucsSysdebugTechSupportFsmTaskEntry_Object = MibTableRow
cucsSysdebugTechSupportFsmTaskEntry = _CucsSysdebugTechSupportFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 20, 1)
)
cucsSysdebugTechSupportFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugTechSupportFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmTaskEntry.setStatus("current")
_CucsSysdebugTechSupportFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSysdebugTechSupportFsmTaskInstanceId_Object = MibTableColumn
cucsSysdebugTechSupportFsmTaskInstanceId = _CucsSysdebugTechSupportFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 20, 1, 1),
    _CucsSysdebugTechSupportFsmTaskInstanceId_Type()
)
cucsSysdebugTechSupportFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmTaskInstanceId.setStatus("current")
_CucsSysdebugTechSupportFsmTaskDn_Type = CucsManagedObjectDn
_CucsSysdebugTechSupportFsmTaskDn_Object = MibTableColumn
cucsSysdebugTechSupportFsmTaskDn = _CucsSysdebugTechSupportFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 20, 1, 2),
    _CucsSysdebugTechSupportFsmTaskDn_Type()
)
cucsSysdebugTechSupportFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmTaskDn.setStatus("current")
_CucsSysdebugTechSupportFsmTaskRn_Type = SnmpAdminString
_CucsSysdebugTechSupportFsmTaskRn_Object = MibTableColumn
cucsSysdebugTechSupportFsmTaskRn = _CucsSysdebugTechSupportFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 20, 1, 3),
    _CucsSysdebugTechSupportFsmTaskRn_Type()
)
cucsSysdebugTechSupportFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmTaskRn.setStatus("current")
_CucsSysdebugTechSupportFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSysdebugTechSupportFsmTaskCompletion_Object = MibTableColumn
cucsSysdebugTechSupportFsmTaskCompletion = _CucsSysdebugTechSupportFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 20, 1, 4),
    _CucsSysdebugTechSupportFsmTaskCompletion_Type()
)
cucsSysdebugTechSupportFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmTaskCompletion.setStatus("current")
_CucsSysdebugTechSupportFsmTaskFlags_Type = CucsFsmFlags
_CucsSysdebugTechSupportFsmTaskFlags_Object = MibTableColumn
cucsSysdebugTechSupportFsmTaskFlags = _CucsSysdebugTechSupportFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 20, 1, 5),
    _CucsSysdebugTechSupportFsmTaskFlags_Type()
)
cucsSysdebugTechSupportFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmTaskFlags.setStatus("current")
_CucsSysdebugTechSupportFsmTaskItem_Type = CucsSysdebugTechSupportFsmTaskItem
_CucsSysdebugTechSupportFsmTaskItem_Object = MibTableColumn
cucsSysdebugTechSupportFsmTaskItem = _CucsSysdebugTechSupportFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 20, 1, 6),
    _CucsSysdebugTechSupportFsmTaskItem_Type()
)
cucsSysdebugTechSupportFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmTaskItem.setStatus("current")
_CucsSysdebugTechSupportFsmTaskSeqId_Type = Gauge32
_CucsSysdebugTechSupportFsmTaskSeqId_Object = MibTableColumn
cucsSysdebugTechSupportFsmTaskSeqId = _CucsSysdebugTechSupportFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 20, 1, 7),
    _CucsSysdebugTechSupportFsmTaskSeqId_Type()
)
cucsSysdebugTechSupportFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmTaskSeqId.setStatus("current")
_CucsSysdebugCoreFsmTaskTable_Object = MibTable
cucsSysdebugCoreFsmTaskTable = _CucsSysdebugCoreFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 21)
)
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmTaskTable.setStatus("current")
_CucsSysdebugCoreFsmTaskEntry_Object = MibTableRow
cucsSysdebugCoreFsmTaskEntry = _CucsSysdebugCoreFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 21, 1)
)
cucsSysdebugCoreFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugCoreFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmTaskEntry.setStatus("current")
_CucsSysdebugCoreFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSysdebugCoreFsmTaskInstanceId_Object = MibTableColumn
cucsSysdebugCoreFsmTaskInstanceId = _CucsSysdebugCoreFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 21, 1, 1),
    _CucsSysdebugCoreFsmTaskInstanceId_Type()
)
cucsSysdebugCoreFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmTaskInstanceId.setStatus("current")
_CucsSysdebugCoreFsmTaskDn_Type = CucsManagedObjectDn
_CucsSysdebugCoreFsmTaskDn_Object = MibTableColumn
cucsSysdebugCoreFsmTaskDn = _CucsSysdebugCoreFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 21, 1, 2),
    _CucsSysdebugCoreFsmTaskDn_Type()
)
cucsSysdebugCoreFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmTaskDn.setStatus("current")
_CucsSysdebugCoreFsmTaskRn_Type = SnmpAdminString
_CucsSysdebugCoreFsmTaskRn_Object = MibTableColumn
cucsSysdebugCoreFsmTaskRn = _CucsSysdebugCoreFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 21, 1, 3),
    _CucsSysdebugCoreFsmTaskRn_Type()
)
cucsSysdebugCoreFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmTaskRn.setStatus("current")
_CucsSysdebugCoreFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSysdebugCoreFsmTaskCompletion_Object = MibTableColumn
cucsSysdebugCoreFsmTaskCompletion = _CucsSysdebugCoreFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 21, 1, 4),
    _CucsSysdebugCoreFsmTaskCompletion_Type()
)
cucsSysdebugCoreFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmTaskCompletion.setStatus("current")
_CucsSysdebugCoreFsmTaskFlags_Type = CucsFsmFlags
_CucsSysdebugCoreFsmTaskFlags_Object = MibTableColumn
cucsSysdebugCoreFsmTaskFlags = _CucsSysdebugCoreFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 21, 1, 5),
    _CucsSysdebugCoreFsmTaskFlags_Type()
)
cucsSysdebugCoreFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmTaskFlags.setStatus("current")
_CucsSysdebugCoreFsmTaskItem_Type = CucsSysdebugCoreFsmTaskItem
_CucsSysdebugCoreFsmTaskItem_Object = MibTableColumn
cucsSysdebugCoreFsmTaskItem = _CucsSysdebugCoreFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 21, 1, 6),
    _CucsSysdebugCoreFsmTaskItem_Type()
)
cucsSysdebugCoreFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmTaskItem.setStatus("current")
_CucsSysdebugCoreFsmTaskSeqId_Type = Gauge32
_CucsSysdebugCoreFsmTaskSeqId_Object = MibTableColumn
cucsSysdebugCoreFsmTaskSeqId = _CucsSysdebugCoreFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 21, 1, 7),
    _CucsSysdebugCoreFsmTaskSeqId_Type()
)
cucsSysdebugCoreFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmTaskSeqId.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmTable_Object = MibTable
cucsSysdebugAutoCoreFileExportTargetFsmTable = _CucsSysdebugAutoCoreFileExportTargetFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22)
)
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmTable.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmEntry_Object = MibTableRow
cucsSysdebugAutoCoreFileExportTargetFsmEntry = _CucsSysdebugAutoCoreFileExportTargetFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22, 1)
)
cucsSysdebugAutoCoreFileExportTargetFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugAutoCoreFileExportTargetFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmEntry.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmInstanceId_Type = CucsManagedObjectId
_CucsSysdebugAutoCoreFileExportTargetFsmInstanceId_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmInstanceId = _CucsSysdebugAutoCoreFileExportTargetFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22, 1, 1),
    _CucsSysdebugAutoCoreFileExportTargetFsmInstanceId_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmInstanceId.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmDn_Type = CucsManagedObjectDn
_CucsSysdebugAutoCoreFileExportTargetFsmDn_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmDn = _CucsSysdebugAutoCoreFileExportTargetFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22, 1, 2),
    _CucsSysdebugAutoCoreFileExportTargetFsmDn_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmDn.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmRn_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetFsmRn_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmRn = _CucsSysdebugAutoCoreFileExportTargetFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22, 1, 3),
    _CucsSysdebugAutoCoreFileExportTargetFsmRn_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmRn.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmCompletionTime_Type = DateAndTime
_CucsSysdebugAutoCoreFileExportTargetFsmCompletionTime_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmCompletionTime = _CucsSysdebugAutoCoreFileExportTargetFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22, 1, 4),
    _CucsSysdebugAutoCoreFileExportTargetFsmCompletionTime_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmCompletionTime.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm_Type = CucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm
_CucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm = _CucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22, 1, 5),
    _CucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmDescrData_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetFsmDescrData_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmDescrData = _CucsSysdebugAutoCoreFileExportTargetFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22, 1, 6),
    _CucsSysdebugAutoCoreFileExportTargetFsmDescrData_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmDescrData.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSysdebugAutoCoreFileExportTargetFsmFsmStatus_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmFsmStatus = _CucsSysdebugAutoCoreFileExportTargetFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22, 1, 7),
    _CucsSysdebugAutoCoreFileExportTargetFsmFsmStatus_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmFsmStatus.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmProgress_Type = Gauge32
_CucsSysdebugAutoCoreFileExportTargetFsmProgress_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmProgress = _CucsSysdebugAutoCoreFileExportTargetFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22, 1, 8),
    _CucsSysdebugAutoCoreFileExportTargetFsmProgress_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmProgress.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmRmtErrCode_Type = Gauge32
_CucsSysdebugAutoCoreFileExportTargetFsmRmtErrCode_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmRmtErrCode = _CucsSysdebugAutoCoreFileExportTargetFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22, 1, 9),
    _CucsSysdebugAutoCoreFileExportTargetFsmRmtErrCode_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmRmtErrCode.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmRmtErrDescr_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetFsmRmtErrDescr_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmRmtErrDescr = _CucsSysdebugAutoCoreFileExportTargetFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22, 1, 10),
    _CucsSysdebugAutoCoreFileExportTargetFsmRmtErrDescr_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmRmtErrDescr.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSysdebugAutoCoreFileExportTargetFsmRmtRslt_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmRmtRslt = _CucsSysdebugAutoCoreFileExportTargetFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 22, 1, 11),
    _CucsSysdebugAutoCoreFileExportTargetFsmRmtRslt_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmRmtRslt.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStageTable_Object = MibTable
cucsSysdebugAutoCoreFileExportTargetFsmStageTable = _CucsSysdebugAutoCoreFileExportTargetFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 23)
)
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStageTable.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStageEntry_Object = MibTableRow
cucsSysdebugAutoCoreFileExportTargetFsmStageEntry = _CucsSysdebugAutoCoreFileExportTargetFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 23, 1)
)
cucsSysdebugAutoCoreFileExportTargetFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugAutoCoreFileExportTargetFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStageEntry.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSysdebugAutoCoreFileExportTargetFsmStageInstanceId_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmStageInstanceId = _CucsSysdebugAutoCoreFileExportTargetFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 23, 1, 1),
    _CucsSysdebugAutoCoreFileExportTargetFsmStageInstanceId_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStageInstanceId.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStageDn_Type = CucsManagedObjectDn
_CucsSysdebugAutoCoreFileExportTargetFsmStageDn_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmStageDn = _CucsSysdebugAutoCoreFileExportTargetFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 23, 1, 2),
    _CucsSysdebugAutoCoreFileExportTargetFsmStageDn_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStageDn.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStageRn_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetFsmStageRn_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmStageRn = _CucsSysdebugAutoCoreFileExportTargetFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 23, 1, 3),
    _CucsSysdebugAutoCoreFileExportTargetFsmStageRn_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStageRn.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStageDescrData_Type = SnmpAdminString
_CucsSysdebugAutoCoreFileExportTargetFsmStageDescrData_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmStageDescrData = _CucsSysdebugAutoCoreFileExportTargetFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 23, 1, 4),
    _CucsSysdebugAutoCoreFileExportTargetFsmStageDescrData_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStageDescrData.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime_Type = DateAndTime
_CucsSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime = _CucsSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 23, 1, 5),
    _CucsSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStageName_Type = CucsSysdebugAutoCoreFileExportTargetFsmStageName
_CucsSysdebugAutoCoreFileExportTargetFsmStageName_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmStageName = _CucsSysdebugAutoCoreFileExportTargetFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 23, 1, 6),
    _CucsSysdebugAutoCoreFileExportTargetFsmStageName_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStageName.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStageOrder_Type = Gauge32
_CucsSysdebugAutoCoreFileExportTargetFsmStageOrder_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmStageOrder = _CucsSysdebugAutoCoreFileExportTargetFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 23, 1, 7),
    _CucsSysdebugAutoCoreFileExportTargetFsmStageOrder_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStageOrder.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStageRetry_Type = Gauge32
_CucsSysdebugAutoCoreFileExportTargetFsmStageRetry_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmStageRetry = _CucsSysdebugAutoCoreFileExportTargetFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 23, 1, 8),
    _CucsSysdebugAutoCoreFileExportTargetFsmStageRetry_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStageRetry.setStatus("current")
_CucsSysdebugAutoCoreFileExportTargetFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSysdebugAutoCoreFileExportTargetFsmStageStageStatus_Object = MibTableColumn
cucsSysdebugAutoCoreFileExportTargetFsmStageStageStatus = _CucsSysdebugAutoCoreFileExportTargetFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 23, 1, 9),
    _CucsSysdebugAutoCoreFileExportTargetFsmStageStageStatus_Type()
)
cucsSysdebugAutoCoreFileExportTargetFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugAutoCoreFileExportTargetFsmStageStageStatus.setStatus("current")
_CucsSysdebugCoreFsmTable_Object = MibTable
cucsSysdebugCoreFsmTable = _CucsSysdebugCoreFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24)
)
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmTable.setStatus("current")
_CucsSysdebugCoreFsmEntry_Object = MibTableRow
cucsSysdebugCoreFsmEntry = _CucsSysdebugCoreFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24, 1)
)
cucsSysdebugCoreFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugCoreFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmEntry.setStatus("current")
_CucsSysdebugCoreFsmInstanceId_Type = CucsManagedObjectId
_CucsSysdebugCoreFsmInstanceId_Object = MibTableColumn
cucsSysdebugCoreFsmInstanceId = _CucsSysdebugCoreFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24, 1, 1),
    _CucsSysdebugCoreFsmInstanceId_Type()
)
cucsSysdebugCoreFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmInstanceId.setStatus("current")
_CucsSysdebugCoreFsmDn_Type = CucsManagedObjectDn
_CucsSysdebugCoreFsmDn_Object = MibTableColumn
cucsSysdebugCoreFsmDn = _CucsSysdebugCoreFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24, 1, 2),
    _CucsSysdebugCoreFsmDn_Type()
)
cucsSysdebugCoreFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmDn.setStatus("current")
_CucsSysdebugCoreFsmRn_Type = SnmpAdminString
_CucsSysdebugCoreFsmRn_Object = MibTableColumn
cucsSysdebugCoreFsmRn = _CucsSysdebugCoreFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24, 1, 3),
    _CucsSysdebugCoreFsmRn_Type()
)
cucsSysdebugCoreFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmRn.setStatus("current")
_CucsSysdebugCoreFsmCompletionTime_Type = DateAndTime
_CucsSysdebugCoreFsmCompletionTime_Object = MibTableColumn
cucsSysdebugCoreFsmCompletionTime = _CucsSysdebugCoreFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24, 1, 4),
    _CucsSysdebugCoreFsmCompletionTime_Type()
)
cucsSysdebugCoreFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmCompletionTime.setStatus("current")
_CucsSysdebugCoreFsmCurrentFsm_Type = CucsSysdebugCoreFsmCurrentFsm
_CucsSysdebugCoreFsmCurrentFsm_Object = MibTableColumn
cucsSysdebugCoreFsmCurrentFsm = _CucsSysdebugCoreFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24, 1, 5),
    _CucsSysdebugCoreFsmCurrentFsm_Type()
)
cucsSysdebugCoreFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmCurrentFsm.setStatus("current")
_CucsSysdebugCoreFsmDescrData_Type = SnmpAdminString
_CucsSysdebugCoreFsmDescrData_Object = MibTableColumn
cucsSysdebugCoreFsmDescrData = _CucsSysdebugCoreFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24, 1, 6),
    _CucsSysdebugCoreFsmDescrData_Type()
)
cucsSysdebugCoreFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmDescrData.setStatus("current")
_CucsSysdebugCoreFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSysdebugCoreFsmFsmStatus_Object = MibTableColumn
cucsSysdebugCoreFsmFsmStatus = _CucsSysdebugCoreFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24, 1, 7),
    _CucsSysdebugCoreFsmFsmStatus_Type()
)
cucsSysdebugCoreFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmFsmStatus.setStatus("current")
_CucsSysdebugCoreFsmProgress_Type = Gauge32
_CucsSysdebugCoreFsmProgress_Object = MibTableColumn
cucsSysdebugCoreFsmProgress = _CucsSysdebugCoreFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24, 1, 8),
    _CucsSysdebugCoreFsmProgress_Type()
)
cucsSysdebugCoreFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmProgress.setStatus("current")
_CucsSysdebugCoreFsmRmtErrCode_Type = Gauge32
_CucsSysdebugCoreFsmRmtErrCode_Object = MibTableColumn
cucsSysdebugCoreFsmRmtErrCode = _CucsSysdebugCoreFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24, 1, 9),
    _CucsSysdebugCoreFsmRmtErrCode_Type()
)
cucsSysdebugCoreFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmRmtErrCode.setStatus("current")
_CucsSysdebugCoreFsmRmtErrDescr_Type = SnmpAdminString
_CucsSysdebugCoreFsmRmtErrDescr_Object = MibTableColumn
cucsSysdebugCoreFsmRmtErrDescr = _CucsSysdebugCoreFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24, 1, 10),
    _CucsSysdebugCoreFsmRmtErrDescr_Type()
)
cucsSysdebugCoreFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmRmtErrDescr.setStatus("current")
_CucsSysdebugCoreFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSysdebugCoreFsmRmtRslt_Object = MibTableColumn
cucsSysdebugCoreFsmRmtRslt = _CucsSysdebugCoreFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 24, 1, 11),
    _CucsSysdebugCoreFsmRmtRslt_Type()
)
cucsSysdebugCoreFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmRmtRslt.setStatus("current")
_CucsSysdebugCoreFsmStageTable_Object = MibTable
cucsSysdebugCoreFsmStageTable = _CucsSysdebugCoreFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 25)
)
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStageTable.setStatus("current")
_CucsSysdebugCoreFsmStageEntry_Object = MibTableRow
cucsSysdebugCoreFsmStageEntry = _CucsSysdebugCoreFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 25, 1)
)
cucsSysdebugCoreFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugCoreFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStageEntry.setStatus("current")
_CucsSysdebugCoreFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSysdebugCoreFsmStageInstanceId_Object = MibTableColumn
cucsSysdebugCoreFsmStageInstanceId = _CucsSysdebugCoreFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 25, 1, 1),
    _CucsSysdebugCoreFsmStageInstanceId_Type()
)
cucsSysdebugCoreFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStageInstanceId.setStatus("current")
_CucsSysdebugCoreFsmStageDn_Type = CucsManagedObjectDn
_CucsSysdebugCoreFsmStageDn_Object = MibTableColumn
cucsSysdebugCoreFsmStageDn = _CucsSysdebugCoreFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 25, 1, 2),
    _CucsSysdebugCoreFsmStageDn_Type()
)
cucsSysdebugCoreFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStageDn.setStatus("current")
_CucsSysdebugCoreFsmStageRn_Type = SnmpAdminString
_CucsSysdebugCoreFsmStageRn_Object = MibTableColumn
cucsSysdebugCoreFsmStageRn = _CucsSysdebugCoreFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 25, 1, 3),
    _CucsSysdebugCoreFsmStageRn_Type()
)
cucsSysdebugCoreFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStageRn.setStatus("current")
_CucsSysdebugCoreFsmStageDescrData_Type = SnmpAdminString
_CucsSysdebugCoreFsmStageDescrData_Object = MibTableColumn
cucsSysdebugCoreFsmStageDescrData = _CucsSysdebugCoreFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 25, 1, 4),
    _CucsSysdebugCoreFsmStageDescrData_Type()
)
cucsSysdebugCoreFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStageDescrData.setStatus("current")
_CucsSysdebugCoreFsmStageLastUpdateTime_Type = DateAndTime
_CucsSysdebugCoreFsmStageLastUpdateTime_Object = MibTableColumn
cucsSysdebugCoreFsmStageLastUpdateTime = _CucsSysdebugCoreFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 25, 1, 5),
    _CucsSysdebugCoreFsmStageLastUpdateTime_Type()
)
cucsSysdebugCoreFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStageLastUpdateTime.setStatus("current")
_CucsSysdebugCoreFsmStageName_Type = CucsSysdebugCoreFsmStageName
_CucsSysdebugCoreFsmStageName_Object = MibTableColumn
cucsSysdebugCoreFsmStageName = _CucsSysdebugCoreFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 25, 1, 6),
    _CucsSysdebugCoreFsmStageName_Type()
)
cucsSysdebugCoreFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStageName.setStatus("current")
_CucsSysdebugCoreFsmStageOrder_Type = Gauge32
_CucsSysdebugCoreFsmStageOrder_Object = MibTableColumn
cucsSysdebugCoreFsmStageOrder = _CucsSysdebugCoreFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 25, 1, 7),
    _CucsSysdebugCoreFsmStageOrder_Type()
)
cucsSysdebugCoreFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStageOrder.setStatus("current")
_CucsSysdebugCoreFsmStageRetry_Type = Gauge32
_CucsSysdebugCoreFsmStageRetry_Object = MibTableColumn
cucsSysdebugCoreFsmStageRetry = _CucsSysdebugCoreFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 25, 1, 8),
    _CucsSysdebugCoreFsmStageRetry_Type()
)
cucsSysdebugCoreFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStageRetry.setStatus("current")
_CucsSysdebugCoreFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSysdebugCoreFsmStageStageStatus_Object = MibTableColumn
cucsSysdebugCoreFsmStageStageStatus = _CucsSysdebugCoreFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 25, 1, 9),
    _CucsSysdebugCoreFsmStageStageStatus_Type()
)
cucsSysdebugCoreFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugCoreFsmStageStageStatus.setStatus("current")
_CucsSysdebugLogControlEpFsmTable_Object = MibTable
cucsSysdebugLogControlEpFsmTable = _CucsSysdebugLogControlEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmTable.setStatus("current")
_CucsSysdebugLogControlEpFsmEntry_Object = MibTableRow
cucsSysdebugLogControlEpFsmEntry = _CucsSysdebugLogControlEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26, 1)
)
cucsSysdebugLogControlEpFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogControlEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmEntry.setStatus("current")
_CucsSysdebugLogControlEpFsmInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogControlEpFsmInstanceId_Object = MibTableColumn
cucsSysdebugLogControlEpFsmInstanceId = _CucsSysdebugLogControlEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26, 1, 1),
    _CucsSysdebugLogControlEpFsmInstanceId_Type()
)
cucsSysdebugLogControlEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmInstanceId.setStatus("current")
_CucsSysdebugLogControlEpFsmDn_Type = CucsManagedObjectDn
_CucsSysdebugLogControlEpFsmDn_Object = MibTableColumn
cucsSysdebugLogControlEpFsmDn = _CucsSysdebugLogControlEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26, 1, 2),
    _CucsSysdebugLogControlEpFsmDn_Type()
)
cucsSysdebugLogControlEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmDn.setStatus("current")
_CucsSysdebugLogControlEpFsmRn_Type = SnmpAdminString
_CucsSysdebugLogControlEpFsmRn_Object = MibTableColumn
cucsSysdebugLogControlEpFsmRn = _CucsSysdebugLogControlEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26, 1, 3),
    _CucsSysdebugLogControlEpFsmRn_Type()
)
cucsSysdebugLogControlEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmRn.setStatus("current")
_CucsSysdebugLogControlEpFsmCompletionTime_Type = DateAndTime
_CucsSysdebugLogControlEpFsmCompletionTime_Object = MibTableColumn
cucsSysdebugLogControlEpFsmCompletionTime = _CucsSysdebugLogControlEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26, 1, 4),
    _CucsSysdebugLogControlEpFsmCompletionTime_Type()
)
cucsSysdebugLogControlEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmCompletionTime.setStatus("current")
_CucsSysdebugLogControlEpFsmCurrentFsm_Type = CucsSysdebugLogControlEpFsmCurrentFsm
_CucsSysdebugLogControlEpFsmCurrentFsm_Object = MibTableColumn
cucsSysdebugLogControlEpFsmCurrentFsm = _CucsSysdebugLogControlEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26, 1, 5),
    _CucsSysdebugLogControlEpFsmCurrentFsm_Type()
)
cucsSysdebugLogControlEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmCurrentFsm.setStatus("current")
_CucsSysdebugLogControlEpFsmDescrData_Type = SnmpAdminString
_CucsSysdebugLogControlEpFsmDescrData_Object = MibTableColumn
cucsSysdebugLogControlEpFsmDescrData = _CucsSysdebugLogControlEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26, 1, 6),
    _CucsSysdebugLogControlEpFsmDescrData_Type()
)
cucsSysdebugLogControlEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmDescrData.setStatus("current")
_CucsSysdebugLogControlEpFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSysdebugLogControlEpFsmFsmStatus_Object = MibTableColumn
cucsSysdebugLogControlEpFsmFsmStatus = _CucsSysdebugLogControlEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26, 1, 7),
    _CucsSysdebugLogControlEpFsmFsmStatus_Type()
)
cucsSysdebugLogControlEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmFsmStatus.setStatus("current")
_CucsSysdebugLogControlEpFsmProgress_Type = Gauge32
_CucsSysdebugLogControlEpFsmProgress_Object = MibTableColumn
cucsSysdebugLogControlEpFsmProgress = _CucsSysdebugLogControlEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26, 1, 8),
    _CucsSysdebugLogControlEpFsmProgress_Type()
)
cucsSysdebugLogControlEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmProgress.setStatus("current")
_CucsSysdebugLogControlEpFsmRmtErrCode_Type = Gauge32
_CucsSysdebugLogControlEpFsmRmtErrCode_Object = MibTableColumn
cucsSysdebugLogControlEpFsmRmtErrCode = _CucsSysdebugLogControlEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26, 1, 9),
    _CucsSysdebugLogControlEpFsmRmtErrCode_Type()
)
cucsSysdebugLogControlEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmRmtErrCode.setStatus("current")
_CucsSysdebugLogControlEpFsmRmtErrDescr_Type = SnmpAdminString
_CucsSysdebugLogControlEpFsmRmtErrDescr_Object = MibTableColumn
cucsSysdebugLogControlEpFsmRmtErrDescr = _CucsSysdebugLogControlEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26, 1, 10),
    _CucsSysdebugLogControlEpFsmRmtErrDescr_Type()
)
cucsSysdebugLogControlEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmRmtErrDescr.setStatus("current")
_CucsSysdebugLogControlEpFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSysdebugLogControlEpFsmRmtRslt_Object = MibTableColumn
cucsSysdebugLogControlEpFsmRmtRslt = _CucsSysdebugLogControlEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 26, 1, 11),
    _CucsSysdebugLogControlEpFsmRmtRslt_Type()
)
cucsSysdebugLogControlEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmRmtRslt.setStatus("current")
_CucsSysdebugLogControlEpFsmStageTable_Object = MibTable
cucsSysdebugLogControlEpFsmStageTable = _CucsSysdebugLogControlEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 27)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStageTable.setStatus("current")
_CucsSysdebugLogControlEpFsmStageEntry_Object = MibTableRow
cucsSysdebugLogControlEpFsmStageEntry = _CucsSysdebugLogControlEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 27, 1)
)
cucsSysdebugLogControlEpFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogControlEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStageEntry.setStatus("current")
_CucsSysdebugLogControlEpFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogControlEpFsmStageInstanceId_Object = MibTableColumn
cucsSysdebugLogControlEpFsmStageInstanceId = _CucsSysdebugLogControlEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 27, 1, 1),
    _CucsSysdebugLogControlEpFsmStageInstanceId_Type()
)
cucsSysdebugLogControlEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStageInstanceId.setStatus("current")
_CucsSysdebugLogControlEpFsmStageDn_Type = CucsManagedObjectDn
_CucsSysdebugLogControlEpFsmStageDn_Object = MibTableColumn
cucsSysdebugLogControlEpFsmStageDn = _CucsSysdebugLogControlEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 27, 1, 2),
    _CucsSysdebugLogControlEpFsmStageDn_Type()
)
cucsSysdebugLogControlEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStageDn.setStatus("current")
_CucsSysdebugLogControlEpFsmStageRn_Type = SnmpAdminString
_CucsSysdebugLogControlEpFsmStageRn_Object = MibTableColumn
cucsSysdebugLogControlEpFsmStageRn = _CucsSysdebugLogControlEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 27, 1, 3),
    _CucsSysdebugLogControlEpFsmStageRn_Type()
)
cucsSysdebugLogControlEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStageRn.setStatus("current")
_CucsSysdebugLogControlEpFsmStageDescrData_Type = SnmpAdminString
_CucsSysdebugLogControlEpFsmStageDescrData_Object = MibTableColumn
cucsSysdebugLogControlEpFsmStageDescrData = _CucsSysdebugLogControlEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 27, 1, 4),
    _CucsSysdebugLogControlEpFsmStageDescrData_Type()
)
cucsSysdebugLogControlEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStageDescrData.setStatus("current")
_CucsSysdebugLogControlEpFsmStageLastUpdateTime_Type = DateAndTime
_CucsSysdebugLogControlEpFsmStageLastUpdateTime_Object = MibTableColumn
cucsSysdebugLogControlEpFsmStageLastUpdateTime = _CucsSysdebugLogControlEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 27, 1, 5),
    _CucsSysdebugLogControlEpFsmStageLastUpdateTime_Type()
)
cucsSysdebugLogControlEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStageLastUpdateTime.setStatus("current")
_CucsSysdebugLogControlEpFsmStageName_Type = CucsSysdebugLogControlEpFsmStageName
_CucsSysdebugLogControlEpFsmStageName_Object = MibTableColumn
cucsSysdebugLogControlEpFsmStageName = _CucsSysdebugLogControlEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 27, 1, 6),
    _CucsSysdebugLogControlEpFsmStageName_Type()
)
cucsSysdebugLogControlEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStageName.setStatus("current")
_CucsSysdebugLogControlEpFsmStageOrder_Type = Gauge32
_CucsSysdebugLogControlEpFsmStageOrder_Object = MibTableColumn
cucsSysdebugLogControlEpFsmStageOrder = _CucsSysdebugLogControlEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 27, 1, 7),
    _CucsSysdebugLogControlEpFsmStageOrder_Type()
)
cucsSysdebugLogControlEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStageOrder.setStatus("current")
_CucsSysdebugLogControlEpFsmStageRetry_Type = Gauge32
_CucsSysdebugLogControlEpFsmStageRetry_Object = MibTableColumn
cucsSysdebugLogControlEpFsmStageRetry = _CucsSysdebugLogControlEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 27, 1, 8),
    _CucsSysdebugLogControlEpFsmStageRetry_Type()
)
cucsSysdebugLogControlEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStageRetry.setStatus("current")
_CucsSysdebugLogControlEpFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSysdebugLogControlEpFsmStageStageStatus_Object = MibTableColumn
cucsSysdebugLogControlEpFsmStageStageStatus = _CucsSysdebugLogControlEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 27, 1, 9),
    _CucsSysdebugLogControlEpFsmStageStageStatus_Type()
)
cucsSysdebugLogControlEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogControlEpFsmStageStageStatus.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmTable_Object = MibTable
cucsSysdebugManualCoreFileExportTargetFsmTable = _CucsSysdebugManualCoreFileExportTargetFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28)
)
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmTable.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmEntry_Object = MibTableRow
cucsSysdebugManualCoreFileExportTargetFsmEntry = _CucsSysdebugManualCoreFileExportTargetFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28, 1)
)
cucsSysdebugManualCoreFileExportTargetFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugManualCoreFileExportTargetFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmEntry.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmInstanceId_Type = CucsManagedObjectId
_CucsSysdebugManualCoreFileExportTargetFsmInstanceId_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmInstanceId = _CucsSysdebugManualCoreFileExportTargetFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28, 1, 1),
    _CucsSysdebugManualCoreFileExportTargetFsmInstanceId_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmInstanceId.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmDn_Type = CucsManagedObjectDn
_CucsSysdebugManualCoreFileExportTargetFsmDn_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmDn = _CucsSysdebugManualCoreFileExportTargetFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28, 1, 2),
    _CucsSysdebugManualCoreFileExportTargetFsmDn_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmDn.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmRn_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetFsmRn_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmRn = _CucsSysdebugManualCoreFileExportTargetFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28, 1, 3),
    _CucsSysdebugManualCoreFileExportTargetFsmRn_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmRn.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmCompletionTime_Type = DateAndTime
_CucsSysdebugManualCoreFileExportTargetFsmCompletionTime_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmCompletionTime = _CucsSysdebugManualCoreFileExportTargetFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28, 1, 4),
    _CucsSysdebugManualCoreFileExportTargetFsmCompletionTime_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmCompletionTime.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmCurrentFsm_Type = CucsSysdebugManualCoreFileExportTargetFsmCurrentFsm
_CucsSysdebugManualCoreFileExportTargetFsmCurrentFsm_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmCurrentFsm = _CucsSysdebugManualCoreFileExportTargetFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28, 1, 5),
    _CucsSysdebugManualCoreFileExportTargetFsmCurrentFsm_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmCurrentFsm.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmDescrData_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetFsmDescrData_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmDescrData = _CucsSysdebugManualCoreFileExportTargetFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28, 1, 6),
    _CucsSysdebugManualCoreFileExportTargetFsmDescrData_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmDescrData.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSysdebugManualCoreFileExportTargetFsmFsmStatus_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmFsmStatus = _CucsSysdebugManualCoreFileExportTargetFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28, 1, 7),
    _CucsSysdebugManualCoreFileExportTargetFsmFsmStatus_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmFsmStatus.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmProgress_Type = Gauge32
_CucsSysdebugManualCoreFileExportTargetFsmProgress_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmProgress = _CucsSysdebugManualCoreFileExportTargetFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28, 1, 8),
    _CucsSysdebugManualCoreFileExportTargetFsmProgress_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmProgress.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmRmtErrCode_Type = Gauge32
_CucsSysdebugManualCoreFileExportTargetFsmRmtErrCode_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmRmtErrCode = _CucsSysdebugManualCoreFileExportTargetFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28, 1, 9),
    _CucsSysdebugManualCoreFileExportTargetFsmRmtErrCode_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmRmtErrCode.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmRmtErrDescr_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetFsmRmtErrDescr_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmRmtErrDescr = _CucsSysdebugManualCoreFileExportTargetFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28, 1, 10),
    _CucsSysdebugManualCoreFileExportTargetFsmRmtErrDescr_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmRmtErrDescr.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSysdebugManualCoreFileExportTargetFsmRmtRslt_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmRmtRslt = _CucsSysdebugManualCoreFileExportTargetFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 28, 1, 11),
    _CucsSysdebugManualCoreFileExportTargetFsmRmtRslt_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmRmtRslt.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStageTable_Object = MibTable
cucsSysdebugManualCoreFileExportTargetFsmStageTable = _CucsSysdebugManualCoreFileExportTargetFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 29)
)
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStageTable.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStageEntry_Object = MibTableRow
cucsSysdebugManualCoreFileExportTargetFsmStageEntry = _CucsSysdebugManualCoreFileExportTargetFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 29, 1)
)
cucsSysdebugManualCoreFileExportTargetFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugManualCoreFileExportTargetFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStageEntry.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSysdebugManualCoreFileExportTargetFsmStageInstanceId_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmStageInstanceId = _CucsSysdebugManualCoreFileExportTargetFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 29, 1, 1),
    _CucsSysdebugManualCoreFileExportTargetFsmStageInstanceId_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStageInstanceId.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStageDn_Type = CucsManagedObjectDn
_CucsSysdebugManualCoreFileExportTargetFsmStageDn_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmStageDn = _CucsSysdebugManualCoreFileExportTargetFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 29, 1, 2),
    _CucsSysdebugManualCoreFileExportTargetFsmStageDn_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStageDn.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStageRn_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetFsmStageRn_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmStageRn = _CucsSysdebugManualCoreFileExportTargetFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 29, 1, 3),
    _CucsSysdebugManualCoreFileExportTargetFsmStageRn_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStageRn.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStageDescrData_Type = SnmpAdminString
_CucsSysdebugManualCoreFileExportTargetFsmStageDescrData_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmStageDescrData = _CucsSysdebugManualCoreFileExportTargetFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 29, 1, 4),
    _CucsSysdebugManualCoreFileExportTargetFsmStageDescrData_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStageDescrData.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime_Type = DateAndTime
_CucsSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime = _CucsSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 29, 1, 5),
    _CucsSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStageName_Type = CucsSysdebugManualCoreFileExportTargetFsmStageName
_CucsSysdebugManualCoreFileExportTargetFsmStageName_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmStageName = _CucsSysdebugManualCoreFileExportTargetFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 29, 1, 6),
    _CucsSysdebugManualCoreFileExportTargetFsmStageName_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStageName.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStageOrder_Type = Gauge32
_CucsSysdebugManualCoreFileExportTargetFsmStageOrder_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmStageOrder = _CucsSysdebugManualCoreFileExportTargetFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 29, 1, 7),
    _CucsSysdebugManualCoreFileExportTargetFsmStageOrder_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStageOrder.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStageRetry_Type = Gauge32
_CucsSysdebugManualCoreFileExportTargetFsmStageRetry_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmStageRetry = _CucsSysdebugManualCoreFileExportTargetFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 29, 1, 8),
    _CucsSysdebugManualCoreFileExportTargetFsmStageRetry_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStageRetry.setStatus("current")
_CucsSysdebugManualCoreFileExportTargetFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSysdebugManualCoreFileExportTargetFsmStageStageStatus_Object = MibTableColumn
cucsSysdebugManualCoreFileExportTargetFsmStageStageStatus = _CucsSysdebugManualCoreFileExportTargetFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 29, 1, 9),
    _CucsSysdebugManualCoreFileExportTargetFsmStageStageStatus_Type()
)
cucsSysdebugManualCoreFileExportTargetFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugManualCoreFileExportTargetFsmStageStageStatus.setStatus("current")
_CucsSysdebugTechSupportFsmTable_Object = MibTable
cucsSysdebugTechSupportFsmTable = _CucsSysdebugTechSupportFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30)
)
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmTable.setStatus("current")
_CucsSysdebugTechSupportFsmEntry_Object = MibTableRow
cucsSysdebugTechSupportFsmEntry = _CucsSysdebugTechSupportFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30, 1)
)
cucsSysdebugTechSupportFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugTechSupportFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmEntry.setStatus("current")
_CucsSysdebugTechSupportFsmInstanceId_Type = CucsManagedObjectId
_CucsSysdebugTechSupportFsmInstanceId_Object = MibTableColumn
cucsSysdebugTechSupportFsmInstanceId = _CucsSysdebugTechSupportFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30, 1, 1),
    _CucsSysdebugTechSupportFsmInstanceId_Type()
)
cucsSysdebugTechSupportFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmInstanceId.setStatus("current")
_CucsSysdebugTechSupportFsmDn_Type = CucsManagedObjectDn
_CucsSysdebugTechSupportFsmDn_Object = MibTableColumn
cucsSysdebugTechSupportFsmDn = _CucsSysdebugTechSupportFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30, 1, 2),
    _CucsSysdebugTechSupportFsmDn_Type()
)
cucsSysdebugTechSupportFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmDn.setStatus("current")
_CucsSysdebugTechSupportFsmRn_Type = SnmpAdminString
_CucsSysdebugTechSupportFsmRn_Object = MibTableColumn
cucsSysdebugTechSupportFsmRn = _CucsSysdebugTechSupportFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30, 1, 3),
    _CucsSysdebugTechSupportFsmRn_Type()
)
cucsSysdebugTechSupportFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmRn.setStatus("current")
_CucsSysdebugTechSupportFsmCompletionTime_Type = DateAndTime
_CucsSysdebugTechSupportFsmCompletionTime_Object = MibTableColumn
cucsSysdebugTechSupportFsmCompletionTime = _CucsSysdebugTechSupportFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30, 1, 4),
    _CucsSysdebugTechSupportFsmCompletionTime_Type()
)
cucsSysdebugTechSupportFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmCompletionTime.setStatus("current")
_CucsSysdebugTechSupportFsmCurrentFsm_Type = CucsSysdebugTechSupportFsmCurrentFsm
_CucsSysdebugTechSupportFsmCurrentFsm_Object = MibTableColumn
cucsSysdebugTechSupportFsmCurrentFsm = _CucsSysdebugTechSupportFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30, 1, 5),
    _CucsSysdebugTechSupportFsmCurrentFsm_Type()
)
cucsSysdebugTechSupportFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmCurrentFsm.setStatus("current")
_CucsSysdebugTechSupportFsmDescrData_Type = SnmpAdminString
_CucsSysdebugTechSupportFsmDescrData_Object = MibTableColumn
cucsSysdebugTechSupportFsmDescrData = _CucsSysdebugTechSupportFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30, 1, 6),
    _CucsSysdebugTechSupportFsmDescrData_Type()
)
cucsSysdebugTechSupportFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmDescrData.setStatus("current")
_CucsSysdebugTechSupportFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSysdebugTechSupportFsmFsmStatus_Object = MibTableColumn
cucsSysdebugTechSupportFsmFsmStatus = _CucsSysdebugTechSupportFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30, 1, 7),
    _CucsSysdebugTechSupportFsmFsmStatus_Type()
)
cucsSysdebugTechSupportFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmFsmStatus.setStatus("current")
_CucsSysdebugTechSupportFsmProgress_Type = Gauge32
_CucsSysdebugTechSupportFsmProgress_Object = MibTableColumn
cucsSysdebugTechSupportFsmProgress = _CucsSysdebugTechSupportFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30, 1, 8),
    _CucsSysdebugTechSupportFsmProgress_Type()
)
cucsSysdebugTechSupportFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmProgress.setStatus("current")
_CucsSysdebugTechSupportFsmRmtErrCode_Type = Gauge32
_CucsSysdebugTechSupportFsmRmtErrCode_Object = MibTableColumn
cucsSysdebugTechSupportFsmRmtErrCode = _CucsSysdebugTechSupportFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30, 1, 9),
    _CucsSysdebugTechSupportFsmRmtErrCode_Type()
)
cucsSysdebugTechSupportFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmRmtErrCode.setStatus("current")
_CucsSysdebugTechSupportFsmRmtErrDescr_Type = SnmpAdminString
_CucsSysdebugTechSupportFsmRmtErrDescr_Object = MibTableColumn
cucsSysdebugTechSupportFsmRmtErrDescr = _CucsSysdebugTechSupportFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30, 1, 10),
    _CucsSysdebugTechSupportFsmRmtErrDescr_Type()
)
cucsSysdebugTechSupportFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmRmtErrDescr.setStatus("current")
_CucsSysdebugTechSupportFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSysdebugTechSupportFsmRmtRslt_Object = MibTableColumn
cucsSysdebugTechSupportFsmRmtRslt = _CucsSysdebugTechSupportFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 30, 1, 11),
    _CucsSysdebugTechSupportFsmRmtRslt_Type()
)
cucsSysdebugTechSupportFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmRmtRslt.setStatus("current")
_CucsSysdebugTechSupportFsmStageTable_Object = MibTable
cucsSysdebugTechSupportFsmStageTable = _CucsSysdebugTechSupportFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 31)
)
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStageTable.setStatus("current")
_CucsSysdebugTechSupportFsmStageEntry_Object = MibTableRow
cucsSysdebugTechSupportFsmStageEntry = _CucsSysdebugTechSupportFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 31, 1)
)
cucsSysdebugTechSupportFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugTechSupportFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStageEntry.setStatus("current")
_CucsSysdebugTechSupportFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSysdebugTechSupportFsmStageInstanceId_Object = MibTableColumn
cucsSysdebugTechSupportFsmStageInstanceId = _CucsSysdebugTechSupportFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 31, 1, 1),
    _CucsSysdebugTechSupportFsmStageInstanceId_Type()
)
cucsSysdebugTechSupportFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStageInstanceId.setStatus("current")
_CucsSysdebugTechSupportFsmStageDn_Type = CucsManagedObjectDn
_CucsSysdebugTechSupportFsmStageDn_Object = MibTableColumn
cucsSysdebugTechSupportFsmStageDn = _CucsSysdebugTechSupportFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 31, 1, 2),
    _CucsSysdebugTechSupportFsmStageDn_Type()
)
cucsSysdebugTechSupportFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStageDn.setStatus("current")
_CucsSysdebugTechSupportFsmStageRn_Type = SnmpAdminString
_CucsSysdebugTechSupportFsmStageRn_Object = MibTableColumn
cucsSysdebugTechSupportFsmStageRn = _CucsSysdebugTechSupportFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 31, 1, 3),
    _CucsSysdebugTechSupportFsmStageRn_Type()
)
cucsSysdebugTechSupportFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStageRn.setStatus("current")
_CucsSysdebugTechSupportFsmStageDescrData_Type = SnmpAdminString
_CucsSysdebugTechSupportFsmStageDescrData_Object = MibTableColumn
cucsSysdebugTechSupportFsmStageDescrData = _CucsSysdebugTechSupportFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 31, 1, 4),
    _CucsSysdebugTechSupportFsmStageDescrData_Type()
)
cucsSysdebugTechSupportFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStageDescrData.setStatus("current")
_CucsSysdebugTechSupportFsmStageLastUpdateTime_Type = DateAndTime
_CucsSysdebugTechSupportFsmStageLastUpdateTime_Object = MibTableColumn
cucsSysdebugTechSupportFsmStageLastUpdateTime = _CucsSysdebugTechSupportFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 31, 1, 5),
    _CucsSysdebugTechSupportFsmStageLastUpdateTime_Type()
)
cucsSysdebugTechSupportFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStageLastUpdateTime.setStatus("current")
_CucsSysdebugTechSupportFsmStageName_Type = CucsSysdebugTechSupportFsmStageName
_CucsSysdebugTechSupportFsmStageName_Object = MibTableColumn
cucsSysdebugTechSupportFsmStageName = _CucsSysdebugTechSupportFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 31, 1, 6),
    _CucsSysdebugTechSupportFsmStageName_Type()
)
cucsSysdebugTechSupportFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStageName.setStatus("current")
_CucsSysdebugTechSupportFsmStageOrder_Type = Gauge32
_CucsSysdebugTechSupportFsmStageOrder_Object = MibTableColumn
cucsSysdebugTechSupportFsmStageOrder = _CucsSysdebugTechSupportFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 31, 1, 7),
    _CucsSysdebugTechSupportFsmStageOrder_Type()
)
cucsSysdebugTechSupportFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStageOrder.setStatus("current")
_CucsSysdebugTechSupportFsmStageRetry_Type = Gauge32
_CucsSysdebugTechSupportFsmStageRetry_Object = MibTableColumn
cucsSysdebugTechSupportFsmStageRetry = _CucsSysdebugTechSupportFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 31, 1, 8),
    _CucsSysdebugTechSupportFsmStageRetry_Type()
)
cucsSysdebugTechSupportFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStageRetry.setStatus("current")
_CucsSysdebugTechSupportFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSysdebugTechSupportFsmStageStageStatus_Object = MibTableColumn
cucsSysdebugTechSupportFsmStageStageStatus = _CucsSysdebugTechSupportFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 31, 1, 9),
    _CucsSysdebugTechSupportFsmStageStageStatus_Type()
)
cucsSysdebugTechSupportFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugTechSupportFsmStageStageStatus.setStatus("current")
_CucsSysdebugLogExportPolicyTable_Object = MibTable
cucsSysdebugLogExportPolicyTable = _CucsSysdebugLogExportPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyTable.setStatus("current")
_CucsSysdebugLogExportPolicyEntry_Object = MibTableRow
cucsSysdebugLogExportPolicyEntry = _CucsSysdebugLogExportPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1)
)
cucsSysdebugLogExportPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogExportPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyEntry.setStatus("current")
_CucsSysdebugLogExportPolicyInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogExportPolicyInstanceId_Object = MibTableColumn
cucsSysdebugLogExportPolicyInstanceId = _CucsSysdebugLogExportPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 1),
    _CucsSysdebugLogExportPolicyInstanceId_Type()
)
cucsSysdebugLogExportPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyInstanceId.setStatus("current")
_CucsSysdebugLogExportPolicyDn_Type = CucsManagedObjectDn
_CucsSysdebugLogExportPolicyDn_Object = MibTableColumn
cucsSysdebugLogExportPolicyDn = _CucsSysdebugLogExportPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 2),
    _CucsSysdebugLogExportPolicyDn_Type()
)
cucsSysdebugLogExportPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyDn.setStatus("current")
_CucsSysdebugLogExportPolicyRn_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyRn_Object = MibTableColumn
cucsSysdebugLogExportPolicyRn = _CucsSysdebugLogExportPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 3),
    _CucsSysdebugLogExportPolicyRn_Type()
)
cucsSysdebugLogExportPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyRn.setStatus("current")
_CucsSysdebugLogExportPolicyAdminState_Type = CucsCommClientAdminState
_CucsSysdebugLogExportPolicyAdminState_Object = MibTableColumn
cucsSysdebugLogExportPolicyAdminState = _CucsSysdebugLogExportPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 4),
    _CucsSysdebugLogExportPolicyAdminState_Type()
)
cucsSysdebugLogExportPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyAdminState.setStatus("current")
_CucsSysdebugLogExportPolicyDescr_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyDescr_Object = MibTableColumn
cucsSysdebugLogExportPolicyDescr = _CucsSysdebugLogExportPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 5),
    _CucsSysdebugLogExportPolicyDescr_Type()
)
cucsSysdebugLogExportPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyDescr.setStatus("current")
_CucsSysdebugLogExportPolicyFsmDescr_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyFsmDescr_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmDescr = _CucsSysdebugLogExportPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 6),
    _CucsSysdebugLogExportPolicyFsmDescr_Type()
)
cucsSysdebugLogExportPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmDescr.setStatus("current")
_CucsSysdebugLogExportPolicyFsmPrev_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyFsmPrev_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmPrev = _CucsSysdebugLogExportPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 7),
    _CucsSysdebugLogExportPolicyFsmPrev_Type()
)
cucsSysdebugLogExportPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmPrev.setStatus("current")
_CucsSysdebugLogExportPolicyFsmProgr_Type = Gauge32
_CucsSysdebugLogExportPolicyFsmProgr_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmProgr = _CucsSysdebugLogExportPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 8),
    _CucsSysdebugLogExportPolicyFsmProgr_Type()
)
cucsSysdebugLogExportPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmProgr.setStatus("current")
_CucsSysdebugLogExportPolicyFsmRmtInvErrCode_Type = Gauge32
_CucsSysdebugLogExportPolicyFsmRmtInvErrCode_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmRmtInvErrCode = _CucsSysdebugLogExportPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 9),
    _CucsSysdebugLogExportPolicyFsmRmtInvErrCode_Type()
)
cucsSysdebugLogExportPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmRmtInvErrCode.setStatus("current")
_CucsSysdebugLogExportPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmRmtInvErrDescr = _CucsSysdebugLogExportPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 10),
    _CucsSysdebugLogExportPolicyFsmRmtInvErrDescr_Type()
)
cucsSysdebugLogExportPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmRmtInvErrDescr.setStatus("current")
_CucsSysdebugLogExportPolicyFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSysdebugLogExportPolicyFsmRmtInvRslt_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmRmtInvRslt = _CucsSysdebugLogExportPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 11),
    _CucsSysdebugLogExportPolicyFsmRmtInvRslt_Type()
)
cucsSysdebugLogExportPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmRmtInvRslt.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStageDescr_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyFsmStageDescr_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmStageDescr = _CucsSysdebugLogExportPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 12),
    _CucsSysdebugLogExportPolicyFsmStageDescr_Type()
)
cucsSysdebugLogExportPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStageDescr.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStamp_Type = DateAndTime
_CucsSysdebugLogExportPolicyFsmStamp_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmStamp = _CucsSysdebugLogExportPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 13),
    _CucsSysdebugLogExportPolicyFsmStamp_Type()
)
cucsSysdebugLogExportPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStamp.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStatus_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyFsmStatus_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmStatus = _CucsSysdebugLogExportPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 14),
    _CucsSysdebugLogExportPolicyFsmStatus_Type()
)
cucsSysdebugLogExportPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStatus.setStatus("current")
_CucsSysdebugLogExportPolicyFsmTry_Type = Gauge32
_CucsSysdebugLogExportPolicyFsmTry_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmTry = _CucsSysdebugLogExportPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 15),
    _CucsSysdebugLogExportPolicyFsmTry_Type()
)
cucsSysdebugLogExportPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmTry.setStatus("current")
_CucsSysdebugLogExportPolicyHostname_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyHostname_Object = MibTableColumn
cucsSysdebugLogExportPolicyHostname = _CucsSysdebugLogExportPolicyHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 16),
    _CucsSysdebugLogExportPolicyHostname_Type()
)
cucsSysdebugLogExportPolicyHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyHostname.setStatus("current")
_CucsSysdebugLogExportPolicyIntId_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyIntId_Object = MibTableColumn
cucsSysdebugLogExportPolicyIntId = _CucsSysdebugLogExportPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 17),
    _CucsSysdebugLogExportPolicyIntId_Type()
)
cucsSysdebugLogExportPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyIntId.setStatus("current")
_CucsSysdebugLogExportPolicyName_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyName_Object = MibTableColumn
cucsSysdebugLogExportPolicyName = _CucsSysdebugLogExportPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 18),
    _CucsSysdebugLogExportPolicyName_Type()
)
cucsSysdebugLogExportPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyName.setStatus("current")
_CucsSysdebugLogExportPolicyPasswordlessSsh_Type = TruthValue
_CucsSysdebugLogExportPolicyPasswordlessSsh_Object = MibTableColumn
cucsSysdebugLogExportPolicyPasswordlessSsh = _CucsSysdebugLogExportPolicyPasswordlessSsh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 19),
    _CucsSysdebugLogExportPolicyPasswordlessSsh_Type()
)
cucsSysdebugLogExportPolicyPasswordlessSsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyPasswordlessSsh.setStatus("current")
_CucsSysdebugLogExportPolicyPath_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyPath_Object = MibTableColumn
cucsSysdebugLogExportPolicyPath = _CucsSysdebugLogExportPolicyPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 20),
    _CucsSysdebugLogExportPolicyPath_Type()
)
cucsSysdebugLogExportPolicyPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyPath.setStatus("current")
_CucsSysdebugLogExportPolicyPolicyLevel_Type = Gauge32
_CucsSysdebugLogExportPolicyPolicyLevel_Object = MibTableColumn
cucsSysdebugLogExportPolicyPolicyLevel = _CucsSysdebugLogExportPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 21),
    _CucsSysdebugLogExportPolicyPolicyLevel_Type()
)
cucsSysdebugLogExportPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyPolicyLevel.setStatus("current")
_CucsSysdebugLogExportPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsSysdebugLogExportPolicyPolicyOwner_Object = MibTableColumn
cucsSysdebugLogExportPolicyPolicyOwner = _CucsSysdebugLogExportPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 22),
    _CucsSysdebugLogExportPolicyPolicyOwner_Type()
)
cucsSysdebugLogExportPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyPolicyOwner.setStatus("current")
_CucsSysdebugLogExportPolicyPostAction_Type = CucsSysfileExporterPostAction
_CucsSysdebugLogExportPolicyPostAction_Object = MibTableColumn
cucsSysdebugLogExportPolicyPostAction = _CucsSysdebugLogExportPolicyPostAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 23),
    _CucsSysdebugLogExportPolicyPostAction_Type()
)
cucsSysdebugLogExportPolicyPostAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyPostAction.setStatus("current")
_CucsSysdebugLogExportPolicyProto_Type = CucsSysdebugLogExportPolicyProto
_CucsSysdebugLogExportPolicyProto_Object = MibTableColumn
cucsSysdebugLogExportPolicyProto = _CucsSysdebugLogExportPolicyProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 24),
    _CucsSysdebugLogExportPolicyProto_Type()
)
cucsSysdebugLogExportPolicyProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyProto.setStatus("current")
_CucsSysdebugLogExportPolicyPwd_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyPwd_Object = MibTableColumn
cucsSysdebugLogExportPolicyPwd = _CucsSysdebugLogExportPolicyPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 25),
    _CucsSysdebugLogExportPolicyPwd_Type()
)
cucsSysdebugLogExportPolicyPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyPwd.setStatus("current")
_CucsSysdebugLogExportPolicyUser_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyUser_Object = MibTableColumn
cucsSysdebugLogExportPolicyUser = _CucsSysdebugLogExportPolicyUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 32, 1, 26),
    _CucsSysdebugLogExportPolicyUser_Type()
)
cucsSysdebugLogExportPolicyUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyUser.setStatus("current")
_CucsSysdebugLogExportPolicyFsmTable_Object = MibTable
cucsSysdebugLogExportPolicyFsmTable = _CucsSysdebugLogExportPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmTable.setStatus("current")
_CucsSysdebugLogExportPolicyFsmEntry_Object = MibTableRow
cucsSysdebugLogExportPolicyFsmEntry = _CucsSysdebugLogExportPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33, 1)
)
cucsSysdebugLogExportPolicyFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogExportPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmEntry.setStatus("current")
_CucsSysdebugLogExportPolicyFsmInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogExportPolicyFsmInstanceId_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmInstanceId = _CucsSysdebugLogExportPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33, 1, 1),
    _CucsSysdebugLogExportPolicyFsmInstanceId_Type()
)
cucsSysdebugLogExportPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmInstanceId.setStatus("current")
_CucsSysdebugLogExportPolicyFsmDn_Type = CucsManagedObjectDn
_CucsSysdebugLogExportPolicyFsmDn_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmDn = _CucsSysdebugLogExportPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33, 1, 2),
    _CucsSysdebugLogExportPolicyFsmDn_Type()
)
cucsSysdebugLogExportPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmDn.setStatus("current")
_CucsSysdebugLogExportPolicyFsmRn_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyFsmRn_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmRn = _CucsSysdebugLogExportPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33, 1, 3),
    _CucsSysdebugLogExportPolicyFsmRn_Type()
)
cucsSysdebugLogExportPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmRn.setStatus("current")
_CucsSysdebugLogExportPolicyFsmCompletionTime_Type = DateAndTime
_CucsSysdebugLogExportPolicyFsmCompletionTime_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmCompletionTime = _CucsSysdebugLogExportPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33, 1, 4),
    _CucsSysdebugLogExportPolicyFsmCompletionTime_Type()
)
cucsSysdebugLogExportPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmCompletionTime.setStatus("current")
_CucsSysdebugLogExportPolicyFsmCurrentFsm_Type = CucsSysdebugLogExportPolicyFsmCurrentFsm
_CucsSysdebugLogExportPolicyFsmCurrentFsm_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmCurrentFsm = _CucsSysdebugLogExportPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33, 1, 5),
    _CucsSysdebugLogExportPolicyFsmCurrentFsm_Type()
)
cucsSysdebugLogExportPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmCurrentFsm.setStatus("current")
_CucsSysdebugLogExportPolicyFsmDescrData_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyFsmDescrData_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmDescrData = _CucsSysdebugLogExportPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33, 1, 6),
    _CucsSysdebugLogExportPolicyFsmDescrData_Type()
)
cucsSysdebugLogExportPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmDescrData.setStatus("current")
_CucsSysdebugLogExportPolicyFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSysdebugLogExportPolicyFsmFsmStatus_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmFsmStatus = _CucsSysdebugLogExportPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33, 1, 7),
    _CucsSysdebugLogExportPolicyFsmFsmStatus_Type()
)
cucsSysdebugLogExportPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmFsmStatus.setStatus("current")
_CucsSysdebugLogExportPolicyFsmProgress_Type = Gauge32
_CucsSysdebugLogExportPolicyFsmProgress_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmProgress = _CucsSysdebugLogExportPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33, 1, 8),
    _CucsSysdebugLogExportPolicyFsmProgress_Type()
)
cucsSysdebugLogExportPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmProgress.setStatus("current")
_CucsSysdebugLogExportPolicyFsmRmtErrCode_Type = Gauge32
_CucsSysdebugLogExportPolicyFsmRmtErrCode_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmRmtErrCode = _CucsSysdebugLogExportPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33, 1, 9),
    _CucsSysdebugLogExportPolicyFsmRmtErrCode_Type()
)
cucsSysdebugLogExportPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmRmtErrCode.setStatus("current")
_CucsSysdebugLogExportPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyFsmRmtErrDescr_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmRmtErrDescr = _CucsSysdebugLogExportPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33, 1, 10),
    _CucsSysdebugLogExportPolicyFsmRmtErrDescr_Type()
)
cucsSysdebugLogExportPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmRmtErrDescr.setStatus("current")
_CucsSysdebugLogExportPolicyFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSysdebugLogExportPolicyFsmRmtRslt_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmRmtRslt = _CucsSysdebugLogExportPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 33, 1, 11),
    _CucsSysdebugLogExportPolicyFsmRmtRslt_Type()
)
cucsSysdebugLogExportPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmRmtRslt.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStageTable_Object = MibTable
cucsSysdebugLogExportPolicyFsmStageTable = _CucsSysdebugLogExportPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 34)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStageTable.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStageEntry_Object = MibTableRow
cucsSysdebugLogExportPolicyFsmStageEntry = _CucsSysdebugLogExportPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 34, 1)
)
cucsSysdebugLogExportPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogExportPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStageEntry.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogExportPolicyFsmStageInstanceId_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmStageInstanceId = _CucsSysdebugLogExportPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 34, 1, 1),
    _CucsSysdebugLogExportPolicyFsmStageInstanceId_Type()
)
cucsSysdebugLogExportPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStageInstanceId.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStageDn_Type = CucsManagedObjectDn
_CucsSysdebugLogExportPolicyFsmStageDn_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmStageDn = _CucsSysdebugLogExportPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 34, 1, 2),
    _CucsSysdebugLogExportPolicyFsmStageDn_Type()
)
cucsSysdebugLogExportPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStageDn.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStageRn_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyFsmStageRn_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmStageRn = _CucsSysdebugLogExportPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 34, 1, 3),
    _CucsSysdebugLogExportPolicyFsmStageRn_Type()
)
cucsSysdebugLogExportPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStageRn.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStageDescrData_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyFsmStageDescrData_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmStageDescrData = _CucsSysdebugLogExportPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 34, 1, 4),
    _CucsSysdebugLogExportPolicyFsmStageDescrData_Type()
)
cucsSysdebugLogExportPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStageDescrData.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CucsSysdebugLogExportPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmStageLastUpdateTime = _CucsSysdebugLogExportPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 34, 1, 5),
    _CucsSysdebugLogExportPolicyFsmStageLastUpdateTime_Type()
)
cucsSysdebugLogExportPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStageLastUpdateTime.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStageName_Type = CucsSysdebugLogExportPolicyFsmStageName
_CucsSysdebugLogExportPolicyFsmStageName_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmStageName = _CucsSysdebugLogExportPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 34, 1, 6),
    _CucsSysdebugLogExportPolicyFsmStageName_Type()
)
cucsSysdebugLogExportPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStageName.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStageOrder_Type = Gauge32
_CucsSysdebugLogExportPolicyFsmStageOrder_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmStageOrder = _CucsSysdebugLogExportPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 34, 1, 7),
    _CucsSysdebugLogExportPolicyFsmStageOrder_Type()
)
cucsSysdebugLogExportPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStageOrder.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStageRetry_Type = Gauge32
_CucsSysdebugLogExportPolicyFsmStageRetry_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmStageRetry = _CucsSysdebugLogExportPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 34, 1, 8),
    _CucsSysdebugLogExportPolicyFsmStageRetry_Type()
)
cucsSysdebugLogExportPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStageRetry.setStatus("current")
_CucsSysdebugLogExportPolicyFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSysdebugLogExportPolicyFsmStageStageStatus_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmStageStageStatus = _CucsSysdebugLogExportPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 34, 1, 9),
    _CucsSysdebugLogExportPolicyFsmStageStageStatus_Type()
)
cucsSysdebugLogExportPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmStageStageStatus.setStatus("current")
_CucsSysdebugLogExportPolicyFsmTaskTable_Object = MibTable
cucsSysdebugLogExportPolicyFsmTaskTable = _CucsSysdebugLogExportPolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 35)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmTaskTable.setStatus("current")
_CucsSysdebugLogExportPolicyFsmTaskEntry_Object = MibTableRow
cucsSysdebugLogExportPolicyFsmTaskEntry = _CucsSysdebugLogExportPolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 35, 1)
)
cucsSysdebugLogExportPolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogExportPolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmTaskEntry.setStatus("current")
_CucsSysdebugLogExportPolicyFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogExportPolicyFsmTaskInstanceId_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmTaskInstanceId = _CucsSysdebugLogExportPolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 35, 1, 1),
    _CucsSysdebugLogExportPolicyFsmTaskInstanceId_Type()
)
cucsSysdebugLogExportPolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmTaskInstanceId.setStatus("current")
_CucsSysdebugLogExportPolicyFsmTaskDn_Type = CucsManagedObjectDn
_CucsSysdebugLogExportPolicyFsmTaskDn_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmTaskDn = _CucsSysdebugLogExportPolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 35, 1, 2),
    _CucsSysdebugLogExportPolicyFsmTaskDn_Type()
)
cucsSysdebugLogExportPolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmTaskDn.setStatus("current")
_CucsSysdebugLogExportPolicyFsmTaskRn_Type = SnmpAdminString
_CucsSysdebugLogExportPolicyFsmTaskRn_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmTaskRn = _CucsSysdebugLogExportPolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 35, 1, 3),
    _CucsSysdebugLogExportPolicyFsmTaskRn_Type()
)
cucsSysdebugLogExportPolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmTaskRn.setStatus("current")
_CucsSysdebugLogExportPolicyFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSysdebugLogExportPolicyFsmTaskCompletion_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmTaskCompletion = _CucsSysdebugLogExportPolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 35, 1, 4),
    _CucsSysdebugLogExportPolicyFsmTaskCompletion_Type()
)
cucsSysdebugLogExportPolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmTaskCompletion.setStatus("current")
_CucsSysdebugLogExportPolicyFsmTaskFlags_Type = CucsFsmFlags
_CucsSysdebugLogExportPolicyFsmTaskFlags_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmTaskFlags = _CucsSysdebugLogExportPolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 35, 1, 5),
    _CucsSysdebugLogExportPolicyFsmTaskFlags_Type()
)
cucsSysdebugLogExportPolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmTaskFlags.setStatus("current")
_CucsSysdebugLogExportPolicyFsmTaskItem_Type = CucsSysdebugLogExportPolicyFsmTaskItem
_CucsSysdebugLogExportPolicyFsmTaskItem_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmTaskItem = _CucsSysdebugLogExportPolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 35, 1, 6),
    _CucsSysdebugLogExportPolicyFsmTaskItem_Type()
)
cucsSysdebugLogExportPolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmTaskItem.setStatus("current")
_CucsSysdebugLogExportPolicyFsmTaskSeqId_Type = Gauge32
_CucsSysdebugLogExportPolicyFsmTaskSeqId_Object = MibTableColumn
cucsSysdebugLogExportPolicyFsmTaskSeqId = _CucsSysdebugLogExportPolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 35, 1, 7),
    _CucsSysdebugLogExportPolicyFsmTaskSeqId_Type()
)
cucsSysdebugLogExportPolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportPolicyFsmTaskSeqId.setStatus("current")
_CucsSysdebugLogExportStatusTable_Object = MibTable
cucsSysdebugLogExportStatusTable = _CucsSysdebugLogExportStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 36)
)
if mibBuilder.loadTexts:
    cucsSysdebugLogExportStatusTable.setStatus("current")
_CucsSysdebugLogExportStatusEntry_Object = MibTableRow
cucsSysdebugLogExportStatusEntry = _CucsSysdebugLogExportStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 36, 1)
)
cucsSysdebugLogExportStatusEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB", "cucsSysdebugLogExportStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysdebugLogExportStatusEntry.setStatus("current")
_CucsSysdebugLogExportStatusInstanceId_Type = CucsManagedObjectId
_CucsSysdebugLogExportStatusInstanceId_Object = MibTableColumn
cucsSysdebugLogExportStatusInstanceId = _CucsSysdebugLogExportStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 36, 1, 1),
    _CucsSysdebugLogExportStatusInstanceId_Type()
)
cucsSysdebugLogExportStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportStatusInstanceId.setStatus("current")
_CucsSysdebugLogExportStatusDn_Type = CucsManagedObjectDn
_CucsSysdebugLogExportStatusDn_Object = MibTableColumn
cucsSysdebugLogExportStatusDn = _CucsSysdebugLogExportStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 36, 1, 2),
    _CucsSysdebugLogExportStatusDn_Type()
)
cucsSysdebugLogExportStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportStatusDn.setStatus("current")
_CucsSysdebugLogExportStatusRn_Type = SnmpAdminString
_CucsSysdebugLogExportStatusRn_Object = MibTableColumn
cucsSysdebugLogExportStatusRn = _CucsSysdebugLogExportStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 36, 1, 3),
    _CucsSysdebugLogExportStatusRn_Type()
)
cucsSysdebugLogExportStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportStatusRn.setStatus("current")
_CucsSysdebugLogExportStatusExportFailureReason_Type = SnmpAdminString
_CucsSysdebugLogExportStatusExportFailureReason_Object = MibTableColumn
cucsSysdebugLogExportStatusExportFailureReason = _CucsSysdebugLogExportStatusExportFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 36, 1, 4),
    _CucsSysdebugLogExportStatusExportFailureReason_Type()
)
cucsSysdebugLogExportStatusExportFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportStatusExportFailureReason.setStatus("current")
_CucsSysdebugLogExportStatusExportStatus_Type = CucsSysdebugExportStatus
_CucsSysdebugLogExportStatusExportStatus_Object = MibTableColumn
cucsSysdebugLogExportStatusExportStatus = _CucsSysdebugLogExportStatusExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 36, 1, 5),
    _CucsSysdebugLogExportStatusExportStatus_Type()
)
cucsSysdebugLogExportStatusExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportStatusExportStatus.setStatus("current")
_CucsSysdebugLogExportStatusSwitchId_Type = CucsNetworkSwitchId
_CucsSysdebugLogExportStatusSwitchId_Object = MibTableColumn
cucsSysdebugLogExportStatusSwitchId = _CucsSysdebugLogExportStatusSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 47, 36, 1, 6),
    _CucsSysdebugLogExportStatusSwitchId_Type()
)
cucsSysdebugLogExportStatusSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysdebugLogExportStatusSwitchId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-SYSDEBUG-MIB",
    **{"cucsSysdebugObjects": cucsSysdebugObjects,
       "cucsSysdebugAutoCoreFileExportTargetTable": cucsSysdebugAutoCoreFileExportTargetTable,
       "cucsSysdebugAutoCoreFileExportTargetEntry": cucsSysdebugAutoCoreFileExportTargetEntry,
       "cucsSysdebugAutoCoreFileExportTargetInstanceId": cucsSysdebugAutoCoreFileExportTargetInstanceId,
       "cucsSysdebugAutoCoreFileExportTargetDn": cucsSysdebugAutoCoreFileExportTargetDn,
       "cucsSysdebugAutoCoreFileExportTargetRn": cucsSysdebugAutoCoreFileExportTargetRn,
       "cucsSysdebugAutoCoreFileExportTargetAdminState": cucsSysdebugAutoCoreFileExportTargetAdminState,
       "cucsSysdebugAutoCoreFileExportTargetDescr": cucsSysdebugAutoCoreFileExportTargetDescr,
       "cucsSysdebugAutoCoreFileExportTargetFsmDescr": cucsSysdebugAutoCoreFileExportTargetFsmDescr,
       "cucsSysdebugAutoCoreFileExportTargetFsmPrev": cucsSysdebugAutoCoreFileExportTargetFsmPrev,
       "cucsSysdebugAutoCoreFileExportTargetFsmProgr": cucsSysdebugAutoCoreFileExportTargetFsmProgr,
       "cucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode": cucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrCode,
       "cucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr": cucsSysdebugAutoCoreFileExportTargetFsmRmtInvErrDescr,
       "cucsSysdebugAutoCoreFileExportTargetFsmRmtInvRslt": cucsSysdebugAutoCoreFileExportTargetFsmRmtInvRslt,
       "cucsSysdebugAutoCoreFileExportTargetFsmStageDescr": cucsSysdebugAutoCoreFileExportTargetFsmStageDescr,
       "cucsSysdebugAutoCoreFileExportTargetFsmStamp": cucsSysdebugAutoCoreFileExportTargetFsmStamp,
       "cucsSysdebugAutoCoreFileExportTargetFsmStatus": cucsSysdebugAutoCoreFileExportTargetFsmStatus,
       "cucsSysdebugAutoCoreFileExportTargetFsmTry": cucsSysdebugAutoCoreFileExportTargetFsmTry,
       "cucsSysdebugAutoCoreFileExportTargetHostname": cucsSysdebugAutoCoreFileExportTargetHostname,
       "cucsSysdebugAutoCoreFileExportTargetIntId": cucsSysdebugAutoCoreFileExportTargetIntId,
       "cucsSysdebugAutoCoreFileExportTargetName": cucsSysdebugAutoCoreFileExportTargetName,
       "cucsSysdebugAutoCoreFileExportTargetPath": cucsSysdebugAutoCoreFileExportTargetPath,
       "cucsSysdebugAutoCoreFileExportTargetPort": cucsSysdebugAutoCoreFileExportTargetPort,
       "cucsSysdebugAutoCoreFileExportTargetPostAction": cucsSysdebugAutoCoreFileExportTargetPostAction,
       "cucsSysdebugAutoCoreFileExportTargetProto": cucsSysdebugAutoCoreFileExportTargetProto,
       "cucsSysdebugAutoCoreFileExportTargetExportFailureReason": cucsSysdebugAutoCoreFileExportTargetExportFailureReason,
       "cucsSysdebugAutoCoreFileExportTargetExportStatus": cucsSysdebugAutoCoreFileExportTargetExportStatus,
       "cucsSysdebugAutoCoreFileExportTargetPolicyLevel": cucsSysdebugAutoCoreFileExportTargetPolicyLevel,
       "cucsSysdebugAutoCoreFileExportTargetPolicyOwner": cucsSysdebugAutoCoreFileExportTargetPolicyOwner,
       "cucsSysdebugAutoCoreFileExportTargetFsmTaskTable": cucsSysdebugAutoCoreFileExportTargetFsmTaskTable,
       "cucsSysdebugAutoCoreFileExportTargetFsmTaskEntry": cucsSysdebugAutoCoreFileExportTargetFsmTaskEntry,
       "cucsSysdebugAutoCoreFileExportTargetFsmTaskInstanceId": cucsSysdebugAutoCoreFileExportTargetFsmTaskInstanceId,
       "cucsSysdebugAutoCoreFileExportTargetFsmTaskDn": cucsSysdebugAutoCoreFileExportTargetFsmTaskDn,
       "cucsSysdebugAutoCoreFileExportTargetFsmTaskRn": cucsSysdebugAutoCoreFileExportTargetFsmTaskRn,
       "cucsSysdebugAutoCoreFileExportTargetFsmTaskCompletion": cucsSysdebugAutoCoreFileExportTargetFsmTaskCompletion,
       "cucsSysdebugAutoCoreFileExportTargetFsmTaskFlags": cucsSysdebugAutoCoreFileExportTargetFsmTaskFlags,
       "cucsSysdebugAutoCoreFileExportTargetFsmTaskItem": cucsSysdebugAutoCoreFileExportTargetFsmTaskItem,
       "cucsSysdebugAutoCoreFileExportTargetFsmTaskSeqId": cucsSysdebugAutoCoreFileExportTargetFsmTaskSeqId,
       "cucsSysdebugBackupBehaviorTable": cucsSysdebugBackupBehaviorTable,
       "cucsSysdebugBackupBehaviorEntry": cucsSysdebugBackupBehaviorEntry,
       "cucsSysdebugBackupBehaviorInstanceId": cucsSysdebugBackupBehaviorInstanceId,
       "cucsSysdebugBackupBehaviorDn": cucsSysdebugBackupBehaviorDn,
       "cucsSysdebugBackupBehaviorRn": cucsSysdebugBackupBehaviorRn,
       "cucsSysdebugBackupBehaviorAction": cucsSysdebugBackupBehaviorAction,
       "cucsSysdebugBackupBehaviorClearOnBackup": cucsSysdebugBackupBehaviorClearOnBackup,
       "cucsSysdebugBackupBehaviorFormat": cucsSysdebugBackupBehaviorFormat,
       "cucsSysdebugBackupBehaviorHostname": cucsSysdebugBackupBehaviorHostname,
       "cucsSysdebugBackupBehaviorInterval": cucsSysdebugBackupBehaviorInterval,
       "cucsSysdebugBackupBehaviorProto": cucsSysdebugBackupBehaviorProto,
       "cucsSysdebugBackupBehaviorPwd": cucsSysdebugBackupBehaviorPwd,
       "cucsSysdebugBackupBehaviorRemotePath": cucsSysdebugBackupBehaviorRemotePath,
       "cucsSysdebugBackupBehaviorUser": cucsSysdebugBackupBehaviorUser,
       "cucsSysdebugCoreTable": cucsSysdebugCoreTable,
       "cucsSysdebugCoreEntry": cucsSysdebugCoreEntry,
       "cucsSysdebugCoreInstanceId": cucsSysdebugCoreInstanceId,
       "cucsSysdebugCoreDn": cucsSysdebugCoreDn,
       "cucsSysdebugCoreRn": cucsSysdebugCoreRn,
       "cucsSysdebugCoreDescr": cucsSysdebugCoreDescr,
       "cucsSysdebugCoreName": cucsSysdebugCoreName,
       "cucsSysdebugCoreSize": cucsSysdebugCoreSize,
       "cucsSysdebugCoreSwitchId": cucsSysdebugCoreSwitchId,
       "cucsSysdebugCoreTs": cucsSysdebugCoreTs,
       "cucsSysdebugCoreUri": cucsSysdebugCoreUri,
       "cucsSysdebugCoreAdminState": cucsSysdebugCoreAdminState,
       "cucsSysdebugCoreFsmDescr": cucsSysdebugCoreFsmDescr,
       "cucsSysdebugCoreFsmPrev": cucsSysdebugCoreFsmPrev,
       "cucsSysdebugCoreFsmProgr": cucsSysdebugCoreFsmProgr,
       "cucsSysdebugCoreFsmRmtInvErrCode": cucsSysdebugCoreFsmRmtInvErrCode,
       "cucsSysdebugCoreFsmRmtInvErrDescr": cucsSysdebugCoreFsmRmtInvErrDescr,
       "cucsSysdebugCoreFsmRmtInvRslt": cucsSysdebugCoreFsmRmtInvRslt,
       "cucsSysdebugCoreFsmStageDescr": cucsSysdebugCoreFsmStageDescr,
       "cucsSysdebugCoreFsmStamp": cucsSysdebugCoreFsmStamp,
       "cucsSysdebugCoreFsmStatus": cucsSysdebugCoreFsmStatus,
       "cucsSysdebugCoreFsmTry": cucsSysdebugCoreFsmTry,
       "cucsSysdebugCoreOperState": cucsSysdebugCoreOperState,
       "cucsSysdebugCoreFileRepositoryTable": cucsSysdebugCoreFileRepositoryTable,
       "cucsSysdebugCoreFileRepositoryEntry": cucsSysdebugCoreFileRepositoryEntry,
       "cucsSysdebugCoreFileRepositoryInstanceId": cucsSysdebugCoreFileRepositoryInstanceId,
       "cucsSysdebugCoreFileRepositoryDn": cucsSysdebugCoreFileRepositoryDn,
       "cucsSysdebugCoreFileRepositoryRn": cucsSysdebugCoreFileRepositoryRn,
       "cucsSysdebugEpTable": cucsSysdebugEpTable,
       "cucsSysdebugEpEntry": cucsSysdebugEpEntry,
       "cucsSysdebugEpInstanceId": cucsSysdebugEpInstanceId,
       "cucsSysdebugEpDn": cucsSysdebugEpDn,
       "cucsSysdebugEpRn": cucsSysdebugEpRn,
       "cucsSysdebugLogControlDestinationFileTable": cucsSysdebugLogControlDestinationFileTable,
       "cucsSysdebugLogControlDestinationFileEntry": cucsSysdebugLogControlDestinationFileEntry,
       "cucsSysdebugLogControlDestinationFileInstanceId": cucsSysdebugLogControlDestinationFileInstanceId,
       "cucsSysdebugLogControlDestinationFileDn": cucsSysdebugLogControlDestinationFileDn,
       "cucsSysdebugLogControlDestinationFileRn": cucsSysdebugLogControlDestinationFileRn,
       "cucsSysdebugLogControlDestinationFileBackupCount": cucsSysdebugLogControlDestinationFileBackupCount,
       "cucsSysdebugLogControlDestinationFileDefaultLevel": cucsSysdebugLogControlDestinationFileDefaultLevel,
       "cucsSysdebugLogControlDestinationFileDefaultSize": cucsSysdebugLogControlDestinationFileDefaultSize,
       "cucsSysdebugLogControlDestinationFileLevel": cucsSysdebugLogControlDestinationFileLevel,
       "cucsSysdebugLogControlDestinationFileSize": cucsSysdebugLogControlDestinationFileSize,
       "cucsSysdebugLogControlDestinationSyslogTable": cucsSysdebugLogControlDestinationSyslogTable,
       "cucsSysdebugLogControlDestinationSyslogEntry": cucsSysdebugLogControlDestinationSyslogEntry,
       "cucsSysdebugLogControlDestinationSyslogInstanceId": cucsSysdebugLogControlDestinationSyslogInstanceId,
       "cucsSysdebugLogControlDestinationSyslogDn": cucsSysdebugLogControlDestinationSyslogDn,
       "cucsSysdebugLogControlDestinationSyslogRn": cucsSysdebugLogControlDestinationSyslogRn,
       "cucsSysdebugLogControlDestinationSyslogDefaultLevel": cucsSysdebugLogControlDestinationSyslogDefaultLevel,
       "cucsSysdebugLogControlDestinationSyslogLevel": cucsSysdebugLogControlDestinationSyslogLevel,
       "cucsSysdebugLogControlDomainTable": cucsSysdebugLogControlDomainTable,
       "cucsSysdebugLogControlDomainEntry": cucsSysdebugLogControlDomainEntry,
       "cucsSysdebugLogControlDomainInstanceId": cucsSysdebugLogControlDomainInstanceId,
       "cucsSysdebugLogControlDomainDn": cucsSysdebugLogControlDomainDn,
       "cucsSysdebugLogControlDomainRn": cucsSysdebugLogControlDomainRn,
       "cucsSysdebugLogControlDomainLevel": cucsSysdebugLogControlDomainLevel,
       "cucsSysdebugLogControlDomainLevelFlag": cucsSysdebugLogControlDomainLevelFlag,
       "cucsSysdebugLogControlDomainName": cucsSysdebugLogControlDomainName,
       "cucsSysdebugLogControlDomainPersist": cucsSysdebugLogControlDomainPersist,
       "cucsSysdebugLogControlDomainReset": cucsSysdebugLogControlDomainReset,
       "cucsSysdebugLogControlEpTable": cucsSysdebugLogControlEpTable,
       "cucsSysdebugLogControlEpEntry": cucsSysdebugLogControlEpEntry,
       "cucsSysdebugLogControlEpInstanceId": cucsSysdebugLogControlEpInstanceId,
       "cucsSysdebugLogControlEpDn": cucsSysdebugLogControlEpDn,
       "cucsSysdebugLogControlEpRn": cucsSysdebugLogControlEpRn,
       "cucsSysdebugLogControlEpFsmDescr": cucsSysdebugLogControlEpFsmDescr,
       "cucsSysdebugLogControlEpFsmPrev": cucsSysdebugLogControlEpFsmPrev,
       "cucsSysdebugLogControlEpFsmProgr": cucsSysdebugLogControlEpFsmProgr,
       "cucsSysdebugLogControlEpFsmRmtInvErrCode": cucsSysdebugLogControlEpFsmRmtInvErrCode,
       "cucsSysdebugLogControlEpFsmRmtInvErrDescr": cucsSysdebugLogControlEpFsmRmtInvErrDescr,
       "cucsSysdebugLogControlEpFsmRmtInvRslt": cucsSysdebugLogControlEpFsmRmtInvRslt,
       "cucsSysdebugLogControlEpFsmStageDescr": cucsSysdebugLogControlEpFsmStageDescr,
       "cucsSysdebugLogControlEpFsmStamp": cucsSysdebugLogControlEpFsmStamp,
       "cucsSysdebugLogControlEpFsmStatus": cucsSysdebugLogControlEpFsmStatus,
       "cucsSysdebugLogControlEpFsmTry": cucsSysdebugLogControlEpFsmTry,
       "cucsSysdebugLogControlEpLevel": cucsSysdebugLogControlEpLevel,
       "cucsSysdebugLogControlEpLevelFlag": cucsSysdebugLogControlEpLevelFlag,
       "cucsSysdebugLogControlEpPersist": cucsSysdebugLogControlEpPersist,
       "cucsSysdebugLogControlEpReset": cucsSysdebugLogControlEpReset,
       "cucsSysdebugLogControlEpFsmTaskTable": cucsSysdebugLogControlEpFsmTaskTable,
       "cucsSysdebugLogControlEpFsmTaskEntry": cucsSysdebugLogControlEpFsmTaskEntry,
       "cucsSysdebugLogControlEpFsmTaskInstanceId": cucsSysdebugLogControlEpFsmTaskInstanceId,
       "cucsSysdebugLogControlEpFsmTaskDn": cucsSysdebugLogControlEpFsmTaskDn,
       "cucsSysdebugLogControlEpFsmTaskRn": cucsSysdebugLogControlEpFsmTaskRn,
       "cucsSysdebugLogControlEpFsmTaskCompletion": cucsSysdebugLogControlEpFsmTaskCompletion,
       "cucsSysdebugLogControlEpFsmTaskFlags": cucsSysdebugLogControlEpFsmTaskFlags,
       "cucsSysdebugLogControlEpFsmTaskItem": cucsSysdebugLogControlEpFsmTaskItem,
       "cucsSysdebugLogControlEpFsmTaskSeqId": cucsSysdebugLogControlEpFsmTaskSeqId,
       "cucsSysdebugLogControlModuleTable": cucsSysdebugLogControlModuleTable,
       "cucsSysdebugLogControlModuleEntry": cucsSysdebugLogControlModuleEntry,
       "cucsSysdebugLogControlModuleInstanceId": cucsSysdebugLogControlModuleInstanceId,
       "cucsSysdebugLogControlModuleDn": cucsSysdebugLogControlModuleDn,
       "cucsSysdebugLogControlModuleRn": cucsSysdebugLogControlModuleRn,
       "cucsSysdebugLogControlModuleDefaultLevel": cucsSysdebugLogControlModuleDefaultLevel,
       "cucsSysdebugLogControlModuleLevel": cucsSysdebugLogControlModuleLevel,
       "cucsSysdebugLogControlModuleName": cucsSysdebugLogControlModuleName,
       "cucsSysdebugLogControlModuleReset": cucsSysdebugLogControlModuleReset,
       "cucsSysdebugMEpLogTable": cucsSysdebugMEpLogTable,
       "cucsSysdebugMEpLogEntry": cucsSysdebugMEpLogEntry,
       "cucsSysdebugMEpLogInstanceId": cucsSysdebugMEpLogInstanceId,
       "cucsSysdebugMEpLogDn": cucsSysdebugMEpLogDn,
       "cucsSysdebugMEpLogRn": cucsSysdebugMEpLogRn,
       "cucsSysdebugMEpLogAdminState": cucsSysdebugMEpLogAdminState,
       "cucsSysdebugMEpLogCapacity": cucsSysdebugMEpLogCapacity,
       "cucsSysdebugMEpLogId": cucsSysdebugMEpLogId,
       "cucsSysdebugMEpLogLastUpdate": cucsSysdebugMEpLogLastUpdate,
       "cucsSysdebugMEpLogOperState": cucsSysdebugMEpLogOperState,
       "cucsSysdebugMEpLogType": cucsSysdebugMEpLogType,
       "cucsSysdebugMEpLogPolicyTable": cucsSysdebugMEpLogPolicyTable,
       "cucsSysdebugMEpLogPolicyEntry": cucsSysdebugMEpLogPolicyEntry,
       "cucsSysdebugMEpLogPolicyInstanceId": cucsSysdebugMEpLogPolicyInstanceId,
       "cucsSysdebugMEpLogPolicyDn": cucsSysdebugMEpLogPolicyDn,
       "cucsSysdebugMEpLogPolicyRn": cucsSysdebugMEpLogPolicyRn,
       "cucsSysdebugMEpLogPolicyDescr": cucsSysdebugMEpLogPolicyDescr,
       "cucsSysdebugMEpLogPolicyIntId": cucsSysdebugMEpLogPolicyIntId,
       "cucsSysdebugMEpLogPolicyName": cucsSysdebugMEpLogPolicyName,
       "cucsSysdebugMEpLogPolicyType": cucsSysdebugMEpLogPolicyType,
       "cucsSysdebugMEpLogPolicyPolicyLevel": cucsSysdebugMEpLogPolicyPolicyLevel,
       "cucsSysdebugMEpLogPolicyPolicyOwner": cucsSysdebugMEpLogPolicyPolicyOwner,
       "cucsSysdebugManualCoreFileExportTargetTable": cucsSysdebugManualCoreFileExportTargetTable,
       "cucsSysdebugManualCoreFileExportTargetEntry": cucsSysdebugManualCoreFileExportTargetEntry,
       "cucsSysdebugManualCoreFileExportTargetInstanceId": cucsSysdebugManualCoreFileExportTargetInstanceId,
       "cucsSysdebugManualCoreFileExportTargetDn": cucsSysdebugManualCoreFileExportTargetDn,
       "cucsSysdebugManualCoreFileExportTargetRn": cucsSysdebugManualCoreFileExportTargetRn,
       "cucsSysdebugManualCoreFileExportTargetAdminState": cucsSysdebugManualCoreFileExportTargetAdminState,
       "cucsSysdebugManualCoreFileExportTargetDescr": cucsSysdebugManualCoreFileExportTargetDescr,
       "cucsSysdebugManualCoreFileExportTargetFsmDescr": cucsSysdebugManualCoreFileExportTargetFsmDescr,
       "cucsSysdebugManualCoreFileExportTargetFsmPrev": cucsSysdebugManualCoreFileExportTargetFsmPrev,
       "cucsSysdebugManualCoreFileExportTargetFsmProgr": cucsSysdebugManualCoreFileExportTargetFsmProgr,
       "cucsSysdebugManualCoreFileExportTargetFsmRmtInvErrCode": cucsSysdebugManualCoreFileExportTargetFsmRmtInvErrCode,
       "cucsSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr": cucsSysdebugManualCoreFileExportTargetFsmRmtInvErrDescr,
       "cucsSysdebugManualCoreFileExportTargetFsmRmtInvRslt": cucsSysdebugManualCoreFileExportTargetFsmRmtInvRslt,
       "cucsSysdebugManualCoreFileExportTargetFsmStageDescr": cucsSysdebugManualCoreFileExportTargetFsmStageDescr,
       "cucsSysdebugManualCoreFileExportTargetFsmStamp": cucsSysdebugManualCoreFileExportTargetFsmStamp,
       "cucsSysdebugManualCoreFileExportTargetFsmStatus": cucsSysdebugManualCoreFileExportTargetFsmStatus,
       "cucsSysdebugManualCoreFileExportTargetFsmTry": cucsSysdebugManualCoreFileExportTargetFsmTry,
       "cucsSysdebugManualCoreFileExportTargetHostname": cucsSysdebugManualCoreFileExportTargetHostname,
       "cucsSysdebugManualCoreFileExportTargetIntId": cucsSysdebugManualCoreFileExportTargetIntId,
       "cucsSysdebugManualCoreFileExportTargetName": cucsSysdebugManualCoreFileExportTargetName,
       "cucsSysdebugManualCoreFileExportTargetPath": cucsSysdebugManualCoreFileExportTargetPath,
       "cucsSysdebugManualCoreFileExportTargetPort": cucsSysdebugManualCoreFileExportTargetPort,
       "cucsSysdebugManualCoreFileExportTargetPostAction": cucsSysdebugManualCoreFileExportTargetPostAction,
       "cucsSysdebugManualCoreFileExportTargetProto": cucsSysdebugManualCoreFileExportTargetProto,
       "cucsSysdebugManualCoreFileExportTargetExportFailureReason": cucsSysdebugManualCoreFileExportTargetExportFailureReason,
       "cucsSysdebugManualCoreFileExportTargetExportStatus": cucsSysdebugManualCoreFileExportTargetExportStatus,
       "cucsSysdebugManualCoreFileExportTargetPolicyLevel": cucsSysdebugManualCoreFileExportTargetPolicyLevel,
       "cucsSysdebugManualCoreFileExportTargetPolicyOwner": cucsSysdebugManualCoreFileExportTargetPolicyOwner,
       "cucsSysdebugManualCoreFileExportTargetFsmTaskTable": cucsSysdebugManualCoreFileExportTargetFsmTaskTable,
       "cucsSysdebugManualCoreFileExportTargetFsmTaskEntry": cucsSysdebugManualCoreFileExportTargetFsmTaskEntry,
       "cucsSysdebugManualCoreFileExportTargetFsmTaskInstanceId": cucsSysdebugManualCoreFileExportTargetFsmTaskInstanceId,
       "cucsSysdebugManualCoreFileExportTargetFsmTaskDn": cucsSysdebugManualCoreFileExportTargetFsmTaskDn,
       "cucsSysdebugManualCoreFileExportTargetFsmTaskRn": cucsSysdebugManualCoreFileExportTargetFsmTaskRn,
       "cucsSysdebugManualCoreFileExportTargetFsmTaskCompletion": cucsSysdebugManualCoreFileExportTargetFsmTaskCompletion,
       "cucsSysdebugManualCoreFileExportTargetFsmTaskFlags": cucsSysdebugManualCoreFileExportTargetFsmTaskFlags,
       "cucsSysdebugManualCoreFileExportTargetFsmTaskItem": cucsSysdebugManualCoreFileExportTargetFsmTaskItem,
       "cucsSysdebugManualCoreFileExportTargetFsmTaskSeqId": cucsSysdebugManualCoreFileExportTargetFsmTaskSeqId,
       "cucsSysdebugTechSupFileRepositoryTable": cucsSysdebugTechSupFileRepositoryTable,
       "cucsSysdebugTechSupFileRepositoryEntry": cucsSysdebugTechSupFileRepositoryEntry,
       "cucsSysdebugTechSupFileRepositoryInstanceId": cucsSysdebugTechSupFileRepositoryInstanceId,
       "cucsSysdebugTechSupFileRepositoryDn": cucsSysdebugTechSupFileRepositoryDn,
       "cucsSysdebugTechSupFileRepositoryRn": cucsSysdebugTechSupFileRepositoryRn,
       "cucsSysdebugTechSupportTable": cucsSysdebugTechSupportTable,
       "cucsSysdebugTechSupportEntry": cucsSysdebugTechSupportEntry,
       "cucsSysdebugTechSupportInstanceId": cucsSysdebugTechSupportInstanceId,
       "cucsSysdebugTechSupportDn": cucsSysdebugTechSupportDn,
       "cucsSysdebugTechSupportRn": cucsSysdebugTechSupportRn,
       "cucsSysdebugTechSupportAdminState": cucsSysdebugTechSupportAdminState,
       "cucsSysdebugTechSupportDescr": cucsSysdebugTechSupportDescr,
       "cucsSysdebugTechSupportFsmDescr": cucsSysdebugTechSupportFsmDescr,
       "cucsSysdebugTechSupportFsmPrev": cucsSysdebugTechSupportFsmPrev,
       "cucsSysdebugTechSupportFsmProgr": cucsSysdebugTechSupportFsmProgr,
       "cucsSysdebugTechSupportFsmRmtInvErrCode": cucsSysdebugTechSupportFsmRmtInvErrCode,
       "cucsSysdebugTechSupportFsmRmtInvErrDescr": cucsSysdebugTechSupportFsmRmtInvErrDescr,
       "cucsSysdebugTechSupportFsmRmtInvRslt": cucsSysdebugTechSupportFsmRmtInvRslt,
       "cucsSysdebugTechSupportFsmStageDescr": cucsSysdebugTechSupportFsmStageDescr,
       "cucsSysdebugTechSupportFsmStamp": cucsSysdebugTechSupportFsmStamp,
       "cucsSysdebugTechSupportFsmStatus": cucsSysdebugTechSupportFsmStatus,
       "cucsSysdebugTechSupportFsmTry": cucsSysdebugTechSupportFsmTry,
       "cucsSysdebugTechSupportName": cucsSysdebugTechSupportName,
       "cucsSysdebugTechSupportOperState": cucsSysdebugTechSupportOperState,
       "cucsSysdebugTechSupportSize": cucsSysdebugTechSupportSize,
       "cucsSysdebugTechSupportSwitchId": cucsSysdebugTechSupportSwitchId,
       "cucsSysdebugTechSupportTs": cucsSysdebugTechSupportTs,
       "cucsSysdebugTechSupportUri": cucsSysdebugTechSupportUri,
       "cucsSysdebugTechSupportCreationTS": cucsSysdebugTechSupportCreationTS,
       "cucsSysdebugTechSupportCmdOptTable": cucsSysdebugTechSupportCmdOptTable,
       "cucsSysdebugTechSupportCmdOptEntry": cucsSysdebugTechSupportCmdOptEntry,
       "cucsSysdebugTechSupportCmdOptInstanceId": cucsSysdebugTechSupportCmdOptInstanceId,
       "cucsSysdebugTechSupportCmdOptDn": cucsSysdebugTechSupportCmdOptDn,
       "cucsSysdebugTechSupportCmdOptRn": cucsSysdebugTechSupportCmdOptRn,
       "cucsSysdebugTechSupportCmdOptChassisCimcId": cucsSysdebugTechSupportCmdOptChassisCimcId,
       "cucsSysdebugTechSupportCmdOptChassisId": cucsSysdebugTechSupportCmdOptChassisId,
       "cucsSysdebugTechSupportCmdOptChassisIomId": cucsSysdebugTechSupportCmdOptChassisIomId,
       "cucsSysdebugTechSupportCmdOptCimcAdapterId": cucsSysdebugTechSupportCmdOptCimcAdapterId,
       "cucsSysdebugTechSupportCmdOptFabExtId": cucsSysdebugTechSupportCmdOptFabExtId,
       "cucsSysdebugTechSupportCmdOptMajorOptType": cucsSysdebugTechSupportCmdOptMajorOptType,
       "cucsSysdebugTechSupportCmdOptRackServerAdapterId": cucsSysdebugTechSupportCmdOptRackServerAdapterId,
       "cucsSysdebugTechSupportCmdOptRackServerId": cucsSysdebugTechSupportCmdOptRackServerId,
       "cucsSysdebugTechSupportCmdOptCartridgeCIMCId": cucsSysdebugTechSupportCmdOptCartridgeCIMCId,
       "cucsSysdebugTechSupportCmdOptChassisCartridgeId": cucsSysdebugTechSupportCmdOptChassisCartridgeId,
       "cucsSysdebugTechSupportCmdOptServerIdList": cucsSysdebugTechSupportCmdOptServerIdList,
       "cucsSysdebugTechSupportCmdOptCommandOptions": cucsSysdebugTechSupportCmdOptCommandOptions,
       "cucsSysdebugTechSupportFsmTaskTable": cucsSysdebugTechSupportFsmTaskTable,
       "cucsSysdebugTechSupportFsmTaskEntry": cucsSysdebugTechSupportFsmTaskEntry,
       "cucsSysdebugTechSupportFsmTaskInstanceId": cucsSysdebugTechSupportFsmTaskInstanceId,
       "cucsSysdebugTechSupportFsmTaskDn": cucsSysdebugTechSupportFsmTaskDn,
       "cucsSysdebugTechSupportFsmTaskRn": cucsSysdebugTechSupportFsmTaskRn,
       "cucsSysdebugTechSupportFsmTaskCompletion": cucsSysdebugTechSupportFsmTaskCompletion,
       "cucsSysdebugTechSupportFsmTaskFlags": cucsSysdebugTechSupportFsmTaskFlags,
       "cucsSysdebugTechSupportFsmTaskItem": cucsSysdebugTechSupportFsmTaskItem,
       "cucsSysdebugTechSupportFsmTaskSeqId": cucsSysdebugTechSupportFsmTaskSeqId,
       "cucsSysdebugCoreFsmTaskTable": cucsSysdebugCoreFsmTaskTable,
       "cucsSysdebugCoreFsmTaskEntry": cucsSysdebugCoreFsmTaskEntry,
       "cucsSysdebugCoreFsmTaskInstanceId": cucsSysdebugCoreFsmTaskInstanceId,
       "cucsSysdebugCoreFsmTaskDn": cucsSysdebugCoreFsmTaskDn,
       "cucsSysdebugCoreFsmTaskRn": cucsSysdebugCoreFsmTaskRn,
       "cucsSysdebugCoreFsmTaskCompletion": cucsSysdebugCoreFsmTaskCompletion,
       "cucsSysdebugCoreFsmTaskFlags": cucsSysdebugCoreFsmTaskFlags,
       "cucsSysdebugCoreFsmTaskItem": cucsSysdebugCoreFsmTaskItem,
       "cucsSysdebugCoreFsmTaskSeqId": cucsSysdebugCoreFsmTaskSeqId,
       "cucsSysdebugAutoCoreFileExportTargetFsmTable": cucsSysdebugAutoCoreFileExportTargetFsmTable,
       "cucsSysdebugAutoCoreFileExportTargetFsmEntry": cucsSysdebugAutoCoreFileExportTargetFsmEntry,
       "cucsSysdebugAutoCoreFileExportTargetFsmInstanceId": cucsSysdebugAutoCoreFileExportTargetFsmInstanceId,
       "cucsSysdebugAutoCoreFileExportTargetFsmDn": cucsSysdebugAutoCoreFileExportTargetFsmDn,
       "cucsSysdebugAutoCoreFileExportTargetFsmRn": cucsSysdebugAutoCoreFileExportTargetFsmRn,
       "cucsSysdebugAutoCoreFileExportTargetFsmCompletionTime": cucsSysdebugAutoCoreFileExportTargetFsmCompletionTime,
       "cucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm": cucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm,
       "cucsSysdebugAutoCoreFileExportTargetFsmDescrData": cucsSysdebugAutoCoreFileExportTargetFsmDescrData,
       "cucsSysdebugAutoCoreFileExportTargetFsmFsmStatus": cucsSysdebugAutoCoreFileExportTargetFsmFsmStatus,
       "cucsSysdebugAutoCoreFileExportTargetFsmProgress": cucsSysdebugAutoCoreFileExportTargetFsmProgress,
       "cucsSysdebugAutoCoreFileExportTargetFsmRmtErrCode": cucsSysdebugAutoCoreFileExportTargetFsmRmtErrCode,
       "cucsSysdebugAutoCoreFileExportTargetFsmRmtErrDescr": cucsSysdebugAutoCoreFileExportTargetFsmRmtErrDescr,
       "cucsSysdebugAutoCoreFileExportTargetFsmRmtRslt": cucsSysdebugAutoCoreFileExportTargetFsmRmtRslt,
       "cucsSysdebugAutoCoreFileExportTargetFsmStageTable": cucsSysdebugAutoCoreFileExportTargetFsmStageTable,
       "cucsSysdebugAutoCoreFileExportTargetFsmStageEntry": cucsSysdebugAutoCoreFileExportTargetFsmStageEntry,
       "cucsSysdebugAutoCoreFileExportTargetFsmStageInstanceId": cucsSysdebugAutoCoreFileExportTargetFsmStageInstanceId,
       "cucsSysdebugAutoCoreFileExportTargetFsmStageDn": cucsSysdebugAutoCoreFileExportTargetFsmStageDn,
       "cucsSysdebugAutoCoreFileExportTargetFsmStageRn": cucsSysdebugAutoCoreFileExportTargetFsmStageRn,
       "cucsSysdebugAutoCoreFileExportTargetFsmStageDescrData": cucsSysdebugAutoCoreFileExportTargetFsmStageDescrData,
       "cucsSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime": cucsSysdebugAutoCoreFileExportTargetFsmStageLastUpdateTime,
       "cucsSysdebugAutoCoreFileExportTargetFsmStageName": cucsSysdebugAutoCoreFileExportTargetFsmStageName,
       "cucsSysdebugAutoCoreFileExportTargetFsmStageOrder": cucsSysdebugAutoCoreFileExportTargetFsmStageOrder,
       "cucsSysdebugAutoCoreFileExportTargetFsmStageRetry": cucsSysdebugAutoCoreFileExportTargetFsmStageRetry,
       "cucsSysdebugAutoCoreFileExportTargetFsmStageStageStatus": cucsSysdebugAutoCoreFileExportTargetFsmStageStageStatus,
       "cucsSysdebugCoreFsmTable": cucsSysdebugCoreFsmTable,
       "cucsSysdebugCoreFsmEntry": cucsSysdebugCoreFsmEntry,
       "cucsSysdebugCoreFsmInstanceId": cucsSysdebugCoreFsmInstanceId,
       "cucsSysdebugCoreFsmDn": cucsSysdebugCoreFsmDn,
       "cucsSysdebugCoreFsmRn": cucsSysdebugCoreFsmRn,
       "cucsSysdebugCoreFsmCompletionTime": cucsSysdebugCoreFsmCompletionTime,
       "cucsSysdebugCoreFsmCurrentFsm": cucsSysdebugCoreFsmCurrentFsm,
       "cucsSysdebugCoreFsmDescrData": cucsSysdebugCoreFsmDescrData,
       "cucsSysdebugCoreFsmFsmStatus": cucsSysdebugCoreFsmFsmStatus,
       "cucsSysdebugCoreFsmProgress": cucsSysdebugCoreFsmProgress,
       "cucsSysdebugCoreFsmRmtErrCode": cucsSysdebugCoreFsmRmtErrCode,
       "cucsSysdebugCoreFsmRmtErrDescr": cucsSysdebugCoreFsmRmtErrDescr,
       "cucsSysdebugCoreFsmRmtRslt": cucsSysdebugCoreFsmRmtRslt,
       "cucsSysdebugCoreFsmStageTable": cucsSysdebugCoreFsmStageTable,
       "cucsSysdebugCoreFsmStageEntry": cucsSysdebugCoreFsmStageEntry,
       "cucsSysdebugCoreFsmStageInstanceId": cucsSysdebugCoreFsmStageInstanceId,
       "cucsSysdebugCoreFsmStageDn": cucsSysdebugCoreFsmStageDn,
       "cucsSysdebugCoreFsmStageRn": cucsSysdebugCoreFsmStageRn,
       "cucsSysdebugCoreFsmStageDescrData": cucsSysdebugCoreFsmStageDescrData,
       "cucsSysdebugCoreFsmStageLastUpdateTime": cucsSysdebugCoreFsmStageLastUpdateTime,
       "cucsSysdebugCoreFsmStageName": cucsSysdebugCoreFsmStageName,
       "cucsSysdebugCoreFsmStageOrder": cucsSysdebugCoreFsmStageOrder,
       "cucsSysdebugCoreFsmStageRetry": cucsSysdebugCoreFsmStageRetry,
       "cucsSysdebugCoreFsmStageStageStatus": cucsSysdebugCoreFsmStageStageStatus,
       "cucsSysdebugLogControlEpFsmTable": cucsSysdebugLogControlEpFsmTable,
       "cucsSysdebugLogControlEpFsmEntry": cucsSysdebugLogControlEpFsmEntry,
       "cucsSysdebugLogControlEpFsmInstanceId": cucsSysdebugLogControlEpFsmInstanceId,
       "cucsSysdebugLogControlEpFsmDn": cucsSysdebugLogControlEpFsmDn,
       "cucsSysdebugLogControlEpFsmRn": cucsSysdebugLogControlEpFsmRn,
       "cucsSysdebugLogControlEpFsmCompletionTime": cucsSysdebugLogControlEpFsmCompletionTime,
       "cucsSysdebugLogControlEpFsmCurrentFsm": cucsSysdebugLogControlEpFsmCurrentFsm,
       "cucsSysdebugLogControlEpFsmDescrData": cucsSysdebugLogControlEpFsmDescrData,
       "cucsSysdebugLogControlEpFsmFsmStatus": cucsSysdebugLogControlEpFsmFsmStatus,
       "cucsSysdebugLogControlEpFsmProgress": cucsSysdebugLogControlEpFsmProgress,
       "cucsSysdebugLogControlEpFsmRmtErrCode": cucsSysdebugLogControlEpFsmRmtErrCode,
       "cucsSysdebugLogControlEpFsmRmtErrDescr": cucsSysdebugLogControlEpFsmRmtErrDescr,
       "cucsSysdebugLogControlEpFsmRmtRslt": cucsSysdebugLogControlEpFsmRmtRslt,
       "cucsSysdebugLogControlEpFsmStageTable": cucsSysdebugLogControlEpFsmStageTable,
       "cucsSysdebugLogControlEpFsmStageEntry": cucsSysdebugLogControlEpFsmStageEntry,
       "cucsSysdebugLogControlEpFsmStageInstanceId": cucsSysdebugLogControlEpFsmStageInstanceId,
       "cucsSysdebugLogControlEpFsmStageDn": cucsSysdebugLogControlEpFsmStageDn,
       "cucsSysdebugLogControlEpFsmStageRn": cucsSysdebugLogControlEpFsmStageRn,
       "cucsSysdebugLogControlEpFsmStageDescrData": cucsSysdebugLogControlEpFsmStageDescrData,
       "cucsSysdebugLogControlEpFsmStageLastUpdateTime": cucsSysdebugLogControlEpFsmStageLastUpdateTime,
       "cucsSysdebugLogControlEpFsmStageName": cucsSysdebugLogControlEpFsmStageName,
       "cucsSysdebugLogControlEpFsmStageOrder": cucsSysdebugLogControlEpFsmStageOrder,
       "cucsSysdebugLogControlEpFsmStageRetry": cucsSysdebugLogControlEpFsmStageRetry,
       "cucsSysdebugLogControlEpFsmStageStageStatus": cucsSysdebugLogControlEpFsmStageStageStatus,
       "cucsSysdebugManualCoreFileExportTargetFsmTable": cucsSysdebugManualCoreFileExportTargetFsmTable,
       "cucsSysdebugManualCoreFileExportTargetFsmEntry": cucsSysdebugManualCoreFileExportTargetFsmEntry,
       "cucsSysdebugManualCoreFileExportTargetFsmInstanceId": cucsSysdebugManualCoreFileExportTargetFsmInstanceId,
       "cucsSysdebugManualCoreFileExportTargetFsmDn": cucsSysdebugManualCoreFileExportTargetFsmDn,
       "cucsSysdebugManualCoreFileExportTargetFsmRn": cucsSysdebugManualCoreFileExportTargetFsmRn,
       "cucsSysdebugManualCoreFileExportTargetFsmCompletionTime": cucsSysdebugManualCoreFileExportTargetFsmCompletionTime,
       "cucsSysdebugManualCoreFileExportTargetFsmCurrentFsm": cucsSysdebugManualCoreFileExportTargetFsmCurrentFsm,
       "cucsSysdebugManualCoreFileExportTargetFsmDescrData": cucsSysdebugManualCoreFileExportTargetFsmDescrData,
       "cucsSysdebugManualCoreFileExportTargetFsmFsmStatus": cucsSysdebugManualCoreFileExportTargetFsmFsmStatus,
       "cucsSysdebugManualCoreFileExportTargetFsmProgress": cucsSysdebugManualCoreFileExportTargetFsmProgress,
       "cucsSysdebugManualCoreFileExportTargetFsmRmtErrCode": cucsSysdebugManualCoreFileExportTargetFsmRmtErrCode,
       "cucsSysdebugManualCoreFileExportTargetFsmRmtErrDescr": cucsSysdebugManualCoreFileExportTargetFsmRmtErrDescr,
       "cucsSysdebugManualCoreFileExportTargetFsmRmtRslt": cucsSysdebugManualCoreFileExportTargetFsmRmtRslt,
       "cucsSysdebugManualCoreFileExportTargetFsmStageTable": cucsSysdebugManualCoreFileExportTargetFsmStageTable,
       "cucsSysdebugManualCoreFileExportTargetFsmStageEntry": cucsSysdebugManualCoreFileExportTargetFsmStageEntry,
       "cucsSysdebugManualCoreFileExportTargetFsmStageInstanceId": cucsSysdebugManualCoreFileExportTargetFsmStageInstanceId,
       "cucsSysdebugManualCoreFileExportTargetFsmStageDn": cucsSysdebugManualCoreFileExportTargetFsmStageDn,
       "cucsSysdebugManualCoreFileExportTargetFsmStageRn": cucsSysdebugManualCoreFileExportTargetFsmStageRn,
       "cucsSysdebugManualCoreFileExportTargetFsmStageDescrData": cucsSysdebugManualCoreFileExportTargetFsmStageDescrData,
       "cucsSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime": cucsSysdebugManualCoreFileExportTargetFsmStageLastUpdateTime,
       "cucsSysdebugManualCoreFileExportTargetFsmStageName": cucsSysdebugManualCoreFileExportTargetFsmStageName,
       "cucsSysdebugManualCoreFileExportTargetFsmStageOrder": cucsSysdebugManualCoreFileExportTargetFsmStageOrder,
       "cucsSysdebugManualCoreFileExportTargetFsmStageRetry": cucsSysdebugManualCoreFileExportTargetFsmStageRetry,
       "cucsSysdebugManualCoreFileExportTargetFsmStageStageStatus": cucsSysdebugManualCoreFileExportTargetFsmStageStageStatus,
       "cucsSysdebugTechSupportFsmTable": cucsSysdebugTechSupportFsmTable,
       "cucsSysdebugTechSupportFsmEntry": cucsSysdebugTechSupportFsmEntry,
       "cucsSysdebugTechSupportFsmInstanceId": cucsSysdebugTechSupportFsmInstanceId,
       "cucsSysdebugTechSupportFsmDn": cucsSysdebugTechSupportFsmDn,
       "cucsSysdebugTechSupportFsmRn": cucsSysdebugTechSupportFsmRn,
       "cucsSysdebugTechSupportFsmCompletionTime": cucsSysdebugTechSupportFsmCompletionTime,
       "cucsSysdebugTechSupportFsmCurrentFsm": cucsSysdebugTechSupportFsmCurrentFsm,
       "cucsSysdebugTechSupportFsmDescrData": cucsSysdebugTechSupportFsmDescrData,
       "cucsSysdebugTechSupportFsmFsmStatus": cucsSysdebugTechSupportFsmFsmStatus,
       "cucsSysdebugTechSupportFsmProgress": cucsSysdebugTechSupportFsmProgress,
       "cucsSysdebugTechSupportFsmRmtErrCode": cucsSysdebugTechSupportFsmRmtErrCode,
       "cucsSysdebugTechSupportFsmRmtErrDescr": cucsSysdebugTechSupportFsmRmtErrDescr,
       "cucsSysdebugTechSupportFsmRmtRslt": cucsSysdebugTechSupportFsmRmtRslt,
       "cucsSysdebugTechSupportFsmStageTable": cucsSysdebugTechSupportFsmStageTable,
       "cucsSysdebugTechSupportFsmStageEntry": cucsSysdebugTechSupportFsmStageEntry,
       "cucsSysdebugTechSupportFsmStageInstanceId": cucsSysdebugTechSupportFsmStageInstanceId,
       "cucsSysdebugTechSupportFsmStageDn": cucsSysdebugTechSupportFsmStageDn,
       "cucsSysdebugTechSupportFsmStageRn": cucsSysdebugTechSupportFsmStageRn,
       "cucsSysdebugTechSupportFsmStageDescrData": cucsSysdebugTechSupportFsmStageDescrData,
       "cucsSysdebugTechSupportFsmStageLastUpdateTime": cucsSysdebugTechSupportFsmStageLastUpdateTime,
       "cucsSysdebugTechSupportFsmStageName": cucsSysdebugTechSupportFsmStageName,
       "cucsSysdebugTechSupportFsmStageOrder": cucsSysdebugTechSupportFsmStageOrder,
       "cucsSysdebugTechSupportFsmStageRetry": cucsSysdebugTechSupportFsmStageRetry,
       "cucsSysdebugTechSupportFsmStageStageStatus": cucsSysdebugTechSupportFsmStageStageStatus,
       "cucsSysdebugLogExportPolicyTable": cucsSysdebugLogExportPolicyTable,
       "cucsSysdebugLogExportPolicyEntry": cucsSysdebugLogExportPolicyEntry,
       "cucsSysdebugLogExportPolicyInstanceId": cucsSysdebugLogExportPolicyInstanceId,
       "cucsSysdebugLogExportPolicyDn": cucsSysdebugLogExportPolicyDn,
       "cucsSysdebugLogExportPolicyRn": cucsSysdebugLogExportPolicyRn,
       "cucsSysdebugLogExportPolicyAdminState": cucsSysdebugLogExportPolicyAdminState,
       "cucsSysdebugLogExportPolicyDescr": cucsSysdebugLogExportPolicyDescr,
       "cucsSysdebugLogExportPolicyFsmDescr": cucsSysdebugLogExportPolicyFsmDescr,
       "cucsSysdebugLogExportPolicyFsmPrev": cucsSysdebugLogExportPolicyFsmPrev,
       "cucsSysdebugLogExportPolicyFsmProgr": cucsSysdebugLogExportPolicyFsmProgr,
       "cucsSysdebugLogExportPolicyFsmRmtInvErrCode": cucsSysdebugLogExportPolicyFsmRmtInvErrCode,
       "cucsSysdebugLogExportPolicyFsmRmtInvErrDescr": cucsSysdebugLogExportPolicyFsmRmtInvErrDescr,
       "cucsSysdebugLogExportPolicyFsmRmtInvRslt": cucsSysdebugLogExportPolicyFsmRmtInvRslt,
       "cucsSysdebugLogExportPolicyFsmStageDescr": cucsSysdebugLogExportPolicyFsmStageDescr,
       "cucsSysdebugLogExportPolicyFsmStamp": cucsSysdebugLogExportPolicyFsmStamp,
       "cucsSysdebugLogExportPolicyFsmStatus": cucsSysdebugLogExportPolicyFsmStatus,
       "cucsSysdebugLogExportPolicyFsmTry": cucsSysdebugLogExportPolicyFsmTry,
       "cucsSysdebugLogExportPolicyHostname": cucsSysdebugLogExportPolicyHostname,
       "cucsSysdebugLogExportPolicyIntId": cucsSysdebugLogExportPolicyIntId,
       "cucsSysdebugLogExportPolicyName": cucsSysdebugLogExportPolicyName,
       "cucsSysdebugLogExportPolicyPasswordlessSsh": cucsSysdebugLogExportPolicyPasswordlessSsh,
       "cucsSysdebugLogExportPolicyPath": cucsSysdebugLogExportPolicyPath,
       "cucsSysdebugLogExportPolicyPolicyLevel": cucsSysdebugLogExportPolicyPolicyLevel,
       "cucsSysdebugLogExportPolicyPolicyOwner": cucsSysdebugLogExportPolicyPolicyOwner,
       "cucsSysdebugLogExportPolicyPostAction": cucsSysdebugLogExportPolicyPostAction,
       "cucsSysdebugLogExportPolicyProto": cucsSysdebugLogExportPolicyProto,
       "cucsSysdebugLogExportPolicyPwd": cucsSysdebugLogExportPolicyPwd,
       "cucsSysdebugLogExportPolicyUser": cucsSysdebugLogExportPolicyUser,
       "cucsSysdebugLogExportPolicyFsmTable": cucsSysdebugLogExportPolicyFsmTable,
       "cucsSysdebugLogExportPolicyFsmEntry": cucsSysdebugLogExportPolicyFsmEntry,
       "cucsSysdebugLogExportPolicyFsmInstanceId": cucsSysdebugLogExportPolicyFsmInstanceId,
       "cucsSysdebugLogExportPolicyFsmDn": cucsSysdebugLogExportPolicyFsmDn,
       "cucsSysdebugLogExportPolicyFsmRn": cucsSysdebugLogExportPolicyFsmRn,
       "cucsSysdebugLogExportPolicyFsmCompletionTime": cucsSysdebugLogExportPolicyFsmCompletionTime,
       "cucsSysdebugLogExportPolicyFsmCurrentFsm": cucsSysdebugLogExportPolicyFsmCurrentFsm,
       "cucsSysdebugLogExportPolicyFsmDescrData": cucsSysdebugLogExportPolicyFsmDescrData,
       "cucsSysdebugLogExportPolicyFsmFsmStatus": cucsSysdebugLogExportPolicyFsmFsmStatus,
       "cucsSysdebugLogExportPolicyFsmProgress": cucsSysdebugLogExportPolicyFsmProgress,
       "cucsSysdebugLogExportPolicyFsmRmtErrCode": cucsSysdebugLogExportPolicyFsmRmtErrCode,
       "cucsSysdebugLogExportPolicyFsmRmtErrDescr": cucsSysdebugLogExportPolicyFsmRmtErrDescr,
       "cucsSysdebugLogExportPolicyFsmRmtRslt": cucsSysdebugLogExportPolicyFsmRmtRslt,
       "cucsSysdebugLogExportPolicyFsmStageTable": cucsSysdebugLogExportPolicyFsmStageTable,
       "cucsSysdebugLogExportPolicyFsmStageEntry": cucsSysdebugLogExportPolicyFsmStageEntry,
       "cucsSysdebugLogExportPolicyFsmStageInstanceId": cucsSysdebugLogExportPolicyFsmStageInstanceId,
       "cucsSysdebugLogExportPolicyFsmStageDn": cucsSysdebugLogExportPolicyFsmStageDn,
       "cucsSysdebugLogExportPolicyFsmStageRn": cucsSysdebugLogExportPolicyFsmStageRn,
       "cucsSysdebugLogExportPolicyFsmStageDescrData": cucsSysdebugLogExportPolicyFsmStageDescrData,
       "cucsSysdebugLogExportPolicyFsmStageLastUpdateTime": cucsSysdebugLogExportPolicyFsmStageLastUpdateTime,
       "cucsSysdebugLogExportPolicyFsmStageName": cucsSysdebugLogExportPolicyFsmStageName,
       "cucsSysdebugLogExportPolicyFsmStageOrder": cucsSysdebugLogExportPolicyFsmStageOrder,
       "cucsSysdebugLogExportPolicyFsmStageRetry": cucsSysdebugLogExportPolicyFsmStageRetry,
       "cucsSysdebugLogExportPolicyFsmStageStageStatus": cucsSysdebugLogExportPolicyFsmStageStageStatus,
       "cucsSysdebugLogExportPolicyFsmTaskTable": cucsSysdebugLogExportPolicyFsmTaskTable,
       "cucsSysdebugLogExportPolicyFsmTaskEntry": cucsSysdebugLogExportPolicyFsmTaskEntry,
       "cucsSysdebugLogExportPolicyFsmTaskInstanceId": cucsSysdebugLogExportPolicyFsmTaskInstanceId,
       "cucsSysdebugLogExportPolicyFsmTaskDn": cucsSysdebugLogExportPolicyFsmTaskDn,
       "cucsSysdebugLogExportPolicyFsmTaskRn": cucsSysdebugLogExportPolicyFsmTaskRn,
       "cucsSysdebugLogExportPolicyFsmTaskCompletion": cucsSysdebugLogExportPolicyFsmTaskCompletion,
       "cucsSysdebugLogExportPolicyFsmTaskFlags": cucsSysdebugLogExportPolicyFsmTaskFlags,
       "cucsSysdebugLogExportPolicyFsmTaskItem": cucsSysdebugLogExportPolicyFsmTaskItem,
       "cucsSysdebugLogExportPolicyFsmTaskSeqId": cucsSysdebugLogExportPolicyFsmTaskSeqId,
       "cucsSysdebugLogExportStatusTable": cucsSysdebugLogExportStatusTable,
       "cucsSysdebugLogExportStatusEntry": cucsSysdebugLogExportStatusEntry,
       "cucsSysdebugLogExportStatusInstanceId": cucsSysdebugLogExportStatusInstanceId,
       "cucsSysdebugLogExportStatusDn": cucsSysdebugLogExportStatusDn,
       "cucsSysdebugLogExportStatusRn": cucsSysdebugLogExportStatusRn,
       "cucsSysdebugLogExportStatusExportFailureReason": cucsSysdebugLogExportStatusExportFailureReason,
       "cucsSysdebugLogExportStatusExportStatus": cucsSysdebugLogExportStatusExportStatus,
       "cucsSysdebugLogExportStatusSwitchId": cucsSysdebugLogExportStatusSwitchId}
)
