# SNMP MIB module (CISCO-UNIFIED-COMPUTING-SYSFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-SYSFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:24 2024
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
 CucsNetworkSwitchId,
 CucsSysfileMutationAction,
 CucsSysfileMutationFsmCurrentFsm,
 CucsSysfileMutationFsmStageName,
 CucsSysfileMutationFsmTaskItem) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsNetworkSwitchId",
    "CucsSysfileMutationAction",
    "CucsSysfileMutationFsmCurrentFsm",
    "CucsSysfileMutationFsmStageName",
    "CucsSysfileMutationFsmTaskItem")

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

cucsSysfileObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsSysfileMutationTable_Object = MibTable
cucsSysfileMutationTable = _CucsSysfileMutationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1)
)
if mibBuilder.loadTexts:
    cucsSysfileMutationTable.setStatus("current")
_CucsSysfileMutationEntry_Object = MibTableRow
cucsSysfileMutationEntry = _CucsSysfileMutationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1)
)
cucsSysfileMutationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSFILE-MIB", "cucsSysfileMutationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysfileMutationEntry.setStatus("current")
_CucsSysfileMutationInstanceId_Type = CucsManagedObjectId
_CucsSysfileMutationInstanceId_Object = MibTableColumn
cucsSysfileMutationInstanceId = _CucsSysfileMutationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 1),
    _CucsSysfileMutationInstanceId_Type()
)
cucsSysfileMutationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysfileMutationInstanceId.setStatus("current")
_CucsSysfileMutationDn_Type = CucsManagedObjectDn
_CucsSysfileMutationDn_Object = MibTableColumn
cucsSysfileMutationDn = _CucsSysfileMutationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 2),
    _CucsSysfileMutationDn_Type()
)
cucsSysfileMutationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationDn.setStatus("current")
_CucsSysfileMutationRn_Type = SnmpAdminString
_CucsSysfileMutationRn_Object = MibTableColumn
cucsSysfileMutationRn = _CucsSysfileMutationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 3),
    _CucsSysfileMutationRn_Type()
)
cucsSysfileMutationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationRn.setStatus("current")
_CucsSysfileMutationAction_Type = CucsSysfileMutationAction
_CucsSysfileMutationAction_Object = MibTableColumn
cucsSysfileMutationAction = _CucsSysfileMutationAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 4),
    _CucsSysfileMutationAction_Type()
)
cucsSysfileMutationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationAction.setStatus("current")
_CucsSysfileMutationDescr_Type = SnmpAdminString
_CucsSysfileMutationDescr_Object = MibTableColumn
cucsSysfileMutationDescr = _CucsSysfileMutationDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 5),
    _CucsSysfileMutationDescr_Type()
)
cucsSysfileMutationDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationDescr.setStatus("current")
_CucsSysfileMutationFsmDescr_Type = SnmpAdminString
_CucsSysfileMutationFsmDescr_Object = MibTableColumn
cucsSysfileMutationFsmDescr = _CucsSysfileMutationFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 6),
    _CucsSysfileMutationFsmDescr_Type()
)
cucsSysfileMutationFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmDescr.setStatus("current")
_CucsSysfileMutationFsmPrev_Type = SnmpAdminString
_CucsSysfileMutationFsmPrev_Object = MibTableColumn
cucsSysfileMutationFsmPrev = _CucsSysfileMutationFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 7),
    _CucsSysfileMutationFsmPrev_Type()
)
cucsSysfileMutationFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmPrev.setStatus("current")
_CucsSysfileMutationFsmProgr_Type = Gauge32
_CucsSysfileMutationFsmProgr_Object = MibTableColumn
cucsSysfileMutationFsmProgr = _CucsSysfileMutationFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 8),
    _CucsSysfileMutationFsmProgr_Type()
)
cucsSysfileMutationFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmProgr.setStatus("current")
_CucsSysfileMutationFsmRmtInvErrCode_Type = Gauge32
_CucsSysfileMutationFsmRmtInvErrCode_Object = MibTableColumn
cucsSysfileMutationFsmRmtInvErrCode = _CucsSysfileMutationFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 9),
    _CucsSysfileMutationFsmRmtInvErrCode_Type()
)
cucsSysfileMutationFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmRmtInvErrCode.setStatus("current")
_CucsSysfileMutationFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSysfileMutationFsmRmtInvErrDescr_Object = MibTableColumn
cucsSysfileMutationFsmRmtInvErrDescr = _CucsSysfileMutationFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 10),
    _CucsSysfileMutationFsmRmtInvErrDescr_Type()
)
cucsSysfileMutationFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmRmtInvErrDescr.setStatus("current")
_CucsSysfileMutationFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSysfileMutationFsmRmtInvRslt_Object = MibTableColumn
cucsSysfileMutationFsmRmtInvRslt = _CucsSysfileMutationFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 11),
    _CucsSysfileMutationFsmRmtInvRslt_Type()
)
cucsSysfileMutationFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmRmtInvRslt.setStatus("current")
_CucsSysfileMutationFsmStageDescr_Type = SnmpAdminString
_CucsSysfileMutationFsmStageDescr_Object = MibTableColumn
cucsSysfileMutationFsmStageDescr = _CucsSysfileMutationFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 12),
    _CucsSysfileMutationFsmStageDescr_Type()
)
cucsSysfileMutationFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStageDescr.setStatus("current")
_CucsSysfileMutationFsmStamp_Type = DateAndTime
_CucsSysfileMutationFsmStamp_Object = MibTableColumn
cucsSysfileMutationFsmStamp = _CucsSysfileMutationFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 13),
    _CucsSysfileMutationFsmStamp_Type()
)
cucsSysfileMutationFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStamp.setStatus("current")
_CucsSysfileMutationFsmStatus_Type = SnmpAdminString
_CucsSysfileMutationFsmStatus_Object = MibTableColumn
cucsSysfileMutationFsmStatus = _CucsSysfileMutationFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 14),
    _CucsSysfileMutationFsmStatus_Type()
)
cucsSysfileMutationFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStatus.setStatus("current")
_CucsSysfileMutationFsmTry_Type = Gauge32
_CucsSysfileMutationFsmTry_Object = MibTableColumn
cucsSysfileMutationFsmTry = _CucsSysfileMutationFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 1, 1, 15),
    _CucsSysfileMutationFsmTry_Type()
)
cucsSysfileMutationFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmTry.setStatus("current")
_CucsSysfileMutationFsmTaskTable_Object = MibTable
cucsSysfileMutationFsmTaskTable = _CucsSysfileMutationFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 2)
)
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmTaskTable.setStatus("current")
_CucsSysfileMutationFsmTaskEntry_Object = MibTableRow
cucsSysfileMutationFsmTaskEntry = _CucsSysfileMutationFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 2, 1)
)
cucsSysfileMutationFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSFILE-MIB", "cucsSysfileMutationFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmTaskEntry.setStatus("current")
_CucsSysfileMutationFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSysfileMutationFsmTaskInstanceId_Object = MibTableColumn
cucsSysfileMutationFsmTaskInstanceId = _CucsSysfileMutationFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 2, 1, 1),
    _CucsSysfileMutationFsmTaskInstanceId_Type()
)
cucsSysfileMutationFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmTaskInstanceId.setStatus("current")
_CucsSysfileMutationFsmTaskDn_Type = CucsManagedObjectDn
_CucsSysfileMutationFsmTaskDn_Object = MibTableColumn
cucsSysfileMutationFsmTaskDn = _CucsSysfileMutationFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 2, 1, 2),
    _CucsSysfileMutationFsmTaskDn_Type()
)
cucsSysfileMutationFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmTaskDn.setStatus("current")
_CucsSysfileMutationFsmTaskRn_Type = SnmpAdminString
_CucsSysfileMutationFsmTaskRn_Object = MibTableColumn
cucsSysfileMutationFsmTaskRn = _CucsSysfileMutationFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 2, 1, 3),
    _CucsSysfileMutationFsmTaskRn_Type()
)
cucsSysfileMutationFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmTaskRn.setStatus("current")
_CucsSysfileMutationFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSysfileMutationFsmTaskCompletion_Object = MibTableColumn
cucsSysfileMutationFsmTaskCompletion = _CucsSysfileMutationFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 2, 1, 4),
    _CucsSysfileMutationFsmTaskCompletion_Type()
)
cucsSysfileMutationFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmTaskCompletion.setStatus("current")
_CucsSysfileMutationFsmTaskFlags_Type = CucsFsmFlags
_CucsSysfileMutationFsmTaskFlags_Object = MibTableColumn
cucsSysfileMutationFsmTaskFlags = _CucsSysfileMutationFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 2, 1, 5),
    _CucsSysfileMutationFsmTaskFlags_Type()
)
cucsSysfileMutationFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmTaskFlags.setStatus("current")
_CucsSysfileMutationFsmTaskItem_Type = CucsSysfileMutationFsmTaskItem
_CucsSysfileMutationFsmTaskItem_Object = MibTableColumn
cucsSysfileMutationFsmTaskItem = _CucsSysfileMutationFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 2, 1, 6),
    _CucsSysfileMutationFsmTaskItem_Type()
)
cucsSysfileMutationFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmTaskItem.setStatus("current")
_CucsSysfileMutationFsmTaskSeqId_Type = Gauge32
_CucsSysfileMutationFsmTaskSeqId_Object = MibTableColumn
cucsSysfileMutationFsmTaskSeqId = _CucsSysfileMutationFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 2, 1, 7),
    _CucsSysfileMutationFsmTaskSeqId_Type()
)
cucsSysfileMutationFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmTaskSeqId.setStatus("current")
_CucsSysfileDigestTable_Object = MibTable
cucsSysfileDigestTable = _CucsSysfileDigestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3)
)
if mibBuilder.loadTexts:
    cucsSysfileDigestTable.setStatus("current")
