# SNMP MIB module (CISCO-UNIFIED-COMPUTING-OBSERVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-OBSERVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:04 2024
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
 CucsMoMoClassId,
 CucsObserveObservedFsmCurrentFsm,
 CucsObserveObservedFsmStageName,
 CucsObserveObservedFsmTaskItem) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsMoMoClassId",
    "CucsObserveObservedFsmCurrentFsm",
    "CucsObserveObservedFsmStageName",
    "CucsObserveObservedFsmTaskItem")

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

cucsObserveObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsObserveFilterTable_Object = MibTable
cucsObserveFilterTable = _CucsObserveFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1)
)
if mibBuilder.loadTexts:
    cucsObserveFilterTable.setStatus("current")
_CucsObserveFilterEntry_Object = MibTableRow
cucsObserveFilterEntry = _CucsObserveFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1)
)
cucsObserveFilterEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", "cucsObserveFilterInstanceId"),
)
if mibBuilder.loadTexts:
    cucsObserveFilterEntry.setStatus("current")
_CucsObserveFilterInstanceId_Type = CucsManagedObjectId
_CucsObserveFilterInstanceId_Object = MibTableColumn
cucsObserveFilterInstanceId = _CucsObserveFilterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 1),
    _CucsObserveFilterInstanceId_Type()
)
cucsObserveFilterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsObserveFilterInstanceId.setStatus("current")
_CucsObserveFilterDn_Type = CucsManagedObjectDn
_CucsObserveFilterDn_Object = MibTableColumn
cucsObserveFilterDn = _CucsObserveFilterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 2),
    _CucsObserveFilterDn_Type()
)
cucsObserveFilterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterDn.setStatus("current")
_CucsObserveFilterRn_Type = SnmpAdminString
_CucsObserveFilterRn_Object = MibTableColumn
cucsObserveFilterRn = _CucsObserveFilterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 3),
    _CucsObserveFilterRn_Type()
)
cucsObserveFilterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterRn.setStatus("current")
_CucsObserveFilterAndOperation_Type = TruthValue
_CucsObserveFilterAndOperation_Object = MibTableColumn
cucsObserveFilterAndOperation = _CucsObserveFilterAndOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 4),
    _CucsObserveFilterAndOperation_Type()
)
cucsObserveFilterAndOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterAndOperation.setStatus("current")
_CucsObserveFilterChildClassId_Type = CucsMoMoClassId
_CucsObserveFilterChildClassId_Object = MibTableColumn
cucsObserveFilterChildClassId = _CucsObserveFilterChildClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 5),
    _CucsObserveFilterChildClassId_Type()
)
cucsObserveFilterChildClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterChildClassId.setStatus("current")
_CucsObserveFilterFilterClassId_Type = CucsMoMoClassId
_CucsObserveFilterFilterClassId_Object = MibTableColumn
cucsObserveFilterFilterClassId = _CucsObserveFilterFilterClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 6),
    _CucsObserveFilterFilterClassId_Type()
)
cucsObserveFilterFilterClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterFilterClassId.setStatus("current")
_CucsObserveFilterFilterPropId1_Type = SnmpAdminString
_CucsObserveFilterFilterPropId1_Object = MibTableColumn
cucsObserveFilterFilterPropId1 = _CucsObserveFilterFilterPropId1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 7),
    _CucsObserveFilterFilterPropId1_Type()
)
cucsObserveFilterFilterPropId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterFilterPropId1.setStatus("current")
_CucsObserveFilterFilterPropId2_Type = SnmpAdminString
_CucsObserveFilterFilterPropId2_Object = MibTableColumn
cucsObserveFilterFilterPropId2 = _CucsObserveFilterFilterPropId2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 8),
    _CucsObserveFilterFilterPropId2_Type()
)
cucsObserveFilterFilterPropId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterFilterPropId2.setStatus("current")
_CucsObserveFilterFilterPropId3_Type = SnmpAdminString
_CucsObserveFilterFilterPropId3_Object = MibTableColumn
cucsObserveFilterFilterPropId3 = _CucsObserveFilterFilterPropId3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 9),
    _CucsObserveFilterFilterPropId3_Type()
)
cucsObserveFilterFilterPropId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterFilterPropId3.setStatus("current")
_CucsObserveFilterFilterPropValue1_Type = SnmpAdminString
_CucsObserveFilterFilterPropValue1_Object = MibTableColumn
cucsObserveFilterFilterPropValue1 = _CucsObserveFilterFilterPropValue1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 10),
    _CucsObserveFilterFilterPropValue1_Type()
)
cucsObserveFilterFilterPropValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterFilterPropValue1.setStatus("current")
_CucsObserveFilterFilterPropValue2_Type = SnmpAdminString
_CucsObserveFilterFilterPropValue2_Object = MibTableColumn
cucsObserveFilterFilterPropValue2 = _CucsObserveFilterFilterPropValue2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 11),
    _CucsObserveFilterFilterPropValue2_Type()
)
cucsObserveFilterFilterPropValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterFilterPropValue2.setStatus("current")
_CucsObserveFilterFilterPropValue3_Type = SnmpAdminString
_CucsObserveFilterFilterPropValue3_Object = MibTableColumn
cucsObserveFilterFilterPropValue3 = _CucsObserveFilterFilterPropValue3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 12),
    _CucsObserveFilterFilterPropValue3_Type()
)
cucsObserveFilterFilterPropValue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterFilterPropValue3.setStatus("current")
_CucsObserveFilterHierarchical_Type = TruthValue
_CucsObserveFilterHierarchical_Object = MibTableColumn
cucsObserveFilterHierarchical = _CucsObserveFilterHierarchical_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 13),
    _CucsObserveFilterHierarchical_Type()
)
cucsObserveFilterHierarchical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterHierarchical.setStatus("current")
_CucsObserveFilterReplicateIfNoChild_Type = TruthValue
_CucsObserveFilterReplicateIfNoChild_Object = MibTableColumn
cucsObserveFilterReplicateIfNoChild = _CucsObserveFilterReplicateIfNoChild_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 1, 1, 14),
    _CucsObserveFilterReplicateIfNoChild_Type()
)
cucsObserveFilterReplicateIfNoChild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveFilterReplicateIfNoChild.setStatus("current")
_CucsObserveObservedTable_Object = MibTable
cucsObserveObservedTable = _CucsObserveObservedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2)
)
if mibBuilder.loadTexts:
    cucsObserveObservedTable.setStatus("current")
