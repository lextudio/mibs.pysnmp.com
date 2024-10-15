# SNMP MIB module (CISCO-UNIFIED-COMPUTING-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-LICENSE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:49 2024
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
 CucsLicenseDownloadActivity,
 CucsLicenseDownloaderFsmCurrentFsm,
 CucsLicenseDownloaderFsmStageName,
 CucsLicenseDownloaderFsmTaskItem,
 CucsLicenseFeatureType,
 CucsLicenseFileFsmCurrentFsm,
 CucsLicenseFileFsmStageName,
 CucsLicenseFileFsmTaskItem,
 CucsLicenseFileState,
 CucsLicenseInstanceFsmCurrentFsm,
 CucsLicenseInstanceFsmStageName,
 CucsLicenseInstanceFsmTaskItem,
 CucsLicensePeerStatus,
 CucsLicenseScope,
 CucsLicenseState,
 CucsLicenseTransferState,
 CucsLicenseTransport,
 CucsLicenseType,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsLicenseDownloadActivity",
    "CucsLicenseDownloaderFsmCurrentFsm",
    "CucsLicenseDownloaderFsmStageName",
    "CucsLicenseDownloaderFsmTaskItem",
    "CucsLicenseFeatureType",
    "CucsLicenseFileFsmCurrentFsm",
    "CucsLicenseFileFsmStageName",
    "CucsLicenseFileFsmTaskItem",
    "CucsLicenseFileState",
    "CucsLicenseInstanceFsmCurrentFsm",
    "CucsLicenseInstanceFsmStageName",
    "CucsLicenseInstanceFsmTaskItem",
    "CucsLicensePeerStatus",
    "CucsLicenseScope",
    "CucsLicenseState",
    "CucsLicenseTransferState",
    "CucsLicenseTransport",
    "CucsLicenseType",
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

cucsLicenseObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsLicenseContentsTable_Object = MibTable
cucsLicenseContentsTable = _CucsLicenseContentsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 1)
)
if mibBuilder.loadTexts:
    cucsLicenseContentsTable.setStatus("current")
_CucsLicenseContentsEntry_Object = MibTableRow
cucsLicenseContentsEntry = _CucsLicenseContentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 1, 1)
)
cucsLicenseContentsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseContentsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseContentsEntry.setStatus("current")
_CucsLicenseContentsInstanceId_Type = CucsManagedObjectId
_CucsLicenseContentsInstanceId_Object = MibTableColumn
cucsLicenseContentsInstanceId = _CucsLicenseContentsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 1, 1, 1),
    _CucsLicenseContentsInstanceId_Type()
)
cucsLicenseContentsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseContentsInstanceId.setStatus("current")
_CucsLicenseContentsDn_Type = CucsManagedObjectDn
_CucsLicenseContentsDn_Object = MibTableColumn
cucsLicenseContentsDn = _CucsLicenseContentsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 1, 1, 2),
    _CucsLicenseContentsDn_Type()
)
cucsLicenseContentsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseContentsDn.setStatus("current")
_CucsLicenseContentsRn_Type = SnmpAdminString
_CucsLicenseContentsRn_Object = MibTableColumn
cucsLicenseContentsRn = _CucsLicenseContentsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 1, 1, 3),
    _CucsLicenseContentsRn_Type()
)
cucsLicenseContentsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseContentsRn.setStatus("current")
_CucsLicenseContentsFeatureName_Type = SnmpAdminString
_CucsLicenseContentsFeatureName_Object = MibTableColumn
cucsLicenseContentsFeatureName = _CucsLicenseContentsFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 1, 1, 4),
    _CucsLicenseContentsFeatureName_Type()
)
cucsLicenseContentsFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseContentsFeatureName.setStatus("current")
_CucsLicenseContentsTotalQuant_Type = Gauge32
_CucsLicenseContentsTotalQuant_Object = MibTableColumn
cucsLicenseContentsTotalQuant = _CucsLicenseContentsTotalQuant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 1, 1, 5),
    _CucsLicenseContentsTotalQuant_Type()
)
cucsLicenseContentsTotalQuant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseContentsTotalQuant.setStatus("current")
_CucsLicenseContentsVendor_Type = SnmpAdminString
_CucsLicenseContentsVendor_Object = MibTableColumn
cucsLicenseContentsVendor = _CucsLicenseContentsVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 1, 1, 6),
    _CucsLicenseContentsVendor_Type()
)
cucsLicenseContentsVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseContentsVendor.setStatus("current")
_CucsLicenseContentsVersion_Type = SnmpAdminString
_CucsLicenseContentsVersion_Object = MibTableColumn
cucsLicenseContentsVersion = _CucsLicenseContentsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 1, 1, 7),
    _CucsLicenseContentsVersion_Type()
)
cucsLicenseContentsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseContentsVersion.setStatus("current")
_CucsLicenseDownloaderTable_Object = MibTable
cucsLicenseDownloaderTable = _CucsLicenseDownloaderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2)
)
if mibBuilder.loadTexts:
    cucsLicenseDownloaderTable.setStatus("current")
_CucsLicenseDownloaderEntry_Object = MibTableRow
cucsLicenseDownloaderEntry = _CucsLicenseDownloaderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1)
)
cucsLicenseDownloaderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseDownloaderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseDownloaderEntry.setStatus("current")
_CucsLicenseDownloaderInstanceId_Type = CucsManagedObjectId
_CucsLicenseDownloaderInstanceId_Object = MibTableColumn
cucsLicenseDownloaderInstanceId = _CucsLicenseDownloaderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 1),
    _CucsLicenseDownloaderInstanceId_Type()
)
cucsLicenseDownloaderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderInstanceId.setStatus("current")
_CucsLicenseDownloaderDn_Type = CucsManagedObjectDn
_CucsLicenseDownloaderDn_Object = MibTableColumn
cucsLicenseDownloaderDn = _CucsLicenseDownloaderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 2),
    _CucsLicenseDownloaderDn_Type()
)
cucsLicenseDownloaderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderDn.setStatus("current")
_CucsLicenseDownloaderRn_Type = SnmpAdminString
_CucsLicenseDownloaderRn_Object = MibTableColumn
cucsLicenseDownloaderRn = _CucsLicenseDownloaderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 3),
    _CucsLicenseDownloaderRn_Type()
)
cucsLicenseDownloaderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderRn.setStatus("current")
_CucsLicenseDownloaderAdminState_Type = CucsLicenseDownloadActivity
_CucsLicenseDownloaderAdminState_Object = MibTableColumn
cucsLicenseDownloaderAdminState = _CucsLicenseDownloaderAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 4),
    _CucsLicenseDownloaderAdminState_Type()
)
cucsLicenseDownloaderAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderAdminState.setStatus("current")
_CucsLicenseDownloaderFileName_Type = SnmpAdminString
_CucsLicenseDownloaderFileName_Object = MibTableColumn
cucsLicenseDownloaderFileName = _CucsLicenseDownloaderFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 5),
    _CucsLicenseDownloaderFileName_Type()
)
cucsLicenseDownloaderFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFileName.setStatus("current")
_CucsLicenseDownloaderFsmDescr_Type = SnmpAdminString
_CucsLicenseDownloaderFsmDescr_Object = MibTableColumn
cucsLicenseDownloaderFsmDescr = _CucsLicenseDownloaderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 6),
    _CucsLicenseDownloaderFsmDescr_Type()
)
cucsLicenseDownloaderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmDescr.setStatus("current")
_CucsLicenseDownloaderFsmPrev_Type = SnmpAdminString
_CucsLicenseDownloaderFsmPrev_Object = MibTableColumn
cucsLicenseDownloaderFsmPrev = _CucsLicenseDownloaderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 7),
    _CucsLicenseDownloaderFsmPrev_Type()
)
cucsLicenseDownloaderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmPrev.setStatus("current")
_CucsLicenseDownloaderFsmProgr_Type = Gauge32
_CucsLicenseDownloaderFsmProgr_Object = MibTableColumn
cucsLicenseDownloaderFsmProgr = _CucsLicenseDownloaderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 8),
    _CucsLicenseDownloaderFsmProgr_Type()
)
cucsLicenseDownloaderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmProgr.setStatus("current")
_CucsLicenseDownloaderFsmRmtInvErrCode_Type = Gauge32
_CucsLicenseDownloaderFsmRmtInvErrCode_Object = MibTableColumn
cucsLicenseDownloaderFsmRmtInvErrCode = _CucsLicenseDownloaderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 9),
    _CucsLicenseDownloaderFsmRmtInvErrCode_Type()
)
cucsLicenseDownloaderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmRmtInvErrCode.setStatus("current")
_CucsLicenseDownloaderFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsLicenseDownloaderFsmRmtInvErrDescr_Object = MibTableColumn
cucsLicenseDownloaderFsmRmtInvErrDescr = _CucsLicenseDownloaderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 10),
    _CucsLicenseDownloaderFsmRmtInvErrDescr_Type()
)
cucsLicenseDownloaderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmRmtInvErrDescr.setStatus("current")
_CucsLicenseDownloaderFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsLicenseDownloaderFsmRmtInvRslt_Object = MibTableColumn
cucsLicenseDownloaderFsmRmtInvRslt = _CucsLicenseDownloaderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 11),
    _CucsLicenseDownloaderFsmRmtInvRslt_Type()
)
cucsLicenseDownloaderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmRmtInvRslt.setStatus("current")
_CucsLicenseDownloaderFsmStageDescr_Type = SnmpAdminString
_CucsLicenseDownloaderFsmStageDescr_Object = MibTableColumn
cucsLicenseDownloaderFsmStageDescr = _CucsLicenseDownloaderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 12),
    _CucsLicenseDownloaderFsmStageDescr_Type()
)
cucsLicenseDownloaderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStageDescr.setStatus("current")
_CucsLicenseDownloaderFsmStamp_Type = DateAndTime
_CucsLicenseDownloaderFsmStamp_Object = MibTableColumn
cucsLicenseDownloaderFsmStamp = _CucsLicenseDownloaderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 13),
    _CucsLicenseDownloaderFsmStamp_Type()
)
cucsLicenseDownloaderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStamp.setStatus("current")
_CucsLicenseDownloaderFsmStatus_Type = SnmpAdminString
_CucsLicenseDownloaderFsmStatus_Object = MibTableColumn
cucsLicenseDownloaderFsmStatus = _CucsLicenseDownloaderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 14),
    _CucsLicenseDownloaderFsmStatus_Type()
)
cucsLicenseDownloaderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStatus.setStatus("current")
_CucsLicenseDownloaderFsmTry_Type = Gauge32
_CucsLicenseDownloaderFsmTry_Object = MibTableColumn
cucsLicenseDownloaderFsmTry = _CucsLicenseDownloaderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 15),
    _CucsLicenseDownloaderFsmTry_Type()
)
cucsLicenseDownloaderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmTry.setStatus("current")
_CucsLicenseDownloaderProt_Type = CucsLicenseTransport
_CucsLicenseDownloaderProt_Object = MibTableColumn
cucsLicenseDownloaderProt = _CucsLicenseDownloaderProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 16),
    _CucsLicenseDownloaderProt_Type()
)
cucsLicenseDownloaderProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderProt.setStatus("current")
_CucsLicenseDownloaderPwd_Type = SnmpAdminString
_CucsLicenseDownloaderPwd_Object = MibTableColumn
cucsLicenseDownloaderPwd = _CucsLicenseDownloaderPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 17),
    _CucsLicenseDownloaderPwd_Type()
)
cucsLicenseDownloaderPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderPwd.setStatus("current")
_CucsLicenseDownloaderRemotePath_Type = SnmpAdminString
_CucsLicenseDownloaderRemotePath_Object = MibTableColumn
cucsLicenseDownloaderRemotePath = _CucsLicenseDownloaderRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 18),
    _CucsLicenseDownloaderRemotePath_Type()
)
cucsLicenseDownloaderRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderRemotePath.setStatus("current")
_CucsLicenseDownloaderServer_Type = SnmpAdminString
_CucsLicenseDownloaderServer_Object = MibTableColumn
cucsLicenseDownloaderServer = _CucsLicenseDownloaderServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 19),
    _CucsLicenseDownloaderServer_Type()
)
cucsLicenseDownloaderServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderServer.setStatus("current")
_CucsLicenseDownloaderTransferState_Type = CucsLicenseTransferState
_CucsLicenseDownloaderTransferState_Object = MibTableColumn
cucsLicenseDownloaderTransferState = _CucsLicenseDownloaderTransferState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 20),
    _CucsLicenseDownloaderTransferState_Type()
)
cucsLicenseDownloaderTransferState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderTransferState.setStatus("current")
_CucsLicenseDownloaderUser_Type = SnmpAdminString
_CucsLicenseDownloaderUser_Object = MibTableColumn
cucsLicenseDownloaderUser = _CucsLicenseDownloaderUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 2, 1, 21),
    _CucsLicenseDownloaderUser_Type()
)
cucsLicenseDownloaderUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderUser.setStatus("current")
_CucsLicenseDownloaderFsmTaskTable_Object = MibTable
cucsLicenseDownloaderFsmTaskTable = _CucsLicenseDownloaderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 3)
)
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmTaskTable.setStatus("current")
_CucsLicenseDownloaderFsmTaskEntry_Object = MibTableRow
cucsLicenseDownloaderFsmTaskEntry = _CucsLicenseDownloaderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 3, 1)
)
cucsLicenseDownloaderFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseDownloaderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmTaskEntry.setStatus("current")
_CucsLicenseDownloaderFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsLicenseDownloaderFsmTaskInstanceId_Object = MibTableColumn
cucsLicenseDownloaderFsmTaskInstanceId = _CucsLicenseDownloaderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 3, 1, 1),
    _CucsLicenseDownloaderFsmTaskInstanceId_Type()
)
cucsLicenseDownloaderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmTaskInstanceId.setStatus("current")
_CucsLicenseDownloaderFsmTaskDn_Type = CucsManagedObjectDn
_CucsLicenseDownloaderFsmTaskDn_Object = MibTableColumn
cucsLicenseDownloaderFsmTaskDn = _CucsLicenseDownloaderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 3, 1, 2),
    _CucsLicenseDownloaderFsmTaskDn_Type()
)
cucsLicenseDownloaderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmTaskDn.setStatus("current")
_CucsLicenseDownloaderFsmTaskRn_Type = SnmpAdminString
_CucsLicenseDownloaderFsmTaskRn_Object = MibTableColumn
cucsLicenseDownloaderFsmTaskRn = _CucsLicenseDownloaderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 3, 1, 3),
    _CucsLicenseDownloaderFsmTaskRn_Type()
)
cucsLicenseDownloaderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmTaskRn.setStatus("current")
_CucsLicenseDownloaderFsmTaskCompletion_Type = CucsFsmCompletion
_CucsLicenseDownloaderFsmTaskCompletion_Object = MibTableColumn
cucsLicenseDownloaderFsmTaskCompletion = _CucsLicenseDownloaderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 3, 1, 4),
    _CucsLicenseDownloaderFsmTaskCompletion_Type()
)
cucsLicenseDownloaderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmTaskCompletion.setStatus("current")
_CucsLicenseDownloaderFsmTaskFlags_Type = CucsFsmFlags
_CucsLicenseDownloaderFsmTaskFlags_Object = MibTableColumn
cucsLicenseDownloaderFsmTaskFlags = _CucsLicenseDownloaderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 3, 1, 5),
    _CucsLicenseDownloaderFsmTaskFlags_Type()
)
cucsLicenseDownloaderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmTaskFlags.setStatus("current")
_CucsLicenseDownloaderFsmTaskItem_Type = CucsLicenseDownloaderFsmTaskItem
_CucsLicenseDownloaderFsmTaskItem_Object = MibTableColumn
cucsLicenseDownloaderFsmTaskItem = _CucsLicenseDownloaderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 3, 1, 6),
    _CucsLicenseDownloaderFsmTaskItem_Type()
)
cucsLicenseDownloaderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmTaskItem.setStatus("current")
_CucsLicenseDownloaderFsmTaskSeqId_Type = Gauge32
_CucsLicenseDownloaderFsmTaskSeqId_Object = MibTableColumn
cucsLicenseDownloaderFsmTaskSeqId = _CucsLicenseDownloaderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 3, 1, 7),
    _CucsLicenseDownloaderFsmTaskSeqId_Type()
)
cucsLicenseDownloaderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmTaskSeqId.setStatus("current")
_CucsLicenseEpTable_Object = MibTable
cucsLicenseEpTable = _CucsLicenseEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 4)
)
if mibBuilder.loadTexts:
    cucsLicenseEpTable.setStatus("current")
