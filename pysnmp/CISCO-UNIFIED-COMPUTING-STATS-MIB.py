# SNMP MIB module (CISCO-UNIFIED-COMPUTING-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:20 2024
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
 CucsConditionSeverity,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsPolicyPolicyOwner,
 CucsStatsCollectionDomain,
 CucsStatsCollectionInterval,
 CucsStatsCollectionPolicyFsmCurrentFsm,
 CucsStatsCollectionPolicyFsmStageName,
 CucsStatsCollectionPolicyFsmTaskItem,
 CucsStatsReportingInterval,
 CucsStatsThr32DefinitionPropType,
 CucsStatsThr32ValuePropType,
 CucsStatsThr64DefinitionPropType,
 CucsStatsThr64ValuePropType,
 CucsStatsThrFloatDefinitionPropType,
 CucsStatsThrFloatValuePropType,
 CucsStatsThresholdDefinitionAutoRecovery,
 CucsStatsThresholdDirection) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsConditionSeverity",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsPolicyPolicyOwner",
    "CucsStatsCollectionDomain",
    "CucsStatsCollectionInterval",
    "CucsStatsCollectionPolicyFsmCurrentFsm",
    "CucsStatsCollectionPolicyFsmStageName",
    "CucsStatsCollectionPolicyFsmTaskItem",
    "CucsStatsReportingInterval",
    "CucsStatsThr32DefinitionPropType",
    "CucsStatsThr32ValuePropType",
    "CucsStatsThr64DefinitionPropType",
    "CucsStatsThr64ValuePropType",
    "CucsStatsThrFloatDefinitionPropType",
    "CucsStatsThrFloatValuePropType",
    "CucsStatsThresholdDefinitionAutoRecovery",
    "CucsStatsThresholdDirection")

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

cucsStatsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsStatsCollectionPolicyTable_Object = MibTable
cucsStatsCollectionPolicyTable = _CucsStatsCollectionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1)
)
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyTable.setStatus("current")
_CucsStatsCollectionPolicyEntry_Object = MibTableRow
cucsStatsCollectionPolicyEntry = _CucsStatsCollectionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1)
)
cucsStatsCollectionPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsCollectionPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyEntry.setStatus("current")
_CucsStatsCollectionPolicyInstanceId_Type = CucsManagedObjectId
_CucsStatsCollectionPolicyInstanceId_Object = MibTableColumn
cucsStatsCollectionPolicyInstanceId = _CucsStatsCollectionPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 1),
    _CucsStatsCollectionPolicyInstanceId_Type()
)
cucsStatsCollectionPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyInstanceId.setStatus("current")
_CucsStatsCollectionPolicyDn_Type = CucsManagedObjectDn
_CucsStatsCollectionPolicyDn_Object = MibTableColumn
cucsStatsCollectionPolicyDn = _CucsStatsCollectionPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 2),
    _CucsStatsCollectionPolicyDn_Type()
)
cucsStatsCollectionPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyDn.setStatus("current")
_CucsStatsCollectionPolicyRn_Type = SnmpAdminString
_CucsStatsCollectionPolicyRn_Object = MibTableColumn
cucsStatsCollectionPolicyRn = _CucsStatsCollectionPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 3),
    _CucsStatsCollectionPolicyRn_Type()
)
cucsStatsCollectionPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyRn.setStatus("current")
_CucsStatsCollectionPolicyCollectionInterval_Type = CucsStatsCollectionInterval
_CucsStatsCollectionPolicyCollectionInterval_Object = MibTableColumn
cucsStatsCollectionPolicyCollectionInterval = _CucsStatsCollectionPolicyCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 4),
    _CucsStatsCollectionPolicyCollectionInterval_Type()
)
cucsStatsCollectionPolicyCollectionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyCollectionInterval.setStatus("current")
_CucsStatsCollectionPolicyFsmDescr_Type = SnmpAdminString
_CucsStatsCollectionPolicyFsmDescr_Object = MibTableColumn
cucsStatsCollectionPolicyFsmDescr = _CucsStatsCollectionPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 5),
    _CucsStatsCollectionPolicyFsmDescr_Type()
)
cucsStatsCollectionPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmDescr.setStatus("current")
_CucsStatsCollectionPolicyFsmPrev_Type = SnmpAdminString
_CucsStatsCollectionPolicyFsmPrev_Object = MibTableColumn
cucsStatsCollectionPolicyFsmPrev = _CucsStatsCollectionPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 6),
    _CucsStatsCollectionPolicyFsmPrev_Type()
)
cucsStatsCollectionPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmPrev.setStatus("current")
_CucsStatsCollectionPolicyFsmProgr_Type = Gauge32
_CucsStatsCollectionPolicyFsmProgr_Object = MibTableColumn
cucsStatsCollectionPolicyFsmProgr = _CucsStatsCollectionPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 7),
    _CucsStatsCollectionPolicyFsmProgr_Type()
)
cucsStatsCollectionPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmProgr.setStatus("current")
_CucsStatsCollectionPolicyFsmRmtInvErrCode_Type = Gauge32
_CucsStatsCollectionPolicyFsmRmtInvErrCode_Object = MibTableColumn
cucsStatsCollectionPolicyFsmRmtInvErrCode = _CucsStatsCollectionPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 8),
    _CucsStatsCollectionPolicyFsmRmtInvErrCode_Type()
)
cucsStatsCollectionPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmRmtInvErrCode.setStatus("current")
_CucsStatsCollectionPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsStatsCollectionPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cucsStatsCollectionPolicyFsmRmtInvErrDescr = _CucsStatsCollectionPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 9),
    _CucsStatsCollectionPolicyFsmRmtInvErrDescr_Type()
)
cucsStatsCollectionPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmRmtInvErrDescr.setStatus("current")
_CucsStatsCollectionPolicyFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsStatsCollectionPolicyFsmRmtInvRslt_Object = MibTableColumn
cucsStatsCollectionPolicyFsmRmtInvRslt = _CucsStatsCollectionPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 10),
    _CucsStatsCollectionPolicyFsmRmtInvRslt_Type()
)
cucsStatsCollectionPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmRmtInvRslt.setStatus("current")
_CucsStatsCollectionPolicyFsmStageDescr_Type = SnmpAdminString
_CucsStatsCollectionPolicyFsmStageDescr_Object = MibTableColumn
cucsStatsCollectionPolicyFsmStageDescr = _CucsStatsCollectionPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 11),
    _CucsStatsCollectionPolicyFsmStageDescr_Type()
)
cucsStatsCollectionPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStageDescr.setStatus("current")
_CucsStatsCollectionPolicyFsmStamp_Type = DateAndTime
_CucsStatsCollectionPolicyFsmStamp_Object = MibTableColumn
cucsStatsCollectionPolicyFsmStamp = _CucsStatsCollectionPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 12),
    _CucsStatsCollectionPolicyFsmStamp_Type()
)
cucsStatsCollectionPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStamp.setStatus("current")
_CucsStatsCollectionPolicyFsmStatus_Type = SnmpAdminString
_CucsStatsCollectionPolicyFsmStatus_Object = MibTableColumn
cucsStatsCollectionPolicyFsmStatus = _CucsStatsCollectionPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 13),
    _CucsStatsCollectionPolicyFsmStatus_Type()
)
cucsStatsCollectionPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStatus.setStatus("current")
_CucsStatsCollectionPolicyFsmTry_Type = Gauge32
_CucsStatsCollectionPolicyFsmTry_Object = MibTableColumn
cucsStatsCollectionPolicyFsmTry = _CucsStatsCollectionPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 14),
    _CucsStatsCollectionPolicyFsmTry_Type()
)
cucsStatsCollectionPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmTry.setStatus("current")
_CucsStatsCollectionPolicyId_Type = Gauge32
_CucsStatsCollectionPolicyId_Object = MibTableColumn
cucsStatsCollectionPolicyId = _CucsStatsCollectionPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 15),
    _CucsStatsCollectionPolicyId_Type()
)
cucsStatsCollectionPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyId.setStatus("current")
_CucsStatsCollectionPolicyName_Type = CucsStatsCollectionDomain
_CucsStatsCollectionPolicyName_Object = MibTableColumn
cucsStatsCollectionPolicyName = _CucsStatsCollectionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 16),
    _CucsStatsCollectionPolicyName_Type()
)
cucsStatsCollectionPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyName.setStatus("current")
_CucsStatsCollectionPolicyReportingInterval_Type = CucsStatsReportingInterval
_CucsStatsCollectionPolicyReportingInterval_Object = MibTableColumn
cucsStatsCollectionPolicyReportingInterval = _CucsStatsCollectionPolicyReportingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 1, 1, 17),
    _CucsStatsCollectionPolicyReportingInterval_Type()
)
cucsStatsCollectionPolicyReportingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyReportingInterval.setStatus("current")
_CucsStatsCollectionPolicyFsmTaskTable_Object = MibTable
cucsStatsCollectionPolicyFsmTaskTable = _CucsStatsCollectionPolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 2)
)
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmTaskTable.setStatus("current")
_CucsStatsCollectionPolicyFsmTaskEntry_Object = MibTableRow
cucsStatsCollectionPolicyFsmTaskEntry = _CucsStatsCollectionPolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 2, 1)
)
cucsStatsCollectionPolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsCollectionPolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmTaskEntry.setStatus("current")
_CucsStatsCollectionPolicyFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsStatsCollectionPolicyFsmTaskInstanceId_Object = MibTableColumn
cucsStatsCollectionPolicyFsmTaskInstanceId = _CucsStatsCollectionPolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 2, 1, 1),
    _CucsStatsCollectionPolicyFsmTaskInstanceId_Type()
)
cucsStatsCollectionPolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmTaskInstanceId.setStatus("current")
_CucsStatsCollectionPolicyFsmTaskDn_Type = CucsManagedObjectDn
_CucsStatsCollectionPolicyFsmTaskDn_Object = MibTableColumn
cucsStatsCollectionPolicyFsmTaskDn = _CucsStatsCollectionPolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 2, 1, 2),
    _CucsStatsCollectionPolicyFsmTaskDn_Type()
)
cucsStatsCollectionPolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmTaskDn.setStatus("current")
_CucsStatsCollectionPolicyFsmTaskRn_Type = SnmpAdminString
_CucsStatsCollectionPolicyFsmTaskRn_Object = MibTableColumn
cucsStatsCollectionPolicyFsmTaskRn = _CucsStatsCollectionPolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 2, 1, 3),
    _CucsStatsCollectionPolicyFsmTaskRn_Type()
)
cucsStatsCollectionPolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmTaskRn.setStatus("current")
_CucsStatsCollectionPolicyFsmTaskCompletion_Type = CucsFsmCompletion
_CucsStatsCollectionPolicyFsmTaskCompletion_Object = MibTableColumn
cucsStatsCollectionPolicyFsmTaskCompletion = _CucsStatsCollectionPolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 2, 1, 4),
    _CucsStatsCollectionPolicyFsmTaskCompletion_Type()
)
cucsStatsCollectionPolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmTaskCompletion.setStatus("current")
_CucsStatsCollectionPolicyFsmTaskFlags_Type = CucsFsmFlags
_CucsStatsCollectionPolicyFsmTaskFlags_Object = MibTableColumn
cucsStatsCollectionPolicyFsmTaskFlags = _CucsStatsCollectionPolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 2, 1, 5),
    _CucsStatsCollectionPolicyFsmTaskFlags_Type()
)
cucsStatsCollectionPolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmTaskFlags.setStatus("current")
_CucsStatsCollectionPolicyFsmTaskItem_Type = CucsStatsCollectionPolicyFsmTaskItem
_CucsStatsCollectionPolicyFsmTaskItem_Object = MibTableColumn
cucsStatsCollectionPolicyFsmTaskItem = _CucsStatsCollectionPolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 2, 1, 6),
    _CucsStatsCollectionPolicyFsmTaskItem_Type()
)
cucsStatsCollectionPolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmTaskItem.setStatus("current")
_CucsStatsCollectionPolicyFsmTaskSeqId_Type = Gauge32
_CucsStatsCollectionPolicyFsmTaskSeqId_Object = MibTableColumn
cucsStatsCollectionPolicyFsmTaskSeqId = _CucsStatsCollectionPolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 2, 1, 7),
    _CucsStatsCollectionPolicyFsmTaskSeqId_Type()
)
cucsStatsCollectionPolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmTaskSeqId.setStatus("current")
_CucsStatsHolderTable_Object = MibTable
cucsStatsHolderTable = _CucsStatsHolderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 3)
)
if mibBuilder.loadTexts:
    cucsStatsHolderTable.setStatus("current")
