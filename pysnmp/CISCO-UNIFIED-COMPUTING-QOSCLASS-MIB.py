# SNMP MIB module (CISCO-UNIFIED-COMPUTING-QOSCLASS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-QOSCLASS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:15 2024
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
 CucsPolicyPolicyOwner,
 CucsQosclassDefinitionFsmCurrentFsm,
 CucsQosclassDefinitionFsmStageName,
 CucsQosclassDefinitionFsmTaskItem,
 CucsQosclassEthBEAdminState,
 CucsQosclassEthBEDrop,
 CucsQosclassEthBEPriority,
 CucsQosclassEthClassifiedAdminState,
 CucsQosclassEthClassifiedDrop,
 CucsQosclassEthClassifiedPriority,
 CucsQosclassFcAdminState,
 CucsQosclassFcDrop,
 CucsQosclassFcPriority) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsPolicyPolicyOwner",
    "CucsQosclassDefinitionFsmCurrentFsm",
    "CucsQosclassDefinitionFsmStageName",
    "CucsQosclassDefinitionFsmTaskItem",
    "CucsQosclassEthBEAdminState",
    "CucsQosclassEthBEDrop",
    "CucsQosclassEthBEPriority",
    "CucsQosclassEthClassifiedAdminState",
    "CucsQosclassEthClassifiedDrop",
    "CucsQosclassEthClassifiedPriority",
    "CucsQosclassFcAdminState",
    "CucsQosclassFcDrop",
    "CucsQosclassFcPriority")

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

cucsQosclassObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsQosclassDefinitionTable_Object = MibTable
cucsQosclassDefinitionTable = _CucsQosclassDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1)
)
if mibBuilder.loadTexts:
    cucsQosclassDefinitionTable.setStatus("current")