_CucsLicenseEpEntry_Object = MibTableRow
cucsLicenseEpEntry = _CucsLicenseEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 4, 1)
)
cucsLicenseEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseEpEntry.setStatus("current")
_CucsLicenseEpInstanceId_Type = CucsManagedObjectId
_CucsLicenseEpInstanceId_Object = MibTableColumn
cucsLicenseEpInstanceId = _CucsLicenseEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 4, 1, 1),
    _CucsLicenseEpInstanceId_Type()
)
cucsLicenseEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseEpInstanceId.setStatus("current")
_CucsLicenseEpDn_Type = CucsManagedObjectDn
_CucsLicenseEpDn_Object = MibTableColumn
cucsLicenseEpDn = _CucsLicenseEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 4, 1, 2),
    _CucsLicenseEpDn_Type()
)
cucsLicenseEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseEpDn.setStatus("current")
_CucsLicenseEpRn_Type = SnmpAdminString
_CucsLicenseEpRn_Object = MibTableColumn
cucsLicenseEpRn = _CucsLicenseEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 4, 1, 3),
    _CucsLicenseEpRn_Type()
)
cucsLicenseEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseEpRn.setStatus("current")
_CucsLicenseFeatureTable_Object = MibTable
cucsLicenseFeatureTable = _CucsLicenseFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5)
)
if mibBuilder.loadTexts:
    cucsLicenseFeatureTable.setStatus("current")
_CucsLicenseFeatureEntry_Object = MibTableRow
cucsLicenseFeatureEntry = _CucsLicenseFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1)
)
cucsLicenseFeatureEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseFeatureInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseFeatureEntry.setStatus("current")
_CucsLicenseFeatureInstanceId_Type = CucsManagedObjectId
_CucsLicenseFeatureInstanceId_Object = MibTableColumn
cucsLicenseFeatureInstanceId = _CucsLicenseFeatureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1, 1),
    _CucsLicenseFeatureInstanceId_Type()
)
cucsLicenseFeatureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseFeatureInstanceId.setStatus("current")
_CucsLicenseFeatureDn_Type = CucsManagedObjectDn
_CucsLicenseFeatureDn_Object = MibTableColumn
cucsLicenseFeatureDn = _CucsLicenseFeatureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1, 2),
    _CucsLicenseFeatureDn_Type()
)
cucsLicenseFeatureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureDn.setStatus("current")
_CucsLicenseFeatureRn_Type = SnmpAdminString
_CucsLicenseFeatureRn_Object = MibTableColumn
cucsLicenseFeatureRn = _CucsLicenseFeatureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1, 3),
    _CucsLicenseFeatureRn_Type()
)
cucsLicenseFeatureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureRn.setStatus("current")
_CucsLicenseFeatureDescr_Type = SnmpAdminString
_CucsLicenseFeatureDescr_Object = MibTableColumn
cucsLicenseFeatureDescr = _CucsLicenseFeatureDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1, 4),
    _CucsLicenseFeatureDescr_Type()
)
cucsLicenseFeatureDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureDescr.setStatus("current")
_CucsLicenseFeatureGracePeriod_Type = Unsigned64
_CucsLicenseFeatureGracePeriod_Object = MibTableColumn
cucsLicenseFeatureGracePeriod = _CucsLicenseFeatureGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1, 5),
    _CucsLicenseFeatureGracePeriod_Type()
)
cucsLicenseFeatureGracePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureGracePeriod.setStatus("current")
_CucsLicenseFeatureIntId_Type = SnmpAdminString
_CucsLicenseFeatureIntId_Object = MibTableColumn
cucsLicenseFeatureIntId = _CucsLicenseFeatureIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1, 6),
    _CucsLicenseFeatureIntId_Type()
)
cucsLicenseFeatureIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureIntId.setStatus("current")
_CucsLicenseFeatureName_Type = SnmpAdminString
_CucsLicenseFeatureName_Object = MibTableColumn
cucsLicenseFeatureName = _CucsLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1, 7),
    _CucsLicenseFeatureName_Type()
)
cucsLicenseFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureName.setStatus("current")
_CucsLicenseFeatureType_Type = CucsLicenseFeatureType
_CucsLicenseFeatureType_Object = MibTableColumn
cucsLicenseFeatureType = _CucsLicenseFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1, 8),
    _CucsLicenseFeatureType_Type()
)
cucsLicenseFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureType.setStatus("current")
_CucsLicenseFeatureVendor_Type = SnmpAdminString
_CucsLicenseFeatureVendor_Object = MibTableColumn
cucsLicenseFeatureVendor = _CucsLicenseFeatureVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1, 9),
    _CucsLicenseFeatureVendor_Type()
)
cucsLicenseFeatureVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureVendor.setStatus("current")
_CucsLicenseFeatureVersion_Type = SnmpAdminString
_CucsLicenseFeatureVersion_Object = MibTableColumn
cucsLicenseFeatureVersion = _CucsLicenseFeatureVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1, 10),
    _CucsLicenseFeatureVersion_Type()
)
cucsLicenseFeatureVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureVersion.setStatus("current")
_CucsLicenseFeaturePolicyLevel_Type = Gauge32
_CucsLicenseFeaturePolicyLevel_Object = MibTableColumn
cucsLicenseFeaturePolicyLevel = _CucsLicenseFeaturePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1, 11),
    _CucsLicenseFeaturePolicyLevel_Type()
)
cucsLicenseFeaturePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeaturePolicyLevel.setStatus("current")
_CucsLicenseFeaturePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsLicenseFeaturePolicyOwner_Object = MibTableColumn
cucsLicenseFeaturePolicyOwner = _CucsLicenseFeaturePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 5, 1, 12),
    _CucsLicenseFeaturePolicyOwner_Type()
)
cucsLicenseFeaturePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeaturePolicyOwner.setStatus("current")
_CucsLicenseFeatureCapProviderTable_Object = MibTable
cucsLicenseFeatureCapProviderTable = _CucsLicenseFeatureCapProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6)
)
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderTable.setStatus("current")
_CucsLicenseFeatureCapProviderEntry_Object = MibTableRow
cucsLicenseFeatureCapProviderEntry = _CucsLicenseFeatureCapProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1)
)
cucsLicenseFeatureCapProviderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseFeatureCapProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderEntry.setStatus("current")
_CucsLicenseFeatureCapProviderInstanceId_Type = CucsManagedObjectId
_CucsLicenseFeatureCapProviderInstanceId_Object = MibTableColumn
cucsLicenseFeatureCapProviderInstanceId = _CucsLicenseFeatureCapProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 1),
    _CucsLicenseFeatureCapProviderInstanceId_Type()
)
cucsLicenseFeatureCapProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderInstanceId.setStatus("current")
_CucsLicenseFeatureCapProviderDn_Type = CucsManagedObjectDn
_CucsLicenseFeatureCapProviderDn_Object = MibTableColumn
cucsLicenseFeatureCapProviderDn = _CucsLicenseFeatureCapProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 2),
    _CucsLicenseFeatureCapProviderDn_Type()
)
cucsLicenseFeatureCapProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderDn.setStatus("current")
_CucsLicenseFeatureCapProviderRn_Type = SnmpAdminString
_CucsLicenseFeatureCapProviderRn_Object = MibTableColumn
cucsLicenseFeatureCapProviderRn = _CucsLicenseFeatureCapProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 3),
    _CucsLicenseFeatureCapProviderRn_Type()
)
cucsLicenseFeatureCapProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderRn.setStatus("current")
_CucsLicenseFeatureCapProviderDefQuant_Type = Gauge32
_CucsLicenseFeatureCapProviderDefQuant_Object = MibTableColumn
cucsLicenseFeatureCapProviderDefQuant = _CucsLicenseFeatureCapProviderDefQuant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 4),
    _CucsLicenseFeatureCapProviderDefQuant_Type()
)
cucsLicenseFeatureCapProviderDefQuant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderDefQuant.setStatus("current")
_CucsLicenseFeatureCapProviderDeprecated_Type = TruthValue
_CucsLicenseFeatureCapProviderDeprecated_Object = MibTableColumn
cucsLicenseFeatureCapProviderDeprecated = _CucsLicenseFeatureCapProviderDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 5),
    _CucsLicenseFeatureCapProviderDeprecated_Type()
)
cucsLicenseFeatureCapProviderDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderDeprecated.setStatus("current")
_CucsLicenseFeatureCapProviderFeatureName_Type = SnmpAdminString
_CucsLicenseFeatureCapProviderFeatureName_Object = MibTableColumn
cucsLicenseFeatureCapProviderFeatureName = _CucsLicenseFeatureCapProviderFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 6),
    _CucsLicenseFeatureCapProviderFeatureName_Type()
)
cucsLicenseFeatureCapProviderFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderFeatureName.setStatus("current")
_CucsLicenseFeatureCapProviderGencount_Type = Gauge32
_CucsLicenseFeatureCapProviderGencount_Object = MibTableColumn
cucsLicenseFeatureCapProviderGencount = _CucsLicenseFeatureCapProviderGencount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 7),
    _CucsLicenseFeatureCapProviderGencount_Type()
)
cucsLicenseFeatureCapProviderGencount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderGencount.setStatus("current")
_CucsLicenseFeatureCapProviderGracePeriod_Type = Unsigned64
_CucsLicenseFeatureCapProviderGracePeriod_Object = MibTableColumn
cucsLicenseFeatureCapProviderGracePeriod = _CucsLicenseFeatureCapProviderGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 8),
    _CucsLicenseFeatureCapProviderGracePeriod_Type()
)
cucsLicenseFeatureCapProviderGracePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderGracePeriod.setStatus("current")
_CucsLicenseFeatureCapProviderLicVendor_Type = SnmpAdminString
_CucsLicenseFeatureCapProviderLicVendor_Object = MibTableColumn
cucsLicenseFeatureCapProviderLicVendor = _CucsLicenseFeatureCapProviderLicVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 9),
    _CucsLicenseFeatureCapProviderLicVendor_Type()
)
cucsLicenseFeatureCapProviderLicVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderLicVendor.setStatus("current")
_CucsLicenseFeatureCapProviderLicVersion_Type = SnmpAdminString
_CucsLicenseFeatureCapProviderLicVersion_Object = MibTableColumn
cucsLicenseFeatureCapProviderLicVersion = _CucsLicenseFeatureCapProviderLicVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 10),
    _CucsLicenseFeatureCapProviderLicVersion_Type()
)
cucsLicenseFeatureCapProviderLicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderLicVersion.setStatus("current")
_CucsLicenseFeatureCapProviderMgmtPlaneVer_Type = SnmpAdminString
_CucsLicenseFeatureCapProviderMgmtPlaneVer_Object = MibTableColumn
cucsLicenseFeatureCapProviderMgmtPlaneVer = _CucsLicenseFeatureCapProviderMgmtPlaneVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 11),
    _CucsLicenseFeatureCapProviderMgmtPlaneVer_Type()
)
cucsLicenseFeatureCapProviderMgmtPlaneVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderMgmtPlaneVer.setStatus("current")
_CucsLicenseFeatureCapProviderModel_Type = SnmpAdminString
_CucsLicenseFeatureCapProviderModel_Object = MibTableColumn
cucsLicenseFeatureCapProviderModel = _CucsLicenseFeatureCapProviderModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 12),
    _CucsLicenseFeatureCapProviderModel_Type()
)
cucsLicenseFeatureCapProviderModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderModel.setStatus("current")
_CucsLicenseFeatureCapProviderRevision_Type = SnmpAdminString
_CucsLicenseFeatureCapProviderRevision_Object = MibTableColumn
cucsLicenseFeatureCapProviderRevision = _CucsLicenseFeatureCapProviderRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 13),
    _CucsLicenseFeatureCapProviderRevision_Type()
)
cucsLicenseFeatureCapProviderRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderRevision.setStatus("current")
_CucsLicenseFeatureCapProviderType_Type = CucsLicenseFeatureType
_CucsLicenseFeatureCapProviderType_Object = MibTableColumn
cucsLicenseFeatureCapProviderType = _CucsLicenseFeatureCapProviderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 14),
    _CucsLicenseFeatureCapProviderType_Type()
)
cucsLicenseFeatureCapProviderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderType.setStatus("current")
_CucsLicenseFeatureCapProviderVendor_Type = SnmpAdminString
_CucsLicenseFeatureCapProviderVendor_Object = MibTableColumn
cucsLicenseFeatureCapProviderVendor = _CucsLicenseFeatureCapProviderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 15),
    _CucsLicenseFeatureCapProviderVendor_Type()
)
cucsLicenseFeatureCapProviderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderVendor.setStatus("current")
_CucsLicenseFeatureCapProviderDeleted_Type = TruthValue
_CucsLicenseFeatureCapProviderDeleted_Object = MibTableColumn
cucsLicenseFeatureCapProviderDeleted = _CucsLicenseFeatureCapProviderDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 16),
    _CucsLicenseFeatureCapProviderDeleted_Type()
)
cucsLicenseFeatureCapProviderDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderDeleted.setStatus("current")
_CucsLicenseFeatureCapProviderSku_Type = SnmpAdminString
_CucsLicenseFeatureCapProviderSku_Object = MibTableColumn
cucsLicenseFeatureCapProviderSku = _CucsLicenseFeatureCapProviderSku_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 17),
    _CucsLicenseFeatureCapProviderSku_Type()
)
cucsLicenseFeatureCapProviderSku.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderSku.setStatus("current")
_CucsLicenseFeatureCapProviderElementLoadFailures_Type = Gauge32
_CucsLicenseFeatureCapProviderElementLoadFailures_Object = MibTableColumn
cucsLicenseFeatureCapProviderElementLoadFailures = _CucsLicenseFeatureCapProviderElementLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 18),
    _CucsLicenseFeatureCapProviderElementLoadFailures_Type()
)
cucsLicenseFeatureCapProviderElementLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderElementLoadFailures.setStatus("current")
_CucsLicenseFeatureCapProviderElementsLoaded_Type = Gauge32
_CucsLicenseFeatureCapProviderElementsLoaded_Object = MibTableColumn
cucsLicenseFeatureCapProviderElementsLoaded = _CucsLicenseFeatureCapProviderElementsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 19),
    _CucsLicenseFeatureCapProviderElementsLoaded_Type()
)
cucsLicenseFeatureCapProviderElementsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderElementsLoaded.setStatus("current")
_CucsLicenseFeatureCapProviderLoadErrors_Type = Gauge32
_CucsLicenseFeatureCapProviderLoadErrors_Object = MibTableColumn
cucsLicenseFeatureCapProviderLoadErrors = _CucsLicenseFeatureCapProviderLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 20),
    _CucsLicenseFeatureCapProviderLoadErrors_Type()
)
cucsLicenseFeatureCapProviderLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderLoadErrors.setStatus("current")
_CucsLicenseFeatureCapProviderLoadWarnings_Type = Gauge32
_CucsLicenseFeatureCapProviderLoadWarnings_Object = MibTableColumn
cucsLicenseFeatureCapProviderLoadWarnings = _CucsLicenseFeatureCapProviderLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 6, 1, 21),
    _CucsLicenseFeatureCapProviderLoadWarnings_Type()
)
cucsLicenseFeatureCapProviderLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureCapProviderLoadWarnings.setStatus("current")
_CucsLicenseFeatureLineTable_Object = MibTable
cucsLicenseFeatureLineTable = _CucsLicenseFeatureLineTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 7)
)
if mibBuilder.loadTexts:
    cucsLicenseFeatureLineTable.setStatus("current")