_CucsStatsHolderEntry_Object = MibTableRow
cucsStatsHolderEntry = _CucsStatsHolderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 3, 1)
)
cucsStatsHolderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsHolderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsHolderEntry.setStatus("current")
_CucsStatsHolderInstanceId_Type = CucsManagedObjectId
_CucsStatsHolderInstanceId_Object = MibTableColumn
cucsStatsHolderInstanceId = _CucsStatsHolderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 3, 1, 1),
    _CucsStatsHolderInstanceId_Type()
)
cucsStatsHolderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsHolderInstanceId.setStatus("current")
_CucsStatsHolderDn_Type = CucsManagedObjectDn
_CucsStatsHolderDn_Object = MibTableColumn
cucsStatsHolderDn = _CucsStatsHolderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 3, 1, 2),
    _CucsStatsHolderDn_Type()
)
cucsStatsHolderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsHolderDn.setStatus("current")
_CucsStatsHolderRn_Type = SnmpAdminString
_CucsStatsHolderRn_Object = MibTableColumn
cucsStatsHolderRn = _CucsStatsHolderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 3, 1, 3),
    _CucsStatsHolderRn_Type()
)
cucsStatsHolderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsHolderRn.setStatus("current")
_CucsStatsHolderName_Type = SnmpAdminString
_CucsStatsHolderName_Object = MibTableColumn
cucsStatsHolderName = _CucsStatsHolderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 3, 1, 4),
    _CucsStatsHolderName_Type()
)
cucsStatsHolderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsHolderName.setStatus("current")
_CucsStatsThr32DefinitionTable_Object = MibTable
cucsStatsThr32DefinitionTable = _CucsStatsThr32DefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4)
)
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionTable.setStatus("current")
_CucsStatsThr32DefinitionEntry_Object = MibTableRow
cucsStatsThr32DefinitionEntry = _CucsStatsThr32DefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1)
)
cucsStatsThr32DefinitionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsThr32DefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionEntry.setStatus("current")
_CucsStatsThr32DefinitionInstanceId_Type = CucsManagedObjectId
_CucsStatsThr32DefinitionInstanceId_Object = MibTableColumn
cucsStatsThr32DefinitionInstanceId = _CucsStatsThr32DefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 1),
    _CucsStatsThr32DefinitionInstanceId_Type()
)
cucsStatsThr32DefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionInstanceId.setStatus("current")
_CucsStatsThr32DefinitionDn_Type = CucsManagedObjectDn
_CucsStatsThr32DefinitionDn_Object = MibTableColumn
cucsStatsThr32DefinitionDn = _CucsStatsThr32DefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 2),
    _CucsStatsThr32DefinitionDn_Type()
)
cucsStatsThr32DefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionDn.setStatus("current")
_CucsStatsThr32DefinitionRn_Type = SnmpAdminString
_CucsStatsThr32DefinitionRn_Object = MibTableColumn
cucsStatsThr32DefinitionRn = _CucsStatsThr32DefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 3),
    _CucsStatsThr32DefinitionRn_Type()
)
cucsStatsThr32DefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionRn.setStatus("current")
_CucsStatsThr32DefinitionDescr_Type = SnmpAdminString
_CucsStatsThr32DefinitionDescr_Object = MibTableColumn
cucsStatsThr32DefinitionDescr = _CucsStatsThr32DefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 4),
    _CucsStatsThr32DefinitionDescr_Type()
)
cucsStatsThr32DefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionDescr.setStatus("current")
_CucsStatsThr32DefinitionIntId_Type = SnmpAdminString
_CucsStatsThr32DefinitionIntId_Object = MibTableColumn
cucsStatsThr32DefinitionIntId = _CucsStatsThr32DefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 5),
    _CucsStatsThr32DefinitionIntId_Type()
)
cucsStatsThr32DefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionIntId.setStatus("current")
_CucsStatsThr32DefinitionName_Type = SnmpAdminString
_CucsStatsThr32DefinitionName_Object = MibTableColumn
cucsStatsThr32DefinitionName = _CucsStatsThr32DefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 6),
    _CucsStatsThr32DefinitionName_Type()
)
cucsStatsThr32DefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionName.setStatus("current")
_CucsStatsThr32DefinitionNormalValue_Type = Gauge32
_CucsStatsThr32DefinitionNormalValue_Object = MibTableColumn
cucsStatsThr32DefinitionNormalValue = _CucsStatsThr32DefinitionNormalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 7),
    _CucsStatsThr32DefinitionNormalValue_Type()
)
cucsStatsThr32DefinitionNormalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionNormalValue.setStatus("current")
_CucsStatsThr32DefinitionPropId_Type = SnmpAdminString
_CucsStatsThr32DefinitionPropId_Object = MibTableColumn
cucsStatsThr32DefinitionPropId = _CucsStatsThr32DefinitionPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 8),
    _CucsStatsThr32DefinitionPropId_Type()
)
cucsStatsThr32DefinitionPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionPropId.setStatus("current")
_CucsStatsThr32DefinitionPropType_Type = CucsStatsThr32DefinitionPropType
_CucsStatsThr32DefinitionPropType_Object = MibTableColumn
cucsStatsThr32DefinitionPropType = _CucsStatsThr32DefinitionPropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 9),
    _CucsStatsThr32DefinitionPropType_Type()
)
cucsStatsThr32DefinitionPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionPropType.setStatus("current")
_CucsStatsThr32DefinitionPolicyLevel_Type = Gauge32
_CucsStatsThr32DefinitionPolicyLevel_Object = MibTableColumn
cucsStatsThr32DefinitionPolicyLevel = _CucsStatsThr32DefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 10),
    _CucsStatsThr32DefinitionPolicyLevel_Type()
)
cucsStatsThr32DefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionPolicyLevel.setStatus("current")
_CucsStatsThr32DefinitionPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStatsThr32DefinitionPolicyOwner_Object = MibTableColumn
cucsStatsThr32DefinitionPolicyOwner = _CucsStatsThr32DefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 11),
    _CucsStatsThr32DefinitionPolicyOwner_Type()
)
cucsStatsThr32DefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionPolicyOwner.setStatus("current")
_CucsStatsThr32DefinitionAutoRecovery_Type = CucsStatsThresholdDefinitionAutoRecovery
_CucsStatsThr32DefinitionAutoRecovery_Object = MibTableColumn
cucsStatsThr32DefinitionAutoRecovery = _CucsStatsThr32DefinitionAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 12),
    _CucsStatsThr32DefinitionAutoRecovery_Type()
)
cucsStatsThr32DefinitionAutoRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionAutoRecovery.setStatus("current")
_CucsStatsThr32DefinitionAutoRecoveryTime_Type = Gauge32
_CucsStatsThr32DefinitionAutoRecoveryTime_Object = MibTableColumn
cucsStatsThr32DefinitionAutoRecoveryTime = _CucsStatsThr32DefinitionAutoRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 13),
    _CucsStatsThr32DefinitionAutoRecoveryTime_Type()
)
cucsStatsThr32DefinitionAutoRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionAutoRecoveryTime.setStatus("current")
_CucsStatsThr32DefinitionErrorDisableFiPort_Type = TruthValue
_CucsStatsThr32DefinitionErrorDisableFiPort_Object = MibTableColumn
cucsStatsThr32DefinitionErrorDisableFiPort = _CucsStatsThr32DefinitionErrorDisableFiPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 4, 1, 14),
    _CucsStatsThr32DefinitionErrorDisableFiPort_Type()
)
cucsStatsThr32DefinitionErrorDisableFiPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32DefinitionErrorDisableFiPort.setStatus("current")
_CucsStatsThr32ValueTable_Object = MibTable
cucsStatsThr32ValueTable = _CucsStatsThr32ValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5)
)
if mibBuilder.loadTexts:
    cucsStatsThr32ValueTable.setStatus("current")
