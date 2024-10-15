# SNMP MIB module (CISCO-UNIFIED-COMPUTING-NFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-NFS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:01 2024
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
 CucsNfsClientConfigState,
 CucsNfsDefAdminState,
 CucsNfsMntAdminState,
 CucsNfsMntOperState,
 CucsNfsMountDefFsmCurrentFsm,
 CucsNfsMountDefFsmStageName,
 CucsNfsMountDefFsmTaskItem,
 CucsNfsMountInstFsmCurrentFsm,
 CucsNfsMountInstFsmStageName,
 CucsNfsMountInstFsmTaskItem,
 CucsNfsPurpose,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsNfsClientConfigState",
    "CucsNfsDefAdminState",
    "CucsNfsMntAdminState",
    "CucsNfsMntOperState",
    "CucsNfsMountDefFsmCurrentFsm",
    "CucsNfsMountDefFsmStageName",
    "CucsNfsMountDefFsmTaskItem",
    "CucsNfsMountInstFsmCurrentFsm",
    "CucsNfsMountInstFsmStageName",
    "CucsNfsMountInstFsmTaskItem",
    "CucsNfsPurpose",
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

cucsNfsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsNfsEpTable_Object = MibTable
cucsNfsEpTable = _CucsNfsEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 1)
)
if mibBuilder.loadTexts:
    cucsNfsEpTable.setStatus("current")
_CucsNfsEpEntry_Object = MibTableRow
cucsNfsEpEntry = _CucsNfsEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 1, 1)
)
cucsNfsEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NFS-MIB", "cucsNfsEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNfsEpEntry.setStatus("current")
_CucsNfsEpInstanceId_Type = CucsManagedObjectId
_CucsNfsEpInstanceId_Object = MibTableColumn
cucsNfsEpInstanceId = _CucsNfsEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 1, 1, 1),
    _CucsNfsEpInstanceId_Type()
)
cucsNfsEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNfsEpInstanceId.setStatus("current")
_CucsNfsEpDn_Type = CucsManagedObjectDn
_CucsNfsEpDn_Object = MibTableColumn
cucsNfsEpDn = _CucsNfsEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 1, 1, 2),
    _CucsNfsEpDn_Type()
)
cucsNfsEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsEpDn.setStatus("current")
_CucsNfsEpRn_Type = SnmpAdminString
_CucsNfsEpRn_Object = MibTableColumn
cucsNfsEpRn = _CucsNfsEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 1, 1, 3),
    _CucsNfsEpRn_Type()
)
cucsNfsEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsEpRn.setStatus("current")
_CucsNfsMountDefTable_Object = MibTable
cucsNfsMountDefTable = _CucsNfsMountDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2)
)
if mibBuilder.loadTexts:
    cucsNfsMountDefTable.setStatus("current")