_CucsLicenseFeatureLineEntry_Object = MibTableRow
cucsLicenseFeatureLineEntry = _CucsLicenseFeatureLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 7, 1)
)
cucsLicenseFeatureLineEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseFeatureLineInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseFeatureLineEntry.setStatus("current")
_CucsLicenseFeatureLineInstanceId_Type = CucsManagedObjectId
_CucsLicenseFeatureLineInstanceId_Object = MibTableColumn
cucsLicenseFeatureLineInstanceId = _CucsLicenseFeatureLineInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 7, 1, 1),
    _CucsLicenseFeatureLineInstanceId_Type()
)
cucsLicenseFeatureLineInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseFeatureLineInstanceId.setStatus("current")
_CucsLicenseFeatureLineDn_Type = CucsManagedObjectDn
_CucsLicenseFeatureLineDn_Object = MibTableColumn
cucsLicenseFeatureLineDn = _CucsLicenseFeatureLineDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 7, 1, 2),
    _CucsLicenseFeatureLineDn_Type()
)
cucsLicenseFeatureLineDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureLineDn.setStatus("current")
_CucsLicenseFeatureLineRn_Type = SnmpAdminString
_CucsLicenseFeatureLineRn_Object = MibTableColumn
cucsLicenseFeatureLineRn = _CucsLicenseFeatureLineRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 7, 1, 3),
    _CucsLicenseFeatureLineRn_Type()
)
cucsLicenseFeatureLineRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureLineRn.setStatus("current")
_CucsLicenseFeatureLineExp_Type = DateAndTime
_CucsLicenseFeatureLineExp_Object = MibTableColumn
cucsLicenseFeatureLineExp = _CucsLicenseFeatureLineExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 7, 1, 4),
    _CucsLicenseFeatureLineExp_Type()
)
cucsLicenseFeatureLineExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureLineExp.setStatus("current")
_CucsLicenseFeatureLineId_Type = SnmpAdminString
_CucsLicenseFeatureLineId_Object = MibTableColumn
cucsLicenseFeatureLineId = _CucsLicenseFeatureLineId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 7, 1, 5),
    _CucsLicenseFeatureLineId_Type()
)
cucsLicenseFeatureLineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureLineId.setStatus("current")
_CucsLicenseFeatureLinePak_Type = SnmpAdminString
_CucsLicenseFeatureLinePak_Object = MibTableColumn
cucsLicenseFeatureLinePak = _CucsLicenseFeatureLinePak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 7, 1, 6),
    _CucsLicenseFeatureLinePak_Type()
)
cucsLicenseFeatureLinePak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureLinePak.setStatus("current")
_CucsLicenseFeatureLineQuant_Type = Gauge32
_CucsLicenseFeatureLineQuant_Object = MibTableColumn
cucsLicenseFeatureLineQuant = _CucsLicenseFeatureLineQuant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 7, 1, 7),
    _CucsLicenseFeatureLineQuant_Type()
)
cucsLicenseFeatureLineQuant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureLineQuant.setStatus("current")
_CucsLicenseFeatureLineSig_Type = SnmpAdminString
_CucsLicenseFeatureLineSig_Object = MibTableColumn
cucsLicenseFeatureLineSig = _CucsLicenseFeatureLineSig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 7, 1, 8),
    _CucsLicenseFeatureLineSig_Type()
)
cucsLicenseFeatureLineSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureLineSig.setStatus("current")
_CucsLicenseFeatureLineType_Type = CucsLicenseType
_CucsLicenseFeatureLineType_Object = MibTableColumn
cucsLicenseFeatureLineType = _CucsLicenseFeatureLineType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 7, 1, 9),
    _CucsLicenseFeatureLineType_Type()
)
cucsLicenseFeatureLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureLineType.setStatus("current")
_CucsLicenseFeatureLineSku_Type = SnmpAdminString
_CucsLicenseFeatureLineSku_Object = MibTableColumn
cucsLicenseFeatureLineSku = _CucsLicenseFeatureLineSku_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 7, 1, 10),
    _CucsLicenseFeatureLineSku_Type()
)
cucsLicenseFeatureLineSku.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFeatureLineSku.setStatus("current")
_CucsLicenseFileTable_Object = MibTable
cucsLicenseFileTable = _CucsLicenseFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8)
)
if mibBuilder.loadTexts:
    cucsLicenseFileTable.setStatus("current")
_CucsLicenseFileEntry_Object = MibTableRow
cucsLicenseFileEntry = _CucsLicenseFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1)
)
cucsLicenseFileEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseFileInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseFileEntry.setStatus("current")
_CucsLicenseFileInstanceId_Type = CucsManagedObjectId
_CucsLicenseFileInstanceId_Object = MibTableColumn
cucsLicenseFileInstanceId = _CucsLicenseFileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 1),
    _CucsLicenseFileInstanceId_Type()
)
cucsLicenseFileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseFileInstanceId.setStatus("current")
_CucsLicenseFileDn_Type = CucsManagedObjectDn
_CucsLicenseFileDn_Object = MibTableColumn
cucsLicenseFileDn = _CucsLicenseFileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 2),
    _CucsLicenseFileDn_Type()
)
cucsLicenseFileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileDn.setStatus("current")
_CucsLicenseFileRn_Type = SnmpAdminString
_CucsLicenseFileRn_Object = MibTableColumn
cucsLicenseFileRn = _CucsLicenseFileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 3),
    _CucsLicenseFileRn_Type()
)
cucsLicenseFileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileRn.setStatus("current")
_CucsLicenseFileAdminState_Type = CucsLicenseFileState
_CucsLicenseFileAdminState_Object = MibTableColumn
cucsLicenseFileAdminState = _CucsLicenseFileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 4),
    _CucsLicenseFileAdminState_Type()
)
cucsLicenseFileAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileAdminState.setStatus("current")
_CucsLicenseFileFsmDescr_Type = SnmpAdminString
_CucsLicenseFileFsmDescr_Object = MibTableColumn
cucsLicenseFileFsmDescr = _CucsLicenseFileFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 5),
    _CucsLicenseFileFsmDescr_Type()
)
cucsLicenseFileFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmDescr.setStatus("current")
_CucsLicenseFileFsmPrev_Type = SnmpAdminString
_CucsLicenseFileFsmPrev_Object = MibTableColumn
cucsLicenseFileFsmPrev = _CucsLicenseFileFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 6),
    _CucsLicenseFileFsmPrev_Type()
)
cucsLicenseFileFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmPrev.setStatus("current")
_CucsLicenseFileFsmProgr_Type = Gauge32
_CucsLicenseFileFsmProgr_Object = MibTableColumn
cucsLicenseFileFsmProgr = _CucsLicenseFileFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 7),
    _CucsLicenseFileFsmProgr_Type()
)
cucsLicenseFileFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmProgr.setStatus("current")
_CucsLicenseFileFsmRmtInvErrCode_Type = Gauge32
_CucsLicenseFileFsmRmtInvErrCode_Object = MibTableColumn
cucsLicenseFileFsmRmtInvErrCode = _CucsLicenseFileFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 8),
    _CucsLicenseFileFsmRmtInvErrCode_Type()
)
cucsLicenseFileFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmRmtInvErrCode.setStatus("current")
_CucsLicenseFileFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsLicenseFileFsmRmtInvErrDescr_Object = MibTableColumn
cucsLicenseFileFsmRmtInvErrDescr = _CucsLicenseFileFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 9),
    _CucsLicenseFileFsmRmtInvErrDescr_Type()
)
cucsLicenseFileFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmRmtInvErrDescr.setStatus("current")
_CucsLicenseFileFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsLicenseFileFsmRmtInvRslt_Object = MibTableColumn
cucsLicenseFileFsmRmtInvRslt = _CucsLicenseFileFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 10),
    _CucsLicenseFileFsmRmtInvRslt_Type()
)
cucsLicenseFileFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmRmtInvRslt.setStatus("current")
_CucsLicenseFileFsmStageDescr_Type = SnmpAdminString
_CucsLicenseFileFsmStageDescr_Object = MibTableColumn
cucsLicenseFileFsmStageDescr = _CucsLicenseFileFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 11),
    _CucsLicenseFileFsmStageDescr_Type()
)
cucsLicenseFileFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStageDescr.setStatus("current")
_CucsLicenseFileFsmStamp_Type = DateAndTime
_CucsLicenseFileFsmStamp_Object = MibTableColumn
cucsLicenseFileFsmStamp = _CucsLicenseFileFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 12),
    _CucsLicenseFileFsmStamp_Type()
)
cucsLicenseFileFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStamp.setStatus("current")
_CucsLicenseFileFsmStatus_Type = SnmpAdminString
_CucsLicenseFileFsmStatus_Object = MibTableColumn
cucsLicenseFileFsmStatus = _CucsLicenseFileFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 13),
    _CucsLicenseFileFsmStatus_Type()
)
cucsLicenseFileFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStatus.setStatus("current")
_CucsLicenseFileFsmTry_Type = Gauge32
_CucsLicenseFileFsmTry_Object = MibTableColumn
cucsLicenseFileFsmTry = _CucsLicenseFileFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 14),
    _CucsLicenseFileFsmTry_Type()
)
cucsLicenseFileFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmTry.setStatus("current")
_CucsLicenseFileId_Type = SnmpAdminString
_CucsLicenseFileId_Object = MibTableColumn
cucsLicenseFileId = _CucsLicenseFileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 15),
    _CucsLicenseFileId_Type()
)
cucsLicenseFileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileId.setStatus("current")
_CucsLicenseFileName_Type = SnmpAdminString
_CucsLicenseFileName_Object = MibTableColumn
cucsLicenseFileName = _CucsLicenseFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 16),
    _CucsLicenseFileName_Type()
)
cucsLicenseFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileName.setStatus("current")
_CucsLicenseFileOperState_Type = CucsLicenseFileState
_CucsLicenseFileOperState_Object = MibTableColumn
cucsLicenseFileOperState = _CucsLicenseFileOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 17),
    _CucsLicenseFileOperState_Type()
)
cucsLicenseFileOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileOperState.setStatus("current")
_CucsLicenseFileOperStateDescr_Type = SnmpAdminString
_CucsLicenseFileOperStateDescr_Object = MibTableColumn
cucsLicenseFileOperStateDescr = _CucsLicenseFileOperStateDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 18),
    _CucsLicenseFileOperStateDescr_Type()
)
cucsLicenseFileOperStateDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileOperStateDescr.setStatus("current")
_CucsLicenseFileScope_Type = CucsLicenseScope
_CucsLicenseFileScope_Object = MibTableColumn
cucsLicenseFileScope = _CucsLicenseFileScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 19),
    _CucsLicenseFileScope_Type()
)
cucsLicenseFileScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileScope.setStatus("current")
_CucsLicenseFileVersion_Type = SnmpAdminString
_CucsLicenseFileVersion_Object = MibTableColumn
cucsLicenseFileVersion = _CucsLicenseFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 8, 1, 20),
    _CucsLicenseFileVersion_Type()
)
cucsLicenseFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileVersion.setStatus("current")
_CucsLicenseFileFsmTaskTable_Object = MibTable
cucsLicenseFileFsmTaskTable = _CucsLicenseFileFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 9)
)
if mibBuilder.loadTexts:
    cucsLicenseFileFsmTaskTable.setStatus("current")
_CucsLicenseFileFsmTaskEntry_Object = MibTableRow
cucsLicenseFileFsmTaskEntry = _CucsLicenseFileFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 9, 1)
)
cucsLicenseFileFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseFileFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseFileFsmTaskEntry.setStatus("current")
_CucsLicenseFileFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsLicenseFileFsmTaskInstanceId_Object = MibTableColumn
cucsLicenseFileFsmTaskInstanceId = _CucsLicenseFileFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 9, 1, 1),
    _CucsLicenseFileFsmTaskInstanceId_Type()
)
cucsLicenseFileFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmTaskInstanceId.setStatus("current")
_CucsLicenseFileFsmTaskDn_Type = CucsManagedObjectDn
_CucsLicenseFileFsmTaskDn_Object = MibTableColumn
cucsLicenseFileFsmTaskDn = _CucsLicenseFileFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 9, 1, 2),
    _CucsLicenseFileFsmTaskDn_Type()
)
cucsLicenseFileFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmTaskDn.setStatus("current")
_CucsLicenseFileFsmTaskRn_Type = SnmpAdminString
_CucsLicenseFileFsmTaskRn_Object = MibTableColumn
cucsLicenseFileFsmTaskRn = _CucsLicenseFileFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 9, 1, 3),
    _CucsLicenseFileFsmTaskRn_Type()
)
cucsLicenseFileFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmTaskRn.setStatus("current")
_CucsLicenseFileFsmTaskCompletion_Type = CucsFsmCompletion
_CucsLicenseFileFsmTaskCompletion_Object = MibTableColumn
cucsLicenseFileFsmTaskCompletion = _CucsLicenseFileFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 9, 1, 4),
    _CucsLicenseFileFsmTaskCompletion_Type()
)
cucsLicenseFileFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmTaskCompletion.setStatus("current")
_CucsLicenseFileFsmTaskFlags_Type = CucsFsmFlags
_CucsLicenseFileFsmTaskFlags_Object = MibTableColumn
cucsLicenseFileFsmTaskFlags = _CucsLicenseFileFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 9, 1, 5),
    _CucsLicenseFileFsmTaskFlags_Type()
)
cucsLicenseFileFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmTaskFlags.setStatus("current")
_CucsLicenseFileFsmTaskItem_Type = CucsLicenseFileFsmTaskItem
_CucsLicenseFileFsmTaskItem_Object = MibTableColumn
cucsLicenseFileFsmTaskItem = _CucsLicenseFileFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 9, 1, 6),
    _CucsLicenseFileFsmTaskItem_Type()
)
cucsLicenseFileFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmTaskItem.setStatus("current")
_CucsLicenseFileFsmTaskSeqId_Type = Gauge32
_CucsLicenseFileFsmTaskSeqId_Object = MibTableColumn
cucsLicenseFileFsmTaskSeqId = _CucsLicenseFileFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 9, 1, 7),
    _CucsLicenseFileFsmTaskSeqId_Type()
)
cucsLicenseFileFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmTaskSeqId.setStatus("current")
_CucsLicenseInstanceTable_Object = MibTable
cucsLicenseInstanceTable = _CucsLicenseInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10)
)
if mibBuilder.loadTexts:
    cucsLicenseInstanceTable.setStatus("current")