_CucsStatsThr32ValueEntry_Object = MibTableRow
cucsStatsThr32ValueEntry = _CucsStatsThr32ValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1)
)
cucsStatsThr32ValueEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsThr32ValueInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsThr32ValueEntry.setStatus("current")
_CucsStatsThr32ValueInstanceId_Type = CucsManagedObjectId
_CucsStatsThr32ValueInstanceId_Object = MibTableColumn
cucsStatsThr32ValueInstanceId = _CucsStatsThr32ValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 1),
    _CucsStatsThr32ValueInstanceId_Type()
)
cucsStatsThr32ValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsThr32ValueInstanceId.setStatus("current")
_CucsStatsThr32ValueDn_Type = CucsManagedObjectDn
_CucsStatsThr32ValueDn_Object = MibTableColumn
cucsStatsThr32ValueDn = _CucsStatsThr32ValueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 2),
    _CucsStatsThr32ValueDn_Type()
)
cucsStatsThr32ValueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32ValueDn.setStatus("current")
_CucsStatsThr32ValueRn_Type = SnmpAdminString
_CucsStatsThr32ValueRn_Object = MibTableColumn
cucsStatsThr32ValueRn = _CucsStatsThr32ValueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 3),
    _CucsStatsThr32ValueRn_Type()
)
cucsStatsThr32ValueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32ValueRn.setStatus("current")
_CucsStatsThr32ValueDeescalating_Type = Gauge32
_CucsStatsThr32ValueDeescalating_Object = MibTableColumn
cucsStatsThr32ValueDeescalating = _CucsStatsThr32ValueDeescalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 4),
    _CucsStatsThr32ValueDeescalating_Type()
)
cucsStatsThr32ValueDeescalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32ValueDeescalating.setStatus("current")
_CucsStatsThr32ValueDescr_Type = SnmpAdminString
_CucsStatsThr32ValueDescr_Object = MibTableColumn
cucsStatsThr32ValueDescr = _CucsStatsThr32ValueDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 5),
    _CucsStatsThr32ValueDescr_Type()
)
cucsStatsThr32ValueDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32ValueDescr.setStatus("current")
_CucsStatsThr32ValueDirection_Type = CucsStatsThresholdDirection
_CucsStatsThr32ValueDirection_Object = MibTableColumn
cucsStatsThr32ValueDirection = _CucsStatsThr32ValueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 6),
    _CucsStatsThr32ValueDirection_Type()
)
cucsStatsThr32ValueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32ValueDirection.setStatus("current")
_CucsStatsThr32ValueEscalating_Type = Gauge32
_CucsStatsThr32ValueEscalating_Object = MibTableColumn
cucsStatsThr32ValueEscalating = _CucsStatsThr32ValueEscalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 7),
    _CucsStatsThr32ValueEscalating_Type()
)
cucsStatsThr32ValueEscalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32ValueEscalating.setStatus("current")
_CucsStatsThr32ValueIntId_Type = SnmpAdminString
_CucsStatsThr32ValueIntId_Object = MibTableColumn
cucsStatsThr32ValueIntId = _CucsStatsThr32ValueIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 8),
    _CucsStatsThr32ValueIntId_Type()
)
cucsStatsThr32ValueIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32ValueIntId.setStatus("current")
_CucsStatsThr32ValueName_Type = SnmpAdminString
_CucsStatsThr32ValueName_Object = MibTableColumn
cucsStatsThr32ValueName = _CucsStatsThr32ValueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 9),
    _CucsStatsThr32ValueName_Type()
)
cucsStatsThr32ValueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32ValueName.setStatus("current")
_CucsStatsThr32ValuePropType_Type = CucsStatsThr32ValuePropType
_CucsStatsThr32ValuePropType_Object = MibTableColumn
cucsStatsThr32ValuePropType = _CucsStatsThr32ValuePropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 10),
    _CucsStatsThr32ValuePropType_Type()
)
cucsStatsThr32ValuePropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32ValuePropType.setStatus("current")
_CucsStatsThr32ValueSeverity_Type = CucsConditionSeverity
_CucsStatsThr32ValueSeverity_Object = MibTableColumn
cucsStatsThr32ValueSeverity = _CucsStatsThr32ValueSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 11),
    _CucsStatsThr32ValueSeverity_Type()
)
cucsStatsThr32ValueSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32ValueSeverity.setStatus("current")
_CucsStatsThr32ValuePolicyLevel_Type = Gauge32
_CucsStatsThr32ValuePolicyLevel_Object = MibTableColumn
cucsStatsThr32ValuePolicyLevel = _CucsStatsThr32ValuePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 12),
    _CucsStatsThr32ValuePolicyLevel_Type()
)
cucsStatsThr32ValuePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32ValuePolicyLevel.setStatus("current")
_CucsStatsThr32ValuePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStatsThr32ValuePolicyOwner_Object = MibTableColumn
cucsStatsThr32ValuePolicyOwner = _CucsStatsThr32ValuePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 5, 1, 13),
    _CucsStatsThr32ValuePolicyOwner_Type()
)
cucsStatsThr32ValuePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr32ValuePolicyOwner.setStatus("current")
_CucsStatsThr64DefinitionTable_Object = MibTable
cucsStatsThr64DefinitionTable = _CucsStatsThr64DefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6)
)
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionTable.setStatus("current")
_CucsStatsThr64DefinitionEntry_Object = MibTableRow
cucsStatsThr64DefinitionEntry = _CucsStatsThr64DefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1)
)
cucsStatsThr64DefinitionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsThr64DefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionEntry.setStatus("current")
_CucsStatsThr64DefinitionInstanceId_Type = CucsManagedObjectId
_CucsStatsThr64DefinitionInstanceId_Object = MibTableColumn
cucsStatsThr64DefinitionInstanceId = _CucsStatsThr64DefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 1),
    _CucsStatsThr64DefinitionInstanceId_Type()
)
cucsStatsThr64DefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionInstanceId.setStatus("current")
_CucsStatsThr64DefinitionDn_Type = CucsManagedObjectDn
_CucsStatsThr64DefinitionDn_Object = MibTableColumn
cucsStatsThr64DefinitionDn = _CucsStatsThr64DefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 2),
    _CucsStatsThr64DefinitionDn_Type()
)
cucsStatsThr64DefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionDn.setStatus("current")
_CucsStatsThr64DefinitionRn_Type = SnmpAdminString
_CucsStatsThr64DefinitionRn_Object = MibTableColumn
cucsStatsThr64DefinitionRn = _CucsStatsThr64DefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 3),
    _CucsStatsThr64DefinitionRn_Type()
)
cucsStatsThr64DefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionRn.setStatus("current")
_CucsStatsThr64DefinitionDescr_Type = SnmpAdminString
_CucsStatsThr64DefinitionDescr_Object = MibTableColumn
cucsStatsThr64DefinitionDescr = _CucsStatsThr64DefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 4),
    _CucsStatsThr64DefinitionDescr_Type()
)
cucsStatsThr64DefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionDescr.setStatus("current")
_CucsStatsThr64DefinitionIntId_Type = SnmpAdminString
_CucsStatsThr64DefinitionIntId_Object = MibTableColumn
cucsStatsThr64DefinitionIntId = _CucsStatsThr64DefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 5),
    _CucsStatsThr64DefinitionIntId_Type()
)
cucsStatsThr64DefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionIntId.setStatus("current")
_CucsStatsThr64DefinitionName_Type = SnmpAdminString
_CucsStatsThr64DefinitionName_Object = MibTableColumn
cucsStatsThr64DefinitionName = _CucsStatsThr64DefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 6),
    _CucsStatsThr64DefinitionName_Type()
)
cucsStatsThr64DefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionName.setStatus("current")
_CucsStatsThr64DefinitionNormalValue_Type = Unsigned64
_CucsStatsThr64DefinitionNormalValue_Object = MibTableColumn
cucsStatsThr64DefinitionNormalValue = _CucsStatsThr64DefinitionNormalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 7),
    _CucsStatsThr64DefinitionNormalValue_Type()
)
cucsStatsThr64DefinitionNormalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionNormalValue.setStatus("current")
_CucsStatsThr64DefinitionPropId_Type = SnmpAdminString
_CucsStatsThr64DefinitionPropId_Object = MibTableColumn
cucsStatsThr64DefinitionPropId = _CucsStatsThr64DefinitionPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 8),
    _CucsStatsThr64DefinitionPropId_Type()
)
cucsStatsThr64DefinitionPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionPropId.setStatus("current")
_CucsStatsThr64DefinitionPropType_Type = CucsStatsThr64DefinitionPropType
_CucsStatsThr64DefinitionPropType_Object = MibTableColumn
cucsStatsThr64DefinitionPropType = _CucsStatsThr64DefinitionPropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 9),
    _CucsStatsThr64DefinitionPropType_Type()
)
cucsStatsThr64DefinitionPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionPropType.setStatus("current")
_CucsStatsThr64DefinitionPolicyLevel_Type = Gauge32
_CucsStatsThr64DefinitionPolicyLevel_Object = MibTableColumn
cucsStatsThr64DefinitionPolicyLevel = _CucsStatsThr64DefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 10),
    _CucsStatsThr64DefinitionPolicyLevel_Type()
)
cucsStatsThr64DefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionPolicyLevel.setStatus("current")
_CucsStatsThr64DefinitionPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStatsThr64DefinitionPolicyOwner_Object = MibTableColumn
cucsStatsThr64DefinitionPolicyOwner = _CucsStatsThr64DefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 11),
    _CucsStatsThr64DefinitionPolicyOwner_Type()
)
cucsStatsThr64DefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionPolicyOwner.setStatus("current")
_CucsStatsThr64DefinitionAutoRecovery_Type = CucsStatsThresholdDefinitionAutoRecovery
_CucsStatsThr64DefinitionAutoRecovery_Object = MibTableColumn
cucsStatsThr64DefinitionAutoRecovery = _CucsStatsThr64DefinitionAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 12),
    _CucsStatsThr64DefinitionAutoRecovery_Type()
)
cucsStatsThr64DefinitionAutoRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionAutoRecovery.setStatus("current")
_CucsStatsThr64DefinitionAutoRecoveryTime_Type = Gauge32
_CucsStatsThr64DefinitionAutoRecoveryTime_Object = MibTableColumn
cucsStatsThr64DefinitionAutoRecoveryTime = _CucsStatsThr64DefinitionAutoRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 13),
    _CucsStatsThr64DefinitionAutoRecoveryTime_Type()
)
cucsStatsThr64DefinitionAutoRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionAutoRecoveryTime.setStatus("current")
_CucsStatsThr64DefinitionErrorDisableFiPort_Type = TruthValue
_CucsStatsThr64DefinitionErrorDisableFiPort_Object = MibTableColumn
cucsStatsThr64DefinitionErrorDisableFiPort = _CucsStatsThr64DefinitionErrorDisableFiPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 6, 1, 14),
    _CucsStatsThr64DefinitionErrorDisableFiPort_Type()
)
cucsStatsThr64DefinitionErrorDisableFiPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64DefinitionErrorDisableFiPort.setStatus("current")
_CucsStatsThr64ValueTable_Object = MibTable
cucsStatsThr64ValueTable = _CucsStatsThr64ValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7)
)
if mibBuilder.loadTexts:
    cucsStatsThr64ValueTable.setStatus("current")
