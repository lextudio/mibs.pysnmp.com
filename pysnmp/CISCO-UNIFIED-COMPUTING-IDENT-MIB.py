# SNMP MIB module (CISCO-UNIFIED-COMPUTING-IDENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-IDENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:40 2024
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
 CucsIdentConsType,
 CucsIdentIdDefinedInIdm,
 CucsIdentIdentReqIntent,
 CucsIdentIdentRequestFsmCurrentFsm,
 CucsIdentIdentRequestFsmStageName,
 CucsIdentIdentRequestFsmTaskItem,
 CucsIdentIdentType,
 CucsIdentMetaSystemFsmCurrentFsm,
 CucsIdentMetaSystemFsmStageName,
 CucsIdentMetaSystemFsmTaskItem,
 CucsIdentRetStatus) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsIdentConsType",
    "CucsIdentIdDefinedInIdm",
    "CucsIdentIdentReqIntent",
    "CucsIdentIdentRequestFsmCurrentFsm",
    "CucsIdentIdentRequestFsmStageName",
    "CucsIdentIdentRequestFsmTaskItem",
    "CucsIdentIdentType",
    "CucsIdentMetaSystemFsmCurrentFsm",
    "CucsIdentMetaSystemFsmStageName",
    "CucsIdentMetaSystemFsmTaskItem",
    "CucsIdentRetStatus")

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

cucsIdentObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsIdentIdentCtxTable_Object = MibTable
cucsIdentIdentCtxTable = _CucsIdentIdentCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1)
)
if mibBuilder.loadTexts:
    cucsIdentIdentCtxTable.setStatus("current")
_CucsIdentIdentCtxEntry_Object = MibTableRow
cucsIdentIdentCtxEntry = _CucsIdentIdentCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1)
)
cucsIdentIdentCtxEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IDENT-MIB", "cucsIdentIdentCtxInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIdentIdentCtxEntry.setStatus("current")
_CucsIdentIdentCtxInstanceId_Type = CucsManagedObjectId
_CucsIdentIdentCtxInstanceId_Object = MibTableColumn
cucsIdentIdentCtxInstanceId = _CucsIdentIdentCtxInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 1),
    _CucsIdentIdentCtxInstanceId_Type()
)
cucsIdentIdentCtxInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxInstanceId.setStatus("current")
_CucsIdentIdentCtxDn_Type = CucsManagedObjectDn
_CucsIdentIdentCtxDn_Object = MibTableColumn
cucsIdentIdentCtxDn = _CucsIdentIdentCtxDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 2),
    _CucsIdentIdentCtxDn_Type()
)
cucsIdentIdentCtxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxDn.setStatus("current")
_CucsIdentIdentCtxRn_Type = SnmpAdminString
_CucsIdentIdentCtxRn_Object = MibTableColumn
cucsIdentIdentCtxRn = _CucsIdentIdentCtxRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 3),
    _CucsIdentIdentCtxRn_Type()
)
cucsIdentIdentCtxRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxRn.setStatus("current")
_CucsIdentIdentCtxAssigned_Type = SnmpAdminString
_CucsIdentIdentCtxAssigned_Object = MibTableColumn
cucsIdentIdentCtxAssigned = _CucsIdentIdentCtxAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 4),
    _CucsIdentIdentCtxAssigned_Type()
)
cucsIdentIdentCtxAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxAssigned.setStatus("current")
_CucsIdentIdentCtxConsDn_Type = SnmpAdminString
_CucsIdentIdentCtxConsDn_Object = MibTableColumn
cucsIdentIdentCtxConsDn = _CucsIdentIdentCtxConsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 5),
    _CucsIdentIdentCtxConsDn_Type()
)
cucsIdentIdentCtxConsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxConsDn.setStatus("current")
_CucsIdentIdentCtxConsType_Type = CucsIdentConsType
_CucsIdentIdentCtxConsType_Object = MibTableColumn
cucsIdentIdentCtxConsType = _CucsIdentIdentCtxConsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 6),
    _CucsIdentIdentCtxConsType_Type()
)
cucsIdentIdentCtxConsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxConsType.setStatus("current")
_CucsIdentIdentCtxDefinedInIdm_Type = CucsIdentIdDefinedInIdm
_CucsIdentIdentCtxDefinedInIdm_Object = MibTableColumn
cucsIdentIdentCtxDefinedInIdm = _CucsIdentIdentCtxDefinedInIdm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 7),
    _CucsIdentIdentCtxDefinedInIdm_Type()
)
cucsIdentIdentCtxDefinedInIdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxDefinedInIdm.setStatus("current")
_CucsIdentIdentCtxIdentPoolName_Type = SnmpAdminString
_CucsIdentIdentCtxIdentPoolName_Object = MibTableColumn
cucsIdentIdentCtxIdentPoolName = _CucsIdentIdentCtxIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 8),
    _CucsIdentIdentCtxIdentPoolName_Type()
)
cucsIdentIdentCtxIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxIdentPoolName.setStatus("current")
_CucsIdentIdentCtxIdentType_Type = CucsIdentIdentType
_CucsIdentIdentCtxIdentType_Object = MibTableColumn
cucsIdentIdentCtxIdentType = _CucsIdentIdentCtxIdentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 9),
    _CucsIdentIdentCtxIdentType_Type()
)
cucsIdentIdentCtxIdentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxIdentType.setStatus("current")
_CucsIdentIdentCtxIntent_Type = CucsIdentIdentReqIntent
_CucsIdentIdentCtxIntent_Object = MibTableColumn
cucsIdentIdentCtxIntent = _CucsIdentIdentCtxIntent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 10),
    _CucsIdentIdentCtxIntent_Type()
)
cucsIdentIdentCtxIntent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxIntent.setStatus("current")
_CucsIdentIdentCtxPoolDn_Type = SnmpAdminString
_CucsIdentIdentCtxPoolDn_Object = MibTableColumn
cucsIdentIdentCtxPoolDn = _CucsIdentIdentCtxPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 11),
    _CucsIdentIdentCtxPoolDn_Type()
)
cucsIdentIdentCtxPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxPoolDn.setStatus("current")
_CucsIdentIdentCtxPoolOrgDn_Type = SnmpAdminString
_CucsIdentIdentCtxPoolOrgDn_Object = MibTableColumn
cucsIdentIdentCtxPoolOrgDn = _CucsIdentIdentCtxPoolOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 12),
    _CucsIdentIdentCtxPoolOrgDn_Type()
)
cucsIdentIdentCtxPoolOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxPoolOrgDn.setStatus("current")
_CucsIdentIdentCtxPooledId_Type = Gauge32
_CucsIdentIdentCtxPooledId_Object = MibTableColumn
cucsIdentIdentCtxPooledId = _CucsIdentIdentCtxPooledId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 13),
    _CucsIdentIdentCtxPooledId_Type()
)
cucsIdentIdentCtxPooledId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxPooledId.setStatus("current")
_CucsIdentIdentCtxRetStatus_Type = CucsIdentRetStatus
_CucsIdentIdentCtxRetStatus_Object = MibTableColumn
cucsIdentIdentCtxRetStatus = _CucsIdentIdentCtxRetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 14),
    _CucsIdentIdentCtxRetStatus_Type()
)
cucsIdentIdentCtxRetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxRetStatus.setStatus("current")
_CucsIdentIdentCtxSeqNum_Type = Gauge32
_CucsIdentIdentCtxSeqNum_Object = MibTableColumn
cucsIdentIdentCtxSeqNum = _CucsIdentIdentCtxSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 15),
    _CucsIdentIdentCtxSeqNum_Type()
)
cucsIdentIdentCtxSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxSeqNum.setStatus("current")
_CucsIdentIdentCtxSupplId1_Type = SnmpAdminString
_CucsIdentIdentCtxSupplId1_Object = MibTableColumn
cucsIdentIdentCtxSupplId1 = _CucsIdentIdentCtxSupplId1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 16),
    _CucsIdentIdentCtxSupplId1_Type()
)
cucsIdentIdentCtxSupplId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxSupplId1.setStatus("current")
_CucsIdentIdentCtxSupplId2_Type = SnmpAdminString
_CucsIdentIdentCtxSupplId2_Object = MibTableColumn
cucsIdentIdentCtxSupplId2 = _CucsIdentIdentCtxSupplId2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 17),
    _CucsIdentIdentCtxSupplId2_Type()
)
cucsIdentIdentCtxSupplId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxSupplId2.setStatus("current")
_CucsIdentIdentCtxSupplId3_Type = SnmpAdminString
_CucsIdentIdentCtxSupplId3_Object = MibTableColumn
cucsIdentIdentCtxSupplId3 = _CucsIdentIdentCtxSupplId3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 18),
    _CucsIdentIdentCtxSupplId3_Type()
)
cucsIdentIdentCtxSupplId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxSupplId3.setStatus("current")
_CucsIdentIdentCtxSupplId4_Type = SnmpAdminString
_CucsIdentIdentCtxSupplId4_Object = MibTableColumn
cucsIdentIdentCtxSupplId4 = _CucsIdentIdentCtxSupplId4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 19),
    _CucsIdentIdentCtxSupplId4_Type()
)
cucsIdentIdentCtxSupplId4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxSupplId4.setStatus("current")
_CucsIdentIdentCtxGlobalAssignedCnt_Type = Gauge32
_CucsIdentIdentCtxGlobalAssignedCnt_Object = MibTableColumn
cucsIdentIdentCtxGlobalAssignedCnt = _CucsIdentIdentCtxGlobalAssignedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 20),
    _CucsIdentIdentCtxGlobalAssignedCnt_Type()
)
cucsIdentIdentCtxGlobalAssignedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxGlobalAssignedCnt.setStatus("current")
_CucsIdentIdentCtxGlobalDefinedCnt_Type = Gauge32
_CucsIdentIdentCtxGlobalDefinedCnt_Object = MibTableColumn
cucsIdentIdentCtxGlobalDefinedCnt = _CucsIdentIdentCtxGlobalDefinedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 21),
    _CucsIdentIdentCtxGlobalDefinedCnt_Type()
)
cucsIdentIdentCtxGlobalDefinedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxGlobalDefinedCnt.setStatus("current")
_CucsIdentIdentCtxIsAssignedLocally_Type = TruthValue
_CucsIdentIdentCtxIsAssignedLocally_Object = MibTableColumn
cucsIdentIdentCtxIsAssignedLocally = _CucsIdentIdentCtxIsAssignedLocally_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 1, 1, 22),
    _CucsIdentIdentCtxIsAssignedLocally_Type()
)
cucsIdentIdentCtxIsAssignedLocally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentCtxIsAssignedLocally.setStatus("current")
_CucsIdentIdentRequestTable_Object = MibTable
cucsIdentIdentRequestTable = _CucsIdentIdentRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2)
)
if mibBuilder.loadTexts:
    cucsIdentIdentRequestTable.setStatus("current")
