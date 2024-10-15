# SNMP MIB module (CISCO-UNIFIED-COMPUTING-EXTVMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-EXTVMM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:27 2024
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

(CucsCommFilePathProtocol,
 CucsConditionRemoteInvRslt,
 CucsExtvmmEpFsmCurrentFsm,
 CucsExtvmmEpFsmStageName,
 CucsExtvmmEpFsmTaskItem,
 CucsExtvmmFabricNetworkType,
 CucsExtvmmKeyStoreFsmCurrentFsm,
 CucsExtvmmKeyStoreFsmStageName,
 CucsExtvmmKeyStoreFsmTaskItem,
 CucsExtvmmMasterExtKeyFsmCurrentFsm,
 CucsExtvmmMasterExtKeyFsmStageName,
 CucsExtvmmMasterExtKeyFsmTaskItem,
 CucsExtvmmNetworkSetConfigQualifier,
 CucsExtvmmNetworkSetsFsmCurrentFsm,
 CucsExtvmmNetworkSetsFsmStageName,
 CucsExtvmmNetworkSetsFsmTaskItem,
 CucsExtvmmProviderFsmCurrentFsm,
 CucsExtvmmProviderFsmStageName,
 CucsExtvmmProviderFsmTaskItem,
 CucsExtvmmProviderVendorType,
 CucsExtvmmRefOperState,
 CucsExtvmmSwitchDelTaskFsmCurrentFsm,
 CucsExtvmmSwitchDelTaskFsmStageName,
 CucsExtvmmSwitchDelTaskFsmTaskItem,
 CucsExtvmmVcVersion,
 CucsExtvmmVnicType,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsCommFilePathProtocol",
    "CucsConditionRemoteInvRslt",
    "CucsExtvmmEpFsmCurrentFsm",
    "CucsExtvmmEpFsmStageName",
    "CucsExtvmmEpFsmTaskItem",
    "CucsExtvmmFabricNetworkType",
    "CucsExtvmmKeyStoreFsmCurrentFsm",
    "CucsExtvmmKeyStoreFsmStageName",
    "CucsExtvmmKeyStoreFsmTaskItem",
    "CucsExtvmmMasterExtKeyFsmCurrentFsm",
    "CucsExtvmmMasterExtKeyFsmStageName",
    "CucsExtvmmMasterExtKeyFsmTaskItem",
    "CucsExtvmmNetworkSetConfigQualifier",
    "CucsExtvmmNetworkSetsFsmCurrentFsm",
    "CucsExtvmmNetworkSetsFsmStageName",
    "CucsExtvmmNetworkSetsFsmTaskItem",
    "CucsExtvmmProviderFsmCurrentFsm",
    "CucsExtvmmProviderFsmStageName",
    "CucsExtvmmProviderFsmTaskItem",
    "CucsExtvmmProviderVendorType",
    "CucsExtvmmRefOperState",
    "CucsExtvmmSwitchDelTaskFsmCurrentFsm",
    "CucsExtvmmSwitchDelTaskFsmStageName",
    "CucsExtvmmSwitchDelTaskFsmTaskItem",
    "CucsExtvmmVcVersion",
    "CucsExtvmmVnicType",
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

cucsExtvmmObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsExtvmmEpTable_Object = MibTable
cucsExtvmmEpTable = _CucsExtvmmEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1)
)
if mibBuilder.loadTexts:
    cucsExtvmmEpTable.setStatus("current")
_CucsExtvmmEpEntry_Object = MibTableRow
cucsExtvmmEpEntry = _CucsExtvmmEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1)
)
cucsExtvmmEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmEpEntry.setStatus("current")
_CucsExtvmmEpInstanceId_Type = CucsManagedObjectId
_CucsExtvmmEpInstanceId_Object = MibTableColumn
cucsExtvmmEpInstanceId = _CucsExtvmmEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 1),
    _CucsExtvmmEpInstanceId_Type()
)
cucsExtvmmEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmEpInstanceId.setStatus("current")
_CucsExtvmmEpDn_Type = CucsManagedObjectDn
_CucsExtvmmEpDn_Object = MibTableColumn
cucsExtvmmEpDn = _CucsExtvmmEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 2),
    _CucsExtvmmEpDn_Type()
)
cucsExtvmmEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpDn.setStatus("current")
_CucsExtvmmEpRn_Type = SnmpAdminString
_CucsExtvmmEpRn_Object = MibTableColumn
cucsExtvmmEpRn = _CucsExtvmmEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 3),
    _CucsExtvmmEpRn_Type()
)
cucsExtvmmEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpRn.setStatus("current")
_CucsExtvmmEpFsmDescr_Type = SnmpAdminString
_CucsExtvmmEpFsmDescr_Object = MibTableColumn
cucsExtvmmEpFsmDescr = _CucsExtvmmEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 4),
    _CucsExtvmmEpFsmDescr_Type()
)
cucsExtvmmEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmDescr.setStatus("current")
_CucsExtvmmEpFsmPrev_Type = SnmpAdminString
_CucsExtvmmEpFsmPrev_Object = MibTableColumn
cucsExtvmmEpFsmPrev = _CucsExtvmmEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 5),
    _CucsExtvmmEpFsmPrev_Type()
)
cucsExtvmmEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmPrev.setStatus("current")
_CucsExtvmmEpFsmProgr_Type = Gauge32
_CucsExtvmmEpFsmProgr_Object = MibTableColumn
cucsExtvmmEpFsmProgr = _CucsExtvmmEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 6),
    _CucsExtvmmEpFsmProgr_Type()
)
cucsExtvmmEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmProgr.setStatus("current")
_CucsExtvmmEpFsmRmtInvErrCode_Type = Gauge32
_CucsExtvmmEpFsmRmtInvErrCode_Object = MibTableColumn
cucsExtvmmEpFsmRmtInvErrCode = _CucsExtvmmEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 7),
    _CucsExtvmmEpFsmRmtInvErrCode_Type()
)
cucsExtvmmEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmRmtInvErrCode.setStatus("current")
_CucsExtvmmEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsExtvmmEpFsmRmtInvErrDescr_Object = MibTableColumn
cucsExtvmmEpFsmRmtInvErrDescr = _CucsExtvmmEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 8),
    _CucsExtvmmEpFsmRmtInvErrDescr_Type()
)
cucsExtvmmEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmRmtInvErrDescr.setStatus("current")
_CucsExtvmmEpFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsExtvmmEpFsmRmtInvRslt_Object = MibTableColumn
cucsExtvmmEpFsmRmtInvRslt = _CucsExtvmmEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 9),
    _CucsExtvmmEpFsmRmtInvRslt_Type()
)
cucsExtvmmEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmRmtInvRslt.setStatus("current")
_CucsExtvmmEpFsmStageDescr_Type = SnmpAdminString
_CucsExtvmmEpFsmStageDescr_Object = MibTableColumn
cucsExtvmmEpFsmStageDescr = _CucsExtvmmEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 10),
    _CucsExtvmmEpFsmStageDescr_Type()
)
cucsExtvmmEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStageDescr.setStatus("current")
_CucsExtvmmEpFsmStamp_Type = DateAndTime
_CucsExtvmmEpFsmStamp_Object = MibTableColumn
cucsExtvmmEpFsmStamp = _CucsExtvmmEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 11),
    _CucsExtvmmEpFsmStamp_Type()
)
cucsExtvmmEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStamp.setStatus("current")
_CucsExtvmmEpFsmStatus_Type = SnmpAdminString
_CucsExtvmmEpFsmStatus_Object = MibTableColumn
cucsExtvmmEpFsmStatus = _CucsExtvmmEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 12),
    _CucsExtvmmEpFsmStatus_Type()
)
cucsExtvmmEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStatus.setStatus("current")
_CucsExtvmmEpFsmTry_Type = Gauge32
_CucsExtvmmEpFsmTry_Object = MibTableColumn
cucsExtvmmEpFsmTry = _CucsExtvmmEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 13),
    _CucsExtvmmEpFsmTry_Type()
)
cucsExtvmmEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmTry.setStatus("current")
_CucsExtvmmEpGenNum_Type = Gauge32
_CucsExtvmmEpGenNum_Object = MibTableColumn
cucsExtvmmEpGenNum = _CucsExtvmmEpGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 1, 1, 14),
    _CucsExtvmmEpGenNum_Type()
)
cucsExtvmmEpGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpGenNum.setStatus("current")
_CucsExtvmmKeyInstTable_Object = MibTable
cucsExtvmmKeyInstTable = _CucsExtvmmKeyInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 2)
)
if mibBuilder.loadTexts:
    cucsExtvmmKeyInstTable.setStatus("current")
_CucsExtvmmKeyInstEntry_Object = MibTableRow
cucsExtvmmKeyInstEntry = _CucsExtvmmKeyInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 2, 1)
)
cucsExtvmmKeyInstEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmKeyInstInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmKeyInstEntry.setStatus("current")
_CucsExtvmmKeyInstInstanceId_Type = CucsManagedObjectId
_CucsExtvmmKeyInstInstanceId_Object = MibTableColumn
cucsExtvmmKeyInstInstanceId = _CucsExtvmmKeyInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 2, 1, 1),
    _CucsExtvmmKeyInstInstanceId_Type()
)
cucsExtvmmKeyInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmKeyInstInstanceId.setStatus("current")
_CucsExtvmmKeyInstDn_Type = CucsManagedObjectDn
_CucsExtvmmKeyInstDn_Object = MibTableColumn
cucsExtvmmKeyInstDn = _CucsExtvmmKeyInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 2, 1, 2),
    _CucsExtvmmKeyInstDn_Type()
)
cucsExtvmmKeyInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyInstDn.setStatus("current")
_CucsExtvmmKeyInstRn_Type = SnmpAdminString
_CucsExtvmmKeyInstRn_Object = MibTableColumn
cucsExtvmmKeyInstRn = _CucsExtvmmKeyInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 2, 1, 3),
    _CucsExtvmmKeyInstRn_Type()
)
cucsExtvmmKeyInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyInstRn.setStatus("current")
_CucsExtvmmKeyInstInst_Type = Gauge32
_CucsExtvmmKeyInstInst_Object = MibTableColumn
cucsExtvmmKeyInstInst = _CucsExtvmmKeyInstInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 2, 1, 4),
    _CucsExtvmmKeyInstInst_Type()
)
cucsExtvmmKeyInstInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyInstInst.setStatus("current")
_CucsExtvmmKeyInstKey_Type = SnmpAdminString
_CucsExtvmmKeyInstKey_Object = MibTableColumn
cucsExtvmmKeyInstKey = _CucsExtvmmKeyInstKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 2, 1, 5),
    _CucsExtvmmKeyInstKey_Type()
)
cucsExtvmmKeyInstKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyInstKey.setStatus("current")
_CucsExtvmmKeyRingTable_Object = MibTable
cucsExtvmmKeyRingTable = _CucsExtvmmKeyRingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 3)
)
if mibBuilder.loadTexts:
    cucsExtvmmKeyRingTable.setStatus("current")
_CucsExtvmmKeyRingEntry_Object = MibTableRow
cucsExtvmmKeyRingEntry = _CucsExtvmmKeyRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 3, 1)
)
cucsExtvmmKeyRingEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmKeyRingInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmKeyRingEntry.setStatus("current")
_CucsExtvmmKeyRingInstanceId_Type = CucsManagedObjectId
_CucsExtvmmKeyRingInstanceId_Object = MibTableColumn
cucsExtvmmKeyRingInstanceId = _CucsExtvmmKeyRingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 3, 1, 1),
    _CucsExtvmmKeyRingInstanceId_Type()
)
cucsExtvmmKeyRingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmKeyRingInstanceId.setStatus("current")
_CucsExtvmmKeyRingDn_Type = CucsManagedObjectDn
_CucsExtvmmKeyRingDn_Object = MibTableColumn
cucsExtvmmKeyRingDn = _CucsExtvmmKeyRingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 3, 1, 2),
    _CucsExtvmmKeyRingDn_Type()
)
cucsExtvmmKeyRingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyRingDn.setStatus("current")
_CucsExtvmmKeyRingRn_Type = SnmpAdminString
_CucsExtvmmKeyRingRn_Object = MibTableColumn
cucsExtvmmKeyRingRn = _CucsExtvmmKeyRingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 3, 1, 3),
    _CucsExtvmmKeyRingRn_Type()
)
cucsExtvmmKeyRingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyRingRn.setStatus("current")
_CucsExtvmmKeyRingCertFile_Type = SnmpAdminString
_CucsExtvmmKeyRingCertFile_Object = MibTableColumn
cucsExtvmmKeyRingCertFile = _CucsExtvmmKeyRingCertFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 3, 1, 4),
    _CucsExtvmmKeyRingCertFile_Type()
)
cucsExtvmmKeyRingCertFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyRingCertFile.setStatus("current")
_CucsExtvmmKeyRingLocation_Type = CucsCommFilePathProtocol
_CucsExtvmmKeyRingLocation_Object = MibTableColumn
cucsExtvmmKeyRingLocation = _CucsExtvmmKeyRingLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 3, 1, 5),
    _CucsExtvmmKeyRingLocation_Type()
)
cucsExtvmmKeyRingLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyRingLocation.setStatus("current")
_CucsExtvmmKeyRingName_Type = SnmpAdminString
_CucsExtvmmKeyRingName_Object = MibTableColumn
cucsExtvmmKeyRingName = _CucsExtvmmKeyRingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 3, 1, 6),
    _CucsExtvmmKeyRingName_Type()
)
cucsExtvmmKeyRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyRingName.setStatus("current")
_CucsExtvmmKeyRingPath_Type = SnmpAdminString
_CucsExtvmmKeyRingPath_Object = MibTableColumn
cucsExtvmmKeyRingPath = _CucsExtvmmKeyRingPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 3, 1, 7),
    _CucsExtvmmKeyRingPath_Type()
)
cucsExtvmmKeyRingPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyRingPath.setStatus("current")
_CucsExtvmmKeyStoreTable_Object = MibTable
cucsExtvmmKeyStoreTable = _CucsExtvmmKeyStoreTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4)
)
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreTable.setStatus("current")
_CucsExtvmmKeyStoreEntry_Object = MibTableRow
cucsExtvmmKeyStoreEntry = _CucsExtvmmKeyStoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1)
)
cucsExtvmmKeyStoreEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmKeyStoreInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreEntry.setStatus("current")
_CucsExtvmmKeyStoreInstanceId_Type = CucsManagedObjectId
_CucsExtvmmKeyStoreInstanceId_Object = MibTableColumn
cucsExtvmmKeyStoreInstanceId = _CucsExtvmmKeyStoreInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 1),
    _CucsExtvmmKeyStoreInstanceId_Type()
)
cucsExtvmmKeyStoreInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreInstanceId.setStatus("current")
_CucsExtvmmKeyStoreDn_Type = CucsManagedObjectDn
_CucsExtvmmKeyStoreDn_Object = MibTableColumn
cucsExtvmmKeyStoreDn = _CucsExtvmmKeyStoreDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 2),
    _CucsExtvmmKeyStoreDn_Type()
)
cucsExtvmmKeyStoreDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreDn.setStatus("current")
_CucsExtvmmKeyStoreRn_Type = SnmpAdminString
_CucsExtvmmKeyStoreRn_Object = MibTableColumn
cucsExtvmmKeyStoreRn = _CucsExtvmmKeyStoreRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 3),
    _CucsExtvmmKeyStoreRn_Type()
)
cucsExtvmmKeyStoreRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreRn.setStatus("current")
_CucsExtvmmKeyStoreFsmDescr_Type = SnmpAdminString
_CucsExtvmmKeyStoreFsmDescr_Object = MibTableColumn
cucsExtvmmKeyStoreFsmDescr = _CucsExtvmmKeyStoreFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 4),
    _CucsExtvmmKeyStoreFsmDescr_Type()
)
cucsExtvmmKeyStoreFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmDescr.setStatus("current")
_CucsExtvmmKeyStoreFsmPrev_Type = SnmpAdminString
_CucsExtvmmKeyStoreFsmPrev_Object = MibTableColumn
cucsExtvmmKeyStoreFsmPrev = _CucsExtvmmKeyStoreFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 5),
    _CucsExtvmmKeyStoreFsmPrev_Type()
)
cucsExtvmmKeyStoreFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmPrev.setStatus("current")
_CucsExtvmmKeyStoreFsmProgr_Type = Gauge32
_CucsExtvmmKeyStoreFsmProgr_Object = MibTableColumn
cucsExtvmmKeyStoreFsmProgr = _CucsExtvmmKeyStoreFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 6),
    _CucsExtvmmKeyStoreFsmProgr_Type()
)
cucsExtvmmKeyStoreFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmProgr.setStatus("current")
_CucsExtvmmKeyStoreFsmRmtInvErrCode_Type = Gauge32
_CucsExtvmmKeyStoreFsmRmtInvErrCode_Object = MibTableColumn
cucsExtvmmKeyStoreFsmRmtInvErrCode = _CucsExtvmmKeyStoreFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 7),
    _CucsExtvmmKeyStoreFsmRmtInvErrCode_Type()
)
cucsExtvmmKeyStoreFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmRmtInvErrCode.setStatus("current")
_CucsExtvmmKeyStoreFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsExtvmmKeyStoreFsmRmtInvErrDescr_Object = MibTableColumn
cucsExtvmmKeyStoreFsmRmtInvErrDescr = _CucsExtvmmKeyStoreFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 8),
    _CucsExtvmmKeyStoreFsmRmtInvErrDescr_Type()
)
cucsExtvmmKeyStoreFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmRmtInvErrDescr.setStatus("current")
_CucsExtvmmKeyStoreFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsExtvmmKeyStoreFsmRmtInvRslt_Object = MibTableColumn
cucsExtvmmKeyStoreFsmRmtInvRslt = _CucsExtvmmKeyStoreFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 9),
    _CucsExtvmmKeyStoreFsmRmtInvRslt_Type()
)
cucsExtvmmKeyStoreFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmRmtInvRslt.setStatus("current")
_CucsExtvmmKeyStoreFsmStageDescr_Type = SnmpAdminString
_CucsExtvmmKeyStoreFsmStageDescr_Object = MibTableColumn
cucsExtvmmKeyStoreFsmStageDescr = _CucsExtvmmKeyStoreFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 10),
    _CucsExtvmmKeyStoreFsmStageDescr_Type()
)
cucsExtvmmKeyStoreFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStageDescr.setStatus("current")
_CucsExtvmmKeyStoreFsmStamp_Type = DateAndTime
_CucsExtvmmKeyStoreFsmStamp_Object = MibTableColumn
cucsExtvmmKeyStoreFsmStamp = _CucsExtvmmKeyStoreFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 11),
    _CucsExtvmmKeyStoreFsmStamp_Type()
)
cucsExtvmmKeyStoreFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStamp.setStatus("current")
_CucsExtvmmKeyStoreFsmStatus_Type = SnmpAdminString
_CucsExtvmmKeyStoreFsmStatus_Object = MibTableColumn
cucsExtvmmKeyStoreFsmStatus = _CucsExtvmmKeyStoreFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 12),
    _CucsExtvmmKeyStoreFsmStatus_Type()
)
cucsExtvmmKeyStoreFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStatus.setStatus("current")
_CucsExtvmmKeyStoreFsmTry_Type = Gauge32
_CucsExtvmmKeyStoreFsmTry_Object = MibTableColumn
cucsExtvmmKeyStoreFsmTry = _CucsExtvmmKeyStoreFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 4, 1, 13),
    _CucsExtvmmKeyStoreFsmTry_Type()
)
cucsExtvmmKeyStoreFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmTry.setStatus("current")
_CucsExtvmmKeyStoreFsmTaskTable_Object = MibTable
cucsExtvmmKeyStoreFsmTaskTable = _CucsExtvmmKeyStoreFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 5)
)
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmTaskTable.setStatus("current")
_CucsExtvmmKeyStoreFsmTaskEntry_Object = MibTableRow
cucsExtvmmKeyStoreFsmTaskEntry = _CucsExtvmmKeyStoreFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 5, 1)
)
cucsExtvmmKeyStoreFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmKeyStoreFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmTaskEntry.setStatus("current")
_CucsExtvmmKeyStoreFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsExtvmmKeyStoreFsmTaskInstanceId_Object = MibTableColumn
cucsExtvmmKeyStoreFsmTaskInstanceId = _CucsExtvmmKeyStoreFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 5, 1, 1),
    _CucsExtvmmKeyStoreFsmTaskInstanceId_Type()
)
cucsExtvmmKeyStoreFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmTaskInstanceId.setStatus("current")
_CucsExtvmmKeyStoreFsmTaskDn_Type = CucsManagedObjectDn
_CucsExtvmmKeyStoreFsmTaskDn_Object = MibTableColumn
cucsExtvmmKeyStoreFsmTaskDn = _CucsExtvmmKeyStoreFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 5, 1, 2),
    _CucsExtvmmKeyStoreFsmTaskDn_Type()
)
cucsExtvmmKeyStoreFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmTaskDn.setStatus("current")
_CucsExtvmmKeyStoreFsmTaskRn_Type = SnmpAdminString
_CucsExtvmmKeyStoreFsmTaskRn_Object = MibTableColumn
cucsExtvmmKeyStoreFsmTaskRn = _CucsExtvmmKeyStoreFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 5, 1, 3),
    _CucsExtvmmKeyStoreFsmTaskRn_Type()
)
cucsExtvmmKeyStoreFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmTaskRn.setStatus("current")
_CucsExtvmmKeyStoreFsmTaskCompletion_Type = CucsFsmCompletion
_CucsExtvmmKeyStoreFsmTaskCompletion_Object = MibTableColumn
cucsExtvmmKeyStoreFsmTaskCompletion = _CucsExtvmmKeyStoreFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 5, 1, 4),
    _CucsExtvmmKeyStoreFsmTaskCompletion_Type()
)
cucsExtvmmKeyStoreFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmTaskCompletion.setStatus("current")
_CucsExtvmmKeyStoreFsmTaskFlags_Type = CucsFsmFlags
_CucsExtvmmKeyStoreFsmTaskFlags_Object = MibTableColumn
cucsExtvmmKeyStoreFsmTaskFlags = _CucsExtvmmKeyStoreFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 5, 1, 5),
    _CucsExtvmmKeyStoreFsmTaskFlags_Type()
)
cucsExtvmmKeyStoreFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmTaskFlags.setStatus("current")
_CucsExtvmmKeyStoreFsmTaskItem_Type = CucsExtvmmKeyStoreFsmTaskItem
_CucsExtvmmKeyStoreFsmTaskItem_Object = MibTableColumn
cucsExtvmmKeyStoreFsmTaskItem = _CucsExtvmmKeyStoreFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 5, 1, 6),
    _CucsExtvmmKeyStoreFsmTaskItem_Type()
)
cucsExtvmmKeyStoreFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmTaskItem.setStatus("current")
_CucsExtvmmKeyStoreFsmTaskSeqId_Type = Gauge32
_CucsExtvmmKeyStoreFsmTaskSeqId_Object = MibTableColumn
cucsExtvmmKeyStoreFsmTaskSeqId = _CucsExtvmmKeyStoreFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 5, 1, 7),
    _CucsExtvmmKeyStoreFsmTaskSeqId_Type()
)
cucsExtvmmKeyStoreFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmTaskSeqId.setStatus("current")
_CucsExtvmmMasterExtKeyTable_Object = MibTable
cucsExtvmmMasterExtKeyTable = _CucsExtvmmMasterExtKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6)
)
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyTable.setStatus("current")
_CucsExtvmmMasterExtKeyEntry_Object = MibTableRow
cucsExtvmmMasterExtKeyEntry = _CucsExtvmmMasterExtKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1)
)
cucsExtvmmMasterExtKeyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmMasterExtKeyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyEntry.setStatus("current")
_CucsExtvmmMasterExtKeyInstanceId_Type = CucsManagedObjectId
_CucsExtvmmMasterExtKeyInstanceId_Object = MibTableColumn
cucsExtvmmMasterExtKeyInstanceId = _CucsExtvmmMasterExtKeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 1),
    _CucsExtvmmMasterExtKeyInstanceId_Type()
)
cucsExtvmmMasterExtKeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyInstanceId.setStatus("current")
_CucsExtvmmMasterExtKeyDn_Type = CucsManagedObjectDn
_CucsExtvmmMasterExtKeyDn_Object = MibTableColumn
cucsExtvmmMasterExtKeyDn = _CucsExtvmmMasterExtKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 2),
    _CucsExtvmmMasterExtKeyDn_Type()
)
cucsExtvmmMasterExtKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyDn.setStatus("current")
_CucsExtvmmMasterExtKeyRn_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyRn_Object = MibTableColumn
cucsExtvmmMasterExtKeyRn = _CucsExtvmmMasterExtKeyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 3),
    _CucsExtvmmMasterExtKeyRn_Type()
)
cucsExtvmmMasterExtKeyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyRn.setStatus("current")
_CucsExtvmmMasterExtKeyFsmDescr_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyFsmDescr_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmDescr = _CucsExtvmmMasterExtKeyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 4),
    _CucsExtvmmMasterExtKeyFsmDescr_Type()
)
cucsExtvmmMasterExtKeyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmDescr.setStatus("current")
_CucsExtvmmMasterExtKeyFsmPrev_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyFsmPrev_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmPrev = _CucsExtvmmMasterExtKeyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 5),
    _CucsExtvmmMasterExtKeyFsmPrev_Type()
)
cucsExtvmmMasterExtKeyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmPrev.setStatus("current")
_CucsExtvmmMasterExtKeyFsmProgr_Type = Gauge32
_CucsExtvmmMasterExtKeyFsmProgr_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmProgr = _CucsExtvmmMasterExtKeyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 6),
    _CucsExtvmmMasterExtKeyFsmProgr_Type()
)
cucsExtvmmMasterExtKeyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmProgr.setStatus("current")
_CucsExtvmmMasterExtKeyFsmRmtInvErrCode_Type = Gauge32
_CucsExtvmmMasterExtKeyFsmRmtInvErrCode_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmRmtInvErrCode = _CucsExtvmmMasterExtKeyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 7),
    _CucsExtvmmMasterExtKeyFsmRmtInvErrCode_Type()
)
cucsExtvmmMasterExtKeyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmRmtInvErrCode.setStatus("current")
_CucsExtvmmMasterExtKeyFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyFsmRmtInvErrDescr_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmRmtInvErrDescr = _CucsExtvmmMasterExtKeyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 8),
    _CucsExtvmmMasterExtKeyFsmRmtInvErrDescr_Type()
)
cucsExtvmmMasterExtKeyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmRmtInvErrDescr.setStatus("current")
_CucsExtvmmMasterExtKeyFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsExtvmmMasterExtKeyFsmRmtInvRslt_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmRmtInvRslt = _CucsExtvmmMasterExtKeyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 9),
    _CucsExtvmmMasterExtKeyFsmRmtInvRslt_Type()
)
cucsExtvmmMasterExtKeyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmRmtInvRslt.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStageDescr_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyFsmStageDescr_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmStageDescr = _CucsExtvmmMasterExtKeyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 10),
    _CucsExtvmmMasterExtKeyFsmStageDescr_Type()
)
cucsExtvmmMasterExtKeyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStageDescr.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStamp_Type = DateAndTime
_CucsExtvmmMasterExtKeyFsmStamp_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmStamp = _CucsExtvmmMasterExtKeyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 11),
    _CucsExtvmmMasterExtKeyFsmStamp_Type()
)
cucsExtvmmMasterExtKeyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStamp.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStatus_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyFsmStatus_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmStatus = _CucsExtvmmMasterExtKeyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 12),
    _CucsExtvmmMasterExtKeyFsmStatus_Type()
)
cucsExtvmmMasterExtKeyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStatus.setStatus("current")
_CucsExtvmmMasterExtKeyFsmTry_Type = Gauge32
_CucsExtvmmMasterExtKeyFsmTry_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmTry = _CucsExtvmmMasterExtKeyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 13),
    _CucsExtvmmMasterExtKeyFsmTry_Type()
)
cucsExtvmmMasterExtKeyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmTry.setStatus("current")
_CucsExtvmmMasterExtKeyKey_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyKey_Object = MibTableColumn
cucsExtvmmMasterExtKeyKey = _CucsExtvmmMasterExtKeyKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 6, 1, 14),
    _CucsExtvmmMasterExtKeyKey_Type()
)
cucsExtvmmMasterExtKeyKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyKey.setStatus("current")
_CucsExtvmmMasterExtKeyFsmTaskTable_Object = MibTable
cucsExtvmmMasterExtKeyFsmTaskTable = _CucsExtvmmMasterExtKeyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 7)
)
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmTaskTable.setStatus("current")
_CucsExtvmmMasterExtKeyFsmTaskEntry_Object = MibTableRow
cucsExtvmmMasterExtKeyFsmTaskEntry = _CucsExtvmmMasterExtKeyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 7, 1)
)
cucsExtvmmMasterExtKeyFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmMasterExtKeyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmTaskEntry.setStatus("current")
_CucsExtvmmMasterExtKeyFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsExtvmmMasterExtKeyFsmTaskInstanceId_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskInstanceId = _CucsExtvmmMasterExtKeyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 7, 1, 1),
    _CucsExtvmmMasterExtKeyFsmTaskInstanceId_Type()
)
cucsExtvmmMasterExtKeyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmTaskInstanceId.setStatus("current")
_CucsExtvmmMasterExtKeyFsmTaskDn_Type = CucsManagedObjectDn
_CucsExtvmmMasterExtKeyFsmTaskDn_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskDn = _CucsExtvmmMasterExtKeyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 7, 1, 2),
    _CucsExtvmmMasterExtKeyFsmTaskDn_Type()
)
cucsExtvmmMasterExtKeyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmTaskDn.setStatus("current")
_CucsExtvmmMasterExtKeyFsmTaskRn_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyFsmTaskRn_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskRn = _CucsExtvmmMasterExtKeyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 7, 1, 3),
    _CucsExtvmmMasterExtKeyFsmTaskRn_Type()
)
cucsExtvmmMasterExtKeyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmTaskRn.setStatus("current")
_CucsExtvmmMasterExtKeyFsmTaskCompletion_Type = CucsFsmCompletion
_CucsExtvmmMasterExtKeyFsmTaskCompletion_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskCompletion = _CucsExtvmmMasterExtKeyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 7, 1, 4),
    _CucsExtvmmMasterExtKeyFsmTaskCompletion_Type()
)
cucsExtvmmMasterExtKeyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmTaskCompletion.setStatus("current")
_CucsExtvmmMasterExtKeyFsmTaskFlags_Type = CucsFsmFlags
_CucsExtvmmMasterExtKeyFsmTaskFlags_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskFlags = _CucsExtvmmMasterExtKeyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 7, 1, 5),
    _CucsExtvmmMasterExtKeyFsmTaskFlags_Type()
)
cucsExtvmmMasterExtKeyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmTaskFlags.setStatus("current")
_CucsExtvmmMasterExtKeyFsmTaskItem_Type = CucsExtvmmMasterExtKeyFsmTaskItem
_CucsExtvmmMasterExtKeyFsmTaskItem_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskItem = _CucsExtvmmMasterExtKeyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 7, 1, 6),
    _CucsExtvmmMasterExtKeyFsmTaskItem_Type()
)
cucsExtvmmMasterExtKeyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmTaskItem.setStatus("current")
_CucsExtvmmMasterExtKeyFsmTaskSeqId_Type = Gauge32
_CucsExtvmmMasterExtKeyFsmTaskSeqId_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmTaskSeqId = _CucsExtvmmMasterExtKeyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 7, 1, 7),
    _CucsExtvmmMasterExtKeyFsmTaskSeqId_Type()
)
cucsExtvmmMasterExtKeyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmTaskSeqId.setStatus("current")
_CucsExtvmmProviderTable_Object = MibTable
cucsExtvmmProviderTable = _CucsExtvmmProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8)
)
if mibBuilder.loadTexts:
    cucsExtvmmProviderTable.setStatus("current")