_CucsNfsMountDefEntry_Object = MibTableRow
cucsNfsMountDefEntry = _CucsNfsMountDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1)
)
cucsNfsMountDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NFS-MIB", "cucsNfsMountDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNfsMountDefEntry.setStatus("current")
_CucsNfsMountDefInstanceId_Type = CucsManagedObjectId
_CucsNfsMountDefInstanceId_Object = MibTableColumn
cucsNfsMountDefInstanceId = _CucsNfsMountDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 1),
    _CucsNfsMountDefInstanceId_Type()
)
cucsNfsMountDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNfsMountDefInstanceId.setStatus("current")
_CucsNfsMountDefDn_Type = CucsManagedObjectDn
_CucsNfsMountDefDn_Object = MibTableColumn
cucsNfsMountDefDn = _CucsNfsMountDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 2),
    _CucsNfsMountDefDn_Type()
)
cucsNfsMountDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefDn.setStatus("current")
_CucsNfsMountDefRn_Type = SnmpAdminString
_CucsNfsMountDefRn_Object = MibTableColumn
cucsNfsMountDefRn = _CucsNfsMountDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 3),
    _CucsNfsMountDefRn_Type()
)
cucsNfsMountDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefRn.setStatus("current")
_CucsNfsMountDefAdminState_Type = CucsNfsDefAdminState
_CucsNfsMountDefAdminState_Object = MibTableColumn
cucsNfsMountDefAdminState = _CucsNfsMountDefAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 4),
    _CucsNfsMountDefAdminState_Type()
)
cucsNfsMountDefAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefAdminState.setStatus("current")
_CucsNfsMountDefDescr_Type = SnmpAdminString
_CucsNfsMountDefDescr_Object = MibTableColumn
cucsNfsMountDefDescr = _CucsNfsMountDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 5),
    _CucsNfsMountDefDescr_Type()
)
cucsNfsMountDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefDescr.setStatus("current")
_CucsNfsMountDefFltAggr_Type = Unsigned64
_CucsNfsMountDefFltAggr_Object = MibTableColumn
cucsNfsMountDefFltAggr = _CucsNfsMountDefFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 6),
    _CucsNfsMountDefFltAggr_Type()
)
cucsNfsMountDefFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFltAggr.setStatus("current")
_CucsNfsMountDefFsmDescr_Type = SnmpAdminString
_CucsNfsMountDefFsmDescr_Object = MibTableColumn
cucsNfsMountDefFsmDescr = _CucsNfsMountDefFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 7),
    _CucsNfsMountDefFsmDescr_Type()
)
cucsNfsMountDefFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmDescr.setStatus("current")
_CucsNfsMountDefFsmPrev_Type = SnmpAdminString
_CucsNfsMountDefFsmPrev_Object = MibTableColumn
cucsNfsMountDefFsmPrev = _CucsNfsMountDefFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 8),
    _CucsNfsMountDefFsmPrev_Type()
)
cucsNfsMountDefFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmPrev.setStatus("current")
_CucsNfsMountDefFsmProgr_Type = Gauge32
_CucsNfsMountDefFsmProgr_Object = MibTableColumn
cucsNfsMountDefFsmProgr = _CucsNfsMountDefFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 9),
    _CucsNfsMountDefFsmProgr_Type()
)
cucsNfsMountDefFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmProgr.setStatus("current")
_CucsNfsMountDefFsmRmtInvErrCode_Type = Gauge32
_CucsNfsMountDefFsmRmtInvErrCode_Object = MibTableColumn
cucsNfsMountDefFsmRmtInvErrCode = _CucsNfsMountDefFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 10),
    _CucsNfsMountDefFsmRmtInvErrCode_Type()
)
cucsNfsMountDefFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmRmtInvErrCode.setStatus("current")
_CucsNfsMountDefFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsNfsMountDefFsmRmtInvErrDescr_Object = MibTableColumn
cucsNfsMountDefFsmRmtInvErrDescr = _CucsNfsMountDefFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 11),
    _CucsNfsMountDefFsmRmtInvErrDescr_Type()
)
cucsNfsMountDefFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmRmtInvErrDescr.setStatus("current")
_CucsNfsMountDefFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsNfsMountDefFsmRmtInvRslt_Object = MibTableColumn
cucsNfsMountDefFsmRmtInvRslt = _CucsNfsMountDefFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 12),
    _CucsNfsMountDefFsmRmtInvRslt_Type()
)
cucsNfsMountDefFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmRmtInvRslt.setStatus("current")
_CucsNfsMountDefFsmStageDescr_Type = SnmpAdminString
_CucsNfsMountDefFsmStageDescr_Object = MibTableColumn
cucsNfsMountDefFsmStageDescr = _CucsNfsMountDefFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 13),
    _CucsNfsMountDefFsmStageDescr_Type()
)
cucsNfsMountDefFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStageDescr.setStatus("current")
_CucsNfsMountDefFsmStamp_Type = DateAndTime
_CucsNfsMountDefFsmStamp_Object = MibTableColumn
cucsNfsMountDefFsmStamp = _CucsNfsMountDefFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 14),
    _CucsNfsMountDefFsmStamp_Type()
)
cucsNfsMountDefFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStamp.setStatus("current")
_CucsNfsMountDefFsmStatus_Type = SnmpAdminString
_CucsNfsMountDefFsmStatus_Object = MibTableColumn
cucsNfsMountDefFsmStatus = _CucsNfsMountDefFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 15),
    _CucsNfsMountDefFsmStatus_Type()
)
cucsNfsMountDefFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStatus.setStatus("current")
_CucsNfsMountDefFsmTry_Type = Gauge32
_CucsNfsMountDefFsmTry_Object = MibTableColumn
cucsNfsMountDefFsmTry = _CucsNfsMountDefFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 16),
    _CucsNfsMountDefFsmTry_Type()
)
cucsNfsMountDefFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmTry.setStatus("current")
_CucsNfsMountDefIntId_Type = SnmpAdminString
_CucsNfsMountDefIntId_Object = MibTableColumn
cucsNfsMountDefIntId = _CucsNfsMountDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 17),
    _CucsNfsMountDefIntId_Type()
)
cucsNfsMountDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefIntId.setStatus("current")
_CucsNfsMountDefLocalDir_Type = SnmpAdminString
_CucsNfsMountDefLocalDir_Object = MibTableColumn
cucsNfsMountDefLocalDir = _CucsNfsMountDefLocalDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 18),
    _CucsNfsMountDefLocalDir_Type()
)
cucsNfsMountDefLocalDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefLocalDir.setStatus("current")
_CucsNfsMountDefName_Type = SnmpAdminString
_CucsNfsMountDefName_Object = MibTableColumn
cucsNfsMountDefName = _CucsNfsMountDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 19),
    _CucsNfsMountDefName_Type()
)
cucsNfsMountDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefName.setStatus("current")
_CucsNfsMountDefPolicyLevel_Type = Gauge32
_CucsNfsMountDefPolicyLevel_Object = MibTableColumn
cucsNfsMountDefPolicyLevel = _CucsNfsMountDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 20),
    _CucsNfsMountDefPolicyLevel_Type()
)
cucsNfsMountDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefPolicyLevel.setStatus("current")
_CucsNfsMountDefPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsNfsMountDefPolicyOwner_Object = MibTableColumn
cucsNfsMountDefPolicyOwner = _CucsNfsMountDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 21),
    _CucsNfsMountDefPolicyOwner_Type()
)
cucsNfsMountDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefPolicyOwner.setStatus("current")
_CucsNfsMountDefPurpose_Type = CucsNfsPurpose
_CucsNfsMountDefPurpose_Object = MibTableColumn
cucsNfsMountDefPurpose = _CucsNfsMountDefPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 22),
    _CucsNfsMountDefPurpose_Type()
)
cucsNfsMountDefPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefPurpose.setStatus("current")
_CucsNfsMountDefRemoteDir_Type = SnmpAdminString
_CucsNfsMountDefRemoteDir_Object = MibTableColumn
cucsNfsMountDefRemoteDir = _CucsNfsMountDefRemoteDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 23),
    _CucsNfsMountDefRemoteDir_Type()
)
cucsNfsMountDefRemoteDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefRemoteDir.setStatus("current")
_CucsNfsMountDefServer_Type = SnmpAdminString
_CucsNfsMountDefServer_Object = MibTableColumn
cucsNfsMountDefServer = _CucsNfsMountDefServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 2, 1, 24),
    _CucsNfsMountDefServer_Type()
)
cucsNfsMountDefServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefServer.setStatus("current")
_CucsNfsMountDefFsmTable_Object = MibTable
cucsNfsMountDefFsmTable = _CucsNfsMountDefFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3)
)
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmTable.setStatus("current")
_CucsNfsMountDefFsmEntry_Object = MibTableRow
cucsNfsMountDefFsmEntry = _CucsNfsMountDefFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3, 1)
)
cucsNfsMountDefFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NFS-MIB", "cucsNfsMountDefFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmEntry.setStatus("current")
_CucsNfsMountDefFsmInstanceId_Type = CucsManagedObjectId
_CucsNfsMountDefFsmInstanceId_Object = MibTableColumn
cucsNfsMountDefFsmInstanceId = _CucsNfsMountDefFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3, 1, 1),
    _CucsNfsMountDefFsmInstanceId_Type()
)
cucsNfsMountDefFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmInstanceId.setStatus("current")
_CucsNfsMountDefFsmDn_Type = CucsManagedObjectDn
_CucsNfsMountDefFsmDn_Object = MibTableColumn
cucsNfsMountDefFsmDn = _CucsNfsMountDefFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3, 1, 2),
    _CucsNfsMountDefFsmDn_Type()
)
cucsNfsMountDefFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmDn.setStatus("current")
_CucsNfsMountDefFsmRn_Type = SnmpAdminString
_CucsNfsMountDefFsmRn_Object = MibTableColumn
cucsNfsMountDefFsmRn = _CucsNfsMountDefFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3, 1, 3),
    _CucsNfsMountDefFsmRn_Type()
)
cucsNfsMountDefFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmRn.setStatus("current")
_CucsNfsMountDefFsmCompletionTime_Type = DateAndTime
_CucsNfsMountDefFsmCompletionTime_Object = MibTableColumn
cucsNfsMountDefFsmCompletionTime = _CucsNfsMountDefFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3, 1, 4),
    _CucsNfsMountDefFsmCompletionTime_Type()
)
cucsNfsMountDefFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmCompletionTime.setStatus("current")
_CucsNfsMountDefFsmCurrentFsm_Type = CucsNfsMountDefFsmCurrentFsm
_CucsNfsMountDefFsmCurrentFsm_Object = MibTableColumn
cucsNfsMountDefFsmCurrentFsm = _CucsNfsMountDefFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3, 1, 5),
    _CucsNfsMountDefFsmCurrentFsm_Type()
)
cucsNfsMountDefFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmCurrentFsm.setStatus("current")
_CucsNfsMountDefFsmDescrData_Type = SnmpAdminString
_CucsNfsMountDefFsmDescrData_Object = MibTableColumn
cucsNfsMountDefFsmDescrData = _CucsNfsMountDefFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3, 1, 6),
    _CucsNfsMountDefFsmDescrData_Type()
)
cucsNfsMountDefFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmDescrData.setStatus("current")
_CucsNfsMountDefFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsNfsMountDefFsmFsmStatus_Object = MibTableColumn
cucsNfsMountDefFsmFsmStatus = _CucsNfsMountDefFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3, 1, 7),
    _CucsNfsMountDefFsmFsmStatus_Type()
)
cucsNfsMountDefFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmFsmStatus.setStatus("current")
_CucsNfsMountDefFsmProgress_Type = Gauge32
_CucsNfsMountDefFsmProgress_Object = MibTableColumn
cucsNfsMountDefFsmProgress = _CucsNfsMountDefFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3, 1, 8),
    _CucsNfsMountDefFsmProgress_Type()
)
cucsNfsMountDefFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmProgress.setStatus("current")
_CucsNfsMountDefFsmRmtErrCode_Type = Gauge32
_CucsNfsMountDefFsmRmtErrCode_Object = MibTableColumn
cucsNfsMountDefFsmRmtErrCode = _CucsNfsMountDefFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3, 1, 9),
    _CucsNfsMountDefFsmRmtErrCode_Type()
)
cucsNfsMountDefFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmRmtErrCode.setStatus("current")
_CucsNfsMountDefFsmRmtErrDescr_Type = SnmpAdminString
_CucsNfsMountDefFsmRmtErrDescr_Object = MibTableColumn
cucsNfsMountDefFsmRmtErrDescr = _CucsNfsMountDefFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3, 1, 10),
    _CucsNfsMountDefFsmRmtErrDescr_Type()
)
cucsNfsMountDefFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmRmtErrDescr.setStatus("current")
_CucsNfsMountDefFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsNfsMountDefFsmRmtRslt_Object = MibTableColumn
cucsNfsMountDefFsmRmtRslt = _CucsNfsMountDefFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 3, 1, 11),
    _CucsNfsMountDefFsmRmtRslt_Type()
)
cucsNfsMountDefFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmRmtRslt.setStatus("current")
_CucsNfsMountDefFsmStageTable_Object = MibTable
cucsNfsMountDefFsmStageTable = _CucsNfsMountDefFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 4)
)
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStageTable.setStatus("current")
_CucsNfsMountDefFsmStageEntry_Object = MibTableRow
cucsNfsMountDefFsmStageEntry = _CucsNfsMountDefFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 4, 1)
)
cucsNfsMountDefFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NFS-MIB", "cucsNfsMountDefFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStageEntry.setStatus("current")
_CucsNfsMountDefFsmStageInstanceId_Type = CucsManagedObjectId
_CucsNfsMountDefFsmStageInstanceId_Object = MibTableColumn
cucsNfsMountDefFsmStageInstanceId = _CucsNfsMountDefFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 4, 1, 1),
    _CucsNfsMountDefFsmStageInstanceId_Type()
)
cucsNfsMountDefFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStageInstanceId.setStatus("current")
_CucsNfsMountDefFsmStageDn_Type = CucsManagedObjectDn
_CucsNfsMountDefFsmStageDn_Object = MibTableColumn
cucsNfsMountDefFsmStageDn = _CucsNfsMountDefFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 4, 1, 2),
    _CucsNfsMountDefFsmStageDn_Type()
)
cucsNfsMountDefFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStageDn.setStatus("current")
_CucsNfsMountDefFsmStageRn_Type = SnmpAdminString
_CucsNfsMountDefFsmStageRn_Object = MibTableColumn
cucsNfsMountDefFsmStageRn = _CucsNfsMountDefFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 4, 1, 3),
    _CucsNfsMountDefFsmStageRn_Type()
)
cucsNfsMountDefFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStageRn.setStatus("current")
_CucsNfsMountDefFsmStageDescrData_Type = SnmpAdminString
_CucsNfsMountDefFsmStageDescrData_Object = MibTableColumn
cucsNfsMountDefFsmStageDescrData = _CucsNfsMountDefFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 4, 1, 4),
    _CucsNfsMountDefFsmStageDescrData_Type()
)
cucsNfsMountDefFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStageDescrData.setStatus("current")
_CucsNfsMountDefFsmStageLastUpdateTime_Type = DateAndTime
_CucsNfsMountDefFsmStageLastUpdateTime_Object = MibTableColumn
cucsNfsMountDefFsmStageLastUpdateTime = _CucsNfsMountDefFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 4, 1, 5),
    _CucsNfsMountDefFsmStageLastUpdateTime_Type()
)
cucsNfsMountDefFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStageLastUpdateTime.setStatus("current")
_CucsNfsMountDefFsmStageName_Type = CucsNfsMountDefFsmStageName
_CucsNfsMountDefFsmStageName_Object = MibTableColumn
cucsNfsMountDefFsmStageName = _CucsNfsMountDefFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 4, 1, 6),
    _CucsNfsMountDefFsmStageName_Type()
)
cucsNfsMountDefFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStageName.setStatus("current")
_CucsNfsMountDefFsmStageOrder_Type = Gauge32
_CucsNfsMountDefFsmStageOrder_Object = MibTableColumn
cucsNfsMountDefFsmStageOrder = _CucsNfsMountDefFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 4, 1, 7),
    _CucsNfsMountDefFsmStageOrder_Type()
)
cucsNfsMountDefFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStageOrder.setStatus("current")
_CucsNfsMountDefFsmStageRetry_Type = Gauge32
_CucsNfsMountDefFsmStageRetry_Object = MibTableColumn
cucsNfsMountDefFsmStageRetry = _CucsNfsMountDefFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 4, 1, 8),
    _CucsNfsMountDefFsmStageRetry_Type()
)
cucsNfsMountDefFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStageRetry.setStatus("current")
_CucsNfsMountDefFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsNfsMountDefFsmStageStageStatus_Object = MibTableColumn
cucsNfsMountDefFsmStageStageStatus = _CucsNfsMountDefFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 4, 1, 9),
    _CucsNfsMountDefFsmStageStageStatus_Type()
)
cucsNfsMountDefFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmStageStageStatus.setStatus("current")
_CucsNfsMountDefFsmTaskTable_Object = MibTable
cucsNfsMountDefFsmTaskTable = _CucsNfsMountDefFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 5)
)
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmTaskTable.setStatus("current")
_CucsNfsMountDefFsmTaskEntry_Object = MibTableRow
cucsNfsMountDefFsmTaskEntry = _CucsNfsMountDefFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 5, 1)
)
cucsNfsMountDefFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NFS-MIB", "cucsNfsMountDefFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmTaskEntry.setStatus("current")
_CucsNfsMountDefFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsNfsMountDefFsmTaskInstanceId_Object = MibTableColumn
cucsNfsMountDefFsmTaskInstanceId = _CucsNfsMountDefFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 5, 1, 1),
    _CucsNfsMountDefFsmTaskInstanceId_Type()
)
cucsNfsMountDefFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmTaskInstanceId.setStatus("current")
_CucsNfsMountDefFsmTaskDn_Type = CucsManagedObjectDn
_CucsNfsMountDefFsmTaskDn_Object = MibTableColumn
cucsNfsMountDefFsmTaskDn = _CucsNfsMountDefFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 5, 1, 2),
    _CucsNfsMountDefFsmTaskDn_Type()
)
cucsNfsMountDefFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmTaskDn.setStatus("current")
_CucsNfsMountDefFsmTaskRn_Type = SnmpAdminString
_CucsNfsMountDefFsmTaskRn_Object = MibTableColumn
cucsNfsMountDefFsmTaskRn = _CucsNfsMountDefFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 5, 1, 3),
    _CucsNfsMountDefFsmTaskRn_Type()
)
cucsNfsMountDefFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmTaskRn.setStatus("current")
_CucsNfsMountDefFsmTaskCompletion_Type = CucsFsmCompletion
_CucsNfsMountDefFsmTaskCompletion_Object = MibTableColumn
cucsNfsMountDefFsmTaskCompletion = _CucsNfsMountDefFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 5, 1, 4),
    _CucsNfsMountDefFsmTaskCompletion_Type()
)
cucsNfsMountDefFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmTaskCompletion.setStatus("current")
_CucsNfsMountDefFsmTaskFlags_Type = CucsFsmFlags
_CucsNfsMountDefFsmTaskFlags_Object = MibTableColumn
cucsNfsMountDefFsmTaskFlags = _CucsNfsMountDefFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 5, 1, 5),
    _CucsNfsMountDefFsmTaskFlags_Type()
)
cucsNfsMountDefFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmTaskFlags.setStatus("current")
_CucsNfsMountDefFsmTaskItem_Type = CucsNfsMountDefFsmTaskItem
_CucsNfsMountDefFsmTaskItem_Object = MibTableColumn
cucsNfsMountDefFsmTaskItem = _CucsNfsMountDefFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 5, 1, 6),
    _CucsNfsMountDefFsmTaskItem_Type()
)
cucsNfsMountDefFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmTaskItem.setStatus("current")
_CucsNfsMountDefFsmTaskSeqId_Type = Gauge32
_CucsNfsMountDefFsmTaskSeqId_Object = MibTableColumn
cucsNfsMountDefFsmTaskSeqId = _CucsNfsMountDefFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 5, 1, 7),
    _CucsNfsMountDefFsmTaskSeqId_Type()
)
cucsNfsMountDefFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountDefFsmTaskSeqId.setStatus("current")
_CucsNfsMountInstTable_Object = MibTable
cucsNfsMountInstTable = _CucsNfsMountInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6)
)
if mibBuilder.loadTexts:
    cucsNfsMountInstTable.setStatus("current")
