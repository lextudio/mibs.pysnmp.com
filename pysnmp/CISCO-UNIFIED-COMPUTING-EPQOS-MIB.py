# SNMP MIB module (CISCO-UNIFIED-COMPUTING-EPQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-EPQOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:20 2024
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
 CucsEpqosDefinitionDelTaskFsmCurrentFsm,
 CucsEpqosDefinitionDelTaskFsmStageName,
 CucsEpqosDefinitionDelTaskFsmTaskItem,
 CucsEpqosDefinitionFsmCurrentFsm,
 CucsEpqosDefinitionFsmStageName,
 CucsEpqosDefinitionFsmTaskItem,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsPolicyPolicyOwner,
 CucsQosHostControl,
 CucsQosPriority) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsEpqosDefinitionDelTaskFsmCurrentFsm",
    "CucsEpqosDefinitionDelTaskFsmStageName",
    "CucsEpqosDefinitionDelTaskFsmTaskItem",
    "CucsEpqosDefinitionFsmCurrentFsm",
    "CucsEpqosDefinitionFsmStageName",
    "CucsEpqosDefinitionFsmTaskItem",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsPolicyPolicyOwner",
    "CucsQosHostControl",
    "CucsQosPriority")

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

cucsEpqosObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsEpqosDefinitionTable_Object = MibTable
cucsEpqosDefinitionTable = _CucsEpqosDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1)
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionTable.setStatus("current")
_CucsEpqosDefinitionEntry_Object = MibTableRow
cucsEpqosDefinitionEntry = _CucsEpqosDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1)
)
cucsEpqosDefinitionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EPQOS-MIB", "cucsEpqosDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionEntry.setStatus("current")
_CucsEpqosDefinitionInstanceId_Type = CucsManagedObjectId
_CucsEpqosDefinitionInstanceId_Object = MibTableColumn
cucsEpqosDefinitionInstanceId = _CucsEpqosDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 1),
    _CucsEpqosDefinitionInstanceId_Type()
)
cucsEpqosDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionInstanceId.setStatus("current")
_CucsEpqosDefinitionDn_Type = CucsManagedObjectDn
_CucsEpqosDefinitionDn_Object = MibTableColumn
cucsEpqosDefinitionDn = _CucsEpqosDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 2),
    _CucsEpqosDefinitionDn_Type()
)
cucsEpqosDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDn.setStatus("current")
_CucsEpqosDefinitionRn_Type = SnmpAdminString
_CucsEpqosDefinitionRn_Object = MibTableColumn
cucsEpqosDefinitionRn = _CucsEpqosDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 3),
    _CucsEpqosDefinitionRn_Type()
)
cucsEpqosDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionRn.setStatus("current")
_CucsEpqosDefinitionDescr_Type = SnmpAdminString
_CucsEpqosDefinitionDescr_Object = MibTableColumn
cucsEpqosDefinitionDescr = _CucsEpqosDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 4),
    _CucsEpqosDefinitionDescr_Type()
)
cucsEpqosDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDescr.setStatus("current")
_CucsEpqosDefinitionFsmDescr_Type = SnmpAdminString
_CucsEpqosDefinitionFsmDescr_Object = MibTableColumn
cucsEpqosDefinitionFsmDescr = _CucsEpqosDefinitionFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 5),
    _CucsEpqosDefinitionFsmDescr_Type()
)
cucsEpqosDefinitionFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmDescr.setStatus("current")
_CucsEpqosDefinitionFsmPrev_Type = SnmpAdminString
_CucsEpqosDefinitionFsmPrev_Object = MibTableColumn
cucsEpqosDefinitionFsmPrev = _CucsEpqosDefinitionFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 6),
    _CucsEpqosDefinitionFsmPrev_Type()
)
cucsEpqosDefinitionFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmPrev.setStatus("current")
_CucsEpqosDefinitionFsmProgr_Type = Gauge32
_CucsEpqosDefinitionFsmProgr_Object = MibTableColumn
cucsEpqosDefinitionFsmProgr = _CucsEpqosDefinitionFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 7),
    _CucsEpqosDefinitionFsmProgr_Type()
)
cucsEpqosDefinitionFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmProgr.setStatus("current")
_CucsEpqosDefinitionFsmRmtInvErrCode_Type = Gauge32
_CucsEpqosDefinitionFsmRmtInvErrCode_Object = MibTableColumn
cucsEpqosDefinitionFsmRmtInvErrCode = _CucsEpqosDefinitionFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 8),
    _CucsEpqosDefinitionFsmRmtInvErrCode_Type()
)
cucsEpqosDefinitionFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmRmtInvErrCode.setStatus("current")
_CucsEpqosDefinitionFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsEpqosDefinitionFsmRmtInvErrDescr_Object = MibTableColumn
cucsEpqosDefinitionFsmRmtInvErrDescr = _CucsEpqosDefinitionFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 9),
    _CucsEpqosDefinitionFsmRmtInvErrDescr_Type()
)
cucsEpqosDefinitionFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmRmtInvErrDescr.setStatus("current")
_CucsEpqosDefinitionFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsEpqosDefinitionFsmRmtInvRslt_Object = MibTableColumn
cucsEpqosDefinitionFsmRmtInvRslt = _CucsEpqosDefinitionFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 10),
    _CucsEpqosDefinitionFsmRmtInvRslt_Type()
)
cucsEpqosDefinitionFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmRmtInvRslt.setStatus("current")
_CucsEpqosDefinitionFsmStageDescr_Type = SnmpAdminString
_CucsEpqosDefinitionFsmStageDescr_Object = MibTableColumn
cucsEpqosDefinitionFsmStageDescr = _CucsEpqosDefinitionFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 11),
    _CucsEpqosDefinitionFsmStageDescr_Type()
)
cucsEpqosDefinitionFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStageDescr.setStatus("current")
_CucsEpqosDefinitionFsmStamp_Type = DateAndTime
_CucsEpqosDefinitionFsmStamp_Object = MibTableColumn
cucsEpqosDefinitionFsmStamp = _CucsEpqosDefinitionFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 12),
    _CucsEpqosDefinitionFsmStamp_Type()
)
cucsEpqosDefinitionFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStamp.setStatus("current")
_CucsEpqosDefinitionFsmStatus_Type = SnmpAdminString
_CucsEpqosDefinitionFsmStatus_Object = MibTableColumn
cucsEpqosDefinitionFsmStatus = _CucsEpqosDefinitionFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 13),
    _CucsEpqosDefinitionFsmStatus_Type()
)
cucsEpqosDefinitionFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStatus.setStatus("current")
_CucsEpqosDefinitionFsmTry_Type = Gauge32
_CucsEpqosDefinitionFsmTry_Object = MibTableColumn
cucsEpqosDefinitionFsmTry = _CucsEpqosDefinitionFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 14),
    _CucsEpqosDefinitionFsmTry_Type()
)
cucsEpqosDefinitionFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmTry.setStatus("current")
_CucsEpqosDefinitionIntId_Type = SnmpAdminString
_CucsEpqosDefinitionIntId_Object = MibTableColumn
cucsEpqosDefinitionIntId = _CucsEpqosDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 15),
    _CucsEpqosDefinitionIntId_Type()
)
cucsEpqosDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionIntId.setStatus("current")
_CucsEpqosDefinitionName_Type = SnmpAdminString
_CucsEpqosDefinitionName_Object = MibTableColumn
cucsEpqosDefinitionName = _CucsEpqosDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 16),
    _CucsEpqosDefinitionName_Type()
)
cucsEpqosDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionName.setStatus("current")
_CucsEpqosDefinitionPolicyLevel_Type = Gauge32
_CucsEpqosDefinitionPolicyLevel_Object = MibTableColumn
cucsEpqosDefinitionPolicyLevel = _CucsEpqosDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 17),
    _CucsEpqosDefinitionPolicyLevel_Type()
)
cucsEpqosDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionPolicyLevel.setStatus("current")
_CucsEpqosDefinitionPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsEpqosDefinitionPolicyOwner_Object = MibTableColumn
cucsEpqosDefinitionPolicyOwner = _CucsEpqosDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 1, 1, 18),
    _CucsEpqosDefinitionPolicyOwner_Type()
)
cucsEpqosDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionPolicyOwner.setStatus("current")
_CucsEpqosDefinitionDelTaskTable_Object = MibTable
cucsEpqosDefinitionDelTaskTable = _CucsEpqosDefinitionDelTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2)
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskTable.setStatus("current")
_CucsEpqosDefinitionDelTaskEntry_Object = MibTableRow
cucsEpqosDefinitionDelTaskEntry = _CucsEpqosDefinitionDelTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1)
)
cucsEpqosDefinitionDelTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EPQOS-MIB", "cucsEpqosDefinitionDelTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskEntry.setStatus("current")
_CucsEpqosDefinitionDelTaskInstanceId_Type = CucsManagedObjectId
_CucsEpqosDefinitionDelTaskInstanceId_Object = MibTableColumn
cucsEpqosDefinitionDelTaskInstanceId = _CucsEpqosDefinitionDelTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 1),
    _CucsEpqosDefinitionDelTaskInstanceId_Type()
)
cucsEpqosDefinitionDelTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskInstanceId.setStatus("current")
_CucsEpqosDefinitionDelTaskDn_Type = CucsManagedObjectDn
_CucsEpqosDefinitionDelTaskDn_Object = MibTableColumn
cucsEpqosDefinitionDelTaskDn = _CucsEpqosDefinitionDelTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 2),
    _CucsEpqosDefinitionDelTaskDn_Type()
)
cucsEpqosDefinitionDelTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskDn.setStatus("current")
_CucsEpqosDefinitionDelTaskRn_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskRn_Object = MibTableColumn
cucsEpqosDefinitionDelTaskRn = _CucsEpqosDefinitionDelTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 3),
    _CucsEpqosDefinitionDelTaskRn_Type()
)
cucsEpqosDefinitionDelTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskRn.setStatus("current")
_CucsEpqosDefinitionDelTaskDefIntId_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskDefIntId_Object = MibTableColumn
cucsEpqosDefinitionDelTaskDefIntId = _CucsEpqosDefinitionDelTaskDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 4),
    _CucsEpqosDefinitionDelTaskDefIntId_Type()
)
cucsEpqosDefinitionDelTaskDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskDefIntId.setStatus("current")
_CucsEpqosDefinitionDelTaskDescr_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskDescr_Object = MibTableColumn
cucsEpqosDefinitionDelTaskDescr = _CucsEpqosDefinitionDelTaskDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 5),
    _CucsEpqosDefinitionDelTaskDescr_Type()
)
cucsEpqosDefinitionDelTaskDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskDescr.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmDescr_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmDescr_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmDescr = _CucsEpqosDefinitionDelTaskFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 6),
    _CucsEpqosDefinitionDelTaskFsmDescr_Type()
)
cucsEpqosDefinitionDelTaskFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmDescr.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmPrev_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmPrev_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmPrev = _CucsEpqosDefinitionDelTaskFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 7),
    _CucsEpqosDefinitionDelTaskFsmPrev_Type()
)
cucsEpqosDefinitionDelTaskFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmPrev.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmProgr_Type = Gauge32
_CucsEpqosDefinitionDelTaskFsmProgr_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmProgr = _CucsEpqosDefinitionDelTaskFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 8),
    _CucsEpqosDefinitionDelTaskFsmProgr_Type()
)
cucsEpqosDefinitionDelTaskFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmProgr.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmRmtInvErrCode_Type = Gauge32
_CucsEpqosDefinitionDelTaskFsmRmtInvErrCode_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmRmtInvErrCode = _CucsEpqosDefinitionDelTaskFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 9),
    _CucsEpqosDefinitionDelTaskFsmRmtInvErrCode_Type()
)
cucsEpqosDefinitionDelTaskFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmRmtInvErrCode.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmRmtInvErrDescr_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmRmtInvErrDescr = _CucsEpqosDefinitionDelTaskFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 10),
    _CucsEpqosDefinitionDelTaskFsmRmtInvErrDescr_Type()
)
cucsEpqosDefinitionDelTaskFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmRmtInvErrDescr.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsEpqosDefinitionDelTaskFsmRmtInvRslt_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmRmtInvRslt = _CucsEpqosDefinitionDelTaskFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 11),
    _CucsEpqosDefinitionDelTaskFsmRmtInvRslt_Type()
)
cucsEpqosDefinitionDelTaskFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmRmtInvRslt.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStageDescr_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmStageDescr_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageDescr = _CucsEpqosDefinitionDelTaskFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 12),
    _CucsEpqosDefinitionDelTaskFsmStageDescr_Type()
)
cucsEpqosDefinitionDelTaskFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStageDescr.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStamp_Type = DateAndTime
_CucsEpqosDefinitionDelTaskFsmStamp_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmStamp = _CucsEpqosDefinitionDelTaskFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 13),
    _CucsEpqosDefinitionDelTaskFsmStamp_Type()
)
cucsEpqosDefinitionDelTaskFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStamp.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStatus_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmStatus_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmStatus = _CucsEpqosDefinitionDelTaskFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 14),
    _CucsEpqosDefinitionDelTaskFsmStatus_Type()
)
cucsEpqosDefinitionDelTaskFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStatus.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmTry_Type = Gauge32
_CucsEpqosDefinitionDelTaskFsmTry_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmTry = _CucsEpqosDefinitionDelTaskFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 15),
    _CucsEpqosDefinitionDelTaskFsmTry_Type()
)
cucsEpqosDefinitionDelTaskFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmTry.setStatus("current")
_CucsEpqosDefinitionDelTaskIntId_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskIntId_Object = MibTableColumn
cucsEpqosDefinitionDelTaskIntId = _CucsEpqosDefinitionDelTaskIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 16),
    _CucsEpqosDefinitionDelTaskIntId_Type()
)
cucsEpqosDefinitionDelTaskIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskIntId.setStatus("current")
_CucsEpqosDefinitionDelTaskName_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskName_Object = MibTableColumn
cucsEpqosDefinitionDelTaskName = _CucsEpqosDefinitionDelTaskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 17),
    _CucsEpqosDefinitionDelTaskName_Type()
)
cucsEpqosDefinitionDelTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskName.setStatus("current")
_CucsEpqosDefinitionDelTaskDefDn_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskDefDn_Object = MibTableColumn
cucsEpqosDefinitionDelTaskDefDn = _CucsEpqosDefinitionDelTaskDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 18),
    _CucsEpqosDefinitionDelTaskDefDn_Type()
)
cucsEpqosDefinitionDelTaskDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskDefDn.setStatus("current")
_CucsEpqosDefinitionDelTaskPolicyLevel_Type = Gauge32
_CucsEpqosDefinitionDelTaskPolicyLevel_Object = MibTableColumn
cucsEpqosDefinitionDelTaskPolicyLevel = _CucsEpqosDefinitionDelTaskPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 19),
    _CucsEpqosDefinitionDelTaskPolicyLevel_Type()
)
cucsEpqosDefinitionDelTaskPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskPolicyLevel.setStatus("current")
_CucsEpqosDefinitionDelTaskPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsEpqosDefinitionDelTaskPolicyOwner_Object = MibTableColumn
cucsEpqosDefinitionDelTaskPolicyOwner = _CucsEpqosDefinitionDelTaskPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 2, 1, 20),
    _CucsEpqosDefinitionDelTaskPolicyOwner_Type()
)
cucsEpqosDefinitionDelTaskPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskPolicyOwner.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmTaskTable_Object = MibTable
cucsEpqosDefinitionDelTaskFsmTaskTable = _CucsEpqosDefinitionDelTaskFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 3)
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmTaskTable.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmTaskEntry_Object = MibTableRow
cucsEpqosDefinitionDelTaskFsmTaskEntry = _CucsEpqosDefinitionDelTaskFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 3, 1)
)
cucsEpqosDefinitionDelTaskFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EPQOS-MIB", "cucsEpqosDefinitionDelTaskFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmTaskEntry.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsEpqosDefinitionDelTaskFsmTaskInstanceId_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskInstanceId = _CucsEpqosDefinitionDelTaskFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 3, 1, 1),
    _CucsEpqosDefinitionDelTaskFsmTaskInstanceId_Type()
)
cucsEpqosDefinitionDelTaskFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmTaskInstanceId.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmTaskDn_Type = CucsManagedObjectDn
_CucsEpqosDefinitionDelTaskFsmTaskDn_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskDn = _CucsEpqosDefinitionDelTaskFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 3, 1, 2),
    _CucsEpqosDefinitionDelTaskFsmTaskDn_Type()
)
cucsEpqosDefinitionDelTaskFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmTaskDn.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmTaskRn_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmTaskRn_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskRn = _CucsEpqosDefinitionDelTaskFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 3, 1, 3),
    _CucsEpqosDefinitionDelTaskFsmTaskRn_Type()
)
cucsEpqosDefinitionDelTaskFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmTaskRn.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmTaskCompletion_Type = CucsFsmCompletion
_CucsEpqosDefinitionDelTaskFsmTaskCompletion_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskCompletion = _CucsEpqosDefinitionDelTaskFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 3, 1, 4),
    _CucsEpqosDefinitionDelTaskFsmTaskCompletion_Type()
)
cucsEpqosDefinitionDelTaskFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmTaskCompletion.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmTaskFlags_Type = CucsFsmFlags
_CucsEpqosDefinitionDelTaskFsmTaskFlags_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskFlags = _CucsEpqosDefinitionDelTaskFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 3, 1, 5),
    _CucsEpqosDefinitionDelTaskFsmTaskFlags_Type()
)
cucsEpqosDefinitionDelTaskFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmTaskFlags.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmTaskItem_Type = CucsEpqosDefinitionDelTaskFsmTaskItem
_CucsEpqosDefinitionDelTaskFsmTaskItem_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskItem = _CucsEpqosDefinitionDelTaskFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 3, 1, 6),
    _CucsEpqosDefinitionDelTaskFsmTaskItem_Type()
)
cucsEpqosDefinitionDelTaskFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmTaskItem.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmTaskSeqId_Type = Gauge32
_CucsEpqosDefinitionDelTaskFsmTaskSeqId_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmTaskSeqId = _CucsEpqosDefinitionDelTaskFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 3, 1, 7),
    _CucsEpqosDefinitionDelTaskFsmTaskSeqId_Type()
)
cucsEpqosDefinitionDelTaskFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmTaskSeqId.setStatus("current")
_CucsEpqosDefinitionFsmTaskTable_Object = MibTable
cucsEpqosDefinitionFsmTaskTable = _CucsEpqosDefinitionFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 4)
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmTaskTable.setStatus("current")
_CucsEpqosDefinitionFsmTaskEntry_Object = MibTableRow
cucsEpqosDefinitionFsmTaskEntry = _CucsEpqosDefinitionFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 4, 1)
)
cucsEpqosDefinitionFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EPQOS-MIB", "cucsEpqosDefinitionFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmTaskEntry.setStatus("current")
_CucsEpqosDefinitionFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsEpqosDefinitionFsmTaskInstanceId_Object = MibTableColumn
cucsEpqosDefinitionFsmTaskInstanceId = _CucsEpqosDefinitionFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 4, 1, 1),
    _CucsEpqosDefinitionFsmTaskInstanceId_Type()
)
cucsEpqosDefinitionFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmTaskInstanceId.setStatus("current")
_CucsEpqosDefinitionFsmTaskDn_Type = CucsManagedObjectDn
_CucsEpqosDefinitionFsmTaskDn_Object = MibTableColumn
cucsEpqosDefinitionFsmTaskDn = _CucsEpqosDefinitionFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 4, 1, 2),
    _CucsEpqosDefinitionFsmTaskDn_Type()
)
cucsEpqosDefinitionFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmTaskDn.setStatus("current")
_CucsEpqosDefinitionFsmTaskRn_Type = SnmpAdminString
_CucsEpqosDefinitionFsmTaskRn_Object = MibTableColumn
cucsEpqosDefinitionFsmTaskRn = _CucsEpqosDefinitionFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 4, 1, 3),
    _CucsEpqosDefinitionFsmTaskRn_Type()
)
cucsEpqosDefinitionFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmTaskRn.setStatus("current")
_CucsEpqosDefinitionFsmTaskCompletion_Type = CucsFsmCompletion
_CucsEpqosDefinitionFsmTaskCompletion_Object = MibTableColumn
cucsEpqosDefinitionFsmTaskCompletion = _CucsEpqosDefinitionFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 4, 1, 4),
    _CucsEpqosDefinitionFsmTaskCompletion_Type()
)
cucsEpqosDefinitionFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmTaskCompletion.setStatus("current")
_CucsEpqosDefinitionFsmTaskFlags_Type = CucsFsmFlags
_CucsEpqosDefinitionFsmTaskFlags_Object = MibTableColumn
cucsEpqosDefinitionFsmTaskFlags = _CucsEpqosDefinitionFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 4, 1, 5),
    _CucsEpqosDefinitionFsmTaskFlags_Type()
)
cucsEpqosDefinitionFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmTaskFlags.setStatus("current")
_CucsEpqosDefinitionFsmTaskItem_Type = CucsEpqosDefinitionFsmTaskItem
_CucsEpqosDefinitionFsmTaskItem_Object = MibTableColumn
cucsEpqosDefinitionFsmTaskItem = _CucsEpqosDefinitionFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 4, 1, 6),
    _CucsEpqosDefinitionFsmTaskItem_Type()
)
cucsEpqosDefinitionFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmTaskItem.setStatus("current")
_CucsEpqosDefinitionFsmTaskSeqId_Type = Gauge32
_CucsEpqosDefinitionFsmTaskSeqId_Object = MibTableColumn
cucsEpqosDefinitionFsmTaskSeqId = _CucsEpqosDefinitionFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 4, 1, 7),
    _CucsEpqosDefinitionFsmTaskSeqId_Type()
)
cucsEpqosDefinitionFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmTaskSeqId.setStatus("current")
_CucsEpqosEgressTable_Object = MibTable
cucsEpqosEgressTable = _CucsEpqosEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 5)
)
if mibBuilder.loadTexts:
    cucsEpqosEgressTable.setStatus("current")