_CucsExtvmmProviderEntry_Object = MibTableRow
cucsExtvmmProviderEntry = _CucsExtvmmProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1)
)
cucsExtvmmProviderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmProviderEntry.setStatus("current")
_CucsExtvmmProviderInstanceId_Type = CucsManagedObjectId
_CucsExtvmmProviderInstanceId_Object = MibTableColumn
cucsExtvmmProviderInstanceId = _CucsExtvmmProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 1),
    _CucsExtvmmProviderInstanceId_Type()
)
cucsExtvmmProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmProviderInstanceId.setStatus("current")
_CucsExtvmmProviderDn_Type = CucsManagedObjectDn
_CucsExtvmmProviderDn_Object = MibTableColumn
cucsExtvmmProviderDn = _CucsExtvmmProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 2),
    _CucsExtvmmProviderDn_Type()
)
cucsExtvmmProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderDn.setStatus("current")
_CucsExtvmmProviderRn_Type = SnmpAdminString
_CucsExtvmmProviderRn_Object = MibTableColumn
cucsExtvmmProviderRn = _CucsExtvmmProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 3),
    _CucsExtvmmProviderRn_Type()
)
cucsExtvmmProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderRn.setStatus("current")
_CucsExtvmmProviderCert_Type = SnmpAdminString
_CucsExtvmmProviderCert_Object = MibTableColumn
cucsExtvmmProviderCert = _CucsExtvmmProviderCert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 4),
    _CucsExtvmmProviderCert_Type()
)
cucsExtvmmProviderCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderCert.setStatus("current")
_CucsExtvmmProviderDescr_Type = SnmpAdminString
_CucsExtvmmProviderDescr_Object = MibTableColumn
cucsExtvmmProviderDescr = _CucsExtvmmProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 5),
    _CucsExtvmmProviderDescr_Type()
)
cucsExtvmmProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderDescr.setStatus("current")
_CucsExtvmmProviderFsmDescr_Type = SnmpAdminString
_CucsExtvmmProviderFsmDescr_Object = MibTableColumn
cucsExtvmmProviderFsmDescr = _CucsExtvmmProviderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 6),
    _CucsExtvmmProviderFsmDescr_Type()
)
cucsExtvmmProviderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmDescr.setStatus("current")
_CucsExtvmmProviderFsmPrev_Type = SnmpAdminString
_CucsExtvmmProviderFsmPrev_Object = MibTableColumn
cucsExtvmmProviderFsmPrev = _CucsExtvmmProviderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 7),
    _CucsExtvmmProviderFsmPrev_Type()
)
cucsExtvmmProviderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmPrev.setStatus("current")
_CucsExtvmmProviderFsmProgr_Type = Gauge32
_CucsExtvmmProviderFsmProgr_Object = MibTableColumn
cucsExtvmmProviderFsmProgr = _CucsExtvmmProviderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 8),
    _CucsExtvmmProviderFsmProgr_Type()
)
cucsExtvmmProviderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmProgr.setStatus("current")
_CucsExtvmmProviderFsmRmtInvErrCode_Type = Gauge32
_CucsExtvmmProviderFsmRmtInvErrCode_Object = MibTableColumn
cucsExtvmmProviderFsmRmtInvErrCode = _CucsExtvmmProviderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 9),
    _CucsExtvmmProviderFsmRmtInvErrCode_Type()
)
cucsExtvmmProviderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmRmtInvErrCode.setStatus("current")
_CucsExtvmmProviderFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsExtvmmProviderFsmRmtInvErrDescr_Object = MibTableColumn
cucsExtvmmProviderFsmRmtInvErrDescr = _CucsExtvmmProviderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 10),
    _CucsExtvmmProviderFsmRmtInvErrDescr_Type()
)
cucsExtvmmProviderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmRmtInvErrDescr.setStatus("current")
_CucsExtvmmProviderFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsExtvmmProviderFsmRmtInvRslt_Object = MibTableColumn
cucsExtvmmProviderFsmRmtInvRslt = _CucsExtvmmProviderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 11),
    _CucsExtvmmProviderFsmRmtInvRslt_Type()
)
cucsExtvmmProviderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmRmtInvRslt.setStatus("current")
_CucsExtvmmProviderFsmStageDescr_Type = SnmpAdminString
_CucsExtvmmProviderFsmStageDescr_Object = MibTableColumn
cucsExtvmmProviderFsmStageDescr = _CucsExtvmmProviderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 12),
    _CucsExtvmmProviderFsmStageDescr_Type()
)
cucsExtvmmProviderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStageDescr.setStatus("current")
_CucsExtvmmProviderFsmStamp_Type = DateAndTime
_CucsExtvmmProviderFsmStamp_Object = MibTableColumn
cucsExtvmmProviderFsmStamp = _CucsExtvmmProviderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 13),
    _CucsExtvmmProviderFsmStamp_Type()
)
cucsExtvmmProviderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStamp.setStatus("current")
_CucsExtvmmProviderFsmStatus_Type = SnmpAdminString
_CucsExtvmmProviderFsmStatus_Object = MibTableColumn
cucsExtvmmProviderFsmStatus = _CucsExtvmmProviderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 14),
    _CucsExtvmmProviderFsmStatus_Type()
)
cucsExtvmmProviderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStatus.setStatus("current")
_CucsExtvmmProviderFsmTry_Type = Gauge32
_CucsExtvmmProviderFsmTry_Object = MibTableColumn
cucsExtvmmProviderFsmTry = _CucsExtvmmProviderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 15),
    _CucsExtvmmProviderFsmTry_Type()
)
cucsExtvmmProviderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmTry.setStatus("current")
_CucsExtvmmProviderHost_Type = SnmpAdminString
_CucsExtvmmProviderHost_Object = MibTableColumn
cucsExtvmmProviderHost = _CucsExtvmmProviderHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 16),
    _CucsExtvmmProviderHost_Type()
)
cucsExtvmmProviderHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderHost.setStatus("current")
_CucsExtvmmProviderIntId_Type = SnmpAdminString
_CucsExtvmmProviderIntId_Object = MibTableColumn
cucsExtvmmProviderIntId = _CucsExtvmmProviderIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 17),
    _CucsExtvmmProviderIntId_Type()
)
cucsExtvmmProviderIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderIntId.setStatus("current")
_CucsExtvmmProviderKey_Type = SnmpAdminString
_CucsExtvmmProviderKey_Object = MibTableColumn
cucsExtvmmProviderKey = _CucsExtvmmProviderKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 18),
    _CucsExtvmmProviderKey_Type()
)
cucsExtvmmProviderKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderKey.setStatus("current")
_CucsExtvmmProviderName_Type = SnmpAdminString
_CucsExtvmmProviderName_Object = MibTableColumn
cucsExtvmmProviderName = _CucsExtvmmProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 19),
    _CucsExtvmmProviderName_Type()
)
cucsExtvmmProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderName.setStatus("current")
_CucsExtvmmProviderUuid_Type = SnmpAdminString
_CucsExtvmmProviderUuid_Object = MibTableColumn
cucsExtvmmProviderUuid = _CucsExtvmmProviderUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 20),
    _CucsExtvmmProviderUuid_Type()
)
cucsExtvmmProviderUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderUuid.setStatus("current")
_CucsExtvmmProviderVer_Type = CucsExtvmmVcVersion
_CucsExtvmmProviderVer_Object = MibTableColumn
cucsExtvmmProviderVer = _CucsExtvmmProviderVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 21),
    _CucsExtvmmProviderVer_Type()
)
cucsExtvmmProviderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderVer.setStatus("current")
_CucsExtvmmProviderVerRaw_Type = SnmpAdminString
_CucsExtvmmProviderVerRaw_Object = MibTableColumn
cucsExtvmmProviderVerRaw = _CucsExtvmmProviderVerRaw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 22),
    _CucsExtvmmProviderVerRaw_Type()
)
cucsExtvmmProviderVerRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderVerRaw.setStatus("current")
_CucsExtvmmProviderPolicyLevel_Type = Gauge32
_CucsExtvmmProviderPolicyLevel_Object = MibTableColumn
cucsExtvmmProviderPolicyLevel = _CucsExtvmmProviderPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 23),
    _CucsExtvmmProviderPolicyLevel_Type()
)
cucsExtvmmProviderPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderPolicyLevel.setStatus("current")
_CucsExtvmmProviderPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsExtvmmProviderPolicyOwner_Object = MibTableColumn
cucsExtvmmProviderPolicyOwner = _CucsExtvmmProviderPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 24),
    _CucsExtvmmProviderPolicyOwner_Type()
)
cucsExtvmmProviderPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderPolicyOwner.setStatus("current")
_CucsExtvmmProviderPortValue_Type = Gauge32
_CucsExtvmmProviderPortValue_Object = MibTableColumn
cucsExtvmmProviderPortValue = _CucsExtvmmProviderPortValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 25),
    _CucsExtvmmProviderPortValue_Type()
)
cucsExtvmmProviderPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderPortValue.setStatus("current")
_CucsExtvmmProviderVendorType_Type = CucsExtvmmProviderVendorType
_CucsExtvmmProviderVendorType_Object = MibTableColumn
cucsExtvmmProviderVendorType = _CucsExtvmmProviderVendorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 8, 1, 26),
    _CucsExtvmmProviderVendorType_Type()
)
cucsExtvmmProviderVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderVendorType.setStatus("current")
_CucsExtvmmProviderFsmTaskTable_Object = MibTable
cucsExtvmmProviderFsmTaskTable = _CucsExtvmmProviderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 9)
)
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmTaskTable.setStatus("current")
_CucsExtvmmProviderFsmTaskEntry_Object = MibTableRow
cucsExtvmmProviderFsmTaskEntry = _CucsExtvmmProviderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 9, 1)
)
cucsExtvmmProviderFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmProviderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmTaskEntry.setStatus("current")
_CucsExtvmmProviderFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsExtvmmProviderFsmTaskInstanceId_Object = MibTableColumn
cucsExtvmmProviderFsmTaskInstanceId = _CucsExtvmmProviderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 9, 1, 1),
    _CucsExtvmmProviderFsmTaskInstanceId_Type()
)
cucsExtvmmProviderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmTaskInstanceId.setStatus("current")
_CucsExtvmmProviderFsmTaskDn_Type = CucsManagedObjectDn
_CucsExtvmmProviderFsmTaskDn_Object = MibTableColumn
cucsExtvmmProviderFsmTaskDn = _CucsExtvmmProviderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 9, 1, 2),
    _CucsExtvmmProviderFsmTaskDn_Type()
)
cucsExtvmmProviderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmTaskDn.setStatus("current")
_CucsExtvmmProviderFsmTaskRn_Type = SnmpAdminString
_CucsExtvmmProviderFsmTaskRn_Object = MibTableColumn
cucsExtvmmProviderFsmTaskRn = _CucsExtvmmProviderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 9, 1, 3),
    _CucsExtvmmProviderFsmTaskRn_Type()
)
cucsExtvmmProviderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmTaskRn.setStatus("current")
_CucsExtvmmProviderFsmTaskCompletion_Type = CucsFsmCompletion
_CucsExtvmmProviderFsmTaskCompletion_Object = MibTableColumn
cucsExtvmmProviderFsmTaskCompletion = _CucsExtvmmProviderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 9, 1, 4),
    _CucsExtvmmProviderFsmTaskCompletion_Type()
)
cucsExtvmmProviderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmTaskCompletion.setStatus("current")
_CucsExtvmmProviderFsmTaskFlags_Type = CucsFsmFlags
_CucsExtvmmProviderFsmTaskFlags_Object = MibTableColumn
cucsExtvmmProviderFsmTaskFlags = _CucsExtvmmProviderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 9, 1, 5),
    _CucsExtvmmProviderFsmTaskFlags_Type()
)
cucsExtvmmProviderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmTaskFlags.setStatus("current")
_CucsExtvmmProviderFsmTaskItem_Type = CucsExtvmmProviderFsmTaskItem
_CucsExtvmmProviderFsmTaskItem_Object = MibTableColumn
cucsExtvmmProviderFsmTaskItem = _CucsExtvmmProviderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 9, 1, 6),
    _CucsExtvmmProviderFsmTaskItem_Type()
)
cucsExtvmmProviderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmTaskItem.setStatus("current")
_CucsExtvmmProviderFsmTaskSeqId_Type = Gauge32
_CucsExtvmmProviderFsmTaskSeqId_Object = MibTableColumn
cucsExtvmmProviderFsmTaskSeqId = _CucsExtvmmProviderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 9, 1, 7),
    _CucsExtvmmProviderFsmTaskSeqId_Type()
)
cucsExtvmmProviderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmTaskSeqId.setStatus("current")
_CucsExtvmmSwitchDelTaskTable_Object = MibTable
cucsExtvmmSwitchDelTaskTable = _CucsExtvmmSwitchDelTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10)
)
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskTable.setStatus("current")
_CucsExtvmmSwitchDelTaskEntry_Object = MibTableRow
cucsExtvmmSwitchDelTaskEntry = _CucsExtvmmSwitchDelTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1)
)
cucsExtvmmSwitchDelTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmSwitchDelTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskEntry.setStatus("current")
_CucsExtvmmSwitchDelTaskInstanceId_Type = CucsManagedObjectId
_CucsExtvmmSwitchDelTaskInstanceId_Object = MibTableColumn
cucsExtvmmSwitchDelTaskInstanceId = _CucsExtvmmSwitchDelTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 1),
    _CucsExtvmmSwitchDelTaskInstanceId_Type()
)
cucsExtvmmSwitchDelTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskInstanceId.setStatus("current")
_CucsExtvmmSwitchDelTaskDn_Type = CucsManagedObjectDn
_CucsExtvmmSwitchDelTaskDn_Object = MibTableColumn
cucsExtvmmSwitchDelTaskDn = _CucsExtvmmSwitchDelTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 2),
    _CucsExtvmmSwitchDelTaskDn_Type()
)
cucsExtvmmSwitchDelTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskDn.setStatus("current")
_CucsExtvmmSwitchDelTaskRn_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskRn_Object = MibTableColumn
cucsExtvmmSwitchDelTaskRn = _CucsExtvmmSwitchDelTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 3),
    _CucsExtvmmSwitchDelTaskRn_Type()
)
cucsExtvmmSwitchDelTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskRn.setStatus("current")
_CucsExtvmmSwitchDelTaskCertFile_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskCertFile_Object = MibTableColumn
cucsExtvmmSwitchDelTaskCertFile = _CucsExtvmmSwitchDelTaskCertFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 4),
    _CucsExtvmmSwitchDelTaskCertFile_Type()
)
cucsExtvmmSwitchDelTaskCertFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskCertFile.setStatus("current")
_CucsExtvmmSwitchDelTaskDcName_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskDcName_Object = MibTableColumn
cucsExtvmmSwitchDelTaskDcName = _CucsExtvmmSwitchDelTaskDcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 5),
    _CucsExtvmmSwitchDelTaskDcName_Type()
)
cucsExtvmmSwitchDelTaskDcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskDcName.setStatus("current")
_CucsExtvmmSwitchDelTaskDcOrg_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskDcOrg_Object = MibTableColumn
cucsExtvmmSwitchDelTaskDcOrg = _CucsExtvmmSwitchDelTaskDcOrg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 6),
    _CucsExtvmmSwitchDelTaskDcOrg_Type()
)
cucsExtvmmSwitchDelTaskDcOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskDcOrg.setStatus("current")
_CucsExtvmmSwitchDelTaskDescr_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskDescr_Object = MibTableColumn
cucsExtvmmSwitchDelTaskDescr = _CucsExtvmmSwitchDelTaskDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 7),
    _CucsExtvmmSwitchDelTaskDescr_Type()
)
cucsExtvmmSwitchDelTaskDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskDescr.setStatus("current")
_CucsExtvmmSwitchDelTaskExtKey_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskExtKey_Object = MibTableColumn
cucsExtvmmSwitchDelTaskExtKey = _CucsExtvmmSwitchDelTaskExtKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 8),
    _CucsExtvmmSwitchDelTaskExtKey_Type()
)
cucsExtvmmSwitchDelTaskExtKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskExtKey.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmDescr_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmDescr_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmDescr = _CucsExtvmmSwitchDelTaskFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 9),
    _CucsExtvmmSwitchDelTaskFsmDescr_Type()
)
cucsExtvmmSwitchDelTaskFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmDescr.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmPrev_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmPrev_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmPrev = _CucsExtvmmSwitchDelTaskFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 10),
    _CucsExtvmmSwitchDelTaskFsmPrev_Type()
)
cucsExtvmmSwitchDelTaskFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmPrev.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmProgr_Type = Gauge32
_CucsExtvmmSwitchDelTaskFsmProgr_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmProgr = _CucsExtvmmSwitchDelTaskFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 11),
    _CucsExtvmmSwitchDelTaskFsmProgr_Type()
)
cucsExtvmmSwitchDelTaskFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmProgr.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmRmtInvErrCode_Type = Gauge32
_CucsExtvmmSwitchDelTaskFsmRmtInvErrCode_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmRmtInvErrCode = _CucsExtvmmSwitchDelTaskFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 12),
    _CucsExtvmmSwitchDelTaskFsmRmtInvErrCode_Type()
)
cucsExtvmmSwitchDelTaskFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmRmtInvErrCode.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmRmtInvErrDescr_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmRmtInvErrDescr = _CucsExtvmmSwitchDelTaskFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 13),
    _CucsExtvmmSwitchDelTaskFsmRmtInvErrDescr_Type()
)
cucsExtvmmSwitchDelTaskFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmRmtInvErrDescr.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsExtvmmSwitchDelTaskFsmRmtInvRslt_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmRmtInvRslt = _CucsExtvmmSwitchDelTaskFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 14),
    _CucsExtvmmSwitchDelTaskFsmRmtInvRslt_Type()
)
cucsExtvmmSwitchDelTaskFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmRmtInvRslt.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStageDescr_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmStageDescr_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageDescr = _CucsExtvmmSwitchDelTaskFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 15),
    _CucsExtvmmSwitchDelTaskFsmStageDescr_Type()
)
cucsExtvmmSwitchDelTaskFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStageDescr.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStamp_Type = DateAndTime
_CucsExtvmmSwitchDelTaskFsmStamp_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmStamp = _CucsExtvmmSwitchDelTaskFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 16),
    _CucsExtvmmSwitchDelTaskFsmStamp_Type()
)
cucsExtvmmSwitchDelTaskFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStamp.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStatus_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmStatus_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmStatus = _CucsExtvmmSwitchDelTaskFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 17),
    _CucsExtvmmSwitchDelTaskFsmStatus_Type()
)
cucsExtvmmSwitchDelTaskFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStatus.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmTry_Type = Gauge32
_CucsExtvmmSwitchDelTaskFsmTry_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmTry = _CucsExtvmmSwitchDelTaskFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 18),
    _CucsExtvmmSwitchDelTaskFsmTry_Type()
)
cucsExtvmmSwitchDelTaskFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmTry.setStatus("current")
_CucsExtvmmSwitchDelTaskHost_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskHost_Object = MibTableColumn
cucsExtvmmSwitchDelTaskHost = _CucsExtvmmSwitchDelTaskHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 19),
    _CucsExtvmmSwitchDelTaskHost_Type()
)
cucsExtvmmSwitchDelTaskHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskHost.setStatus("current")
_CucsExtvmmSwitchDelTaskIntId_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskIntId_Object = MibTableColumn
cucsExtvmmSwitchDelTaskIntId = _CucsExtvmmSwitchDelTaskIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 20),
    _CucsExtvmmSwitchDelTaskIntId_Type()
)
cucsExtvmmSwitchDelTaskIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskIntId.setStatus("current")
_CucsExtvmmSwitchDelTaskKeyInst_Type = Gauge32
_CucsExtvmmSwitchDelTaskKeyInst_Object = MibTableColumn
cucsExtvmmSwitchDelTaskKeyInst = _CucsExtvmmSwitchDelTaskKeyInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 21),
    _CucsExtvmmSwitchDelTaskKeyInst_Type()
)
cucsExtvmmSwitchDelTaskKeyInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskKeyInst.setStatus("current")
_CucsExtvmmSwitchDelTaskName_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskName_Object = MibTableColumn
cucsExtvmmSwitchDelTaskName = _CucsExtvmmSwitchDelTaskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 22),
    _CucsExtvmmSwitchDelTaskName_Type()
)
cucsExtvmmSwitchDelTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskName.setStatus("current")
_CucsExtvmmSwitchDelTaskOrgPath_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskOrgPath_Object = MibTableColumn
cucsExtvmmSwitchDelTaskOrgPath = _CucsExtvmmSwitchDelTaskOrgPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 23),
    _CucsExtvmmSwitchDelTaskOrgPath_Type()
)
cucsExtvmmSwitchDelTaskOrgPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskOrgPath.setStatus("current")
_CucsExtvmmSwitchDelTaskProvIntId_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskProvIntId_Object = MibTableColumn
cucsExtvmmSwitchDelTaskProvIntId = _CucsExtvmmSwitchDelTaskProvIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 24),
    _CucsExtvmmSwitchDelTaskProvIntId_Type()
)
cucsExtvmmSwitchDelTaskProvIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskProvIntId.setStatus("current")
_CucsExtvmmSwitchDelTaskProvider_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskProvider_Object = MibTableColumn
cucsExtvmmSwitchDelTaskProvider = _CucsExtvmmSwitchDelTaskProvider_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 25),
    _CucsExtvmmSwitchDelTaskProvider_Type()
)
cucsExtvmmSwitchDelTaskProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskProvider.setStatus("current")
_CucsExtvmmSwitchDelTaskSwIntId_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskSwIntId_Object = MibTableColumn
cucsExtvmmSwitchDelTaskSwIntId = _CucsExtvmmSwitchDelTaskSwIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 26),
    _CucsExtvmmSwitchDelTaskSwIntId_Type()
)
cucsExtvmmSwitchDelTaskSwIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskSwIntId.setStatus("current")
_CucsExtvmmSwitchDelTaskSwName_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskSwName_Object = MibTableColumn
cucsExtvmmSwitchDelTaskSwName = _CucsExtvmmSwitchDelTaskSwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 27),
    _CucsExtvmmSwitchDelTaskSwName_Type()
)
cucsExtvmmSwitchDelTaskSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskSwName.setStatus("current")
_CucsExtvmmSwitchDelTaskPolicyLevel_Type = Gauge32
_CucsExtvmmSwitchDelTaskPolicyLevel_Object = MibTableColumn
cucsExtvmmSwitchDelTaskPolicyLevel = _CucsExtvmmSwitchDelTaskPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 28),
    _CucsExtvmmSwitchDelTaskPolicyLevel_Type()
)
cucsExtvmmSwitchDelTaskPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskPolicyLevel.setStatus("current")
_CucsExtvmmSwitchDelTaskPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsExtvmmSwitchDelTaskPolicyOwner_Object = MibTableColumn
cucsExtvmmSwitchDelTaskPolicyOwner = _CucsExtvmmSwitchDelTaskPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 29),
    _CucsExtvmmSwitchDelTaskPolicyOwner_Type()
)
cucsExtvmmSwitchDelTaskPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskPolicyOwner.setStatus("current")
_CucsExtvmmSwitchDelTaskPortValue_Type = Gauge32
_CucsExtvmmSwitchDelTaskPortValue_Object = MibTableColumn
cucsExtvmmSwitchDelTaskPortValue = _CucsExtvmmSwitchDelTaskPortValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 10, 1, 30),
    _CucsExtvmmSwitchDelTaskPortValue_Type()
)
cucsExtvmmSwitchDelTaskPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskPortValue.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmTaskTable_Object = MibTable
cucsExtvmmSwitchDelTaskFsmTaskTable = _CucsExtvmmSwitchDelTaskFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 11)
)
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmTaskTable.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmTaskEntry_Object = MibTableRow
cucsExtvmmSwitchDelTaskFsmTaskEntry = _CucsExtvmmSwitchDelTaskFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 11, 1)
)
cucsExtvmmSwitchDelTaskFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmSwitchDelTaskFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmTaskEntry.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsExtvmmSwitchDelTaskFsmTaskInstanceId_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskInstanceId = _CucsExtvmmSwitchDelTaskFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 11, 1, 1),
    _CucsExtvmmSwitchDelTaskFsmTaskInstanceId_Type()
)
cucsExtvmmSwitchDelTaskFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmTaskInstanceId.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmTaskDn_Type = CucsManagedObjectDn
_CucsExtvmmSwitchDelTaskFsmTaskDn_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskDn = _CucsExtvmmSwitchDelTaskFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 11, 1, 2),
    _CucsExtvmmSwitchDelTaskFsmTaskDn_Type()
)
cucsExtvmmSwitchDelTaskFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmTaskDn.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmTaskRn_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmTaskRn_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskRn = _CucsExtvmmSwitchDelTaskFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 11, 1, 3),
    _CucsExtvmmSwitchDelTaskFsmTaskRn_Type()
)
cucsExtvmmSwitchDelTaskFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmTaskRn.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmTaskCompletion_Type = CucsFsmCompletion
_CucsExtvmmSwitchDelTaskFsmTaskCompletion_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskCompletion = _CucsExtvmmSwitchDelTaskFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 11, 1, 4),
    _CucsExtvmmSwitchDelTaskFsmTaskCompletion_Type()
)
cucsExtvmmSwitchDelTaskFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmTaskCompletion.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmTaskFlags_Type = CucsFsmFlags
_CucsExtvmmSwitchDelTaskFsmTaskFlags_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskFlags = _CucsExtvmmSwitchDelTaskFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 11, 1, 5),
    _CucsExtvmmSwitchDelTaskFsmTaskFlags_Type()
)
cucsExtvmmSwitchDelTaskFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmTaskFlags.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmTaskItem_Type = CucsExtvmmSwitchDelTaskFsmTaskItem
_CucsExtvmmSwitchDelTaskFsmTaskItem_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskItem = _CucsExtvmmSwitchDelTaskFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 11, 1, 6),
    _CucsExtvmmSwitchDelTaskFsmTaskItem_Type()
)
cucsExtvmmSwitchDelTaskFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmTaskItem.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmTaskSeqId_Type = Gauge32
_CucsExtvmmSwitchDelTaskFsmTaskSeqId_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmTaskSeqId = _CucsExtvmmSwitchDelTaskFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 11, 1, 7),
    _CucsExtvmmSwitchDelTaskFsmTaskSeqId_Type()
)
cucsExtvmmSwitchDelTaskFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmTaskSeqId.setStatus("current")
_CucsExtvmmEpFsmTaskTable_Object = MibTable
cucsExtvmmEpFsmTaskTable = _CucsExtvmmEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 12)
)
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmTaskTable.setStatus("current")
_CucsExtvmmEpFsmTaskEntry_Object = MibTableRow
cucsExtvmmEpFsmTaskEntry = _CucsExtvmmEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 12, 1)
)
cucsExtvmmEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmTaskEntry.setStatus("current")
_CucsExtvmmEpFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsExtvmmEpFsmTaskInstanceId_Object = MibTableColumn
cucsExtvmmEpFsmTaskInstanceId = _CucsExtvmmEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 12, 1, 1),
    _CucsExtvmmEpFsmTaskInstanceId_Type()
)
cucsExtvmmEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmTaskInstanceId.setStatus("current")
_CucsExtvmmEpFsmTaskDn_Type = CucsManagedObjectDn
_CucsExtvmmEpFsmTaskDn_Object = MibTableColumn
cucsExtvmmEpFsmTaskDn = _CucsExtvmmEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 12, 1, 2),
    _CucsExtvmmEpFsmTaskDn_Type()
)
cucsExtvmmEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmTaskDn.setStatus("current")
_CucsExtvmmEpFsmTaskRn_Type = SnmpAdminString
_CucsExtvmmEpFsmTaskRn_Object = MibTableColumn
cucsExtvmmEpFsmTaskRn = _CucsExtvmmEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 12, 1, 3),
    _CucsExtvmmEpFsmTaskRn_Type()
)
cucsExtvmmEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmTaskRn.setStatus("current")
_CucsExtvmmEpFsmTaskCompletion_Type = CucsFsmCompletion
_CucsExtvmmEpFsmTaskCompletion_Object = MibTableColumn
cucsExtvmmEpFsmTaskCompletion = _CucsExtvmmEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 12, 1, 4),
    _CucsExtvmmEpFsmTaskCompletion_Type()
)
cucsExtvmmEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmTaskCompletion.setStatus("current")
_CucsExtvmmEpFsmTaskFlags_Type = CucsFsmFlags
_CucsExtvmmEpFsmTaskFlags_Object = MibTableColumn
cucsExtvmmEpFsmTaskFlags = _CucsExtvmmEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 12, 1, 5),
    _CucsExtvmmEpFsmTaskFlags_Type()
)
cucsExtvmmEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmTaskFlags.setStatus("current")
_CucsExtvmmEpFsmTaskItem_Type = CucsExtvmmEpFsmTaskItem
_CucsExtvmmEpFsmTaskItem_Object = MibTableColumn
cucsExtvmmEpFsmTaskItem = _CucsExtvmmEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 12, 1, 6),
    _CucsExtvmmEpFsmTaskItem_Type()
)
cucsExtvmmEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmTaskItem.setStatus("current")
_CucsExtvmmEpFsmTaskSeqId_Type = Gauge32
_CucsExtvmmEpFsmTaskSeqId_Object = MibTableColumn
cucsExtvmmEpFsmTaskSeqId = _CucsExtvmmEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 12, 1, 7),
    _CucsExtvmmEpFsmTaskSeqId_Type()
)
cucsExtvmmEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmTaskSeqId.setStatus("current")
_CucsExtvmmSwitchSetTable_Object = MibTable
cucsExtvmmSwitchSetTable = _CucsExtvmmSwitchSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 13)
)
if mibBuilder.loadTexts:
    cucsExtvmmSwitchSetTable.setStatus("current")