_CucsLicenseInstanceEntry_Object = MibTableRow
cucsLicenseInstanceEntry = _CucsLicenseInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1)
)
cucsLicenseInstanceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseInstanceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseInstanceEntry.setStatus("current")
_CucsLicenseInstanceInstanceId_Type = CucsManagedObjectId
_CucsLicenseInstanceInstanceId_Object = MibTableColumn
cucsLicenseInstanceInstanceId = _CucsLicenseInstanceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 1),
    _CucsLicenseInstanceInstanceId_Type()
)
cucsLicenseInstanceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseInstanceInstanceId.setStatus("current")
_CucsLicenseInstanceDn_Type = CucsManagedObjectDn
_CucsLicenseInstanceDn_Object = MibTableColumn
cucsLicenseInstanceDn = _CucsLicenseInstanceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 2),
    _CucsLicenseInstanceDn_Type()
)
cucsLicenseInstanceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceDn.setStatus("current")
_CucsLicenseInstanceRn_Type = SnmpAdminString
_CucsLicenseInstanceRn_Object = MibTableColumn
cucsLicenseInstanceRn = _CucsLicenseInstanceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 3),
    _CucsLicenseInstanceRn_Type()
)
cucsLicenseInstanceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceRn.setStatus("current")
_CucsLicenseInstanceAbsQuant_Type = Gauge32
_CucsLicenseInstanceAbsQuant_Object = MibTableColumn
cucsLicenseInstanceAbsQuant = _CucsLicenseInstanceAbsQuant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 4),
    _CucsLicenseInstanceAbsQuant_Type()
)
cucsLicenseInstanceAbsQuant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceAbsQuant.setStatus("current")
_CucsLicenseInstanceDefQuant_Type = Gauge32
_CucsLicenseInstanceDefQuant_Object = MibTableColumn
cucsLicenseInstanceDefQuant = _CucsLicenseInstanceDefQuant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 5),
    _CucsLicenseInstanceDefQuant_Type()
)
cucsLicenseInstanceDefQuant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceDefQuant.setStatus("current")
_CucsLicenseInstanceFeature_Type = SnmpAdminString
_CucsLicenseInstanceFeature_Object = MibTableColumn
cucsLicenseInstanceFeature = _CucsLicenseInstanceFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 6),
    _CucsLicenseInstanceFeature_Type()
)
cucsLicenseInstanceFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFeature.setStatus("current")
_CucsLicenseInstanceFsmDescr_Type = SnmpAdminString
_CucsLicenseInstanceFsmDescr_Object = MibTableColumn
cucsLicenseInstanceFsmDescr = _CucsLicenseInstanceFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 7),
    _CucsLicenseInstanceFsmDescr_Type()
)
cucsLicenseInstanceFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmDescr.setStatus("current")
_CucsLicenseInstanceFsmPrev_Type = SnmpAdminString
_CucsLicenseInstanceFsmPrev_Object = MibTableColumn
cucsLicenseInstanceFsmPrev = _CucsLicenseInstanceFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 8),
    _CucsLicenseInstanceFsmPrev_Type()
)
cucsLicenseInstanceFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmPrev.setStatus("current")
_CucsLicenseInstanceFsmProgr_Type = Gauge32
_CucsLicenseInstanceFsmProgr_Object = MibTableColumn
cucsLicenseInstanceFsmProgr = _CucsLicenseInstanceFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 9),
    _CucsLicenseInstanceFsmProgr_Type()
)
cucsLicenseInstanceFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmProgr.setStatus("current")
_CucsLicenseInstanceFsmRmtInvErrCode_Type = Gauge32
_CucsLicenseInstanceFsmRmtInvErrCode_Object = MibTableColumn
cucsLicenseInstanceFsmRmtInvErrCode = _CucsLicenseInstanceFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 10),
    _CucsLicenseInstanceFsmRmtInvErrCode_Type()
)
cucsLicenseInstanceFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmRmtInvErrCode.setStatus("current")
_CucsLicenseInstanceFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsLicenseInstanceFsmRmtInvErrDescr_Object = MibTableColumn
cucsLicenseInstanceFsmRmtInvErrDescr = _CucsLicenseInstanceFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 11),
    _CucsLicenseInstanceFsmRmtInvErrDescr_Type()
)
cucsLicenseInstanceFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmRmtInvErrDescr.setStatus("current")
_CucsLicenseInstanceFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsLicenseInstanceFsmRmtInvRslt_Object = MibTableColumn
cucsLicenseInstanceFsmRmtInvRslt = _CucsLicenseInstanceFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 12),
    _CucsLicenseInstanceFsmRmtInvRslt_Type()
)
cucsLicenseInstanceFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmRmtInvRslt.setStatus("current")
_CucsLicenseInstanceFsmStageDescr_Type = SnmpAdminString
_CucsLicenseInstanceFsmStageDescr_Object = MibTableColumn
cucsLicenseInstanceFsmStageDescr = _CucsLicenseInstanceFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 13),
    _CucsLicenseInstanceFsmStageDescr_Type()
)
cucsLicenseInstanceFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStageDescr.setStatus("current")
_CucsLicenseInstanceFsmStamp_Type = DateAndTime
_CucsLicenseInstanceFsmStamp_Object = MibTableColumn
cucsLicenseInstanceFsmStamp = _CucsLicenseInstanceFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 14),
    _CucsLicenseInstanceFsmStamp_Type()
)
cucsLicenseInstanceFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStamp.setStatus("current")
_CucsLicenseInstanceFsmStatus_Type = SnmpAdminString
_CucsLicenseInstanceFsmStatus_Object = MibTableColumn
cucsLicenseInstanceFsmStatus = _CucsLicenseInstanceFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 15),
    _CucsLicenseInstanceFsmStatus_Type()
)
cucsLicenseInstanceFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStatus.setStatus("current")
_CucsLicenseInstanceFsmTry_Type = Gauge32
_CucsLicenseInstanceFsmTry_Object = MibTableColumn
cucsLicenseInstanceFsmTry = _CucsLicenseInstanceFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 16),
    _CucsLicenseInstanceFsmTry_Type()
)
cucsLicenseInstanceFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmTry.setStatus("current")
_CucsLicenseInstanceGracePeriodUsed_Type = Unsigned64
_CucsLicenseInstanceGracePeriodUsed_Object = MibTableColumn
cucsLicenseInstanceGracePeriodUsed = _CucsLicenseInstanceGracePeriodUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 17),
    _CucsLicenseInstanceGracePeriodUsed_Type()
)
cucsLicenseInstanceGracePeriodUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceGracePeriodUsed.setStatus("current")
_CucsLicenseInstanceOperState_Type = CucsLicenseState
_CucsLicenseInstanceOperState_Object = MibTableColumn
cucsLicenseInstanceOperState = _CucsLicenseInstanceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 18),
    _CucsLicenseInstanceOperState_Type()
)
cucsLicenseInstanceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceOperState.setStatus("current")
_CucsLicenseInstancePeerStatus_Type = CucsLicensePeerStatus
_CucsLicenseInstancePeerStatus_Object = MibTableColumn
cucsLicenseInstancePeerStatus = _CucsLicenseInstancePeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 19),
    _CucsLicenseInstancePeerStatus_Type()
)
cucsLicenseInstancePeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstancePeerStatus.setStatus("current")
_CucsLicenseInstanceScope_Type = CucsLicenseScope
_CucsLicenseInstanceScope_Object = MibTableColumn
cucsLicenseInstanceScope = _CucsLicenseInstanceScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 20),
    _CucsLicenseInstanceScope_Type()
)
cucsLicenseInstanceScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceScope.setStatus("current")
_CucsLicenseInstanceUsedQuant_Type = Gauge32
_CucsLicenseInstanceUsedQuant_Object = MibTableColumn
cucsLicenseInstanceUsedQuant = _CucsLicenseInstanceUsedQuant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 21),
    _CucsLicenseInstanceUsedQuant_Type()
)
cucsLicenseInstanceUsedQuant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceUsedQuant.setStatus("current")
_CucsLicenseInstanceIsPresent_Type = TruthValue
_CucsLicenseInstanceIsPresent_Object = MibTableColumn
cucsLicenseInstanceIsPresent = _CucsLicenseInstanceIsPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 22),
    _CucsLicenseInstanceIsPresent_Type()
)
cucsLicenseInstanceIsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceIsPresent.setStatus("current")
_CucsLicenseInstanceSku_Type = SnmpAdminString
_CucsLicenseInstanceSku_Object = MibTableColumn
cucsLicenseInstanceSku = _CucsLicenseInstanceSku_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 23),
    _CucsLicenseInstanceSku_Type()
)
cucsLicenseInstanceSku.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceSku.setStatus("current")
_CucsLicenseInstanceSubordinateUsedQuant_Type = Gauge32
_CucsLicenseInstanceSubordinateUsedQuant_Object = MibTableColumn
cucsLicenseInstanceSubordinateUsedQuant = _CucsLicenseInstanceSubordinateUsedQuant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 10, 1, 24),
    _CucsLicenseInstanceSubordinateUsedQuant_Type()
)
cucsLicenseInstanceSubordinateUsedQuant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceSubordinateUsedQuant.setStatus("current")
_CucsLicenseInstanceFsmTaskTable_Object = MibTable
cucsLicenseInstanceFsmTaskTable = _CucsLicenseInstanceFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 11)
)
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmTaskTable.setStatus("current")
_CucsLicenseInstanceFsmTaskEntry_Object = MibTableRow
cucsLicenseInstanceFsmTaskEntry = _CucsLicenseInstanceFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 11, 1)
)
cucsLicenseInstanceFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseInstanceFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmTaskEntry.setStatus("current")
_CucsLicenseInstanceFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsLicenseInstanceFsmTaskInstanceId_Object = MibTableColumn
cucsLicenseInstanceFsmTaskInstanceId = _CucsLicenseInstanceFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 11, 1, 1),
    _CucsLicenseInstanceFsmTaskInstanceId_Type()
)
cucsLicenseInstanceFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmTaskInstanceId.setStatus("current")
_CucsLicenseInstanceFsmTaskDn_Type = CucsManagedObjectDn
_CucsLicenseInstanceFsmTaskDn_Object = MibTableColumn
cucsLicenseInstanceFsmTaskDn = _CucsLicenseInstanceFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 11, 1, 2),
    _CucsLicenseInstanceFsmTaskDn_Type()
)
cucsLicenseInstanceFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmTaskDn.setStatus("current")
_CucsLicenseInstanceFsmTaskRn_Type = SnmpAdminString
_CucsLicenseInstanceFsmTaskRn_Object = MibTableColumn
cucsLicenseInstanceFsmTaskRn = _CucsLicenseInstanceFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 11, 1, 3),
    _CucsLicenseInstanceFsmTaskRn_Type()
)
cucsLicenseInstanceFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmTaskRn.setStatus("current")
_CucsLicenseInstanceFsmTaskCompletion_Type = CucsFsmCompletion
_CucsLicenseInstanceFsmTaskCompletion_Object = MibTableColumn
cucsLicenseInstanceFsmTaskCompletion = _CucsLicenseInstanceFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 11, 1, 4),
    _CucsLicenseInstanceFsmTaskCompletion_Type()
)
cucsLicenseInstanceFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmTaskCompletion.setStatus("current")
_CucsLicenseInstanceFsmTaskFlags_Type = CucsFsmFlags
_CucsLicenseInstanceFsmTaskFlags_Object = MibTableColumn
cucsLicenseInstanceFsmTaskFlags = _CucsLicenseInstanceFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 11, 1, 5),
    _CucsLicenseInstanceFsmTaskFlags_Type()
)
cucsLicenseInstanceFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmTaskFlags.setStatus("current")
_CucsLicenseInstanceFsmTaskItem_Type = CucsLicenseInstanceFsmTaskItem
_CucsLicenseInstanceFsmTaskItem_Object = MibTableColumn
cucsLicenseInstanceFsmTaskItem = _CucsLicenseInstanceFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 11, 1, 6),
    _CucsLicenseInstanceFsmTaskItem_Type()
)
cucsLicenseInstanceFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmTaskItem.setStatus("current")
_CucsLicenseInstanceFsmTaskSeqId_Type = Gauge32
_CucsLicenseInstanceFsmTaskSeqId_Object = MibTableColumn
cucsLicenseInstanceFsmTaskSeqId = _CucsLicenseInstanceFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 11, 1, 7),
    _CucsLicenseInstanceFsmTaskSeqId_Type()
)
cucsLicenseInstanceFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmTaskSeqId.setStatus("current")
_CucsLicensePropTable_Object = MibTable
cucsLicensePropTable = _CucsLicensePropTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 12)
)
if mibBuilder.loadTexts:
    cucsLicensePropTable.setStatus("current")
_CucsLicensePropEntry_Object = MibTableRow
cucsLicensePropEntry = _CucsLicensePropEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 12, 1)
)
cucsLicensePropEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicensePropInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicensePropEntry.setStatus("current")
_CucsLicensePropInstanceId_Type = CucsManagedObjectId
_CucsLicensePropInstanceId_Object = MibTableColumn
cucsLicensePropInstanceId = _CucsLicensePropInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 12, 1, 1),
    _CucsLicensePropInstanceId_Type()
)
cucsLicensePropInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicensePropInstanceId.setStatus("current")
_CucsLicensePropDn_Type = CucsManagedObjectDn
_CucsLicensePropDn_Object = MibTableColumn
cucsLicensePropDn = _CucsLicensePropDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 12, 1, 2),
    _CucsLicensePropDn_Type()
)
cucsLicensePropDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicensePropDn.setStatus("current")
_CucsLicensePropRn_Type = SnmpAdminString
_CucsLicensePropRn_Object = MibTableColumn
cucsLicensePropRn = _CucsLicensePropRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 12, 1, 3),
    _CucsLicensePropRn_Type()
)
cucsLicensePropRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicensePropRn.setStatus("current")
_CucsLicensePropName_Type = SnmpAdminString
_CucsLicensePropName_Object = MibTableColumn
cucsLicensePropName = _CucsLicensePropName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 12, 1, 4),
    _CucsLicensePropName_Type()
)
cucsLicensePropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicensePropName.setStatus("current")
_CucsLicensePropValue_Type = SnmpAdminString
_CucsLicensePropValue_Object = MibTableColumn
cucsLicensePropValue = _CucsLicensePropValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 12, 1, 5),
    _CucsLicensePropValue_Type()
)
cucsLicensePropValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicensePropValue.setStatus("current")
_CucsLicenseServerHostIdTable_Object = MibTable
cucsLicenseServerHostIdTable = _CucsLicenseServerHostIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 13)
)
if mibBuilder.loadTexts:
    cucsLicenseServerHostIdTable.setStatus("current")
_CucsLicenseServerHostIdEntry_Object = MibTableRow
cucsLicenseServerHostIdEntry = _CucsLicenseServerHostIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 13, 1)
)
cucsLicenseServerHostIdEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseServerHostIdInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseServerHostIdEntry.setStatus("current")
_CucsLicenseServerHostIdInstanceId_Type = CucsManagedObjectId
_CucsLicenseServerHostIdInstanceId_Object = MibTableColumn
cucsLicenseServerHostIdInstanceId = _CucsLicenseServerHostIdInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 13, 1, 1),
    _CucsLicenseServerHostIdInstanceId_Type()
)
cucsLicenseServerHostIdInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseServerHostIdInstanceId.setStatus("current")
_CucsLicenseServerHostIdDn_Type = CucsManagedObjectDn
_CucsLicenseServerHostIdDn_Object = MibTableColumn
cucsLicenseServerHostIdDn = _CucsLicenseServerHostIdDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 13, 1, 2),
    _CucsLicenseServerHostIdDn_Type()
)
cucsLicenseServerHostIdDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseServerHostIdDn.setStatus("current")
_CucsLicenseServerHostIdRn_Type = SnmpAdminString
_CucsLicenseServerHostIdRn_Object = MibTableColumn
cucsLicenseServerHostIdRn = _CucsLicenseServerHostIdRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 13, 1, 3),
    _CucsLicenseServerHostIdRn_Type()
)
cucsLicenseServerHostIdRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseServerHostIdRn.setStatus("current")
_CucsLicenseServerHostIdHostId_Type = SnmpAdminString
_CucsLicenseServerHostIdHostId_Object = MibTableColumn
cucsLicenseServerHostIdHostId = _CucsLicenseServerHostIdHostId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 13, 1, 4),
    _CucsLicenseServerHostIdHostId_Type()
)
cucsLicenseServerHostIdHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseServerHostIdHostId.setStatus("current")
_CucsLicenseServerHostIdScope_Type = CucsLicenseScope
_CucsLicenseServerHostIdScope_Object = MibTableColumn
cucsLicenseServerHostIdScope = _CucsLicenseServerHostIdScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 13, 1, 5),
    _CucsLicenseServerHostIdScope_Type()
)
cucsLicenseServerHostIdScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseServerHostIdScope.setStatus("current")
_CucsLicenseSourceTable_Object = MibTable
cucsLicenseSourceTable = _CucsLicenseSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 14)
)
if mibBuilder.loadTexts:
    cucsLicenseSourceTable.setStatus("current")