_CucsObserveObservedEntry_Object = MibTableRow
cucsObserveObservedEntry = _CucsObserveObservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1)
)
cucsObserveObservedEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", "cucsObserveObservedInstanceId"),
)
if mibBuilder.loadTexts:
    cucsObserveObservedEntry.setStatus("current")
_CucsObserveObservedInstanceId_Type = CucsManagedObjectId
_CucsObserveObservedInstanceId_Object = MibTableColumn
cucsObserveObservedInstanceId = _CucsObserveObservedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 1),
    _CucsObserveObservedInstanceId_Type()
)
cucsObserveObservedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsObserveObservedInstanceId.setStatus("current")
_CucsObserveObservedDn_Type = CucsManagedObjectDn
_CucsObserveObservedDn_Object = MibTableColumn
cucsObserveObservedDn = _CucsObserveObservedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 2),
    _CucsObserveObservedDn_Type()
)
cucsObserveObservedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedDn.setStatus("current")
_CucsObserveObservedRn_Type = SnmpAdminString
_CucsObserveObservedRn_Object = MibTableColumn
cucsObserveObservedRn = _CucsObserveObservedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 3),
    _CucsObserveObservedRn_Type()
)
cucsObserveObservedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedRn.setStatus("current")
_CucsObserveObservedDataSrcAppType_Type = SnmpAdminString
_CucsObserveObservedDataSrcAppType_Object = MibTableColumn
cucsObserveObservedDataSrcAppType = _CucsObserveObservedDataSrcAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 4),
    _CucsObserveObservedDataSrcAppType_Type()
)
cucsObserveObservedDataSrcAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedDataSrcAppType.setStatus("current")
_CucsObserveObservedDataSrcSysId_Type = Gauge32
_CucsObserveObservedDataSrcSysId_Object = MibTableColumn
cucsObserveObservedDataSrcSysId = _CucsObserveObservedDataSrcSysId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 5),
    _CucsObserveObservedDataSrcSysId_Type()
)
cucsObserveObservedDataSrcSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedDataSrcSysId.setStatus("current")
_CucsObserveObservedFsmDescr_Type = SnmpAdminString
_CucsObserveObservedFsmDescr_Object = MibTableColumn
cucsObserveObservedFsmDescr = _CucsObserveObservedFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 6),
    _CucsObserveObservedFsmDescr_Type()
)
cucsObserveObservedFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmDescr.setStatus("current")
_CucsObserveObservedFsmPrev_Type = SnmpAdminString
_CucsObserveObservedFsmPrev_Object = MibTableColumn
cucsObserveObservedFsmPrev = _CucsObserveObservedFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 7),
    _CucsObserveObservedFsmPrev_Type()
)
cucsObserveObservedFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmPrev.setStatus("current")
_CucsObserveObservedFsmProgr_Type = Gauge32
_CucsObserveObservedFsmProgr_Object = MibTableColumn
cucsObserveObservedFsmProgr = _CucsObserveObservedFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 8),
    _CucsObserveObservedFsmProgr_Type()
)
cucsObserveObservedFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmProgr.setStatus("current")
_CucsObserveObservedFsmRmtInvErrCode_Type = Gauge32
_CucsObserveObservedFsmRmtInvErrCode_Object = MibTableColumn
cucsObserveObservedFsmRmtInvErrCode = _CucsObserveObservedFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 9),
    _CucsObserveObservedFsmRmtInvErrCode_Type()
)
cucsObserveObservedFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmRmtInvErrCode.setStatus("current")
_CucsObserveObservedFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsObserveObservedFsmRmtInvErrDescr_Object = MibTableColumn
cucsObserveObservedFsmRmtInvErrDescr = _CucsObserveObservedFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 10),
    _CucsObserveObservedFsmRmtInvErrDescr_Type()
)
cucsObserveObservedFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmRmtInvErrDescr.setStatus("current")
_CucsObserveObservedFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsObserveObservedFsmRmtInvRslt_Object = MibTableColumn
cucsObserveObservedFsmRmtInvRslt = _CucsObserveObservedFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 11),
    _CucsObserveObservedFsmRmtInvRslt_Type()
)
cucsObserveObservedFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmRmtInvRslt.setStatus("current")
_CucsObserveObservedFsmStageDescr_Type = SnmpAdminString
_CucsObserveObservedFsmStageDescr_Object = MibTableColumn
cucsObserveObservedFsmStageDescr = _CucsObserveObservedFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 12),
    _CucsObserveObservedFsmStageDescr_Type()
)
cucsObserveObservedFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStageDescr.setStatus("current")
_CucsObserveObservedFsmStamp_Type = DateAndTime
_CucsObserveObservedFsmStamp_Object = MibTableColumn
cucsObserveObservedFsmStamp = _CucsObserveObservedFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 13),
    _CucsObserveObservedFsmStamp_Type()
)
cucsObserveObservedFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStamp.setStatus("current")
_CucsObserveObservedFsmStatus_Type = SnmpAdminString
_CucsObserveObservedFsmStatus_Object = MibTableColumn
cucsObserveObservedFsmStatus = _CucsObserveObservedFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 14),
    _CucsObserveObservedFsmStatus_Type()
)
cucsObserveObservedFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStatus.setStatus("current")
_CucsObserveObservedFsmTry_Type = Gauge32
_CucsObserveObservedFsmTry_Object = MibTableColumn
cucsObserveObservedFsmTry = _CucsObserveObservedFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 15),
    _CucsObserveObservedFsmTry_Type()
)
cucsObserveObservedFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmTry.setStatus("current")
_CucsObserveObservedGenNum_Type = Gauge32
_CucsObserveObservedGenNum_Object = MibTableColumn
cucsObserveObservedGenNum = _CucsObserveObservedGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 16),
    _CucsObserveObservedGenNum_Type()
)
cucsObserveObservedGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedGenNum.setStatus("current")
_CucsObserveObservedHierarchical_Type = TruthValue
_CucsObserveObservedHierarchical_Object = MibTableColumn
cucsObserveObservedHierarchical = _CucsObserveObservedHierarchical_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 17),
    _CucsObserveObservedHierarchical_Type()
)
cucsObserveObservedHierarchical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedHierarchical.setStatus("current")
_CucsObserveObservedId_Type = Gauge32
_CucsObserveObservedId_Object = MibTableColumn
cucsObserveObservedId = _CucsObserveObservedId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 18),
    _CucsObserveObservedId_Type()
)
cucsObserveObservedId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedId.setStatus("current")
_CucsObserveObservedIsDeleted_Type = TruthValue
_CucsObserveObservedIsDeleted_Object = MibTableColumn
cucsObserveObservedIsDeleted = _CucsObserveObservedIsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 19),
    _CucsObserveObservedIsDeleted_Type()
)
cucsObserveObservedIsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedIsDeleted.setStatus("current")
_CucsObserveObservedObservedDn_Type = SnmpAdminString
_CucsObserveObservedObservedDn_Object = MibTableColumn
cucsObserveObservedObservedDn = _CucsObserveObservedObservedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 2, 1, 20),
    _CucsObserveObservedObservedDn_Type()
)
cucsObserveObservedObservedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedObservedDn.setStatus("current")
_CucsObserveObservedContTable_Object = MibTable
cucsObserveObservedContTable = _CucsObserveObservedContTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 3)
)
if mibBuilder.loadTexts:
    cucsObserveObservedContTable.setStatus("current")