_CucsExtvmmSwitchSetEntry_Object = MibTableRow
cucsExtvmmSwitchSetEntry = _CucsExtvmmSwitchSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 13, 1)
)
cucsExtvmmSwitchSetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmSwitchSetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmSwitchSetEntry.setStatus("current")
_CucsExtvmmSwitchSetInstanceId_Type = CucsManagedObjectId
_CucsExtvmmSwitchSetInstanceId_Object = MibTableColumn
cucsExtvmmSwitchSetInstanceId = _CucsExtvmmSwitchSetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 13, 1, 1),
    _CucsExtvmmSwitchSetInstanceId_Type()
)
cucsExtvmmSwitchSetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchSetInstanceId.setStatus("current")
_CucsExtvmmSwitchSetDn_Type = CucsManagedObjectDn
_CucsExtvmmSwitchSetDn_Object = MibTableColumn
cucsExtvmmSwitchSetDn = _CucsExtvmmSwitchSetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 13, 1, 2),
    _CucsExtvmmSwitchSetDn_Type()
)
cucsExtvmmSwitchSetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchSetDn.setStatus("current")
_CucsExtvmmSwitchSetRn_Type = SnmpAdminString
_CucsExtvmmSwitchSetRn_Object = MibTableColumn
cucsExtvmmSwitchSetRn = _CucsExtvmmSwitchSetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 13, 1, 3),
    _CucsExtvmmSwitchSetRn_Type()
)
cucsExtvmmSwitchSetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchSetRn.setStatus("current")
_CucsExtvmmEpFsmTable_Object = MibTable
cucsExtvmmEpFsmTable = _CucsExtvmmEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14)
)
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmTable.setStatus("current")
_CucsExtvmmEpFsmEntry_Object = MibTableRow
cucsExtvmmEpFsmEntry = _CucsExtvmmEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14, 1)
)
cucsExtvmmEpFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmEntry.setStatus("current")
_CucsExtvmmEpFsmInstanceId_Type = CucsManagedObjectId
_CucsExtvmmEpFsmInstanceId_Object = MibTableColumn
cucsExtvmmEpFsmInstanceId = _CucsExtvmmEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14, 1, 1),
    _CucsExtvmmEpFsmInstanceId_Type()
)
cucsExtvmmEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmInstanceId.setStatus("current")
_CucsExtvmmEpFsmDn_Type = CucsManagedObjectDn
_CucsExtvmmEpFsmDn_Object = MibTableColumn
cucsExtvmmEpFsmDn = _CucsExtvmmEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14, 1, 2),
    _CucsExtvmmEpFsmDn_Type()
)
cucsExtvmmEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmDn.setStatus("current")
_CucsExtvmmEpFsmRn_Type = SnmpAdminString
_CucsExtvmmEpFsmRn_Object = MibTableColumn
cucsExtvmmEpFsmRn = _CucsExtvmmEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14, 1, 3),
    _CucsExtvmmEpFsmRn_Type()
)
cucsExtvmmEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmRn.setStatus("current")
_CucsExtvmmEpFsmCompletionTime_Type = DateAndTime
_CucsExtvmmEpFsmCompletionTime_Object = MibTableColumn
cucsExtvmmEpFsmCompletionTime = _CucsExtvmmEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14, 1, 4),
    _CucsExtvmmEpFsmCompletionTime_Type()
)
cucsExtvmmEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmCompletionTime.setStatus("current")
_CucsExtvmmEpFsmCurrentFsm_Type = CucsExtvmmEpFsmCurrentFsm
_CucsExtvmmEpFsmCurrentFsm_Object = MibTableColumn
cucsExtvmmEpFsmCurrentFsm = _CucsExtvmmEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14, 1, 5),
    _CucsExtvmmEpFsmCurrentFsm_Type()
)
cucsExtvmmEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmCurrentFsm.setStatus("current")
_CucsExtvmmEpFsmDescrData_Type = SnmpAdminString
_CucsExtvmmEpFsmDescrData_Object = MibTableColumn
cucsExtvmmEpFsmDescrData = _CucsExtvmmEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14, 1, 6),
    _CucsExtvmmEpFsmDescrData_Type()
)
cucsExtvmmEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmDescrData.setStatus("current")
_CucsExtvmmEpFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsExtvmmEpFsmFsmStatus_Object = MibTableColumn
cucsExtvmmEpFsmFsmStatus = _CucsExtvmmEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14, 1, 7),
    _CucsExtvmmEpFsmFsmStatus_Type()
)
cucsExtvmmEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmFsmStatus.setStatus("current")
_CucsExtvmmEpFsmProgress_Type = Gauge32
_CucsExtvmmEpFsmProgress_Object = MibTableColumn
cucsExtvmmEpFsmProgress = _CucsExtvmmEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14, 1, 8),
    _CucsExtvmmEpFsmProgress_Type()
)
cucsExtvmmEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmProgress.setStatus("current")
_CucsExtvmmEpFsmRmtErrCode_Type = Gauge32
_CucsExtvmmEpFsmRmtErrCode_Object = MibTableColumn
cucsExtvmmEpFsmRmtErrCode = _CucsExtvmmEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14, 1, 9),
    _CucsExtvmmEpFsmRmtErrCode_Type()
)
cucsExtvmmEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmRmtErrCode.setStatus("current")
_CucsExtvmmEpFsmRmtErrDescr_Type = SnmpAdminString
_CucsExtvmmEpFsmRmtErrDescr_Object = MibTableColumn
cucsExtvmmEpFsmRmtErrDescr = _CucsExtvmmEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14, 1, 10),
    _CucsExtvmmEpFsmRmtErrDescr_Type()
)
cucsExtvmmEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmRmtErrDescr.setStatus("current")
_CucsExtvmmEpFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsExtvmmEpFsmRmtRslt_Object = MibTableColumn
cucsExtvmmEpFsmRmtRslt = _CucsExtvmmEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 14, 1, 11),
    _CucsExtvmmEpFsmRmtRslt_Type()
)
cucsExtvmmEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmRmtRslt.setStatus("current")
_CucsExtvmmEpFsmStageTable_Object = MibTable
cucsExtvmmEpFsmStageTable = _CucsExtvmmEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 15)
)
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStageTable.setStatus("current")
_CucsExtvmmEpFsmStageEntry_Object = MibTableRow
cucsExtvmmEpFsmStageEntry = _CucsExtvmmEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 15, 1)
)
cucsExtvmmEpFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStageEntry.setStatus("current")
_CucsExtvmmEpFsmStageInstanceId_Type = CucsManagedObjectId
_CucsExtvmmEpFsmStageInstanceId_Object = MibTableColumn
cucsExtvmmEpFsmStageInstanceId = _CucsExtvmmEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 15, 1, 1),
    _CucsExtvmmEpFsmStageInstanceId_Type()
)
cucsExtvmmEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStageInstanceId.setStatus("current")
_CucsExtvmmEpFsmStageDn_Type = CucsManagedObjectDn
_CucsExtvmmEpFsmStageDn_Object = MibTableColumn
cucsExtvmmEpFsmStageDn = _CucsExtvmmEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 15, 1, 2),
    _CucsExtvmmEpFsmStageDn_Type()
)
cucsExtvmmEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStageDn.setStatus("current")
_CucsExtvmmEpFsmStageRn_Type = SnmpAdminString
_CucsExtvmmEpFsmStageRn_Object = MibTableColumn
cucsExtvmmEpFsmStageRn = _CucsExtvmmEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 15, 1, 3),
    _CucsExtvmmEpFsmStageRn_Type()
)
cucsExtvmmEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStageRn.setStatus("current")
_CucsExtvmmEpFsmStageDescrData_Type = SnmpAdminString
_CucsExtvmmEpFsmStageDescrData_Object = MibTableColumn
cucsExtvmmEpFsmStageDescrData = _CucsExtvmmEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 15, 1, 4),
    _CucsExtvmmEpFsmStageDescrData_Type()
)
cucsExtvmmEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStageDescrData.setStatus("current")
_CucsExtvmmEpFsmStageLastUpdateTime_Type = DateAndTime
_CucsExtvmmEpFsmStageLastUpdateTime_Object = MibTableColumn
cucsExtvmmEpFsmStageLastUpdateTime = _CucsExtvmmEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 15, 1, 5),
    _CucsExtvmmEpFsmStageLastUpdateTime_Type()
)
cucsExtvmmEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStageLastUpdateTime.setStatus("current")
_CucsExtvmmEpFsmStageName_Type = CucsExtvmmEpFsmStageName
_CucsExtvmmEpFsmStageName_Object = MibTableColumn
cucsExtvmmEpFsmStageName = _CucsExtvmmEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 15, 1, 6),
    _CucsExtvmmEpFsmStageName_Type()
)
cucsExtvmmEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStageName.setStatus("current")
_CucsExtvmmEpFsmStageOrder_Type = Gauge32
_CucsExtvmmEpFsmStageOrder_Object = MibTableColumn
cucsExtvmmEpFsmStageOrder = _CucsExtvmmEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 15, 1, 7),
    _CucsExtvmmEpFsmStageOrder_Type()
)
cucsExtvmmEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStageOrder.setStatus("current")
_CucsExtvmmEpFsmStageRetry_Type = Gauge32
_CucsExtvmmEpFsmStageRetry_Object = MibTableColumn
cucsExtvmmEpFsmStageRetry = _CucsExtvmmEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 15, 1, 8),
    _CucsExtvmmEpFsmStageRetry_Type()
)
cucsExtvmmEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStageRetry.setStatus("current")
_CucsExtvmmEpFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsExtvmmEpFsmStageStageStatus_Object = MibTableColumn
cucsExtvmmEpFsmStageStageStatus = _CucsExtvmmEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 15, 1, 9),
    _CucsExtvmmEpFsmStageStageStatus_Type()
)
cucsExtvmmEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmEpFsmStageStageStatus.setStatus("current")
_CucsExtvmmKeyStoreFsmTable_Object = MibTable
cucsExtvmmKeyStoreFsmTable = _CucsExtvmmKeyStoreFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16)
)
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmTable.setStatus("current")
_CucsExtvmmKeyStoreFsmEntry_Object = MibTableRow
cucsExtvmmKeyStoreFsmEntry = _CucsExtvmmKeyStoreFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16, 1)
)
cucsExtvmmKeyStoreFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmKeyStoreFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmEntry.setStatus("current")
_CucsExtvmmKeyStoreFsmInstanceId_Type = CucsManagedObjectId
_CucsExtvmmKeyStoreFsmInstanceId_Object = MibTableColumn
cucsExtvmmKeyStoreFsmInstanceId = _CucsExtvmmKeyStoreFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16, 1, 1),
    _CucsExtvmmKeyStoreFsmInstanceId_Type()
)
cucsExtvmmKeyStoreFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmInstanceId.setStatus("current")
_CucsExtvmmKeyStoreFsmDn_Type = CucsManagedObjectDn
_CucsExtvmmKeyStoreFsmDn_Object = MibTableColumn
cucsExtvmmKeyStoreFsmDn = _CucsExtvmmKeyStoreFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16, 1, 2),
    _CucsExtvmmKeyStoreFsmDn_Type()
)
cucsExtvmmKeyStoreFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmDn.setStatus("current")
_CucsExtvmmKeyStoreFsmRn_Type = SnmpAdminString
_CucsExtvmmKeyStoreFsmRn_Object = MibTableColumn
cucsExtvmmKeyStoreFsmRn = _CucsExtvmmKeyStoreFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16, 1, 3),
    _CucsExtvmmKeyStoreFsmRn_Type()
)
cucsExtvmmKeyStoreFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmRn.setStatus("current")
_CucsExtvmmKeyStoreFsmCompletionTime_Type = DateAndTime
_CucsExtvmmKeyStoreFsmCompletionTime_Object = MibTableColumn
cucsExtvmmKeyStoreFsmCompletionTime = _CucsExtvmmKeyStoreFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16, 1, 4),
    _CucsExtvmmKeyStoreFsmCompletionTime_Type()
)
cucsExtvmmKeyStoreFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmCompletionTime.setStatus("current")
_CucsExtvmmKeyStoreFsmCurrentFsm_Type = CucsExtvmmKeyStoreFsmCurrentFsm
_CucsExtvmmKeyStoreFsmCurrentFsm_Object = MibTableColumn
cucsExtvmmKeyStoreFsmCurrentFsm = _CucsExtvmmKeyStoreFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16, 1, 5),
    _CucsExtvmmKeyStoreFsmCurrentFsm_Type()
)
cucsExtvmmKeyStoreFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmCurrentFsm.setStatus("current")
_CucsExtvmmKeyStoreFsmDescrData_Type = SnmpAdminString
_CucsExtvmmKeyStoreFsmDescrData_Object = MibTableColumn
cucsExtvmmKeyStoreFsmDescrData = _CucsExtvmmKeyStoreFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16, 1, 6),
    _CucsExtvmmKeyStoreFsmDescrData_Type()
)
cucsExtvmmKeyStoreFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmDescrData.setStatus("current")
_CucsExtvmmKeyStoreFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsExtvmmKeyStoreFsmFsmStatus_Object = MibTableColumn
cucsExtvmmKeyStoreFsmFsmStatus = _CucsExtvmmKeyStoreFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16, 1, 7),
    _CucsExtvmmKeyStoreFsmFsmStatus_Type()
)
cucsExtvmmKeyStoreFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmFsmStatus.setStatus("current")
_CucsExtvmmKeyStoreFsmProgress_Type = Gauge32
_CucsExtvmmKeyStoreFsmProgress_Object = MibTableColumn
cucsExtvmmKeyStoreFsmProgress = _CucsExtvmmKeyStoreFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16, 1, 8),
    _CucsExtvmmKeyStoreFsmProgress_Type()
)
cucsExtvmmKeyStoreFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmProgress.setStatus("current")
_CucsExtvmmKeyStoreFsmRmtErrCode_Type = Gauge32
_CucsExtvmmKeyStoreFsmRmtErrCode_Object = MibTableColumn
cucsExtvmmKeyStoreFsmRmtErrCode = _CucsExtvmmKeyStoreFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16, 1, 9),
    _CucsExtvmmKeyStoreFsmRmtErrCode_Type()
)
cucsExtvmmKeyStoreFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmRmtErrCode.setStatus("current")
_CucsExtvmmKeyStoreFsmRmtErrDescr_Type = SnmpAdminString
_CucsExtvmmKeyStoreFsmRmtErrDescr_Object = MibTableColumn
cucsExtvmmKeyStoreFsmRmtErrDescr = _CucsExtvmmKeyStoreFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16, 1, 10),
    _CucsExtvmmKeyStoreFsmRmtErrDescr_Type()
)
cucsExtvmmKeyStoreFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmRmtErrDescr.setStatus("current")
_CucsExtvmmKeyStoreFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsExtvmmKeyStoreFsmRmtRslt_Object = MibTableColumn
cucsExtvmmKeyStoreFsmRmtRslt = _CucsExtvmmKeyStoreFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 16, 1, 11),
    _CucsExtvmmKeyStoreFsmRmtRslt_Type()
)
cucsExtvmmKeyStoreFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmRmtRslt.setStatus("current")
_CucsExtvmmKeyStoreFsmStageTable_Object = MibTable
cucsExtvmmKeyStoreFsmStageTable = _CucsExtvmmKeyStoreFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 17)
)
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStageTable.setStatus("current")
_CucsExtvmmKeyStoreFsmStageEntry_Object = MibTableRow
cucsExtvmmKeyStoreFsmStageEntry = _CucsExtvmmKeyStoreFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 17, 1)
)
cucsExtvmmKeyStoreFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmKeyStoreFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStageEntry.setStatus("current")
_CucsExtvmmKeyStoreFsmStageInstanceId_Type = CucsManagedObjectId
_CucsExtvmmKeyStoreFsmStageInstanceId_Object = MibTableColumn
cucsExtvmmKeyStoreFsmStageInstanceId = _CucsExtvmmKeyStoreFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 17, 1, 1),
    _CucsExtvmmKeyStoreFsmStageInstanceId_Type()
)
cucsExtvmmKeyStoreFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStageInstanceId.setStatus("current")
_CucsExtvmmKeyStoreFsmStageDn_Type = CucsManagedObjectDn
_CucsExtvmmKeyStoreFsmStageDn_Object = MibTableColumn
cucsExtvmmKeyStoreFsmStageDn = _CucsExtvmmKeyStoreFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 17, 1, 2),
    _CucsExtvmmKeyStoreFsmStageDn_Type()
)
cucsExtvmmKeyStoreFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStageDn.setStatus("current")
_CucsExtvmmKeyStoreFsmStageRn_Type = SnmpAdminString
_CucsExtvmmKeyStoreFsmStageRn_Object = MibTableColumn
cucsExtvmmKeyStoreFsmStageRn = _CucsExtvmmKeyStoreFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 17, 1, 3),
    _CucsExtvmmKeyStoreFsmStageRn_Type()
)
cucsExtvmmKeyStoreFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStageRn.setStatus("current")
_CucsExtvmmKeyStoreFsmStageDescrData_Type = SnmpAdminString
_CucsExtvmmKeyStoreFsmStageDescrData_Object = MibTableColumn
cucsExtvmmKeyStoreFsmStageDescrData = _CucsExtvmmKeyStoreFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 17, 1, 4),
    _CucsExtvmmKeyStoreFsmStageDescrData_Type()
)
cucsExtvmmKeyStoreFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStageDescrData.setStatus("current")
_CucsExtvmmKeyStoreFsmStageLastUpdateTime_Type = DateAndTime
_CucsExtvmmKeyStoreFsmStageLastUpdateTime_Object = MibTableColumn
cucsExtvmmKeyStoreFsmStageLastUpdateTime = _CucsExtvmmKeyStoreFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 17, 1, 5),
    _CucsExtvmmKeyStoreFsmStageLastUpdateTime_Type()
)
cucsExtvmmKeyStoreFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStageLastUpdateTime.setStatus("current")
_CucsExtvmmKeyStoreFsmStageName_Type = CucsExtvmmKeyStoreFsmStageName
_CucsExtvmmKeyStoreFsmStageName_Object = MibTableColumn
cucsExtvmmKeyStoreFsmStageName = _CucsExtvmmKeyStoreFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 17, 1, 6),
    _CucsExtvmmKeyStoreFsmStageName_Type()
)
cucsExtvmmKeyStoreFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStageName.setStatus("current")
_CucsExtvmmKeyStoreFsmStageOrder_Type = Gauge32
_CucsExtvmmKeyStoreFsmStageOrder_Object = MibTableColumn
cucsExtvmmKeyStoreFsmStageOrder = _CucsExtvmmKeyStoreFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 17, 1, 7),
    _CucsExtvmmKeyStoreFsmStageOrder_Type()
)
cucsExtvmmKeyStoreFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStageOrder.setStatus("current")
_CucsExtvmmKeyStoreFsmStageRetry_Type = Gauge32
_CucsExtvmmKeyStoreFsmStageRetry_Object = MibTableColumn
cucsExtvmmKeyStoreFsmStageRetry = _CucsExtvmmKeyStoreFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 17, 1, 8),
    _CucsExtvmmKeyStoreFsmStageRetry_Type()
)
cucsExtvmmKeyStoreFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStageRetry.setStatus("current")
_CucsExtvmmKeyStoreFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsExtvmmKeyStoreFsmStageStageStatus_Object = MibTableColumn
cucsExtvmmKeyStoreFsmStageStageStatus = _CucsExtvmmKeyStoreFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 17, 1, 9),
    _CucsExtvmmKeyStoreFsmStageStageStatus_Type()
)
cucsExtvmmKeyStoreFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmKeyStoreFsmStageStageStatus.setStatus("current")
_CucsExtvmmMasterExtKeyFsmTable_Object = MibTable
cucsExtvmmMasterExtKeyFsmTable = _CucsExtvmmMasterExtKeyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18)
)
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmTable.setStatus("current")
_CucsExtvmmMasterExtKeyFsmEntry_Object = MibTableRow
cucsExtvmmMasterExtKeyFsmEntry = _CucsExtvmmMasterExtKeyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18, 1)
)
cucsExtvmmMasterExtKeyFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmMasterExtKeyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmEntry.setStatus("current")
_CucsExtvmmMasterExtKeyFsmInstanceId_Type = CucsManagedObjectId
_CucsExtvmmMasterExtKeyFsmInstanceId_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmInstanceId = _CucsExtvmmMasterExtKeyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18, 1, 1),
    _CucsExtvmmMasterExtKeyFsmInstanceId_Type()
)
cucsExtvmmMasterExtKeyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmInstanceId.setStatus("current")
_CucsExtvmmMasterExtKeyFsmDn_Type = CucsManagedObjectDn
_CucsExtvmmMasterExtKeyFsmDn_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmDn = _CucsExtvmmMasterExtKeyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18, 1, 2),
    _CucsExtvmmMasterExtKeyFsmDn_Type()
)
cucsExtvmmMasterExtKeyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmDn.setStatus("current")
_CucsExtvmmMasterExtKeyFsmRn_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyFsmRn_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmRn = _CucsExtvmmMasterExtKeyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18, 1, 3),
    _CucsExtvmmMasterExtKeyFsmRn_Type()
)
cucsExtvmmMasterExtKeyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmRn.setStatus("current")
_CucsExtvmmMasterExtKeyFsmCompletionTime_Type = DateAndTime
_CucsExtvmmMasterExtKeyFsmCompletionTime_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmCompletionTime = _CucsExtvmmMasterExtKeyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18, 1, 4),
    _CucsExtvmmMasterExtKeyFsmCompletionTime_Type()
)
cucsExtvmmMasterExtKeyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmCompletionTime.setStatus("current")
_CucsExtvmmMasterExtKeyFsmCurrentFsm_Type = CucsExtvmmMasterExtKeyFsmCurrentFsm
_CucsExtvmmMasterExtKeyFsmCurrentFsm_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmCurrentFsm = _CucsExtvmmMasterExtKeyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18, 1, 5),
    _CucsExtvmmMasterExtKeyFsmCurrentFsm_Type()
)
cucsExtvmmMasterExtKeyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmCurrentFsm.setStatus("current")
_CucsExtvmmMasterExtKeyFsmDescrData_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyFsmDescrData_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmDescrData = _CucsExtvmmMasterExtKeyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18, 1, 6),
    _CucsExtvmmMasterExtKeyFsmDescrData_Type()
)
cucsExtvmmMasterExtKeyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmDescrData.setStatus("current")
_CucsExtvmmMasterExtKeyFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsExtvmmMasterExtKeyFsmFsmStatus_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmFsmStatus = _CucsExtvmmMasterExtKeyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18, 1, 7),
    _CucsExtvmmMasterExtKeyFsmFsmStatus_Type()
)
cucsExtvmmMasterExtKeyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmFsmStatus.setStatus("current")
_CucsExtvmmMasterExtKeyFsmProgress_Type = Gauge32
_CucsExtvmmMasterExtKeyFsmProgress_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmProgress = _CucsExtvmmMasterExtKeyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18, 1, 8),
    _CucsExtvmmMasterExtKeyFsmProgress_Type()
)
cucsExtvmmMasterExtKeyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmProgress.setStatus("current")
_CucsExtvmmMasterExtKeyFsmRmtErrCode_Type = Gauge32
_CucsExtvmmMasterExtKeyFsmRmtErrCode_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmRmtErrCode = _CucsExtvmmMasterExtKeyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18, 1, 9),
    _CucsExtvmmMasterExtKeyFsmRmtErrCode_Type()
)
cucsExtvmmMasterExtKeyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmRmtErrCode.setStatus("current")
_CucsExtvmmMasterExtKeyFsmRmtErrDescr_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyFsmRmtErrDescr_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmRmtErrDescr = _CucsExtvmmMasterExtKeyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18, 1, 10),
    _CucsExtvmmMasterExtKeyFsmRmtErrDescr_Type()
)
cucsExtvmmMasterExtKeyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmRmtErrDescr.setStatus("current")
_CucsExtvmmMasterExtKeyFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsExtvmmMasterExtKeyFsmRmtRslt_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmRmtRslt = _CucsExtvmmMasterExtKeyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 18, 1, 11),
    _CucsExtvmmMasterExtKeyFsmRmtRslt_Type()
)
cucsExtvmmMasterExtKeyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmRmtRslt.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStageTable_Object = MibTable
cucsExtvmmMasterExtKeyFsmStageTable = _CucsExtvmmMasterExtKeyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 19)
)
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStageTable.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStageEntry_Object = MibTableRow
cucsExtvmmMasterExtKeyFsmStageEntry = _CucsExtvmmMasterExtKeyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 19, 1)
)
cucsExtvmmMasterExtKeyFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmMasterExtKeyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStageEntry.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStageInstanceId_Type = CucsManagedObjectId
_CucsExtvmmMasterExtKeyFsmStageInstanceId_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmStageInstanceId = _CucsExtvmmMasterExtKeyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 19, 1, 1),
    _CucsExtvmmMasterExtKeyFsmStageInstanceId_Type()
)
cucsExtvmmMasterExtKeyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStageInstanceId.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStageDn_Type = CucsManagedObjectDn
_CucsExtvmmMasterExtKeyFsmStageDn_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmStageDn = _CucsExtvmmMasterExtKeyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 19, 1, 2),
    _CucsExtvmmMasterExtKeyFsmStageDn_Type()
)
cucsExtvmmMasterExtKeyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStageDn.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStageRn_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyFsmStageRn_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmStageRn = _CucsExtvmmMasterExtKeyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 19, 1, 3),
    _CucsExtvmmMasterExtKeyFsmStageRn_Type()
)
cucsExtvmmMasterExtKeyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStageRn.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStageDescrData_Type = SnmpAdminString
_CucsExtvmmMasterExtKeyFsmStageDescrData_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmStageDescrData = _CucsExtvmmMasterExtKeyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 19, 1, 4),
    _CucsExtvmmMasterExtKeyFsmStageDescrData_Type()
)
cucsExtvmmMasterExtKeyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStageDescrData.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStageLastUpdateTime_Type = DateAndTime
_CucsExtvmmMasterExtKeyFsmStageLastUpdateTime_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmStageLastUpdateTime = _CucsExtvmmMasterExtKeyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 19, 1, 5),
    _CucsExtvmmMasterExtKeyFsmStageLastUpdateTime_Type()
)
cucsExtvmmMasterExtKeyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStageLastUpdateTime.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStageName_Type = CucsExtvmmMasterExtKeyFsmStageName
_CucsExtvmmMasterExtKeyFsmStageName_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmStageName = _CucsExtvmmMasterExtKeyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 19, 1, 6),
    _CucsExtvmmMasterExtKeyFsmStageName_Type()
)
cucsExtvmmMasterExtKeyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStageName.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStageOrder_Type = Gauge32
_CucsExtvmmMasterExtKeyFsmStageOrder_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmStageOrder = _CucsExtvmmMasterExtKeyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 19, 1, 7),
    _CucsExtvmmMasterExtKeyFsmStageOrder_Type()
)
cucsExtvmmMasterExtKeyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStageOrder.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStageRetry_Type = Gauge32
_CucsExtvmmMasterExtKeyFsmStageRetry_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmStageRetry = _CucsExtvmmMasterExtKeyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 19, 1, 8),
    _CucsExtvmmMasterExtKeyFsmStageRetry_Type()
)
cucsExtvmmMasterExtKeyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStageRetry.setStatus("current")
_CucsExtvmmMasterExtKeyFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsExtvmmMasterExtKeyFsmStageStageStatus_Object = MibTableColumn
cucsExtvmmMasterExtKeyFsmStageStageStatus = _CucsExtvmmMasterExtKeyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 19, 1, 9),
    _CucsExtvmmMasterExtKeyFsmStageStageStatus_Type()
)
cucsExtvmmMasterExtKeyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmMasterExtKeyFsmStageStageStatus.setStatus("current")
_CucsExtvmmProviderFsmTable_Object = MibTable
cucsExtvmmProviderFsmTable = _CucsExtvmmProviderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20)
)
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmTable.setStatus("current")
_CucsExtvmmProviderFsmEntry_Object = MibTableRow
cucsExtvmmProviderFsmEntry = _CucsExtvmmProviderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20, 1)
)
cucsExtvmmProviderFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmProviderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmEntry.setStatus("current")
_CucsExtvmmProviderFsmInstanceId_Type = CucsManagedObjectId
_CucsExtvmmProviderFsmInstanceId_Object = MibTableColumn
cucsExtvmmProviderFsmInstanceId = _CucsExtvmmProviderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20, 1, 1),
    _CucsExtvmmProviderFsmInstanceId_Type()
)
cucsExtvmmProviderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmInstanceId.setStatus("current")
_CucsExtvmmProviderFsmDn_Type = CucsManagedObjectDn
_CucsExtvmmProviderFsmDn_Object = MibTableColumn
cucsExtvmmProviderFsmDn = _CucsExtvmmProviderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20, 1, 2),
    _CucsExtvmmProviderFsmDn_Type()
)
cucsExtvmmProviderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmDn.setStatus("current")
_CucsExtvmmProviderFsmRn_Type = SnmpAdminString
_CucsExtvmmProviderFsmRn_Object = MibTableColumn
cucsExtvmmProviderFsmRn = _CucsExtvmmProviderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20, 1, 3),
    _CucsExtvmmProviderFsmRn_Type()
)
cucsExtvmmProviderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmRn.setStatus("current")
_CucsExtvmmProviderFsmCompletionTime_Type = DateAndTime
_CucsExtvmmProviderFsmCompletionTime_Object = MibTableColumn
cucsExtvmmProviderFsmCompletionTime = _CucsExtvmmProviderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20, 1, 4),
    _CucsExtvmmProviderFsmCompletionTime_Type()
)
cucsExtvmmProviderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmCompletionTime.setStatus("current")
_CucsExtvmmProviderFsmCurrentFsm_Type = CucsExtvmmProviderFsmCurrentFsm
_CucsExtvmmProviderFsmCurrentFsm_Object = MibTableColumn
cucsExtvmmProviderFsmCurrentFsm = _CucsExtvmmProviderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20, 1, 5),
    _CucsExtvmmProviderFsmCurrentFsm_Type()
)
cucsExtvmmProviderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmCurrentFsm.setStatus("current")
_CucsExtvmmProviderFsmDescrData_Type = SnmpAdminString
_CucsExtvmmProviderFsmDescrData_Object = MibTableColumn
cucsExtvmmProviderFsmDescrData = _CucsExtvmmProviderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20, 1, 6),
    _CucsExtvmmProviderFsmDescrData_Type()
)
cucsExtvmmProviderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmDescrData.setStatus("current")
_CucsExtvmmProviderFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsExtvmmProviderFsmFsmStatus_Object = MibTableColumn
cucsExtvmmProviderFsmFsmStatus = _CucsExtvmmProviderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20, 1, 7),
    _CucsExtvmmProviderFsmFsmStatus_Type()
)
cucsExtvmmProviderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmFsmStatus.setStatus("current")
_CucsExtvmmProviderFsmProgress_Type = Gauge32
_CucsExtvmmProviderFsmProgress_Object = MibTableColumn
cucsExtvmmProviderFsmProgress = _CucsExtvmmProviderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20, 1, 8),
    _CucsExtvmmProviderFsmProgress_Type()
)
cucsExtvmmProviderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmProgress.setStatus("current")
_CucsExtvmmProviderFsmRmtErrCode_Type = Gauge32
_CucsExtvmmProviderFsmRmtErrCode_Object = MibTableColumn
cucsExtvmmProviderFsmRmtErrCode = _CucsExtvmmProviderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20, 1, 9),
    _CucsExtvmmProviderFsmRmtErrCode_Type()
)
cucsExtvmmProviderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmRmtErrCode.setStatus("current")
_CucsExtvmmProviderFsmRmtErrDescr_Type = SnmpAdminString
_CucsExtvmmProviderFsmRmtErrDescr_Object = MibTableColumn
cucsExtvmmProviderFsmRmtErrDescr = _CucsExtvmmProviderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20, 1, 10),
    _CucsExtvmmProviderFsmRmtErrDescr_Type()
)
cucsExtvmmProviderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmRmtErrDescr.setStatus("current")
_CucsExtvmmProviderFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsExtvmmProviderFsmRmtRslt_Object = MibTableColumn
cucsExtvmmProviderFsmRmtRslt = _CucsExtvmmProviderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 20, 1, 11),
    _CucsExtvmmProviderFsmRmtRslt_Type()
)
cucsExtvmmProviderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmRmtRslt.setStatus("current")
_CucsExtvmmProviderFsmStageTable_Object = MibTable
cucsExtvmmProviderFsmStageTable = _CucsExtvmmProviderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 21)
)
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStageTable.setStatus("current")
_CucsExtvmmProviderFsmStageEntry_Object = MibTableRow
cucsExtvmmProviderFsmStageEntry = _CucsExtvmmProviderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 21, 1)
)
cucsExtvmmProviderFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmProviderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStageEntry.setStatus("current")
_CucsExtvmmProviderFsmStageInstanceId_Type = CucsManagedObjectId
_CucsExtvmmProviderFsmStageInstanceId_Object = MibTableColumn
cucsExtvmmProviderFsmStageInstanceId = _CucsExtvmmProviderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 21, 1, 1),
    _CucsExtvmmProviderFsmStageInstanceId_Type()
)
cucsExtvmmProviderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStageInstanceId.setStatus("current")
_CucsExtvmmProviderFsmStageDn_Type = CucsManagedObjectDn
_CucsExtvmmProviderFsmStageDn_Object = MibTableColumn
cucsExtvmmProviderFsmStageDn = _CucsExtvmmProviderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 21, 1, 2),
    _CucsExtvmmProviderFsmStageDn_Type()
)
cucsExtvmmProviderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStageDn.setStatus("current")
_CucsExtvmmProviderFsmStageRn_Type = SnmpAdminString
_CucsExtvmmProviderFsmStageRn_Object = MibTableColumn
cucsExtvmmProviderFsmStageRn = _CucsExtvmmProviderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 21, 1, 3),
    _CucsExtvmmProviderFsmStageRn_Type()
)
cucsExtvmmProviderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStageRn.setStatus("current")
_CucsExtvmmProviderFsmStageDescrData_Type = SnmpAdminString
_CucsExtvmmProviderFsmStageDescrData_Object = MibTableColumn
cucsExtvmmProviderFsmStageDescrData = _CucsExtvmmProviderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 21, 1, 4),
    _CucsExtvmmProviderFsmStageDescrData_Type()
)
cucsExtvmmProviderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStageDescrData.setStatus("current")
_CucsExtvmmProviderFsmStageLastUpdateTime_Type = DateAndTime
_CucsExtvmmProviderFsmStageLastUpdateTime_Object = MibTableColumn
cucsExtvmmProviderFsmStageLastUpdateTime = _CucsExtvmmProviderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 21, 1, 5),
    _CucsExtvmmProviderFsmStageLastUpdateTime_Type()
)
cucsExtvmmProviderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStageLastUpdateTime.setStatus("current")
_CucsExtvmmProviderFsmStageName_Type = CucsExtvmmProviderFsmStageName
_CucsExtvmmProviderFsmStageName_Object = MibTableColumn
cucsExtvmmProviderFsmStageName = _CucsExtvmmProviderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 21, 1, 6),
    _CucsExtvmmProviderFsmStageName_Type()
)
cucsExtvmmProviderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStageName.setStatus("current")
_CucsExtvmmProviderFsmStageOrder_Type = Gauge32
_CucsExtvmmProviderFsmStageOrder_Object = MibTableColumn
cucsExtvmmProviderFsmStageOrder = _CucsExtvmmProviderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 21, 1, 7),
    _CucsExtvmmProviderFsmStageOrder_Type()
)
cucsExtvmmProviderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStageOrder.setStatus("current")
_CucsExtvmmProviderFsmStageRetry_Type = Gauge32
_CucsExtvmmProviderFsmStageRetry_Object = MibTableColumn
cucsExtvmmProviderFsmStageRetry = _CucsExtvmmProviderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 21, 1, 8),
    _CucsExtvmmProviderFsmStageRetry_Type()
)
cucsExtvmmProviderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStageRetry.setStatus("current")
_CucsExtvmmProviderFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsExtvmmProviderFsmStageStageStatus_Object = MibTableColumn
cucsExtvmmProviderFsmStageStageStatus = _CucsExtvmmProviderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 21, 1, 9),
    _CucsExtvmmProviderFsmStageStageStatus_Type()
)
cucsExtvmmProviderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmProviderFsmStageStageStatus.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmTable_Object = MibTable
cucsExtvmmSwitchDelTaskFsmTable = _CucsExtvmmSwitchDelTaskFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22)
)
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmTable.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmEntry_Object = MibTableRow
cucsExtvmmSwitchDelTaskFsmEntry = _CucsExtvmmSwitchDelTaskFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22, 1)
)
cucsExtvmmSwitchDelTaskFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmSwitchDelTaskFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmEntry.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmInstanceId_Type = CucsManagedObjectId
_CucsExtvmmSwitchDelTaskFsmInstanceId_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmInstanceId = _CucsExtvmmSwitchDelTaskFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22, 1, 1),
    _CucsExtvmmSwitchDelTaskFsmInstanceId_Type()
)
cucsExtvmmSwitchDelTaskFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmInstanceId.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmDn_Type = CucsManagedObjectDn
_CucsExtvmmSwitchDelTaskFsmDn_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmDn = _CucsExtvmmSwitchDelTaskFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22, 1, 2),
    _CucsExtvmmSwitchDelTaskFsmDn_Type()
)
cucsExtvmmSwitchDelTaskFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmDn.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmRn_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmRn_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmRn = _CucsExtvmmSwitchDelTaskFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22, 1, 3),
    _CucsExtvmmSwitchDelTaskFsmRn_Type()
)
cucsExtvmmSwitchDelTaskFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmRn.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmCompletionTime_Type = DateAndTime
_CucsExtvmmSwitchDelTaskFsmCompletionTime_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmCompletionTime = _CucsExtvmmSwitchDelTaskFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22, 1, 4),
    _CucsExtvmmSwitchDelTaskFsmCompletionTime_Type()
)
cucsExtvmmSwitchDelTaskFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmCompletionTime.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmCurrentFsm_Type = CucsExtvmmSwitchDelTaskFsmCurrentFsm
_CucsExtvmmSwitchDelTaskFsmCurrentFsm_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmCurrentFsm = _CucsExtvmmSwitchDelTaskFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22, 1, 5),
    _CucsExtvmmSwitchDelTaskFsmCurrentFsm_Type()
)
cucsExtvmmSwitchDelTaskFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmCurrentFsm.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmDescrData_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmDescrData_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmDescrData = _CucsExtvmmSwitchDelTaskFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22, 1, 6),
    _CucsExtvmmSwitchDelTaskFsmDescrData_Type()
)
cucsExtvmmSwitchDelTaskFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmDescrData.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsExtvmmSwitchDelTaskFsmFsmStatus_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmFsmStatus = _CucsExtvmmSwitchDelTaskFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22, 1, 7),
    _CucsExtvmmSwitchDelTaskFsmFsmStatus_Type()
)
cucsExtvmmSwitchDelTaskFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmFsmStatus.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmProgress_Type = Gauge32
_CucsExtvmmSwitchDelTaskFsmProgress_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmProgress = _CucsExtvmmSwitchDelTaskFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22, 1, 8),
    _CucsExtvmmSwitchDelTaskFsmProgress_Type()
)
cucsExtvmmSwitchDelTaskFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmProgress.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmRmtErrCode_Type = Gauge32
_CucsExtvmmSwitchDelTaskFsmRmtErrCode_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmRmtErrCode = _CucsExtvmmSwitchDelTaskFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22, 1, 9),
    _CucsExtvmmSwitchDelTaskFsmRmtErrCode_Type()
)
cucsExtvmmSwitchDelTaskFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmRmtErrCode.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmRmtErrDescr_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmRmtErrDescr_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmRmtErrDescr = _CucsExtvmmSwitchDelTaskFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22, 1, 10),
    _CucsExtvmmSwitchDelTaskFsmRmtErrDescr_Type()
)
cucsExtvmmSwitchDelTaskFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmRmtErrDescr.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsExtvmmSwitchDelTaskFsmRmtRslt_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmRmtRslt = _CucsExtvmmSwitchDelTaskFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 22, 1, 11),
    _CucsExtvmmSwitchDelTaskFsmRmtRslt_Type()
)
cucsExtvmmSwitchDelTaskFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmRmtRslt.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStageTable_Object = MibTable
cucsExtvmmSwitchDelTaskFsmStageTable = _CucsExtvmmSwitchDelTaskFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 23)
)
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStageTable.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStageEntry_Object = MibTableRow
cucsExtvmmSwitchDelTaskFsmStageEntry = _CucsExtvmmSwitchDelTaskFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 23, 1)
)
cucsExtvmmSwitchDelTaskFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmSwitchDelTaskFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStageEntry.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStageInstanceId_Type = CucsManagedObjectId
_CucsExtvmmSwitchDelTaskFsmStageInstanceId_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageInstanceId = _CucsExtvmmSwitchDelTaskFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 23, 1, 1),
    _CucsExtvmmSwitchDelTaskFsmStageInstanceId_Type()
)
cucsExtvmmSwitchDelTaskFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStageInstanceId.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStageDn_Type = CucsManagedObjectDn
_CucsExtvmmSwitchDelTaskFsmStageDn_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageDn = _CucsExtvmmSwitchDelTaskFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 23, 1, 2),
    _CucsExtvmmSwitchDelTaskFsmStageDn_Type()
)
cucsExtvmmSwitchDelTaskFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStageDn.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStageRn_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmStageRn_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageRn = _CucsExtvmmSwitchDelTaskFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 23, 1, 3),
    _CucsExtvmmSwitchDelTaskFsmStageRn_Type()
)
cucsExtvmmSwitchDelTaskFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStageRn.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStageDescrData_Type = SnmpAdminString
_CucsExtvmmSwitchDelTaskFsmStageDescrData_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageDescrData = _CucsExtvmmSwitchDelTaskFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 23, 1, 4),
    _CucsExtvmmSwitchDelTaskFsmStageDescrData_Type()
)
cucsExtvmmSwitchDelTaskFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStageDescrData.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStageLastUpdateTime_Type = DateAndTime
_CucsExtvmmSwitchDelTaskFsmStageLastUpdateTime_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageLastUpdateTime = _CucsExtvmmSwitchDelTaskFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 23, 1, 5),
    _CucsExtvmmSwitchDelTaskFsmStageLastUpdateTime_Type()
)
cucsExtvmmSwitchDelTaskFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStageLastUpdateTime.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStageName_Type = CucsExtvmmSwitchDelTaskFsmStageName
_CucsExtvmmSwitchDelTaskFsmStageName_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageName = _CucsExtvmmSwitchDelTaskFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 23, 1, 6),
    _CucsExtvmmSwitchDelTaskFsmStageName_Type()
)
cucsExtvmmSwitchDelTaskFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStageName.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStageOrder_Type = Gauge32
_CucsExtvmmSwitchDelTaskFsmStageOrder_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageOrder = _CucsExtvmmSwitchDelTaskFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 23, 1, 7),
    _CucsExtvmmSwitchDelTaskFsmStageOrder_Type()
)
cucsExtvmmSwitchDelTaskFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStageOrder.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStageRetry_Type = Gauge32
_CucsExtvmmSwitchDelTaskFsmStageRetry_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageRetry = _CucsExtvmmSwitchDelTaskFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 23, 1, 8),
    _CucsExtvmmSwitchDelTaskFsmStageRetry_Type()
)
cucsExtvmmSwitchDelTaskFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStageRetry.setStatus("current")
_CucsExtvmmSwitchDelTaskFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsExtvmmSwitchDelTaskFsmStageStageStatus_Object = MibTableColumn
cucsExtvmmSwitchDelTaskFsmStageStageStatus = _CucsExtvmmSwitchDelTaskFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 23, 1, 9),
    _CucsExtvmmSwitchDelTaskFsmStageStageStatus_Type()
)
cucsExtvmmSwitchDelTaskFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmSwitchDelTaskFsmStageStageStatus.setStatus("current")
_CucsExtvmmFNDReferenceTable_Object = MibTable
cucsExtvmmFNDReferenceTable = _CucsExtvmmFNDReferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 24)
)
if mibBuilder.loadTexts:
    cucsExtvmmFNDReferenceTable.setStatus("current")