_CucsStatsThr64ValueEntry_Object = MibTableRow
cucsStatsThr64ValueEntry = _CucsStatsThr64ValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1)
)
cucsStatsThr64ValueEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsThr64ValueInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsThr64ValueEntry.setStatus("current")
_CucsStatsThr64ValueInstanceId_Type = CucsManagedObjectId
_CucsStatsThr64ValueInstanceId_Object = MibTableColumn
cucsStatsThr64ValueInstanceId = _CucsStatsThr64ValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 1),
    _CucsStatsThr64ValueInstanceId_Type()
)
cucsStatsThr64ValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsThr64ValueInstanceId.setStatus("current")
_CucsStatsThr64ValueDn_Type = CucsManagedObjectDn
_CucsStatsThr64ValueDn_Object = MibTableColumn
cucsStatsThr64ValueDn = _CucsStatsThr64ValueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 2),
    _CucsStatsThr64ValueDn_Type()
)
cucsStatsThr64ValueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64ValueDn.setStatus("current")
_CucsStatsThr64ValueRn_Type = SnmpAdminString
_CucsStatsThr64ValueRn_Object = MibTableColumn
cucsStatsThr64ValueRn = _CucsStatsThr64ValueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 3),
    _CucsStatsThr64ValueRn_Type()
)
cucsStatsThr64ValueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64ValueRn.setStatus("current")
_CucsStatsThr64ValueDeescalating_Type = Unsigned64
_CucsStatsThr64ValueDeescalating_Object = MibTableColumn
cucsStatsThr64ValueDeescalating = _CucsStatsThr64ValueDeescalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 4),
    _CucsStatsThr64ValueDeescalating_Type()
)
cucsStatsThr64ValueDeescalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64ValueDeescalating.setStatus("current")
_CucsStatsThr64ValueDescr_Type = SnmpAdminString
_CucsStatsThr64ValueDescr_Object = MibTableColumn
cucsStatsThr64ValueDescr = _CucsStatsThr64ValueDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 5),
    _CucsStatsThr64ValueDescr_Type()
)
cucsStatsThr64ValueDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64ValueDescr.setStatus("current")
_CucsStatsThr64ValueDirection_Type = CucsStatsThresholdDirection
_CucsStatsThr64ValueDirection_Object = MibTableColumn
cucsStatsThr64ValueDirection = _CucsStatsThr64ValueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 6),
    _CucsStatsThr64ValueDirection_Type()
)
cucsStatsThr64ValueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64ValueDirection.setStatus("current")
_CucsStatsThr64ValueEscalating_Type = Unsigned64
_CucsStatsThr64ValueEscalating_Object = MibTableColumn
cucsStatsThr64ValueEscalating = _CucsStatsThr64ValueEscalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 7),
    _CucsStatsThr64ValueEscalating_Type()
)
cucsStatsThr64ValueEscalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64ValueEscalating.setStatus("current")
_CucsStatsThr64ValueIntId_Type = SnmpAdminString
_CucsStatsThr64ValueIntId_Object = MibTableColumn
cucsStatsThr64ValueIntId = _CucsStatsThr64ValueIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 8),
    _CucsStatsThr64ValueIntId_Type()
)
cucsStatsThr64ValueIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64ValueIntId.setStatus("current")
_CucsStatsThr64ValueName_Type = SnmpAdminString
_CucsStatsThr64ValueName_Object = MibTableColumn
cucsStatsThr64ValueName = _CucsStatsThr64ValueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 9),
    _CucsStatsThr64ValueName_Type()
)
cucsStatsThr64ValueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64ValueName.setStatus("current")
_CucsStatsThr64ValuePropType_Type = CucsStatsThr64ValuePropType
_CucsStatsThr64ValuePropType_Object = MibTableColumn
cucsStatsThr64ValuePropType = _CucsStatsThr64ValuePropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 10),
    _CucsStatsThr64ValuePropType_Type()
)
cucsStatsThr64ValuePropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64ValuePropType.setStatus("current")
_CucsStatsThr64ValueSeverity_Type = CucsConditionSeverity
_CucsStatsThr64ValueSeverity_Object = MibTableColumn
cucsStatsThr64ValueSeverity = _CucsStatsThr64ValueSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 11),
    _CucsStatsThr64ValueSeverity_Type()
)
cucsStatsThr64ValueSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64ValueSeverity.setStatus("current")
_CucsStatsThr64ValuePolicyLevel_Type = Gauge32
_CucsStatsThr64ValuePolicyLevel_Object = MibTableColumn
cucsStatsThr64ValuePolicyLevel = _CucsStatsThr64ValuePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 12),
    _CucsStatsThr64ValuePolicyLevel_Type()
)
cucsStatsThr64ValuePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64ValuePolicyLevel.setStatus("current")
_CucsStatsThr64ValuePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStatsThr64ValuePolicyOwner_Object = MibTableColumn
cucsStatsThr64ValuePolicyOwner = _CucsStatsThr64ValuePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 7, 1, 13),
    _CucsStatsThr64ValuePolicyOwner_Type()
)
cucsStatsThr64ValuePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThr64ValuePolicyOwner.setStatus("current")
_CucsStatsThrFloatDefinitionTable_Object = MibTable
cucsStatsThrFloatDefinitionTable = _CucsStatsThrFloatDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8)
)
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionTable.setStatus("current")
_CucsStatsThrFloatDefinitionEntry_Object = MibTableRow
cucsStatsThrFloatDefinitionEntry = _CucsStatsThrFloatDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1)
)
cucsStatsThrFloatDefinitionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsThrFloatDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionEntry.setStatus("current")
_CucsStatsThrFloatDefinitionInstanceId_Type = CucsManagedObjectId
_CucsStatsThrFloatDefinitionInstanceId_Object = MibTableColumn
cucsStatsThrFloatDefinitionInstanceId = _CucsStatsThrFloatDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 1),
    _CucsStatsThrFloatDefinitionInstanceId_Type()
)
cucsStatsThrFloatDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionInstanceId.setStatus("current")
_CucsStatsThrFloatDefinitionDn_Type = CucsManagedObjectDn
_CucsStatsThrFloatDefinitionDn_Object = MibTableColumn
cucsStatsThrFloatDefinitionDn = _CucsStatsThrFloatDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 2),
    _CucsStatsThrFloatDefinitionDn_Type()
)
cucsStatsThrFloatDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionDn.setStatus("current")
_CucsStatsThrFloatDefinitionRn_Type = SnmpAdminString
_CucsStatsThrFloatDefinitionRn_Object = MibTableColumn
cucsStatsThrFloatDefinitionRn = _CucsStatsThrFloatDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 3),
    _CucsStatsThrFloatDefinitionRn_Type()
)
cucsStatsThrFloatDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionRn.setStatus("current")
_CucsStatsThrFloatDefinitionDescr_Type = SnmpAdminString
_CucsStatsThrFloatDefinitionDescr_Object = MibTableColumn
cucsStatsThrFloatDefinitionDescr = _CucsStatsThrFloatDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 4),
    _CucsStatsThrFloatDefinitionDescr_Type()
)
cucsStatsThrFloatDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionDescr.setStatus("current")
_CucsStatsThrFloatDefinitionIntId_Type = SnmpAdminString
_CucsStatsThrFloatDefinitionIntId_Object = MibTableColumn
cucsStatsThrFloatDefinitionIntId = _CucsStatsThrFloatDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 5),
    _CucsStatsThrFloatDefinitionIntId_Type()
)
cucsStatsThrFloatDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionIntId.setStatus("current")
_CucsStatsThrFloatDefinitionName_Type = SnmpAdminString
_CucsStatsThrFloatDefinitionName_Object = MibTableColumn
cucsStatsThrFloatDefinitionName = _CucsStatsThrFloatDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 6),
    _CucsStatsThrFloatDefinitionName_Type()
)
cucsStatsThrFloatDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionName.setStatus("current")
_CucsStatsThrFloatDefinitionNormalValue_Type = Integer32
_CucsStatsThrFloatDefinitionNormalValue_Object = MibTableColumn
cucsStatsThrFloatDefinitionNormalValue = _CucsStatsThrFloatDefinitionNormalValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 7),
    _CucsStatsThrFloatDefinitionNormalValue_Type()
)
cucsStatsThrFloatDefinitionNormalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionNormalValue.setStatus("current")
_CucsStatsThrFloatDefinitionPropId_Type = SnmpAdminString
_CucsStatsThrFloatDefinitionPropId_Object = MibTableColumn
cucsStatsThrFloatDefinitionPropId = _CucsStatsThrFloatDefinitionPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 8),
    _CucsStatsThrFloatDefinitionPropId_Type()
)
cucsStatsThrFloatDefinitionPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionPropId.setStatus("current")
_CucsStatsThrFloatDefinitionPropType_Type = CucsStatsThrFloatDefinitionPropType
_CucsStatsThrFloatDefinitionPropType_Object = MibTableColumn
cucsStatsThrFloatDefinitionPropType = _CucsStatsThrFloatDefinitionPropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 9),
    _CucsStatsThrFloatDefinitionPropType_Type()
)
cucsStatsThrFloatDefinitionPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionPropType.setStatus("current")
_CucsStatsThrFloatDefinitionPolicyLevel_Type = Gauge32
_CucsStatsThrFloatDefinitionPolicyLevel_Object = MibTableColumn
cucsStatsThrFloatDefinitionPolicyLevel = _CucsStatsThrFloatDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 10),
    _CucsStatsThrFloatDefinitionPolicyLevel_Type()
)
cucsStatsThrFloatDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionPolicyLevel.setStatus("current")
_CucsStatsThrFloatDefinitionPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStatsThrFloatDefinitionPolicyOwner_Object = MibTableColumn
cucsStatsThrFloatDefinitionPolicyOwner = _CucsStatsThrFloatDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 11),
    _CucsStatsThrFloatDefinitionPolicyOwner_Type()
)
cucsStatsThrFloatDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionPolicyOwner.setStatus("current")
_CucsStatsThrFloatDefinitionAutoRecovery_Type = CucsStatsThresholdDefinitionAutoRecovery
_CucsStatsThrFloatDefinitionAutoRecovery_Object = MibTableColumn
cucsStatsThrFloatDefinitionAutoRecovery = _CucsStatsThrFloatDefinitionAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 12),
    _CucsStatsThrFloatDefinitionAutoRecovery_Type()
)
cucsStatsThrFloatDefinitionAutoRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionAutoRecovery.setStatus("current")
_CucsStatsThrFloatDefinitionAutoRecoveryTime_Type = Gauge32
_CucsStatsThrFloatDefinitionAutoRecoveryTime_Object = MibTableColumn
cucsStatsThrFloatDefinitionAutoRecoveryTime = _CucsStatsThrFloatDefinitionAutoRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 13),
    _CucsStatsThrFloatDefinitionAutoRecoveryTime_Type()
)
cucsStatsThrFloatDefinitionAutoRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionAutoRecoveryTime.setStatus("current")
_CucsStatsThrFloatDefinitionErrorDisableFiPort_Type = TruthValue
_CucsStatsThrFloatDefinitionErrorDisableFiPort_Object = MibTableColumn
cucsStatsThrFloatDefinitionErrorDisableFiPort = _CucsStatsThrFloatDefinitionErrorDisableFiPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 8, 1, 14),
    _CucsStatsThrFloatDefinitionErrorDisableFiPort_Type()
)
cucsStatsThrFloatDefinitionErrorDisableFiPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatDefinitionErrorDisableFiPort.setStatus("current")
_CucsStatsThrFloatValueTable_Object = MibTable
cucsStatsThrFloatValueTable = _CucsStatsThrFloatValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9)
)
if mibBuilder.loadTexts:
    cucsStatsThrFloatValueTable.setStatus("current")