_CucsLicenseSourceEntry_Object = MibTableRow
cucsLicenseSourceEntry = _CucsLicenseSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 14, 1)
)
cucsLicenseSourceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseSourceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseSourceEntry.setStatus("current")
_CucsLicenseSourceInstanceId_Type = CucsManagedObjectId
_CucsLicenseSourceInstanceId_Object = MibTableColumn
cucsLicenseSourceInstanceId = _CucsLicenseSourceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 14, 1, 1),
    _CucsLicenseSourceInstanceId_Type()
)
cucsLicenseSourceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseSourceInstanceId.setStatus("current")
_CucsLicenseSourceDn_Type = CucsManagedObjectDn
_CucsLicenseSourceDn_Object = MibTableColumn
cucsLicenseSourceDn = _CucsLicenseSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 14, 1, 2),
    _CucsLicenseSourceDn_Type()
)
cucsLicenseSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceDn.setStatus("current")
_CucsLicenseSourceRn_Type = SnmpAdminString
_CucsLicenseSourceRn_Object = MibTableColumn
cucsLicenseSourceRn = _CucsLicenseSourceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 14, 1, 3),
    _CucsLicenseSourceRn_Type()
)
cucsLicenseSourceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceRn.setStatus("current")
_CucsLicenseSourceAlwaysUse_Type = TruthValue
_CucsLicenseSourceAlwaysUse_Object = MibTableColumn
cucsLicenseSourceAlwaysUse = _CucsLicenseSourceAlwaysUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 14, 1, 4),
    _CucsLicenseSourceAlwaysUse_Type()
)
cucsLicenseSourceAlwaysUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceAlwaysUse.setStatus("current")
_CucsLicenseSourceHostId_Type = SnmpAdminString
_CucsLicenseSourceHostId_Object = MibTableColumn
cucsLicenseSourceHostId = _CucsLicenseSourceHostId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 14, 1, 5),
    _CucsLicenseSourceHostId_Type()
)
cucsLicenseSourceHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceHostId.setStatus("current")
_CucsLicenseSourceHostName_Type = SnmpAdminString
_CucsLicenseSourceHostName_Object = MibTableColumn
cucsLicenseSourceHostName = _CucsLicenseSourceHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 14, 1, 6),
    _CucsLicenseSourceHostName_Type()
)
cucsLicenseSourceHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceHostName.setStatus("current")
_CucsLicenseSourceVendorDaemonPath_Type = SnmpAdminString
_CucsLicenseSourceVendorDaemonPath_Object = MibTableColumn
cucsLicenseSourceVendorDaemonPath = _CucsLicenseSourceVendorDaemonPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 14, 1, 7),
    _CucsLicenseSourceVendorDaemonPath_Type()
)
cucsLicenseSourceVendorDaemonPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceVendorDaemonPath.setStatus("current")
_CucsLicenseSourceSku_Type = SnmpAdminString
_CucsLicenseSourceSku_Object = MibTableColumn
cucsLicenseSourceSku = _CucsLicenseSourceSku_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 14, 1, 8),
    _CucsLicenseSourceSku_Type()
)
cucsLicenseSourceSku.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceSku.setStatus("current")
_CucsLicenseSourceFileTable_Object = MibTable
cucsLicenseSourceFileTable = _CucsLicenseSourceFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15)
)
if mibBuilder.loadTexts:
    cucsLicenseSourceFileTable.setStatus("current")
_CucsLicenseSourceFileEntry_Object = MibTableRow
cucsLicenseSourceFileEntry = _CucsLicenseSourceFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15, 1)
)
cucsLicenseSourceFileEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseSourceFileInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseSourceFileEntry.setStatus("current")
_CucsLicenseSourceFileInstanceId_Type = CucsManagedObjectId
_CucsLicenseSourceFileInstanceId_Object = MibTableColumn
cucsLicenseSourceFileInstanceId = _CucsLicenseSourceFileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15, 1, 1),
    _CucsLicenseSourceFileInstanceId_Type()
)
cucsLicenseSourceFileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseSourceFileInstanceId.setStatus("current")
_CucsLicenseSourceFileDn_Type = CucsManagedObjectDn
_CucsLicenseSourceFileDn_Object = MibTableColumn
cucsLicenseSourceFileDn = _CucsLicenseSourceFileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15, 1, 2),
    _CucsLicenseSourceFileDn_Type()
)
cucsLicenseSourceFileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceFileDn.setStatus("current")
_CucsLicenseSourceFileRn_Type = SnmpAdminString
_CucsLicenseSourceFileRn_Object = MibTableColumn
cucsLicenseSourceFileRn = _CucsLicenseSourceFileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15, 1, 3),
    _CucsLicenseSourceFileRn_Type()
)
cucsLicenseSourceFileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceFileRn.setStatus("current")
_CucsLicenseSourceFileExp_Type = DateAndTime
_CucsLicenseSourceFileExp_Object = MibTableColumn
cucsLicenseSourceFileExp = _CucsLicenseSourceFileExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15, 1, 4),
    _CucsLicenseSourceFileExp_Type()
)
cucsLicenseSourceFileExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceFileExp.setStatus("current")
_CucsLicenseSourceFileHostId_Type = SnmpAdminString
_CucsLicenseSourceFileHostId_Object = MibTableColumn
cucsLicenseSourceFileHostId = _CucsLicenseSourceFileHostId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15, 1, 5),
    _CucsLicenseSourceFileHostId_Type()
)
cucsLicenseSourceFileHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceFileHostId.setStatus("current")
_CucsLicenseSourceFileId_Type = SnmpAdminString
_CucsLicenseSourceFileId_Object = MibTableColumn
cucsLicenseSourceFileId = _CucsLicenseSourceFileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15, 1, 6),
    _CucsLicenseSourceFileId_Type()
)
cucsLicenseSourceFileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceFileId.setStatus("current")
_CucsLicenseSourceFileLine_Type = SnmpAdminString
_CucsLicenseSourceFileLine_Object = MibTableColumn
cucsLicenseSourceFileLine = _CucsLicenseSourceFileLine_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15, 1, 7),
    _CucsLicenseSourceFileLine_Type()
)
cucsLicenseSourceFileLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceFileLine.setStatus("current")
_CucsLicenseSourceFilePak_Type = SnmpAdminString
_CucsLicenseSourceFilePak_Object = MibTableColumn
cucsLicenseSourceFilePak = _CucsLicenseSourceFilePak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15, 1, 8),
    _CucsLicenseSourceFilePak_Type()
)
cucsLicenseSourceFilePak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceFilePak.setStatus("current")
_CucsLicenseSourceFileQuant_Type = Gauge32
_CucsLicenseSourceFileQuant_Object = MibTableColumn
cucsLicenseSourceFileQuant = _CucsLicenseSourceFileQuant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15, 1, 9),
    _CucsLicenseSourceFileQuant_Type()
)
cucsLicenseSourceFileQuant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceFileQuant.setStatus("current")
_CucsLicenseSourceFileSig_Type = SnmpAdminString
_CucsLicenseSourceFileSig_Object = MibTableColumn
cucsLicenseSourceFileSig = _CucsLicenseSourceFileSig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15, 1, 10),
    _CucsLicenseSourceFileSig_Type()
)
cucsLicenseSourceFileSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceFileSig.setStatus("current")
_CucsLicenseSourceFileType_Type = CucsLicenseType
_CucsLicenseSourceFileType_Object = MibTableColumn
cucsLicenseSourceFileType = _CucsLicenseSourceFileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 15, 1, 11),
    _CucsLicenseSourceFileType_Type()
)
cucsLicenseSourceFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseSourceFileType.setStatus("current")
_CucsLicenseDownloaderFsmTable_Object = MibTable
cucsLicenseDownloaderFsmTable = _CucsLicenseDownloaderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16)
)
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmTable.setStatus("current")
_CucsLicenseDownloaderFsmEntry_Object = MibTableRow
cucsLicenseDownloaderFsmEntry = _CucsLicenseDownloaderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16, 1)
)
cucsLicenseDownloaderFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseDownloaderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmEntry.setStatus("current")
_CucsLicenseDownloaderFsmInstanceId_Type = CucsManagedObjectId
_CucsLicenseDownloaderFsmInstanceId_Object = MibTableColumn
cucsLicenseDownloaderFsmInstanceId = _CucsLicenseDownloaderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16, 1, 1),
    _CucsLicenseDownloaderFsmInstanceId_Type()
)
cucsLicenseDownloaderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmInstanceId.setStatus("current")
_CucsLicenseDownloaderFsmDn_Type = CucsManagedObjectDn
_CucsLicenseDownloaderFsmDn_Object = MibTableColumn
cucsLicenseDownloaderFsmDn = _CucsLicenseDownloaderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16, 1, 2),
    _CucsLicenseDownloaderFsmDn_Type()
)
cucsLicenseDownloaderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmDn.setStatus("current")
_CucsLicenseDownloaderFsmRn_Type = SnmpAdminString
_CucsLicenseDownloaderFsmRn_Object = MibTableColumn
cucsLicenseDownloaderFsmRn = _CucsLicenseDownloaderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16, 1, 3),
    _CucsLicenseDownloaderFsmRn_Type()
)
cucsLicenseDownloaderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmRn.setStatus("current")
_CucsLicenseDownloaderFsmCompletionTime_Type = DateAndTime
_CucsLicenseDownloaderFsmCompletionTime_Object = MibTableColumn
cucsLicenseDownloaderFsmCompletionTime = _CucsLicenseDownloaderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16, 1, 4),
    _CucsLicenseDownloaderFsmCompletionTime_Type()
)
cucsLicenseDownloaderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmCompletionTime.setStatus("current")
_CucsLicenseDownloaderFsmCurrentFsm_Type = CucsLicenseDownloaderFsmCurrentFsm
_CucsLicenseDownloaderFsmCurrentFsm_Object = MibTableColumn
cucsLicenseDownloaderFsmCurrentFsm = _CucsLicenseDownloaderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16, 1, 5),
    _CucsLicenseDownloaderFsmCurrentFsm_Type()
)
cucsLicenseDownloaderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmCurrentFsm.setStatus("current")
_CucsLicenseDownloaderFsmDescrData_Type = SnmpAdminString
_CucsLicenseDownloaderFsmDescrData_Object = MibTableColumn
cucsLicenseDownloaderFsmDescrData = _CucsLicenseDownloaderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16, 1, 6),
    _CucsLicenseDownloaderFsmDescrData_Type()
)
cucsLicenseDownloaderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmDescrData.setStatus("current")
_CucsLicenseDownloaderFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsLicenseDownloaderFsmFsmStatus_Object = MibTableColumn
cucsLicenseDownloaderFsmFsmStatus = _CucsLicenseDownloaderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16, 1, 7),
    _CucsLicenseDownloaderFsmFsmStatus_Type()
)
cucsLicenseDownloaderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmFsmStatus.setStatus("current")
_CucsLicenseDownloaderFsmProgress_Type = Gauge32
_CucsLicenseDownloaderFsmProgress_Object = MibTableColumn
cucsLicenseDownloaderFsmProgress = _CucsLicenseDownloaderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16, 1, 8),
    _CucsLicenseDownloaderFsmProgress_Type()
)
cucsLicenseDownloaderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmProgress.setStatus("current")
_CucsLicenseDownloaderFsmRmtErrCode_Type = Gauge32
_CucsLicenseDownloaderFsmRmtErrCode_Object = MibTableColumn
cucsLicenseDownloaderFsmRmtErrCode = _CucsLicenseDownloaderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16, 1, 9),
    _CucsLicenseDownloaderFsmRmtErrCode_Type()
)
cucsLicenseDownloaderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmRmtErrCode.setStatus("current")
_CucsLicenseDownloaderFsmRmtErrDescr_Type = SnmpAdminString
_CucsLicenseDownloaderFsmRmtErrDescr_Object = MibTableColumn
cucsLicenseDownloaderFsmRmtErrDescr = _CucsLicenseDownloaderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16, 1, 10),
    _CucsLicenseDownloaderFsmRmtErrDescr_Type()
)
cucsLicenseDownloaderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmRmtErrDescr.setStatus("current")
_CucsLicenseDownloaderFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsLicenseDownloaderFsmRmtRslt_Object = MibTableColumn
cucsLicenseDownloaderFsmRmtRslt = _CucsLicenseDownloaderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 16, 1, 11),
    _CucsLicenseDownloaderFsmRmtRslt_Type()
)
cucsLicenseDownloaderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmRmtRslt.setStatus("current")
_CucsLicenseDownloaderFsmStageTable_Object = MibTable
cucsLicenseDownloaderFsmStageTable = _CucsLicenseDownloaderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 17)
)
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStageTable.setStatus("current")
_CucsLicenseDownloaderFsmStageEntry_Object = MibTableRow
cucsLicenseDownloaderFsmStageEntry = _CucsLicenseDownloaderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 17, 1)
)
cucsLicenseDownloaderFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseDownloaderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStageEntry.setStatus("current")
_CucsLicenseDownloaderFsmStageInstanceId_Type = CucsManagedObjectId
_CucsLicenseDownloaderFsmStageInstanceId_Object = MibTableColumn
cucsLicenseDownloaderFsmStageInstanceId = _CucsLicenseDownloaderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 17, 1, 1),
    _CucsLicenseDownloaderFsmStageInstanceId_Type()
)
cucsLicenseDownloaderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStageInstanceId.setStatus("current")
_CucsLicenseDownloaderFsmStageDn_Type = CucsManagedObjectDn
_CucsLicenseDownloaderFsmStageDn_Object = MibTableColumn
cucsLicenseDownloaderFsmStageDn = _CucsLicenseDownloaderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 17, 1, 2),
    _CucsLicenseDownloaderFsmStageDn_Type()
)
cucsLicenseDownloaderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStageDn.setStatus("current")
_CucsLicenseDownloaderFsmStageRn_Type = SnmpAdminString
_CucsLicenseDownloaderFsmStageRn_Object = MibTableColumn
cucsLicenseDownloaderFsmStageRn = _CucsLicenseDownloaderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 17, 1, 3),
    _CucsLicenseDownloaderFsmStageRn_Type()
)
cucsLicenseDownloaderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStageRn.setStatus("current")
_CucsLicenseDownloaderFsmStageDescrData_Type = SnmpAdminString
_CucsLicenseDownloaderFsmStageDescrData_Object = MibTableColumn
cucsLicenseDownloaderFsmStageDescrData = _CucsLicenseDownloaderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 17, 1, 4),
    _CucsLicenseDownloaderFsmStageDescrData_Type()
)
cucsLicenseDownloaderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStageDescrData.setStatus("current")
_CucsLicenseDownloaderFsmStageLastUpdateTime_Type = DateAndTime
_CucsLicenseDownloaderFsmStageLastUpdateTime_Object = MibTableColumn
cucsLicenseDownloaderFsmStageLastUpdateTime = _CucsLicenseDownloaderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 17, 1, 5),
    _CucsLicenseDownloaderFsmStageLastUpdateTime_Type()
)
cucsLicenseDownloaderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStageLastUpdateTime.setStatus("current")
_CucsLicenseDownloaderFsmStageName_Type = CucsLicenseDownloaderFsmStageName
_CucsLicenseDownloaderFsmStageName_Object = MibTableColumn
cucsLicenseDownloaderFsmStageName = _CucsLicenseDownloaderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 17, 1, 6),
    _CucsLicenseDownloaderFsmStageName_Type()
)
cucsLicenseDownloaderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStageName.setStatus("current")
_CucsLicenseDownloaderFsmStageOrder_Type = Gauge32
_CucsLicenseDownloaderFsmStageOrder_Object = MibTableColumn
cucsLicenseDownloaderFsmStageOrder = _CucsLicenseDownloaderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 17, 1, 7),
    _CucsLicenseDownloaderFsmStageOrder_Type()
)
cucsLicenseDownloaderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStageOrder.setStatus("current")
_CucsLicenseDownloaderFsmStageRetry_Type = Gauge32
_CucsLicenseDownloaderFsmStageRetry_Object = MibTableColumn
cucsLicenseDownloaderFsmStageRetry = _CucsLicenseDownloaderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 17, 1, 8),
    _CucsLicenseDownloaderFsmStageRetry_Type()
)
cucsLicenseDownloaderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStageRetry.setStatus("current")
_CucsLicenseDownloaderFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsLicenseDownloaderFsmStageStageStatus_Object = MibTableColumn
cucsLicenseDownloaderFsmStageStageStatus = _CucsLicenseDownloaderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 17, 1, 9),
    _CucsLicenseDownloaderFsmStageStageStatus_Type()
)
cucsLicenseDownloaderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseDownloaderFsmStageStageStatus.setStatus("current")
_CucsLicenseFileFsmTable_Object = MibTable
cucsLicenseFileFsmTable = _CucsLicenseFileFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18)
)
if mibBuilder.loadTexts:
    cucsLicenseFileFsmTable.setStatus("current")