_CucsExtvmmFNDReferenceEntry_Object = MibTableRow
cucsExtvmmFNDReferenceEntry = _CucsExtvmmFNDReferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 24, 1)
)
cucsExtvmmFNDReferenceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmFNDReferenceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmFNDReferenceEntry.setStatus("current")
_CucsExtvmmFNDReferenceInstanceId_Type = CucsManagedObjectId
_CucsExtvmmFNDReferenceInstanceId_Object = MibTableColumn
cucsExtvmmFNDReferenceInstanceId = _CucsExtvmmFNDReferenceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 24, 1, 1),
    _CucsExtvmmFNDReferenceInstanceId_Type()
)
cucsExtvmmFNDReferenceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmFNDReferenceInstanceId.setStatus("current")
_CucsExtvmmFNDReferenceDn_Type = CucsManagedObjectDn
_CucsExtvmmFNDReferenceDn_Object = MibTableColumn
cucsExtvmmFNDReferenceDn = _CucsExtvmmFNDReferenceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 24, 1, 2),
    _CucsExtvmmFNDReferenceDn_Type()
)
cucsExtvmmFNDReferenceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFNDReferenceDn.setStatus("current")
_CucsExtvmmFNDReferenceRn_Type = SnmpAdminString
_CucsExtvmmFNDReferenceRn_Object = MibTableColumn
cucsExtvmmFNDReferenceRn = _CucsExtvmmFNDReferenceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 24, 1, 3),
    _CucsExtvmmFNDReferenceRn_Type()
)
cucsExtvmmFNDReferenceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFNDReferenceRn.setStatus("current")
_CucsExtvmmFNDReferenceDescr_Type = SnmpAdminString
_CucsExtvmmFNDReferenceDescr_Object = MibTableColumn
cucsExtvmmFNDReferenceDescr = _CucsExtvmmFNDReferenceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 24, 1, 4),
    _CucsExtvmmFNDReferenceDescr_Type()
)
cucsExtvmmFNDReferenceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFNDReferenceDescr.setStatus("current")
_CucsExtvmmFNDReferenceFnDefName_Type = SnmpAdminString
_CucsExtvmmFNDReferenceFnDefName_Object = MibTableColumn
cucsExtvmmFNDReferenceFnDefName = _CucsExtvmmFNDReferenceFnDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 24, 1, 5),
    _CucsExtvmmFNDReferenceFnDefName_Type()
)
cucsExtvmmFNDReferenceFnDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFNDReferenceFnDefName.setStatus("current")
_CucsExtvmmFNDReferenceIntId_Type = SnmpAdminString
_CucsExtvmmFNDReferenceIntId_Object = MibTableColumn
cucsExtvmmFNDReferenceIntId = _CucsExtvmmFNDReferenceIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 24, 1, 6),
    _CucsExtvmmFNDReferenceIntId_Type()
)
cucsExtvmmFNDReferenceIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFNDReferenceIntId.setStatus("current")
_CucsExtvmmFNDReferenceName_Type = SnmpAdminString
_CucsExtvmmFNDReferenceName_Object = MibTableColumn
cucsExtvmmFNDReferenceName = _CucsExtvmmFNDReferenceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 24, 1, 7),
    _CucsExtvmmFNDReferenceName_Type()
)
cucsExtvmmFNDReferenceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFNDReferenceName.setStatus("current")
_CucsExtvmmFNDReferenceOperFnDefName_Type = SnmpAdminString
_CucsExtvmmFNDReferenceOperFnDefName_Object = MibTableColumn
cucsExtvmmFNDReferenceOperFnDefName = _CucsExtvmmFNDReferenceOperFnDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 24, 1, 8),
    _CucsExtvmmFNDReferenceOperFnDefName_Type()
)
cucsExtvmmFNDReferenceOperFnDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFNDReferenceOperFnDefName.setStatus("current")
_CucsExtvmmFNDReferencePolicyLevel_Type = Gauge32
_CucsExtvmmFNDReferencePolicyLevel_Object = MibTableColumn
cucsExtvmmFNDReferencePolicyLevel = _CucsExtvmmFNDReferencePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 24, 1, 9),
    _CucsExtvmmFNDReferencePolicyLevel_Type()
)
cucsExtvmmFNDReferencePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFNDReferencePolicyLevel.setStatus("current")
_CucsExtvmmFNDReferencePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsExtvmmFNDReferencePolicyOwner_Object = MibTableColumn
cucsExtvmmFNDReferencePolicyOwner = _CucsExtvmmFNDReferencePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 24, 1, 10),
    _CucsExtvmmFNDReferencePolicyOwner_Type()
)
cucsExtvmmFNDReferencePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFNDReferencePolicyOwner.setStatus("current")
_CucsExtvmmFabricNetworkTable_Object = MibTable
cucsExtvmmFabricNetworkTable = _CucsExtvmmFabricNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25)
)
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkTable.setStatus("current")
_CucsExtvmmFabricNetworkEntry_Object = MibTableRow
cucsExtvmmFabricNetworkEntry = _CucsExtvmmFabricNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25, 1)
)
cucsExtvmmFabricNetworkEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmFabricNetworkInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkEntry.setStatus("current")
_CucsExtvmmFabricNetworkInstanceId_Type = CucsManagedObjectId
_CucsExtvmmFabricNetworkInstanceId_Object = MibTableColumn
cucsExtvmmFabricNetworkInstanceId = _CucsExtvmmFabricNetworkInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25, 1, 1),
    _CucsExtvmmFabricNetworkInstanceId_Type()
)
cucsExtvmmFabricNetworkInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkInstanceId.setStatus("current")
_CucsExtvmmFabricNetworkDn_Type = CucsManagedObjectDn
_CucsExtvmmFabricNetworkDn_Object = MibTableColumn
cucsExtvmmFabricNetworkDn = _CucsExtvmmFabricNetworkDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25, 1, 2),
    _CucsExtvmmFabricNetworkDn_Type()
)
cucsExtvmmFabricNetworkDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDn.setStatus("current")
_CucsExtvmmFabricNetworkRn_Type = SnmpAdminString
_CucsExtvmmFabricNetworkRn_Object = MibTableColumn
cucsExtvmmFabricNetworkRn = _CucsExtvmmFabricNetworkRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25, 1, 3),
    _CucsExtvmmFabricNetworkRn_Type()
)
cucsExtvmmFabricNetworkRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkRn.setStatus("current")
_CucsExtvmmFabricNetworkDescr_Type = SnmpAdminString
_CucsExtvmmFabricNetworkDescr_Object = MibTableColumn
cucsExtvmmFabricNetworkDescr = _CucsExtvmmFabricNetworkDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25, 1, 4),
    _CucsExtvmmFabricNetworkDescr_Type()
)
cucsExtvmmFabricNetworkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDescr.setStatus("current")
_CucsExtvmmFabricNetworkGuid_Type = SnmpAdminString
_CucsExtvmmFabricNetworkGuid_Object = MibTableColumn
cucsExtvmmFabricNetworkGuid = _CucsExtvmmFabricNetworkGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25, 1, 5),
    _CucsExtvmmFabricNetworkGuid_Type()
)
cucsExtvmmFabricNetworkGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkGuid.setStatus("current")
_CucsExtvmmFabricNetworkIntId_Type = SnmpAdminString
_CucsExtvmmFabricNetworkIntId_Object = MibTableColumn
cucsExtvmmFabricNetworkIntId = _CucsExtvmmFabricNetworkIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25, 1, 6),
    _CucsExtvmmFabricNetworkIntId_Type()
)
cucsExtvmmFabricNetworkIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkIntId.setStatus("current")
_CucsExtvmmFabricNetworkName_Type = SnmpAdminString
_CucsExtvmmFabricNetworkName_Object = MibTableColumn
cucsExtvmmFabricNetworkName = _CucsExtvmmFabricNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25, 1, 7),
    _CucsExtvmmFabricNetworkName_Type()
)
cucsExtvmmFabricNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkName.setStatus("current")
_CucsExtvmmFabricNetworkNetworkType_Type = CucsExtvmmFabricNetworkType
_CucsExtvmmFabricNetworkNetworkType_Object = MibTableColumn
cucsExtvmmFabricNetworkNetworkType = _CucsExtvmmFabricNetworkNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25, 1, 8),
    _CucsExtvmmFabricNetworkNetworkType_Type()
)
cucsExtvmmFabricNetworkNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkNetworkType.setStatus("current")
_CucsExtvmmFabricNetworkPolicyLevel_Type = Gauge32
_CucsExtvmmFabricNetworkPolicyLevel_Object = MibTableColumn
cucsExtvmmFabricNetworkPolicyLevel = _CucsExtvmmFabricNetworkPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25, 1, 9),
    _CucsExtvmmFabricNetworkPolicyLevel_Type()
)
cucsExtvmmFabricNetworkPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkPolicyLevel.setStatus("current")
_CucsExtvmmFabricNetworkPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsExtvmmFabricNetworkPolicyOwner_Object = MibTableColumn
cucsExtvmmFabricNetworkPolicyOwner = _CucsExtvmmFabricNetworkPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25, 1, 10),
    _CucsExtvmmFabricNetworkPolicyOwner_Type()
)
cucsExtvmmFabricNetworkPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkPolicyOwner.setStatus("current")
_CucsExtvmmFabricNetworkRefOperState_Type = CucsExtvmmRefOperState
_CucsExtvmmFabricNetworkRefOperState_Object = MibTableColumn
cucsExtvmmFabricNetworkRefOperState = _CucsExtvmmFabricNetworkRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 25, 1, 11),
    _CucsExtvmmFabricNetworkRefOperState_Type()
)
cucsExtvmmFabricNetworkRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkRefOperState.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionTable_Object = MibTable
cucsExtvmmFabricNetworkDefinitionTable = _CucsExtvmmFabricNetworkDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26)
)
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionTable.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionEntry_Object = MibTableRow
cucsExtvmmFabricNetworkDefinitionEntry = _CucsExtvmmFabricNetworkDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1)
)
cucsExtvmmFabricNetworkDefinitionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmFabricNetworkDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionEntry.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionInstanceId_Type = CucsManagedObjectId
_CucsExtvmmFabricNetworkDefinitionInstanceId_Object = MibTableColumn
cucsExtvmmFabricNetworkDefinitionInstanceId = _CucsExtvmmFabricNetworkDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1, 1),
    _CucsExtvmmFabricNetworkDefinitionInstanceId_Type()
)
cucsExtvmmFabricNetworkDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionInstanceId.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionDn_Type = CucsManagedObjectDn
_CucsExtvmmFabricNetworkDefinitionDn_Object = MibTableColumn
cucsExtvmmFabricNetworkDefinitionDn = _CucsExtvmmFabricNetworkDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1, 2),
    _CucsExtvmmFabricNetworkDefinitionDn_Type()
)
cucsExtvmmFabricNetworkDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionDn.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionRn_Type = SnmpAdminString
_CucsExtvmmFabricNetworkDefinitionRn_Object = MibTableColumn
cucsExtvmmFabricNetworkDefinitionRn = _CucsExtvmmFabricNetworkDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1, 3),
    _CucsExtvmmFabricNetworkDefinitionRn_Type()
)
cucsExtvmmFabricNetworkDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionRn.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionAllowedVnicType_Type = CucsExtvmmVnicType
_CucsExtvmmFabricNetworkDefinitionAllowedVnicType_Object = MibTableColumn
cucsExtvmmFabricNetworkDefinitionAllowedVnicType = _CucsExtvmmFabricNetworkDefinitionAllowedVnicType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1, 4),
    _CucsExtvmmFabricNetworkDefinitionAllowedVnicType_Type()
)
cucsExtvmmFabricNetworkDefinitionAllowedVnicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionAllowedVnicType.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionDescr_Type = SnmpAdminString
_CucsExtvmmFabricNetworkDefinitionDescr_Object = MibTableColumn
cucsExtvmmFabricNetworkDefinitionDescr = _CucsExtvmmFabricNetworkDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1, 5),
    _CucsExtvmmFabricNetworkDefinitionDescr_Type()
)
cucsExtvmmFabricNetworkDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionDescr.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionGuid_Type = SnmpAdminString
_CucsExtvmmFabricNetworkDefinitionGuid_Object = MibTableColumn
cucsExtvmmFabricNetworkDefinitionGuid = _CucsExtvmmFabricNetworkDefinitionGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1, 6),
    _CucsExtvmmFabricNetworkDefinitionGuid_Type()
)
cucsExtvmmFabricNetworkDefinitionGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionGuid.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionIntId_Type = SnmpAdminString
_CucsExtvmmFabricNetworkDefinitionIntId_Object = MibTableColumn
cucsExtvmmFabricNetworkDefinitionIntId = _CucsExtvmmFabricNetworkDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1, 7),
    _CucsExtvmmFabricNetworkDefinitionIntId_Type()
)
cucsExtvmmFabricNetworkDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionIntId.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionName_Type = SnmpAdminString
_CucsExtvmmFabricNetworkDefinitionName_Object = MibTableColumn
cucsExtvmmFabricNetworkDefinitionName = _CucsExtvmmFabricNetworkDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1, 8),
    _CucsExtvmmFabricNetworkDefinitionName_Type()
)
cucsExtvmmFabricNetworkDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionName.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionPolicyLevel_Type = Gauge32
_CucsExtvmmFabricNetworkDefinitionPolicyLevel_Object = MibTableColumn
cucsExtvmmFabricNetworkDefinitionPolicyLevel = _CucsExtvmmFabricNetworkDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1, 9),
    _CucsExtvmmFabricNetworkDefinitionPolicyLevel_Type()
)
cucsExtvmmFabricNetworkDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionPolicyLevel.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsExtvmmFabricNetworkDefinitionPolicyOwner_Object = MibTableColumn
cucsExtvmmFabricNetworkDefinitionPolicyOwner = _CucsExtvmmFabricNetworkDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1, 10),
    _CucsExtvmmFabricNetworkDefinitionPolicyOwner_Type()
)
cucsExtvmmFabricNetworkDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionPolicyOwner.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionPrimaryVlanId_Type = Gauge32
_CucsExtvmmFabricNetworkDefinitionPrimaryVlanId_Object = MibTableColumn
cucsExtvmmFabricNetworkDefinitionPrimaryVlanId = _CucsExtvmmFabricNetworkDefinitionPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1, 11),
    _CucsExtvmmFabricNetworkDefinitionPrimaryVlanId_Type()
)
cucsExtvmmFabricNetworkDefinitionPrimaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionPrimaryVlanId.setStatus("current")
_CucsExtvmmFabricNetworkDefinitionRefOperState_Type = CucsExtvmmRefOperState
_CucsExtvmmFabricNetworkDefinitionRefOperState_Object = MibTableColumn
cucsExtvmmFabricNetworkDefinitionRefOperState = _CucsExtvmmFabricNetworkDefinitionRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 26, 1, 12),
    _CucsExtvmmFabricNetworkDefinitionRefOperState_Type()
)
cucsExtvmmFabricNetworkDefinitionRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmFabricNetworkDefinitionRefOperState.setStatus("current")
_CucsExtvmmNetworkSetsTable_Object = MibTable
cucsExtvmmNetworkSetsTable = _CucsExtvmmNetworkSetsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27)
)
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsTable.setStatus("current")
_CucsExtvmmNetworkSetsEntry_Object = MibTableRow
cucsExtvmmNetworkSetsEntry = _CucsExtvmmNetworkSetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1)
)
cucsExtvmmNetworkSetsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmNetworkSetsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsEntry.setStatus("current")
_CucsExtvmmNetworkSetsInstanceId_Type = CucsManagedObjectId
_CucsExtvmmNetworkSetsInstanceId_Object = MibTableColumn
cucsExtvmmNetworkSetsInstanceId = _CucsExtvmmNetworkSetsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 1),
    _CucsExtvmmNetworkSetsInstanceId_Type()
)
cucsExtvmmNetworkSetsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsInstanceId.setStatus("current")
_CucsExtvmmNetworkSetsDn_Type = CucsManagedObjectDn
_CucsExtvmmNetworkSetsDn_Object = MibTableColumn
cucsExtvmmNetworkSetsDn = _CucsExtvmmNetworkSetsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 2),
    _CucsExtvmmNetworkSetsDn_Type()
)
cucsExtvmmNetworkSetsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsDn.setStatus("current")
_CucsExtvmmNetworkSetsRn_Type = SnmpAdminString
_CucsExtvmmNetworkSetsRn_Object = MibTableColumn
cucsExtvmmNetworkSetsRn = _CucsExtvmmNetworkSetsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 3),
    _CucsExtvmmNetworkSetsRn_Type()
)
cucsExtvmmNetworkSetsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsRn.setStatus("current")
_CucsExtvmmNetworkSetsFltAggr_Type = Unsigned64
_CucsExtvmmNetworkSetsFltAggr_Object = MibTableColumn
cucsExtvmmNetworkSetsFltAggr = _CucsExtvmmNetworkSetsFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 4),
    _CucsExtvmmNetworkSetsFltAggr_Type()
)
cucsExtvmmNetworkSetsFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFltAggr.setStatus("current")
_CucsExtvmmNetworkSetsFsmDescr_Type = SnmpAdminString
_CucsExtvmmNetworkSetsFsmDescr_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmDescr = _CucsExtvmmNetworkSetsFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 5),
    _CucsExtvmmNetworkSetsFsmDescr_Type()
)
cucsExtvmmNetworkSetsFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmDescr.setStatus("current")
_CucsExtvmmNetworkSetsFsmPrev_Type = SnmpAdminString
_CucsExtvmmNetworkSetsFsmPrev_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmPrev = _CucsExtvmmNetworkSetsFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 6),
    _CucsExtvmmNetworkSetsFsmPrev_Type()
)
cucsExtvmmNetworkSetsFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmPrev.setStatus("current")
_CucsExtvmmNetworkSetsFsmProgr_Type = Gauge32
_CucsExtvmmNetworkSetsFsmProgr_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmProgr = _CucsExtvmmNetworkSetsFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 7),
    _CucsExtvmmNetworkSetsFsmProgr_Type()
)
cucsExtvmmNetworkSetsFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmProgr.setStatus("current")
_CucsExtvmmNetworkSetsFsmRmtInvErrCode_Type = Gauge32
_CucsExtvmmNetworkSetsFsmRmtInvErrCode_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmRmtInvErrCode = _CucsExtvmmNetworkSetsFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 8),
    _CucsExtvmmNetworkSetsFsmRmtInvErrCode_Type()
)
cucsExtvmmNetworkSetsFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmRmtInvErrCode.setStatus("current")
_CucsExtvmmNetworkSetsFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsExtvmmNetworkSetsFsmRmtInvErrDescr_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmRmtInvErrDescr = _CucsExtvmmNetworkSetsFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 9),
    _CucsExtvmmNetworkSetsFsmRmtInvErrDescr_Type()
)
cucsExtvmmNetworkSetsFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmRmtInvErrDescr.setStatus("current")
_CucsExtvmmNetworkSetsFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsExtvmmNetworkSetsFsmRmtInvRslt_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmRmtInvRslt = _CucsExtvmmNetworkSetsFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 10),
    _CucsExtvmmNetworkSetsFsmRmtInvRslt_Type()
)
cucsExtvmmNetworkSetsFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmRmtInvRslt.setStatus("current")
_CucsExtvmmNetworkSetsFsmStageDescr_Type = SnmpAdminString
_CucsExtvmmNetworkSetsFsmStageDescr_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmStageDescr = _CucsExtvmmNetworkSetsFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 11),
    _CucsExtvmmNetworkSetsFsmStageDescr_Type()
)
cucsExtvmmNetworkSetsFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStageDescr.setStatus("current")
_CucsExtvmmNetworkSetsFsmStamp_Type = DateAndTime
_CucsExtvmmNetworkSetsFsmStamp_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmStamp = _CucsExtvmmNetworkSetsFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 12),
    _CucsExtvmmNetworkSetsFsmStamp_Type()
)
cucsExtvmmNetworkSetsFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStamp.setStatus("current")
_CucsExtvmmNetworkSetsFsmStatus_Type = SnmpAdminString
_CucsExtvmmNetworkSetsFsmStatus_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmStatus = _CucsExtvmmNetworkSetsFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 13),
    _CucsExtvmmNetworkSetsFsmStatus_Type()
)
cucsExtvmmNetworkSetsFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStatus.setStatus("current")
_CucsExtvmmNetworkSetsFsmTry_Type = Gauge32
_CucsExtvmmNetworkSetsFsmTry_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmTry = _CucsExtvmmNetworkSetsFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 14),
    _CucsExtvmmNetworkSetsFsmTry_Type()
)
cucsExtvmmNetworkSetsFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmTry.setStatus("current")
_CucsExtvmmNetworkSetsGenNum_Type = Gauge32
_CucsExtvmmNetworkSetsGenNum_Object = MibTableColumn
cucsExtvmmNetworkSetsGenNum = _CucsExtvmmNetworkSetsGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 27, 1, 15),
    _CucsExtvmmNetworkSetsGenNum_Type()
)
cucsExtvmmNetworkSetsGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsGenNum.setStatus("current")
_CucsExtvmmNetworkSetsFsmTable_Object = MibTable
cucsExtvmmNetworkSetsFsmTable = _CucsExtvmmNetworkSetsFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28)
)
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmTable.setStatus("current")
_CucsExtvmmNetworkSetsFsmEntry_Object = MibTableRow
cucsExtvmmNetworkSetsFsmEntry = _CucsExtvmmNetworkSetsFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28, 1)
)
cucsExtvmmNetworkSetsFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmNetworkSetsFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmEntry.setStatus("current")
_CucsExtvmmNetworkSetsFsmInstanceId_Type = CucsManagedObjectId
_CucsExtvmmNetworkSetsFsmInstanceId_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmInstanceId = _CucsExtvmmNetworkSetsFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28, 1, 1),
    _CucsExtvmmNetworkSetsFsmInstanceId_Type()
)
cucsExtvmmNetworkSetsFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmInstanceId.setStatus("current")
_CucsExtvmmNetworkSetsFsmDn_Type = CucsManagedObjectDn
_CucsExtvmmNetworkSetsFsmDn_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmDn = _CucsExtvmmNetworkSetsFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28, 1, 2),
    _CucsExtvmmNetworkSetsFsmDn_Type()
)
cucsExtvmmNetworkSetsFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmDn.setStatus("current")
_CucsExtvmmNetworkSetsFsmRn_Type = SnmpAdminString
_CucsExtvmmNetworkSetsFsmRn_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmRn = _CucsExtvmmNetworkSetsFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28, 1, 3),
    _CucsExtvmmNetworkSetsFsmRn_Type()
)
cucsExtvmmNetworkSetsFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmRn.setStatus("current")
_CucsExtvmmNetworkSetsFsmCompletionTime_Type = DateAndTime
_CucsExtvmmNetworkSetsFsmCompletionTime_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmCompletionTime = _CucsExtvmmNetworkSetsFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28, 1, 4),
    _CucsExtvmmNetworkSetsFsmCompletionTime_Type()
)
cucsExtvmmNetworkSetsFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmCompletionTime.setStatus("current")
_CucsExtvmmNetworkSetsFsmCurrentFsm_Type = CucsExtvmmNetworkSetsFsmCurrentFsm
_CucsExtvmmNetworkSetsFsmCurrentFsm_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmCurrentFsm = _CucsExtvmmNetworkSetsFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28, 1, 5),
    _CucsExtvmmNetworkSetsFsmCurrentFsm_Type()
)
cucsExtvmmNetworkSetsFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmCurrentFsm.setStatus("current")
_CucsExtvmmNetworkSetsFsmDescrData_Type = SnmpAdminString
_CucsExtvmmNetworkSetsFsmDescrData_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmDescrData = _CucsExtvmmNetworkSetsFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28, 1, 6),
    _CucsExtvmmNetworkSetsFsmDescrData_Type()
)
cucsExtvmmNetworkSetsFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmDescrData.setStatus("current")
_CucsExtvmmNetworkSetsFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsExtvmmNetworkSetsFsmFsmStatus_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmFsmStatus = _CucsExtvmmNetworkSetsFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28, 1, 7),
    _CucsExtvmmNetworkSetsFsmFsmStatus_Type()
)
cucsExtvmmNetworkSetsFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmFsmStatus.setStatus("current")
_CucsExtvmmNetworkSetsFsmProgress_Type = Gauge32
_CucsExtvmmNetworkSetsFsmProgress_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmProgress = _CucsExtvmmNetworkSetsFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28, 1, 8),
    _CucsExtvmmNetworkSetsFsmProgress_Type()
)
cucsExtvmmNetworkSetsFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmProgress.setStatus("current")
_CucsExtvmmNetworkSetsFsmRmtErrCode_Type = Gauge32
_CucsExtvmmNetworkSetsFsmRmtErrCode_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmRmtErrCode = _CucsExtvmmNetworkSetsFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28, 1, 9),
    _CucsExtvmmNetworkSetsFsmRmtErrCode_Type()
)
cucsExtvmmNetworkSetsFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmRmtErrCode.setStatus("current")
_CucsExtvmmNetworkSetsFsmRmtErrDescr_Type = SnmpAdminString
_CucsExtvmmNetworkSetsFsmRmtErrDescr_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmRmtErrDescr = _CucsExtvmmNetworkSetsFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28, 1, 10),
    _CucsExtvmmNetworkSetsFsmRmtErrDescr_Type()
)
cucsExtvmmNetworkSetsFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmRmtErrDescr.setStatus("current")
_CucsExtvmmNetworkSetsFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsExtvmmNetworkSetsFsmRmtRslt_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmRmtRslt = _CucsExtvmmNetworkSetsFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 28, 1, 11),
    _CucsExtvmmNetworkSetsFsmRmtRslt_Type()
)
cucsExtvmmNetworkSetsFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmRmtRslt.setStatus("current")
_CucsExtvmmNetworkSetsFsmStageTable_Object = MibTable
cucsExtvmmNetworkSetsFsmStageTable = _CucsExtvmmNetworkSetsFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 29)
)
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStageTable.setStatus("current")
_CucsExtvmmNetworkSetsFsmStageEntry_Object = MibTableRow
cucsExtvmmNetworkSetsFsmStageEntry = _CucsExtvmmNetworkSetsFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 29, 1)
)
cucsExtvmmNetworkSetsFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmNetworkSetsFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStageEntry.setStatus("current")
_CucsExtvmmNetworkSetsFsmStageInstanceId_Type = CucsManagedObjectId
_CucsExtvmmNetworkSetsFsmStageInstanceId_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmStageInstanceId = _CucsExtvmmNetworkSetsFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 29, 1, 1),
    _CucsExtvmmNetworkSetsFsmStageInstanceId_Type()
)
cucsExtvmmNetworkSetsFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStageInstanceId.setStatus("current")
_CucsExtvmmNetworkSetsFsmStageDn_Type = CucsManagedObjectDn
_CucsExtvmmNetworkSetsFsmStageDn_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmStageDn = _CucsExtvmmNetworkSetsFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 29, 1, 2),
    _CucsExtvmmNetworkSetsFsmStageDn_Type()
)
cucsExtvmmNetworkSetsFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStageDn.setStatus("current")
_CucsExtvmmNetworkSetsFsmStageRn_Type = SnmpAdminString
_CucsExtvmmNetworkSetsFsmStageRn_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmStageRn = _CucsExtvmmNetworkSetsFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 29, 1, 3),
    _CucsExtvmmNetworkSetsFsmStageRn_Type()
)
cucsExtvmmNetworkSetsFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStageRn.setStatus("current")
_CucsExtvmmNetworkSetsFsmStageDescrData_Type = SnmpAdminString
_CucsExtvmmNetworkSetsFsmStageDescrData_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmStageDescrData = _CucsExtvmmNetworkSetsFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 29, 1, 4),
    _CucsExtvmmNetworkSetsFsmStageDescrData_Type()
)
cucsExtvmmNetworkSetsFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStageDescrData.setStatus("current")
_CucsExtvmmNetworkSetsFsmStageLastUpdateTime_Type = DateAndTime
_CucsExtvmmNetworkSetsFsmStageLastUpdateTime_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmStageLastUpdateTime = _CucsExtvmmNetworkSetsFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 29, 1, 5),
    _CucsExtvmmNetworkSetsFsmStageLastUpdateTime_Type()
)
cucsExtvmmNetworkSetsFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStageLastUpdateTime.setStatus("current")
_CucsExtvmmNetworkSetsFsmStageName_Type = CucsExtvmmNetworkSetsFsmStageName
_CucsExtvmmNetworkSetsFsmStageName_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmStageName = _CucsExtvmmNetworkSetsFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 29, 1, 6),
    _CucsExtvmmNetworkSetsFsmStageName_Type()
)
cucsExtvmmNetworkSetsFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStageName.setStatus("current")
_CucsExtvmmNetworkSetsFsmStageOrder_Type = Gauge32
_CucsExtvmmNetworkSetsFsmStageOrder_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmStageOrder = _CucsExtvmmNetworkSetsFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 29, 1, 7),
    _CucsExtvmmNetworkSetsFsmStageOrder_Type()
)
cucsExtvmmNetworkSetsFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStageOrder.setStatus("current")
_CucsExtvmmNetworkSetsFsmStageRetry_Type = Gauge32
_CucsExtvmmNetworkSetsFsmStageRetry_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmStageRetry = _CucsExtvmmNetworkSetsFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 29, 1, 8),
    _CucsExtvmmNetworkSetsFsmStageRetry_Type()
)
cucsExtvmmNetworkSetsFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStageRetry.setStatus("current")
_CucsExtvmmNetworkSetsFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsExtvmmNetworkSetsFsmStageStageStatus_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmStageStageStatus = _CucsExtvmmNetworkSetsFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 29, 1, 9),
    _CucsExtvmmNetworkSetsFsmStageStageStatus_Type()
)
cucsExtvmmNetworkSetsFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmStageStageStatus.setStatus("current")
_CucsExtvmmNetworkSetsFsmTaskTable_Object = MibTable
cucsExtvmmNetworkSetsFsmTaskTable = _CucsExtvmmNetworkSetsFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 30)
)
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmTaskTable.setStatus("current")
_CucsExtvmmNetworkSetsFsmTaskEntry_Object = MibTableRow
cucsExtvmmNetworkSetsFsmTaskEntry = _CucsExtvmmNetworkSetsFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 30, 1)
)
cucsExtvmmNetworkSetsFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmNetworkSetsFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmTaskEntry.setStatus("current")
_CucsExtvmmNetworkSetsFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsExtvmmNetworkSetsFsmTaskInstanceId_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmTaskInstanceId = _CucsExtvmmNetworkSetsFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 30, 1, 1),
    _CucsExtvmmNetworkSetsFsmTaskInstanceId_Type()
)
cucsExtvmmNetworkSetsFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmTaskInstanceId.setStatus("current")
_CucsExtvmmNetworkSetsFsmTaskDn_Type = CucsManagedObjectDn
_CucsExtvmmNetworkSetsFsmTaskDn_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmTaskDn = _CucsExtvmmNetworkSetsFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 30, 1, 2),
    _CucsExtvmmNetworkSetsFsmTaskDn_Type()
)
cucsExtvmmNetworkSetsFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmTaskDn.setStatus("current")
_CucsExtvmmNetworkSetsFsmTaskRn_Type = SnmpAdminString
_CucsExtvmmNetworkSetsFsmTaskRn_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmTaskRn = _CucsExtvmmNetworkSetsFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 30, 1, 3),
    _CucsExtvmmNetworkSetsFsmTaskRn_Type()
)
cucsExtvmmNetworkSetsFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmTaskRn.setStatus("current")
_CucsExtvmmNetworkSetsFsmTaskCompletion_Type = CucsFsmCompletion
_CucsExtvmmNetworkSetsFsmTaskCompletion_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmTaskCompletion = _CucsExtvmmNetworkSetsFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 30, 1, 4),
    _CucsExtvmmNetworkSetsFsmTaskCompletion_Type()
)
cucsExtvmmNetworkSetsFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmTaskCompletion.setStatus("current")
_CucsExtvmmNetworkSetsFsmTaskFlags_Type = CucsFsmFlags
_CucsExtvmmNetworkSetsFsmTaskFlags_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmTaskFlags = _CucsExtvmmNetworkSetsFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 30, 1, 5),
    _CucsExtvmmNetworkSetsFsmTaskFlags_Type()
)
cucsExtvmmNetworkSetsFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmTaskFlags.setStatus("current")
_CucsExtvmmNetworkSetsFsmTaskItem_Type = CucsExtvmmNetworkSetsFsmTaskItem
_CucsExtvmmNetworkSetsFsmTaskItem_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmTaskItem = _CucsExtvmmNetworkSetsFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 30, 1, 6),
    _CucsExtvmmNetworkSetsFsmTaskItem_Type()
)
cucsExtvmmNetworkSetsFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmTaskItem.setStatus("current")
_CucsExtvmmNetworkSetsFsmTaskSeqId_Type = Gauge32
_CucsExtvmmNetworkSetsFsmTaskSeqId_Object = MibTableColumn
cucsExtvmmNetworkSetsFsmTaskSeqId = _CucsExtvmmNetworkSetsFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 30, 1, 7),
    _CucsExtvmmNetworkSetsFsmTaskSeqId_Type()
)
cucsExtvmmNetworkSetsFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmNetworkSetsFsmTaskSeqId.setStatus("current")
_CucsExtvmmUpLinkPPTable_Object = MibTable
cucsExtvmmUpLinkPPTable = _CucsExtvmmUpLinkPPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31)
)
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPTable.setStatus("current")
_CucsExtvmmUpLinkPPEntry_Object = MibTableRow
cucsExtvmmUpLinkPPEntry = _CucsExtvmmUpLinkPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31, 1)
)
cucsExtvmmUpLinkPPEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmUpLinkPPInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPEntry.setStatus("current")
_CucsExtvmmUpLinkPPInstanceId_Type = CucsManagedObjectId
_CucsExtvmmUpLinkPPInstanceId_Object = MibTableColumn
cucsExtvmmUpLinkPPInstanceId = _CucsExtvmmUpLinkPPInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31, 1, 1),
    _CucsExtvmmUpLinkPPInstanceId_Type()
)
cucsExtvmmUpLinkPPInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPInstanceId.setStatus("current")
_CucsExtvmmUpLinkPPDn_Type = CucsManagedObjectDn
_CucsExtvmmUpLinkPPDn_Object = MibTableColumn
cucsExtvmmUpLinkPPDn = _CucsExtvmmUpLinkPPDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31, 1, 2),
    _CucsExtvmmUpLinkPPDn_Type()
)
cucsExtvmmUpLinkPPDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPDn.setStatus("current")
_CucsExtvmmUpLinkPPRn_Type = SnmpAdminString
_CucsExtvmmUpLinkPPRn_Object = MibTableColumn
cucsExtvmmUpLinkPPRn = _CucsExtvmmUpLinkPPRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31, 1, 3),
    _CucsExtvmmUpLinkPPRn_Type()
)
cucsExtvmmUpLinkPPRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPRn.setStatus("current")
_CucsExtvmmUpLinkPPDescr_Type = SnmpAdminString
_CucsExtvmmUpLinkPPDescr_Object = MibTableColumn
cucsExtvmmUpLinkPPDescr = _CucsExtvmmUpLinkPPDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31, 1, 4),
    _CucsExtvmmUpLinkPPDescr_Type()
)
cucsExtvmmUpLinkPPDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPDescr.setStatus("current")
_CucsExtvmmUpLinkPPFltAggr_Type = Unsigned64
_CucsExtvmmUpLinkPPFltAggr_Object = MibTableColumn
cucsExtvmmUpLinkPPFltAggr = _CucsExtvmmUpLinkPPFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31, 1, 5),
    _CucsExtvmmUpLinkPPFltAggr_Type()
)
cucsExtvmmUpLinkPPFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPFltAggr.setStatus("current")
_CucsExtvmmUpLinkPPGuid_Type = SnmpAdminString
_CucsExtvmmUpLinkPPGuid_Object = MibTableColumn
cucsExtvmmUpLinkPPGuid = _CucsExtvmmUpLinkPPGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31, 1, 6),
    _CucsExtvmmUpLinkPPGuid_Type()
)
cucsExtvmmUpLinkPPGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPGuid.setStatus("current")
_CucsExtvmmUpLinkPPIntId_Type = SnmpAdminString
_CucsExtvmmUpLinkPPIntId_Object = MibTableColumn
cucsExtvmmUpLinkPPIntId = _CucsExtvmmUpLinkPPIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31, 1, 7),
    _CucsExtvmmUpLinkPPIntId_Type()
)
cucsExtvmmUpLinkPPIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPIntId.setStatus("current")
_CucsExtvmmUpLinkPPName_Type = SnmpAdminString
_CucsExtvmmUpLinkPPName_Object = MibTableColumn
cucsExtvmmUpLinkPPName = _CucsExtvmmUpLinkPPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31, 1, 8),
    _CucsExtvmmUpLinkPPName_Type()
)
cucsExtvmmUpLinkPPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPName.setStatus("current")
_CucsExtvmmUpLinkPPPolicyLevel_Type = Gauge32
_CucsExtvmmUpLinkPPPolicyLevel_Object = MibTableColumn
cucsExtvmmUpLinkPPPolicyLevel = _CucsExtvmmUpLinkPPPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31, 1, 9),
    _CucsExtvmmUpLinkPPPolicyLevel_Type()
)
cucsExtvmmUpLinkPPPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPPolicyLevel.setStatus("current")
_CucsExtvmmUpLinkPPPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsExtvmmUpLinkPPPolicyOwner_Object = MibTableColumn
cucsExtvmmUpLinkPPPolicyOwner = _CucsExtvmmUpLinkPPPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31, 1, 10),
    _CucsExtvmmUpLinkPPPolicyOwner_Type()
)
cucsExtvmmUpLinkPPPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPPolicyOwner.setStatus("current")
_CucsExtvmmUpLinkPPRefOperState_Type = CucsExtvmmRefOperState
_CucsExtvmmUpLinkPPRefOperState_Object = MibTableColumn
cucsExtvmmUpLinkPPRefOperState = _CucsExtvmmUpLinkPPRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 31, 1, 11),
    _CucsExtvmmUpLinkPPRefOperState_Type()
)
cucsExtvmmUpLinkPPRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmUpLinkPPRefOperState.setStatus("current")
_CucsExtvmmVMNDRefTable_Object = MibTable
cucsExtvmmVMNDRefTable = _CucsExtvmmVMNDRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32)
)
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefTable.setStatus("current")
_CucsExtvmmVMNDRefEntry_Object = MibTableRow
cucsExtvmmVMNDRefEntry = _CucsExtvmmVMNDRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1)
)
cucsExtvmmVMNDRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmVMNDRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefEntry.setStatus("current")
_CucsExtvmmVMNDRefInstanceId_Type = CucsManagedObjectId
_CucsExtvmmVMNDRefInstanceId_Object = MibTableColumn
cucsExtvmmVMNDRefInstanceId = _CucsExtvmmVMNDRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 1),
    _CucsExtvmmVMNDRefInstanceId_Type()
)
cucsExtvmmVMNDRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefInstanceId.setStatus("current")
_CucsExtvmmVMNDRefDn_Type = CucsManagedObjectDn
_CucsExtvmmVMNDRefDn_Object = MibTableColumn
cucsExtvmmVMNDRefDn = _CucsExtvmmVMNDRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 2),
    _CucsExtvmmVMNDRefDn_Type()
)
cucsExtvmmVMNDRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefDn.setStatus("current")
_CucsExtvmmVMNDRefRn_Type = SnmpAdminString
_CucsExtvmmVMNDRefRn_Object = MibTableColumn
cucsExtvmmVMNDRefRn = _CucsExtvmmVMNDRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 3),
    _CucsExtvmmVMNDRefRn_Type()
)
cucsExtvmmVMNDRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefRn.setStatus("current")
_CucsExtvmmVMNDRefConfigQualifier_Type = CucsExtvmmNetworkSetConfigQualifier
_CucsExtvmmVMNDRefConfigQualifier_Object = MibTableColumn
cucsExtvmmVMNDRefConfigQualifier = _CucsExtvmmVMNDRefConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 4),
    _CucsExtvmmVMNDRefConfigQualifier_Type()
)
cucsExtvmmVMNDRefConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefConfigQualifier.setStatus("current")
_CucsExtvmmVMNDRefDescr_Type = SnmpAdminString
_CucsExtvmmVMNDRefDescr_Object = MibTableColumn
cucsExtvmmVMNDRefDescr = _CucsExtvmmVMNDRefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 5),
    _CucsExtvmmVMNDRefDescr_Type()
)
cucsExtvmmVMNDRefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefDescr.setStatus("current")
_CucsExtvmmVMNDRefFnDefName_Type = SnmpAdminString
_CucsExtvmmVMNDRefFnDefName_Object = MibTableColumn
cucsExtvmmVMNDRefFnDefName = _CucsExtvmmVMNDRefFnDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 6),
    _CucsExtvmmVMNDRefFnDefName_Type()
)
cucsExtvmmVMNDRefFnDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefFnDefName.setStatus("current")
_CucsExtvmmVMNDRefFnName_Type = SnmpAdminString
_CucsExtvmmVMNDRefFnName_Object = MibTableColumn
cucsExtvmmVMNDRefFnName = _CucsExtvmmVMNDRefFnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 7),
    _CucsExtvmmVMNDRefFnName_Type()
)
cucsExtvmmVMNDRefFnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefFnName.setStatus("current")
_CucsExtvmmVMNDRefIntId_Type = SnmpAdminString
_CucsExtvmmVMNDRefIntId_Object = MibTableColumn
cucsExtvmmVMNDRefIntId = _CucsExtvmmVMNDRefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 8),
    _CucsExtvmmVMNDRefIntId_Type()
)
cucsExtvmmVMNDRefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefIntId.setStatus("current")
_CucsExtvmmVMNDRefName_Type = SnmpAdminString
_CucsExtvmmVMNDRefName_Object = MibTableColumn
cucsExtvmmVMNDRefName = _CucsExtvmmVMNDRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 9),
    _CucsExtvmmVMNDRefName_Type()
)
cucsExtvmmVMNDRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefName.setStatus("current")
_CucsExtvmmVMNDRefOperVmNetworkDefName_Type = SnmpAdminString
_CucsExtvmmVMNDRefOperVmNetworkDefName_Object = MibTableColumn
cucsExtvmmVMNDRefOperVmNetworkDefName = _CucsExtvmmVMNDRefOperVmNetworkDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 10),
    _CucsExtvmmVMNDRefOperVmNetworkDefName_Type()
)
cucsExtvmmVMNDRefOperVmNetworkDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefOperVmNetworkDefName.setStatus("current")
_CucsExtvmmVMNDRefPolicyLevel_Type = Gauge32
_CucsExtvmmVMNDRefPolicyLevel_Object = MibTableColumn
cucsExtvmmVMNDRefPolicyLevel = _CucsExtvmmVMNDRefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 11),
    _CucsExtvmmVMNDRefPolicyLevel_Type()
)
cucsExtvmmVMNDRefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefPolicyLevel.setStatus("current")
_CucsExtvmmVMNDRefPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsExtvmmVMNDRefPolicyOwner_Object = MibTableColumn
cucsExtvmmVMNDRefPolicyOwner = _CucsExtvmmVMNDRefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 12),
    _CucsExtvmmVMNDRefPolicyOwner_Type()
)
cucsExtvmmVMNDRefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefPolicyOwner.setStatus("current")
_CucsExtvmmVMNDRefVmNetworkDefName_Type = SnmpAdminString
_CucsExtvmmVMNDRefVmNetworkDefName_Object = MibTableColumn
cucsExtvmmVMNDRefVmNetworkDefName = _CucsExtvmmVMNDRefVmNetworkDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 32, 1, 13),
    _CucsExtvmmVMNDRefVmNetworkDefName_Type()
)
cucsExtvmmVMNDRefVmNetworkDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNDRefVmNetworkDefName.setStatus("current")
_CucsExtvmmVMNetworkTable_Object = MibTable
cucsExtvmmVMNetworkTable = _CucsExtvmmVMNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33)
)
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkTable.setStatus("current")
_CucsExtvmmVMNetworkEntry_Object = MibTableRow
cucsExtvmmVMNetworkEntry = _CucsExtvmmVMNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1)
)
cucsExtvmmVMNetworkEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmVMNetworkInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkEntry.setStatus("current")
_CucsExtvmmVMNetworkInstanceId_Type = CucsManagedObjectId
_CucsExtvmmVMNetworkInstanceId_Object = MibTableColumn
cucsExtvmmVMNetworkInstanceId = _CucsExtvmmVMNetworkInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1, 1),
    _CucsExtvmmVMNetworkInstanceId_Type()
)
cucsExtvmmVMNetworkInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkInstanceId.setStatus("current")
_CucsExtvmmVMNetworkDn_Type = CucsManagedObjectDn
_CucsExtvmmVMNetworkDn_Object = MibTableColumn
cucsExtvmmVMNetworkDn = _CucsExtvmmVMNetworkDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1, 2),
    _CucsExtvmmVMNetworkDn_Type()
)
cucsExtvmmVMNetworkDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDn.setStatus("current")
_CucsExtvmmVMNetworkRn_Type = SnmpAdminString
_CucsExtvmmVMNetworkRn_Object = MibTableColumn
cucsExtvmmVMNetworkRn = _CucsExtvmmVMNetworkRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1, 3),
    _CucsExtvmmVMNetworkRn_Type()
)
cucsExtvmmVMNetworkRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkRn.setStatus("current")
_CucsExtvmmVMNetworkDescr_Type = SnmpAdminString
_CucsExtvmmVMNetworkDescr_Object = MibTableColumn
cucsExtvmmVMNetworkDescr = _CucsExtvmmVMNetworkDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1, 4),
    _CucsExtvmmVMNetworkDescr_Type()
)
cucsExtvmmVMNetworkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDescr.setStatus("current")
_CucsExtvmmVMNetworkFabricNetworkName_Type = SnmpAdminString
_CucsExtvmmVMNetworkFabricNetworkName_Object = MibTableColumn
cucsExtvmmVMNetworkFabricNetworkName = _CucsExtvmmVMNetworkFabricNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1, 5),
    _CucsExtvmmVMNetworkFabricNetworkName_Type()
)
cucsExtvmmVMNetworkFabricNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkFabricNetworkName.setStatus("current")
_CucsExtvmmVMNetworkFltAggr_Type = Unsigned64
_CucsExtvmmVMNetworkFltAggr_Object = MibTableColumn
cucsExtvmmVMNetworkFltAggr = _CucsExtvmmVMNetworkFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1, 6),
    _CucsExtvmmVMNetworkFltAggr_Type()
)
cucsExtvmmVMNetworkFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkFltAggr.setStatus("current")
_CucsExtvmmVMNetworkGuid_Type = SnmpAdminString
_CucsExtvmmVMNetworkGuid_Object = MibTableColumn
cucsExtvmmVMNetworkGuid = _CucsExtvmmVMNetworkGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1, 7),
    _CucsExtvmmVMNetworkGuid_Type()
)
cucsExtvmmVMNetworkGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkGuid.setStatus("current")
_CucsExtvmmVMNetworkIntId_Type = SnmpAdminString
_CucsExtvmmVMNetworkIntId_Object = MibTableColumn
cucsExtvmmVMNetworkIntId = _CucsExtvmmVMNetworkIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1, 8),
    _CucsExtvmmVMNetworkIntId_Type()
)
cucsExtvmmVMNetworkIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkIntId.setStatus("current")
_CucsExtvmmVMNetworkName_Type = SnmpAdminString
_CucsExtvmmVMNetworkName_Object = MibTableColumn
cucsExtvmmVMNetworkName = _CucsExtvmmVMNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1, 9),
    _CucsExtvmmVMNetworkName_Type()
)
cucsExtvmmVMNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkName.setStatus("current")
_CucsExtvmmVMNetworkOperFabricNetworkName_Type = SnmpAdminString
_CucsExtvmmVMNetworkOperFabricNetworkName_Object = MibTableColumn
cucsExtvmmVMNetworkOperFabricNetworkName = _CucsExtvmmVMNetworkOperFabricNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1, 10),
    _CucsExtvmmVMNetworkOperFabricNetworkName_Type()
)
cucsExtvmmVMNetworkOperFabricNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkOperFabricNetworkName.setStatus("current")
_CucsExtvmmVMNetworkPolicyLevel_Type = Gauge32
_CucsExtvmmVMNetworkPolicyLevel_Object = MibTableColumn
cucsExtvmmVMNetworkPolicyLevel = _CucsExtvmmVMNetworkPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1, 11),
    _CucsExtvmmVMNetworkPolicyLevel_Type()
)
cucsExtvmmVMNetworkPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkPolicyLevel.setStatus("current")
_CucsExtvmmVMNetworkPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsExtvmmVMNetworkPolicyOwner_Object = MibTableColumn
cucsExtvmmVMNetworkPolicyOwner = _CucsExtvmmVMNetworkPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 33, 1, 12),
    _CucsExtvmmVMNetworkPolicyOwner_Type()
)
cucsExtvmmVMNetworkPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkPolicyOwner.setStatus("current")
_CucsExtvmmVMNetworkDefinitionTable_Object = MibTable
cucsExtvmmVMNetworkDefinitionTable = _CucsExtvmmVMNetworkDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34)
)
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionTable.setStatus("current")
_CucsExtvmmVMNetworkDefinitionEntry_Object = MibTableRow
cucsExtvmmVMNetworkDefinitionEntry = _CucsExtvmmVMNetworkDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1)
)
cucsExtvmmVMNetworkDefinitionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmVMNetworkDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionEntry.setStatus("current")
_CucsExtvmmVMNetworkDefinitionInstanceId_Type = CucsManagedObjectId
_CucsExtvmmVMNetworkDefinitionInstanceId_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionInstanceId = _CucsExtvmmVMNetworkDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 1),
    _CucsExtvmmVMNetworkDefinitionInstanceId_Type()
)
cucsExtvmmVMNetworkDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionInstanceId.setStatus("current")
_CucsExtvmmVMNetworkDefinitionDn_Type = CucsManagedObjectDn
_CucsExtvmmVMNetworkDefinitionDn_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionDn = _CucsExtvmmVMNetworkDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 2),
    _CucsExtvmmVMNetworkDefinitionDn_Type()
)
cucsExtvmmVMNetworkDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionDn.setStatus("current")
_CucsExtvmmVMNetworkDefinitionRn_Type = SnmpAdminString
_CucsExtvmmVMNetworkDefinitionRn_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionRn = _CucsExtvmmVMNetworkDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 3),
    _CucsExtvmmVMNetworkDefinitionRn_Type()
)
cucsExtvmmVMNetworkDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionRn.setStatus("current")
_CucsExtvmmVMNetworkDefinitionDescr_Type = SnmpAdminString
_CucsExtvmmVMNetworkDefinitionDescr_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionDescr = _CucsExtvmmVMNetworkDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 4),
    _CucsExtvmmVMNetworkDefinitionDescr_Type()
)
cucsExtvmmVMNetworkDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionDescr.setStatus("current")
_CucsExtvmmVMNetworkDefinitionExtIpPoolName_Type = SnmpAdminString
_CucsExtvmmVMNetworkDefinitionExtIpPoolName_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionExtIpPoolName = _CucsExtvmmVMNetworkDefinitionExtIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 5),
    _CucsExtvmmVMNetworkDefinitionExtIpPoolName_Type()
)
cucsExtvmmVMNetworkDefinitionExtIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionExtIpPoolName.setStatus("current")
_CucsExtvmmVMNetworkDefinitionGuid_Type = SnmpAdminString
_CucsExtvmmVMNetworkDefinitionGuid_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionGuid = _CucsExtvmmVMNetworkDefinitionGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 6),
    _CucsExtvmmVMNetworkDefinitionGuid_Type()
)
cucsExtvmmVMNetworkDefinitionGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionGuid.setStatus("current")
_CucsExtvmmVMNetworkDefinitionIntId_Type = SnmpAdminString
_CucsExtvmmVMNetworkDefinitionIntId_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionIntId = _CucsExtvmmVMNetworkDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 7),
    _CucsExtvmmVMNetworkDefinitionIntId_Type()
)
cucsExtvmmVMNetworkDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionIntId.setStatus("current")
_CucsExtvmmVMNetworkDefinitionIpPoolGuid_Type = SnmpAdminString
_CucsExtvmmVMNetworkDefinitionIpPoolGuid_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionIpPoolGuid = _CucsExtvmmVMNetworkDefinitionIpPoolGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 8),
    _CucsExtvmmVMNetworkDefinitionIpPoolGuid_Type()
)
cucsExtvmmVMNetworkDefinitionIpPoolGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionIpPoolGuid.setStatus("current")
_CucsExtvmmVMNetworkDefinitionMaxPorts_Type = Gauge32
_CucsExtvmmVMNetworkDefinitionMaxPorts_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionMaxPorts = _CucsExtvmmVMNetworkDefinitionMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 9),
    _CucsExtvmmVMNetworkDefinitionMaxPorts_Type()
)
cucsExtvmmVMNetworkDefinitionMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionMaxPorts.setStatus("current")
_CucsExtvmmVMNetworkDefinitionName_Type = SnmpAdminString
_CucsExtvmmVMNetworkDefinitionName_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionName = _CucsExtvmmVMNetworkDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 10),
    _CucsExtvmmVMNetworkDefinitionName_Type()
)
cucsExtvmmVMNetworkDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionName.setStatus("current")
_CucsExtvmmVMNetworkDefinitionOperExtIpPoolName_Type = SnmpAdminString
_CucsExtvmmVMNetworkDefinitionOperExtIpPoolName_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionOperExtIpPoolName = _CucsExtvmmVMNetworkDefinitionOperExtIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 11),
    _CucsExtvmmVMNetworkDefinitionOperExtIpPoolName_Type()
)
cucsExtvmmVMNetworkDefinitionOperExtIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionOperExtIpPoolName.setStatus("current")
_CucsExtvmmVMNetworkDefinitionPolicyLevel_Type = Gauge32
_CucsExtvmmVMNetworkDefinitionPolicyLevel_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionPolicyLevel = _CucsExtvmmVMNetworkDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 12),
    _CucsExtvmmVMNetworkDefinitionPolicyLevel_Type()
)
cucsExtvmmVMNetworkDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionPolicyLevel.setStatus("current")
_CucsExtvmmVMNetworkDefinitionPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsExtvmmVMNetworkDefinitionPolicyOwner_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionPolicyOwner = _CucsExtvmmVMNetworkDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 13),
    _CucsExtvmmVMNetworkDefinitionPolicyOwner_Type()
)
cucsExtvmmVMNetworkDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionPolicyOwner.setStatus("current")
_CucsExtvmmVMNetworkDefinitionPrimaryVlanId_Type = Gauge32
_CucsExtvmmVMNetworkDefinitionPrimaryVlanId_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionPrimaryVlanId = _CucsExtvmmVMNetworkDefinitionPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 14),
    _CucsExtvmmVMNetworkDefinitionPrimaryVlanId_Type()
)
cucsExtvmmVMNetworkDefinitionPrimaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionPrimaryVlanId.setStatus("current")
_CucsExtvmmVMNetworkDefinitionRefOperState_Type = CucsExtvmmRefOperState
_CucsExtvmmVMNetworkDefinitionRefOperState_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionRefOperState = _CucsExtvmmVMNetworkDefinitionRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 15),
    _CucsExtvmmVMNetworkDefinitionRefOperState_Type()
)
cucsExtvmmVMNetworkDefinitionRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionRefOperState.setStatus("current")
_CucsExtvmmVMNetworkDefinitionVlanName_Type = SnmpAdminString
_CucsExtvmmVMNetworkDefinitionVlanName_Object = MibTableColumn
cucsExtvmmVMNetworkDefinitionVlanName = _CucsExtvmmVMNetworkDefinitionVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 34, 1, 16),
    _CucsExtvmmVMNetworkDefinitionVlanName_Type()
)
cucsExtvmmVMNetworkDefinitionVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkDefinitionVlanName.setStatus("current")
_CucsExtvmmVMNetworkSetsTable_Object = MibTable
cucsExtvmmVMNetworkSetsTable = _CucsExtvmmVMNetworkSetsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 35)
)
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkSetsTable.setStatus("current")
_CucsExtvmmVMNetworkSetsEntry_Object = MibTableRow
cucsExtvmmVMNetworkSetsEntry = _CucsExtvmmVMNetworkSetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 35, 1)
)
cucsExtvmmVMNetworkSetsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB", "cucsExtvmmVMNetworkSetsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkSetsEntry.setStatus("current")
_CucsExtvmmVMNetworkSetsInstanceId_Type = CucsManagedObjectId
_CucsExtvmmVMNetworkSetsInstanceId_Object = MibTableColumn
cucsExtvmmVMNetworkSetsInstanceId = _CucsExtvmmVMNetworkSetsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 35, 1, 1),
    _CucsExtvmmVMNetworkSetsInstanceId_Type()
)
cucsExtvmmVMNetworkSetsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkSetsInstanceId.setStatus("current")
_CucsExtvmmVMNetworkSetsDn_Type = CucsManagedObjectDn
_CucsExtvmmVMNetworkSetsDn_Object = MibTableColumn
cucsExtvmmVMNetworkSetsDn = _CucsExtvmmVMNetworkSetsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 35, 1, 2),
    _CucsExtvmmVMNetworkSetsDn_Type()
)
cucsExtvmmVMNetworkSetsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkSetsDn.setStatus("current")
_CucsExtvmmVMNetworkSetsRn_Type = SnmpAdminString
_CucsExtvmmVMNetworkSetsRn_Object = MibTableColumn
cucsExtvmmVMNetworkSetsRn = _CucsExtvmmVMNetworkSetsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 35, 1, 3),
    _CucsExtvmmVMNetworkSetsRn_Type()
)
cucsExtvmmVMNetworkSetsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkSetsRn.setStatus("current")
_CucsExtvmmVMNetworkSetsFltAggr_Type = Unsigned64
_CucsExtvmmVMNetworkSetsFltAggr_Object = MibTableColumn
cucsExtvmmVMNetworkSetsFltAggr = _CucsExtvmmVMNetworkSetsFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 35, 1, 4),
    _CucsExtvmmVMNetworkSetsFltAggr_Type()
)
cucsExtvmmVMNetworkSetsFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkSetsFltAggr.setStatus("current")
_CucsExtvmmVMNetworkSetsGenNum_Type = Gauge32
_CucsExtvmmVMNetworkSetsGenNum_Object = MibTableColumn
cucsExtvmmVMNetworkSetsGenNum = _CucsExtvmmVMNetworkSetsGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 18, 35, 1, 5),
    _CucsExtvmmVMNetworkSetsGenNum_Type()
)
cucsExtvmmVMNetworkSetsGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsExtvmmVMNetworkSetsGenNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-EXTVMM-MIB",
    **{"cucsExtvmmObjects": cucsExtvmmObjects,
       "cucsExtvmmEpTable": cucsExtvmmEpTable,
       "cucsExtvmmEpEntry": cucsExtvmmEpEntry,
       "cucsExtvmmEpInstanceId": cucsExtvmmEpInstanceId,
       "cucsExtvmmEpDn": cucsExtvmmEpDn,
       "cucsExtvmmEpRn": cucsExtvmmEpRn,
       "cucsExtvmmEpFsmDescr": cucsExtvmmEpFsmDescr,
       "cucsExtvmmEpFsmPrev": cucsExtvmmEpFsmPrev,
       "cucsExtvmmEpFsmProgr": cucsExtvmmEpFsmProgr,
       "cucsExtvmmEpFsmRmtInvErrCode": cucsExtvmmEpFsmRmtInvErrCode,
       "cucsExtvmmEpFsmRmtInvErrDescr": cucsExtvmmEpFsmRmtInvErrDescr,
       "cucsExtvmmEpFsmRmtInvRslt": cucsExtvmmEpFsmRmtInvRslt,
       "cucsExtvmmEpFsmStageDescr": cucsExtvmmEpFsmStageDescr,
       "cucsExtvmmEpFsmStamp": cucsExtvmmEpFsmStamp,
       "cucsExtvmmEpFsmStatus": cucsExtvmmEpFsmStatus,
       "cucsExtvmmEpFsmTry": cucsExtvmmEpFsmTry,
       "cucsExtvmmEpGenNum": cucsExtvmmEpGenNum,
       "cucsExtvmmKeyInstTable": cucsExtvmmKeyInstTable,
       "cucsExtvmmKeyInstEntry": cucsExtvmmKeyInstEntry,
       "cucsExtvmmKeyInstInstanceId": cucsExtvmmKeyInstInstanceId,
       "cucsExtvmmKeyInstDn": cucsExtvmmKeyInstDn,
       "cucsExtvmmKeyInstRn": cucsExtvmmKeyInstRn,
       "cucsExtvmmKeyInstInst": cucsExtvmmKeyInstInst,
       "cucsExtvmmKeyInstKey": cucsExtvmmKeyInstKey,
       "cucsExtvmmKeyRingTable": cucsExtvmmKeyRingTable,
       "cucsExtvmmKeyRingEntry": cucsExtvmmKeyRingEntry,
       "cucsExtvmmKeyRingInstanceId": cucsExtvmmKeyRingInstanceId,
       "cucsExtvmmKeyRingDn": cucsExtvmmKeyRingDn,
       "cucsExtvmmKeyRingRn": cucsExtvmmKeyRingRn,
       "cucsExtvmmKeyRingCertFile": cucsExtvmmKeyRingCertFile,
       "cucsExtvmmKeyRingLocation": cucsExtvmmKeyRingLocation,
       "cucsExtvmmKeyRingName": cucsExtvmmKeyRingName,
       "cucsExtvmmKeyRingPath": cucsExtvmmKeyRingPath,
       "cucsExtvmmKeyStoreTable": cucsExtvmmKeyStoreTable,
       "cucsExtvmmKeyStoreEntry": cucsExtvmmKeyStoreEntry,
       "cucsExtvmmKeyStoreInstanceId": cucsExtvmmKeyStoreInstanceId,
       "cucsExtvmmKeyStoreDn": cucsExtvmmKeyStoreDn,
       "cucsExtvmmKeyStoreRn": cucsExtvmmKeyStoreRn,
       "cucsExtvmmKeyStoreFsmDescr": cucsExtvmmKeyStoreFsmDescr,
       "cucsExtvmmKeyStoreFsmPrev": cucsExtvmmKeyStoreFsmPrev,
       "cucsExtvmmKeyStoreFsmProgr": cucsExtvmmKeyStoreFsmProgr,
       "cucsExtvmmKeyStoreFsmRmtInvErrCode": cucsExtvmmKeyStoreFsmRmtInvErrCode,
       "cucsExtvmmKeyStoreFsmRmtInvErrDescr": cucsExtvmmKeyStoreFsmRmtInvErrDescr,
       "cucsExtvmmKeyStoreFsmRmtInvRslt": cucsExtvmmKeyStoreFsmRmtInvRslt,
       "cucsExtvmmKeyStoreFsmStageDescr": cucsExtvmmKeyStoreFsmStageDescr,
       "cucsExtvmmKeyStoreFsmStamp": cucsExtvmmKeyStoreFsmStamp,
       "cucsExtvmmKeyStoreFsmStatus": cucsExtvmmKeyStoreFsmStatus,
       "cucsExtvmmKeyStoreFsmTry": cucsExtvmmKeyStoreFsmTry,
       "cucsExtvmmKeyStoreFsmTaskTable": cucsExtvmmKeyStoreFsmTaskTable,
       "cucsExtvmmKeyStoreFsmTaskEntry": cucsExtvmmKeyStoreFsmTaskEntry,
       "cucsExtvmmKeyStoreFsmTaskInstanceId": cucsExtvmmKeyStoreFsmTaskInstanceId,
       "cucsExtvmmKeyStoreFsmTaskDn": cucsExtvmmKeyStoreFsmTaskDn,
       "cucsExtvmmKeyStoreFsmTaskRn": cucsExtvmmKeyStoreFsmTaskRn,
       "cucsExtvmmKeyStoreFsmTaskCompletion": cucsExtvmmKeyStoreFsmTaskCompletion,
       "cucsExtvmmKeyStoreFsmTaskFlags": cucsExtvmmKeyStoreFsmTaskFlags,
       "cucsExtvmmKeyStoreFsmTaskItem": cucsExtvmmKeyStoreFsmTaskItem,
       "cucsExtvmmKeyStoreFsmTaskSeqId": cucsExtvmmKeyStoreFsmTaskSeqId,
       "cucsExtvmmMasterExtKeyTable": cucsExtvmmMasterExtKeyTable,
       "cucsExtvmmMasterExtKeyEntry": cucsExtvmmMasterExtKeyEntry,
       "cucsExtvmmMasterExtKeyInstanceId": cucsExtvmmMasterExtKeyInstanceId,
       "cucsExtvmmMasterExtKeyDn": cucsExtvmmMasterExtKeyDn,
       "cucsExtvmmMasterExtKeyRn": cucsExtvmmMasterExtKeyRn,
       "cucsExtvmmMasterExtKeyFsmDescr": cucsExtvmmMasterExtKeyFsmDescr,
       "cucsExtvmmMasterExtKeyFsmPrev": cucsExtvmmMasterExtKeyFsmPrev,
       "cucsExtvmmMasterExtKeyFsmProgr": cucsExtvmmMasterExtKeyFsmProgr,
       "cucsExtvmmMasterExtKeyFsmRmtInvErrCode": cucsExtvmmMasterExtKeyFsmRmtInvErrCode,
       "cucsExtvmmMasterExtKeyFsmRmtInvErrDescr": cucsExtvmmMasterExtKeyFsmRmtInvErrDescr,
       "cucsExtvmmMasterExtKeyFsmRmtInvRslt": cucsExtvmmMasterExtKeyFsmRmtInvRslt,
       "cucsExtvmmMasterExtKeyFsmStageDescr": cucsExtvmmMasterExtKeyFsmStageDescr,
       "cucsExtvmmMasterExtKeyFsmStamp": cucsExtvmmMasterExtKeyFsmStamp,
       "cucsExtvmmMasterExtKeyFsmStatus": cucsExtvmmMasterExtKeyFsmStatus,
       "cucsExtvmmMasterExtKeyFsmTry": cucsExtvmmMasterExtKeyFsmTry,
       "cucsExtvmmMasterExtKeyKey": cucsExtvmmMasterExtKeyKey,
       "cucsExtvmmMasterExtKeyFsmTaskTable": cucsExtvmmMasterExtKeyFsmTaskTable,
       "cucsExtvmmMasterExtKeyFsmTaskEntry": cucsExtvmmMasterExtKeyFsmTaskEntry,
       "cucsExtvmmMasterExtKeyFsmTaskInstanceId": cucsExtvmmMasterExtKeyFsmTaskInstanceId,
       "cucsExtvmmMasterExtKeyFsmTaskDn": cucsExtvmmMasterExtKeyFsmTaskDn,
       "cucsExtvmmMasterExtKeyFsmTaskRn": cucsExtvmmMasterExtKeyFsmTaskRn,
       "cucsExtvmmMasterExtKeyFsmTaskCompletion": cucsExtvmmMasterExtKeyFsmTaskCompletion,
       "cucsExtvmmMasterExtKeyFsmTaskFlags": cucsExtvmmMasterExtKeyFsmTaskFlags,
       "cucsExtvmmMasterExtKeyFsmTaskItem": cucsExtvmmMasterExtKeyFsmTaskItem,
       "cucsExtvmmMasterExtKeyFsmTaskSeqId": cucsExtvmmMasterExtKeyFsmTaskSeqId,
       "cucsExtvmmProviderTable": cucsExtvmmProviderTable,
       "cucsExtvmmProviderEntry": cucsExtvmmProviderEntry,
       "cucsExtvmmProviderInstanceId": cucsExtvmmProviderInstanceId,
       "cucsExtvmmProviderDn": cucsExtvmmProviderDn,
       "cucsExtvmmProviderRn": cucsExtvmmProviderRn,
       "cucsExtvmmProviderCert": cucsExtvmmProviderCert,
       "cucsExtvmmProviderDescr": cucsExtvmmProviderDescr,
       "cucsExtvmmProviderFsmDescr": cucsExtvmmProviderFsmDescr,
       "cucsExtvmmProviderFsmPrev": cucsExtvmmProviderFsmPrev,
       "cucsExtvmmProviderFsmProgr": cucsExtvmmProviderFsmProgr,
       "cucsExtvmmProviderFsmRmtInvErrCode": cucsExtvmmProviderFsmRmtInvErrCode,
       "cucsExtvmmProviderFsmRmtInvErrDescr": cucsExtvmmProviderFsmRmtInvErrDescr,
       "cucsExtvmmProviderFsmRmtInvRslt": cucsExtvmmProviderFsmRmtInvRslt,
       "cucsExtvmmProviderFsmStageDescr": cucsExtvmmProviderFsmStageDescr,
       "cucsExtvmmProviderFsmStamp": cucsExtvmmProviderFsmStamp,
       "cucsExtvmmProviderFsmStatus": cucsExtvmmProviderFsmStatus,
       "cucsExtvmmProviderFsmTry": cucsExtvmmProviderFsmTry,
       "cucsExtvmmProviderHost": cucsExtvmmProviderHost,
       "cucsExtvmmProviderIntId": cucsExtvmmProviderIntId,
       "cucsExtvmmProviderKey": cucsExtvmmProviderKey,
       "cucsExtvmmProviderName": cucsExtvmmProviderName,
       "cucsExtvmmProviderUuid": cucsExtvmmProviderUuid,
       "cucsExtvmmProviderVer": cucsExtvmmProviderVer,
       "cucsExtvmmProviderVerRaw": cucsExtvmmProviderVerRaw,
       "cucsExtvmmProviderPolicyLevel": cucsExtvmmProviderPolicyLevel,
       "cucsExtvmmProviderPolicyOwner": cucsExtvmmProviderPolicyOwner,
       "cucsExtvmmProviderPortValue": cucsExtvmmProviderPortValue,
       "cucsExtvmmProviderVendorType": cucsExtvmmProviderVendorType,
       "cucsExtvmmProviderFsmTaskTable": cucsExtvmmProviderFsmTaskTable,
       "cucsExtvmmProviderFsmTaskEntry": cucsExtvmmProviderFsmTaskEntry,
       "cucsExtvmmProviderFsmTaskInstanceId": cucsExtvmmProviderFsmTaskInstanceId,
       "cucsExtvmmProviderFsmTaskDn": cucsExtvmmProviderFsmTaskDn,
       "cucsExtvmmProviderFsmTaskRn": cucsExtvmmProviderFsmTaskRn,
       "cucsExtvmmProviderFsmTaskCompletion": cucsExtvmmProviderFsmTaskCompletion,
       "cucsExtvmmProviderFsmTaskFlags": cucsExtvmmProviderFsmTaskFlags,
       "cucsExtvmmProviderFsmTaskItem": cucsExtvmmProviderFsmTaskItem,
       "cucsExtvmmProviderFsmTaskSeqId": cucsExtvmmProviderFsmTaskSeqId,
       "cucsExtvmmSwitchDelTaskTable": cucsExtvmmSwitchDelTaskTable,
       "cucsExtvmmSwitchDelTaskEntry": cucsExtvmmSwitchDelTaskEntry,
       "cucsExtvmmSwitchDelTaskInstanceId": cucsExtvmmSwitchDelTaskInstanceId,
       "cucsExtvmmSwitchDelTaskDn": cucsExtvmmSwitchDelTaskDn,
       "cucsExtvmmSwitchDelTaskRn": cucsExtvmmSwitchDelTaskRn,
       "cucsExtvmmSwitchDelTaskCertFile": cucsExtvmmSwitchDelTaskCertFile,
       "cucsExtvmmSwitchDelTaskDcName": cucsExtvmmSwitchDelTaskDcName,
       "cucsExtvmmSwitchDelTaskDcOrg": cucsExtvmmSwitchDelTaskDcOrg,
       "cucsExtvmmSwitchDelTaskDescr": cucsExtvmmSwitchDelTaskDescr,
       "cucsExtvmmSwitchDelTaskExtKey": cucsExtvmmSwitchDelTaskExtKey,
       "cucsExtvmmSwitchDelTaskFsmDescr": cucsExtvmmSwitchDelTaskFsmDescr,
       "cucsExtvmmSwitchDelTaskFsmPrev": cucsExtvmmSwitchDelTaskFsmPrev,
       "cucsExtvmmSwitchDelTaskFsmProgr": cucsExtvmmSwitchDelTaskFsmProgr,
       "cucsExtvmmSwitchDelTaskFsmRmtInvErrCode": cucsExtvmmSwitchDelTaskFsmRmtInvErrCode,
       "cucsExtvmmSwitchDelTaskFsmRmtInvErrDescr": cucsExtvmmSwitchDelTaskFsmRmtInvErrDescr,
       "cucsExtvmmSwitchDelTaskFsmRmtInvRslt": cucsExtvmmSwitchDelTaskFsmRmtInvRslt,
       "cucsExtvmmSwitchDelTaskFsmStageDescr": cucsExtvmmSwitchDelTaskFsmStageDescr,
       "cucsExtvmmSwitchDelTaskFsmStamp": cucsExtvmmSwitchDelTaskFsmStamp,
       "cucsExtvmmSwitchDelTaskFsmStatus": cucsExtvmmSwitchDelTaskFsmStatus,
       "cucsExtvmmSwitchDelTaskFsmTry": cucsExtvmmSwitchDelTaskFsmTry,
       "cucsExtvmmSwitchDelTaskHost": cucsExtvmmSwitchDelTaskHost,
       "cucsExtvmmSwitchDelTaskIntId": cucsExtvmmSwitchDelTaskIntId,
       "cucsExtvmmSwitchDelTaskKeyInst": cucsExtvmmSwitchDelTaskKeyInst,
       "cucsExtvmmSwitchDelTaskName": cucsExtvmmSwitchDelTaskName,
       "cucsExtvmmSwitchDelTaskOrgPath": cucsExtvmmSwitchDelTaskOrgPath,
       "cucsExtvmmSwitchDelTaskProvIntId": cucsExtvmmSwitchDelTaskProvIntId,
       "cucsExtvmmSwitchDelTaskProvider": cucsExtvmmSwitchDelTaskProvider,
       "cucsExtvmmSwitchDelTaskSwIntId": cucsExtvmmSwitchDelTaskSwIntId,
       "cucsExtvmmSwitchDelTaskSwName": cucsExtvmmSwitchDelTaskSwName,
       "cucsExtvmmSwitchDelTaskPolicyLevel": cucsExtvmmSwitchDelTaskPolicyLevel,
       "cucsExtvmmSwitchDelTaskPolicyOwner": cucsExtvmmSwitchDelTaskPolicyOwner,
       "cucsExtvmmSwitchDelTaskPortValue": cucsExtvmmSwitchDelTaskPortValue,
       "cucsExtvmmSwitchDelTaskFsmTaskTable": cucsExtvmmSwitchDelTaskFsmTaskTable,
       "cucsExtvmmSwitchDelTaskFsmTaskEntry": cucsExtvmmSwitchDelTaskFsmTaskEntry,
       "cucsExtvmmSwitchDelTaskFsmTaskInstanceId": cucsExtvmmSwitchDelTaskFsmTaskInstanceId,
       "cucsExtvmmSwitchDelTaskFsmTaskDn": cucsExtvmmSwitchDelTaskFsmTaskDn,
       "cucsExtvmmSwitchDelTaskFsmTaskRn": cucsExtvmmSwitchDelTaskFsmTaskRn,
       "cucsExtvmmSwitchDelTaskFsmTaskCompletion": cucsExtvmmSwitchDelTaskFsmTaskCompletion,
       "cucsExtvmmSwitchDelTaskFsmTaskFlags": cucsExtvmmSwitchDelTaskFsmTaskFlags,
       "cucsExtvmmSwitchDelTaskFsmTaskItem": cucsExtvmmSwitchDelTaskFsmTaskItem,
       "cucsExtvmmSwitchDelTaskFsmTaskSeqId": cucsExtvmmSwitchDelTaskFsmTaskSeqId,
       "cucsExtvmmEpFsmTaskTable": cucsExtvmmEpFsmTaskTable,
       "cucsExtvmmEpFsmTaskEntry": cucsExtvmmEpFsmTaskEntry,
       "cucsExtvmmEpFsmTaskInstanceId": cucsExtvmmEpFsmTaskInstanceId,
       "cucsExtvmmEpFsmTaskDn": cucsExtvmmEpFsmTaskDn,
       "cucsExtvmmEpFsmTaskRn": cucsExtvmmEpFsmTaskRn,
       "cucsExtvmmEpFsmTaskCompletion": cucsExtvmmEpFsmTaskCompletion,
       "cucsExtvmmEpFsmTaskFlags": cucsExtvmmEpFsmTaskFlags,
       "cucsExtvmmEpFsmTaskItem": cucsExtvmmEpFsmTaskItem,
       "cucsExtvmmEpFsmTaskSeqId": cucsExtvmmEpFsmTaskSeqId,
       "cucsExtvmmSwitchSetTable": cucsExtvmmSwitchSetTable,
       "cucsExtvmmSwitchSetEntry": cucsExtvmmSwitchSetEntry,
       "cucsExtvmmSwitchSetInstanceId": cucsExtvmmSwitchSetInstanceId,
       "cucsExtvmmSwitchSetDn": cucsExtvmmSwitchSetDn,
       "cucsExtvmmSwitchSetRn": cucsExtvmmSwitchSetRn,
       "cucsExtvmmEpFsmTable": cucsExtvmmEpFsmTable,
       "cucsExtvmmEpFsmEntry": cucsExtvmmEpFsmEntry,
       "cucsExtvmmEpFsmInstanceId": cucsExtvmmEpFsmInstanceId,
       "cucsExtvmmEpFsmDn": cucsExtvmmEpFsmDn,
       "cucsExtvmmEpFsmRn": cucsExtvmmEpFsmRn,
       "cucsExtvmmEpFsmCompletionTime": cucsExtvmmEpFsmCompletionTime,
       "cucsExtvmmEpFsmCurrentFsm": cucsExtvmmEpFsmCurrentFsm,
       "cucsExtvmmEpFsmDescrData": cucsExtvmmEpFsmDescrData,
       "cucsExtvmmEpFsmFsmStatus": cucsExtvmmEpFsmFsmStatus,
       "cucsExtvmmEpFsmProgress": cucsExtvmmEpFsmProgress,
       "cucsExtvmmEpFsmRmtErrCode": cucsExtvmmEpFsmRmtErrCode,
       "cucsExtvmmEpFsmRmtErrDescr": cucsExtvmmEpFsmRmtErrDescr,
       "cucsExtvmmEpFsmRmtRslt": cucsExtvmmEpFsmRmtRslt,
       "cucsExtvmmEpFsmStageTable": cucsExtvmmEpFsmStageTable,
       "cucsExtvmmEpFsmStageEntry": cucsExtvmmEpFsmStageEntry,
       "cucsExtvmmEpFsmStageInstanceId": cucsExtvmmEpFsmStageInstanceId,
       "cucsExtvmmEpFsmStageDn": cucsExtvmmEpFsmStageDn,
       "cucsExtvmmEpFsmStageRn": cucsExtvmmEpFsmStageRn,
       "cucsExtvmmEpFsmStageDescrData": cucsExtvmmEpFsmStageDescrData,
       "cucsExtvmmEpFsmStageLastUpdateTime": cucsExtvmmEpFsmStageLastUpdateTime,
       "cucsExtvmmEpFsmStageName": cucsExtvmmEpFsmStageName,
       "cucsExtvmmEpFsmStageOrder": cucsExtvmmEpFsmStageOrder,
       "cucsExtvmmEpFsmStageRetry": cucsExtvmmEpFsmStageRetry,
       "cucsExtvmmEpFsmStageStageStatus": cucsExtvmmEpFsmStageStageStatus,
       "cucsExtvmmKeyStoreFsmTable": cucsExtvmmKeyStoreFsmTable,
       "cucsExtvmmKeyStoreFsmEntry": cucsExtvmmKeyStoreFsmEntry,
       "cucsExtvmmKeyStoreFsmInstanceId": cucsExtvmmKeyStoreFsmInstanceId,
       "cucsExtvmmKeyStoreFsmDn": cucsExtvmmKeyStoreFsmDn,
       "cucsExtvmmKeyStoreFsmRn": cucsExtvmmKeyStoreFsmRn,
       "cucsExtvmmKeyStoreFsmCompletionTime": cucsExtvmmKeyStoreFsmCompletionTime,
       "cucsExtvmmKeyStoreFsmCurrentFsm": cucsExtvmmKeyStoreFsmCurrentFsm,
       "cucsExtvmmKeyStoreFsmDescrData": cucsExtvmmKeyStoreFsmDescrData,
       "cucsExtvmmKeyStoreFsmFsmStatus": cucsExtvmmKeyStoreFsmFsmStatus,
       "cucsExtvmmKeyStoreFsmProgress": cucsExtvmmKeyStoreFsmProgress,
       "cucsExtvmmKeyStoreFsmRmtErrCode": cucsExtvmmKeyStoreFsmRmtErrCode,
       "cucsExtvmmKeyStoreFsmRmtErrDescr": cucsExtvmmKeyStoreFsmRmtErrDescr,
       "cucsExtvmmKeyStoreFsmRmtRslt": cucsExtvmmKeyStoreFsmRmtRslt,
       "cucsExtvmmKeyStoreFsmStageTable": cucsExtvmmKeyStoreFsmStageTable,
       "cucsExtvmmKeyStoreFsmStageEntry": cucsExtvmmKeyStoreFsmStageEntry,
       "cucsExtvmmKeyStoreFsmStageInstanceId": cucsExtvmmKeyStoreFsmStageInstanceId,
       "cucsExtvmmKeyStoreFsmStageDn": cucsExtvmmKeyStoreFsmStageDn,
       "cucsExtvmmKeyStoreFsmStageRn": cucsExtvmmKeyStoreFsmStageRn,
       "cucsExtvmmKeyStoreFsmStageDescrData": cucsExtvmmKeyStoreFsmStageDescrData,
       "cucsExtvmmKeyStoreFsmStageLastUpdateTime": cucsExtvmmKeyStoreFsmStageLastUpdateTime,
       "cucsExtvmmKeyStoreFsmStageName": cucsExtvmmKeyStoreFsmStageName,
       "cucsExtvmmKeyStoreFsmStageOrder": cucsExtvmmKeyStoreFsmStageOrder,
       "cucsExtvmmKeyStoreFsmStageRetry": cucsExtvmmKeyStoreFsmStageRetry,
       "cucsExtvmmKeyStoreFsmStageStageStatus": cucsExtvmmKeyStoreFsmStageStageStatus,
       "cucsExtvmmMasterExtKeyFsmTable": cucsExtvmmMasterExtKeyFsmTable,
       "cucsExtvmmMasterExtKeyFsmEntry": cucsExtvmmMasterExtKeyFsmEntry,
       "cucsExtvmmMasterExtKeyFsmInstanceId": cucsExtvmmMasterExtKeyFsmInstanceId,
       "cucsExtvmmMasterExtKeyFsmDn": cucsExtvmmMasterExtKeyFsmDn,
       "cucsExtvmmMasterExtKeyFsmRn": cucsExtvmmMasterExtKeyFsmRn,
       "cucsExtvmmMasterExtKeyFsmCompletionTime": cucsExtvmmMasterExtKeyFsmCompletionTime,
       "cucsExtvmmMasterExtKeyFsmCurrentFsm": cucsExtvmmMasterExtKeyFsmCurrentFsm,
       "cucsExtvmmMasterExtKeyFsmDescrData": cucsExtvmmMasterExtKeyFsmDescrData,
       "cucsExtvmmMasterExtKeyFsmFsmStatus": cucsExtvmmMasterExtKeyFsmFsmStatus,
       "cucsExtvmmMasterExtKeyFsmProgress": cucsExtvmmMasterExtKeyFsmProgress,
       "cucsExtvmmMasterExtKeyFsmRmtErrCode": cucsExtvmmMasterExtKeyFsmRmtErrCode,
       "cucsExtvmmMasterExtKeyFsmRmtErrDescr": cucsExtvmmMasterExtKeyFsmRmtErrDescr,
       "cucsExtvmmMasterExtKeyFsmRmtRslt": cucsExtvmmMasterExtKeyFsmRmtRslt,
       "cucsExtvmmMasterExtKeyFsmStageTable": cucsExtvmmMasterExtKeyFsmStageTable,
       "cucsExtvmmMasterExtKeyFsmStageEntry": cucsExtvmmMasterExtKeyFsmStageEntry,
       "cucsExtvmmMasterExtKeyFsmStageInstanceId": cucsExtvmmMasterExtKeyFsmStageInstanceId,
       "cucsExtvmmMasterExtKeyFsmStageDn": cucsExtvmmMasterExtKeyFsmStageDn,
       "cucsExtvmmMasterExtKeyFsmStageRn": cucsExtvmmMasterExtKeyFsmStageRn,
       "cucsExtvmmMasterExtKeyFsmStageDescrData": cucsExtvmmMasterExtKeyFsmStageDescrData,
       "cucsExtvmmMasterExtKeyFsmStageLastUpdateTime": cucsExtvmmMasterExtKeyFsmStageLastUpdateTime,
       "cucsExtvmmMasterExtKeyFsmStageName": cucsExtvmmMasterExtKeyFsmStageName,
       "cucsExtvmmMasterExtKeyFsmStageOrder": cucsExtvmmMasterExtKeyFsmStageOrder,
       "cucsExtvmmMasterExtKeyFsmStageRetry": cucsExtvmmMasterExtKeyFsmStageRetry,
       "cucsExtvmmMasterExtKeyFsmStageStageStatus": cucsExtvmmMasterExtKeyFsmStageStageStatus,
       "cucsExtvmmProviderFsmTable": cucsExtvmmProviderFsmTable,
       "cucsExtvmmProviderFsmEntry": cucsExtvmmProviderFsmEntry,
       "cucsExtvmmProviderFsmInstanceId": cucsExtvmmProviderFsmInstanceId,
       "cucsExtvmmProviderFsmDn": cucsExtvmmProviderFsmDn,
       "cucsExtvmmProviderFsmRn": cucsExtvmmProviderFsmRn,
       "cucsExtvmmProviderFsmCompletionTime": cucsExtvmmProviderFsmCompletionTime,
       "cucsExtvmmProviderFsmCurrentFsm": cucsExtvmmProviderFsmCurrentFsm,
       "cucsExtvmmProviderFsmDescrData": cucsExtvmmProviderFsmDescrData,
       "cucsExtvmmProviderFsmFsmStatus": cucsExtvmmProviderFsmFsmStatus,
       "cucsExtvmmProviderFsmProgress": cucsExtvmmProviderFsmProgress,
       "cucsExtvmmProviderFsmRmtErrCode": cucsExtvmmProviderFsmRmtErrCode,
       "cucsExtvmmProviderFsmRmtErrDescr": cucsExtvmmProviderFsmRmtErrDescr,
       "cucsExtvmmProviderFsmRmtRslt": cucsExtvmmProviderFsmRmtRslt,
       "cucsExtvmmProviderFsmStageTable": cucsExtvmmProviderFsmStageTable,
       "cucsExtvmmProviderFsmStageEntry": cucsExtvmmProviderFsmStageEntry,
       "cucsExtvmmProviderFsmStageInstanceId": cucsExtvmmProviderFsmStageInstanceId,
       "cucsExtvmmProviderFsmStageDn": cucsExtvmmProviderFsmStageDn,
       "cucsExtvmmProviderFsmStageRn": cucsExtvmmProviderFsmStageRn,
       "cucsExtvmmProviderFsmStageDescrData": cucsExtvmmProviderFsmStageDescrData,
       "cucsExtvmmProviderFsmStageLastUpdateTime": cucsExtvmmProviderFsmStageLastUpdateTime,
       "cucsExtvmmProviderFsmStageName": cucsExtvmmProviderFsmStageName,
       "cucsExtvmmProviderFsmStageOrder": cucsExtvmmProviderFsmStageOrder,
       "cucsExtvmmProviderFsmStageRetry": cucsExtvmmProviderFsmStageRetry,
       "cucsExtvmmProviderFsmStageStageStatus": cucsExtvmmProviderFsmStageStageStatus,
       "cucsExtvmmSwitchDelTaskFsmTable": cucsExtvmmSwitchDelTaskFsmTable,
       "cucsExtvmmSwitchDelTaskFsmEntry": cucsExtvmmSwitchDelTaskFsmEntry,
       "cucsExtvmmSwitchDelTaskFsmInstanceId": cucsExtvmmSwitchDelTaskFsmInstanceId,
       "cucsExtvmmSwitchDelTaskFsmDn": cucsExtvmmSwitchDelTaskFsmDn,
       "cucsExtvmmSwitchDelTaskFsmRn": cucsExtvmmSwitchDelTaskFsmRn,
       "cucsExtvmmSwitchDelTaskFsmCompletionTime": cucsExtvmmSwitchDelTaskFsmCompletionTime,
       "cucsExtvmmSwitchDelTaskFsmCurrentFsm": cucsExtvmmSwitchDelTaskFsmCurrentFsm,
       "cucsExtvmmSwitchDelTaskFsmDescrData": cucsExtvmmSwitchDelTaskFsmDescrData,
       "cucsExtvmmSwitchDelTaskFsmFsmStatus": cucsExtvmmSwitchDelTaskFsmFsmStatus,
       "cucsExtvmmSwitchDelTaskFsmProgress": cucsExtvmmSwitchDelTaskFsmProgress,
       "cucsExtvmmSwitchDelTaskFsmRmtErrCode": cucsExtvmmSwitchDelTaskFsmRmtErrCode,
       "cucsExtvmmSwitchDelTaskFsmRmtErrDescr": cucsExtvmmSwitchDelTaskFsmRmtErrDescr,
       "cucsExtvmmSwitchDelTaskFsmRmtRslt": cucsExtvmmSwitchDelTaskFsmRmtRslt,
       "cucsExtvmmSwitchDelTaskFsmStageTable": cucsExtvmmSwitchDelTaskFsmStageTable,
       "cucsExtvmmSwitchDelTaskFsmStageEntry": cucsExtvmmSwitchDelTaskFsmStageEntry,
       "cucsExtvmmSwitchDelTaskFsmStageInstanceId": cucsExtvmmSwitchDelTaskFsmStageInstanceId,
       "cucsExtvmmSwitchDelTaskFsmStageDn": cucsExtvmmSwitchDelTaskFsmStageDn,
       "cucsExtvmmSwitchDelTaskFsmStageRn": cucsExtvmmSwitchDelTaskFsmStageRn,
       "cucsExtvmmSwitchDelTaskFsmStageDescrData": cucsExtvmmSwitchDelTaskFsmStageDescrData,
       "cucsExtvmmSwitchDelTaskFsmStageLastUpdateTime": cucsExtvmmSwitchDelTaskFsmStageLastUpdateTime,
       "cucsExtvmmSwitchDelTaskFsmStageName": cucsExtvmmSwitchDelTaskFsmStageName,
       "cucsExtvmmSwitchDelTaskFsmStageOrder": cucsExtvmmSwitchDelTaskFsmStageOrder,
       "cucsExtvmmSwitchDelTaskFsmStageRetry": cucsExtvmmSwitchDelTaskFsmStageRetry,
       "cucsExtvmmSwitchDelTaskFsmStageStageStatus": cucsExtvmmSwitchDelTaskFsmStageStageStatus,
       "cucsExtvmmFNDReferenceTable": cucsExtvmmFNDReferenceTable,
       "cucsExtvmmFNDReferenceEntry": cucsExtvmmFNDReferenceEntry,
       "cucsExtvmmFNDReferenceInstanceId": cucsExtvmmFNDReferenceInstanceId,
       "cucsExtvmmFNDReferenceDn": cucsExtvmmFNDReferenceDn,
       "cucsExtvmmFNDReferenceRn": cucsExtvmmFNDReferenceRn,
       "cucsExtvmmFNDReferenceDescr": cucsExtvmmFNDReferenceDescr,
       "cucsExtvmmFNDReferenceFnDefName": cucsExtvmmFNDReferenceFnDefName,
       "cucsExtvmmFNDReferenceIntId": cucsExtvmmFNDReferenceIntId,
       "cucsExtvmmFNDReferenceName": cucsExtvmmFNDReferenceName,
       "cucsExtvmmFNDReferenceOperFnDefName": cucsExtvmmFNDReferenceOperFnDefName,
       "cucsExtvmmFNDReferencePolicyLevel": cucsExtvmmFNDReferencePolicyLevel,
       "cucsExtvmmFNDReferencePolicyOwner": cucsExtvmmFNDReferencePolicyOwner,
       "cucsExtvmmFabricNetworkTable": cucsExtvmmFabricNetworkTable,
       "cucsExtvmmFabricNetworkEntry": cucsExtvmmFabricNetworkEntry,
       "cucsExtvmmFabricNetworkInstanceId": cucsExtvmmFabricNetworkInstanceId,
       "cucsExtvmmFabricNetworkDn": cucsExtvmmFabricNetworkDn,
       "cucsExtvmmFabricNetworkRn": cucsExtvmmFabricNetworkRn,
       "cucsExtvmmFabricNetworkDescr": cucsExtvmmFabricNetworkDescr,
       "cucsExtvmmFabricNetworkGuid": cucsExtvmmFabricNetworkGuid,
       "cucsExtvmmFabricNetworkIntId": cucsExtvmmFabricNetworkIntId,
       "cucsExtvmmFabricNetworkName": cucsExtvmmFabricNetworkName,
       "cucsExtvmmFabricNetworkNetworkType": cucsExtvmmFabricNetworkNetworkType,
       "cucsExtvmmFabricNetworkPolicyLevel": cucsExtvmmFabricNetworkPolicyLevel,
       "cucsExtvmmFabricNetworkPolicyOwner": cucsExtvmmFabricNetworkPolicyOwner,
       "cucsExtvmmFabricNetworkRefOperState": cucsExtvmmFabricNetworkRefOperState,
       "cucsExtvmmFabricNetworkDefinitionTable": cucsExtvmmFabricNetworkDefinitionTable,
       "cucsExtvmmFabricNetworkDefinitionEntry": cucsExtvmmFabricNetworkDefinitionEntry,
       "cucsExtvmmFabricNetworkDefinitionInstanceId": cucsExtvmmFabricNetworkDefinitionInstanceId,
       "cucsExtvmmFabricNetworkDefinitionDn": cucsExtvmmFabricNetworkDefinitionDn,
       "cucsExtvmmFabricNetworkDefinitionRn": cucsExtvmmFabricNetworkDefinitionRn,
       "cucsExtvmmFabricNetworkDefinitionAllowedVnicType": cucsExtvmmFabricNetworkDefinitionAllowedVnicType,
       "cucsExtvmmFabricNetworkDefinitionDescr": cucsExtvmmFabricNetworkDefinitionDescr,
       "cucsExtvmmFabricNetworkDefinitionGuid": cucsExtvmmFabricNetworkDefinitionGuid,
       "cucsExtvmmFabricNetworkDefinitionIntId": cucsExtvmmFabricNetworkDefinitionIntId,
       "cucsExtvmmFabricNetworkDefinitionName": cucsExtvmmFabricNetworkDefinitionName,
       "cucsExtvmmFabricNetworkDefinitionPolicyLevel": cucsExtvmmFabricNetworkDefinitionPolicyLevel,
       "cucsExtvmmFabricNetworkDefinitionPolicyOwner": cucsExtvmmFabricNetworkDefinitionPolicyOwner,
       "cucsExtvmmFabricNetworkDefinitionPrimaryVlanId": cucsExtvmmFabricNetworkDefinitionPrimaryVlanId,
       "cucsExtvmmFabricNetworkDefinitionRefOperState": cucsExtvmmFabricNetworkDefinitionRefOperState,
       "cucsExtvmmNetworkSetsTable": cucsExtvmmNetworkSetsTable,
       "cucsExtvmmNetworkSetsEntry": cucsExtvmmNetworkSetsEntry,
       "cucsExtvmmNetworkSetsInstanceId": cucsExtvmmNetworkSetsInstanceId,
       "cucsExtvmmNetworkSetsDn": cucsExtvmmNetworkSetsDn,
       "cucsExtvmmNetworkSetsRn": cucsExtvmmNetworkSetsRn,
       "cucsExtvmmNetworkSetsFltAggr": cucsExtvmmNetworkSetsFltAggr,
       "cucsExtvmmNetworkSetsFsmDescr": cucsExtvmmNetworkSetsFsmDescr,
       "cucsExtvmmNetworkSetsFsmPrev": cucsExtvmmNetworkSetsFsmPrev,
       "cucsExtvmmNetworkSetsFsmProgr": cucsExtvmmNetworkSetsFsmProgr,
       "cucsExtvmmNetworkSetsFsmRmtInvErrCode": cucsExtvmmNetworkSetsFsmRmtInvErrCode,
       "cucsExtvmmNetworkSetsFsmRmtInvErrDescr": cucsExtvmmNetworkSetsFsmRmtInvErrDescr,
       "cucsExtvmmNetworkSetsFsmRmtInvRslt": cucsExtvmmNetworkSetsFsmRmtInvRslt,
       "cucsExtvmmNetworkSetsFsmStageDescr": cucsExtvmmNetworkSetsFsmStageDescr,
       "cucsExtvmmNetworkSetsFsmStamp": cucsExtvmmNetworkSetsFsmStamp,
       "cucsExtvmmNetworkSetsFsmStatus": cucsExtvmmNetworkSetsFsmStatus,
       "cucsExtvmmNetworkSetsFsmTry": cucsExtvmmNetworkSetsFsmTry,
       "cucsExtvmmNetworkSetsGenNum": cucsExtvmmNetworkSetsGenNum,
       "cucsExtvmmNetworkSetsFsmTable": cucsExtvmmNetworkSetsFsmTable,
       "cucsExtvmmNetworkSetsFsmEntry": cucsExtvmmNetworkSetsFsmEntry,
       "cucsExtvmmNetworkSetsFsmInstanceId": cucsExtvmmNetworkSetsFsmInstanceId,
       "cucsExtvmmNetworkSetsFsmDn": cucsExtvmmNetworkSetsFsmDn,
       "cucsExtvmmNetworkSetsFsmRn": cucsExtvmmNetworkSetsFsmRn,
       "cucsExtvmmNetworkSetsFsmCompletionTime": cucsExtvmmNetworkSetsFsmCompletionTime,
       "cucsExtvmmNetworkSetsFsmCurrentFsm": cucsExtvmmNetworkSetsFsmCurrentFsm,
       "cucsExtvmmNetworkSetsFsmDescrData": cucsExtvmmNetworkSetsFsmDescrData,
       "cucsExtvmmNetworkSetsFsmFsmStatus": cucsExtvmmNetworkSetsFsmFsmStatus,
       "cucsExtvmmNetworkSetsFsmProgress": cucsExtvmmNetworkSetsFsmProgress,
       "cucsExtvmmNetworkSetsFsmRmtErrCode": cucsExtvmmNetworkSetsFsmRmtErrCode,
       "cucsExtvmmNetworkSetsFsmRmtErrDescr": cucsExtvmmNetworkSetsFsmRmtErrDescr,
       "cucsExtvmmNetworkSetsFsmRmtRslt": cucsExtvmmNetworkSetsFsmRmtRslt,
       "cucsExtvmmNetworkSetsFsmStageTable": cucsExtvmmNetworkSetsFsmStageTable,
       "cucsExtvmmNetworkSetsFsmStageEntry": cucsExtvmmNetworkSetsFsmStageEntry,
       "cucsExtvmmNetworkSetsFsmStageInstanceId": cucsExtvmmNetworkSetsFsmStageInstanceId,
       "cucsExtvmmNetworkSetsFsmStageDn": cucsExtvmmNetworkSetsFsmStageDn,
       "cucsExtvmmNetworkSetsFsmStageRn": cucsExtvmmNetworkSetsFsmStageRn,
       "cucsExtvmmNetworkSetsFsmStageDescrData": cucsExtvmmNetworkSetsFsmStageDescrData,
       "cucsExtvmmNetworkSetsFsmStageLastUpdateTime": cucsExtvmmNetworkSetsFsmStageLastUpdateTime,
       "cucsExtvmmNetworkSetsFsmStageName": cucsExtvmmNetworkSetsFsmStageName,
       "cucsExtvmmNetworkSetsFsmStageOrder": cucsExtvmmNetworkSetsFsmStageOrder,
       "cucsExtvmmNetworkSetsFsmStageRetry": cucsExtvmmNetworkSetsFsmStageRetry,
       "cucsExtvmmNetworkSetsFsmStageStageStatus": cucsExtvmmNetworkSetsFsmStageStageStatus,
       "cucsExtvmmNetworkSetsFsmTaskTable": cucsExtvmmNetworkSetsFsmTaskTable,
       "cucsExtvmmNetworkSetsFsmTaskEntry": cucsExtvmmNetworkSetsFsmTaskEntry,
       "cucsExtvmmNetworkSetsFsmTaskInstanceId": cucsExtvmmNetworkSetsFsmTaskInstanceId,
       "cucsExtvmmNetworkSetsFsmTaskDn": cucsExtvmmNetworkSetsFsmTaskDn,
       "cucsExtvmmNetworkSetsFsmTaskRn": cucsExtvmmNetworkSetsFsmTaskRn,
       "cucsExtvmmNetworkSetsFsmTaskCompletion": cucsExtvmmNetworkSetsFsmTaskCompletion,
       "cucsExtvmmNetworkSetsFsmTaskFlags": cucsExtvmmNetworkSetsFsmTaskFlags,
       "cucsExtvmmNetworkSetsFsmTaskItem": cucsExtvmmNetworkSetsFsmTaskItem,
       "cucsExtvmmNetworkSetsFsmTaskSeqId": cucsExtvmmNetworkSetsFsmTaskSeqId,
       "cucsExtvmmUpLinkPPTable": cucsExtvmmUpLinkPPTable,
       "cucsExtvmmUpLinkPPEntry": cucsExtvmmUpLinkPPEntry,
       "cucsExtvmmUpLinkPPInstanceId": cucsExtvmmUpLinkPPInstanceId,
       "cucsExtvmmUpLinkPPDn": cucsExtvmmUpLinkPPDn,
       "cucsExtvmmUpLinkPPRn": cucsExtvmmUpLinkPPRn,
       "cucsExtvmmUpLinkPPDescr": cucsExtvmmUpLinkPPDescr,
       "cucsExtvmmUpLinkPPFltAggr": cucsExtvmmUpLinkPPFltAggr,
       "cucsExtvmmUpLinkPPGuid": cucsExtvmmUpLinkPPGuid,
       "cucsExtvmmUpLinkPPIntId": cucsExtvmmUpLinkPPIntId,
       "cucsExtvmmUpLinkPPName": cucsExtvmmUpLinkPPName,
       "cucsExtvmmUpLinkPPPolicyLevel": cucsExtvmmUpLinkPPPolicyLevel,
       "cucsExtvmmUpLinkPPPolicyOwner": cucsExtvmmUpLinkPPPolicyOwner,
       "cucsExtvmmUpLinkPPRefOperState": cucsExtvmmUpLinkPPRefOperState,
       "cucsExtvmmVMNDRefTable": cucsExtvmmVMNDRefTable,
       "cucsExtvmmVMNDRefEntry": cucsExtvmmVMNDRefEntry,
       "cucsExtvmmVMNDRefInstanceId": cucsExtvmmVMNDRefInstanceId,
       "cucsExtvmmVMNDRefDn": cucsExtvmmVMNDRefDn,
       "cucsExtvmmVMNDRefRn": cucsExtvmmVMNDRefRn,
       "cucsExtvmmVMNDRefConfigQualifier": cucsExtvmmVMNDRefConfigQualifier,
       "cucsExtvmmVMNDRefDescr": cucsExtvmmVMNDRefDescr,
       "cucsExtvmmVMNDRefFnDefName": cucsExtvmmVMNDRefFnDefName,
       "cucsExtvmmVMNDRefFnName": cucsExtvmmVMNDRefFnName,
       "cucsExtvmmVMNDRefIntId": cucsExtvmmVMNDRefIntId,
       "cucsExtvmmVMNDRefName": cucsExtvmmVMNDRefName,
       "cucsExtvmmVMNDRefOperVmNetworkDefName": cucsExtvmmVMNDRefOperVmNetworkDefName,
       "cucsExtvmmVMNDRefPolicyLevel": cucsExtvmmVMNDRefPolicyLevel,
       "cucsExtvmmVMNDRefPolicyOwner": cucsExtvmmVMNDRefPolicyOwner,
       "cucsExtvmmVMNDRefVmNetworkDefName": cucsExtvmmVMNDRefVmNetworkDefName,
       "cucsExtvmmVMNetworkTable": cucsExtvmmVMNetworkTable,
       "cucsExtvmmVMNetworkEntry": cucsExtvmmVMNetworkEntry,
       "cucsExtvmmVMNetworkInstanceId": cucsExtvmmVMNetworkInstanceId,
       "cucsExtvmmVMNetworkDn": cucsExtvmmVMNetworkDn,
       "cucsExtvmmVMNetworkRn": cucsExtvmmVMNetworkRn,
       "cucsExtvmmVMNetworkDescr": cucsExtvmmVMNetworkDescr,
       "cucsExtvmmVMNetworkFabricNetworkName": cucsExtvmmVMNetworkFabricNetworkName,
       "cucsExtvmmVMNetworkFltAggr": cucsExtvmmVMNetworkFltAggr,
       "cucsExtvmmVMNetworkGuid": cucsExtvmmVMNetworkGuid,
       "cucsExtvmmVMNetworkIntId": cucsExtvmmVMNetworkIntId,
       "cucsExtvmmVMNetworkName": cucsExtvmmVMNetworkName,
       "cucsExtvmmVMNetworkOperFabricNetworkName": cucsExtvmmVMNetworkOperFabricNetworkName,
       "cucsExtvmmVMNetworkPolicyLevel": cucsExtvmmVMNetworkPolicyLevel,
       "cucsExtvmmVMNetworkPolicyOwner": cucsExtvmmVMNetworkPolicyOwner,
       "cucsExtvmmVMNetworkDefinitionTable": cucsExtvmmVMNetworkDefinitionTable,
       "cucsExtvmmVMNetworkDefinitionEntry": cucsExtvmmVMNetworkDefinitionEntry,
       "cucsExtvmmVMNetworkDefinitionInstanceId": cucsExtvmmVMNetworkDefinitionInstanceId,
       "cucsExtvmmVMNetworkDefinitionDn": cucsExtvmmVMNetworkDefinitionDn,
       "cucsExtvmmVMNetworkDefinitionRn": cucsExtvmmVMNetworkDefinitionRn,
       "cucsExtvmmVMNetworkDefinitionDescr": cucsExtvmmVMNetworkDefinitionDescr,
       "cucsExtvmmVMNetworkDefinitionExtIpPoolName": cucsExtvmmVMNetworkDefinitionExtIpPoolName,
       "cucsExtvmmVMNetworkDefinitionGuid": cucsExtvmmVMNetworkDefinitionGuid,
       "cucsExtvmmVMNetworkDefinitionIntId": cucsExtvmmVMNetworkDefinitionIntId,
       "cucsExtvmmVMNetworkDefinitionIpPoolGuid": cucsExtvmmVMNetworkDefinitionIpPoolGuid,
       "cucsExtvmmVMNetworkDefinitionMaxPorts": cucsExtvmmVMNetworkDefinitionMaxPorts,
       "cucsExtvmmVMNetworkDefinitionName": cucsExtvmmVMNetworkDefinitionName,
       "cucsExtvmmVMNetworkDefinitionOperExtIpPoolName": cucsExtvmmVMNetworkDefinitionOperExtIpPoolName,
       "cucsExtvmmVMNetworkDefinitionPolicyLevel": cucsExtvmmVMNetworkDefinitionPolicyLevel,
       "cucsExtvmmVMNetworkDefinitionPolicyOwner": cucsExtvmmVMNetworkDefinitionPolicyOwner,
       "cucsExtvmmVMNetworkDefinitionPrimaryVlanId": cucsExtvmmVMNetworkDefinitionPrimaryVlanId,
       "cucsExtvmmVMNetworkDefinitionRefOperState": cucsExtvmmVMNetworkDefinitionRefOperState,
       "cucsExtvmmVMNetworkDefinitionVlanName": cucsExtvmmVMNetworkDefinitionVlanName,
       "cucsExtvmmVMNetworkSetsTable": cucsExtvmmVMNetworkSetsTable,
       "cucsExtvmmVMNetworkSetsEntry": cucsExtvmmVMNetworkSetsEntry,
       "cucsExtvmmVMNetworkSetsInstanceId": cucsExtvmmVMNetworkSetsInstanceId,
       "cucsExtvmmVMNetworkSetsDn": cucsExtvmmVMNetworkSetsDn,
       "cucsExtvmmVMNetworkSetsRn": cucsExtvmmVMNetworkSetsRn,
       "cucsExtvmmVMNetworkSetsFltAggr": cucsExtvmmVMNetworkSetsFltAggr,
       "cucsExtvmmVMNetworkSetsGenNum": cucsExtvmmVMNetworkSetsGenNum}
)