_CucsIdentIdentRequestEntry_Object = MibTableRow
cucsIdentIdentRequestEntry = _CucsIdentIdentRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1)
)
cucsIdentIdentRequestEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IDENT-MIB", "cucsIdentIdentRequestInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIdentIdentRequestEntry.setStatus("current")
_CucsIdentIdentRequestInstanceId_Type = CucsManagedObjectId
_CucsIdentIdentRequestInstanceId_Object = MibTableColumn
cucsIdentIdentRequestInstanceId = _CucsIdentIdentRequestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 1),
    _CucsIdentIdentRequestInstanceId_Type()
)
cucsIdentIdentRequestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestInstanceId.setStatus("current")
_CucsIdentIdentRequestDn_Type = CucsManagedObjectDn
_CucsIdentIdentRequestDn_Object = MibTableColumn
cucsIdentIdentRequestDn = _CucsIdentIdentRequestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 2),
    _CucsIdentIdentRequestDn_Type()
)
cucsIdentIdentRequestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestDn.setStatus("current")
_CucsIdentIdentRequestRn_Type = SnmpAdminString
_CucsIdentIdentRequestRn_Object = MibTableColumn
cucsIdentIdentRequestRn = _CucsIdentIdentRequestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 3),
    _CucsIdentIdentRequestRn_Type()
)
cucsIdentIdentRequestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestRn.setStatus("current")
_CucsIdentIdentRequestEpDn_Type = SnmpAdminString
_CucsIdentIdentRequestEpDn_Object = MibTableColumn
cucsIdentIdentRequestEpDn = _CucsIdentIdentRequestEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 4),
    _CucsIdentIdentRequestEpDn_Type()
)
cucsIdentIdentRequestEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestEpDn.setStatus("current")
_CucsIdentIdentRequestFsmDescr_Type = SnmpAdminString
_CucsIdentIdentRequestFsmDescr_Object = MibTableColumn
cucsIdentIdentRequestFsmDescr = _CucsIdentIdentRequestFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 5),
    _CucsIdentIdentRequestFsmDescr_Type()
)
cucsIdentIdentRequestFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmDescr.setStatus("current")
_CucsIdentIdentRequestFsmPrev_Type = SnmpAdminString
_CucsIdentIdentRequestFsmPrev_Object = MibTableColumn
cucsIdentIdentRequestFsmPrev = _CucsIdentIdentRequestFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 6),
    _CucsIdentIdentRequestFsmPrev_Type()
)
cucsIdentIdentRequestFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmPrev.setStatus("current")
_CucsIdentIdentRequestFsmProgr_Type = Gauge32
_CucsIdentIdentRequestFsmProgr_Object = MibTableColumn
cucsIdentIdentRequestFsmProgr = _CucsIdentIdentRequestFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 7),
    _CucsIdentIdentRequestFsmProgr_Type()
)
cucsIdentIdentRequestFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmProgr.setStatus("current")
_CucsIdentIdentRequestFsmRmtInvErrCode_Type = Gauge32
_CucsIdentIdentRequestFsmRmtInvErrCode_Object = MibTableColumn
cucsIdentIdentRequestFsmRmtInvErrCode = _CucsIdentIdentRequestFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 8),
    _CucsIdentIdentRequestFsmRmtInvErrCode_Type()
)
cucsIdentIdentRequestFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmRmtInvErrCode.setStatus("current")
_CucsIdentIdentRequestFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsIdentIdentRequestFsmRmtInvErrDescr_Object = MibTableColumn
cucsIdentIdentRequestFsmRmtInvErrDescr = _CucsIdentIdentRequestFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 9),
    _CucsIdentIdentRequestFsmRmtInvErrDescr_Type()
)
cucsIdentIdentRequestFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmRmtInvErrDescr.setStatus("current")
_CucsIdentIdentRequestFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsIdentIdentRequestFsmRmtInvRslt_Object = MibTableColumn
cucsIdentIdentRequestFsmRmtInvRslt = _CucsIdentIdentRequestFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 10),
    _CucsIdentIdentRequestFsmRmtInvRslt_Type()
)
cucsIdentIdentRequestFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmRmtInvRslt.setStatus("current")
_CucsIdentIdentRequestFsmStageDescr_Type = SnmpAdminString
_CucsIdentIdentRequestFsmStageDescr_Object = MibTableColumn
cucsIdentIdentRequestFsmStageDescr = _CucsIdentIdentRequestFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 11),
    _CucsIdentIdentRequestFsmStageDescr_Type()
)
cucsIdentIdentRequestFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStageDescr.setStatus("current")
_CucsIdentIdentRequestFsmStamp_Type = DateAndTime
_CucsIdentIdentRequestFsmStamp_Object = MibTableColumn
cucsIdentIdentRequestFsmStamp = _CucsIdentIdentRequestFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 12),
    _CucsIdentIdentRequestFsmStamp_Type()
)
cucsIdentIdentRequestFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStamp.setStatus("current")
_CucsIdentIdentRequestFsmStatus_Type = SnmpAdminString
_CucsIdentIdentRequestFsmStatus_Object = MibTableColumn
cucsIdentIdentRequestFsmStatus = _CucsIdentIdentRequestFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 13),
    _CucsIdentIdentRequestFsmStatus_Type()
)
cucsIdentIdentRequestFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStatus.setStatus("current")
_CucsIdentIdentRequestFsmTry_Type = Gauge32
_CucsIdentIdentRequestFsmTry_Object = MibTableColumn
cucsIdentIdentRequestFsmTry = _CucsIdentIdentRequestFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 14),
    _CucsIdentIdentRequestFsmTry_Type()
)
cucsIdentIdentRequestFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmTry.setStatus("current")
_CucsIdentIdentRequestId_Type = Gauge32
_CucsIdentIdentRequestId_Object = MibTableColumn
cucsIdentIdentRequestId = _CucsIdentIdentRequestId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 15),
    _CucsIdentIdentRequestId_Type()
)
cucsIdentIdentRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestId.setStatus("current")
_CucsIdentIdentRequestRequestSize_Type = Gauge32
_CucsIdentIdentRequestRequestSize_Object = MibTableColumn
cucsIdentIdentRequestRequestSize = _CucsIdentIdentRequestRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 16),
    _CucsIdentIdentRequestRequestSize_Type()
)
cucsIdentIdentRequestRequestSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestRequestSize.setStatus("current")
_CucsIdentIdentRequestSeqNum_Type = Gauge32
_CucsIdentIdentRequestSeqNum_Object = MibTableColumn
cucsIdentIdentRequestSeqNum = _CucsIdentIdentRequestSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 2, 1, 17),
    _CucsIdentIdentRequestSeqNum_Type()
)
cucsIdentIdentRequestSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestSeqNum.setStatus("current")
_CucsIdentIdentRequestFsmTable_Object = MibTable
cucsIdentIdentRequestFsmTable = _CucsIdentIdentRequestFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3)
)
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmTable.setStatus("current")
_CucsIdentIdentRequestFsmEntry_Object = MibTableRow
cucsIdentIdentRequestFsmEntry = _CucsIdentIdentRequestFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3, 1)
)
cucsIdentIdentRequestFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IDENT-MIB", "cucsIdentIdentRequestFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmEntry.setStatus("current")
_CucsIdentIdentRequestFsmInstanceId_Type = CucsManagedObjectId
_CucsIdentIdentRequestFsmInstanceId_Object = MibTableColumn
cucsIdentIdentRequestFsmInstanceId = _CucsIdentIdentRequestFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3, 1, 1),
    _CucsIdentIdentRequestFsmInstanceId_Type()
)
cucsIdentIdentRequestFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmInstanceId.setStatus("current")
_CucsIdentIdentRequestFsmDn_Type = CucsManagedObjectDn
_CucsIdentIdentRequestFsmDn_Object = MibTableColumn
cucsIdentIdentRequestFsmDn = _CucsIdentIdentRequestFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3, 1, 2),
    _CucsIdentIdentRequestFsmDn_Type()
)
cucsIdentIdentRequestFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmDn.setStatus("current")
_CucsIdentIdentRequestFsmRn_Type = SnmpAdminString
_CucsIdentIdentRequestFsmRn_Object = MibTableColumn
cucsIdentIdentRequestFsmRn = _CucsIdentIdentRequestFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3, 1, 3),
    _CucsIdentIdentRequestFsmRn_Type()
)
cucsIdentIdentRequestFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmRn.setStatus("current")
_CucsIdentIdentRequestFsmCompletionTime_Type = DateAndTime
_CucsIdentIdentRequestFsmCompletionTime_Object = MibTableColumn
cucsIdentIdentRequestFsmCompletionTime = _CucsIdentIdentRequestFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3, 1, 4),
    _CucsIdentIdentRequestFsmCompletionTime_Type()
)
cucsIdentIdentRequestFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmCompletionTime.setStatus("current")
_CucsIdentIdentRequestFsmCurrentFsm_Type = CucsIdentIdentRequestFsmCurrentFsm
_CucsIdentIdentRequestFsmCurrentFsm_Object = MibTableColumn
cucsIdentIdentRequestFsmCurrentFsm = _CucsIdentIdentRequestFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3, 1, 5),
    _CucsIdentIdentRequestFsmCurrentFsm_Type()
)
cucsIdentIdentRequestFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmCurrentFsm.setStatus("current")
_CucsIdentIdentRequestFsmDescrData_Type = SnmpAdminString
_CucsIdentIdentRequestFsmDescrData_Object = MibTableColumn
cucsIdentIdentRequestFsmDescrData = _CucsIdentIdentRequestFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3, 1, 6),
    _CucsIdentIdentRequestFsmDescrData_Type()
)
cucsIdentIdentRequestFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmDescrData.setStatus("current")
_CucsIdentIdentRequestFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsIdentIdentRequestFsmFsmStatus_Object = MibTableColumn
cucsIdentIdentRequestFsmFsmStatus = _CucsIdentIdentRequestFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3, 1, 7),
    _CucsIdentIdentRequestFsmFsmStatus_Type()
)
cucsIdentIdentRequestFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmFsmStatus.setStatus("current")
_CucsIdentIdentRequestFsmProgress_Type = Gauge32
_CucsIdentIdentRequestFsmProgress_Object = MibTableColumn
cucsIdentIdentRequestFsmProgress = _CucsIdentIdentRequestFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3, 1, 8),
    _CucsIdentIdentRequestFsmProgress_Type()
)
cucsIdentIdentRequestFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmProgress.setStatus("current")
_CucsIdentIdentRequestFsmRmtErrCode_Type = Gauge32
_CucsIdentIdentRequestFsmRmtErrCode_Object = MibTableColumn
cucsIdentIdentRequestFsmRmtErrCode = _CucsIdentIdentRequestFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3, 1, 9),
    _CucsIdentIdentRequestFsmRmtErrCode_Type()
)
cucsIdentIdentRequestFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmRmtErrCode.setStatus("current")
_CucsIdentIdentRequestFsmRmtErrDescr_Type = SnmpAdminString
_CucsIdentIdentRequestFsmRmtErrDescr_Object = MibTableColumn
cucsIdentIdentRequestFsmRmtErrDescr = _CucsIdentIdentRequestFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3, 1, 10),
    _CucsIdentIdentRequestFsmRmtErrDescr_Type()
)
cucsIdentIdentRequestFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmRmtErrDescr.setStatus("current")
_CucsIdentIdentRequestFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsIdentIdentRequestFsmRmtRslt_Object = MibTableColumn
cucsIdentIdentRequestFsmRmtRslt = _CucsIdentIdentRequestFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 3, 1, 11),
    _CucsIdentIdentRequestFsmRmtRslt_Type()
)
cucsIdentIdentRequestFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmRmtRslt.setStatus("current")
_CucsIdentIdentRequestFsmStageTable_Object = MibTable
cucsIdentIdentRequestFsmStageTable = _CucsIdentIdentRequestFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 4)
)
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStageTable.setStatus("current")
_CucsIdentIdentRequestFsmStageEntry_Object = MibTableRow
cucsIdentIdentRequestFsmStageEntry = _CucsIdentIdentRequestFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 4, 1)
)
cucsIdentIdentRequestFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IDENT-MIB", "cucsIdentIdentRequestFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStageEntry.setStatus("current")
_CucsIdentIdentRequestFsmStageInstanceId_Type = CucsManagedObjectId
_CucsIdentIdentRequestFsmStageInstanceId_Object = MibTableColumn
cucsIdentIdentRequestFsmStageInstanceId = _CucsIdentIdentRequestFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 4, 1, 1),
    _CucsIdentIdentRequestFsmStageInstanceId_Type()
)
cucsIdentIdentRequestFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStageInstanceId.setStatus("current")
_CucsIdentIdentRequestFsmStageDn_Type = CucsManagedObjectDn
_CucsIdentIdentRequestFsmStageDn_Object = MibTableColumn
cucsIdentIdentRequestFsmStageDn = _CucsIdentIdentRequestFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 4, 1, 2),
    _CucsIdentIdentRequestFsmStageDn_Type()
)
cucsIdentIdentRequestFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStageDn.setStatus("current")
_CucsIdentIdentRequestFsmStageRn_Type = SnmpAdminString
_CucsIdentIdentRequestFsmStageRn_Object = MibTableColumn
cucsIdentIdentRequestFsmStageRn = _CucsIdentIdentRequestFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 4, 1, 3),
    _CucsIdentIdentRequestFsmStageRn_Type()
)
cucsIdentIdentRequestFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStageRn.setStatus("current")
_CucsIdentIdentRequestFsmStageDescrData_Type = SnmpAdminString
_CucsIdentIdentRequestFsmStageDescrData_Object = MibTableColumn
cucsIdentIdentRequestFsmStageDescrData = _CucsIdentIdentRequestFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 4, 1, 4),
    _CucsIdentIdentRequestFsmStageDescrData_Type()
)
cucsIdentIdentRequestFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStageDescrData.setStatus("current")
_CucsIdentIdentRequestFsmStageLastUpdateTime_Type = DateAndTime
_CucsIdentIdentRequestFsmStageLastUpdateTime_Object = MibTableColumn
cucsIdentIdentRequestFsmStageLastUpdateTime = _CucsIdentIdentRequestFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 4, 1, 5),
    _CucsIdentIdentRequestFsmStageLastUpdateTime_Type()
)
cucsIdentIdentRequestFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStageLastUpdateTime.setStatus("current")
_CucsIdentIdentRequestFsmStageName_Type = CucsIdentIdentRequestFsmStageName
_CucsIdentIdentRequestFsmStageName_Object = MibTableColumn
cucsIdentIdentRequestFsmStageName = _CucsIdentIdentRequestFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 4, 1, 6),
    _CucsIdentIdentRequestFsmStageName_Type()
)
cucsIdentIdentRequestFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStageName.setStatus("current")
_CucsIdentIdentRequestFsmStageOrder_Type = Gauge32
_CucsIdentIdentRequestFsmStageOrder_Object = MibTableColumn
cucsIdentIdentRequestFsmStageOrder = _CucsIdentIdentRequestFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 4, 1, 7),
    _CucsIdentIdentRequestFsmStageOrder_Type()
)
cucsIdentIdentRequestFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStageOrder.setStatus("current")
_CucsIdentIdentRequestFsmStageRetry_Type = Gauge32
_CucsIdentIdentRequestFsmStageRetry_Object = MibTableColumn
cucsIdentIdentRequestFsmStageRetry = _CucsIdentIdentRequestFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 4, 1, 8),
    _CucsIdentIdentRequestFsmStageRetry_Type()
)
cucsIdentIdentRequestFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStageRetry.setStatus("current")
_CucsIdentIdentRequestFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsIdentIdentRequestFsmStageStageStatus_Object = MibTableColumn
cucsIdentIdentRequestFsmStageStageStatus = _CucsIdentIdentRequestFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 4, 1, 9),
    _CucsIdentIdentRequestFsmStageStageStatus_Type()
)
cucsIdentIdentRequestFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmStageStageStatus.setStatus("current")
_CucsIdentIdentRequestFsmTaskTable_Object = MibTable
cucsIdentIdentRequestFsmTaskTable = _CucsIdentIdentRequestFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 5)
)
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmTaskTable.setStatus("current")
_CucsIdentIdentRequestFsmTaskEntry_Object = MibTableRow
cucsIdentIdentRequestFsmTaskEntry = _CucsIdentIdentRequestFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 5, 1)
)
cucsIdentIdentRequestFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IDENT-MIB", "cucsIdentIdentRequestFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmTaskEntry.setStatus("current")
_CucsIdentIdentRequestFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsIdentIdentRequestFsmTaskInstanceId_Object = MibTableColumn
cucsIdentIdentRequestFsmTaskInstanceId = _CucsIdentIdentRequestFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 5, 1, 1),
    _CucsIdentIdentRequestFsmTaskInstanceId_Type()
)
cucsIdentIdentRequestFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmTaskInstanceId.setStatus("current")
_CucsIdentIdentRequestFsmTaskDn_Type = CucsManagedObjectDn
_CucsIdentIdentRequestFsmTaskDn_Object = MibTableColumn
cucsIdentIdentRequestFsmTaskDn = _CucsIdentIdentRequestFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 5, 1, 2),
    _CucsIdentIdentRequestFsmTaskDn_Type()
)
cucsIdentIdentRequestFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmTaskDn.setStatus("current")
_CucsIdentIdentRequestFsmTaskRn_Type = SnmpAdminString
_CucsIdentIdentRequestFsmTaskRn_Object = MibTableColumn
cucsIdentIdentRequestFsmTaskRn = _CucsIdentIdentRequestFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 5, 1, 3),
    _CucsIdentIdentRequestFsmTaskRn_Type()
)
cucsIdentIdentRequestFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmTaskRn.setStatus("current")
_CucsIdentIdentRequestFsmTaskCompletion_Type = CucsFsmCompletion
_CucsIdentIdentRequestFsmTaskCompletion_Object = MibTableColumn
cucsIdentIdentRequestFsmTaskCompletion = _CucsIdentIdentRequestFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 5, 1, 4),
    _CucsIdentIdentRequestFsmTaskCompletion_Type()
)
cucsIdentIdentRequestFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmTaskCompletion.setStatus("current")
_CucsIdentIdentRequestFsmTaskFlags_Type = CucsFsmFlags
_CucsIdentIdentRequestFsmTaskFlags_Object = MibTableColumn
cucsIdentIdentRequestFsmTaskFlags = _CucsIdentIdentRequestFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 5, 1, 5),
    _CucsIdentIdentRequestFsmTaskFlags_Type()
)
cucsIdentIdentRequestFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmTaskFlags.setStatus("current")
_CucsIdentIdentRequestFsmTaskItem_Type = CucsIdentIdentRequestFsmTaskItem
_CucsIdentIdentRequestFsmTaskItem_Object = MibTableColumn
cucsIdentIdentRequestFsmTaskItem = _CucsIdentIdentRequestFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 5, 1, 6),
    _CucsIdentIdentRequestFsmTaskItem_Type()
)
cucsIdentIdentRequestFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmTaskItem.setStatus("current")
_CucsIdentIdentRequestFsmTaskSeqId_Type = Gauge32
_CucsIdentIdentRequestFsmTaskSeqId_Object = MibTableColumn
cucsIdentIdentRequestFsmTaskSeqId = _CucsIdentIdentRequestFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 5, 1, 7),
    _CucsIdentIdentRequestFsmTaskSeqId_Type()
)
cucsIdentIdentRequestFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentIdentRequestFsmTaskSeqId.setStatus("current")
_CucsIdentMetaSystemTable_Object = MibTable
cucsIdentMetaSystemTable = _CucsIdentMetaSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6)
)
if mibBuilder.loadTexts:
    cucsIdentMetaSystemTable.setStatus("current")