_CucsStatsThrFloatValueEntry_Object = MibTableRow
cucsStatsThrFloatValueEntry = _CucsStatsThrFloatValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1)
)
cucsStatsThrFloatValueEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsThrFloatValueInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsThrFloatValueEntry.setStatus("current")
_CucsStatsThrFloatValueInstanceId_Type = CucsManagedObjectId
_CucsStatsThrFloatValueInstanceId_Object = MibTableColumn
cucsStatsThrFloatValueInstanceId = _CucsStatsThrFloatValueInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 1),
    _CucsStatsThrFloatValueInstanceId_Type()
)
cucsStatsThrFloatValueInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValueInstanceId.setStatus("current")
_CucsStatsThrFloatValueDn_Type = CucsManagedObjectDn
_CucsStatsThrFloatValueDn_Object = MibTableColumn
cucsStatsThrFloatValueDn = _CucsStatsThrFloatValueDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 2),
    _CucsStatsThrFloatValueDn_Type()
)
cucsStatsThrFloatValueDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValueDn.setStatus("current")
_CucsStatsThrFloatValueRn_Type = SnmpAdminString
_CucsStatsThrFloatValueRn_Object = MibTableColumn
cucsStatsThrFloatValueRn = _CucsStatsThrFloatValueRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 3),
    _CucsStatsThrFloatValueRn_Type()
)
cucsStatsThrFloatValueRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValueRn.setStatus("current")
_CucsStatsThrFloatValueDeescalating_Type = Integer32
_CucsStatsThrFloatValueDeescalating_Object = MibTableColumn
cucsStatsThrFloatValueDeescalating = _CucsStatsThrFloatValueDeescalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 4),
    _CucsStatsThrFloatValueDeescalating_Type()
)
cucsStatsThrFloatValueDeescalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValueDeescalating.setStatus("current")
_CucsStatsThrFloatValueDescr_Type = SnmpAdminString
_CucsStatsThrFloatValueDescr_Object = MibTableColumn
cucsStatsThrFloatValueDescr = _CucsStatsThrFloatValueDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 5),
    _CucsStatsThrFloatValueDescr_Type()
)
cucsStatsThrFloatValueDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValueDescr.setStatus("current")
_CucsStatsThrFloatValueDirection_Type = CucsStatsThresholdDirection
_CucsStatsThrFloatValueDirection_Object = MibTableColumn
cucsStatsThrFloatValueDirection = _CucsStatsThrFloatValueDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 6),
    _CucsStatsThrFloatValueDirection_Type()
)
cucsStatsThrFloatValueDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValueDirection.setStatus("current")
_CucsStatsThrFloatValueEscalating_Type = Integer32
_CucsStatsThrFloatValueEscalating_Object = MibTableColumn
cucsStatsThrFloatValueEscalating = _CucsStatsThrFloatValueEscalating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 7),
    _CucsStatsThrFloatValueEscalating_Type()
)
cucsStatsThrFloatValueEscalating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValueEscalating.setStatus("current")
_CucsStatsThrFloatValueIntId_Type = SnmpAdminString
_CucsStatsThrFloatValueIntId_Object = MibTableColumn
cucsStatsThrFloatValueIntId = _CucsStatsThrFloatValueIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 8),
    _CucsStatsThrFloatValueIntId_Type()
)
cucsStatsThrFloatValueIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValueIntId.setStatus("current")
_CucsStatsThrFloatValueName_Type = SnmpAdminString
_CucsStatsThrFloatValueName_Object = MibTableColumn
cucsStatsThrFloatValueName = _CucsStatsThrFloatValueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 9),
    _CucsStatsThrFloatValueName_Type()
)
cucsStatsThrFloatValueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValueName.setStatus("current")
_CucsStatsThrFloatValuePropType_Type = CucsStatsThrFloatValuePropType
_CucsStatsThrFloatValuePropType_Object = MibTableColumn
cucsStatsThrFloatValuePropType = _CucsStatsThrFloatValuePropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 10),
    _CucsStatsThrFloatValuePropType_Type()
)
cucsStatsThrFloatValuePropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValuePropType.setStatus("current")
_CucsStatsThrFloatValueSeverity_Type = CucsConditionSeverity
_CucsStatsThrFloatValueSeverity_Object = MibTableColumn
cucsStatsThrFloatValueSeverity = _CucsStatsThrFloatValueSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 11),
    _CucsStatsThrFloatValueSeverity_Type()
)
cucsStatsThrFloatValueSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValueSeverity.setStatus("current")
_CucsStatsThrFloatValuePolicyLevel_Type = Gauge32
_CucsStatsThrFloatValuePolicyLevel_Object = MibTableColumn
cucsStatsThrFloatValuePolicyLevel = _CucsStatsThrFloatValuePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 12),
    _CucsStatsThrFloatValuePolicyLevel_Type()
)
cucsStatsThrFloatValuePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValuePolicyLevel.setStatus("current")
_CucsStatsThrFloatValuePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStatsThrFloatValuePolicyOwner_Object = MibTableColumn
cucsStatsThrFloatValuePolicyOwner = _CucsStatsThrFloatValuePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 9, 1, 13),
    _CucsStatsThrFloatValuePolicyOwner_Type()
)
cucsStatsThrFloatValuePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThrFloatValuePolicyOwner.setStatus("current")
_CucsStatsThresholdClassTable_Object = MibTable
cucsStatsThresholdClassTable = _CucsStatsThresholdClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 10)
)
if mibBuilder.loadTexts:
    cucsStatsThresholdClassTable.setStatus("current")
_CucsStatsThresholdClassEntry_Object = MibTableRow
cucsStatsThresholdClassEntry = _CucsStatsThresholdClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 10, 1)
)
cucsStatsThresholdClassEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsThresholdClassInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsThresholdClassEntry.setStatus("current")
_CucsStatsThresholdClassInstanceId_Type = CucsManagedObjectId
_CucsStatsThresholdClassInstanceId_Object = MibTableColumn
cucsStatsThresholdClassInstanceId = _CucsStatsThresholdClassInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 10, 1, 1),
    _CucsStatsThresholdClassInstanceId_Type()
)
cucsStatsThresholdClassInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsThresholdClassInstanceId.setStatus("current")
_CucsStatsThresholdClassDn_Type = CucsManagedObjectDn
_CucsStatsThresholdClassDn_Object = MibTableColumn
cucsStatsThresholdClassDn = _CucsStatsThresholdClassDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 10, 1, 2),
    _CucsStatsThresholdClassDn_Type()
)
cucsStatsThresholdClassDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdClassDn.setStatus("current")
_CucsStatsThresholdClassRn_Type = SnmpAdminString
_CucsStatsThresholdClassRn_Object = MibTableColumn
cucsStatsThresholdClassRn = _CucsStatsThresholdClassRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 10, 1, 3),
    _CucsStatsThresholdClassRn_Type()
)
cucsStatsThresholdClassRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdClassRn.setStatus("current")
_CucsStatsThresholdClassDescr_Type = SnmpAdminString
_CucsStatsThresholdClassDescr_Object = MibTableColumn
cucsStatsThresholdClassDescr = _CucsStatsThresholdClassDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 10, 1, 4),
    _CucsStatsThresholdClassDescr_Type()
)
cucsStatsThresholdClassDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdClassDescr.setStatus("current")
_CucsStatsThresholdClassIntId_Type = SnmpAdminString
_CucsStatsThresholdClassIntId_Object = MibTableColumn
cucsStatsThresholdClassIntId = _CucsStatsThresholdClassIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 10, 1, 5),
    _CucsStatsThresholdClassIntId_Type()
)
cucsStatsThresholdClassIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdClassIntId.setStatus("current")
_CucsStatsThresholdClassName_Type = SnmpAdminString
_CucsStatsThresholdClassName_Object = MibTableColumn
cucsStatsThresholdClassName = _CucsStatsThresholdClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 10, 1, 6),
    _CucsStatsThresholdClassName_Type()
)
cucsStatsThresholdClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdClassName.setStatus("current")
_CucsStatsThresholdClassStatsClassId_Type = SnmpAdminString
_CucsStatsThresholdClassStatsClassId_Object = MibTableColumn
cucsStatsThresholdClassStatsClassId = _CucsStatsThresholdClassStatsClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 10, 1, 7),
    _CucsStatsThresholdClassStatsClassId_Type()
)
cucsStatsThresholdClassStatsClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdClassStatsClassId.setStatus("current")
_CucsStatsThresholdClassPolicyLevel_Type = Gauge32
_CucsStatsThresholdClassPolicyLevel_Object = MibTableColumn
cucsStatsThresholdClassPolicyLevel = _CucsStatsThresholdClassPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 10, 1, 8),
    _CucsStatsThresholdClassPolicyLevel_Type()
)
cucsStatsThresholdClassPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdClassPolicyLevel.setStatus("current")
_CucsStatsThresholdClassPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStatsThresholdClassPolicyOwner_Object = MibTableColumn
cucsStatsThresholdClassPolicyOwner = _CucsStatsThresholdClassPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 10, 1, 9),
    _CucsStatsThresholdClassPolicyOwner_Type()
)
cucsStatsThresholdClassPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdClassPolicyOwner.setStatus("current")
_CucsStatsThresholdPolicyTable_Object = MibTable
cucsStatsThresholdPolicyTable = _CucsStatsThresholdPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 11)
)
if mibBuilder.loadTexts:
    cucsStatsThresholdPolicyTable.setStatus("current")