_CucsObserveObservedContEntry_Object = MibTableRow
cucsObserveObservedContEntry = _CucsObserveObservedContEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 3, 1)
)
cucsObserveObservedContEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", "cucsObserveObservedContInstanceId"),
)
if mibBuilder.loadTexts:
    cucsObserveObservedContEntry.setStatus("current")
_CucsObserveObservedContInstanceId_Type = CucsManagedObjectId
_CucsObserveObservedContInstanceId_Object = MibTableColumn
cucsObserveObservedContInstanceId = _CucsObserveObservedContInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 3, 1, 1),
    _CucsObserveObservedContInstanceId_Type()
)
cucsObserveObservedContInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsObserveObservedContInstanceId.setStatus("current")
_CucsObserveObservedContDn_Type = CucsManagedObjectDn
_CucsObserveObservedContDn_Object = MibTableColumn
cucsObserveObservedContDn = _CucsObserveObservedContDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 3, 1, 2),
    _CucsObserveObservedContDn_Type()
)
cucsObserveObservedContDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedContDn.setStatus("current")
_CucsObserveObservedContRn_Type = SnmpAdminString
_CucsObserveObservedContRn_Object = MibTableColumn
cucsObserveObservedContRn = _CucsObserveObservedContRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 3, 1, 3),
    _CucsObserveObservedContRn_Type()
)
cucsObserveObservedContRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedContRn.setStatus("current")
_CucsObserveObservedContIdCount_Type = Gauge32
_CucsObserveObservedContIdCount_Object = MibTableColumn
cucsObserveObservedContIdCount = _CucsObserveObservedContIdCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 3, 1, 4),
    _CucsObserveObservedContIdCount_Type()
)
cucsObserveObservedContIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedContIdCount.setStatus("current")
_CucsObserveObservedFsmTable_Object = MibTable
cucsObserveObservedFsmTable = _CucsObserveObservedFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4)
)
if mibBuilder.loadTexts:
    cucsObserveObservedFsmTable.setStatus("current")