_CucsNfsMountInstEntry_Object = MibTableRow
cucsNfsMountInstEntry = _CucsNfsMountInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1)
)
cucsNfsMountInstEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NFS-MIB", "cucsNfsMountInstInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNfsMountInstEntry.setStatus("current")
_CucsNfsMountInstInstanceId_Type = CucsManagedObjectId
_CucsNfsMountInstInstanceId_Object = MibTableColumn
cucsNfsMountInstInstanceId = _CucsNfsMountInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 1),
    _CucsNfsMountInstInstanceId_Type()
)
cucsNfsMountInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNfsMountInstInstanceId.setStatus("current")
_CucsNfsMountInstDn_Type = CucsManagedObjectDn
_CucsNfsMountInstDn_Object = MibTableColumn
cucsNfsMountInstDn = _CucsNfsMountInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 2),
    _CucsNfsMountInstDn_Type()
)
cucsNfsMountInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstDn.setStatus("current")
_CucsNfsMountInstRn_Type = SnmpAdminString
_CucsNfsMountInstRn_Object = MibTableColumn
cucsNfsMountInstRn = _CucsNfsMountInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 3),
    _CucsNfsMountInstRn_Type()
)
cucsNfsMountInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstRn.setStatus("current")
_CucsNfsMountInstAdminState_Type = CucsNfsMntAdminState
_CucsNfsMountInstAdminState_Object = MibTableColumn
cucsNfsMountInstAdminState = _CucsNfsMountInstAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 4),
    _CucsNfsMountInstAdminState_Type()
)
cucsNfsMountInstAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstAdminState.setStatus("current")
_CucsNfsMountInstClientConfigState_Type = CucsNfsClientConfigState
_CucsNfsMountInstClientConfigState_Object = MibTableColumn
cucsNfsMountInstClientConfigState = _CucsNfsMountInstClientConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 5),
    _CucsNfsMountInstClientConfigState_Type()
)
cucsNfsMountInstClientConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstClientConfigState.setStatus("current")
_CucsNfsMountInstDefDn_Type = SnmpAdminString
_CucsNfsMountInstDefDn_Object = MibTableColumn
cucsNfsMountInstDefDn = _CucsNfsMountInstDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 6),
    _CucsNfsMountInstDefDn_Type()
)
cucsNfsMountInstDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstDefDn.setStatus("current")
_CucsNfsMountInstFsmDescr_Type = SnmpAdminString
_CucsNfsMountInstFsmDescr_Object = MibTableColumn
cucsNfsMountInstFsmDescr = _CucsNfsMountInstFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 7),
    _CucsNfsMountInstFsmDescr_Type()
)
cucsNfsMountInstFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmDescr.setStatus("current")
_CucsNfsMountInstFsmPrev_Type = SnmpAdminString
_CucsNfsMountInstFsmPrev_Object = MibTableColumn
cucsNfsMountInstFsmPrev = _CucsNfsMountInstFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 8),
    _CucsNfsMountInstFsmPrev_Type()
)
cucsNfsMountInstFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmPrev.setStatus("current")
_CucsNfsMountInstFsmProgr_Type = Gauge32
_CucsNfsMountInstFsmProgr_Object = MibTableColumn
cucsNfsMountInstFsmProgr = _CucsNfsMountInstFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 9),
    _CucsNfsMountInstFsmProgr_Type()
)
cucsNfsMountInstFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmProgr.setStatus("current")
_CucsNfsMountInstFsmRmtInvErrCode_Type = Gauge32
_CucsNfsMountInstFsmRmtInvErrCode_Object = MibTableColumn
cucsNfsMountInstFsmRmtInvErrCode = _CucsNfsMountInstFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 10),
    _CucsNfsMountInstFsmRmtInvErrCode_Type()
)
cucsNfsMountInstFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmRmtInvErrCode.setStatus("current")
_CucsNfsMountInstFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsNfsMountInstFsmRmtInvErrDescr_Object = MibTableColumn
cucsNfsMountInstFsmRmtInvErrDescr = _CucsNfsMountInstFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 11),
    _CucsNfsMountInstFsmRmtInvErrDescr_Type()
)
cucsNfsMountInstFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmRmtInvErrDescr.setStatus("current")
_CucsNfsMountInstFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsNfsMountInstFsmRmtInvRslt_Object = MibTableColumn
cucsNfsMountInstFsmRmtInvRslt = _CucsNfsMountInstFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 12),
    _CucsNfsMountInstFsmRmtInvRslt_Type()
)
cucsNfsMountInstFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmRmtInvRslt.setStatus("current")
_CucsNfsMountInstFsmStageDescr_Type = SnmpAdminString
_CucsNfsMountInstFsmStageDescr_Object = MibTableColumn
cucsNfsMountInstFsmStageDescr = _CucsNfsMountInstFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 13),
    _CucsNfsMountInstFsmStageDescr_Type()
)
cucsNfsMountInstFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStageDescr.setStatus("current")
_CucsNfsMountInstFsmStamp_Type = DateAndTime
_CucsNfsMountInstFsmStamp_Object = MibTableColumn
cucsNfsMountInstFsmStamp = _CucsNfsMountInstFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 14),
    _CucsNfsMountInstFsmStamp_Type()
)
cucsNfsMountInstFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStamp.setStatus("current")
_CucsNfsMountInstFsmStatus_Type = SnmpAdminString
_CucsNfsMountInstFsmStatus_Object = MibTableColumn
cucsNfsMountInstFsmStatus = _CucsNfsMountInstFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 15),
    _CucsNfsMountInstFsmStatus_Type()
)
cucsNfsMountInstFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStatus.setStatus("current")
_CucsNfsMountInstFsmTry_Type = Gauge32
_CucsNfsMountInstFsmTry_Object = MibTableColumn
cucsNfsMountInstFsmTry = _CucsNfsMountInstFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 16),
    _CucsNfsMountInstFsmTry_Type()
)
cucsNfsMountInstFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmTry.setStatus("current")
_CucsNfsMountInstLocalDir_Type = SnmpAdminString
_CucsNfsMountInstLocalDir_Object = MibTableColumn
cucsNfsMountInstLocalDir = _CucsNfsMountInstLocalDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 17),
    _CucsNfsMountInstLocalDir_Type()
)
cucsNfsMountInstLocalDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstLocalDir.setStatus("current")
_CucsNfsMountInstName_Type = SnmpAdminString
_CucsNfsMountInstName_Object = MibTableColumn
cucsNfsMountInstName = _CucsNfsMountInstName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 18),
    _CucsNfsMountInstName_Type()
)
cucsNfsMountInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstName.setStatus("current")
_CucsNfsMountInstOperState_Type = CucsNfsMntOperState
_CucsNfsMountInstOperState_Object = MibTableColumn
cucsNfsMountInstOperState = _CucsNfsMountInstOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 19),
    _CucsNfsMountInstOperState_Type()
)
cucsNfsMountInstOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstOperState.setStatus("current")
_CucsNfsMountInstPurpose_Type = CucsNfsPurpose
_CucsNfsMountInstPurpose_Object = MibTableColumn
cucsNfsMountInstPurpose = _CucsNfsMountInstPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 20),
    _CucsNfsMountInstPurpose_Type()
)
cucsNfsMountInstPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstPurpose.setStatus("current")
_CucsNfsMountInstRemoteDir_Type = SnmpAdminString
_CucsNfsMountInstRemoteDir_Object = MibTableColumn
cucsNfsMountInstRemoteDir = _CucsNfsMountInstRemoteDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 21),
    _CucsNfsMountInstRemoteDir_Type()
)
cucsNfsMountInstRemoteDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstRemoteDir.setStatus("current")
_CucsNfsMountInstServer_Type = SnmpAdminString
_CucsNfsMountInstServer_Object = MibTableColumn
cucsNfsMountInstServer = _CucsNfsMountInstServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 6, 1, 22),
    _CucsNfsMountInstServer_Type()
)
cucsNfsMountInstServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstServer.setStatus("current")
_CucsNfsMountInstFsmTable_Object = MibTable
cucsNfsMountInstFsmTable = _CucsNfsMountInstFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7)
)
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmTable.setStatus("current")
_CucsNfsMountInstFsmEntry_Object = MibTableRow
cucsNfsMountInstFsmEntry = _CucsNfsMountInstFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7, 1)
)
cucsNfsMountInstFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NFS-MIB", "cucsNfsMountInstFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmEntry.setStatus("current")
_CucsNfsMountInstFsmInstanceId_Type = CucsManagedObjectId
_CucsNfsMountInstFsmInstanceId_Object = MibTableColumn
cucsNfsMountInstFsmInstanceId = _CucsNfsMountInstFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7, 1, 1),
    _CucsNfsMountInstFsmInstanceId_Type()
)
cucsNfsMountInstFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmInstanceId.setStatus("current")
_CucsNfsMountInstFsmDn_Type = CucsManagedObjectDn
_CucsNfsMountInstFsmDn_Object = MibTableColumn
cucsNfsMountInstFsmDn = _CucsNfsMountInstFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7, 1, 2),
    _CucsNfsMountInstFsmDn_Type()
)
cucsNfsMountInstFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmDn.setStatus("current")
_CucsNfsMountInstFsmRn_Type = SnmpAdminString
_CucsNfsMountInstFsmRn_Object = MibTableColumn
cucsNfsMountInstFsmRn = _CucsNfsMountInstFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7, 1, 3),
    _CucsNfsMountInstFsmRn_Type()
)
cucsNfsMountInstFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmRn.setStatus("current")
_CucsNfsMountInstFsmCompletionTime_Type = DateAndTime
_CucsNfsMountInstFsmCompletionTime_Object = MibTableColumn
cucsNfsMountInstFsmCompletionTime = _CucsNfsMountInstFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7, 1, 4),
    _CucsNfsMountInstFsmCompletionTime_Type()
)
cucsNfsMountInstFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmCompletionTime.setStatus("current")
_CucsNfsMountInstFsmCurrentFsm_Type = CucsNfsMountInstFsmCurrentFsm
_CucsNfsMountInstFsmCurrentFsm_Object = MibTableColumn
cucsNfsMountInstFsmCurrentFsm = _CucsNfsMountInstFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7, 1, 5),
    _CucsNfsMountInstFsmCurrentFsm_Type()
)
cucsNfsMountInstFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmCurrentFsm.setStatus("current")
_CucsNfsMountInstFsmDescrData_Type = SnmpAdminString
_CucsNfsMountInstFsmDescrData_Object = MibTableColumn
cucsNfsMountInstFsmDescrData = _CucsNfsMountInstFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7, 1, 6),
    _CucsNfsMountInstFsmDescrData_Type()
)
cucsNfsMountInstFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmDescrData.setStatus("current")
_CucsNfsMountInstFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsNfsMountInstFsmFsmStatus_Object = MibTableColumn
cucsNfsMountInstFsmFsmStatus = _CucsNfsMountInstFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7, 1, 7),
    _CucsNfsMountInstFsmFsmStatus_Type()
)
cucsNfsMountInstFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmFsmStatus.setStatus("current")
_CucsNfsMountInstFsmProgress_Type = Gauge32
_CucsNfsMountInstFsmProgress_Object = MibTableColumn
cucsNfsMountInstFsmProgress = _CucsNfsMountInstFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7, 1, 8),
    _CucsNfsMountInstFsmProgress_Type()
)
cucsNfsMountInstFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmProgress.setStatus("current")
_CucsNfsMountInstFsmRmtErrCode_Type = Gauge32
_CucsNfsMountInstFsmRmtErrCode_Object = MibTableColumn
cucsNfsMountInstFsmRmtErrCode = _CucsNfsMountInstFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7, 1, 9),
    _CucsNfsMountInstFsmRmtErrCode_Type()
)
cucsNfsMountInstFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmRmtErrCode.setStatus("current")
_CucsNfsMountInstFsmRmtErrDescr_Type = SnmpAdminString
_CucsNfsMountInstFsmRmtErrDescr_Object = MibTableColumn
cucsNfsMountInstFsmRmtErrDescr = _CucsNfsMountInstFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7, 1, 10),
    _CucsNfsMountInstFsmRmtErrDescr_Type()
)
cucsNfsMountInstFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmRmtErrDescr.setStatus("current")
_CucsNfsMountInstFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsNfsMountInstFsmRmtRslt_Object = MibTableColumn
cucsNfsMountInstFsmRmtRslt = _CucsNfsMountInstFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 7, 1, 11),
    _CucsNfsMountInstFsmRmtRslt_Type()
)
cucsNfsMountInstFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmRmtRslt.setStatus("current")
_CucsNfsMountInstFsmStageTable_Object = MibTable
cucsNfsMountInstFsmStageTable = _CucsNfsMountInstFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 8)
)
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStageTable.setStatus("current")
_CucsNfsMountInstFsmStageEntry_Object = MibTableRow
cucsNfsMountInstFsmStageEntry = _CucsNfsMountInstFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 8, 1)
)
cucsNfsMountInstFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NFS-MIB", "cucsNfsMountInstFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStageEntry.setStatus("current")
_CucsNfsMountInstFsmStageInstanceId_Type = CucsManagedObjectId
_CucsNfsMountInstFsmStageInstanceId_Object = MibTableColumn
cucsNfsMountInstFsmStageInstanceId = _CucsNfsMountInstFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 8, 1, 1),
    _CucsNfsMountInstFsmStageInstanceId_Type()
)
cucsNfsMountInstFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStageInstanceId.setStatus("current")
_CucsNfsMountInstFsmStageDn_Type = CucsManagedObjectDn
_CucsNfsMountInstFsmStageDn_Object = MibTableColumn
cucsNfsMountInstFsmStageDn = _CucsNfsMountInstFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 8, 1, 2),
    _CucsNfsMountInstFsmStageDn_Type()
)
cucsNfsMountInstFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStageDn.setStatus("current")
_CucsNfsMountInstFsmStageRn_Type = SnmpAdminString
_CucsNfsMountInstFsmStageRn_Object = MibTableColumn
cucsNfsMountInstFsmStageRn = _CucsNfsMountInstFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 8, 1, 3),
    _CucsNfsMountInstFsmStageRn_Type()
)
cucsNfsMountInstFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStageRn.setStatus("current")
_CucsNfsMountInstFsmStageDescrData_Type = SnmpAdminString
_CucsNfsMountInstFsmStageDescrData_Object = MibTableColumn
cucsNfsMountInstFsmStageDescrData = _CucsNfsMountInstFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 8, 1, 4),
    _CucsNfsMountInstFsmStageDescrData_Type()
)
cucsNfsMountInstFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStageDescrData.setStatus("current")
_CucsNfsMountInstFsmStageLastUpdateTime_Type = DateAndTime
_CucsNfsMountInstFsmStageLastUpdateTime_Object = MibTableColumn
cucsNfsMountInstFsmStageLastUpdateTime = _CucsNfsMountInstFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 8, 1, 5),
    _CucsNfsMountInstFsmStageLastUpdateTime_Type()
)
cucsNfsMountInstFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStageLastUpdateTime.setStatus("current")
_CucsNfsMountInstFsmStageName_Type = CucsNfsMountInstFsmStageName
_CucsNfsMountInstFsmStageName_Object = MibTableColumn
cucsNfsMountInstFsmStageName = _CucsNfsMountInstFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 8, 1, 6),
    _CucsNfsMountInstFsmStageName_Type()
)
cucsNfsMountInstFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStageName.setStatus("current")
_CucsNfsMountInstFsmStageOrder_Type = Gauge32
_CucsNfsMountInstFsmStageOrder_Object = MibTableColumn
cucsNfsMountInstFsmStageOrder = _CucsNfsMountInstFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 8, 1, 7),
    _CucsNfsMountInstFsmStageOrder_Type()
)
cucsNfsMountInstFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStageOrder.setStatus("current")
_CucsNfsMountInstFsmStageRetry_Type = Gauge32
_CucsNfsMountInstFsmStageRetry_Object = MibTableColumn
cucsNfsMountInstFsmStageRetry = _CucsNfsMountInstFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 8, 1, 8),
    _CucsNfsMountInstFsmStageRetry_Type()
)
cucsNfsMountInstFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStageRetry.setStatus("current")
_CucsNfsMountInstFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsNfsMountInstFsmStageStageStatus_Object = MibTableColumn
cucsNfsMountInstFsmStageStageStatus = _CucsNfsMountInstFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 8, 1, 9),
    _CucsNfsMountInstFsmStageStageStatus_Type()
)
cucsNfsMountInstFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmStageStageStatus.setStatus("current")
_CucsNfsMountInstFsmTaskTable_Object = MibTable
cucsNfsMountInstFsmTaskTable = _CucsNfsMountInstFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 9)
)
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmTaskTable.setStatus("current")
_CucsNfsMountInstFsmTaskEntry_Object = MibTableRow
cucsNfsMountInstFsmTaskEntry = _CucsNfsMountInstFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 9, 1)
)
cucsNfsMountInstFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NFS-MIB", "cucsNfsMountInstFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmTaskEntry.setStatus("current")
_CucsNfsMountInstFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsNfsMountInstFsmTaskInstanceId_Object = MibTableColumn
cucsNfsMountInstFsmTaskInstanceId = _CucsNfsMountInstFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 9, 1, 1),
    _CucsNfsMountInstFsmTaskInstanceId_Type()
)
cucsNfsMountInstFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmTaskInstanceId.setStatus("current")
_CucsNfsMountInstFsmTaskDn_Type = CucsManagedObjectDn
_CucsNfsMountInstFsmTaskDn_Object = MibTableColumn
cucsNfsMountInstFsmTaskDn = _CucsNfsMountInstFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 9, 1, 2),
    _CucsNfsMountInstFsmTaskDn_Type()
)
cucsNfsMountInstFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmTaskDn.setStatus("current")
_CucsNfsMountInstFsmTaskRn_Type = SnmpAdminString
_CucsNfsMountInstFsmTaskRn_Object = MibTableColumn
cucsNfsMountInstFsmTaskRn = _CucsNfsMountInstFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 9, 1, 3),
    _CucsNfsMountInstFsmTaskRn_Type()
)
cucsNfsMountInstFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmTaskRn.setStatus("current")
_CucsNfsMountInstFsmTaskCompletion_Type = CucsFsmCompletion
_CucsNfsMountInstFsmTaskCompletion_Object = MibTableColumn
cucsNfsMountInstFsmTaskCompletion = _CucsNfsMountInstFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 9, 1, 4),
    _CucsNfsMountInstFsmTaskCompletion_Type()
)
cucsNfsMountInstFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmTaskCompletion.setStatus("current")
_CucsNfsMountInstFsmTaskFlags_Type = CucsFsmFlags
_CucsNfsMountInstFsmTaskFlags_Object = MibTableColumn
cucsNfsMountInstFsmTaskFlags = _CucsNfsMountInstFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 9, 1, 5),
    _CucsNfsMountInstFsmTaskFlags_Type()
)
cucsNfsMountInstFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmTaskFlags.setStatus("current")
_CucsNfsMountInstFsmTaskItem_Type = CucsNfsMountInstFsmTaskItem
_CucsNfsMountInstFsmTaskItem_Object = MibTableColumn
cucsNfsMountInstFsmTaskItem = _CucsNfsMountInstFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 9, 1, 6),
    _CucsNfsMountInstFsmTaskItem_Type()
)
cucsNfsMountInstFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmTaskItem.setStatus("current")
_CucsNfsMountInstFsmTaskSeqId_Type = Gauge32
_CucsNfsMountInstFsmTaskSeqId_Object = MibTableColumn
cucsNfsMountInstFsmTaskSeqId = _CucsNfsMountInstFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 67, 9, 1, 7),
    _CucsNfsMountInstFsmTaskSeqId_Type()
)
cucsNfsMountInstFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNfsMountInstFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-NFS-MIB",
    **{"cucsNfsObjects": cucsNfsObjects,
       "cucsNfsEpTable": cucsNfsEpTable,
       "cucsNfsEpEntry": cucsNfsEpEntry,
       "cucsNfsEpInstanceId": cucsNfsEpInstanceId,
       "cucsNfsEpDn": cucsNfsEpDn,
       "cucsNfsEpRn": cucsNfsEpRn,
       "cucsNfsMountDefTable": cucsNfsMountDefTable,
       "cucsNfsMountDefEntry": cucsNfsMountDefEntry,
       "cucsNfsMountDefInstanceId": cucsNfsMountDefInstanceId,
       "cucsNfsMountDefDn": cucsNfsMountDefDn,
       "cucsNfsMountDefRn": cucsNfsMountDefRn,
       "cucsNfsMountDefAdminState": cucsNfsMountDefAdminState,
       "cucsNfsMountDefDescr": cucsNfsMountDefDescr,
       "cucsNfsMountDefFltAggr": cucsNfsMountDefFltAggr,
       "cucsNfsMountDefFsmDescr": cucsNfsMountDefFsmDescr,
       "cucsNfsMountDefFsmPrev": cucsNfsMountDefFsmPrev,
       "cucsNfsMountDefFsmProgr": cucsNfsMountDefFsmProgr,
       "cucsNfsMountDefFsmRmtInvErrCode": cucsNfsMountDefFsmRmtInvErrCode,
       "cucsNfsMountDefFsmRmtInvErrDescr": cucsNfsMountDefFsmRmtInvErrDescr,
       "cucsNfsMountDefFsmRmtInvRslt": cucsNfsMountDefFsmRmtInvRslt,
       "cucsNfsMountDefFsmStageDescr": cucsNfsMountDefFsmStageDescr,
       "cucsNfsMountDefFsmStamp": cucsNfsMountDefFsmStamp,
       "cucsNfsMountDefFsmStatus": cucsNfsMountDefFsmStatus,
       "cucsNfsMountDefFsmTry": cucsNfsMountDefFsmTry,
       "cucsNfsMountDefIntId": cucsNfsMountDefIntId,
       "cucsNfsMountDefLocalDir": cucsNfsMountDefLocalDir,
       "cucsNfsMountDefName": cucsNfsMountDefName,
       "cucsNfsMountDefPolicyLevel": cucsNfsMountDefPolicyLevel,
       "cucsNfsMountDefPolicyOwner": cucsNfsMountDefPolicyOwner,
       "cucsNfsMountDefPurpose": cucsNfsMountDefPurpose,
       "cucsNfsMountDefRemoteDir": cucsNfsMountDefRemoteDir,
       "cucsNfsMountDefServer": cucsNfsMountDefServer,
       "cucsNfsMountDefFsmTable": cucsNfsMountDefFsmTable,
       "cucsNfsMountDefFsmEntry": cucsNfsMountDefFsmEntry,
       "cucsNfsMountDefFsmInstanceId": cucsNfsMountDefFsmInstanceId,
       "cucsNfsMountDefFsmDn": cucsNfsMountDefFsmDn,
       "cucsNfsMountDefFsmRn": cucsNfsMountDefFsmRn,
       "cucsNfsMountDefFsmCompletionTime": cucsNfsMountDefFsmCompletionTime,
       "cucsNfsMountDefFsmCurrentFsm": cucsNfsMountDefFsmCurrentFsm,
       "cucsNfsMountDefFsmDescrData": cucsNfsMountDefFsmDescrData,
       "cucsNfsMountDefFsmFsmStatus": cucsNfsMountDefFsmFsmStatus,
       "cucsNfsMountDefFsmProgress": cucsNfsMountDefFsmProgress,
       "cucsNfsMountDefFsmRmtErrCode": cucsNfsMountDefFsmRmtErrCode,
       "cucsNfsMountDefFsmRmtErrDescr": cucsNfsMountDefFsmRmtErrDescr,
       "cucsNfsMountDefFsmRmtRslt": cucsNfsMountDefFsmRmtRslt,
       "cucsNfsMountDefFsmStageTable": cucsNfsMountDefFsmStageTable,
       "cucsNfsMountDefFsmStageEntry": cucsNfsMountDefFsmStageEntry,
       "cucsNfsMountDefFsmStageInstanceId": cucsNfsMountDefFsmStageInstanceId,
       "cucsNfsMountDefFsmStageDn": cucsNfsMountDefFsmStageDn,
       "cucsNfsMountDefFsmStageRn": cucsNfsMountDefFsmStageRn,
       "cucsNfsMountDefFsmStageDescrData": cucsNfsMountDefFsmStageDescrData,
       "cucsNfsMountDefFsmStageLastUpdateTime": cucsNfsMountDefFsmStageLastUpdateTime,
       "cucsNfsMountDefFsmStageName": cucsNfsMountDefFsmStageName,
       "cucsNfsMountDefFsmStageOrder": cucsNfsMountDefFsmStageOrder,
       "cucsNfsMountDefFsmStageRetry": cucsNfsMountDefFsmStageRetry,
       "cucsNfsMountDefFsmStageStageStatus": cucsNfsMountDefFsmStageStageStatus,
       "cucsNfsMountDefFsmTaskTable": cucsNfsMountDefFsmTaskTable,
       "cucsNfsMountDefFsmTaskEntry": cucsNfsMountDefFsmTaskEntry,
       "cucsNfsMountDefFsmTaskInstanceId": cucsNfsMountDefFsmTaskInstanceId,
       "cucsNfsMountDefFsmTaskDn": cucsNfsMountDefFsmTaskDn,
       "cucsNfsMountDefFsmTaskRn": cucsNfsMountDefFsmTaskRn,
       "cucsNfsMountDefFsmTaskCompletion": cucsNfsMountDefFsmTaskCompletion,
       "cucsNfsMountDefFsmTaskFlags": cucsNfsMountDefFsmTaskFlags,
       "cucsNfsMountDefFsmTaskItem": cucsNfsMountDefFsmTaskItem,
       "cucsNfsMountDefFsmTaskSeqId": cucsNfsMountDefFsmTaskSeqId,
       "cucsNfsMountInstTable": cucsNfsMountInstTable,
       "cucsNfsMountInstEntry": cucsNfsMountInstEntry,
       "cucsNfsMountInstInstanceId": cucsNfsMountInstInstanceId,
       "cucsNfsMountInstDn": cucsNfsMountInstDn,
       "cucsNfsMountInstRn": cucsNfsMountInstRn,
       "cucsNfsMountInstAdminState": cucsNfsMountInstAdminState,
       "cucsNfsMountInstClientConfigState": cucsNfsMountInstClientConfigState,
       "cucsNfsMountInstDefDn": cucsNfsMountInstDefDn,
       "cucsNfsMountInstFsmDescr": cucsNfsMountInstFsmDescr,
       "cucsNfsMountInstFsmPrev": cucsNfsMountInstFsmPrev,
       "cucsNfsMountInstFsmProgr": cucsNfsMountInstFsmProgr,
       "cucsNfsMountInstFsmRmtInvErrCode": cucsNfsMountInstFsmRmtInvErrCode,
       "cucsNfsMountInstFsmRmtInvErrDescr": cucsNfsMountInstFsmRmtInvErrDescr,
       "cucsNfsMountInstFsmRmtInvRslt": cucsNfsMountInstFsmRmtInvRslt,
       "cucsNfsMountInstFsmStageDescr": cucsNfsMountInstFsmStageDescr,
       "cucsNfsMountInstFsmStamp": cucsNfsMountInstFsmStamp,
       "cucsNfsMountInstFsmStatus": cucsNfsMountInstFsmStatus,
       "cucsNfsMountInstFsmTry": cucsNfsMountInstFsmTry,
       "cucsNfsMountInstLocalDir": cucsNfsMountInstLocalDir,
       "cucsNfsMountInstName": cucsNfsMountInstName,
       "cucsNfsMountInstOperState": cucsNfsMountInstOperState,
       "cucsNfsMountInstPurpose": cucsNfsMountInstPurpose,
       "cucsNfsMountInstRemoteDir": cucsNfsMountInstRemoteDir,
       "cucsNfsMountInstServer": cucsNfsMountInstServer,
       "cucsNfsMountInstFsmTable": cucsNfsMountInstFsmTable,
       "cucsNfsMountInstFsmEntry": cucsNfsMountInstFsmEntry,
       "cucsNfsMountInstFsmInstanceId": cucsNfsMountInstFsmInstanceId,
       "cucsNfsMountInstFsmDn": cucsNfsMountInstFsmDn,
       "cucsNfsMountInstFsmRn": cucsNfsMountInstFsmRn,
       "cucsNfsMountInstFsmCompletionTime": cucsNfsMountInstFsmCompletionTime,
       "cucsNfsMountInstFsmCurrentFsm": cucsNfsMountInstFsmCurrentFsm,
       "cucsNfsMountInstFsmDescrData": cucsNfsMountInstFsmDescrData,
       "cucsNfsMountInstFsmFsmStatus": cucsNfsMountInstFsmFsmStatus,
       "cucsNfsMountInstFsmProgress": cucsNfsMountInstFsmProgress,
       "cucsNfsMountInstFsmRmtErrCode": cucsNfsMountInstFsmRmtErrCode,
       "cucsNfsMountInstFsmRmtErrDescr": cucsNfsMountInstFsmRmtErrDescr,
       "cucsNfsMountInstFsmRmtRslt": cucsNfsMountInstFsmRmtRslt,
       "cucsNfsMountInstFsmStageTable": cucsNfsMountInstFsmStageTable,
       "cucsNfsMountInstFsmStageEntry": cucsNfsMountInstFsmStageEntry,
       "cucsNfsMountInstFsmStageInstanceId": cucsNfsMountInstFsmStageInstanceId,
       "cucsNfsMountInstFsmStageDn": cucsNfsMountInstFsmStageDn,
       "cucsNfsMountInstFsmStageRn": cucsNfsMountInstFsmStageRn,
       "cucsNfsMountInstFsmStageDescrData": cucsNfsMountInstFsmStageDescrData,
       "cucsNfsMountInstFsmStageLastUpdateTime": cucsNfsMountInstFsmStageLastUpdateTime,
       "cucsNfsMountInstFsmStageName": cucsNfsMountInstFsmStageName,
       "cucsNfsMountInstFsmStageOrder": cucsNfsMountInstFsmStageOrder,
       "cucsNfsMountInstFsmStageRetry": cucsNfsMountInstFsmStageRetry,
       "cucsNfsMountInstFsmStageStageStatus": cucsNfsMountInstFsmStageStageStatus,
       "cucsNfsMountInstFsmTaskTable": cucsNfsMountInstFsmTaskTable,
       "cucsNfsMountInstFsmTaskEntry": cucsNfsMountInstFsmTaskEntry,
       "cucsNfsMountInstFsmTaskInstanceId": cucsNfsMountInstFsmTaskInstanceId,
       "cucsNfsMountInstFsmTaskDn": cucsNfsMountInstFsmTaskDn,
       "cucsNfsMountInstFsmTaskRn": cucsNfsMountInstFsmTaskRn,
       "cucsNfsMountInstFsmTaskCompletion": cucsNfsMountInstFsmTaskCompletion,
       "cucsNfsMountInstFsmTaskFlags": cucsNfsMountInstFsmTaskFlags,
       "cucsNfsMountInstFsmTaskItem": cucsNfsMountInstFsmTaskItem,
       "cucsNfsMountInstFsmTaskSeqId": cucsNfsMountInstFsmTaskSeqId}
)