_CucsEpqosEgressEntry_Object = MibTableRow
cucsEpqosEgressEntry = _CucsEpqosEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 5, 1)
)
cucsEpqosEgressEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EPQOS-MIB", "cucsEpqosEgressInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEpqosEgressEntry.setStatus("current")
_CucsEpqosEgressInstanceId_Type = CucsManagedObjectId
_CucsEpqosEgressInstanceId_Object = MibTableColumn
cucsEpqosEgressInstanceId = _CucsEpqosEgressInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 5, 1, 1),
    _CucsEpqosEgressInstanceId_Type()
)
cucsEpqosEgressInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEpqosEgressInstanceId.setStatus("current")
_CucsEpqosEgressDn_Type = CucsManagedObjectDn
_CucsEpqosEgressDn_Object = MibTableColumn
cucsEpqosEgressDn = _CucsEpqosEgressDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 5, 1, 2),
    _CucsEpqosEgressDn_Type()
)
cucsEpqosEgressDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosEgressDn.setStatus("current")
_CucsEpqosEgressRn_Type = SnmpAdminString
_CucsEpqosEgressRn_Object = MibTableColumn
cucsEpqosEgressRn = _CucsEpqosEgressRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 5, 1, 3),
    _CucsEpqosEgressRn_Type()
)
cucsEpqosEgressRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosEgressRn.setStatus("current")
_CucsEpqosEgressBurst_Type = Gauge32
_CucsEpqosEgressBurst_Object = MibTableColumn
cucsEpqosEgressBurst = _CucsEpqosEgressBurst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 5, 1, 4),
    _CucsEpqosEgressBurst_Type()
)
cucsEpqosEgressBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosEgressBurst.setStatus("current")
_CucsEpqosEgressHostControl_Type = CucsQosHostControl
_CucsEpqosEgressHostControl_Object = MibTableColumn
cucsEpqosEgressHostControl = _CucsEpqosEgressHostControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 5, 1, 5),
    _CucsEpqosEgressHostControl_Type()
)
cucsEpqosEgressHostControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosEgressHostControl.setStatus("current")
_CucsEpqosEgressName_Type = SnmpAdminString
_CucsEpqosEgressName_Object = MibTableColumn
cucsEpqosEgressName = _CucsEpqosEgressName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 5, 1, 6),
    _CucsEpqosEgressName_Type()
)
cucsEpqosEgressName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosEgressName.setStatus("current")
_CucsEpqosEgressPrio_Type = CucsQosPriority
_CucsEpqosEgressPrio_Object = MibTableColumn
cucsEpqosEgressPrio = _CucsEpqosEgressPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 5, 1, 7),
    _CucsEpqosEgressPrio_Type()
)
cucsEpqosEgressPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosEgressPrio.setStatus("current")
_CucsEpqosEgressRate_Type = Gauge32
_CucsEpqosEgressRate_Object = MibTableColumn
cucsEpqosEgressRate = _CucsEpqosEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 5, 1, 8),
    _CucsEpqosEgressRate_Type()
)
cucsEpqosEgressRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosEgressRate.setStatus("current")
_CucsEpqosEgressOperPrio_Type = CucsQosPriority
_CucsEpqosEgressOperPrio_Object = MibTableColumn
cucsEpqosEgressOperPrio = _CucsEpqosEgressOperPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 5, 1, 9),
    _CucsEpqosEgressOperPrio_Type()
)
cucsEpqosEgressOperPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosEgressOperPrio.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmTable_Object = MibTable
cucsEpqosDefinitionDelTaskFsmTable = _CucsEpqosDefinitionDelTaskFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6)
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmTable.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmEntry_Object = MibTableRow
cucsEpqosDefinitionDelTaskFsmEntry = _CucsEpqosDefinitionDelTaskFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6, 1)
)
cucsEpqosDefinitionDelTaskFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EPQOS-MIB", "cucsEpqosDefinitionDelTaskFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmEntry.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmInstanceId_Type = CucsManagedObjectId
_CucsEpqosDefinitionDelTaskFsmInstanceId_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmInstanceId = _CucsEpqosDefinitionDelTaskFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6, 1, 1),
    _CucsEpqosDefinitionDelTaskFsmInstanceId_Type()
)
cucsEpqosDefinitionDelTaskFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmInstanceId.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmDn_Type = CucsManagedObjectDn
_CucsEpqosDefinitionDelTaskFsmDn_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmDn = _CucsEpqosDefinitionDelTaskFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6, 1, 2),
    _CucsEpqosDefinitionDelTaskFsmDn_Type()
)
cucsEpqosDefinitionDelTaskFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmDn.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmRn_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmRn_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmRn = _CucsEpqosDefinitionDelTaskFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6, 1, 3),
    _CucsEpqosDefinitionDelTaskFsmRn_Type()
)
cucsEpqosDefinitionDelTaskFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmRn.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmCompletionTime_Type = DateAndTime
_CucsEpqosDefinitionDelTaskFsmCompletionTime_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmCompletionTime = _CucsEpqosDefinitionDelTaskFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6, 1, 4),
    _CucsEpqosDefinitionDelTaskFsmCompletionTime_Type()
)
cucsEpqosDefinitionDelTaskFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmCompletionTime.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmCurrentFsm_Type = CucsEpqosDefinitionDelTaskFsmCurrentFsm
_CucsEpqosDefinitionDelTaskFsmCurrentFsm_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmCurrentFsm = _CucsEpqosDefinitionDelTaskFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6, 1, 5),
    _CucsEpqosDefinitionDelTaskFsmCurrentFsm_Type()
)
cucsEpqosDefinitionDelTaskFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmCurrentFsm.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmDescrData_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmDescrData_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmDescrData = _CucsEpqosDefinitionDelTaskFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6, 1, 6),
    _CucsEpqosDefinitionDelTaskFsmDescrData_Type()
)
cucsEpqosDefinitionDelTaskFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmDescrData.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsEpqosDefinitionDelTaskFsmFsmStatus_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmFsmStatus = _CucsEpqosDefinitionDelTaskFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6, 1, 7),
    _CucsEpqosDefinitionDelTaskFsmFsmStatus_Type()
)
cucsEpqosDefinitionDelTaskFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmFsmStatus.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmProgress_Type = Gauge32
_CucsEpqosDefinitionDelTaskFsmProgress_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmProgress = _CucsEpqosDefinitionDelTaskFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6, 1, 8),
    _CucsEpqosDefinitionDelTaskFsmProgress_Type()
)
cucsEpqosDefinitionDelTaskFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmProgress.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmRmtErrCode_Type = Gauge32
_CucsEpqosDefinitionDelTaskFsmRmtErrCode_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmRmtErrCode = _CucsEpqosDefinitionDelTaskFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6, 1, 9),
    _CucsEpqosDefinitionDelTaskFsmRmtErrCode_Type()
)
cucsEpqosDefinitionDelTaskFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmRmtErrCode.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmRmtErrDescr_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmRmtErrDescr_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmRmtErrDescr = _CucsEpqosDefinitionDelTaskFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6, 1, 10),
    _CucsEpqosDefinitionDelTaskFsmRmtErrDescr_Type()
)
cucsEpqosDefinitionDelTaskFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmRmtErrDescr.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsEpqosDefinitionDelTaskFsmRmtRslt_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmRmtRslt = _CucsEpqosDefinitionDelTaskFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 6, 1, 11),
    _CucsEpqosDefinitionDelTaskFsmRmtRslt_Type()
)
cucsEpqosDefinitionDelTaskFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmRmtRslt.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStageTable_Object = MibTable
cucsEpqosDefinitionDelTaskFsmStageTable = _CucsEpqosDefinitionDelTaskFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 7)
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStageTable.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStageEntry_Object = MibTableRow
cucsEpqosDefinitionDelTaskFsmStageEntry = _CucsEpqosDefinitionDelTaskFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 7, 1)
)
cucsEpqosDefinitionDelTaskFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EPQOS-MIB", "cucsEpqosDefinitionDelTaskFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStageEntry.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStageInstanceId_Type = CucsManagedObjectId
_CucsEpqosDefinitionDelTaskFsmStageInstanceId_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageInstanceId = _CucsEpqosDefinitionDelTaskFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 7, 1, 1),
    _CucsEpqosDefinitionDelTaskFsmStageInstanceId_Type()
)
cucsEpqosDefinitionDelTaskFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStageInstanceId.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStageDn_Type = CucsManagedObjectDn
_CucsEpqosDefinitionDelTaskFsmStageDn_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageDn = _CucsEpqosDefinitionDelTaskFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 7, 1, 2),
    _CucsEpqosDefinitionDelTaskFsmStageDn_Type()
)
cucsEpqosDefinitionDelTaskFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStageDn.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStageRn_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmStageRn_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageRn = _CucsEpqosDefinitionDelTaskFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 7, 1, 3),
    _CucsEpqosDefinitionDelTaskFsmStageRn_Type()
)
cucsEpqosDefinitionDelTaskFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStageRn.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStageDescrData_Type = SnmpAdminString
_CucsEpqosDefinitionDelTaskFsmStageDescrData_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageDescrData = _CucsEpqosDefinitionDelTaskFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 7, 1, 4),
    _CucsEpqosDefinitionDelTaskFsmStageDescrData_Type()
)
cucsEpqosDefinitionDelTaskFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStageDescrData.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStageLastUpdateTime_Type = DateAndTime
_CucsEpqosDefinitionDelTaskFsmStageLastUpdateTime_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageLastUpdateTime = _CucsEpqosDefinitionDelTaskFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 7, 1, 5),
    _CucsEpqosDefinitionDelTaskFsmStageLastUpdateTime_Type()
)
cucsEpqosDefinitionDelTaskFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStageLastUpdateTime.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStageName_Type = CucsEpqosDefinitionDelTaskFsmStageName
_CucsEpqosDefinitionDelTaskFsmStageName_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageName = _CucsEpqosDefinitionDelTaskFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 7, 1, 6),
    _CucsEpqosDefinitionDelTaskFsmStageName_Type()
)
cucsEpqosDefinitionDelTaskFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStageName.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStageOrder_Type = Gauge32
_CucsEpqosDefinitionDelTaskFsmStageOrder_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageOrder = _CucsEpqosDefinitionDelTaskFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 7, 1, 7),
    _CucsEpqosDefinitionDelTaskFsmStageOrder_Type()
)
cucsEpqosDefinitionDelTaskFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStageOrder.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStageRetry_Type = Gauge32
_CucsEpqosDefinitionDelTaskFsmStageRetry_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageRetry = _CucsEpqosDefinitionDelTaskFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 7, 1, 8),
    _CucsEpqosDefinitionDelTaskFsmStageRetry_Type()
)
cucsEpqosDefinitionDelTaskFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStageRetry.setStatus("current")
_CucsEpqosDefinitionDelTaskFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsEpqosDefinitionDelTaskFsmStageStageStatus_Object = MibTableColumn
cucsEpqosDefinitionDelTaskFsmStageStageStatus = _CucsEpqosDefinitionDelTaskFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 7, 1, 9),
    _CucsEpqosDefinitionDelTaskFsmStageStageStatus_Type()
)
cucsEpqosDefinitionDelTaskFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionDelTaskFsmStageStageStatus.setStatus("current")
_CucsEpqosDefinitionFsmTable_Object = MibTable
cucsEpqosDefinitionFsmTable = _CucsEpqosDefinitionFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8)
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmTable.setStatus("current")
_CucsEpqosDefinitionFsmEntry_Object = MibTableRow
cucsEpqosDefinitionFsmEntry = _CucsEpqosDefinitionFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8, 1)
)
cucsEpqosDefinitionFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EPQOS-MIB", "cucsEpqosDefinitionFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmEntry.setStatus("current")
_CucsEpqosDefinitionFsmInstanceId_Type = CucsManagedObjectId
_CucsEpqosDefinitionFsmInstanceId_Object = MibTableColumn
cucsEpqosDefinitionFsmInstanceId = _CucsEpqosDefinitionFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8, 1, 1),
    _CucsEpqosDefinitionFsmInstanceId_Type()
)
cucsEpqosDefinitionFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmInstanceId.setStatus("current")
_CucsEpqosDefinitionFsmDn_Type = CucsManagedObjectDn
_CucsEpqosDefinitionFsmDn_Object = MibTableColumn
cucsEpqosDefinitionFsmDn = _CucsEpqosDefinitionFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8, 1, 2),
    _CucsEpqosDefinitionFsmDn_Type()
)
cucsEpqosDefinitionFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmDn.setStatus("current")
_CucsEpqosDefinitionFsmRn_Type = SnmpAdminString
_CucsEpqosDefinitionFsmRn_Object = MibTableColumn
cucsEpqosDefinitionFsmRn = _CucsEpqosDefinitionFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8, 1, 3),
    _CucsEpqosDefinitionFsmRn_Type()
)
cucsEpqosDefinitionFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmRn.setStatus("current")
_CucsEpqosDefinitionFsmCompletionTime_Type = DateAndTime
_CucsEpqosDefinitionFsmCompletionTime_Object = MibTableColumn
cucsEpqosDefinitionFsmCompletionTime = _CucsEpqosDefinitionFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8, 1, 4),
    _CucsEpqosDefinitionFsmCompletionTime_Type()
)
cucsEpqosDefinitionFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmCompletionTime.setStatus("current")
_CucsEpqosDefinitionFsmCurrentFsm_Type = CucsEpqosDefinitionFsmCurrentFsm
_CucsEpqosDefinitionFsmCurrentFsm_Object = MibTableColumn
cucsEpqosDefinitionFsmCurrentFsm = _CucsEpqosDefinitionFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8, 1, 5),
    _CucsEpqosDefinitionFsmCurrentFsm_Type()
)
cucsEpqosDefinitionFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmCurrentFsm.setStatus("current")
_CucsEpqosDefinitionFsmDescrData_Type = SnmpAdminString
_CucsEpqosDefinitionFsmDescrData_Object = MibTableColumn
cucsEpqosDefinitionFsmDescrData = _CucsEpqosDefinitionFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8, 1, 6),
    _CucsEpqosDefinitionFsmDescrData_Type()
)
cucsEpqosDefinitionFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmDescrData.setStatus("current")
_CucsEpqosDefinitionFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsEpqosDefinitionFsmFsmStatus_Object = MibTableColumn
cucsEpqosDefinitionFsmFsmStatus = _CucsEpqosDefinitionFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8, 1, 7),
    _CucsEpqosDefinitionFsmFsmStatus_Type()
)
cucsEpqosDefinitionFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmFsmStatus.setStatus("current")
_CucsEpqosDefinitionFsmProgress_Type = Gauge32
_CucsEpqosDefinitionFsmProgress_Object = MibTableColumn
cucsEpqosDefinitionFsmProgress = _CucsEpqosDefinitionFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8, 1, 8),
    _CucsEpqosDefinitionFsmProgress_Type()
)
cucsEpqosDefinitionFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmProgress.setStatus("current")
_CucsEpqosDefinitionFsmRmtErrCode_Type = Gauge32
_CucsEpqosDefinitionFsmRmtErrCode_Object = MibTableColumn
cucsEpqosDefinitionFsmRmtErrCode = _CucsEpqosDefinitionFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8, 1, 9),
    _CucsEpqosDefinitionFsmRmtErrCode_Type()
)
cucsEpqosDefinitionFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmRmtErrCode.setStatus("current")
_CucsEpqosDefinitionFsmRmtErrDescr_Type = SnmpAdminString
_CucsEpqosDefinitionFsmRmtErrDescr_Object = MibTableColumn
cucsEpqosDefinitionFsmRmtErrDescr = _CucsEpqosDefinitionFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8, 1, 10),
    _CucsEpqosDefinitionFsmRmtErrDescr_Type()
)
cucsEpqosDefinitionFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmRmtErrDescr.setStatus("current")
_CucsEpqosDefinitionFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsEpqosDefinitionFsmRmtRslt_Object = MibTableColumn
cucsEpqosDefinitionFsmRmtRslt = _CucsEpqosDefinitionFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 8, 1, 11),
    _CucsEpqosDefinitionFsmRmtRslt_Type()
)
cucsEpqosDefinitionFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmRmtRslt.setStatus("current")
_CucsEpqosDefinitionFsmStageTable_Object = MibTable
cucsEpqosDefinitionFsmStageTable = _CucsEpqosDefinitionFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 9)
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStageTable.setStatus("current")
_CucsEpqosDefinitionFsmStageEntry_Object = MibTableRow
cucsEpqosDefinitionFsmStageEntry = _CucsEpqosDefinitionFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 9, 1)
)
cucsEpqosDefinitionFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EPQOS-MIB", "cucsEpqosDefinitionFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStageEntry.setStatus("current")
_CucsEpqosDefinitionFsmStageInstanceId_Type = CucsManagedObjectId
_CucsEpqosDefinitionFsmStageInstanceId_Object = MibTableColumn
cucsEpqosDefinitionFsmStageInstanceId = _CucsEpqosDefinitionFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 9, 1, 1),
    _CucsEpqosDefinitionFsmStageInstanceId_Type()
)
cucsEpqosDefinitionFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStageInstanceId.setStatus("current")
_CucsEpqosDefinitionFsmStageDn_Type = CucsManagedObjectDn
_CucsEpqosDefinitionFsmStageDn_Object = MibTableColumn
cucsEpqosDefinitionFsmStageDn = _CucsEpqosDefinitionFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 9, 1, 2),
    _CucsEpqosDefinitionFsmStageDn_Type()
)
cucsEpqosDefinitionFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStageDn.setStatus("current")
_CucsEpqosDefinitionFsmStageRn_Type = SnmpAdminString
_CucsEpqosDefinitionFsmStageRn_Object = MibTableColumn
cucsEpqosDefinitionFsmStageRn = _CucsEpqosDefinitionFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 9, 1, 3),
    _CucsEpqosDefinitionFsmStageRn_Type()
)
cucsEpqosDefinitionFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStageRn.setStatus("current")
_CucsEpqosDefinitionFsmStageDescrData_Type = SnmpAdminString
_CucsEpqosDefinitionFsmStageDescrData_Object = MibTableColumn
cucsEpqosDefinitionFsmStageDescrData = _CucsEpqosDefinitionFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 9, 1, 4),
    _CucsEpqosDefinitionFsmStageDescrData_Type()
)
cucsEpqosDefinitionFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStageDescrData.setStatus("current")
_CucsEpqosDefinitionFsmStageLastUpdateTime_Type = DateAndTime
_CucsEpqosDefinitionFsmStageLastUpdateTime_Object = MibTableColumn
cucsEpqosDefinitionFsmStageLastUpdateTime = _CucsEpqosDefinitionFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 9, 1, 5),
    _CucsEpqosDefinitionFsmStageLastUpdateTime_Type()
)
cucsEpqosDefinitionFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStageLastUpdateTime.setStatus("current")
_CucsEpqosDefinitionFsmStageName_Type = CucsEpqosDefinitionFsmStageName
_CucsEpqosDefinitionFsmStageName_Object = MibTableColumn
cucsEpqosDefinitionFsmStageName = _CucsEpqosDefinitionFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 9, 1, 6),
    _CucsEpqosDefinitionFsmStageName_Type()
)
cucsEpqosDefinitionFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStageName.setStatus("current")
_CucsEpqosDefinitionFsmStageOrder_Type = Gauge32
_CucsEpqosDefinitionFsmStageOrder_Object = MibTableColumn
cucsEpqosDefinitionFsmStageOrder = _CucsEpqosDefinitionFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 9, 1, 7),
    _CucsEpqosDefinitionFsmStageOrder_Type()
)
cucsEpqosDefinitionFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStageOrder.setStatus("current")
_CucsEpqosDefinitionFsmStageRetry_Type = Gauge32
_CucsEpqosDefinitionFsmStageRetry_Object = MibTableColumn
cucsEpqosDefinitionFsmStageRetry = _CucsEpqosDefinitionFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 9, 1, 8),
    _CucsEpqosDefinitionFsmStageRetry_Type()
)
cucsEpqosDefinitionFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStageRetry.setStatus("current")
_CucsEpqosDefinitionFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsEpqosDefinitionFsmStageStageStatus_Object = MibTableColumn
cucsEpqosDefinitionFsmStageStageStatus = _CucsEpqosDefinitionFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 14, 9, 1, 9),
    _CucsEpqosDefinitionFsmStageStageStatus_Type()
)
cucsEpqosDefinitionFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsEpqosDefinitionFsmStageStageStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-EPQOS-MIB",
    **{"cucsEpqosObjects": cucsEpqosObjects,
       "cucsEpqosDefinitionTable": cucsEpqosDefinitionTable,
       "cucsEpqosDefinitionEntry": cucsEpqosDefinitionEntry,
       "cucsEpqosDefinitionInstanceId": cucsEpqosDefinitionInstanceId,
       "cucsEpqosDefinitionDn": cucsEpqosDefinitionDn,
       "cucsEpqosDefinitionRn": cucsEpqosDefinitionRn,
       "cucsEpqosDefinitionDescr": cucsEpqosDefinitionDescr,
       "cucsEpqosDefinitionFsmDescr": cucsEpqosDefinitionFsmDescr,
       "cucsEpqosDefinitionFsmPrev": cucsEpqosDefinitionFsmPrev,
       "cucsEpqosDefinitionFsmProgr": cucsEpqosDefinitionFsmProgr,
       "cucsEpqosDefinitionFsmRmtInvErrCode": cucsEpqosDefinitionFsmRmtInvErrCode,
       "cucsEpqosDefinitionFsmRmtInvErrDescr": cucsEpqosDefinitionFsmRmtInvErrDescr,
       "cucsEpqosDefinitionFsmRmtInvRslt": cucsEpqosDefinitionFsmRmtInvRslt,
       "cucsEpqosDefinitionFsmStageDescr": cucsEpqosDefinitionFsmStageDescr,
       "cucsEpqosDefinitionFsmStamp": cucsEpqosDefinitionFsmStamp,
       "cucsEpqosDefinitionFsmStatus": cucsEpqosDefinitionFsmStatus,
       "cucsEpqosDefinitionFsmTry": cucsEpqosDefinitionFsmTry,
       "cucsEpqosDefinitionIntId": cucsEpqosDefinitionIntId,
       "cucsEpqosDefinitionName": cucsEpqosDefinitionName,
       "cucsEpqosDefinitionPolicyLevel": cucsEpqosDefinitionPolicyLevel,
       "cucsEpqosDefinitionPolicyOwner": cucsEpqosDefinitionPolicyOwner,
       "cucsEpqosDefinitionDelTaskTable": cucsEpqosDefinitionDelTaskTable,
       "cucsEpqosDefinitionDelTaskEntry": cucsEpqosDefinitionDelTaskEntry,
       "cucsEpqosDefinitionDelTaskInstanceId": cucsEpqosDefinitionDelTaskInstanceId,
       "cucsEpqosDefinitionDelTaskDn": cucsEpqosDefinitionDelTaskDn,
       "cucsEpqosDefinitionDelTaskRn": cucsEpqosDefinitionDelTaskRn,
       "cucsEpqosDefinitionDelTaskDefIntId": cucsEpqosDefinitionDelTaskDefIntId,
       "cucsEpqosDefinitionDelTaskDescr": cucsEpqosDefinitionDelTaskDescr,
       "cucsEpqosDefinitionDelTaskFsmDescr": cucsEpqosDefinitionDelTaskFsmDescr,
       "cucsEpqosDefinitionDelTaskFsmPrev": cucsEpqosDefinitionDelTaskFsmPrev,
       "cucsEpqosDefinitionDelTaskFsmProgr": cucsEpqosDefinitionDelTaskFsmProgr,
       "cucsEpqosDefinitionDelTaskFsmRmtInvErrCode": cucsEpqosDefinitionDelTaskFsmRmtInvErrCode,
       "cucsEpqosDefinitionDelTaskFsmRmtInvErrDescr": cucsEpqosDefinitionDelTaskFsmRmtInvErrDescr,
       "cucsEpqosDefinitionDelTaskFsmRmtInvRslt": cucsEpqosDefinitionDelTaskFsmRmtInvRslt,
       "cucsEpqosDefinitionDelTaskFsmStageDescr": cucsEpqosDefinitionDelTaskFsmStageDescr,
       "cucsEpqosDefinitionDelTaskFsmStamp": cucsEpqosDefinitionDelTaskFsmStamp,
       "cucsEpqosDefinitionDelTaskFsmStatus": cucsEpqosDefinitionDelTaskFsmStatus,
       "cucsEpqosDefinitionDelTaskFsmTry": cucsEpqosDefinitionDelTaskFsmTry,
       "cucsEpqosDefinitionDelTaskIntId": cucsEpqosDefinitionDelTaskIntId,
       "cucsEpqosDefinitionDelTaskName": cucsEpqosDefinitionDelTaskName,
       "cucsEpqosDefinitionDelTaskDefDn": cucsEpqosDefinitionDelTaskDefDn,
       "cucsEpqosDefinitionDelTaskPolicyLevel": cucsEpqosDefinitionDelTaskPolicyLevel,
       "cucsEpqosDefinitionDelTaskPolicyOwner": cucsEpqosDefinitionDelTaskPolicyOwner,
       "cucsEpqosDefinitionDelTaskFsmTaskTable": cucsEpqosDefinitionDelTaskFsmTaskTable,
       "cucsEpqosDefinitionDelTaskFsmTaskEntry": cucsEpqosDefinitionDelTaskFsmTaskEntry,
       "cucsEpqosDefinitionDelTaskFsmTaskInstanceId": cucsEpqosDefinitionDelTaskFsmTaskInstanceId,
       "cucsEpqosDefinitionDelTaskFsmTaskDn": cucsEpqosDefinitionDelTaskFsmTaskDn,
       "cucsEpqosDefinitionDelTaskFsmTaskRn": cucsEpqosDefinitionDelTaskFsmTaskRn,
       "cucsEpqosDefinitionDelTaskFsmTaskCompletion": cucsEpqosDefinitionDelTaskFsmTaskCompletion,
       "cucsEpqosDefinitionDelTaskFsmTaskFlags": cucsEpqosDefinitionDelTaskFsmTaskFlags,
       "cucsEpqosDefinitionDelTaskFsmTaskItem": cucsEpqosDefinitionDelTaskFsmTaskItem,
       "cucsEpqosDefinitionDelTaskFsmTaskSeqId": cucsEpqosDefinitionDelTaskFsmTaskSeqId,
       "cucsEpqosDefinitionFsmTaskTable": cucsEpqosDefinitionFsmTaskTable,
       "cucsEpqosDefinitionFsmTaskEntry": cucsEpqosDefinitionFsmTaskEntry,
       "cucsEpqosDefinitionFsmTaskInstanceId": cucsEpqosDefinitionFsmTaskInstanceId,
       "cucsEpqosDefinitionFsmTaskDn": cucsEpqosDefinitionFsmTaskDn,
       "cucsEpqosDefinitionFsmTaskRn": cucsEpqosDefinitionFsmTaskRn,
       "cucsEpqosDefinitionFsmTaskCompletion": cucsEpqosDefinitionFsmTaskCompletion,
       "cucsEpqosDefinitionFsmTaskFlags": cucsEpqosDefinitionFsmTaskFlags,
       "cucsEpqosDefinitionFsmTaskItem": cucsEpqosDefinitionFsmTaskItem,
       "cucsEpqosDefinitionFsmTaskSeqId": cucsEpqosDefinitionFsmTaskSeqId,
       "cucsEpqosEgressTable": cucsEpqosEgressTable,
       "cucsEpqosEgressEntry": cucsEpqosEgressEntry,
       "cucsEpqosEgressInstanceId": cucsEpqosEgressInstanceId,
       "cucsEpqosEgressDn": cucsEpqosEgressDn,
       "cucsEpqosEgressRn": cucsEpqosEgressRn,
       "cucsEpqosEgressBurst": cucsEpqosEgressBurst,
       "cucsEpqosEgressHostControl": cucsEpqosEgressHostControl,
       "cucsEpqosEgressName": cucsEpqosEgressName,
       "cucsEpqosEgressPrio": cucsEpqosEgressPrio,
       "cucsEpqosEgressRate": cucsEpqosEgressRate,
       "cucsEpqosEgressOperPrio": cucsEpqosEgressOperPrio,
       "cucsEpqosDefinitionDelTaskFsmTable": cucsEpqosDefinitionDelTaskFsmTable,
       "cucsEpqosDefinitionDelTaskFsmEntry": cucsEpqosDefinitionDelTaskFsmEntry,
       "cucsEpqosDefinitionDelTaskFsmInstanceId": cucsEpqosDefinitionDelTaskFsmInstanceId,
       "cucsEpqosDefinitionDelTaskFsmDn": cucsEpqosDefinitionDelTaskFsmDn,
       "cucsEpqosDefinitionDelTaskFsmRn": cucsEpqosDefinitionDelTaskFsmRn,
       "cucsEpqosDefinitionDelTaskFsmCompletionTime": cucsEpqosDefinitionDelTaskFsmCompletionTime,
       "cucsEpqosDefinitionDelTaskFsmCurrentFsm": cucsEpqosDefinitionDelTaskFsmCurrentFsm,
       "cucsEpqosDefinitionDelTaskFsmDescrData": cucsEpqosDefinitionDelTaskFsmDescrData,
       "cucsEpqosDefinitionDelTaskFsmFsmStatus": cucsEpqosDefinitionDelTaskFsmFsmStatus,
       "cucsEpqosDefinitionDelTaskFsmProgress": cucsEpqosDefinitionDelTaskFsmProgress,
       "cucsEpqosDefinitionDelTaskFsmRmtErrCode": cucsEpqosDefinitionDelTaskFsmRmtErrCode,
       "cucsEpqosDefinitionDelTaskFsmRmtErrDescr": cucsEpqosDefinitionDelTaskFsmRmtErrDescr,
       "cucsEpqosDefinitionDelTaskFsmRmtRslt": cucsEpqosDefinitionDelTaskFsmRmtRslt,
       "cucsEpqosDefinitionDelTaskFsmStageTable": cucsEpqosDefinitionDelTaskFsmStageTable,
       "cucsEpqosDefinitionDelTaskFsmStageEntry": cucsEpqosDefinitionDelTaskFsmStageEntry,
       "cucsEpqosDefinitionDelTaskFsmStageInstanceId": cucsEpqosDefinitionDelTaskFsmStageInstanceId,
       "cucsEpqosDefinitionDelTaskFsmStageDn": cucsEpqosDefinitionDelTaskFsmStageDn,
       "cucsEpqosDefinitionDelTaskFsmStageRn": cucsEpqosDefinitionDelTaskFsmStageRn,
       "cucsEpqosDefinitionDelTaskFsmStageDescrData": cucsEpqosDefinitionDelTaskFsmStageDescrData,
       "cucsEpqosDefinitionDelTaskFsmStageLastUpdateTime": cucsEpqosDefinitionDelTaskFsmStageLastUpdateTime,
       "cucsEpqosDefinitionDelTaskFsmStageName": cucsEpqosDefinitionDelTaskFsmStageName,
       "cucsEpqosDefinitionDelTaskFsmStageOrder": cucsEpqosDefinitionDelTaskFsmStageOrder,
       "cucsEpqosDefinitionDelTaskFsmStageRetry": cucsEpqosDefinitionDelTaskFsmStageRetry,
       "cucsEpqosDefinitionDelTaskFsmStageStageStatus": cucsEpqosDefinitionDelTaskFsmStageStageStatus,
       "cucsEpqosDefinitionFsmTable": cucsEpqosDefinitionFsmTable,
       "cucsEpqosDefinitionFsmEntry": cucsEpqosDefinitionFsmEntry,
       "cucsEpqosDefinitionFsmInstanceId": cucsEpqosDefinitionFsmInstanceId,
       "cucsEpqosDefinitionFsmDn": cucsEpqosDefinitionFsmDn,
       "cucsEpqosDefinitionFsmRn": cucsEpqosDefinitionFsmRn,
       "cucsEpqosDefinitionFsmCompletionTime": cucsEpqosDefinitionFsmCompletionTime,
       "cucsEpqosDefinitionFsmCurrentFsm": cucsEpqosDefinitionFsmCurrentFsm,
       "cucsEpqosDefinitionFsmDescrData": cucsEpqosDefinitionFsmDescrData,
       "cucsEpqosDefinitionFsmFsmStatus": cucsEpqosDefinitionFsmFsmStatus,
       "cucsEpqosDefinitionFsmProgress": cucsEpqosDefinitionFsmProgress,
       "cucsEpqosDefinitionFsmRmtErrCode": cucsEpqosDefinitionFsmRmtErrCode,
       "cucsEpqosDefinitionFsmRmtErrDescr": cucsEpqosDefinitionFsmRmtErrDescr,
       "cucsEpqosDefinitionFsmRmtRslt": cucsEpqosDefinitionFsmRmtRslt,
       "cucsEpqosDefinitionFsmStageTable": cucsEpqosDefinitionFsmStageTable,
       "cucsEpqosDefinitionFsmStageEntry": cucsEpqosDefinitionFsmStageEntry,
       "cucsEpqosDefinitionFsmStageInstanceId": cucsEpqosDefinitionFsmStageInstanceId,
       "cucsEpqosDefinitionFsmStageDn": cucsEpqosDefinitionFsmStageDn,
       "cucsEpqosDefinitionFsmStageRn": cucsEpqosDefinitionFsmStageRn,
       "cucsEpqosDefinitionFsmStageDescrData": cucsEpqosDefinitionFsmStageDescrData,
       "cucsEpqosDefinitionFsmStageLastUpdateTime": cucsEpqosDefinitionFsmStageLastUpdateTime,
       "cucsEpqosDefinitionFsmStageName": cucsEpqosDefinitionFsmStageName,
       "cucsEpqosDefinitionFsmStageOrder": cucsEpqosDefinitionFsmStageOrder,
       "cucsEpqosDefinitionFsmStageRetry": cucsEpqosDefinitionFsmStageRetry,
       "cucsEpqosDefinitionFsmStageStageStatus": cucsEpqosDefinitionFsmStageStageStatus}
)