_CucsObserveObservedFsmEntry_Object = MibTableRow
cucsObserveObservedFsmEntry = _CucsObserveObservedFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1)
)
cucsObserveObservedFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", "cucsObserveObservedFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsObserveObservedFsmEntry.setStatus("current")
_CucsObserveObservedFsmInstanceId_Type = CucsManagedObjectId
_CucsObserveObservedFsmInstanceId_Object = MibTableColumn
cucsObserveObservedFsmInstanceId = _CucsObserveObservedFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 1),
    _CucsObserveObservedFsmInstanceId_Type()
)
cucsObserveObservedFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmInstanceId.setStatus("current")
_CucsObserveObservedFsmDn_Type = CucsManagedObjectDn
_CucsObserveObservedFsmDn_Object = MibTableColumn
cucsObserveObservedFsmDn = _CucsObserveObservedFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 2),
    _CucsObserveObservedFsmDn_Type()
)
cucsObserveObservedFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmDn.setStatus("current")
_CucsObserveObservedFsmRn_Type = SnmpAdminString
_CucsObserveObservedFsmRn_Object = MibTableColumn
cucsObserveObservedFsmRn = _CucsObserveObservedFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 3),
    _CucsObserveObservedFsmRn_Type()
)
cucsObserveObservedFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmRn.setStatus("current")
_CucsObserveObservedFsmCompletionTime_Type = DateAndTime
_CucsObserveObservedFsmCompletionTime_Object = MibTableColumn
cucsObserveObservedFsmCompletionTime = _CucsObserveObservedFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 4),
    _CucsObserveObservedFsmCompletionTime_Type()
)
cucsObserveObservedFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmCompletionTime.setStatus("current")
_CucsObserveObservedFsmCurrentFsm_Type = CucsObserveObservedFsmCurrentFsm
_CucsObserveObservedFsmCurrentFsm_Object = MibTableColumn
cucsObserveObservedFsmCurrentFsm = _CucsObserveObservedFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 5),
    _CucsObserveObservedFsmCurrentFsm_Type()
)
cucsObserveObservedFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmCurrentFsm.setStatus("current")
_CucsObserveObservedFsmDescrData_Type = SnmpAdminString
_CucsObserveObservedFsmDescrData_Object = MibTableColumn
cucsObserveObservedFsmDescrData = _CucsObserveObservedFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 6),
    _CucsObserveObservedFsmDescrData_Type()
)
cucsObserveObservedFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmDescrData.setStatus("current")
_CucsObserveObservedFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsObserveObservedFsmFsmStatus_Object = MibTableColumn
cucsObserveObservedFsmFsmStatus = _CucsObserveObservedFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 7),
    _CucsObserveObservedFsmFsmStatus_Type()
)
cucsObserveObservedFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmFsmStatus.setStatus("current")
_CucsObserveObservedFsmProgress_Type = Gauge32
_CucsObserveObservedFsmProgress_Object = MibTableColumn
cucsObserveObservedFsmProgress = _CucsObserveObservedFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 8),
    _CucsObserveObservedFsmProgress_Type()
)
cucsObserveObservedFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmProgress.setStatus("current")
_CucsObserveObservedFsmRmtErrCode_Type = Gauge32
_CucsObserveObservedFsmRmtErrCode_Object = MibTableColumn
cucsObserveObservedFsmRmtErrCode = _CucsObserveObservedFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 9),
    _CucsObserveObservedFsmRmtErrCode_Type()
)
cucsObserveObservedFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmRmtErrCode.setStatus("current")
_CucsObserveObservedFsmRmtErrDescr_Type = SnmpAdminString
_CucsObserveObservedFsmRmtErrDescr_Object = MibTableColumn
cucsObserveObservedFsmRmtErrDescr = _CucsObserveObservedFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 10),
    _CucsObserveObservedFsmRmtErrDescr_Type()
)
cucsObserveObservedFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmRmtErrDescr.setStatus("current")
_CucsObserveObservedFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsObserveObservedFsmRmtRslt_Object = MibTableColumn
cucsObserveObservedFsmRmtRslt = _CucsObserveObservedFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 4, 1, 11),
    _CucsObserveObservedFsmRmtRslt_Type()
)
cucsObserveObservedFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmRmtRslt.setStatus("current")
_CucsObserveObservedFsmStageTable_Object = MibTable
cucsObserveObservedFsmStageTable = _CucsObserveObservedFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5)
)
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStageTable.setStatus("current")
_CucsObserveObservedFsmStageEntry_Object = MibTableRow
cucsObserveObservedFsmStageEntry = _CucsObserveObservedFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1)
)
cucsObserveObservedFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", "cucsObserveObservedFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStageEntry.setStatus("current")
_CucsObserveObservedFsmStageInstanceId_Type = CucsManagedObjectId
_CucsObserveObservedFsmStageInstanceId_Object = MibTableColumn
cucsObserveObservedFsmStageInstanceId = _CucsObserveObservedFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 1),
    _CucsObserveObservedFsmStageInstanceId_Type()
)
cucsObserveObservedFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStageInstanceId.setStatus("current")
_CucsObserveObservedFsmStageDn_Type = CucsManagedObjectDn
_CucsObserveObservedFsmStageDn_Object = MibTableColumn
cucsObserveObservedFsmStageDn = _CucsObserveObservedFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 2),
    _CucsObserveObservedFsmStageDn_Type()
)
cucsObserveObservedFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStageDn.setStatus("current")
_CucsObserveObservedFsmStageRn_Type = SnmpAdminString
_CucsObserveObservedFsmStageRn_Object = MibTableColumn
cucsObserveObservedFsmStageRn = _CucsObserveObservedFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 3),
    _CucsObserveObservedFsmStageRn_Type()
)
cucsObserveObservedFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStageRn.setStatus("current")
_CucsObserveObservedFsmStageDescrData_Type = SnmpAdminString
_CucsObserveObservedFsmStageDescrData_Object = MibTableColumn
cucsObserveObservedFsmStageDescrData = _CucsObserveObservedFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 4),
    _CucsObserveObservedFsmStageDescrData_Type()
)
cucsObserveObservedFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStageDescrData.setStatus("current")
_CucsObserveObservedFsmStageLastUpdateTime_Type = DateAndTime
_CucsObserveObservedFsmStageLastUpdateTime_Object = MibTableColumn
cucsObserveObservedFsmStageLastUpdateTime = _CucsObserveObservedFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 5),
    _CucsObserveObservedFsmStageLastUpdateTime_Type()
)
cucsObserveObservedFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStageLastUpdateTime.setStatus("current")
_CucsObserveObservedFsmStageName_Type = CucsObserveObservedFsmStageName
_CucsObserveObservedFsmStageName_Object = MibTableColumn
cucsObserveObservedFsmStageName = _CucsObserveObservedFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 6),
    _CucsObserveObservedFsmStageName_Type()
)
cucsObserveObservedFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStageName.setStatus("current")
_CucsObserveObservedFsmStageOrder_Type = Gauge32
_CucsObserveObservedFsmStageOrder_Object = MibTableColumn
cucsObserveObservedFsmStageOrder = _CucsObserveObservedFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 7),
    _CucsObserveObservedFsmStageOrder_Type()
)
cucsObserveObservedFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStageOrder.setStatus("current")
_CucsObserveObservedFsmStageRetry_Type = Gauge32
_CucsObserveObservedFsmStageRetry_Object = MibTableColumn
cucsObserveObservedFsmStageRetry = _CucsObserveObservedFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 8),
    _CucsObserveObservedFsmStageRetry_Type()
)
cucsObserveObservedFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStageRetry.setStatus("current")
_CucsObserveObservedFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsObserveObservedFsmStageStageStatus_Object = MibTableColumn
cucsObserveObservedFsmStageStageStatus = _CucsObserveObservedFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 5, 1, 9),
    _CucsObserveObservedFsmStageStageStatus_Type()
)
cucsObserveObservedFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmStageStageStatus.setStatus("current")
_CucsObserveObservedFsmTaskTable_Object = MibTable
cucsObserveObservedFsmTaskTable = _CucsObserveObservedFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6)
)
if mibBuilder.loadTexts:
    cucsObserveObservedFsmTaskTable.setStatus("current")