_CucsIdentMetaSystemEntry_Object = MibTableRow
cucsIdentMetaSystemEntry = _CucsIdentMetaSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1)
)
cucsIdentMetaSystemEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IDENT-MIB", "cucsIdentMetaSystemInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIdentMetaSystemEntry.setStatus("current")
_CucsIdentMetaSystemInstanceId_Type = CucsManagedObjectId
_CucsIdentMetaSystemInstanceId_Object = MibTableColumn
cucsIdentMetaSystemInstanceId = _CucsIdentMetaSystemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 1),
    _CucsIdentMetaSystemInstanceId_Type()
)
cucsIdentMetaSystemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemInstanceId.setStatus("current")
_CucsIdentMetaSystemDn_Type = CucsManagedObjectDn
_CucsIdentMetaSystemDn_Object = MibTableColumn
cucsIdentMetaSystemDn = _CucsIdentMetaSystemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 2),
    _CucsIdentMetaSystemDn_Type()
)
cucsIdentMetaSystemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemDn.setStatus("current")
_CucsIdentMetaSystemRn_Type = SnmpAdminString
_CucsIdentMetaSystemRn_Object = MibTableColumn
cucsIdentMetaSystemRn = _CucsIdentMetaSystemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 3),
    _CucsIdentMetaSystemRn_Type()
)
cucsIdentMetaSystemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemRn.setStatus("current")
_CucsIdentMetaSystemFsmDescr_Type = SnmpAdminString
_CucsIdentMetaSystemFsmDescr_Object = MibTableColumn
cucsIdentMetaSystemFsmDescr = _CucsIdentMetaSystemFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 4),
    _CucsIdentMetaSystemFsmDescr_Type()
)
cucsIdentMetaSystemFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmDescr.setStatus("current")
_CucsIdentMetaSystemFsmPrev_Type = SnmpAdminString
_CucsIdentMetaSystemFsmPrev_Object = MibTableColumn
cucsIdentMetaSystemFsmPrev = _CucsIdentMetaSystemFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 5),
    _CucsIdentMetaSystemFsmPrev_Type()
)
cucsIdentMetaSystemFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmPrev.setStatus("current")
_CucsIdentMetaSystemFsmProgr_Type = Gauge32
_CucsIdentMetaSystemFsmProgr_Object = MibTableColumn
cucsIdentMetaSystemFsmProgr = _CucsIdentMetaSystemFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 6),
    _CucsIdentMetaSystemFsmProgr_Type()
)
cucsIdentMetaSystemFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmProgr.setStatus("current")
_CucsIdentMetaSystemFsmRmtInvErrCode_Type = Gauge32
_CucsIdentMetaSystemFsmRmtInvErrCode_Object = MibTableColumn
cucsIdentMetaSystemFsmRmtInvErrCode = _CucsIdentMetaSystemFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 7),
    _CucsIdentMetaSystemFsmRmtInvErrCode_Type()
)
cucsIdentMetaSystemFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmRmtInvErrCode.setStatus("current")
_CucsIdentMetaSystemFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsIdentMetaSystemFsmRmtInvErrDescr_Object = MibTableColumn
cucsIdentMetaSystemFsmRmtInvErrDescr = _CucsIdentMetaSystemFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 8),
    _CucsIdentMetaSystemFsmRmtInvErrDescr_Type()
)
cucsIdentMetaSystemFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmRmtInvErrDescr.setStatus("current")
_CucsIdentMetaSystemFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsIdentMetaSystemFsmRmtInvRslt_Object = MibTableColumn
cucsIdentMetaSystemFsmRmtInvRslt = _CucsIdentMetaSystemFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 9),
    _CucsIdentMetaSystemFsmRmtInvRslt_Type()
)
cucsIdentMetaSystemFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmRmtInvRslt.setStatus("current")
_CucsIdentMetaSystemFsmStageDescr_Type = SnmpAdminString
_CucsIdentMetaSystemFsmStageDescr_Object = MibTableColumn
cucsIdentMetaSystemFsmStageDescr = _CucsIdentMetaSystemFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 10),
    _CucsIdentMetaSystemFsmStageDescr_Type()
)
cucsIdentMetaSystemFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStageDescr.setStatus("current")
_CucsIdentMetaSystemFsmStamp_Type = DateAndTime
_CucsIdentMetaSystemFsmStamp_Object = MibTableColumn
cucsIdentMetaSystemFsmStamp = _CucsIdentMetaSystemFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 11),
    _CucsIdentMetaSystemFsmStamp_Type()
)
cucsIdentMetaSystemFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStamp.setStatus("current")
_CucsIdentMetaSystemFsmStatus_Type = SnmpAdminString
_CucsIdentMetaSystemFsmStatus_Object = MibTableColumn
cucsIdentMetaSystemFsmStatus = _CucsIdentMetaSystemFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 12),
    _CucsIdentMetaSystemFsmStatus_Type()
)
cucsIdentMetaSystemFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStatus.setStatus("current")
_CucsIdentMetaSystemFsmTry_Type = Gauge32
_CucsIdentMetaSystemFsmTry_Object = MibTableColumn
cucsIdentMetaSystemFsmTry = _CucsIdentMetaSystemFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 13),
    _CucsIdentMetaSystemFsmTry_Type()
)
cucsIdentMetaSystemFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmTry.setStatus("current")
_CucsIdentMetaSystemGeneration_Type = Gauge32
_CucsIdentMetaSystemGeneration_Object = MibTableColumn
cucsIdentMetaSystemGeneration = _CucsIdentMetaSystemGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 14),
    _CucsIdentMetaSystemGeneration_Type()
)
cucsIdentMetaSystemGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemGeneration.setStatus("current")
_CucsIdentMetaSystemNextReqId_Type = Gauge32
_CucsIdentMetaSystemNextReqId_Object = MibTableColumn
cucsIdentMetaSystemNextReqId = _CucsIdentMetaSystemNextReqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 15),
    _CucsIdentMetaSystemNextReqId_Type()
)
cucsIdentMetaSystemNextReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemNextReqId.setStatus("current")
_CucsIdentMetaSystemSysid_Type = Gauge32
_CucsIdentMetaSystemSysid_Object = MibTableColumn
cucsIdentMetaSystemSysid = _CucsIdentMetaSystemSysid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 16),
    _CucsIdentMetaSystemSysid_Type()
)
cucsIdentMetaSystemSysid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemSysid.setStatus("current")
_CucsIdentMetaSystemUcscGeneration_Type = Gauge32
_CucsIdentMetaSystemUcscGeneration_Object = MibTableColumn
cucsIdentMetaSystemUcscGeneration = _CucsIdentMetaSystemUcscGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 6, 1, 17),
    _CucsIdentMetaSystemUcscGeneration_Type()
)
cucsIdentMetaSystemUcscGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemUcscGeneration.setStatus("current")
_CucsIdentMetaSystemFsmTable_Object = MibTable
cucsIdentMetaSystemFsmTable = _CucsIdentMetaSystemFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7)
)
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmTable.setStatus("current")
_CucsIdentMetaSystemFsmEntry_Object = MibTableRow
cucsIdentMetaSystemFsmEntry = _CucsIdentMetaSystemFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7, 1)
)
cucsIdentMetaSystemFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IDENT-MIB", "cucsIdentMetaSystemFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmEntry.setStatus("current")
_CucsIdentMetaSystemFsmInstanceId_Type = CucsManagedObjectId
_CucsIdentMetaSystemFsmInstanceId_Object = MibTableColumn
cucsIdentMetaSystemFsmInstanceId = _CucsIdentMetaSystemFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7, 1, 1),
    _CucsIdentMetaSystemFsmInstanceId_Type()
)
cucsIdentMetaSystemFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmInstanceId.setStatus("current")
_CucsIdentMetaSystemFsmDn_Type = CucsManagedObjectDn
_CucsIdentMetaSystemFsmDn_Object = MibTableColumn
cucsIdentMetaSystemFsmDn = _CucsIdentMetaSystemFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7, 1, 2),
    _CucsIdentMetaSystemFsmDn_Type()
)
cucsIdentMetaSystemFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmDn.setStatus("current")
_CucsIdentMetaSystemFsmRn_Type = SnmpAdminString
_CucsIdentMetaSystemFsmRn_Object = MibTableColumn
cucsIdentMetaSystemFsmRn = _CucsIdentMetaSystemFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7, 1, 3),
    _CucsIdentMetaSystemFsmRn_Type()
)
cucsIdentMetaSystemFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmRn.setStatus("current")
_CucsIdentMetaSystemFsmCompletionTime_Type = DateAndTime
_CucsIdentMetaSystemFsmCompletionTime_Object = MibTableColumn
cucsIdentMetaSystemFsmCompletionTime = _CucsIdentMetaSystemFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7, 1, 4),
    _CucsIdentMetaSystemFsmCompletionTime_Type()
)
cucsIdentMetaSystemFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmCompletionTime.setStatus("current")
_CucsIdentMetaSystemFsmCurrentFsm_Type = CucsIdentMetaSystemFsmCurrentFsm
_CucsIdentMetaSystemFsmCurrentFsm_Object = MibTableColumn
cucsIdentMetaSystemFsmCurrentFsm = _CucsIdentMetaSystemFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7, 1, 5),
    _CucsIdentMetaSystemFsmCurrentFsm_Type()
)
cucsIdentMetaSystemFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmCurrentFsm.setStatus("current")
_CucsIdentMetaSystemFsmDescrData_Type = SnmpAdminString
_CucsIdentMetaSystemFsmDescrData_Object = MibTableColumn
cucsIdentMetaSystemFsmDescrData = _CucsIdentMetaSystemFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7, 1, 6),
    _CucsIdentMetaSystemFsmDescrData_Type()
)
cucsIdentMetaSystemFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmDescrData.setStatus("current")
_CucsIdentMetaSystemFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsIdentMetaSystemFsmFsmStatus_Object = MibTableColumn
cucsIdentMetaSystemFsmFsmStatus = _CucsIdentMetaSystemFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7, 1, 7),
    _CucsIdentMetaSystemFsmFsmStatus_Type()
)
cucsIdentMetaSystemFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmFsmStatus.setStatus("current")
_CucsIdentMetaSystemFsmProgress_Type = Gauge32
_CucsIdentMetaSystemFsmProgress_Object = MibTableColumn
cucsIdentMetaSystemFsmProgress = _CucsIdentMetaSystemFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7, 1, 8),
    _CucsIdentMetaSystemFsmProgress_Type()
)
cucsIdentMetaSystemFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmProgress.setStatus("current")
_CucsIdentMetaSystemFsmRmtErrCode_Type = Gauge32
_CucsIdentMetaSystemFsmRmtErrCode_Object = MibTableColumn
cucsIdentMetaSystemFsmRmtErrCode = _CucsIdentMetaSystemFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7, 1, 9),
    _CucsIdentMetaSystemFsmRmtErrCode_Type()
)
cucsIdentMetaSystemFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmRmtErrCode.setStatus("current")
_CucsIdentMetaSystemFsmRmtErrDescr_Type = SnmpAdminString
_CucsIdentMetaSystemFsmRmtErrDescr_Object = MibTableColumn
cucsIdentMetaSystemFsmRmtErrDescr = _CucsIdentMetaSystemFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7, 1, 10),
    _CucsIdentMetaSystemFsmRmtErrDescr_Type()
)
cucsIdentMetaSystemFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmRmtErrDescr.setStatus("current")
_CucsIdentMetaSystemFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsIdentMetaSystemFsmRmtRslt_Object = MibTableColumn
cucsIdentMetaSystemFsmRmtRslt = _CucsIdentMetaSystemFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 7, 1, 11),
    _CucsIdentMetaSystemFsmRmtRslt_Type()
)
cucsIdentMetaSystemFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmRmtRslt.setStatus("current")
_CucsIdentMetaSystemFsmStageTable_Object = MibTable
cucsIdentMetaSystemFsmStageTable = _CucsIdentMetaSystemFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 8)
)
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStageTable.setStatus("current")
_CucsIdentMetaSystemFsmStageEntry_Object = MibTableRow
cucsIdentMetaSystemFsmStageEntry = _CucsIdentMetaSystemFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 8, 1)
)
cucsIdentMetaSystemFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IDENT-MIB", "cucsIdentMetaSystemFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStageEntry.setStatus("current")
_CucsIdentMetaSystemFsmStageInstanceId_Type = CucsManagedObjectId
_CucsIdentMetaSystemFsmStageInstanceId_Object = MibTableColumn
cucsIdentMetaSystemFsmStageInstanceId = _CucsIdentMetaSystemFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 8, 1, 1),
    _CucsIdentMetaSystemFsmStageInstanceId_Type()
)
cucsIdentMetaSystemFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStageInstanceId.setStatus("current")
_CucsIdentMetaSystemFsmStageDn_Type = CucsManagedObjectDn
_CucsIdentMetaSystemFsmStageDn_Object = MibTableColumn
cucsIdentMetaSystemFsmStageDn = _CucsIdentMetaSystemFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 8, 1, 2),
    _CucsIdentMetaSystemFsmStageDn_Type()
)
cucsIdentMetaSystemFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStageDn.setStatus("current")
_CucsIdentMetaSystemFsmStageRn_Type = SnmpAdminString
_CucsIdentMetaSystemFsmStageRn_Object = MibTableColumn
cucsIdentMetaSystemFsmStageRn = _CucsIdentMetaSystemFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 8, 1, 3),
    _CucsIdentMetaSystemFsmStageRn_Type()
)
cucsIdentMetaSystemFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStageRn.setStatus("current")
_CucsIdentMetaSystemFsmStageDescrData_Type = SnmpAdminString
_CucsIdentMetaSystemFsmStageDescrData_Object = MibTableColumn
cucsIdentMetaSystemFsmStageDescrData = _CucsIdentMetaSystemFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 8, 1, 4),
    _CucsIdentMetaSystemFsmStageDescrData_Type()
)
cucsIdentMetaSystemFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStageDescrData.setStatus("current")
_CucsIdentMetaSystemFsmStageLastUpdateTime_Type = DateAndTime
_CucsIdentMetaSystemFsmStageLastUpdateTime_Object = MibTableColumn
cucsIdentMetaSystemFsmStageLastUpdateTime = _CucsIdentMetaSystemFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 8, 1, 5),
    _CucsIdentMetaSystemFsmStageLastUpdateTime_Type()
)
cucsIdentMetaSystemFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStageLastUpdateTime.setStatus("current")
_CucsIdentMetaSystemFsmStageName_Type = CucsIdentMetaSystemFsmStageName
_CucsIdentMetaSystemFsmStageName_Object = MibTableColumn
cucsIdentMetaSystemFsmStageName = _CucsIdentMetaSystemFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 8, 1, 6),
    _CucsIdentMetaSystemFsmStageName_Type()
)
cucsIdentMetaSystemFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStageName.setStatus("current")
_CucsIdentMetaSystemFsmStageOrder_Type = Gauge32
_CucsIdentMetaSystemFsmStageOrder_Object = MibTableColumn
cucsIdentMetaSystemFsmStageOrder = _CucsIdentMetaSystemFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 8, 1, 7),
    _CucsIdentMetaSystemFsmStageOrder_Type()
)
cucsIdentMetaSystemFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStageOrder.setStatus("current")
_CucsIdentMetaSystemFsmStageRetry_Type = Gauge32
_CucsIdentMetaSystemFsmStageRetry_Object = MibTableColumn
cucsIdentMetaSystemFsmStageRetry = _CucsIdentMetaSystemFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 8, 1, 8),
    _CucsIdentMetaSystemFsmStageRetry_Type()
)
cucsIdentMetaSystemFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStageRetry.setStatus("current")
_CucsIdentMetaSystemFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsIdentMetaSystemFsmStageStageStatus_Object = MibTableColumn
cucsIdentMetaSystemFsmStageStageStatus = _CucsIdentMetaSystemFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 8, 1, 9),
    _CucsIdentMetaSystemFsmStageStageStatus_Type()
)
cucsIdentMetaSystemFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmStageStageStatus.setStatus("current")
_CucsIdentMetaSystemFsmTaskTable_Object = MibTable
cucsIdentMetaSystemFsmTaskTable = _CucsIdentMetaSystemFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 9)
)
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmTaskTable.setStatus("current")
_CucsIdentMetaSystemFsmTaskEntry_Object = MibTableRow
cucsIdentMetaSystemFsmTaskEntry = _CucsIdentMetaSystemFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 9, 1)
)
cucsIdentMetaSystemFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IDENT-MIB", "cucsIdentMetaSystemFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmTaskEntry.setStatus("current")
_CucsIdentMetaSystemFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsIdentMetaSystemFsmTaskInstanceId_Object = MibTableColumn
cucsIdentMetaSystemFsmTaskInstanceId = _CucsIdentMetaSystemFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 9, 1, 1),
    _CucsIdentMetaSystemFsmTaskInstanceId_Type()
)
cucsIdentMetaSystemFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmTaskInstanceId.setStatus("current")
_CucsIdentMetaSystemFsmTaskDn_Type = CucsManagedObjectDn
_CucsIdentMetaSystemFsmTaskDn_Object = MibTableColumn
cucsIdentMetaSystemFsmTaskDn = _CucsIdentMetaSystemFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 9, 1, 2),
    _CucsIdentMetaSystemFsmTaskDn_Type()
)
cucsIdentMetaSystemFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmTaskDn.setStatus("current")
_CucsIdentMetaSystemFsmTaskRn_Type = SnmpAdminString
_CucsIdentMetaSystemFsmTaskRn_Object = MibTableColumn
cucsIdentMetaSystemFsmTaskRn = _CucsIdentMetaSystemFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 9, 1, 3),
    _CucsIdentMetaSystemFsmTaskRn_Type()
)
cucsIdentMetaSystemFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmTaskRn.setStatus("current")
_CucsIdentMetaSystemFsmTaskCompletion_Type = CucsFsmCompletion
_CucsIdentMetaSystemFsmTaskCompletion_Object = MibTableColumn
cucsIdentMetaSystemFsmTaskCompletion = _CucsIdentMetaSystemFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 9, 1, 4),
    _CucsIdentMetaSystemFsmTaskCompletion_Type()
)
cucsIdentMetaSystemFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmTaskCompletion.setStatus("current")
_CucsIdentMetaSystemFsmTaskFlags_Type = CucsFsmFlags
_CucsIdentMetaSystemFsmTaskFlags_Object = MibTableColumn
cucsIdentMetaSystemFsmTaskFlags = _CucsIdentMetaSystemFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 9, 1, 5),
    _CucsIdentMetaSystemFsmTaskFlags_Type()
)
cucsIdentMetaSystemFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmTaskFlags.setStatus("current")
_CucsIdentMetaSystemFsmTaskItem_Type = CucsIdentMetaSystemFsmTaskItem
_CucsIdentMetaSystemFsmTaskItem_Object = MibTableColumn
cucsIdentMetaSystemFsmTaskItem = _CucsIdentMetaSystemFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 9, 1, 6),
    _CucsIdentMetaSystemFsmTaskItem_Type()
)
cucsIdentMetaSystemFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmTaskItem.setStatus("current")
_CucsIdentMetaSystemFsmTaskSeqId_Type = Gauge32
_CucsIdentMetaSystemFsmTaskSeqId_Object = MibTableColumn
cucsIdentMetaSystemFsmTaskSeqId = _CucsIdentMetaSystemFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 9, 1, 7),
    _CucsIdentMetaSystemFsmTaskSeqId_Type()
)
cucsIdentMetaSystemFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaSystemFsmTaskSeqId.setStatus("current")
_CucsIdentMetaVerseTable_Object = MibTable
cucsIdentMetaVerseTable = _CucsIdentMetaVerseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 10)
)
if mibBuilder.loadTexts:
    cucsIdentMetaVerseTable.setStatus("current")