_CucsQosclassDefinitionEntry_Object = MibTableRow
cucsQosclassDefinitionEntry = _CucsQosclassDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1)
)
cucsQosclassDefinitionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-QOSCLASS-MIB", "cucsQosclassDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsQosclassDefinitionEntry.setStatus("current")
_CucsQosclassDefinitionInstanceId_Type = CucsManagedObjectId
_CucsQosclassDefinitionInstanceId_Object = MibTableColumn
cucsQosclassDefinitionInstanceId = _CucsQosclassDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 1),
    _CucsQosclassDefinitionInstanceId_Type()
)
cucsQosclassDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionInstanceId.setStatus("current")
_CucsQosclassDefinitionDn_Type = CucsManagedObjectDn
_CucsQosclassDefinitionDn_Object = MibTableColumn
cucsQosclassDefinitionDn = _CucsQosclassDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 2),
    _CucsQosclassDefinitionDn_Type()
)
cucsQosclassDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionDn.setStatus("current")
_CucsQosclassDefinitionRn_Type = SnmpAdminString
_CucsQosclassDefinitionRn_Object = MibTableColumn
cucsQosclassDefinitionRn = _CucsQosclassDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 3),
    _CucsQosclassDefinitionRn_Type()
)
cucsQosclassDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionRn.setStatus("current")
_CucsQosclassDefinitionDescr_Type = SnmpAdminString
_CucsQosclassDefinitionDescr_Object = MibTableColumn
cucsQosclassDefinitionDescr = _CucsQosclassDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 4),
    _CucsQosclassDefinitionDescr_Type()
)
cucsQosclassDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionDescr.setStatus("current")
_CucsQosclassDefinitionFsmDescr_Type = SnmpAdminString
_CucsQosclassDefinitionFsmDescr_Object = MibTableColumn
cucsQosclassDefinitionFsmDescr = _CucsQosclassDefinitionFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 5),
    _CucsQosclassDefinitionFsmDescr_Type()
)
cucsQosclassDefinitionFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmDescr.setStatus("current")
_CucsQosclassDefinitionFsmPrev_Type = SnmpAdminString
_CucsQosclassDefinitionFsmPrev_Object = MibTableColumn
cucsQosclassDefinitionFsmPrev = _CucsQosclassDefinitionFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 6),
    _CucsQosclassDefinitionFsmPrev_Type()
)
cucsQosclassDefinitionFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmPrev.setStatus("current")
_CucsQosclassDefinitionFsmProgr_Type = Gauge32
_CucsQosclassDefinitionFsmProgr_Object = MibTableColumn
cucsQosclassDefinitionFsmProgr = _CucsQosclassDefinitionFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 7),
    _CucsQosclassDefinitionFsmProgr_Type()
)
cucsQosclassDefinitionFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmProgr.setStatus("current")
_CucsQosclassDefinitionFsmRmtInvErrCode_Type = Gauge32
_CucsQosclassDefinitionFsmRmtInvErrCode_Object = MibTableColumn
cucsQosclassDefinitionFsmRmtInvErrCode = _CucsQosclassDefinitionFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 8),
    _CucsQosclassDefinitionFsmRmtInvErrCode_Type()
)
cucsQosclassDefinitionFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmRmtInvErrCode.setStatus("current")
_CucsQosclassDefinitionFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsQosclassDefinitionFsmRmtInvErrDescr_Object = MibTableColumn
cucsQosclassDefinitionFsmRmtInvErrDescr = _CucsQosclassDefinitionFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 9),
    _CucsQosclassDefinitionFsmRmtInvErrDescr_Type()
)
cucsQosclassDefinitionFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmRmtInvErrDescr.setStatus("current")
_CucsQosclassDefinitionFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsQosclassDefinitionFsmRmtInvRslt_Object = MibTableColumn
cucsQosclassDefinitionFsmRmtInvRslt = _CucsQosclassDefinitionFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 10),
    _CucsQosclassDefinitionFsmRmtInvRslt_Type()
)
cucsQosclassDefinitionFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmRmtInvRslt.setStatus("current")
_CucsQosclassDefinitionFsmStageDescr_Type = SnmpAdminString
_CucsQosclassDefinitionFsmStageDescr_Object = MibTableColumn
cucsQosclassDefinitionFsmStageDescr = _CucsQosclassDefinitionFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 11),
    _CucsQosclassDefinitionFsmStageDescr_Type()
)
cucsQosclassDefinitionFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStageDescr.setStatus("current")
_CucsQosclassDefinitionFsmStamp_Type = DateAndTime
_CucsQosclassDefinitionFsmStamp_Object = MibTableColumn
cucsQosclassDefinitionFsmStamp = _CucsQosclassDefinitionFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 12),
    _CucsQosclassDefinitionFsmStamp_Type()
)
cucsQosclassDefinitionFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStamp.setStatus("current")
_CucsQosclassDefinitionFsmStatus_Type = SnmpAdminString
_CucsQosclassDefinitionFsmStatus_Object = MibTableColumn
cucsQosclassDefinitionFsmStatus = _CucsQosclassDefinitionFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 13),
    _CucsQosclassDefinitionFsmStatus_Type()
)
cucsQosclassDefinitionFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStatus.setStatus("current")
_CucsQosclassDefinitionFsmTry_Type = Gauge32
_CucsQosclassDefinitionFsmTry_Object = MibTableColumn
cucsQosclassDefinitionFsmTry = _CucsQosclassDefinitionFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 14),
    _CucsQosclassDefinitionFsmTry_Type()
)
cucsQosclassDefinitionFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmTry.setStatus("current")
_CucsQosclassDefinitionIntId_Type = SnmpAdminString
_CucsQosclassDefinitionIntId_Object = MibTableColumn
cucsQosclassDefinitionIntId = _CucsQosclassDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 15),
    _CucsQosclassDefinitionIntId_Type()
)
cucsQosclassDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionIntId.setStatus("current")
_CucsQosclassDefinitionName_Type = SnmpAdminString
_CucsQosclassDefinitionName_Object = MibTableColumn
cucsQosclassDefinitionName = _CucsQosclassDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 16),
    _CucsQosclassDefinitionName_Type()
)
cucsQosclassDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionName.setStatus("current")
_CucsQosclassDefinitionPolicyLevel_Type = Gauge32
_CucsQosclassDefinitionPolicyLevel_Object = MibTableColumn
cucsQosclassDefinitionPolicyLevel = _CucsQosclassDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 17),
    _CucsQosclassDefinitionPolicyLevel_Type()
)
cucsQosclassDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionPolicyLevel.setStatus("current")
_CucsQosclassDefinitionPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsQosclassDefinitionPolicyOwner_Object = MibTableColumn
cucsQosclassDefinitionPolicyOwner = _CucsQosclassDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 18),
    _CucsQosclassDefinitionPolicyOwner_Type()
)
cucsQosclassDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionPolicyOwner.setStatus("current")
_CucsQosclassDefinitionMmuPercent_Type = Gauge32
_CucsQosclassDefinitionMmuPercent_Object = MibTableColumn
cucsQosclassDefinitionMmuPercent = _CucsQosclassDefinitionMmuPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 19),
    _CucsQosclassDefinitionMmuPercent_Type()
)
cucsQosclassDefinitionMmuPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionMmuPercent.setStatus("current")
_CucsQosclassDefinitionNumBreakoutPort_Type = Gauge32
_CucsQosclassDefinitionNumBreakoutPort_Object = MibTableColumn
cucsQosclassDefinitionNumBreakoutPort = _CucsQosclassDefinitionNumBreakoutPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 1, 1, 20),
    _CucsQosclassDefinitionNumBreakoutPort_Type()
)
cucsQosclassDefinitionNumBreakoutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionNumBreakoutPort.setStatus("current")
_CucsQosclassDefinitionFsmTaskTable_Object = MibTable
cucsQosclassDefinitionFsmTaskTable = _CucsQosclassDefinitionFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 2)
)
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmTaskTable.setStatus("current")
_CucsQosclassDefinitionFsmTaskEntry_Object = MibTableRow
cucsQosclassDefinitionFsmTaskEntry = _CucsQosclassDefinitionFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 2, 1)
)
cucsQosclassDefinitionFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-QOSCLASS-MIB", "cucsQosclassDefinitionFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmTaskEntry.setStatus("current")
_CucsQosclassDefinitionFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsQosclassDefinitionFsmTaskInstanceId_Object = MibTableColumn
cucsQosclassDefinitionFsmTaskInstanceId = _CucsQosclassDefinitionFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 2, 1, 1),
    _CucsQosclassDefinitionFsmTaskInstanceId_Type()
)
cucsQosclassDefinitionFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmTaskInstanceId.setStatus("current")
_CucsQosclassDefinitionFsmTaskDn_Type = CucsManagedObjectDn
_CucsQosclassDefinitionFsmTaskDn_Object = MibTableColumn
cucsQosclassDefinitionFsmTaskDn = _CucsQosclassDefinitionFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 2, 1, 2),
    _CucsQosclassDefinitionFsmTaskDn_Type()
)
cucsQosclassDefinitionFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmTaskDn.setStatus("current")
_CucsQosclassDefinitionFsmTaskRn_Type = SnmpAdminString
_CucsQosclassDefinitionFsmTaskRn_Object = MibTableColumn
cucsQosclassDefinitionFsmTaskRn = _CucsQosclassDefinitionFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 2, 1, 3),
    _CucsQosclassDefinitionFsmTaskRn_Type()
)
cucsQosclassDefinitionFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmTaskRn.setStatus("current")
_CucsQosclassDefinitionFsmTaskCompletion_Type = CucsFsmCompletion
_CucsQosclassDefinitionFsmTaskCompletion_Object = MibTableColumn
cucsQosclassDefinitionFsmTaskCompletion = _CucsQosclassDefinitionFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 2, 1, 4),
    _CucsQosclassDefinitionFsmTaskCompletion_Type()
)
cucsQosclassDefinitionFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmTaskCompletion.setStatus("current")
_CucsQosclassDefinitionFsmTaskFlags_Type = CucsFsmFlags
_CucsQosclassDefinitionFsmTaskFlags_Object = MibTableColumn
cucsQosclassDefinitionFsmTaskFlags = _CucsQosclassDefinitionFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 2, 1, 5),
    _CucsQosclassDefinitionFsmTaskFlags_Type()
)
cucsQosclassDefinitionFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmTaskFlags.setStatus("current")
_CucsQosclassDefinitionFsmTaskItem_Type = CucsQosclassDefinitionFsmTaskItem
_CucsQosclassDefinitionFsmTaskItem_Object = MibTableColumn
cucsQosclassDefinitionFsmTaskItem = _CucsQosclassDefinitionFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 2, 1, 6),
    _CucsQosclassDefinitionFsmTaskItem_Type()
)
cucsQosclassDefinitionFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmTaskItem.setStatus("current")
_CucsQosclassDefinitionFsmTaskSeqId_Type = Gauge32
_CucsQosclassDefinitionFsmTaskSeqId_Object = MibTableColumn
cucsQosclassDefinitionFsmTaskSeqId = _CucsQosclassDefinitionFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 2, 1, 7),
    _CucsQosclassDefinitionFsmTaskSeqId_Type()
)
cucsQosclassDefinitionFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmTaskSeqId.setStatus("current")
_CucsQosclassEthBETable_Object = MibTable
cucsQosclassEthBETable = _CucsQosclassEthBETable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3)
)
if mibBuilder.loadTexts:
    cucsQosclassEthBETable.setStatus("current")