_CucsStatsThresholdPolicyEntry_Object = MibTableRow
cucsStatsThresholdPolicyEntry = _CucsStatsThresholdPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 11, 1)
)
cucsStatsThresholdPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsThresholdPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsThresholdPolicyEntry.setStatus("current")
_CucsStatsThresholdPolicyInstanceId_Type = CucsManagedObjectId
_CucsStatsThresholdPolicyInstanceId_Object = MibTableColumn
cucsStatsThresholdPolicyInstanceId = _CucsStatsThresholdPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 11, 1, 1),
    _CucsStatsThresholdPolicyInstanceId_Type()
)
cucsStatsThresholdPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsThresholdPolicyInstanceId.setStatus("current")
_CucsStatsThresholdPolicyDn_Type = CucsManagedObjectDn
_CucsStatsThresholdPolicyDn_Object = MibTableColumn
cucsStatsThresholdPolicyDn = _CucsStatsThresholdPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 11, 1, 2),
    _CucsStatsThresholdPolicyDn_Type()
)
cucsStatsThresholdPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdPolicyDn.setStatus("current")
_CucsStatsThresholdPolicyRn_Type = SnmpAdminString
_CucsStatsThresholdPolicyRn_Object = MibTableColumn
cucsStatsThresholdPolicyRn = _CucsStatsThresholdPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 11, 1, 3),
    _CucsStatsThresholdPolicyRn_Type()
)
cucsStatsThresholdPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdPolicyRn.setStatus("current")
_CucsStatsThresholdPolicyDescr_Type = SnmpAdminString
_CucsStatsThresholdPolicyDescr_Object = MibTableColumn
cucsStatsThresholdPolicyDescr = _CucsStatsThresholdPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 11, 1, 4),
    _CucsStatsThresholdPolicyDescr_Type()
)
cucsStatsThresholdPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdPolicyDescr.setStatus("current")
_CucsStatsThresholdPolicyIntId_Type = SnmpAdminString
_CucsStatsThresholdPolicyIntId_Object = MibTableColumn
cucsStatsThresholdPolicyIntId = _CucsStatsThresholdPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 11, 1, 5),
    _CucsStatsThresholdPolicyIntId_Type()
)
cucsStatsThresholdPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdPolicyIntId.setStatus("current")
_CucsStatsThresholdPolicyName_Type = SnmpAdminString
_CucsStatsThresholdPolicyName_Object = MibTableColumn
cucsStatsThresholdPolicyName = _CucsStatsThresholdPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 11, 1, 6),
    _CucsStatsThresholdPolicyName_Type()
)
cucsStatsThresholdPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdPolicyName.setStatus("current")
_CucsStatsThresholdPolicyPolicyLevel_Type = Gauge32
_CucsStatsThresholdPolicyPolicyLevel_Object = MibTableColumn
cucsStatsThresholdPolicyPolicyLevel = _CucsStatsThresholdPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 11, 1, 7),
    _CucsStatsThresholdPolicyPolicyLevel_Type()
)
cucsStatsThresholdPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdPolicyPolicyLevel.setStatus("current")
_CucsStatsThresholdPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsStatsThresholdPolicyPolicyOwner_Object = MibTableColumn
cucsStatsThresholdPolicyPolicyOwner = _CucsStatsThresholdPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 11, 1, 8),
    _CucsStatsThresholdPolicyPolicyOwner_Type()
)
cucsStatsThresholdPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdPolicyPolicyOwner.setStatus("current")
_CucsStatsThresholdPolicyDefaultThresholdsAdded_Type = TruthValue
_CucsStatsThresholdPolicyDefaultThresholdsAdded_Object = MibTableColumn
cucsStatsThresholdPolicyDefaultThresholdsAdded = _CucsStatsThresholdPolicyDefaultThresholdsAdded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 11, 1, 9),
    _CucsStatsThresholdPolicyDefaultThresholdsAdded_Type()
)
cucsStatsThresholdPolicyDefaultThresholdsAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsThresholdPolicyDefaultThresholdsAdded.setStatus("current")
_CucsStatsCollectionPolicyFsmTable_Object = MibTable
cucsStatsCollectionPolicyFsmTable = _CucsStatsCollectionPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12)
)
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmTable.setStatus("current")
_CucsStatsCollectionPolicyFsmEntry_Object = MibTableRow
cucsStatsCollectionPolicyFsmEntry = _CucsStatsCollectionPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12, 1)
)
cucsStatsCollectionPolicyFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsCollectionPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmEntry.setStatus("current")
_CucsStatsCollectionPolicyFsmInstanceId_Type = CucsManagedObjectId
_CucsStatsCollectionPolicyFsmInstanceId_Object = MibTableColumn
cucsStatsCollectionPolicyFsmInstanceId = _CucsStatsCollectionPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12, 1, 1),
    _CucsStatsCollectionPolicyFsmInstanceId_Type()
)
cucsStatsCollectionPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmInstanceId.setStatus("current")
_CucsStatsCollectionPolicyFsmDn_Type = CucsManagedObjectDn
_CucsStatsCollectionPolicyFsmDn_Object = MibTableColumn
cucsStatsCollectionPolicyFsmDn = _CucsStatsCollectionPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12, 1, 2),
    _CucsStatsCollectionPolicyFsmDn_Type()
)
cucsStatsCollectionPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmDn.setStatus("current")
_CucsStatsCollectionPolicyFsmRn_Type = SnmpAdminString
_CucsStatsCollectionPolicyFsmRn_Object = MibTableColumn
cucsStatsCollectionPolicyFsmRn = _CucsStatsCollectionPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12, 1, 3),
    _CucsStatsCollectionPolicyFsmRn_Type()
)
cucsStatsCollectionPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmRn.setStatus("current")
_CucsStatsCollectionPolicyFsmCompletionTime_Type = DateAndTime
_CucsStatsCollectionPolicyFsmCompletionTime_Object = MibTableColumn
cucsStatsCollectionPolicyFsmCompletionTime = _CucsStatsCollectionPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12, 1, 4),
    _CucsStatsCollectionPolicyFsmCompletionTime_Type()
)
cucsStatsCollectionPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmCompletionTime.setStatus("current")
_CucsStatsCollectionPolicyFsmCurrentFsm_Type = CucsStatsCollectionPolicyFsmCurrentFsm
_CucsStatsCollectionPolicyFsmCurrentFsm_Object = MibTableColumn
cucsStatsCollectionPolicyFsmCurrentFsm = _CucsStatsCollectionPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12, 1, 5),
    _CucsStatsCollectionPolicyFsmCurrentFsm_Type()
)
cucsStatsCollectionPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmCurrentFsm.setStatus("current")
_CucsStatsCollectionPolicyFsmDescrData_Type = SnmpAdminString
_CucsStatsCollectionPolicyFsmDescrData_Object = MibTableColumn
cucsStatsCollectionPolicyFsmDescrData = _CucsStatsCollectionPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12, 1, 6),
    _CucsStatsCollectionPolicyFsmDescrData_Type()
)
cucsStatsCollectionPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmDescrData.setStatus("current")
_CucsStatsCollectionPolicyFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsStatsCollectionPolicyFsmFsmStatus_Object = MibTableColumn
cucsStatsCollectionPolicyFsmFsmStatus = _CucsStatsCollectionPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12, 1, 7),
    _CucsStatsCollectionPolicyFsmFsmStatus_Type()
)
cucsStatsCollectionPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmFsmStatus.setStatus("current")
_CucsStatsCollectionPolicyFsmProgress_Type = Gauge32
_CucsStatsCollectionPolicyFsmProgress_Object = MibTableColumn
cucsStatsCollectionPolicyFsmProgress = _CucsStatsCollectionPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12, 1, 8),
    _CucsStatsCollectionPolicyFsmProgress_Type()
)
cucsStatsCollectionPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmProgress.setStatus("current")
_CucsStatsCollectionPolicyFsmRmtErrCode_Type = Gauge32
_CucsStatsCollectionPolicyFsmRmtErrCode_Object = MibTableColumn
cucsStatsCollectionPolicyFsmRmtErrCode = _CucsStatsCollectionPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12, 1, 9),
    _CucsStatsCollectionPolicyFsmRmtErrCode_Type()
)
cucsStatsCollectionPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmRmtErrCode.setStatus("current")
_CucsStatsCollectionPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CucsStatsCollectionPolicyFsmRmtErrDescr_Object = MibTableColumn
cucsStatsCollectionPolicyFsmRmtErrDescr = _CucsStatsCollectionPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12, 1, 10),
    _CucsStatsCollectionPolicyFsmRmtErrDescr_Type()
)
cucsStatsCollectionPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmRmtErrDescr.setStatus("current")
_CucsStatsCollectionPolicyFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsStatsCollectionPolicyFsmRmtRslt_Object = MibTableColumn
cucsStatsCollectionPolicyFsmRmtRslt = _CucsStatsCollectionPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 12, 1, 11),
    _CucsStatsCollectionPolicyFsmRmtRslt_Type()
)
cucsStatsCollectionPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmRmtRslt.setStatus("current")
_CucsStatsCollectionPolicyFsmStageTable_Object = MibTable
cucsStatsCollectionPolicyFsmStageTable = _CucsStatsCollectionPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 13)
)
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStageTable.setStatus("current")
_CucsStatsCollectionPolicyFsmStageEntry_Object = MibTableRow
cucsStatsCollectionPolicyFsmStageEntry = _CucsStatsCollectionPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 13, 1)
)
cucsStatsCollectionPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-STATS-MIB", "cucsStatsCollectionPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStageEntry.setStatus("current")
_CucsStatsCollectionPolicyFsmStageInstanceId_Type = CucsManagedObjectId
_CucsStatsCollectionPolicyFsmStageInstanceId_Object = MibTableColumn
cucsStatsCollectionPolicyFsmStageInstanceId = _CucsStatsCollectionPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 13, 1, 1),
    _CucsStatsCollectionPolicyFsmStageInstanceId_Type()
)
cucsStatsCollectionPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStageInstanceId.setStatus("current")
_CucsStatsCollectionPolicyFsmStageDn_Type = CucsManagedObjectDn
_CucsStatsCollectionPolicyFsmStageDn_Object = MibTableColumn
cucsStatsCollectionPolicyFsmStageDn = _CucsStatsCollectionPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 13, 1, 2),
    _CucsStatsCollectionPolicyFsmStageDn_Type()
)
cucsStatsCollectionPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStageDn.setStatus("current")
_CucsStatsCollectionPolicyFsmStageRn_Type = SnmpAdminString
_CucsStatsCollectionPolicyFsmStageRn_Object = MibTableColumn
cucsStatsCollectionPolicyFsmStageRn = _CucsStatsCollectionPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 13, 1, 3),
    _CucsStatsCollectionPolicyFsmStageRn_Type()
)
cucsStatsCollectionPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStageRn.setStatus("current")
_CucsStatsCollectionPolicyFsmStageDescrData_Type = SnmpAdminString
_CucsStatsCollectionPolicyFsmStageDescrData_Object = MibTableColumn
cucsStatsCollectionPolicyFsmStageDescrData = _CucsStatsCollectionPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 13, 1, 4),
    _CucsStatsCollectionPolicyFsmStageDescrData_Type()
)
cucsStatsCollectionPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStageDescrData.setStatus("current")
_CucsStatsCollectionPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CucsStatsCollectionPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cucsStatsCollectionPolicyFsmStageLastUpdateTime = _CucsStatsCollectionPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 13, 1, 5),
    _CucsStatsCollectionPolicyFsmStageLastUpdateTime_Type()
)
cucsStatsCollectionPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStageLastUpdateTime.setStatus("current")
_CucsStatsCollectionPolicyFsmStageName_Type = CucsStatsCollectionPolicyFsmStageName
_CucsStatsCollectionPolicyFsmStageName_Object = MibTableColumn
cucsStatsCollectionPolicyFsmStageName = _CucsStatsCollectionPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 13, 1, 6),
    _CucsStatsCollectionPolicyFsmStageName_Type()
)
cucsStatsCollectionPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStageName.setStatus("current")
_CucsStatsCollectionPolicyFsmStageOrder_Type = Gauge32
_CucsStatsCollectionPolicyFsmStageOrder_Object = MibTableColumn
cucsStatsCollectionPolicyFsmStageOrder = _CucsStatsCollectionPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 13, 1, 7),
    _CucsStatsCollectionPolicyFsmStageOrder_Type()
)
cucsStatsCollectionPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStageOrder.setStatus("current")
_CucsStatsCollectionPolicyFsmStageRetry_Type = Gauge32
_CucsStatsCollectionPolicyFsmStageRetry_Object = MibTableColumn
cucsStatsCollectionPolicyFsmStageRetry = _CucsStatsCollectionPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 13, 1, 8),
    _CucsStatsCollectionPolicyFsmStageRetry_Type()
)
cucsStatsCollectionPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStageRetry.setStatus("current")
_CucsStatsCollectionPolicyFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsStatsCollectionPolicyFsmStageStageStatus_Object = MibTableColumn
cucsStatsCollectionPolicyFsmStageStageStatus = _CucsStatsCollectionPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 44, 13, 1, 9),
    _CucsStatsCollectionPolicyFsmStageStageStatus_Type()
)
cucsStatsCollectionPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsStatsCollectionPolicyFsmStageStageStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-STATS-MIB",
    **{"cucsStatsObjects": cucsStatsObjects,
       "cucsStatsCollectionPolicyTable": cucsStatsCollectionPolicyTable,
       "cucsStatsCollectionPolicyEntry": cucsStatsCollectionPolicyEntry,
       "cucsStatsCollectionPolicyInstanceId": cucsStatsCollectionPolicyInstanceId,
       "cucsStatsCollectionPolicyDn": cucsStatsCollectionPolicyDn,
       "cucsStatsCollectionPolicyRn": cucsStatsCollectionPolicyRn,
       "cucsStatsCollectionPolicyCollectionInterval": cucsStatsCollectionPolicyCollectionInterval,
       "cucsStatsCollectionPolicyFsmDescr": cucsStatsCollectionPolicyFsmDescr,
       "cucsStatsCollectionPolicyFsmPrev": cucsStatsCollectionPolicyFsmPrev,
       "cucsStatsCollectionPolicyFsmProgr": cucsStatsCollectionPolicyFsmProgr,
       "cucsStatsCollectionPolicyFsmRmtInvErrCode": cucsStatsCollectionPolicyFsmRmtInvErrCode,
       "cucsStatsCollectionPolicyFsmRmtInvErrDescr": cucsStatsCollectionPolicyFsmRmtInvErrDescr,
       "cucsStatsCollectionPolicyFsmRmtInvRslt": cucsStatsCollectionPolicyFsmRmtInvRslt,
       "cucsStatsCollectionPolicyFsmStageDescr": cucsStatsCollectionPolicyFsmStageDescr,
       "cucsStatsCollectionPolicyFsmStamp": cucsStatsCollectionPolicyFsmStamp,
       "cucsStatsCollectionPolicyFsmStatus": cucsStatsCollectionPolicyFsmStatus,
       "cucsStatsCollectionPolicyFsmTry": cucsStatsCollectionPolicyFsmTry,
       "cucsStatsCollectionPolicyId": cucsStatsCollectionPolicyId,
       "cucsStatsCollectionPolicyName": cucsStatsCollectionPolicyName,
       "cucsStatsCollectionPolicyReportingInterval": cucsStatsCollectionPolicyReportingInterval,
       "cucsStatsCollectionPolicyFsmTaskTable": cucsStatsCollectionPolicyFsmTaskTable,
       "cucsStatsCollectionPolicyFsmTaskEntry": cucsStatsCollectionPolicyFsmTaskEntry,
       "cucsStatsCollectionPolicyFsmTaskInstanceId": cucsStatsCollectionPolicyFsmTaskInstanceId,
       "cucsStatsCollectionPolicyFsmTaskDn": cucsStatsCollectionPolicyFsmTaskDn,
       "cucsStatsCollectionPolicyFsmTaskRn": cucsStatsCollectionPolicyFsmTaskRn,
       "cucsStatsCollectionPolicyFsmTaskCompletion": cucsStatsCollectionPolicyFsmTaskCompletion,
       "cucsStatsCollectionPolicyFsmTaskFlags": cucsStatsCollectionPolicyFsmTaskFlags,
       "cucsStatsCollectionPolicyFsmTaskItem": cucsStatsCollectionPolicyFsmTaskItem,
       "cucsStatsCollectionPolicyFsmTaskSeqId": cucsStatsCollectionPolicyFsmTaskSeqId,
       "cucsStatsHolderTable": cucsStatsHolderTable,
       "cucsStatsHolderEntry": cucsStatsHolderEntry,
       "cucsStatsHolderInstanceId": cucsStatsHolderInstanceId,
       "cucsStatsHolderDn": cucsStatsHolderDn,
       "cucsStatsHolderRn": cucsStatsHolderRn,
       "cucsStatsHolderName": cucsStatsHolderName,
       "cucsStatsThr32DefinitionTable": cucsStatsThr32DefinitionTable,
       "cucsStatsThr32DefinitionEntry": cucsStatsThr32DefinitionEntry,
       "cucsStatsThr32DefinitionInstanceId": cucsStatsThr32DefinitionInstanceId,
       "cucsStatsThr32DefinitionDn": cucsStatsThr32DefinitionDn,
       "cucsStatsThr32DefinitionRn": cucsStatsThr32DefinitionRn,
       "cucsStatsThr32DefinitionDescr": cucsStatsThr32DefinitionDescr,
       "cucsStatsThr32DefinitionIntId": cucsStatsThr32DefinitionIntId,
       "cucsStatsThr32DefinitionName": cucsStatsThr32DefinitionName,
       "cucsStatsThr32DefinitionNormalValue": cucsStatsThr32DefinitionNormalValue,
       "cucsStatsThr32DefinitionPropId": cucsStatsThr32DefinitionPropId,
       "cucsStatsThr32DefinitionPropType": cucsStatsThr32DefinitionPropType,
       "cucsStatsThr32DefinitionPolicyLevel": cucsStatsThr32DefinitionPolicyLevel,
       "cucsStatsThr32DefinitionPolicyOwner": cucsStatsThr32DefinitionPolicyOwner,
       "cucsStatsThr32DefinitionAutoRecovery": cucsStatsThr32DefinitionAutoRecovery,
       "cucsStatsThr32DefinitionAutoRecoveryTime": cucsStatsThr32DefinitionAutoRecoveryTime,
       "cucsStatsThr32DefinitionErrorDisableFiPort": cucsStatsThr32DefinitionErrorDisableFiPort,
       "cucsStatsThr32ValueTable": cucsStatsThr32ValueTable,
       "cucsStatsThr32ValueEntry": cucsStatsThr32ValueEntry,
       "cucsStatsThr32ValueInstanceId": cucsStatsThr32ValueInstanceId,
       "cucsStatsThr32ValueDn": cucsStatsThr32ValueDn,
       "cucsStatsThr32ValueRn": cucsStatsThr32ValueRn,
       "cucsStatsThr32ValueDeescalating": cucsStatsThr32ValueDeescalating,
       "cucsStatsThr32ValueDescr": cucsStatsThr32ValueDescr,
       "cucsStatsThr32ValueDirection": cucsStatsThr32ValueDirection,
       "cucsStatsThr32ValueEscalating": cucsStatsThr32ValueEscalating,
       "cucsStatsThr32ValueIntId": cucsStatsThr32ValueIntId,
       "cucsStatsThr32ValueName": cucsStatsThr32ValueName,
       "cucsStatsThr32ValuePropType": cucsStatsThr32ValuePropType,
       "cucsStatsThr32ValueSeverity": cucsStatsThr32ValueSeverity,
       "cucsStatsThr32ValuePolicyLevel": cucsStatsThr32ValuePolicyLevel,
       "cucsStatsThr32ValuePolicyOwner": cucsStatsThr32ValuePolicyOwner,
       "cucsStatsThr64DefinitionTable": cucsStatsThr64DefinitionTable,
       "cucsStatsThr64DefinitionEntry": cucsStatsThr64DefinitionEntry,
       "cucsStatsThr64DefinitionInstanceId": cucsStatsThr64DefinitionInstanceId,
       "cucsStatsThr64DefinitionDn": cucsStatsThr64DefinitionDn,
       "cucsStatsThr64DefinitionRn": cucsStatsThr64DefinitionRn,
       "cucsStatsThr64DefinitionDescr": cucsStatsThr64DefinitionDescr,
       "cucsStatsThr64DefinitionIntId": cucsStatsThr64DefinitionIntId,
       "cucsStatsThr64DefinitionName": cucsStatsThr64DefinitionName,
       "cucsStatsThr64DefinitionNormalValue": cucsStatsThr64DefinitionNormalValue,
       "cucsStatsThr64DefinitionPropId": cucsStatsThr64DefinitionPropId,
       "cucsStatsThr64DefinitionPropType": cucsStatsThr64DefinitionPropType,
       "cucsStatsThr64DefinitionPolicyLevel": cucsStatsThr64DefinitionPolicyLevel,
       "cucsStatsThr64DefinitionPolicyOwner": cucsStatsThr64DefinitionPolicyOwner,
       "cucsStatsThr64DefinitionAutoRecovery": cucsStatsThr64DefinitionAutoRecovery,
       "cucsStatsThr64DefinitionAutoRecoveryTime": cucsStatsThr64DefinitionAutoRecoveryTime,
       "cucsStatsThr64DefinitionErrorDisableFiPort": cucsStatsThr64DefinitionErrorDisableFiPort,
       "cucsStatsThr64ValueTable": cucsStatsThr64ValueTable,
       "cucsStatsThr64ValueEntry": cucsStatsThr64ValueEntry,
       "cucsStatsThr64ValueInstanceId": cucsStatsThr64ValueInstanceId,
       "cucsStatsThr64ValueDn": cucsStatsThr64ValueDn,
       "cucsStatsThr64ValueRn": cucsStatsThr64ValueRn,
       "cucsStatsThr64ValueDeescalating": cucsStatsThr64ValueDeescalating,
       "cucsStatsThr64ValueDescr": cucsStatsThr64ValueDescr,
       "cucsStatsThr64ValueDirection": cucsStatsThr64ValueDirection,
       "cucsStatsThr64ValueEscalating": cucsStatsThr64ValueEscalating,
       "cucsStatsThr64ValueIntId": cucsStatsThr64ValueIntId,
       "cucsStatsThr64ValueName": cucsStatsThr64ValueName,
       "cucsStatsThr64ValuePropType": cucsStatsThr64ValuePropType,
       "cucsStatsThr64ValueSeverity": cucsStatsThr64ValueSeverity,
       "cucsStatsThr64ValuePolicyLevel": cucsStatsThr64ValuePolicyLevel,
       "cucsStatsThr64ValuePolicyOwner": cucsStatsThr64ValuePolicyOwner,
       "cucsStatsThrFloatDefinitionTable": cucsStatsThrFloatDefinitionTable,
       "cucsStatsThrFloatDefinitionEntry": cucsStatsThrFloatDefinitionEntry,
       "cucsStatsThrFloatDefinitionInstanceId": cucsStatsThrFloatDefinitionInstanceId,
       "cucsStatsThrFloatDefinitionDn": cucsStatsThrFloatDefinitionDn,
       "cucsStatsThrFloatDefinitionRn": cucsStatsThrFloatDefinitionRn,
       "cucsStatsThrFloatDefinitionDescr": cucsStatsThrFloatDefinitionDescr,
       "cucsStatsThrFloatDefinitionIntId": cucsStatsThrFloatDefinitionIntId,
       "cucsStatsThrFloatDefinitionName": cucsStatsThrFloatDefinitionName,
       "cucsStatsThrFloatDefinitionNormalValue": cucsStatsThrFloatDefinitionNormalValue,
       "cucsStatsThrFloatDefinitionPropId": cucsStatsThrFloatDefinitionPropId,
       "cucsStatsThrFloatDefinitionPropType": cucsStatsThrFloatDefinitionPropType,
       "cucsStatsThrFloatDefinitionPolicyLevel": cucsStatsThrFloatDefinitionPolicyLevel,
       "cucsStatsThrFloatDefinitionPolicyOwner": cucsStatsThrFloatDefinitionPolicyOwner,
       "cucsStatsThrFloatDefinitionAutoRecovery": cucsStatsThrFloatDefinitionAutoRecovery,
       "cucsStatsThrFloatDefinitionAutoRecoveryTime": cucsStatsThrFloatDefinitionAutoRecoveryTime,
       "cucsStatsThrFloatDefinitionErrorDisableFiPort": cucsStatsThrFloatDefinitionErrorDisableFiPort,
       "cucsStatsThrFloatValueTable": cucsStatsThrFloatValueTable,
       "cucsStatsThrFloatValueEntry": cucsStatsThrFloatValueEntry,
       "cucsStatsThrFloatValueInstanceId": cucsStatsThrFloatValueInstanceId,
       "cucsStatsThrFloatValueDn": cucsStatsThrFloatValueDn,
       "cucsStatsThrFloatValueRn": cucsStatsThrFloatValueRn,
       "cucsStatsThrFloatValueDeescalating": cucsStatsThrFloatValueDeescalating,
       "cucsStatsThrFloatValueDescr": cucsStatsThrFloatValueDescr,
       "cucsStatsThrFloatValueDirection": cucsStatsThrFloatValueDirection,
       "cucsStatsThrFloatValueEscalating": cucsStatsThrFloatValueEscalating,
       "cucsStatsThrFloatValueIntId": cucsStatsThrFloatValueIntId,
       "cucsStatsThrFloatValueName": cucsStatsThrFloatValueName,
       "cucsStatsThrFloatValuePropType": cucsStatsThrFloatValuePropType,
       "cucsStatsThrFloatValueSeverity": cucsStatsThrFloatValueSeverity,
       "cucsStatsThrFloatValuePolicyLevel": cucsStatsThrFloatValuePolicyLevel,
       "cucsStatsThrFloatValuePolicyOwner": cucsStatsThrFloatValuePolicyOwner,
       "cucsStatsThresholdClassTable": cucsStatsThresholdClassTable,
       "cucsStatsThresholdClassEntry": cucsStatsThresholdClassEntry,
       "cucsStatsThresholdClassInstanceId": cucsStatsThresholdClassInstanceId,
       "cucsStatsThresholdClassDn": cucsStatsThresholdClassDn,
       "cucsStatsThresholdClassRn": cucsStatsThresholdClassRn,
       "cucsStatsThresholdClassDescr": cucsStatsThresholdClassDescr,
       "cucsStatsThresholdClassIntId": cucsStatsThresholdClassIntId,
       "cucsStatsThresholdClassName": cucsStatsThresholdClassName,
       "cucsStatsThresholdClassStatsClassId": cucsStatsThresholdClassStatsClassId,
       "cucsStatsThresholdClassPolicyLevel": cucsStatsThresholdClassPolicyLevel,
       "cucsStatsThresholdClassPolicyOwner": cucsStatsThresholdClassPolicyOwner,
       "cucsStatsThresholdPolicyTable": cucsStatsThresholdPolicyTable,
       "cucsStatsThresholdPolicyEntry": cucsStatsThresholdPolicyEntry,
       "cucsStatsThresholdPolicyInstanceId": cucsStatsThresholdPolicyInstanceId,
       "cucsStatsThresholdPolicyDn": cucsStatsThresholdPolicyDn,
       "cucsStatsThresholdPolicyRn": cucsStatsThresholdPolicyRn,
       "cucsStatsThresholdPolicyDescr": cucsStatsThresholdPolicyDescr,
       "cucsStatsThresholdPolicyIntId": cucsStatsThresholdPolicyIntId,
       "cucsStatsThresholdPolicyName": cucsStatsThresholdPolicyName,
       "cucsStatsThresholdPolicyPolicyLevel": cucsStatsThresholdPolicyPolicyLevel,
       "cucsStatsThresholdPolicyPolicyOwner": cucsStatsThresholdPolicyPolicyOwner,
       "cucsStatsThresholdPolicyDefaultThresholdsAdded": cucsStatsThresholdPolicyDefaultThresholdsAdded,
       "cucsStatsCollectionPolicyFsmTable": cucsStatsCollectionPolicyFsmTable,
       "cucsStatsCollectionPolicyFsmEntry": cucsStatsCollectionPolicyFsmEntry,
       "cucsStatsCollectionPolicyFsmInstanceId": cucsStatsCollectionPolicyFsmInstanceId,
       "cucsStatsCollectionPolicyFsmDn": cucsStatsCollectionPolicyFsmDn,
       "cucsStatsCollectionPolicyFsmRn": cucsStatsCollectionPolicyFsmRn,
       "cucsStatsCollectionPolicyFsmCompletionTime": cucsStatsCollectionPolicyFsmCompletionTime,
       "cucsStatsCollectionPolicyFsmCurrentFsm": cucsStatsCollectionPolicyFsmCurrentFsm,
       "cucsStatsCollectionPolicyFsmDescrData": cucsStatsCollectionPolicyFsmDescrData,
       "cucsStatsCollectionPolicyFsmFsmStatus": cucsStatsCollectionPolicyFsmFsmStatus,
       "cucsStatsCollectionPolicyFsmProgress": cucsStatsCollectionPolicyFsmProgress,
       "cucsStatsCollectionPolicyFsmRmtErrCode": cucsStatsCollectionPolicyFsmRmtErrCode,
       "cucsStatsCollectionPolicyFsmRmtErrDescr": cucsStatsCollectionPolicyFsmRmtErrDescr,
       "cucsStatsCollectionPolicyFsmRmtRslt": cucsStatsCollectionPolicyFsmRmtRslt,
       "cucsStatsCollectionPolicyFsmStageTable": cucsStatsCollectionPolicyFsmStageTable,
       "cucsStatsCollectionPolicyFsmStageEntry": cucsStatsCollectionPolicyFsmStageEntry,
       "cucsStatsCollectionPolicyFsmStageInstanceId": cucsStatsCollectionPolicyFsmStageInstanceId,
       "cucsStatsCollectionPolicyFsmStageDn": cucsStatsCollectionPolicyFsmStageDn,
       "cucsStatsCollectionPolicyFsmStageRn": cucsStatsCollectionPolicyFsmStageRn,
       "cucsStatsCollectionPolicyFsmStageDescrData": cucsStatsCollectionPolicyFsmStageDescrData,
       "cucsStatsCollectionPolicyFsmStageLastUpdateTime": cucsStatsCollectionPolicyFsmStageLastUpdateTime,
       "cucsStatsCollectionPolicyFsmStageName": cucsStatsCollectionPolicyFsmStageName,
       "cucsStatsCollectionPolicyFsmStageOrder": cucsStatsCollectionPolicyFsmStageOrder,
       "cucsStatsCollectionPolicyFsmStageRetry": cucsStatsCollectionPolicyFsmStageRetry,
       "cucsStatsCollectionPolicyFsmStageStageStatus": cucsStatsCollectionPolicyFsmStageStageStatus}
)