_CucsLicenseFileFsmEntry_Object = MibTableRow
cucsLicenseFileFsmEntry = _CucsLicenseFileFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18, 1)
)
cucsLicenseFileFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseFileFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseFileFsmEntry.setStatus("current")
_CucsLicenseFileFsmInstanceId_Type = CucsManagedObjectId
_CucsLicenseFileFsmInstanceId_Object = MibTableColumn
cucsLicenseFileFsmInstanceId = _CucsLicenseFileFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18, 1, 1),
    _CucsLicenseFileFsmInstanceId_Type()
)
cucsLicenseFileFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmInstanceId.setStatus("current")
_CucsLicenseFileFsmDn_Type = CucsManagedObjectDn
_CucsLicenseFileFsmDn_Object = MibTableColumn
cucsLicenseFileFsmDn = _CucsLicenseFileFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18, 1, 2),
    _CucsLicenseFileFsmDn_Type()
)
cucsLicenseFileFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmDn.setStatus("current")
_CucsLicenseFileFsmRn_Type = SnmpAdminString
_CucsLicenseFileFsmRn_Object = MibTableColumn
cucsLicenseFileFsmRn = _CucsLicenseFileFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18, 1, 3),
    _CucsLicenseFileFsmRn_Type()
)
cucsLicenseFileFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmRn.setStatus("current")
_CucsLicenseFileFsmCompletionTime_Type = DateAndTime
_CucsLicenseFileFsmCompletionTime_Object = MibTableColumn
cucsLicenseFileFsmCompletionTime = _CucsLicenseFileFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18, 1, 4),
    _CucsLicenseFileFsmCompletionTime_Type()
)
cucsLicenseFileFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmCompletionTime.setStatus("current")
_CucsLicenseFileFsmCurrentFsm_Type = CucsLicenseFileFsmCurrentFsm
_CucsLicenseFileFsmCurrentFsm_Object = MibTableColumn
cucsLicenseFileFsmCurrentFsm = _CucsLicenseFileFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18, 1, 5),
    _CucsLicenseFileFsmCurrentFsm_Type()
)
cucsLicenseFileFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmCurrentFsm.setStatus("current")
_CucsLicenseFileFsmDescrData_Type = SnmpAdminString
_CucsLicenseFileFsmDescrData_Object = MibTableColumn
cucsLicenseFileFsmDescrData = _CucsLicenseFileFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18, 1, 6),
    _CucsLicenseFileFsmDescrData_Type()
)
cucsLicenseFileFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmDescrData.setStatus("current")
_CucsLicenseFileFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsLicenseFileFsmFsmStatus_Object = MibTableColumn
cucsLicenseFileFsmFsmStatus = _CucsLicenseFileFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18, 1, 7),
    _CucsLicenseFileFsmFsmStatus_Type()
)
cucsLicenseFileFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmFsmStatus.setStatus("current")
_CucsLicenseFileFsmProgress_Type = Gauge32
_CucsLicenseFileFsmProgress_Object = MibTableColumn
cucsLicenseFileFsmProgress = _CucsLicenseFileFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18, 1, 8),
    _CucsLicenseFileFsmProgress_Type()
)
cucsLicenseFileFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmProgress.setStatus("current")
_CucsLicenseFileFsmRmtErrCode_Type = Gauge32
_CucsLicenseFileFsmRmtErrCode_Object = MibTableColumn
cucsLicenseFileFsmRmtErrCode = _CucsLicenseFileFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18, 1, 9),
    _CucsLicenseFileFsmRmtErrCode_Type()
)
cucsLicenseFileFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmRmtErrCode.setStatus("current")
_CucsLicenseFileFsmRmtErrDescr_Type = SnmpAdminString
_CucsLicenseFileFsmRmtErrDescr_Object = MibTableColumn
cucsLicenseFileFsmRmtErrDescr = _CucsLicenseFileFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18, 1, 10),
    _CucsLicenseFileFsmRmtErrDescr_Type()
)
cucsLicenseFileFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmRmtErrDescr.setStatus("current")
_CucsLicenseFileFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsLicenseFileFsmRmtRslt_Object = MibTableColumn
cucsLicenseFileFsmRmtRslt = _CucsLicenseFileFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 18, 1, 11),
    _CucsLicenseFileFsmRmtRslt_Type()
)
cucsLicenseFileFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmRmtRslt.setStatus("current")
_CucsLicenseFileFsmStageTable_Object = MibTable
cucsLicenseFileFsmStageTable = _CucsLicenseFileFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 19)
)
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStageTable.setStatus("current")
_CucsLicenseFileFsmStageEntry_Object = MibTableRow
cucsLicenseFileFsmStageEntry = _CucsLicenseFileFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 19, 1)
)
cucsLicenseFileFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseFileFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStageEntry.setStatus("current")
_CucsLicenseFileFsmStageInstanceId_Type = CucsManagedObjectId
_CucsLicenseFileFsmStageInstanceId_Object = MibTableColumn
cucsLicenseFileFsmStageInstanceId = _CucsLicenseFileFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 19, 1, 1),
    _CucsLicenseFileFsmStageInstanceId_Type()
)
cucsLicenseFileFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStageInstanceId.setStatus("current")
_CucsLicenseFileFsmStageDn_Type = CucsManagedObjectDn
_CucsLicenseFileFsmStageDn_Object = MibTableColumn
cucsLicenseFileFsmStageDn = _CucsLicenseFileFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 19, 1, 2),
    _CucsLicenseFileFsmStageDn_Type()
)
cucsLicenseFileFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStageDn.setStatus("current")
_CucsLicenseFileFsmStageRn_Type = SnmpAdminString
_CucsLicenseFileFsmStageRn_Object = MibTableColumn
cucsLicenseFileFsmStageRn = _CucsLicenseFileFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 19, 1, 3),
    _CucsLicenseFileFsmStageRn_Type()
)
cucsLicenseFileFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStageRn.setStatus("current")
_CucsLicenseFileFsmStageDescrData_Type = SnmpAdminString
_CucsLicenseFileFsmStageDescrData_Object = MibTableColumn
cucsLicenseFileFsmStageDescrData = _CucsLicenseFileFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 19, 1, 4),
    _CucsLicenseFileFsmStageDescrData_Type()
)
cucsLicenseFileFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStageDescrData.setStatus("current")
_CucsLicenseFileFsmStageLastUpdateTime_Type = DateAndTime
_CucsLicenseFileFsmStageLastUpdateTime_Object = MibTableColumn
cucsLicenseFileFsmStageLastUpdateTime = _CucsLicenseFileFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 19, 1, 5),
    _CucsLicenseFileFsmStageLastUpdateTime_Type()
)
cucsLicenseFileFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStageLastUpdateTime.setStatus("current")
_CucsLicenseFileFsmStageName_Type = CucsLicenseFileFsmStageName
_CucsLicenseFileFsmStageName_Object = MibTableColumn
cucsLicenseFileFsmStageName = _CucsLicenseFileFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 19, 1, 6),
    _CucsLicenseFileFsmStageName_Type()
)
cucsLicenseFileFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStageName.setStatus("current")
_CucsLicenseFileFsmStageOrder_Type = Gauge32
_CucsLicenseFileFsmStageOrder_Object = MibTableColumn
cucsLicenseFileFsmStageOrder = _CucsLicenseFileFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 19, 1, 7),
    _CucsLicenseFileFsmStageOrder_Type()
)
cucsLicenseFileFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStageOrder.setStatus("current")
_CucsLicenseFileFsmStageRetry_Type = Gauge32
_CucsLicenseFileFsmStageRetry_Object = MibTableColumn
cucsLicenseFileFsmStageRetry = _CucsLicenseFileFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 19, 1, 8),
    _CucsLicenseFileFsmStageRetry_Type()
)
cucsLicenseFileFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStageRetry.setStatus("current")
_CucsLicenseFileFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsLicenseFileFsmStageStageStatus_Object = MibTableColumn
cucsLicenseFileFsmStageStageStatus = _CucsLicenseFileFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 19, 1, 9),
    _CucsLicenseFileFsmStageStageStatus_Type()
)
cucsLicenseFileFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseFileFsmStageStageStatus.setStatus("current")
_CucsLicenseInstanceFsmTable_Object = MibTable
cucsLicenseInstanceFsmTable = _CucsLicenseInstanceFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20)
)
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmTable.setStatus("current")
_CucsLicenseInstanceFsmEntry_Object = MibTableRow
cucsLicenseInstanceFsmEntry = _CucsLicenseInstanceFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20, 1)
)
cucsLicenseInstanceFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseInstanceFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmEntry.setStatus("current")
_CucsLicenseInstanceFsmInstanceId_Type = CucsManagedObjectId
_CucsLicenseInstanceFsmInstanceId_Object = MibTableColumn
cucsLicenseInstanceFsmInstanceId = _CucsLicenseInstanceFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20, 1, 1),
    _CucsLicenseInstanceFsmInstanceId_Type()
)
cucsLicenseInstanceFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmInstanceId.setStatus("current")
_CucsLicenseInstanceFsmDn_Type = CucsManagedObjectDn
_CucsLicenseInstanceFsmDn_Object = MibTableColumn
cucsLicenseInstanceFsmDn = _CucsLicenseInstanceFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20, 1, 2),
    _CucsLicenseInstanceFsmDn_Type()
)
cucsLicenseInstanceFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmDn.setStatus("current")
_CucsLicenseInstanceFsmRn_Type = SnmpAdminString
_CucsLicenseInstanceFsmRn_Object = MibTableColumn
cucsLicenseInstanceFsmRn = _CucsLicenseInstanceFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20, 1, 3),
    _CucsLicenseInstanceFsmRn_Type()
)
cucsLicenseInstanceFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmRn.setStatus("current")
_CucsLicenseInstanceFsmCompletionTime_Type = DateAndTime
_CucsLicenseInstanceFsmCompletionTime_Object = MibTableColumn
cucsLicenseInstanceFsmCompletionTime = _CucsLicenseInstanceFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20, 1, 4),
    _CucsLicenseInstanceFsmCompletionTime_Type()
)
cucsLicenseInstanceFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmCompletionTime.setStatus("current")
_CucsLicenseInstanceFsmCurrentFsm_Type = CucsLicenseInstanceFsmCurrentFsm
_CucsLicenseInstanceFsmCurrentFsm_Object = MibTableColumn
cucsLicenseInstanceFsmCurrentFsm = _CucsLicenseInstanceFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20, 1, 5),
    _CucsLicenseInstanceFsmCurrentFsm_Type()
)
cucsLicenseInstanceFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmCurrentFsm.setStatus("current")
_CucsLicenseInstanceFsmDescrData_Type = SnmpAdminString
_CucsLicenseInstanceFsmDescrData_Object = MibTableColumn
cucsLicenseInstanceFsmDescrData = _CucsLicenseInstanceFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20, 1, 6),
    _CucsLicenseInstanceFsmDescrData_Type()
)
cucsLicenseInstanceFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmDescrData.setStatus("current")
_CucsLicenseInstanceFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsLicenseInstanceFsmFsmStatus_Object = MibTableColumn
cucsLicenseInstanceFsmFsmStatus = _CucsLicenseInstanceFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20, 1, 7),
    _CucsLicenseInstanceFsmFsmStatus_Type()
)
cucsLicenseInstanceFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmFsmStatus.setStatus("current")
_CucsLicenseInstanceFsmProgress_Type = Gauge32
_CucsLicenseInstanceFsmProgress_Object = MibTableColumn
cucsLicenseInstanceFsmProgress = _CucsLicenseInstanceFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20, 1, 8),
    _CucsLicenseInstanceFsmProgress_Type()
)
cucsLicenseInstanceFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmProgress.setStatus("current")
_CucsLicenseInstanceFsmRmtErrCode_Type = Gauge32
_CucsLicenseInstanceFsmRmtErrCode_Object = MibTableColumn
cucsLicenseInstanceFsmRmtErrCode = _CucsLicenseInstanceFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20, 1, 9),
    _CucsLicenseInstanceFsmRmtErrCode_Type()
)
cucsLicenseInstanceFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmRmtErrCode.setStatus("current")
_CucsLicenseInstanceFsmRmtErrDescr_Type = SnmpAdminString
_CucsLicenseInstanceFsmRmtErrDescr_Object = MibTableColumn
cucsLicenseInstanceFsmRmtErrDescr = _CucsLicenseInstanceFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20, 1, 10),
    _CucsLicenseInstanceFsmRmtErrDescr_Type()
)
cucsLicenseInstanceFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmRmtErrDescr.setStatus("current")
_CucsLicenseInstanceFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsLicenseInstanceFsmRmtRslt_Object = MibTableColumn
cucsLicenseInstanceFsmRmtRslt = _CucsLicenseInstanceFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 20, 1, 11),
    _CucsLicenseInstanceFsmRmtRslt_Type()
)
cucsLicenseInstanceFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmRmtRslt.setStatus("current")
_CucsLicenseInstanceFsmStageTable_Object = MibTable
cucsLicenseInstanceFsmStageTable = _CucsLicenseInstanceFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 21)
)
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStageTable.setStatus("current")
_CucsLicenseInstanceFsmStageEntry_Object = MibTableRow
cucsLicenseInstanceFsmStageEntry = _CucsLicenseInstanceFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 21, 1)
)
cucsLicenseInstanceFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseInstanceFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStageEntry.setStatus("current")
_CucsLicenseInstanceFsmStageInstanceId_Type = CucsManagedObjectId
_CucsLicenseInstanceFsmStageInstanceId_Object = MibTableColumn
cucsLicenseInstanceFsmStageInstanceId = _CucsLicenseInstanceFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 21, 1, 1),
    _CucsLicenseInstanceFsmStageInstanceId_Type()
)
cucsLicenseInstanceFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStageInstanceId.setStatus("current")
_CucsLicenseInstanceFsmStageDn_Type = CucsManagedObjectDn
_CucsLicenseInstanceFsmStageDn_Object = MibTableColumn
cucsLicenseInstanceFsmStageDn = _CucsLicenseInstanceFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 21, 1, 2),
    _CucsLicenseInstanceFsmStageDn_Type()
)
cucsLicenseInstanceFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStageDn.setStatus("current")
_CucsLicenseInstanceFsmStageRn_Type = SnmpAdminString
_CucsLicenseInstanceFsmStageRn_Object = MibTableColumn
cucsLicenseInstanceFsmStageRn = _CucsLicenseInstanceFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 21, 1, 3),
    _CucsLicenseInstanceFsmStageRn_Type()
)
cucsLicenseInstanceFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStageRn.setStatus("current")
_CucsLicenseInstanceFsmStageDescrData_Type = SnmpAdminString
_CucsLicenseInstanceFsmStageDescrData_Object = MibTableColumn
cucsLicenseInstanceFsmStageDescrData = _CucsLicenseInstanceFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 21, 1, 4),
    _CucsLicenseInstanceFsmStageDescrData_Type()
)
cucsLicenseInstanceFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStageDescrData.setStatus("current")
_CucsLicenseInstanceFsmStageLastUpdateTime_Type = DateAndTime
_CucsLicenseInstanceFsmStageLastUpdateTime_Object = MibTableColumn
cucsLicenseInstanceFsmStageLastUpdateTime = _CucsLicenseInstanceFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 21, 1, 5),
    _CucsLicenseInstanceFsmStageLastUpdateTime_Type()
)
cucsLicenseInstanceFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStageLastUpdateTime.setStatus("current")
_CucsLicenseInstanceFsmStageName_Type = CucsLicenseInstanceFsmStageName
_CucsLicenseInstanceFsmStageName_Object = MibTableColumn
cucsLicenseInstanceFsmStageName = _CucsLicenseInstanceFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 21, 1, 6),
    _CucsLicenseInstanceFsmStageName_Type()
)
cucsLicenseInstanceFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStageName.setStatus("current")
_CucsLicenseInstanceFsmStageOrder_Type = Gauge32
_CucsLicenseInstanceFsmStageOrder_Object = MibTableColumn
cucsLicenseInstanceFsmStageOrder = _CucsLicenseInstanceFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 21, 1, 7),
    _CucsLicenseInstanceFsmStageOrder_Type()
)
cucsLicenseInstanceFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStageOrder.setStatus("current")
_CucsLicenseInstanceFsmStageRetry_Type = Gauge32
_CucsLicenseInstanceFsmStageRetry_Object = MibTableColumn
cucsLicenseInstanceFsmStageRetry = _CucsLicenseInstanceFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 21, 1, 8),
    _CucsLicenseInstanceFsmStageRetry_Type()
)
cucsLicenseInstanceFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStageRetry.setStatus("current")
_CucsLicenseInstanceFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsLicenseInstanceFsmStageStageStatus_Object = MibTableColumn
cucsLicenseInstanceFsmStageStageStatus = _CucsLicenseInstanceFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 21, 1, 9),
    _CucsLicenseInstanceFsmStageStageStatus_Type()
)
cucsLicenseInstanceFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseInstanceFsmStageStageStatus.setStatus("current")
_CucsLicenseTargetTable_Object = MibTable
cucsLicenseTargetTable = _CucsLicenseTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 22)
)
if mibBuilder.loadTexts:
    cucsLicenseTargetTable.setStatus("current")