_CucsIdentMetaVerseEntry_Object = MibTableRow
cucsIdentMetaVerseEntry = _CucsIdentMetaVerseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 10, 1)
)
cucsIdentMetaVerseEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IDENT-MIB", "cucsIdentMetaVerseInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIdentMetaVerseEntry.setStatus("current")
_CucsIdentMetaVerseInstanceId_Type = CucsManagedObjectId
_CucsIdentMetaVerseInstanceId_Object = MibTableColumn
cucsIdentMetaVerseInstanceId = _CucsIdentMetaVerseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 10, 1, 1),
    _CucsIdentMetaVerseInstanceId_Type()
)
cucsIdentMetaVerseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIdentMetaVerseInstanceId.setStatus("current")
_CucsIdentMetaVerseDn_Type = CucsManagedObjectDn
_CucsIdentMetaVerseDn_Object = MibTableColumn
cucsIdentMetaVerseDn = _CucsIdentMetaVerseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 10, 1, 2),
    _CucsIdentMetaVerseDn_Type()
)
cucsIdentMetaVerseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaVerseDn.setStatus("current")
_CucsIdentMetaVerseRn_Type = SnmpAdminString
_CucsIdentMetaVerseRn_Object = MibTableColumn
cucsIdentMetaVerseRn = _CucsIdentMetaVerseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 10, 1, 3),
    _CucsIdentMetaVerseRn_Type()
)
cucsIdentMetaVerseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentMetaVerseRn.setStatus("current")
_CucsIdentRequestEpTable_Object = MibTable
cucsIdentRequestEpTable = _CucsIdentRequestEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 11)
)
if mibBuilder.loadTexts:
    cucsIdentRequestEpTable.setStatus("current")