_CucsObserveObservedFsmTaskEntry_Object = MibTableRow
cucsObserveObservedFsmTaskEntry = _CucsObserveObservedFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1)
)
cucsObserveObservedFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB", "cucsObserveObservedFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsObserveObservedFsmTaskEntry.setStatus("current")
_CucsObserveObservedFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsObserveObservedFsmTaskInstanceId_Object = MibTableColumn
cucsObserveObservedFsmTaskInstanceId = _CucsObserveObservedFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 1),
    _CucsObserveObservedFsmTaskInstanceId_Type()
)
cucsObserveObservedFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmTaskInstanceId.setStatus("current")
_CucsObserveObservedFsmTaskDn_Type = CucsManagedObjectDn
_CucsObserveObservedFsmTaskDn_Object = MibTableColumn
cucsObserveObservedFsmTaskDn = _CucsObserveObservedFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 2),
    _CucsObserveObservedFsmTaskDn_Type()
)
cucsObserveObservedFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmTaskDn.setStatus("current")
_CucsObserveObservedFsmTaskRn_Type = SnmpAdminString
_CucsObserveObservedFsmTaskRn_Object = MibTableColumn
cucsObserveObservedFsmTaskRn = _CucsObserveObservedFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 3),
    _CucsObserveObservedFsmTaskRn_Type()
)
cucsObserveObservedFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmTaskRn.setStatus("current")
_CucsObserveObservedFsmTaskCompletion_Type = CucsFsmCompletion
_CucsObserveObservedFsmTaskCompletion_Object = MibTableColumn
cucsObserveObservedFsmTaskCompletion = _CucsObserveObservedFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 4),
    _CucsObserveObservedFsmTaskCompletion_Type()
)
cucsObserveObservedFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmTaskCompletion.setStatus("current")
_CucsObserveObservedFsmTaskFlags_Type = CucsFsmFlags
_CucsObserveObservedFsmTaskFlags_Object = MibTableColumn
cucsObserveObservedFsmTaskFlags = _CucsObserveObservedFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 5),
    _CucsObserveObservedFsmTaskFlags_Type()
)
cucsObserveObservedFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmTaskFlags.setStatus("current")
_CucsObserveObservedFsmTaskItem_Type = CucsObserveObservedFsmTaskItem
_CucsObserveObservedFsmTaskItem_Object = MibTableColumn
cucsObserveObservedFsmTaskItem = _CucsObserveObservedFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 6),
    _CucsObserveObservedFsmTaskItem_Type()
)
cucsObserveObservedFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmTaskItem.setStatus("current")
_CucsObserveObservedFsmTaskSeqId_Type = Gauge32
_CucsObserveObservedFsmTaskSeqId_Object = MibTableColumn
cucsObserveObservedFsmTaskSeqId = _CucsObserveObservedFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 68, 6, 1, 7),
    _CucsObserveObservedFsmTaskSeqId_Type()
)
cucsObserveObservedFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsObserveObservedFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-OBSERVE-MIB",
    **{"cucsObserveObjects": cucsObserveObjects,
       "cucsObserveFilterTable": cucsObserveFilterTable,
       "cucsObserveFilterEntry": cucsObserveFilterEntry,
       "cucsObserveFilterInstanceId": cucsObserveFilterInstanceId,
       "cucsObserveFilterDn": cucsObserveFilterDn,
       "cucsObserveFilterRn": cucsObserveFilterRn,
       "cucsObserveFilterAndOperation": cucsObserveFilterAndOperation,
       "cucsObserveFilterChildClassId": cucsObserveFilterChildClassId,
       "cucsObserveFilterFilterClassId": cucsObserveFilterFilterClassId,
       "cucsObserveFilterFilterPropId1": cucsObserveFilterFilterPropId1,
       "cucsObserveFilterFilterPropId2": cucsObserveFilterFilterPropId2,
       "cucsObserveFilterFilterPropId3": cucsObserveFilterFilterPropId3,
       "cucsObserveFilterFilterPropValue1": cucsObserveFilterFilterPropValue1,
       "cucsObserveFilterFilterPropValue2": cucsObserveFilterFilterPropValue2,
       "cucsObserveFilterFilterPropValue3": cucsObserveFilterFilterPropValue3,
       "cucsObserveFilterHierarchical": cucsObserveFilterHierarchical,
       "cucsObserveFilterReplicateIfNoChild": cucsObserveFilterReplicateIfNoChild,
       "cucsObserveObservedTable": cucsObserveObservedTable,
       "cucsObserveObservedEntry": cucsObserveObservedEntry,
       "cucsObserveObservedInstanceId": cucsObserveObservedInstanceId,
       "cucsObserveObservedDn": cucsObserveObservedDn,
       "cucsObserveObservedRn": cucsObserveObservedRn,
       "cucsObserveObservedDataSrcAppType": cucsObserveObservedDataSrcAppType,
       "cucsObserveObservedDataSrcSysId": cucsObserveObservedDataSrcSysId,
       "cucsObserveObservedFsmDescr": cucsObserveObservedFsmDescr,
       "cucsObserveObservedFsmPrev": cucsObserveObservedFsmPrev,
       "cucsObserveObservedFsmProgr": cucsObserveObservedFsmProgr,
       "cucsObserveObservedFsmRmtInvErrCode": cucsObserveObservedFsmRmtInvErrCode,
       "cucsObserveObservedFsmRmtInvErrDescr": cucsObserveObservedFsmRmtInvErrDescr,
       "cucsObserveObservedFsmRmtInvRslt": cucsObserveObservedFsmRmtInvRslt,
       "cucsObserveObservedFsmStageDescr": cucsObserveObservedFsmStageDescr,
       "cucsObserveObservedFsmStamp": cucsObserveObservedFsmStamp,
       "cucsObserveObservedFsmStatus": cucsObserveObservedFsmStatus,
       "cucsObserveObservedFsmTry": cucsObserveObservedFsmTry,
       "cucsObserveObservedGenNum": cucsObserveObservedGenNum,
       "cucsObserveObservedHierarchical": cucsObserveObservedHierarchical,
       "cucsObserveObservedId": cucsObserveObservedId,
       "cucsObserveObservedIsDeleted": cucsObserveObservedIsDeleted,
       "cucsObserveObservedObservedDn": cucsObserveObservedObservedDn,
       "cucsObserveObservedContTable": cucsObserveObservedContTable,
       "cucsObserveObservedContEntry": cucsObserveObservedContEntry,
       "cucsObserveObservedContInstanceId": cucsObserveObservedContInstanceId,
       "cucsObserveObservedContDn": cucsObserveObservedContDn,
       "cucsObserveObservedContRn": cucsObserveObservedContRn,
       "cucsObserveObservedContIdCount": cucsObserveObservedContIdCount,
       "cucsObserveObservedFsmTable": cucsObserveObservedFsmTable,
       "cucsObserveObservedFsmEntry": cucsObserveObservedFsmEntry,
       "cucsObserveObservedFsmInstanceId": cucsObserveObservedFsmInstanceId,
       "cucsObserveObservedFsmDn": cucsObserveObservedFsmDn,
       "cucsObserveObservedFsmRn": cucsObserveObservedFsmRn,
       "cucsObserveObservedFsmCompletionTime": cucsObserveObservedFsmCompletionTime,
       "cucsObserveObservedFsmCurrentFsm": cucsObserveObservedFsmCurrentFsm,
       "cucsObserveObservedFsmDescrData": cucsObserveObservedFsmDescrData,
       "cucsObserveObservedFsmFsmStatus": cucsObserveObservedFsmFsmStatus,
       "cucsObserveObservedFsmProgress": cucsObserveObservedFsmProgress,
       "cucsObserveObservedFsmRmtErrCode": cucsObserveObservedFsmRmtErrCode,
       "cucsObserveObservedFsmRmtErrDescr": cucsObserveObservedFsmRmtErrDescr,
       "cucsObserveObservedFsmRmtRslt": cucsObserveObservedFsmRmtRslt,
       "cucsObserveObservedFsmStageTable": cucsObserveObservedFsmStageTable,
       "cucsObserveObservedFsmStageEntry": cucsObserveObservedFsmStageEntry,
       "cucsObserveObservedFsmStageInstanceId": cucsObserveObservedFsmStageInstanceId,
       "cucsObserveObservedFsmStageDn": cucsObserveObservedFsmStageDn,
       "cucsObserveObservedFsmStageRn": cucsObserveObservedFsmStageRn,
       "cucsObserveObservedFsmStageDescrData": cucsObserveObservedFsmStageDescrData,
       "cucsObserveObservedFsmStageLastUpdateTime": cucsObserveObservedFsmStageLastUpdateTime,
       "cucsObserveObservedFsmStageName": cucsObserveObservedFsmStageName,
       "cucsObserveObservedFsmStageOrder": cucsObserveObservedFsmStageOrder,
       "cucsObserveObservedFsmStageRetry": cucsObserveObservedFsmStageRetry,
       "cucsObserveObservedFsmStageStageStatus": cucsObserveObservedFsmStageStageStatus,
       "cucsObserveObservedFsmTaskTable": cucsObserveObservedFsmTaskTable,
       "cucsObserveObservedFsmTaskEntry": cucsObserveObservedFsmTaskEntry,
       "cucsObserveObservedFsmTaskInstanceId": cucsObserveObservedFsmTaskInstanceId,
       "cucsObserveObservedFsmTaskDn": cucsObserveObservedFsmTaskDn,
       "cucsObserveObservedFsmTaskRn": cucsObserveObservedFsmTaskRn,
       "cucsObserveObservedFsmTaskCompletion": cucsObserveObservedFsmTaskCompletion,
       "cucsObserveObservedFsmTaskFlags": cucsObserveObservedFsmTaskFlags,
       "cucsObserveObservedFsmTaskItem": cucsObserveObservedFsmTaskItem,
       "cucsObserveObservedFsmTaskSeqId": cucsObserveObservedFsmTaskSeqId}
)