_CucsSysfileDigestEntry_Object = MibTableRow
cucsSysfileDigestEntry = _CucsSysfileDigestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3, 1)
)
cucsSysfileDigestEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSFILE-MIB", "cucsSysfileDigestInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysfileDigestEntry.setStatus("current")
_CucsSysfileDigestInstanceId_Type = CucsManagedObjectId
_CucsSysfileDigestInstanceId_Object = MibTableColumn
cucsSysfileDigestInstanceId = _CucsSysfileDigestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3, 1, 1),
    _CucsSysfileDigestInstanceId_Type()
)
cucsSysfileDigestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysfileDigestInstanceId.setStatus("current")
_CucsSysfileDigestDn_Type = CucsManagedObjectDn
_CucsSysfileDigestDn_Object = MibTableColumn
cucsSysfileDigestDn = _CucsSysfileDigestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3, 1, 2),
    _CucsSysfileDigestDn_Type()
)
cucsSysfileDigestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileDigestDn.setStatus("current")
_CucsSysfileDigestRn_Type = SnmpAdminString
_CucsSysfileDigestRn_Object = MibTableColumn
cucsSysfileDigestRn = _CucsSysfileDigestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3, 1, 3),
    _CucsSysfileDigestRn_Type()
)
cucsSysfileDigestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileDigestRn.setStatus("current")
_CucsSysfileDigestCreationTS_Type = Unsigned64
_CucsSysfileDigestCreationTS_Object = MibTableColumn
cucsSysfileDigestCreationTS = _CucsSysfileDigestCreationTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3, 1, 4),
    _CucsSysfileDigestCreationTS_Type()
)
cucsSysfileDigestCreationTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileDigestCreationTS.setStatus("current")
_CucsSysfileDigestDescr_Type = SnmpAdminString
_CucsSysfileDigestDescr_Object = MibTableColumn
cucsSysfileDigestDescr = _CucsSysfileDigestDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3, 1, 5),
    _CucsSysfileDigestDescr_Type()
)
cucsSysfileDigestDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileDigestDescr.setStatus("current")
_CucsSysfileDigestName_Type = SnmpAdminString
_CucsSysfileDigestName_Object = MibTableColumn
cucsSysfileDigestName = _CucsSysfileDigestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3, 1, 6),
    _CucsSysfileDigestName_Type()
)
cucsSysfileDigestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileDigestName.setStatus("current")
_CucsSysfileDigestSize_Type = Gauge32
_CucsSysfileDigestSize_Object = MibTableColumn
cucsSysfileDigestSize = _CucsSysfileDigestSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3, 1, 7),
    _CucsSysfileDigestSize_Type()
)
cucsSysfileDigestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileDigestSize.setStatus("current")
_CucsSysfileDigestSource_Type = SnmpAdminString
_CucsSysfileDigestSource_Object = MibTableColumn
cucsSysfileDigestSource = _CucsSysfileDigestSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3, 1, 8),
    _CucsSysfileDigestSource_Type()
)
cucsSysfileDigestSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileDigestSource.setStatus("current")
_CucsSysfileDigestSwitchId_Type = CucsNetworkSwitchId
_CucsSysfileDigestSwitchId_Object = MibTableColumn
cucsSysfileDigestSwitchId = _CucsSysfileDigestSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3, 1, 9),
    _CucsSysfileDigestSwitchId_Type()
)
cucsSysfileDigestSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileDigestSwitchId.setStatus("current")
_CucsSysfileDigestTs_Type = DateAndTime
_CucsSysfileDigestTs_Object = MibTableColumn
cucsSysfileDigestTs = _CucsSysfileDigestTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3, 1, 10),
    _CucsSysfileDigestTs_Type()
)
cucsSysfileDigestTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileDigestTs.setStatus("current")
_CucsSysfileDigestUri_Type = SnmpAdminString
_CucsSysfileDigestUri_Object = MibTableColumn
cucsSysfileDigestUri = _CucsSysfileDigestUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 3, 1, 11),
    _CucsSysfileDigestUri_Type()
)
cucsSysfileDigestUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileDigestUri.setStatus("current")
_CucsSysfileMutationFsmTable_Object = MibTable
cucsSysfileMutationFsmTable = _CucsSysfileMutationFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4)
)
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmTable.setStatus("current")
_CucsSysfileMutationFsmEntry_Object = MibTableRow
cucsSysfileMutationFsmEntry = _CucsSysfileMutationFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4, 1)
)
cucsSysfileMutationFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSFILE-MIB", "cucsSysfileMutationFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmEntry.setStatus("current")
_CucsSysfileMutationFsmInstanceId_Type = CucsManagedObjectId
_CucsSysfileMutationFsmInstanceId_Object = MibTableColumn
cucsSysfileMutationFsmInstanceId = _CucsSysfileMutationFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4, 1, 1),
    _CucsSysfileMutationFsmInstanceId_Type()
)
cucsSysfileMutationFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmInstanceId.setStatus("current")
_CucsSysfileMutationFsmDn_Type = CucsManagedObjectDn
_CucsSysfileMutationFsmDn_Object = MibTableColumn
cucsSysfileMutationFsmDn = _CucsSysfileMutationFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4, 1, 2),
    _CucsSysfileMutationFsmDn_Type()
)
cucsSysfileMutationFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmDn.setStatus("current")
_CucsSysfileMutationFsmRn_Type = SnmpAdminString
_CucsSysfileMutationFsmRn_Object = MibTableColumn
cucsSysfileMutationFsmRn = _CucsSysfileMutationFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4, 1, 3),
    _CucsSysfileMutationFsmRn_Type()
)
cucsSysfileMutationFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmRn.setStatus("current")
_CucsSysfileMutationFsmCompletionTime_Type = DateAndTime
_CucsSysfileMutationFsmCompletionTime_Object = MibTableColumn
cucsSysfileMutationFsmCompletionTime = _CucsSysfileMutationFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4, 1, 4),
    _CucsSysfileMutationFsmCompletionTime_Type()
)
cucsSysfileMutationFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmCompletionTime.setStatus("current")
_CucsSysfileMutationFsmCurrentFsm_Type = CucsSysfileMutationFsmCurrentFsm
_CucsSysfileMutationFsmCurrentFsm_Object = MibTableColumn
cucsSysfileMutationFsmCurrentFsm = _CucsSysfileMutationFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4, 1, 5),
    _CucsSysfileMutationFsmCurrentFsm_Type()
)
cucsSysfileMutationFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmCurrentFsm.setStatus("current")
_CucsSysfileMutationFsmDescrData_Type = SnmpAdminString
_CucsSysfileMutationFsmDescrData_Object = MibTableColumn
cucsSysfileMutationFsmDescrData = _CucsSysfileMutationFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4, 1, 6),
    _CucsSysfileMutationFsmDescrData_Type()
)
cucsSysfileMutationFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmDescrData.setStatus("current")
_CucsSysfileMutationFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSysfileMutationFsmFsmStatus_Object = MibTableColumn
cucsSysfileMutationFsmFsmStatus = _CucsSysfileMutationFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4, 1, 7),
    _CucsSysfileMutationFsmFsmStatus_Type()
)
cucsSysfileMutationFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmFsmStatus.setStatus("current")
_CucsSysfileMutationFsmProgress_Type = Gauge32
_CucsSysfileMutationFsmProgress_Object = MibTableColumn
cucsSysfileMutationFsmProgress = _CucsSysfileMutationFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4, 1, 8),
    _CucsSysfileMutationFsmProgress_Type()
)
cucsSysfileMutationFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmProgress.setStatus("current")
_CucsSysfileMutationFsmRmtErrCode_Type = Gauge32
_CucsSysfileMutationFsmRmtErrCode_Object = MibTableColumn
cucsSysfileMutationFsmRmtErrCode = _CucsSysfileMutationFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4, 1, 9),
    _CucsSysfileMutationFsmRmtErrCode_Type()
)
cucsSysfileMutationFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmRmtErrCode.setStatus("current")
_CucsSysfileMutationFsmRmtErrDescr_Type = SnmpAdminString
_CucsSysfileMutationFsmRmtErrDescr_Object = MibTableColumn
cucsSysfileMutationFsmRmtErrDescr = _CucsSysfileMutationFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4, 1, 10),
    _CucsSysfileMutationFsmRmtErrDescr_Type()
)
cucsSysfileMutationFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmRmtErrDescr.setStatus("current")
_CucsSysfileMutationFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSysfileMutationFsmRmtRslt_Object = MibTableColumn
cucsSysfileMutationFsmRmtRslt = _CucsSysfileMutationFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 4, 1, 11),
    _CucsSysfileMutationFsmRmtRslt_Type()
)
cucsSysfileMutationFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmRmtRslt.setStatus("current")
_CucsSysfileMutationFsmStageTable_Object = MibTable
cucsSysfileMutationFsmStageTable = _CucsSysfileMutationFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 5)
)
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStageTable.setStatus("current")
_CucsSysfileMutationFsmStageEntry_Object = MibTableRow
cucsSysfileMutationFsmStageEntry = _CucsSysfileMutationFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 5, 1)
)
cucsSysfileMutationFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SYSFILE-MIB", "cucsSysfileMutationFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStageEntry.setStatus("current")
_CucsSysfileMutationFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSysfileMutationFsmStageInstanceId_Object = MibTableColumn
cucsSysfileMutationFsmStageInstanceId = _CucsSysfileMutationFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 5, 1, 1),
    _CucsSysfileMutationFsmStageInstanceId_Type()
)
cucsSysfileMutationFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStageInstanceId.setStatus("current")
_CucsSysfileMutationFsmStageDn_Type = CucsManagedObjectDn
_CucsSysfileMutationFsmStageDn_Object = MibTableColumn
cucsSysfileMutationFsmStageDn = _CucsSysfileMutationFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 5, 1, 2),
    _CucsSysfileMutationFsmStageDn_Type()
)
cucsSysfileMutationFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStageDn.setStatus("current")
_CucsSysfileMutationFsmStageRn_Type = SnmpAdminString
_CucsSysfileMutationFsmStageRn_Object = MibTableColumn
cucsSysfileMutationFsmStageRn = _CucsSysfileMutationFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 5, 1, 3),
    _CucsSysfileMutationFsmStageRn_Type()
)
cucsSysfileMutationFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStageRn.setStatus("current")
_CucsSysfileMutationFsmStageDescrData_Type = SnmpAdminString
_CucsSysfileMutationFsmStageDescrData_Object = MibTableColumn
cucsSysfileMutationFsmStageDescrData = _CucsSysfileMutationFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 5, 1, 4),
    _CucsSysfileMutationFsmStageDescrData_Type()
)
cucsSysfileMutationFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStageDescrData.setStatus("current")
_CucsSysfileMutationFsmStageLastUpdateTime_Type = DateAndTime
_CucsSysfileMutationFsmStageLastUpdateTime_Object = MibTableColumn
cucsSysfileMutationFsmStageLastUpdateTime = _CucsSysfileMutationFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 5, 1, 5),
    _CucsSysfileMutationFsmStageLastUpdateTime_Type()
)
cucsSysfileMutationFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStageLastUpdateTime.setStatus("current")
_CucsSysfileMutationFsmStageName_Type = CucsSysfileMutationFsmStageName
_CucsSysfileMutationFsmStageName_Object = MibTableColumn
cucsSysfileMutationFsmStageName = _CucsSysfileMutationFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 5, 1, 6),
    _CucsSysfileMutationFsmStageName_Type()
)
cucsSysfileMutationFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStageName.setStatus("current")
_CucsSysfileMutationFsmStageOrder_Type = Gauge32
_CucsSysfileMutationFsmStageOrder_Object = MibTableColumn
cucsSysfileMutationFsmStageOrder = _CucsSysfileMutationFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 5, 1, 7),
    _CucsSysfileMutationFsmStageOrder_Type()
)
cucsSysfileMutationFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStageOrder.setStatus("current")
_CucsSysfileMutationFsmStageRetry_Type = Gauge32
_CucsSysfileMutationFsmStageRetry_Object = MibTableColumn
cucsSysfileMutationFsmStageRetry = _CucsSysfileMutationFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 5, 1, 8),
    _CucsSysfileMutationFsmStageRetry_Type()
)
cucsSysfileMutationFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStageRetry.setStatus("current")
_CucsSysfileMutationFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSysfileMutationFsmStageStageStatus_Object = MibTableColumn
cucsSysfileMutationFsmStageStageStatus = _CucsSysfileMutationFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 48, 5, 1, 9),
    _CucsSysfileMutationFsmStageStageStatus_Type()
)
cucsSysfileMutationFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSysfileMutationFsmStageStageStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-SYSFILE-MIB",
    **{"cucsSysfileObjects": cucsSysfileObjects,
       "cucsSysfileMutationTable": cucsSysfileMutationTable,
       "cucsSysfileMutationEntry": cucsSysfileMutationEntry,
       "cucsSysfileMutationInstanceId": cucsSysfileMutationInstanceId,
       "cucsSysfileMutationDn": cucsSysfileMutationDn,
       "cucsSysfileMutationRn": cucsSysfileMutationRn,
       "cucsSysfileMutationAction": cucsSysfileMutationAction,
       "cucsSysfileMutationDescr": cucsSysfileMutationDescr,
       "cucsSysfileMutationFsmDescr": cucsSysfileMutationFsmDescr,
       "cucsSysfileMutationFsmPrev": cucsSysfileMutationFsmPrev,
       "cucsSysfileMutationFsmProgr": cucsSysfileMutationFsmProgr,
       "cucsSysfileMutationFsmRmtInvErrCode": cucsSysfileMutationFsmRmtInvErrCode,
       "cucsSysfileMutationFsmRmtInvErrDescr": cucsSysfileMutationFsmRmtInvErrDescr,
       "cucsSysfileMutationFsmRmtInvRslt": cucsSysfileMutationFsmRmtInvRslt,
       "cucsSysfileMutationFsmStageDescr": cucsSysfileMutationFsmStageDescr,
       "cucsSysfileMutationFsmStamp": cucsSysfileMutationFsmStamp,
       "cucsSysfileMutationFsmStatus": cucsSysfileMutationFsmStatus,
       "cucsSysfileMutationFsmTry": cucsSysfileMutationFsmTry,
       "cucsSysfileMutationFsmTaskTable": cucsSysfileMutationFsmTaskTable,
       "cucsSysfileMutationFsmTaskEntry": cucsSysfileMutationFsmTaskEntry,
       "cucsSysfileMutationFsmTaskInstanceId": cucsSysfileMutationFsmTaskInstanceId,
       "cucsSysfileMutationFsmTaskDn": cucsSysfileMutationFsmTaskDn,
       "cucsSysfileMutationFsmTaskRn": cucsSysfileMutationFsmTaskRn,
       "cucsSysfileMutationFsmTaskCompletion": cucsSysfileMutationFsmTaskCompletion,
       "cucsSysfileMutationFsmTaskFlags": cucsSysfileMutationFsmTaskFlags,
       "cucsSysfileMutationFsmTaskItem": cucsSysfileMutationFsmTaskItem,
       "cucsSysfileMutationFsmTaskSeqId": cucsSysfileMutationFsmTaskSeqId,
       "cucsSysfileDigestTable": cucsSysfileDigestTable,
       "cucsSysfileDigestEntry": cucsSysfileDigestEntry,
       "cucsSysfileDigestInstanceId": cucsSysfileDigestInstanceId,
       "cucsSysfileDigestDn": cucsSysfileDigestDn,
       "cucsSysfileDigestRn": cucsSysfileDigestRn,
       "cucsSysfileDigestCreationTS": cucsSysfileDigestCreationTS,
       "cucsSysfileDigestDescr": cucsSysfileDigestDescr,
       "cucsSysfileDigestName": cucsSysfileDigestName,
       "cucsSysfileDigestSize": cucsSysfileDigestSize,
       "cucsSysfileDigestSource": cucsSysfileDigestSource,
       "cucsSysfileDigestSwitchId": cucsSysfileDigestSwitchId,
       "cucsSysfileDigestTs": cucsSysfileDigestTs,
       "cucsSysfileDigestUri": cucsSysfileDigestUri,
       "cucsSysfileMutationFsmTable": cucsSysfileMutationFsmTable,
       "cucsSysfileMutationFsmEntry": cucsSysfileMutationFsmEntry,
       "cucsSysfileMutationFsmInstanceId": cucsSysfileMutationFsmInstanceId,
       "cucsSysfileMutationFsmDn": cucsSysfileMutationFsmDn,
       "cucsSysfileMutationFsmRn": cucsSysfileMutationFsmRn,
       "cucsSysfileMutationFsmCompletionTime": cucsSysfileMutationFsmCompletionTime,
       "cucsSysfileMutationFsmCurrentFsm": cucsSysfileMutationFsmCurrentFsm,
       "cucsSysfileMutationFsmDescrData": cucsSysfileMutationFsmDescrData,
       "cucsSysfileMutationFsmFsmStatus": cucsSysfileMutationFsmFsmStatus,
       "cucsSysfileMutationFsmProgress": cucsSysfileMutationFsmProgress,
       "cucsSysfileMutationFsmRmtErrCode": cucsSysfileMutationFsmRmtErrCode,
       "cucsSysfileMutationFsmRmtErrDescr": cucsSysfileMutationFsmRmtErrDescr,
       "cucsSysfileMutationFsmRmtRslt": cucsSysfileMutationFsmRmtRslt,
       "cucsSysfileMutationFsmStageTable": cucsSysfileMutationFsmStageTable,
       "cucsSysfileMutationFsmStageEntry": cucsSysfileMutationFsmStageEntry,
       "cucsSysfileMutationFsmStageInstanceId": cucsSysfileMutationFsmStageInstanceId,
       "cucsSysfileMutationFsmStageDn": cucsSysfileMutationFsmStageDn,
       "cucsSysfileMutationFsmStageRn": cucsSysfileMutationFsmStageRn,
       "cucsSysfileMutationFsmStageDescrData": cucsSysfileMutationFsmStageDescrData,
       "cucsSysfileMutationFsmStageLastUpdateTime": cucsSysfileMutationFsmStageLastUpdateTime,
       "cucsSysfileMutationFsmStageName": cucsSysfileMutationFsmStageName,
       "cucsSysfileMutationFsmStageOrder": cucsSysfileMutationFsmStageOrder,
       "cucsSysfileMutationFsmStageRetry": cucsSysfileMutationFsmStageRetry,
       "cucsSysfileMutationFsmStageStageStatus": cucsSysfileMutationFsmStageStageStatus}
)