_CucsIdentRequestEpEntry_Object = MibTableRow
cucsIdentRequestEpEntry = _CucsIdentRequestEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 11, 1)
)
cucsIdentRequestEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IDENT-MIB", "cucsIdentRequestEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIdentRequestEpEntry.setStatus("current")
_CucsIdentRequestEpInstanceId_Type = CucsManagedObjectId
_CucsIdentRequestEpInstanceId_Object = MibTableColumn
cucsIdentRequestEpInstanceId = _CucsIdentRequestEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 11, 1, 1),
    _CucsIdentRequestEpInstanceId_Type()
)
cucsIdentRequestEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIdentRequestEpInstanceId.setStatus("current")
_CucsIdentRequestEpDn_Type = CucsManagedObjectDn
_CucsIdentRequestEpDn_Object = MibTableColumn
cucsIdentRequestEpDn = _CucsIdentRequestEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 11, 1, 2),
    _CucsIdentRequestEpDn_Type()
)
cucsIdentRequestEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentRequestEpDn.setStatus("current")
_CucsIdentRequestEpRn_Type = SnmpAdminString
_CucsIdentRequestEpRn_Object = MibTableColumn
cucsIdentRequestEpRn = _CucsIdentRequestEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 11, 1, 3),
    _CucsIdentRequestEpRn_Type()
)
cucsIdentRequestEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentRequestEpRn.setStatus("current")
_CucsIdentRequestEpReqDn_Type = SnmpAdminString
_CucsIdentRequestEpReqDn_Object = MibTableColumn
cucsIdentRequestEpReqDn = _CucsIdentRequestEpReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 11, 1, 4),
    _CucsIdentRequestEpReqDn_Type()
)
cucsIdentRequestEpReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentRequestEpReqDn.setStatus("current")
_CucsIdentRequestEpReqId_Type = Gauge32
_CucsIdentRequestEpReqId_Object = MibTableColumn
cucsIdentRequestEpReqId = _CucsIdentRequestEpReqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 11, 1, 5),
    _CucsIdentRequestEpReqId_Type()
)
cucsIdentRequestEpReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentRequestEpReqId.setStatus("current")
_CucsIdentSysInfoTable_Object = MibTable
cucsIdentSysInfoTable = _CucsIdentSysInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 12)
)
if mibBuilder.loadTexts:
    cucsIdentSysInfoTable.setStatus("current")