_CucsQosclassEthBEEntry_Object = MibTableRow
cucsQosclassEthBEEntry = _CucsQosclassEthBEEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1)
)
cucsQosclassEthBEEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-QOSCLASS-MIB", "cucsQosclassEthBEInstanceId"),
)
if mibBuilder.loadTexts:
    cucsQosclassEthBEEntry.setStatus("current")
_CucsQosclassEthBEInstanceId_Type = CucsManagedObjectId
_CucsQosclassEthBEInstanceId_Object = MibTableColumn
cucsQosclassEthBEInstanceId = _CucsQosclassEthBEInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1, 1),
    _CucsQosclassEthBEInstanceId_Type()
)
cucsQosclassEthBEInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsQosclassEthBEInstanceId.setStatus("current")
_CucsQosclassEthBEDn_Type = CucsManagedObjectDn
_CucsQosclassEthBEDn_Object = MibTableColumn
cucsQosclassEthBEDn = _CucsQosclassEthBEDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1, 2),
    _CucsQosclassEthBEDn_Type()
)
cucsQosclassEthBEDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthBEDn.setStatus("current")
_CucsQosclassEthBERn_Type = SnmpAdminString
_CucsQosclassEthBERn_Object = MibTableColumn
cucsQosclassEthBERn = _CucsQosclassEthBERn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1, 3),
    _CucsQosclassEthBERn_Type()
)
cucsQosclassEthBERn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthBERn.setStatus("current")
_CucsQosclassEthBEAdminState_Type = CucsQosclassEthBEAdminState
_CucsQosclassEthBEAdminState_Object = MibTableColumn
cucsQosclassEthBEAdminState = _CucsQosclassEthBEAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1, 4),
    _CucsQosclassEthBEAdminState_Type()
)
cucsQosclassEthBEAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthBEAdminState.setStatus("current")
_CucsQosclassEthBEBwPercent_Type = Gauge32
_CucsQosclassEthBEBwPercent_Object = MibTableColumn
cucsQosclassEthBEBwPercent = _CucsQosclassEthBEBwPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1, 5),
    _CucsQosclassEthBEBwPercent_Type()
)
cucsQosclassEthBEBwPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthBEBwPercent.setStatus("current")
_CucsQosclassEthBECos_Type = Gauge32
_CucsQosclassEthBECos_Object = MibTableColumn
cucsQosclassEthBECos = _CucsQosclassEthBECos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1, 6),
    _CucsQosclassEthBECos_Type()
)
cucsQosclassEthBECos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthBECos.setStatus("current")
_CucsQosclassEthBEDrop_Type = CucsQosclassEthBEDrop
_CucsQosclassEthBEDrop_Object = MibTableColumn
cucsQosclassEthBEDrop = _CucsQosclassEthBEDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1, 7),
    _CucsQosclassEthBEDrop_Type()
)
cucsQosclassEthBEDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthBEDrop.setStatus("current")
_CucsQosclassEthBEMtu_Type = SnmpAdminString
_CucsQosclassEthBEMtu_Object = MibTableColumn
cucsQosclassEthBEMtu = _CucsQosclassEthBEMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1, 8),
    _CucsQosclassEthBEMtu_Type()
)
cucsQosclassEthBEMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthBEMtu.setStatus("current")
_CucsQosclassEthBEMulticastOptimize_Type = TruthValue
_CucsQosclassEthBEMulticastOptimize_Object = MibTableColumn
cucsQosclassEthBEMulticastOptimize = _CucsQosclassEthBEMulticastOptimize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1, 9),
    _CucsQosclassEthBEMulticastOptimize_Type()
)
cucsQosclassEthBEMulticastOptimize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthBEMulticastOptimize.setStatus("current")
_CucsQosclassEthBEName_Type = SnmpAdminString
_CucsQosclassEthBEName_Object = MibTableColumn
cucsQosclassEthBEName = _CucsQosclassEthBEName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1, 10),
    _CucsQosclassEthBEName_Type()
)
cucsQosclassEthBEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthBEName.setStatus("current")
_CucsQosclassEthBEPriority_Type = CucsQosclassEthBEPriority
_CucsQosclassEthBEPriority_Object = MibTableColumn
cucsQosclassEthBEPriority = _CucsQosclassEthBEPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1, 11),
    _CucsQosclassEthBEPriority_Type()
)
cucsQosclassEthBEPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthBEPriority.setStatus("current")
_CucsQosclassEthBEWeight_Type = Gauge32
_CucsQosclassEthBEWeight_Object = MibTableColumn
cucsQosclassEthBEWeight = _CucsQosclassEthBEWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 3, 1, 12),
    _CucsQosclassEthBEWeight_Type()
)
cucsQosclassEthBEWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthBEWeight.setStatus("current")
_CucsQosclassEthClassifiedTable_Object = MibTable
cucsQosclassEthClassifiedTable = _CucsQosclassEthClassifiedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4)
)
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedTable.setStatus("current")
_CucsQosclassEthClassifiedEntry_Object = MibTableRow
cucsQosclassEthClassifiedEntry = _CucsQosclassEthClassifiedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1)
)
cucsQosclassEthClassifiedEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-QOSCLASS-MIB", "cucsQosclassEthClassifiedInstanceId"),
)
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedEntry.setStatus("current")
_CucsQosclassEthClassifiedInstanceId_Type = CucsManagedObjectId
_CucsQosclassEthClassifiedInstanceId_Object = MibTableColumn
cucsQosclassEthClassifiedInstanceId = _CucsQosclassEthClassifiedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1, 1),
    _CucsQosclassEthClassifiedInstanceId_Type()
)
cucsQosclassEthClassifiedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedInstanceId.setStatus("current")
_CucsQosclassEthClassifiedDn_Type = CucsManagedObjectDn
_CucsQosclassEthClassifiedDn_Object = MibTableColumn
cucsQosclassEthClassifiedDn = _CucsQosclassEthClassifiedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1, 2),
    _CucsQosclassEthClassifiedDn_Type()
)
cucsQosclassEthClassifiedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedDn.setStatus("current")
_CucsQosclassEthClassifiedRn_Type = SnmpAdminString
_CucsQosclassEthClassifiedRn_Object = MibTableColumn
cucsQosclassEthClassifiedRn = _CucsQosclassEthClassifiedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1, 3),
    _CucsQosclassEthClassifiedRn_Type()
)
cucsQosclassEthClassifiedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedRn.setStatus("current")
_CucsQosclassEthClassifiedAdminState_Type = CucsQosclassEthClassifiedAdminState
_CucsQosclassEthClassifiedAdminState_Object = MibTableColumn
cucsQosclassEthClassifiedAdminState = _CucsQosclassEthClassifiedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1, 4),
    _CucsQosclassEthClassifiedAdminState_Type()
)
cucsQosclassEthClassifiedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedAdminState.setStatus("current")
_CucsQosclassEthClassifiedBwPercent_Type = Gauge32
_CucsQosclassEthClassifiedBwPercent_Object = MibTableColumn
cucsQosclassEthClassifiedBwPercent = _CucsQosclassEthClassifiedBwPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1, 5),
    _CucsQosclassEthClassifiedBwPercent_Type()
)
cucsQosclassEthClassifiedBwPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedBwPercent.setStatus("current")
_CucsQosclassEthClassifiedCos_Type = Gauge32
_CucsQosclassEthClassifiedCos_Object = MibTableColumn
cucsQosclassEthClassifiedCos = _CucsQosclassEthClassifiedCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1, 6),
    _CucsQosclassEthClassifiedCos_Type()
)
cucsQosclassEthClassifiedCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedCos.setStatus("current")
_CucsQosclassEthClassifiedDrop_Type = CucsQosclassEthClassifiedDrop
_CucsQosclassEthClassifiedDrop_Object = MibTableColumn
cucsQosclassEthClassifiedDrop = _CucsQosclassEthClassifiedDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1, 7),
    _CucsQosclassEthClassifiedDrop_Type()
)
cucsQosclassEthClassifiedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedDrop.setStatus("current")
_CucsQosclassEthClassifiedMtu_Type = SnmpAdminString
_CucsQosclassEthClassifiedMtu_Object = MibTableColumn
cucsQosclassEthClassifiedMtu = _CucsQosclassEthClassifiedMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1, 8),
    _CucsQosclassEthClassifiedMtu_Type()
)
cucsQosclassEthClassifiedMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedMtu.setStatus("current")
_CucsQosclassEthClassifiedMulticastOptimize_Type = TruthValue
_CucsQosclassEthClassifiedMulticastOptimize_Object = MibTableColumn
cucsQosclassEthClassifiedMulticastOptimize = _CucsQosclassEthClassifiedMulticastOptimize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1, 9),
    _CucsQosclassEthClassifiedMulticastOptimize_Type()
)
cucsQosclassEthClassifiedMulticastOptimize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedMulticastOptimize.setStatus("current")
_CucsQosclassEthClassifiedName_Type = SnmpAdminString
_CucsQosclassEthClassifiedName_Object = MibTableColumn
cucsQosclassEthClassifiedName = _CucsQosclassEthClassifiedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1, 10),
    _CucsQosclassEthClassifiedName_Type()
)
cucsQosclassEthClassifiedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedName.setStatus("current")
_CucsQosclassEthClassifiedPriority_Type = CucsQosclassEthClassifiedPriority
_CucsQosclassEthClassifiedPriority_Object = MibTableColumn
cucsQosclassEthClassifiedPriority = _CucsQosclassEthClassifiedPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1, 11),
    _CucsQosclassEthClassifiedPriority_Type()
)
cucsQosclassEthClassifiedPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedPriority.setStatus("current")
_CucsQosclassEthClassifiedWeight_Type = Gauge32
_CucsQosclassEthClassifiedWeight_Object = MibTableColumn
cucsQosclassEthClassifiedWeight = _CucsQosclassEthClassifiedWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 4, 1, 12),
    _CucsQosclassEthClassifiedWeight_Type()
)
cucsQosclassEthClassifiedWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassEthClassifiedWeight.setStatus("current")
_CucsQosclassFcTable_Object = MibTable
cucsQosclassFcTable = _CucsQosclassFcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5)
)
if mibBuilder.loadTexts:
    cucsQosclassFcTable.setStatus("current")