_CucsLicenseTargetEntry_Object = MibTableRow
cucsLicenseTargetEntry = _CucsLicenseTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 22, 1)
)
cucsLicenseTargetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-LICENSE-MIB", "cucsLicenseTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsLicenseTargetEntry.setStatus("current")
_CucsLicenseTargetInstanceId_Type = CucsManagedObjectId
_CucsLicenseTargetInstanceId_Object = MibTableColumn
cucsLicenseTargetInstanceId = _CucsLicenseTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 22, 1, 1),
    _CucsLicenseTargetInstanceId_Type()
)
cucsLicenseTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsLicenseTargetInstanceId.setStatus("current")
_CucsLicenseTargetDn_Type = CucsManagedObjectDn
_CucsLicenseTargetDn_Object = MibTableColumn
cucsLicenseTargetDn = _CucsLicenseTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 22, 1, 2),
    _CucsLicenseTargetDn_Type()
)
cucsLicenseTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseTargetDn.setStatus("current")
_CucsLicenseTargetRn_Type = SnmpAdminString
_CucsLicenseTargetRn_Object = MibTableColumn
cucsLicenseTargetRn = _CucsLicenseTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 22, 1, 3),
    _CucsLicenseTargetRn_Type()
)
cucsLicenseTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseTargetRn.setStatus("current")
_CucsLicenseTargetPortId_Type = Gauge32
_CucsLicenseTargetPortId_Object = MibTableColumn
cucsLicenseTargetPortId = _CucsLicenseTargetPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 22, 1, 4),
    _CucsLicenseTargetPortId_Type()
)
cucsLicenseTargetPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseTargetPortId.setStatus("current")
_CucsLicenseTargetSlotId_Type = Gauge32
_CucsLicenseTargetSlotId_Object = MibTableColumn
cucsLicenseTargetSlotId = _CucsLicenseTargetSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 22, 1, 5),
    _CucsLicenseTargetSlotId_Type()
)
cucsLicenseTargetSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseTargetSlotId.setStatus("current")
_CucsLicenseTargetIsRackPresent_Type = TruthValue
_CucsLicenseTargetIsRackPresent_Object = MibTableColumn
cucsLicenseTargetIsRackPresent = _CucsLicenseTargetIsRackPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 22, 1, 6),
    _CucsLicenseTargetIsRackPresent_Type()
)
cucsLicenseTargetIsRackPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseTargetIsRackPresent.setStatus("current")
_CucsLicenseTargetAggrPortId_Type = Gauge32
_CucsLicenseTargetAggrPortId_Object = MibTableColumn
cucsLicenseTargetAggrPortId = _CucsLicenseTargetAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 25, 22, 1, 7),
    _CucsLicenseTargetAggrPortId_Type()
)
cucsLicenseTargetAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsLicenseTargetAggrPortId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-LICENSE-MIB",
    **{"cucsLicenseObjects": cucsLicenseObjects,
       "cucsLicenseContentsTable": cucsLicenseContentsTable,
       "cucsLicenseContentsEntry": cucsLicenseContentsEntry,
       "cucsLicenseContentsInstanceId": cucsLicenseContentsInstanceId,
       "cucsLicenseContentsDn": cucsLicenseContentsDn,
       "cucsLicenseContentsRn": cucsLicenseContentsRn,
       "cucsLicenseContentsFeatureName": cucsLicenseContentsFeatureName,
       "cucsLicenseContentsTotalQuant": cucsLicenseContentsTotalQuant,
       "cucsLicenseContentsVendor": cucsLicenseContentsVendor,
       "cucsLicenseContentsVersion": cucsLicenseContentsVersion,
       "cucsLicenseDownloaderTable": cucsLicenseDownloaderTable,
       "cucsLicenseDownloaderEntry": cucsLicenseDownloaderEntry,
       "cucsLicenseDownloaderInstanceId": cucsLicenseDownloaderInstanceId,
       "cucsLicenseDownloaderDn": cucsLicenseDownloaderDn,
       "cucsLicenseDownloaderRn": cucsLicenseDownloaderRn,
       "cucsLicenseDownloaderAdminState": cucsLicenseDownloaderAdminState,
       "cucsLicenseDownloaderFileName": cucsLicenseDownloaderFileName,
       "cucsLicenseDownloaderFsmDescr": cucsLicenseDownloaderFsmDescr,
       "cucsLicenseDownloaderFsmPrev": cucsLicenseDownloaderFsmPrev,
       "cucsLicenseDownloaderFsmProgr": cucsLicenseDownloaderFsmProgr,
       "cucsLicenseDownloaderFsmRmtInvErrCode": cucsLicenseDownloaderFsmRmtInvErrCode,
       "cucsLicenseDownloaderFsmRmtInvErrDescr": cucsLicenseDownloaderFsmRmtInvErrDescr,
       "cucsLicenseDownloaderFsmRmtInvRslt": cucsLicenseDownloaderFsmRmtInvRslt,
       "cucsLicenseDownloaderFsmStageDescr": cucsLicenseDownloaderFsmStageDescr,
       "cucsLicenseDownloaderFsmStamp": cucsLicenseDownloaderFsmStamp,
       "cucsLicenseDownloaderFsmStatus": cucsLicenseDownloaderFsmStatus,
       "cucsLicenseDownloaderFsmTry": cucsLicenseDownloaderFsmTry,
       "cucsLicenseDownloaderProt": cucsLicenseDownloaderProt,
       "cucsLicenseDownloaderPwd": cucsLicenseDownloaderPwd,
       "cucsLicenseDownloaderRemotePath": cucsLicenseDownloaderRemotePath,
       "cucsLicenseDownloaderServer": cucsLicenseDownloaderServer,
       "cucsLicenseDownloaderTransferState": cucsLicenseDownloaderTransferState,
       "cucsLicenseDownloaderUser": cucsLicenseDownloaderUser,
       "cucsLicenseDownloaderFsmTaskTable": cucsLicenseDownloaderFsmTaskTable,
       "cucsLicenseDownloaderFsmTaskEntry": cucsLicenseDownloaderFsmTaskEntry,
       "cucsLicenseDownloaderFsmTaskInstanceId": cucsLicenseDownloaderFsmTaskInstanceId,
       "cucsLicenseDownloaderFsmTaskDn": cucsLicenseDownloaderFsmTaskDn,
       "cucsLicenseDownloaderFsmTaskRn": cucsLicenseDownloaderFsmTaskRn,
       "cucsLicenseDownloaderFsmTaskCompletion": cucsLicenseDownloaderFsmTaskCompletion,
       "cucsLicenseDownloaderFsmTaskFlags": cucsLicenseDownloaderFsmTaskFlags,
       "cucsLicenseDownloaderFsmTaskItem": cucsLicenseDownloaderFsmTaskItem,
       "cucsLicenseDownloaderFsmTaskSeqId": cucsLicenseDownloaderFsmTaskSeqId,
       "cucsLicenseEpTable": cucsLicenseEpTable,
       "cucsLicenseEpEntry": cucsLicenseEpEntry,
       "cucsLicenseEpInstanceId": cucsLicenseEpInstanceId,
       "cucsLicenseEpDn": cucsLicenseEpDn,
       "cucsLicenseEpRn": cucsLicenseEpRn,
       "cucsLicenseFeatureTable": cucsLicenseFeatureTable,
       "cucsLicenseFeatureEntry": cucsLicenseFeatureEntry,
       "cucsLicenseFeatureInstanceId": cucsLicenseFeatureInstanceId,
       "cucsLicenseFeatureDn": cucsLicenseFeatureDn,
       "cucsLicenseFeatureRn": cucsLicenseFeatureRn,
       "cucsLicenseFeatureDescr": cucsLicenseFeatureDescr,
       "cucsLicenseFeatureGracePeriod": cucsLicenseFeatureGracePeriod,
       "cucsLicenseFeatureIntId": cucsLicenseFeatureIntId,
       "cucsLicenseFeatureName": cucsLicenseFeatureName,
       "cucsLicenseFeatureType": cucsLicenseFeatureType,
       "cucsLicenseFeatureVendor": cucsLicenseFeatureVendor,
       "cucsLicenseFeatureVersion": cucsLicenseFeatureVersion,
       "cucsLicenseFeaturePolicyLevel": cucsLicenseFeaturePolicyLevel,
       "cucsLicenseFeaturePolicyOwner": cucsLicenseFeaturePolicyOwner,
       "cucsLicenseFeatureCapProviderTable": cucsLicenseFeatureCapProviderTable,
       "cucsLicenseFeatureCapProviderEntry": cucsLicenseFeatureCapProviderEntry,
       "cucsLicenseFeatureCapProviderInstanceId": cucsLicenseFeatureCapProviderInstanceId,
       "cucsLicenseFeatureCapProviderDn": cucsLicenseFeatureCapProviderDn,
       "cucsLicenseFeatureCapProviderRn": cucsLicenseFeatureCapProviderRn,
       "cucsLicenseFeatureCapProviderDefQuant": cucsLicenseFeatureCapProviderDefQuant,
       "cucsLicenseFeatureCapProviderDeprecated": cucsLicenseFeatureCapProviderDeprecated,
       "cucsLicenseFeatureCapProviderFeatureName": cucsLicenseFeatureCapProviderFeatureName,
       "cucsLicenseFeatureCapProviderGencount": cucsLicenseFeatureCapProviderGencount,
       "cucsLicenseFeatureCapProviderGracePeriod": cucsLicenseFeatureCapProviderGracePeriod,
       "cucsLicenseFeatureCapProviderLicVendor": cucsLicenseFeatureCapProviderLicVendor,
       "cucsLicenseFeatureCapProviderLicVersion": cucsLicenseFeatureCapProviderLicVersion,
       "cucsLicenseFeatureCapProviderMgmtPlaneVer": cucsLicenseFeatureCapProviderMgmtPlaneVer,
       "cucsLicenseFeatureCapProviderModel": cucsLicenseFeatureCapProviderModel,
       "cucsLicenseFeatureCapProviderRevision": cucsLicenseFeatureCapProviderRevision,
       "cucsLicenseFeatureCapProviderType": cucsLicenseFeatureCapProviderType,
       "cucsLicenseFeatureCapProviderVendor": cucsLicenseFeatureCapProviderVendor,
       "cucsLicenseFeatureCapProviderDeleted": cucsLicenseFeatureCapProviderDeleted,
       "cucsLicenseFeatureCapProviderSku": cucsLicenseFeatureCapProviderSku,
       "cucsLicenseFeatureCapProviderElementLoadFailures": cucsLicenseFeatureCapProviderElementLoadFailures,
       "cucsLicenseFeatureCapProviderElementsLoaded": cucsLicenseFeatureCapProviderElementsLoaded,
       "cucsLicenseFeatureCapProviderLoadErrors": cucsLicenseFeatureCapProviderLoadErrors,
       "cucsLicenseFeatureCapProviderLoadWarnings": cucsLicenseFeatureCapProviderLoadWarnings,
       "cucsLicenseFeatureLineTable": cucsLicenseFeatureLineTable,
       "cucsLicenseFeatureLineEntry": cucsLicenseFeatureLineEntry,
       "cucsLicenseFeatureLineInstanceId": cucsLicenseFeatureLineInstanceId,
       "cucsLicenseFeatureLineDn": cucsLicenseFeatureLineDn,
       "cucsLicenseFeatureLineRn": cucsLicenseFeatureLineRn,
       "cucsLicenseFeatureLineExp": cucsLicenseFeatureLineExp,
       "cucsLicenseFeatureLineId": cucsLicenseFeatureLineId,
       "cucsLicenseFeatureLinePak": cucsLicenseFeatureLinePak,
       "cucsLicenseFeatureLineQuant": cucsLicenseFeatureLineQuant,
       "cucsLicenseFeatureLineSig": cucsLicenseFeatureLineSig,
       "cucsLicenseFeatureLineType": cucsLicenseFeatureLineType,
       "cucsLicenseFeatureLineSku": cucsLicenseFeatureLineSku,
       "cucsLicenseFileTable": cucsLicenseFileTable,
       "cucsLicenseFileEntry": cucsLicenseFileEntry,
       "cucsLicenseFileInstanceId": cucsLicenseFileInstanceId,
       "cucsLicenseFileDn": cucsLicenseFileDn,
       "cucsLicenseFileRn": cucsLicenseFileRn,
       "cucsLicenseFileAdminState": cucsLicenseFileAdminState,
       "cucsLicenseFileFsmDescr": cucsLicenseFileFsmDescr,
       "cucsLicenseFileFsmPrev": cucsLicenseFileFsmPrev,
       "cucsLicenseFileFsmProgr": cucsLicenseFileFsmProgr,
       "cucsLicenseFileFsmRmtInvErrCode": cucsLicenseFileFsmRmtInvErrCode,
       "cucsLicenseFileFsmRmtInvErrDescr": cucsLicenseFileFsmRmtInvErrDescr,
       "cucsLicenseFileFsmRmtInvRslt": cucsLicenseFileFsmRmtInvRslt,
       "cucsLicenseFileFsmStageDescr": cucsLicenseFileFsmStageDescr,
       "cucsLicenseFileFsmStamp": cucsLicenseFileFsmStamp,
       "cucsLicenseFileFsmStatus": cucsLicenseFileFsmStatus,
       "cucsLicenseFileFsmTry": cucsLicenseFileFsmTry,
       "cucsLicenseFileId": cucsLicenseFileId,
       "cucsLicenseFileName": cucsLicenseFileName,
       "cucsLicenseFileOperState": cucsLicenseFileOperState,
       "cucsLicenseFileOperStateDescr": cucsLicenseFileOperStateDescr,
       "cucsLicenseFileScope": cucsLicenseFileScope,
       "cucsLicenseFileVersion": cucsLicenseFileVersion,
       "cucsLicenseFileFsmTaskTable": cucsLicenseFileFsmTaskTable,
       "cucsLicenseFileFsmTaskEntry": cucsLicenseFileFsmTaskEntry,
       "cucsLicenseFileFsmTaskInstanceId": cucsLicenseFileFsmTaskInstanceId,
       "cucsLicenseFileFsmTaskDn": cucsLicenseFileFsmTaskDn,
       "cucsLicenseFileFsmTaskRn": cucsLicenseFileFsmTaskRn,
       "cucsLicenseFileFsmTaskCompletion": cucsLicenseFileFsmTaskCompletion,
       "cucsLicenseFileFsmTaskFlags": cucsLicenseFileFsmTaskFlags,
       "cucsLicenseFileFsmTaskItem": cucsLicenseFileFsmTaskItem,
       "cucsLicenseFileFsmTaskSeqId": cucsLicenseFileFsmTaskSeqId,
       "cucsLicenseInstanceTable": cucsLicenseInstanceTable,
       "cucsLicenseInstanceEntry": cucsLicenseInstanceEntry,
       "cucsLicenseInstanceInstanceId": cucsLicenseInstanceInstanceId,
       "cucsLicenseInstanceDn": cucsLicenseInstanceDn,
       "cucsLicenseInstanceRn": cucsLicenseInstanceRn,
       "cucsLicenseInstanceAbsQuant": cucsLicenseInstanceAbsQuant,
       "cucsLicenseInstanceDefQuant": cucsLicenseInstanceDefQuant,
       "cucsLicenseInstanceFeature": cucsLicenseInstanceFeature,
       "cucsLicenseInstanceFsmDescr": cucsLicenseInstanceFsmDescr,
       "cucsLicenseInstanceFsmPrev": cucsLicenseInstanceFsmPrev,
       "cucsLicenseInstanceFsmProgr": cucsLicenseInstanceFsmProgr,
       "cucsLicenseInstanceFsmRmtInvErrCode": cucsLicenseInstanceFsmRmtInvErrCode,
       "cucsLicenseInstanceFsmRmtInvErrDescr": cucsLicenseInstanceFsmRmtInvErrDescr,
       "cucsLicenseInstanceFsmRmtInvRslt": cucsLicenseInstanceFsmRmtInvRslt,
       "cucsLicenseInstanceFsmStageDescr": cucsLicenseInstanceFsmStageDescr,
       "cucsLicenseInstanceFsmStamp": cucsLicenseInstanceFsmStamp,
       "cucsLicenseInstanceFsmStatus": cucsLicenseInstanceFsmStatus,
       "cucsLicenseInstanceFsmTry": cucsLicenseInstanceFsmTry,
       "cucsLicenseInstanceGracePeriodUsed": cucsLicenseInstanceGracePeriodUsed,
       "cucsLicenseInstanceOperState": cucsLicenseInstanceOperState,
       "cucsLicenseInstancePeerStatus": cucsLicenseInstancePeerStatus,
       "cucsLicenseInstanceScope": cucsLicenseInstanceScope,
       "cucsLicenseInstanceUsedQuant": cucsLicenseInstanceUsedQuant,
       "cucsLicenseInstanceIsPresent": cucsLicenseInstanceIsPresent,
       "cucsLicenseInstanceSku": cucsLicenseInstanceSku,
       "cucsLicenseInstanceSubordinateUsedQuant": cucsLicenseInstanceSubordinateUsedQuant,
       "cucsLicenseInstanceFsmTaskTable": cucsLicenseInstanceFsmTaskTable,
       "cucsLicenseInstanceFsmTaskEntry": cucsLicenseInstanceFsmTaskEntry,
       "cucsLicenseInstanceFsmTaskInstanceId": cucsLicenseInstanceFsmTaskInstanceId,
       "cucsLicenseInstanceFsmTaskDn": cucsLicenseInstanceFsmTaskDn,
       "cucsLicenseInstanceFsmTaskRn": cucsLicenseInstanceFsmTaskRn,
       "cucsLicenseInstanceFsmTaskCompletion": cucsLicenseInstanceFsmTaskCompletion,
       "cucsLicenseInstanceFsmTaskFlags": cucsLicenseInstanceFsmTaskFlags,
       "cucsLicenseInstanceFsmTaskItem": cucsLicenseInstanceFsmTaskItem,
       "cucsLicenseInstanceFsmTaskSeqId": cucsLicenseInstanceFsmTaskSeqId,
       "cucsLicensePropTable": cucsLicensePropTable,
       "cucsLicensePropEntry": cucsLicensePropEntry,
       "cucsLicensePropInstanceId": cucsLicensePropInstanceId,
       "cucsLicensePropDn": cucsLicensePropDn,
       "cucsLicensePropRn": cucsLicensePropRn,
       "cucsLicensePropName": cucsLicensePropName,
       "cucsLicensePropValue": cucsLicensePropValue,
       "cucsLicenseServerHostIdTable": cucsLicenseServerHostIdTable,
       "cucsLicenseServerHostIdEntry": cucsLicenseServerHostIdEntry,
       "cucsLicenseServerHostIdInstanceId": cucsLicenseServerHostIdInstanceId,
       "cucsLicenseServerHostIdDn": cucsLicenseServerHostIdDn,
       "cucsLicenseServerHostIdRn": cucsLicenseServerHostIdRn,
       "cucsLicenseServerHostIdHostId": cucsLicenseServerHostIdHostId,
       "cucsLicenseServerHostIdScope": cucsLicenseServerHostIdScope,
       "cucsLicenseSourceTable": cucsLicenseSourceTable,
       "cucsLicenseSourceEntry": cucsLicenseSourceEntry,
       "cucsLicenseSourceInstanceId": cucsLicenseSourceInstanceId,
       "cucsLicenseSourceDn": cucsLicenseSourceDn,
       "cucsLicenseSourceRn": cucsLicenseSourceRn,
       "cucsLicenseSourceAlwaysUse": cucsLicenseSourceAlwaysUse,
       "cucsLicenseSourceHostId": cucsLicenseSourceHostId,
       "cucsLicenseSourceHostName": cucsLicenseSourceHostName,
       "cucsLicenseSourceVendorDaemonPath": cucsLicenseSourceVendorDaemonPath,
       "cucsLicenseSourceSku": cucsLicenseSourceSku,
       "cucsLicenseSourceFileTable": cucsLicenseSourceFileTable,
       "cucsLicenseSourceFileEntry": cucsLicenseSourceFileEntry,
       "cucsLicenseSourceFileInstanceId": cucsLicenseSourceFileInstanceId,
       "cucsLicenseSourceFileDn": cucsLicenseSourceFileDn,
       "cucsLicenseSourceFileRn": cucsLicenseSourceFileRn,
       "cucsLicenseSourceFileExp": cucsLicenseSourceFileExp,
       "cucsLicenseSourceFileHostId": cucsLicenseSourceFileHostId,
       "cucsLicenseSourceFileId": cucsLicenseSourceFileId,
       "cucsLicenseSourceFileLine": cucsLicenseSourceFileLine,
       "cucsLicenseSourceFilePak": cucsLicenseSourceFilePak,
       "cucsLicenseSourceFileQuant": cucsLicenseSourceFileQuant,
       "cucsLicenseSourceFileSig": cucsLicenseSourceFileSig,
       "cucsLicenseSourceFileType": cucsLicenseSourceFileType,
       "cucsLicenseDownloaderFsmTable": cucsLicenseDownloaderFsmTable,
       "cucsLicenseDownloaderFsmEntry": cucsLicenseDownloaderFsmEntry,
       "cucsLicenseDownloaderFsmInstanceId": cucsLicenseDownloaderFsmInstanceId,
       "cucsLicenseDownloaderFsmDn": cucsLicenseDownloaderFsmDn,
       "cucsLicenseDownloaderFsmRn": cucsLicenseDownloaderFsmRn,
       "cucsLicenseDownloaderFsmCompletionTime": cucsLicenseDownloaderFsmCompletionTime,
       "cucsLicenseDownloaderFsmCurrentFsm": cucsLicenseDownloaderFsmCurrentFsm,
       "cucsLicenseDownloaderFsmDescrData": cucsLicenseDownloaderFsmDescrData,
       "cucsLicenseDownloaderFsmFsmStatus": cucsLicenseDownloaderFsmFsmStatus,
       "cucsLicenseDownloaderFsmProgress": cucsLicenseDownloaderFsmProgress,
       "cucsLicenseDownloaderFsmRmtErrCode": cucsLicenseDownloaderFsmRmtErrCode,
       "cucsLicenseDownloaderFsmRmtErrDescr": cucsLicenseDownloaderFsmRmtErrDescr,
       "cucsLicenseDownloaderFsmRmtRslt": cucsLicenseDownloaderFsmRmtRslt,
       "cucsLicenseDownloaderFsmStageTable": cucsLicenseDownloaderFsmStageTable,
       "cucsLicenseDownloaderFsmStageEntry": cucsLicenseDownloaderFsmStageEntry,
       "cucsLicenseDownloaderFsmStageInstanceId": cucsLicenseDownloaderFsmStageInstanceId,
       "cucsLicenseDownloaderFsmStageDn": cucsLicenseDownloaderFsmStageDn,
       "cucsLicenseDownloaderFsmStageRn": cucsLicenseDownloaderFsmStageRn,
       "cucsLicenseDownloaderFsmStageDescrData": cucsLicenseDownloaderFsmStageDescrData,
       "cucsLicenseDownloaderFsmStageLastUpdateTime": cucsLicenseDownloaderFsmStageLastUpdateTime,
       "cucsLicenseDownloaderFsmStageName": cucsLicenseDownloaderFsmStageName,
       "cucsLicenseDownloaderFsmStageOrder": cucsLicenseDownloaderFsmStageOrder,
       "cucsLicenseDownloaderFsmStageRetry": cucsLicenseDownloaderFsmStageRetry,
       "cucsLicenseDownloaderFsmStageStageStatus": cucsLicenseDownloaderFsmStageStageStatus,
       "cucsLicenseFileFsmTable": cucsLicenseFileFsmTable,
       "cucsLicenseFileFsmEntry": cucsLicenseFileFsmEntry,
       "cucsLicenseFileFsmInstanceId": cucsLicenseFileFsmInstanceId,
       "cucsLicenseFileFsmDn": cucsLicenseFileFsmDn,
       "cucsLicenseFileFsmRn": cucsLicenseFileFsmRn,
       "cucsLicenseFileFsmCompletionTime": cucsLicenseFileFsmCompletionTime,
       "cucsLicenseFileFsmCurrentFsm": cucsLicenseFileFsmCurrentFsm,
       "cucsLicenseFileFsmDescrData": cucsLicenseFileFsmDescrData,
       "cucsLicenseFileFsmFsmStatus": cucsLicenseFileFsmFsmStatus,
       "cucsLicenseFileFsmProgress": cucsLicenseFileFsmProgress,
       "cucsLicenseFileFsmRmtErrCode": cucsLicenseFileFsmRmtErrCode,
       "cucsLicenseFileFsmRmtErrDescr": cucsLicenseFileFsmRmtErrDescr,
       "cucsLicenseFileFsmRmtRslt": cucsLicenseFileFsmRmtRslt,
       "cucsLicenseFileFsmStageTable": cucsLicenseFileFsmStageTable,
       "cucsLicenseFileFsmStageEntry": cucsLicenseFileFsmStageEntry,
       "cucsLicenseFileFsmStageInstanceId": cucsLicenseFileFsmStageInstanceId,
       "cucsLicenseFileFsmStageDn": cucsLicenseFileFsmStageDn,
       "cucsLicenseFileFsmStageRn": cucsLicenseFileFsmStageRn,
       "cucsLicenseFileFsmStageDescrData": cucsLicenseFileFsmStageDescrData,
       "cucsLicenseFileFsmStageLastUpdateTime": cucsLicenseFileFsmStageLastUpdateTime,
       "cucsLicenseFileFsmStageName": cucsLicenseFileFsmStageName,
       "cucsLicenseFileFsmStageOrder": cucsLicenseFileFsmStageOrder,
       "cucsLicenseFileFsmStageRetry": cucsLicenseFileFsmStageRetry,
       "cucsLicenseFileFsmStageStageStatus": cucsLicenseFileFsmStageStageStatus,
       "cucsLicenseInstanceFsmTable": cucsLicenseInstanceFsmTable,
       "cucsLicenseInstanceFsmEntry": cucsLicenseInstanceFsmEntry,
       "cucsLicenseInstanceFsmInstanceId": cucsLicenseInstanceFsmInstanceId,
       "cucsLicenseInstanceFsmDn": cucsLicenseInstanceFsmDn,
       "cucsLicenseInstanceFsmRn": cucsLicenseInstanceFsmRn,
       "cucsLicenseInstanceFsmCompletionTime": cucsLicenseInstanceFsmCompletionTime,
       "cucsLicenseInstanceFsmCurrentFsm": cucsLicenseInstanceFsmCurrentFsm,
       "cucsLicenseInstanceFsmDescrData": cucsLicenseInstanceFsmDescrData,
       "cucsLicenseInstanceFsmFsmStatus": cucsLicenseInstanceFsmFsmStatus,
       "cucsLicenseInstanceFsmProgress": cucsLicenseInstanceFsmProgress,
       "cucsLicenseInstanceFsmRmtErrCode": cucsLicenseInstanceFsmRmtErrCode,
       "cucsLicenseInstanceFsmRmtErrDescr": cucsLicenseInstanceFsmRmtErrDescr,
       "cucsLicenseInstanceFsmRmtRslt": cucsLicenseInstanceFsmRmtRslt,
       "cucsLicenseInstanceFsmStageTable": cucsLicenseInstanceFsmStageTable,
       "cucsLicenseInstanceFsmStageEntry": cucsLicenseInstanceFsmStageEntry,
       "cucsLicenseInstanceFsmStageInstanceId": cucsLicenseInstanceFsmStageInstanceId,
       "cucsLicenseInstanceFsmStageDn": cucsLicenseInstanceFsmStageDn,
       "cucsLicenseInstanceFsmStageRn": cucsLicenseInstanceFsmStageRn,
       "cucsLicenseInstanceFsmStageDescrData": cucsLicenseInstanceFsmStageDescrData,
       "cucsLicenseInstanceFsmStageLastUpdateTime": cucsLicenseInstanceFsmStageLastUpdateTime,
       "cucsLicenseInstanceFsmStageName": cucsLicenseInstanceFsmStageName,
       "cucsLicenseInstanceFsmStageOrder": cucsLicenseInstanceFsmStageOrder,
       "cucsLicenseInstanceFsmStageRetry": cucsLicenseInstanceFsmStageRetry,
       "cucsLicenseInstanceFsmStageStageStatus": cucsLicenseInstanceFsmStageStageStatus,
       "cucsLicenseTargetTable": cucsLicenseTargetTable,
       "cucsLicenseTargetEntry": cucsLicenseTargetEntry,
       "cucsLicenseTargetInstanceId": cucsLicenseTargetInstanceId,
       "cucsLicenseTargetDn": cucsLicenseTargetDn,
       "cucsLicenseTargetRn": cucsLicenseTargetRn,
       "cucsLicenseTargetPortId": cucsLicenseTargetPortId,
       "cucsLicenseTargetSlotId": cucsLicenseTargetSlotId,
       "cucsLicenseTargetIsRackPresent": cucsLicenseTargetIsRackPresent,
       "cucsLicenseTargetAggrPortId": cucsLicenseTargetAggrPortId}
)