_CucsIdentSysInfoEntry_Object = MibTableRow
cucsIdentSysInfoEntry = _CucsIdentSysInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 12, 1)
)
cucsIdentSysInfoEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IDENT-MIB", "cucsIdentSysInfoInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIdentSysInfoEntry.setStatus("current")
_CucsIdentSysInfoInstanceId_Type = CucsManagedObjectId
_CucsIdentSysInfoInstanceId_Object = MibTableColumn
cucsIdentSysInfoInstanceId = _CucsIdentSysInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 12, 1, 1),
    _CucsIdentSysInfoInstanceId_Type()
)
cucsIdentSysInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIdentSysInfoInstanceId.setStatus("current")
_CucsIdentSysInfoDn_Type = CucsManagedObjectDn
_CucsIdentSysInfoDn_Object = MibTableColumn
cucsIdentSysInfoDn = _CucsIdentSysInfoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 12, 1, 2),
    _CucsIdentSysInfoDn_Type()
)
cucsIdentSysInfoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentSysInfoDn.setStatus("current")
_CucsIdentSysInfoRn_Type = SnmpAdminString
_CucsIdentSysInfoRn_Object = MibTableColumn
cucsIdentSysInfoRn = _CucsIdentSysInfoRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 12, 1, 3),
    _CucsIdentSysInfoRn_Type()
)
cucsIdentSysInfoRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentSysInfoRn.setStatus("current")
_CucsIdentSysInfoGeneration_Type = Gauge32
_CucsIdentSysInfoGeneration_Object = MibTableColumn
cucsIdentSysInfoGeneration = _CucsIdentSysInfoGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 12, 1, 4),
    _CucsIdentSysInfoGeneration_Type()
)
cucsIdentSysInfoGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentSysInfoGeneration.setStatus("current")
_CucsIdentSysInfoIsSync_Type = TruthValue
_CucsIdentSysInfoIsSync_Object = MibTableColumn
cucsIdentSysInfoIsSync = _CucsIdentSysInfoIsSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 12, 1, 5),
    _CucsIdentSysInfoIsSync_Type()
)
cucsIdentSysInfoIsSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentSysInfoIsSync.setStatus("current")
_CucsIdentSysInfoIsSyncAllowed_Type = TruthValue
_CucsIdentSysInfoIsSyncAllowed_Object = MibTableColumn
cucsIdentSysInfoIsSyncAllowed = _CucsIdentSysInfoIsSyncAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 12, 1, 6),
    _CucsIdentSysInfoIsSyncAllowed_Type()
)
cucsIdentSysInfoIsSyncAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentSysInfoIsSyncAllowed.setStatus("current")
_CucsIdentSysInfoIsFirstSync_Type = TruthValue
_CucsIdentSysInfoIsFirstSync_Object = MibTableColumn
cucsIdentSysInfoIsFirstSync = _CucsIdentSysInfoIsFirstSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 12, 1, 7),
    _CucsIdentSysInfoIsFirstSync_Type()
)
cucsIdentSysInfoIsFirstSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentSysInfoIsFirstSync.setStatus("current")
_CucsIdentSysInfoUcscGeneration_Type = Gauge32
_CucsIdentSysInfoUcscGeneration_Object = MibTableColumn
cucsIdentSysInfoUcscGeneration = _CucsIdentSysInfoUcscGeneration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 64, 12, 1, 8),
    _CucsIdentSysInfoUcscGeneration_Type()
)
cucsIdentSysInfoUcscGeneration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIdentSysInfoUcscGeneration.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-IDENT-MIB",
    **{"cucsIdentObjects": cucsIdentObjects,
       "cucsIdentIdentCtxTable": cucsIdentIdentCtxTable,
       "cucsIdentIdentCtxEntry": cucsIdentIdentCtxEntry,
       "cucsIdentIdentCtxInstanceId": cucsIdentIdentCtxInstanceId,
       "cucsIdentIdentCtxDn": cucsIdentIdentCtxDn,
       "cucsIdentIdentCtxRn": cucsIdentIdentCtxRn,
       "cucsIdentIdentCtxAssigned": cucsIdentIdentCtxAssigned,
       "cucsIdentIdentCtxConsDn": cucsIdentIdentCtxConsDn,
       "cucsIdentIdentCtxConsType": cucsIdentIdentCtxConsType,
       "cucsIdentIdentCtxDefinedInIdm": cucsIdentIdentCtxDefinedInIdm,
       "cucsIdentIdentCtxIdentPoolName": cucsIdentIdentCtxIdentPoolName,
       "cucsIdentIdentCtxIdentType": cucsIdentIdentCtxIdentType,
       "cucsIdentIdentCtxIntent": cucsIdentIdentCtxIntent,
       "cucsIdentIdentCtxPoolDn": cucsIdentIdentCtxPoolDn,
       "cucsIdentIdentCtxPoolOrgDn": cucsIdentIdentCtxPoolOrgDn,
       "cucsIdentIdentCtxPooledId": cucsIdentIdentCtxPooledId,
       "cucsIdentIdentCtxRetStatus": cucsIdentIdentCtxRetStatus,
       "cucsIdentIdentCtxSeqNum": cucsIdentIdentCtxSeqNum,
       "cucsIdentIdentCtxSupplId1": cucsIdentIdentCtxSupplId1,
       "cucsIdentIdentCtxSupplId2": cucsIdentIdentCtxSupplId2,
       "cucsIdentIdentCtxSupplId3": cucsIdentIdentCtxSupplId3,
       "cucsIdentIdentCtxSupplId4": cucsIdentIdentCtxSupplId4,
       "cucsIdentIdentCtxGlobalAssignedCnt": cucsIdentIdentCtxGlobalAssignedCnt,
       "cucsIdentIdentCtxGlobalDefinedCnt": cucsIdentIdentCtxGlobalDefinedCnt,
       "cucsIdentIdentCtxIsAssignedLocally": cucsIdentIdentCtxIsAssignedLocally,
       "cucsIdentIdentRequestTable": cucsIdentIdentRequestTable,
       "cucsIdentIdentRequestEntry": cucsIdentIdentRequestEntry,
       "cucsIdentIdentRequestInstanceId": cucsIdentIdentRequestInstanceId,
       "cucsIdentIdentRequestDn": cucsIdentIdentRequestDn,
       "cucsIdentIdentRequestRn": cucsIdentIdentRequestRn,
       "cucsIdentIdentRequestEpDn": cucsIdentIdentRequestEpDn,
       "cucsIdentIdentRequestFsmDescr": cucsIdentIdentRequestFsmDescr,
       "cucsIdentIdentRequestFsmPrev": cucsIdentIdentRequestFsmPrev,
       "cucsIdentIdentRequestFsmProgr": cucsIdentIdentRequestFsmProgr,
       "cucsIdentIdentRequestFsmRmtInvErrCode": cucsIdentIdentRequestFsmRmtInvErrCode,
       "cucsIdentIdentRequestFsmRmtInvErrDescr": cucsIdentIdentRequestFsmRmtInvErrDescr,
       "cucsIdentIdentRequestFsmRmtInvRslt": cucsIdentIdentRequestFsmRmtInvRslt,
       "cucsIdentIdentRequestFsmStageDescr": cucsIdentIdentRequestFsmStageDescr,
       "cucsIdentIdentRequestFsmStamp": cucsIdentIdentRequestFsmStamp,
       "cucsIdentIdentRequestFsmStatus": cucsIdentIdentRequestFsmStatus,
       "cucsIdentIdentRequestFsmTry": cucsIdentIdentRequestFsmTry,
       "cucsIdentIdentRequestId": cucsIdentIdentRequestId,
       "cucsIdentIdentRequestRequestSize": cucsIdentIdentRequestRequestSize,
       "cucsIdentIdentRequestSeqNum": cucsIdentIdentRequestSeqNum,
       "cucsIdentIdentRequestFsmTable": cucsIdentIdentRequestFsmTable,
       "cucsIdentIdentRequestFsmEntry": cucsIdentIdentRequestFsmEntry,
       "cucsIdentIdentRequestFsmInstanceId": cucsIdentIdentRequestFsmInstanceId,
       "cucsIdentIdentRequestFsmDn": cucsIdentIdentRequestFsmDn,
       "cucsIdentIdentRequestFsmRn": cucsIdentIdentRequestFsmRn,
       "cucsIdentIdentRequestFsmCompletionTime": cucsIdentIdentRequestFsmCompletionTime,
       "cucsIdentIdentRequestFsmCurrentFsm": cucsIdentIdentRequestFsmCurrentFsm,
       "cucsIdentIdentRequestFsmDescrData": cucsIdentIdentRequestFsmDescrData,
       "cucsIdentIdentRequestFsmFsmStatus": cucsIdentIdentRequestFsmFsmStatus,
       "cucsIdentIdentRequestFsmProgress": cucsIdentIdentRequestFsmProgress,
       "cucsIdentIdentRequestFsmRmtErrCode": cucsIdentIdentRequestFsmRmtErrCode,
       "cucsIdentIdentRequestFsmRmtErrDescr": cucsIdentIdentRequestFsmRmtErrDescr,
       "cucsIdentIdentRequestFsmRmtRslt": cucsIdentIdentRequestFsmRmtRslt,
       "cucsIdentIdentRequestFsmStageTable": cucsIdentIdentRequestFsmStageTable,
       "cucsIdentIdentRequestFsmStageEntry": cucsIdentIdentRequestFsmStageEntry,
       "cucsIdentIdentRequestFsmStageInstanceId": cucsIdentIdentRequestFsmStageInstanceId,
       "cucsIdentIdentRequestFsmStageDn": cucsIdentIdentRequestFsmStageDn,
       "cucsIdentIdentRequestFsmStageRn": cucsIdentIdentRequestFsmStageRn,
       "cucsIdentIdentRequestFsmStageDescrData": cucsIdentIdentRequestFsmStageDescrData,
       "cucsIdentIdentRequestFsmStageLastUpdateTime": cucsIdentIdentRequestFsmStageLastUpdateTime,
       "cucsIdentIdentRequestFsmStageName": cucsIdentIdentRequestFsmStageName,
       "cucsIdentIdentRequestFsmStageOrder": cucsIdentIdentRequestFsmStageOrder,
       "cucsIdentIdentRequestFsmStageRetry": cucsIdentIdentRequestFsmStageRetry,
       "cucsIdentIdentRequestFsmStageStageStatus": cucsIdentIdentRequestFsmStageStageStatus,
       "cucsIdentIdentRequestFsmTaskTable": cucsIdentIdentRequestFsmTaskTable,
       "cucsIdentIdentRequestFsmTaskEntry": cucsIdentIdentRequestFsmTaskEntry,
       "cucsIdentIdentRequestFsmTaskInstanceId": cucsIdentIdentRequestFsmTaskInstanceId,
       "cucsIdentIdentRequestFsmTaskDn": cucsIdentIdentRequestFsmTaskDn,
       "cucsIdentIdentRequestFsmTaskRn": cucsIdentIdentRequestFsmTaskRn,
       "cucsIdentIdentRequestFsmTaskCompletion": cucsIdentIdentRequestFsmTaskCompletion,
       "cucsIdentIdentRequestFsmTaskFlags": cucsIdentIdentRequestFsmTaskFlags,
       "cucsIdentIdentRequestFsmTaskItem": cucsIdentIdentRequestFsmTaskItem,
       "cucsIdentIdentRequestFsmTaskSeqId": cucsIdentIdentRequestFsmTaskSeqId,
       "cucsIdentMetaSystemTable": cucsIdentMetaSystemTable,
       "cucsIdentMetaSystemEntry": cucsIdentMetaSystemEntry,
       "cucsIdentMetaSystemInstanceId": cucsIdentMetaSystemInstanceId,
       "cucsIdentMetaSystemDn": cucsIdentMetaSystemDn,
       "cucsIdentMetaSystemRn": cucsIdentMetaSystemRn,
       "cucsIdentMetaSystemFsmDescr": cucsIdentMetaSystemFsmDescr,
       "cucsIdentMetaSystemFsmPrev": cucsIdentMetaSystemFsmPrev,
       "cucsIdentMetaSystemFsmProgr": cucsIdentMetaSystemFsmProgr,
       "cucsIdentMetaSystemFsmRmtInvErrCode": cucsIdentMetaSystemFsmRmtInvErrCode,
       "cucsIdentMetaSystemFsmRmtInvErrDescr": cucsIdentMetaSystemFsmRmtInvErrDescr,
       "cucsIdentMetaSystemFsmRmtInvRslt": cucsIdentMetaSystemFsmRmtInvRslt,
       "cucsIdentMetaSystemFsmStageDescr": cucsIdentMetaSystemFsmStageDescr,
       "cucsIdentMetaSystemFsmStamp": cucsIdentMetaSystemFsmStamp,
       "cucsIdentMetaSystemFsmStatus": cucsIdentMetaSystemFsmStatus,
       "cucsIdentMetaSystemFsmTry": cucsIdentMetaSystemFsmTry,
       "cucsIdentMetaSystemGeneration": cucsIdentMetaSystemGeneration,
       "cucsIdentMetaSystemNextReqId": cucsIdentMetaSystemNextReqId,
       "cucsIdentMetaSystemSysid": cucsIdentMetaSystemSysid,
       "cucsIdentMetaSystemUcscGeneration": cucsIdentMetaSystemUcscGeneration,
       "cucsIdentMetaSystemFsmTable": cucsIdentMetaSystemFsmTable,
       "cucsIdentMetaSystemFsmEntry": cucsIdentMetaSystemFsmEntry,
       "cucsIdentMetaSystemFsmInstanceId": cucsIdentMetaSystemFsmInstanceId,
       "cucsIdentMetaSystemFsmDn": cucsIdentMetaSystemFsmDn,
       "cucsIdentMetaSystemFsmRn": cucsIdentMetaSystemFsmRn,
       "cucsIdentMetaSystemFsmCompletionTime": cucsIdentMetaSystemFsmCompletionTime,
       "cucsIdentMetaSystemFsmCurrentFsm": cucsIdentMetaSystemFsmCurrentFsm,
       "cucsIdentMetaSystemFsmDescrData": cucsIdentMetaSystemFsmDescrData,
       "cucsIdentMetaSystemFsmFsmStatus": cucsIdentMetaSystemFsmFsmStatus,
       "cucsIdentMetaSystemFsmProgress": cucsIdentMetaSystemFsmProgress,
       "cucsIdentMetaSystemFsmRmtErrCode": cucsIdentMetaSystemFsmRmtErrCode,
       "cucsIdentMetaSystemFsmRmtErrDescr": cucsIdentMetaSystemFsmRmtErrDescr,
       "cucsIdentMetaSystemFsmRmtRslt": cucsIdentMetaSystemFsmRmtRslt,
       "cucsIdentMetaSystemFsmStageTable": cucsIdentMetaSystemFsmStageTable,
       "cucsIdentMetaSystemFsmStageEntry": cucsIdentMetaSystemFsmStageEntry,
       "cucsIdentMetaSystemFsmStageInstanceId": cucsIdentMetaSystemFsmStageInstanceId,
       "cucsIdentMetaSystemFsmStageDn": cucsIdentMetaSystemFsmStageDn,
       "cucsIdentMetaSystemFsmStageRn": cucsIdentMetaSystemFsmStageRn,
       "cucsIdentMetaSystemFsmStageDescrData": cucsIdentMetaSystemFsmStageDescrData,
       "cucsIdentMetaSystemFsmStageLastUpdateTime": cucsIdentMetaSystemFsmStageLastUpdateTime,
       "cucsIdentMetaSystemFsmStageName": cucsIdentMetaSystemFsmStageName,
       "cucsIdentMetaSystemFsmStageOrder": cucsIdentMetaSystemFsmStageOrder,
       "cucsIdentMetaSystemFsmStageRetry": cucsIdentMetaSystemFsmStageRetry,
       "cucsIdentMetaSystemFsmStageStageStatus": cucsIdentMetaSystemFsmStageStageStatus,
       "cucsIdentMetaSystemFsmTaskTable": cucsIdentMetaSystemFsmTaskTable,
       "cucsIdentMetaSystemFsmTaskEntry": cucsIdentMetaSystemFsmTaskEntry,
       "cucsIdentMetaSystemFsmTaskInstanceId": cucsIdentMetaSystemFsmTaskInstanceId,
       "cucsIdentMetaSystemFsmTaskDn": cucsIdentMetaSystemFsmTaskDn,
       "cucsIdentMetaSystemFsmTaskRn": cucsIdentMetaSystemFsmTaskRn,
       "cucsIdentMetaSystemFsmTaskCompletion": cucsIdentMetaSystemFsmTaskCompletion,
       "cucsIdentMetaSystemFsmTaskFlags": cucsIdentMetaSystemFsmTaskFlags,
       "cucsIdentMetaSystemFsmTaskItem": cucsIdentMetaSystemFsmTaskItem,
       "cucsIdentMetaSystemFsmTaskSeqId": cucsIdentMetaSystemFsmTaskSeqId,
       "cucsIdentMetaVerseTable": cucsIdentMetaVerseTable,
       "cucsIdentMetaVerseEntry": cucsIdentMetaVerseEntry,
       "cucsIdentMetaVerseInstanceId": cucsIdentMetaVerseInstanceId,
       "cucsIdentMetaVerseDn": cucsIdentMetaVerseDn,
       "cucsIdentMetaVerseRn": cucsIdentMetaVerseRn,
       "cucsIdentRequestEpTable": cucsIdentRequestEpTable,
       "cucsIdentRequestEpEntry": cucsIdentRequestEpEntry,
       "cucsIdentRequestEpInstanceId": cucsIdentRequestEpInstanceId,
       "cucsIdentRequestEpDn": cucsIdentRequestEpDn,
       "cucsIdentRequestEpRn": cucsIdentRequestEpRn,
       "cucsIdentRequestEpReqDn": cucsIdentRequestEpReqDn,
       "cucsIdentRequestEpReqId": cucsIdentRequestEpReqId,
       "cucsIdentSysInfoTable": cucsIdentSysInfoTable,
       "cucsIdentSysInfoEntry": cucsIdentSysInfoEntry,
       "cucsIdentSysInfoInstanceId": cucsIdentSysInfoInstanceId,
       "cucsIdentSysInfoDn": cucsIdentSysInfoDn,
       "cucsIdentSysInfoRn": cucsIdentSysInfoRn,
       "cucsIdentSysInfoGeneration": cucsIdentSysInfoGeneration,
       "cucsIdentSysInfoIsSync": cucsIdentSysInfoIsSync,
       "cucsIdentSysInfoIsSyncAllowed": cucsIdentSysInfoIsSyncAllowed,
       "cucsIdentSysInfoIsFirstSync": cucsIdentSysInfoIsFirstSync,
       "cucsIdentSysInfoUcscGeneration": cucsIdentSysInfoUcscGeneration}
)