_CucsQosclassFcEntry_Object = MibTableRow
cucsQosclassFcEntry = _CucsQosclassFcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5, 1)
)
cucsQosclassFcEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-QOSCLASS-MIB", "cucsQosclassFcInstanceId"),
)
if mibBuilder.loadTexts:
    cucsQosclassFcEntry.setStatus("current")
_CucsQosclassFcInstanceId_Type = CucsManagedObjectId
_CucsQosclassFcInstanceId_Object = MibTableColumn
cucsQosclassFcInstanceId = _CucsQosclassFcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5, 1, 1),
    _CucsQosclassFcInstanceId_Type()
)
cucsQosclassFcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsQosclassFcInstanceId.setStatus("current")
_CucsQosclassFcDn_Type = CucsManagedObjectDn
_CucsQosclassFcDn_Object = MibTableColumn
cucsQosclassFcDn = _CucsQosclassFcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5, 1, 2),
    _CucsQosclassFcDn_Type()
)
cucsQosclassFcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassFcDn.setStatus("current")
_CucsQosclassFcRn_Type = SnmpAdminString
_CucsQosclassFcRn_Object = MibTableColumn
cucsQosclassFcRn = _CucsQosclassFcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5, 1, 3),
    _CucsQosclassFcRn_Type()
)
cucsQosclassFcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassFcRn.setStatus("current")
_CucsQosclassFcAdminState_Type = CucsQosclassFcAdminState
_CucsQosclassFcAdminState_Object = MibTableColumn
cucsQosclassFcAdminState = _CucsQosclassFcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5, 1, 4),
    _CucsQosclassFcAdminState_Type()
)
cucsQosclassFcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassFcAdminState.setStatus("current")
_CucsQosclassFcBwPercent_Type = Gauge32
_CucsQosclassFcBwPercent_Object = MibTableColumn
cucsQosclassFcBwPercent = _CucsQosclassFcBwPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5, 1, 5),
    _CucsQosclassFcBwPercent_Type()
)
cucsQosclassFcBwPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassFcBwPercent.setStatus("current")
_CucsQosclassFcCos_Type = Gauge32
_CucsQosclassFcCos_Object = MibTableColumn
cucsQosclassFcCos = _CucsQosclassFcCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5, 1, 6),
    _CucsQosclassFcCos_Type()
)
cucsQosclassFcCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassFcCos.setStatus("current")
_CucsQosclassFcDrop_Type = CucsQosclassFcDrop
_CucsQosclassFcDrop_Object = MibTableColumn
cucsQosclassFcDrop = _CucsQosclassFcDrop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5, 1, 7),
    _CucsQosclassFcDrop_Type()
)
cucsQosclassFcDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassFcDrop.setStatus("current")
_CucsQosclassFcMtu_Type = SnmpAdminString
_CucsQosclassFcMtu_Object = MibTableColumn
cucsQosclassFcMtu = _CucsQosclassFcMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5, 1, 8),
    _CucsQosclassFcMtu_Type()
)
cucsQosclassFcMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassFcMtu.setStatus("current")
_CucsQosclassFcName_Type = SnmpAdminString
_CucsQosclassFcName_Object = MibTableColumn
cucsQosclassFcName = _CucsQosclassFcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5, 1, 9),
    _CucsQosclassFcName_Type()
)
cucsQosclassFcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassFcName.setStatus("current")
_CucsQosclassFcPriority_Type = CucsQosclassFcPriority
_CucsQosclassFcPriority_Object = MibTableColumn
cucsQosclassFcPriority = _CucsQosclassFcPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5, 1, 10),
    _CucsQosclassFcPriority_Type()
)
cucsQosclassFcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassFcPriority.setStatus("current")
_CucsQosclassFcWeight_Type = Gauge32
_CucsQosclassFcWeight_Object = MibTableColumn
cucsQosclassFcWeight = _CucsQosclassFcWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 5, 1, 11),
    _CucsQosclassFcWeight_Type()
)
cucsQosclassFcWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassFcWeight.setStatus("current")
_CucsQosclassDefinitionFsmTable_Object = MibTable
cucsQosclassDefinitionFsmTable = _CucsQosclassDefinitionFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6)
)
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmTable.setStatus("current")
_CucsQosclassDefinitionFsmEntry_Object = MibTableRow
cucsQosclassDefinitionFsmEntry = _CucsQosclassDefinitionFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6, 1)
)
cucsQosclassDefinitionFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-QOSCLASS-MIB", "cucsQosclassDefinitionFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmEntry.setStatus("current")
_CucsQosclassDefinitionFsmInstanceId_Type = CucsManagedObjectId
_CucsQosclassDefinitionFsmInstanceId_Object = MibTableColumn
cucsQosclassDefinitionFsmInstanceId = _CucsQosclassDefinitionFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6, 1, 1),
    _CucsQosclassDefinitionFsmInstanceId_Type()
)
cucsQosclassDefinitionFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmInstanceId.setStatus("current")
_CucsQosclassDefinitionFsmDn_Type = CucsManagedObjectDn
_CucsQosclassDefinitionFsmDn_Object = MibTableColumn
cucsQosclassDefinitionFsmDn = _CucsQosclassDefinitionFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6, 1, 2),
    _CucsQosclassDefinitionFsmDn_Type()
)
cucsQosclassDefinitionFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmDn.setStatus("current")
_CucsQosclassDefinitionFsmRn_Type = SnmpAdminString
_CucsQosclassDefinitionFsmRn_Object = MibTableColumn
cucsQosclassDefinitionFsmRn = _CucsQosclassDefinitionFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6, 1, 3),
    _CucsQosclassDefinitionFsmRn_Type()
)
cucsQosclassDefinitionFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmRn.setStatus("current")
_CucsQosclassDefinitionFsmCompletionTime_Type = DateAndTime
_CucsQosclassDefinitionFsmCompletionTime_Object = MibTableColumn
cucsQosclassDefinitionFsmCompletionTime = _CucsQosclassDefinitionFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6, 1, 4),
    _CucsQosclassDefinitionFsmCompletionTime_Type()
)
cucsQosclassDefinitionFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmCompletionTime.setStatus("current")
_CucsQosclassDefinitionFsmCurrentFsm_Type = CucsQosclassDefinitionFsmCurrentFsm
_CucsQosclassDefinitionFsmCurrentFsm_Object = MibTableColumn
cucsQosclassDefinitionFsmCurrentFsm = _CucsQosclassDefinitionFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6, 1, 5),
    _CucsQosclassDefinitionFsmCurrentFsm_Type()
)
cucsQosclassDefinitionFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmCurrentFsm.setStatus("current")
_CucsQosclassDefinitionFsmDescrData_Type = SnmpAdminString
_CucsQosclassDefinitionFsmDescrData_Object = MibTableColumn
cucsQosclassDefinitionFsmDescrData = _CucsQosclassDefinitionFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6, 1, 6),
    _CucsQosclassDefinitionFsmDescrData_Type()
)
cucsQosclassDefinitionFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmDescrData.setStatus("current")
_CucsQosclassDefinitionFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsQosclassDefinitionFsmFsmStatus_Object = MibTableColumn
cucsQosclassDefinitionFsmFsmStatus = _CucsQosclassDefinitionFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6, 1, 7),
    _CucsQosclassDefinitionFsmFsmStatus_Type()
)
cucsQosclassDefinitionFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmFsmStatus.setStatus("current")
_CucsQosclassDefinitionFsmProgress_Type = Gauge32
_CucsQosclassDefinitionFsmProgress_Object = MibTableColumn
cucsQosclassDefinitionFsmProgress = _CucsQosclassDefinitionFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6, 1, 8),
    _CucsQosclassDefinitionFsmProgress_Type()
)
cucsQosclassDefinitionFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmProgress.setStatus("current")
_CucsQosclassDefinitionFsmRmtErrCode_Type = Gauge32
_CucsQosclassDefinitionFsmRmtErrCode_Object = MibTableColumn
cucsQosclassDefinitionFsmRmtErrCode = _CucsQosclassDefinitionFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6, 1, 9),
    _CucsQosclassDefinitionFsmRmtErrCode_Type()
)
cucsQosclassDefinitionFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmRmtErrCode.setStatus("current")
_CucsQosclassDefinitionFsmRmtErrDescr_Type = SnmpAdminString
_CucsQosclassDefinitionFsmRmtErrDescr_Object = MibTableColumn
cucsQosclassDefinitionFsmRmtErrDescr = _CucsQosclassDefinitionFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6, 1, 10),
    _CucsQosclassDefinitionFsmRmtErrDescr_Type()
)
cucsQosclassDefinitionFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmRmtErrDescr.setStatus("current")
_CucsQosclassDefinitionFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsQosclassDefinitionFsmRmtRslt_Object = MibTableColumn
cucsQosclassDefinitionFsmRmtRslt = _CucsQosclassDefinitionFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 6, 1, 11),
    _CucsQosclassDefinitionFsmRmtRslt_Type()
)
cucsQosclassDefinitionFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmRmtRslt.setStatus("current")
_CucsQosclassDefinitionFsmStageTable_Object = MibTable
cucsQosclassDefinitionFsmStageTable = _CucsQosclassDefinitionFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 7)
)
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStageTable.setStatus("current")
_CucsQosclassDefinitionFsmStageEntry_Object = MibTableRow
cucsQosclassDefinitionFsmStageEntry = _CucsQosclassDefinitionFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 7, 1)
)
cucsQosclassDefinitionFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-QOSCLASS-MIB", "cucsQosclassDefinitionFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStageEntry.setStatus("current")
_CucsQosclassDefinitionFsmStageInstanceId_Type = CucsManagedObjectId
_CucsQosclassDefinitionFsmStageInstanceId_Object = MibTableColumn
cucsQosclassDefinitionFsmStageInstanceId = _CucsQosclassDefinitionFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 7, 1, 1),
    _CucsQosclassDefinitionFsmStageInstanceId_Type()
)
cucsQosclassDefinitionFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStageInstanceId.setStatus("current")
_CucsQosclassDefinitionFsmStageDn_Type = CucsManagedObjectDn
_CucsQosclassDefinitionFsmStageDn_Object = MibTableColumn
cucsQosclassDefinitionFsmStageDn = _CucsQosclassDefinitionFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 7, 1, 2),
    _CucsQosclassDefinitionFsmStageDn_Type()
)
cucsQosclassDefinitionFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStageDn.setStatus("current")
_CucsQosclassDefinitionFsmStageRn_Type = SnmpAdminString
_CucsQosclassDefinitionFsmStageRn_Object = MibTableColumn
cucsQosclassDefinitionFsmStageRn = _CucsQosclassDefinitionFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 7, 1, 3),
    _CucsQosclassDefinitionFsmStageRn_Type()
)
cucsQosclassDefinitionFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStageRn.setStatus("current")
_CucsQosclassDefinitionFsmStageDescrData_Type = SnmpAdminString
_CucsQosclassDefinitionFsmStageDescrData_Object = MibTableColumn
cucsQosclassDefinitionFsmStageDescrData = _CucsQosclassDefinitionFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 7, 1, 4),
    _CucsQosclassDefinitionFsmStageDescrData_Type()
)
cucsQosclassDefinitionFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStageDescrData.setStatus("current")
_CucsQosclassDefinitionFsmStageLastUpdateTime_Type = DateAndTime
_CucsQosclassDefinitionFsmStageLastUpdateTime_Object = MibTableColumn
cucsQosclassDefinitionFsmStageLastUpdateTime = _CucsQosclassDefinitionFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 7, 1, 5),
    _CucsQosclassDefinitionFsmStageLastUpdateTime_Type()
)
cucsQosclassDefinitionFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStageLastUpdateTime.setStatus("current")
_CucsQosclassDefinitionFsmStageName_Type = CucsQosclassDefinitionFsmStageName
_CucsQosclassDefinitionFsmStageName_Object = MibTableColumn
cucsQosclassDefinitionFsmStageName = _CucsQosclassDefinitionFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 7, 1, 6),
    _CucsQosclassDefinitionFsmStageName_Type()
)
cucsQosclassDefinitionFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStageName.setStatus("current")
_CucsQosclassDefinitionFsmStageOrder_Type = Gauge32
_CucsQosclassDefinitionFsmStageOrder_Object = MibTableColumn
cucsQosclassDefinitionFsmStageOrder = _CucsQosclassDefinitionFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 7, 1, 7),
    _CucsQosclassDefinitionFsmStageOrder_Type()
)
cucsQosclassDefinitionFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStageOrder.setStatus("current")
_CucsQosclassDefinitionFsmStageRetry_Type = Gauge32
_CucsQosclassDefinitionFsmStageRetry_Object = MibTableColumn
cucsQosclassDefinitionFsmStageRetry = _CucsQosclassDefinitionFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 7, 1, 8),
    _CucsQosclassDefinitionFsmStageRetry_Type()
)
cucsQosclassDefinitionFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStageRetry.setStatus("current")
_CucsQosclassDefinitionFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsQosclassDefinitionFsmStageStageStatus_Object = MibTableColumn
cucsQosclassDefinitionFsmStageStageStatus = _CucsQosclassDefinitionFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 42, 7, 1, 9),
    _CucsQosclassDefinitionFsmStageStageStatus_Type()
)
cucsQosclassDefinitionFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsQosclassDefinitionFsmStageStageStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-QOSCLASS-MIB",
    **{"cucsQosclassObjects": cucsQosclassObjects,
       "cucsQosclassDefinitionTable": cucsQosclassDefinitionTable,
       "cucsQosclassDefinitionEntry": cucsQosclassDefinitionEntry,
       "cucsQosclassDefinitionInstanceId": cucsQosclassDefinitionInstanceId,
       "cucsQosclassDefinitionDn": cucsQosclassDefinitionDn,
       "cucsQosclassDefinitionRn": cucsQosclassDefinitionRn,
       "cucsQosclassDefinitionDescr": cucsQosclassDefinitionDescr,
       "cucsQosclassDefinitionFsmDescr": cucsQosclassDefinitionFsmDescr,
       "cucsQosclassDefinitionFsmPrev": cucsQosclassDefinitionFsmPrev,
       "cucsQosclassDefinitionFsmProgr": cucsQosclassDefinitionFsmProgr,
       "cucsQosclassDefinitionFsmRmtInvErrCode": cucsQosclassDefinitionFsmRmtInvErrCode,
       "cucsQosclassDefinitionFsmRmtInvErrDescr": cucsQosclassDefinitionFsmRmtInvErrDescr,
       "cucsQosclassDefinitionFsmRmtInvRslt": cucsQosclassDefinitionFsmRmtInvRslt,
       "cucsQosclassDefinitionFsmStageDescr": cucsQosclassDefinitionFsmStageDescr,
       "cucsQosclassDefinitionFsmStamp": cucsQosclassDefinitionFsmStamp,
       "cucsQosclassDefinitionFsmStatus": cucsQosclassDefinitionFsmStatus,
       "cucsQosclassDefinitionFsmTry": cucsQosclassDefinitionFsmTry,
       "cucsQosclassDefinitionIntId": cucsQosclassDefinitionIntId,
       "cucsQosclassDefinitionName": cucsQosclassDefinitionName,
       "cucsQosclassDefinitionPolicyLevel": cucsQosclassDefinitionPolicyLevel,
       "cucsQosclassDefinitionPolicyOwner": cucsQosclassDefinitionPolicyOwner,
       "cucsQosclassDefinitionMmuPercent": cucsQosclassDefinitionMmuPercent,
       "cucsQosclassDefinitionNumBreakoutPort": cucsQosclassDefinitionNumBreakoutPort,
       "cucsQosclassDefinitionFsmTaskTable": cucsQosclassDefinitionFsmTaskTable,
       "cucsQosclassDefinitionFsmTaskEntry": cucsQosclassDefinitionFsmTaskEntry,
       "cucsQosclassDefinitionFsmTaskInstanceId": cucsQosclassDefinitionFsmTaskInstanceId,
       "cucsQosclassDefinitionFsmTaskDn": cucsQosclassDefinitionFsmTaskDn,
       "cucsQosclassDefinitionFsmTaskRn": cucsQosclassDefinitionFsmTaskRn,
       "cucsQosclassDefinitionFsmTaskCompletion": cucsQosclassDefinitionFsmTaskCompletion,
       "cucsQosclassDefinitionFsmTaskFlags": cucsQosclassDefinitionFsmTaskFlags,
       "cucsQosclassDefinitionFsmTaskItem": cucsQosclassDefinitionFsmTaskItem,
       "cucsQosclassDefinitionFsmTaskSeqId": cucsQosclassDefinitionFsmTaskSeqId,
       "cucsQosclassEthBETable": cucsQosclassEthBETable,
       "cucsQosclassEthBEEntry": cucsQosclassEthBEEntry,
       "cucsQosclassEthBEInstanceId": cucsQosclassEthBEInstanceId,
       "cucsQosclassEthBEDn": cucsQosclassEthBEDn,
       "cucsQosclassEthBERn": cucsQosclassEthBERn,
       "cucsQosclassEthBEAdminState": cucsQosclassEthBEAdminState,
       "cucsQosclassEthBEBwPercent": cucsQosclassEthBEBwPercent,
       "cucsQosclassEthBECos": cucsQosclassEthBECos,
       "cucsQosclassEthBEDrop": cucsQosclassEthBEDrop,
       "cucsQosclassEthBEMtu": cucsQosclassEthBEMtu,
       "cucsQosclassEthBEMulticastOptimize": cucsQosclassEthBEMulticastOptimize,
       "cucsQosclassEthBEName": cucsQosclassEthBEName,
       "cucsQosclassEthBEPriority": cucsQosclassEthBEPriority,
       "cucsQosclassEthBEWeight": cucsQosclassEthBEWeight,
       "cucsQosclassEthClassifiedTable": cucsQosclassEthClassifiedTable,
       "cucsQosclassEthClassifiedEntry": cucsQosclassEthClassifiedEntry,
       "cucsQosclassEthClassifiedInstanceId": cucsQosclassEthClassifiedInstanceId,
       "cucsQosclassEthClassifiedDn": cucsQosclassEthClassifiedDn,
       "cucsQosclassEthClassifiedRn": cucsQosclassEthClassifiedRn,
       "cucsQosclassEthClassifiedAdminState": cucsQosclassEthClassifiedAdminState,
       "cucsQosclassEthClassifiedBwPercent": cucsQosclassEthClassifiedBwPercent,
       "cucsQosclassEthClassifiedCos": cucsQosclassEthClassifiedCos,
       "cucsQosclassEthClassifiedDrop": cucsQosclassEthClassifiedDrop,
       "cucsQosclassEthClassifiedMtu": cucsQosclassEthClassifiedMtu,
       "cucsQosclassEthClassifiedMulticastOptimize": cucsQosclassEthClassifiedMulticastOptimize,
       "cucsQosclassEthClassifiedName": cucsQosclassEthClassifiedName,
       "cucsQosclassEthClassifiedPriority": cucsQosclassEthClassifiedPriority,
       "cucsQosclassEthClassifiedWeight": cucsQosclassEthClassifiedWeight,
       "cucsQosclassFcTable": cucsQosclassFcTable,
       "cucsQosclassFcEntry": cucsQosclassFcEntry,
       "cucsQosclassFcInstanceId": cucsQosclassFcInstanceId,
       "cucsQosclassFcDn": cucsQosclassFcDn,
       "cucsQosclassFcRn": cucsQosclassFcRn,
       "cucsQosclassFcAdminState": cucsQosclassFcAdminState,
       "cucsQosclassFcBwPercent": cucsQosclassFcBwPercent,
       "cucsQosclassFcCos": cucsQosclassFcCos,
       "cucsQosclassFcDrop": cucsQosclassFcDrop,
       "cucsQosclassFcMtu": cucsQosclassFcMtu,
       "cucsQosclassFcName": cucsQosclassFcName,
       "cucsQosclassFcPriority": cucsQosclassFcPriority,
       "cucsQosclassFcWeight": cucsQosclassFcWeight,
       "cucsQosclassDefinitionFsmTable": cucsQosclassDefinitionFsmTable,
       "cucsQosclassDefinitionFsmEntry": cucsQosclassDefinitionFsmEntry,
       "cucsQosclassDefinitionFsmInstanceId": cucsQosclassDefinitionFsmInstanceId,
       "cucsQosclassDefinitionFsmDn": cucsQosclassDefinitionFsmDn,
       "cucsQosclassDefinitionFsmRn": cucsQosclassDefinitionFsmRn,
       "cucsQosclassDefinitionFsmCompletionTime": cucsQosclassDefinitionFsmCompletionTime,
       "cucsQosclassDefinitionFsmCurrentFsm": cucsQosclassDefinitionFsmCurrentFsm,
       "cucsQosclassDefinitionFsmDescrData": cucsQosclassDefinitionFsmDescrData,
       "cucsQosclassDefinitionFsmFsmStatus": cucsQosclassDefinitionFsmFsmStatus,
       "cucsQosclassDefinitionFsmProgress": cucsQosclassDefinitionFsmProgress,
       "cucsQosclassDefinitionFsmRmtErrCode": cucsQosclassDefinitionFsmRmtErrCode,
       "cucsQosclassDefinitionFsmRmtErrDescr": cucsQosclassDefinitionFsmRmtErrDescr,
       "cucsQosclassDefinitionFsmRmtRslt": cucsQosclassDefinitionFsmRmtRslt,
       "cucsQosclassDefinitionFsmStageTable": cucsQosclassDefinitionFsmStageTable,
       "cucsQosclassDefinitionFsmStageEntry": cucsQosclassDefinitionFsmStageEntry,
       "cucsQosclassDefinitionFsmStageInstanceId": cucsQosclassDefinitionFsmStageInstanceId,
       "cucsQosclassDefinitionFsmStageDn": cucsQosclassDefinitionFsmStageDn,
       "cucsQosclassDefinitionFsmStageRn": cucsQosclassDefinitionFsmStageRn,
       "cucsQosclassDefinitionFsmStageDescrData": cucsQosclassDefinitionFsmStageDescrData,
       "cucsQosclassDefinitionFsmStageLastUpdateTime": cucsQosclassDefinitionFsmStageLastUpdateTime,
       "cucsQosclassDefinitionFsmStageName": cucsQosclassDefinitionFsmStageName,
       "cucsQosclassDefinitionFsmStageOrder": cucsQosclassDefinitionFsmStageOrder,
       "cucsQosclassDefinitionFsmStageRetry": cucsQosclassDefinitionFsmStageRetry,
       "cucsQosclassDefinitionFsmStageStageStatus": cucsQosclassDefinitionFsmStageStageStatus}
)
